Use database CSE544DatabaseOlga;
Use warehouse LOAD_WH;

create or replace file format OlgaD400_json type = json;

create or replace stage OlgaD400_semscholar url = 's3://ai2-s2-research-public/open-corpus/2020-02-01/' file_format = OlgaD400_json;

create or replace table raw_source (
  src variant);
  
copy into raw_source from @OlgaD400_semscholar On_Error = skip_file;

-- DATA WE ACTUALLY CARE ABOUT 
create or replace table important_data as 
select src:authors as authors, src:fieldsOfStudy as fieldsOfStudy, src:venue as venue, 
src:year as year, src:id as pubid, src:journalName as journalName, src:inCitations as inCitations, src:outCitations as outCitations from raw_source 
where src:inCitations != '[]' or src:outCitations != '[]';

__________________________________________________

-- Create author table containing name and id and make id the primary key
__________________________________________________

-- Create a temporary table of gross author json data and pubid
create table temporary_authors as 
select pubid, parse_json(authors) as auth from important_data;

--Create a temporary author table keeping track of pubid, author name, and author id
create table temporary_authors2 as 
select pubid::string as pubid,
   f.value:ids[0]::int as authid,
   f.value:name::string as name
 from temporary_authors as t,
   lateral flatten(input => t.auth) f;
   
--IMPORTANT: There are some entries without author information, some with names but no ids
--The names without ids are not listed in the authors table
--authored does not contain information about publications where the author id is not specified
   

create table Authors as
select authid, name from temporary_authors2 
group by authid, name;

alter table Authors add primary key (authid);

__________________________________________________

-- Create authored table relation containing author id and pubid table
__________________________________________________

create table Authored as
select authid, pubid from temporary_authors2
group by authid, pubid;

alter table Authored add primary key(authid, pubid)

drop table temporary_authors;
drop table temporary_authors2; 
__________________________________________________

-- Create incitation and outcitation relationships tables
__________________________________________________
create table temp_incitations as 
select pubid, parse_json(inCitations) as inCitations from important_data;

create or replace table inCitations as
select pubid::string as pubid, 
f.value::string as inCitations
from temp_incitations as t,
lateral flatten(input => t.inCitations, outer => true) f;

drop table temp_incitations;
alter table inCitations add primary key (pubid);

create table temp_outcitations as 
select pubid, parse_json(outCitations) as outCitations from important_data;

create or replace table outCitations as
select pubid::string as pubid, 
f.value::string as outCitations
from temp_outcitations as t,
lateral flatten(input => t.outCitations, outer => true) f;

drop table temp_outcitations;
alter table out_Citations add primary key (pubid);

--NOTE THE INCITATION TABLE WILL NOT CONTAIN INFO FOR PUBLICATIONS WITHOUT INCITATIONS LISTED
--NOTE THE OUTCITATION TABLE WILL NOT CONTAIN INFO FOR PUBLICATIONS WITHOUT OUTCITATIONS LISTED
--IMPORTANT BECAUSE: SOME PUBLICATIONS CONTAIN OUT OR IN CITATIONS BUT NOT BOTH
--I could change this but not sure if I should or not?

__________________________________________________

-- Create publication table
__________________________________________________

create table temp_pub as 
select pubid, year, venue, parse_json(fieldsOfStudy) as fieldsOfStudy from important_data;

create table Publication as
select pubid::string as pubid,
year::int as year,
venue::string as venue, 
f.value::string as fieldOfStudy
from temp_pub as t,
lateral flatten(input => t.fieldsOfStudy, outer => true) f;

drop table temp_pub;
alter table Publciation add primary key (pubid);

__________________________________________________

-- Create Journal table
__________________________________________________

create table tempJournal as
select distinct journalName::string as journalName from important_data where journalName != '';

create or replace table Journal(journalId int, journalName string);
drop sequence q;
create sequence q;
insert into Journal(select q.nextval as journalId, journalName::string as journalName from tempJournal);

drop table tempJournal;
alter table Journal add primary key (journalId);

__________________________________________________

-- Create PublishedIn Relation table
__________________________________________________
create table PublishedIn as
select pubid, journalId from important_data
left outer join journal using(journalName); 




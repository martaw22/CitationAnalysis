def FillInTable(citation_data,Publications,Authors,Journals,PublishedIn,InCitations,OutCitations,Authored):
    for pub in citation_data:
    
        if 'id' not in pub:
            continue

        AddJournals(pub,Journals,PublishedIn)
        AddPublications(pub,Publications)
        AddInCitations(pub,InCitations)
        AddOutCitations(pub,OutCitations)

        try:
            authors = pub['authors']
        except KeyError:
            authors = []
        if authors != []:
            AddAuthors(pub['id'],authors,Authors,Authored)



def AddOutCitations(pub,OutCitations):
    try:
        
        if len(pub['outCitations'])>0:
            for pid in pub['outCitations']:
                outCitation = {}
                outCitation['pid1'] = pub['id']
                outCitation['pid2'] = pid
                OutCitations.append(outCitation)
    except KeyError:
        pass



def AddInCitations(pub,InCitations):
    try:
        
        if len(pub['inCitations'])>0:
            for pid in pub['inCitations']:
                inCitation = {}
                inCitation['pid1'] = pub['id']
                inCitation['pid2'] = pid
                InCitations.append(inCitation)
    except KeyError:
        pass



def AddJournals(pub,Journals,PublishedIn):
    try:
        journalName = pub['journalName']
        
        if journalName == '':
            return 0
        if journalName not in Journals:
            Journals[journalName] = len(Journals)+1

        PublishedIn[pub['id']] = Journals[journalName]
    except KeyError:
        pass
    



def AddPublications(pub,Publications): # Add to Publications
    publication = {}
    try:
        publication['pid'] = pub['id']
    except KeyError:
        pass
    
    try:
        publication['year'] = pub['year']
    except KeyError:
        publication['year'] = -1
    
    try:
        if len(pub['fieldsOfStudy'])>0:
            publication['fieldsOfStudy'] = pub['fieldsOfStudy'][0]
        else:
            publication['fieldsOfStudy'] = ''
    except KeyError:
        publication['fieldsOfStudy'] = ''
    
    try:
        publication['venue'] = pub['venue']
    except KeyError:
        publication['venue'] = ''
        
    Publications.append(publication)
    


def AddAuthors(pid,authors,Authors,Authored): # add authors(pub) to Authors(whole)
    for author in authors:
        authorId = -1
        try:
            authorId = int(author['ids'][0])
            if authorId not in Authors:
                Authors[authorId] = author['name']
            
            authored = {}
            authored['pid'] = pid
            authored['authorid'] = authorId
            Authored.append(authored)
        except ValueError:
            continue
    



import os 

def SaveAuthored(save_dir,Authored):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'Authored.txt', 'w',encoding='utf-8') as txt_file:
        for authored in Authored:
            txt_file.write(str(authored['authorid']))
            txt_file.write("\t")
            txt_file.write(authored['pid'])
            txt_file.write("\n")

def SavePublishedIn(save_dir,PublishedIn):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'PublishedIn.txt', 'w',encoding='utf-8') as txt_file:
        for pid in PublishedIn:
            txt_file.write(pid)
            txt_file.write("\t")
            txt_file.write(str(PublishedIn[pid]))
            txt_file.write("\n")



def SaveOutCitations(save_dir,OutCitations):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'OutCitation.txt', 'w',encoding='utf-8') as txt_file:
        for outcitation in OutCitations:
            txt_file.write(outcitation['pid1'])
            txt_file.write("\t")
            txt_file.write(outcitation['pid2'])
            txt_file.write("\n")



def SaveInCitations(save_dir,InCitations):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'InCitation.txt', 'w',encoding='utf-8') as txt_file:
        for incitation in InCitations:
            txt_file.write(incitation['pid1'])
            txt_file.write("\t")
            txt_file.write(incitation['pid2'])
            txt_file.write("\n")





def SaveJournals(save_dir,Journals):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'Journal.txt', 'w',encoding='utf-8') as txt_file:
        for key in Journals:
            txt_file.write(str(Journals[key]))
            txt_file.write("\t")
            txt_file.write(key)
            txt_file.write("\n")



def SavePublications(save_dir,Publications):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'Publication.txt', 'w',encoding='utf-8') as txt_file:
        for pub in Publications:
            txt_file.write(pub['pid'])
            txt_file.write("\t")
            txt_file.write(str(pub['year']))
            txt_file.write("\t")
            txt_file.write(pub['venue'])
            txt_file.write("\t")
            txt_file.write(pub['fieldsOfStudy'])
            txt_file.write("\n")




def SaveAuthors(save_dir,Authors):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + 'Author.txt', 'w',encoding='utf-8') as txt_file:
        for key in Authors:
            txt_file.write(str(key))
            txt_file.write("\t")
            txt_file.write(Authors[key])
            txt_file.write("\n")



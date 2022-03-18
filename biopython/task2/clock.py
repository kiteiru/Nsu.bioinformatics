from Bio import Entrez

def GetmRNASeq(search, name):
    handle = Entrez.esearch(db="nucleotide", term=search)
    record = Entrez.read(handle)
    ids = record['IdList']

    seqID = ids[0]
    handle = Entrez.efetch(db="nucleotide", id=seqID, rettype="fasta", retmode="text")
    record = handle.read()

    filename = "out/" + name + ".fasta"
    with open(filename, "w") as file:
        file.write(record.rstrip("\n"))

Entrez.email = "enjiterin@gmail.com"

human = "Homo sapien"
mouse = "Mouse"
rat = "Rat"

searchHuman = "Clock[Gene] AND " + human + "[Organism] AND mRNA[Filter]"
searchMouse = "Clock[Gene] AND " + mouse + "[Organism] AND mRNA[Filter]"
searchRat = "Clock[Gene] AND " + rat + "[Organism] AND mRNA[Filter]"

GetmRNASeq(searchHuman, "clockHuman")
GetmRNASeq(searchMouse, "clockMouse")
GetmRNASeq(searchRat, "clockRat")
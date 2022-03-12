from Bio import Entrez

Entrez.email = "enjiterin@gmail.com"

human = "Homo sapien"
mouse = "Mouse"
rat = "Rat"

searchHuman = "Clock[Gene] AND " + human + "[Organism] AND mRNA[Filter]"
searchMouse = "Clock[Gene] AND " + mouse + "[Organism] AND mRNA[Filter]"
searchRat = "Clock[Gene] AND " + rat + "[Organism] AND mRNA[Filter]"

handle = Entrez.esearch(db="nucleotide", term=searchHuman)
record = Entrez.read(handle)
ids = record['IdList']

seqID = ids[0]
handle = Entrez.efetch(db="nucleotide", id=seqID, rettype="fasta", retmode="text")
record = handle.read()
with open("out/clockHuman.fasta", "w") as file:
    file.write(record.rstrip("\n"))

handle = Entrez.esearch(db="nucleotide", term=searchMouse)
record = Entrez.read(handle)
ids = record['IdList']

seqID = ids[0]
handle = Entrez.efetch(db="nucleotide", id=seqID, rettype="fasta", retmode="text")
record = handle.read()
with open("out/clockMouse.fasta", "w") as file:
    file.write(record.rstrip("\n"))

handle = Entrez.esearch(db="nucleotide", term=searchRat)
record = Entrez.read(handle)
ids = record['IdList']

seqID = ids[0]
handle = Entrez.efetch(db="nucleotide", id=seqID, rettype="fasta", retmode="text")
record = handle.read()
with open("out/clockRat.fasta", "w") as file:
    file.write(record.rstrip("\n"))
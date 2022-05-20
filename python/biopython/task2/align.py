from Bio import SeqIO, pairwise2
from Bio.pairwise2 import format_alignment

def DoPairwiseAlign(first, second, name):
    alignments = pairwise2.align.localxx(first[:650], second[:650])
    filename = "out/" + name + ".txt"
    with open(filename, "w") as file:
        for a in alignments:
            file.write(format_alignment(*a))

seqHuman = ""
seqMouse = ""
seqRat = ""
for seqRecord in SeqIO.parse("out/clockHuman.fasta", "fasta"):
    seqHuman = seqRecord.seq
    break
for seqRecord in SeqIO.parse("out/clockMouse.fasta", "fasta"):
    seqMouse = seqRecord.seq
    break
for seqRecord in SeqIO.parse("out/clockRat.fasta", "fasta"):
    seqRat = seqRecord.seq
    break

DoPairwiseAlign(seqHuman, seqMouse, "alignHumanAndMouse")
DoPairwiseAlign(seqHuman, seqRat, "alignHumanAndRat")
DoPairwiseAlign(seqMouse, seqRat, "alignMouseAndRat")
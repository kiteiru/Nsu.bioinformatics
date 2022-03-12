from Bio import SeqIO, pairwise2
from Bio.pairwise2 import format_alignment

seqHuman = ""
seqMouse = ""
for seqRecord in SeqIO.parse("out/clockHuman.fasta", "fasta"):
    seqHuman = seqRecord.seq
    break
for seqRecord in SeqIO.parse("out/clockMouse.fasta", "fasta"):
    seqMouse = seqRecord.seq
    break

alignments = pairwise2.align.localxx(seqHuman[:650], seqMouse[:650])
for a in alignments:
    print(format_alignment(*a))
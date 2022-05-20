from Bio.Align import MultipleSeqAlignment
from Bio.Blast import NCBIWWW
from Bio import SeqIO, AlignIO, pairwise2
import random
#import CreateSyntheticSeq from synthetic
from Bio.SeqRecord import SeqRecord
from Bio.pairwise2 import format_alignment


def MultipleAlign(seqList):
    '''align = MultipleSeqAlignment(seqList)
    with open("out/myAlign.phy", "w") as file:
        AlignIO.write(align, file, "phylip")'''
    with open("out/myAlign.phy", "w") as file:
        for i in range(49):
            align = pairwise2.align.globalxx(seqList[i], seqList[i+1])
            for a in align:
                file.write(format_alignment(*a))

def CreateSyntheticSeq(seqHuman):
    nucliotide = ["A", "T", "G", "C"]
    for i in range(50):
        string = seqHuman
        for j in range(20):
            idx = int(random.uniform(0, len(string)))
            string = string[:idx] + nucliotide[idx % 4] + string[idx:]
        seqList.append(string)
    print(seqList)

seqHuman = ""
for seqRecord in SeqIO.parse("out/clockHuman.fasta", "fasta"):
    seqHuman += seqRecord.seq

size = len(seqHuman)
num = int(random.uniform(0, size-100))
seqHuman = seqHuman[num:num+100]
print(seqHuman)

seqList = []
CreateSyntheticSeq(seqHuman)
MultipleAlign(seqList)

#result = NCBIWWW.qblast("blastn", "nt", )


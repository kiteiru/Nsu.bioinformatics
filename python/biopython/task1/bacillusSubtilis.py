from Bio import SeqIO
filePath = input("Please, enter filePath: ") #.fasta format file, for example: "data/geneSeq.fasta"

try:
    for seqRecord in SeqIO.parse(filePath, "fasta"):
        seq = seqRecord.seq
        print("Sequence: " + seq)
        print("\nComplement sequence: " + seq.complement())
        print("\nReverse complement sequence: " + seq.reverse_complement())
        print("\nTranslated sequence: " + seq.translate())
except:
    print("Usage: [fileName].fasta")

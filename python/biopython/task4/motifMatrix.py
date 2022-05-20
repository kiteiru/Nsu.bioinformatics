from pyjaspar import jaspardb

genes = ["Clock", "Arntl", "Cry1", "Cry2", "Per1", "Per2", "Nr1d1", "Nr1d2", "Rora", "Rorb", "Rorc", "Dbp", "Nfil3"]
jdb_obj = jaspardb()
motifs = jdb_obj.fetch_motifs_by_name(genes)
print(motifs)
with open("./out/motifMatrices.txt", "w") as file:
    file.write(str(motifs))

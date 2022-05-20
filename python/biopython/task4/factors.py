from pyjaspar import jaspardb

genes = ["Clock", "Arntl", "Dbp", "Nfil3", "Nr1d1", "Nr1d2", "Rora", "Rorb", "Rorc"]

jdb_obj = jaspardb()
motif = jdb_obj.fetch_motifs_by_name(genes)

for m in motif:
    freqMatrix = m.counts
    vector = []
    for j in range(len(freqMatrix[0])):
        all = 0
        for i in range(len(freqMatrix)):
            all += float(freqMatrix[i][j])
        vector.append(all)

    for j in range(len(freqMatrix[0])):
        for i in range(len(freqMatrix)):
            freqMatrix[i][j] = float(freqMatrix[i][j]) / vector[j]
    print(m.name + " weight matrix")
    print(freqMatrix)

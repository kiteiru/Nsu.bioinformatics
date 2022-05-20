if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install(version = "3.14")
BiocManager::install(c("MotifDb",  "GenomicFeatures", 
                       "TxDb.Scerevisiae.UCSC.sacCer3.sgdGene",
                       "org.Sc.sgd.db", "BSgenome.Scerevisiae.UCSC.sacCer3",
                       "motifStack", "seqLogo"))
library(BiocManager)
library(MotifDb)
library(S4Vectors)
library(seqLogo)
library(motifStack)
library(Biostrings)
library(GenomicFeatures)
library(org.Sc.sgd.db)
library(BSgenome.Scerevisiae.UCSC.sacCer3)
library(TxDb.Scerevisiae.UCSC.sacCer3.sgdGene)

BiocManager::install(c("org.Hs.eg.db", "TxDb.Hsapiens.UCSC.hg19.knownGene", "BSgenome.Hsapiens.UCSC.hg19"))

library(org.Hs.eg.db)
library(TxDb.Hsapiens.UCSC.hg19.knownGene)
library(BSgenome.Hsapiens.UCSC.hg19)

txdb=(TxDb.Hsapiens.UCSC.hg19.knownGene)

my_genes = c("CLOCK", "ARNTL", "CRY1", "CRY2",
             "PER1", "PER2", "NR1D1", "NR1D2", 
             "RORA", "RORB", "RORC", "DBP", "NFIL3")

myGeneSymbols <- select(org.Hs.eg.db,
                        keys = my_genes,
                        columns = c("SYMBOL","ENTREZID"),
                        keytype = "SYMBOL")

myGeneSymbolsTx <- select(TxDb.Hsapiens.UCSC.hg19.knownGene,
                          keys = myGeneSymbols$ENTREZID,
                          columns = c("GENEID", "TXID", "TXCHROM", "TXSTART", "TXEND"),
                          keytype = "GENEID")

res <- merge(myGeneSymbols, myGeneSymbolsTx, by.x = "ENTREZID", by.y = "GENEID")
dataframe <- res[,c("SYMBOL","TXSTART","TXEND")]

print(dataframe)

uniqueID <- res[, 1]
uniqueID <- uniqueID[!duplicated(uniqueID)]
print(uniqueID)

names <- res[, 2]
names <- names[!duplicated(names)]
print(names)

print(res)
for (i in 1:length(uniqueID)) {
  geneRangesList <- transcriptsBy(TxDb.Hsapiens.UCSC.hg19.knownGene, by = "gene") [uniqueID[i]]
  
  promoter.seq <- getPromoterSeq(geneRangesList, Hsapiens, upstream=500, downstream=100)
  
  print(names[i])
  print(promoter.seq)
}

clockID <- uniqueID[which(names == "CLOCK")[[1]]]
print(clockID)

arntlID <- uniqueID[which(names == "ARNTL")[[1]]]
print(arntlID)

query(MotifDb, clockID) 
pfm.clock.jaspar <- query(MotifDb,clockID)[[1]]
seqLogo(pfm.clock.jaspar)

chrom <-transcriptsBy(TxDb.Hsapiens.UCSC.hg19.knownGene, by="gene") [arntlID]
prom <- getPromoterSeq(chrom, Hsapiens, upstream=1000, downstream=0)
pcm.clock.jaspar <- round(100 * pfm.clock.jaspar)
matchPWM(pcm.clock.jaspar, unlist(prom)[[1]], "90%")

pfm.clock.jaspar <- query(MotifDb,"CLOCK")[[1]]
seqLogo(pfm.clock.jaspar)

pfm.arntl.jaspar <- query(MotifDb,"ARNTL")[[1]]
seqLogo(pfm.arntl.jaspar)

print(pfm.clock.jaspar)
print(pfm.arntl.jaspar)

dal1 <- clockID
chromosomal.loc <- 
  transcriptsBy(TxDb.Hsapiens.UCSC.hg19.knownGene, by="gene") [arntlID]
promoter.dal1 <- 
  getPromoterSeq(chromosomal.loc, Hsapiens, upstream=1000, downstream=0)
pcm.dal80.jaspar <- round(100 * pfm.dal80.jaspar)
matchPWM(pcm.dal80.jaspar, unlist(promoter.dal1)[[1]], "90%")


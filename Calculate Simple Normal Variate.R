dataset <- read.csv(file="E:\\sg_spectral", header=FALSE, sep=",")

library(inspectr)
 
s <- apply_spectra(dataset, snv)
library(prospectr)
snv <- standardNormalVariate(X = d)
write.csv(snv, file = "D:\\snv.csv")

dataset <- read.csv(file="E:\LUCAS.SOIL_corr.Rdata\LUCAS_wo_artifacts.csv", header=FALSE, sep=",")

library(inspectr)
 
s <- apply_spectra(dataset, snv)
library(prospectr)
snv <- standardNormalVariate(X = d)
write.csv(snv, file = "D:\\snv.csv")

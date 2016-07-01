x <- read.csv("up.csv",header=T,sep=",")
a<-x[[3]]
b<-c(250,500,750,1000,1250,1500,1750)
y<-split(a, findInterval(a, b))

z<-data.frame(NROW(y$'0'),NROW(y$'1'),NROW(y$'2'),NROW(y$'3'),NROW(y$'4'),NROW(y$'5'),NROW(y$'6'))


print(z)
write.table(z,"x.csv",sep=",",col.names=FALSE,row.names=FALSE)

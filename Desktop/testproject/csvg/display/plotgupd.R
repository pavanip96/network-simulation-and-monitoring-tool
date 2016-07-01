library(plotrix)

fo<-function(x)
{
df=read.csv("ClientUp.csv")
packet.freq<-table(df[[2]])
df2=read.csv("ClientDown.csv")
packet.freq<-table(df2[[2]])



df.pi<-unique(df[[2]],incomparables=FALSE)
df.pi
df.per<-prop.table(df.pi)
df.p<-df.per*100
y<-head(df.p)
pie(y)
columns <- rainbow((head(df.p)));


jpeg(file ="C://Users//P PRABHAKAR//Desktop//testproject//csvg//display//static//display//mainplotg.jpeg")

hist(packet.freq,xlab="packet",col="blue",breaks=15)

dev.off()

}

fo(h)


calc<-function()
{
     df<-read.csv("ClientUp.csv")
     df2<-read.csv("ClientDown.csv")
  
     row<-NROW(df)
     row2<-NROW(df2)
     print(row)
     print(row2)
     sum.df<-sum(df[[2]])
     sum.df2<-sum(df2[[2]])
     mean.df<-mean(df[[2]])
     mean.df2<-mean(df2[[2]])
     
     row<-NROW(df)
     row2<-NROW(df2)
     print(row)
     print(row2)
     print("sum is")
     print(sum.df)
     print(sum.df2)
     print("mean is") 
     print(mean.df)
     print(mean.df2)

     x<-(sum.df)/(60*60)
     x2<-(sum.df2)/(60*60)
     print("bandwidth for ClientUp(kbps)")
     print(x)
     print("bandwidth for ClientDown(kbps)")
     print(x2)
    
      id<-Sys.Date()
     date<-Sys.Date()
     ipd<-head(df2[[1]],1)
     print(ipd)
     

  df1<-data.frame(id,df[[1]],ipd,sum.df,sum.df2,mean.df,mean.df2,x,x2)
  w<-head(df1,1)
  print(w)
  write.csv(w,file="C://ProgramData//MySQL//MySQL Server 5.7//Uploads//writefile.csv",row.names=FALSE,col.names=FALSE,sep=",")

}
calc()









getwd()
full.matches<-list.files(pattern='up.*.csv',recursive=TRUE)
full.matches2<-list.files(pattern='down.*.csv',recursive=TRUE)
print(full.matches)
print(full.matches2)
tmp <- grep(pattern='^download/',full.matches, value = TRUE)
tmp2 <- grep(pattern='^download/',full.matches2, value = TRUE)
print(tmp)
print(tmp2)
args <- commandArgs(trailingOnly = TRUE)
time = as.numeric(args)

time=time-1
 

analysis<-function()

{
iden<-identical(tmp,character(0))
if(iden==TRUE)
{
date<-Sys.Date()
 dfm<-data.frame(date,"NILL","NILL",0,0,0,0,0,0,0,0,0)
        print(dfm)
	pack<-data.frame(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

        write.table(dfm,file="storedb.csv",sep=",",append="TRUE",row.names=FALSE,col.names=FALSE)
	write.table(pack,"packperc.csv",sep=",",col.names=FALSE,row.names=FALSE,append=TRUE)

}
else
{
for(i in 1:length(tmp))
	{
	print(i)

	upload=read.csv(tmp[i],sep=",")
	download=read.csv(tmp2[i])
#	x <- read.csv("up.csv",header=T,sep=",")
	set<-upload[[3]]
        ips<-head(upload[[1]],1)
	interval<-c(250,500,750,1000,1250,1500,1750,1000000000)
	y<-split(set, findInterval(set,interval))

	pack<-data.frame(ips,NROW(y$'0'),NROW(y$'1'),NROW(y$'2'),NROW(y$'3'),NROW(y$'4'),NROW(y$'5'),NROW(y$'6'),NROW(y$'7'))


	print(pack)
	set2<-download[[3]]
        interval<-c(250,500,750,1000,1250,1500,1750,1000000000)
        y2<-split(set2, findInterval(set2,interval))

    #    pack<-data.frame(ips,NROW(y2$'0'),NROW(y2$'1'),NROW(y2$'2'),NROW(y2$'3'),NROW(y2$'4'),NROW(y2$'5'),NROW(y2$'6'),NROW(y2$'7'))
        pack$new.col1 <-NROW(y2$'0')
	pack$new.col2 <-NROW(y2$'1')
	pack$new.col3 <-NROW(y2$'2')
        pack$new.col4 <-NROW(y2$'3')
        pack$new.col5 <-NROW(y2$'4')
        pack$new.col6 <-NROW(y2$'5')
        pack$new.col7 <-NROW(y2$'6')
        pack$new.col8 <-NROW(y2$'7')
	pack$new.col9<-length(upload[[3]])
	pack$new.col10<-length(download[[3]])
       write.table(pack,"packperc.csv",sep=",",col.names=FALSE,row.names=FALSE,append=TRUE)

        sum.up=0
	mean.up=0
	band.up=0
	sum.down=0
	mean.down=0
	band.down=0
	uppacket=upload
	downpacket=download

	

	sum.up<-sum(uppacket[[3]])
	print(sum.up)
	totalpacketsup<-NROW(uppacket)
	print(totalpacketsup)
	mean.up<-mean(uppacket[[3]])
	print(mean.up)
	band.up<-((totalpacketsup*mean.up)/(time*1000))*8
	print(band.up)
	sum.down<-sum(downpacket[[3]])
	print(sum.down)
	totalpacketsdown<-NROW(downpacket)
	print(totalpacketsdown)
	mean.down<-mean(downpacket[[3]])
	print(mean.down)
	band.down<-((totalpacketsdown*mean.down)/(time*1000))*8
	print(band.down)
	totalpackets=totalpacketsup+totalpacketsdown
	print(totalpackets)

	ips<-head(uppacket[[1]],1)
	ipd<-head(uppacket[[2]],1)
	date<-Sys.Date()
	
	dfm<-data.frame(date,ips,ipd,totalpacketsup,totalpacketsdown,totalpackets,sum.up,mean.up,band.up,sum.down,mean.down,band.down)
	print(dfm)
	
	
	write.table(dfm,file="storedb.csv",sep=",",append="TRUE",row.names=FALSE,col.names=FALSE)
	}
}
}

analysis()






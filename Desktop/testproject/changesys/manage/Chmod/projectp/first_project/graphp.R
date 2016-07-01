library(RMySQL)
library(plotrix)

	args <- commandArgs(trailingOnly = TRUE)
        monid = as.character(args[1])
#	args2 <- commandArgs(trailingOnly = TRUE)
#	pcid = as.character(args[2])
	print(monid)
#	print(pcid)

#monid="20160627-14:22:31-M"

	mysqlconnection = dbConnect(MySQL(), user = 'root', password = 'qwerty', dbname = 'manu',host = 'localhost')
	x=dbListTables(mysqlconnection)
	print(x)
	sql<-sprintf("select * from nettest_percentageofpacketup where monid1='%s'",monid )
	up=dbGetQuery(mysqlconnection,sql)
	u=up[[3]]
	
	print(up)
        sql2<-sprintf("select * from nettest_percentageofpacketdown where monid1='%s' ",monid)
		
	down = dbGetQuery(mysqlconnection,sql2)
	sql3<-sprintf("select pcid from nettest_percentageofpacketup where monid1='%s' ",monid)
        pcid=dbGetQuery(mysqlconnection,sql3)
        print("pcidlist")

	print(u)	
	u=up[[3]]
	d=down[[3]]
	print("id")
	
	for(j in 1:NROW(up[[3]]))
{

	sql<-sprintf("select * from nettest_percentageofpacketup where monid1='%s' and pcid='%s'",monid,u[[j]] )
        up=dbGetQuery(mysqlconnection,sql)
	print("first up query")
	print(up)
	sql2<-sprintf("select * from nettest_percentageofpacketdown where monid1='%s' and pcid='%s' ",monid,d[[j]])
	pcid1=u[[j]]

        down = dbGetQuery(mysqlconnection,sql2)
	pcid2=d[[j]]
	
	print(d[[j]])
	print(down)
	print("no. of rows")
	print(	NROW(up))
	print(NROW(down))
#	result<-sprintf("select * from nettest_monitable where monid='%s' and pcid='%s';",monid,pcid)

#	result1=dbGetQuery(mysqlconnection,result)
#	jpeg("table.jpeg",height=1000,width=200)
#	grid.table(result1)
 #       grid.arrange(result1)
	for( i in 1:(NROW(up)))
{ 
	pcid=d[[i]]
	pu1_250=(up[[5]]/up[[13]])*100
	print(pu1_250)
	pu251_500=(up[[6]]/up[[13]])*100
	print(pu251_500)
	pu501_750=(up[[7]]/up[[13]])*100
	print(pu501_750)
	pu751_1000=(up[[8]]/up[[13]])*100
        print(pu751_1000)
	pu1001_1250=(up[[9]]/up[[13]])*100
	pu1251_1500=(up[[10]]/up[[13]])*100
        print(pu1251_1500)
        pu1501_1750=(up[[11]]/up[[13]])*100
        print(pu1501_1750)
        pu1751=(up[[12]]/up[[13]])*100
       
	ptotup=up[[13]]

	pd1_250=(down[[5]]/down[[13]])*100
	pd251_500=(down[[6]]/down[[13]])*100
	pd501_750=(down[[7]]/down[[13]])*100
	pd751_1000=(down[[8]]/down[[13]])*100
	pd1001_1250=(down[[9]]/down[[13]])*100	
	pd1251_1500=(down[[10]]/down[[13]])*100
	pd1501_1750=(down[[11]]/down[[13]])*100
	pd1751=(down[[12]]/down[[13]])*100

	ptotdown=down[[13]]

	slices<-c(pu1_250,pu251_500,pu501_750,pu751_1000,pu1001_1250,pu1251_1500,pu1501_1750,pu1751)
	print(slices)
#	barup<-table(slices)
#	cols <- c("red","blue","green","yellow")
	percentlabels<- round(100*slices/sum(slices), 1)
	jpeg(file=paste0("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/nettest/static/nettest/percpackup",j,i,".jpeg"))

	pie(slices,main=paste0("piechart for percentage of uploaded packets",pcid1,":"),col=rainbow(length(percentlabels)),labels=percentlabels)
	legend("topright", c("1-250","251-500","501-1000","1001-1250","1251-1500","1501-1750",">1751"), cex=0.8, fill=rainbow(length(percentlabels)))

	jpeg(file=paste0("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/nettest/static/nettest/barperup",j,i,".jpeg"))

	barplot(slices,main=paste0("barplot of % of uploaded packets",pcid1,":"),xlab="packets",ylab="percentage of packets",col=rainbow(length(percentlabels)))
        legend("topright", c("1-250","251-500","501-1000","1001-1250","1251-1500","1501-1750",">1751"), cex=0.8, fill=rainbow(length(percentlabels)))
        slices2<-c(pd1_250,pd251_500,pd501_750,pd751_1000,pd1001_1250,pd1251_1500,pd1501_1750,pd1751)
#	bardown<-table(slices2)
 #       col2s <- c("red","blue","green","yellow")
        percentlabels<- round(100*slices2/sum(slices2), 1)
        jpeg(file=paste0("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/nettest/static/nettest/percpackdown",j,i,".jpeg"))
        pie(slices2,main=paste0("piechart for percentage of downloaded packets for ",pcid2,":"),col=rainbow(length(percentlabels)),labels=percentlabels)
        legend("topright",c("1-250","251-500","501-1000","1001-1250","1251-1500","1501-1750",">1751"), cex=0.8, fill=rainbow(length(percentlabels)))

        jpeg(file=paste0("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/nettest/static/nettest/barperdown",j,i,".jpeg"))
        barplot(slices2,main=paste0("barplot of % of downloaded packets",pcid2,":"),xlab="packets",ylab="percentage of packets",col=rainbow(length(percentlabels)))
        legend("topright", c("1-250","251-500","501-1000","1001-1250","1251-1500","1501-1750",">1751"), cex=0.8, fill=rainbow(length(percentlabels)))
	
#	jpeg(file="/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/nettest/static/nettest/lineup1.jpeg")
#	bandu<-read.csv("bandwidth.csv",header=FALSE)
#	plot(bandu,type="l",xlab="time",ylab="bandwidth(upload)")
 #       jpeg(file="/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/nettest/static/nettest/linedown1.jpeg")
  #      bandd<-read.csv("bandwidthdown.csv",header=FALSE)
   #     plot(bandd,type="l",xlab="time",ylab="bandwidth(download)")
	graphics.off()
#	all_cons <- dbListConnections(MySQL())
 #    for(con in all_cons)
  #    dbDisconnect(con)
	
}	
	
	
	}

 all_cons <- dbListConnections(MySQL())
     for(con in all_cons)
     dbDisconnect(con)

band_multiple_calci<-function()
{   
    args <- commandArgs(trailingOnly = TRUE)
i   time = as.numeric(args)
    df_uploadPacket<-read.csv("clientUp.csv",header=FALSE)
   df_downloadPacket<-read.csv("clientDown.csv",header=FALSE)
  vvi  ip_upload<-df_uploadPacket[[1]]
    ipd_upload<-df_uploadPacket[[2]]
    ip_download<-df_downloadPacket[[2]]
    ipd_download<-df_downloadPacket   unique_ipUpload<-unique(df_uploadPacket[[1]])
    unique_ipDownload<-unique(df_downloadPacket[[2]])
    sum.upload=0;
    sum.download=0;
    mean.upload=0;
    mean.download=0;
    band.upload=0;
    band.download=0;
    sumofpacketup=0
    sumofpacketdown=0
    date<-Sys.Date()
    time=120
    packets_upload<-df_uploadPacket[[3]]
    packets_download<-df_downloadPacket[[3]]

      for(i in 1:length(unique_ipUpload))
	{
	sum.upload=0
      mean.upload=0
      band.upload=0
      count=0
      sumofpacketup=0

		for(j in 1:length(df_uploadPacket[[1]]))
		{
			if(ip_upload[[j]]==unique_ipUpload[[i]])
			{
                  sumofpacketup=sumofpacketup+1


			sum.upload=sum.upload+packets_upload[[j]]
                  mean.upload=sum.upload/sumofpacketup;	

			
			band.upload=((sumofpacketup*mean.upload)/(time*1000))
			dfm<-data.frame(ipupload=ip_upload[[j]],ipdown=ipd_upload[[1]],sum=sumofpacketup,sum.upload,mean=mean.upload,band=band.upload)
			}
		}
	write.table(dfm,file="//home//ttt//Documents//monitor//projectp//first_project//mul.csv",sep=",",append="TRUE",row.names=FALSE,col.names=FALSE)
	}
  
      for(i in 1:length(unique_ipDownload))
	{
	sum.download=0
      mean.download=0
      band.download=0
      count=0
      sumofpacketdown=0

		for(j in 1:length(df_downloadPacket[[1]]))
		{
			if(ip_download[[j]]==unique_ipDownload[[i]])
			{
                  sumofpacketdown=sumofpacketdown+1

			sum.download=sum.download+packets_download[[j]]
                  mean.download=sum.download/sumofpacketdown;	

			
			band.download=((sumofpacketdown*mean.upload)/(time*1000))
			dfm<-data.frame(ips=ipd_download[[j]],ipd=unique_ipDownload[[i]],sum=sumofpacketdown,sum.download,mean=mean.download,band=band.download)
			}
		}
	write.table(dfm,file="//home//ttt//Documents//monitor//projectp//first_project//mul2.csv",sep=",",append="TRUE",row.names=FALSE,col.names=FALSE)
	}




	}

band_multiple_calci()

# Monthly data analysis: February 2013

# Data set from: http://report.nih.gov/categorical_spending.aspx

# Before you begin, you will have to open the xls file and unmerge rows 2+3,
# then delete rows 1+2.  There are also a bunch of rows at the end to delete.
# Save as a csv file, which will get rid of any excess formatting.

# To follow my analysis, run the file.  This will create a pdf.  Open the pdf,
# and read through this file while checking the pdf as you go.  You can make
# changes to this file and run it while keeping the pdf open and it will
# update automatically.

# To run the file you may need to install the calibrate package.  
# To do so, uncomment the lines below:
#install.packages("calibrate")
#library(calibrate)

# read in file
funding_raw <- read.csv("funding.csv")
funding <- funding_raw

# Get rid of dollar signs and commas in the data, and convert to numeric
clean <- function(ttt){
	as.numeric( gsub('[$,]', '', ttt))
}
funding_raw <- sapply(funding_raw[2:9], clean)
funding[2:9] <- funding_raw

# Start by looking at overall funding
pdf("funding_analysis.pdf")
par(mfrow=c(3,2)) # Layout
hist(funding$FY.2008Actual,main="Chart 1: 2008")
hist(funding$FY.2013Estimated,main="Chart 2: 2013")

# These look pretty similar, so we're not getting much out of this view.
# What do we want to know?  Maybe which diseases have changed funding?
# Let's look at the percent change in funding between 2008 and 2013.

# Get rid of rows with NAs or 0s
fund_clean <- funding[complete.cases(funding),]
fund_clean <- fund_clean[fund_clean$FY.2008Actual > 0,]
# Graph
hist(fund_clean$FY.2013Estimated/fund_clean$FY.2008Actual,main="Chart3: Percent change 2008-2013",xlab="2013 funding over 2008 funding")

# As expected, most funding levels have stayed about the same.  Which are
# the outliers?

# Make the change column part of our data frame
fund_clean$change <- fund_clean$FY.2013Estimated/fund_clean$FY.2008Actual

# Create new, smaller dataset made up of only top 5 and bottom 5
top_fund <- head(fund_clean[order(fund_clean$change,decreasing=TRUE),],5)
bot_fund <- head(fund_clean[order(fund_clean$change,decreasing=FALSE),],5)
changed <- rbind(top_fund,bot_fund)

# You can view this dataset in the R prompt
print(changed)

# Plot the biggest growth as a time series
top_ts <- ts(changed[,1],start=c(2008, 1), end=c(2013, 1), frequency=1)
plot(top_ts,main="Time Series for Largest Growing Research Area",ylab=changed[1,1])

# Plot the biggest decrease as a time series
bot_ts <- ts(changed[,10],start=c(2008, 1), end=c(2013,1), frequency=1)
plot(bot_ts,main="Time Series for Research Area With Greatest Decrease",ylab=changed[10,1])

# Save pdf
dev.off()

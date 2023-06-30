class dateHandler:
 # Return all the posibilities of each date (list of lists)
    def getPossibleDates(self):
        result=[]
        for date in Info.dateData:
            options=[]
            options.append(dateHandler.dayConverter(date.day))
            options.append(self.monthConverter(date.month))
            options.append(self.yearConverter(date.year))
            result.append(options)
        return result
    
 # All the options of a day      
    def dayConverter( day ):
        return [*set([str(day),"0" + str(day)])] if day<10 else [*set([str(day),str(day)])]
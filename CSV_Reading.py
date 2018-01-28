'''
Created on Jan 22, 2018

@author: Kingsley
'''
import collections
import urllib.request
import csv

htmlfile = urllib.request.urlopen("http://stackabuse.com/download-files-with-python/")
urllib.request.urlretrieve("http://rapid-hub.org/data/angles_UCI_CS.csv", "try.csv")
csv1 = open("try.csv")
csvread = csv.reader(csv1)
csvlist = [csvread]
csvdict = collections.OrderedDict()
lister = []

def printcsv(csvread):
    for a in csvread:
        print(a)

def simpleCSV(b):
    lists = []
    slices = ''
    for a  in b:
        if len(csvdict) < 2:
            csvdict[a[0]] = []
            csvdict[a[1]] = []
            lists.append(a[0])
            lists.append(a[1])
            slices = lists.index(a[0])
        else:
            for key, value in csvdict.items():
                if key == lists[slices]:
                    value.append(a[0])
                else:    
                    value.append(a[1])
    
        
def printdict(b):
    lister = []
    for keys, values in b.items():
        a = (keys,values)
        lister.append(a)
    station= ''
    for i in lister[0][1]:
        station += "{}: {} {}: {}".format(lister[0][0],i, lister[1][0],lister[1][1].pop(0))
        print(station)
        station = ''
    





if __name__ == '__main__':
    #printcsv(csvread)
    simpleCSV(csvread)
    printdict(csvdict)
    csv1.close()
    pass
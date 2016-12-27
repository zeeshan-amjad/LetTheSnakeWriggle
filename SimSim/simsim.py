import webbrowser, sys

def runScript():        #opens the list of urls stored in the text file: simsim.txt
        urlList = getUrlList()
        if len (urlList) == 0:
                c = input ('Oops! There are no URLs! Want to add some? [Y/N]: ')
                while c == 'Y' or c == 'y':
                        addUrl()        #adds a url input by the user
                        c = input ('Want to add more? [Y/N]: ')
        urlList = getUrlList()
        for url in urlList:
                webbrowser.open (url)

def addUrl():
        url = input ('enter url: ')
        with open ('simsim.txt', 'a') as f:
                f.write (url + '\n')
        f.close()

def delUrl():
        url = input ('enter url: ')
        urls = getUrlList()
        f = open ('simsim.txt', 'w')
        for u in urls:
                if u != url:
                        f.write (u + '\n')
        f.close()

def clearUrlList():
        open ('simsim.txt', 'w').close()

def getUrlList():
        with open ('simsim.txt') as f:
                urlList = f.read().splitlines()
        f.close()
        return urlList

def showUrlList():
        urlList = getUrlList()
        print (urlList)

if len (sys.argv) > 1:
        s = str (sys.argv[1])
        if s == 'add':
                addUrl()
        if s == 'remove':
                delUrl()
        if s == 'clear':
                clearUrlList()
        if s == 'show':
                showUrlList()
else:
        runScript()

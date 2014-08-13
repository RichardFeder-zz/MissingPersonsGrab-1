2#This web scraper pulls information from findthemissing.org
#We will be pulling the following: the link to the case number,picture, name, address.

import requests
import lxml.html

#possible storage = file system

class NamUSGrab:
    def __init__(self):
        self.cases = []
    
    def pageGrab(self,url_query):
        base_query = url_query
        r = requests.get(url_query)
        count = 1
        while r.status_code == 200:

            html = lxml.html.fromstring(r.text)
            parsed = html.xpath('//table[@class="case_result"]')
            
            self.cases.append([])
            url_query = url_query.replace(str(count),str(count+1))
            count += 1
            r = requests.get(url_query)

        return cases
#https://www.findthemissing.org/en/cases/search/thumbnail?direction=asc&order=cases.DateLKA&page=1


#http://doenetwork.org/cases/disappear.html
def pageGrabDoe(url):
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    to_parse = 
    
    
    
    
    
    
def SeleniumNamusGrab():
    from selenium import webdriver
    webdriver.Firefox()
    url = 'https://www.findthemissing.org/en/searches'
    browser.get(url)
    url = 'https://www.findthemissing.org/en/cases/search'
    browser.get(url)
    url = 'https://www.findthemissing.org/en/cases/search/thumbnail'
    browser.get(url)
    
    
def NamusGrab2(url):
    import requests
    import lxml.html
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    processed = html.xpath('//img')
    images = []
    for elem in processed:
        if not "National" in elem.values()[0]:
            if not "Star" in elem.values()[0]:
                if not "Grey_star" in elem.values()[0]:
                    if not "Nij_logo" in elem.values()[0]:
                        if not "Ojp_seal" in elem.values()[0]:
                            if not "1229961902" in elem.values()[0]:
                                if not "Right" in elem.values()[0]:
                                    if not "Left" in elem.values()[0]:
                                        images.append(elem.values())
    del images[0:4]
    return images
   
        
        
def iterGrabNamus():
    base_url_namus = 'https://www.findthemissing.org/en/cases/'
    namus_urls = []
    for i in xrange(25,32):
        iter_url_namus =  base_url_namus.replace("cases/","cases/"+ str(i))
        r = requests.get(iter_url_namus)
        html = lxml.html.fromstring(r.text)
        if r.status_code == 200:
            namus_urls.append(iter_url_namus)
    case_data = []
    for case in namus_urls:
        r = requests.get(case)
        case_images = NamusGrab2(case)
        case_file_urls = []
        for rel_url in case_images:
            case_file_urls.append("http://findthemissing.org"+rel_url[0])
        case_file_urls.insert(0,case)
        case_data.append(case_file_urls)
        print case_data
    lengths = [len(x) for x in case_data]
    print lengths
    for j in xrange(lengths):
        print int(lengths[j])
    return case_data
    
    
    



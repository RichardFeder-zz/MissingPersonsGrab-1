import requests
import lxml.html
def doeGrab(url):
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    processed = html.xpath('//a')
    images = []
    for elem in processed:
        if not "disappear" in elem.values()[0]:
            if not "http" in elem.values()[0]:
                images.append(elem.values())
    case_file_urls = []
    for rel_url in images:
        case_file_urls.append("http://doenetwork.org/cases/"+rel_url[0])
    case_data = []
    for case in case_file_urls:
        r = requests.get(case)
        html = lxml.html.fromstring(r.text)
        case_html = html.xpath('//img')
        case_images = [elem.values() for elem in case_html]
        case_images.insert(0,case)
        case_data.append(case_images)
    return case_data


# doeGrab('http://doenetwork.org/cases/disappear.html')


def iterGrab():
    base_url = 'http://doenetwork.org/cases/disappear.html'
    r = requests.get(base_url)
    i = 2
    all_cases = []
    print r.status_code, "status code"
    while r.status_code == 200:
        iter_url = base_url.replace("disappear","disappear" + str(i))
        print iter_url, "iter url"
        r = requests.get(iter_url)
        print r.status_code, "status code inside while loop"
        stuff = doeGrab(iter_url)
        print stuff," result of doeGrab()" 
        all_cases.append(stuff)
        print all_cases, " print total cases thus far"
        i += 1
        print i, " where we are in the iteration"
    return all_cases
# iterGrab('http://doenetwork.org/cases/disappear.html')

import requests
import lxml.html

def NamphGrab(url):
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    processed = html.xpath('//a')
    images = []
    links = []
    for elem in processed:
        if not "index" in elem.values()[0]:
            if not "mp" in elem.values()[0]:
                if not "hot" in elem.values()[0]:
                    if not "submit" in elem.values()[0]:
                        if not "search" in elem.values()[0]:
                            if not "contact" in elem.values()[0]:
                                if not "located" in elem.values()[0]:
                                    if not "media" in elem.values()[0]:
                                        if not "about" in elem.values()[0]:
                                            if not "links" in elem.values()[0]:
                                                if not "bravenet" in elem.values()[0]:
                                                    if not "s18" in elem.values()[0]:
                                                        if not "microsoft" in elem.values()[0]:
                                                            if not "mailto" in elem.values()[0]:
                                                                if not "updates" in elem.values()[0]:
                                                                    if not "Bravenet" in elem.values()[0]:
                                                                        links.append(elem.values())
    case_file_urls = []
    
    for rel_url in links:
        case_file_urls.append("http://www.nampn.org/"+rel_url[0])
    case_data = []
    for case in case_file_urls:
        r = requests.get(case)
        html = lxml.html.fromstring(r.text)
        case_html = html.xpath('//img')
        case_images = [elem.values() for elem in case_html]
        case_images.insert(0,case)
        case_data.append(case_images)
    return case_data
    
# use NamphGrab("http://www.nampn.org/cases") to get all cases, use iterGrabNamph() for all cases 1996 to present.
def iterGrabNamph():
    months = ['Jan-Mar', 'Apr-Jun', 'Jul-Sep', 'Oct-Dec']
    for period in months:
        base_url_namph = 'http://www.nampn.org/mp' + str((months[period])
        i = 1996
        r = requests.get(base_url_namph)
        all_cases = []
        while r.status_code == 200:
            iter_url_namph = base_url_namph.replace("mp","mp" + str(i))
            r = requests.get(iter_url_namph)
            cases = doeGrab(iter_url_namph)
            all_cases.append(cases)
            i += 1
    return all_cases                                           


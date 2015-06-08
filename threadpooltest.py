import urllib2
import time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool

urls = [
    'http://www.python.org', 
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/',
    'http://www.baidu.com/',
    'http://www.163.com/'
    ]
def openURL(url):
    response = urllib2.urlopen(url)

if __name__ == "__main__":
    starttime = time.time()
    # Make the Pool of workers
    #pool = ThreadPool(20)
    pool = ProcessPool()
    # Open the urls in their own threads
    # and return the results
    # Notice: if you use multi-process, you can not use class method directly(here urllib2.urlopen)
    # You have to encapsulate yourself(here openURL)
    pool.map(openURL, urls) 
    #close the pool and wait for the work to finish 
    pool.close() 
    pool.join()
    endtime = time.time()
    time = endtime - starttime
    print "It took %ds totally." %time

 
 googleScholar_spider
====================
 
 
##About 

googleScholar_spider

It's a Program based on google_search_module developed by: 

Author: Tan Kok Hua (Guohua tan)

Email: spider123@gmail.com

More information can be obtained from: http://wp.me/p4nnkg-1i


Modified by:

Author: David Hine 

Email:david@hine.co.cr




## General Information


Retrieve Google Scholar results using python and Scrapy

Program obtained the results links from googleScholar main page, and each links are run separately using Scrapy. googleScholar_spider add the posibility to extract metadata such as: Author, Publisher, date; using Google & Dublin Core standard.

Dublin Core Sintaxis example:

    <META NAME="DC.Title "CONTENT=" 

    <META NAME="DC.Creatorr "CONTENT=" 

    <META NAME="DC.Subject "CONTENT=" 

    <META NAME="DC.Description "CONTENT=" 

    <META NAME="DC.Publisher "CONTENT=" 

    <META NAME="DC.Contributor "CONTENT=" 

    <META NAME="DC.Date" CONTENT=" 

    <META NAME="DC.Coverage "CONTENT=" 

    <META NAME="DC.Format "CONTENT=" 

    <META NAME="DC.Identifier"CONTENT=" 

    <META NAME="DC.Fuente "CONTENT=" 

    <META NAME="DC.Language "CONTENT=" 

    <META NAME="DC. type "CONTENT=" 

    <META NAME="DC.Relation "CONTENT=" 

    <META NAME="DC.Rights "CONTENT="


## Installation & Configuration

Dependency of script are Scrapy and yaml (for unicode handling). Both can be downloaded using PIP.

    pip install Scrapy

    pip search yaml
  
    pip install pyyaml

if you want to install with linux repositories.

    $ sudo apt-get install python-yaml
  
    $ sudo yum install python-yaml

 Scripts is divided into 2 parts. The main script for running is from Google_Scholar.py The get_google_link_results.py is the scrapy spider for crawling either the google Scholar search page or individual websites. 

##Support & Documentation

Scrapy
    http://doc.scrapy.org/en/0.24/

Dubli Core Sintaxis
    http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1024-94352006000400009


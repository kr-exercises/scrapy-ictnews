Installation Guide:

1- Create virtual environment:

    virtualenv epg-env

2- Activate virtual environment:

    source epg-env/bin/activate
 
3- Install requirements:

    pip install -r requirements.txt
    
4-  Start :

    scrapy runspider ict.py -o ictnews.csv

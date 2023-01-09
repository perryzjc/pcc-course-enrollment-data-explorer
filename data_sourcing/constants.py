"""Store the constants used in the data_sourcing package
"""
import os

# REQUEST_INTERVAL is the time interval (in seconds) between two requests
REQUEST_INTERVAL = 30 * 60
# OUTPUT_FOLDER specifies the folder where the output files are stored
OUTPUT_FOLDER = 'output'
# OUTPUT_DATA_SOURCING_FOLDER specifies the folder where the output files from data sourcing are stored
OUTPUT_DATA_SOURCING_FOLDER = os.path.join(OUTPUT_FOLDER, 'data_source')
# SAMPLE_FOLDER specifies the folder where the sample html files are stored
SAMPLE_HTML_FOLDER = 'sample_html'
# ALL_COURSES_URL is the url of the PCC course schedule web
ALL_COURSES_URL = 'https://ssb-prod.ec.pasadena.edu/PROD/pw_psearch_sched.p_listthislist'
# HEADER is the header of the request for PCC course schedule web
HEADER = {
    'Host': 'ssb-prod.ec.pasadena.edu',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://ssb-prod.ec.pasadena.edu',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://ssb-prod.ec.pasadena.edu/PROD/pw_psearch_sched.p_search'}
# POST_DATA is the data of the request for PCC course schedule web
POST_DATA = "TERM=202330&TERM_DESC=Spring+2023&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_camp=dummy&sel_ism=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attrib=dummy&sel_schd=%25&sel_subj=%25&sel_crse=&sel_crn=&sel_title=&sel_ptrm=%25&sel_instr=%25&sel_attrib=%25&begin_hh=5&begin_mi=0&begin_ap=a&end_hh=11&end_mi=0&end_ap=p&aa=N&bb=N&ee=N&sel_sess=%25&sel_ism=%25&sel_camp=%25"

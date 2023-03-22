"""Store the constants used in the data_sourcing package
"""
from backend.config.config import CONFIG_DIR_PATH
import os

# REQUEST_INTERVAL is the time interval (in seconds) between two requests
REQUEST_INTERVAL = 30 * 60

# COURSE_STATUS_LIST is the list of all possible course status
COURSE_STATUS_LIST = ['OPEN', 'CLOSED', 'Waitlisted', 'Restricted: See Counselor',
                      'Restricted: Dual Enrollment', 'Restricted: SLPA', 'Restricted',
                      'Permission of Instructor', 'Permission of Dean',
                      'Restricted: Restorative Dental',
                      'Restricted: Biotechnology Prog', 'Restricted: Nursing Program',
                      'Audition Required', 'Restricted: Med Asst Program',
                      'Restricted: Math Path', 'Restricted: Dental Hygiene',
                      'Restricted: Dental Assisting', 'Restricted: Ujima',
                      'Restricted: Puente', 'Restricted: Study Abroad', 'See Instructor']


# DATA_FOLDER specifies the folder where the data files are stored
DATA_FOLDER = os.path.join(CONFIG_DIR_PATH, '../data')

# OUTPUT_DATA_SOURCING_FOLDER specifies the folder where the data files from data sourcing are stored
DATA_DATA_SOURCING_FOLDER = os.path.join(DATA_FOLDER, 'data_source')

# SAMPLE_FOLDER specifies the folder where the sample html files are stored
SAMPLE_HTML_FOLDER = 'sample_html'

# ALL_COURSES_URL is the url of the PCC course schedule web
ALL_COURSES_URL = 'https://ssb-prod.ec.pasadena.edu/PROD/pw_psearch_sched.p_listthislist'

# KEY_BEFORE_FIRST_COURSE_DATA is the key word used search in order to find the first course data
KEY_BEFORE_FIRST_COURSE_DATA = '<td nowrap="nowrap" valign="top" class="default'

# HEADER is the header of the request for PCC course schedule web
# This data can be obtained by inspecting the request header in the browser
# A example tool on MAC can be FiddlerEverywhere
HEADER = {
    'Host': 'ssb-prod.ec.pasadena.edu',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://ssb-prod.ec.pasadena.edu',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://ssb-prod.ec.pasadena.edu/PROD/pw_psearch_sched.p_search'}

# POST_DATA is the data of the request for PCC course schedule web
# This data can be obtained by Fiddler
# To change the term for search,
# replace TERM=202330 with TERM=year + term code
# replace TERM_DESC=Spring+2023 with TERM_DESC=term description + year
POST_DATA = "TERM=202330&TERM_DESC=Spring+2023&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_camp=dummy&sel_ism=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attrib=dummy&sel_schd=%25&sel_subj=%25&sel_crse=&sel_crn=&sel_title=&sel_ptrm=%25&sel_instr=%25&sel_attrib=%25&begin_hh=5&begin_mi=0&begin_ap=a&end_hh=11&end_mi=0&end_ap=p&aa=N&bb=N&ee=N&sel_sess=%25&sel_ism=%25&sel_camp=%25"
DUMMY_TERM_CODE = '202330'
DUMMY_TERM_DESC = 'Spring+2023'
# TERM_MAP is the map from term description to term code
TERM_MAP = {'Spring': '30', 'Summer': '50', 'Fall': '70'}

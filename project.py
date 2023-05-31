import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt 
import seaborn as sns
SEED = 42
pd.set_option("display.max_columns", None)

df = pd.read_csv(r'data.csv', delimiter='\t') #import dataset

# build list of removed features to deleted from dataset
removedFeatures = [f'Q{i}E' for i in range(1, 43)] # add feature 'Q1E' to 'Q42E' to be removed
removedFeatures.extend([f'Q{i}I' for i in range(1, 43)]) # add feature 'Q1I' to 'Q42I' to be removed
removedFeatures.extend([f'VCL{i}' for i in range(1, 17)]) # add feature 'VCL1' to 'VCL16' to be removed
removedFeatures.extend([ 'source', 'introelapse', 'testelapse', 'surveyelapse', 'engnat', 'hand', 'orientation',
    'voted', 'country', 'screensize', 'uniquenetworklocation']) #add other features to be removed

# remove features from the dataset
depression = df.drop(removedFeatures, axis=1)

plt.figure(figsize=(17, 8))
sns.heatmap(depression.isnull())

print(depression.isnull().sum())

'''
    education "How much education have you completed?"
    1=Less than high school, 
    2=High school, 
    3=University degree, 
    4=Graduate degree   
'''

# combine 0 and 1 values as one value of 1

depression['education'] = depression['education'].map({ 0: 1,  1: 1, 2: 2, 3: 3, 4: 4 })

def changeEducationTitle(title) -> str:
    if title == 0 or title == 1:
        return 'Less than high school'
    if title == 2:
        return 'High school'
    if title == 3: 
        return 'University degree'
    if title == 4: 
        return 'Graduate degree'
    return title


# change education values form numbers to values to understand
education_string = depression['education'].apply(changeEducationTitle)
print(education_string)

plt.figure(figsize=(15, 8))
sns.countplot(x=depression['education'], hue=education_string)

# change the major values that are related

def changeMajorValues(title):
    if 'busin' in str(title).lower() or 'manage' in str(title).lower() or 'Buss' in str(title) or 'Bisness' in str(title) or 'Manag' in str(title) or 'buis' in str(title) or 'Entrepreneur' in str(title) or 'entrepr' in str(title).lower() or 'managment' in str(title).lower() or 'Buis' in str(title) or 'Busni' in str(title) or 'Mana' in str(title) or 'buss' in str(title).lower() or 'Bi' in str(title) or 'Mgt' in str(title) or 'MBA' in str(title) or 'Mgmt' in str(title) or 'MD' in str(title):
        return 'Business/Management'
    elif 'information technology' in str(title).lower() or 'IT' in str(title) or 'it' in str(title):
        return 'I.T'
    elif 'math' in str(title).lower() or 'LOGISTICS' in str(title) or 'st' in str(title).lower() or 'marh' in str(title).lower() or 'Mate' in str(title):
        return 'Mathematics'
    elif 'computer' in str(title).lower():
        return 'I.T'
    elif 'bio' in str(title).lower() or 'Plant' in str(title) or 'plant' in str(title).lower() or 'Micro' in str(title):
        return 'Biology'
    elif 'tesl' in str(title).lower() or 'TES' in str(title) or 'Teso' in str(title) or 'Enhlish' in str(title):
        return 'English'
    elif 'account' in str(title).lower() or 'Accoun' in str(title) or 'Acc' in str(title) or 'acc' in str(title).lower() or 'Acouunt' in str(title) or 'Acvount' in str(title) or 'Count' in str(title):
        return 'Accountacy'
    elif 'CA' in str(title):
        return 'CA'
    elif 'none' in str(title).lower() or '0' in str(title) or  '_' in str(title) or '.' in str(title) or 'Nine' in str(title) or '19' in str(title):
        return 'No Degree'
    elif 'nurs' in str(title).lower() or 'BSN' in str(title):
        return 'Nursing'
    elif '-' in str(title).lower() or 'NIL' in str(title):
        return 'No Degree'
    elif 'teach' in str(title).lower() or 'Lect' in str(title) or 'eet' in str(title).lower():
        return 'Teaching'
    elif 'pharma' in str(title).lower() or 'medic' in str(title).lower() or 'med' in str(title).lower() or 'hospi' in str(title).lower() or 'Mwdicine' in str(title) or 'Farmacy' in str(title) or 'Pharacology' in str(title) or 'farmasi' in str(title).lower() or 'Farmasy' in str(title):
        return 'Pharmacy/Medical'
    elif 'doctor' in str(title).lower() or  'MBBS' in str(title) or 'Mbbs' in str(title) or 'Surge' in str(title) or 'surge' in str(title) or 'mbbs' in str(title).lower()or 'dermat' in str(title).lower() or 'Podiat' in str(title) :
        return 'Doctor'
    elif 'no' in str(title).lower() or 'Undec' in str(title) or 'Idk' in str(title) or 'idk' in str(title).lower() or 'Hahaha' in str(title) or 'never' in str(title).lower() or 'T' in str(title) or 'Good' in str(title):
        return 'No Degree'
    elif 'film' in str(title).lower() or 'Cinema' in str(title) or 'fil' in str(title).lower() or 'Adver' in str(title) or 'adver' in str(title) or 'Act' in str(title) or 'Enter' in str(title) or 'digital' in str(title).lower() or 'cinema' in str(title).lower() or 'Video' in str(title) or 'Direct' in str(title) or 'Theat' in str(title) or 'Radio' in str(title) or 'theat' in str(title).lower() or 'drama' in str(title).lower():
        return 'Media'
    elif 'international' in str(title).lower() or 'Internatianal' in str(title):
        return 'International Relations'
    elif 'human' in str(title).lower() or 'hr' in str(title).lower() or 'Hs' in str(title) or 'Hm' in str(title) or 'Humam' in str(title):
        return 'Human Resources'
    elif 'art' in str(title).lower() or 'Painting' in str(title) or 'Drawing' in str(title) or 'ba' in str(title) or 'Printing' in str(title) or 'las' in str(title).lower() or 'Ma' in str(title) or 'paint' in str(title).lower() or 'creative' in str(title).lower() or 'AA' in str(title) or 'BA' in str(title):
        return 'Arts'
    elif 'islam' in str(title).lower() or 'Muamalat' in str(title) or 'Quran' in str(title) or 'Halal' in str(title) or 'Usul' in str(title) or 'Zakat' in str(title) or 'usul' in str(title).lower():
        return 'Islamic Studies'
    elif 'physio' in str(title).lower() or 'fis' in str(title).lower():
        return 'Physiotherapy'
    elif 'socio' in str(title).lower() or 'social' in str(title).lower() or 'soical' in str(title).lower() or 'Sis' in str(title) or 'Sosio' in str(title) or 'Sicio' in str(title) or 'sosiality' in str(title).lower():
        return 'Sociology'
    elif 'bank' in str(title).lower():
        return 'Banking'
    elif 'agri' in str(title).lower():
        return 'Agriculture'
    elif 'Market' in str(title) or 'Finan' in str(title) or 'finance' in str(title).lower() or 'MARKETING' in str(title) or 'market' in str(title).lower() or 'retail' in str(title).lower() or 'CMP' in str(title) or 'Merket' in str(title):
        return 'Marketing/Finance'
    elif 'counsel' in str(title).lower() or 'cauns' in str(title) or 'Kaunseling' in str(title) or 'kaunseling' in str(title) or 'Caunsel' in str(title):
        return 'Counselling'
    elif 'programming' in str(title).lower() or 'coding' in str(title).lower() or 'Ibm' in str(title) or 'ceit' in str(title) or 'Hacking' in str(title):
        return 'I.T'
    elif 'civil' in str(title).lower() or 'comp' in str(title).lower() or 'Mechanical' in str(title) or 'Electrical' in str(title) or 'Mechatronics' in str(title) or 'Eee' in str(title) or 'cs' in str(title).lower() or 'mecha' in str(title) or 'Chemical' in str(title) or 'chemical' in str(title) or 'tech' in str(title) or 'ec' in str(title).lower() or 'egineering' in str(title).lower() or 'manufacturing' in str(title).lower():
        return 'Engineering'
    elif 'ict' in str(title).lower() or 'developer' in str(title).lower() or 'I.T' in str(title) or 'CAE&D' in str(title) or 'It' in str(title):
        return 'I.T'
    elif 'commu' in str(title).lower() or 'comm' in str(title).lower() or 'com' in str(title).lower() or 'Conmunication' in str(title):
        return 'Communications'
    elif 'administration' in str(title).lower() or 'admin' in str(title).lower():
        return 'Administration'
    elif 'psycho' in str(title).lower() or 'psy' in str(title).lower() or 'Clinical osychology' in str(title) or 'hschology' in str(title) or 'Pysch' in str(title) or 'pys' in str(title).lower() or 'Pych' in str(title) or 'pscy' in str(title) or 'payc' in str(title).lower() or 'Phyc' in str(title) or 'psicologia' in str(title) or 'Phsychology' in str(title) or 'Phichology' in str(title) or 'psuchology' in str(title) or 'Pschology' in str(title) or 'psikologi' in str(title).lower():
        return 'Psychology'
    elif 'english' in str(title).lower() or 'Elglish' in str(title) or 'esl' in str(title).lower() or 'Emg' in str(title) or 'emglisj' in str(title).lower():
        return 'English'
    elif 'law' in str(title).lower() or 'BBA' in str(title) or 'llb' in str(title) or 'lew' in str(title).lower() or 'kaw' in str(title).lower() or 'enforcement' in str(title).lower() or 'Kaw' in str(title):
        return 'Law'
    elif 'engineering' in str(title).lower() or 'engi' in str(title).lower() or 'eng' in str(title).lower() or 'Software' in str(title) or 'soft' in str(title).lower() or 'mechanical' in str(title).lower() or 'Egineeering' in  str(title) or 'electronic' in str(title).lower() or 'CE' in str(title) or 'mech' in str(title).lower() or 'Ciclvil' in str(title) or 'Eggineering' in str(title) or 'Tech' in str(title) or 'Teol' in str(title) or 'EEE' in str(title) or 'PE' in str(title):
        return 'Engineering'
    elif 'architecture' in str(title).lower() or 'aechitecture' in str(title).lower() or 'archirecture' in str(title).lower() or 'architect' in str(title).lower() or 'Arsitechture' in str(title) or 'Building' in str(title) or 'building' in str(title).lower() or 'Arc' in str(title):
        return 'Architecture'
    elif 'design' in str(title).lower() or 'Desig' in str(title) or 'Dssign' in str(title):
        return 'Designer'
    elif 'science' in str(title).lower() or 'Sceince' in str(title) or 'Sci' in str(title) or 'sciene' in str(title) or 'BS' in str(title):
        return 'Pure Sciences'
    elif 'physics' in str(title).lower() or 'Phsyics' in str(title) or 'EMC' in str(title) or 'Physic' in str(title) or 'physi' in str(title):
        return 'Physics'
    elif 'chemistry' in str(title).lower() or 'CIS' in str(title) or 'Chem' in str(title):
        return 'Chemistry'
    elif 'french' in str(title).lower() or 'Fr' in str(title):
        return 'French'
    elif 'religi' in str(title).lower() or 'Relegion' in str(title) or 'Rel' in str(title) or 'Hukum' in str(title) or 'Sains' in str(title):
        return 'Religious Studies'
    elif title=='&#1593;&#1604;&#1605; &#1606;&#1601;&#1587;' or title=='&#22810;&#23186;&#39636;&#35373;&#35336;' or title=='nil' or title=='drop out' or title=='&#1055;&#1089;&#1080;&#1093;&#1086;&#1083;&#1' or title=='75' or title=='Secondary education' or title=='Thiê&#769;t kê&#769; &#273;ô&#768; ho&#803;a' or title=='18' or title=='ongoing' or title=='&#28888;&#22521;' or title=='lol' or title=='In college currently' or title=='secondary education' or title=='Dropped out' or title=='na' or title=='didnt attend' or title=='im going on the next year. ' or title=='&#304;lahiyat' or title=='lmfao, im 15' or title=='Elem Ed' or title=='yes' or title=='N/a' or title=='/' or title=='???' or title=='cocaine 101' or title=='doesnt matter' or title== 'oooo' or title=='G' or title=='Yes' or title=='Na' or title=='Na 'or title=='Want sure':
        return 'No Degree'
    elif 'Music' in str(title) or 'Dance' in str(title) or 'danc' in str(title).lower() or 'Vocational' in str(title) or 'Muisc' in str(title) or 'music' in str(title).lower() or 'Performance' in str(title):
        return 'Music/Dance'
    elif 'pol' in str(title).lower() or 'Govern' in str(title) or 'Right' in str(title):
        return 'Politics'
    elif 'photo' in str(title).lower() or 'Foto' in str(title) or 'Photo' in str(title):
        return 'Photography'
    elif 'Television' in str(title) or 'telev' in str(title).lower():
        return 'Television'
    elif 'bahasa' in str(title).lower() or 'Bahasa' in str(title) or 'Malay' in str(title) or 'malay' in str(title).lower():
        return 'Malaysian languages'
    elif 'Urban' in str(title) or 'Town' in str(title) or 'town' in str(title).lower() or 'planning' in str(title) or 'Plann' in str(title) or 'development' in str(title):
        return 'Economic Developments'
    elif 'Public' in str(title) or 'public' in str(title).lower():
        return 'Public Relations'
    elif 'Writing' in str(title) or 'writing' in str(title).lower() or 'Screenwritinf' in str(title) or 'Author' in str(title):
        return 'Writing/Author'
    elif 'philosophy' in str(title).lower() or 'Phil' in str(title) or 'philos' in str(title).lower() or 'Filo' in str(title) or 'Phylosophy' in str(title):
        return 'Philosophy'
    elif 'Actua' in str(title):
        return 'Acturial Studies'
    elif 'DENTALWORKS' in str(title) or 'dental' in str(title) or 'Dental' in str(title) or 'Odont' in str(title):
        return 'Dentist'
    elif 'beaut' in str(title).lower() or 'Fashion' in str(title) or 'make' in str(title) or 'fashion' in str(title).lower() or 'hair' in str(title).lower() or 'cosmet' in str(title).lower():
        return 'Fashion'
    elif 'Health' in str(title) or 'health' in str(title).lower() or 'wellness' in str(title).lower() or 'Healtcare' in str(title):
        return 'Healthcare'
    elif 'Language' in str(title) or 'lang' in str(title).lower() or 'Laq' in str(title):
        return 'Languages'
    elif 'cook' in str(title).lower() or 'bakery' in str(title).lower() or 'Bak' in str(title) or 'CULINARY' in str(title) or 'Food' in str(title) or 'food' in str(title) or 'chef' in str(title).lower() or 'Cul' in str(title) or 'Patiss' in str(title) or 'culi' in str(title).lower():
        return 'Cookings'
    elif 'Hotel' in str(title) or 'hotel' in str(title).lower() or 'food service' in str(title) or 'cater' in str(title).lower():
        return 'Hotel Management'
    elif 'therapy' in str(title).lower() or 'ot' in str(title).lower() or 'theraphy' in str(title):
        return 'Therapeutical Studies'
    elif 'veter' in str(title).lower() or 'Veter' in str(title) or 'Vet' in str(title):
        return 'Veterinary'
    elif 'Survey' in str(title) or 'survey' in str(title) or 'serveyors' in str(title).lower() or 'Qs' in str(title) or 'SURVEYING' in str(title) or 'QS' in str(title) or 'Surver' in str(title):
        return 'Surveyour Studies'
    elif 'Aircraft' in str(title) or 'aircraft' in str(title).lower() or 'aircr' in str(title).lower() or 'aviation' in str(title).lower() or 'Aero' in str(title) or 'navigation' in str(title).lower():
        return 'Aircrafts'
    elif 'environment' in str(title).lower() or 'Environment' in str(title) or 'envi' in str(title).lower():
        return 'Environmental Educations'
    elif 'Syariah' in str(title) or 'syariah' in str(title):
        return 'Syrian Languages'
    elif 'judicial' in str(title).lower() or 'juri' in str(title).lower() or 'legal' in str(title).lower():
        return 'Judicial Studies'
    elif 'Liter' in str(title) or 'literature' in str(title) or 'litt' in str(title).lower():
        return 'Literature'
    elif 'child' in str(title).lower() or 'Child' in str(title) or 'Preschool' in str(title):
        return 'Child Educations'
    elif 'Tour' in str(title) or 'tour'  in str(title).lower():
        return 'Tourisms'
    elif 'Gam' in str(title) or 'game' in str(title).lower():
        return 'Gaming'
    elif 'education' in str(title).lower() or 'Education' in str(title) or 'ed' in str(title).lower() or 'acad' in str(title) or 'Dploma' in str(title):
        return 'B.Ed or M.Ed'
    elif 'Sport' in str(title) or 'sport' in str(title).lower():
        return 'Sports'
    elif 'Petro' in str(title):
        return 'Petroleum'
    elif 'Journ' in str(title) or 'jour' in str(title).lower() or 'Joun' in str(title) or 'Jurn' in str(title):
        return 'Journalism'
    elif 'Mandarin' in str(title):
        return 'Chinese/Mandarin Languages'
    elif 'Electrician' in str(title):
        return 'Electrician'
    elif 'Network' in str(title) or 'network' in str(title).lower():
        return 'Networking'
    elif 'geo' in str(title).lower() or 'GEO' in str(title):
        return 'Geography'
    elif 'Librarian' in str(title) or 'lib' in str(title).lower():
        return 'Librarian'
    elif 'Mission' in str(title) or 'mission' in str(title).lower():
        return 'Missionary Studies'
    elif 'Forensic' in str(title) or 'foren' in str(title).lower() or 'Crime' in str(title) or 'crim' in str(title).lower():
        return 'Forensic/Criminal studies'
    elif 'Animation' in str(title) or 'animation' in str(title).lower() or 'imag' in str(title) or 'graphic' in str(title) or 'Graphic' in str(title):
        return 'Animations'
    elif 'aqua' in str(title).lower() or 'Aqu' in str(title):
        return 'Aquaculture'
    elif 'soldier' in str(title).lower() or 'lwa' in str(title).lower() or 'defence' in str(title):
        return 'Army'
    elif 'Kinesi' in str(title) or 'kines' in str(title).lower() or 'hod' in str(title):
        return 'Human Kinetics'
    elif 'Horti' in str(title) or 'horti' in str(title) or 'Landscape' in str(title):
        return 'Horticulture'
    elif 'commerce' in str(title).lower() or 'Coome' in str(title):
        return 'Commerce'
    elif 'Speech' in str(title) or 'speech' in str(title).lower():
        return 'Speech Pathology'
    elif 'SECRET' in str(title) or 'secret' in str(title).lower():
        return 'Secretary'
    elif 'Animals' in str(title) or 'animal' in str(title).lower() or 'Pet' in str(title):
        return 'Animal Care'
    elif 'Organisation' in str(title) or 'organi' in str(title).lower():
        return 'Organizational Behaviour'
    elif 'event' in str(title).lower() or 'Event' in str(title):
        return 'Event Managment'
    elif 'radiology' in str(title).lower() or 'Radiography' in str(title) or 'radiograpghy' in str(title).lower() or 'Radiation' in str(title) or 'radiography' in str(title):
        return 'Radiography'
    elif 'nutrition' in str(title).lower() or 'Nutrition' in str(title):
        return 'Nutritionist'
    elif 'Audit' in str(title) or 'audit' in str(title).lower():
        return 'Auditing'
    elif 'Neuro' in str(title) or 'neuroligy' in str(title).lower():
        return 'Neurology'
    elif 'Anato' in str(title) or 'anat' in str(title).lower():
        return 'Anatomy'
    elif 'trade' in str(title).lower():
        return 'Trading'
    elif 'Interpre' in str(title) or 'translation' in str(title).lower():
        return 'Interpreter'
    elif 'audio' in str(title).lower() or 'Audio' in str(title):
        return 'Audiology'
    elif 'insurance' in str(title).lower() or 'Insurance' in str(title):
        return 'Insurances'
    elif 'archaeology' in str(title).lower() or 'archaeology' in str(title).lower() or 'archeology' in str(title).lower() or 'treasury' in str(title):
        return 'Archeology'
    elif 'SERV'in str(title) or 'service' in str(title).lower():
        return 'Service Training'
    elif 'GERMAN' in str(title) or 'german' in str(title).lower():
        return 'German'
    elif 'KOREAN' in str(title) or 'Korea' in str(title):
        return 'Korean'
    elif 'valuat' in str(title).lower() or 'valuer' in str(title).lower():
        return 'Registered Valuer'
    elif 'skil' in str(title).lower() or 'Skill' in str(title) or 'Professional' in str(title) or 'practical' in str(title).lower():
        return 'Skilled Labour'
    elif 'virology' in str(title):
        return 'Virology'
    elif 'lab' in str(title).lower() or 'Lab' in str(title) or 'MLT' in str(title):
        return 'Laboratory Worker'
    elif 'GENERAL' in str(title) or 'General' in str(title):
        return 'General'
    elif 'Opto' in str(title) or 'opto' in str(title).lower():
        return 'Optometry'
    elif 'Zoo' in str(title) or 'zoo' in str(title).lower():
        return 'Zoology'
    elif 'office' in str(title).lower() or 'Office' in str(title):
        return 'Office Skills'
    elif 'found' in str(title).lower() or 'Found' in str(title):
        return 'Foundation Education'
    elif 'general' in str(title).lower() or 'General' in str(title):
        return 'General Education'
    elif 'real estate' in str(title).lower() or 'property' in str(title).lower():
        return 'Realtor'
    elif 'Meteorology' in str(title) or 'Metrology' in str(title):
        return 'Meterology'
    elif 'operations' in str(title).lower() or 'Operation' in str(title):
        return 'Operational Managment'
    elif 'Merchandising' in str(title) or 'merchand' in str(title).lower():
        return 'Merchandising'
    elif 'Spanish' in str(title):
        return 'Spanish'
    elif 'Nature' in str(title) or 'natur' in str(title).lower():
        return 'Nature Conservation/Resources'
    elif title=='a level ' or title==' ':
        return 'No Degree'
    elif 'Corporate' in str(title) or 'corporate' in str(title).lower():
        return 'Corporate'
    elif 'greek' in str(title).lower() or 'Greek' in str(title):
        return 'Greek'
    elif 'Behaviour' in str(title) or 'Behavior' in str(title) or 'Organizational Behaviour' in str(title):
        return 'Behaviour Analysis'
    elif 'publish' in str(title).lower():
        return 'Publishing'
    elif 'Safety' in str(title) or 'safety' in str(title).lower():
        return 'Safety Training'
    elif 'genetic' in str(title).lower() or 'Genetic' in str(title):
        return 'Genetics'
    elif 'Dietetic' in str(title):
        return 'Dietician'
    elif 'Production' in str(title) or 'manufacturing' in str(title).lower():
        return 'Production And Manufacturing'
    elif 'Welding' in str(title):
        return 'Welding'
    elif 'Geron' in str(title):
        return 'Gerontology'
    elif 'Research' in str(title) or 'Ph D' in str(title):
        return 'Ph.D'
    elif 'arabic' in str(title).lower() or 'Arabic' in str(title):
        return 'Arabic'
    else:
        return title

# if major has np.nan then fill with 'No Degree' value
depression['major'].fillna('No Degree', inplace=True)
depression['major'] = depression['major'].apply(changeMajorValues)

depression['major'].value_counts()

plt.figure(figsize=(18, 7))
depression['major'].value_counts()[:20].plot(kind = 'barh')
# sns.countplot(x=depression['major'], orient='v')

depression.drop('major', inplace=True, axis=1)
depression.head()

'''
Urban Feature Values:
    1=Rural (country side), 
    2=Suburban, 
    3=Urban (town, city)
    0=None
'''

# change 0 to 3 value as it's the most used one
depression['urban'] = depression['urban'].map({0: 3, 1: 1, 2: 2, 3: 3})

def changeUrbanValues(value):
    if value == 1:
        return 'Rural (country side)'
    if value == 2:
        return 'Suburban'
    if value == 3:  # if value is 0 means user don't entered this value and we assume he is urban as most records are
        return 'Urban (town, city)'
    return value 

urban = depression['urban'].apply(changeUrbanValues)

plt.figure(figsize=(16, 8))
sns.countplot(x=depression['urban'], hue= urban)

'''
Gender Feature Values
    0=None
    1=Male, 
    2=Female, 
    3=Other
'''

# change value 0 to 2 as female are most recorded in depressionset
depression['gender'] = depression['gender'].map({0: 2, 1: 1, 2: 2, 3: 3})

def changeGenderValue(value):
    if value == 1:
        return 'Male'
    if value == 2 or value == 0: # value = 0 means user didn't enter this value, we assume it's female as most records are
        return 'Female'
    return 'Other' # if 3 or 0 return other as value

gender = depression['gender'].apply(changeGenderValue)

plt.figure(figsize=(18, 7))
sns.countplot(x = depression['gender'], hue=gender)


# change 0 value to 12 as it's ohter value for people who didn't enter value to this field
def updateEducationValue(value):
    if value == 0: 
        return 12
    return value

depression['religion'] = depression['religion'].apply(updateEducationValue)

def changeReliginValues(value) -> str:
    if value == 0:
        return 'Other'
    if value == 1:
        return 'Agnostic'
    if value == 2:
        return 'Atheist'
    if value == 3:
        return 'Buddhist'
    if value == 4:
        return 'Christian (Catholic)'
    if value == 5:
        return 'Christian (Mormon)'
    if value == 6:
        return '=Christian (Protestant)'
    if value == 7:
        return 'Christian (Other)'
    if value == 8:
        return 'Hindu'
    if value == 9:
        return 'Jewish'
    if value == 10:
        return 'Muslim'
    if value == 11:
        return 'Sikh'
    if value == 12:
        return 'Other'
    return value

religin = depression['religion'].apply(changeReliginValues)

# show value counts of religin depression
display(depression['religion'].value_counts())

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['religion'], hue= religin)
    

# divide values by 10
depression['race'] = depression['race'].apply(lambda x: x/10)
depression['race'].head()

def changeRaceValues(value)->str: 
    if value == 1:
        return 'Asian'
    if value == 2:
        return 'Arab'
    if value == 3:
        return 'Black'
    if value == 4:
        return 'Indigenous Australian'
    if value == 5:
        return 'Native American'
    if value == 6:
        return 'White'
    if value == 7:
        return 'Other'

    return value

race = depression['race'].apply(changeRaceValues)

# show value counts of race
display(depression['race'].value_counts())

# show some Viz
plt.figure(figsize=(18, 7))
sns.countplot(x=depression['race'], hue=race)

depression.head()

depression['TIPI1'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
def changeFromToinTIPI(value, From, to):
    if value == From:
        return to
    return value

depression['TIPI1'] = depression['TIPI1'].apply(lambda value: changeFromToinTIPI(value, 0, 5))

def changeTIPIValues(value):
    if value == 1:
        return 'Disagree strongly'
    if value == 2:
        return 'Disagree moderately'
    if value == 3:
        return 'Disagree a little'
    if value == 4:
        return 'Neither agree nor disagree'
    if value == 5:
        return 'Agree a little'
    if value == 6:
        return 'Agree moderately'
    if value == 7:
        return 'Agree strongly'

    return value

tipi = depression['TIPI1'].apply(changeTIPIValues)


plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI1'], hue=tipi)

depression['TIPI2'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI2'] = depression['TIPI2'].apply(lambda value: changeFromToinTIPI(value, 0, 5))

# convert numbers to string for better viz
tipi = depression['TIPI2'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI2'], hue=tipi)

depression['TIPI3'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI3'] = depression['TIPI3'].apply(lambda value: changeFromToinTIPI(value, 0, 6))

# convert numbers to string for better viz
tipi = depression['TIPI3'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI3'], hue=tipi)



depression['TIPI4'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI4'] = depression['TIPI4'].apply(lambda value: changeFromToinTIPI(value, 0, 6))

# convert numbers to string for better viz
tipi = depression['TIPI4'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI4'], hue=tipi)

depression['TIPI5'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI5'] = depression['TIPI5'].apply(lambda value: changeFromToinTIPI(value, 0, 6))

# convert numbers to string for better viz
tipi = depression['TIPI5'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI5'], hue=tipi)

depression['TIPI6'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI6'] = depression['TIPI6'].apply(lambda value: changeFromToinTIPI(value, 0, 7))

# convert numbers to string for better viz
tipi = depression['TIPI6'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI6'], hue=tipi)

depression['TIPI7'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI7'] = depression['TIPI7'].apply(lambda value: changeFromToinTIPI(value, 0, 6))

# convert numbers to string for better viz
tipi = depression['TIPI7'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI7'], hue=tipi)

depression['TIPI8'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI8'] = depression['TIPI8'].apply(lambda value: changeFromToinTIPI(value, 0, 5))

# convert numbers to string for better viz
tipi = depression['TIPI8'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI8'], hue=tipi)

depression['TIPI9'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI9'] = depression['TIPI9'].apply(lambda value: changeFromToinTIPI(value, 0, 4))

# convert numbers to string for better viz
tipi = depression['TIPI9'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI9'], hue=tipi)

depression['TIPI10'].value_counts()

# change 0 value to 5 as it's the most chosen value in the survey
depression['TIPI10'] = depression['TIPI10'].apply(lambda value: changeFromToinTIPI(value, 0, 4))

# convert numbers to string for better viz
tipi = depression['TIPI10'].apply(changeTIPIValues)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['TIPI10'], hue=tipi)

depression['familysize'].value_counts()

plt.figure(figsize=(18, 5))
sns.distplot(x=depression['familysize'])

# remove reocrds that has family size more than 13
indexes = depression[depression['familysize'] > 13].index

# reomve these indexes from dataframe
print(f'Depression size before: {depression.shape[0]}')
depression = depression.drop(indexes, axis=0)
print(f'Depression size after: {depression.shape[0]}')

plt.figure(figsize=(18, 5))
sns.distplot(x=depression['familysize'])

depression['married'].value_counts()

def change0to1inMarried(value):
    if value == 0:
        return 1
    return value

# change 0 to 1 value as it is the most answered one
depression['married'] = depression['married'].apply(change0to1inMarried)

def changeMarriedValueToString(value):
    if value == 1:
        return 'Never married'
    if value == 2:
        return 'Currently married'
    if value == 3:
        return 'Previously married'
    return value

# change numbers to strings for better viz
married = depression['married'].apply(changeMarriedValueToString)


plt.figure(figsize=(18, 7))
sns.countplot(x=depression['married'], hue=married)

depression.head()

display(depression['age'].value_counts())

# show viz
plt.figure(figsize=(18, 7))
sns.boxenplot(x=depression['age']) 

# remove age > 80 years old

age_indexes = depression[depression['age'] > 80]['age'].index

display(age_indexes) # figure out how many

# remove these indexes
print(f'Depression size before: {depression.shape[0]}')
depression.drop(age_indexes, axis=0, inplace=True) 
print(f'Depression size after: {depression.shape[0]}') 


# show viz
plt.figure(figsize=(18, 7))
sns.boxenplot(x=depression['age']) 

def makeAgeGroup(value):
    if value <= 10:
        return 'Under 10'
    if  10 <= value <= 16:
        return 'Primary Children'
    if 17 <= value <= 21:
        return 'Secondary Children'
    if 21 <= value <= 35:
        return 'Adults' 
    if 36 <= value <= 48:
        return 'Elder Adults'
    if value >= 49:
        return 'Older People'

age = depression['age'].apply(makeAgeGroup)

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['age'], hue=age)

# create age_group feature
def makeAgeGroupFeature(value):
    if value <= 10:
        return 1
    if  10 <= value <= 16:
        return 2
    if 17 <= value <= 21:
        return 3
    if 21 <= value <= 35:
        return 4 
    if 36 <= value <= 48:
        return 5
    if value >= 49:
        return 6

depression['age_group'] = depression['age'].apply(makeAgeGroupFeature)

depression.head()

depression.drop('age', axis=1, inplace=True)
depression.head()

depression['total_count']  = depression.sum(axis=1)
depression.head()

depression['total_count'].describe()

plt.figure(figsize=(18, 7))
sns.distplot(x=depression['total_count'])

depression['total_count'].describe()

# let's divide the values under 170 to split moderate to another values
depression[depression['total_count'] < 170]['total_count'].describe()

# let's divide the values under 147 to split Mild to another value
depression[depression['total_count'] < 147]['total_count'].describe()

# let's divide the values above 170 to split moderate to another values
depression[depression['total_count'] > 170]['total_count'].describe()

def buildTarget(value):
    if value <= 133:
        return 'Normal'
    if 133 < value <= 147:
        return 'Mild'
    if 147 < value <= 170:
        return 'Moderate'
    if 170 < value <= 194:
        return 'Severe'
    if value > 194:
        return 'Extremely Severe'

    
# build target feature
depression['target'] = depression['total_count'].apply(buildTarget)

depression.head()

plt.figure(figsize=(18, 7))
sns.countplot(x=depression['target'])

def buildTargetMove15Steps(value):
    if value <= 143:
        return 'Normal'
    if 143 < value <= 157:
        return 'Mild'
    if 157 < value <= 180:
        return 'Moderate'
    if 180 < value <= 204:
        return 'Severe'
    if value > 204:
        return 'Extremely Severe'

    
# build target feature
depression['target'] = depression['total_count'].apply(buildTargetMove15Steps)

# Let's visualize to see
plt.figure(figsize=(18, 7))
sns.countplot(x=depression['target'])

depression.head()

print(depression.columns)

# splitting attributes and target
target = depression['target']
depression.drop(['target', 'total_count'], axis=1, inplace=True)

# splitting training and testing dataset into 80% and 20% respectively

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(depression, target, test_size=.2)
print(f'x_train: {x_train.shape}, y_train: {y_train.shape}')
print(f'x_test: {x_test.shape}, y_test: {y_test.shape}')

#preprocessing : scaling
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

from sklearn import metrics

#model 1: Random Forest
from sklearn.ensemble import RandomForestClassifier 
rnd_clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=SEED) #importing model
rnd_clf.fit(x_train_scaled, y_train) #training
rnd_clf.score(x_test_scaled, y_test)

y_pred_rnd = rnd_clf.predict(x_test_scaled) #prediction

"""from sklearn.metrics import confusion_matrix #prediction's accuracy and error
confusion_matrix(y_test, y_pred_rnd) 

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_rnd)) #prediction's accuracy and error
"""
print("Random Forest Accuracy:", metrics.accuracy_score(y_test,y_pred_rnd)*100)

#model 2: SVM Model
from sklearn.svm import SVC
svc_clf = SVC() #importing model
svc_clf.fit(x_train_scaled, y_train) #training
"""
# Cross Validation
from sklearn.model_selection import cross_val_score
cross_score = cross_val_score(svc_clf, x_train_scaled, y_train, cv=5) #import model
print(f'Mean Score {np.mean(cross_score)}')

svc_clf.score(x_test_scaled, y_test)
"""
y_pred_svc = svc_clf.predict(x_test_scaled) #prediction
print("Accuracy by SVM",metrics.accuracy_score(y_test,y_pred_svc)*100)

#model 3: kNN Algorithm
from sklearn.neighbors import KNeighborsClassifier
kn_clf=KNeighborsClassifier(n_neighbors=199,metric='euclidean') #import model
kn_clf.fit(x_train_scaled,y_train) #training
y_pred_kn=kn_clf.predict(x_test_scaled) #prediction
print("Accuracy by kNN",metrics.accuracy_score(y_test, y_pred_kn)*100) #accuracy and error

#model 4: Naive Bayes
from sklearn.naive_bayes import GaussianNB  
nby_clf= GaussianNB()  #importing model
nby_clf.fit(x_train, y_train)  #training
y_pred_nby=nby_clf.predict(x_test_scaled) #prediction
print("Accuracy by Naive Bayes",metrics.accuracy_score(y_test, y_pred_nby)*100) #accuracy and error

# this method used to build random values to use it for testing the model
def buildRandomValuesForPrediction():
    # get random answers for Q1A to Q42A questions
    qaAnswers = []
    for i in range(1, 43):
        qaAnswers.append(np.random.randint(1, 5)) # random from 1 to 4
    # get random answers for TIPI1 to TIPI questions
    tipiAnswers = []
    for i in range(1, 11):
        tipiAnswers.append(np.random.randint(1, 8)) # random from 1 to 7
    education = np.random.randint(1, 5) # random from 1 to 4
    urban = np.random.randint(1, 4) # random from 1 to 3
    gender = np.random.randint(1, 4) # random from 1 to 3
    religion = np.random.randint(1, 13) # random from 1 to 12
    race = np.random.randint(1, 8) # random from 1 to 7
    married = np.random.randint(1, 4) # random from 1 to 3
    familysize = np.random.randint(1, 21) # random from 1 to 20 
    age_group = np.random.randint(1, 7) # random from 1 to 6
    return np.array([*qaAnswers, *tipiAnswers, education, urban, gender, religion, race, married, familysize, age_group])

"""#PREDICTION PART BY DIFFERENT  ALGOS
# make prediction couple of times
for i in range(1, 10): #means model test results for 10 sets of generated data
    answers = buildRandomValuesForPrediction() #data values for testing purposes
    answers_scaled = scaler.transform([answers]) #preprocessing
    print(f'*********** Iteration {i} *************') #one set or record is tested in every iteration
    print(f'Test Values: {answers}') #prints tranformed data
    print(f'Prediction by random forest ===> {rnd_clf.predict(answers_scaled)}') #prediction by random forest
    print(f'Prediction by svc model ===> {svc_clf.predict(answers_scaled)}') #prediction by svc model
    print(f'Prediction by kNN model ===> {kn_clf.predict(answers_scaled)}') #prediction by kNN model
    print(f'Prediction by Naive Bayes Model ===> {nby_clf.predict(answers_scaled)}\n') #prediction by naive bayes model
    
#Result is in 5 categories,i.e.,"moderate","severe","Normal","Mild","Moderate","Severe","Extremely Severe"
import pickle, os
if not os.path.exists('./models'): # create models directory
    os.mkdir('models')

# Saving Models
pickle.dump(svc_clf, open('models/svc_model.h5', 'wb')) # Model 1
pickle.dump(rnd_clf, open('models/randomForest.h5', 'wb')) # Model 2
#Model 3
#Model 4
#Model 5
"""

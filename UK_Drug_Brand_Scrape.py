import bs4,requests,os,re
import pandas as pd

search_url='https://www.medicines.org.uk/emc/search?q='
reg=re.compile(r'.+?(?= \d|$)')

def get_drugs(drug):
    wp=requests.get(search_url+drug)
    page=bs4.BeautifulSoup(wp.text,features='html.parser')
    return [i.find('h2').text for i in page.findAll('div',{'class':'row data-row'})]





drugs={'Antidepressants': ['fluoxetine', 'sertraline', 'paroxetine', 'fluvoxamine', 'citalopram', 'escitalopram', 'bupropion', 'trazadone', 'trazodone', 'desvenlafaxine', 'duloxetine', 'venlafaxine'],
       'Stimulants': ['methylphenidate', 'dexmethylphenidate', 'dextroamphetamine', 'lisdexamfetamine', 'amphetamine', 'atomoxetine'],
       'Antiepileptics': ['lamotrigine',  'oxcarbazepine', 'topiramate', 'clonazepam', 'levetiracetam', 'carbamazepine', 'valproic acid', 'phenobarbital',
                          'gabapentin', 'pregabalin'],
       'Beta-2 agonists': ['albuterol', 'levalbuterol', 'formoterol', 'salmeterol'],
       'Macrolides': ['azithromycin', 'clarithromycin'],
        'Proton pump inhibitors': ['esomeprazole', 'lansoprazole', 'omeprazole', 'pantoprazole'],
       'Antibiotics': ['amoxicillin', 'penicillin', 'cefdinir', 'cephalexin', 'ceftriaxone', 'cefprozil', 'cefuroxime', 'cefixime', 'cefadroxil',
                        'azithromycin', 'erythromycin', 'clindamycin', 'clarithromycin', 'ciprofloxacin', 'metronidazole', 'nitrofurantoin']}

manual=['divalproex sodium', 'amphetamine/dextroamphetamine','erythromycin (oral only)', 'amoxicillin-clavulanate','sulfamethoxazole-trimethoprim']







ind_drugs=dict()
for i in drugs:
    for drug in drugs[i]:
        print(i,drug)
        ind_drugs[drug]=get_drugs(drug)



for i in list(ind_drugs):
    for x in ind_drugs[i]:
        ind_drugs[i][ind_drugs[i].index(x)]=x.rstrip('\n')


    
for i in ind_drugs:
	for x in ind_drugs[i]:
		reg.search(x)

ind2=dict()
for i in ind_drugs:
    ind2[i]=[]
    for x in ind_drugs[i]:
        ind2[i].append(reg.search(x).group().lower())
    ind2[i]=set(ind2[i])
    print(i,ind2[i])

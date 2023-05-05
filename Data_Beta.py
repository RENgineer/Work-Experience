import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import math
import sys
import os
from os import walk,listdir
import time

#create a list to hold all of the names of the data files within the folder
files_list = []

#change the name of the path depending on the location of the files
files_path = "/Users/RenOnly./Documents/RyskAlign_BETA/"
directory = os.listdir(files_path)

#loop through all the files in the named folder
for filename in directory:
    if ".csv" in filename:
        files_list.append(filename)
    #    stem_name = filename.replace(".csv",'')
    #    files_list.append(stem_name)
    #    print(stem_name)
        
#instantiate empty counters for the summation of all the entities from each file
ent_count=[0,0,0,0,0]
true_match_lst_7=[0,0,0,0,0]
false_pos_lst_7=[0,0,0,0,0]
true_match_lst_8=[0,0,0,0,0]
false_pos_lst_8=[0,0,0,0,0]

#loop through all of the files within the files_list list to collect all the data
#reference the import file using the path used to locate it (may be found by using the File Explorer)
#Note: the extension of the original file is ".xlsx". 
#Note:The path has to be relative to where the file is located on the client system. 
#Note: If accessing the path from a Windows computer, use backslashes instead of forward slashes.
datalen=0
data_cnt_true=0
for file in range(len(files_list)):
    datafile = files_path+files_list[file]
    #print(datafile)

#name the columns accordingly using their existing headers or give them new names
#columns = ["MID","Age (Days)", "Charge Value", "Charge Type", "Charge Level", "Convicted? Y'/N", \
#           "Incident Reported Date"]

#read in data from the file using pandas into a DataFrame. 'usecols' references the columns being used
#Note: the 'read_csv' method works for CSV files, whereas the 'read_excel' method works for Excel files
    dataframe=pd.read_csv(datafile, usecols=[1,2,7,9,11,12,13,14,24], index_col=False, na_filter=False)

#**a field may be appended to each record to determine whether a false positive or true match is identified**
#(column 18 omitted)

#truncate the dataframe based on the number of entries per file into the new df_trunc variable
    df_trunc=[]
    df_checklist=[]
    for record in range(len(dataframe)):
        if '3' in dataframe.loc[record][0]:
            #print(dataframe.loc[record][0])
            if not list(dataframe.loc[record]) in df_checklist:
                df_checklist.append(list(dataframe.loc[record]))
                df_trunc.append(dataframe.loc[record])
    #print(len(df_trunc),'ldftrunc')

#drop the 'd' from the number of days column in the original file
    int_list=['0','1','2','3','4','5','6','7','8','9']
    for rec in range(len(df_trunc)):
        num_days=''
        for num in range(len(df_trunc[rec][7])):
            if df_trunc[rec][7][num] in int_list:
                num_days=num_days+df_trunc[rec][7][num]
        df_trunc[rec][7]=num_days
    
    #print(df_trunc[-1])
    prev_datalen=len(df_trunc)
    datalen+=len(df_trunc)
    data_cnt=0
#sort data based on specific characteristics, then count false positives and true matches for each entity type
    for ent in range(len(df_trunc)):
        if df_trunc[ent][8]=='Sole Prop' or df_trunc[ent][8]=='Sole Proprietor':
            ent_count[0]+=1
            if df_trunc[ent][2]=='7' or int(df_trunc[ent][2]) == 7:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=1825:
                        false_pos_lst_7[0]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_7[0]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_7[0]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='8' or int(df_trunc[ent][2]) == 8:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=int(3652):
                        false_pos_lst_8[0]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[0]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[0]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='9' or int(df_trunc[ent][2]) == 9:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=int(3652):
                        false_pos_lst_8[0]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[0]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[0]+=1
                    data_cnt+=1
        elif df_trunc[ent][8]=='LLC':
            ent_count[1]+=1
            if df_trunc[ent][2]=='7' or int(df_trunc[ent][2]) == 7:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=1825:
                        false_pos_lst_7[1]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_7[1]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_7[1]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='8' or int(df_trunc[ent][2]) == 8:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=3652:
                        false_pos_lst_8[1]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[1]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[1]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='9' or int(df_trunc[ent][2]) == 9:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=int(3652):
                        false_pos_lst_8[1]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[1]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[1]+=1
                    data_cnt+=1
        elif df_trunc[ent][8]=='Association/Estate/Trust':
            ent_count[2]+=1
            if df_trunc[ent][2]=='7' or int(df_trunc[ent][2]) == 7:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=1825:
                        false_pos_lst_7[2]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_7[2]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_7[2]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='8' or int(df_trunc[ent][2]) == 8:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=3652:
                        false_pos_lst_8[2]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[2]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[2]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='9' or int(df_trunc[ent][2]) == 9:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=int(3652):
                        false_pos_lst_8[2]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[2]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[2]+=1
                    data_cnt+=1
        elif df_trunc[ent][8]=='Partnership':
            ent_count[3]+=1
            if df_trunc[ent][2]=='7' or int(df_trunc[ent][2]) == 7:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=1825:
                        false_pos_lst_7[3]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_7[3]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_7[3]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='8' or int(df_trunc[ent][2]) == 8:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=3652:
                        false_pos_lst_8[3]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[3]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[3]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='9' or int(df_trunc[ent][2]) == 9:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=int(3652):
                        false_pos_lst_8[3]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[3]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[3]+=1
                    data_cnt+=1
        elif df_trunc[ent][8]=='Corporation':
            ent_count[4]+=1
            if df_trunc[ent][2]=='7' or int(df_trunc[ent][2]) == 7:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=1825:
                        false_pos_lst_7[4]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_7[4]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_7[4]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='8' or int(df_trunc[ent][2]) == 8:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=3652:
                        false_pos_lst_8[4]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[4]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[4]+=1
                    data_cnt+=1
            elif df_trunc[ent][2]=='9' or int(df_trunc[ent][2]) == 9:
                if not df_trunc[ent][7] == '':
                    if int(df_trunc[ent][7])>=int(3652):
                        false_pos_lst_8[4]+=1
                        data_cnt+=1
                    else:
                        true_match_lst_8[4]+=1
                        data_cnt+=1
                elif df_trunc[ent][7] == '':
                    print('The entity with the MID {} has no entry here and is unable to be placed ' \
                          'in a category.'.format(df_trunc[ent][0]))
                    data_cnt+=1
                else:
                    true_match_lst_8[4]+=1
                    data_cnt+=1
        else:
            print('The entity with the MID {} was unable to be categorized.'.format(df_trunc[ent][0]))
            data_cnt+=1
                
        data_cnt_true+=data_cnt
            
    #print(data_cnt,'dc')
    #print(datalen,"dl")
    #print(datalen-prev_datalen,'data vs. file length')
        
#calculate the remaining entities that fall into neither category for both entities, then change to an array
false_pos_lst_7=np.array(false_pos_lst_7)
print(false_pos_lst_7,'fps7')
true_match_lst_7=np.array(true_match_lst_7)
print(true_match_lst_7,'tms7')
false_pos_lst_8=np.array(false_pos_lst_8)
print(false_pos_lst_8, 'fps8')
true_match_lst_8=np.array(true_match_lst_8)
print(true_match_lst_8,'tms8')
#sp_rem=ent_count[0]-(true_match_lst_7[0]+false_pos_lst_7[0]+true_match_lst_8[0]+false_pos_lst_8[0])
#llc_rem=ent_count[1]-(true_match_lst[1]+false_pos_lst[1]+true_match_lst_8[1]+false_pos_lst_8[1])
#rem_lst=np.array([sp_rem,llc_rem])

false_count = np.add(false_pos_lst_7,false_pos_lst_8)
true_count = np.add(true_match_lst_7,true_match_lst_8)
total_rec = np.add(true_count,false_count)
#add the function to add values on the plot
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i],horizontalalignment='center',fontsize=20)
def addlabelsleft(x,y):
    for i in range(len(x)):
        plt.text(i+.175,y[i],y[i],horizontalalignment='left',fontsize=20)
def addlabelsright(x,y):
    for i in range(len(x)):
        plt.text(i-.175,y[i],y[i],horizontalalignment='right',fontsize=20)

#construct stacked bar chart based on collected data
#may change from file to file; incorporate into loop to be dynamic (monthly/quarterly) or static (all simultaneously)
ent_type_lst=['Sole Proprietor','LLC','Assn./Estate/Trust','Partnership','Corporation']
ent_type_cnt=len(ent_type_lst)
ind=np.arange(ent_type_cnt)
figure=plt.subplots(figsize=(15,10))
first_lvl_bar=plt.bar(ent_type_lst,true_match_lst_7,color='red')
second_lvl_bar=plt.bar(ent_type_lst,false_pos_lst_7,color='green',bottom=true_match_lst_7)
third_lvl_bar=plt.bar(ent_type_lst,true_match_lst_8,color='pink',bottom=true_match_lst_7+false_pos_lst_7)
fourth_lvl_bar=plt.bar(ent_type_lst,false_pos_lst_8,color='lime',bottom=true_match_lst_7+false_pos_lst_7 \
                     +true_match_lst_8)

#create details for the graph and the stacked bar chart itself
x_legend=['True Match, Offense Type = 7','False Positive (Time Threshold\nExceeded, etc.), Offense Type = 7', \
         'True Match, Offense Type = 8','False Positive (Time Threshold\nExceeded etc.), Offense Type = 8']
x_label='Entity Type'
y_label='Entity Count'
chart_title='Total Risk by Entity Type'
addlabels(ent_type_lst,ent_count)
#plt.rcParams['font.size'] = '20'
#for label in (ax.get_xticklabels() + ax.get_yticklabels()):
#	label.set_fontsize('20')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel(x_label, fontsize=20)
plt.ylabel(y_label, fontsize=20)
plt.legend(x_legend,loc='center left', bbox_to_anchor=(1, 0.5), fontsize=20)
plt.title(chart_title, fontsize=20)
plt.show()

#add entities to buckets depending on the value of their risk and age
#**0-1 years, 1-5 years, 5-8 years, 8-10 years**
sp_bucket_count=[0,0,0,0,0]
llc_bucket_count=[0,0,0,0,0]
partner_bucket_count=[0,0,0,0,0]
assc_bucket_count=[0,0,0,0,0]
corp_bucket_count=[0,0,0,0,0]
llc_ot7_bucket=[0,0,0,0,0]
llc_ot8_bucket=[0,0,0,0,0]
llc_ot9_bucket=[0,0,0,0,0]
sp_ot7_bucket=[0,0,0,0,0]
sp_ot8_bucket=[0,0,0,0,0]
sp_ot9_bucket=[0,0,0,0,0]
partner_ot7_bucket=[0,0,0,0,0]
partner_ot8_bucket=[0,0,0,0,0]
partner_ot9_bucket=[0,0,0,0,0]
assc_ot7_bucket=[0,0,0,0,0]
assc_ot8_bucket=[0,0,0,0,0]
assc_ot9_bucket=[0,0,0,0,0]
corp_ot7_bucket=[0,0,0,0,0]
corp_ot8_bucket=[0,0,0,0,0]
corp_ot9_bucket=[0,0,0,0,0]
for ent in range(len(df_trunc)):
    if df_trunc[ent][8]=='LLC':
        if df_trunc[ent][2]=='7' or df_trunc[ent][2]==7:
            if int(df_trunc[ent][7])<=365:
                llc_ot7_bucket[0]+=1
                llc_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                llc_ot7_bucket[1]+=1
                llc_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                llc_ot7_bucket[2]+=1
                llc_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                llc_ot7_bucket[3]+=1
                llc_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                llc_ot7_bucket[4]+=1
                llc_bucket_count[4]+=1
        elif df_trunc[ent][2]=='8' or df_trunc[ent][2]==8:
            if int(df_trunc[ent][7])<=365:
                llc_ot8_bucket[0]+=1
                llc_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                llc_ot8_bucket[1]+=1
                llc_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                llc_ot8_bucket[2]+=1
                llc_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                llc_ot8_bucket[3]+=1
                llc_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                llc_ot8_bucket[4]+=1
                llc_bucket_count[4]+=1
        elif df_trunc[ent][2]=='9' or df_trunc[ent][2]==9:
            if int(df_trunc[ent][7])<=365:
                llc_ot9_bucket[0]+=1
                llc_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                llc_ot9_bucket[1]+=1
                llc_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                llc_ot9_bucket[2]+=1
                llc_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                llc_ot9_bucket[3]+=1
                llc_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                llc_ot9_bucket[4]+=1
                llc_bucket_count[4]+=1
    if df_trunc[ent][8]=='Sole Prop' or df_trunc[ent][8]=='Sole Proprietor':
        if df_trunc[ent][2]=='7' or df_trunc[ent][2]==7:
            if int(df_trunc[ent][7])<=365:
                sp_ot7_bucket[0]+=1
                sp_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                sp_ot7_bucket[1]+=1
                sp_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                sp_ot7_bucket[2]+=1
                sp_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                sp_ot7_bucket[3]+=1
                sp_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                sp_ot7_bucket[4]+=1
                sp_bucket_count[4]+=1
        elif df_trunc[ent][2]=='8' or df_trunc[ent][2]==8:
            if df_trunc[ent][7]=='':
                print('The number of days for this entry is empty.')
                continue
            if int(df_trunc[ent][7])<=365:
                sp_ot8_bucket[0]+=1
                sp_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                sp_ot8_bucket[1]+=1
                sp_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                sp_ot8_bucket[2]+=1
                sp_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                sp_ot8_bucket[3]+=1
                sp_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                sp_ot8_bucket[4]+=1
                sp_bucket_count[4]+=1
        elif df_trunc[ent][2]=='9' or df_trunc[ent][2]==9:
            if int(df_trunc[ent][7])<=365:
                sp_ot9_bucket[0]+=1
                sp_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                sp_ot9_bucket[1]+=1
                sp_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                sp_ot9_bucket[2]+=1
                sp_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                sp_ot9_bucket[3]+=1
                sp_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                sp_ot9_bucket[4]+=1
                sp_bucket_count[4]+=1
    if df_trunc[ent][8]=='Association/Estate/Trust':
        if df_trunc[ent][2]=='7' or df_trunc[ent][2]==7:
            if int(df_trunc[ent][7])<=365:
                assc_ot7_bucket[0]+=1
                assc_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                assc_ot7_bucket[1]+=1
                assc_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                assc_ot7_bucket[2]+=1
                assc_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                assc_ot7_bucket[3]+=1
                assc_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                llc_ot7_bucket[4]+=1
                llc_bucket_count[4]+=1
        elif df_trunc[ent][2]=='8' or df_trunc[ent][2]==8:
            if int(df_trunc[ent][7])<=365:
                assc_ot8_bucket[0]+=1
                assc_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                assc_ot8_bucket[1]+=1
                assc_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                assc_ot8_bucket[2]+=1
                assc_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                assc_ot8_bucket[3]+=1
                assc_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                assc_ot8_bucket[4]+=1
                assc_bucket_count[4]+=1
        elif df_trunc[ent][2]=='9' or df_trunc[ent][2]==9:
            if int(df_trunc[ent][7])<=365:
                assc_ot9_bucket[0]+=1
                assc_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                assc_ot9_bucket[1]+=1
                assc_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                assc_ot9_bucket[2]+=1
                assc_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                assc_ot9_bucket[3]+=1
                assc_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                assc_ot9_bucket[4]+=1
                assc_bucket_count[4]+=1
    if df_trunc[ent][8]=='Partnership':
        if df_trunc[ent][2]=='7' or df_trunc[ent][2]==7:
            if int(df_trunc[ent][7])<=365:
                partner_ot7_bucket[0]+=1
                partner_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                partner_ot7_bucket[1]+=1
                partner_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                partner_ot7_bucket[2]+=1
                partner_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                partner_ot7_bucket[3]+=1
                partner_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                partner_ot7_bucket[4]+=1
                partner_bucket_count[4]+=1
        elif df_trunc[ent][2]=='8' or df_trunc[ent][2]==8:
            if int(df_trunc[ent][7])<=365:
                partner_ot8_bucket[0]+=1
                partner_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                partner_ot8_bucket[1]+=1
                partner_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                partner_ot8_bucket[2]+=1
                partner_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                partner_ot8_bucket[3]+=1
                partner_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                partner_ot8_bucket[4]+=1
                partner_bucket_count[4]+=1
        elif df_trunc[ent][2]=='9' or df_trunc[ent][2]==9:
            if int(df_trunc[ent][7])<=365:
                partner_ot9_bucket[0]+=1
                partner_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                partner_ot9_bucket[1]+=1
                partner_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                partner_ot9_bucket[2]+=1
                partner_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                partner_ot9_bucket[3]+=1
                partner_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                partner_ot9_bucket[4]+=1
                partner_bucket_count[4]+=1
    if df_trunc[ent][8]=='Corporation':
        if df_trunc[ent][7]=='':
                continue
        if df_trunc[ent][2]=='7' or df_trunc[ent][2]==7:
            if int(df_trunc[ent][7])<=365:
                corp_ot7_bucket[0]+=1
                corp_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                corp_ot7_bucket[1]+=1
                corp_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                corp_ot7_bucket[2]+=1
                corp_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                corp_ot7_bucket[3]+=1
                corp_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                corp_ot7_bucket[4]+=1
                corp_bucket_count[4]+=1
        elif df_trunc[ent][2]=='8' or df_trunc[ent][2]==8:
            if df_trunc[ent][7]=='':
                continue
            if int(df_trunc[ent][7])<=365:
                corp_ot8_bucket[0]+=1
                corp_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                corp_ot8_bucket[1]+=1
                corp_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                corp_ot8_bucket[2]+=1
                corp_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                corp_ot8_bucket[3]+=1
                corp_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                corp_ot8_bucket[4]+=1
                corp_bucket_count[4]+=1
        elif df_trunc[ent][2]=='9' or df_trunc[ent][2]==9:
            if df_trunc[ent][7]=='':
                continue
            if int(df_trunc[ent][7])<=365:
                corp_ot9_bucket[0]+=1
                corp_bucket_count[0]+=1
            elif int(df_trunc[ent][7])>365 and int(df_trunc[ent][7])<=1826:
                corp_ot9_bucket[1]+=1
                corp_bucket_count[1]+=1
            elif int(df_trunc[ent][7])>1826 and int(df_trunc[ent][7])<=2920:
                corp_ot9_bucket[2]+=1
                corp_bucket_count[2]+=1
            elif int(df_trunc[ent][7])>2920 and int(df_trunc[ent][7])<=3652:
                corp_ot9_bucket[3]+=1
                corp_bucket_count[3]+=1
            elif int(df_trunc[ent][7])>3652:
                corp_ot9_bucket[4]+=1
                corp_bucket_count[4]+=1
            
#create a multidimensional array containing all buckets
md_bkt_array=[llc_ot7_bucket,llc_ot8_bucket,llc_ot9_bucket,sp_ot7_bucket,sp_ot8_bucket,sp_ot9_bucket,assc_ot7_bucket,\
             assc_ot8_bucket,assc_ot9_bucket,partner_ot7_bucket,partner_ot8_bucket,partner_ot9_bucket,corp_ot7_bucket,\
             corp_ot8_bucket,corp_ot9_bucket]
#md_bkt_array=pd.DataFrame(md_bkt_array)
#print(md_bkt_array)

#change the buckets into arrays
llc_ot7_bucket=np.array(llc_ot7_bucket)
llc_ot8_bucket=np.array(llc_ot8_bucket)
llc_ot9_bucket=np.array(llc_ot9_bucket)
sp_ot7_bucket=np.array(sp_ot7_bucket)
sp_ot8_bucket=np.array(sp_ot8_bucket)
sp_ot9_bucket=np.array(sp_ot9_bucket)
assc_ot7_bucket=np.array(assc_ot7_bucket)
assc_ot8_bucket=np.array(assc_ot8_bucket)
assc_ot9_bucket=np.array(assc_ot9_bucket)
partner_ot7_bucket=np.array(partner_ot7_bucket)
partner_ot8_bucket=np.array(partner_ot8_bucket)
partner_ot9_bucket=np.array(partner_ot9_bucket)
corp_ot7_bucket=np.array(corp_ot7_bucket)
corp_ot8_bucket=np.array(corp_ot8_bucket)
corp_ot9_bucket=np.array(corp_ot9_bucket)


#sum all totals for future use
llc_bucket_sum=sum(llc_ot7_bucket+llc_ot8_bucket+llc_ot9_bucket)
sp_bucket_sum=sum(sp_ot7_bucket+sp_ot8_bucket+sp_ot9_bucket)
assc_bucket_sum=sum(assc_ot7_bucket+assc_ot8_bucket+assc_ot9_bucket)
partner_bucket_sum=sum(partner_ot7_bucket+partner_ot8_bucket+partner_ot9_bucket)
corp_bucket_sum=sum(corp_ot7_bucket+corp_ot8_bucket+corp_ot9_bucket)
total_bucket_sum=llc_bucket_sum+sp_bucket_sum+assc_bucket_sum+partner_bucket_sum+corp_bucket_sum

#create percentages for each category
llc_bar1_pct=(llc_ot7_bucket/total_bucket_sum)*100
llc_bar2_pct=(llc_ot8_bucket/total_bucket_sum)*100
llc_bar3_pct=(llc_ot9_bucket/total_bucket_sum)*100
sp_bar1_pct=(sp_ot7_bucket/total_bucket_sum)*100
sp_bar2_pct=(sp_ot8_bucket/total_bucket_sum)*100
sp_bar3_pct=(sp_ot9_bucket/total_bucket_sum)*100
assc_bar1_pct=(assc_ot7_bucket/total_bucket_sum)*100
assc_bar2_pct=(assc_ot8_bucket/total_bucket_sum)*100
assc_bar3_pct=(assc_ot9_bucket/total_bucket_sum)*100
partner_bar1_pct=(partner_ot7_bucket/total_bucket_sum)*100
partner_bar2_pct=(partner_ot8_bucket/total_bucket_sum)*100
partner_bar3_pct=(partner_ot9_bucket/total_bucket_sum)*100
corp_bar1_pct=(corp_ot7_bucket/total_bucket_sum)*100
corp_bar2_pct=(corp_ot8_bucket/total_bucket_sum)*100
corp_bar3_pct=(corp_ot9_bucket/total_bucket_sum)*100

#add a graph for correlations between the time an entity has been in business and offenses
bucket_lst=['<= 12 months','12-60 months','60-96 months','96-120 months','>120 months']
ent_type_cnt2=len(bucket_lst)
ind=np.arange(ent_type_cnt2)
ind2=ind+.1
ind3=ind-.1
ind4=ind+.2
ind5=ind-.2
width=.1
width1=-0.1
width2=0.1
figure2,ax=plt.subplots(figsize=(30,15))
#ax.tick_params(axis='x', labelsize=20)
#ax.set_xticks(ind)
llc_first_lvl_bar=plt2.bar(x=ind,height=llc_ot7_bucket,tick_label=bucket_lst,color='purple',width=.1)
llc_second_lvl_bar=plt2.bar(x=ind,height=llc_ot8_bucket,tick_label=bucket_lst,color='brown',bottom=llc_ot7_bucket,width=.1)
llc_third_lvl_bar2=plt2.bar(x=ind,height=llc_ot9_bucket,tick_label=bucket_lst,color='navy',bottom=llc_ot7_bucket+llc_ot8_bucket,width=.1)
#plt2.xticks(ind,fontsize=30)
#ax.set_xticks(ind2)
sp_first_lvl_bar2=plt2.bar(ind2,sp_ot7_bucket,color='cyan',align='center',width=width)
sp_second_lvl_bar2=plt2.bar(ind2,sp_ot8_bucket,color='magenta',bottom=sp_ot7_bucket,align='center',width=width)
sp_third_lvl_bar2=plt2.bar(ind2,sp_ot9_bucket,color='grey',bottom=sp_ot7_bucket+sp_ot8_bucket,align='center',width=width)
#plt2.xticks(ind2,fontsize=30)
#ax.set_xticks(ind3)
assc_first_lvl_bar=plt2.bar(ind3,assc_ot7_bucket,color='blue',align='center',width=width1)
assc_second_lvl_bar=plt2.bar(ind3,assc_ot8_bucket,color='black',bottom=assc_ot7_bucket,align='center',width=width1)
assc_third_lvl_bar=plt2.bar(ind3,assc_ot9_bucket,color='yellow',bottom=assc_ot7_bucket+assc_ot8_bucket,align='center',width=width1)
#plt2.xticks(ind3,fontsize=30)
#ax.set_xticks(ind4)
partner_first_lvl_bar=plt2.bar(ind4,partner_ot7_bucket,color='gold',align='center',width=width1)
partner_second_lvl_bar=plt2.bar(ind4,partner_ot8_bucket,color='orange',bottom=partner_ot7_bucket,align='center',width=width1)
partner_third_lvl_bar=plt2.bar(ind4,partner_ot9_bucket,color='pink',bottom=partner_ot7_bucket+partner_ot8_bucket,align='center',width=width1)
#plt2.xticks(ind4,fontsize=30)
#ax.set_xticks(ind5)
corp_first_lvl_bar=plt2.bar(ind5,corp_ot7_bucket,color='green',align='center',width=width2)
corp_second_lvl_bar=plt2.bar(ind5,corp_ot8_bucket,color='beige',bottom=corp_ot7_bucket,width=width2,align='center')
corp_third_lvl_bar=plt2.bar(ind5,corp_ot9_bucket,color='lime',bottom=corp_ot7_bucket+corp_ot8_bucket,width=width2,align='center')
#plt2.xticks(ind5,fontsize=30)

#rects1 = ax.bar(ind - width/2, bucket_lst,llc_ot7_bucket, width, label='LLC')
#rects2 = ax.bar(ind + width/2, bucket_lst,llc_ot8_bucket, width, label='Sole Prop')

#fig.tight_layout()

#put all of the named percentages into a single data frame
ent_cat_df=[llc_bar1_pct,llc_bar2_pct,llc_bar3_pct,sp_bar1_pct,sp_bar2_pct,sp_bar3_pct,assc_bar1_pct,assc_bar2_pct,\
            assc_bar3_pct,partner_bar1_pct,partner_bar2_pct,partner_bar3_pct,corp_bar1_pct,corp_bar2_pct,corp_bar3_pct]
df = pd.DataFrame(md_bkt_array,columns = bucket_lst)
#print((df,'df; same as ecd but formatted'))

#define the relative and absolute totals for percentages on the graph
#and create data frames in which percentages will be displayed
#df_total = total_bucket_sum
#df_rel = df[df.columns[:]].div(df_total, 0)*100
#print(df_rel,'df rel')

#determine the values of each double bar
def barHeightCalc(bkt1,bkt2,bkt3):
    bar_heights=[]
    if len(bkt1) == len(bkt2) == len(bkt3):
        for h in range(len(bkt1)):
            ind_barhs=[]
            ind_barhs=[bkt1[h],bkt2[h],bkt3[h]]
            bar_heights.append(ind_barhs)
        print(bar_heights,'bh')
    
llc_barh=barHeightCalc(llc_ot7_bucket,llc_ot8_bucket,llc_ot9_bucket)
sp_barh=barHeightCalc(sp_ot7_bucket,sp_ot8_bucket,sp_ot9_bucket)
assc_barh=barHeightCalc(assc_ot7_bucket,assc_ot8_bucket,assc_ot9_bucket)
partner_barh=barHeightCalc(partner_ot7_bucket,partner_ot8_bucket,partner_ot9_bucket)
corp_barh=barHeightCalc(corp_ot7_bucket,corp_ot8_bucket,corp_ot9_bucket)

#'cs' means column size, 'pc' means percent
#for n in df_rel:
    #for i, (cs, pc) in enumerate(zip(df.iloc[:, :][n],llc_barh_df[n], df[n])):
    #for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, :][n], df[n], df_rel[n])):
        #print(cs,'cs')
        ##print(ab,'ab')
        #print(pc,'pc')
        #plt.text(cs - llc_barh[n] / 2, i, str(np.round(pc, 2)) + '%', 
                 #va = 'center', ha = 'center')
        #plt.text(cs - ab/ 2, i, str(np.round(pc, 2)) + '%', 
                 #va = 'center', ha = 'center')
            
df_total = total_bucket_sum
df_rel = df[df.columns[1:]].div(df_total, 0) * 100
#print(df_rel,'dr')
 
#for n in df_rel:
#    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], 
#                                         df[n], df_rel[n])):
#        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
#                 va = 'center', ha = 'center', fontsize = 8)

        
#for n in df_rel:
#    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], 
#                                         df[n], df_rel[n])):
#        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
#                 va = 'center', ha = 'center', rotation = 20, fontsize = 8)


    
#plotleftPct(llc_bar1_pct,'right')

x_legend2=['True Match, Offense Type = 7 (LLC)','True Match, Offense Type = 8 (LLC)','True Match, Offense Type = 9 (LLC)',\
          'True Match, Offense Type = 7 (SP)','True Match, Offense Type = 8 (SP)','True Match, Offense Type = 9 (SP)',\
          'True Match, Offense Type = 7 (A/E/T)','True Match, Offense Type = 8 (A/E/T)','True Match, Offense Type = 9 (A/E/T)',\
          'True Match, Offense Type = 7 (P)','True Match, Offense Type = 8 (P)','True Match, Offense Type = 9 (P)',\
          'True Match, Offense Type = 7 (C)','True Match, Offense Type = 8 (C)','True Match, Offense Type = 9 (C)']
x_label2='Newly Boarded Merchants Years in Business'
y_label2='# of Merchants'
chart_title2='Correlation between # Years in Business and Criminal Background Check Type'
#addlabelsright(bucket_lst,llc_bucket_count)
#addlabelsleft(bucket_lst,sp_bucket_count)
#partner_bucket_count, assc_bucket_count, corp_bucket_count
plt2.rcParams.update({'font.size': 30})
plt2.xlabel(x_label2, fontsize=30)
plt2.xticks(fontsize=30)
#plt2.xticks(ind2,fontsize=30)
#ax.set_xticks(ind+2*width)
plt2.yticks(fontsize=30)
plt2.ylabel(y_label2, fontsize=30)
plt2.legend(x_legend2,loc='center left', bbox_to_anchor=(1, 0.5), fontsize=30)
plt2.title(chart_title2, fontsize=30)
#plt2.margins(y=6)
#plt2.subplots_adjust(bottom=.5)
figure2.tight_layout()
plt2.show()

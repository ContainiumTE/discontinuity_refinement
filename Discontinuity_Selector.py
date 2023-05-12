#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import streamlit as st
import requests


# In[34]:


username = 'ContainiumTE'
token = 'RRopW0EJvVEcfS5EGt1rxxswfGF5IfzU3Bh4VkPHS10'

github_session = requests.Session()
github_session.auth = (username,token)


# In[30]:



st.title("Discontinuity Weighting Tool")

menu = ["Home","Other"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.subheader("Home")
    data_file = st.file_uploader("Upload CSV", type=["csv"])

    if data_file is not None:
        #st.write(type(data_file))
        df_rmr = pd.read_csv(data_file)


# In[50]:

#df_rmr = pd.read_csv('Qjr_selection.csv')
pd.set_option('display.max_columns',500)
pd.set_option('display.max_rows',500)


# In[51]:


df_rmr.columns = df_rmr.columns.str.strip().str.lower().str.replace(' ','_').str.replace('(', '').str.replace(')', '')
df_rmr.head()


# In[52]:


hole_id = df_rmr['hole_id'].unique()
#hole_id


# In[53]:


def joint_roughness1(jr1,jr1_count):
    
    polished_1=0
    smooth_planar_2 = 0
    rough_planar_3 = 0
    slickensided_undulating_4 = 0
    smooth_undulating_5 = 0
    rough_undulating_6 = 0
    slickensided_stepped_7 = 0
    smooth_stepped_8 = 0
    rough_stepped_9 = 0

    pol_rat_1=0
    smoot_rat_2=0
    rou_rat_3=0
    slick_rat_4=0
    smoot_und_rat_5=0
    rou_und_rat_6=0
    slick_ste_rat_7=0
    smoot_step_rat_8=0
    rou_step_rat_9=0
    
    if jr1=='1 - Polished':
        polished_1 = jr1_count
        pol_rat_1 = jr1_count*0.45
        print("Jr1 Allocated to: 1 - Polished")
    
    elif jr1=='2 - Smooth Planar':
        smooth_planar_2= jr1_count
        smoot_rat_2 = jr1_count*0.4
        print("Jr1 Allocated to: 2 - Smooth Planar")
            
    elif jr1=='3 - Rough Planar':
        rough_planar_3 = jr1_count
        rou_rat_3 = jr1_count*0.35
        print("Jr1 Allocated to: 3 - Rough Planar")

    elif jr1=='4 - Slickensided Undulating':
        slickensided_undulating_4 = jr1_count
        slick_rat_4 = jr1_count*0.3
        print("Jr1 Allocated to: 4 - Slickensided Undulating")

    elif jr1=='5 - Smooth Undulating':
        smooth_undulating_5= jr1_count
        smoot_und_rat_5 = jr1_count*0.25
        print("Jr1 Allocated to: 5 - Smooth Undulating")

    elif jr1=='6 - Rough Undulating':
        rough_undulating_6 = jr1_count
        rou_und_rat_6 = jr1_count*0.2
        print("Jr1 Allocated to: 6 - Rough Undulating")

    elif jr1=='7 - Slickensided Stepped':
        slickensided_stepped_7 = jr1_count
        slick_ste_rat_7 = jr1_count*0.15
        print("Jr1 Allocated to: 7 - Slickensided Stepped")

    elif jr1=='8 - Smooth Stepped':
        smooth_stepped_8 = jr1_count
        smoot_step_rat_8 = jr1_count*0.1
        print("Jr1 Allocated to: 8 - Smooth Stepped")

    elif jr1=='9 - Rough Stepped / Irregular':
        rough_stepped_9 = jr1_count
        rou_step_rat_9 = jr1_count*0.05
        print("Jr1 Allocated to: 9 - Rough Stepped / Irregular")
    elif jr1=='':
        print("No Jr1")
    else:
        print("None")
        
    return polished_1, smooth_planar_2, rough_planar_3, slickensided_undulating_4, smooth_undulating_5, rough_undulating_6, slickensided_stepped_7, smooth_stepped_8, rough_stepped_9,pol_rat_1,smoot_rat_2,rou_rat_3,slick_rat_4,smoot_und_rat_5,rou_und_rat_6,slick_ste_rat_7,smoot_step_rat_8, rou_step_rat_9


# In[54]:


def joint_roughness2(jr2,jr2_count):
    
    polished_1_2=0
    smooth_planar_2_2 = 0
    rough_planar_3_2 = 0
    slickensided_undulating_4_2 = 0
    smooth_undulating_5_2 = 0
    rough_undulating_6_2 = 0
    slickensided_stepped_7_2 = 0
    smooth_stepped_8_2 = 0
    rough_stepped_9_2 = 0

    pol_rat_1_2=0
    smoot_rat_2_2=0
    rou_rat_3_2=0
    slick_rat_4_2=0
    smoot_und_rat_5_2=0
    rou_und_rat_6_2=0
    slick_ste_rat_7_2=0
    smoot_step_rat_8_2=0
    rou_step_rat_9_2=0
    
    if jr2=='1 - Polished':
        polished_1_2 = jr2_count
        pol_rat_1_2 = jr2_count*0.45
        print("Jr2 Allocated to: 1 - Polished")
    
    elif jr2=='2 - Smooth Planar':
        smooth_planar_2_2= jr2_count
        smoot_rat_2_2 = jr2_count*0.4
        print("Jr2 Allocated to: 2 - Smooth Planar")
            
    elif jr2=='3 - Rough Planar':
        rough_planar_3_2 = jr2_count
        rou_rat_3_2 = jr2_count*0.35
        print("Jr2 Allocated to: 3 - Rough Planar")

    elif jr2=='4 - Slickensided Undulating':
        slickensided_undulating_4_2 = jr2_count
        slick_rat_4_2 = jr2_count*0.3
        print("Jr2 Allocated to: 4 - Slickensided Undulating")

    elif jr2=='5 - Smooth Undulating':
        smooth_undulating_5_2= jr2_count
        smoot_und_rat_5_2 = jr2_count*0.25
        print("Jr2 Allocated to: 5 - Smooth Undulating")

    elif jr2=='6 - Rough Undulating':
        rough_undulating_6_2 = jr2_count
        rou_und_rat_6_2 = jr2_count*0.2
        print("Jr2 Allocated to: 6 - Rough Undulating")

    elif jr2=='7 - Slickensided Stepped':
        slickensided_stepped_7_2 = jr2_count
        slick_ste_rat_7_2 = jr2_count*0.15
        print("Jr2 Allocated to: 7 - Slickensided Stepped")

    elif jr2=='8 - Smooth Stepped':
        smooth_stepped_8_2 = jr2_count
        smoot_step_rat_8_2 = jr2_count*0.1
        print("Jr2 Allocated to: 8 - Smooth Stepped")

    elif jr2=='9 - Rough Stepped / Irregular':
        rough_stepped_9_2 = jr2_count
        rou_step_rat_9_2 = jr2_count*0.05
        print("Jr2 Allocated to: 9 - Rough Stepped / Irregular")
    elif jr2=='NaN':
        print("No Jr2")
    else:
        print("None")
        
    return polished_1_2, smooth_planar_2_2, rough_planar_3_2, slickensided_undulating_4_2, smooth_undulating_5_2, rough_undulating_6_2, slickensided_stepped_7_2, smooth_stepped_8_2, rough_stepped_9_2,pol_rat_1_2,smoot_rat_2_2,rou_rat_3_2,slick_rat_4_2,smoot_und_rat_5_2,rou_und_rat_6_2,slick_ste_rat_7_2,smoot_step_rat_8_2, rou_step_rat_9_2


# In[55]:


def joint_roughness3(jr3,jr3_count):
    
    polished_1_3=0
    smooth_planar_2_3 = 0
    rough_planar_3_3 = 0
    slickensided_undulating_4_3 = 0
    smooth_undulating_5_3 = 0
    rough_undulating_6_3 = 0
    slickensided_stepped_7_3 = 0
    smooth_stepped_8_3 = 0
    rough_stepped_9_3 = 0

    pol_rat_1_3=0
    smoot_rat_2_3=0
    rou_rat_3_3=0
    slick_rat_4_3=0
    smoot_und_rat_5_3=0
    rou_und_rat_6_3=0
    slick_ste_rat_7_3=0
    smoot_step_rat_8_3=0
    rou_step_rat_9_3=0
    
    if jr3=='1 - Polished':
        polished_1_3 = jr3_count
        pol_rat_1_3 = jr3_count*0.45
        print("Jr3 Allocated to: 1 - Polished")
    
    elif jr3=='2 - Smooth Planar':
        smooth_planar_2_3= jr3_count
        smoot_rat_2_3 = jr3_count*0.4
        print("Jr3 Allocated to: 2 - Smooth Planar")
            
    elif jr3=='3 - Rough Planar':
        rough_planar_3_3 = jr3_count
        rou_rat_3_3 = jr3_count*0.35
        print("Jr3 Allocated to: 3 - Rough Planar")

    elif jr3=='4 - Slickensided Undulating':
        slickensided_undulating_4_3 = jr3_count
        slick_rat_4_3 = jr3_count*0.3
        print("Jr3 Allocated to: 4 - Slickensided Undulating")

    elif jr3=='5 - Smooth Undulating':
        smooth_undulating_5_3= jr3_count
        smoot_und_rat_5_3 = jr3_count*0.25
        print("Jr3 Allocated to: 5 - Smooth Undulating")

    elif jr3=='6 - Rough Undulating':
        rough_undulating_6_3 = jr3_count
        rou_und_rat_6_3 = jr3_count*0.2
        print("Jr3 Allocated to: 6 - Rough Undulating")

    elif jr3=='7 - Slickensided Stepped':
        slickensided_stepped_7_3 = jr3_count
        slick_ste_rat_7_3 = jr3_count*0.15
        print("Jr3 Allocated to: 7 - Slickensided Stepped")

    elif jr3=='8 - Smooth Stepped':
        smooth_stepped_8_3 = jr3_count
        smoot_step_rat_8_3 = jr3_count*0.1
        print("Jr3 Allocated to: 8 - Smooth Stepped")

    elif jr3=='9 - Rough Stepped / Irregular':
        rough_stepped_9_3 = jr3_count
        rou_step_rat_9_3 = jr3_count*0.05
        print("Jr3 Allocated to: 9 - Rough Stepped / Irregular")
    elif jr3=='NaN':
        print("No Jr3")
    else:
        print("None")
        
    return polished_1_3, smooth_planar_2_3, rough_planar_3_3, slickensided_undulating_4_3, smooth_undulating_5_3, rough_undulating_6_3, slickensided_stepped_7_3, smooth_stepped_8_3, rough_stepped_9_3,pol_rat_1_3,smoot_rat_2_3,rou_rat_3_3,slick_rat_4_3,smoot_und_rat_5_3,rou_und_rat_6_3,slick_ste_rat_7_3,smoot_step_rat_8_3, rou_step_rat_9_3


# In[56]:


def sum_of_weighting(count_oj,polished_1,smooth_planar_2,rough_planar_3,slickensided_undulating_4,smooth_undulating_5,rough_undulating_6,slickensided_stepped_7,smooth_stepped_8,rough_stepped_9,pol_rat_1,smoot_rat_2,rou_rat_3,slick_rat_4,smoot_und_rat_5,rou_und_rat_6,slick_ste_rat_7,smoot_step_rat_8, rou_step_rat_9,polished_1_2,smooth_planar_2_2,rough_planar_3_2,slickensided_undulating_4_2,smooth_undulating_5_2,rough_undulating_6_2,slickensided_stepped_7_2,smooth_stepped_8_2,rough_stepped_9_2,pol_rat_1_2,smoot_rat_2_2,rou_rat_3_2,slick_rat_4_2,smoot_und_rat_5_2,rou_und_rat_6_2,slick_ste_rat_7_2,smoot_step_rat_8_2, rou_step_rat_9_2,polished_1_3, smooth_planar_2_3, rough_planar_3_3, slickensided_undulating_4_3, smooth_undulating_5_3, rough_undulating_6_3, slickensided_stepped_7_3, smooth_stepped_8_3, rough_stepped_9_3,pol_rat_1_3,smoot_rat_2_3,rou_rat_3_3,slick_rat_4_3,smoot_und_rat_5_3,rou_und_rat_6_3,slick_ste_rat_7_3,smoot_step_rat_8_3, rou_step_rat_9_3):
    
    sum_total_weighting = pol_rat_1 + smoot_rat_2 + rou_rat_3 + slick_rat_4 + smoot_und_rat_5 + rou_und_rat_6 + slick_ste_rat_7 + smoot_step_rat_8 + rou_step_rat_9 + pol_rat_1_2 + smoot_rat_2_2 + rou_rat_3_2+slick_rat_4_2+smoot_und_rat_5_2+rou_und_rat_6_2+slick_ste_rat_7_2+smoot_step_rat_8_2+ rou_step_rat_9_2+pol_rat_1_3+smoot_rat_2_3+rou_rat_3_3+slick_rat_4_3+smoot_und_rat_5_3+rou_und_rat_6_3+slick_ste_rat_7_3+smoot_step_rat_8_3+ rou_step_rat_9_3
    if (count_oj>0) and (sum_total_weighting>0):
        
        count = count_oj
        weighting_1 = (polished_1+polished_1_2+polished_1_3)/count
        weighting_2 = (smooth_planar_2+smooth_planar_2_2+smooth_planar_2_3)/count
        weighting_3 = (rough_planar_3+rough_planar_3_2+rough_planar_3_3)/count
        weighting_4 = (slickensided_undulating_4+slickensided_undulating_4_2+slickensided_undulating_4_3)/count
        weighting_5 = (smooth_undulating_5+smooth_undulating_5_2+smooth_undulating_5_3)/count
        weighting_6 = (rough_undulating_6+rough_undulating_6_2+rough_undulating_6_3)/count
        weighting_7 = (slickensided_stepped_7+slickensided_stepped_7_2+slickensided_stepped_7_3)/count
        weighting_8 = (smooth_stepped_8+smooth_stepped_8_2+smooth_stepped_8_3)/count
        weighting_9 = (rough_stepped_9+rough_stepped_9_2+rough_stepped_9_3)/count

        weighting_rating_1 = (pol_rat_1+pol_rat_1_2+pol_rat_1_3)/sum_total_weighting
        weighting_rating_2 = (smoot_rat_2+smoot_rat_2_2+smoot_rat_2_3)/sum_total_weighting
        weighting_rating_3 = (rou_rat_3+rou_rat_3_2+rou_rat_3_3)/sum_total_weighting
        weighting_rating_4 = (slick_rat_4+slick_rat_4_2+slick_rat_4_3)/sum_total_weighting
        weighting_rating_5 = (smoot_und_rat_5+smoot_und_rat_5_2+smoot_und_rat_5_3)/sum_total_weighting
        weighting_rating_6 = (rou_und_rat_6+rou_und_rat_6_2+rou_und_rat_6_3)/sum_total_weighting
        weighting_rating_7 = (slick_ste_rat_7+slick_ste_rat_7_2+slick_ste_rat_7_3)/sum_total_weighting
        weighting_rating_8 = (smoot_step_rat_8+smoot_step_rat_8_2+smoot_step_rat_8_3)/sum_total_weighting
        weighting_rating_9 = (rou_step_rat_9+rou_step_rat_9_2+rou_step_rat_9_3)/sum_total_weighting

        total_rating_1 = weighting_1*weighting_rating_1
        total_rating_2 = weighting_2*weighting_rating_2
        total_rating_3 = weighting_3*weighting_rating_3
        total_rating_4 = weighting_4*weighting_rating_4
        total_rating_5 = weighting_5*weighting_rating_5
        total_rating_6 = weighting_6*weighting_rating_6
        total_rating_7 = weighting_7*weighting_rating_7
        total_rating_8 = weighting_8*weighting_rating_8
        total_rating_9 = weighting_9*weighting_rating_9

        max_rating = max(total_rating_1,total_rating_2,total_rating_3,total_rating_4,total_rating_5,total_rating_6,total_rating_7,total_rating_8,total_rating_9)

        ratings = [total_rating_1,total_rating_2,total_rating_3,total_rating_4,total_rating_5,total_rating_6,total_rating_7,total_rating_8,total_rating_9]
        index = ratings.index(max_rating)
        
        print("1 ","Polished",polished_1," - ",total_rating_1)
        print("2 ","Smoothe Planar",smooth_planar_2," - ",total_rating_2)
        print("3 ","Rough Planar",rough_planar_3," - ",total_rating_3)
        print("4 ","Slickensided Undulating",slickensided_undulating_4," - ",total_rating_4)
        print("5 ","Smooth Undulating",smooth_undulating_5," - ",total_rating_5)
        print("6 ","Rough Undulating",rough_undulating_6," - ",total_rating_6)
        print("7 ","Slickensided Stepped",slickensided_stepped_7," - ",total_rating_7)
        print("8 ","Smoothe Stepped",smooth_stepped_8," - ",total_rating_8)
        print("9 ","Rough Stepped",rough_stepped_9," - ",total_rating_9)

        #print("The selected Micro Joughness is ",max_rating)
        #print(index)

        selected_roughness = 0
        if index==0:
            selected_roughness = '1 - Polished'
        elif index==1:
            selected_roughness = '2 - Smooth Planar'
        elif index==2:
            selected_roughness = '3 - Rough Planar'
        elif index==3:
            selected_roughness = '4 - Slickensided Undulating'
        elif index==4:
            selected_roughness = '5 - Smooth Undulating'
        elif index==5:
            selected_roughness = '6 - Rough Undulating'
        elif index==6:
            selected_roughness = '7 - Slickensided Stepped'
        elif index==7:
            selected_roughness = '8 - Smooth Stepped'
        elif index==8:
            selected_roughness = '9 - Rough Stepped/Irregular'
        else:
            selected_roughness = 'None'
    
        #
    else:
        print("No Micro Roughness Allocated")    
        
    return selected_roughness


# In[57]:


discon_data1 = {'hole_id': [],'from': [],'to': [],'Oj1': [],'Jr1': [],'Oj2': [],'Jr2': [],'Oj3': [],'Jr3': [],'Selected Jr': []}

QJr = pd.DataFrame(discon_data1)

for i in hole_id:
    df_b = df_rmr[(df_rmr['hole_id']==i)]
    print("Hole ID: ",i)
    
    for k in df_b.index:
        from_1 = df_b['from_m'][k]
        to_1 = df_b['to_m'][k]
        print("Interval Depth (m): ",from_1," - ",to_1)
        jr1 = df_b['j1_-_micro_roughness'][k]
        jr1_count = df_b['j1_-_oj_count'][k]

        jr2 = df_b['j2_-_micro_roughness'][k]
        jr2_count = df_b['j2_-_oj_count'][k]

        jr3 = df_b['j3_-_micro_roughness'][k]
        jr3_count = df_b['j3_-_oj_count'][k]
        
        count_oj =  jr1_count + jr2_count + jr3_count
        
        if count_oj > 0:
        
            jr1_result = joint_roughness1(jr1,jr1_count)
            jr2_result = joint_roughness2(jr2,jr2_count)
            jr3_result = joint_roughness3(jr3,jr3_count)      

            polished_1,smooth_planar_2,rough_planar_3,slickensided_undulating_4,smooth_undulating_5,rough_undulating_6,slickensided_stepped_7,smooth_stepped_8,rough_stepped_9,pol_rat_1,smoot_rat_2,rou_rat_3,slick_rat_4,smoot_und_rat_5,rou_und_rat_6,slick_ste_rat_7,smoot_step_rat_8, rou_step_rat_9 = jr1_result[0],jr1_result[1],jr1_result[2],jr1_result[3],jr1_result[4],jr1_result[5],jr1_result[6],jr1_result[7],jr1_result[8],jr1_result[9],jr1_result[10],jr1_result[11],jr1_result[12],jr1_result[13],jr1_result[14],jr1_result[15],jr1_result[16],jr1_result[17]
            polished_1_2,smooth_planar_2_2,rough_planar_3_2,slickensided_undulating_4_2,smooth_undulating_5_2,rough_undulating_6_2,slickensided_stepped_7_2,smooth_stepped_8_2,rough_stepped_9_2,pol_rat_1_2,smoot_rat_2_2,rou_rat_3_2,slick_rat_4_2,smoot_und_rat_5_2,rou_und_rat_6_2,slick_ste_rat_7_2,smoot_step_rat_8_2, rou_step_rat_9_2 = jr2_result[0],jr2_result[1],jr2_result[2],jr2_result[3],jr2_result[4],jr2_result[5],jr2_result[6],jr2_result[7],jr2_result[8],jr2_result[9],jr2_result[10],jr2_result[11],jr2_result[12],jr2_result[13],jr2_result[14],jr2_result[15],jr2_result[16],jr2_result[17]
            polished_1_3,smooth_planar_2_3,rough_planar_3_3,slickensided_undulating_4_3,smooth_undulating_5_3,rough_undulating_6_3,slickensided_stepped_7_3,smooth_stepped_8_3,rough_stepped_9_3,pol_rat_1_3,smoot_rat_2_3,rou_rat_3_3,slick_rat_4_3,smoot_und_rat_5_3,rou_und_rat_6_3,slick_ste_rat_7_3,smoot_step_rat_8_3, rou_step_rat_9_3 = jr3_result[0],jr3_result[1],jr3_result[2],jr3_result[3],jr3_result[4],jr3_result[5],jr3_result[6],jr3_result[7],jr3_result[8],jr3_result[9],jr3_result[10],jr3_result[11],jr3_result[12],jr3_result[13],jr3_result[14],jr3_result[15],jr3_result[16],jr3_result[17]

            Qjr = sum_of_weighting(count_oj,polished_1,smooth_planar_2,rough_planar_3,slickensided_undulating_4,smooth_undulating_5,rough_undulating_6,slickensided_stepped_7,smooth_stepped_8,rough_stepped_9,pol_rat_1,smoot_rat_2,rou_rat_3,slick_rat_4,smoot_und_rat_5,rou_und_rat_6,slick_ste_rat_7,smoot_step_rat_8, rou_step_rat_9,polished_1_2,smooth_planar_2_2,rough_planar_3_2,slickensided_undulating_4_2,smooth_undulating_5_2,rough_undulating_6_2,slickensided_stepped_7_2,smooth_stepped_8_2,rough_stepped_9_2,pol_rat_1_2,smoot_rat_2_2,rou_rat_3_2,slick_rat_4_2,smoot_und_rat_5_2,rou_und_rat_6_2,slick_ste_rat_7_2,smoot_step_rat_8_2, rou_step_rat_9_2,polished_1_3, smooth_planar_2_3, rough_planar_3_3, slickensided_undulating_4_3, smooth_undulating_5_3, rough_undulating_6_3, slickensided_stepped_7_3, smooth_stepped_8_3, rough_stepped_9_3,pol_rat_1_3,smoot_rat_2_3,rou_rat_3_3,slick_rat_4_3,smoot_und_rat_5_3,rou_und_rat_6_3,slick_ste_rat_7_3,smoot_step_rat_8_3, rou_step_rat_9_3)
            print("Selected Roughness: ",Qjr)

            new_row = {'hole_id': i,'from': from_1,'to': to_1, 'Oj1': jr1_count, 'Jr1': jr1, 'Oj2': jr2_count, 'Jr2': jr2, 'Oj3': jr3_count, 'Jr3': jr3, 'Selected Jr': Qjr}
            QJr = QJr.append(new_row,ignore_index=True)
            
        else:
            new_row = {'hole_id': i,'from': from_1,'to': to_1, 'Oj1': 0, 'Jr1': '', 'Oj2': 0, 'Jr2': '', 'Oj3': 0, 'Jr3': '', 'Selected Jr': ''}
            QJr = QJr.append(new_row,ignore_index=True)
#QJr.to_csv('QJr_export.csv')
def convert_df(QJr):
    return QJr.to_csv(index=False).encode('utf-8')
csv = convert_df(QJr)

st.download_button("Press to Download",csv,"discontinuity_weighting.csv","text/csv",key='download-csv')
print('Data Export Complete')


# In[ ]:





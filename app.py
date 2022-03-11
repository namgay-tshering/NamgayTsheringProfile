#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random
from dash.exceptions import PreventUpdate
import plotly.express as px

import dash
from dash import Dash, dcc, html, Input, Output
from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, callback, dash_table


# In[2]:


df=pd.read_csv('Grade10.csv')
df1=pd.read_csv('Grade12.csv')


# In[3]:


df.astype(str)
df1.astype(str)


# In[4]:


def scoreinfo(Grade):
    
    if (Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        highestscore = k.max()[2]
        highestscore
        
        grpscore = k.groupby(['Name','Subject']).sum()['Score']
        sub_nam = grpscore.idxmax()[1]
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        highestscore = k.max()[2]
        highestscore
        
        grpscore = k.groupby(['Name','Subject']).sum()['Score']
        sub_nam = grpscore.idxmax()[1]

    return [sub_nam,highestscore]


# In[5]:


def scoreinfo1(Grade):
    
    if (Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        highestscore1 = n.max()[2]
        highestscore1
        
        grpscore = n.groupby(['Name','Subject']).sum()['Score']
        sub_nam1 = grpscore.idxmax()[1]
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        highestscore1 = n.max()[2]
        highestscore1
        
        grpscore = n.groupby(['Name','Subject']).sum()['Score']
        sub_nam1 = grpscore.idxmax()[1]
        
    return [sub_nam1,highestscore1]


# In[6]:


def avg(Grade):
    
    if (Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        k.sort_values('Score', ascending=False,inplace=True)
        kk=k.head(5)
        kavg=kk.mean()
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        k.sort_values('Score', ascending=False,inplace=True)
        kk=k.head(5)
        kavg=kk.mean()

    return kavg


# In[7]:


def avg1(Grade):
    
    if (Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        n.sort_values('Score', ascending=False,inplace=True)
        nn=n.head(5)
        kavg1=nn.mean()
       
    
    else:
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        n=df2[df2['Name']=='Namgay']
        n.sort_values('Score', ascending=False,inplace=True)
        nn=n.head(5)
        kavg1=nn.mean()

    return kavg1


# In[8]:


def gradedata(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg3 = df1[['Name','Subject','Score']].copy()
        df4 = gg3.groupby(['Name','Subject']).sum()[['Score']]
        df4.reset_index(inplace=True)
        k12=df4[df4['Name']=='Kiran']
        
    else:
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Subject','Score']].copy()
        df2 = gg1.groupby(['Name','Subject']).sum()[['Score']]
        df2.reset_index(inplace=True)
        k=df2[df2['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg3 = df1[['Name','Subject','Score']].copy()
        df4 = gg3.groupby(['Name','Subject']).sum()[['Score']]
        df4.reset_index(inplace=True)
        k12=df4[df4['Name']=='Kiran']
        
    return[k,k12]


# In[9]:


def gradedata1(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg2 = df[['Name','Subject','Score']].copy()
        df3 = gg2.groupby(['Name','Subject']).sum()[['Score']]
        df3.reset_index(inplace=True)
        n=df3[df3['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg4 = df1[['Name','Subject','Score']].copy()
        df5 = gg4.groupby(['Name','Subject']).sum()[['Score']]
        df5.reset_index(inplace=True)
        n12=df5[df5['Name']=='Namgay']
    else:
        df=pd.read_csv('Grade10.csv')
        gg2 = df[['Name','Subject','Score']].copy()
        df3 = gg2.groupby(['Name','Subject']).sum()[['Score']]
        df3.reset_index(inplace=True)
        n=df3[df3['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg4 = df1[['Name','Subject','Score']].copy()
        df5 = gg4.groupby(['Name','Subject']).sum()[['Score']]
        df5.reset_index(inplace=True)
        n12=df5[df5['Name']=='Namgay']

        
    return[n,n12]


# In[10]:


def mapdata(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        kmap10=gg1[gg1['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        kmap12=gg1[gg1['Name']=='Kiran']
        
    else:
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        kmap10=gg1[gg1['Name']=='Kiran']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        kmap12=gg1[gg1['Name']=='Kiran']
        
    return[kmap10,kmap12]


# In[11]:


def mapdata1(Grade):
    if(Grade=='10th grade'):
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        nmap10=gg1[gg1['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        nmap12=gg1[gg1['Name']=='Namgay']
        
    else:
        df=pd.read_csv('Grade10.csv')
        gg1 = df[['Name','Lat','Long','Dzongkhag']].copy()
        nmap10=gg1[gg1['Name']=='Namgay']
        
        df1=pd.read_csv('Grade12.csv')
        gg1 = df1[['Name','Lat','Long','Dzongkhag']].copy()
        nmap12=gg1[gg1['Name']=='Namgay']
        
    return[nmap10,nmap12]


# In[12]:


def getkiran():
    df10 = df[df['Name']=="Kiran"]
    df10 = df[df['Name']=="Kiran"]
    df12 = df1[df1['Name']=="Kiran"]
    dfk = pd.concat([df10, df12])
    return dfk


# In[13]:


def getnamgay():
    df10 = df[df['Name']=="Namgay"]
    df10 = df[df['Name']=="Namgay"]
    df12 = df1[df1['Name']=="Namgay"]
    dfn = pd.concat([df10, df12])
    return dfn


# In[14]:


def drawfig(Grade):
    [k,k12]=gradedata(Grade)
    [kmap10,kmap12]=mapdata(Grade)
    if(Grade=='10th grade'):
        fig1 = px.bar(k, x='Subject', y='Score',color='Subject',title='Grade 10 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range = [0,100])
        
        fig2 = px.scatter_mapbox(kmap10, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
        
        
    else:
        fig1 = px.bar(k12, x='Subject', y='Score',color='Subject',title='Grade 12 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range = [0,100])
        
        fig2 = px.scatter_mapbox(kmap12, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
        
    return[fig1,fig2]     


# In[15]:


def drawfig1(Grade):
    [n,n12]=gradedata1(Grade)
    [nmap10,nmap12]=mapdata1(Grade)
    if(Grade=='10th grade'):
        fig1 = px.bar(n, x='Subject', y='Score',color='Subject',title='Grade 10 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range = [0,100])
        
        fig2 = px.scatter_mapbox(nmap10, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
    else:
        fig1 = px.bar(n12, x='Subject', y='Score',color='Subject',title='Grade 12 Score(100)',text='Score',width=700,height=500)
        fig1.update_yaxes(range = [0,100])
        
        fig2 = px.scatter_mapbox(nmap12, lat="Lat", lon="Long", color="Dzongkhag")
        fig2.update_layout(mapbox_style="open-street-map")
    return[fig1,fig2] 


# In[16]:


app = JupyterDash(external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME])
app.title = "Result Report of Examination"
server=app.server


# In[17]:


Grade= ['10th grade','12th grade']
app.layout = dbc.Container([
    
    html.H1("Grade Report",style={'textAlign':'center','color':'#3498db','fontsize':50}),
    
    dbc.Card(
        [
        dbc.CardImg(src="https://lh3.google.com/pw/AM-JKLXtgbEPhDMv4pTELI23AtEkqTEGgmYTJsb5bV5eUZZqGBNJlBlkUBM-GYVaAqODhxv-bI1webVai6TXEdQWQWLA9Z3NFHE=w1139-h854-no?authuser=0", top=True),
        dbc.CardBody(
            [
                html.H2("BCSE and BHSCE Examination Marks", className="card-title"),
                html.P(
                    "Marks scored by Kiran and Namgay  "
                    "During Middle and High School Days.",
                    className="card-text",
                ),
                dbc.Button("Namgay Middle school", color="#66BFBF",href='https://www.facebook.com/chumigthang/?__tn__=%3C'),
                dbc.Button("Kiran Middle school", color="#66BFBF",href='https://www.facebook.com/Bajohssw/?__tn__=%3C'),
                dbc.Button("Namgay High school", color="#66BFBF",href='https://www.facebook.com/NorbuAcademy/?ref=page_internal'),
                dbc.Button("Kiran High school", color="#66BFBF",href='https://www.facebook.com/groups/42276304044/'),
            ]
        ),
    ],
    style={"display": "flex", "flexWrap": "wrap"},
    ),
        
        

        
        html.Div(
    [
        dbc.Spinner(color="primary"),
        dbc.Spinner(color="secondary"),
        dbc.Spinner(color="success"),
        dbc.Spinner(color="warning"),
        dbc.Spinner(color="danger"),
        dbc.Spinner(color="info"),
        dbc.Spinner(color="light"),
        dbc.Spinner(color="dark"),
    ]
),

        dbc.Tabs([
                dbc.Tab(label="Namgay Tshering", tab_id="namgay"),
                dbc.Tab(label="Kiran Gurung", tab_id="kiran"),
            ],id="tabs",active_tab="namgay",

    ),
        
        html.Div([
        html.H2('Grade',style={'textAlign':'left','color':'#3498db','fontsize':40}),
        # create drop down
            dcc.Dropdown(id='grade_id',clearable=False,
                    options=[{'label':i,'value':i} for i in Grade],
                    placeholder='' ,
                    style={'width':'40%','padding':'3px','fontsize':40}),

        html.Div([
            html.H2('Highest Score Subject',style={'textAlign':'center','color':'#3498db','fontsize':10}),
            html.Div(id='numOf_id', style={'height': 20, 'textAlign':'center', 'fontsize':15,
                        'border-color': 'red','background-color': '#010b12','margin-left': '20px'}), 
        ], id = 'num_box', style = {"width": "30%", 'padding': 5}),


        html.Div([
            html.H2('Highest Mark',style={'textAlign':'center','color':'#3498db','fontsize':10}),
            html.Div(id='major_id', style={'height': 20, 'textAlign':'center', 'fontsize':15,
                           'border-color': 'red','background-color': '#010b12','margin-left': '20px'}), 
        ], id = 'mark_box', style = {"width": "30%", 'padding': 5}),
       
        html.Div([
            html.H2('Avarage Score(Top 5)',style={'textAlign':'center','color':'#3498db','fontsize':10}),
            html.Div(id='score_id', style={'height': 20, 'textAlign':'center', 'fontsize':15,
                           'border-color': 'red','background-color': '#010b12','margin-left': '20px'}), 
        ], id = 'score_box', style = {"width": "30%", 'padding': 5}),

    ], style = {'display': 'flex'}),

     html.Br() , 

    #5th division
    html.Div([
        dcc.Graph(id='plot1'),
        dcc.Graph(id='plot2'),
        
        ], style = {'display': 'flex'}),
    
        html.Div([
        dbc.Tabs([
            dbc.Tab(label="Kiran", tab_id="kiran"),
            dbc.Tab(label="Namgay", tab_id="namgay"),
            dbc.Tab(label="Grade 10", tab_id="G10"),
            dbc.Tab(label="Grade 12", tab_id="G12"),
            
        ],id="tabs1",active_tab="kiran"),
    ]),
        
    html.Div(id="table"),

    ] 
)


# In[18]:


@app.callback(
    Output("table", "children"),
    Input('tabs1','active_tab'),
)

def make_table(atab):
    if (atab =='kiran'):
        df = getkiran()
    elif(atab == 'namgay'):
        df = getnamgay()
    elif(atab=='G10'):
        df = pd.read_csv('Grade10.csv')
    else:
        df = pd.read_csv('Grade12.csv')
        
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, color = "primary", hover=True)


# In[19]:


@app.callback([
    Output('numOf_id','children'),
    Output('major_id','children'),
    Output('score_id','children'),
    Output('plot1','figure'),
    Output('plot2','figure'),
],[Input('grade_id','value'),
Input('tabs','active_tab'),])
def update_graphs(Grade,tabs):
    
    if Grade is None or tabs is None:
        raise PreventUpdate
        
    elif(tabs=='namgay'):
        [op1,op2]=scoreinfo1(Grade)
        [op3]=avg1(Grade)
        [fig1,fig2]=drawfig1(Grade)
        
    elif(tabs=='kiran'):
        [op1,op2]=scoreinfo(Grade)
        [op3]=avg(Grade)
        [fig1,fig2]=drawfig(Grade)

    else:
        op1='Economics IT'
        op2=75
        [fig1,fig2]=drawfig(Grade)
            
    return [op1,op2,op3,fig1,fig2]


# In[20]:


if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)    
    url = "http://127.0.0.1:{0}".format(port)    
    app.run_server(use_reloader=False, debug=True, port=port)


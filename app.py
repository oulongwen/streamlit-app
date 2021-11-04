import pandas as pd
import streamlit as st
import plotly.express as px
from openpyxl import load_workbook
import formulas
import streamlit.components.v1 as components
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


# from PIL import image

import tableauserverclient as TSC

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

server = TSC.Server('https://prod-useast-b.online.tableau.com', use_server_version=True)
tableau_auth = TSC.PersonalAccessTokenAuth('streamlit-app-testing','2Qkrwe2XTXScKZEkOFr47Q==:aebWT5tlM4SKwtioGVwHVVodn5XHsOo5', 'thisisatestsite')
server.auth.sign_in_with_personal_access_token(tableau_auth)

st.set_page_config(page_title='Test page')

st.title("LCA results")

uploaded_file = st.file_uploader("Upload LCI file")
ph = st.empty()
# html_temp = """
# <div class='tableauPlaceholder' id='viz1635994783808' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ta&#47;tableautest_16359947046400&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='tableautest_16359947046400&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ta&#47;tableautest_16359947046400&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1635994783808');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1500px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1500px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
# """
st.header('Pathway name')
html_temp = """
<script type='text/javascript' src='https://prod-useast-b.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 1000px; height: 827px;'><object class='tableauViz' width='1000' height='827' style='display:none;'><param name='host_url' value='https%3A%2F%2Fprod-useast-b.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;thisisatestsite' /><param name='name' value='googledrivetest2&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>
"""
# placeholder = st.empty()
components.html(html_temp, width=2000, height=1200)

# components.iframe("https://prod-useast-b.online.tableau.com/t/thisisatestsite/views/googledrivetest2/Dashboard1?:showAppBanner=false&:display_count=n&:showVizHome=n&:origin=viz_share_link")


if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # st.write(os.listdir('/'))
    # st.write(os.listdir('/tmp'))
    df.to_excel('/tmp/test.xlsx', index=False)
    upload_file_list = ['/tmp/test.xlsx']

    file_list = drive.ListFile({'q':"'1Ioa8OO8Gll4cFl_-z8wA1i0P89IpJ92W' in parents and trashed=False"}).GetList()
    # for x in range(len(file_list)):
    #     # if file_list[x]['title'] == 'Sample data22.xlsx':
    #     #     st.write(file_list[x]['id'])
    #     st.write(file_list[x]['title'], file_list[x]['id'])
    # st.write(os.listdir('/tmp'))
    for upload_file in upload_file_list:
        gfile = drive.CreateFile(
            {
                'parents': [{'id': '1Ioa8OO8Gll4cFl_-z8wA1i0P89IpJ92W'}], 
                'title': "Sample data22.xlsx",
                'id': '1Q105BwUlwLfadQRq0zVsKSEDpdEEN8u3'
            })
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload()
    ph.write("Data source updated. Please refresh the visualization.")
#1AZ9Empft2v3YuINBToqNMlVdITPwny9e

# 1IqdEpAvGgeVsxATpiLEMrXDfv_Dl8BLc
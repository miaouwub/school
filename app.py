import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time
import dotenv
import os

#----------------------------------------------------------------




with st.sidebar:
    choice = st.selectbox(
        "選擇操作", ['圖表.1','第一章','GPT'])
        
#圖表
if choice=='圖表.1':
    st.image('https://pbs.twimg.com/media/GfI_wgIaoAANz64.jpg')
    st.image('https://pbs.twimg.com/media/GfI_wgIa4AA_OaW.jpg')


if choice=='第一章':
    st.title('第一章')
    st.write('## 壹、前言')
    st.write('##### 土地婆在台灣民間信仰中是一位重要的女神，與土地公相輔相成， 她被信徒視為賜福的象徵，能夠帶來富貴與幸福，台灣各地都有土地公廟，但是有土地婆的廟卻寥寥無幾，大部分集中在桃園市，究竟為什麼土地婆的信仰人數如此稀少呢？是因為土地公仁民愛物而深得民心，相對土地婆因擔心土地公變成爛好人而阻擋土地公有求必應的做法，被部分信眾所討厭。')
    st.write('##### 但是在桃園區的土地婆通常被視為富貴的象徵，這種正面的形象使得信徒更願意供奉她，光是桃園區的土地公廟中就有近三分之一供奉著土地婆神尊，地婆的信仰也反映了對女性角色的重視，這在當地的社會文化中具有重要意義。')
    st.write('## 二、研究動機與目標')
    st.write('##### - **動機**：當我們在新聞中看到信仰土地婆的人很少的時候，就去搜尋為什麼台灣人不太信奉土地婆，才發現有一些故事，導致土地婆名聲不太好，因此想做個遊戲宣傳一下土地婆，一方面是想創造遊戲，一方面是想讓大家認識土地婆')
    st.write('##### - **目標**：讓土地婆文化與遊戲結合，增加介紹土地婆的趣味性，使其能夠邊輕鬆地玩遊戲，邊介紹土地婆')
    st.write('##### - **想做的事**：VR、MR 拜供品 變身土地公、做土地婆阻擋土地公當爛好人的小game ')
    st.write('##### - **祭拜**：->點兩柱香依序參拜：->天公爐（第一柱香）->主爐（第二柱香）->正殿供主祀開漳聖王、合祀武財神、觀世音菩薩、天上聖母、諸佛菩薩與眾神明->金母殿奉祀金母娘娘與眾神明->月老殿奉祀月老神君->註生殿奉祀註生娘娘與十二婆姐等神明->至聖殿奉祀至聖先師、文昌帝君、魁星爺->依參拜順序參拜完即可輕輕敲響祈福鐘->金紙部除了金紙有販售一些小紀念品及藝術文創商品->現場可以求平安符及平安米')
    st.write('## 叁、宣傳目的')
    st.write('##### - **文化傳承**：強調土地婆作為中國民間信仰的重要標誌，致力於保護和傳承地方文化與習俗。')
    st.write('##### - **教堂**：宣傳土地婆能夠促進社區居民之間的聯繫，增強社區的聚集力，讓人們在祭拜過程中團結互助。 ，提供心理上的關懷和支持，幫助人們面對生活中的困難。活動5. **環保意識**：結合土地對土地的守護理念，倡導環保和永續發展的概念，讓更多人關注環境保護。by: chatgpt')
    st.write('## 肆、製作過程中有甚麼困難')
    st.write('##### 1.遊戲製作軟體')
    st.write('##### 2.遊戲程式語言')
    st.write('##### 3.模型製作')
    st.write('##### 4.沒老師教')
    st.write('##### 5.只能看影片')

if choice=='GPT':
    dotenv.load_dotenv()
    api_key = os.getenv("OPENAI_KEY")
    user_input = st.text_input("輸入對話:")    
    # 當使用者點擊 "送出" 按鈕時觸發
    if st.button("送出"):
        # 顯示用戶訊息
        with st.chat_message("user"):
            st.write(user_input)
        # 設定聊天區域，用於顯示 GPT 回應
        with st.chat_message("assistant"):
            output_placeholder = st.empty()
            # 創建 OpenAI 客戶端
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            # 呼叫 OpenAI API 並啟用串流模式
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": user_input}],
                stream=True,
            )
            # 逐步顯示 GPT 回應
            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    output_placeholder.markdown(full_response)

                    stream = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": user_input}],
                    stream=True,
                )

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time
import dotenv
import os

#----------------------------------------------------------------




with st.sidebar:
    choice = st.selectbox(
        "MENU", ['前言','圖表','遊戲','文書第一章','GPT'])

if choice=='遊戲':
    st.image('https://i.ibb.co/HjfYMN5/22.jpg')
    st.image('https://i.ibb.co/sJPZMsxT/23.jpg')
    st.image('https://i.ibb.co/21byC45L/24.jpg')
    st.image('https://i.ibb.co/8gYrbzvB/25.jpg')
    st.image('https://i.ibb.co/qYQcLBb3/26.jpg')
    st.image('https://i.ibb.co/PZc2hgps/27.jpg')
    st.image('https://i.ibb.co/Txc64Q7y/28.jpg')
    st.image('https://i.ibb.co/hF86WNXG/29.jpg')
    st.image('https://i.ibb.co/9mtK8NbL/30.jpg')
    st.video('https://youtu.be/PkVSpu131_8')
    


if choice=='前言':
    st.write('## 研究動機')
    st.write('##### 由報導指出，土地婆在一般民眾心中，不甚討好，然而')
    st.write('##### 在桃園仍有近1/3的廟宇供奉土地婆。因此希望藉由遊戲與介紹推廣伯婆文化')
    st.write('##### 同時也希望，無論是現實生活或是文化上，消除對女性的各種形式的歧視。')
    st.write('## 研究目的')
    st.write('##### （一）了解土地婆文化及土地婆供奉率低下之原因')
    st.write('##### （二）用文獻資料、訪談與問卷，分析土地婆祭祀文化在台灣供奉率低的原因')
    st.write('##### （三）運用Unity遊戲引擎學習製作遊戲及Streamlit製作網站')
    st.write('##### （四）藉由遊戲的趣味性宣傳來增加土地婆的知名度')
    st.write('### 一、土地婆文化概述')
    st.write('##### 1. 定義與角色')
    st.write('土地婆，又稱土地奶奶、土地嬤，是土地公的配偶，屬於台灣及華人民間信仰中的地方守護神祇。 ')
    st.write('雖然在官方神明系統中較少見，但在部分民間信仰中有供奉，象徵陰陽平衡、家庭和諧與女性力量。')
    st.write('土地婆常被視為掌管家庭財庫、庇佑女性與孩童，亦象徵農業社會中的「賢內助」。')
    st.write('##### 2. 起源與信仰 ')
    st.write('根源可能來自於母系社會信仰遺留或女性神格的補充形象。 ')
    st.write('土地公信仰興盛後，部分地區為補足性別與家庭形象，加入土地婆作為配偶神明。 ')
    st.write('### 二、土地婆供奉率低的原因 ')
    st.write('##### 1. 性別文化因素')
    st.write('傳統社會中男性神明居主導地位，如土地公、城隍爺、關公等。 ')
    st.write('土地婆常被視為附屬角色，缺乏主神地位，導致關注與供奉度低。 ')
    st.write('##### 2. 文獻記載稀少 ')
    st.write('地方志與宗教典籍多記錄土地公，對土地婆的描寫與祭祀流程少，難以成為主流信仰。 ')
    st.write('缺乏歷史故事與神蹟傳說的加持，信徒較難產生信仰連結。')
    st.write('##### 3. 廟宇空間與形象設置 ')
    st.write('多數土地公廟僅供奉土地公，有土地婆者多僅附設於旁，甚至形象模糊（有時僅一小石或無神像）。')
    st.write('##### 4. 現代社會功能弱化 ')
    st.write('現代人生活與信仰功能改變，土地婆象徵的農耕、家務管理等意義被削弱。')         
    st.write('女性守護神角色漸被媽祖、註生娘娘等更知名的神祇取代。 ')
    st.write('##### 5. 宗教教育與宣傳不足 ')
    st.write('社會與宗教團體對土地婆的介紹與教育不多，缺乏祭典活動的推廣與儀式設計。 ')
    st.write('僅在特定地區或民俗活動中出現，影響其普遍信仰基礎。 ')         
    st.write('### 三、地方案例與文化保存 ')
    st.write('南投、苗栗、嘉義等部分農村地區仍有供奉土地婆的傳統，且在部分鄉土教材與宗教研究中被重新關注。 ')
    st.write('近年一些文史團體與宗教文化復興者，開始重新挖掘女性神祇，土地婆逐漸被重新認識。 ')         
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')         
    st.write(' ')         


             





             
#圖表
if choice=='圖表':
    st.write('# 桃園市各廟宇主祀神祇比例')
    st.write('##### 以下是從桃園市資料開放平台蒐集的.json資料，並用pyplot分析過的長條圖')
    st.write('##### 其中顯示出了福德正神是桃園主祀神祇占比最多的神祇。')
    st.image('https://i.ibb.co/F4bh2Jbx/Figure-1.png')
    st.image('https://pbs.twimg.com/media/GfI_wgIaoAANz64.jpg')
    st.image('https://pbs.twimg.com/media/GfI_wgIa4AA_OaW.jpg')
    st.image('https://pbs.twimg.com/media/GpMG0cua4AE4etz.jpg')
    st.write('上圖為台灣五大公廟分布圖')
    st.write('1.屏東車城 - 福安宮 台灣最大土地公廟分布圖')
    st.write('2.新北中和 - 南山福德宮 北台灣土地公信仰中心')
    st.write('3.宜蘭四結 - 福德廟 台灣最大金身土地公')
    st.write('4.台中 - 惠來里福德祠 全市地價最高土地公廟')
    st.write('5.桃園 - 土地公文化館 桃園區土地公廟密度全國第一')











if choice=='文書第一章':
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

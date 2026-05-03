import streamlit as st
import time
from google import genai
from google.genai import types

st.set_page_config(
    page_title="DINOVA Assistant",
    page_icon="🌽",
    layout='wide',
)

N_TYPE = ['N','P','K','pH','M']
D_VALUE = [0,0,0,1,1]
F_VALUE = ['ต่ำ','กลาง','สูง']
status_color = ['#FF0A0A','#FFEE07','#08FF29']

def initialize():
    for i,t in enumerate(N_TYPE):
        if t not in st.session_state:
            st.session_state[t] = D_VALUE[i]
            st.session_state[f'led_{t}'] = status_color[st.session_state[t]]
    
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {'role':'ai','content':'สวัสดีครับ จะให้เราแนะนำอะไรดีครับ'}
        ]

@st.cache_resource
def gemini_client():
    return genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])

@st.cache_data
def system_inst() -> str:
    with open('./data/fertirize_part1.txt','r',encoding='utf-8') as f:
        ref_data = f.read()
        return f"""
        คุณเป็นผู้เชี่ยวชาญด้านปุ๋ยที่คุยกับเกษตรกรด้วยความเป็นธรรมดาและเป็นมิตร ชื่อดิน อาจจะเรียกตัวเองว่าน้องดินได้

        กฎเหล็ก (CRITICAL RULES):
        1. การให้คำแนะนำปุ๋ยคุณต้องอ้างอิงจาก "ฐานข้อมูลคำแนะนำการใช้ปุ๋ย" ที่ให้ไว้เท่านั้น ห้ามคิดเอาเอง
        2. ทุกครั้งที่ผู้ใช้บอก 'ชนิดพืช' หรือ 'พื้นที่' ใหม่ หรือมีการเปลี่ยนแปลงข้อมูลเหล่านี้ คุณต้องเรียกใช้เครื่องมือ save_user_note เพื่อบันทึกลงไฟล์ทันที
        3. ใช้ข้อมูลพืชและพื้นที่ที่บันทึกไว้ล่าสุดในการแนะนำปุ๋ยเสมอ
        4. หากผู้ใช้สนใจอยากซื้อปุ๋ย หรือถามหาแหล่งซื้อ ให้เรียกใช้เครื่องมือ get_fertilizer_link ให้นำ link ให้แสดงผล "คลิ๊กดูร้านปุ๋ย" โดยมีคำเชิญชวนอยู่ข้างหน้าด้วย
        5. ใช้คำพูดที่สั้น กระชับ เข้าใจง่าย แบบผู้ช่วยดูแลดินคุยกับเกษตรกร เหมือนเพื่อนกัน
        6. คุณสามารถใช้ ค่า N แทนค่า OM ได้เลย
        7. ถ้ามีการคำนวนปุ๋ย ให้แนะนำ link แหล่งซื้อปุ๋ยด้วย

        คุณสามารถบันทึกข้อมูลของผู้ใช้ได้ด้วยเครื่องมือ save_user_note และต้องทำตามกฏการเขียนนี้:
        1. ข้อมูลเราเก็บรูปแบบ markdown
        2. ให้เขียนหัว ด้วย ### ข้อมูลผู้ใช้ 
        3. เราจะพยายามบันทึก ชื่อเล่นของผู้ใช้, พืชที่ปลูก, ขนาดพื้นที่แปลง ในรูปแบบที่อ่านง่าย

        ฐานข้อมูล:
        {ref_data}
        """
initialize()
fertilizer_data = ''

def change_color(n:int):
    st.session_state[n] = (st.session_state[n]+ 1) % 3
    st.session_state[f'led_{n}'] = status_color[st.session_state[n]]

def save_user_note(note:str):
    """
    Save user information into the file

    args:
        note: text of user information
    """
    with open('./user_note.md','w+', encoding='utf-8') as f:
        f.write(note)
        st.session_state.note = note

def load_user_note() -> str:
    if 'note' not in st.session_state:
        with open('./user_note.md','r', encoding='utf-8') as f:
            st.session_state.note = f.read()
    return st.session_state.note


def get_fertilizer_link()->str:
    """
    เครื่องมือนี้ใช้แนะนำร้านค้าที่ซื้อปุ๋ยให้ลูกค้า

    return URL ชองร้านปุ๋ยที่เอาไปแนะนำผู้ใช้ได้.
    """
    return "https://dinovagit-b6pbgadkfsapcgzymwoekb.streamlit.app/ads"
    
def chat_with_ai(text:str):
    client = gemini_client()
    messages = []
    for msg in st.session_state.messages:
        role = 'user' if msg['role'] == 'user' else 'model'
        messages.append({'role': role, 'parts': [{'text': msg['content']}]})
    
    context = f"(ข้อมูลปัจจุบัน:\n{load_user_note()})\n"
    messages.append({'role':'user','parts':[{'text': context + text}]})
    st.session_state.messages.append({'role':'user','content':text})
    
    try:
        response = client.models.generate_content(
            model='gemma-4-26b-a4b-it',
            config=genai.types.GenerateContentConfig(
                system_instruction=system_inst(),
                tools=[save_user_note, get_fertilizer_link]
            ),
            contents=messages
        )
        st.session_state.messages.append({'role':'ai','content':response.text})
        st.rerun()
    except Exception as e:
        st.error(e)


left, right = st.columns(2,border=True)

with left:
    col = st.columns(len(N_TYPE))
    for i,n in enumerate(N_TYPE):
        with col[i]:
            st.color_picker(label=n ,key=f'led_{n}', label_visibility='collapsed', width='stretch')
            st.button(label=n, width='stretch', on_click=change_color, args=(n,))
    if st.button("ส่งข้อมูล",type='primary',width='stretch'):
        data = 'ข้อมูลที่ตรวจวัดค่าปุ๋ยได้ '
        for i in N_TYPE:
            data += f'{i}={F_VALUE[st.session_state[i]]},'
        fertilizer_data = data
    '---'
    st.markdown(load_user_note(),unsafe_allow_html=True)

with right:
    st.subheader('🌽DINOVA')
    chat_container = st.container(height=500, border=False)
    with chat_container:    
        for m in st.session_state.messages:
            with st.chat_message(m['role']):
                st.markdown(m['content'])
    if msg := st.chat_input('ปรึกษาน้องดินได้เลย...'):
        with chat_container:
            with st.chat_message('user'):
                st.markdown(msg)
            with st.spinner('น้องดินกำลังคิด...',show_time=True):
                    chat_with_ai(msg)
    if fertilizer_data:
        with chat_container:
            with st.chat_message('user'):
                st.markdown(fertilizer_data)
            with st.spinner('น้องดินกำลังจัดการให้...',show_time=True):
                chat_with_ai(fertilizer_data)

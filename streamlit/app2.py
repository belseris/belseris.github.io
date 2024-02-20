import streamlit as st
st.header('MY OOP')
st.subheader('เว็บไซต์ส่วนตัวของฉัน')
st.write('เว็บไซต์นี้เเลกหยาดเหงื่อเเละความอดทน')
banner = st.image('https://picsum.photos/800/250')
text = st.text_input('prompt: ')
if text:
    # st.write(f'กำลังสร้างภาพ...."{text}"')
    st.image('https://picsum.photos/800/250')
    b = st.button('จะไปต่อหรือ...')





# st.title('OOP in ML')
# st.sideber.text('Sidebre')
# st.sideber.button('go>')
# st.sideber.button('went>')
# st.sideber.button('gone>')
# st.title('OOP in ML')
# st.image('bl1.jpy/500/600')
# st.text_input("What's your name")


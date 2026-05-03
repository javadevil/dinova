import streamlit as st

st.set_page_config(
    page_title="DINOVA Shop - แหล่งรวมปุ๋ยคุณภาพ",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS for Rich Aesthetics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&family=Sarabun:wght@400;600&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Sarabun', sans-serif;
        background: linear-gradient(135deg, #0f172a 0%, #022c22 100%);
        color: #f8fafc;
    }
    
    .hero-section {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #10b981, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #cbd5e1;
        margin-bottom: 20px;
    }
    
    .product-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 20px;
        transition: all 0.3s ease;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(16, 185, 129, 0.3);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .product-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #34d399;
        margin: 15px 0 5px 0;
    }
    
    .product-desc {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-bottom: 15px;
        flex-grow: 1;
    }
    
    .product-price {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 15px;
    }
    
    .badge-promo {
        background: linear-gradient(90deg, #f59e0b, #ef4444);
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Hero Banner
st.markdown("""
<div class="hero-section">
    <div class="hero-title">DINOVA Fertilizer Shop</div>
    <div class="hero-subtitle">ศูนย์รวมปุ๋ยพรีเมียม เพื่อผลผลิตที่งอกงามสำหรับเกษตรกรไทย</div>
</div>
""", unsafe_allow_html=True)

col_hero_img, col_hero_txt = st.columns([3, 2])
with col_hero_img:
    st.image("C:/Users/nkimm/.gemini/antigravity/brain/086dbc16-eddd-431c-b101-cd5cdd0aa125/fertilizer_shop_hero_1777385646501.png", use_container_width=True, caption="ความอุดมสมบูรณ์ที่คุณเลือกได้")
with col_hero_txt:
    st.markdown("""
    ### ทำไมต้องเลือกปุ๋ย DINOVA?
    - **สูตรเข้มข้น:** ผลิตจากวัตถุดิบคุณภาพสูง ละลายน้ำง่าย พืชดูดซึมได้ทันที
    - **ตอบโจทย์ทุกช่วงวัย:** ไม่ว่าจะเร่งต้น เร่งใบ เร่งดอก หรือขยายผล
    - **ประหยัดต้นทุน:** ใช้ปริมาณน้อยลง แต่ได้ผลผลิตเพิ่มขึ้น
    
    *สั่งซื้อวันนี้ รับส่วนลดพิเศษและคำแนะนำการใส่ปุ๋ยฟรีจากระบบ AI อัจฉริยะ*
    """)
    st.button("รับส่วนลดพิเศษ 🎁", type="primary", width='stretch')

st.write("---")
st.markdown("### 📦 เลือกซื้อปุ๋ยตามสูตรที่เหมาะสม")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="product-card">
        <span class="badge-promo">ขายดีอันดับ 1</span>
        <div class="product-title">ปุ๋ยสูตรเสมอ NPK 15-15-15</div>
        <div class="product-desc">บำรุงต้น ใบ ดอก และผล ให้เติบโตอย่างสม่ำเสมอ เหมาะสำหรับพืชทุกชนิด</div>
        <div class="product-price">฿ 850 / กระสอบ</div>
    </div>
    """, unsafe_allow_html=True)
    st.image("C:/Users/nkimm/.gemini/antigravity/brain/086dbc16-eddd-431c-b101-cd5cdd0aa125/fertilizer_product_npk_1777385675511.png", use_container_width=True)
    st.button("เลือกใส่ตะกร้า (15-15-15)", key="buy_15", width='stretch')

with col2:
    st.markdown("""
    <div class="product-card">
        <span class="badge-promo">เร่งต้น เร่งใบ</span>
        <div class="product-title">ปุ๋ยยูเรีย NPK 46-0-0</div>
        <div class="product-desc">เพิ่มความเขียวขจี เร่งการเจริญเติบโตทางลำต้นและใบอย่างรวดเร็ว</div>
        <div class="product-price">฿ 750 / กระสอบ</div>
    </div>
    """, unsafe_allow_html=True)
    st.image("C:/Users/nkimm/.gemini/antigravity/brain/086dbc16-eddd-431c-b101-cd5cdd0aa125/fertilizer_shop_hero_1777385646501.png", use_container_width=True)
    st.button("เลือกใส่ตะกร้า (46-0-0)", key="buy_46", width='stretch')

with col3:
    st.markdown("""
    <div class="product-card">
        <span class="badge-promo">เร่งดอก เร่งผล</span>
        <div class="product-title">ปุ๋ยรับรวง NPK 8-24-24</div>
        <div class="product-desc">สะสมอาหารเพื่อการออกดอก สร้างเนื้อ ขยายขนาดผล เพิ่มความหวาน</div>
        <div class="product-price">฿ 980 / กระสอบ</div>
    </div>
    """, unsafe_allow_html=True)
    st.image("C:/Users/nkimm/.gemini/antigravity/brain/086dbc16-eddd-431c-b101-cd5cdd0aa125/fertilizer_product_npk_1777385675511.png", use_container_width=True)
    st.button("เลือกใส่ตะกร้า (8-24-24)", key="buy_8",width='stretch')

st.write("---")
if st.button("⬅️ กลับสู่ระบบผู้ช่วย DINOVA Assistant", width='stretch'):
    st.switch_page("app_fer.py")
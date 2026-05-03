import streamlit as st

st.set_page_config(
    page_title="DINOVA Shop - แหล่งรวมปุ๋ยคุณภาพ",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS for Rich Aesthetics without external font imports
st.markdown("""
<style>
    /* 
       No external resources (no external fonts or images) to comply with requirements.
       Using safe fallback fonts and system emojis.
    */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #0f172a 0%, #022c22 100%);
        color: #f8fafc;
    }
    
    .hero-section {
        background: linear-gradient(120deg, rgba(16, 185, 129, 0.15), rgba(255, 255, 255, 0.02));
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        padding: 60px 40px;
        border: 1px solid rgba(16, 185, 129, 0.2);
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        position: relative;
        overflow: hidden;
    }

    .hero-section::before {
        content: "🌱";
        position: absolute;
        font-size: 15rem;
        opacity: 0.05;
        top: -50px;
        left: -20px;
        transform: rotate(-15deg);
    }
    
    .hero-section::after {
        content: "✨";
        position: absolute;
        font-size: 8rem;
        opacity: 0.05;
        bottom: 20px;
        right: 20px;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(to right, #34d399, #10b981, #059669);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: #e2e8f0;
        margin-bottom: 30px;
        font-weight: 300;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .feature-card {
        background: rgba(15, 23, 42, 0.6);
        border-left: 4px solid #10b981;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        transition: transform 0.3s ease, background 0.3s ease;
    }

    .feature-card:hover {
        transform: translateX(10px);
        background: rgba(16, 185, 129, 0.1);
    }
    
    .product-card {
        background: linear-gradient(180deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px 20px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        position: relative;
        overflow: hidden;
    }
    
    .product-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, transparent, #10b981, transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .product-card:hover {
        transform: translateY(-10px);
        border-color: rgba(16, 185, 129, 0.4);
        box-shadow: 0 15px 30px rgba(16, 185, 129, 0.15);
    }

    .product-card:hover::before {
        opacity: 1;
    }
    
    .product-icon {
        font-size: 5rem;
        margin-bottom: 20px;
        filter: drop-shadow(0 10px 10px rgba(0,0,0,0.3));
        transition: transform 0.5s ease;
    }

    .product-card:hover .product-icon {
        transform: scale(1.1) rotate(5deg);
    }

    .product-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #fff;
        margin: 10px 0;
        letter-spacing: 0.5px;
    }
    
    .product-desc {
        font-size: 1rem;
        color: #94a3b8;
        margin-bottom: 25px;
        line-height: 1.6;
        flex-grow: 1;
    }
    
    .product-price {
        font-size: 1.8rem;
        font-weight: 800;
        color: #34d399;
        margin-bottom: 20px;
        background: rgba(16, 185, 129, 0.1);
        padding: 10px;
        border-radius: 12px;
        display: inline-block;
    }
    
    .badge-promo {
        position: absolute;
        top: 15px;
        right: -30px;
        background: linear-gradient(90deg, #ef4444, #f59e0b);
        color: white;
        padding: 5px 40px;
        font-size: 0.85rem;
        font-weight: bold;
        transform: rotate(45deg);
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        z-index: 10;
    }

    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 40px 0;
        color: #fff;
        position: relative;
    }

    .section-title::after {
        content: '';
        display: block;
        width: 80px;
        height: 4px;
        background: #10b981;
        margin: 15px auto 0;
        border-radius: 2px;
    }

</style>
""", unsafe_allow_html=True)

# Hero Banner
st.markdown("""
<div class="hero-section">
    <div class="hero-title">DINOVA PRO SHOP</div>
    <div class="hero-subtitle">ยกระดับผลผลิตของคุณด้วยปุ๋ยพรีเมียมสูตรนวัตกรรม เพื่อเกษตรกรไทยยุคใหม่ที่ต้องการผลลัพธ์ที่ดีที่สุด</div>
</div>
""", unsafe_allow_html=True)

# Features Section
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("""
    <div style="padding: 20px; height: 100%; display: flex; flex-direction: column; justify-content: center;">
        <h2 style="color: #34d399; font-size: 2.2rem; margin-bottom: 20px;">ทำไมเกษตรกรมืออาชีพถึงเลือกเรา?</h2>
        <div class="feature-card">
            <h4 style="margin: 0; color: #fff;">🔬 นวัตกรรมสูตรเข้มข้น</h4>
            <p style="margin: 5px 0 0 0; color: #94a3b8;">ผลิตด้วยเทคโนโลยีขั้นสูง ละลายน้ำ 100% พืชดูดซึมไปใช้ได้ทันที</p>
        </div>
        <div class="feature-card">
            <h4 style="margin: 0; color: #fff;">🎯 ตรงจุดทุกช่วงการเจริญเติบโต</h4>
            <p style="margin: 5px 0 0 0; color: #94a3b8;">มีสูตรเฉพาะตั้งแต่เริ่มปลูก บำรุงต้น เร่งดอก ไปจนถึงขยายผล</p>
        </div>
        <div class="feature-card">
            <h4 style="margin: 0; color: #fff;">💰 คุ้มค่า ลดต้นทุน</h4>
            <p style="margin: 5px 0 0 0; color: #94a3b8;">ใช้ปริมาณน้อยลงกว่าเดิม 30% แต่ได้ผลผลิตเพิ่มขึ้นอย่างชัดเจน</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    # Creating an aesthetic design element without images using only CSS and text
    st.markdown("""
    <div style="background: radial-gradient(circle at center, rgba(16, 185, 129, 0.2) 0%, rgba(15, 23, 42, 0.5) 70%); border-radius: 24px; padding: 40px; text-align: center; border: 1px dashed rgba(52, 211, 153, 0.3); height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <div style="font-size: 6rem; margin-bottom: 20px; animation: float 3s ease-in-out infinite;">🏆</div>
        <h3 style="color: #fff;">การันตีคุณภาพ</h3>
        <p style="color: #cbd5e1; font-size: 1.1rem;">ได้รับความไว้วางใจจากเครือข่ายเกษตรกรกว่า 10,000 รายทั่วประเทศ</p>
        <style>
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-15px); }
                100% { transform: translateY(0px); }
            }
        </style>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">คอลเลกชันผลิตภัณฑ์ 📦</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="product-card">
        <div class="badge-promo">BEST SELLER</div>
        <div class="product-icon">⚖️</div>
        <div class="product-title">ปุ๋ยสูตรเสมอ NPK 15-15-15</div>
        <div class="product-desc">สูตรอเนกประสงค์ บำรุงครบถ้วนทั้ง ต้น ใบ ดอก และผล ให้เติบโตอย่างสมบูรณ์แบบ เหมาะกับพืชทุกชนิด</div>
        <div class="product-price">฿ 850<span style="font-size: 1rem; color: #64748b;"> / กระสอบ</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.button("🛒 เพิ่มลงตะกร้า (15-15-15)", key="buy_15", use_container_width=True)

with col2:
    st.markdown("""
    <div class="product-card">
        <div class="badge-promo" style="background: linear-gradient(90deg, #3b82f6, #06b6d4);">NEW</div>
        <div class="product-icon">🌿</div>
        <div class="product-title">ปุ๋ยยูเรีย NPK 46-0-0</div>
        <div class="product-desc">สูตรปลดปล่อยไว เพิ่มความเขียวขจี เร่งการเจริญเติบโตทางลำต้นและใบอย่างรวดเร็ว ฟื้นต้นโทรมได้ดี</div>
        <div class="product-price">฿ 750<span style="font-size: 1rem; color: #64748b;"> / กระสอบ</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.button("🛒 เพิ่มลงตะกร้า (46-0-0)", key="buy_46", use_container_width=True)

with col3:
    st.markdown("""
    <div class="product-card">
        <div class="badge-promo" style="background: linear-gradient(90deg, #8b5cf6, #d946ef);">PREMIUM</div>
        <div class="product-icon">🍎</div>
        <div class="product-title">ปุ๋ยรับรวง NPK 8-24-24</div>
        <div class="product-desc">สูตรเน้นผลผลิต สะสมอาหารเพื่อการออกดอก สร้างเนื้อ ขยายขนาดผล เพิ่มน้ำหนักและความหวาน</div>
        <div class="product-price">฿ 980<span style="font-size: 1rem; color: #64748b;"> / กระสอบ</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.button("🛒 เพิ่มลงตะกร้า (8-24-24)", key="buy_8", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.write("---")

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("⬅️ กลับสู่ระบบผู้ช่วย DINOVA Assistant", use_container_width=True, type="secondary"):
        st.switch_page("app_fer.py")
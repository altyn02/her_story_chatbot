import csv
import os
from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="Her Story",
    page_icon="🌸",
    layout="wide",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff8fb 0%, #fffdfd 100%);
    }
    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.2rem;
        padding: 0.4rem 0 0.8rem 0;
    }
    .brand-wrap {
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    .chatbot-icon {
        width: 100px;
        height: 100px;
        border-radius: 16px;
        background: linear-gradient(135deg, #ffb7d5 0%, #f4c7ff 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.7rem;
        box-shadow: 0 8px 24px rgba(255, 165, 204, 0.25);
    }
    .brand-title {
        font-size: 2rem;
        font-weight: 700;
        color: #5c3451;
        margin: 0;
    }
    .brand-sub {
        font-size: 0.98rem;
        color: #8a627b;
        margin: 0.15rem 0 0 0;
    }
    .hero {
        padding: 3rem 2rem;
        border-radius: 26px;
        background: linear-gradient(135deg, #ffe4ef 0%, #fdf1ff 55%, #fff8fb 100%);
        margin-bottom: 2rem;
        border: 1px solid #f8d6e5;
        box-shadow: 0 10px 30px rgba(240, 170, 205, 0.15);
    }
    .card {
        padding: 1.2rem;
        border-radius: 18px;
        background: #fffafb;
        border: 1px solid #f5dce8;
        min-height: 220px;
        box-shadow: 0 6px 20px rgba(240, 170, 205, 0.08);
    }
    .soft-box {
        padding: 1rem 1.2rem;
        border-radius: 16px;
        background: #fff0f6;
        border-left: 5px solid #f19ac0;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        color: #8b6a7d;
        font-size: 0.9rem;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Multilingual text
# -----------------------------
content = {
    "English": {
        "nav": ["Home", "About", "Our Service", "Target Users", "Future Vision", "Contact"],
        "hero_title": "🌸Her Story🌸",
        "hero_subtitle": "A supportive digital space for migrant women in Korea",
        "hero_text": (
            "Her Story is designed to support emotional well-being, reflection, and "
            "easier access to guidance through a multilingual and user-friendly digital service."
        ),
        "button_1": "Explore Our Service",
        "button_2": "Read Future Vision",
        "cards": [
            ("Multilingual Support", "Users can explore the platform in a language that feels comfortable and natural."),
            ("Reflection and Guidance", "The service is designed to support emotional expression, self-reflection, and practical guidance."),
            ("Accessible Experience", "A calm and welcoming interface helps users feel supported and included."),
        ],
        "about_title": "About 🌸Her Story🌸",
        "about_text": (
            "Her Story is a concept service created to support migrant and marriage migrant women living in South Korea. "
            "The project focuses on emotional support, self-expression, and accessible guidance."
        ),
        "service_title": "Our Service",
        "service_text": (
            "The service is planned as a multilingual digital support platform. "
            "It may include reflective writing support, practical guidance, emotional support, "
            "and future AI-assisted features."
        ),
        "target_title": "Who We Aim to Support",
        "target_text": (
            "Our main target users are migrant and marriage migrant women in Korea who may face language barriers, "
            "social isolation, cultural adjustment difficulties, or uncertainty in everyday life."
        ),
        "future_title": "Future Vision",
        "future_text": (
            "In the future, Her Story can grow into a more interactive platform with personalized guidance, "
            "community resources, multilingual content, and AI-supported reflection tools."
        ),
        "contact_title": "Contact",
        "contact_text": "For collaboration, pilot testing, or project inquiries, please contact the Her Story team.",
        "form_name": "Name",
        "form_email": "Email",
        "form_message": "Message",
        "form_button": "Submit",
        "form_success": "Thank you. Your message was saved successfully.",
        "footer": "Prototype website built with Streamlit.",
        "key_elements": "Key Elements",
        "why_matters": "Why It Matters",
        "primary_users": "Primary users: migrant and marriage migrant women in Korea",
        "key_elements_items": [
            "Reflection support",
            "Multilingual accessibility",
            "Gentle guidance",
            "Future AI-based features",
        ],
        "why_items": [
            "Reduces barriers",
            "Supports self-expression",
            "Makes guidance easier to access",
            "Creates a welcoming digital experience",
        ],
        "concept_stage": "Concept development stage",
        "brand_sub": "A gentle, multilingual support concept",
    },
    "한국어": {
        "nav": ["홈", "소개", "서비스", "대상 사용자", "향후 비전", "문의"],
        "hero_title": "🌸Her Story🌸",
        "hero_subtitle": "한국에 거주하는 이주여성을 위한 따뜻한 디지털 공간",
        "hero_text": (
            "Her Story는 다국어 기반의 사용자 친화적인 디지털 서비스를 통해 "
            "정서적 지원, 자기성찰, 그리고 유용한 정보 접근을 돕는 것을 목표로 합니다."
        ),
        "button_1": "서비스 보기",
        "button_2": "향후 비전 보기",
        "cards": [
            ("다국어 지원", "사용자가 더 편안하고 자연스러운 언어로 플랫폼을 이용할 수 있습니다."),
            ("성찰과 가이드", "감정 표현, 자기 성찰, 그리고 실질적인 안내를 지원하도록 설계되었습니다."),
            ("접근성 중심 경험", "차분하고 따뜻한 인터페이스를 통해 사용자가 안전함과 편안함을 느낄 수 있습니다."),
        ],
        "about_title": "🌸Her Story🌸 소개",
        "about_text": (
            "Her Story는 한국에 거주하는 결혼이주여성과 이주여성을 지원하기 위해 기획된 서비스입니다. "
            "이 프로젝트는 정서적 지원, 자기표현, 그리고 실질적인 안내에 더 쉽게 접근할 수 있도록 하는 데 초점을 둡니다."
        ),
        "service_title": "서비스 소개",
        "service_text": (
            "이 서비스는 다국어 디지털 지원 플랫폼으로 기획되었습니다. "
            "성찰적 글쓰기 지원, 실질적 안내, 정서적 지원, 그리고 향후 AI 기반 기능을 포함할 수 있습니다."
        ),
        "target_title": "주요 대상 사용자",
        "target_text": (
            "주요 대상은 한국에서 언어 장벽, 사회적 고립, 문화 적응의 어려움, "
            "일상 속 불확실성을 경험할 수 있는 이주여성 및 결혼이주여성입니다."
        ),
        "future_title": "향후 비전",
        "future_text": (
            "향후 Her Story는 개인 맞춤형 안내, 지역사회 자원, 다국어 콘텐츠, "
            "AI 기반 성찰 도구를 포함한 더 확장된 플랫폼으로 발전할 수 있습니다."
        ),
        "contact_title": "문의",
        "contact_text": "협업, 파일럿 테스트 또는 프로젝트 문의는 Her Story 팀에 연락해 주세요.",
        "form_name": "이름",
        "form_email": "이메일",
        "form_message": "메시지",
        "form_button": "제출",
        "form_success": "감사합니다. 메시지가 저장되었습니다.",
        "footer": "Streamlit으로 제작한 프로토타입 웹사이트입니다.",
        "key_elements": "핵심 요소",
        "why_matters": "이 서비스가 중요한 이유",
        "primary_users": "주요 사용자: 한국에 거주하는 이주여성 및 결혼이주여성",
        "key_elements_items": ["성찰 지원", "다국어 접근성", "부드러운 안내", "향후 AI 기반 기능"],
        "why_items": ["장벽 감소", "자기 표현 지원", "정보 접근성 향상", "환영받는 디지털 경험 제공"],
        "concept_stage": "개념 개발 단계",
        "brand_sub": "따뜻한 다국어 지원 서비스 컨셉",
    },
    "Русский": {
        "nav": ["Главная", "О проекте", "Наш сервис", "Для кого", "Будущее", "Контакты"],
        "hero_title": "🌸Her Story🌸",
        "hero_subtitle": "Поддерживающее цифровое пространство для мигранток в Корее",
        "hero_text": (
            "Her Story создан как многоязычный и удобный цифровой сервис, "
            "который помогает с эмоциональной поддержкой, рефлексией и доступом к полезной информации."
        ),
        "button_1": "О сервисе",
        "button_2": "Будущее проекта",
        "cards": [
            ("Многоязычная поддержка", "Пользовательницы могут пользоваться платформой на более удобном и естественном для себя языке."),
            ("Рефлексия и поддержка", "Сервис помогает с эмоциональным выражением, саморефлексией и практической поддержкой."),
            ("Удобный интерфейс", "Спокойный и дружелюбный интерфейс помогает чувствовать себя безопасно и комфортно."),
        ],
        "about_title": "О проекте Her Story",
        "about_text": (
            "Her Story — это концепция сервиса, созданного для поддержки мигранток и женщин в брачной миграции, "
            "живущих в Южной Корее. Проект фокусируется на эмоциональной поддержке, самовыражении и доступной помощи."
        ),
        "service_title": "Наш сервис",
        "service_text": (
            "Сервис задуман как многоязычная цифровая платформа поддержки. "
            "Он может включать помощь в рефлексивном письме, практические рекомендации, "
            "эмоциональную поддержку и будущие AI-инструменты."
        ),
        "target_title": "Для кого этот сервис",
        "target_text": (
            "Наша основная аудитория — мигрантки и женщины в брачной миграции в Корее, "
            "которые могут сталкиваться с языковыми барьерами, социальной изоляцией, культурной адаптацией "
            "или неопределённостью в повседневной жизни."
        ),
        "future_title": "Будущее развитие",
        "future_text": (
            "В будущем Her Story может вырасти в более интерактивную платформу с персонализированной поддержкой, "
            "полезными ресурсами сообщества, многоязычным контентом и AI-инструментами для рефлексии."
        ),
        "contact_title": "Контакты",
        "contact_text": "По вопросам сотрудничества, пилотного тестирования или проекта свяжитесь с командой Her Story.",
        "form_name": "Имя",
        "form_email": "Email",
        "form_message": "Сообщение",
        "form_button": "Отправить",
        "form_success": "Спасибо. Сообщение успешно сохранено.",
        "footer": "Прототип сайта, созданный на Streamlit.",
        "key_elements": "Ключевые элементы",
        "why_matters": "Почему это важно",
        "primary_users": "Основные пользователи: мигрантки и женщины в брачной миграции в Корее",
        "key_elements_items": [
            "Поддержка рефлексии",
            "Многоязычная доступность",
            "Мягкое сопровождение",
            "Будущие AI-инструменты",
        ],
        "why_items": [
            "Снижение барьеров",
            "Поддержка самовыражения",
            "Более простой доступ к информации",
            "Создание дружелюбного цифрового пространства",
        ],
        "concept_stage": "Стадия разработки концепции",
        "brand_sub": "Мягкая многоязычная концепция поддержки",
    },
    "Tiếng Việt": {
        "nav": ["Trang chủ", "Giới thiệu", "Dịch vụ", "Người dùng", "Tầm nhìn", "Liên hệ"],
        "hero_title": "🌸Her Story🌸",
        "hero_subtitle": "Không gian kỹ thuật số hỗ trợ phụ nữ nhập cư tại Hàn Quốc",
        "hero_text": (
            "Her Story được thiết kế như một dịch vụ kỹ thuật số đa ngôn ngữ "
            "nhằm hỗ trợ sức khỏe tinh thần, sự tự phản ánh và giúp tiếp cận thông tin dễ dàng hơn."
        ),
        "button_1": "Khám phá dịch vụ",
        "button_2": "Tầm nhìn tương lai",
        "cards": [
            ("Hỗ trợ đa ngôn ngữ", "Người dùng có thể sử dụng nền tảng bằng ngôn ngữ mà họ cảm thấy thoải mái nhất."),
            ("Tự phản ánh và hỗ trợ", "Dịch vụ giúp người dùng thể hiện cảm xúc, suy ngẫm về bản thân và nhận được hướng dẫn thực tế."),
            ("Trải nghiệm thân thiện", "Giao diện đơn giản và nhẹ nhàng giúp người dùng cảm thấy an toàn và được chào đón."),
        ],
        "about_title": "Giới thiệu về Her Story",
        "about_text": (
            "Her Story là một ý tưởng dịch vụ được tạo ra để hỗ trợ phụ nữ nhập cư "
            "và phụ nữ kết hôn với người Hàn đang sống tại Hàn Quốc. "
            "Dự án tập trung vào hỗ trợ cảm xúc, khả năng thể hiện bản thân "
            "và tiếp cận thông tin hữu ích dễ dàng hơn."
        ),
        "service_title": "Dịch vụ của chúng tôi",
        "service_text": (
            "Dịch vụ được thiết kế như một nền tảng hỗ trợ kỹ thuật số đa ngôn ngữ. "
            "Nó có thể bao gồm hỗ trợ viết phản ánh, hướng dẫn thực tế, "
            "hỗ trợ cảm xúc và các công cụ AI trong tương lai."
        ),
        "target_title": "Đối tượng người dùng",
        "target_text": (
            "Người dùng chính là phụ nữ nhập cư và phụ nữ kết hôn với người Hàn "
            "có thể gặp rào cản ngôn ngữ, cô lập xã hội, khó khăn trong thích nghi văn hóa "
            "hoặc sự không chắc chắn trong cuộc sống hàng ngày."
        ),
        "future_title": "Tầm nhìn tương lai",
        "future_text": (
            "Trong tương lai, Her Story có thể phát triển thành một nền tảng tương tác hơn "
            "với hướng dẫn cá nhân hóa, tài nguyên cộng đồng, nội dung đa ngôn ngữ "
            "và các công cụ AI hỗ trợ tự phản ánh."
        ),
        "contact_title": "Liên hệ",
        "contact_text": "Để hợp tác, thử nghiệm dự án hoặc tìm hiểu thêm, vui lòng liên hệ với nhóm Her Story.",
        "form_name": "Tên",
        "form_email": "Email",
        "form_message": "Tin nhắn",
        "form_button": "Gửi",
        "form_success": "Cảm ơn bạn. Tin nhắn đã được lưu thành công.",
        "footer": "Trang web nguyên mẫu được xây dựng bằng Streamlit.",
        "key_elements": "Các yếu tố chính",
        "why_matters": "Tại sao điều này quan trọng",
        "primary_users": "Người dùng chính: phụ nữ nhập cư và phụ nữ kết hôn với người Hàn tại Hàn Quốc",
        "key_elements_items": [
            "Hỗ trợ tự phản ánh",
            "Khả năng truy cập đa ngôn ngữ",
            "Hướng dẫn nhẹ nhàng",
            "Các tính năng AI trong tương lai",
        ],
        "why_items": [
            "Giảm rào cản",
            "Hỗ trợ thể hiện bản thân",
            "Dễ tiếp cận thông tin hơn",
            "Tạo trải nghiệm kỹ thuật số thân thiện",
        ],
        "concept_stage": "Giai đoạn phát triển ý tưởng",
        "brand_sub": "Một ý tưởng hỗ trợ đa ngôn ngữ nhẹ nhàng",
    },
}

# -----------------------------
# Top bar
# -----------------------------
col1, col2 = st.columns([7, 1])
with col2:
    language = st.selectbox("🌍", ["English", "한국어", "Русский", "Tiếng Việt"])

T = content[language]
page = st.radio("", T["nav"], horizontal=True)

st.markdown(
    f"""
    <div class="topbar">
        <div class="brand-wrap">
            <div class="chatbot-icon">🤖</div>
            <div>
                <p class="brand-title">🌸Re: Her Chatbot</p>
                <p class="brand-sub">{T['brand_sub']}</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Save contact submissions
# -----------------------------
def save_contact(name, email, message, language_used):
    file_path = "contact_messages.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "name", "email", "message", "language"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name,
            email,
            message,
            language_used,
        ])

# -----------------------------
# Pages
# -----------------------------
if page == T["nav"][0]:
    st.markdown(
        f"""
        <div class="hero">
            <h1>{T['hero_title']}</h1>
            <h3>{T['hero_subtitle']}</h3>
            <p style="font-size: 1.05rem;">{T['hero_text']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button(T["button_1"], use_container_width=True)
    with col2:
        st.button(T["button_2"], use_container_width=True)

    st.write("")
    cards = st.columns(3)
    for col, (title, desc) in zip(cards, T["cards"]):
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.image(
        "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?q=80&w=1600&auto=format&fit=crop",
        use_container_width=True,
    )

elif page == T["nav"][1]:
    st.header(T["about_title"])
    st.write(T["about_text"])
    st.markdown(
        f"""
        <div class="soft-box">
        {T['hero_title']} is designed around accessibility, emotional support, and inclusion.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == T["nav"][2]:
    st.header(T["service_title"])
    st.write(T["service_text"])

    c1, c2 = st.columns(2)
    with c1:
        st.subheader(T["key_elements"])
        for item in T["key_elements_items"]:
            st.write(f"- {item}")

    with c2:
        st.subheader(T["why_matters"])
        for item in T["why_items"]:
            st.write(f"- {item}")

elif page == T["nav"][3]:
    st.header(T["target_title"])
    st.write(T["target_text"])
    st.info(T["primary_users"])

elif page == T["nav"][4]:
    st.header(T["future_title"])
    st.write(T["future_text"])
    st.progress(65)
    st.caption(T["concept_stage"])

elif page == T["nav"][5]:
    st.header(T["contact_title"])
    st.write(T["contact_text"])

    with st.form("contact_form"):
        name = st.text_input(T["form_name"])
        email = st.text_input(T["form_email"])
        message = st.text_area(T["form_message"])
        submitted = st.form_submit_button(T["form_button"])

        if submitted:
            if name and email and message:
                save_contact(name, email, message, language)
                st.success(T["form_success"])
            else:
                st.warning("Please fill in all fields.")

st.markdown(f"<div class='footer'>{T['footer']}</div>", unsafe_allow_html=True)

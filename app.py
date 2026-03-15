import streamlit as st

st.set_page_config(
    page_title="Her Story",
    page_icon="🌿",
    layout="wide",
)

# -----------------------------
# Simple custom styling
# -----------------------------
st.markdown(
    """
    <style>
    .hero {
        padding: 3rem 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #f7efe8 0%, #f4f0ff 100%);
        margin-bottom: 2rem;
    }
    .card {
        padding: 1.2rem;
        border-radius: 18px;
        background: #fafafa;
        border: 1px solid #eeeeee;
        min-height: 220px;
    }
    .soft-box {
        padding: 1rem 1.2rem;
        border-radius: 16px;
        background: #f8f9ff;
        border-left: 5px solid #b8baf8;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        color: #777777;
        font-size: 0.9rem;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Re:Her")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Our Service", "Target Users", "Future Vision", "Contact"]
)

language = st.sidebar.selectbox("Language", ["English", "한국어", "Русский", "Tiếng Việt"])

# -----------------------------
# Multilingual text
# -----------------------------
content = {
    "English": {
        "hero_title": "Re:Her",
        "hero_subtitle": "A supportive digital space for migrant women in Korea",
        "hero_text": (
            "Re:Her is designed to support emotional well-being, reflection, and "
            "easier access to guidance through a multilingual and user-friendly digital service."
        ),
        "button_1": "Explore Our Service",
        "button_2": "Read Future Vision",
        "cards": [
            ("Multilingual Support",
             "Users can explore the platform in a language that feels comfortable and natural."),
            ("Reflection and Guidance",
             "The service is designed to support emotional expression, self-reflection, and practical guidance."),
            ("Accessible Experience",
             "A calm and welcoming interface helps users feel supported and included."),
        ],
        "about_title": "About Re:Her",
        "about_text": (
            "Re:Her is a concept service created to support migrant and marriage migrant women living in South Korea. "
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
            "In the future, Re:Her can grow into a more interactive platform with personalized guidance, "
            "community resources, multilingual content, and AI-supported reflection tools."
        ),
        "contact_title": "Contact",
        "contact_text": "For collaboration, pilot testing, or project inquiries, please contact the Re:Her team.",
        "form_name": "Name",
        "form_email": "Email",
        "form_message": "Message",
        "form_button": "Submit",
        "form_success": "Thank you. Your message was submitted in this prototype.",
        "footer": "Prototype website built with Streamlit.",
        "key_elements": "Key Elements",
        "why_matters": "Why It Matters",
    },
    "한국어": {
        "hero_title": "Re:Her",
        "hero_subtitle": "한국에 거주하는 이주여성을 위한 따뜻한 디지털 공간",
        "hero_text": (
            "Re:Her는 다국어 기반의 사용자 친화적인 디지털 서비스를 통해 "
            "정서적 지원, 자기성찰, 그리고 유용한 정보 접근을 돕는 것을 목표로 합니다."
        ),
        "button_1": "서비스 보기",
        "button_2": "향후 비전 보기",
        "cards": [
            ("다국어 지원",
             "사용자가 더 편안하고 자연스러운 언어로 플랫폼을 이용할 수 있습니다."),
            ("성찰과 가이드",
             "감정 표현, 자기 성찰, 그리고 실질적인 안내를 지원하도록 설계되었습니다."),
            ("접근성 중심 경험",
             "차분하고 따뜻한 인터페이스를 통해 사용자가 안전함과 편안함을 느낄 수 있습니다."),
        ],
        "about_title": "Re:Her 소개",
        "about_text": (
            "Re:Her는 한국에 거주하는 결혼이주여성과 이주여성을 지원하기 위해 기획된 서비스입니다. "
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
            "향후 Re:Her는 개인 맞춤형 안내, 지역사회 자원, 다국어 콘텐츠, "
            "AI 기반 성찰 도구를 포함한 더 확장된 플랫폼으로 발전할 수 있습니다."
        ),
        "contact_title": "문의",
        "contact_text": "협업, 파일럿 테스트 또는 프로젝트 문의는 Re:Her 팀에 연락해 주세요.",
        "form_name": "이름",
        "form_email": "이메일",
        "form_message": "메시지",
        "form_button": "제출",
        "form_success": "감사합니다. 이 프로토타입에서 메시지가 제출되었습니다.",
        "footer": "Streamlit으로 제작한 프로토타입 웹사이트입니다.",
        "key_elements": "핵심 요소",
        "why_matters": "이 서비스가 중요한 이유",
    },
    "Русский": {
        "hero_title": "Re:Her",
        "hero_subtitle": "Поддерживающее цифровое пространство для мигранток в Корее",
        "hero_text": (
            "Re:Her создан как многоязычный и удобный цифровой сервис, "
            "который помогает с эмоциональной поддержкой, рефлексией и доступом к полезной информации."
        ),
        "button_1": "О сервисе",
        "button_2": "Будущее проекта",
        "cards": [
            ("Многоязычная поддержка",
             "Пользовательницы могут пользоваться платформой на более удобном и естественном для себя языке."),
            ("Рефлексия и поддержка",
             "Сервис помогает с эмоциональным выражением, саморефлексией и практической поддержкой."),
            ("Удобный интерфейс",
             "Спокойный и дружелюбный интерфейс помогает чувствовать себя безопасно и комфортно."),
        ],
        "about_title": "О проекте Re:Her",
        "about_text": (
            "Re:Her — это концепция сервиса, созданного для поддержки мигранток и женщин в брачной миграции, "
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
            "В будущем Re:Her может вырасти в более интерактивную платформу с персонализированной поддержкой, "
            "полезными ресурсами сообщества, многоязычным контентом и AI-инструментами для рефлексии."
        ),
        "contact_title": "Контакты",
        "contact_text": "По вопросам сотрудничества, пилотного тестирования или проекта свяжитесь с командой Re:Her.",
        "form_name": "Имя",
        "form_email": "Email",
        "form_message": "Сообщение",
        "form_button": "Отправить",
        "form_success": "Спасибо. В этом прототипе сообщение было отправлено.",
        "footer": "Прототип сайта, созданный на Streamlit.",
        "key_elements": "Ключевые элементы",
        "why_matters": "Почему это важно",
    }, 
        "Tiếng Việt": {
        "hero_title": "Re:Her",
        "hero_subtitle": "Không gian kỹ thuật số hỗ trợ phụ nữ nhập cư tại Hàn Quốc",
        "hero_text": (
            "Re:Her được thiết kế như một dịch vụ kỹ thuật số đa ngôn ngữ "
            "nhằm hỗ trợ sức khỏe tinh thần, sự tự phản ánh và giúp tiếp cận thông tin dễ dàng hơn."
        ),
        "button_1": "Khám phá dịch vụ",
        "button_2": "Tầm nhìn tương lai",
        "cards": [
            ("Hỗ trợ đa ngôn ngữ",
             "Người dùng có thể sử dụng nền tảng bằng ngôn ngữ mà họ cảm thấy thoải mái nhất."),
            ("Tự phản ánh và hỗ trợ",
             "Dịch vụ giúp người dùng thể hiện cảm xúc, suy ngẫm về bản thân và nhận được hướng dẫn thực tế."),
            ("Trải nghiệm thân thiện",
             "Giao diện đơn giản và nhẹ nhàng giúp người dùng cảm thấy an toàn và được chào đón."),
        ],
        "about_title": "Giới thiệu về Re:Her",
        "about_text": (
            "Re:Her là một ý tưởng dịch vụ được tạo ra để hỗ trợ phụ nữ nhập cư "
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
            "Trong tương lai, Re:Her có thể phát triển thành một nền tảng tương tác hơn "
            "với hướng dẫn cá nhân hóa, tài nguyên cộng đồng, nội dung đa ngôn ngữ "
            "và các công cụ AI hỗ trợ tự phản ánh."
        ),
        "contact_title": "Liên hệ",
        "contact_text": "Để hợp tác, thử nghiệm dự án hoặc tìm hiểu thêm, vui lòng liên hệ với nhóm Re:Her.",
        "form_name": "Tên",
        "form_email": "Email",
        "form_message": "Tin nhắn",
        "form_button": "Gửi",
        "form_success": "Cảm ơn bạn. Tin nhắn đã được gửi trong bản thử nghiệm này.",
        "footer": "Trang web nguyên mẫu được xây dựng bằng Streamlit.",
        "key_elements": "Các yếu tố chính",
        "why_matters": "Tại sao điều này quan trọng",
    }
}

T = content[language]

# -----------------------------
# Pages
# -----------------------------
if page == "Home":
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

elif page == "About":
    st.header(T["about_title"])
    st.write(T["about_text"])
    st.markdown(
        """
        <div class="soft-box">
        Re:Her is designed around accessibility, emotional support, and inclusion.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Our Service":
    st.header(T["service_title"])
    st.write(T["service_text"])

    c1, c2 = st.columns(2)
    with c1:
        st.subheader(T["key_elements"])
        st.write("- Reflection support")
        st.write("- Multilingual accessibility")
        st.write("- Gentle guidance")
        st.write("- Future AI-based features")

    with c2:
        st.subheader(T["why_matters"])
        st.write("- Reduces barriers")
        st.write("- Supports self-expression")
        st.write("- Makes guidance easier to access")
        st.write("- Creates a welcoming digital experience")

elif page == "Target Users":
    st.header(T["target_title"])
    st.write(T["target_text"])
    st.info("Primary users: migrant and marriage migrant women in Korea")

elif page == "Future Vision":
    st.header(T["future_title"])
    st.write(T["future_text"])
    st.progress(65)
    st.caption("Concept development stage")

elif page == "Contact":
    st.header(T["contact_title"])
    st.write(T["contact_text"])

    with st.form("contact_form"):
        name = st.text_input(T["form_name"])
        email = st.text_input(T["form_email"])
        message = st.text_area(T["form_message"])
        submitted = st.form_submit_button(T["form_button"])

        if submitted:
            st.success(T["form_success"])

st.markdown(f"<div class='footer'>{T['footer']}</div>", unsafe_allow_html=True)

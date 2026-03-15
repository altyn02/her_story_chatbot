import streamlit as st

st.set_page_config(
    page_title="Re:Her",
    page_icon="🌿",
    layout="wide",
)

# -----------------------------
# Simple styling
# -----------------------------
st.markdown(
    """
    <style>
    .hero {
        padding: 2rem 1rem 1rem 1rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #f7efe8 0%, #f5f1ff 100%);
        margin-bottom: 1.5rem;
    }
    .section-card {
        padding: 1.2rem;
        border-radius: 18px;
        background: #fafafa;
        border: 1px solid #eeeeee;
        height: 100%;
    }
    .soft-note {
        padding: 1rem;
        border-radius: 16px;
        background: #f8f9ff;
        border-left: 5px solid #b8baf8;
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
    ["Home", "About", "Our Service", "Target Users", "Future Vision", "Contact"],
)

language = st.sidebar.selectbox("Language", ["English", "한국어", "Русский"])

# -----------------------------
# Language dictionary
# -----------------------------
text = {
    "English": {
        "hero_title": "Re:Her",
        "hero_sub": "A supportive digital space for migrant women in Korea.",
        "hero_desc": "Re:Her aims to provide emotional guidance, reflection support, and accessible information through a multilingual and user-friendly digital service.",
        "cta1": "Explore Our Service",
        "cta2": "Read Project Vision",
        "home_cards": [
            ("Multilingual Support", "Users can engage in a language that feels natural and comfortable."),
            ("Reflection and Guidance", "The service is designed to support emotional expression, self-reflection, and everyday guidance."),
            ("Accessible Design", "A simple, welcoming interface helps users feel safe and supported."),
        ],
        "about_title": "About Re:Her",
        "about_text": "Re:Her is a concept service designed to support migrant and marriage migrant women living in South Korea. The project focuses on emotional well-being, self-expression, and easier access to practical guidance.",
        "service_title": "Our Service",
        "service_text": "The service is designed as a multilingual digital support space. It can include reflective writing support, emotional guidance, information about life in Korea, and future AI-assisted support tools.",
        "targets_title": "Who We Aim to Support",
        "targets_text": "Our main target users are migrant and marriage migrant women in Korea who may face language barriers, social isolation, cultural adjustment difficulties, or uncertainty in daily life.",
        "future_title": "Future Vision",
        "future_text": "In the future, Re:Her can expand into a more interactive digital platform with personalized guidance, multilingual content, community resources, and AI-supported reflection tools.",
        "contact_title": "Contact",
        "contact_text": "For collaboration, pilot testing, or project inquiries, please contact the Re:Her team.",
        "footer": "Prototype website built with Streamlit.",
    },
    "한국어": {
        "hero_title": "Re:Her",
        "hero_sub": "한국에 거주하는 이주여성을 위한 따뜻한 디지털 공간",
        "hero_desc": "Re:Her는 다국어 기반의 사용자 친화적인 디지털 서비스를 통해 정서적 지원, 자기성찰, 그리고 유용한 정보 접근을 돕는 것을 목표로 합니다.",
        "cta1": "서비스 보기",
        "cta2": "프로젝트 비전 보기",
        "home_cards": [
            ("다국어 지원", "사용자가 더 편안한 언어로 서비스를 이용할 수 있습니다."),
            ("성찰과 가이드", "감정 표현, 자기 성찰, 일상적 안내를 지원하도록 설계되었습니다."),
            ("접근성 중심 디자인", "단순하고 따뜻한 인터페이스를 통해 사용자가 안전함을 느낄 수 있도록 합니다."),
        ],
        "about_title": "Re:Her 소개",
        "about_text": "Re:Her는 한국에 거주하는 결혼이주여성과 이주여성을 지원하기 위해 기획된 서비스입니다. 이 프로젝트는 정서적 웰빙, 자기표현, 그리고 실질적인 안내에 더 쉽게 접근할 수 있도록 하는 데 초점을 둡니다.",
        "service_title": "서비스 소개",
        "service_text": "이 서비스는 다국어 디지털 지원 공간으로 설계되었습니다. 성찰적 글쓰기 지원, 정서적 안내, 한국 생활 정보, 그리고 향후 AI 기반 지원 도구를 포함할 수 있습니다.",
        "targets_title": "주요 대상 사용자",
        "targets_text": "주요 대상은 한국에서 언어 장벽, 사회적 고립, 문화 적응의 어려움, 일상 속 불확실성을 경험할 수 있는 이주여성 및 결혼이주여성입니다.",
        "future_title": "향후 비전",
        "future_text": "향후 Re:Her는 개인 맞춤형 안내, 다국어 콘텐츠, 지역사회 자원, AI 기반 성찰 도구를 포함한 보다 확장된 디지털 플랫폼으로 발전할 수 있습니다.",
        "contact_title": "문의",
        "contact_text": "협업, 파일럿 테스트 또는 프로젝트 문의는 Re:Her 팀에 연락해 주세요.",
        "footer": "Streamlit으로 제작한 프로토타입 웹사이트입니다.",
    },
    "Русский": {
        "hero_title": "Re:Her",
        "hero_sub": "Поддерживающее цифровое пространство для мигранток в Корее.",
        "hero_desc": "Re:Her стремится предоставлять эмоциональную поддержку, пространство для рефлексии и доступную информацию через многоязычный и удобный цифровой сервис.",
        "cta1": "Посмотреть сервис",
        "cta2": "Узнать о проекте",
        "home_cards": [
            ("Многоязычная поддержка", "Пользовательницы могут общаться на наиболее удобном для них языке."),
            ("Рефлексия и поддержка", "Сервис помогает с эмоциональным выражением, саморефлексией и повседневной поддержкой."),
            ("Удобный интерфейс", "Простой и дружелюбный интерфейс помогает пользователям чувствовать себя спокойно и безопасно."),
        ],
        "about_title": "О проекте Re:Her",
        "about_text": "Re:Her — это концепция сервиса, созданного для поддержки мигранток и женщин в брачной миграции, живущих в Южной Корее. Проект фокусируется на эмоциональном благополучии, самовыражении и более лёгком доступе к полезной информации.",
        "service_title": "Наш сервис",
        "service_text": "Сервис задуман как многоязычное цифровое пространство поддержки. Он может включать помощь в рефлексивном письме, эмоциональную поддержку, информацию о жизни в Корее и будущие AI-инструменты для сопровождения пользователей.",
        "targets_title": "Для кого этот сервис",
        "targets_text": "Наша основная аудитория — мигрантки и женщины в брачной миграции в Корее, которые могут сталкиваться с языковыми барьерами, социальной изоляцией, трудностями культурной адаптации или неопределённостью в повседневной жизни.",
        "future_title": "Будущее развитие",
        "future_text": "В будущем Re:Her может вырасти в более интерактивную цифровую платформу с персонализированной поддержкой, многоязычным контентом, полезными ресурсами сообщества и AI-инструментами для рефлексии.",
        "contact_title": "Контакты",
        "contact_text": "По вопросам сотрудничества, пилотного тестирования или проекта свяжитесь с командой Re:Her.",
        "footer": "Прототип сайта, созданный на Streamlit.",
    },
}

T = text[language]

# -----------------------------
# Pages
# -----------------------------
if page == "Home":
    st.markdown(f"""
    <div class='hero'>
        <h1>{T['hero_title']}</h1>
        <h3>{T['hero_sub']}</h3>
        <p>{T['hero_desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.button(T["cta1"], use_container_width=True)
    with c2:
        st.button(T["cta2"], use_container_width=True)

    st.markdown("")
    cols = st.columns(3)
    for col, (title, body) in zip(cols, T["home_cards"]):
        with col:
            st.markdown(
                f"""
                <div class='section-card'>
                    <h4>{title}</h4>
                    <p>{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("")
    st.image(
        "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?q=80&w=1600&auto=format&fit=crop",
        use_container_width=True,
    )

elif page == "About":
    st.header(T["about_title"])
    st.write(T["about_text"])
    st.markdown("<div class='soft-note'>Re:Her is designed around accessibility, emotional support, and inclusion.</div>", unsafe_allow_html=True)

elif page == "Our Service":
    st.header(T["service_title"])
    st.write(T["service_text"])
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Key Elements")
        st.write("- Reflection support")
        st.write("- Multilingual accessibility")
        st.write("- Gentle guidance")
        st.write("- Future AI-based tools")
    with col2:
        st.subheader("Why It Matters")
        st.write("- Reduces barriers")
        st.write("- Supports self-expression")
        st.write("- Makes information easier to access")
        st.write("- Creates a welcoming digital experience")

elif page == "Target Users":
    st.header(T["targets_title"])
    st.write(T["targets_text"])
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
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you. This prototype form was submitted locally.")

st.divider()
st.caption(T["footer"])

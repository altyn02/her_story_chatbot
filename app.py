import csv
import os
from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="HerStory",
    page_icon="💙",
    layout="wide",
)

# -----------------------------
# Multilingual text
# -----------------------------
content = {
    "English": {
        "nav": ["Home", "About", "Our Service", "Target Users", "Future Vision", "Contact"],
        "hero_title": "HerStory",
        "hero_subtitle": "A supportive digital space for migrant women in Korea",
        "hero_text": (
            "HerStory is designed to support emotional well-being, reflection, and "
            "easier access to guidance through a multilingual and user-friendly digital service."
        ),
        "chatbot_info_title": "What is Re:Her Chatbot?",
        "chatbot_info_text": (
            "Re:Her Chatbot is a gentle guidance-based chatbot designed to support migrant women "
            "through emotional check-ins, reflective conversation, and multilingual interaction. "
            "To use this chatbot, registration for Claude may be required."
        ),
        "cards": [
            ("Multilingual Support", "Users can explore the platform in a language that feels comfortable and natural."),
            ("Reflection and Guidance", "The service is designed to support emotional expression, self-reflection, and practical guidance."),
            ("Accessible Experience", "A calm and welcoming interface helps users feel supported and included."),
        ],
        "about_title": "About HerStory",
        "about_text": (
            "HerStory is a concept service created to support migrant and marriage migrant women living in South Korea. "
            "The project focuses on emotional support, self-expression, and accessible guidance."
        ),
        "about_note": "HerStory is designed around accessibility, emotional support, and inclusion.",
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
            "In the future, HerStory can grow into a more interactive platform with personalized guidance, "
            "community resources, multilingual content, and AI-supported reflection tools."
        ),
        "contact_title": "Contact",
        "contact_text": "For collaboration, pilot testing, or project inquiries, please contact the HerStory team.",
        "form_name": "Name",
        "form_email": "Email",
        "form_message": "Message",
        "form_button": "Submit",
        "form_success": "Thank you. Your message was saved successfully.",
        "form_warning": "Please fill in all fields.",
        "form_invalid_email": "Please enter a valid email address.",
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
        "chatbot_title": "🤖 Re:Her Chatbot",
        "chatbot_desc": "Click here to open the interactive chatbot experience.",
        "image_caption": "Supporting migrant and marriage migrant women in Korea",
        "image_not_found": "Image file not found. Please check the path in your repository.",
        "theme_label": "Theme",
        "theme_light": "Light",
        "theme_dark": "Dark",
    },
    "한국어": {
        "nav": ["홈", "소개", "서비스", "대상 사용자", "향후 비전", "문의"],
        "hero_title": "HerStory",
        "hero_subtitle": "한국에 거주하는 이주여성을 위한 따뜻한 디지털 공간",
        "hero_text": (
            "HerStory는 다국어 기반의 사용자 친화적인 디지털 서비스를 통해 "
            "정서적 지원, 자기성찰, 그리고 유용한 정보 접근을 돕는 것을 목표로 합니다."
        ),
        "chatbot_info_title": "Re:Her 챗봇이란?",
        "chatbot_info_text": (
            "Re:Her 챗봇은 이주여성을 위해 설계된 부드러운 가이드형 챗봇으로, "
            "감정 확인, 성찰적 대화, 그리고 다국어 상호작용을 지원합니다. "
            "이용을 위해 Claude 가입이 필요할 수 있습니다."
        ),
        "cards": [
            ("다국어 지원", "사용자가 더 편안하고 자연스러운 언어로 플랫폼을 이용할 수 있습니다."),
            ("성찰과 가이드", "감정 표현, 자기 성찰, 그리고 실질적인 안내를 지원하도록 설계되었습니다."),
            ("접근성 중심 경험", "차분하고 따뜻한 인터페이스를 통해 사용자가 안전함과 편안함을 느낄 수 있습니다."),
        ],
        "about_title": "HerStory 소개",
        "about_text": (
            "HerStory는 한국에 거주하는 결혼이주여성과 이주여성을 지원하기 위해 기획된 서비스입니다. "
            "이 프로젝트는 정서적 지원, 자기표현, 그리고 실질적인 안내에 더 쉽게 접근할 수 있도록 하는 데 초점을 둡니다."
        ),
        "about_note": "HerStory는 접근성, 정서적 지원, 그리고 포용성을 중심으로 설계되었습니다.",
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
            "향후 HerStory는 개인 맞춤형 안내, 지역사회 자원, 다국어 콘텐츠, "
            "AI 기반 성찰 도구를 포함한 더 확장된 플랫폼으로 발전할 수 있습니다."
        ),
        "contact_title": "문의",
        "contact_text": "협업, 파일럿 테스트 또는 프로젝트 문의는 HerStory 팀에 연락해 주세요.",
        "form_name": "이름",
        "form_email": "이메일",
        "form_message": "메시지",
        "form_button": "제출",
        "form_success": "감사합니다. 메시지가 저장되었습니다.",
        "form_warning": "모든 항목을 입력해 주세요.",
        "form_invalid_email": "올바른 이메일 주소를 입력해 주세요.",
        "footer": "Streamlit으로 제작한 프로토타입 웹사이트입니다.",
        "key_elements": "핵심 요소",
        "why_matters": "이 서비스가 중요한 이유",
        "primary_users": "주요 사용자: 한국에 거주하는 이주여성 및 결혼이주여성",
        "key_elements_items": ["성찰 지원", "다국어 접근성", "부드러운 안내", "향후 AI 기반 기능"],
        "why_items": ["장벽 감소", "자기 표현 지원", "정보 접근성 향상", "환영받는 디지털 경험 제공"],
        "concept_stage": "개념 개발 단계",
        "chatbot_title": "🤖 Re:Her 챗봇",
        "chatbot_desc": "클릭하여 대화형 챗봇 경험을 시작하세요.",
        "image_caption": "한국의 이주여성과 결혼이주여성을 위한 지원",
        "image_not_found": "이미지 파일을 찾을 수 없습니다. 저장소의 경로를 확인해 주세요.",
        "theme_label": "테마",
        "theme_light": "라이트",
        "theme_dark": "다크",
    },
    "Русский": {
        "nav": ["Главная", "О проекте", "Наш сервис", "Для кого", "Будущее", "Контакты"],
        "hero_title": "HerStory",
        "hero_subtitle": "Поддерживающее цифровое пространство для мигранток в Корее",
        "hero_text": (
            "HerStory создан как многоязычный и удобный цифровой сервис, "
            "который помогает с эмоциональной поддержкой, рефлексией и доступом к полезной информации."
        ),
        "chatbot_info_title": "Что такое Re:Her Chatbot?",
        "chatbot_info_text": (
            "Re:Her Chatbot — это чатбот с мягким направляющим стилем, созданный для поддержки "
            "женщин-мигранток через эмоциональную поддержку, рефлексивный диалог и многоязычное общение. "
            "Для использования может потребоваться регистрация в Claude."
        ),
        "cards": [
            ("Многоязычная поддержка", "Пользовательницы могут пользоваться платформой на более удобном и естественном для себя языке."),
            ("Рефлексия и поддержка", "Сервис помогает с эмоциональным выражением, саморефлексией и практической поддержкой."),
            ("Удобный интерфейс", "Спокойный и дружелюбный интерфейс помогает чувствовать себя безопасно и комфортно."),
        ],
        "about_title": "О проекте HerStory",
        "about_text": (
            "HerStory — это концепция сервиса, созданного для поддержки мигранток и женщин в брачной миграции, "
            "живущих в Южной Корее. Проект фокусируется на эмоциональной поддержке, самовыражении и доступной помощи."
        ),
        "about_note": "HerStory создан с акцентом на доступность, эмоциональную поддержку и инклюзивность.",
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
            "В будущем HerStory может вырасти в более интерактивную платформу с персонализированной поддержкой, "
            "полезными ресурсами сообщества, многоязычным контентом и AI-инструментами для рефлексии."
        ),
        "contact_title": "Контакты",
        "contact_text": "По вопросам сотрудничества, пилотного тестирования или проекта свяжитесь с командой HerStory.",
        "form_name": "Имя",
        "form_email": "Email",
        "form_message": "Сообщение",
        "form_button": "Отправить",
        "form_success": "Спасибо. Сообщение успешно сохранено.",
        "form_warning": "Пожалуйста, заполните все поля.",
        "form_invalid_email": "Пожалуйста, введите корректный email.",
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
        "chatbot_title": "🤖 Re:Her Чатбот",
        "chatbot_desc": "Нажмите здесь, чтобы открыть интерактивный чатбот.",
        "image_caption": "Поддержка мигранток и женщин в брачной миграции в Корее",
        "image_not_found": "Файл изображения не найден. Проверьте путь в repository.",
        "theme_label": "Тема",
        "theme_light": "Светлая",
        "theme_dark": "Тёмная",
    },
    "Tiếng Việt": {
        "nav": ["Trang chủ", "Giới thiệu", "Dịch vụ", "Người dùng", "Tầm nhìn", "Liên hệ"],
        "hero_title": "HerStory",
        "hero_subtitle": "Không gian kỹ thuật số hỗ trợ phụ nữ nhập cư tại Hàn Quốc",
        "hero_text": (
            "HerStory được thiết kế như một dịch vụ kỹ thuật số đa ngôn ngữ "
            "nhằm hỗ trợ sức khỏe tinh thần, sự tự phản ánh và giúp tiếp cận thông tin dễ dàng hơn."
        ),
        "chatbot_info_title": "Re:Her Chatbot là gì?",
        "chatbot_info_text": (
            "Re:Her Chatbot là một chatbot hướng dẫn nhẹ nhàng, được thiết kế để hỗ trợ phụ nữ nhập cư "
            "thông qua trò chuyện phản ánh, hỗ trợ cảm xúc và tương tác đa ngôn ngữ. "
            "Có thể cần đăng ký Claude để sử dụng."
        ),
        "cards": [
            ("Hỗ trợ đa ngôn ngữ", "Người dùng có thể sử dụng nền tảng bằng ngôn ngữ mà họ cảm thấy thoải mái nhất."),
            ("Tự phản ánh và hỗ trợ", "Dịch vụ giúp người dùng thể hiện cảm xúc, suy ngẫm về bản thân và nhận được hướng dẫn thực tế."),
            ("Trải nghiệm thân thiện", "Giao diện đơn giản và nhẹ nhàng giúp người dùng cảm thấy an toàn và được chào đón."),
        ],
        "about_title": "Giới thiệu về HerStory",
        "about_text": (
            "HerStory là một ý tưởng dịch vụ được tạo ra để hỗ trợ phụ nữ nhập cư "
            "và phụ nữ kết hôn với người Hàn đang sống tại Hàn Quốc. "
            "Dự án tập trung vào hỗ trợ cảm xúc, khả năng thể hiện bản thân "
            "và tiếp cận thông tin hữu ích dễ dàng hơn."
        ),
        "about_note": "HerStory được thiết kế dựa trên khả năng tiếp cận, hỗ trợ cảm xúc và tính bao trùm.",
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
            "Trong tương lai, HerStory có thể phát triển thành một nền tảng tương tác hơn "
            "với hướng dẫn cá nhân hóa, tài nguyên cộng đồng, nội dung đa ngôn ngữ "
            "và các công cụ AI hỗ trợ tự phản ánh."
        ),
        "contact_title": "Liên hệ",
        "contact_text": "Để hợp tác, thử nghiệm dự án hoặc tìm hiểu thêm, vui lòng liên hệ với nhóm HerStory.",
        "form_name": "Tên",
        "form_email": "Email",
        "form_message": "Tin nhắn",
        "form_button": "Gửi",
        "form_success": "Cảm ơn bạn. Tin nhắn đã được lưu thành công.",
        "form_warning": "Vui lòng điền đầy đủ tất cả các trường.",
        "form_invalid_email": "Vui lòng nhập địa chỉ email hợp lệ.",
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
        "chatbot_title": "🤖 Chatbot Re:Her",
        "chatbot_desc": "Nhấn vào đây để mở trải nghiệm chatbot tương tác.",
        "image_caption": "Hỗ trợ phụ nữ nhập cư và phụ nữ kết hôn với người Hàn tại Hàn Quốc",
        "image_not_found": "Không tìm thấy tệp hình ảnh. Vui lòng kiểm tra đường dẫn trong repository.",
        "theme_label": "Giao diện",
        "theme_light": "Sáng",
        "theme_dark": "Tối",
    },
}

# -----------------------------
# Helper functions
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

def is_valid_email(email):
    email = email.strip()
    return "@" in email and "." in email and len(email) >= 5

def show_main_image(caption, not_found_message):
    possible_paths = [
        "women_dior.png",
        "image/women_dior.png",
        "images/women_dior.png",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            st.image(path, caption=caption, use_container_width=True)
            return

    st.warning(not_found_message)

def apply_custom_css(theme_mode="Light"):
    if theme_mode == "Dark":
        bg = "#212121"
        surface = "#2B2B2B"
        soft_surface = "#1E2D3B"
        border = "#3A3A3A"
        text = "#FFFFFF"
        muted = "#D1D5DB"
        subtle = "#A1A1AA"
        card_text = "#F5F5F5"
        link = "#66B2FF"
        shadow = "0 8px 24px rgba(0, 0, 0, 0.35)"
    else:
        bg = "#FFFFFF"
        surface = "#F8FBFF"
        soft_surface = "#EAF4FF"
        border = "#D6E6F5"
        text = "#212121"
        muted = "#4B5563"
        subtle = "#6B7280"
        card_text = "#2D3748"
        link = "#0077D4"
        shadow = "0 8px 24px rgba(0, 119, 212, 0.10)"

    primary = "#0077D4"

    st.markdown(
        f"""
        <style>
        html, body, [class*="css"] {{
            font-family: "Inter", "Segoe UI", sans-serif;
        }}

        .stApp {{
            background: {bg};
            color: {text};
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        [data-testid="stToolbar"] {{
            right: 1rem;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: {text} !important;
        }}

        p, li, label, div, span {{
            color: {text};
        }}

        .hero-subtitle-custom {{
            font-size: 1.2rem;
            font-weight: 700;
            color: {primary};
            margin-top: 0.2rem;
            margin-bottom: 1rem;
        }}

        .hero-text-custom {{
            font-size: 1.05rem;
            color: {muted};
            line-height: 1.8;
            margin-bottom: 1.2rem;
            max-width: 900px;
        }}

        .card {{
            padding: 1.25rem;
            border-radius: 20px;
            background: {surface};
            border: 1px solid {border};
            min-height: 220px;
            box-shadow: {shadow};
        }}

        .card h4 {{
            color: {primary} !important;
            margin-bottom: 0.6rem;
        }}

        .card p {{
            color: {card_text};
            line-height: 1.65;
            margin-bottom: 0;
        }}

        .soft-box {{
            padding: 1rem 1.2rem;
            border-radius: 16px;
            background: {soft_surface};
            border-left: 5px solid {primary};
            margin-top: 1rem;
            margin-bottom: 1rem;
        }}

        .soft-box h4 {{
            margin-bottom: 0.5rem;
            color: {primary} !important;
        }}

        .soft-box p {{
            margin-bottom: 0;
            color: {card_text};
            line-height: 1.7;
        }}

        .footer {{
            text-align: center;
            color: {subtle};
            font-size: 0.9rem;
            padding-top: 2rem;
            padding-bottom: 1rem;
        }}

        .chatbot-card-wrap {{
            display: flex;
            justify-content: flex-start;
            margin-top: 0.4rem;
            margin-bottom: 1.4rem;
        }}

        .chatbot-card {{
            position: relative;
            width: 430px;
            background: {surface};
            border: 1px solid {border};
            border-radius: 24px;
            padding: 22px 24px;
            text-decoration: none;
            color: {text} !important;
            box-shadow: {shadow};
            transition: all 0.2s ease;
            display: block;
        }}

        .chatbot-card:hover {{
            transform: translateY(-4px);
            border-color: {primary};
        }}

        .chatbot-title {{
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 8px;
            color: {primary};
        }}

        .chatbot-desc {{
            font-size: 0.96rem;
            color: {muted};
            line-height: 1.6;
        }}

        .click-pointer {{
            position: absolute;
            right: 18px;
            bottom: 14px;
            font-size: 1.9rem;
            animation: bounceClick 1.2s infinite;
        }}

        @keyframes bounceClick {{
            0% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0); }}
        }}

        div[data-testid="stForm"] {{
            background: {surface};
            border: 1px solid {border};
            border-radius: 18px;
            padding: 1rem;
        }}

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        textarea,
        input {{
            background-color: {surface} !important;
            color: {text} !important;
        }}

        .stTextInput input,
        .stTextArea textarea {{
            background-color: {surface} !important;
            color: {text} !important;
            border: 1px solid {border} !important;
            border-radius: 12px !important;
        }}

        .stTextInput input:focus,
        .stTextArea textarea:focus {{
            border-color: {primary} !important;
            box-shadow: 0 0 0 1px {primary} !important;
        }}

        .stButton > button,
        .stFormSubmitButton > button {{
            background-color: {primary};
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
        }}

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {{
            background-color: #0062AD;
            color: white;
        }}

        [data-testid="stRadio"] label,
        [data-testid="stSelectbox"] label {{
            color: {text} !important;
        }}

        .stInfo {{
            border-radius: 14px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# State
# -----------------------------
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Light"

# -----------------------------
# Top controls
# -----------------------------
col1, col2, col3 = st.columns([6, 1.3, 1.2])

with col2:
    language = st.selectbox("🌍", ["English", "한국어", "Русский", "Tiếng Việt"])

T = content[language]

with col3:
    theme_display = st.selectbox(
        T["theme_label"],
        [T["theme_light"], T["theme_dark"]],
        index=0 if st.session_state.theme_mode == "Light" else 1
    )
    st.session_state.theme_mode = "Light" if theme_display == T["theme_light"] else "Dark"

apply_custom_css(st.session_state.theme_mode)

page = st.radio("", T["nav"], horizontal=True)

# -----------------------------
# Pages
# -----------------------------
if page == T["nav"][0]:
    chatbot_url = "https://claude.ai/public/artifacts/a3324fa8-e26c-4eb8-ab95-779f14b9f59c"

    st.title(T["hero_title"])
    st.markdown(
        f'<div class="hero-subtitle-custom">{T["hero_subtitle"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="hero-text-custom">{T["hero_text"]}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="soft-box">
            <h4>{T["chatbot_info_title"]}</h4>
            <p>{T["chatbot_info_text"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="chatbot-card-wrap">
            <a class="chatbot-card" href="{chatbot_url}" target="_blank">
                <div class="chatbot-title">{T['chatbot_title']}</div>
                <div class="chatbot-desc">{T['chatbot_desc']}</div>
                <div class="click-pointer">👆</div>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
    show_main_image(T["image_caption"], T["image_not_found"])

elif page == T["nav"][1]:
    st.header(T["about_title"])
    st.write(T["about_text"])
    st.markdown(
        f"""
        <div class="soft-box">
            {T["about_note"]}
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
            clean_name = name.strip()
            clean_email = email.strip()
            clean_message = message.strip()

            if not clean_name or not clean_email or not clean_message:
                st.warning(T["form_warning"])
            elif not is_valid_email(clean_email):
                st.warning(T["form_invalid_email"])
            else:
                save_contact(clean_name, clean_email, clean_message, language)
                st.success(T["form_success"])

st.markdown(f"<div class='footer'>{T['footer']}</div>", unsafe_allow_html=True)

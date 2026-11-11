JAZZMIN_SETTINGS = {
    # Brauzer sarlavhasi (Title)
    "site_title": "Boshqaruv Paneli",

    # Admin panel tepasidagi sarlavha (Header)
    "site_header": "Mening Loyiham",

    # Chap yuqori burchakdagi brend nomi
    "site_brand": "Admin Panel",

    # Logotip yo'li (static papkadan olinadi, masalan: 'img/logo.png')
    "site_logo": None,

    # Login sahifasidagi logotip
    "login_logo": None,

    # Login sahifasi uchun qorong'u mavzu logotipi
    "login_logo_dark": None,

    # Logotipga CSS klasslar qo'shish (masalan: 'img-circle')
    "site_logo_classes": "img-circle",

    # Brauzer tabidagi kichik rasm (Favicon)
    "site_icon": None,

    # Login sahifasidagi xush kelibsiz matni
    "welcome_sign": "Tizimga xush kelibsiz",

    # Pastki qismdagi (Footer) mualliflik huquqi matni
    "copyright": "Kompaniya Nomi © 2026",

    # Yuqori qidiruv maydoni qaysi modellardan qidirishi
    "search_model": ["auth.User", "auth.Group"],

    # Foydalanuvchi avatar maydoni nomi (User modelida bo'lsa)
    "user_avatar": None,

    ############
    # Yuqori Menyu (Top Menu)
    ############
    "topmenu_links": [
        # Bosh sahifaga havola
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},

        # Tashqi havola (yangi oynada ochiladi)
        {"name": "Saytga o'tish", "url": "/", "new_window": True},

        # Modelga tezkor havola
        {"model": "auth.User"},

        # Ilova (App) ichidagi barcha modellarni ochuvchi menyu
        {"app": "books"},
    ],

    #############
    # Foydalanuvchi menyusi (O'ng yuqori burchakda)
    #############
    "usermenu_links": [
        {"name": "Qo'llab-quvvatlash", "url": "https://t.me", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Yon Menyu (Side Menu)
    #############
    # Yon menyuni ko'rsatish
    "show_sidebar": True,

    # Menyuni kengaytirilgan holda ochish
    "navigation_expanded": True,

    # Ma'lum bir ilova yoki modellarni menyudan yashirish
    "hide_apps": [],
    "hide_models": [],

    # Ilova va modellarni tartiblash (nomlari bo'yicha)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Ilova va modellar uchun FontAwesome ikonkalari
    # To'liq ro'yxat: https://fontawesome.com
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Ikonka berilmagan modellar uchun standart ikonkalar
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Bog'liq modellar (Related Modal)
    #################
    # Pop-up oyna o'rniga modal oyna ishlatish
    "related_modal_active": False,

    #############
    # UI Sozlamalari
    #############
    # Maxsus CSS yoki JS fayllar ulash (static papkadan)
    "custom_css": None,
    "custom_js": None,

    # Saytda ko'rsatish uchun Google Fonts
    "use_google_fonts_cdn": True,

    # Jonli UI dizayn o'zgartirgichni ko'rsatish (sozlash uchun qulay)
    "show_ui_builder": False,

    ###############
    # Tahrirlash sahifasi ko'rinishi (Change view)
    ###############
    # Variantlar: single, horizontal_tabs (standart), vertical_tabs, collapsible, carousel
    "changeform_format": "horizontal_tabs",
    
    # Alohida modellar uchun ko'rinishni o'zgartirish
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },

    # Tillarni almashtirish tugmasini qo'shish (Django i18n yoqilgan bo'lsa)
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    # Mavzular: default, cerulean, cosmo, cyborg, darkly, flatly, journal, litera, lumen, lux, materia, minty, pulse, sandstone, simplex, sketchy, slate, solar, spacelab, superhero, united, yeti
    "theme": "default",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

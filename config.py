"""
DR RAJESH KHANDELWAL IBC CONFIGURATION
=====================================

Supreme Identity and Connection Settings
for DR RAJESH KHANDELWAL IBC
"""

import os

# =========================================================
# 👑 SUPREME IDENTITY
# =========================================================

APP_NAME = "DR RAJESH KHANDELWAL IBC"
DISPLAY_NAME = "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑"

# Supreme IDs
PERSON_ID = "PRS-7K4M-2Q8N-6T1X"
BUSINESS_ID = "BUS-2M7R-9Q4A-6T8C"
COMPANY_ID = "CMP-8D3F-6N1Q-4X9K"
SUPREME_ID = "SUP-9C4M-7X2K-6P8R"

# User Information
INTERNAL_USER_ID = "0194F8A27C317B4E9D218A6F3C5B1E90"
USERNAME = "RAJESHKHANDELWALOFFICIAL"
ROLE = "SUPREME_OWNER"
LEVEL = 100  # Maximum level - Supreme Owner
STATUS = "ACTIVE"

# =========================================================
# 📡 PLATFORM CONNECTIONS
# =========================================================

PLATFORM_CONNECTIONS = {
    "SUPREMESETUHUB": {
        "name": "SUPREMESETUHUB",
        "url": "https://rajesh-khandelwal.github.io/SUPREMESETUHUB/",
        "repo": "https://github.com/RAJESH-KHANDELWAL/SUPREMESETUHUB",
        "type": "PRIMARY",
        "description": "All-in-One Digital Ecosystem Platform",
        "modules": [
            "Master Identity",
            "Authentication",
            "Authorization",
            "Business Management",
            "AI Services",
            "Storage",
            "Security",
            "Dashboard",
            "Social Integration",
            "Mukti Mahal"
        ]
    },
    "RAJESHKHANDELWAL": {
        "name": "RAJESHKHANDELWAL",
        "url": "https://rajesh-khandelwal.github.io/RAJESHKHANDELWAL/",
        "repo": "https://github.com/RAJESH-KHANDELWAL/RAJESHKHANDELWAL",
        "type": "AI_ENGINE",
        "description": "AI Engine and Advanced ML Integration",
        "modules": [
            "Advanced AI Logic",
            "Machine Learning",
            "Intelligent Automation",
            "Integration Services",
            "Analytics"
        ]
    }
}

# =========================================================
# 📧 EMAIL CONFIGURATION
# =========================================================

EMAILS = [
    "DRRAJESHKHANDELWALIBCOFFICIAL@GMAIL.COM",
    "RAJESHKHANDELWAL@GMAIL.COM",
    "RAJESHKHANDELWAL468@GMAIL.COM",
    "RAJESHKHANDELWALOFFICIAL@GMAIL.COM",
    "DRRAJESHKHANDELWALIBC@GMAIL.COM",
    "INFO@RAJESHKHANDELWALOFFICIAL.COM"
]

PRIMARY_EMAIL = "DRRAJESHKHANDELWALIBCOFFICIAL@GMAIL.COM"

# =========================================================
# 📛 ALIAS NAMES
# =========================================================

ALIAS_NAMES = [
    "RAJESHKHANDELWAL",
    "RAJESHKHANDELWAL OFFICIAL",
    "SUPREME RAJESH KHANDELWAL",
    "SUPREME RAJESH KHANDELWAL OFFICIAL",
    "SUPREME DR RAJESH KHANDELWAL IBC",
    "SUPREME DR RAJESH KHANDELWAL IBC OFFICIAL",
    "DR RAJESH KHANDELWAL IBC",
    "DR RAJESH KHANDELWAL IBC OFFICIAL",
    "RAJESHKHANDELWALOFFICIAL"
]

# =========================================================
# 🎯 PROFILE SETTINGS
# =========================================================

PROFILE_CONFIG = {
    "visibility": "OWNER_ONLY",
    "two_factor_enabled": True,
    "dashboard_name": "🔱 🕉️ SUPREME SHIV SHAKTI SYSTEM 🕉️ 🔱",
    "dashboard_theme": "SUPREME",
    "profile_theme": "PREMIUM_DARK",
    "system_version": "1.0.0"
}

# =========================================================
# 🏷️ PROFILE METADATA
# =========================================================

PROFILE_METADATA = {
    "title": "Digital Pioneer | AI Visionary",
    "bio": "Creator of SUPREMESETUHUB. Building the next generation of digital ecosystems.",
    "avatar_type": "PREMIUM",
    "badge_supreme": True,
    "badge_verified": True,
    "badge_official": True,
    "followers": "1.2M+",
    "following": "456K",
    "posts": "2.3K"
}

# =========================================================
# 🔐 SECURITY SETTINGS
# =========================================================

SECURITY_CONFIG = {
    "password_hash_method": "PBKDF2-SHA256",
    "session_timeout_minutes": 3600,
    "max_login_attempts": 5,
    "account_lockout_duration_minutes": 30,
    "password_expiry_days": 90,
    "require_email_verification": True,
    "require_phone_verification": True
}

# =========================================================
# 📊 PERMISSIONS
# =========================================================

PERMISSIONS = [
    "MANAGE_IDENTITY",
    "MANAGE_USERS",
    "MANAGE_BUSINESS",
    "MANAGE_SECURITY",
    "MANAGE_AI",
    "MANAGE_STORAGE",
    "MANAGE_DASHBOARD",
    "MANAGE_ANALYTICS",
    "MANAGE_SOCIAL",
    "MANAGE_INTEGRATIONS",
    "MANAGE_MUKTI_MAHAL"
]

# =========================================================
# 🌐 SYSTEM CONFIGURATION
# =========================================================

SYSTEM_CONFIG = {
    "app_name": APP_NAME,
    "environment": os.getenv("ENVIRONMENT", "production"),
    "debug": os.getenv("DEBUG", "False").lower() == "true",
    "port": int(os.getenv("PORT", "5000")),
    "host": os.getenv("HOST", "0.0.0.0"),
    "database_url": os.getenv("DATABASE_URL", "sqlite:///supremeibc.db"),
    "redis_url": os.getenv("REDIS_URL", "redis://localhost:6379")
}

# =========================================================
# 👑 SUPREME BRANDING
# =========================================================

BRANDING = {
    "primary_color": "#1F41BB",
    "secondary_color": "#E7245D",
    "accent_color": "#FFB800",
    "logo": "👑 DR RAJESH KHANDELWAL IBC 👑",
    "tagline": "Digital Pioneer | AI Visionary | Supreme Owner",
    "mission": "Building the next generation of digital ecosystems"
}

# =========================================================
# 📱 SOCIAL PRESENCE
# =========================================================

SOCIAL_PRESENCE = {
    "supremesetuhub": {
        "platform": "SUPREMESETUHUB",
        "username": USERNAME,
        "verified": True,
        "official": True,
        "followers": "1.2M+"
    },
    "github": {
        "platform": "GITHUB",
        "username": "RAJESH-KHANDELWAL",
        "verified": True,
        "url": "https://github.com/RAJESH-KHANDELWAL"
    }
}

# =========================================================
# 🚀 STARTUP CONFIGURATION
# =========================================================

STARTUP_CONFIG = {
    "initialize_database": True,
    "create_default_owner": True,
    "load_platform_connections": True,
    "enable_social_integration": True,
    "enable_ai_services": True
}

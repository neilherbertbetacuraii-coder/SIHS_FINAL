"""
Configuration Settings for School Website
Centralized configuration for easy customization
"""

# ===========================================
# SCHOOL INFORMATION
# ===========================================
SCHOOL_NAME = "Modern Academy"
SCHOOL_TAGLINE = "Excellence in Education"
SCHOOL_PHONE = "+1 (555) 123-4567"
SCHOOL_EMAIL = "sanisidrohighschool-kadingilan@edu.ph"
SCHOOL_ADDRESS = "P3, Poblacion, Kadingilan, Bukidnon"

# ===========================================
# SOCIAL MEDIA LINKS
# ===========================================
SOCIAL_MEDIA = {
    'facebook': 'https://facebook.com/your-school',
    'twitter': 'https://twitter.com/your-school',
    'instagram': 'https://instagram.com/your-school',
    'youtube': 'https://youtube.com/your-school',
    'linkedin': 'https://linkedin.com/company/your-school'
}

# ===========================================
# PROGRAMS INFORMATION
# ===========================================
PROGRAMS = {
    'kindergarten': {
        'name': 'Kindergarten',
        'grade': 'Ages 3-5',
        'description': 'Early childhood development through play-based learning',
        'icon': 'fa-child',
        'color': 'primary'
    },
    'elementary': {
        'name': 'Elementary',
        'grade': 'Grades 1-6',
        'description': 'Strong foundation in academics with extracurricular activities',
        'icon': 'fa-pencil',
        'color': 'success'
    },
    'junior_high': {
        'name': 'Junior High',
        'grade': 'Grades 7-9',
        'description': 'Advanced curriculum with STEM and sports programs',
        'icon': 'fa-graduation-cap',
        'color': 'info'
    },
    'senior_high': {
        'name': 'Senior High',
        'grade': 'Grades 10-12',
        'description': 'College preparation with specialized tracks',
        'icon': 'fa-university',
        'color': 'warning'
    }
}

# ===========================================
# FEES INFORMATION
# ===========================================
FEES = {
    'kindergarten': {
        'monthly': 2500,
        'currency': '₹',
        'includes': ['Classes', 'Lunch', 'Activities']
    },
    'elementary': {
        'monthly': 3500,
        'currency': '₹',
        'includes': ['Classes', 'Lunch', 'Activities']
    },
    'junior_high': {
        'monthly': 4500,
        'currency': '₹',
        'includes': ['Classes', 'Lunch', 'Activities']
    },
    'senior_high': {
        'monthly': 5500,
        'currency': '₹',
        'includes': ['Classes', 'Lunch', 'Activities']
    }
}

# ===========================================
# FACULTY INFORMATION
# ===========================================
FACULTY = [
    {
        'name': 'Dr. John Smith',
        'position': 'Principal',
        'qualification': 'Ed.D. in Educational Administration',
        'experience': '20 years'
    },
    {
        'name': 'Ms. Sarah Johnson',
        'position': 'Vice Principal',
        'qualification': 'M.Ed. in Curriculum Design',
        'experience': '15 years'
    },
    {
        'name': 'Prof. Michael Brown',
        'position': 'Head of Academics',
        'qualification': 'M.Sc. in Physics',
        'experience': '18 years'
    },
    {
        'name': 'Ms. Emily Davis',
        'position': 'Student Counselor',
        'qualification': 'M.A. in Psychology',
        'experience': '12 years'
    }
]

# ===========================================
# CORE VALUES
# ===========================================
CORE_VALUES = {
    'excellence': {
        'icon': 'fa-star',
        'description': 'Excellence in all aspects of work'
    },
    'integrity': {
        'icon': 'fa-handshake',
        'description': 'Honesty and moral principles'
    },
    'respect': {
        'icon': 'fa-people-arrows',
        'description': 'Value dignity and diversity'
    },
    'innovation': {
        'icon': 'fa-lightbulb',
        'description': 'Embrace change and improvement'
    }
}

# ===========================================
# SCHOOL STATISTICS
# ===========================================
STATISTICS = {
    'years_of_excellence': 25,
    'total_students': 500,
    'faculty_members': 50,
    'success_rate': 95
}

# ===========================================
# SPECIAL PROGRAMS
# ===========================================
SPECIAL_PROGRAMS = [
    {
        'name': 'Sports & Recreation',
        'icon': 'fa-basketball',
        'description': 'Basketball, Football, Volleyball, Tennis, Swimming'
    },
    {
        'name': 'Clubs & Societies',
        'icon': 'fa-users',
        'description': 'Debate, Science, Art, Music, Drama and Technology clubs'
    },
    {
        'name': 'STEM Programs',
        'icon': 'fa-flask',
        'description': 'Robotics, Coding, Science Projects and Innovation Labs'
    },
    {
        'name': 'Field Trips',
        'icon': 'fa-bus',
        'description': 'Educational excursions to museums and historical sites'
    }
]

# ===========================================
# SCHOLARSHIP TYPES
# ===========================================
SCHOLARSHIPS = {
    'academic': {
        'name': 'Academic Excellence',
        'percentage': '25-75%',
        'criteria': 'Based on academic performance'
    },
    'sports': {
        'name': 'Sports & Talent',
        'percentage': 'Merit-based',
        'criteria': 'For athletes and artists'
    },
    'need_based': {
        'name': 'Need-Based',
        'percentage': 'Up to 100%',
        'criteria': 'Financial assistance for deserving families'
    },
    'staff': {
        'name': 'Staff Children',
        'percentage': '20-50%',
        'criteria': 'For staff members\' children'
    }
}

# ===========================================
# FLASK CONFIGURATION
# ===========================================
class Config:
    """Flask configuration settings"""
    ENV = 'development'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'dev-secret-key-change-in-production'
    JSON_SORT_KEYS = False
    PREFERRED_URL_SCHEME = 'http'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'
    SECRET_KEY = 'your-production-secret-key'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# ===========================================
# ADMISSION TIMELINE
# ===========================================
ADMISSION_TIMELINE = [
    {
        'step': 1,
        'title': 'Apply Online',
        'description': 'Fill out the application form with required information',
        'timeline': 'Available Year-Round',
        'icon': 'fa-calendar'
    },
    {
        'step': 2,
        'title': 'Submit Documents',
        'description': 'Provide birth certificate, previous records, and health documents',
        'timeline': 'Within 2 Weeks of Application',
        'icon': 'fa-file-alt'
    },
    {
        'step': 3,
        'title': 'Assessment',
        'description': 'Attend entrance exam or assessment session',
        'timeline': 'Scheduled as Per Convenience',
        'icon': 'fa-person'
    },
    {
        'step': 4,
        'title': 'Admission Decision',
        'description': 'Receive admission decision and enrollment confirmation',
        'timeline': 'Within 5 Working Days',
        'icon': 'fa-check'
    }
]

# ===========================================
# FAQ ITEMS
# ===========================================
FAQ_ITEMS = [
    {
        'question': 'What is the minimum age requirement for admission?',
        'answer': '''For Kindergarten, children should be 3 years old by the end of June. 
                     For elementary, students must have completed kindergarten or be at least 
                     6 years old. Age proofs through birth certificate are mandatory.'''
    },
    {
        'question': 'What documents are required for admission?',
        'answer': '''Required documents include: Birth Certificate, Vaccination Records, 
                     Previous School Report Card, Medical Certificate, and Parents' ID proof. 
                     A complete checklist will be provided during the application process.'''
    },
    {
        'question': 'Is there an entrance examination?',
        'answer': '''Yes, entrance examinations are conducted for classes 2 and above. 
                     For Kindergarten and Grade 1, we conduct a readiness assessment and 
                     a parent interview.'''
    },
    {
        'question': 'How long does the admission process take?',
        'answer': '''The complete admission process typically takes 2-3 weeks from application 
                     to final admission decision. Applications are processed on a rolling basis 
                     throughout the year.'''
    },
    {
        'question': 'Do you offer payment plans?',
        'answer': '''Yes, we offer flexible payment options including monthly, quarterly, 
                     and annual payment plans. Special arrangements can be made upon application 
                     and discussion with the administration.'''
    }
]

# ===========================================
# NAVIGATION MENU STRUCTURE
# ===========================================
NAVIGATION_MENU = [
    {
        'label': 'HOME',
        'url': '/',
        'icon': 'fa-home'
    },
    {
        'label': 'ABOUT',
        'url': '/about',
        'icon': 'fa-info-circle',
        'dropdown': True,
        'items': [
            {'name': 'History', 'icon': 'fa-book'},
            {'name': 'Mission & Vision', 'icon': 'fa-bullseye'},
            {'name': 'Leadership', 'icon': 'fa-users'},
            {'name': 'Gallery', 'icon': 'fa-images'}
        ]
    },
    {
        'label': 'PROGRAMS',
        'url': '/programs',
        'icon': 'fa-book-open',
        'dropdown': True,
        'items': [
            {'name': 'Kindergarten', 'icon': 'fa-child'},
            {'name': 'Elementary', 'icon': 'fa-pencil'},
            {'name': 'Junior High', 'icon': 'fa-graduation-cap'},
            {'name': 'Senior High', 'icon': 'fa-university'}
        ]
    },
    {
        'label': 'ADMISSION',
        'url': '/admission',
        'icon': 'fa-clipboard-list',
        'dropdown': True,
        'items': [
            {'name': 'Enroll Now', 'icon': 'fa-edit'},
            {'name': 'Requirements', 'icon': 'fa-info-circle'},
            {'name': 'Scholarships', 'icon': 'fa-gift'},
            {'name': 'FAQ', 'icon': 'fa-question'}
        ]
    },
    {
        'label': 'FEED',
        'url': '#',
        'icon': 'fa-newspaper'
    },
    {
        'label': 'ASSIST',
        'url': '#',
        'icon': 'fa-life-ring'
    },
    {
        'label': 'CONTACT',
        'url': '#',
        'icon': 'fa-envelope'
    }
]

# ===========================================
# PAGE METADATA
# ===========================================
PAGE_META = {
    'home': {
        'title': 'Home',
        'description': 'Welcome to our school - Excellence in Education',
        'keywords': 'school, education, learning'
    },
    'about': {
        'title': 'About Us',
        'description': 'Learn about our school history and mission',
        'keywords': 'about, history, mission, vision'
    },
    'programs': {
        'title': 'Our Programs',
        'description': 'Explore our educational programs',
        'keywords': 'programs, education, curriculum'
    },
    'admission': {
        'title': 'Admission',
        'description': 'Apply now and join our school',
        'keywords': 'admission, enrollment, apply'
    }
}

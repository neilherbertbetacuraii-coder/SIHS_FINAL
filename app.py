"""
School Website Navigation System - Flask Backend
A modern, responsive school website with Mega Menu navigation
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


class School:
    """School information configuration"""
    name = "San Isidro High School Page"
    tagline = "Excellence in Education"
    phone = "+1 (555) 123-4567"
    email = "sanisidrohighschool-kadingilan@edu.ph"
    address = "P3, Poblacion, Kadingilan, Bukidnon"


@app.route('/')
def index():
    """Home page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline,
            'phone': School.phone,
            'email': School.email,
            'address': School.address
        },
        'current_year': datetime.now().year
    }
    return render_template('index.html', **context)


@app.route('/about')
def about():
    """About page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('about.html', **context)


@app.route('/programs')
def programs():
    """Programs page"""
    programs_data = {
        'Kindergarten': 'Ages 3-5',
        'Elementary': 'Grades 1-6',
        'Junior High': 'Grades 7-9',
        'Senior High': 'Grades 10-12'
    }
    return render_template('programs.html', programs=programs_data)


@app.route('/admission')
def admission():
    """Admission page"""
    context = {
        'school_name': School.name
    }
    return render_template('admission.html', **context)


# About section routes
@app.route('/history')
def history():
    """History page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('history.html', **context)


@app.route('/mission-vision')
def mission_vision():
    """Mission, Vision & Core Principles page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('mission-vision.html', **context)


@app.route('/school-logo')
def school_logo():
    """School Logo page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('school-logo.html', **context)


@app.route('/faculty')
def faculty():
    """Admin, Faculty & Staff page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('faculty.html', **context)


@app.route('/gallery')
def gallery():
    """Gallery page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('gallery.html', **context)


# Programs section routes
@app.route('/academic-programs')
def academic_programs():
    """Academic Programs page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('academic-programs.html', **context)


@app.route('/curriculum')
def curriculum():
    """Curriculum Overview page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('curriculum.html', **context)


@app.route('/special-programs')
def special_programs():
    """Special Programs page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('special-programs.html', **context)


@app.route('/student-life')
def student_life():
    """Student Life page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('student-life.html', **context)


# Admission section routes
@app.route('/how-to-apply')
def how_to_apply():
    """How to Apply page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('how-to-apply.html', **context)


@app.route('/requirements')
def requirements():
    """Requirements page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('requirements.html', **context)


@app.route('/fees')
def fees():
    """Fees & Payment page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('fees.html', **context)


@app.route('/scholarships')
def scholarships():
    """Scholarships page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline
        }
    }
    return render_template('scholarships.html', **context)


@app.route('/school-feed')
def school_feed():
    """School Feed page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline,
            'phone': School.phone,
            'email': School.email,
            'address': School.address
        }
    }
    return render_template('school-feed.html', **context)


@app.route('/contact')
def contact():
    """Contact page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline,
            'phone': School.phone,
            'email': School.email,
            'address': School.address
        },
        'current_year': datetime.now().year
    }
    return render_template('contact.html', **context)


@app.route('/assist')
def assist():
    """Assist page"""
    context = {
        'school': {
            'name': School.name,
            'tagline': School.tagline,
            'phone': School.phone,
            'email': School.email,
            'address': School.address
        },
        'current_year': datetime.now().year
    }
    return render_template('assist.html', **context)


@app.route('/login')
def login():
    """Login page"""
    context = {
        'school': {
            'name': "Torres Capitol College",
            'tagline': "Excellence in Education"
        }
    }
    return render_template('login.html', **context)


@app.route('/enrollment')
def enrollment():
    """Enrollment page"""
    context = {
        'school': {
            'name': "Torres Capitol College",
            'tagline': "Excellence in Education"
        }
    }
    return render_template('enrollment.html', **context)


@app.route('/api/menu')
def api_menu():
    """API endpoint for navigation menu structure"""
    menu_data = {
        'main_items': [
            {'label': 'HOME', 'url': '/'},
            {'label': 'ABOUT', 'url': '/about', 'mega_menu': 'about'},
            {'label': 'PROGRAMS', 'url': '/programs', 'mega_menu': 'programs'},
            {'label': 'ADMISSION', 'url': '/admission', 'mega_menu': 'admission'},
            {'label': 'FEED', 'url': '/school-feed'},
            {'label': 'ASSIST', 'url': '/assist'},
            {'label': 'CONTACT', 'url': '/contact'}
        ]
    }
    return jsonify(menu_data)


@app.route('/api/search', methods=['POST'])
def api_search():
    """API endpoint for search functionality"""
    query = request.get_json().get('query', '').lower()
    
    # Mock search results
    results = []
    if query:
        search_items = [
            {'title': 'About Us', 'url': '/about'},
            {'title': 'Programs', 'url': '/programs'},
            {'title': 'Admission', 'url': '/admission'},
            {'title': 'Contact Us', 'url': '#'},
        ]
        results = [item for item in search_items if query in item['title'].lower()]
    
    return jsonify({'results': results})


@app.route('/api/enroll', methods=['POST'])
def api_enroll():
    """API endpoint for enrollment submission"""
    data = request.get_json()
    # In a real application, this would save to a database
    return jsonify({
        'success': True,
        'message': f"Thank you for your interest, {data.get('name', 'Guest')}! We'll contact you soon."
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)

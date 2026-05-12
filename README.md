# School Website Navigation System

A modern, professional, and responsive school website using Flask backend with HTML5, CSS3, JavaScript, and Bootstrap 5 frontend.

## 🎯 Features

### Navigation
- **Sticky Responsive Navbar** - Stays at the top while scrolling
- **Mega Menus** - Professional dropdown menus with rich content:
  - ABOUT - History, Mission & Vision, Faculty, Gallery
  - PROGRAMS - Kindergarten, Elementary, Junior High, Senior High
  - ADMISSION - Enrollment, Requirements, Scholarships, FAQ
- **Mobile-Friendly Hamburger Menu** - Fully responsive design
- **Search Functionality** - Real-time search with API integration
- **Enroll Now CTA Button** - Prominent enrollment call-to-action

### Design & UX
- **Smooth Animations & Transitions** - Modern hover effects and transitions
- **Professional UI Design** - Clean, academic, and corporate aesthetic
- **Font Awesome Icons** - Rich icon library for visual appeal
- **Bootstrap 5 Integration** - Responsive grid system and components
- **Dark Sticky Footer** - Complete page structure

### Pages Included
- **Home** - Hero section, features, statistics, programs preview, news
- **About** - History, mission/vision, core values, faculty, gallery
- **Programs** - Detailed program information with timeline and highlights
- **Admission** - Timeline, requirements, fees, scholarships, FAQ

### Technical Features
- **Flask Backend** - Clean Python Flask framework
- **Jinja2 Templates** - Template inheritance and modular design
- **RESTful APIs** - Endpoints for menu, search, and enrollment
- **Form Handling** - Interactive enrollment form with validation
- **Responsive Design** - Mobile-first approach
- **Accessibility** - WCAG compliant design

## 📋 Project Structure

```
school_website/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── config.py              # Configuration settings
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/
│   │   └── script.js      # JavaScript functionality
│   └── images/            # Image folder
└── templates/
    ├── base.html          # Base template with navigation
    ├── index.html         # Home page
    ├── about.html         # About page
    ├── programs.html      # Programs page
    ├── admission.html     # Admission page
    ├── 404.html           # 404 error page
    └── 500.html           # 500 error page
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
cd school_website
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

## 🎨 Customization

### School Information
Edit the `School` class in `app.py`:
```python
class School:
    name = "Modern Academy"
    tagline = "Excellence in Education"
    phone = "+1 (555) 123-4567"
    email = "sanisidrohighschool-kadingilan@edu.ph"
    address = "P3, Poblacion, Kadingilan, Bukidnon"
```

### Colors & Styling
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    --success-color: #198754;
    /* ... more colors ... */
}
```

### Navigation Menu
The navigation structure is defined in `templates/base.html`. Modify the navbar section to add/remove menu items.

### Content
Edit individual page templates in the `templates` folder to customize content:
- `index.html` - Home page content
- `about.html` - About page content
- `programs.html` - Programs description
- `admission.html` - Admission details

## 🌐 Navigation Structure

### Main Navigation Items
1. **HOME** - Landing page with hero section
2. **ABOUT** - School information and history
   - History
   - Mission, Vision & Core Values
   - Faculty & Leadership
   - Campus Gallery
3. **PROGRAMS** - Educational programs
   - Kindergarten (Ages 3-5)
   - Elementary (Grades 1-6)
   - Junior High (Grades 7-9)
   - Senior High (Grades 10-12)
4. **ADMISSION** - Enrollment information
   - Enroll Now CTA
   - Enrollment Requirements
   - Scholarship Information
   - Admission FAQ
5. **SCHOOL FEED** - News and updates
6. **ASSIST** - Student support services
7. **CONTACT** - Contact information

## 📱 Responsive Design

The website is fully responsive with breakpoints:
- **Mobile** (< 576px) - Hamburger menu, stacked layout
- **Tablet** (576px - 991px) - Medium layout, responsive grid
- **Desktop** (992px+) - Full mega menu, optimal spacing
- **Large Desktop** (1200px+) - Max width container

## 🔧 API Endpoints

### `/api/menu`
Returns the navigation menu structure.
```
GET /api/menu
Response: JSON with menu items
```

### `/api/search`
Search functionality.
```
POST /api/search
Body: {"query": "search term"}
Response: List of matching results
```

### `/api/enroll`
Enrollment form submission.
```
POST /api/enroll
Body: {
    "name": "Student Name",
    "email": "email@example.com",
    "phone": "1234567890",
    "grade": "Kindergarten"
}
```

## 🎯 Features Breakdown

### Mega Menu System
- Auto-expand on hover (desktop)
- Click to expand (mobile)
- 4-column layout for ABOUT
- 2x2 grid for PROGRAMS
- 2-column layout for ADMISSION

### Search Modal
- Real-time search capability
- Keyboard shortcuts (Enter key)
- Debounced input for performance

### Enrollment Modal
- Form validation
- Email validation
- Grade level selection
- Toast notifications for feedback

### Animations
- Fade-in effects on scroll
- Smooth hover transitions
- Bounce animations for icons
- Slide animations for menus

## 🔐 Security Considerations

- CSRF protection ready (add Flask-WTF for production)
- Input sanitization in forms
- Error handling for 404 and 500 errors
- Secure headers recommendations

## ⚡ Performance Optimizations

- CSS minification ready
- Lazy loading for images
- Efficient JavaScript bundling
- Bootstrap CDN for faster loading
- Reduced motion support for accessibility

## 🌍 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📚 Technologies Used

### Backend
- Python 3.7+
- Flask 2.3.2
- Jinja2 template engine

### Frontend
- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap 5.3.0
- Font Awesome 6.4.0

## 🚀 Deployment

### Production Deployment
1. Install Gunicorn: `pip install gunicorn`
2. Run: `gunicorn app:app`
3. Use Nginx as reverse proxy
4. Enable SSL/HTTPS
5. Set `debug=False` in app.py

### Environment Variables
Create `.env` file for production:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key
DEBUG=False
```

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Support

For issues, questions, or suggestions, please open an issue or contact the development team.

## 🔄 Future Enhancements

- [ ] Student Portal
- [ ] Online Payment Integration
- [ ] CMS for dynamic content
- [ ] Multi-language support
- [ ] Blog/News system
- [ ] Event Calendar
- [ ] Alumni Portal
- [ ] Mobile app
- [ ] Database integration
- [ ] Email notifications

---

**Happy Learning! 🎓**

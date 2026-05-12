# Quick Start Guide - School Website Navigation System

## 🚀 Get Started in 3 Steps

### Step 1: Install Python Requirements
```bash
pip install -r requirements.txt
```

This installs:
- Flask 2.3.2 - Web framework
- Werkzeug 2.3.6 - WSGI utility library
- Jinja2 3.1.2 - Template engine

### Step 2: Run the Flask Server
```bash
python app.py
```

Output should show:
```
* Running on http://127.0.0.1:5000
* Running on http://192.168.1.56:5000
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## 🎯 What You Get

### ✅ Complete Responsive Design
- Desktop, Tablet, and Mobile optimized
- Sticky navigation bar
- Mobile hamburger menu
- Touch-friendly interactions

### ✅ Modern Navigation System
- **Mega Menus** with professional design
- **Search functionality** with real-time results
- **Enroll Now** call-to-action button
- Smooth animations and transitions

### ✅ Multiple Pages
- **Home** - Hero section with features and programs preview
- **About** - School history, mission/vision, faculty, gallery
- **Programs** - Detailed information for each grade level
- **Admission** - Enrollment process, requirements, fees, FAQ

### ✅ Professional Features
- Contact information in footer
- Social media links
- Newsletter subscription
- Responsive image galleries
- Accordion FAQs
- Modal enrollment form

---

## 📂 Project Structure

```
SIHS_WEB_FINAL - Copy/
├── app.py                    # Flask application (run this!)
├── requirements.txt          # Python packages
├── README.md                 # Full documentation
├── SETUP.md                  # This file
├── static/
│   ├── css/style.css         # All styling
│   ├── js/script.js          # All interactivity
│   └── images/               # For your images
└── templates/
    ├── base.html             # Navigation & layout
    ├── index.html            # Home page
    ├── about.html            # About page
    ├── programs.html         # Programs page
    ├── admission.html        # Admission page
    ├── 404.html              # Error page
    └── 500.html              # Server error
```

---

## 🎨 Customization Guide

### Change School Name
Edit `app.py` line 12:
```python
class School:
    name = "Your School Name"  # Change this
    tagline = "Your Tagline"   # And this
```

### Change Colors
Edit `static/css/style.css` lines 10-21:
```css
:root {
    --primary-color: #0d6efd;    /* Main color */
    --success-color: #198754;    /* Green color */
    --info-color: #0dcaf0;       /* Blue color */
    /* ... more colors ... */
}
```

### Update Contact Info
Edit `app.py` lines 13-16:
```python
phone = "Your Phone Number"
email = "your-email@school.edu"
address = "Your School Address"
```

### Edit Page Content
Edit individual HTML files in `templates/` folder:
- `index.html` - Home page
- `about.html` - About section
- `programs.html` - Programs details
- `admission.html` - Admission info

---

## 🌐 Navigation Menu Structure

```
HOME
├── (Direct link)

ABOUT (Mega Menu)
├── History
├── Mission, Vision & Core Values
├── Leadership Team
└── Gallery

PROGRAMS (Mega Menu)
├── Kindergarten
├── Elementary
├── Junior High
└── Senior High

ADMISSION (Mega Menu)
├── Enroll Now
├── Enrollment Requirements
├── Scholarship Information
└── Admission FAQ

SCHOOL FEED
├── (Link)

ASSIST
├── (Link)

CONTACT
├── (Link)
```

---

## 💡 Key Features Explained

### 🔍 Mega Menus
Click on ABOUT, PROGRAMS, or ADMISSION to see rich dropdown menus with:
- Icons for visual appeal
- Organized categories
- Rich content preview
- Smooth animations

### 🔎 Search Function
Click the search icon (🔍) to:
- Real-time search results
- Quick navigation
- Modal popup interface

### 📝 Enrollment Form
Click "Enroll Now" to open a modal form for:
- Student name
- Parent email
- Contact phone
- Grade level selection

### 📱 Mobile Experience
On mobile devices:
- Hamburger menu (☰) appears
- Tap to expand navigation
- Optimized touch targets
- Responsive images

---

## 🔧 Common Tasks

### Add a New Menu Item
1. Open `templates/base.html`
2. Find the `<ul class="navbar-nav">` section
3. Add a new `<li>` item with navigation link

### Change Font or Styling
1. Open `static/css/style.css`
2. Modify CSS properties
3. Refresh browser to see changes

### Add Images
1. Save images in `static/images/`
2. Update HTML files with image paths
3. Use: `<img src="{{ url_for('static', filename='images/your-image.jpg') }}">`

### Add New Page
1. Create new HTML file in `templates/` folder
2. Extend base.html: `{% extends "base.html" %}`
3. Add route in `app.py`:
```python
@app.route('/newpage')
def newpage():
    return render_template('newpage.html')
```

---

## 🛠️ Troubleshooting

### Port Already in Use
If port 5000 is busy, edit `app.py` last line:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001
```

### Template Not Found Error
Make sure all HTML files are in `templates/` folder and paths are correct in `app.py`

### CSS/JS Not Loading
Clear browser cache (Ctrl+Shift+Delete) and refresh (Ctrl+F5)

### Images Not Showing
Save images in `static/images/` and use correct paths in HTML

---

## 📱 Testing Responsive Design

### Desktop
- Open browser on full screen
- Test all mega menus
- Click search and enrollment buttons

### Tablet
- Use browser DevTools (F12)
- Select iPad or tablet device
- Test landscape and portrait modes

### Mobile
- Use browser DevTools (F12)
- Select iPhone or mobile device
- Test hamburger menu and mobile layout

---

## 🌟 Next Steps

1. **Personalize Content**
   - Update school name and contact info
   - Edit page content
   - Add school logo image

2. **Add Your Content**
   - Upload school photos
   - Update program descriptions
   - Add actual faculty information

3. **Enhance Features**
   - Connect to database
   - Add email sending for enrollments
   - Integrate payment gateway

4. **Deploy Online**
   - Choose hosting (Heroku, AWS, DigitalOcean)
   - Setup custom domain
   - Enable SSL/HTTPS

---

## 📚 Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Bootstrap 5**: https://getbootstrap.com/
- **Font Awesome Icons**: https://fontawesome.com/
- **Flask Deployment**: https://flask.palletsprojects.com/deployment/

---

## ✨ Features Highlight

✅ **Sticky Navigation** - Bar stays visible while scrolling  
✅ **Mega Menus** - Rich dropdown content  
✅ **Search Function** - Find content quickly  
✅ **Responsive Design** - Works on all devices  
✅ **Modern UI** - Professional appearance  
✅ **Smooth Animations** - Engaging interactions  
✅ **Mobile Menu** - Hamburger navigation  
✅ **Enrollment Form** - Beautiful modal popup  
✅ **FAQ Section** - Accordion-style Q&A  
✅ **Professional Footer** - Complete page structure  

---

## 🎓 Learning Path

1. **Understand the structure** - Learn where files are located
2. **Customize styling** - Change colors and fonts
3. **Edit content** - Update text and information
4. **Add images** - Include your school photos
5. **Test responsiveness** - Check on different devices
6. **Deploy** - Put online for the world to see

---

**Happy Building! 🚀**

For detailed information, see README.md

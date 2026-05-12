/**
 * School Website Navigation System - JavaScript
 * Modern interactive navigation with search and form handling
 */

document.addEventListener('DOMContentLoaded', function () {
    initializeNavigation();
    initializeLogin();
    initializeEnrollment();
    initializeScrollEffects();
    initializeFloatingAssist();
});

/**
 * Initialize Navigation Features
 */
function initializeNavigation() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');

    // Sticky navbar shadow effect
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow');
        } else {
            navbar.classList.remove('shadow');
        }
    });

    // Close mega menu when clicking on a link
    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            const navbar = document.querySelector('.navbar-collapse');
            const bsCollapse = new bootstrap.Collapse(navbar, {
                toggle: false
            });
            // Don't close if it's a dropdown toggle
            if (!this.classList.contains('dropdown-toggle')) {
                bsCollapse.hide();
            }
        });
    });

    // Click-based mega menu behavior
    const megaNavItems = document.querySelectorAll('.mega-nav-item');
    let activeMegaMenu = null;

    megaNavItems.forEach(item => {
        const dropdownToggle = item.querySelector('.dropdown-toggle');
        const megaMenu = item.querySelector('.mega-menu, .about-dropdown, .programs-dropdown, .admission-dropdown');

        if (dropdownToggle && megaMenu) {
            dropdownToggle.addEventListener('click', function (e) {
                e.preventDefault();

                // If this menu is already active, close it
                if (item.classList.contains('active')) {
                    item.classList.remove('active');
                    dropdownToggle.setAttribute('aria-expanded', 'false');
                    activeMegaMenu = null;
                    return;
                }

                // Close any currently open menu
                if (activeMegaMenu) {
                    activeMegaMenu.classList.remove('active');
                    const prevToggle = activeMegaMenu.querySelector('.dropdown-toggle');
                    if (prevToggle) {
                        prevToggle.setAttribute('aria-expanded', 'false');
                    }
                }

                // Open this menu
                item.classList.add('active');
                dropdownToggle.setAttribute('aria-expanded', 'true');
                activeMegaMenu = item;
            });
        }
    });

    // Close mega menu when clicking outside
    document.addEventListener('click', function (e) {
        if (!e.target.closest('.mega-nav-item')) {
            if (activeMegaMenu) {
                activeMegaMenu.classList.remove('active');
                const activeToggle = activeMegaMenu.querySelector('.dropdown-toggle');
                if (activeToggle) {
                    activeToggle.setAttribute('aria-expanded', 'false');
                }
                activeMegaMenu = null;
            }
        }
    });

    // Close mega menu on escape key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && activeMegaMenu) {
            activeMegaMenu.classList.remove('active');
            const activeToggle = activeMegaMenu.querySelector('.dropdown-toggle');
            if (activeToggle) {
                activeToggle.setAttribute('aria-expanded', 'false');
            }
            activeMegaMenu = null;
        }
    });

    console.log('Navigation initialized successfully');
}

/**
 * Initialize Login Modal
 */
function initializeLogin() {
    const loginBtn = document.getElementById('loginBtn');
    const loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
    const loginEmail = document.getElementById('loginEmail');
    const loginForm = document.getElementById('loginForm');

    if (loginBtn) {
        loginBtn.addEventListener('click', function () {
            loginModal.show();
            setTimeout(() => loginEmail.focus(), 500);
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            loginModal.hide();
            // Future login action can be added here
        });
    }
}

/**
 * Perform Search
 */
async function performSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    const query = searchInput.value.trim();

    if (!query) {
        searchResults.innerHTML = '<p class="text-muted p-3">Enter a search term</p>';
        return;
    }

    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query })
        });

        const data = await response.json();

        if (data.results.length > 0) {
            searchResults.innerHTML = data.results.map(result => `
                <a href="${result.url}" class="d-block p-3 text-decoration-none">
                    <i class="fas fa-search"></i> ${result.title}
                </a>
            `).join('');
        } else {
            searchResults.innerHTML = `<p class="text-muted p-3">No results found for "${query}"</p>`;
        }
    } catch (error) {
        console.error('Search error:', error);
        searchResults.innerHTML = '<p class="text-danger p-3">Error performing search</p>';
    }
}

/**
 * Initialize Enrollment Form
 */
function initializeEnrollment() {
    const enrollForm = document.getElementById('enrollForm');

    enrollForm.addEventListener('submit', function (e) {
        e.preventDefault();
        submitEnrollmentForm();
    });
}

/**
 * Submit Enrollment Form
 */
async function submitEnrollmentForm() {
    const name = document.getElementById('enrollName').value;
    const email = document.getElementById('enrollEmail').value;
    const phone = document.getElementById('enrollPhone').value;
    const grade = document.getElementById('enrollGrade').value;

    if (!name || !email) {
        showAlert('Please fill in all required fields', 'warning');
        return;
    }

    try {
        const response = await fetch('/api/enroll', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                email: email,
                phone: phone,
                grade: grade
            })
        });

        const data = await response.json();

        if (data.success) {
            showAlert(data.message, 'success');
            // Reset form
            document.getElementById('enrollForm').reset();
            // Close modal after 2 seconds
            setTimeout(() => {
                bootstrap.Modal.getInstance(document.getElementById('enrollModal')).hide();
            }, 2000);
        } else {
            showAlert('Error submitting enrollment', 'danger');
        }
    } catch (error) {
        console.error('Enrollment error:', error);
        showAlert('Error submitting enrollment form', 'danger');
    }
}

/**
 * Show Alert Message
 */
function showAlert(message, type = 'info') {
    // Create alert element
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.top = '100px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '2000';
    alertDiv.style.minWidth = '300px';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(alertDiv);

    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const alert = new bootstrap.Alert(alertDiv);
        alert.close();
    }, 5000);
}

/**
 * Initialize Floating Assist Button
 */
function initializeFloatingAssist() {
    const assistButton = document.getElementById('floatingAssistButton');
    if (!assistButton) return;

    let isDragging = false;
    let dragMoved = false;
    let startX = 0;
    let startY = 0;
    let originalX = 0;
    let originalY = 0;

    function setPosition(x, y) {
        const minX = 16;
        const minY = 16;
        const maxX = window.innerWidth - assistButton.offsetWidth - 16;
        const maxY = window.innerHeight - assistButton.offsetHeight - 16;
        assistButton.style.left = Math.min(Math.max(x, minX), maxX) + 'px';
        assistButton.style.top = Math.min(Math.max(y, minY), maxY) + 'px';
    }

    function onPointerMove(event) {
        if (!isDragging) return;
        event.preventDefault();
        const x = event.clientX;
        const y = event.clientY;
        const deltaX = x - startX;
        const deltaY = y - startY;
        if (!dragMoved && (Math.abs(deltaX) > 5 || Math.abs(deltaY) > 5)) {
            dragMoved = true;
        }
        setPosition(originalX + deltaX, originalY + deltaY);
    }

    function onPointerUp(event) {
        if (!isDragging) return;
        isDragging = false;
        assistButton.releasePointerCapture(event.pointerId);
        assistButton.style.cursor = 'grab';
        document.removeEventListener('pointermove', onPointerMove);
        document.removeEventListener('pointerup', onPointerUp);
        document.removeEventListener('pointercancel', onPointerUp);
    }

    const rect = assistButton.getBoundingClientRect();
    assistButton.style.position = 'fixed';
    assistButton.style.left = rect.left + 'px';
    assistButton.style.top = rect.top + 'px';
    assistButton.style.right = 'auto';
    assistButton.style.bottom = 'auto';
    assistButton.style.cursor = 'grab';
    assistButton.style.touchAction = 'none';
    assistButton.style.userSelect = 'none';

    assistButton.addEventListener('pointerdown', function (event) {
        if (event.button !== 0) return;
        event.preventDefault();
        isDragging = true;
        dragMoved = false;
        startX = event.clientX;
        startY = event.clientY;
        originalX = assistButton.offsetLeft;
        originalY = assistButton.offsetTop;
        assistButton.style.cursor = 'grabbing';
        assistButton.setPointerCapture(event.pointerId);
        document.addEventListener('pointermove', onPointerMove);
        document.addEventListener('pointerup', onPointerUp);
        document.addEventListener('pointercancel', onPointerUp);
    });

    assistButton.addEventListener('click', function (event) {
        if (dragMoved) {
            event.preventDefault();
            event.stopImmediatePropagation();
            dragMoved = false;
        }
    });

    const assistBubble = document.getElementById('floatingAssistBubble');
    if (assistBubble) {
        assistBubble.classList.add('hidden');
        setTimeout(() => {
            assistBubble.textContent = 'Hi, if you need assistance click me';
            assistBubble.classList.remove('hidden');
            assistBubble.classList.add('visible');
        }, 1500);

        setTimeout(() => {
            assistBubble.textContent = 'Goodbye!';
            assistBubble.classList.remove('visible');
            assistBubble.classList.add('hidden');
        }, 4500);
    }
}

/**
 * Initialize Scroll Effects
 */
function initializeScrollEffects() {
    // Add animations to elements as they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });

    // Observe program cards
    document.querySelectorAll('.program-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });

    // Observe news cards
    document.querySelectorAll('.news-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });

    console.log('Scroll effects initialized');
}

/**
 * Utility: Smooth Scroll to Element
 */
function smoothScrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

/**
 * Utility: Add Loading State to Button
 */
function setButtonLoading(button, isLoading = true) {
    if (isLoading) {
        button.disabled = true;
        button.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
    } else {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-paper-plane"></i> Submit';
    }
}

/**
 * Utility: Debounce Function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Utility: Throttle Function
 */
function throttle(func, limit) {
    let inThrottle;
    return function (...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export functions for use in other scripts
window.schoolWebsite = {
    smoothScrollTo,
    setButtonLoading,
    showAlert,
    performSearch
};

console.log('School Website Navigation System loaded successfully');

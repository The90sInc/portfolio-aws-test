# Personal Portfolio Website

A simple yet elegant personal portfolio website built with FastAPI and HTML, designed to showcase projects and blog posts in a professional manner.

## Features

- **Home Page**: Hero section with featured projects and recent blog posts
- **Projects Showcase**: Display all your projects with descriptions, technologies, and links
- **Blog Section**: Share your thoughts and insights through blog posts
- **About Page**: Tell your story and highlight your skills
- **Responsive Design**: Beautiful UI that works on all devices
- **REST API**: FastAPI backend with endpoints for projects and blog posts

## Project Structure

```
simple_website/
├── app/
│   └── main.py                 # FastAPI application
├── templates/
│   ├── index.html             # Home page
│   ├── projects.html          # Projects showcase
│   ├── blog.html              # Blog posts
│   └── about.html             # About page
├── static/
│   └── css/
│       └── style.css          # Global styles
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**

2. **Create a virtual environment** (optional but recommended):
```bash
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Running the Application

1. **Navigate to the app directory**:
```bash
cd app
```

2. **Start the FastAPI server**:
```bash
uvicorn main:app --reload
```

3. **Open your browser** and navigate to:
```
http://localhost:8000
```

The `--reload` flag enables auto-restart when you make changes to the code.

## API Endpoints

- `GET /` - Home page
- `GET /about` - About page
- `GET /projects` - Projects page
- `GET /blog` - Blog page
- `GET /api/projects` - Get all projects (JSON)
- `GET /api/projects/{project_id}` - Get specific project
- `GET /api/blog` - Get all blog posts (JSON)
- `GET /api/blog/{post_id}` - Get specific blog post
- `GET /api/stats` - Get portfolio statistics

## Customization

### Adding Projects

Edit the `PROJECTS` list in `app/main.py`:

```python
{
    "id": 4,
    "title": "Your Project Title",
    "description": "Project description",
    "technologies": ["Tech1", "Tech2"],
    "image_url": "/static/images/project4.jpg",
    "github_link": "https://github.com/yourusername/project",
    "demo_link": "https://project-demo.com",
    "date": "2025-12-01"
}
```

### Adding Blog Posts

Edit the `BLOG_POSTS` list in `app/main.py`:

```python
{
    "id": 4,
    "title": "Post Title",
    "excerpt": "Short excerpt",
    "content": "Full post content",
    "date": "2025-12-01",
    "tags": ["Tag1", "Tag2"]
}
```

### Customizing Styles

Modify `static/css/style.css` to change colors, fonts, and layout. Key CSS variables at the top:

```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
    --dark-color: #1f2937;
    /* ... more colors ... */
}
```

## Technologies Used

- **Backend**: Python, FastAPI, Pydantic
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Server**: Uvicorn

## Future Enhancements

- Database integration (SQLAlchemy, PostgreSQL)
- User authentication
- Contact form functionality
- Image upload capability
- Comment system for blog posts
- Search functionality
- Dark mode toggle

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, feel free to create an issue or contact the project maintainer.

---

**Enjoy showcasing your portfolio!** 🚀

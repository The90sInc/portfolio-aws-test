from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import json
import os
import uvicorn
from pathlib import Path

app = FastAPI(title="Portfolio Website")
BASE_DIR = Path(__file__).resolve().parent.parent

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Pydantic models
class Project(BaseModel):
    id: int
    title: str
    description: str
    technologies: List[str]
    image_url: Optional[str] = None
    github_link: Optional[str] = None
    demo_link: Optional[str] = None
    date: str

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    excerpt: str
    date: str
    tags: List[str]

# Sample data
PROJECTS = [
    {
        "id": 1,
        "title": "Weather App",
        "description": "A responsive weather application that fetches real-time weather data using an external API.",
        "technologies": ["React", "Python", "FastAPI"],
        "image_url": "/static/images/project1.jpg",
        "github_link": "https://github.com/yourusername/weather-app",
        "demo_link": "https://weather-app-demo.com",
        "date": "2025-12-01"
    },
    {
        "id": 2,
        "title": "Portfolio Website",
        "description": "A beautiful personal portfolio website built with FastAPI and HTML, showcasing projects and blog posts.",
        "technologies": ["FastAPI", "HTML", "CSS", "Python"],
        "image_url": "/static/images/project2.jpg",
        "github_link": "https://github.com/yourusername/portfolio",
        "date": "2025-11-15"
    },
    {
        "id": 3,
        "title": "Task Manager",
        "description": "A full-stack task management application with user authentication and real-time updates.",
        "technologies": ["FastAPI", "JavaScript", "SQLAlchemy"],
        "image_url": "/static/images/project3.jpg",
        "github_link": "https://github.com/yourusername/task-manager",
        "demo_link": "https://task-manager-demo.com",
        "date": "2025-10-20"
    }
]

BLOG_POSTS = [
    {
        "id": 1,
        "title": "Getting Started with FastAPI",
        "excerpt": "Learn how to build fast and modern APIs with FastAPI and Python.",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python 3.7+. In this post, we'll explore how to create your first API endpoint...",
        "date": "2025-12-15",
        "tags": ["FastAPI", "Python", "Backend"]
    },
    {
        "id": 2,
        "title": "Frontend Best Practices",
        "excerpt": "Essential tips for writing clean and maintainable HTML and CSS code.",
        "content": "Writing clean HTML and CSS is fundamental to web development. Here are some best practices to keep your code organized and accessible...",
        "date": "2025-12-10",
        "tags": ["Frontend", "HTML", "CSS"]
    },
    {
        "id": 3,
        "title": "Building Responsive Websites",
        "excerpt": "Master responsive design techniques for different screen sizes.",
        "content": "Responsive design is crucial in today's multi-device world. Let's explore media queries, flexible layouts, and mobile-first approaches...",
        "date": "2025-12-01",
        "tags": ["CSS", "Responsive Design", "Web Development"]
    }
]

# Routes
@app.get("/")
async def read_root():
    """Serve the home page"""
    return FileResponse(BASE_DIR / "templates" / "index.html", media_type="text/html")

@app.get("/about")
async def read_about():
    """Serve the about page"""
    return FileResponse(BASE_DIR / "templates" / "about.html", media_type="text/html")

@app.get("/blog")
async def read_blog():
    """Serve the blog page"""
    return FileResponse(BASE_DIR / "templates" / "blog.html", media_type="text/html")

@app.get("/projects")
async def read_projects():
    """Serve the projects page"""
    return FileResponse(BASE_DIR / "templates" / "projects.html", media_type="text/html")

# API endpoints
@app.get("/api/projects")
async def get_projects():
    """Get all projects"""
    return PROJECTS

@app.get("/api/projects/{project_id}")
async def get_project(project_id: int):
    """Get a specific project by ID"""
    for project in PROJECTS:
        if project["id"] == project_id:
            return project
    return {"error": "Project not found"}

@app.get("/api/blog")
async def get_blog_posts():
    """Get all blog posts"""
    return BLOG_POSTS

@app.get("/api/blog/{post_id}")
async def get_blog_post(post_id: int):
    """Get a specific blog post by ID"""
    for post in BLOG_POSTS:
        if post["id"] == post_id:
            return post
    return {"error": "Blog post not found"}

@app.get("/api/stats")
async def get_stats():
    """Get portfolio statistics"""
    return {
        "total_projects": len(PROJECTS),
        "total_blog_posts": len(BLOG_POSTS),
        "technologies": list(set([tech for project in PROJECTS for tech in project["technologies"]]))
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

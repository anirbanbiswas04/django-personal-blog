# Code and Explore
A Django personal blog web app. The blog lets to post, edit, and delete articles, with images and markdown. The blog also has comments, search, pagination, sitemap, RSS feed. 
A possible README.md file for a Django personal blog site uploaded to GitHub is:

## Features

The site has the following features:

- A clean and modern user interface, with a responsive design.
- Creating and editing blog posts, with support for Markdown syntax, code highlighting, images.
- A comment system.
- A search system for finding blog posts by titles, body, or category, with a search bar on the header.
- A pagination system for displaying blog posts in multiple pages.
- A sitemap system for generating a sitemap.xml file for SEO purposes, with a sitemap link on the footer.
- A RSS feed system for providing a RSS feed of my latest blog posts.
- A custom admin panel for managing my blog content.

## Technologies

The site is powered by Django, which is a high-level Python web framework that encourages rapid development and clean design. The site uses SQLite as the database engine, which is a self-contained, serverless, zero-configuration, transactional SQL database engine. The site uses Bulma CSS as the front-end framework, which is a free and open-source CSS framework for creating responsive, mobile-first websites.

## Installation

To run the site locally, you need to have Python 3.6 or higher installed on your machine. You also need to install the required packages using pip:

```bash
pip install -r requirements.txt
```

You can migrate the database and create a superuser account:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Finally, you can run the development server:

```bash
python manage.py runserver
```

The site will be available at http://127.0.0.1:8000/.

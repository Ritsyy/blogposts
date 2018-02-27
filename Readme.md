# Blogs

Blogs is the application to comment on each paragraph of a blog.

  - You will be able to add blog posts. Blog posts have a unique random identifier, a title     and plain text where paragraphs are separated by two new-line characters.
  - You will be able to view all blog posts (list-mode) starting with first 5 and then the next 5 and so on. This view will not have any comments.
  - You will be able to see comments on each paragraph of a blog in detail view in the API.

# Project Setup
```

   virtualenv env_blogposts
   source env_blogposts/bin/activate
   pip install -r requirements.txt
   ./manage.py makemigrations
   ./manage.py migrate
   ./manage.py createsuperuser
```

  - After making superuser runserver with ` ./manage.py runserver`
  - on localhost:8000/admin create sample blogposts, it will automatically generate paragraphs for every two line enters
  - in the comments section you can enter comment on each paragraph
  - Now for the API view to get all the blogs in List view
  - hit ` localhost:8000/apiv1/blogs` it will give the first 5 blogs
  - for the next page hit ` localhost:8000/apiv1/blogs?page=2`
  - For detail view of a blog with comments in each paragarph, hit ` localhost:8000/apiv1/blog/1`
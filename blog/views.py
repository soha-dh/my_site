from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "sohastar",
        "date": date(2021, 7, 21),
        "title": "Mounting Hiking",
        "excerpt": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio sequi quasi nisi rerum nemo perspiciatis nihil tenetur doloremque dolorum amet!",
        "content": """ 
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut corporis nostrum sequi 
            accusantium facere reiciendis dignissimos temporibus, in architecto fugit eaque, 
            molestias quisquam nisi consectetur deserunt ut ipsum perspiciatis hic.
            """

    },  {
        "slug": "swiming-in-the-sea",
        "image": "mountains.jpg",
        "author": "elham",
        "date": date(2021, 8, 22),
        "title": "swiming in the sea",
        "excerpt": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio sequi quasi nisi rerum nemo perspiciatis nihil tenetur doloremque dolorum amet!",
        "content": """ 
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut corporis nostrum sequi 
            accusantium facere reiciendis dignissimos temporibus, in architecto fugit eaque, 
            molestias quisquam nisi consectetur deserunt ut ipsum perspiciatis hic.
            """

    }, {
        "slug": "Dansing-in-the-club",
        "image": "mountains.jpg",
        "author": "mahsa",
        "date": date(2021, 9, 23),
        "title": "Dansing in the club",
        "excerpt": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio sequi quasi nisi rerum nemo perspiciatis nihil tenetur doloremque dolorum amet!",
        "content": """ 
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut corporis nostrum sequi 
            accusantium facere reiciendis dignissimos temporibus, in architecto fugit eaque, 
            molestias quisquam nisi consectetur deserunt ut ipsum perspiciatis hic.
            """

    }
]

# Helper function to Get date for sorting


def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]   # two last items in the list
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")

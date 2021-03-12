from django.shortcuts import render, redirect
from django.views import generic
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from .forms import UploadImageForm, RegistrationForm
from .models import Image
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import os
import datetime

# defines the file extensions that can be inserted into the database. Must be
# image files in order for the rest of the code to work properly.
VALID_EXTENSIONS = ['jpg', 'gif', 'png']


class ImageListView(generic.ListView):
    """the main page view. Orders returned images by the date they were
    created."""
    model = Image
    queryset = Image.objects.order_by('date_created')


def search(request, search: str):
    """returns all image entries which contain <search> in their name or
    description, formatted the same as the main page."""
    image_list = Image.objects.filter(
        Q(name__icontains=search) | Q(description__icontains=search))
    context = {'image_list': image_list}
    return render(request, 'image_list.html', context=context)


def user(request, username: str):
    """returns all image entries uploaded by user <username>, formatted
    the same as the main page."""
    image_list = Image.objects.filter(username=username)
    context = {'image_list': image_list}
    return render(request, 'image_list.html', context=context)


def image_request(request, pk: int):
    """defines how to read image files from the database in order to view them
    on the site."""
    x = Image.objects.get(pk=pk)
    response = HttpResponse(x.image_file)
    return response


@login_required
def upload_file(request):
    """allows the user to upload an image file. requires the user to be logged
    in."""
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            if str(uploaded_img.image_file)[-3:] not in VALID_EXTENSIONS:
                return HttpResponseNotFound(f'<h1>Error! File must be of type '
                                            f'gif, png, or jpg.</h1>')
            uploaded_img.username = request.user
            uploaded_img.save()
            return redirect('/')
    else:
        form = UploadImageForm()
    return render(request, 'main_app/upload.html', {'form': form})


def register(request):
    """allows the user to be registered in the user database. It is important
    to note that there is currently no restrictions on password length or
    security, and the email address is not confirmed."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = make_password(request.POST['password'])
            new_user.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'main_app/register.html', {'form': form})


@login_required
def edit_file(request, pk: int):
    """allows a user to edit the image with id <pk>, providing they were
    the user that uploaded it. If image file is changed, the local copy that
    was stored of the previous image file is deleted. If the image file does
    not exist, then it fails silently."""
    x = Image.objects.get(pk=pk)
    if str(request.user) != str(x.username):
        return HttpResponseNotFound(f'<h1>Page not Found</h1>')
    if request.method == 'POST':
        if request.POST['name'] != '':
            x.name = request.POST['name']
        if request.POST['description'] != '':
            x.description = request.POST['description']
        if 'image_file' not in request.POST:
            try:
                os.remove(str(x.image_file))
            except FileNotFoundError:
                pass
            if str(request.FILES['image_file'])[-3:] not in VALID_EXTENSIONS:
                return HttpResponseNotFound(f'<h1>Error! File must be of type '
                                            f'gif, png, or jpg.</h1>')
            x.image_file = request.FILES['image_file']
        x.date_modified = datetime.datetime.now()
        x.save()
        return redirect('/')
    else:
        form = UploadImageForm(initial={'name': x.name,
                                        'description': x.description,
                                        'image_file': x.image_file})
    return render(request, 'main_app/upload.html', {'form': form})

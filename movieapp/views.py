from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Movie

# LIST all movies

def splash(request):
    return render(request, 'movieapp/splash.html')

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movieapp/index.html', {'movies': movies})

# ADD movie via form
def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        status = request.POST.get('status')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')

        # Basic validation
        if not title or not genre or not status or not release_year or not rating:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        movie = Movie.objects.create(
            title=title,
            genre=genre,
            status=status,
            release_year=int(release_year),
            rating=float(rating)
        )
        return JsonResponse({'success': 'Movie added successfully!'})

    return render(request, 'movieapp/add.html')

# EDIT movie
def edit_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        status = request.POST.get('status')
        release_year = request.POST.get('release_year')
        rating = request.POST.get('rating')

        if not title or not genre or not status or not release_year or not rating:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        movie.title = title
        movie.genre = genre
        movie.status = status
        movie.release_year = int(release_year)
        movie.rating = float(rating)
        movie.save()

        return JsonResponse({'success': 'Movie updated successfully!'})

    return render(request, 'movieapp/edit.html', {'movie': movie})

# DELETE movie
def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return JsonResponse({'success': 'Movie deleted successfully!'})
    return render(request, 'movieapp/delete.html', {'movie': movie})


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Movie

# # READ (Display all movies)
# def index(request):
#     movies = Movie.objects.all()
#     return render(request, 'movieapp/index.html', {'movies': movies})

# # CREATE (Add a new movie)
# def add_movie(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         genre = request.POST['genre']
#         status = request.POST['status']
#         release_year = request.POST['release_year']
#         rating = request.POST['rating']

#         if not title or not genre or not status or not release_year or not rating:
#             messages.error(request, "⚠️ All fields are required!")
#             return render(request, 'movieapp/add.html')

#         Movie.objects.create(
#             title=title,
#             genre=genre,
#             status=status,
#             release_year=release_year,
#             rating=rating
#         )
#         messages.success(request, "✅ Movie added successfully!")
#         return redirect('movieapp/index.html')

#     return render(request, 'movieapp/add.html')

# # UPDATE (Edit movie)
# def edit_movie(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     if request.method == 'POST':
#         movie.title = request.POST['title']
#         movie.genre = request.POST['genre']
#         movie.status = request.POST['status']
#         movie.release_year = request.POST['release_year']
#         movie.rating = request.POST['rating']
#         movie.save()
#         messages.success(request, "✏️ Movie updated successfully!")
#         return redirect('movieapp/index.html')
#     return render(request, 'movieapp/edit.html', {'movie': movie})

# # DELETE
# # def delete_movie(request, id):
# #     movie = get_object_or_404(Movie, id=id)
# #     movie.delete()
# #     messages.success(request, "🗑️ Movie deleted successfully!")
# #     return redirect('index')
# def delete_movie(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     if request.method == 'POST':
#         movie.delete()
#         messages.success(request, "🗑️ Movie deleted successfully!")
#         return redirect('movieapp/index.html')
        
#     return render(request, 'movieapp/delete.html', {'movie': movie})

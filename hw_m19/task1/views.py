from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator

# Create your views here.
info = {}

users = Buyer.objects.all()


def platform(request):
    title = 'Мой сайт'
    header = 'Главная страница'
    context = {"title": title,
               "header": header
               }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Магазин'
    header = 'Игры'
    games_all = Game.objects.all()
    context = {"title": title,
               "header": header,
               "games_all": games_all
               }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    header = 'Корзина'
    message = 'Извините, Ваша корзина пуста'
    context = {"title": title,
               "header": header,
               "message": message
               }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    usernames = [user.username for user in users]
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and username not in usernames:
                new_user = Buyer.objects.create(username=f'{username}', password=f'{password}', age=f'{age}')
                new_user.save()
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context=info)
                # return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context=info)
            elif username in usernames:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context=info)
        else:
            info['error'] = 'Некорректный ввод данных'
            return render(request, 'registration_page.html', context=info)
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    usernames = [user.username for user in users]
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password == repeat_password and username not in usernames:
            new_user = Buyer.objects.create(username=f'{username}', password=f'{password}', age=f'{age}')
            new_user.save()
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', context=info)
        # elif age < 18:
        #     info['error'] = 'Вы должны быть старше 18'
        #     return render(request, 'registration_page.html', context=info)
        elif username in usernames:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', context=info)
    return render(request, 'registration_page.html')


def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})


def faq(request):
    faq = FAQ.objects.all().order_by('-date')
    paginator = Paginator(faq, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'faq.html', {'page_obj': page_obj})


def review(request):
    review = Review.objects.all().order_by('-date')
    paginator = Paginator(review, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'review.html', {'page_obj': page_obj})

from django.shortcuts import render, redirect
from .models import userModel, pushNotifications
from django.contrib.auth.decorators import login_required
from allauth.account import signals
from .forms import UserForm, PushForm
from django.contrib.auth.models import User, auth


# Create your views here.
@login_required
def profile_view(request):
    user_all = userModel.objects.all()
    flag = 0
    for obj in user_all:
        print(obj.User)
        if request.user == obj.User:
            flag = 1
    if flag == 0:
        print(request.user)
        u = userModel.objects.create(User=request.user)
        u.save()
    user = userModel.objects.get(User=request.user)
    form = UserForm(instance=user)
    push = pushNotifications.objects.all()
    context = {
        'form': form,
        'details': user,
        'push': push,
    }
    if request.user.is_superuser:
        pushform = PushForm()
        context = {
            'form': form,
            'details': user,
            'pushform': pushform,
            'push': push,
        }

    if not request.user.is_authenticated:
        return render(request, '/login.html')
    if request.method == 'POST':
        if 'profile' in request.POST:
            inst = UserForm(
                request.POST,
                request.FILES or None,
                instance=user,
            )
            print(inst)
            inst.save()
            return redirect('/accounts/profile')
        else:
            form = PushForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()

    return render(request, "profiles/profile.html", context)


def push_detail(request):
    push_list = pushNotifications.objects.all()
    print(push_list)
    context = {
        'list': push_list,
    }
    return render(request, 'profiles/detail.html', context)


def push_update(request, pk):
    push_list = pushNotifications.objects.get(id=pk)
    print(push_list)
    pushform = PushForm(instance=push_list)
    context = {
        'form': pushform,
    }
    if request.method == 'POST':
        inst = PushForm(
            request.POST,
            request.FILES or None,
            instance=push_list,
        )
        inst.save()
        return redirect('/accounts/detail')
    return render(request, 'profiles/update.html', context)


def push_delete(request, pk):
    push_list = pushNotifications.objects.get(id=pk)
    push_list.delete()

    return redirect('/accounts/detail')


def logout(request):
    auth.logout(request)
    return redirect('/login/')

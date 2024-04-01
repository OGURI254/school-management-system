from django.shortcuts import redirect, render
from instructor.forms import SocialMediaForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def profile(request):
    context = {
        'title':"My Profile",
    }
    return render(request, 'users/profile.html', context)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and pform.is_valid():
            form.save()
            pform.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('users:profile')
    else:
        form = UserForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)
    
    context = {
        'title': "Edit Profile",
        'form': form,
        'pform': pform
    }
    return render(request, 'users/edit-profile.html', context)

@login_required
def social_profile(request):
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, instance=request.user.social)
        if form.is_valid():
            form.save()
            messages.success(request, "Social Link Updated Successfully")
            return redirect('users:social_profile')
    else:
        form = SocialMediaForm(instance=request.user.social)
    context = {
        'title':"Social Link",
        'form': form
    }

    return render(request, 'users/social-profiles.html', context)

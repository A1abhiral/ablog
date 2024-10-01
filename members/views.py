from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm,Edit_Profile_Form,Update_Password_Form,ProfilePageForm,EditProfilePageForm
from theblog.models import Profile,Category
from django.views.generic import DetailView,CreateView
import cloudinary.uploader

    


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "registration/create_profile_page.html"
    form_class = ProfilePageForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        # Upload profile picture to Cloudinary
        profile_pic = form.cleaned_data.get('profile_pic')  # Ensure 'profile_pic' is the correct field name
        if profile_pic:
            response = cloudinary.uploader.upload(profile_pic)
            form.instance.profile_pic = response['secure_url']  # Store the Cloudinary URL
            
        return super().form_valid(form)



class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_view.html'
    form_class = EditProfilePageForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Get the current profile picture URL before trying to upload a new one
        current_profile_pic = self.object.profile_pic

        # Check if a new profile picture has been uploaded
        profile_pic = form.cleaned_data.get('profile_pic')

        if profile_pic:  # Only upload if a new image is provided
            try:
                # Upload the new profile picture to Cloudinary
                response = cloudinary.uploader.upload(profile_pic)
                # Update the form instance with the new Cloudinary URL
                form.instance.profile_pic = response['secure_url']
            except cloudinary.exceptions.Error as e:
                form.add_error('profile_pic', f'Upload failed: {str(e)}')
                return self.form_invalid(form)
            except Exception as e:
                form.add_error('profile_pic', 'You must re-upload previous image or upload a new image to update.')
                return self.form_invalid(form)
        else:
            # If no new profile picture was uploaded, retain the current image
            form.instance.profile_pic = current_profile_pic

        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args,**kwargs) :
        context = super().get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


def Password_changed_successfully(request):
    return render(request,'registration/Password_changed_successfully.html',{})

class PasswordChange(PasswordChangeView):
    form_class = Update_Password_Form
    success_url = reverse_lazy('Password_changed_successfully')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args,**kwargs) :
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class UserEditView(generic.UpdateView):
    form_class = Edit_Profile_Form
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
      # Ensure that the current user is the one being edited
      return self.request.user
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm,Edit_Profile_Form,Update_Password_Form,ProfilePageForm,EditProfilePageForm
from theblog.models import Profile,Category
from django.views.generic import DetailView,CreateView
    


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "registration/create_profile_page.html"
    #fields = '__all__'
    form_class = ProfilePageForm
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_view.html'
    form_class = EditProfilePageForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.user = self.request.user
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
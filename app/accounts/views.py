from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm, CustomAuthForm, UserUpdateForm, ChangePasswordForm
from app.order.models import Order

# Create your views here.
class RegisterView(View):
    form_class = UserCreateForm
    def get(self, request):
        create_form = self.form_class
        context = {
            "form": create_form
        }
        return render(request, "accounts/register.html", context)

    def post(self, request):
        create_form = self.form_class(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('accounts:login')
        else:
            messages.error(request, f"{create_form.errors}")
            context = {
                "form": create_form
            }
            return render(request, "accounts/register.html", context)


class LoginView(View):
    form_class = CustomAuthForm
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('products:home')
        else:
            login_form = self.form_class

            return render(request, "accounts/login.html", {"login_form": login_form})

    def post(self, request):
        url = request.META.get('HTTP_REFERER')
        
        login_form = self.form_class(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, "You have successfully logged in.")

            return redirect('products:home')
        else:
            return render(request, "accounts/login.html", {"login_form": login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("products:home")

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        my_order = Order.objects.filter(user = request.user)
        context = {
            "user": request.user,
            'my_order' : my_order
            }
        return render(request, "accounts/profile.html", context)

class ProfileUpdateView(LoginRequiredMixin, View):
    form_class = UserUpdateForm
    def post(self, request):
        user_update_form = self.form_class(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have successfully updated your profile.")

            return redirect("accounts:profile")
        else:
            messages.success(request, f"{user_update_form.errors}")
            return redirect("accounts:profile")

        


class PasswordChangeView(LoginRequiredMixin,View):
    from_class = ChangePasswordForm
    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Password changed successfully")
            return redirect('accounts:login')
        else:
            messages.error(request, f"{form.errors}")
            return redirect('accounts:profile')   
        

   
class OrderDetailView(View):
    def get(self, request, uuid):
        my_order = Order.objects.get(user = request.user, uuid=uuid)
        context = {
            'order' : my_order
            }
        return render(request, "order-confirmed-shop.html", context)
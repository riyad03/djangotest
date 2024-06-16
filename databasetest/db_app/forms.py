from django import forms
from .models import MyUser,Book

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = MyUser
        fields = [ 'email', 'first_name', 'last_name','password1','password2','date_of_birth']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password=self.cleaned_data["password1"]
        if commit:
            user.save()
        return user
    
class BookForm(forms.ModelForm):
    published_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

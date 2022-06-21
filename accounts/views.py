from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST': # 회원가입 데이터 입력 완료 상황
        user_form = RegisterForm(request.POST) #request.POST-사용자가입력한 값
        if user_form.is_valid(): #데이터형식이맞는지 확인, validation 호출
            new_user = user_form.save(commit=False) #해당 form 모델의 인스턴스를 얻어옴
            new_user.set_password(user_form.cleaned_data['password']) #password할당
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:#회원가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})
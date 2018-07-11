from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



from Authentication.forms import LoginForm



# Create your views here


class LoginView(FormView):
	template_name = 'login.html'
	from_class = LoginForm

	def get(self, request):
		form = self.from_class()
		context = {}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.from_class(request.POST)
		context = {'form': form}
		if form.is_valid():
			username = form.cleaned_data['login']
			password = form.cleaned_data['password']
			user = authenticate(request, username = username, password = password)
			if user is not None:
				login(request, user)
				return redirect('/tickets/index/')

		return render(request, self.template_name, context)



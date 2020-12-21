from .forms import AppointmentForm

# def settings(request):
# 	return{'settings': SiteSettings.load()}

def appointment_form(request):
	return{'appointment_form': AppointmentForm}
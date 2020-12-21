from django import forms

class AppointmentForm(forms.Form):
	name = forms.CharField(max_length=100, min_length=2)
	phone = forms.CharField(max_length=70, min_length=11, help_text='Укажите в формате: +7 000 000-00-00')
	email = forms.EmailField(max_length=150, min_length=4, help_text='Укажите Ваш действующий email')

	def clean(self):
		cleaned_data = super().clean()

		if cleaned_data.get('email'):
			self.add_error('email', 'Some custome message about email')

		email = cleaned_data.get('email')
		email_confirm = cleaned_data.get('email_confirm')

		if email and email_confirm and email != email_confirm:
			self.add_error('email', 'Оба почтовых ящиков должны совпадать')
			self.add_error('email_confirm', 'Оба почтовых ящиков должны совпадать')

		return cleaned_data

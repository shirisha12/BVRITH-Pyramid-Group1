from django.forms import ModelForm
from app.models import PersonInfo

class PersonInfoForm(ModelForm):
	class Meta:
		model = PersonInfo
		fields = '__all__'

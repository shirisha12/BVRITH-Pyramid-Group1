from django.forms import ModelForm
from faculty.models import Details

class DetailsForm(ModelForm):
	class Meta:
		model = Details
		fields = '__all__'


from django import forms
from django.forms import ModelForm

from .models import Student, Branch

class StudentForm(ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    MATERIALS_CHOICES = (
        ('notebook', ' Note Book'),
        ('pen', 'Pen'),
        ('exam_papers', 'Exam Papers'),
        # Add more materials as needed
    )

    gender = forms.ChoiceField(
        label='Gender',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )

    materials = forms.MultipleChoiceField(
        label='Materials Provided',
        choices=MATERIALS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Set this to True if selecting materials is mandatory
    )

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['branch'].queryset = Branch.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to an empty Branch queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.department.branch_set.order_by('name')

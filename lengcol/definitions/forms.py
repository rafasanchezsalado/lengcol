from django import forms
from extra_views import InlineFormSetFactory
from snowpenguin.django.recaptcha3 import fields

from definitions import models


class ModelChoiceFieldAsText(forms.ModelChoiceField):
    def __init__(self, queryset, field, *args, **kwargs):
        super().__init__(queryset, *args, **kwargs)
        self.widget = forms.TextInput()
        self.field = field

    def to_python(self, value):
        if value in self.empty_values:
            return None

        obj, created = self.queryset.get_or_create(**{self.field: value})

        return obj


class DefinitionForm(forms.ModelForm):
    value = forms.CharField(label='Definición', widget=forms.Textarea())

    captcha = fields.ReCaptchaField()

    class Meta:
        model = models.Definition
        exclude = ('user', 'term', 'active')


class NewDefinitionForm(DefinitionForm):
    term = ModelChoiceFieldAsText(
        queryset=models.Term.objects.all(),
        field='value',
        label='Término',
    )

    class Meta:
        model = models.Definition
        exclude = ('user', 'active')


class ExampleForm(forms.ModelForm):
    value = forms.CharField(label='')

    class Meta:
        model = models.Example
        fields = ('value',)


class ExampleInline(InlineFormSetFactory):
    model = models.Example
    form_class = ExampleForm
    factory_kwargs = {'extra': 2, 'max_num': 5}

from django import forms
from .models import food_table
class UserForm(forms.ModelForm):
    # title = forms.CharField(label='',
    #                         widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    # description = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             "placeholder": "Your description",
    #             "class": "new-class-name two",
    #             "id": "my-id-for-textarea",
    #             "rows": 20,
    #             'cols': 120
    #         }
    #    )
    # )
    class Meta:
        model = food_table
        fields = [
            'Name',
            'Carbonhydrates',
            'Fiber',
            'Protein',
            'Fat',
        ]

# class RawProductForm(forms.Form)
#     title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
#     description = forms.CharField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder": "Your description",
#                 "class": "new-class-name two",
#                 "id": "my-id-for-textarea",
#                 "rows": 20,
#                 'cols': 120
#             }
#         )
#     )
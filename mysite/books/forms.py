from django import forms

topic_choices = (
    ('general', 'General enquiry'),
    ('bug' 'Report a bug'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=topic_choices)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)



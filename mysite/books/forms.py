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

    # def clean_message(self):
    #     message = self.clean_data.get('message', '')
    #     num_words = len(message.spit())
    #     if num_words < 4:
    #         raise forms.ValidationError('Max. 4 chars!')
    #     return message


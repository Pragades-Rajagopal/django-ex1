from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from books.models import Book
from books.forms import ContactForm

def search (request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__contains=query) |
            Q(authors__first_name__contains=query) |
            Q(authors__last_name__contains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []

    return render(request, 'books/search.html', {
        'results': results,
        'query': query
    })


def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            send_mail(
                'Feedback from your site Mysite, topic: ' + topic,
                message, sender,
                ['admin@example.com']
            )
            return HttpResponseRedirect('<html><body>Thanks</body><html>')
    else:
        form = ContactForm()
    return render(request, 'books/contact.html', { 'form': form })


from django.shortcuts import render
from subjects.models import Subject, Topic, Book, Chapter, Note

# Create your views here.

# View to list all subjects
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})

# View to display topics for a specific subject
def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    topics = Topic.objects.filter(subject=subject).order_by('order')
    return render(request, 'subjects/topic_list.html', {'subject': subject, 'topics': topics})

# View to display books for a specific topic
def book_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    books = Book.objects.filter(topic=topic)
    return render(request, 'subjects/book_list.html', {'topic': topic, 'books': books})

# View to display details of a specific book and its chapters
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    chapters = Chapter.objects.filter(book=book).order_by('number')
    return render(request, 'subjects/book_detail.html', {'book': book, 'chapters': chapters})

# View to display notes for a specific chapter
def chapter_notes(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    notes = Note.objects.filter(chapter=chapter)
    return render(request, 'subjects/chapter_notes.html', {'chapter': chapter, 'notes': notes})

# View to display detail about specific Subject 
def subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)
    context = {
        "subject": subject
    }
    return render(request, "subjects/subject_detail.html", context)
# Create a Subject
subject = Subject(name="Physics", description="")
subject.save()

# Create a Topic linked to the Subject
topic = Topic(name="Introduction to Mechanics", description="Bbasics of motion in a straight line, motion in two dimensions, motion in three dimensions, Newton's Laws, work, kinetic energy, potential energy, the conservation of energy, momentum, collisions, rotation and rotational motion, gravitation, and periodic motion.", subject=subject, order=1)
topic.save()

# Create a Book linked to the Topic
book = Book(title="University Physics with Modern Physics", author="Young and Freedman", isbn="978-0135159552", topic=topic)
book.save()

# Create a Chapter linked to the Book
chapter = Chapter(title="Units, Physical Quantities, and Vectors", number=1, book=book)
chapter.save()

# Create a Note linked to the Chapter
note = Note(content="A unit vector has magnitude of 1, unitless", chapter=chapter)
note.save()
from datetime import datetime
from django.test import TestCase
from prototype.models import Event, Note, User


# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        u1 = User.objects.create(username='testUser')
        date1 = datetime(2021, 3, 17)
        date2 = datetime(2021, 3, 18)
        date3 = datetime(2021, 3, 16)
        Event.objects.create(event_title="St Patrick's day", event_description="Parade is on", location="Main street",
                             start_date=date1, end_date=date2, colour="Green", user=u1)
        Event.objects.create(event_title="Wrong", event_description="This should not work", location="MehMeh",
                             start_date=date1, end_date=date3, colour="Red", user=u1)

    def test_event_date(self):
        patrick = Event.objects.get(event_title="St Patrick's day")
        wrong = Event.objects.get(event_title="Wrong")
        assert patrick.start_date < patrick.end_date, "This is ok"
        assert wrong.start_date < wrong.end_date, "Oi the end date is before the start date"


# Note
class NoteTestCase(TestCase):
    def setUp(self):
        u2 = User.objects.create(username='SecondUser')
        Note.objects.create(note_title="Test Note so basically i am going to check that this part is "
                                       "less than 50 characters but we shall see"
                            , note_content="Make sure these tests work", user=u2)

    def test_note(self):
        fifty = Note.objects.get(note_title="Test Note")
        assert len(fifty.note_title) < 50, \
            "Oi the title for the note is longer than 50 characters"

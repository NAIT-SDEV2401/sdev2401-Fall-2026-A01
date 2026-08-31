from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from events.models import Event

User = get_user_model()


class EventAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.organizer = User.objects.create_user(
            username="organizer1",
            password="testpass123",
            role="organizer",
            full_name="Test Organizer",
            status="active",
        )
        self.presenter = User.objects.create_user(
            username="presenter1",
            password="testpass123",
            role="presenter",
            full_name="Test Presenter",
            status="active",
        )
        self.org_token = Token.objects.create(user=self.organizer)
        self.pre_token = Token.objects.create(user=self.presenter)
        self.event = Event.objects.create(
            name="Test Event",
            description="A test event.",
            location="Test City",
            start_date="2025-01-01",
            end_date="2025-01-02",
        )

    def test_get_events_requires_auth(self):
        response = self.client.get("/v1/api/events/")
        self.assertEqual(response.status_code, 401)

    def test_get_events_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.pre_token.key}")
        response = self.client.get("/v1/api/events/")
        self.assertEqual(response.status_code, 200)

    def test_get_single_event(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.pre_token.key}")
        response = self.client.get(f"/v1/api/events/{self.event.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Test Event")

    def test_get_missing_event_returns_404(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.pre_token.key}")
        response = self.client.get("/v1/api/events/9999/")
        self.assertEqual(response.status_code, 404)

    def test_presenter_cannot_create_event(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.pre_token.key}")
        response = self.client.post("/v1/api/events/", {
            "name": "New Event",
            "description": "Desc",
            "location": "City",
            "start_date": "2025-06-01",
            "end_date": "2025-06-02",
        })
        self.assertEqual(response.status_code, 403)

    def test_organizer_can_create_event(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.org_token.key}")
        response = self.client.post("/v1/api/events/", {
            "name": "New Event",
            "description": "Desc",
            "location": "City",
            "start_date": "2025-06-01",
            "end_date": "2025-06-02",
        })
        self.assertEqual(response.status_code, 201)

    def test_get_talks_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.pre_token.key}")
        response = self.client.get("/v1/api/talks/")
        self.assertEqual(response.status_code, 200)

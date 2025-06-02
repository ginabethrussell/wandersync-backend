# 🌍 WanderSync

**WanderSync** is a collaborative travel itinerary sharing app that lets users upload detailed trip plans via CSV, explore others' journeys, and get inspired to travel more. Built with a modern full-stack setup using **Next.js (frontend)** and **Django + Django REST Framework (backend)**.

## 🖼️ Frontend Repository

The frontend for this project is available at:

👉 [github.com/ginabethrussell/wandersync](https://github.com/ginabethrussell/wandersync)

It’s built with **Next.js + Tailwind CSS** and deployed with vercel at [https://wandersync.vercel.app/](https://wandersync.vercel.app/)

## ✨ Features

### ✅ Backend (Django + DRF)
- Django 5.2.1 + Django REST Framework
- REST API to support travel itinerary creation, retrieval, deletion
- Supports nested itinerary items (e.g., daily plans per trip)
- In-memory SQLite database (no external DB needed for development)
- Admin panel to manage itineraries
- Deployed locally (production deployment coming soon)

---

## 📁 Project Structure

```txt
wandersync-backend/
├── config/                 # Project settings
│   └── urls.py             # Root URLs
├── itineraries/            # App for itineraries
│   ├── migrations/
│   ├── models.py           # Itinerary and ItineraryItem models
│   ├── serializers.py      # DRF serializers for nested create
│   ├── urls.py             # App-level routes
│   └── views.py            # Viewsets for CRUD API
├── db.sqlite3              # SQLite DB (created on migrate)
├── manage.py               # Django management
└── README.md
```

## 🔧 Local Development Setup

1. Clone the Repository
```bash
git clone https://github.com/ginabethrussell/wandersync-backend.git
cd wandersync-backend
```
2. Create a Virtual Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install django djangorestframework
```
4. Run Migrations
```bash
python manage.py migrate
```
5. Run the Development Server
```bash
python manage.py runserver
```

View the server in your browser at Open http://localhost:8000 in your browser.

## 🔗 API Endpoints

Base URL: http://localhost:8000/api/

| Method | Endpoint             | Description                    |
| ------ | -------------------- | ------------------------------ |
| GET    | `/itineraries/`      | Get all itineraries            |
| POST   | `/itineraries/`      | Create a new itinerary + items |
| GET    | `/itineraries/{id}/` | Get single itinerary by ID     |
| DELETE | `/itineraries/{id}/` | Delete itinerary by ID         |
| PUT    | `/itineraries/{id}/` | Update full itinerary          |
| PATCH  | `/itineraries/{id}/` | Partial update                 |

## 🧪 Example JSON Payload (POST)
```JSON
{
  "title": "Paris Adventure",
  "destination": "Paris, France",
  "days": 5,
  "summary": "A romantic getaway in Paris",
  "recommended_time": "Spring (Mar–May)",
  "tags": ["couple", "luxury"],
  "items": [
    {
      "day": 1,
      "location": "Eiffel Tower",
      "activity": "Sightseeing",
      "lodging": "Hotel Lumière",
      "dining": "Le Jules Verne",
      "notes": "Start the trip with a bang"
    },
    {
      "day": 2,
      "location": "Louvre",
      "activity": "Museum visit",
      "lodging": "Hotel Lumière",
      "dining": "Cafe Marly",
      "notes": "Book tickets ahead"
    }
  ]
}
```
## 🧼 To Reset Your Local DB
```bash
rm db.sqlite3
python manage.py migrate
```

## 📄 License

MIT — free to use, modify, and deploy.

Built with ❤️ by travel lovers.
© 2025 Ginabeth Russell | WanderSync

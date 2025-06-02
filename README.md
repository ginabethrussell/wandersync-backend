# 🌍 WanderSync

**WanderSync** is a collaborative travel itinerary sharing app that lets users upload detailed trip plans via CSV, explore others' journeys, and get inspired to travel more. Built with a modern full-stack setup using **Next.js (frontend)** and **Django + Django REST Framework (backend)**.

## ✨ Features

### ✅ Frontend (Next.js + Tailwind CSS)
- Responsive homepage and upload interface
- Upload form with:
  - Trip metadata (title, destination, summary, tags, time to go)
  - CSV upload and preview of itinerary items
- View uploaded itineraries as a list
- View itinerary detail pages with day-by-day breakdown
- Uses Montserrat font and custom WanderSync logo
- Styled with Tailwind CSS (custom color + hover states)
- Deployed via **Vercel**

### ✅ Backend (Django + DRF)
- REST API with:
  - `GET /api/itineraries/` - Get all itineraries
  - `GET /api/itineraries/:id/` - Get a single itinerary by ID
  - `POST /api/itineraries/` - Upload a new itinerary with day-by-day items
  - `DELETE /api/itineraries/:id/` - Delete a single itinerary
- SQLite used as local development database
- Admin panel to manage itineraries
- Deployed locally (production deployment coming soon)

---


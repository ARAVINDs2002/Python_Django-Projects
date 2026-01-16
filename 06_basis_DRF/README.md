# Basic DRF Demo (06_basis_DRF)

![Project Preview](screenshots/preview.png)

A minimal project demonstrating the core concepts of **Django Rest Framework (DRF)** and its ability to serve both JSON data and rendered HTML templates.

## 🚀 Key Features
- **Serializers**: Uses `ModelSerializer` to convert database objects into JSON format.
- **APIViews**: 
    - `ItemListAPIView`: Returns pure JSON data (Standard REST API).
    - `ItemListWebView`: Uses DRF's `TemplateHTMLRenderer` to render the same data into an HTML template.
- **Browsable API**: Built-in DRF interface for testing the API directly in the browser.

## 📂 Components Used
- `djangorestframework`: The core library for building the API.
- `ItemSerializer`: Definition of how the `Item` model is represented in JSON.
- `TemplateHTMLRenderer`: A powerful DRF feature that allows API logic to stay the same while serving HTML to web browsers.

---

## 🔄 Application Flow

1. **Database to Serializer**:
   - The `Item` model stores product data.
   - The `ItemSerializer` picks up this data and prepares it for transmission.

2. **JSON Endpoint (`/api/items/`)**:
   - The user/client requests the URL.
   - DRF logic fetches the items, runs them through the serializer, and returns a clean JSON array.

3. **HTML Endpoint (`/items/`)**:
   - The user visits the URL in a browser.
   - DRF logic fetches the items, but instead of returning JSON, it passes the data to `item_list.html`.
   - The template renders the data into a clean product catalog table.

---

## 🚀 How to Run
1. Run migrations: `python manage.py migrate`
2. Start server: `python manage.py runserver 8002`
3. View the Catalog: `http://127.0.0.1:8002/items/`
4. View the Raw API: `http://127.0.0.1:8002/api/items/` (Includes the DRF Browsable UI)
5. Admin Access: `admin` / `admin123`

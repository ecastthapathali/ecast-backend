## API Guide

### Base URL

The base URL for all API endpoints is `/api/contact/`.

### Endpoints

#### ContactForm

- **Endpoint:** `/api/contact/form/`
- **Description:** This endpoint is used to interact with the contact form data.

##### CRUD Operations

1. **Create (POST):** `/api/contact/form/`
   - **Required Parameters:**
     - `name`
     - `email`
     - `message`
   - **Optional Parameters:** None

2. **Read (GET):** `/api/contact/form/` and `/api/contact/form/{id}/`
   - **Required Parameters:**
     - None for `/api/contact/form/`
     - `id` is required for `/api/contact/form/{id}/`

3. **Update (PUT/PATCH):** `/api/contact/form/{id}/`
   - **Required Parameters:**
     - `id`
   - **Optional Parameters:**
     - `name`
     - `email`
     - `message`

4. **Delete (DELETE):** `/api/contact/form/{id}/`
   - **Required Parameters:**
     - `id`


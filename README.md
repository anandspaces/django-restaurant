# Restaurant Reservation System

A Django-based restaurant reservation system with a simple frontend built using vanilla JavaScript, HTML, and CSS. This application enables customers to make reservations, view their reservation details, and confirm their reservations.

## Features

- **Home Page:** Landing page for the application.
- **Reservation Form:** Customers can fill out a form to make a reservation.
- **Unique Reference Number:** Each reservation is assigned a unique reference number.
- **Reservation Details:** View reservation details after submission.
- **Reservation Confirmation:** Confirmation page for successful reservations.
- **User Authentication:** Basic login and signup pages (templates provided).

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** JavaScript, HTML, CSS
- **Database:** SQLite (default Django database)

## Installation and Setup

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.x
- Django 4.x
- Virtual environment tool (optional but recommended)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/restaurant-reservation-system.git
   cd restaurant-reservation-system
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

## Usage

### Reservation Flow

1. Navigate to the homepage.
2. Click on "Make a Reservation" to access the reservation form.
3. Fill out the required details and submit the form.
4. View your reservation details and unique reference number.
5. Confirm your reservation.

### Authentication

- Use the login and signup pages to manage user accounts (templates provided but not fully functional).

## Future Enhancements

- Integrate user authentication for secure reservations.
- Add an admin panel for restaurant staff to manage reservations.
- Improve the UI/UX with modern frontend frameworks
- Enable email notifications for reservation confirmation.

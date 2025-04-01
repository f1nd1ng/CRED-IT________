## Getting Started


### Prerequisites 

> - django fromework backend
>     - Requirements
>       - Python (>= 3.x)
>       - pip (Python package manager)
>       - Virtualenv (Recommended for dependency management)
>       - Django

> 
> - next.js frontend
>   - Requirements
>       - Node.js (>= 16.x recommended)
>       - npm


### Installation

> - Clone the Repository
> ```
> git clone <Repository url>
> 
> ```
> - Install Django framework
> ```
> # Navigate to the backend directory
> cd credit_backend
> 
> # Create a virtual environment(Optional but Recommended)
> python -m venv venv
> 
> # Activate the virtual environment
> # Windows:
> venv\Scripts\activate
> # macOS/Linux:
> source venv/bin/activate
> 
>  # Install dependencies
> pip install -r requirements.txt
> 
> # Apply database migrations
> python manage.py migrate
> 
> # Run the Django server
> python manage.py runserver
> 
> #By default, the backend will run at: http://127.0.0.1:8000/
> ```
> - Install npm
> ```
> # Navigate to the frontend directory
> cd ../credit_frontend
> 
> # Install dependencies
> npm install
> 
> # Run the Next.js development server
> npm run dev  
>
> # Make sure to run at (http://localhost:3000/) due to google authentication
> ```
>

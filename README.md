##About the Project 
(already written by Sakshi)


## Built With

This project was developed using the following technologies:

[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)  
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)  
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)  
[![Gemini API](https://img.shields.io/badge/Gemini%20API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemini-api/docs/api-key)  


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




## Usage

This project helps users **track expenses, estimate credit scores, and receive personalized credit card recommendations** based on their spending habits. Here’s how it can be used:  

#### **1. Profile Management & Secure Login**  
- Users can **sign up, log in, and manage their profiles** securely, with Google login support for convenience.  
- Profile details, including **income and expenses,** can be updated to ensure accurate recommendations.  

#### **2. Expense and Income Tracking**  
- Users can **log income and categorize expenses** (e.g., groceries, rent, dining) for better financial awareness.  
- A **detailed transaction history** helps monitor spending trends.  

#### **3. Personalized Credit Card Recommendations**  
- The system **analyzes spending patterns** to suggest the **top 5 credit cards** that best match the user's lifestyle.  
- Recommendations consider **rewards, cashback, and benefits and spending habits** to maximize value.  

#### **4. Credit Score Estimation**  
- Users can **estimate their credit score** based on financial inputs like income, expenses, and outstanding debt.  
- The system helps users understand how different financial decisions **may impact their score.**  

#### **5. Financial Guidance via Chatbot**  
- A **Gemini API-powered chatbot** provides **basic financial advice** and answers common questions about credit cards and credit scores.  

By using this system, users can **gain better financial insights, optimize their spending, and choose the right credit card with confidence.**



## Contributors

> By Group 4(JuniHers)

- Ramanu Rishita -       [f1nd1ng](https://github.com/f1nd1ng) - Developed the finance tracker feature and worked on integration.
- Kaithey Hanika Vasu -  [Hanikaaaa](https://github.com/Hanikaaaa) - Worked on the chatbot and contributed to the credit card recommendation model.
- Sonali Sharma -        [Sonali0309](https://github.com/Sonali0309) - Worked on the chatbot and contributed to the credit card recommendation model.
- Vidhi Gupta -           [vidhi-gupta45](https://github.com/vidhi-gupta45) - Developed the credit score simulator and worked on UI.

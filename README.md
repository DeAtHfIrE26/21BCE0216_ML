# 🌟 Intelligent Retrieval System

[![GitHub stars](https://img.shields.io/github/stars/DeAtHfIrE26/21BCE0216_ML?style=social)](https://github.com/DeAtHfIrE26/21BCE0216_ML/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/DeAtHfIrE26/21BCE0216_ML?style=social)](https://github.com/DeAtHfIrE26/21BCE0216_ML/network/members)
[![GitHub issues](https://img.shields.io/github/issues/DeAtHfIrE26/21BCE0216_ML)](https://github.com/DeAtHfIrE26/21BCE0216_ML/issues)

Welcome to the **Intelligent Retrieval System**! This project is a sophisticated backend solution for document retrieval, leveraging the power of Neo4j for data storage and providing a robust API interface for real-time document search and management.

![Drs](https://github.com/user-attachments/assets/ac31efd9-5327-4103-8759-49458f340d0e)


## ✨ Features

- **Advanced Document Retrieval:** Utilizes custom encoders and Neo4j for efficient document storage and retrieval.
- **High-Performance Caching:** Implements optimized caching strategies for faster response times.
- **Background Scraping Service:** Automatically scrapes news articles in a separate thread to keep the data up-to-date.
- **Comprehensive API Endpoints:** Provides endpoints for health checks, search functionality, and user management.
- **User Request Management:** Monitors user request frequency and manages rate-limiting.
- **Dockerized Deployment:** Easily deploy the application using Docker for consistent and scalable environments.
- **API Logging and Inference Time Recording:** Tracks API performance and request details for better observability.

## 🛠️ Installation and Setup

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8 or above
- Docker (for containerized deployment)
- Neo4j Desktop or AuraDB account

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/DeAtHfIrE26/21BCE0216_ML.git
   cd 21BCE0216_ML

Set Up Python Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
Configure Neo4j Connection:

Update the graph_service.py file with your Neo4j credentials:

python
Copy code
uri = "neo4j+s://<your-neo4j-uri>"
user = "neo4j"
password = "<your-password>"
Run the Application:

bash
Copy code
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
The API will be available at http://localhost:8000.

🐳 Docker Deployment
Build the Docker Image:

bash
Copy code
docker build -t intelligent-retrieval-system .
Run the Docker Container:

bash
Copy code
docker run -p 8000:8000 intelligent-retrieval-system

📖 Usage
Available API Endpoints
GET /health - Check if the API is active.
POST /search - Perform a search query with parameters like text, top_k, and threshold.
GET /users/{user_id} - Fetch user details and request frequency.
GET /logs - Retrieve API logs and inference times.
Example Request
bash
Copy code
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{
  "text": "machine learning",
  "top_k": 5,
  "threshold": 0.7
}'

🔄 Background Scraping Service
The application automatically starts a background thread to scrape news articles as soon as the server starts. This feature ensures that the database is continuously updated with the latest information.

📊 Performance and Rate Limiting
Rate Limiting: Each user can make up to 5 requests; exceeding this limit will result in an HTTP 429 status code.
API Logging: Logs all API requests and records inference time for monitoring and debugging purposes.

🚧 Future Enhancements
Integrate more sophisticated machine learning models for document encoding.
Expand the scraping service to include a wider range of data sources.
Improve caching strategies to further optimize performance.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Neo4j - Graph Database Platform
FastAPI - Modern, Fast (high-performance) web framework for Python
Uvicorn - ASGI server for Python web apps

📬 Contact
If you have any questions or feedback, feel free to open an issue or contact the repository maintainer at DeAtHfIrE26.

## UI Components

This section contains various UI components designed to demonstrate modern web design practices. Check out the sample UI card component:

- [Sample UI Card](ui-components/sample-ui-card.html)




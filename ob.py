import chromadb
from langchain_community.llms import Ollama

chroma_client = chromadb.PersistentClient(path='apidata')
job_collection = chroma_client.get_or_create_collection(name="job_details")
    #data preprocessing
candidate_data=[
  {
    "title": "Modern Portfolio Website",
    "description": "A clean and minimal portfolio template for designers and developers.",
    "metadata": {
      "category": "Portfolio",
      "author": "John Doe"
    },
    "link": "https://example.com/portfolio-template"
  },
  {
    "title": "E-commerce Storefront",
    "description": "A responsive e-commerce template with integrated shopping cart and checkout.",
    "metadata": {
      "category": "E-commerce",
      "author": "Jane Smith"
    },
    "link": "https://example.com/ecommerce-template"
  },
  {
    "title": "Corporate Business Landing Page",
    "description": "A professional landing page template for corporate businesses and startups.",
    "metadata": {
      "category": "Business",
      "author": "Alice Brown"
    },
    "link": "https://example.com/business-template"
  },
  {
    "title": "Restaurant Website Template",
    "description": "A stylish and functional template for restaurants, cafes, and food businesses.",
    "metadata": {
      "category": "Food & Beverage",
      "author": "Michael Lee"
    },
    "link": "https://example.com/restaurant-template"
  },
  {
    "title": "Real Estate Listing Page",
    "description": "A modern template for real estate agencies to showcase property listings.",
    "metadata": {
      "category": "Real Estate",
      "author": "Sophia Martinez"
    },
    "link": "https://example.com/real-estate-template"
  },
  {
    "title": "SaaS Product Landing Page",
    "description": "A conversion-optimized landing page for SaaS products and startups.",
    "metadata": {
      "category": "Technology",
      "author": "David Wilson"
    },
    "link": "https://example.com/saas-template"
  },
  {
    "title": "Event Conference Website",
    "description": "An engaging website template for promoting and managing events and conferences.",
    "metadata": {
      "category": "Events",
      "author": "Olivia Taylor"
    },
    "link": "https://example.com/event-template"
  },
  {
    "title": "Travel Blog Template",
    "description": "A visually appealing blog template for travel enthusiasts and bloggers.",
    "metadata": {
      "category": "Blogging",
      "author": "Liam Anderson"
    },
    "link": "https://example.com/travel-blog-template"
  },
  {
    "title": "Fitness Coaching Website",
    "description": "A dynamic and engaging website template for personal trainers and fitness coaches.",
    "metadata": {
      "category": "Health & Fitness",
      "author": "Emma White"
    },
    "link": "https://example.com/fitness-template"
  },
  {
    "title": "Educational Course Platform",
    "description": "A fully responsive template for online courses, featuring lessons and quizzes.",
    "metadata": {
      "category": "Education",
      "author": "Noah Harris"
    },
    "link": "https://example.com/education-template"
  }, {
    "title": "Tech Startup Landing Page",
    "description": "A modern and sleek landing page template for tech startups and SaaS businesses.",
    "metadata": {
      "category": "Landing Page",
      "author": "Emily Brown"
    },
    "link": "https://example.com/tech-startup-template"
  },
  {
    "title": "Real Estate Listing Website",
    "description": "A comprehensive template for real estate agents to list properties with images and details.",
    "metadata": {
      "category": "Real Estate",
      "author": "Michael Lee"
    },
    "link": "https://example.com/real-estate-template1"
  },
  {
    "title": "Fitness Gym Website",
    "description": "A high-energy fitness website template perfect for gyms, trainers, and workout programs.",
    "metadata": {
      "category": "Health & Fitness",
      "author": "Sarah Johnson"
    },
    "link": "https://example.com/fitness-gym-template"
  },
  {
    "title": "Travel Blog Template",
    "description": "A stylish and visually appealing travel blog template for explorers and storytellers.",
    "metadata": {
      "category": "Blog",
      "author": "David Martinez"
    },
    "link": "https://example.com/travel-blog-template1"
  },
  {
    "title": "Restaurant Menu Website",
    "description": "A restaurant menu and reservation template featuring an elegant design.",
    "metadata": {
      "category": "Food & Beverage",
      "author": "Olivia Wilson"
    },
    "link": "https://example.com/restaurant-menu-template"
  },
  {
    "title": "Photography Portfolio",
    "description": "A visually rich portfolio template for photographers to showcase their work.",
    "metadata": {
      "category": "Portfolio",
      "author": "James Anderson"
    },
    "link": "https://example.com/photography-portfolio-template"
  },
  {
    "title": "Online Course Platform",
    "description": "A complete online course template for educators and e-learning platforms.",
    "metadata": {
      "category": "Education",
      "author": "Sophia Miller"
    },
    "link": "https://example.com/online-course-template"
  },
  {
    "title": "Event Booking Website",
    "description": "An event booking and ticketing template for concerts, meetups, and conferences.",
    "metadata": {
      "category": "Events",
      "author": "Daniel Roberts"
    },
    "link": "https://example.com/event-booking-template"
  },
  {
    "title": "Medical Clinic Website",
    "description": "A professional website template for medical clinics and healthcare providers.",
    "metadata": {
      "category": "Healthcare",
      "author": "Isabella Clark"
    },
    "link": "https://example.com/medical-clinic-template"
  },
  {
    "title": "Non-Profit Organization Website",
    "description": "A charity-focused website template to promote fundraising and volunteer opportunities.",
    "metadata": {
      "category": "Non-Profit",
      "author": "William Scott"
    },
    "link": "https://example.com/nonprofit-template"
  }
]
#yaha pe change kerna data jo dena hai isformat me dena
documents = []
metadata = []
url = []
description=[]
for items in candidate_data:
    items=dict(items)
    documents.append(items["title"])
    metadata.append(items["metadata"])
    url.append(items["link"])
    description.append(items["description"])

    #pushing the resume data to vector database

job_collection.upsert(documents=documents,metadatas=metadata,ids=url)

system_prompt='''You are an advanced AI assistant that processes multilingual user queries and converts them into clear, concise English for retrieval in a vector database.
Instructions:
Accept user input in any language.
Accurately translate and simplify the query into standard English while preserving the original intent.
Remove unnecessary words, slang, or regional idioms while ensuring clarity.
Structure the output in a format optimized for search in a vector database.
If the query is ambiguous, provide a clearer version while maintaining neutrality.'''
#initilizing llama2 model
llm = Ollama(model="llama2", base_url = "http://localhost:11434", system=system_prompt, temperature=0.0)
UI=input("enter request: ")
prompt=llm.invoke(UI)
job_result = job_collection.query(query_texts=[prompt],n_results=1)
print(job_result)



#using servers api
import requests

# Define Ollama's API URL (you will need to provide the correct one)
ollama_api_url = "http://103.251.17.92:6565/output"  # Example: "http://localhost:8080/api/generate"

# Define the prompt you want to send to Ollama
prompt = input("enter query from user : ")

# Create a payload (parameters can change depending on the Ollama API)
payload = {"text": prompt}

# Send a POST request to Ollama API
response = requests.post(ollama_api_url, json=payload)

# Check if the response is successful and print the result
if response.status_code == 200:
    result = response.json()
    print(f"Response: {result['text']}")
else:
    print(f"Error: {response.status_code}")

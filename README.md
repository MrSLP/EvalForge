A project overview and usage instructions.

markdown
Copy
# EvalForge

EvalForge is a local, HIPAA-safe evaluation and reporting assistant that:
- Allows secure upload and processing of evaluation reports.
- Uses local AI models (via Ollama) for dual-model summarization.
- Incorporates RAG-style memory for style-aware prompt generation.
- Provides interfaces for managing student profiles, file vaults, timelines, and eligibility criteria.
- Generates professional narrative reports and exports them to DOCX, PDF, or TXT.
- Includes advanced features such as auto-tagging, progress dashboards, voice commands, and more.

## Project Structure

EvalForge_Full_Project_Final/ ├── app/ │ ├── init.py # Application factory & configuration │ ├── app.py # Main Flask app │ ├── models.py # SQLAlchemy models │ ├── backend/ # Core backend modules (PDF parsing, summarization, etc.) │ └── rag_engine/ # RAG memory and prompt building modules ├── frontend/ # HTML, CSS, and JavaScript for UI ├── node/ # Helper node scripts ├── uploads/ # Directory for uploaded files ├── instance/ # Instance-specific configuration ├── requirements.txt # Python dependencies ├── run.py # Application entry point ├── start_evalforge.bat # Windows launcher ├── .gitignore # Git ignore file └── README.md # Project overview

markdown
Copy

## Setup Instructions

1. **Install Dependencies**  
   Create a virtual environment and run:  
pip install -r requirements.txt

markdown
Copy

2. **Configure the Application**  
Create an `instance/config.py` file (see sample below) to set your secret keys and configuration parameters.

3. **Run the Application**  
Start the Flask app using:  
python run.py

nginx
Copy
Or use the provided batch script on Windows:  
start_evalforge.bat

markdown
Copy

4. **Access the UI**  
Open your browser and navigate to:  
http://127.0.0.1:5000/

csharp
Copy

## License

[Specify your license here]

## Contact

[Your contact information]

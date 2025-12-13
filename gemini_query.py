import google.generativeai as genai
import config

class GeminiQueryEngine:
    """Handles queries to Gemini with document context"""
    
    def __init__(self):
        """Initialize Gemini API"""
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(config.GEMINI_MODEL)
        print("✅ Connected to Gemini API")
    
    def query(self, context, user_question):
        """Query Gemini with document context"""
        try:
            # Create prompt with context
            prompt = f"""You are an AI assistant with access to the following documents:

{context}

Based on the documents above, please answer the following question:
{user_question}

If the answer is not found in the documents, say so clearly."""

            print("🤔 Sending query to Gemini...")
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            print(f"❌ Error querying Gemini: {e}")
            return f"Error: {str(e)}"
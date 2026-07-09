from huggingface_hub import InferenceClient
import requests
from dotenv import load_dotenv
import os


load_dotenv()

client = InferenceClient(
    
    api_key = os.getenv("HF_TOKEN"),
)

def generate_health_remark(glucose, haemoglobin, cholesterol):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced healthcare assistant. "
                    "Evaluate ONLY the three laboratory values provided. "
                    "Use these reference ranges:\n\n"

                "Glucose (fasting):\n"
                "- 70-99 mg/dL: Normal\n"
                "- 100-125 mg/dL: Prediabetes\n"
                "- 126 mg/dL or above: High\n\n"

                "Haemoglobin:\n"
                "- 12.0-17.5 g/dL: Normal\n"
                "- Below 12.0 g/dL: Low\n"
                "- Above 17.5 g/dL: High\n\n"

                "Total Cholesterol:\n"
                "- Below 200 mg/dL: Normal\n"
                "- 200-239 mg/dL: Borderline High\n"
                "- 240 mg/dL or above: High\n\n"

                "Rules:\n"
                "1. Compare only with these ranges.\n"
                "2. Do not invent diseases.\n"
                "3. If a value is normal, say it is normal.\n"
                "4. Recommend consulting a doctor ONLY when one or more values are outside the normal range.\n"
                "5. If all values are normal, encourage maintaining a healthy lifestyle instead.\n"
                "6. Keep the response concise."
          
                 )
            },
            {   "role": "user",
                "content": f"""
                Glucose: {glucose} mg/dL
                Haemoglobin: {haemoglobin} g/dL
                Cholesterol: {cholesterol} mg/dL

               Return the result in this format:

               Glucose:
              - Status:
              - Remark:

               Haemoglobin:
              - Status:
              - Remark:

               Cholesterol: 
              - Status:
              - Remark:

              Overall Summary:
              - Summary:

            Recommendation:
            - Recommendation:
                            """}] , max_tokens=500,
    )

    return response.choices[0].message.content


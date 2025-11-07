from flask import Flask, request, jsonify
from common import vn
import pandas as pd

app = Flask(__name__)

# Keywords to identify strategic questions
STRATEGIC_KEYWORDS = ["why", "how", "what if", "strategy", "suggest"]

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({"error": "Question is required."}), 400

    # "Two-Brain" Logic: Route question based on keywords
    if any(keyword in question.lower() for keyword in STRATEGIC_KEYWORDS):
        # Route to Gemma for strategic questions
        try:
            response = vn.generate_plotly_code(question=question)
            return jsonify({"response_type": "strategic", "response": response})
        except Exception as e:
            return jsonify({"error": f"Error with strategic model: {e}"}), 500
    else:
        # Route to Vanna for factual questions
        try:
            sql = vn.generate_sql(question=question)
            df = vn.run_sql(sql=sql)

            # "Presentation Layer": Summarize the data with Gemma
            if not df.empty:
                summary_prompt = f"Summarize the following data in a friendly, natural language sentence:\n{df.to_string()}"
                summary = vn.generate_plotly_code(question=summary_prompt) # Using generate_plotly_code as a stand-in for a generic text generator
                return jsonify({
                    "response_type": "factual",
                    "summary": summary,
                    "data": df.to_dict(orient='records')
                })
            else:
                return jsonify({
                    "response_type": "factual",
                    "summary": "I couldn't find any data to answer your question.",
                    "data": []
                })

        except Exception as e:
            return jsonify({"error": f"Error with factual model: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

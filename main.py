from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

answers = {
    "Does the college have a football team?" : "Yes, the college has a football team. The name of the team is Cincinnati Bearcats",
    "Does it have a Computer Science Major?" : "Yes, the college offers a Computer Science Major Program.",
    "What is the in-state tuition?" : "The in-state tuition for the college is $20,000.",
    "Does it have on-campus housing?" : "Yes, the college offers on-campus housing in various places around the campus."
}

@app.route('/')
def index():
    return render_template('user.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        user_first_name = request.form['user_first_name']
        user_last_name = request.form['user_last_name']
        user_email = request.form['user_email']
        questions = list(answers.keys())
        return render_template('chatbot.html', user_first_name=user_first_name, user_last_name=user_last_name, user_email=user_email, questions=questions)

@app.route('/answers', methods=['POST'])
def get_answers():
    selected_questions = request.json.get('questions', [])
    response = [answers.get(q, "I'm sorry, I don't have an answer. If you have any question from the above list, please type full question as mentioned above.") for q in selected_questions]
    return jsonify(response)

@app.route('/end_chat', methods=['GET', 'POST'])
def end_chat():
    if request.method == 'GET':
        user_first_name = request.args.get('first_name', '')
        user_last_name = request.args.get('last_name', '')
        user_email = request.args.get('email', '')
        creator_first_name = "Uday Surya Deveswar Reddy"  # Replace with actual creator's first name
        creator_last_name = "Kovvuri"    # Replace with actual creator's last name
        creator_email = "kovvuruy@mail.uc.edu"    # Replace with actual creator's email address
        return render_template('final_page.html', user_first_name=user_first_name, user_last_name=user_last_name, user_email=user_email, creator_first_name=creator_first_name, creator_last_name=creator_last_name, creator_email=creator_email)
    elif request.method == 'POST':
        # Handle post request (if needed)
        return "Method not allowed", 405

if __name__ == '__main__':
    app.run(debug=True)
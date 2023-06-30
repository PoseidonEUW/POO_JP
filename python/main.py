from Options.date import Date
from Options.word import Word
from passwordGuesser import PasswordGuesser
from info import Info
from verify import Verify

from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__, template_folder='templates',static_folder='static')

@app.route('/', methods=['GET'])
def show_form():
   return render_template('index.html')

@app.route('/results', methods=['POST'])
def handle_form_submission():
   data = request.get_json()

   # Retrieve the form values from the data
   name = data['name']
   currentDate = data['currentDate']
   # If currentDate is empty, set it to today's date
   if currentDate == '':
      currentDate = datetime.date.today()
      formatedCurrentDate = currentDate
   # Format the date to YYYY-MM-DD
   else:
      formatedCurrentDate = datetime.datetime.strptime(currentDate, '%Y-%m-%d')
   optionWord = data['optionWord']
   optionDate = data['optionDate']
   optionSpecialChars = data['optionSpecialChars']

   # Set up the required objects and parameters for password generation
   optionWordObj = Date(
      optionWord['allMin'],
      optionWord['allMaj'],
      optionWord['capital'],
      optionWord['noAccent'],
      optionWord['leet']
   )
   optionDateObj = Word(
      optionDate['dateNumbers'],
      optionDate['humanMonth'],
      optionDate['twoDigitYear'],
      optionDate['fourDigitYear'],
      optionDate['language']
   )
   personalInfo = Info([name], [formatedCurrentDate])
   verify = Verify(personalInfo, optionWordObj, optionDateObj)

   passwordGenerator = PasswordGuesser(verify)

   # Generate the password based on the form options
   passwords = passwordGenerator.all_combinations
   # Return the response as JSON
   response = {'password': passwords}
   return jsonify(response)

def main():
   print("Welcome to Password Checker")
   handle_form_submission()

# Using the special variable __name__
if __name__ == "__main__":
    main()
    app.run()
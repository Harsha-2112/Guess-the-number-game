import random
from flask import Flask , render_template,request,redirect
app = Flask(__name__)
secret_number = random.randint(1,100)
chances = 5
game_over = False

@app.route('/', methods = ['GET','POST'])
def home():
    global chances,game_over
    message = " "

    if request.method == 'POST':
        if chances<= 0:
            message = 'Game over click try again'
        else :
            guess = int(request.form['guess'])
            if guess<secret_number:
                chances -= 1
                message = 'Too low try again above ',guess
          
            elif guess > secret_number:
                chances -= 1
                message = ' Too High try agin below ', guess
            
            else :
                message = 'Congratulations.. You guessed correctly',secret_number
                game_over = True
        if chances == 0:
            message = ' Game over The number was :',secret_number
            game_over = True

    return render_template('index.html', message=message,chances=chances,game_over=game_over)

@app.route('/restart')
def restart () :
    global secret_number , chances, game_over
    secret_number = random.randint(1,100)
    chances = 5
    game_over = False
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
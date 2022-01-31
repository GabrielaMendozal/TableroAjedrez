from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/', methods = ['GET'])
def paginaInicial ():
    return render_template('index.html',row=8,col=8)




if __name__ == '__main__':
    app.run(debug=True)



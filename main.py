from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def promotion_image():
    return f'''<title>Колонизация</title><link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" /><h1>Жди нас, Марс</h1><img src="{url_for('static', filename='img/img.png')}" 
                   alt="здесь должна была быть картинка, но не нашлась"><h1>{'</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                                                                                           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])}</h1>'''


@app.route('/choice/<name>')
def choice(name):
    return f'''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <body>
  <h1>Мое предложение: {name}</h1>
  <div class="alert alert-primary" role="alert"> 
           Эта планета просто прекрсаная 
           </div> 
           <div class="alert alert-secondary" role="alert"> 
           Потому что в её навание есть гласные буквы 
           </div> 
           <div class="alert alert-success" role="alert"> 
           Ура солнечной системе! 
           </div> 
           <div class="alert alert-danger" role="alert"> 
           Ура нашей миссии по колонизации марса!' 
           </div> 
           <div class="alert alert-warning" role="alert"> 
           Преходите на /form_sample 
           </div> 
           </div>
  </body>
</html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
      </head>
      <body>
      <h1>Результаты отбора</h2>
      <h3>Претендента на участие в миссии: {nickname}</h1>
      <div class="alert alert-primary" role="alert">
          Поздравляем ваш рейтинг после {level} этапа
        </div>
        <div class="alert alert-secondary" role="alert">
          составляет {rating}
        </div>
        <div class="alert alert-danger" role="alert">
          Желаем удачи
        </div>
      </body>
    </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 text-align="center">Анкета претендента</h1>
                            <h2 text-align="center">На участие в миссии</h2>
                            <div>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                            <title>Отбор астронавтов</title>
                                    <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" placeholder="Введите почту" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Другое</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="classSelect">Какая у Вас профессия</label>
                                        <select class="form-control" id="classSelect" name="profession">
                                          <option>Инженер-исследователь</option>
                                          <option>Пилот</option>
                                          <option>Экзобиолог</option>
                                          <option>Инженер по терраформированию</option>
                                          <option>Специалист по радиационной защите</option>
                                          <option>Астрогеолог</option>
                                          <option>Инженер жизнеобеспечения</option>
                                          <option>Метеоролог</option>
                                          <option>Оператор марсохода</option>
                                          <option>Киберинженер</option>
                                          <option>Штурман</option>
                                          <option>Пилот дронов</option>
                                        </select>
                                     </div>
                                         <div class="form-group">
                                            <label for="photo">Выберите файл</label>
                                            <input type="file" class="form-control-file" id="file" name="file">
                                         </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="form-group">
                                        <label for="about">Мотивация</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Готовы остаться на Марсе?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="answer" id="yes" value="yes" checked>
                                          <label class="form-check-label" for="yes">
                                            Да
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="answer" id="no" value="no">
                                          <label class="form-check-label" for="no">
                                            Нет
                                          </label>
                                        </div>
                                    </div>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['profession'])
        try:
            print(request.files['file'])
            f = request.files['file']
            out = open("static/res.jpg", 'wb')
            out.write(f.read())
            out.close()
        except Exception:
            pass
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['answer'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

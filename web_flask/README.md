#Web framework

 Web web application  web  a software framework that is designed to support the development of web applications including web services, web resources and web . In simple words, web frameworks are a piece of software that offers a way to create and run web applications. Thus, you t need to code on your own and look for probable miscalculations and faults.donAPIsas frameworksor frameworksframework

 # Flask

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

                             
                               # save this as app.py
                        from flask import Flask, escape, request

                        app = Flask(__name__)

                        @app.route('/')
                         def hello():
                         name = request.args.get("name", "World")
                         return f'Hello, {escape(name)}!'

                   $ flask run
           
              * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)      

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""<h1>Bienvenido a nuestra página de inicio</h1>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac ligula et lorem ultricies eleifend. Nulla facilisi.</p>
                        """)

def about(request):
    return HttpResponse("""<p>Suspendisse potenti. Mauris rutrum, arcu vitae bibendum placerat, dolor purus feugiat tortor, a bibendum mi ex vitae velit. Ut ac odio et tortor molestie mattis. Fusce non orci est. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Duis feugiat velit justo, et dictum mauris bibendum sed. Ut in fermentum dui, ac tristique magna.</p>
                        """)

def contact(request):
    return HttpResponse("""<h3>Contacto</h3>
                        <form action="/my-handling-form-page" method="post">
                        <ul>
                            <li>
                            <label for="name">Nombre:</label>
                            <input type="text" id="name" name="user_name" />
                            </li>
                            <li>
                            <label for="mail">Correo electrónico:</label>
                            <input type="email" id="mail" name="user_mail" />
                            </li>
                            <li>
                            <label for="msg">Mensaje:</label>
                            <textarea id="msg" name="user_message"></textarea>
                            </li>
                        </ul>
                        </form>
                        """)




from pywebio import start_server #local server
from pywebio.input import *   
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def App():
    def check_user (data) :
        if len(data['username']) > 7:
            return ('username', 'اسم المشترك اكتر من 7 احرف')
        
    # رسائل من نوع popup and toast
    popup("Hi! I'm Marouan Welcom To My Python Web Application. May,26 2022 1h39AM",
    put_text("اضغط هنا لمشاهدة عدد المشتركين").onclick(lambda: toast("الان فقط صاحب الموقع و انت"))
  )
     # image and text tag html
    put_html('<center><h3> نضام تشجيل المشركين </h3><img src="https://ps.w.org/user-avatar-reloaded/assets/icon-256x256.png?rev=2540745" width="150px"></center>')

    # المداخل 
    data = input_group(
      'مشترك جديد',
      [
          input('اسم المشترك', name='username'),
          input('البريد الالكتروني', name='email'),
          input('كلمة السر', name='pass', type=PASSWORD)
      ],validate=check_user # def chack user lfo9
  )
      # print data

    put_text('New User :').style('background: red; color: white; font-weight: bold; font-size:18px;')
    put_text('Username : %r' % data['username'])
    put_text('Email : %r' % data['email'])
    put_text('Password : %r' % data['pass'])


start_server (App, port=4567 , debug=True)




# python version 3.9.7
#librery  pywebio
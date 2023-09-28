from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask,render_template,request,redirect,session,jsonify
from DBConnection import Db
import datetime
import random
import tkinter


app = Flask(__name__)
app.secret_key="a"
path=r"C:\Users\akash\PycharmProjects\COLLEGE AUTOMATION\static\IMAGE\\"






@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        user=request.form['textfield']
        pswd = request.form['textfield2']
        db=Db()
        res=db.selectOne("select * from login where username='"+user+"'and password='"+pswd+"'")
        if res is not None:
            session['lid']=res['LOGIN_ID']
            if res['USERTYPE']=='admin':
                return redirect('/adminhome')
            elif res['USERTYPE']=='teacher':
                return redirect('/teacherhome')
            else :
                return "invalid"
        else :
            return "invalid"
    return render_template("index.html")




@app.route('/adminhome')
def adminhome():
    return render_template('adminindex.html')

@app.route('/teacherhome')
def teacherhome():
    return render_template('teacherindex.html')

@app.route('/logout')
def logout():
    return render_template('index.html')



@app.route('/ADD_COURSE',methods=['get','post'])
def ADD_COURSE():
    if request.method == "POST":
        dep  = request.form['select']
        course = request.form['textfield']
        db=Db()
        db.insert("insert into course values('','"+dep+"','"+course+"')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_COURSE"</script>'
    else:
        db=Db()
        res=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        return render_template("admin/ADD_COURSE.html",data=res)

@app.route('/VIEW_COURSE')
def VIEW_COURSE():
        db=Db()
        qry=db.select("select * from course,department where course.DEPARTMENT_ID=department.DEPARTMENT_ID  ORDER BY COURSE_NAME ASC")
        return render_template("admin/VIEW_COURSE.html",data=qry)


@app.route('/UPDATE_COURSE/<cid>',methods=['GET','POST'])
def UPDATE_COURSE(cid):
    if request.method == "POST":
        dep  = request.form['select']
        course = request.form['textfield']
        db=Db()
        db.update("update course set DEPARTMENT_ID='"+dep+"',COURSE_NAME='"+course+"' where COURSE_ID='"+cid+"' ")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_COURSE"</script>'
    else:
        db=Db()
        res=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        re=db.selectOne("select * from course where COURSE_ID='"+cid+"' ORDER BY COURSE_NAME ASC")
        return render_template("admin/UPDATE_COURSE.html",data2=res,data=re)
@app.route('/DELETE_COURSE/<d>')
def DELETE_COURSE(d):
        db=Db()
        db.delete("delete from course where COURSE_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_COURSE"</script>'





@app.route('/ADD_DEPARTMENT',methods=['get','post'])
def ADD_DEPARTMENT():
    if request.method == "POST":
        dep = request.form['textfield']
        db = Db()
        db.insert("insert into department values('','"+dep+"')")
        return '<script>alert("ADDES SUCCESFULLY");window.location="/adminhome"</script>'
    else:
        return render_template("admin/ADD_DEPARTMENT.html")
@app.route('/UPDATE_DEPARTMENT/<did>',methods=['GET','POST'])
def UPDATE_DEPARMENT(did):
    if request.method == "POST":
        dep  = request.form['textfield']
        db=Db()
        db.update("update department set DEPARTMENT_NAME='"+dep+"' where DEPARTMENT_ID='"+did+"' ")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_DEPARTMENT"</script>'
    else:
        db=Db()
        r=db.selectOne("select * from department where DEPARTMENT_ID='"+did+"'")
        return render_template("admin/UPDATE_DEPARTMENT.html",data=r)
@app.route('/VIEW_DEPARTMENT')
def VIEW_DEPARTMENT():
        db = Db()
        qry=db.select("SELECT * FROM department ORDER BY DEPARTMENT_NAME ASC ")
        return render_template("admin/VIEW_DEPARTMENT.html",data=qry)
@app.route('/DELETE_DEPARTMENT/<d>')
def DELETE_DEPARTMENT(d):
        db=Db()
        db.delete("delete from department where DEPARTMENT_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_DEPARTMENT"</script>'






@app.route('/ADD_EVENT',methods=['get','post'])
def ADD_EVENT():
    if request.method == "POST":
        name = request.form['textfield']
        date = request.form['textfield2']
        image = request.files['fileField']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        image.save(path + d + '.jpg')
        pp = "/static/IMAGE/" + d + '.jpg'
        details= request.form['textarea']
        db = Db()
        db.insert("insert into event values('','"+name+"','"+details+"','"+pp+"','"+date+"')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_EVENT"</script>'
    else:
        return render_template("admin/ADD_EVENT.html")
@app.route('/UPDATE_EVENT/<upe>',methods=['get','post'])
def UPDATE_EVENT(upe):
    if request.method == "POST":
        eventname=request.form['textfield']
        eventdate=request.form['textfield2']
        eventimg=request.files['fileField']
        d=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        eventimg.save(path+d+'.jpg')
        pp="/static/IMAGE/"+d+'.jpg'
        eventdet=request.form['textarea']
        db = Db()
        res=db.selectOne("select * from event where EVENT_ID='"+str(upe)+"' and EVENT_NAME='"+eventname+"'and EVENT_DATE='"+eventdate+"'and EVENT_IMAGE='"+pp+"'and EVENT_DEATILES='"+eventdet+"'")
        if res is not None:
            return '<script>alert("no change");window.location="//VIEW_EVENT"</script>'
        else:
            if request.files!="none":
                if eventimg.filename!="":
                        db.update("update event set EVENT_NAME='"+eventname+"',EVENT_DATE='"+eventdate+"',EVENT_IMAGE='"+pp+"',EVENT_DEATILES='"+eventdet+"' where EVENT_ID='"+str(upe)+"'")
                        return  '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_EVENT"</script>'
                else:
                    db.update("update event set EVENT_NAME='" + eventname + "',EVENT_DATE='" + eventdate + "',EVENT_DEATILES='" + eventdet + "' where EVENT_ID='" + str( upe) + "'")
                    return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_EVENT"</script>'
            else:
                db.update("update event set EVENT_NAME='" + eventname + "',EVENT_DATE='" + eventdate + "',EVENT_DEATILES='" + eventdet + "' where EVENT_ID='" + str(upe) + "'")
                return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_EVENT"</script>'

    else:
        db=Db()
        r=db.selectOne("select * from event where EVENT_ID='"+upe+"'")
        return render_template("admin/UPDATE_EVENT.html",data=r)
@app.route('/VIEW_EVENT')
def VIEW_EVENT():
        db = Db()
        qry=db.select("select * from event ORDER BY DATE(EVENT_DATE) ASC")
        return render_template("admin/VIEW_EVENT.html",data=qry)
@app.route('/DELETE_EVENT/<d>')
def DELETE_EVENT(d):
        db=Db()
        db.delete("delete from event where EVENT_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_EVENT"</script>'













@app.route('/ADD_NOTIFICATION',methods=['get','post'])
def ADD_NOTIFICATION():
    if request.method == "POST":
        name = request.form['textfield2']
        deails = request.form['textarea']
        rec=request.form['select']
        db = Db()
        db.insert("insert into notification values('','"+name+"','"+deails+"',curdate(),'admin','"+rec+"')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_NOTIFICATION"</script>'
    else:
        return render_template("admin/ADD_NOTIFICATION.html")
@app.route('/UPDATE_NOTIFICATION/<id>',methods=['get','post'])
def UPDATE_NOTIFICATION(id):
    if request.method == "POST":
        notification=request.form['textfield']
        notification_det=request.form['textarea']
        db = Db()
        db.update("update notification set NOTIFICATION_NAME='"+notification+"',NOTIFICATION_DEATILES='"+notification_det+"' where NOTIFICATION_ID='"+id+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_NOTIFICATION"</script>'
    else:
        db=Db()
        r=db.selectOne("select * from notification")
        return render_template("admin/UPDATE_NOTIFICATION.html",data=r)
@app.route('/VIEW_NOTIFICATION')
def VIEW_NOTIFICATION():
        db = Db()
        qry=db.select("select * from notification ORDER BY DATE(NOTIFICATION_DATE) ASC")
        return render_template("admin/VIEW_NOTIFICATION.html",data=qry)
@app.route('/DELETE_NOTIFICATION/<d>')
def DELETE_NOTIFICATION(d):
        db=Db()
        db.delete("delete from notification where NOTIFICATION_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_NOTIFICATION"</script>'








@app.route('/ADD_STUDENT',methods=['get','post'])
def ADD_STUDENT():
    if request.method == "POST":
       dept = request.form['select']
       course = request.form['select2']
       sems = request.form['select3']
       name= request.form['textfield2']
       email = request.form['textfield3']
       regno = request.form['textfield']
       passwd=random.randint(0000,9999)
       import smtplib
       try:
           s = smtplib.SMTP(host='smtp.gmail.com', port=587)
           s.starttls()
           s.login("pcasc2020.23@gmail.com", "lsbebosufwinwsmv")
           msg = MIMEMultipart()  # create a message.........."
           msg['From'] = "pcasc2020.23@gmail.com"
           msg['To'] = email
           msg['Subject'] = "Your Password for Smart Donation Website"
           try:
               body = "Your username is your email     Your Password is:- - " + str(passwd)
               msg.attach(MIMEText(body, 'plain'))
               s.send_message(msg)

               db = Db()
               r = db.insert("insert into login values('','" + email + "','" + str(passwd) + "','student')")
               db.insert("insert into student values('" + str(r) + "','" + name + "','" + dept + "','" + course + "','" + regno + "','','" + sems + "','','','','','','" + email + "','pending')")
               return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_STUDENT"</script>'
           except Exception as e:
               return '<script>alert("WRONG");window.location="/ADD_STUDENT"</script>'
       except Exception as e:
           return '<script>alert("INVALID EMAIL ");window.location="/ADD_STUDENT"</script>'
    else:
        db=Db()
        q=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        r=db.select("select * from course ORDER BY COURSE_NAME ASC")
        return render_template("admin/ADD_STUDENT.html",data=q,data2=r)
@app.route('/UPDATE_STUDENT/<ID>',methods=['get','post'])
def UPDATE_STUDENT(ID):
    if request.method == "POST":
        department=request.form['select']
        course=request.form['select2']
        sems=request.form['select3']
        regno = request.form['textfield4']
        name=request.form['textfield2']
        email=request.form['textfield3']
        db = Db()
        db.update("update student set STUDENT_NAME='"+name+"',DEPARTMENT_ID='"+department+"',COURSE_ID='"+course+"',REGISTER_NO='"+regno+"',SEM='"+sems+"',EMAIL='"+email+"' where STUDENT_ID='"+ID+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_STUDENT"</script>'
    else:
        db=Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        q=db.select("select * from course ORDER BY COURSE_NAME ASC")
        t=db.selectOne("select * from student where STUDENT_ID='"+ID+"'")
        return render_template("admin/UPDATE_STUDENT.html",data2=r,data1=q,data=t)
@app.route('/VIEW_STUDENT',methods=['get','post'])
def VIEW_STUDENT():
    if request.method=="POST":
        c=request.form['select']
        d=request.form['select2']
        db = Db()
        dept = db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        cos = db.select("select * from course  ORDER BY COURSE_NAME ASC ")
        qry=db.select("select * from student,department,course where student.DEPARTMENT_ID=department.DEPARTMENT_ID AND student.COURSE_ID=course.COURSE_ID AND course.DEPARTMENT_ID=department.DEPARTMENT_ID and student.DEPARTMENT_ID='"+c+"'and student.COURSE_ID='"+d+"' ORDER BY STUDENT_NAME ASC")
        return render_template("admin/VIEW_STUDENT.html",data=qry,data2=dept,data3=cos)
    else:
        db = Db()
        dept=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        cos=db.select("select * from course ORDER BY COURSE_NAME ASC")
        qry = db.select("select * from student,department,course where student.DEPARTMENT_ID=department.DEPARTMENT_ID AND student.COURSE_ID=course.COURSE_ID AND course.DEPARTMENT_ID=department.DEPARTMENT_ID")
        return render_template("admin/VIEW_STUDENT.html", data=qry,data2=dept,data3=cos)

@app.route('/DELETE_STUDENT/<d>')
def DELETE_STUDENT(d):
        db=Db()
        db.delete("delete from student where STUDENT_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_STUDENT"</script>'







@app.route('/ADD_SUBJECT',methods=['get','post'])
def ADD_SUBJECT():
    if request.method == "POST":
        dept = request.form['select']
        course = request.form['select2']
        sub = request.form['textfield']
        db = Db()
        db.insert("insert into subject values('','"+sub+"','"+course+"','"+dept+"')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_SUBJECT"</script>'
    else:
        db=Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        q=db.select("select * from course ORDER BY COURSE_NAME ASC")
        return render_template("admin/ADD_SUBJECT.html",data=r,data2=q)

@app.route('/UPDATE_SUBJECT/<ID>',methods=['GET','POST'])
def UPDATE_SUBJECT(ID):
    if request.method == "POST":
        dep  = request.form['select']
        course = request.form['select2']
        sub=request.form['textfield']
        db=Db()
        db.update("update subject set DEPARTMENT_ID='"+dep+"',COURSE_ID='"+course+"',SUBJECT_NAME='"+sub+"' where SUBJECT_ID='"+ID+"' ")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_SUBJECT"</script>'
    else:
        db=Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        q=db.select("select * from course ORDER BY COURSE_NAME ASC")
        t = db.selectOne("select * from subject where SUBJECT_ID='"+ID+"'")
        return render_template("admin/UPDATE_SUBJECT.html",data2=r,data1=q,data=t)
@app.route('/VIEW_SUBJECT')
def VIEW_SUBJECT():
        db = Db()
        qry=db.select("select * from `subject`,course where subject.COURSE_ID=course.COURSE_ID ORDER BY SUBJECT_NAME ASC")
        return render_template("admin/VIEW_SUBJECT.html",data=qry)
@app.route('/DELETE_SUBJECT/<d>')
def DELETE_SUBJECT(d):
        db=Db()
        db.delete("delete from subject where SUBJECT_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_SUBJECT"</script>'









@app.route('/ADD_TEACHER',methods=['get','post'])
def ADD_TEACHER():
    if request.method == "POST":
        dept = request.form['select']
        name = request.form['textfield']
        email = request.form['textfield2']
        passwd = random.randint(0000, 9999)
        import smtplib
        try:
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("pcasc2020.23@gmail.com", "lsbebosufwinwsmv")
            msg = MIMEMultipart()  # create a message.........."
            msg['From'] = "pcasc2020.23@gmail.com"
            msg['To'] = email
            msg['Subject'] = "Your Password for Smart Donation Website"
            try:
                body = "Your Password is:- - " + str(passwd)
                msg.attach(MIMEText(body, 'plain'))
                s.send_message(msg)

                db = Db()
                r = db.insert("insert into login values('','" + email + "','" + str(passwd) + "','teacher')")
                q=db.insert("insert into teacher values('"+str(r)+"','"+dept+"','"+name+"','','','','','','','','"+email+"')")
                return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_TEACHER"</script>'
            except Exception as e:
                return '<script>alert("WRONG");window.location="/ADD_TEACHER"</script>'
        except Exception as e:
            return '<script>alert("INVALID EMAIL ");window.location="/ADD_TEACHER"</script>'
    else:
        db=Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        return render_template("admin/ADD_TEACHER.html",data=r)

@app.route('/UPDATE_TEACHER/<id>',methods=['get','post'])
def UPDATE_TEACHER(id):
    if request.method == "POST":
        department=request.form['select']
        name=request.form['textfield']
        email=request.form['textfield2']
        db = Db()
        db.update("update teacher set TEACHER_NAME='"+name+"',DEPARTMENT_ID='"+department+"',EMAIL='"+email+"' where TEACHER_ID='"+id+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_TEACHER"</script>'
    else:
        db=Db()
        r1=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        r=db.selectOne("select * from teacher where TEACHER_ID='"+id+"'")
        return render_template("admin/UPDATE_TEACHER.html",data=r,data1=r1)
@app.route('/VIEW_TEACHER',methods=['get','post'])
def VIEW_TEACHER():
    if request.method=="POST":
        depart=request.form['select']
        db = Db()
        res = db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        qry=db.select("select * from teacher,department where teacher.DEPARTMENT_ID=department.DEPARTMENT_ID and department.DEPARTMENT_ID='"+str(depart)+"' ORDER BY TEACHER_NAME ASC")
        return render_template("admin/VIEW_TEACHER.html",data=qry,data2=res)
    else:
        db=Db()
        res=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        return render_template("admin/VIEW_TEACHER.html",data2=res)
@app.route('/DELETE_TEACHER/<d>')
def DELETE_TEACHER(d):
        db=Db()
        db.delete("delete from teacher where TEACHER_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_TEACHER"</script>'










@app.route('/ADD_TUTOR',methods=['get','post'])
def ADD_TUTOR():
    if request.method == "POST":
        teachname = request.form['select']
        coursename = request.form['select2']
        sem= request.form['select3']
        db = Db()
        db.insert("insert into tutor values('','"+teachname+"','"+coursename+"','"+sem+"')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_TUTOR"</script>'
    else:
        db=Db()
        r=db.select("select * from teacher ORDER BY TEACHER_NAME ASC" )
        q=db.select("select * from course ORDER BY COURSE_NAME ASC")
        return render_template("admin/ADD_TUTOR.html",data=r,data2=q)
@app.route('/UPDATE_TUTOR/<ID>',methods=['get','post'])
def UPDATE_TUTOR(ID):
    if request.method == "POST":
        name=request.form['select']
        cou=request.form['select2']
        db = Db()
        db.update("update tutor set TEACHER_ID='"+name+"',COURSE_ID='"+cou+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/UPDATE_TUTOR"</script>'
    else:
        db=Db()
        r1=db.select("select * from teacher ORDER BY TEACHER_NAME ASC")
        r=db.select("select * from course  ORDER BY COURSE_NAME ASC")
        t=db.selectOne("select * from tutor")
        return render_template("admin/UPDATE_TUTOR.html",data2=r,data1=r1,data=t)
@app.route('/VIEW_TUTOR')
def VIEW_TUTOR():
        db = Db()
        qry=db.select("select * from tutor,teacher,course where tutor.TEACHER_ID=teacher.TEACHER_ID AND tutor.COURSE_ID=course.COURSE_ID  ORDER BY TEACHER_NAME ASC")
        return render_template("admin/VIEW_TUTOR.html",data=qry)
@app.route('/DELETE_TUTOR/<d>')
def DELETE_TUTOR(d):
        db=Db()
        db.delete("delete from tutor where TUTOR_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_TUTOR"</script>'








@app.route('/ADD_TIMETABLE',methods=['get','post'])
def ADD_TIMETABLE():
    if request.method == "POST":
        dept = request.form['select']
        course = request.form['select2']
        sem = request.form['select3']
        date=request.form['textfield']
        s1 = request.form['select4']
        s2 = request.form['select5']
        s3 = request.form['select6']
        s4 = request.form['select7']
        s5 = request.form['select8']
        db = Db()
        db.insert("insert into timetable value('','"+date+"','"+s1+"','"+s2+"','"+s3+"','"+s4+"','"+s5+"','"+dept+"','"+course+"','"+sem+"')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/ADD_TIMETABLE"</script>'
    else:
        db=Db()
        r=db.select("select * from department  ORDER BY DEPARTMENT_NAME ASC")
        q=db.select("select * from course  ORDER BY COURSE_NAME ASC")
        t=db.select("select * from subject  ORDER BY SUBJECT_NAME ASC")
        return render_template("admin/ADD_TIMETABLE.html",data=r,data2=q,data3=t)
@app.route('/UPDATE_TIMETABLE/<tid>',methods=['get','post'])
def UPDATE_TIMETABLE(tid):
    if request.method == "POST":
        department =request.form['select']
        course =request.form['select2']
        sem = request.form['select3']
        sub1=request.form['select4']
        sub2 = request.form['select5']
        sub3 = request.form['select6']
        sub4 = request.form['select7']
        sub5 = request.form['select8']
        db = Db()
        db.update("update timetable set DEPARTMENT_ID='"+department+"',COURSE_ID='"+course+"',SUBJECT1='"+sub1+"',SUBJECT2='"+sub2+"',SUBJECT3='"+sub3+"',SUBJECT4='"+sub4+"',SUBJECT5='"+sub5+"',SEMESTER='"+sem+"' where TIMETABLE_ID='"+tid+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_TIMETABLE"</script>'
    else:
        db=Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC ")
        q=db.select("select * from course ORDER BY COURSE_NAME ASC")
        t=db.select("select * from subject ORDER BY SUBJECT_NAME ASC ")
        s=db.selectOne("select * from timetable where TIMETABLE_ID='"+tid+"'")
        return render_template("admin/UPDATE_TIMETABLE.html",data=r,data2=q,data3=t, data4=s)
@app.route('/VIEW_TIMETABLE',methods=['get','post'])
def VIEW_TIMETABLE():
    if request.method=="POST":
        dept=request.form['select']
        cou=request.form['select2']
        sem=request.form['select3']
        db = Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        q = db.select("select * from course ORDER BY COURSE_NAME ASC")
        qry=db.select("SELECT t.*, A.SUBJECT_NAME AS SUBJECT1_NAME, B.SUBJECT_NAME AS SUBJECT2_NAME, G.SUBJECT_NAME AS SUBJECT3_NAME, E.SUBJECT_NAME AS SUBJECT4_NAME, F.SUBJECT_NAME AS SUBJECT5_NAME FROM timetable t INNER JOIN department d ON t.DEPARTMENT_ID = d.DEPARTMENT_ID INNER JOIN course c ON t.COURSE_ID = c.COURSE_ID LEFT JOIN subject A ON t.SUBJECT1 = A.SUBJECT_ID  LEFT JOIN subject B ON t.SUBJECT2 = B.SUBJECT_ID LEFT JOIN subject G ON t.SUBJECT3 = G.SUBJECT_ID  LEFT JOIN subject E ON t.SUBJECT4 = E.SUBJECT_ID  LEFT JOIN subject F ON t.SUBJECT5 = F.SUBJECT_ID   WHERE d.DEPARTMENT_ID = '"+dept+"'  AND c.COURSE_ID = '"+cou+"'  AND t.SEMESTER = '"+sem+"'")
        return render_template("admin/VIEW_TIMETABLE.html",data3=qry,data=r,data2=q)
    else:
        db=Db()
        r=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        q=db.select("select * from course ORDER BY COURSE_NAME ASC")
        return render_template("admin/VIEW_TIMETABLE.html", data=r,data2=q)
@app.route('/DELETE_TIMETABLE/<d>')
def DELETE_TIMETABLE(d):
        db=Db()
        db.delete("delete from timetable where TIMETABLE_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_TIMETABLE"</script>'









@app.route('/VIEW_REPLY')
def VIEW_REPLY():
        db = Db()
        qry=db.select("select * from `leave`,teacher where leave.TEACHER_ID=teacher.TEACHER_ID")
        return render_template("admin/VIEW_REPLY.html",data=qry)
@app.route('/DELETE_REPLY/<d>')
def DELETE_REPLY(d):
        db=Db()
        db.delete("delete from leave where LEAVE_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_REPLY"</script>'
@app.route('/SEND_REPLY/<id>',methods=['get','post'])
def SEND_REPLY(id):
    if request.method=="POST":
        reply=request.form['textarea']
        db = Db()
        db.update("update `leave` set REPLY='"+reply+"',REPLY_DATE=curdate() where LEAVE_ID='"+str(id)+"'")
        return '<script>alert("REPLY SEND SUCCESFULLY");window.location="/VIEW_REPLY"</script>'
    else:
        return render_template("admin/SEND_REPLY.html")



###############################################     TEACHER           #############################################################################################
###############################################     TEACHER           #############################################################################################


@app.route('/ADD_ATTENDANCE/<SID>',methods=['get','post'])
def ADD_ATTENDANCE(SID):
    if request.method=="POST":
      subject=request.form['select2']
      attendance=request.form['select']
      db=Db()
      db.insert("insert into attendence values('','"+subject+"','"+SID+"',curdate(),'"+attendance+"')")
      return '<script>alert("ADDED SUCCESFULLY");window.location="/VIEW_ATTENDANCE"</script>'
    else :
        db=Db()
        r=db.select("select * from subject ORDER BY SUBJECT_NAME ASC")
        return render_template("teacher/ADD_ATTENDANCE.html",data=r)

@app.route('/UPDATE_ATTENDANCE<SID>',methods=['get','post'])
def UPDATE_ATTENDANCE(SID):
    if request.method == "POST":
        subject = request.form['select']
        attendance = request.form['select2']
        db=Db()
        db.update("update attendence set SUBJECT_ID='"+subject+"',ATTENDENCE='"+attendance+"'")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/VIEW_ATTENDANCE"</script>'
    else:
        db=Db()
        res=db.select("select * from subject ORDER BY SUBJECT_NAME ASC")
        return render_template("teacher/UPDATE_ATTENDANCE.html",data=res)


@app.route('/VIEW_ATTENDANCE',methods=['get','post'])
def VIEW_ATTENDANCE():
    if request.method=="POST":
        subject=request.form['select']
        db=Db()
        res2 = db.select("select * from subject ORDER BY SUBJECT_NAME ASC")
        res=db.select("select * from attendence,subject,student where attendence.SUBJECT_ID=subject.SUBJECT_ID and attendence.STUDENT_ID=student.STUDENT_ID like subject.SUBJECT_NAME='%"+subject+"%'")
        return render_template("teacher/VIEW_ATTENDENCE.html",data2=res,data=res2)
    else:
        db=Db()
        res=db.select("select * from subject ORDER BY SUBJECT_NAME ASC")
        return render_template("teacher/VIEW_ATTENDENCE.html",data=res)

@app.route('/DELETE_ATTENDANCE<SID>')
def DELETE_ATTENDANCE():
    db=Db()
    db.delete("delete from attendence where ATENDENCE_ID='"+SID+"'")
    return "OK"



@app.route('/ADD_PROFILE',methods=['get','post'])
def ADD_PROFILE():
    if request.method == "POST":
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        picture = request.files['fileField']
        picture.save(path + d + '.jpg')
        pic = "/static/IMAGE/" + d + '.jpg'
        dob=request.form['textfield']
        qualification=request.form['textfield2']
        place=request.form['textfield3']
        post=request.form['textfield4']
        pin=request.form['textfield5']
        cont=request.form['textfield6']
        email=request.form['textfield7']
        db=Db()
        res=db.selectOne("select * from teacher where EMAIL='"+email+"'")
        if res is not None:
            db.update("update teacher set DOB='"+dob+"',QUALIFICATION='"+qualification+"',PLACE='"+place+"',PIN='"+pin+"',POST='"+post+"',IMAGE='"+pic+"',CONTACT='"+cont+"',EMAIL='"+email+"'")
            return  '<script>alert("ADDED SUCCESFULLY");window.location="/VIEW_PROFILE"</script>'
        else:
            return '<script>alert("INVAILD");window.location="/ADD_PROFILE"</script>'
    else:
        return render_template("teacher/ADD_PROFILE.html")
@app.route('/UPDATE_PROFILE/<ID>',methods=['get','post'])
def UPDATE_PROFILE(ID):
    if request.method == "POST" :
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        picture = request.files['fileField']
        picture.save(path + d + '.jpg')
        pic = "/static/IMAGE/" + d + '.jpg'
        dob = request.form['textfield']
        qualification = request.form['textfield2']
        place = request.form['textfield3']
        post = request.form['textfield4']
        pin = request.form['textfield5']
        cont = request.form['textfield6']
        name = request.form['textfield7']
        email = request.form['textfield8']
        db=Db()
        res=db.selectOne("select * from teacher where TEACHER_ID='"+str(ID)+"'AND TEACHER_NAME='"+name+"'AND DOB='"+dob+"'AND QUALIFICATION='"+qualification+"'AND PLACE='"+place+"' AND PIN='"+pin+"' AND POST='"+post+"' AND IMAGE='"+pic+"' AND CONTACT='"+cont+"'AND EMAIL='"+email+"'")
        if res is not None:
            return '<script>alert("no change");window.location="//VIEW_PROFILE"</script>'
        else:
            if request.files!="none":
                if picture.filename!="":
                    db.update("update teacher set TEACHER_NAME='"+name+"',DOB='"+dob+"',QUALIFICATION='"+qualification+"',PLACE='"+place+"',PIN='"+pin+"',POST='"+post+"',IMAGE='"+pic+"',CONTACT='"+cont+"',EMAIL='"+email+"' where TEACHER_ID='"+ID+"' ")
                    return '<script>alert("UPDATED SUCCESFULLY");window.location="//VIEW_PROFILE"</script>'
                else:
                    db.update("update teacher set TEACHER_NAME='"+name+"',DOB='"+dob+"',QUALIFICATION='"+qualification+"',PLACE='"+place+"',PIN='"+pin+"',POST='"+post+"',CONTACT='"+cont+"',EMAIL='"+email+"' where TEACHER_ID='"+ID+"' ")
                    return '<script>alert("UPDATED SUCCESFULLY");window.location="//VIEW_PROFILE"</script>'
            else:
                db.update("update teacher set TEACHER_NAME='"+name+"',DOB='"+dob+"',QUALIFICATION='"+qualification+"',PLACE='"+place+"',PIN='"+pin+"',POST='"+post+"',CONTACT='"+cont+"',EMAIL='"+email+"' where TEACHER_ID='"+ID+"' ")
                return '<script>alert("UPDATED SUCCESFULLY");window.location="//VIEW_PROFILE"</script>'
    else:
        db = Db()
        r = db.selectOne("select * from teacher where TEACHER_ID='"+ID+"'")
        return render_template("teacher/UPDATE_PROFILE.html", data=r)

@app.route('/VIEW_PROFILE')
def VIEW_PROFILE():
    db = Db()
    qry = db.selectOne("select * from teacher,department where teacher.DEPARTMENT_ID=department.DEPARTMENT_ID and TEACHER_ID='"+str(session['lid'])+"'")
    return render_template("teacher/VIEW_PROFILE.html",data=qry)

#@app.route('/DELETE_PROFILE<ID>')
#def DELETE_PROFILE(ID):
   ##db.delete("delete from timetable where TIMETABLE_ID='"+ID+"'")
    #return "OK"


@app.route('/VIEW_STUDENT_LIST')
def VIEW_STUDENT_LIST():
    db=Db()
    res=db.select("select * from student,course where student.COURSE_ID=course.COURSE_ID  AND STATUS='APPROVED' ORDER BY STUDENT_NAME ASC")
    return render_template('teacher/VIEW_STUDENT_LIST.html',data=res)



@app.route('/ADD_MARK/<sid>/<cid>',methods=['get','post'])
def ADD_MARK(sid,cid):
    if request.method=="POST":
        sub=request.form['select']
        mark=request.form['textfield']
        db=Db()
        db.insert("insert into mark values('','"+sid+"','"+cid+"','"+sub+"','"+mark+"',null,null)")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/VIEW_MARK"</script>'
    else:
        db=Db()
        res=db.select("select * from subject ORDER BY SUBJECT_NAME ASC")
        return render_template("teacher/ADD_MARK.html",data=res)
@app.route('/UPDATE_MARK<MID>',methods=['get','post'])
def UPDATE_MARK(MID):
    if request.method == "POST":
        mark = request.form['textfield']
        db = Db()
        db.update("update mark set SCORE='" + mark + "' WHERE MARK_ID='"+MID+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_MARK"</script>'
    else:
     return render_template("teacher/UPDATE_MARK.html")
@app.route('/VIEW_MARK/<sid>/<cid>')
def VIEW_MARK(sid,cid):
    db=Db()
    res=db.select("select * from mark,subject where mark.SUBJECT_ID=subject.SUBJECT_ID and mark.STUDENT_ID = '"+sid+"' and mark.COURSE_ID= '"+cid+"'")
    return render_template("teacher/VIEW_MARK.html",data=res)
@app.route('/DELETE_MARK<MID>')
def DELETE_MARK(MID):
    db=Db()
    db.delete("delete from mark where MARK_ID='"+MID+"'")
    return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_MARK"</script>'





@app.route('/ADD_TEACHER_NOTIFICATION',methods=['get','post'])
def ADD_TEACHER_NOTIFICATION():
    if request.method == "POST":
        name = request.form['textfield']
        deails = request.form['textarea']
        db = Db()
        db.insert("insert into notification values('','"+name+"','"+deails+"',curdate(),'teacher','student')")
        return '<script>alert("ADDED SUCCESFULLY");window.location="/VIEW_TEACHER_NOTIFICATION"</script>'
    else:
        return render_template("teacher/ADD_NOTIFICATION.html")
@app.route('/UPDATE_TEACHER_NOTIFICATION/<id>',methods=['get','post'])
def UPDATE_TEACHER_NOTIFICATION(id):
    if request.method == "POST":
        notification=request.form['textfield']
        notification_det=request.form['textarea']
        db = Db()
        db.update("update notification set NOTIFICATION_NAME='"+notification+"',NOTIFICATION_DEATILES='"+notification_det+"' where NOTIFICATION_ID='"+id+"'")
        return '<script>alert("UPDATED SUCCESFULLY");window.location="/VIEW_TEACHER_NOTIFICATION"</script>'
    else:
        db=Db()
        r=db.selectOne("select * from notification")
        return render_template("teacher/UPDATE_NOTIFICATION.html",data=r)
@app.route('/VIEW_TEACHER_NOTIFICATION')
def VIEW_TEACHER_NOTIFICATION():
        db = Db()
        qry=db.select("select * from notification where USERTYPE='teacher'")
        return render_template("teacher/VIEW_NOTIFICATION.html",data=qry)
@app.route('/DELETE_TEACHER_NOTIFICATION/<d>')
def DELETE_TEACHER_NOTIFICATION(d):
        db=Db()
        db.delete("delete from notification where NOTIFICATION_ID='"+d+"'")
        return '<script>alert("DELETED SUCCESFULLY");window.location="/VIEW_TEACHER_NOTIFICATION"</script>'






@app.route('/VIEW_ADMIN_NOTIFICATION')
def VIEW_ADMIN_NOTIFICATION():
    db=Db()
    res=db.select("select * from notification where USERTYPE='admin'")
    return render_template("teacher/VIEW_ADMIN_NOTIFICATION.html",data=res)

@app.route('/VIEW_ADMIN_EVENT')
def VIEW_ADMIN_EVENT():
    db=Db()
    res=db.select("select * from event")
    return render_template("teacher/VIEW_ADMIN_EVENT.html",data=res)

@app.route('/APPROVE_STUDENT_PROFILE')
def APPROVE_STUDENT_PROFILE():
    db=Db()
    res=db.select("select * from student,department,course WHERE STATUS='pending' and IMAGE!='' and student.DEPARTMENT_ID=department.DEPARTMENT_ID ORDER BY STUDENT_NAME ASC")
    return render_template("teacher/APPROVE _STUDENT_PROFILE.html",data=res)
@app.route('/APPROVE_STUDENT/<sid>')
def APPROVE_STUDENT(sid):
    db=Db()
    db.update("update student set STATUS='APPROVED' where STUDENT_ID='"+sid+"'")
    return '<script>alert("APPROVED");window.location="/STUDENT_PROFILE"</script>'
@app.route('/REJECT_STUDENT/<sid>')
def REJECT_STUDENT(sid):
    db=Db()
    db.update("update student set STATUS='REJECT' where STUDENT_ID='"+sid+"'")
    return '<script>alert("APPROVED");window.location="/APPROVE_STUDENT_PROFILE"</script>'




@app.route('/STUDENT_PROFILE')
def STUDENT_PROFILE():
    db=Db()
    res=db.select("select * from student,department,course where STATUS='APPROVED' and student.DEPARTMENT_ID=department.DEPARTMENT_ID ORDER BY STUDENT_NAME ASC ")
    return render_template("teacher/STUDENT_PROFILE.html",data=res)




@app.route('/SEND_LEAVE_REQUEST',methods=['get','post'])
def SEND_LEAVE_REQUEST():
    if request.method == "POST":
        dept=request.form['select']
        LEAVE_REASON=request.form['textfield']
        leave_date=request.form['textfield1']
        db=Db()
        res=db.insert("insert into `leave` values('','"+LEAVE_REASON+"','"+str(session['lid'])+"','pending','pending','"+dept+"','"+leave_date+"')")
        return '<script>alert("SENT SUCCESFULLY");window.location="/VIEW_LEAVE_REQUEST_REPLY"</script>'
    else:
        db = Db()
        res=db.select("select * from department ORDER BY DEPARTMENT_NAME ASC")
        return render_template('teacher/SEND_LEAVE_REASON.html',data=res)


@app.route('/VIEW_LEAVE_REQUEST_REPLY')
def VIEW_LEAVE_REQ_REPLY():
    db=Db()
    res=db.select("select * from `leave`")
    return render_template('teacher/VIEW_LEAVE REQUEST_REPLY.html',data=res)





@app.route('/VIEW_STUDENT_LEAVE_REQUEST')
def VIEW_STUDENT_LEAVE_REQUEST():
    db = Db()
    qry = db.select("select * from `leave_student`,student where leave_student.STUDENT_ID=student.STUDENT_ID ORDER BY STUDENT_NAME ASC")
    return render_template('teacher/VIEW_STUDENT_LEAVE_REQUEST.html',data=qry)
@app.route('/SEND_STUDENT_LEAVE_REPLY/<id>',methods=['get','post'])
def SEND_STUDENT_LEAVE_REPLY(id):
    if request.method == "POST":
        reply = request.form['textfield']
        db = Db()
        db.update("update `leave_student` set REPLY='" + reply + "',REPLY_DATE=curdate() where LEAVE_ID='" + str(id) + "'")
        return '<script>alert("REPLY SENT");window.location="/VIEW_STUDENT_LEAVE_REQUEST"</script>'
    else:
        return render_template('teacher/SEND_STUDENT_LEAVE_REPLY.html')


@app.route('/VIEW_SUBJECTS',methods=['get','post'])
def VIEW_SUBJECTS():
    if request.method=="POST":
        course=request.form['course']
        db=Db()
        res=db.select("select * from course ORDER BY COURSE_NAME ASC")
        qry=db.select("select * from subject,course where subject.COURSE_ID=course.COURSE_ID and course.COURSE_ID='"+str(course)+"' ORDER BY SUBJECT_NAME ASC")
        return render_template('teacher/VIEW_SUBJECT.html', data=res, data1=qry)
    else:
        db=Db()
        res=db.select("select * from course ORDER BY COURSE_NAME ASC")
        return render_template('teacher/VIEW_SUBJECT.html', data=res)


@app.route('/UPLOAD/<sid>',methods=['get','post'])
def UPLOAD(sid):
    if request.method=="POST":
        up=request.files['fileField']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        up.save(r"C:\Users\akash\PycharmProjects\COLLEGE AUTOMATION\static\materials\\" + d + '.pdf')
        doc = "/static/materials/" + d + '.pdf'
        db=Db()
        db.insert("insert into study_material values('','"+sid+"',curdate(),'"+doc+"')")
        return '<script>alert("UPLOADED SUCCESFULLY");window.location="/VIEW_SUBJECTS"</script>'
    else:
        return render_template('teacher/UPLOAD_MATERIALS.html')



@app.route('/VIEW_UPLOAD/<sid>')
def VIEW_UPLOAD(sid):
    db=Db()
    res=db.select("select * from study_material,subject where study_material.SUBJECT_ID=subject.SUBJECT_ID  AND study_material.SUBJECT_ID='"+sid+"'")
    return render_template('teacher/VIEW_MATERIAL.html',data=res)



@app.route('/VIEW_PARENT_PROFILE/<sid>')
def VIEW_PARENT_PROFILE(sid):
        db = Db()
        qry=db.selectOne("select * from parent,student where parent.STUDENT_ID=student.STUDENT_ID and student.STUDENT_ID='"+str(sid)+"'")
        return  render_template('teacher/PARENT_PROFILE.html',data=qry)


@app.route('/ADD_PARENT/<sid>',methods=['get','post'])
def ADD_PARENT(sid):
    if request.method=='POST':
        na=request.form['textfield']
        co=request.form['textfield2']
        email=request.form['textfield3']
        passwd = random.randint(0000, 9999)
        import smtplib
        try:
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("pcasc2020.23@gmail.com", "lsbebosufwinwsmv")
            msg = MIMEMultipart()  # create a message.........."
            msg['From'] = "pcasc2020.23@gmail.com"
            msg['To'] = email
            msg['Subject'] = "Your Password for Smart Donation Website"
            try:
                body = "Your username is your email     Your Password is:- - " + str(passwd)
                msg.attach(MIMEText(body, 'plain'))
                s.send_message(msg)

                db = Db()
                r = db.insert("insert into login values('','" + email + "','" + str(passwd) + "','parent')")
                db.insert("insert into parent value('"+str(r)+"','" + sid + "','" + na + "','" + co + "','"+email+"')")
                return '<script>alert("ADDED SUCCESFULLY");window.location="/STUDENT_PROFILE"</script>'
            except Exception as e:
                return '<script>alert("WRONG");window.location="/STUDENT_PROFILE"</script>'
        except Exception as e:
            print(e)
            return '<script>alert("INVALID EMAIL ");window.location="/STUDENT_PROFILE"</script>'
    else:
        return render_template('teacher/ADD_PARENT.html')





#################################################3ANDROID###############################################################




@app.route('/AND_LOGIN_STUDENT',methods=['post'])
def AND_LOGIN_STUDENT():
    username=request.form['u']
    passwrd=request.form['p']
    db=Db()
    res=db.selectOne("Select * from login where USERNAME='"+username+"' and PASSWORD='"+passwrd+"'")
    return jsonify(status="ok",lid=res['LOGIN_ID'],type=res['USERTYPE'])


@app.route('/AND_SEND_LEAVE_REQUEST',methods=['post'])
def AND_SEND_LEAVE_REQUEST():
    reason=request.form['reason']
    lid=request.form['id']
    db=Db()
    db.insert("insert into leave_student values('','"+lid+"',curdate(),'"+reason+"','pending','pending')")
    return jsonify(status="ok")



@app.route('/AND_VIEW_EVENT',methods=['post'])
def AND_VIEW_EVENT():
    db=Db()
    qry=db.select("select * from event ")
    return jsonify(status="ok",data=qry)



@app.route('/AND_VIEW_LEAVE_STATUS',methods=['post'])
def AND_VIEW_LEAVE_STATUS():
    sid = request.form['id']
    db=Db()
    qry=db.select("select * from leave_student where leave_student.STUDENT_ID='"+sid+"'")
    return jsonify(status="ok", data=qry)


@app.route('/AND_VIEW_NOTIFICATION',methods=['post'])
def AND_VIEW_NOTIFICATION():
    db=Db()
    qry=db.select("SELECT * FROM notification WHERE notification.RECIVER_TYPE IN ('STUDENT', 'BOTH')")
    return jsonify(status="ok", data=qry)


@app.route('/AND_VIEW_SUBJECT',methods=['post'])
def AND_VIEW_SUBJECT():
    u=request.form['id']
    db=Db()
    qry=db.select("select * from department,course,`subject`,student where course.DEPARTMENT_ID=department.DEPARTMENT_ID and student.COURSE_ID=course.COURSE_ID AND subject.COURSE_ID=course.COURSE_ID AND student.STUDENT_ID='"+u+"' ")
    print(qry)
    return jsonify(status="ok", data=qry)


@app.route('/AND_VIEW_PROFILE',methods=['post'])
def AND_VIEW_PROFILE():
    sid=request.form['login']
    db=Db()
    qry=db.selectOne("select * from student,course,department where STUDENT_ID='"+sid+"' and STATUS='APPROVED' and student.COURSE_ID=course.COURSE_ID and student.DEPARTMENT_ID=department.DEPARTMENT_ID")
    return jsonify(status="ok", data=qry)\



@app.route('/AND_VIEW_ATTENDENCE',methods=['post'])
def AND_VIEW_ATTENDENCE():
    a=request.form['sbid']
    b=request.form['id']
    db=Db()
    qry=db.select("select * from attendence,subject where attendence.SUBJECT_ID='"+a+"' and attendence.STUDENT_ID='"+b+"' and attendence.SUBJECT_ID=subject.SUBJECT_ID")
    return jsonify(status="ok", data=qry)




@app.route('/AND_VIEW_STUDY_MATERIAL',methods=['post'])
def AND_VIEW_STUDY_MATERIAL():
    # sid=request.form['id']
    a = request.form['suid']
    db = Db()
    qry=db.select("select * from study_material where study_material.SUBJECT_ID='"+a+"'")
    # qry=db.select("select * from study_material,subject,student,course where study_material.SUBJECT_ID='"+a+"' and  subject.COURSE_ID=course.COURSE_ID and study_material.SUBJECT_ID=subject.SUBJECT_ID and student.STUDENT_ID='"+sid+"'")
    return jsonify(status="ok", data=qry)





@app.route('/AND_VIEW_MARK',methods=['post'])
def AND_VIEW_MARK():
    sid=request.form['sid']
    a = request.form['suid']
    db = Db()
    qry=db.select("select * from mark where mark.SUBJECT_ID='"+a+"' and mark.STUDENT_ID='"+sid+"'")
    return jsonify(status="ok", data=qry)





# @app.route('/AND_VIEW_TOTAL_MARK',methods=['post'])
# def AND_VIEW_TOTAL_MARK():
#     db = Db()
#     qry=db.select("SELECT  SUM(score) AS TOTAL FROM mark GROUP BY student_id")
#     return jsonify(status="ok", data=qry)



@app.route('/AND_REGISTRATION',methods=['post'])
def AND_REGISTRATION():
    dob=request.form['dob']
    bg=request.form['bg']
    pl=request.form['pl']
    pt=request.form['pt']
    pn=request.form['pn']
    em=request.form['em']
    d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    picture = request.files['pic']
    picture.save(path + d + '.jpg')
    pic = "/static/IMAGE/" + d + '.jpg'
    login=request.form['lid']
    db = Db()
    res=db.selectOne("select * from student where  EMAIL='"+em+"'AND student.STUDENT_ID='"+login+"'")
    if res is  not None:
        db.update("update student set DOB='"+dob+"' , BLOOD_GROUP='"+bg+"', PLACE='"+pl+"', POST='"+pt+"', PIN='"+pn+"' , EMAIL='"+em+"' , IMAGE='"+pic+"' where STUDENT_ID='"+login+"'")
        return jsonify(status="ok")
    else:
        return jsonify(status="invalid")



########################################################PARENT MODULE##########################################################################################





@app.route('/PARENT_AND_VIEW_SUBJECT',methods=['post'])
def PARENT_AND_VIEW_SUBJECT():
    u=request.form['id']
    print(u)
    db=Db()
    qry=db.select("select * from department,course,`subject`,student,parent where course.DEPARTMENT_ID=department.DEPARTMENT_ID and student.COURSE_ID=course.COURSE_ID AND subject.COURSE_ID=course.COURSE_ID AND parent.STUDENT_ID=student.STUDENT_ID AND parent.PARENT_ID='"+u+"' ")
    print(qry)
    return jsonify(status="ok", data=qry)





@app.route('/AND_PARENT_VIEW_LEAVE_STATUS',methods=['post'])
def AND_PARENT_VIEW_LEAVE_STATUS():
    sid = request.form['id']
    db=Db()
    qry=db.select("select * from leave_student,parent where parent.STUDENT_ID=leave_student.STUDENT_ID and parent.PARENT_ID='"+sid+"'")
    print(qry)
    return jsonify(status="ok", data=qry)


@app.route('/AND_PARENT_VIEW_MARK',methods=['post'])
def AND_PARENT_VIEW_MARK():
    sid=request.form['id']
    a=request.form['suid']
    db=Db()
    qry=db.select("select * from mark,parent where parent.STUDENT_ID=mark.STUDENT_ID AND parent.PARENT_ID='"+sid+"' and mark.SUBJECT_ID='"+a+"'")
    print(qry)
    return jsonify(status="ok",data=qry)




@app.route('/AND_PARENT_VIEW_ATTENDENCE',methods=['post'])
def AND_PARENT_VIEW_ATTENDENCE():
    sid=request.form['id']
    a=request.form['suid']
    db=Db()
    qry=db.select("select * from attendence,parent where parent.STUDENT_ID=attendence.STUDENT_ID AND parent.PARENT_ID='"+sid+"' and attendence.SUBJECT_ID='"+a+"'")
    print(qry)
    return jsonify(status="ok",data=qry)




#################################################################GUEST MODULE################################################################################


@app.route('/GUEST_VIEW_DEPARTMENT',methods=['post'])
def GUEST_VIEW_DEPARTMENT():
    # lid=request.form['id']
    db=Db()
    qry=db.select("select * from department ")
    return jsonify(status="ok", data=qry)


@app.route('/GUEST_VIEW_COURSE',methods=['post'])
def GUEST_VIEW_COURSE():
    a=request.form['did']
    db=Db()
    qry=db.select("select * from course where course.DEPARTMENT_ID='"+a+"' ")
    return jsonify(status="ok", data=qry)\




@app.route('/GUEST_VIEW_EVENT',methods=['post'])
def GUEST_VIEW_EVENT():
    a=request.form['did']
    db=Db()
    qry=db.select("select * from event")
    return jsonify(status="ok", data=qry)






if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


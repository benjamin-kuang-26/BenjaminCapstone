from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Assignment, Comment
from app.classes.forms import AssignmentForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/assignment/new', methods=['GET', 'POST'])
@login_required
def assignmentNew():
    form = AssignmentForm()

    if form.validate_on_submit():

        newAssignment = Assignment(
            assignment_name = form.assignment_name.data,
            course = form.course.data,
            period = form.period.data,
            teacher = form.teacher.data,
            due_date = form.due_date.data,
            author = current_user.id
        )
        newAssignment.save()


        return redirect(url_for('assignment',assignmentID=newAssignment.id))

    return render_template('assignmentform.html',form=form)


@app.route('/assignment/<assignmentID>')

@login_required
def assignment(assignmentID):
    
    thisAssignment = Assignment.objects.get(id=assignmentID)
    
    return render_template('assignment.html', assignment=thisAssignment)


@app.route('/assignment/list')
@app.route('/assignments')
@login_required
def assignmentList():

    assignments = Assignment.objects()
    
    return render_template('assignments.html', assignments=assignments)

 
@app.route('/assignment/edit/<assignmentID>', methods=['GET', 'POST'])
@login_required
def assignmentEdit(assignmentID):
    editAssignment = Assignment.objects.get(id=assignmentID)

    if current_user != editAssignment.author:
        flash("You can't edit a blog you don't own.")
        return redirect(url_for('assignment',assignmentID=assignmentID))

    form = AssignmentForm()
    
    if form.validate_on_submit():
        
        editAssignment.update(
            assignment_name = form.assignment_name.data,
            course = form.course.data,
            period = form.period.data,
            teacher = form.teacher.data,
            due_date = form.due_date.data,
            author = current_user.id,
        )

        return redirect(url_for('assignment',assignmentID=assignmentID))

    form.assignment_name.data = editAssignment.assignment_name
    form.course.data = editAssignment.course
    form.period.data = editAssignment.period
    form.teacher.data = editAssignment.teacher
    form.due_date.data = editAssignment.due_date

    return render_template('assignmentform.html',form=form)


@app.route('/assignment/delete/<assignmentID>')

@login_required
def assignmentDelete(assignmentID):

    deleteAssignment = Assignment.objects.get(id=assignmentID)

    if current_user == deleteAssignment.author:
        
        deleteAssignment.delete()
        
        flash('The Assignment was deleted.')
    else:
        
        flash("You can't delete an assignment you didn't list")
   
    assignments = Assignment.objects()  
   
    return render_template('assignments.html',assignments=assignments)
from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.book import Book


@app.route('/book/new')
def book_form():
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    return render_template('book_form.html')

@app.route('/book', methods=['POST'])
def create_book():
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    # validate data
    if not Book.validate_book(request.form):
        return redirect('/')
    
    data = {
        "title":request.form['title'],
        "author":request.form['author'],
        "num_pages":request.form['num_pages'],
        "user_id": session['user_id']
    }

    Book.save(data)
    return redirect('/dashboard')

@app.route('/book/<int:id>/edit')
def edit_page(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id
    }
    book = Book.get_one_by_id(data)

    return render_template('edit.html', book=book)

@app.route('/book/<int:id>/edit',methods=['POST'])
def edit_book(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id,
        "title":request.form['title'],
        "author":request.form['author'],
        "num_pages":request.form['num_pages'],
        "user_id": session['user_id']
    }
    Book.update(data)
    return redirect('/dashboard')

@app.route('/book/<int:id>/delete')
def delete(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id
    }
    Book.delete(data)
    return redirect('/dashboard')

@app.route('/book/<int:id>')
def show_page(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id
    }
    book = Book.get_one_by_id(data)
    return render_template('show.html', book=book)




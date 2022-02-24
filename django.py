# add form to database 


# there are two ways to do it 
    # using form   --> form .save
    # using create new model  -> model.save()


# first method 
def todocreate(request):
    error = ""
    if request.method == "POST":
        if request.POST["title"] is not None and request.POST["title"] != "":
            form = TodoForms(request.POST)
            newtodo = form.save(commit=False) # dont save it on the database
            newtodo.user = request.user       # add user 
            newtodo.save()
            return redirect('todo:todoall')
        else:
            error = "empty title not allow"
    return render(request, 'todo/createTodo.html' , {'form' : TodoForms() ,'error' : error} )


# show specific user 


def todoContent(request):
    todos_not = Todo.objects.filter(user=request.user, datecompleted__isnull=True)  # read not compleated
    todos_compleate = Todo.objects.filter(user=request.user, datecompleted__isnull=False) # read compleated
    return render(request, 'todo/allinfo.html' , {'todos' : todos })
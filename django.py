# form with all fillded informatnio 

def todopageinfo(request,todo_id):
    todo = get_object_or_404(Todo , pk=todo_id)  # find the instance 
    form = TodoForms(instance=todo)              # create form 
    return render(request , 'todo/todoinfo.html' , { 'todo' : todo , 'form' : form })
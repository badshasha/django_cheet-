
def todopageinfo(request,todo_id):
    todo = get_object_or_404(Todo , pk=todo_id , user= request.user) # other wise user can access to all other objects 

    if request.method == "GET":
        form = TodoForms(instance=todo)
        return render(request , 'todo/todoinfo.html' , { 'todo' : todo , 'form' : form })
    else:
        try:
            form = TodoForms(request.POST,instance=todo)  # most important part [instance todo important]
            form.save()
            print("working")
            return redirect('todo:todoall')
        except ValueError:
            return HttpResponse("bad information ")


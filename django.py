# delete todo

@login_required
def tododelete(request,todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)  # safe content raking
    if request.method == "POST":
        todo.delete()
        return redirect('todo:todoall')
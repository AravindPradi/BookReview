from django.shortcuts import render,redirect
from . models import Books
from . forms import bookform
# Create your views here.
def demo(request):
    result = Books.objects.all()
    context = {
        'book_list':result
    }
    return render(request,"index.html",context)

def detail(request,book_id):
    out = Books.objects.get(id=book_id)
    return render(request,"detail.html",{'result':out})

def add(request):
    if request.method =='POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']

        books = Books(name=name,desc=desc,year=year,img=img)
        books.save()
        return redirect('/')
    return render(request,"add.html")

def update(request,id):
    book = Books.objects.get(id=id)
    form = bookform(request.POST or None,request.FILES,instance=book)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'book':book,'form':form})

def delete(request,id):
    if request.method == 'POST':
        movie = Books.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")
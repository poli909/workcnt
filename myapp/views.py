from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')


def result(request):
    if request.method == 'POST':
        data = request.POST['fulltext']
        word_dict = {}
        words = data.split(' ')
        cnt = len(words)
        

        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        context = {
            'cnt' :cnt,
            'original' : request.POST['fulltext'],
            'dict' : word_dict.items()
        }
        context.update(word_dict)
        print(context)
        return render(request, 'result.html', context)
    return HttpResponse('잘못된 접근입니다.')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
import random
from app.models import JobPost
# Create your views here.

class TemClass:
    x = 5

# job_title = [
#     "First job",
#     "Second job",
#     'Third job'
# ]

# job_description = [
#     "First job description",
#     "Second job description",
#     "Second job description"
# ]

def hello(request):
    #template = loader.get_template('app/hello.html')
    first_list = ["alpha", "beta"]
    is_authenticated = False
    context = {"name": "YC", "age": random.randint(1, 101), "first_list":first_list, "temp": TemClass(), "is_authenticated": is_authenticated}
    # return HttpResponse("<h3>Hello World</h3>")
    #return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)

def job_list(request):
    #<ul><li>Job1</li> <li>job2</li> <li> job 3</li></ul>
    # list_job="<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)

    # # for job_id in range(0, len(job_title)):
    #     print(job_id)
    #     list_job +=f"<li><a href='job/{job_id}'>{job_title[job_id]}</a></li>"
    # list_job+='</ul>'
    # print(list_job)
    # return HttpResponse(list_job)  
    jobs = JobPost.objects.all() 
    context = {"jobs": jobs}
    return render(request, 'app/index.html', context)

def job_detail(request, id):

    print(type(id))
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
            # return redirect("/")
        # return_html=f'<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>'
        job = JobPost.objects.get(id=id)

        # context = {"job_title": job.title, "job_detail": job.description}
        context = {'job': job}
         
    except:
        #return HttpResponse("Not Found")
    #this one will show 200 since it returns to right response
        return HttpResponseNotFound('Not Found') #it shows 404





    # site = 'https://google/com'
    # return HttpResponse(f"<h1>Job detail {id}</h1>")
    # return HttpResponse(f"Visit <a href={site}>Google Here</a>")
    # return HttpResponse(return_html)
    return render(request, 'app/job_detail.html', context)
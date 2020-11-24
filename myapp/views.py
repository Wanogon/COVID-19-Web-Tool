from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import sys
sys.path.append(r'D:\\django_web\\mysite')
import closed_form_A2_approximate_10 as cf
import Testing_cycle_simulation as tcs
import Optimal_Testing_Cycle as otc

# Create your views here.
def welcome(request):
    if request.method == 'GET':
        return render(request, "welcome.html")
    if request.method == 'POST':
        if "Start" in request.POST:
            return HttpResponseRedirect('/myapp/templates/index.html')

#def index(request):
#    if request.method == 'GET':
#        return render(request, "index.html")
#    if request.method == 'POST':
#        print(request.POST.get('p0'))
#        print(request.POST.get('C'))
#        print(request.POST.get('N'))
#        p0, C, N = request.POST.get('p0'), request.POST.get('C'), request.POST.get('N')
#        p0, C, N = eval(p0), eval(C), eval(N)
#        optimal_pool_size, expected_test_times, expected_false_negatives = cf.mixed_array_optimal_n_formulation(N, p0, C)
#       return render(request, "result.html",
#                  {"optimal_pool_size": optimal_pool_size, "expected_test_times": expected_test_times,
 #                  "expected_false_negatives": expected_false_negatives})

def index(request):
    if request.method == 'GET':
        return render(request, "index.html")
    if request.method == 'POST':
        N, C, p0, T, alpha_in, alpha_out = request.POST.get('N'),request.POST.get('C'),request.POST.get('p0'),request.POST.get('T'),request.POST.get('alpha_in'), request.POST.get('alpha_out')
        l = request.POST.get('l')
        N, C, p0, T, alpha_in, alpha_out = eval(N), eval(C), eval(p0), eval(T), eval(alpha_in), eval(alpha_out)
        if l:
            l = eval(l)
            fp, avgs, avgt, avgrq, avgwq, avgfn = tcs.TCS(T, l, N, C, p0, alpha_in, alpha_out)
            if fp != -1:
                msg_1 = 'The final prevalence rate is: '+str(fp)
                msg_2 = 'The optimal pool size for each day is: '+str(avgs)
                msg_3 = 'The expected daily number of tests for each day is: '+str(avgt)
                msg_4 = 'The expected true positives for each day is: '+str(avgrq)
                msg_5 = 'The expected false positives for each day is: '+str(avgwq)
                msg_6 = 'The expected false negatives for each day is: '+str(avgfn)
                msg = msg_1+'\n '+msg_2+'\n '+msg_3+'\n '+msg_4+'\n '+msg_5+'\n '+msg_6+'\n '
                msg = msg.replace('\n', '<br/>')
                return render(request, "result.html", {'Result_Message': msg,
                                                       'final prevalence rate': fp, 'optimal_pool_size': avgs, "expected_test_times": avgt,
                        "expected_true_positives": avgrq, "expected_false_positives": avgwq, "expected_false_negatives": avgfn})
            else:
                msg = 'Error: The testing cycle length is too short to provide enough testing capacity. Please try larger testing cycle length or larger testing capacity.'
                return render(request, "result.html", {'Result_Message': msg})
        else:
            opt_t, fp, avgs, avgt, avgrq, avgwq, avgfn = otc.OTCL(T, N, C, p0, alpha_in, alpha_out)
            if opt_t != -1:
                msg_1 = 'The optimal testing cycle length is: '+str(opt_t)
                msg_2 = 'Corresponding performance measures: '
                msg_3 = 'The final prevalence rate is: '+str(fp)
                msg_4 = 'The optimal pool size for each day is: '+str(avgs)
                msg_5 = 'The expected daily number of tests for each day is: '+str(avgt)
                msg_6 = 'The expected true positives for each day is: '+str(avgrq)
                msg_7 = 'The expected false positives for each day is: '+str(avgwq)
                msg_8 = 'The expected false negatives for each day is: '+str(avgfn)
                msg = msg_1+'\n'+msg_2+'\n'+msg_3+'\n'+msg_4+'\n'+msg_5+'\n'+msg_6+'\n'+msg_7+'\n'+msg_8+'\n'
                msg = msg.replace('\n', '<br/>')
                return render(request, "result.html", {'Result_Message': msg, 'optimal testing cycle length': opt_t, 'final prevalence rate': fp, 'optimal_pool_size': avgs, "expected_test_times": avgt,
                        "expected_true_positives": avgrq, "expected_false_positives": avgwq, "expected_false_negatives": avgfn})
            else:
                msg = 'Error: Reach the maximum of value of testing cycle length, still do not find a feasible length.'
                return render(request, "result.html", {'Result_Message': msg})

def result(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def demo_wait(request):
    return render(request, 'demo_wait.html')
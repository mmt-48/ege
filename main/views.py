from django.shortcuts import render
from .models import Topic
from .models import Probl
from .models import Bimg
from .models import Themes
import socket

def theme(request,pkk):
    prb = Probl.objects.get(pk=pkk)
    hnt = prb.hint_txt

    th = hnt.split("/")
    thm = []
    for t in th:
        tt = Themes.objects.get(pk=int(t))

        u = tt.name_theme.center(100)+tt.content_theme
        thm.append(u)

    context = {
        'thm': thm
    }

    return render(request, 'main/theme.html', context=context)

def index(request):
    if "DESKTOP" in socket.gethostname():
       form_nopor()

    m = nclass(request)

    mm = int(m)

    topp1 = Topic.objects.filter(tip_top=1, mett__lte=mm).order_by("number_in_order")
    topp2 = Topic.objects.filter(tip_top=2, mett__lte=mm).order_by("number_in_order")
    topp3 = Topic.objects.filter(tip_top=3, mett__lte=mm).order_by("number_in_order")
    context = {
        'mm': mm,
        'topp1': topp1,
        'topp2': topp2,
        'topp3': topp3
        }

    return render(request, 'main/index.html', context=context)


def probls(request, pkk):

    m = nclass(request)

    mm = int(m)
    bimgs = Bimg.objects.filter()

    probls = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0).order_by("complexity")

    for p in probls:
        p.ege = p.gkey[0:4]
        p.place_ege = name_zone(zone(p.gkey))
        p.name_potok = name_potok(potok(p.gkey))

    context = {
       'bimgs': bimgs,
       'probls': probls
    }

    return render(request, 'main/probls.html', context=context)

def task(request, pkk):
    houm = 0
    if "DESKTOP" in socket.gethostname():
        houm = 1

    tsk = Probl.objects.filter(pk=pkk)
    context = {
        'houm': houm,
        'tsk': tsk
    }

    return render(request, 'main/task.html', context=context)

def rvvod(request, pkk):
    print('1', request)
    print('2', pkk)
    tsk = Probl.objects.get(pk=pkk)
    hint = tsk.hint_txt
    id = pkk
    context = {
         'id': id,
         'hint': hint
    }

    return render(request, 'main/vvod.html', context=context)


def vvod(request, pkk):

    tsk = Probl.objects.get(pk=pkk)
    hint = tsk.hint_txt
    id = pkk
    context = {
         'id': id,
         'hint': hint
    }

    return render(request, 'main/vvod.html', context=context)


def  zone(gkey):
    if gkey[6] == '_':
        u = gkey[5]
    else:
        u = gkey[5:7]
    return u


def potok(gkey):
    if gkey[6] == '_':
        u = gkey[7]
    else:
        u = gkey[8]
    return u


def name_potok(potok):
    if potok == '1':
        np = 'Профильный-основная волна'
    elif potok == '2':
        np = 'Профильный -досрочная волна'
    elif potok == '3':
        np = 'Профильный-резервный день основной волны'
    elif potok == '4':
        np = 'Профильный-резервный день досрочной волны'
    elif potok == '5':
        np = 'Базовый-основная волна'
    elif potok == '6':
        np = 'Базовый -досрочная волна'
    elif potok == '7':
        np = 'Базовый -резервный день основной волны'
    elif potok == '8':
        np = 'Базовый-резервный день досрочной волны'
    else:
        np = '???'

    return np


def name_zone(zone):
    if zone == '1':
        nz = 'Калининградская область'
    elif zone == '2':                   
        nz = 'Центральная зона'
    elif zone == '3':
        nz = 'Урал'
    elif zone == '5':
        nz = 'Сибирь'
    elif zone == '9':
        nz = 'Дальный Восток'
    else:
        nz = '???'

    return nz


def form_nopor():
    topp = Topic.objects.filter()
    for t in topp:
        t.mett = 11
        probl = Probl.objects.filter(topic=t.pk)
        for p in probl:
            if p.school_class  > 0 and p.school_class < t.mett:
                t.mett = p.school_class
            if p.school_class == 0:
                p.school_class = 11
                p.save()
            t.save()


def ege(request):
    return render(request, 'main/ege.html')


def nclass(request):

    u = str(request)

    k = u.find('_class=')
    m = '11'
    if k > 0:
        m = u[k + 7:k + 8]
        if m == '1':
            m = u[k + 7:k + 9]

    return m

def tak():
     probls = Probl.objects.get(pk=229)

     probls.hint_txt = "<p>1)Решение простых показательных уравнений" \
                      "<p>2)Действия со степенями" \
                      "<p>3)Степень с отрицательным показателем" \
                      "<p>4)Решение линейных уравнений"

     probls.save()

from django.shortcuts import render
from .models import Topic
from .models import Probl
from .models import Bimg
from .models import Themes
from .models import Smailic

import socket


def theme(request, pkk):
    prb = Probl.objects.get(pk=pkk)
    tp = Topic.objects.get(pk=prb.topic_id)
    hnt = prb.hint_txt

    th = hnt.split("/")
    thm = []
    for t in th:
        tt = Themes.objects.get(pk=int(t))

        u = tt.name_theme.center(100) + tt.content_theme
        thm.append(u)

    context = {
        'tp': tp,
        'thm': thm
    }

    return render(request, 'main/theme.html', context=context)


def index(request):
    tp = Topic.objects.get(pk=1)
    e_t = extip(request)
    e_tt = int(e_t)
    if "DESKTOP" in socket.gethostname():
        form_nopor(e_tt)

    m = nclass(request)
    mm = int(m)

    m6_11 = [6, 7, 8, 9, 10, 11]
    if e_tt == 3:
        m6_11 = [6, 7, 8, 9]
        if mm > 9:
            mm = 9
    toppp = Topic.objects.filter(mett2__lte=mm, mett2__gte=1).order_by("number_in_order")
    topp = Topic.objects.filter(mett1__lte=mm, mett1__gte=1).order_by("number_in_order")
    topp1 = Topic.objects.filter(tip_top=1, mett__lte=mm).order_by("number_in_order")
    topp2 = Topic.objects.filter(tip_top=2, mett__lte=mm).order_by("number_in_order")
    topp3 = Topic.objects.filter(tip_top=3, mett__lte=mm).order_by("number_in_order")
    context = {
        'tp': tp,
        'mm': mm,
        'e_tt': e_tt,
        'm6_11': m6_11,
        'toppp': toppp,
        'topp': topp,
        'topp1': topp1,
        'topp2': topp2,
        'topp3': topp3
        }

    return render(request, 'main/index.html', context=context)


def probls(request, pkkk, mm, e_tt):

    tp = Topic.objects.get(pk=pkkk)

    pkk = pkkk

    bimgs = Bimg.objects.filter()

   # pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0).order_by("complexity")
    if e_tt == 1:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=4).order_by("complexity")

    if e_tt == 2:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=8, exam_tip__gte=5).order_by("complexity")

    if e_tt == 3:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=12, exam_tip__gte=9).order_by("complexity")

    sm = Smailic.objects.get(pk=1)

    for p in pr:
        p.ege = p.gkey[0:4]
        p.place_ege = name_zone(zone(p.gkey))
        p.name_potok = name_potok(potok(p.gkey))
        if p.result:
            pp = p.result
            pp = pp.replace('\\', '')
            pp = pp.replace('(', '')
            pp = pp.replace(')', '')
            p.result_full = pp

    context = {
        'mm': mm,
        'tp': tp,
        'sm': sm,
        'bimgs': bimgs,
        'probls': pr

    }

    return render(request, 'main/probls.html', context=context)


def task(request, pkk):
    houm = 0
    if "DESKTOP" in socket.gethostname():
        houm = 1

    tsk = Probl.objects.get(pk=pkk)
    tp = Topic.objects.get(pk=tsk.topic_id)


    tsk.ege = tsk.gkey[0:4]
    tsk.place_ege = name_zone(zone(tsk.gkey))
    tsk.name_potok = name_potok(potok(tsk.gkey))


    context = {
        'tp':tp,
        'houm': houm,
        'tsk': tsk
    }

    return render(request, 'main/task.html', context=context)


def rvvod(request, pkk):

    tsk = Probl.objects.get(pk=pkk)
    hint = tsk.hint_txt
    idd = pkk
    context = {
        'id': idd,
        'hint': hint
    }

    return render(request, 'main/vvod.html', context=context)


def vvod(request, pkk):
    tsk = Probl.objects.get(pk=pkk)
    hint = tsk.hint_txt
    idd = pkk

    context = {
        'id': idd,
        'hint': hint
    }

    return render(request, 'main/vvod.html', context=context)

def zone(gkey):
    return gkey.split('_')[1]

def potok(gkey):
    return gkey.split('_')[2]

def name_potok(potokk):
    if potokk == '1':
        np = 'ЕГЭ профильный-основная волна'
    elif potokk == '2':
        np = 'ЕГЭ профильный -досрочная волна'
    elif potokk == '3':
        np = 'ЕГЭ профильный-резервный день основной волны'
    elif potokk == '4':
        np = 'ЕГЭ профильный-резервный день досрочной волны'
    elif potokk == '5':
        np = 'ЕГЭ базовый-основная волна'
    elif potokk == '6':
        np = 'ЕГЭ базовый-досрочная волна'
    elif potokk == '7':
        np = 'ЕГЭ базовый -резервный день основной волны'
    elif potokk == '8':
        np = 'ЕГЭ базовый-резервный день досрочной волны'
    elif potokk == '9':
        np = 'ОГЭ-основная волна'
    elif potokk == '10':
        np = 'ОГЭ -досрочная волна'
    elif potokk == '11':
        np = 'ОГЭ -резервный день основной волны'
    elif potokk == '12':
        np = 'ОГЭ-резервный день досрочной волны'
    else:
        np = '???'

    return np


def name_zone(zonne):
    if zonne == '1':
        nz = 'Калининградская область'
    elif zonne == '2':
        nz = 'Центральная зона'
    elif zonne == '3':
        nz = 'Урал'
    elif zonne == '5':
        nz = 'Сибирь'
    elif zonne == '9':
        nz = 'Дальный Восток'
    else:
        nz = '???'

    return nz

def form_nopor(e_tt):
    topp = Topic.objects.filter()
    for t in topp:
        t.mett = 12
        t.mett1 = 12
        t.mett2 = 10

    for t in topp:
        pr = Probl.objects.filter(topic=t.pk)

        for p in pr:
            if p.exam_tip != int(potok(p.gkey)):
                p.exam_tip = int(potok(p.gkey))
                p.save()

            if (p.school_class > 0) and (p.school_class < t.mett) and (p.exam_tip <= 4):
                t.mett = p.school_class
            if (p.school_class > 0) and (p.school_class < t.mett1) and (p.exam_tip >= 5) and (p.exam_tip <= 8):
                t.mett1 = p.school_class

            if (p.school_class > 0) and (p.school_class < t.mett2) and (p.exam_tip >= 9) and (p.exam_tip <= 12):
                t.mett2 = p.school_class

            if p.school_class == 0:
                p.school_class = 11
                if e_tt == 3:
                    p.school_class = 9
                p.save()
        if t.mett == 12:
            t.mett = 0
        if t.mett1 == 12:
            t.mett1 = 0
        if t.mett2 == 10:
            t.mett2 = 0

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

def extip(request):
    u = str(request)

    k = u.find('ex_tip=')
    m = '1'
    if k > 0:
        m = u[k + 7:k + 8]

    return m

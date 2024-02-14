from django.shortcuts import render
from .models import Topic
from .models import Probl
from .models import Bimg
from .models import Themes
from .models import Smailic
from .models import Bpdf

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


def variant(request, pkk, e_tt):
    sm = Smailic.objects.get(pk=1)

    prb = Bpdf.objects.get(pk=pkk)
    tp = Topic.objects.get(pk=e_tt) #для фона-у каждого типа- свой фон

    hnt = prb.variant

    th = hnt.split(",")
    thm = []
    for t in th:
        if int(t) != 0:
            tt = Probl.objects.get(pk=int(t))
            tt.complexity = int(t)
            u = tt    ##.condition_txt
            thm.append(u)

    for p in thm:
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
        'tp': tp,
        'sm': sm,
        'thm': thm
    }

    return render(request, 'main/variant.html', context=context)


def index(request):
    #app = QApplication(sys.argv)
    #q = QDesktopWidget().availableGeometry()

    monitor_width = 1000 #q.width()

    mob = 0
    if monitor_width < 500:
        mob = 1


    tp = Topic.objects.get(pk=1)
    e_t = extip(request)
    e_tt = int(e_t)
    vr = exvarsad(request)
    v_r = int(vr)
    if "DESKTOP" in socket.gethostname():
        form_nopor(e_tt)

    m = nclass(request)
    mm = int(m)

    m6_11 = [6, 7, 8, 9, 10, 11]
    if e_tt == 3:
        m6_11 = [6, 7, 8, 9]
        if mm > 9:
            mm = 9

    topppp = Topic.objects.filter(mett3__lte=mm, mett3__gte=1).order_by("number_in_order")
    toppp = Topic.objects.filter(mett2__lte=mm, mett2__gte=1).order_by("number_in_order")
    topp = Topic.objects.filter(mett1__lte=mm, mett1__gte=1).order_by("number_in_order")
    topp1 = Topic.objects.filter(tip_top=1, mett__lte=mm, mett__gte=1).order_by("number_in_order")
    topp2 = Topic.objects.filter(tip_top=2, mett__lte=mm).order_by("number_in_order")
    topp3 = Topic.objects.filter(tip_top=3, mett__lte=mm).order_by("number_in_order")

    if e_tt == 1:
        topr = []
    if e_tt == 2:
        topr = topp
    if e_tt == 3:
        topr = toppp
    if e_tt == 4:
        topr = topppp


    tpdf = Bpdf.objects.filter(exam_tip=e_tt).order_by('gkey')


    for p in tpdf:
        p.variant = p.gkey[0:4] + ' г. ' + name_zone(zone(p.gkey)) + ' ' + name_potok(potok(p.gkey))

    m4 = [['ЕГЭ профиль', 1, 11], ['ЕГЭ база', 2, 11], ['ОГЭ (ГИА)', 3, 9], ['ДВИ (МГУ)', 4, 11]]

    context = {
        'm4': m4,
        'tpdf': tpdf,
        'v_r': v_r,
        'tp': tp,
        'mm': mm,
        'mob': mob,
        'e_tt': e_tt,
        'm6_11': m6_11,
        'topr': topr,
        'topppp': topppp,
        'toppp': toppp,
        'topp': topp,
        'topp1': topp1,
        'topp2': topp2,
        'topp3': topp3
        }

    return render(request, 'main/index.html', context=context)


def pdf(request, e_tt):

    tpdf = Bpdf.objects.filter(exam_tip=e_tt)

    context = {
        'e_tt': e_tt,
         'tpdf': tpdf
    }

    return render(request, 'main/pdf.html', context=context)


def probls(request, pkkk, mm, e_tt):

    tp = Topic.objects.get(pk=pkkk)

    pkk = pkkk

    bimgs = Bimg.objects.filter()

    #pr = Probl.objects.filter()

    if e_tt == 1:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=4).order_by("complexity")

    if e_tt == 2:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=8, exam_tip__gte=5).order_by("complexity")

    if e_tt == 3:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=12, exam_tip__gte=9).order_by("complexity")

    if e_tt == 4:
        pr = Probl.objects.filter(topic=pkk, school_class__lte=mm, number_task__gt=0, exam_tip__lte=13, exam_tip__gte=13).order_by("complexity")


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
       'e_tt': e_tt,
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
    ps = 0
    if 'onclick="smw(' in tsk.solution_txt:
          ps = 1

    tsk.ege = tsk.gkey[0:4]
    tsk.place_ege = name_zone(zone(tsk.gkey))
    tsk.name_potok = name_potok(potok(tsk.gkey))

    str_value = tsk.solution_txt
    f = True
    a = ''
    while ( f ):
        f = False
        x = str_value.partition('smw(')

        if x[1] == 'smw(':
            if a:
                a = a+'/'
            f = True
            str_value = x[2]
            xx = str_value.partition(')')
            a = a+xx[0]
            str_value = x[2]

    thm = []
    th = a.split("/")

    if a:
        for t in th:
            tt = Themes.objects.get(pk=int(t))
            ttt = t
            if int(t) < 10:
                ttt = '90000'+t

            if int(t) > 9 and int(t)<100:
                ttt = '9000'+t
            if int(t)>99 and int(t)<1000:
                ttt = '900'+t

            u = ttt+tt.name_theme.center(100) + tt.content_theme
            thm.append(u)

    context = {
        'tp': tp,
        'thm': thm,
        'houm': houm,
        'ps': ps,
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
    elif potokk == '13':
        np = 'ДВИ'
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
        t.mett3 = 12

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
            if (p.school_class > 0) and (p.school_class < t.mett3) and (p.exam_tip == 13):
                t.mett3 = p.school_class

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
        if t.mett3 == 12:
            t.mett3 = 0

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

def exvarsad(request):
    u = str(request)

    k = u.find('varsad=')
    m = '1'
    if k > 0:
        m = u[k + 7:k + 8]

    return m

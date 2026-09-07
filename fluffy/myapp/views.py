from django.shortcuts import render, HttpResponse
import math
import pandas as pd
import io
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
def home(request):
    return render(request, "home.html")

def og_home(request):
    return render(request, "og-home.html")

def frame_maker(request):
    return render(request, "frame-maker.html")

@ensure_csrf_cookie
def mutuals(request):
    return render(request, "mutuals.html")

@ensure_csrf_cookie
def get_moots_view(upload):
    if upload.method == "POST":
        peopleDoc = pd.read_excel(upload.FILES["classDataUpload"])

        # make a list of all people and class values
        allPeopleList = pd.DataFrame(columns=['Name', 'Classes'])
        classes = pd.DataFrame(columns=['Class', 'Value'])

        maxMootClasses = 0

        for classData in peopleDoc.items():
            for student in classData[1]:
                if type(student) == type(6.7) and math.isnan(student):
                    break
                elif type(student) == type(67) or type(student) == type(6.7):
                    classes.loc[len(classes)] = [classData[0], student]
                else:
                    if not student in allPeopleList.values:
                        allPeopleList.loc[len(allPeopleList)] = [student, [classData[0]]]
                    else:
                        ind = allPeopleList.index[allPeopleList['Name'] == student][0]
                        mootClassList = allPeopleList.at[ind, 'Classes'] + [classData[0]]
                        allPeopleList.loc[ind] = [student, mootClassList]

                        if len(mootClassList) > maxMootClasses:
                            maxMootClasses = len(mootClassList)

        finalString = ""
        for i in range(maxMootClasses, 0, -1):
            for student in allPeopleList.iterrows():
                classesList = student[1]['Classes']
                if len(classesList) == i:
                    finalString = finalString + "(" + str(len(classesList)) + ") " + student[1]['Name'] + ": " + str(classesList) + " | "

            # finalString = finalString +  "\n"

        return JsonResponse({"result": finalString})
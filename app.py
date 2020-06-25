# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:22:08 2020

@author: School
"""
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

import sys
sys.path.append("/abunator_main/")

import counter
import setters
import sqlMethods
import Examine
import result


PathList = [0]


@app.route('/start/<key>',methods = ['GET'])
def starter(key):
    if 'true' in key and len(key) == 14:
        global linker
        linker = key
        setters.setPathList()
        setters.setColumnList()
        setters.setQuestionList()
        setters.setSQLList()
        column = Examine.getCulumn()
        question = Examine.getQuestion(column)
        counter.ColumnList.append(column)
        counter.QuestionList.append(question)
        return render_template('/main.html',\
            key = linker,\
#            question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))
            question = question)

@app.route('/return/<key>',methods = ['GET'])
def initial(key):
    linker = key
    return redirect('https://abunatorroute.azurewebsites.net/return/' + linker)


#@app.route('/main',methods = ['GET'])
#def procedure():
#    return render_template('/main.html',\count = count ,\
#        question = sqlMethods.questionVerse(sqlMethods.getCalm(counter.ColumnList)))


@app.route('/main/<key>', methods = ['POST'])
def branch(key):
    linker = key
    answer = request.form.get("answer")
    path = request.form.get("path")
    column = counter.ColumnList[len(counter.ColumnList)-1]
    question = counter.QuestionList[len(counter.QuestionList)-1]

    del PathList[len(PathList)-1]
    PathList.append(int(path))

    counter.ListMaker(int(answer),column,question)
    count = counter.GetCount()

    if PathList[len(PathList)-1] == 1 and counter.QuestionList[len(counter.QuestionList)-1] == counter.QuestionList[0]:
        return redirect('https://abunatorroute.azurewebsites.net/return/' + linker)

    elif PathList[len(PathList)-1] == 1:
        del counter.SQLList [len(counter.SQLList)-1]
        del counter.SQLList [len(counter.SQLList)-1]
        del counter.ColumnList [len(counter.ColumnList)-1]
        del counter.QuestionList [len(counter.QuestionList)-1]
        return render_template('/main.html',\
        key = linker,\
        question = counter.QuestionList[len(counter.QuestionList)-1])

    elif count == 1:
        number = result.resNumber()
        name = result.resName(number)
        dealing = result.resDealing(number)
        no = str(linker[0:10])
        result.insert(no,name)
        return render_template('/result.html',\
        key = linker,\
        number = number,\
        name = name,\
        no = no,\
        dealing = dealing)

    elif count == 0 or len(counter.ColumnList) >= 50:
        return render_template('/unknown.html',
        key = linker)

    elif count >= 2:
        column = Examine.getCulumn()
        question = Examine.getQuestion(column)
        if not question in counter.QuestionList:
            counter.ColumnList.append(column)
            counter.QuestionList.append(question)
            return render_template('/main.html',\
            key = linker,\
            question = question)
        else:
            while question in counter.QuestionList:
                column = Examine.getCulumn()
                question = Examine.getQuestion(column)
            counter.ColumnList.append(column)
            counter.QuestionList.append(question)
            return render_template('/main.html',\
            key = linker,\
            question = question)
    else:   
        return render_template('/error.html',\
        key = linker)

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)
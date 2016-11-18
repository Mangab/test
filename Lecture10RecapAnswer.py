import statistics

#Problem 1:
def classGrades(infile):
    fileIn = open(infile)
    indexsLst = fileIn.readline().replace('\n','').split('\t')
    contents = fileIn.readlines()
    mainDic = {}

    for line in contents:
        valueDic = {}
        valueLst = line.replace('\n','').split('\t')
        for i in range(len(indexsLst)):
            if valueLst[0] not in mainDic.keys():
                valueDic[indexsLst[i]] = int(valueLst[i])
        if (valueDic['exam2'] - valueDic['exam1']) / 2 > 0:
            valueDic['pta'] = (valueDic['exam2'] - valueDic['exam1']) / 2
        else:
            valueDic['pta'] = 0
        mainDic[valueLst[0]]= valueDic
    return mainDic

examResults = classGrades("MOCK_DATA.txt")


def examStats(gradeBook):
    count = 0
    exam1Lst = []
    exam2Lst = []
    
    for key in gradeBook.keys():
        exam1Lst.append(gradeBook[key]['exam1'])
        exam2Lst.append(gradeBook[key]['exam2'])
        count += 1
    exam1Lst.sort()
    exam2Lst.sort()
    exam1OfAve = round(sum(exam1Lst)/count ,2)
    exam2OfAve = round(sum(exam2Lst)/count ,2)
    medianOfExam1 = exam1Lst[int(count/2)]
    medianOfExam2 = exam2Lst[int(count/2)]
    rangeExam1 = exam1Lst[count-1]-exam1Lst[0]
    rangeExam2 = exam2Lst[count-1]-exam2Lst[0]
    exstat = {'exam1':{'average':exam1OfAve, 'median':medianOfExam1, 'range':rangeExam1},'exam2':{'average':exam2OfAve, 'median':medianOfExam2, 'range':rangeExam2}}
    return exstat
    

def finalExamGrade(student):
    letterGradeScale = {'A': 90, 'B+': 85, 'B':80, 'C+': 75, 'C': 70, 'D': 65}
    needOfFinal = {}
    for SID in student.keys():
        stuGrade = (student[SID]['exam1']+student[SID]['pta'])*0.2 + student[SID]['exam2']*0.2 + student[SID]['homework']*0.1 + student[SID]['attendance']*0.04 + student[SID]['project1']*0.05 + student[SID]['project2']*0.05 + student[SID]['classrecap']*0.06
        if (letterGradeScale['A']-stuGrade)/0.3 <= 100:
            A = round((letterGradeScale['A']-stuGrade)/0.3, 2)
        else:
            A = 'N/A'
        if (letterGradeScale['B+']-stuGrade)/0.3 <= 100:
            Bp = round((letterGradeScale['B+']-stuGrade)/0.3, 2)
        else:
            Bp = 'N/A'
        if (letterGradeScale['B']-stuGrade)/0.3 <= 100:
            B = round((letterGradeScale['B']-stuGrade)/0.3, 2)
        else:
            B = 'N/A'
        if (letterGradeScale['C+']-stuGrade)/0.3 <= 100:
            Cp = round((letterGradeScale['C+']-stuGrade)/0.3, 2)
        else:
            Cp = 'N/A'
        if (letterGradeScale['C']-stuGrade)/0.3 <= 100:
            C = round((letterGradeScale['C']-stuGrade)/0.3, 2)
        else:
            C = 'N/A'
        if (letterGradeScale['D']-stuGrade)/0.3 <= 100:
            D = round((letterGradeScale['D']-stuGrade)/0.3, 2)
        else:
            D = 'N/A'
        needOfFinalSub = {'A':A,'B+':Bp,'B':B,'C+':Cp,'C':C,'D':D}
        needOfFinal[SID] = needOfFinalSub
    return needOfFinal

finalP = finalExamGrade(examResults)
print(finalP)
def generateReport(gradeBook, student):
    fileOut = open('FinalGrade.txt','w')
    for SID in student.keys():
        if (gradeBook[SID]['exam1']+gradeBook[SID]['pta'])*0.2 + gradeBook[SID]['exam2']*0.2 + gradeBook[SID]['homework']*0.1 + gradeBook[SID]['attendance']*0.04 + gradeBook[SID]['project1']*0.05 + gradeBook[SID]['project2']*0.05 + gradeBook[SID]['classrecap']*0.06 >= 60:
            fileOut.write(SID, '\t', gradeBook[SID]['exam1'], '\t', gradeBook[SID]['exam2'], '\t', gradeBook[SID]['homework'], '\t', gradeBook[SID]['attendance'], '\t', gradeBook[SID]['project1'], '\t', gradeBook[SID]['project2'], '\t', gradeBook[SID]['classrecap'], '\n', student[SID]['A'], '\t', 'A')
        elif (gradeBook[SID]['exam1']+gradeBook[SID]['pta'])*0.2 + gradeBook[SID]['exam2']*0.2 + gradeBook[SID]['homework']*0.1 + gradeBook[SID]['attendance']*0.04 + gradeBook[SID]['project1']*0.05 + gradeBook[SID]['project2']*0.05 + gradeBook[SID]['classrecap']*0.06 >= 55:
            fileOut.write(SID, '\t', gradeBook[SID]['exam1'], '\t', gradeBook[SID]['exam2'], '\t', gradeBook[SID]['homework'], '\t', gradeBook[SID]['attendance'], '\t', gradeBook[SID]['project1'], '\t', gradeBook[SID]['project2'], '\t', gradeBook[SID]['classrecap'], '\n', student[SID]['B+'], '\t', 'B+')
generateReport(examResults, finalP)

def enrollment_stats(universites):
    student_enrolled = []
    tuition_fee = []
    for university in universites:
        student_enrolled.append(university[1])
        tuition_fee.append(university[2])
    return student_enrolled, tuition_fee

def mean(list_for_mean):
    total = 0
    for i in list_for_mean:
        total = total + i
    mean_value = total/len(list_for_mean)
    return mean_value,total

def median(list_for_median):
    for i in list_for_median:
        list_for_median.sort()
        list_for_median_len = len(list_for_median)
        if ( list_for_median_len % 2 == 0 ):
            median_value = (list_for_median[list_for_median_len/2] + list_for_median[list_for_median_len/2 - 1])/2
        else:
            median_value = list_for_median[list_for_median_len/2]
    return median_value
universites = [['CaliforniaInstituteofTechnology',2175,37704],['Harvard',19627,39849],['MassachusettsInstituteofTechnology',10566,40732],['Princeton',7802,37000],['Rice',5879,35551],['Stanford',19535,40569],['Yale',11701,40500]]

student_enrolled,tuition_fee = enrollment_stats(universites)
student_mean, total_student = mean(student_enrolled)
student_median = median(student_enrolled)
tuition_mean, total_fee = mean(tuition_fee)
tuition_median = median(tuition_fee)

print ("******************************************")
print ("Total students: {}".format(total_student))
print ("Total tuition: ${}".format(total_fee))
print ("Student mean:   {}".format(student_mean))
print ("Student median: {}".format(student_median))
print ("Tuition mean:  ${}".format(tuition_mean))
print ("Tuition median:${}".format(tuition_median))
print ("******************************************")


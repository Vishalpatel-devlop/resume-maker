from django.db import models

class get_data1(models.Model): #here we getting data from form we created.
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    linkedin=models.CharField(max_length=100) # we null and blank this when we add new field. also because there is already existing data in other fields.
    location=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)  
    objective=models.CharField(max_length=254)


class get_data2(models.Model): #here we getting data from html form we created.
    hard_skill=models.CharField(max_length=100)
    soft_skill=models.CharField(max_length=100)
    person_id = models.ForeignKey(get_data1, on_delete=models.CASCADE, related_name="skill")

   
class get_data3(models.Model): #here we getting data from html form we created.
    degree_name=models.CharField(max_length=100)
    inst_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    g_date=models.DateField(max_length=100)
    person_id = models.ForeignKey(get_data1, on_delete=models.CASCADE, related_name="graduated")

class get_data4(models.Model): #here we getting data from form we created.
    job_title=models.CharField(max_length=100)
    comp_name=models.CharField(max_length=100)
    achievement=models.CharField(max_length=100)
    doj=models.DateField(max_length=100)
    dol=models.DateField(max_length=100)
    person_id = models.ForeignKey(get_data1, on_delete=models.CASCADE, related_name="experience")
   
class get_data5(models.Model): #here we getting data from form we created.
    projects=models.CharField(max_length=100)
    certificate=models.CharField(max_length=100)
    hobby=models.CharField(max_length=100)
    ability=models.CharField(max_length=100)
    achievements=models.CharField(max_length=100, null=True,blank=True)
    img=models.ImageField(upload_to='uploads/',max_length=254, null=True,blank=True)
    person_id = models.ForeignKey(get_data1, on_delete=models.CASCADE, related_name="other_info")

class get_data6(models.Model): #here we getting data from form we created.
    school=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    percent_10=models.CharField(max_length=100)
    percent_12=models.CharField(max_length=100)
    person_id = models.ForeignKey(get_data1, on_delete=models.CASCADE, related_name="undergraduation")
  

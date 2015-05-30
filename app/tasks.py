from celeryconfig import celery1

@celery1.task
def add_together_pawan(a, b):    
	print "############5555555555555555555"
	c = str(a+b)    

	return c

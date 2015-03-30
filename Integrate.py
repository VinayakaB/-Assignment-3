>>> class Integrate():

	def Trapezoidal(a,b,n,fn):                    
		sol=fn(a)
		for i in range(1,n):
			sol=sol+2*fn(a+(i*(b-a))/n)
		sol=sol+fn(b)
		sol=(sol*(b-a))/(2*n)                    
		return sol                                
	def Simpson(a,b,n,fn):                       
		sol=fn(a)
		for i in range(1,n,2):
			sol=sol+ 4*fn(a+(i*(b-a))/n)
		for i in range(2,n,2):
			sol=sol+ 2*fn(a+(i*(b-a))/n)
		sol=sol+fn(b)
		sol=(sol*(b-a))/(3*n)                     
		return sol                                
	def solve(self,a,b,n,fn,method):                  
		if(method=='trapezoid'):
			sol=Trapezoidal(a,b,n,fn)
			return sol
		if(method=='simpson'):
			sol=Simpson(a,b,n,fn)
			return sol
      
        def plot(self,a,b,n,fn):
		import matplotlib.pyplot as pt                #import plotting library
		from numpy import arange
		x=[i for i in arange(a,b,(b-a)/(n*1000.0))]    #list of values between a and b
		x=x+[b]                                        
		y=[i for i in arange(a,b,(b-a)/(n*1.0))]       #list of values of x
		y=y+[b]                                      
		z=[fn(i) for i in x]                           #list of function values
		pt.plot(x,z)                                  #plotting the curve
		for i in range(n+1):
			pt.plot([y[i],y[i]],[0,fn(y[i])])             #parallel sides of the trapezium
		for i in range(n):
			pt.plot([y[i],y[i+1]],[fn(y[i]),fn(y[i+1])])  #non-parallel sides of trapezium
		pt.show()	                                       #output
 



#Initial Example:
>>> f=lambda x:x*x			
>>> igr=Integrate()
>>> for method in ['trapezoid','simpson']:
	solution=igr.solve(1,6,100,f,method)
	print(solution)

	
71.66875
71.66666666666666

#New Example:
>>> f=lambda: x:x*x*x
>>> igr=Integrate()
>>> a,b,n=2,7,15
>>> igr.plot(a,b,n,f)
#Different trapezoid regions can be clearly distinguished

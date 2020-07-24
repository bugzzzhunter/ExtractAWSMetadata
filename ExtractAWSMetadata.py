import requests,os

latest=[]
url='http://169.254.169.254/latest/'

def fetchLatest(url):
	x = requests.get(url)
	#print(x.text)
	dir=url.split('/')[-2]
	latest=x.text.split('\n')
	if not os.path.exists('latest'):
		os.mkdir('latest')
	os.chdir('latest')
	curr=os.getcwd()
	for i in latest:
		os.chdir(curr)
		if not os.path.exists(i) and i!='user-data':
			os.mkdir(i)
			os.chdir(i)
		fetch(url+i+'/')


def fetch(url):
	print('-'*30)
	print('Fetching url: '+url)
	print('-'*30)
	x = requests.get(url)
	#print('URL Split:'+str(url.split('/')))
	if url.split('/')[-2]=='user-data':
		#print('-'*30)
		#print('Creating File: user-data')
		#print('-'*30)
		f=open(url.split('/')[-2],'w')
		f.write(x.text)
		f.close()
	else:
		#print('URL is: '+x.text)
		outData=x.text.split('\n')
		#print('outdata is: '+str(outData))
		curr2=os.getcwd()
		for i in outData:
			if i and i[-1]=='/':
				os.chdir(curr2)
				#print('-'*30)
				#print('Creating Directory: '+i)
				#print('-'*30)
				if not os.path.exists(i) and i!='user-data':
					os.mkdir(i)
					os.chdir(i)
				#print('Calling url: '+url+i)
				fetch(url+i)
			elif i!='':
				os.chdir(curr2)
				#print('-'*30)
				#print('Creating File: '+i)
				#print('-'*30)
				print('-'*30)
				print('Fetching url: '+url)
				print('-'*30)
				y = requests.get(url+i)
				f=open(i,'w')
				f.write(y.text)
				f.close()



def main():
	fetchLatest(url)

if __name__=='__main__':
	main()

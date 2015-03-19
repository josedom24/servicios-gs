#!/usr/bin/python
import commands,os
layout_prefix='''
---
layout: index
---
'''
branch = commands.getoutput("git rev-parse --abbrev-ref HEAD")
if branch=="master":
	ficheros=commands.getoutput("git show --name-only|grep md")
	lista_fich=ficheros.split("\n")
	#os.system("git checkout gh-pages")
	os.system("git checkout gh-pages")
	for fich in lista_fich:
		
		os.system("git checkout master -- %s" % fich)
		if fich=="README.md":
			fich="index.md"
		os.system("echo '%s'>%s"%(layout_prefix,fich+".tmp"))
		os.system("cat %s>>%s"%(fich,fich+".tmp"))
		os.system("cat %s>>%s"%(fich+".tmp",fich))
		os.system("rm %s"%fich+".tmp")
		print "Sync %s de master a gh-pages" % fich
		os.system('git commit -am "Sync %s de master a gh-pages"' % fich)
	os.system("git checkout master")
else:
	print "Debes estar en la rama master"
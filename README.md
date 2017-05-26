UvaTools
======
My own [uhunt api](http://uhunt.felix-halim.net/api) Encapsulation on python3
## Installing
---
```
git clone https://github.com/sd12582000/UvaTools.git  
cd UvaTools 
pip install .
```
## Example UvaProblems
---
```
import UvaTools
problemDics = UvaTools.UvaProblems()
problemDics.get_title('100') #return The 3n + 1 problem

#Make dir  
problemDics.creat_problem_dir('root','100')#mkdir 'root/volume001\100-The 3n + 1 problem'
```
## Example UvaUser
---
```
import UvaTools
user_sumbit = UvaTools.UvaUser('sd12582000')
user_sumbit.is_acept('100') #return True
```
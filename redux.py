import os

fpath=input('Please give me the folder path: ')
prefix=input("please give me the name of new reducer: ")
redux_path=fpath+'\\'+prefix
op="{"
cl="}"
real_name=None
os.mkdir(redux_path)

with open(redux_path+"\\"+prefix+".types.js","w") as fp:
  real_name=prefix.split('.')[0].capitalize()+"ActionTypes"
  fp.writelines('\n'.join([f"const {real_name} = {op}",cl,
                 f"export default {real_name}"]))
with open(redux_path+"\\"+prefix+".action.js","w") as fp:
  fp.writelines('\n'.join([f"import {real_name} from './{prefix}.types'"]))
with open(redux_path+"\\"+prefix+".reducer.jsx","w") as fp:
  fp.writelines('\n'.join([f"import {real_name} from './{prefix}.types'",
                 f'const INITIAL_STATE = {op}{cl};',
                 f"const {prefix}Reducer = (state = INITIAL_STATE, action) => {op}",
                 f"switch (action.type) {op}",
                 f"case {real_name}. :",
                 f"return {op}",
                 f"...state {cl}",
                 f"default : return state",
                 f"{cl}{cl}",
                 f"export default {prefix}Reducer;"]))




if input("type y/n based on having file named root-reducer.js: ")=="n":
  with open(fpath+"\\"+"root-reducer.js","w") as fp:
    fp.writelines('\n'.join(["import { combineReducers } from 'redux';",
                             "export default combineReducers({",'});']))
    
if input("type y/n based on having file named store.js: ")=="n":
  with open(fpath+"\\"+"store.js","w") as fp:
    fp.writelines(open('store.txt',"r").readlines())


with open(fpath+"\\"+"root-reducer.js", "r") as f:
    contents = f.readlines()
contents.insert(1,f"import {prefix}Reducer from './{prefix}/{prefix}.reducer';\n")
contents.insert(-1,f"{prefix}:{prefix}Reducer,\n")

with open(fpath+"\\"+"root-reducer.js","w") as fp:
  fp.writelines(contents)

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:27:35 2021

@author: yidee
"""
import re

import os

#song_playlist的資料夾目錄清單
path ='D:\\music\\song_playlist'
folder_name_list=os.listdir(path)


#分別進入各個資料夾
for folder_name in folder_name_list:
    
    #進入目錄的第一層
    name = os.path.join(path,folder_name)
    
    #第二層目錄清單
    folder_folder_list = os.listdir(name)
    
    #分別進入第二層資料夾
    for folder_folder_name in folder_folder_list:
        
        #進入第三層資料夾
        name1 = os.path.join(name,folder_folder_name)
        
        #偵測是否需要進入第三層
        if os.path.isfile(name1)==0:
            
            #進入資料夾直到變成檔案
            while os.path.isfile(name1)==0:
                
                #初始化name_fold給後面退出都是檔案的資料夾方便
                name_fold=name1
                
                #初始化list成第三層資料夾內容
                list = os.listdir(name1)
                
                #print資料夾內的音樂
                print(list)
                
                #如果第三層不是檔案，進入下一層
                if list != []:
                    name1 = os.path.join(name1,list[0])
                else:
                    break
                
                #print('888'+name1)
            #顯示包含檔案的資料夾
            print('最終資料夾 :'+name_fold)
            
        
        #進入第二層就是包含音樂的資料夾
        else:
            
            name_fold =os.path.abspath(os.path.dirname(name1))
            print("不用進入"+name_fold)
        '''
        #正則表達式找出'MYFREEMP3.VIP'
        regex = re.compile(r'(.*)+(myfreemp3.vip)')
        check_name = os.path.join(name_fold,folder_folder_name)
        check = regex.search(check_name)
        
        
        #當regex配上時，寫入en_str,停止
        if check != None:
            print(check.group(1))
                      #os.rename(os.path.join(name_fold,folder_folder_name),os.path.join(name_fold,check.group(1)))
            
        else:
            print(folder_folder_name)
        '''
# 软件使用说明书

### 1.首先运行 `gen_nums.py`

> gen_nums.py 在Temp文件夹下<br>
> 根据自己的需求，将n个顺序排列的cid号存储到txt中，然后把生成的temp.txt去[https://pubchem.ncbi.nlm.nih.gov/](https://pubchem.ncbi.nlm.nih.gov/)
> ,点击Upload ID List...
> <br>`记得清空txt的内容，或者新建txt文件`<br>
> `cid号并不是所有都有，例如10。`

### 2.转化mol文件

> 程序为 `pubchem_code.py`
> 输入csv路径<br>
> `path_name = '1_1k.csv'`<br>
> 输入sdf路径<br>
> `sdf_path = '1_1k.sdf'`<br>
> 将csv转化为excel<br>
> ` ConvertToExcel(path_name=path_name)`<br>
>
> 默认存储在ALL_Mol文件夹下，若想要自定义路径，请看注释详细说明，可以搜索"自定义路径"找到入口<br>
> 这个是保存你想要存储转化好的mol文件存储文件夹的名字<br>
> `filename = '1_1k'`<br>
>
> `fail_sdf.log 仅仅只会记录转化失败的`<br>

> 补充（选看）
> > 首次运行时候，需要先处理csv为excel，因为csv文件存在一部分问题。
> > > `path_name='1.csv'` 写入你的csv路径，默认是在当前文件夹下，如果在别的地方，记得写绝对路径，注意使用 '/',详情见代码页面（注释部分），会将csv文件转化为同名的xxx.xlsx。<br>
> > > `turn_flag=True` 默认开启，代表把cas存储到excel中，如果是第二次运行，则设置 turn_flag=False <br>
> > > 修改这段代码(turn_flag=False) `temp_data = get_cas_list(excel_path=r'{excel_path_f}'.format(excel_path_f=excel_path_f),turn_flag=False)`

### 3.更改cid图片为cas命名 `Rename_Pic.py`
> 读取excel的地址，会根据里面的cid去命名图片<br>
> read_path = '1_1w.xlsx<br>
> 图片所在文件夹，注意格式的书写<br>
> filePath = 'D:\\test'`
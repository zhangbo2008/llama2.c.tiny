import subprocess
string='runq.exe out\model.bin -t 0.8 -n 256 -z D:\\data_llama\\tok2048.bin -i "asdf"'
result=subprocess.getoutput(string)
print("result::: ",result)
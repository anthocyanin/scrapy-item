from os.path import realpath, dirname
import json


def get_config(name):
    # realpath(__file__) 这是什么意思呢？
    # 经查询是得到当前文件所在目录的意思，这里也就是scrapyuniversal
    # 下面是代码就是构造出scrapyuniversal/congfigs/name.json，这个文件路径然后赋值给path
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

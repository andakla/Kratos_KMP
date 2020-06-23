import json
from jsonpath_ng import jsonpath, parse

def compare_json(self, json_src, json_des):
    str_src = json.dumps(json_src, sort_keys=True)
    with open(json_des) as f:
        js_data = json.load(f)
    str_des = json.dumps(js_data, sort_keys=True)
    return (str_src==str_des)

# def compare_json_by_node_path(self, json_src, path):
#     lst_value =refix_path(path)
#     jsonpath_expression = parse(lst_value[0])
#     for match in jsonpath_expression.find(json_src):
#         if match.value == lst_value[1]:
#             return True
#     return False

def refix_path(self,path):
    list_arg=path.split(":")
    return list_arg
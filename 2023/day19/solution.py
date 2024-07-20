import re

###### define input and make workflows and parts
def make_workflows_parts(input_file):
    with open(input_file, 'r') as f:
        two = f.read().split("\n\n")
    
    raw_workflows, raw_parts = two[0], two[1]

    workflows = raw_workflows.split('\n')
    dict_workflows = {}
    for wf in workflows:
        name_wf = re.match(r'^[A-Za-z]+', wf).group(0)
        steps = wf.replace(name_wf, "")[1:-1].split(",")
        condition = []
        next_step = []

        for step in steps:
            step = step.split(':')
            if len(step) != 1:
                condition.append(step[0])
                next_step.append(step[1])
            else:
                condition.append(step[0])
                next_step.append(step[0])

        dict_workflows[name_wf] = {"condition": condition, "next_step": next_step}


    parts = [x[1:-1].split(',') for x in raw_parts.split('\n')]
    list_list_parts = [tuple(int(ele.split('=')[1]) for ele in part) for part in parts]

    return dict_workflows, list_list_parts


dict_workflows, list_list_parts = make_workflows_parts("2023/day19/input.in")


######## check example 1

x, m, a, s = list_list_parts[2]

cur_workflow_name = "in"

while cur_workflow_name not in ["A", "R"]:

    cur_workflow = dict_workflows.get(cur_workflow_name)

    # print(cur_workflow_name, cur_workflow)

    for idx, condition in enumerate(cur_workflow['condition']):
        if not re.findall(r"\d+", condition):
            cur_workflow_name = condition
        else:
            if eval(condition):
                if condition in ["A", "R"]:
                    # print(condition)
                    break
                else:
                    cur_workflow_name = cur_workflow['next_step'][idx]
                    break

    # print("after:", cur_workflow_name)

########################### 

def find_acceptance(part):

    x, m, a, s = part

    cur_workflow_name = "in"

    while cur_workflow_name not in ["A", "R"]:

        cur_workflow = dict_workflows.get(cur_workflow_name)

        for idx, condition in enumerate(cur_workflow["condition"]):
            if not re.findall(r"\d+", condition):
                cur_workflow_name = condition
                break
            else: 
                if eval(condition):
                    if condition in ["A", "R"]:
                        break
                    else:
                        cur_workflow_name = cur_workflow['next_step'][idx]
                        break

    return cur_workflow_name


##########################

s = 0

for part in list_list_parts:
    
    if find_acceptance(part) == "A":

        s += sum(part)

# part 1: 325952
# part 2 is tough (LATER)

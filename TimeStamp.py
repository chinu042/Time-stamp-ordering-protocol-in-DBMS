class T:
    def __init__(self, name, time):
        self.name = name
        self.time = time


class parameter:
    def __init__(self, name):
        self.name = name
        self.w_time = 0
        self.r_time = 0


def preprocessing(s):
    s = "".join(s.split())
    if s[:2] != 'st':
        print("Transaction should start with st. Like this: st1; st2; r2(A);w1(B);w2(B)")
        exit()
    if s.find(';') == -1:
        print("You should have ';' between each section. Like this: st1; st2; r2(A);w1(B);w2(B)")
        exit()
    return s


def next_one(s):
    if not s:
        print("No transactions left")
        return None, None
    if s.find(';') == -1:
        next_item = s
        leftover_string = None
    else:
        next_item = s[:string.find(';')]
        leftover_string = s[string.find(';') + 1:]
    return next_item, leftover_string


def trans(s):
    for i in set_of_trans:
        if i.name == s:
            return i
    return None


def params(s):
    for i in set_of_parameters:
        if i.name == s:
            return i
    return None


def print_set_of_parameters(set_of_parameters):
    S = sum(1 for num in set_of_parameters)
    if S > 0:
        print("\nset_of_parameters: ")
        for x in set_of_parameters:

            print(x.name + " W:" + str(x.w_time) + " R:" + str(x.r_time))

    else:
        return None


if __name__ == '__main__':

    string = preprocessing(str(input()))

    global set_of_trans, set_of_vars, time
    set_of_trans = set()
    set_of_parameters = set()
    time = 1

    while (string):
        print_set_of_parameters(set_of_parameters)
        next_item, string = next_one(string)
        print("\nCommand: " + str(next_item) +
              ". Remaining commands:" + str(string))

        if next_item[:2] == 'st':
            id = "T" + next_item[2]
            if not trans(id):
                set_of_trans.add(T(id, time))
                time += 1
                print("Added " + id + " to set_of_transaction")
            else:
                print("Transaction " + id + " exists in set_of_transaction ")

        elif next_item[:1] == 'r':
            p = next_item[next_item.find('(') + 1:next_item.find(')')]
            t_no = next_item[1:2]
            T_i = trans('T' + t_no)
            if not T_i:
                print("Error: Transaction " + 'T' + t_no + " does not exist")
                exit()
            else:
                if not params(p):
                    var = parameter(p)
                    set_of_parameters.add(var)
                    var.r_time = T_i.time
                    print("Execute " + next_item + ". New parameter " + var.name + " added. Read time set to " + str(
                        var.r_time))
                else:
                    var = params(p)
                    if (var.w_time > T_i.time):
                        print(
                            "Read time of " + var.name + " >= " + T_i.name + " time. Reject " + next_item + " and roll back " + T_i.name)
                        exit()
                    else:
                        print("Execute  " + next_item)
                        o = var.r_time
                        var.r_time = max(var.r_time, T_i.time)
                        print("Read time of " + var.name + " changed from " +
                              str(o) + " to " + str(var.r_time))

        elif next_item[:1] == 'w':
            p = next_item[next_item.find('(') + 1:next_item.find(')')]
            t_no = next_item[1:2]
            T_i = trans('T' + t_no)
            if not T_i:
                print("Error: Transaction " + 'T' + t_no + " does not exist")
                exit()
            else:
                if not params(p):
                    var = parameter(p)
                    set_of_parameters.add(var)
                    var.w_time = T_i.time
                    print("Execute " + next_item + ". New parameter " + var.name + " added. Write time set to " + str(
                        var.w_time))
                else:
                    var = params(p)
                    if (var.r_time > T_i.time):
                        print(
                            "Read time of " + var.name + " > " + T_i.name + " time. Reject " + next_item + " and roll back " + T_i.name)
                        exit()
                    elif (var.w_time > T_i.time):
                        print("Ignore " + next_item +
                              " by Thomas write rule. Trans:" + T_i.name)

                    else:
                        print("Execute " + next_item + " in " + T_i.name)
                        o = var.w_time
                        var.w_time = T_i.time
                        print("Write time of " + var.name +
                              " changed from " + str(o) + " to " + str(var.w_time))

        else:
            print("Command ignored")
            pass

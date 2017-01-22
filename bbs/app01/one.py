d = {1: {2: {3: {4: {}}}, 20: {30: {}}}, 11: {21: {}}}
def Ldd():
    bbs = Bbs.objects.get(pk=1)
    comment = bbs.comment_set.all()
    dic = {}
    for i in comment:
        if i.ladder_comment == None:
            dic[i] = {}

    for i in comment:
        for j,k in dic.items():
            if i.ladder_comment == j:
                k[i] = {}
                if i.l_comment.all() == []:
                    continue
            else:
                return Ladder(k,dic)

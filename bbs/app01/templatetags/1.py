@register.simple_tag
def Comment_tree(ladder):
    l = ["<div>"]
    def Split(n,x,y):
        item = x.items()
        ite = sorted(item,key=lambda x:x[0].c_date)
        print ite
        for i,j in ite:
            m = ite.index((i,j))
            n = n + 40 - 40*m
            s1 = '''<div class="hello" style="margin-left:%spx">
                            <ul>
                                <li>%s</li>
                                <li>%s</li>
                                <li>%s</li>
                            </ul>
                    </div>'''%(n,i.author.name,i.comment,i.c_date)
            y[0] = y[0] + s1
            if j != {}:
                Split(n,j,y)

        return y
    if ladder != {}:
        item = ladder.items()
        ite = sorted(item,key=lambda x:x[0].c_date)
        for i,j in ite:
            n = 20
            s1 = '''<div class="hello" style="margin-left:%spx">
                        <ul>
                            <li>%s</li>
                            <li>%s</li>
                            <li>%s</li>
                        </ul>
                    </div>'''%(n,i.author.name,i.comment,i.c_date)
            l[0] = l[0] + s1
            if j != {}:
                Split(n,j,l)
            else:
                continue
    else:
        return None
    return l[0]+'</div>'
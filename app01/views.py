from django.shortcuts import render

# Create your views here.


def test(request):
    name="ADKJFALGH'kkcSJksFGkjfdkfj#$$!@%"
    return render(request, 'test.html', {'name': name})


LIST = []
for i in range(1, 138):
    LIST.append(i)


from django.utils.safestring import mark_safe


def lst(request):
    pg = request.GET.get('pg', 3)
    current_pg = int(pg)
    start = (current_pg-1)*10
    end = current_pg*10
    li = LIST[start: end]
    cou_num = len(LIST)
    count, remainder = divmod(cou_num, 10)
    if remainder: # 如果有余数，代表不是整除，总页数+1
        count += 1
    page_list = []
    # range(count) 0-count   从1开始数 count也需要+1
    for i in range(1, count+1):
        if i == current_pg: # 如果i=当前页，然后加上class = active样式 active样式为点击后加底色
            temp = """<a class="page active" href="/app01/page/?pg=%s">%s</a>""" %(i, i)
        else: # 否则正常显示
            temp = """<a class="page" href="/app01/page/?pg=%s">%s</a>""" % (i, i)
        page_list.append(temp)
    pg_str = "".join(page_list)
    pg_str = mark_safe(pg_str)
    return render(request, 'list.html', {'list': li, 'pg_num': pg_str})
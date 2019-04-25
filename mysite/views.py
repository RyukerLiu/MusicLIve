from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request, tvno = 0):
    tv_list = [{'name':'Good Live', 'tvcode':'taD9hqwCb1o'},
            {'name':'Rainy Jazz', 'tvcode':'DSGyEsJ17cI'},
            {'name':'lofi hip hop', 'tvcode':'hHW1oY26kxQ'},
            {'name':'Calm Piano', 'tvcode':'XULUBg_ZcAU'},]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())

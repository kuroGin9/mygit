# -*- coding: utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port='3306', user='root', password='shaonian.0', db='awesome')
    u = User(name='qianqian', email='qian@163.com', password='1111', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

beanstalkc
==========

py3beanstalk 是 beanstalkd 的一个 python3 客户端库. 
[beanstalkd][] 是一个高速,分布式,内存级的消息队列服务
py3beanstalk 依赖于 [PyYAML][]，但可以避免依赖，请参阅附录A.
beanstalkc 是纯Python，与 [eventlet][] 和 [gevent][] 兼容。
py3beanstalk 是基于 [beanstalkc][] 的修改版, 仅支持 python3

py3beanstalk 已经测试过, 再次执行
python3 py3beanstalk.py
执行前, 请启动全新的 beanstalkd 

鸟语实在太难学, 只能用的中文了, 请见谅!

[beanstalkd]: http://kr.github.com/beanstalkd/
[eventlet]: http://eventlet.net/
[gevent]: http://www.gevent.org/
[PyYAML]: http://pyyaml.org/
[beanstalkc]: http://github.com/earl/beanstalkc


Usage
-----

Here is a short example, to illustrate the flavor of beanstalkc:

    >>> import py3beanstalk
    >>> beanstalk = py3beanstalk.Connection(host='localhost', port=11300)
    >>> beanstalk.put(b'ni hao !')
    1
    >>> job = beanstalk.reserve()
    >>> job.body
    b'ni hao !'
    >>> job.delete()

For more information, see [the tutorial](TUTORIAL.mkd), which will explain most
everything.


License
-------

Copyright (C) 2008-2016 Andreas Bolka, Licensed under the [Apache License,
Version 2.0][license].

[license]: http://www.apache.org/licenses/LICENSE-2.0

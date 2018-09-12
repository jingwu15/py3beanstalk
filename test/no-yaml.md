Regression tests for YAMLless operation
=======================================

Job priorities are not preserved
--------------------------------

Setup a connection that won't parse YAML:

    >>> import beanstalkc3
    >>> beanstalk = beanstalkc3.Connection(host='localhost', port=11300,
    ...                                   parse_yaml=False)

Observe that YAML is not parsed:

    >>> not isinstance(beanstalk.stats(), dict)
    b'OK' [b'913']
    True

Note that while Job#release and Job#bury will still work, they won't
automatically maintain the released/buried Job's priority:

    >>> jid = beanstalk.put(b'foo', priority=42)
    b'INSERTED' [b'13']

    >>> job = beanstalk.reserve()
    b'RESERVED' [b'13', b'3']
    >>> print(repr(job.stats()))                    # doctest: +ELLIPSIS
    b'OK' [b'152']
    b'...pri: 42...'

    >>> job.release()               # Succeeds, but ...
    b'OK' [b'152']
    b'RELEASED' []

    >>> job = beanstalk.reserve()   # ... may not do what you want.
    b'RESERVED' [b'13', b'3']
    >>> print(repr(job.stats()))                    # doctest: +ELLIPSIS
    b'OK' [b'160']
    b'...pri: 2147483648...'

    >>> job.delete()
    b'DELETED' []

Same for Job#bury:

    >>> jid = beanstalk.put(b'bar', priority=42)
    b'INSERTED' [b'14']

    >>> job = beanstalk.reserve()
    b'RESERVED' [b'14', b'3']
    >>> print(repr(job.stats()))                    # doctest: +ELLIPSIS
    b'OK' [b'152']
    b'...pri: 42...'

    >>> job.bury()
    b'OK' [b'152']
    b'BURIED' []

    >>> print(repr(beanstalk.stats_job(jid)))       # doctest: +ELLIPSIS
    b'OK' [b'156']
    b'...pri: 2147483648...'

And that was that.

    >>> beanstalk.close()
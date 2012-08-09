from crash_hound import CrashHound, ReportCrash, CommonChecks, SenderQiyi

def check_fn():
    if 42:
        raise ReportCrash('42 is true!')
    else:
        pass #Ignore


crash_sender = SenderQiyi("18600761080")

crash_checker = CrashHound(crash_sender)

crash_checker.register_check('42 Checker',
                             check_fn,
                             notify_every=60)

crash_checker.register_check('Google.com Blah test',
                             lambda: CommonChecks.website_check('http://google.com'),
                             notify_every=60)

crash_checker.run_checks(check_interval=10)

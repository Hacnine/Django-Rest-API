from rest_framework.throttling import *


class JackRateThrottle(UserRateThrottle):
    scope = 'jack'



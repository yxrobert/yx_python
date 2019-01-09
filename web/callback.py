# _*_ coding: utf-8 _*_
class CallbackBase:
    def __init__(self):

        self.__callbackMap = {}
        for k in (getattr(self, x) for x in dir(self)):
            if hasattr(k, "bind_to_event"):
                self.__callbackMap.setdefault(k.bind_to_event, []).append(k)
            elif hasattr(k, "bind_to_event_list"):
                for j in k.bind_to_event_list:
                    self.__callbackMap.setdefault(j, []).append(k)

    @staticmethod
    def callback(event):
        def f(g, ev=event):
            g.bind_to_event = ev
            return g

        return f

    @staticmethod
    def callbacklist(eventlist):
        def f(g, evl=eventlist):
            g.bind_to_event_list = evl
            return g

        return f

    def dispatch(self, event):

        l = self.__callbackMap[event]

        # def f(*args, **kargs):
        #     return map(lambda x: x(*args, **kargs), l)

        # lambda x: x(*args, **kargs)
        # def k(x):
        #     return k(*args, **kargs)
        # ff =

        f = lambda *args, **kargs: map(lambda x: x(*args, **kargs), l)
        # print type(f)
        # print f
        return f


class MyClass(CallbackBase):
    EVENT1 = 1
    EVENT2 = 2

    @CallbackBase.callback(EVENT1)
    def handler1(self, param1, param2):
        print("handler1 with param: %s %s" % (str(param1), str(param2)))
        return None

    @CallbackBase.callbacklist([EVENT1, EVENT2])
    def handler2(self, param1=None, param2=None):
        print("handler2 with param: %s" % str(param1))
        return None

    def run(self, event, param1=None, param2=None):
        self.dispatch(event)(param1, param2)


if __name__ == "__main__":
    a = MyClass()
    # a.run(MyClass.EVENT1, 'mandarina')
    a.run(MyClass.EVENT1, 'naranja', 'xxx')

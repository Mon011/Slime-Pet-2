class EventManager:
    def __init__(self):
        self.callbacks = {}
    
    def register_event(self, event_name, callback):
        if event_name not in self.callbacks:
            self.callbacks[event_name] = []
        self.callbacks[event_name].append(callback)
        print(self.callbacks)
    
    def trigger_event(self, event_name, *args, **kwargs):
        print("event_name:", event_name)
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                print("Callback called: ", callback)
                callback(*args, **kwargs)

                
class Manager():
    def __init__(self, _class = None):
        self._class = _class
        
    def __str__(self):
        return f"{self._class}"
    
    def search(self, **kwargs):
        results = list()
        for key, value in kwargs.items():
                    if key.endswith("__min"):
                        key = key[:-5] #removes the last five character from the key(__min)
                        compare_key = "min"
                    elif key.endswith("__max"):
                        key = key[:-5]  #removes the last five character from the key(__max)
                        compare_key = "max"
                    else:
                        compare_key = "eqaul"
                                       
                    if results:
                        self._class.object_list.clear()
                        for obj in results:
                            self._class.object_list.append(obj)
                        results.clear()
                    for obj in self._class.object_list:
                        if hasattr(obj, key): #checks if the key exists like price_per_meter
                            if compare_key == "max":
                                result = bool(getattr(obj, key) <= value)
                            elif compare_key == "min":
                                result = bool(getattr(obj, key) >= value)
                            else:
                                result = bool(getattr(obj, key) == value)

                            if result:
                                results.append(obj)
        return results                      


    def get(self, **kwargs):
        for key, value in kwargs.items():
                    if key.endswith("__min"):
                        key = key[:-5] #removes the last five character from the key(__min)
                        compare_key = "min"
                    elif key.endswith("__max"):
                        key = key[:-5]  #removes the last five character from the key(__max)
                        compare_key = "max"
                    else:
                        compare_key = "equal"

                    for obj in self._class.object_list:
                         if hasattr(obj, key): #checks if the key exists like price_per_meter
                            if compare_key == "max":
                                result = bool(getattr(obj, key) <= value)
                            elif compare_key == "min":
                                result = bool(getattr(obj, key) >= value)
                            else:
                                result = bool(getattr(obj, key) == value)

                            if result:
                                return (obj)
        return None
    
    def count(self):
         return len(self._class.object_list)
        
                                        
                              
                              
         



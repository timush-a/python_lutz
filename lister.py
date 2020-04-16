class ListInsstance:
    """
    Mix-in class;
    Displays instance atrrs only;
    Self is instance of lowest class;
    __X names avoid clashing with client's attrs
    """

    def __str__(self):
        return f"""Instance of {self.__class__.__name__},
        adress:{id.self}, \n{self.__attrnames()}"""
        
    def __attrnames(self):
        result = ""
        for attr in sorted(self.__dict__):
            result += f"\tname {attr} = {self.__dict__[attr]}\n"
        return result

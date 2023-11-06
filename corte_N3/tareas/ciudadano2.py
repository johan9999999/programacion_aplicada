class Ciudadano:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #----------Setters------------
    def setNombre(self,nombre:str):
        self.nombre=nombre

    def setEdad(self,edad:int):
        self.edad=edad

    #----------Getters------------
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad    

    def presentarse(self):
        return(f"Soy {self.nombre}, tengo {self.edad} años y soy un ciudadano.")

#----------------------------------------------------------------------------------        

class Medico(Ciudadano):
    def __init__(self, nombre, edad, especialidad, hospital):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.hospital = hospital

    #----------Setters------------
    def setNombre(self,especialidad:str):
        self.especialidad=especialidad

    def setEdad(self,hospital:str):
        self.hospital=hospital

    #----------Getters------------
    def getespecialidad(self):
        return self.especialidad
    
    def gethospital(self):
        return self.hospital   

    def presentarse(self):
        return(f"Me presento, soy el Dr. {self.nombre}, tengo {self.edad} años, soy médico {self.especialidad} y trabajo en el hospital {self.hospital}.")

    def realizar_cirugia(self, paciente):
        return(f"El Dr. {self.nombre} está realizando una cirugía en {paciente}.")

class Abogado(Ciudadano):
    def __init__(self, nombre, edad, especialidad, despacho):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.despacho = despacho

    #----------Setters------------
    def setespecialidad(self,especialidad:str):
        self.especialidad=especialidad

    def setdespacho(self,despacho:str):
        self.despacho=despacho

    #----------Getters------------
    def getespecialidad(self):
        return self.especialidad
    
    def getdespacho(self):
        return self.despacho         

    def presentarse(self):
        return(f"Me presento, soy el Abogado {self.nombre}, tengo {self.edad} años, soy especialista en {self.especialidad} y trabajo en el despacho {self.despacho}.")

    def representar_cliente(self, cliente):
        return(f"El Abogado {self.nombre} está representando a {cliente} en el tribunal.")

class Profesor(Ciudadano):
    def __init__(self, nombre, edad, materia, universidad):
        super().__init__(nombre, edad)
        self.materia = materia
        self.universidad = universidad

    #----------Setters------------
    def setmateria(self,materia:str):
        self.materia=materia

    def setuniversidad(self,universidad:str):
        self.universidad=universidad

    #----------Getters------------
    def getmateria(self):
        return self.materia
    
    def getuniversidad(self):
        return self.universidad
    
    def presentarse(self):
        return(f"Me presento, soy el Profesor {self.nombre}, tengo {self.edad} años, enseño {self.materia} en la universidad {self.universidad}.")

    def dar_clase(self, tema):
        return(f"El Profesor {self.nombre} está dando una clase sobre {tema}.")

def main():
    inscrito=Medico("Juan Bohorquez", 33, "Cirujano", "Hospital General")
    print(f'Nombre: {inscrito.getNombre()}\n',\
        f'Edad: {inscrito.getEdad()}\n',\
            f'especialidad: {inscrito.getespecialidad()}\n',\
                f'hospital: {inscrito.gethospital()}\n')
    print(inscrito.presentarse())
    print(inscrito.realizar_cirugia("Johan"))

    print('\n------------------------------------')
    inscrito2=Abogado("Maria Rodriguez", 40, "Derecho Penal", "Bufete Legal")
    print(f'Nombre: {inscrito2.getNombre()}\n',\
        f'Edad: {inscrito2.getEdad()}\n',\
            f'especialidad: {inscrito2.getespecialidad()}\n',\
                f'despacho : {inscrito2.getdespacho ()}\n')
    print(inscrito2.presentarse())
    print(inscrito2.representar_cliente("David"))

    print('\n------------------------------------')
    inscrito3=Profesor("Alberto Cifuentes", 30, "programacion", "San Buenaventura")
    print(f'Nombre: {inscrito3.getNombre()}\n',\
        f'Edad: {inscrito2.getEdad()}\n',\
            f'materia : {inscrito3.getmateria()}\n',\
                f'universidad : {inscrito3.getuniversidad()}\n')
    print(inscrito3.presentarse())
    print(inscrito3.dar_clase("Programacion orientada a objetos"))
if __name__=="__main__":
    main()
  

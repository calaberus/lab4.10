class album:

  def __init__(self):
      self.fotos=[]
      
def agregar_fotos(self,foto):
    print(f"foto´{foto}´ágregar al album.")
          
def eliminar_foto(self,foto):
    if foto in self.fotos:
        sefl.fotos.remove(foto)
        print(f"foto´{foto}´eliminada del album.")
    else:
        print(f"foto´{foto}´no encontrada")
        
def mostar_fotos(self):
    if self.fotos:
        print("fotos en el album:",",".join(self.fotos))
    else:
        print("el album esta vacio.")
        
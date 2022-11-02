from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        CandidatoActual=Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.nombre=infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        CandidatoActual.cedula = infoCandidato["cedula"]
        CandidatoActual.nroResolucion = infoCandidato["nroResolucion"]
        return self.repositorioCandidato.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)
    """
    Relación Partido y Candidato
    """
    def asignarPartido(self, cedula, id_Partido):
        CandidatoActual = Candidato(self.repositorioCandidato.findById(cedula))
        PartidoActual = Partido(self. repositorioPartido.findById(id_Partido))
        CandidatoActual.Partido = PartidoActual
        return self.repositorioCandidato.save(CandidatoActual)

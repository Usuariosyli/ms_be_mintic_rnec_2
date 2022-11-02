from Modelos.ResultadosVo import ResultadosVo
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultadosVo import RepositorioResultadosVo
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorResultadosVo():
    def __init__(self):
        self.repositorioResultadosVo = RepositorioResultadosVo()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidatos = RepositorioCandidato()
    def index(self):
        return self.repositorioResultadosVo.findAll()
    """
    Asignacion Mesa y Candidato a resultados
    """
    def create(self,infoResultadosVo,id_Mesa,id_Candidato):
        nuevaResultadosVo=ResultadosVo(infoResultadosVo)
        elMesa=Mesa(self.repositorioMesa.findById(id_Mesa))
        laCandidato=Candidato(self.repositorioCandidatos.findById(id_Candidato))
        nuevaResultadosVo.Mesa=elMesa
        nuevaResultadosVo.Candidato=laCandidato
        return self.repositorioResultadosVo.save(nuevaResultadosVo)
    def show(self,id):
        elResultadosVo=ResultadosVo(self.repositorioResultadosVo.findById(id))
        return elResultadosVo.__dict__
    """
    Modificación de resultados (Mesa y Candidato)
    """
    def update(self,id,infoResultadosVo,id_Mesa,id_Candidato):
        laResultadosVo=ResultadosVo(self.repositorioResultadosVo.findById(id))
        laResultadosVo.cantvotos_final=infoResultadosVo["cantvotos_final"]
        elMesa = Mesa(self.repositorioMesa.findById(id_Mesa))
        laCandidato = Candidato(self.repositorioCandidatos.findById(id_Candidato))
        laResultadosVo.Mesa = elMesa
        laResultadosVo.Candidato = laCandidato
        return self.repositorioResultadosVo.save(laResultadosVo)
    def delete(self, id):
        return self.repositorioResultadosVo.delete(id)
    "Obtener todos los resultados de un Candidato"
    def listarInscritosEnCandidato(self,id_Candidato):
        return self.repositorioResultadosVo.getListadoInscritosEnCandidato(id_Candidato)
    "Obtener votos mas altas por candidato"
    def votosMasAltosPorCandidato(self):
        return self.repositorioResultadosVo.getMayorVotosPorCandidato()
    "Obtener promedio de votos por Candidato"
    def promedioVotosEnCandidato(self,id_Candidato):
        return self.repositorioResultadosVo.getPromedioVotosEnCandidato(id_Candidato)
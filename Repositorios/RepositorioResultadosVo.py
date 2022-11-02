from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.ResultadosVo import ResultadosVo

from bson import ObjectId

class RepositorioResultadosVo(InterfaceRepositorio[ResultadosVo]):
    def getListadoInscritosEnCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    def getMayorVotosPorCandidato(self):
        query1={
                "$group": {
                    "_id": "$candidato",
                    "max": {
                        "$max": "$cantvotos_final"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def getPromedioVotosEnCandidato(self,id_candidato):
        query1 = {
          "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
          "$group": {
            "_id": "$candidato",
            "promedio": {
              "$avg": "$cantvotos_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)


from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorResultadosVo import ControladorResultadosVo
miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()
miControladorCandidato=ControladorCandidato()
miControladorResultadosVo=ControladorResultadosVo()
###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###  Mesas  ################################################################################
@app.route("/mesas",methods=['GET'])
def getmesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
### Partidos ################################################################################
@app.route("/partidos",methods=['GET'])
def getpartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
### Candidatos ################################################################################
@app.route("/candidatos",methods=['GET'])
def getcandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)
### Resultados votos ################################################################################
@app.route("/resultadosvo",methods=['GET']) #nok
def getresultadosvo():
    json=miControladorResultadosVo.index()
    return jsonify(json)
@app.route("/resultadosvo/<string:id>",methods=['GET']) #ok
def getResultadosVo(id):
    json=miControladorResultadosVo.show(id)
    return jsonify(json)
@app.route("/resultadosvo/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST']) 
def crearResultadosVo(id_mesa,id_candidato): #ok
    data = request.get_json()
    json=miControladorResultadosVo.create(data,id_mesa,id_candidato)
    return jsonify(json)
#@app.route("/resultadosvo/<string:id_ResultadosVo>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
#def modificarResultadosVo(id_ResultadosVo,id_estudiante,id_materia):
#    data = request.get_json()
#    json=miControladorResultadosVo.update(id_ResultadosVo,data,id_estudiante,id_materia)
#    return jsonify(json)
#@app.route("/resultadosvo/<string:id_ResultadosVo>",methods=['DELETE'])
#def eliminarResultadosVo(id_ResultadosVo):
#    json=miControladorResultadosVo.delete(id_ResultadosVo)
#    return jsonify(json)
@app.route("/resultadosvo/candidato/<string:id_Candidato>",methods=['GET'])
def resultadosEnCandidato(id_Candidato): #nok
    json=miControladorResultadosVo.listarResultadosEnCandidato(id_Candidato)
    return jsonify(json)
@app.route("/resultadosvo/cvotos_final",methods=['GET'])
def getMayorVotosPorCandidato():
    json=miControladorResultadosVo.votosMasAltosPorCandidato()
    return jsonify(json)
@app.route("/resultadosvo/promedio_votos/candidato/<string:id_Candidato>",methods=['GET'])
def getPromedioVotosEnCandidato(id_Candidato):
    json=miControladorResultadosVo.promedioVotosEnCandidato(id_Candidato)
    return jsonify(json)
###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


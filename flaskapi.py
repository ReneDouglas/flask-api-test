import json
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/clientes")
def listarPacientes():
    return jsonify({
        'pacientes':[
            {
                'id':1,
                'nome':'Golas',
                'cpf':'123456789',
                'data_nasc':'17/08/1990',
                'enderecos':[
                    {
                        'rua':'rua 1',
                        'numero':'1',
                        'bairro':'bairro 1',
                        'cidade':'cidade 1'
                    },
                    {
                        'rua':'rua 2',
                        'numero':'2',
                        'bairro':'bairro 2',
                        'cidade':'cidade 2'
                    },
                ]
            },
            {
                'id':2,
                'nome':'Guiné',
                'cpf':'987654321',
                'data_nasc':'01/01/2000',
                'enderecos':[
                    {
                        'rua':'rua 1',
                        'numero':'1',
                        'bairro':'bairro 1',
                        'cidade':'cidade 1'
                    }
                ]
            },
            {
                'id':3,
                'nome':'Galo',
                'cpf':'666666666',
                'data_nasc':'01/10/2005',
                'enderecos':''
            }
        ]
    })

@app.route("/psfs")
def listarPsfs():
    return jsonify({
        'nomes_psf':[
            'Sao brás',
            'Sobreira',
            'Centro',
            'Rua Nova',
            'Ponte'
        ]
    })

@app.route("/cliente", methods=['GET']) 
def getPaciente():
    id = request.args.get('id')
    if id == "1":
        return jsonify({
			'id':1,
			'nome':'Golas',
			'cpf':'123456789',
			'data_nasc':'17/08/1990',
			'enderecos':[
				{
					'rua':'rua 1',
					'numero':'1',
					'bairro':'bairro 1',
					'cidade':'cidade 1'
				},
				{
					'rua':'rua 2',
					'numero':'2',
					'bairro':'bairro 2',
					'cidade':'cidade 2'
				},
			]
		})
    elif id == "2":
        return jsonify({
			'id':2,
			'nome':'Guiné',
			'cpf':'987654321',
			'data_nasc':'01/01/2000',
			'enderecos':[
				{
					'rua':'rua 1',
					'numero':'1',
					'bairro':'bairro 1',
					'cidade':'cidade 1'
				}
			]
		})
    elif id == "3":
        return jsonify({
			'id':3,
			'nome':'Galo',
			'cpf':'666666666',
			'data_nasc':'01/10/2005',
			'enderecos':''
		})
    else:
        return jsonify({'message':'paciente não existe'})


@app.route("/inserir", methods=['POST'])
def cadastrarPaciente():
    try:
        json_data = json.loads(request.data, strict=False)
        return jsonify(json_data)
    except:
        return jsonify({'message':'bad request', 'error':'404'})

app.run()
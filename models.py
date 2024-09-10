from flask_sqlalchemy import SQLAlchemy

# Inicializando o banco de dados
db = SQLAlchemy()

# Definindo o modelo para o Lead
class Lead(db.Model):
	__tablename__ = 'leads'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	latitude = db.Column(db.Float, nullable=False)
	longitude = db.Column(db.Float, nullable=False)
	temperature = db.Column(db.Float, nullable=False)
	interest = db.Column(db.String(200), nullable=False)

	def __init__(self, name, latitude, longitude, temperature, interest):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.temperature = temperature
		self.interest = interest

	# Função para retornar os dados como dicionário
	def as_dict(self):
		return {
        	'id': self.id,
        	'name': self.name,
        	'latitude': self.latitude,
        	'longitude': self.longitude,
        	'temperature': self.temperature,
        	'interest': self.interest
    	}
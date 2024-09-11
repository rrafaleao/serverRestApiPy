import random
from models import Lead, db

# Função para gerar leads fictícios
def generate_leads():
	names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
	interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']
	emails =  ['maria.souza1990@exemplo.com', 'joao.silva2021@exemplo.org','ana.pereira85@teste.net','carlos.oliveira12@exemplo.com.br','fernanda.martins88@dadosfake.com']
	telefones = ['(11) 98765-4321','(21) 91234-5678','(31) 99876-5432','(41) 93456-7890','(51) 98765-0987']

	for _ in range(100):
		name = random.choice(names)
		latitude = random.uniform(-90, 90)
		longitude = random.uniform(-180, 180)
		temperature = random.uniform(10, 40)
		interest = random.choice(interests)
		email = random.choice(emails)
		telefone = random.choice(telefones)

		lead = Lead(name, latitude, longitude, temperature, interest, email, telefone)
		db.session.add(lead)
		db.session.commit()
from src.main import app
from src.models import db
from src.models.cliente import Cliente
from src.models.financeiro import Financeiro
from src.models.agenda import Agenda
from src.models.user import User
import datetime

with app.app_context():
    # Criar cliente de exemplo se não existir
    cliente = Cliente.query.filter_by(email='cliente@exemplo.com').first()
    if not cliente:
        cliente = Cliente(
            nome='Cliente Teste', 
            email='cliente@exemplo.com', 
            telefone='(11) 99999-9999', 
            endereco='Rua Exemplo, 123', 
            cidade='São Paulo', 
            estado='SP', 
            cep='01234-567', 
            cnpj='12.345.678/0001-90', 
            contato='João Silva', 
            observacoes='Cliente de teste', 
            ativo=True, 
            data_cadastro=datetime.datetime.now()
        )
        db.session.add(cliente)
        db.session.commit()
        print('Cliente criado com sucesso!')
    else:
        print('Cliente já existe')
        cliente_id = cliente.id
    
    # Criar agenda de exemplo
    agenda = Agenda(
        titulo='Reunião de planejamento', 
        descricao='Discussão sobre novas rotas', 
        data=datetime.datetime.now() + datetime.timedelta(days=2), 
        hora='14:00', 
        local='Sede da empresa', 
        status='agendado', 
        cliente_id=1
    )
    db.session.add(agenda)
    
    # Criar financeiro de exemplo
    financeiro = Financeiro(
        descricao='Pagamento de frete', 
        valor=1500.00, 
        tipo='receita', 
        data=datetime.datetime.now(), 
        status='pago', 
        cliente_id=1, 
        observacoes='Pagamento referente ao mês atual'
    )
    db.session.add(financeiro)
    
    # Commit das alterações
    db.session.commit()
    print('Dados de exemplo criados com sucesso!')

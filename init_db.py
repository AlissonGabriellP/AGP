from src.main import app
from src.models import db
from src.models.user import User
from src.models.cliente import Cliente, Entrega
from src.models.financeiro import Financeiro
from src.models.agenda import Agenda
import datetime
import werkzeug.security

# Script para recriar o banco de dados e inserir dados iniciais

with app.app_context():
    # Recriar todas as tabelas
    db.drop_all()
    db.create_all()
    print("Banco de dados recriado com sucesso!")
    
    # Criar usuário administrador
    admin = User(
        username='admin',
        email='admin@agp.com.br',
        nome='Administrador',
        password_hash=werkzeug.security.generate_password_hash('admin123'),
        role='admin',
        is_active=True,
        created_at=datetime.datetime.now()
    )
    db.session.add(admin)
    
    # Criar usuário cliente
    cliente_user = User(
        username='cliente',
        email='cliente@exemplo.com',
        nome='Cliente Teste',
        password_hash=werkzeug.security.generate_password_hash('cliente123'),
        role='cliente',
        is_active=True,
        created_at=datetime.datetime.now()
    )
    db.session.add(cliente_user)
    db.session.commit()
    print("Usuários criados com sucesso!")
    
    # Criar cliente de exemplo
    cliente = Cliente(
        nome='Empresa Exemplo Ltda',
        email='contato@empresaexemplo.com.br',
        telefone='(11) 99999-9999',
        endereco='Rua Exemplo, 123',
        cidade='São Paulo',
        estado='SP',
        cep='01234-567',
        cnpj='12.345.678/0001-90',
        is_active=True,
        created_at=datetime.datetime.now()
    )
    db.session.add(cliente)
    db.session.commit()
    print("Cliente criado com sucesso!")
    
    # Criar entregas de exemplo
    entrega1 = Entrega(
        cliente_id=cliente.id,
        origem='São Paulo, SP',
        destino='Rio de Janeiro, RJ',
        descricao_carga='Eletrônicos diversos',
        peso=150.5,
        volume=2.3,
        valor=2500.00,
        status='pendente',
        data_coleta=datetime.datetime.now(),
        data_entrega_prevista=datetime.datetime.now() + datetime.timedelta(days=3),
        telefone_contato='(11) 98765-4321',
        nota_fiscal='NF-123456'
    )
    
    entrega2 = Entrega(
        cliente_id=cliente.id,
        origem='São Paulo, SP',
        destino='Belo Horizonte, MG',
        descricao_carga='Móveis para escritório',
        peso=320.0,
        volume=5.8,
        valor=1800.00,
        status='em_transito',
        data_coleta=datetime.datetime.now() - datetime.timedelta(days=1),
        data_entrega_prevista=datetime.datetime.now() + datetime.timedelta(days=2),
        telefone_contato='(11) 98765-4321',
        nota_fiscal='NF-123457'
    )
    
    db.session.add(entrega1)
    db.session.add(entrega2)
    db.session.commit()
    print("Entregas criadas com sucesso!")
    
    # Verificar campos do modelo Agenda
    try:
        # Criar agenda de exemplo
        agenda1 = Agenda(
            titulo='Reunião de planejamento',
            descricao='Discussão sobre novas rotas',
            data_inicio=datetime.datetime.now() + datetime.timedelta(days=2),
            data_fim=datetime.datetime.now() + datetime.timedelta(days=2, hours=2),
            tipo='reuniao',
            status='agendado',
            cliente_id=cliente.id,
            usuario_id=admin.id  # Campo obrigatório
        )
        
        agenda2 = Agenda(
            titulo='Coleta de mercadorias',
            descricao='Coleta de produtos eletrônicos',
            data_inicio=datetime.datetime.now() + datetime.timedelta(days=1),
            data_fim=datetime.datetime.now() + datetime.timedelta(days=1, hours=1),
            tipo='coleta',
            status='agendado',
            cliente_id=cliente.id,
            entrega_id=entrega1.id,
            usuario_id=admin.id  # Campo obrigatório
        )
        
        db.session.add(agenda1)
        db.session.add(agenda2)
        db.session.commit()
        print("Agendamentos criados com sucesso!")
    except Exception as e:
        print(f"Erro ao criar agendamentos: {e}")
        db.session.rollback()
    
    # Verificar campos do modelo Financeiro
    try:
        # Criar financeiro de exemplo
        financeiro1 = Financeiro(
            descricao='Pagamento de frete',
            valor=2500.00,
            tipo='receita',
            categoria='frete',
            data_lancamento=datetime.datetime.now(),
            data_vencimento=datetime.datetime.now() + datetime.timedelta(days=5),
            status='pendente',
            entrega_id=entrega1.id,
            created_by=admin.id  # Campo obrigatório
        )
        
        financeiro2 = Financeiro(
            descricao='Manutenção de veículos',
            valor=800.00,
            tipo='despesa',
            categoria='manutencao',
            data_lancamento=datetime.datetime.now(),
            data_pagamento=datetime.datetime.now(),
            status='pago',
            created_by=admin.id  # Campo obrigatório
        )
        
        db.session.add(financeiro1)
        db.session.add(financeiro2)
        db.session.commit()
        print("Registros financeiros criados com sucesso!")
    except Exception as e:
        print(f"Erro ao criar registros financeiros: {e}")
        db.session.rollback()
    
    print("Banco de dados inicializado com dados de exemplo!")

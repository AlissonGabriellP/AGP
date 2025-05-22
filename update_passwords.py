from src.main import app
from src.models import db
from src.models.user import User
import werkzeug.security

with app.app_context():
    # Atualizar senha do admin
    admin = User.query.filter_by(username='admin').first()
    if admin:
        admin.password_hash = werkzeug.security.generate_password_hash('admin123')
        print(f"Senha do usuário {admin.username} atualizada com hash")
    else:
        print("Usuário admin não encontrado")
    
    # Atualizar senha do cliente
    cliente = User.query.filter_by(username='cliente').first()
    if cliente:
        cliente.password_hash = werkzeug.security.generate_password_hash('cliente123')
        print(f"Senha do usuário {cliente.username} atualizada com hash")
    else:
        print("Usuário cliente não encontrado")
    
    # Commit das alterações
    db.session.commit()
    print("Alterações salvas no banco de dados")

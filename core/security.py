from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha (senha: str, hash_senha: str) -> bool:
    
    """
    Função para verificar se a senha está correta
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    
    
    return CRIPTO.hash(senha)
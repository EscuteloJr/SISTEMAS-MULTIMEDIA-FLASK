from enum import unique
from sqlalchemy import true
from app import  db


class EstadoCivil(db.Model):
    __tablename__ = "tb_estado_civil"
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = nome = db.Column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<EstadoCivil %r>" % self.descricao
    
    
class AnoLectivo(db.Model):
    __tablename__ = "tb_ano_lectivo"
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, descricao, estado):
        self.descricao = descricao
        self.estado = estado
        
    def __repr__(self):
        return "<AnoLectivo %r>" % self.descricao
        

class Sexo(db.Model):
    __tablename__ = "tb_sexo"
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = nome = db.Column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<Sexo %r>" % self.descricao


class Pessoa(db.Model):
    __tablename__ = "tb_pessoa"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    sobrenome = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(60), unique=true)
    sexo_id =  db.Column(db.Integer, db.ForeignKey('tb_sexo.id'))
    estado_civil_id =  db.Column(db.Integer, db.ForeignKey('tb_estado_civil.id'))
    bi = db.Column(db.String(14), nullable=False)
    data_cadastro = db.Column(db.Date, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    
    sexo = db.relationship('Sexo', foreign_keys=sexo_id)
    estadoCivil = db.relationship('EstadoCivil', foreign_keys=estado_civil_id)
    
    def __int__(self, nome, sobrenome, email, sexo_id, bi, data_cadastro, estado):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.sexo_id = sexo_id
        self.bi = bi
        self.data_cadastro = data_cadastro
        self.estado = estado
        
    def __repr__(self):
        return "<Pessoa %r>" % self.nome
    
    
class Encarregado(db.Model): 
    ___tablename__ = "tb_encarregado"
    
    id = db.Column(db.Integer, primary_key=True)
    qtdCriancas = db.Column(db.Integer, nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('tb_pessoa.id'))
    data_cadastro = db.Column(db.Date, nullable=False)
    
    pessoa = db.relationship('Pessoa', foreign_keys=pessoa_id)
    
    def __init__(self, qtdCriancas, pessoa_id, data_cadastro):
        self.qtdCriancas = qtdCriancas
        self.pessoa_id = pessoa_id
        self.data_cadastro = data_cadastro
        
    def __repr__(self):
        return "<Encarregado %r>" % self.id
    
    
class Crianca(db.Model):
    ___tablename__ = "tb_crianca"
    
    id = db.Column(db.Integer, primary_key=True) 
    pessoa_id = db.Column(db.Integer, db.ForeignKey('tb_pessoa.id'))
    encarregado_id = db.Column(db.Integer, db.ForeignKey('tb_encarregado.id'))    
    data_cadastro = db.Column(db.Date, nullable=False) 
        
    encarregado = db.relationship('Encarregado', foreign_keys=encarregado_id)
    pessoa = db.relationship('Pessoa', foreign_keys=pessoa_id)
    
    def __init__(self, encarregado_id, pessoa_id, data_cadastro):
        self.encarregado_id = encarregado_id
        self.data_cadastro = data_cadastro
        self.pessoa_id = pessoa_id
        
    def __repr__(self):
        return "<Crianca %r>" % self.id

'''
class PlanoDeEstudo(db.Model):
    __tablename__ = "tb_plano_estudo"
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = nome = db.Column(db.String, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, descricao, estado):
        self.descricao = descricao
        self.estado = estado
        
    def __repr__(self):
        return "<PlanoDeEstudo %r>" % self.descricao
    
    
class Material(db.Model):
    __tablename__ = "tb_material"
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = nome = db.Column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<Material %r>" % self.descricao
    
    
class PlanoMaterial(db.Model):
    __tablename__ = "tb_plano_material"
    
    id = db.Column(db.Integer, primary_key=True)
    plano_id =  db.Column(db.Integer, db.ForeignKey('tb_plano_estudo.id', on_delete=db.CASCADE))
    material_id =  db.Column(db.Integer, db.ForeignKey('tb_material.id', on_delete=db.CASCADE))
    
    PlanoDeEstudo = db.relationship('PlanoDeEstudo', foreign_keys=plano_id)
    Material = db.relationship('Material', foreign_keys=material_id)
    
    def __init__(self, plano_id, material_id):
        self.plano_id = plano_id
        self.material_id = material_id
        
    def __repr__(self):
        return "<PlanoMaterial %r>" % self.id    
    

class Classe(db.Model):
    ___tablename__ = "tb_classe"
    id = db.Column(db.Integer, primary_key=True) 
    descricao = nome = db.Column(db.String, nullable=False)
    plano_estudo_id = db.Column(db.Integer, db.ForeignKey('tb_plano_estudo.id', on_delete=db.CASCADE))
    estado = db.Column(db.Boolean, nullable=False)
        
    PlanoDeEstudo = db.relationship('PlanoDeEstudo', foreign_keys=plano_estudo_id)
    
    def __init__(self, plano_estudo_id, estado):
        self.plano_estudo_id = plano_estudo_id
        self.estado = estado
        
    def __repr__(self):
        return "<Classe %r>" % self.descricao   
    
    
class Turma(db.Model):
    ___tablename__ = "tb_turma"
    id = db.Column(db.Integer, primary_key=True) 
    descricao = nome = db.Column(db.String, nullable=False)
    classe_id = db.Column(db.Integer, db.ForeignKey('tb_classe.id', on_delete=db.CASCADE))
    ano_ectivo_id = db.Column(db.Integer, db.ForeignKey('tb_ano_lectivo.id', on_delete=db.CASCADE))
    estado = db.Column(db.Boolean, nullable=False)
         
    Classe = db.relationship('Classe', foreign_keys=classe_id)
    AnoLectivo = db.relationship('AnoLectivo', foreign_keys=ano_ectivo_id)
    
    def __init__(self, classe_id, ano_ectivo_id, estado):
        self.classe_id = classe_id
        self.ano_ectivo_id = ano_ectivo_id
        self.estado = estado
        
    def __repr__(self):
        return "<Turma %r>" % self.descricao  
    
    
class Matricula(db.Model):
    __tablename__ = "tb_matricula"
    
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('tb_turma.id', on_delete=db.CASCADE))
    encarregado_id = db.Column(db.Integer, db.ForeignKey('tb_encarregado.id', on_delete=db.CASCADE))
    crianca_id = db.Column(db.Integer, db.ForeignKey('tb_crianca.id', on_delete=db.CASCADE))
    data_matricula = db.Column(db.Date, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)
        
    Pessoa = db.relationship('Pessoa', foreign_keys=encarregado_id)
    Crianca = db.relationship('Crianca', foreign_keys=crianca_id)
    
    def __init__(self, turma_id, encarregado_id, crianca_id, data_matricula, estado):
        self.turma_id = turma_id
        self.encarregado_id = encarregado_id
        self.crianca_id = crianca_id
        self.data_matricula = data_matricula
        self.estado = estado
        
    def __repr__(self):
        return "<Matricula %r>" % self.id    
    
    
class ConfirmacaoMatricula(db.Model):
    ___tablename__ = "tb_confirmacao_matricula"
    id = db.Column(db.Integer, primary_key=True) 
    matricula_id = db.Column(db.Integer, db.ForeignKey('tb_matricula.id', on_delete=db.CASCADE))
    data_confirmacao = db.Column(db.Date, nullable=False) 
        
    Pessoa = db.relationship('Matricula', foreign_keys=matricula_id)
    
    def __init__(self, matricula_id, data_confirmacao):
        self.matricula_id = matricula_id
        self.data_confirmacao = data_confirmacao
        
    def __repr__(self):
        return "<ConfirmacaoMatricula %r>" % self.id
'''
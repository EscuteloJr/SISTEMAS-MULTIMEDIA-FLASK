from enum import unique
from sqlalchemy import true
from app import  db


class EstadoCivil(db.Model):
    __tablename__ = "tb_estado_civil"
    
    id = db.column(db.Integer, primary_key=true)
    descricao = nome = db.column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<EstadoCivil %r>" % self.descricao
    
    
class AnoLectivo(db.Model):
    __tablename__ = "tb_ano_lectivo"
    
    id = db.column(db.Integer, primary_key=true)
    descricao = nome = db.column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<AnoLectivo %r>" % self.descricao
        

class Sexo(db.Model):
    __tablename__ = "tb_sexo"
    
    id = db.column(db.Integer, primary_key=true)
    descricao = nome = db.column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<Sexo %r>" % self.descricao


class Pessoa(db.Model):
    __tablename__ = "tb_pessoa"
    
    id = db.column(db.Integer, primary_key=true)
    nome = db.column(db.String(40), nullable=False)
    sobrenome = db.column(db.String(40), nullable=False)
    email = db.column(db.String(60), unique=true)
    sexo_id =  db.column(db.Integer, db.models.ForeignKey('tb_sexo.id', on_delete=db.CASCADE))
    estado_civil_id =  db.column(db.Integer, db.models.ForeignKey('tb_estado_civil.id', on_delete=db.CASCADE))
    bi = db.column(db.String(14), nullable=False)
    data_cadastro = db.column(db.Date, nullable=False)
    
    Sexo = db.relationship('Sexo', foreign_key=sexo_id)
    EstadoCivil = db.relationship('EstadoCivil', foreign_key=estado_civil_id)
    
    def __int__(self, nome, sobrenome, email, sexo_id, bi, data_cadastro):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.sexo_id = sexo_id
        self.bi = bi
        self.data_cadastro = data_cadastro
        
    def __repr__(self):
        return "<Pessoa %r>" % self.nome
    
    
class Encarregado(db.Model): 
    ___tablename__ = "tb_encarregado"
    
    id = db.column(db.Integer, primary_key=true)
    qtdCriancas = db.column(db.Integer, nullable=False)
    pessoa_id = db.column(db.Integer, db.models.ForeignKey('tb_pessoa.id', on_delete=db.CASCADE))
    data_cadastro = db.column(db.Date, nullable=False)
    
    Pessoa = db.relationship('Pessoa', foreign_key=pessoa_id)
    
    def __init__(self, qtdCriancas, pessoa_id, data_cadastro):
        self.qtdCriancas = qtdCriancas
        self.pessoa_id = pessoa_id
        self.data_cadastro = data_cadastro
        
    def __repr__(self):
        return "<Encarregado %r>" % self.id
    
    
class Crianca(db.Model):
    ___tablename__ = "tb_crianca"
    id = db.column(db.Integer, primary_key=true) 
    encarregado_id = db.column(db.Integer, db.models.ForeignKey('tb_encarregado.id', on_delete=db.CASCADE))
    data_cadastro = db.column(db.Date, nullable=False) 
        
    Pessoa = db.relationship('Pessoa', foreign_key=encarregado_id)
    
    def __init__(self, encarregado_id, data_cadastro):
        self.encarregado_id = encarregado_id
        self.data_cadastro = data_cadastro
        
    def __repr__(self):
        return "<Crianca %r>" % self.id


class PlanoDeEstudo(db.Model):
    __tablename__ = "tb_plano_estudo"
    
    id = db.column(db.Integer, primary_key=true)
    descricao = nome = db.column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<PlanoDeEstudo %r>" % self.descricao
    
    
class Material(db.Model):
    __tablename__ = "tb_material"
    
    id = db.column(db.Integer, primary_key=true)
    descricao = nome = db.column(db.String, nullable=False)
    
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __repr__(self):
        return "<Material %r>" % self.descricao
    
    
class PlanoMaterial(db.Model):
    __tablename__ = "tb_plano_material"
    
    id = db.column(db.Integer, primary_key=true)
    plano_id =  db.column(db.Integer, db.models.ForeignKey('tb_plano_estudo.id', on_delete=db.CASCADE))
    material_id =  db.column(db.Integer, db.models.ForeignKey('tb_material.id', on_delete=db.CASCADE))
    
    PlanoDeEstudo = db.relationship('PlanoDeEstudo', foreign_key=plano_id)
    Material = db.relationship('Material', foreign_key=material_id)
    
    def __init__(self, plano_id, material_id):
        self.plano_id = plano_id
        self.material_id = material_id
        
    def __repr__(self):
        return "<PlanoMaterial %r>" % self.id    
    

class Classe(db.Model):
    ___tablename__ = "tb_classe"
    id = db.column(db.Integer, primary_key=true) 
    descricao = nome = db.column(db.String, nullable=False)
    plano_estudo_id = db.column(db.Integer, db.models.ForeignKey('tb_plano_estudo.id', on_delete=db.CASCADE))
        
    PlanoDeEstudo = db.relationship('PlanoDeEstudo', foreign_key=plano_estudo_id)
    
    def __init__(self, plano_estudo_id):
        self.plano_estudo_id = plano_estudo_id
        
    def __repr__(self):
        return "<Classe %r>" % self.descricao   
    
    
class Turma(db.Model):
    ___tablename__ = "tb_turma"
    id = db.column(db.Integer, primary_key=true) 
    descricao = nome = db.column(db.String, nullable=False)
    classe_id = db.column(db.Integer, db.models.ForeignKey('tb_classe.id', on_delete=db.CASCADE))
    ano_ectivo_id = db.column(db.Integer, db.models.ForeignKey('tb_ano_lectivo.id', on_delete=db.CASCADE))
        
    Classe = db.relationship('Classe', foreign_key=classe_id)
    AnoLectivo = db.relationship('AnoLectivo', foreign_key=ano_ectivo_id)
    
    def __init__(self, classe_id, ano_ectivo_id):
        self.classe_id = classe_id
        self.ano_ectivo_id = ano_ectivo_id
        
    def __repr__(self):
        return "<Turma %r>" % self.descricao  
    
    
class Matricula(db.Model):
    __tablename__ = "tb_matricula"
    
    id = db.column(db.Integer, primary_key=true)
    turma_id = db.column(db.Integer, db.models.ForeignKey('tb_turma.id', on_delete=db.CASCADE))
    encarregado_id = db.column(db.Integer, db.models.ForeignKey('tb_encarregado.id', on_delete=db.CASCADE))
    crianca_id = db.column(db.Integer, db.models.ForeignKey('tb_crianca.id', on_delete=db.CASCADE))
    data_matricula = db.column(db.Date, nullable=False)
        
    Pessoa = db.relationship('Pessoa', foreign_key=encarregado_id)
    Crianca = db.relationship('Crianca', foreign_key=crianca_id)
    
    def __init__(self, turma_id, encarregado_id, crianca_id, data_matricula):
        self.turma_id = turma_id
        self.encarregado_id = encarregado_id
        self.crianca_id = crianca_id
        self.data_matricula = data_matricula
        
    def __repr__(self):
        return "<Matricula %r>" % self.id    
    
    
class ConfirmacaoMatricula(db.Model):
    ___tablename__ = "tb_confirmacao_matricula"
    id = db.column(db.Integer, primary_key=true) 
    matricula_id = db.column(db.Integer, db.models.ForeignKey('tb_matricula.id', on_delete=db.CASCADE))
    data_confirmacao = db.column(db.Date, nullable=False) 
        
    Pessoa = db.relationship('Matricula', foreign_key=matricula_id)
    
    def __init__(self, matricula_id, data_confirmacao):
        self.matricula_id = matricula_id
        self.data_confirmacao = data_confirmacao
        
    def __repr__(self):
        return "<ConfirmacaoMatricula %r>" % self.id    
    
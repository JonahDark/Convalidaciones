from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class alumno_model(models.Model):
    _name='convalidaciones.profesor_model'
    _description = 'Modelo de Profesores'


    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre del profesor")
    apellidos =fields.Char(string="Apellidos",required=True,help="Apellidos del profesor")
    dni=fields.Char(string="DNI",required=True,help="DNI del profesor")
    email=fields.Char(string="E-mail",required=True,help="E-mail del profesor")
    foto = fields.Binary()
    ciclos = fields.Many2many("convalidaciones.ciclo_model","cicl_prof_rel","cicl_id","prof_id",string="Ciclos")    
    modulos = fields.One2many("convalidaciones.modulo_model","profesor",string="Modulos")
    alumnos = fields.Many2many("convalidaciones.alumno_model","alu_prof_rel","prof_id","alu_id",string="Alumnos")
    numAlu = fields.Integer(string="Numero de alumnos", compute="_nAlu", store=True)

    @api.depends("alumnos") #decorador que ejecutara el metodo cuando alumnos se modifique 
    def _nAlu(self):
        self.numAlu=len(self.alumnos)

    @api.depends("dni")
    def _validacionDNI(self):
        letras="TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = self.dni[:-1]
        resto=num%23
        letraDNI=letras[resto]
        if letraDNI != letra:
            raise ValidationError("DNI no valido")
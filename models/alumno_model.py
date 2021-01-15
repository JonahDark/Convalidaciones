# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class alumno_model(models.Model):
    _name='convalidaciones.alumno_model'
    _description = 'Modelo de alumnos'

    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre del alumno")
    foto=fields.Binary()
    password=fields.Char(string="Password",size=10,help="Password del alumno")
    edad=fields.Integer(string="Edad",required=True,help="Edad del alumno")
    localidad=fields.Char(string="Localidad",size=100,required=True,help="Localidad del alumno")
    provincia=fields.Char(string="Provincia",size=100,required=True,help="Provincia del alumno")
    email=fields.Char(string="Email",size=100,required=False,help="Email del alumno")
    convalidaciones = fields.One2many("convalidaciones.conva_model","alumno_id",string="Convalidaciones")
    profesores = fields.Many2many("convalidaciones.profesor_model","alu_prof_rel","alu_id","prof_id",string="Profesores")


    @api.constrains("edad")
    def _mayorDe14(self):
        if self.edad<14:
            raise ValidationError("La edad debe ser alemnos de 14 años")

    def generarPassword(self):
        self.password=""
        self.ensure_one()
        for i in range (10):
            self.password+=random.choice("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
        return True    
            

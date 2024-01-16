# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Alumno
class Alumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Alumno de FP'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    curso_academico = fields.Char(string='Curso Académico', required=True)
    correo_electronico = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    ciclo_formativo = fields.Selection([('1', 'DAM'), ('2', 'DAW'), ('3', 'ASIR')], string='Ciclo Formativo', required=True)
    periodo_practica = fields.Selection([('1', 'Abril'), ('2', 'Septiembre')], string='Periodo de Práctica', required=True)
    nota_media = fields.Float(string='Nota Media', required=True)
    nota_media_texto = fields.Char(string='Nota Media en Texto', compute='_compute_nota_media_texto', store=True)

    @api.depends('nota_media')
    def _compute_nota_media_texto(self):
        for alumno in self:
            if alumno.nota_media >= 9:
                alumno.nota_media_texto = 'Sobresaliente'
            elif 7 <= alumno.nota_media < 9:
                alumno.nota_media_texto = 'Notable'
            elif 5 <= alumno.nota_media < 7:
                alumno.nota_media_texto = 'Aprobado'
            else:
                alumno.nota_media_texto = 'Suspenso'

    empresa_ids = fields.Many2many('fcties.empresa', string='Empresas de Prácticas')

# models/empresa.py
class Empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa Colaboradora'

    name = fields.Char(string='Nombre', required=True)
    persona_contacto = fields.Char(string='Persona de Contacto', required=True)
    telefono_contacto = fields.Char(string='Teléfono de Contacto', required=True)
    correo_electronico = fields.Char(string='Correo Electrónico', required=True)
    direccion = fields.Text(string='Dirección', required=True)

    alumno_ids = fields.Many2many('fcties.alumno', string='Alumnos en Prácticas')

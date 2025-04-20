from odoo import models, fields

class Student(models.Model):
    _name = 'exam.student'
    _description = 'Student'

    name = fields.Char(required=True)
    email = fields.Char()

class Subject(models.Model):
    _name = 'exam.subject'
    _description = 'Subject'

    name = fields.Char(required=True)

class Room(models.Model):
    _name = 'exam.room'
    _description = 'Exam Room'

    number = fields.Char(required=True)

class Supervisor(models.Model):
    _name = 'exam.supervisor'
    _description = 'Supervisor'

    name = fields.Char(required=True)

class Semester(models.Model):
    _name = 'exam.semester'
    _description = 'Semester'

    name = fields.Char(required=True)

class AcademicYear(models.Model):
    _name = 'exam.academicyear'
    _description = 'Academic Year'

    year = fields.Char(required=True)

class ExamType(models.Model):
    _name = 'exam.type'
    _description = 'Exam Type'

    name = fields.Selection([
        ('control', 'Contrôle Continu'),
        ('final', 'Examen Final'),
        ('retake', 'Rattrapage'),
    ], required=True)

class Exam(models.Model):
    _name = 'exam.exam'
    _description = 'Exam'

    student_id = fields.Many2one('exam.student', string='Student')
    subject_id = fields.Many2one('exam.subject', string='Subject')
    room_id = fields.Many2one('exam.room', string='Room')
    supervisor_id = fields.Many2one('exam.supervisor', string='Supervisor')
    semester_id = fields.Many2one('exam.semester', string='Semester')
    year_id = fields.Many2one('exam.academicyear', string='Academic Year')
    type_id = fields.Many2one('exam.type', string='Exam Type')
    date = fields.Date()
    time = fields.Float(string='Time')

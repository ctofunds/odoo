# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class Activity(models.Model):
    _name = 'project_hicto.activity'
    name = fields.Char(string='服务概述')
    project_id = fields.Many2one('project_hicto.project', string='项目')
    company_id = fields.Many2one('res.partner', string='公司', related='project_id.company_id', readonly=True)
    service_item = fields.Many2one('product.product', string='服务项', domain="[('type', '=', 'service')]")
    service_way = fields.Selection([
        ('onsite', '现场'),
        ('remote', '远程'),
        ('prepare', '线下准备')
        ], string="服务形式" )
    activity_start = fields.Datetime(string='开始时间')
    expert_id = fields.Many2one('res.users', string='HiCTO组织者')
    participants = fields.Many2many('res.partner', string='客户参与者', domain="[('is_company', '=', False),('parent_id', '=', company_id)]")
    desc = fields.Html(string='服务详细描述')
    timesheet_ids = fields.One2many('project_hicto.timesheet', 'activity_id', string='工时')

class Timesheet(models.Model):
    _name = 'project_hicto.timesheet'
    _rec_name = 'expert_id'
    activity_id = fields.Many2one('project_hicto.activity', string='服务记录')
    expert_id = fields.Many2one('res.users', string='HiCTO参与者')
    work_hour = fields.Float(string='小时', default=1.0)
    desc = fields.Html(string='工作内容')

class Project(models.Model):
    _name = 'project_hicto.project'
    name = fields.Char(string='项目名称')
    company_id = fields.Many2one('res.partner', string='公司', domain="[('is_company', '=', True), ('id', '!=', 1)]")
    contact_id = fields.Many2one('res.partner', string='客户联系人', domain="[('is_company','=',False), ('parent_id', '=', company_id)]")
    manager_id = fields.Many2one('res.users', string='项目负责人')
    expert_ids = fields.Many2many('res.users', string='项目参与者')
    date_start = fields.Date(string='合同开始时间')
    status = fields.Selection([
        ('open', '进行中'),
        ('close', '已结束')
        ], string='状态', compute='_get_status')
    months = fields.Integer(string='服务时长(月)', default=12)
    desc = fields.Html(string='备注')
    activity_ids = fields.One2many('project_hicto.activity', 'project_id', string='服务记录')

    @api.multi
    def _get_status(self):
        today = fields.Date.today()
        for record in self:
            record.status = 'open' if today < fields.Date.add(record.date_start,months=record.months) else 'close'

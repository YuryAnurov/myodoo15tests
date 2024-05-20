git log - смотрим историю коммитов
git checkout … (код коммита) - переключаемся в detached режиме, можно смотреть
git checkout (branch_name) - возвращаемся

Commits content
----
	step1 - model, menu and views created  - Create Models, Menus, Actions and Views
    8a90e5600bbb6c348188e2592ee990af47579620

	step2 - chatter, tracking fields changes, onchange functions, compute fields, constraints, validation error
    e4133f21ccac078a7d5437cfab3781a646077193 

	step3 -	sequential value, inherit create method, no update attribute, search view 
    732718ec054df993f0bce1bfea08b8cb5ea0524d
    - data directory, noupdate="1", ir.sequence, 
    - search not only by name, but all fields, adding default filters, group by options, addressing search view
    - filter_domain="['|', ('name', 'ilike', self), ('ref', 'ilike', self)]"/>-объединение в поиске нескольких полей
    - Контекст поиска, который будет применен при открытии окна. search_default + filter_childs

    step4 - many2one, rec name, name get function, archive option, web ribbon, many2many
    05096c4ef8c38c32d715cb6f00bcfb52b4aee71b
    - Many2One Field In Odoo,  options="{'no_open': True, 'no_create': True}", Rec Name And Name Get Function, 
    - Icon added, can be .png or .svg 
    - Archive Option And Web Ribbon In Odoo (attrs="{'invisible': [('active', '=', True)]},
    ribbon colors - bg_color="bg-danger")
    - Many2many Field In Odoo (tags)
----
    step1_5 - Default Filter And Group By, web_icon(web_responsive), domain For Menu Action, Default Value Using Context
    52f6725ad009854b786c1f785a10ece58f244321
    now odoo15, new git, for steps 1-4 see odoo16 git
    - web_icon="om_hospital,static/description/icon.png" - в меню айтем
    - <field name="context">{'search_default_filter_male': 1, 'search_default_group_by_gender': 1}</field>
        сортировка и группировка по умолчанию
    - <field name="domain">[('gender', '=','female')]</field>
        из меню Female открывается tree view только c females
    - <field name="context">{'default_gender': 'female'}</field>
        при открытии формы (create) из меню Female в gender по умолчанию стоит female

    step6 - Add Search Panel, Add another Many2one Field, Add Date And Datetime Fields, Set Default Values
    1f07e34d5714db8fe7e00938cc3de848cb75c5d0
    - <searchpanel> <field name="gender" enable_counters="1"/> icon="fa-users" icon="fa-filter" select="multi"
    - new model appointment with many2one
    - date and datetime, + db settings date and time in youtube
https://www.youtube.com/watch?v=ykUB7Y5g6Sc&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=24

    - default date and time, default value for gender versus context
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                              string="Gender", tracking=True, default='female')
https://www.youtube.com/watch?v=TaRRpYnbdLI&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=25

    step7 - Related Fields,  Computed Fields, Onchange Functions. RecName(as in step4)
    62a89382be191a75117604d93900ef74e19fc8c2
    - related - gender = fields.Selection(related='patient_id.gender'), адресуем через many2one поле, все атрибуты
    удаляем, все берется из related, по умолчанию не редактируемое, но если сделать редактируемым - меняет родителя
    - сomputed
https://www.youtube.com/watch?v=NlbdnA6WMd8&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=26

          - не можем использовать не хранимое вычисляемое поле в search view. else обязателен - иначе будет ошибка
            быстро смотрим в базе:
            sudo su postgres - logged into postgres?, psql, \c dev_db (имя бд), select * from hospital_patient;
            если поле не хранимое - в базе его нет (оно есть, т.к. ранее было не хранимое, если удалить модуль и 
            поставить заново - поля age нет, поэтому его и в sarch view использовать нельзя - вычисляется налету
          - чтобы значение age вычислялось сразу же, а не при нажатии save - нужно добавить декоратор 
            @api.depends('date_of_birth') - без него метод запускался только при записи, а с ним - при любом изменении 
            поля
    - onchange
            ref = fields.Char(string="Reference")

            @api.onchange('patient_id')
            def onchange_patient_id(self):
                self.ref = self.patient_id.ref
    - rec name - по умолчанию поле name, если такого поля в модели нет, выбранная запись будет отражаться в хлебных 
    крошках как (модель, id). Можно задать, например так: _rec_name = 'patient_id' и тогда и в этой модели и в других 
    через many2one поле - запись будет отражаться по указанному имени. 

    step8 -  Notebook And Pages, HTML Field, Remove Create/Edit/Delete/Duplicate Options, Priority Widget (Stars)
    ee97e117d645d5fd39b57ef58766032ea4c394f9 
https://www.youtube.com/watch?v=yNuGJYykeSA&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=30
https://www.youtube.com/watch?v=co7891dHjH4&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=30
https://www.youtube.com/watch?v=eqWd2zHSRio&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=32
    
    - notebook and pages - group is mandatory
    - html field
        prescription = fields.Html(string='Prescription')
        <field name="prescription" placeholder="Enter your prescription"/>
    - Remove Create, Edit, Delete and Duplicate Options From Views In Odoo
            <form create="0" delete="0" edit="0">
            <tree create="0" delete="0">
    - Priority Widget (stars)
            priority = fields.Selection([
                ('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string="Priority")
            <field name="priority" widget="priority" class="mr-r"/>
            <h1></h1> - добавит размер

    step 9 - Statusbar, Buttons, Confirmation message on button click, help message for fields/buttons
    06f0b5755250c3a13a49e846d5b5914ef206aca3
https://www.youtube.com/watch?v=Z7nux4M3rrc&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=33
https://www.youtube.com/watch?v=gxF5zpUjLxo&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=34
https://www.youtube.com/watch?v=5ykMlMcUPis&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=35
https://www.youtube.com/watch?v=GRwwboUuzHs&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=36

    - Statusbar 
        в модели  
            state = fields.Selection([('draft', 'Draft'), ('in_consultation', 'In Consultation'),
                        ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status", required=True)
                    default и required - чтобы не было пустых статусо 
        в представлении
                <header>
                    <field name="state" widget="statusbar" nolabel="1" options="{'clickable': '1'}"
                                                        statusbar_visible="draft,in_consultation,done"/>
                </header>
                    statusbar_visible="draft,in_consultation,done" - скрыает статус, если он не выбран для записи
    - Buttons - 2х типов:
        типа object - ищет питон метод в модели, без class="oe_highlight" - будет белая кнопка с черной надписью
        <button name="action_test" string="Test Button" type="object" class="oe_highlight"/>
        типа action - запускает action по id (любой модели) - ссылается на action из patient_views
            <button name="%(om_hospital.action_hospital_patient)d" string="Action Button"
                    type="action" class="oe_highlight"/>
    - Confirmation
        <button name (на любую позицию )
         confirm="Are you sure to open the patient action ?" - перед выплнением будет окно с вопросом
    - help messages
        для поля 
            в питоне ref = fields.Char(string="Reference", help="Reference of the patient from patient record")
            в представлении <field name="booking_date" help="Date of booking"/>
        для кнопок
        <button name="action_test" string="Object Button" type="object"
            help="A message will be printed in the log"
            class="oe_highlight"/>

    step 10  Fix Compute Method Failed To Assign Value Error, Rainbow Effect, Badge Widget And Decorations
    67ee93f63e80558e18468c06406d696158ef6069
https://www.youtube.com/watch?v=Mz35lKuSUX0&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=37
https://www.youtube.com/watch?v=qfUcUSyoXhg&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=38
https://www.youtube.com/watch?v=_7w09OZmfbk&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=39

    Fix Compute Method Failed To Assign Value Error - нет else(у меня в коде было - else требуется с одоо 14 и далее)
        def _compute_age(self):
            today = date.today()
            for rec in self:
                if rec.date_of_birth:
                    rec.age = today.year - rec.date_of_birth.year - (
                            (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
                else:
                    rec.age = 0
    Rainbow Effect - добавляем в питон:
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfully',
                'type': 'rainbow_man',
            }
        }
    добавляем бедж в три вью:
    сам виджет внизу, плюс цвета success - зеленый, danger - красный, info - голубой, muted - серый (без цвета)
    <field name="state"
           decoration-success="state == 'done'"
           decoration-info="state == 'draft'"
           decoration-danger="state == 'in_consultation'"
           decoration-muted="state == 'cancel'"
           widget='badge'/>

    step 11 How To Give Color For Tree View Records In Odoo
    d441544b901b7ea8c1be113aab8f6ae1b2f63b9a
https://www.youtube.com/watch?v=muoreBKSRCk&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=40

    Меняем не виджет, а саму строчку, для этого те же стили что писали в field пишем в tree
        <!--            <tree create="0" delete="0" -->
            <tree
                  decoration-success = "state == 'done'"
                  decoration-danger="state == 'in_consultation'"
                  decoration-muted="state == 'cancel'"
                  decoration-info="state == 'draft'">

    step 12 Widget List Activity

https://www.youtube.com/watch?v=WNZgyRdTrP4&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=41&t=47s

    под формой у одоо мейта были send message, log note и shcedule activity, а у меня не было shcedule activity
    в модели - 
    class HospitalAppointment(models.Model):
        _name = "hospital.appointment"
        # _inherit = 'mail.thread'
        _inherit = ['mail.thread', 'mail.activity.mixin']
    и в форме 
    <div class="oe_chatter">
        <field name="message_follower_ids"/>
        <field name="activity_ids"/>  - этого не было
        <field name="message_ids" options="{'post_refresh': 'recipients'}"/>
    </div>
    Добавим это поле и в лист вью
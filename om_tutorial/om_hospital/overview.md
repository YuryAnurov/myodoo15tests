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

    step1_5 - Default Filter And Group By, web_icon(web_responsive), domain For Menu Action, Default Value Using Context
    now odoo15, new git, for steps 1-4 see odoo16 git
    - web_icon="om_hospital,static/description/icon.png" - в меню айтем
    - <field name="context">{'search_default_filter_male': 1, 'search_default_group_by_gender': 1}</field>
        сортировка и группировка по умолчанию
    - <field name="domain">[('gender', '=','female')]</field>
        из меню Female открывается tree view только c females
    - <field name="context">{'default_gender': 'female'}</field>
        при открытии формы (create) из меню Female в gender по умолчанию стоит female



{
    "name": "Web/URL http Request Default Value",
    "description": """
Usage
=====
    
Default in model

employee_code = fields.Char(
string='Employee ID.',
    default = lambda self: self.env['web.url.httprequest'].get('empid')
)

Url
    /web?debug=&empid=001234#view_type=form&model=hr.employee&action=348
    
        """,
    "version": "8.0",
    "author": "Jakkrich.cha",
    "website": "",
    "category": "Tools",
    "depends": ["web"],
    "data": [],
    "auto_install": False,
}

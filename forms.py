from wtforms import Form, StringField, SelectField, validators

class GPUSearchForm(Form):
    choices = [('Brand', 'Price')]
    select = SelectField('Search for Matches:', choices=choices)
    search = StringField('')
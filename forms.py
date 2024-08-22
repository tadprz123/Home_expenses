from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class TransactionForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    type = SelectField('Type', choices=[('income', 'Income'), ('expense', 'Expense')], validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    amount = DecimalField('Amount', places=2, validators=[DataRequired(), NumberRange(min=0)])
    currency = SelectField('Currency', choices=[('PLN', 'PLN'), ('USD', 'USD'), ('EUR', 'EUR')], validators=[DataRequired()])
    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ExpenseForm(FlaskForm):
    category = StringField("Category", validators=[DataRequired(), Length(min=1, max=50)])
    amount = DecimalField("Amount", validators=[DataRequired(), NumberRange(min=0.01)])
    description = TextAreaField("Description", validators=[Length(max=200)])
    submit = SubmitField("Add Expense")
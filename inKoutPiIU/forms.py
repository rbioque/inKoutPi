from django import forms

class ConfigForm(forms.Form):
	tem_max = forms.DecimalField(label='Temperatura máxima', max_digits=4, decimal_places=2, max_value=35.00, min_value=25.00, localize=True)
	tem_min = forms.DecimalField(label='Temperatura mínima', max_digits=4, decimal_places=2, max_value=35.00, min_value=25.00, localize=True)
	hum_max = forms.DecimalField(label='Humedad máxima', max_digits=5, decimal_places=2, max_value=120.00, min_value=0.00, localize=True)
	hum_min = forms.DecimalField(label='Humedad mínima', max_digits=5, decimal_places=2, max_value=120.00, min_value=0.00, localize=True)

class ConfigAlertForm(forms.Form):
        tem_alert_max = forms.DecimalField(label='Temperatura máxima', max_digits=4, decimal_places=2, max_value=35.00, min_value=25.00, localize=True)
        tem_alert_min = forms.DecimalField(label='Temperatura mínima', max_digits=4, decimal_places=2, max_value=35.00, min_value=25.00, localize=True)
        hum_alert_max = forms.DecimalField(label='Humedad máxima', max_digits=5, decimal_places=2, max_value=120.00, min_value=0.00, localize=True)
        hum_alert_min = forms.DecimalField(label='Humedad mínima', max_digits=5, decimal_places=2, max_value=120.00, min_value=0.00, localize=True)
        mail_alert = forms.EmailField(label='Correo')

from django import forms

select_service = 'Select Service'
air_freight = 'Air Freight'
shipping_cargo = 'Shipping Cargo'
retail_cargo = 'Retail Cargo'
warehousing = 'Warehousing'

KG_WEIGHT = 'Weight KG'
KG_100 = '100kg'
KG_200 = '200kg'
KG_300 = '300kg'
KG_400 = '400kg'
KG_500 = '500kg'
KG_600 = '600kg'
KG_700 = '700kg'


QUOTE_FORM_DATA = {
    'services': [
        (select_service, select_service),
        (air_freight, air_freight),
        (shipping_cargo, shipping_cargo),
        (retail_cargo, retail_cargo),
        (warehousing, warehousing),
    ],

    'weight': [
        (KG_WEIGHT, KG_WEIGHT),
        (KG_100, KG_100),
        (KG_200, KG_200),
        (KG_300, KG_300),
        (KG_400, KG_400),
        (KG_500, KG_500),
        (KG_600, KG_600),
        (KG_700, KG_700),
    ]
}

class TrackingForm(forms.Form):
    tracking_code = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Tracking id'
        }),
        max_length=100,
        )

class QuoteForm(forms.Form):
    service = forms.CharField(widget=forms.Select(
        choices=QUOTE_FORM_DATA['services'],
        attrs={'class': 'custom-select'},
        ))
    length = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Length cm'}), max_length=100)
    height = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Height cm'}), max_length=100)
    from_country = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Shipment location',
            }), max_length=100)
    to_country = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Shipment destination'}), max_length=100)
    weight = forms.CharField(widget=forms.Select(
        choices=QUOTE_FORM_DATA['weight'],
        attrs={'class': 'custom-select'},
    ))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address'}), max_length=100)

    is_door_to_door = forms.CharField(
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
            'id': 'customCheck1'}), required=False)

    is_mailbox = forms.CharField(
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
            'id': 'customCheck2'}), required=False)

    is_pickup = forms.CharField(
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
            'id': 'customCheck3'}), required=False)

    is_warehousing = forms.CharField(
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-control-input',
            'id': 'customCheck4'}), required=False)
    
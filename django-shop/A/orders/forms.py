from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, initial=1)


class CouponApplyForm(forms.Form):
    code = forms.CharField()

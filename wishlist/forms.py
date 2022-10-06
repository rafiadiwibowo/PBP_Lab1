from django import forms
from wishlist.models import BarangWishlist

class FormTask(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = {"nama_barang", "harga_barang", "deskripsi"}
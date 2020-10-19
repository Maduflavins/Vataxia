from django.urls import path
from .views.invitation import InvitationView
from .views.transfer import TransferView
from .views.wallet import WalletDetail

app_name="credits"
urlpatterns = [

    # Invitations
    path('invitations/', InvitationView.as_view(), name='invitations'),

    # Transfers
    path('transfers/', TransferView.as_view(), name='transfers'),

    # Wallets
    path('wallets/<user_id>/', WalletDetail.as_view(), name='wallets'),

]

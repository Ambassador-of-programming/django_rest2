from rest_framework import serializers

from mainapp.models import Shop, Ticket

from mainapp.send_gmail import send_msg



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id', 'shop', 'name',
            'price',
            'replace_from', 'replace_to',
        )


class ShopSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(read_only=True, many=True)
    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'time_start', 'status',
            'time_end', 'address', 'tickets',
            'avg_ticket_price',
            'min_ticket_price',
            'max_ticket_price',
            'amount_ticket',
            'sum_ticket_price',
        )

    def create(self, validated_data):
        user = self.context.get('request').user
        send_msg(user.email, validated_data.get('name'), user.username)
        return super().create(validated_data)

 
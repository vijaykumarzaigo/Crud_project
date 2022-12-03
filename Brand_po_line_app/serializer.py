from rest_framework import serializers
from.models import Po_line_item


class Brand_po_line_item_serializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"start_date": "Start Date should not be greater than End Date."})

        return data
    class Meta:
        model = Po_line_item
        fields = ['id', 'line_item_id','state', 'city', 'type_quantity', 'sub_type', 'quantity', 'start_date', 'end_date',
                  'unit_line_price_amount']

from rest_framework import serializers
from django.utils import timezone

from agenda.models import Agendamento


class AgendamentoSerializer(serializers.Serializer):

    class Meta:
        model = Agendamento
        fields = ['id','data_horario','nome_cliente','email_cliente', 'telefone_cliente']
    
    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Agendamento não pode ser feto no passado!")
        return value

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente", "")

        if email_cliente.endswith(".br") and telefone_cliente.startswith("+") and not telefone_client.startswith("+55"):
            raise serializers.ValidationError("E-mail brasileinro deve estar associado a um numero do Brasil (+55)")
        return attrs
  
   
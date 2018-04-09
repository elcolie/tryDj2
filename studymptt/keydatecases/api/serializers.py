from rest_framework import serializers

from keydatecases.models import KeyDateCase, ICD10, CaseICD10Connection


class KeyDateCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyDateCase
        fields = [
            'id',
            'name',
            'diagnose_all_icd_10',
        ]
        read_only_fields = ['id', 'diagnose_all_icd_10']


class ICD10Serializer(serializers.ModelSerializer):
    class Meta:
        model = ICD10
        fields = [
            'primary_key_number',
            'star_key_number',
            'additional_key_number',
            'preferred_short_description',
        ]


class CaseICD10ConnectionSerializer(serializers.ModelSerializer):
    case = KeyDateCaseSerializer()
    icd_10 = ICD10Serializer()

    class Meta:
        model = CaseICD10Connection
        fields = [
            'case',
            'icd_10',
            'is_primary',
            'certainty',
        ]

    def create(self, validated_data) -> CaseICD10Connection:
        # import ipdb;
        # ipdb.set_trace()
        # create key_date_case
        key_date_case = KeyDateCase.objects.create(**validated_data.get('case'))

        # create icd10
        icd10 = ICD10.objects.create(**validated_data.get('icd_10'))

        # create connection
        conn = CaseICD10Connection.objects.create(
            case=key_date_case, icd_10=icd10, is_primary=validated_data.get('is_primary'),
            certainty=validated_data.get('certainty')
        )
        return conn

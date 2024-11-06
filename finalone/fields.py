from rest_framework import serializers
import re

class PhoneNumberField(serializers.Field):
    def to_representation(self, value):
        """Format the phone number for display."""
        return f"({value[:3]}) {value[3:6]}-{value[6:]}" if value else ""

    def to_internal_value(self, data):
        """Validate and clean the phone number before saving."""
        # Only allow digits and ensure length is correct
        cleaned_data = re.sub(r'\D', '', data)  # Remove non-digit characters
        if len(cleaned_data) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits long.")
        return cleaned_data
from rest_framework import serializers
from .models import CommitteeMember, SocialMedia

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'platform', 'handle')

class CommitteeMemberSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerializer(many=True)  # related_name="social_media"

    class Meta:
        model = CommitteeMember
        fields = ('id', 'name', 'position', 'started_from', 'tenure', 'memberPhoto', 'social_media')
        
    def create(self, validated_data):
        social_media_data = validated_data.pop('social_media')
        print("Social Media Data:", social_media_data)
        member = CommitteeMember.objects.create(**validated_data)
        print("Created Member:", member)
        for sm in social_media_data:
            print("Creating Social Media for Member:", sm)
            SocialMedia.objects.create(user=member, **sm)
        return member

    def update(self, instance, validated_data):
        social_media_data = validated_data.pop('social_media', None)
        print("Updating Member:", instance)
        # Update member fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            print(f"Updated {attr} to {value} of Member:", instance)
        instance.save()

        if social_media_data:
            # Clear existing social links
            instance.social_media.all().delete()
            for sm in social_media_data:
                print("Creating Social Media for Updated Member:", sm)
                SocialMedia.objects.create(user=instance, **sm)

        return instance

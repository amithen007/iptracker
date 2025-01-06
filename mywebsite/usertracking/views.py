# usertracking/views.py
import geocoder
from django.shortcuts import render
from .models import Visitor


def track_visitor(request):
    # Get the IP address of the visitor
    ip_address = request.META.get('REMOTE_ADDR')

    # Fetch geolocation details using geocoder
    g = geocoder.ip(ip_address)

    # Ensure all fields have a fallback value to prevent IntegrityError
    Visitor.objects.create(
        ip_address=ip_address,
        hostname=g.hostname if g.hostname else 'Not available',
        city=g.city if g.city else 'Not available',
        region=g.region if hasattr(g, 'region') else 'Not available',
        country=g.country if g.country else 'Not available',
        country_code=g.country_code if hasattr(g, 'country_code') else 'Not available',
        latitude=g.latlng[0] if g.latlng else None,
        longitude=g.latlng[1] if g.latlng else None,
        timezone=g.timezone if hasattr(g, 'timezone') else 'Not available',
        postal_code=g.postal if hasattr(g, 'postal') else 'Not available',
        organisation=g.org if hasattr(g, 'org') else 'Not available'  # Ensure fallback value
    )

    # Prepare the data for rendering the response
    geolocation_info = {
        "IP Address": g.ip,
        "Hostname": g.hostname if g.hostname else "Not available",
        "City": g.city if g.city else "Not available",
        "Region": g.region if hasattr(g, 'region') else "Not available",
        "Country": g.country if g.country else "Not available",
        "Country Code": g.country_code if hasattr(g, 'country_code') else "Not available",
        "Latitude": g.latlng[0] if g.latlng else "Not available",
        "Longitude": g.latlng[1] if g.latlng else "Not available",
        "Timezone": g.timezone if hasattr(g, 'timezone') else "Not available",
        "Postal Code": g.postal if hasattr(g, 'postal') else "Not available",
        "Organisation": g.org if hasattr(g, 'org') else "Not available"
    }

    # Render the template and pass the geolocation details
    return render(request, 'usertracking/index.html', {'geolocation_info': geolocation_info})



def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'usertracking/visitor_list.html', {'visitors': visitors})

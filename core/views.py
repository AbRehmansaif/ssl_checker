# from django.shortcuts import render
# from .utils import check_website
# import pandas as pd


# def home(request):
#     results = []

#     if request.method == "POST":
#         urls = request.POST.get("urls").split()
#         for url in urls:
#             if not url.startswith("http"):
#                 url = "https://" + url
#             result = check_website(url)
#             results.append(result)

#         # CSV Export
#         df = pd.DataFrame(results)
#         df.to_csv("website_report.csv", index=False)

#     return render(request, "core/home.html", {"results": results})


from django.shortcuts import render
from .utils import check_website
from .models import WebsiteCheck  # ✅ Import your model
import pandas as pd
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import csv


def home(request):
    results = []
    validator = URLValidator()

    if request.method == "POST":
        urls = request.POST.get("urls").split()
        for url in urls:
            # Add protocol if missing
            if not url.startswith("http"):
                url = "https://" + url

            # ✅ Validate URL before processing
            try:
                validator(url)
            except ValidationError:
                results.append({
                    "url": url,
                    "status": "Invalid URL",
                    "ssl_days_left": None
                })
                continue

            # Get result from your utils.py
            result = check_website(url)
            results.append(result)

            # ✅ Save result in DB
            WebsiteCheck.objects.create(
                url=result["url"],
                status_code=result.get("status"),
                ssl_expiry_days=result.get("ssl_days_left")
            )

        # ✅ Export all checked results as CSV
        df = pd.DataFrame(results)
        df.to_csv("website_report.csv", index=False)

    return render(request, "core/home.html", {"results": results})


def download_report(request):
    # Query all WebsiteCheck objects
    checks = WebsiteCheck.objects.all().order_by('-checked_at')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=website_report.csv'
    writer = csv.writer(response)
    writer.writerow(['url', 'status_code', 'ssl_expiry_days', 'checked_at'])
    for check in checks:
        writer.writerow([check.url, check.status_code, check.ssl_expiry_days, check.checked_at])
    return response

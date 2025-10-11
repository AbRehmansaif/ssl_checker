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


def home(request):
    results = []

    if request.method == "POST":
        urls = request.POST.get("urls").split()
        for url in urls:
            # Add protocol if missing
            if not url.startswith("http"):
                url = "https://" + url

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

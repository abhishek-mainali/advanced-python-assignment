# 1. Product Prices - filter, map, lambda
prices = [20, 55, 80, 45, 120, 60]
filtered_prices = filter(lambda p: p >= 50, prices)
discounted_prices = list(map(lambda p: p * 0.9, filtered_prices))
print("Discounted Prices:", discounted_prices)


# 2. Employee Work Hours
hours = [35, 40, 45, 50, 38, 60]
overtime = list(map(lambda h: h - 40, filter(lambda h: h >= 40, hours)))
print("Overtime Hours:", overtime)


# 3. Customer Feedback
feedback = ["Great service!", "Loved it, will come again.", "Good", "Excellent experience, very satisfied!"]
filtered_feedback = filter(lambda f: len(f) >= 20, feedback)
lower_feedback = list(map(lambda f: f.lower(), filtered_feedback))
print("Processed Feedback:", lower_feedback)

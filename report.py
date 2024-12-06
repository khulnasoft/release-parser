import time

from src.common import releaselog

products = releaselog.list_products()
count_auto = len([product for product in products if product.auto_configs()])

print(f"As of {time.strftime('%Y-%m-%d')}, {count_auto} of the {len(products)} products"
      f" tracked by releaselog have automatically tracked releases:")
print()
print('| Product | Permalink | Auto | Method(s) |')
print('|---------|-----------|------|-----------|')
for product in products:
    title = product.get_title()
    permalink = product.get_permalink()
    auto = '✔️' if product.has_auto_configs() else '❌'
    methods = ', '.join(sorted({config.method for config in product.auto_configs()}))
    print(f"| {title} | [`{permalink}`](https://releaselog.netlify.app{permalink}) | {auto} | {methods} |")
print()
print('This table has been generated by [report.py](/report.py).')

# Decision Table – Promo Code Creation

| Conditions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| Promo code unique | Yes | No | Yes | Yes |
| Discount value valid | Yes | Yes | No | Yes |
| Date range valid | Yes | Yes | Yes | No |

| Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| Promo code created | ✔ | ✘ | ✘ | ✘ |
| Show duplicate error | ✘ | ✔ | ✘ | ✘ |
| Show validation error | ✘ | ✘ | ✔ | ✔ |


# Decision Table – VIP Discount Rules

| Conditions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| Customer is VIP | Yes | Yes | No | No |
| Order amount > 100€ | Yes | No | Yes | No |

| Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| 20% discount | ✔ | ✘ | ✘ | ✘ |
| 10% discount | ✘ | ✔ | ✘ | ✘ |
| 5% discount | ✘ | ✘ | ✔ | ✘ |
| No discount | ✘ | ✘ | ✘ | ✔ |

## Explanation

| Case | Result |
|---|---|
| VIP and order > 100€ | 20% discount |
| VIP and order ≤ 100€ | 10% discount |
| Non‑VIP and order > 100€ | 5% discount |
| Non‑VIP and order ≤ 100€ | No discount |

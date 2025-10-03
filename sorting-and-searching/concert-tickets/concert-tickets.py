from bisect import bisect_right
from sortedcontainers import SortedList


def concert_tickets(
    n_tickets: int,
    ticket_prices: list[int],
    m_customers: int,
    customer_prices: list[int],
):

    if not (1 <= n_tickets <= 200000):
        print("number of tickets must be between 1 and 200000")
        return
    if not (1 <= m_customers <= 200000):
        print("number of customers must be between 1 and 200000")
        return
    if len(ticket_prices) != n_tickets:
        print("number of tickets and length of ticket_prices do not match")
        return
    if len(customer_prices) != m_customers:
        print("number of customers and length of customer_prices do not match")
        return

    tickets = SortedList(ticket_prices)

    for customer_price in customer_prices:
        idx = tickets.bisect_right(customer_price) - 1

        if idx >= 0:
            chosen_ticket = tickets[idx]
            print(chosen_ticket)
            tickets.pop(idx)
        else:
            print(-1)


concert_tickets(5, [5, 3, 7, 8, 5], 3, [4, 8, 3])

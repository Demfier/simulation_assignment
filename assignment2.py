"""
Author: Gaurav Sahu, 18/01/2018 16:47:17

Problem Statement: Simulation of an Inventory system.

Retail store selling automobile types.
Aim: To adopt an optimum policy for ordering new supplies

Notations:
    D = Demands per day
    P = Reorder point (constant)
    Q = Reorder quantity (fixed)
    S = Stock

Rules:
    - If Stock <= P, order Q items
    - If D > S => (sales loss)
      else => carry_over cost

Assumptions:

a) Lead Time = 3 days (If order placed on 10th, will get on 13th)
b) Carrying cost per day per unit = 0.75 Rs.
c) Loss per unit out of stock = 18 Rs.
d) Ordering cost per order = 75 Rs. (inclusive of transportation cost)
e) Demand in a day is between 0-99
f) There is never more than one replenishment order
g) Initial Conditions:
    S = 115 units, no outstanding order

Select the best policy out of the 5 given alternatives after operating for 180
days.
"""

import random
import operator

POLICIES = [(125, 150),
            (125, 250),
            (150, 250),
            (175, 250),
            (175, 300)]  # set of P (Reorder Point) and Q (Reorder Quantity)

LEAD_TIME = 3  # days
CPD = 0.75  # Carrying cost per day per unit in rupees
LPS = 18  # Loss per unit out of stock in rupees
OC = 75  # Ordering cost per order in rupees

S = 115  # Stocks in units
TOTAL_SIMULATION_PERIOD = 180  # days
POLICY_COST = []  # List of tuples to store policy id and the cost incurred


def place_order(day, order_quantity, repl_order):
    """Place order in queue and returns the order tuple"""
    if repl_order is None:
        repl_order = (day, order_quantity)
    return(repl_order)

for policy_id, policy in enumerate(POLICIES):
    repl_order = None  # Replenishment order, can't be > 1 orders at a time
    total_cost = 0
    (P, Q) = policy
    for day in range(TOTAL_SIMULATION_PERIOD):
        if repl_order and day == repl_order[0] + 3:
            S += repl_order[1]  # Stock replenished
            repl_order = None  # empty order queue
        D = random.randint(0, 99)  # Demand in a day
        S -= D  # subtract demand from current stock
        if S <= P:
            repl_order = place_order(day, Q, repl_order)
            total_cost += OC  # Add ordering cost
        if D > S:
            total_cost += LPS * (D - S)  # Add sales cost
        else:
            total_cost += CPD * S  # Add carry over cost
    POLICY_COST.append((policy_id, total_cost))

(bestpolicy_id, bestpolicy_cost) = min(POLICY_COST, key=operator.itemgetter(1))
print("The policy with Reorder point(P)=%d & Reorder quantity(Q)=%d is the"
      "best policy with a total cost of Rs %d\n" % (POLICIES[bestpolicy_id][0],
                                                    POLICIES[bestpolicy_id][1],
                                                    bestpolicy_cost))

print("--"*15)
print("The various policies and their total cost is enumerated:")
print("--"*15)
for p_id, cost in POLICY_COST:
    print("(P, Q)=(%d, %d) COST=%d" % (POLICIES[p_id][0],
                                       POLICIES[p_id][1],
                                       cost))

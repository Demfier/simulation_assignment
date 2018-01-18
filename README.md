# simulation_assignment

Solution to all the assignments given in the Simulation course (IM31006)

# Assignments:
  ## 1. [Fighter-Target Problem](assignment1.py):

The initial co-ordinate of a fighter plane is given which is supposed to hit a bombing site. The bombing site is moving and its co-ordinates at 1 second interval are given. If the velocity of the bomb is 20 kmph and it is always directed towards the bombing site, determine whether the bomb will hit the bombing site successfully or not.

**Note**: The bomb would be said to successfully hit the target if it is within 10km proximity of the target at a point of time.

  ## 2. [Simulation of an Inventory system](assignment2.py):

Retail store selling automobile types.<br>
  **Aim**: To adopt an optimum policy for ordering new supplies.

  **Notations**:
  - D = Demands per day
  - P = Reorder point (constant)
  - Q = Reorder quantity (fixed)
  - S = Stock

   **Rules**:
   - *If* Stock <= P, order Q items
   - *If* D > S => (sales loss) *else* => carry_over cost

  **Assumptions**:
  1. Lead Time = 3 days (If order placed on 10th, will get on 13th)
  2. Carrying cost per day per unit = 0.75 Rs.
  3. Loss per unit out of stock = 18 Rs.
  4. Ordering cost per order = 75 Rs. (inclusive of transportation cost)
  5. Demand in a day is between 0-99
  6. There is never more than one replenishment order
  7. Initial Conditions: S = 115 units, no outstanding order<br>
  Select the best policy out of the 5 given alternatives after operating for 180 days.


# Feedback Relevance Analysis
# Prof. Barankay's Comments vs. Current Paper Direction

The current paper is now framed as a direct extension of Farboodi, Singal, Veldkamp, and
Venkateswaran (2021), "Valuing Financial Data." This reframing changes the relevance of each
piece of feedback materially. Below is a point-by-point assessment.

---

## Reading List Recommendations

### Admati and Pfleiderer (1986), "A Monopolistic Market for Information" — HIGHLY RELEVANT

This is now the most important new paper to incorporate. Farboodi et al. (2021) explicitly
acknowledge that their procedure yields private value, not a transaction price, and they do not
model the seller's problem. Admati and Pfleiderer directly fill that gap: they model a monopolist
data vendor choosing a price and licensing scope to maximize revenue, and show that the vendor
may optimally add noise to the signal to prevent arbitrage from eroding its value. This maps
precisely onto the paper's Section 5 ("From Value to Price") and the extensions on exclusivity
vs. shared access. **Add this to the literature review and use it as the theoretical backbone of
Section 5.**

### Farboodi, Matray, Veldkamp, and Venkateswaran (2022), "Where Has All the Data Gone?" — HIGHLY RELEVANT

This 2022 follow-on paper by three of the same authors as the 2021 paper provides the general
equilibrium model of the "data economy" that the 2021 paper defers. It formalizes how data
diffusion changes price informativeness and returns to information. This is the closest existing
work to the crowding and alpha decay mechanisms that distinguish this paper from the 2021
version. **Read this before finalizing Section 6 (competitive adoption and alpha decay). It should
be cited prominently and differentiated from carefully — the question is what this paper adds
beyond what the 2022 paper does.**

### Kyle (1985), "Continuous Auctions and Insider Trading" — HIGHLY RELEVANT

The Kyle Lambda (λ) is the standard tool for modeling how informed trades move prices.
It is the right formal instrument for the crowding channel: as n investors trade on the same
signal, aggregate informed order flow grows, λ rises (or equivalently, the per-investor price
impact on their trades increases), and the economic value of the signal falls. Farboodi et al.
(2021) already reference Kyle (1989) and Kacperczyk, Nosal, and Sundaresan (2021) for the
imperfect competition extension. **This paper should use the Kyle framework to formalize
V_i(D, n) as decreasing in n via the price impact channel.** This is the mathematical
vocabulary that the professor said was needed.

### Dessaint, Foucault, Fresard, and Matray (2021), "No News is Bad News" — MODERATELY RELEVANT

This paper provides an empirical methodology for measuring information depletion and its
market efficiency consequences. It is not a core theoretical input, but it offers a useful
empirical analogy and template if the paper adds an illustrative empirical section. Given
the paper is explicitly theoretical, incorporate this as a footnote or motivating example
rather than a primary reference. **Lower priority — address only after the model sections
are complete.**

---

## Methodological Recommendations

### Transition to a Rational Expectations Equilibrium (REE) Framework — HIGHLY RELEVANT

The professor's recommendation to adopt an explicit REE framework is directly aligned with
the Farboodi et al. (2021) extension framing. Their model is a noisy rational expectations
model — prices partially reveal private signals, and investors update beliefs using both their
own data and market prices. Since this paper builds on that structure, the model setup should
use the same REE foundation, then add the n-investor adoption layer on top. **This is not a
new direction; it is the correct way to extend the Farboodi et al. framework. The paper should
make this explicit in Section 3.**

### Formalize the Alpha Decay Mechanism via a Capacity Constraint — HIGHLY RELEVANT

The professor's suggestion to introduce a "capacity constraint" variable distinguishing
high-frequency signals (low capacity, fast decay) from fundamental signals (high capacity,
slow decay) is a clean contribution that neither Farboodi et al. (2021) nor the 2022 paper
formalizes in this way. **This should become a first-order object in the model.** Define
a dataset capacity parameter C(D) such that V_i(D, n) falls faster in n when C(D) is low.
This gives comparative statics that are both analytically tractable and empirically meaningful.

### Empirical Validation via Simulated Anomaly Decay — PARTIALLY RELEVANT

The professor suggests using an existing anomaly (e.g., Post-Earnings Announcement Drift)
and simulating Sharpe Ratio decay as the number of artificial users increases. This is
feasible and would strengthen the paper. However, given the paper is explicitly theoretical,
this is best treated as an illustrative numerical example rather than a formal empirical test.
**Include as a calibrated example in Section 4 or 5, not as a separate empirical section.**

---

## Framing and Structural Recommendations

### The Information Seller's Paradox as the Central Tension — HIGHLY RELEVANT

The professor frames the core problem as: "If the seller sells to too many, the data becomes
worthless; if too few, revenue is too low. What is the optimal subscriber count?" This is
exactly the content of Section 5 and is sharper and more memorable than the current framing.
**Use this as the organizing tension for the introduction and Section 5.**

### Replace "To Do" Lists with Actual Propositions — HIGHLY RELEVANT, ALREADY PLANNED

This is urgent. The current draft lists what propositions will say, not what they actually are.
The sections below in the full paper draft replace those lists with formal proposition statements.

### Justify Economic Value over Predictive Power — ALREADY CENTRAL, NEEDS SHARPER STATEMENT

The paper already makes this point. What it needs is a concrete quantitative illustration —
e.g., a dataset with R² = 0.90 but V_i(D) = 0 because crowding costs exceed gains. **Add
a numerical example with this structure in Section 4.**

### Standardize References — ROUTINE

Add Admati-Pfleiderer (1986), Farboodi et al. (2022), and Kyle (1985) to the bibliography.
Ensure all entries include journal name, volume, and page numbers.

---

## Summary: Priority Order for Incorporating Feedback

| Item | Relevance | Action |
|---|---|---|
| Admati-Pfleiderer (1986) | High | Add to lit review; anchor Section 5 |
| Farboodi et al. (2022) | High | Read, cite, differentiate carefully |
| Kyle (1985) | High | Use Lambda for crowding formalization |
| REE framework | High | Already implicit; make explicit in Section 3 |
| Capacity constraint | High | New variable in the model |
| Information seller's paradox | High | Reframe Section 5 around this tension |
| Formalize propositions | High | Done in full paper draft |
| Dessaint et al. (2021) | Moderate | Footnote or motivating example |
| Empirical simulation | Moderate | Numerical calibration example only |
| Reference formatting | Low | Housekeeping |

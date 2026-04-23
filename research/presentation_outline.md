# Presentation Outline — Paper Proposal
## Valuing and Pricing Financial Datasets
### Bailey McIntosh | Wharton Research Scholars | April 2026
### Target: 10 minutes (~8 slides, ~1–1.5 min each)

---

## Slide 1 — Title (30 sec)

**Valuing and Pricing Financial Datasets: From Predictive Power to Economic Value**

Bailey McIntosh | Wharton Research Scholars

*No talking points needed. Use this to settle in and state the one-sentence version: "I want to understand how financial datasets should be priced — not just for individual investors, but as a market."*

---

## Slide 2 — Research Question + Motivation (1.5 min)

**Header:** How should a financial dataset be priced?

**Bullet points:**
- The alternative data market is now >$8B annually and growing
- Investment firms increasingly compete on *data*, not just modeling — quantitative methods have diffused broadly, compressing the alpha from modeling skill alone
- Data markets are now the primary mechanism through which private financial information gets allocated into prices
- Yet these markets are almost entirely private and opaque — no publicly observable prices, no standard contracts, no theory of how they work

**The question has two parts:**
1. What is a dataset worth to a single investor?
2. How does a data vendor set a price — and to how many buyers?

*Talking point: emphasize that data markets are economically enormous and theoretically understudied. The opacity is the motivation for theory, not a limitation of the paper.*

---

## Slide 3 — Why It's Not Obvious (1.5 min)

**Header:** The intuitive answer is wrong

**The naive answer:** Pay up to the expected alpha the data generates.

**Three reasons this fails:**

1. **Statistical accuracy ≠ economic value.** A dataset with 90% out-of-sample R² for earnings prediction can be worthless if the tradeable market is too small or price impact absorbs all gains.

2. **Private value ≠ market price.** The vendor has market power; buyers are heterogeneous. The transaction price is set by the interaction between them — not by any individual's willingness to pay.

3. **Value is endogenous to adoption.** As more investors buy and trade on the same signal, they collectively reveal it to the market faster. The dataset's value depends on how many other people own it.

**The punchline:** Information markets have an *inverted network effect* — most goods become more valuable with more users; financial data becomes less valuable.

*Talking point: the inverted network effect is the conceptual hook. State it clearly and let it land.*

---

## Slide 4 — Contribution (1 min)

**Header:** Three steps beyond the existing literature

The closest prior work — Farboodi, Singal, Veldkamp, and Venkateswaran (2021) — derives how much a dataset is worth to a *single investor*, using sufficient statistics. They explicitly set aside two questions. This paper takes both of those next steps, plus a third.

**Contribution 1:** Bridge from observable statistical metrics (out-of-sample R², MSE reduction) to the signal precision parameters that determine economic value. Makes the existing valuation framework computable from numbers practitioners actually have.

**Contribution 2:** Derive equilibrium *transaction prices*, not just private values — the vendor's optimal licensing problem: how many licenses to sell, and at what price.

**Contribution 3:** Make competitive adoption a first-order mechanism. As n investors share and trade the same signal, crowding erodes its value for all holders. Introduce *dataset capacity* as the rate at which this erosion occurs.

*Talking point: be clear that you are building on Farboodi et al., not competing with it. You are doing the steps they said needed doing.*

---

## Slide 5 — Literature (1 min)

**Header:** Five strands, one gap

*Don't list papers — show the structure of the field.*

| Strand | Key insight | Role in this paper |
|---|---|---|
| Costly information | Grossman-Stiglitz (1980): informed investors must earn rents or no one gets informed | Why datasets have positive value at all |
| Data valuation | Farboodi et al. (2021): private value reducible to sufficient statistics | Direct foundation; this paper extends it |
| Information monopoly | Admati-Pfleiderer (1986): seller balances price vs. adoption | Vendor's pricing framework |
| Crowding & decay | Kyle (1985), Holden-Subrahmanyam (1992), McLean-Pontiff (2016) | Micro-foundation for value erosion with n |
| Club goods | Buchanan (1965): optimal club size under congestion | Structure of the n* optimization |

**The gap:** No existing paper derives a market transaction price for data that accounts for both investor heterogeneity and endogenous value erosion from shared adoption.

*Talking point: you don't need to explain each paper. The table shows you know the field. Spend your words on the gap.*

---

## Slide 6 — Model and Methods (1.5 min)

**Header:** Theory: how the model is built

*This is a theoretical paper. "Methods" = model structure and propositions.*

**Setup:**
- N risky assets; overlapping-generations CARA investors, heterogeneous in AUM, risk aversion, and investment style
- Dataset D produces a Gaussian signal about dividend innovations with precision K(D)
- Market equilibrium via noisy rational expectations (Farboodi et al. framework)

**Three modeling components:**

1. **Prediction-precision bridge.** Maps the observable ΔR² of a dataset to the signal precision K(D) that enters the valuation formula. Connects what practitioners measure to what the theory uses.

2. **Private value formula.** Closed-form expression: value is proportional to AUM, decreasing in risk aversion, convex in ΔR², decreasing in implementation cost. Heterogeneous across investors.

3. **Crowding mechanism.** n investors sharing the same signal trade more aggressively (Holden-Subrahmanyam 1992), increasing the Kyle price impact coefficient λ(n), reducing each investor's extractable profit. Dataset *capacity* C(D) parametrizes how fast this erosion occurs — derived from how detectable aggregate informed order flow is in the tradeable universe.

**Key constructs:** signal quality (ΔR²), capacity (C(D)), adoption (n), investor heterogeneity (AUM, style, existing data).

---

## Slide 7 — Key Results (1.5 min)

**Header:** What the model delivers

**Proposition 1 — Optimal licensing:** The vendor maximizes revenue by selling n* = (C(D)+1)/2 licenses. Optimal n* is increasing in capacity. Very low-capacity datasets should be licensed exclusively; broad fundamental datasets can sustain many buyers.

**Proposition 3 — Information seller's paradox:** A dataset with high predictive accuracy (ΔR² near 1) can have zero or negative economic value when capacity is low and adoption is broad. Statistical power is necessary but not sufficient for economic value.

**Key comparative statics:**
- Total vendor revenue is increasing in *both* signal quality and capacity — a moderately accurate, high-capacity dataset can generate more revenue than a highly accurate, low-capacity one
- Large investors (high AUM) are *more* sensitive to crowding than small investors — their advantage narrows as n grows
- The vendor's optimal policy is to restrict n, which also solves the prisoner's dilemma among buyers (each individually would trade too aggressively; exclusivity forces the cooperative pace)

*Talking point: the paradox result is the most counterintuitive and the most useful for practitioners. Lead with it.*

---

## Slide 8 — Next Steps (1 min)

**Header:** What comes next

**Immediate (this paper):**
- Derive C(D) from Kyle/Holden-Subrahmanyam primitives rather than imposing the functional form — replaces a free parameter with a derived object
- Solve the heterogeneous-investor vendor problem fully (demand curve for data, optimal price discrimination)
- Add dynamic adoption section: alpha lifecycle as n grows endogenously (McLean-Pontiff as empirical anchor)

**Extensions (potentially separate paper):**
- Equilibrium under algorithmic trading: AI traders can implicitly collude on the cooperative trading pace (Goldstein and Dou), sustaining value at larger n — the optimal n* is increasing in how algorithmic the buyer pool is
- Incentives to produce new datasets: which datasets get created in equilibrium?
- Empirical implications: map propositions to observable proxies (comomentum, 13F similarity, post-publication alpha decay)

**The thesis direction:** A complete theory of data market equilibrium — private value, transaction price, adoption dynamics, and vendor strategy — that can serve as the benchmark model for empirical work as data market observability improves.

---

## Timing guide

| Slide | Content | Time |
|---|---|---|
| 1 | Title | 0:30 |
| 2 | Research question | 1:30 |
| 3 | Why not obvious | 1:30 |
| 4 | Contribution | 1:00 |
| 5 | Literature | 1:00 |
| 6 | Model | 1:30 |
| 7 | Results | 1:30 |
| 8 | Next steps | 1:00 |
| **Total** | | **~10:00** |

---

## Key lines to memorize (for transitions)

- Opening: *"The alternative data market is $8 billion and almost entirely invisible. I want to build a theory of how it works."*
- After slide 3: *"So the interesting question isn't just 'how accurate is the data' — it's 'who has it, how many of them, and what can they actually do with it.'"*
- After slide 4: *"Farboodi et al. solved the private value problem. I want to solve the pricing problem and the crowding problem."*
- Closing: *"The goal is a model clean enough that when this market becomes more observable, there's something to test against."*

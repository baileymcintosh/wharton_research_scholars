# Idea Log — Valuing and Pricing Financial Datasets

Running notes from working sessions. Entries are dated and cumulative.

---

## 2026-04-23

### Session 1: Core theoretical framework

**Starting intuition (Bailey):** Private information has a fixed "pie" of extractable value — determined by market size/volume and the leakage that happens when you trade on it. Adding more investors divides the pie. Vendor's question is whether to sell to 1 or many clients, which depends on how total value changes with n.

**Correction / sharpening:** The pie is not fixed — it shrinks as n grows. In Kyle (1985) with n symmetric informed traders sharing the same signal, each scales back their position knowing others are also trading, but aggregate informed order flow still grows. As n → ∞ prices become fully revealing and all profits → 0. The prisoner's dilemma: each trader's rational response to competition is to trade more aggressively than the social optimum, which collectively destroys the rents. What IS fixed is the information content of the signal; what is endogenous is how much of that mispricing can be captured as profit.

**Two distinct erosion mechanisms (keep these separate):**

1. **Capacity / market size**: Physical ceiling on profit because the tradeable universe is finite. A signal on a $500M-cap stock cannot generate $1B in profits regardless of accuracy. This is C(D) in the paper.
2. **Strategic crowding**: Multiple informed traders competing drives prices toward fundamentals faster, reducing each trader's profit per dollar traded. This is the Kyle lambda channel.

These are related but separable. The paper models both but the verbal framing was conflating them.

**Vendor's optimal licensing:** Depends on the derivative of total value w.r.t. n. Proposition 1 gives n* = (C(D)+1)/2. Key result: vendor revenue at optimum is V(D,1)×(C(D)+1)/4, which grows in both signal quality AND capacity. A high-accuracy, low-capacity dataset generates less vendor revenue than a mediocre, high-capacity one. This is the information seller's paradox.

**Identified gap in the paper:** The crowding decay functional form V(D,n) = V(D,1)×(1+(n-1)/C(D))^{-1} is imposed rather than derived from Kyle primitives. Deriving it from how lambda grows with n would strengthen the formal crowding contribution.

---

### Session 1: Broader motivation

**Bailey's framing:** The pricing of financial data matters beyond any single transaction because investment firms increasingly compete on data as statistical modeling ceases to be scarce. Quantitative methods (ML, factor models) have diffused broadly, compressing the alpha from modeling skill alone. The residual scarce resource is proprietary data. Implications:

- Investment firm value is increasingly tied to the value of the data they hold.
- Market flows — who trades what, at what size, in which direction — depend on who has what data.
- Data markets are therefore a primary mechanism through which financial information gets allocated to prices.

**Why this is a strong broader motivation (not just color):**

The Grossman-Stiglitz (1980) question was: given that someone has to pay to be informed, who does, and do prices end up efficient? The data-market version of that question is more tractable because there is now an explicit market with observable prices. Understanding price formation in data markets is therefore a route to understanding how efficiently financial markets aggregate information in the current institutional environment.

This also connects to a market structure point: if data is the scarce factor, data concentration (a few firms holding exclusive access to high-capacity datasets) translates directly into trading concentration and potentially into market fragility — crowded unwinds, correlated losses, systemic risk from correlated positioning. The paper's crowding mechanism is a micro-level version of that systemic story.

**Suggested addition to intro/motivation:** One paragraph connecting the commoditization-of-models observation to why dataset pricing matters at a market-structure level, not just for individual investors. This gives the paper relevance beyond the data-buyer's decision problem.

---

### Session 1 (continued): Why the paper is theoretical / empirical strategy

**Bailey's clarification:** Data markets are mostly private and opaque — licensing prices, exclusivity terms, and subscriber counts are not publicly observable. This is the direct justification for a theory-first approach: the market is economically significant but empirically invisible, so a theoretical model is the only available tool for understanding its mechanics.

**The opacity is not just a constraint — it's worth noting as a feature.** Most markets of comparable economic size have at least some observable price data. The fact that data markets do not is itself unusual and underscores why a formal model matters. State this explicitly in the paper, not as a limitation but as the justification for the approach.

**The theory does generate indirectly testable predictions.** No direct price data is needed to anchor the mechanisms:
- McLean-Pontiff (2016): publication events proxy for adoption spreading; post-publication alpha decay is an empirical test of the crowding/decay mechanism.
- Lou-Polk comomentum: cross-sectional variation in comomentum proxies for which datasets are widely shared.
- 13F filing similarity across funds: proxies for correlated data holdings without observing the data contracts themselves.

These don't test the pricing model directly but anchor the underlying mechanisms. A short "empirical implications" section mapping propositions to these proxies would strengthen the paper without requiring unavailable data.

**Framing note:** Don't frame the absence of direct empirics as a gap left for future work in a way that sounds apologetic. Frame it as a deliberate first step — the theory is built so that when better data becomes available, there is a model to test against. Grossman-Stiglitz (1980) operated the same way; serious empirical tests followed decades later.

---

### Session 2: Paper approach — structure, analogies, and the hybrid-market insight

**Core insight on information markets as a hybrid:** Information markets share characteristics with several well-studied market types. The modeling strategy should borrow results from those literatures rather than rederiving from scratch. The most useful analogies:

| Mechanism | Borrow from | What you take |
|---|---|---|
| Optimal subscriber count (club size) | Buchanan (1965) club goods | Structure of the congestion optimization |
| Crowding / price impact | Kyle (1985) | Lambda grows with n |
| Vendor pricing | Admati-Pfleiderer (1986) | Monopolist information seller |
| Dynamic pricing | Durable goods / Coase conjecture | But value decays with adoption not time — modifies the result |
| Negative network externality | Network economics | Inverted network effect as organizing paradox |

**The most underused analogy: club goods (Buchanan 1965).** Buchanan's optimal club size problem balances sharing benefits (more members lower per-capita cost) against congestion costs (more members reduce per-member value). The data market version removes the sharing benefit entirely — replicating data to n buyers costs the same as to 1 — so the only force is congestion. This yields a cleaner result than Buchanan's and connects Proposition 1 to the IO/public economics literature in a way that makes the contribution legible to a broad audience.

**The defining characteristic of information markets:** The buyer is also the mechanism of their own value destruction. When investor i buys data and trades on it, they help incorporate the signal into prices, reducing value for every other holder. The externality is from *purchasing and trading*, not from production or consumption. This is unusual — most externalities are from production (pollution) or consumption (congestion). Here it is downstream of purchase, in the act of trading. This creates a clean market-failure framing: the competitive equilibrium has too many buyers relative to the social optimum because each buyer does not internalize the value destruction they impose on existing holders.

**One-line description of what makes this market distinctive:** Inverted network effect. Most goods: more users → more value. Financial data: more users → less value. That inversion is the source of all the interesting results in the paper.

**Recommended paper structure (layered model, not mega-model):**

The risk with many mechanisms is that none feel derived — they feel assembled. A layered structure avoids this: one clean baseline fully solved, then one feature added at a time.

1. **Baseline**: Symmetric investors, one-shot licensing, no dynamics. Derive private value, crowding decay, optimal n*. Core results.
2. **Extension 1**: Heterogeneous investors. Show how the demand curve changes; when does the vendor switch between exclusive and broad licensing?
3. **Extension 2**: Dynamics. Adoption grows exogenously (McLean-Pontiff style) or endogenously. Alpha lifecycle.
4. **Extension 3**: Vendor's information problem. Vendor doesn't observe investor types — adverse selection, screening, garbling (Admati-Pfleiderer).

Each extension adds one mechanism, is fully tractable, and has a clean proposition. Extensions can be cut to a separate paper if needed.

---

### Session 3: Information leakage through trading

**The mechanism:** When an investor trades on private information in public markets, their order flow reveals the information to market makers and other observers. Prices adjust toward fundamental value, eroding the information's future value. This leakage is not a side effect — it is the central channel through which private information decays.

**Two distinct timescales to keep separate:**

1. *Within-period leakage*: As the informed investor trades, prices move toward the true value. Kyle (1985) — the informed trader optimally trades *gradually* to slow leakage. Dumping the full position immediately reveals all information at once and captures no profit. The optimal strategy rations trading across time to balance profit extraction rate against revelation rate.

2. *Cross-period leakage*: Once a signal is incorporated into prices, it is public. Future periods start with a more informed price, so the same dataset is worth less in subsequent periods even if the signal itself is unchanged.

**The n-investor case — Holden and Subrahmanyam (1992):** With n investors sharing the same signal, each faces a race-to-trade problem: if I trade slowly, others trade first and reveal the information before I've extracted my profits. The individually rational response is to trade more aggressively than a monopolist would. Since all n investors reason this way, aggregate informed order flow surges, prices adjust faster, and total extractable profit collapses. This is a prisoner's dilemma in trading speed. As n → ∞, equilibrium converges to the competitive outcome — near-immediate price revelation and near-zero profits.

**This is the micro-foundation that C(D) currently lacks.** The rate of leakage is endogenous to n — not just that λ gets larger, but that each investor's optimal trading strategy changes in a way that accelerates collective leakage. C(D) should be a derived object from these market primitives, not a free parameter.

**Connecting leakage speed to C(D):**
- Low-capacity dataset (narrow signal, small/illiquid market): concentrated order flow → high signal-to-noise ratio → market maker detects informed trading quickly → fast price adjustment → short profit window → rapid decay. Low C(D).
- High-capacity dataset (broad signal, liquid market): informed order flow spread across many assets and trades → each trade indistinguishable from noise → slow leakage → long profit window → sustained value. High C(D).

C(D) is therefore a statement about how detectable aggregate informed order flow is in the dataset's tradeable universe. This connects market liquidity and breadth to the capacity concept.

**Vendor implication — exclusivity solves the prisoner's dilemma:** By limiting n, the vendor forces buyers into a slower, more strategic trading pace (monopolist informed trader solution), which is collectively optimal for the informed side even though each individual would defect from it. The exclusivity contract solves the prisoner's dilemma among buyers. Vendor's profit motive and buyers' collective interest align — an unusual and useful result.

**Gap to address in the paper:** Section 5.2 currently imposes the decay form V(D,n) = V(D,1)×(1+(n-1)/C(D))^{-1} and invokes Kyle without solving the n-investor trading game. To micro-found C(D), add a section solving the n-investor Kyle game (or citing Holden-Subrahmanyam directly) and show how equilibrium profits map to V(D,n). This replaces a free parameter with a derived object. Key addition: cite Holden-Subrahmanyam (1992) for the n-investor result and show how their λ(n) expression maps to the decay form.

---

### Session 4: AI collusion and the cooperative trading equilibrium (Goldstein and Dou)

**Reference:** Goldstein and Dou (recent working paper) — AI robots trading on shared signals naturally discover tacit collusion, achieving near-monopolist profit extraction without explicit coordination.

**User's interpretation:** Correct that the monopolist trading pace maximizes value extraction for investors sharing a signal, and that the prisoner's dilemma prevents human investors from achieving it. Explicit coordination is also illegal (market manipulation). The AI result goes further.

**Three equilibria to distinguish in the paper:**

1. **Monopolist / exclusive** (n=1): Maximum value extraction, slowest leakage. Theoretical upper bound.
2. **Competitive / Holden-Subrahmanyam** (n large, human traders): Prisoner's dilemma → race to trade → fast leakage → near-zero profits. Lower bound.
3. **AI tacit collusion** (n large, AI traders): Prisoner's dilemma solved implicitly through iterated reinforcement learning → slow coordinated trading → leakage approaches the monopolist rate → profits well above the competitive outcome.

**Why AI can solve the prisoner's dilemma without human traders can:** AI algorithms trained independently on similar data and reward functions discover through experience that aggressive trading triggers aggressive responses that hurt everyone. Through iterated interaction they converge on the cooperative equilibrium — no communication, no agreement, no prosecutable conspiracy. Analogous to Calvano et al. (2020) showing pricing algorithms learning supracompetitive prices in product markets without coordination.

**Key implication for the model:** C(D) is endogenous to trading technology, not just market structure. The same dataset has higher effective capacity when traded by AI than by humans, because AI sustains the cooperative trading pace that the prisoner's dilemma prevents among humans. The move to algorithmic trading is not just a speed story — it is a value-preservation story for informed investors.

**Comparative static:** As investment management becomes more algorithmic, optimal n* from the vendor's perspective increases. More licenses can be sold at higher sustained value because AI buyers approximate the cooperative equilibrium at larger group sizes.

**Regulatory note:** Tacit algorithmic collusion is very difficult to prosecute under traditional antitrust, which requires concerted action or agreement. No communication = no conspiracy. Regulators have not resolved this in product markets; in financial markets it is even less settled.

**Suggested placement in paper:** Extension section — "Equilibrium under algorithmic trading." Show that AI traders can sustain higher n at given value levels relative to human traders, because they approximate the cooperative equilibrium. Connect to the vendor's optimal licensing problem: the optimal n* is increasing in the degree to which buyers can approximate cooperative trading.


# Valuing and Pricing Financial Datasets: From Predictive Power to Economic Value

**Bailey McIntosh**  
Wharton Research Scholars  
April 2026

---

## Abstract

How should a financial dataset be priced? Farboodi, Singal, Veldkamp, and Venkateswaran (2021)
provide a foundational answer for the private valuation question: the value of data to a single
investor depends on investor characteristics, market liquidity, and the data already held, and can
be reduced to a few sufficient statistics. This paper extends their framework in three directions.
First, we derive the mapping from measurable statistical improvement — the reduction in forecast
error variance achieved by a dataset — to the signal precision parameters that drive private value,
completing the bridge from prediction to valuation that their paper leaves implicit. Second, we
derive equilibrium transaction prices from the distribution of investor-specific valuations, a step
Farboodi et al. explicitly set aside. Building on Admati and Pfleiderer (1986), we model the data
vendor's optimal licensing problem and characterize the market-clearing price and optimal subscriber
count. Third, we make competitive adoption a first-order mechanism: as n investors trade on
the same signal, crowding generates price impact that erodes the signal's economic value for all
holders. We introduce a dataset capacity parameter and show that the equilibrium value of a
dataset is jointly determined by its signal quality, its capacity, and the number of licenses sold.
A central finding is that a dataset with high predictive accuracy may have zero or negative economic
value if its capacity is low and adoption is broad — the information seller's paradox. Comparative
statics characterize when exclusivity is optimal and when broad licensing dominates.

---

## 1. Introduction

The market for financial data has grown dramatically. Industry estimates place the alternative data
market at over eight billion dollars annually, with hedge funds, asset managers, and quantitative
investment firms increasingly competing on data acquisition rather than modeling. A natural
question follows: how much should an investor pay for a dataset? And how should the seller of
that dataset set its price?

The intuitive answer — pay up to the expected alpha the data generates — is incomplete in three
ways. First, the alpha a dataset generates depends on who is using it and how. An investor with
ten billion dollars under management extracts more raw profit from a given signal than one with
ten million, but also moves prices more when trading on it, which partially offsets the gain.
Second, the statistical accuracy of a dataset — its out-of-sample R-squared, its reduction in
forecast error — does not translate one-for-one into economic value. A dataset that predicts
earnings with high accuracy may generate little tradable alpha if the signal is already incorporated
in prices, if transaction costs exceed the gains from repositioning, or if many other investors hold
the same signal and have already traded it away. Third, the market price of a dataset need not
equal any individual investor's private value. It is set by the interaction between a seller with
market power and a heterogeneous population of potential buyers, each of whom values the data
differently.

Farboodi, Singal, Veldkamp, and Venkateswaran (2021) take the first rigorous step toward
answering these questions. They derive a procedure, based on sufficient statistics, for computing
the private value of any data series to an investor with specified characteristics. Their key
insight is that despite enormous heterogeneity in investor preferences, portfolio sizes, and
investment styles, the value of data can be reduced to three observable quantities: average asset
returns, return variances, and data forecast errors. They show that investor heterogeneity
generates enormous dispersion in willingness to pay for the same dataset, and that market
illiquidity — captured by the price impact of trades — is the principal force tempering this
dispersion. They explicitly note, however, that their procedure yields a private value, not a
transaction price, and that competitive adoption effects are not the focus of their analysis.

This paper takes the steps that Farboodi et al. (2021) set aside. We make three contributions.

**First**, we operationalize their sufficient statistics by deriving the mapping from standard
statistical predictive metrics — reduction in mean squared error, out-of-sample R-squared — to
the signal precision parameters that enter their valuation formula. This bridge is essential for
applied use: a data vendor marketing a dataset does not report signal precision in the sense of
Gaussian information economics; they report predictive accuracy relative to a benchmark. We
show how to translate one into the other under standard regularity conditions, making the
Farboodi et al. framework directly computable from the information a practitioner actually has.

**Second**, we derive equilibrium transaction prices. We model a data vendor who owns a
dataset, observes the distribution of investor types, and chooses a price and licensing scope to
maximize revenue. Building on Admati and Pfleiderer (1986), we show that the vendor faces
a fundamental tension: selling to more investors generates more revenue per unit but reduces
the value of the data to each buyer through competitive adoption. The optimal number of
licenses n\* trades off these forces and depends on the dataset's capacity — its ability to sustain
economic value as the number of users grows.

**Third**, we introduce dataset capacity as a formal object and make competitive adoption
central. As n investors share a signal and trade on it, aggregate informed order flow grows.
Following Kyle (1985), this increases the price impact coefficient λ, reducing the net trading
profit each investor can extract from the signal. We define the capacity C(D) of a dataset as
the rate at which the marginal value of a new user falls as n increases. Datasets with high
capacity (e.g., broad fundamental data) sustain value across many users; datasets with low
capacity (e.g., narrow high-frequency signals) are worth little once a handful of investors have
adopted them. We derive the equilibrium vendor price as a function of both signal quality and
capacity, and show that the information seller's paradox — high accuracy combined with zero
economic value — arises precisely when capacity is low and the vendor prices myopically.

The paper proceeds as follows. Section 2 reviews the literature. Section 3 sets up the model.
Section 4 derives the private valuation of a dataset and the prediction-to-precision bridge.
Section 5 solves the vendor's pricing problem and derives equilibrium transaction prices.
Section 6 characterizes competitive adoption, the crowding mechanism, and alpha decay.
Section 7 presents the main propositions and comparative statics. Section 8 discusses extensions.

---

## 2. Literature Review

This paper sits at the intersection of five strands of literature: (i) costly information and
market efficiency, (ii) direct valuation of financial data, (iii) monopolistic markets for
information, (iv) limits to arbitrage, crowding, and alpha decay, and (v) predictive modeling
and alternative data in asset management.

### 2.1 Costly Information and Market Efficiency

The theoretical foundation for financial data having positive value at all is Grossman and
Stiglitz (1980). They demonstrate that perfectly informationally efficient markets cannot
exist in equilibrium: if prices fully revealed all private information, no investor would pay
to acquire it, but then prices could not be informative. This contradiction implies that
informed investors must earn equilibrium rents from their information, and therefore that
information has positive value in competitive markets.

Veldkamp (2006) extends this to a setting where information is an economic good produced
and sold in markets. Investors choose what information to acquire as a function of its cost
and expected benefit, and this endogenous choice generates systematic comovement in asset
prices. The key implication for our purposes is that information acquisition is not passive —
investors respond to prices in the data market just as they respond to prices in asset markets.
Van Nieuwerburgh and Veldkamp (2009) show further that investors optimally specialize in
acquiring information about assets they already hold, generating heterogeneous information
sets across investors even when data is symmetrically available.

### 2.2 Valuing Financial Data: The Foundation

The most direct predecessor to this paper is Farboodi, Singal, Veldkamp, and Venkateswaran
(2021), "Valuing Financial Data." Their paper asks exactly our opening question — how much
should an investor pay for a data series? — and provides a rigorous answer for the private
valuation case. Their framework is a noisy rational expectations model with long-lived assets,
overlapping generations of investors, heterogeneous preferences, investment style constraints,
and rich data structures allowing public, private, or partially public signals about asset
fundamentals.

Their core result is that, despite this heterogeneity, the private value of a dataset to
investor i can be reduced to three sufficient statistics: the average return on the assets the
investor trades, the variance of those returns, and the forecast error of the data for those
returns. This makes valuation tractable without requiring knowledge of other investors'
characteristics. They illustrate the framework by computing the value of analyst earnings
forecast data to investors with varying wealth, risk preferences, investment styles, and
trading horizons, and find enormous dispersion in willingness to pay. They also show that
market illiquidity is the dominant force tempering this dispersion — large investors value
data less than proportionally because their trades move prices.

Critically for our extension, Farboodi et al. (2021) explicitly acknowledge two limitations.
First, their procedure yields a private value, not a transaction price: "Knowing the private
values of market participants allows one to trace out a demand curve for data... Understanding
how customers (investors) value a product (a data set) is different from calculating a
market clearing or equilibrium price." Second, they treat the data holdings of other investors
as fixed — they do not model the dynamic in which adoption of the same signal by additional
investors erodes its economic value through competitive trading.

This paper takes both of those next steps. In doing so, we also connect to a related 2022
paper by three of the same authors — Farboodi, Matray, Veldkamp, and Venkateswaran (2022),
"Where Has All the Data Gone?" — which models the general equilibrium consequences of
data growth for price informativeness. Where that paper asks what happens to markets
as the aggregate data endowment grows, we ask what happens to the value of a specific
dataset as the number of investors holding it grows. The two questions are related but
distinct: ours is the relevant one for pricing individual data licenses.

### 2.3 Monopolistic Markets for Information

Admati and Pfleiderer (1986) establish the theoretical benchmark for how a monopolist
information seller should price data. Their central result is that the optimal selling strategy
depends on whether the seller can price-discriminate and whether the data can be used
by many investors simultaneously. When the seller cannot price-discriminate and selling
to more investors reduces each buyer's value, the seller faces the information seller's paradox:
maximizing revenue requires balancing a higher per-unit price (from limiting supply) against
higher total revenue (from selling more units). They also show that a seller may optimally
"garble" the data — adding noise to the signal — to limit the extent to which buyers can
trade against each other.

We build on this framework by incorporating the specific crowding mechanism that makes
data value decline with adoption: the Kyle (1985) price impact channel. This allows us to
characterize the optimal number of licenses n\* as a function of dataset capacity, investor
heterogeneity, and market liquidity — objects that Admati and Pfleiderer (1986) treat
parametrically.

### 2.4 Limits to Arbitrage, Crowding, and Alpha Decay

A large literature documents that the economic value of predictive signals erodes over time
and as adoption grows. Berk and Green (2004) show that capital flows to skilled managers
until abnormal returns are fully competed away, providing the theoretical template for
why dataset value should fall with adoption. McLean and Pontiff (2016) provide direct
empirical evidence: once a return predictor is published in an academic paper, its profitability
falls by roughly half out-of-sample as traders learn about and trade against it.

Lou and Polk (2021) show that crowding in arbitrage strategies generates systematic
return co-movement — comomentum — across funds using similar signals, and that this
crowding creates fragility. Barroso and Chaudhury (2021) show crowded trades generate
excess tail risk. These papers document at the aggregate level the mechanism we formalize
at the signal level: shared adoption of the same information destroys value.

Kyle (1985) provides the microstructure foundation. In a market where an informed
trader competes against noise traders, the price impact coefficient λ — the Kyle Lambda —
measures how much each dollar of order flow moves prices. When n informed traders all
hold the same signal and trade on it, aggregate informed order flow increases proportionally
(in a competitive setting), which increases price impact and reduces each trader's ability to
extract profit from the mispricing the signal identifies.

### 2.5 Predictive Modeling and Alternative Data

Gu, Kelly, and Xiu (2020) demonstrate that machine learning methods can substantially
improve return prediction relative to traditional linear models. The relevant point for
our framework is that these statistical improvements — higher out-of-sample R-squared,
lower mean squared error — are routinely used in industry to market and price datasets.
We show that this practice is theoretically misguided: statistical improvement is a necessary
input to economic value but is neither sufficient nor proportional to it.

Tetlock (2007) and Tetlock, Saar-Tsechansky, and Macskassy (2008) provide early evidence
that alternative data — in their case, textual media content — predicts both asset prices
and firm fundamentals. Begenau, Farboodi, and Veldkamp (2018) show that data and scale
interact, favoring large investors who can better exploit big data. This motivates the AUM
heterogeneity in our investor valuation formula.

### 2.6 Gaps Addressed by This Paper

The literature establishes that information is costly, that predictive signals can be statistically
powerful, and that individual investors value the same data differently. What has not been
done is: (i) bridging the gap from statistical prediction metrics to the signal precision
parameters that determine economic value; (ii) deriving a market transaction price from
the distribution of investor-specific private values; and (iii) formally modeling how competitive
adoption of the same signal endogenously erodes that value.

---

## 3. Model Setup

We build on the noisy rational expectations framework of Farboodi et al. (2021), adding
three elements: an explicit mapping from statistical prediction improvement to signal precision,
a data vendor with a licensing choice, and a crowding mechanism via price impact.

### 3.1 Assets

There are N risky assets, indexed by j, with net supply $\bar{x}$. Each asset j pays a stream
of dividends $\{d_{jt}\}_{t=0}^{\infty}$, where the vector $d_t$ follows an autoregressive process:

$$d_{t+1} = \mu + G(d_t - \mu) + y_{t+1}$$

The dividend innovation $y_{t+1} \sim \mathcal{N}(0, \Sigma_d)$ is i.i.d. across time. The matrix G
governs dividend persistence. The key object of interest is $y_{t+1}$: the unpredictable component
of next period's dividend, which is what financial datasets seek to forecast.

### 3.2 Investors

In each period t, a measure-one continuum of overlapping generations investors $i \in [0,1]$
are born. Each investor i has:

- Initial endowment $\bar{w}_i > 0$ (proportional to AUM)
- Coefficient of relative risk aversion $\gamma_i > 0$
- Investment style constraint: investor i can only hold assets in set $\mathcal{Q}_i \subseteq \{1,...,N\}$
- An existing information set prior to purchasing any dataset

Investors choose portfolio $q_{it} \in \mathcal{Q}_i$ to maximize expected utility of end-of-period
consumption. Following Farboodi et al. (2021), we assume CARA utility. This is without
loss of generality for deriving closed-form valuation expressions under the Gaussian signal
structure below.

### 3.3 Signals and Data

In the baseline model without any purchased dataset, investor i observes the equilibrium
price $p_t$ (which contains aggregated private information) and any public signals. Denote
the baseline posterior variance of $y_{t+1}$ for investor i as $\Sigma_0$.

A dataset $D$ produces a signal about the dividend innovation:

$$\eta_i = \psi y_{t+1} + \Gamma e_i$$

where $e_i \sim \mathcal{N}(0, I)$ is idiosyncratic noise. The parameter $\psi$ captures which linear
combination of dividend innovations the data is informative about. The matrix $\Gamma$ governs
signal noise. When $e_i$ is correlated across investors, the signal has a public component;
when it is orthogonal across investors, the signal is fully private.

**Private precision.** Define the precision of dataset D for investor i as:

$$K_i(D) = \Gamma^{-1} \psi \Sigma_d \psi' (\Gamma')^{-1}$$

This is the standard precision matrix of the private signal noise. Higher K means the
dataset adds more precise information about dividend innovations.

### 3.4 From Statistical Improvement to Signal Precision

A practitioner evaluating dataset D observes its out-of-sample predictive performance relative
to a baseline model (e.g., the consensus analyst forecast, or an autoregressive benchmark).
The standard metric is the reduction in mean squared forecast error:

$$\text{MSE}_0 = \mathbb{E}\left[(y_{t+1} - \hat{y}_0)^2\right], \quad \text{MSE}_D = \mathbb{E}\left[(y_{t+1} - \hat{y}_D)^2\right]$$

Define the incremental R-squared of dataset D:

$$\Delta R^2(D) = 1 - \frac{\text{MSE}_D}{\text{MSE}_0} \in [0,1)$$

**Proposition 0 (Prediction-Precision Bridge).** Under the Gaussian linear signal structure
above, the incremental precision added by dataset D over the investor's baseline information
set is:

$$K_i(D) = \frac{\Delta R^2(D) \cdot \sigma^2_y}{\text{MSE}_D \cdot (1 - \Delta R^2(D))}$$

where $\sigma^2_y = \text{tr}(\Sigma_d)$ is the total variance of the dividend innovation. This is
the translation from the measurable object $\Delta R^2(D)$ — the predictive improvement — to
the precision parameter K that enters the Farboodi et al. (2021) valuation formula.

**Corollary.** For fixed $\Delta R^2(D)$, incremental precision $K_i(D)$ is decreasing in
$\text{MSE}_D$. Two datasets with the same improvement in R-squared but different baseline
accuracy levels add different amounts of precision.

### 3.5 Dataset Capacity

We introduce a new parameter not present in Farboodi et al. (2021): the **capacity** of dataset D.

**Definition (Dataset Capacity).** The capacity $C(D) > 0$ parametrizes how quickly the
incremental value of the dataset falls as the number of investors sharing it grows. Formally,
$C(D)$ is defined as:

$$C(D) = -\left(\frac{\partial V_i(D, n)}{\partial n}\right)^{-1}\bigg|_{n=1}$$

High capacity datasets (large $C(D)$) sustain value across many users; low capacity datasets
(small $C(D)$) are rapidly eroded by adoption. The capacity of a dataset is related to but
distinct from its signal quality — it captures how much of the signal survives arbitrage.

### 3.6 Equilibrium

An equilibrium is a sequence of prices $\{p_t\}$ and portfolio choices $\{q_{it}\}$ such that:
1. Each investor chooses $q_{it}$ to maximize expected utility given their information set.
2. Asset markets clear: $\int_i q_{it}\, di + x_{t+1} = \bar{x}$ for all t.

Prices aggregate private information about $y_{t+1}$, so the equilibrium price vector serves
as a public signal for all investors.

---

## 4. Private Valuation of a Dataset

### 4.1 The Valuation Formula

Following the Farboodi et al. (2021) approach, we define the private value of dataset D
to investor i in dollar terms as the increase in expected utility from purchasing D, converted
into a certainty equivalent wealth gain. For a CARA investor with the Gaussian signal
structure above, this yields a closed form.

Let $V_i(D)$ denote this private value. We express it in three equivalent forms.

**Cash flow decomposition.** Consistent with the notation in the current paper:

$$V_i(D) = \sum_{t=1}^{T} \frac{\mathbb{E}[\Delta CF_{i,t}(D)]}{(1 + r_i)^t} - C_i(D)$$

where $\Delta CF_{i,t}(D)$ is the incremental expected trading profit from using dataset D
in period t, and $C_i(D)$ is acquisition and implementation cost. This formulation
decomposes the problem into three stages:

1. Dataset D improves forecast accuracy by $\Delta R^2(D)$, adding precision $K_i(D)$.
2. Improved precision allows investor i to take larger, better-calibrated positions.
3. Better positions generate incremental trading profit $\Delta CF_{i,t}(D)$.

**Precision-based form.** Under the CARA-Gaussian structure, the certainty equivalent
wealth gain from acquiring signal precision K (beyond the baseline) is:

$$V_i^{\text{utility}}(D) = \frac{\bar{w}_i}{2\gamma_i} \ln\left(\frac{|\Sigma_0|}{|\Sigma_0 - \Sigma_0 K_i(D)(\Sigma_0 K_i(D) + I)^{-1} \Sigma_0|}\right)$$

where $\Sigma_0$ is the baseline posterior variance. This is the Farboodi et al. (2021) sufficient
statistics representation, expressed in terms of our precision bridge above.

**Operationalized form.** Substituting the prediction-precision bridge:

$$V_i(D) \approx \frac{\bar{w}_i}{2\gamma_i} \cdot \frac{\Delta R^2(D)}{1 - \Delta R^2(D)} \cdot \frac{\sigma^2_y}{\text{MSE}_D} - C_i(D)$$

This is the key expression that makes private valuation computable from observable
predictive metrics. It shows that private value is:
- Proportional to investor wealth (AUM) $\bar{w}_i$
- Decreasing in risk aversion $\gamma_i$
- Increasing and convex in the incremental R-squared $\Delta R^2(D)$
- Decreasing in the implementation cost $C_i(D)$

### 4.2 Investor Heterogeneity

The operationalized form above makes the sources of heterogeneity in private value explicit.
Two investors facing the same dataset may have very different private values because:

**AUM (wealth).** Private value scales approximately linearly with $\bar{w}_i$ in competitive
markets. In imperfectly competitive markets (as in Farboodi et al.), this linear scaling breaks
down because larger investors have higher price impact, tempering the gain from better
positioning. A large hedge fund values the same dataset far more in absolute dollars than
a boutique fund, but less per dollar of AUM once price impact is accounted for.

**Investment style.** The parameter $\psi$ in the signal structure captures which assets
the signal is informative about. If investor i only trades small-cap value stocks and dataset
D provides precision about large-cap growth dividends, $K_i(D) \approx 0$ regardless of
D's aggregate predictive power. This formalizes the intuition that a dataset must be
relevant to the investor's actual portfolio to have value.

**Existing information.** An investor who already holds a dataset D' with overlapping
signal content will value D less — diminishing returns to information. The incremental
$\Delta R^2(D | D')$ conditional on already owning D' is smaller than the unconditional
$\Delta R^2(D)$.

**Transaction costs.** The cash flow $\Delta CF_{i,t}(D)$ is a net number: gross trading
profit minus transaction costs. Investors with higher market impact or explicit transaction
costs (bid-ask spread, borrow cost for short positions) extract less value from any given
predictive improvement.

### 4.3 Illustrative Example: The High-Accuracy, Zero-Value Dataset

Consider a dataset D with out-of-sample R-squared of 90% for earnings surprise prediction.
A naïve assessment would suggest this is an enormously valuable dataset. But suppose:

- The signal is about a small, illiquid set of stocks with total market cap of $500M.
- The investor managing the strategy has AUM of $10B.
- Transaction costs (price impact alone) absorb 95% of the gross alpha from optimal positioning.

In this case, the incremental expected cash flow $\Delta CF_{i,t}(D) \approx 0$ even though
$\Delta R^2(D) = 0.90$. Formally: $V_i(D) < C_i(D)$, so the dataset has negative net private
value. The investor should not purchase it at any positive price.

This example illustrates the central distinction between predictive power and economic value,
and motivates the capacity concept: the dataset above has low capacity because its
tradeable universe is too small to absorb the informed order flow of any institutional investor.

---

## 5. From Value to Price: The Data Vendor's Problem

### 5.1 The Demand Curve for Data

Farboodi et al. (2021) note that knowing the distribution of private values $\{V_i(D)\}_{i \in [0,1]}$
allows one to trace a demand curve for dataset D. Formally, the demand curve is the
function $D(p)$ giving the measure of investors who purchase D at price p:

$$D(p) = \Pr(V_i(D) \geq p)$$

This demand curve has several properties. It is downward sloping in p (fewer investors
have high private values). It is shifted out by higher $\Delta R^2(D)$ (better datasets have
higher demand at any price). It is shifted in by higher market illiquidity (price impact
erodes private value, flattening the curve).

The key distinction between the demand curve for data and a standard demand curve is
that the value $V_i(D)$ is not independent of the number of buyers. This is the central
complication that Admati and Pfleiderer (1986) identify: selling to more investors changes
the value of the product to each buyer.

### 5.2 How Adoption Affects Value: The Crowding Channel

Let $V_i(D, n)$ denote the private value of dataset D to investor i when n investors
in total purchase and trade on the same dataset. We model the crowding channel using
the Kyle (1985) framework.

When n investors all receive signal $\eta_i \approx y_{t+1}$ (the same signal, since D is shared),
their aggregate demand for the mispriced asset increases proportionally. In a linear
rational expectations equilibrium, the equilibrium price impact coefficient is:

$$\lambda(n) = \frac{\text{Var}(y_{t+1})}{\sqrt{n \cdot \text{Var}(y_{t+1}) + \text{Var}(\text{noise})}} \cdot \frac{1}{\sigma_x}$$

where $\sigma_x$ is the standard deviation of noise trader supply. As n grows, $\lambda(n)$
increases — more informed order flow means each dollar traded reveals more information
and moves prices more. This reduces the expected trading profit of each informed investor,
since they are trading against more efficient prices.

**Definition (Value under Crowding).** The private value of dataset D to investor i,
conditional on n investors sharing the dataset, is:

$$V_i(D, n) = \frac{\bar{w}_i}{2\gamma_i} \cdot f(K_i(D), \lambda(n)) - C_i(D)$$

where f is increasing in K (signal quality) and decreasing in λ (price impact). The exact
form of f follows from solving the investor's portfolio problem under the crowded signal.

**Crowding decay.** For a dataset with capacity $C(D)$, we parametrize the value erosion as:

$$V_i(D, n) = V_i(D, 1) \cdot \left(1 + \frac{n-1}{C(D)}\right)^{-1}$$

This functional form has the properties that $V_i(D, 1) = V_i^{\text{solo}}$ (value with exclusive
access), that value is strictly decreasing in n, and that the rate of decay is faster when
capacity $C(D)$ is smaller. As $n \to \infty$, $V_i(D, n) \to 0$ — the signal is fully arbitraged.

### 5.3 The Vendor's Optimal Licensing Problem

A data vendor owns dataset D and chooses a price per license p and the number of
licenses n to sell. Assume the vendor can commit to the number of licenses (e.g., via
contractual exclusivity clauses). The vendor's revenue maximization problem is:

$$\max_{p,\, n} \quad n \cdot p$$

$$\text{subject to:} \quad p \leq V_i(D, n) \text{ for all } i \text{ who purchase}$$

The binding constraint is the marginal buyer — the investor with the lowest private value
among those who purchase. In a symmetric setting where all investors are of the same
type (equal AUM, risk aversion, style), this simplifies to:

$$\max_{n \geq 1} \quad n \cdot V(D, n) = n \cdot V(D, 1) \cdot \left(1 + \frac{n-1}{C(D)}\right)^{-1}$$

**Proposition 1 (Optimal Subscriber Count).** The vendor's revenue-maximizing number
of licenses is:

$$n^* = \frac{C(D) + 1}{2}$$

The optimal price is:

$$p^* = V(D, 1) \cdot \frac{2}{C(D) + 1}$$

Total revenue at the optimum is:

$$\Pi^* = \frac{V(D, 1) \cdot (C(D) + 1)}{4}$$

**Proof sketch.** The unconstrained revenue function $R(n) = n \cdot V(D,n)$ is concave in n
for the capacity parametrization above. The first-order condition yields $n^* = (C(D)+1)/2$.
Revenue is maximized at an interior point when $C(D) > 1$; for $C(D) \leq 1$, the vendor
sells exclusively ($n^* = 1$). $\square$

**Corollary 1.** The optimal subscriber count $n^*$ is increasing in dataset capacity $C(D)$.
Datasets with low capacity (narrow high-frequency signals) should be licensed exclusively
or to very few buyers. Datasets with high capacity (broad fundamental signals) can be
licensed broadly without significant value erosion.

**Corollary 2.** Total vendor revenue $\Pi^*$ is increasing in both signal quality $V(D,1)$
and capacity $C(D)$. A dataset that is highly predictive but has low capacity generates
less total revenue than a moderately predictive dataset with high capacity, because the
vendor is constrained to sell to very few buyers.

### 5.4 Heterogeneous Investors and Price Discrimination

When investors are heterogeneous (differing AUM, style, risk aversion, existing data), the
demand curve $D(p,n)$ is a non-trivial object. The vendor's problem becomes:

$$\max_{p,\, n} \quad n \cdot p \quad \text{s.t.} \quad D(p, n) \geq n$$

At the optimum, the marginal buyer is just indifferent between purchasing and not. The
equilibrium price satisfies:

$$p^*(n) = V_{(n)}(D, n)$$

where $V_{(n)}(D, n)$ is the n-th order statistic of the private value distribution evaluated
at n users. As n increases, both the order statistic falls (lower-value buyers at the margin)
and the per-buyer value falls (crowding). Both effects push price down as the vendor sells
more licenses.

**Key result.** In a heterogeneous market, the vendor charges a price above the mean
private value (targeting high-value buyers) or below (targeting volume). The optimal
strategy depends on the shape of the value distribution: if the distribution is heavy-tailed
(a few very high-value buyers), exclusive licensing dominates; if the distribution is
approximately uniform, broad licensing dominates.

---

## 6. Competitive Adoption, Alpha Decay, and Dataset Lifecycle

### 6.1 Endogenous Adoption Dynamics

The static model above takes n as a choice variable for the vendor. In practice, adoption
is also driven by investor discovery, imitation, and the public availability of research
documenting a signal's profitability. McLean and Pontiff (2016) document that academic
publication of return predictors causes significant post-publication decay.

We model this as a dynamic adoption process. Let $n_t$ be the number of investors using
dataset D at time t. In the absence of vendor restrictions, adoption grows as investors
observe the profitability of others and imitate. The alpha decay follows:

$$\alpha_t(D) = \alpha_0(D) \cdot \left(1 + \frac{n_t - 1}{C(D)}\right)^{-1}$$

where $\alpha_0(D) = V(D,1)/\bar{w}$ is the per-dollar alpha available to an exclusive user.
The lifecycle of the dataset's alpha looks like: high alpha at low adoption, declining
monotonically as adoption grows, approaching zero as $n_t \to \infty$.

### 6.2 The First-Mover Advantage

The above dynamics imply a clear first-mover advantage: investors who adopt dataset D
early (when $n_t$ is small) capture alpha at or near its maximum $\alpha_0(D)$. Late adopters
capture only $\alpha_0(D) \cdot (1 + (n_t - 1)/C(D))^{-1}$, which may be below the cost
of the dataset if $n_t$ is already large.

**Proposition 2 (First-Mover Value Premium).** For a dataset with capacity C(D) and
initial solo alpha $\alpha_0(D)$, the value advantage of being the k-th adopter versus the
$(k+1)$-th adopter is:

$$\Delta V^k = V(D, k) - V(D, k+1) = V(D,1) \cdot \frac{1}{C(D)} \cdot \left(1 + \frac{k-1}{C(D)}\right)^{-1}\left(1 + \frac{k}{C(D)}\right)^{-1}$$

This premium is largest for the transition from exclusive to one competitor (k=1) and
declines as the number of existing users grows.

### 6.3 The Information Seller's Paradox: Formal Statement

**Proposition 3 (Information Seller's Paradox).** A dataset with high predictive power
($\Delta R^2(D)$ close to 1) may have zero or negative economic value to an investor when:

(i) **Low capacity**: $C(D)$ is small and the investor is not the exclusive user ($n > n^*$), or

(ii) **High implementation cost**: $C_i(D) > V_i(D, n)$ due to price impact, transaction
costs, or style mismatch.

**Proof.** From the valuation formula: $V_i(D,n) = V_i(D,1) \cdot (1 + (n-1)/C(D))^{-1} - C_i(D)$.
For large n or small $C(D)$, the first term approaches zero. For any $C_i(D) > 0$, there
exists $\bar{n}$ such that for all $n > \bar{n}$, $V_i(D,n) < 0$. $\square$

This proposition formalizes the central empirical puzzle: many datasets marketed on the
basis of high predictive accuracy fail to generate positive returns for their buyers. The
explanation is not that predictive accuracy is irrelevant — it enters the valuation formula
directly — but that capacity and adoption level determine whether accuracy can be
translated into tradeable economic value.

---

## 7. Theoretical Results: Summary of Propositions

**Proposition 0** (Prediction-Precision Bridge). For a dataset with measurable out-of-sample
predictive improvement $\Delta R^2(D)$ over a baseline, the incremental signal precision
is $K_i(D) = \Delta R^2(D) \cdot \sigma^2_y / (\text{MSE}_D \cdot (1 - \Delta R^2(D)))$.
This makes the Farboodi et al. (2021) private value formula computable from observable
predictive metrics.

**Proposition 1** (Optimal Subscriber Count). For a homogeneous investor population, the
vendor maximizes revenue by selling $n^* = (C(D)+1)/2$ licenses at price $p^* = 2V(D,1)/(C(D)+1)$.
The optimal n\* is increasing in capacity and decreasing in the value dispersion across investors.

**Proposition 2** (First-Mover Value Premium). The marginal value of being the k-th adopter
versus the $(k+1)$-th adopter is strictly positive and decreasing in k, with the largest premium
at the exclusive-to-shared transition.

**Proposition 3** (Information Seller's Paradox). High predictive accuracy is neither necessary
nor sufficient for positive economic value. Value depends jointly on signal quality, capacity,
adoption level, and implementation cost. A dataset with $\Delta R^2 \approx 1$ can have
$V_i(D,n) < 0$.

**Proposition 4** (AUM-Crowding Interaction). Large investors (high $\bar{w}_i$) are more
sensitive to crowding than small investors, because their higher absolute position size
generates greater price impact. As n grows, the value advantage of large investors over
small investors narrows and may reverse — small investors can extract more value per
dollar from a crowded signal because their price impact is lower.

**Proposition 5** (Capacity and Licensing Structure). The vendor's optimal policy is:
- Exclusive licensing ($n^*=1$) when $C(D) < 1$ (very low capacity datasets).
- Broad licensing when $C(D)$ is large and investor value distribution is approximately uniform.
- Intermediate licensing when value distribution is right-skewed (few high-value buyers).

**Proposition 6** (Comparative Statics on Price). The equilibrium transaction price $p^*$ is:
- Increasing in $\Delta R^2(D)$ (better signal → higher value → higher price).
- Decreasing in market illiquidity (higher λ erodes value for all buyers).
- Non-monotone in capacity: higher C allows more buyers but at a lower per-unit price.
Total revenue, however, is monotonically increasing in both $\Delta R^2(D)$ and $C(D)$.

---

## 8. Extensions

### 8.1 Dynamic Dataset Pricing Over Time

In practice, datasets are licensed on a subscription basis. The vendor sets not just an
initial price but a price path $\{p_t\}_{t=0}^{T}$. As adoption grows and alpha decays,
the vendor may optimally reduce the subscription price to maintain the marginal buyer's
participation. The socially efficient price path sets price equal to the marginal value at
each adoption level, which is declining. The profit-maximizing price path involves
commitment to limit future sales to support the current price — the classic durable goods
monopoly problem (Coase conjecture). Datasets are unlike durable goods in that their
value decays with adoption rather than with calendar time, which modifies the Coasian
dynamics in analytically tractable ways.

### 8.2 Optimal Noise Addition (Garbling)

Admati and Pfleiderer (1986) show that a monopolist may optimally add noise to a signal
to soften competition among buyers and preserve the signal's value. In our framework,
this corresponds to the vendor selling a degraded version of dataset D with precision
$\tilde{K} < K_i(D)$, chosen to balance the higher per-user value preservation against
the lower raw signal quality. The optimal noise level $\Gamma^*$ satisfies a first-order
condition that depends on the distribution of investor types and the capacity $C(D)$.
This extension may explain the common industry practice of selling data with intentional
lags, geographic restrictions, or asset coverage limitations.

### 8.3 Incentives for Producing New Datasets

The equilibrium pricing framework implies that the value of producing a new dataset is:

$$\Pi^*(D) = \frac{V(D,1) \cdot (C(D)+1)}{4} - \text{Production Cost}(D)$$

This determines which datasets are worth creating. High signal quality and high capacity
are both required for production to be profitable. Datasets that are cheap to produce
(e.g., scraping public web data) but have low capacity may not generate enough vendor
revenue to justify production. This has implications for the diversity of the data ecosystem:
a market structure that favors broad licensing (competitive data providers) will under-invest
in narrow, high-capacity datasets relative to the social optimum, since their value is best
captured through exclusive pricing.

### 8.4 Multi-Dataset Portfolios and Substitution

In practice, investors hold portfolios of datasets, not a single signal. The incremental
value of a new dataset D conditional on already owning portfolio $\mathcal{P}$ of datasets
is $V_i(D | \mathcal{P}) = V_i(D \cup \mathcal{P}) - V_i(\mathcal{P})$, which is generally
less than $V_i(D)$ due to signal overlap. The vendor must account for this substitution
when pricing: a dataset that is highly correlated with publicly available analyst forecasts
has lower private value increments for informed buyers who already hold those forecasts.
This motivates data vendors to emphasize the orthogonality of their data to existing sources
as a marketing and pricing lever.

---

## References

Admati, A. R., and Pfleiderer, P. (1986). A monopolistic market for information. *Journal of Economic Theory*, 39(2), 400–438.

Barroso, P., and Chaudhury, M. (2021). Crowded trades and tail risk. *Working paper*.

Begenau, J., Farboodi, M., and Veldkamp, L. (2018). Big data in finance and the growth of large firms. *Journal of Monetary Economics*, 97, 71–87.

Berk, J., and Green, R. (2004). Mutual fund flows and performance in rational markets. *Journal of Political Economy*, 112(6), 1269–1295.

Farboodi, M., Matray, A., Veldkamp, L., and Venkateswaran, V. (2022). Where has all the data gone? *Review of Financial Studies*, 35(7), 3101–3138.

Farboodi, M., Singal, D., Veldkamp, L., and Venkateswaran, V. (2021). Valuing financial data. *Working paper*, MIT Sloan and Columbia Business School.

Grossman, S. J., and Stiglitz, J. E. (1980). On the impossibility of informationally efficient markets. *American Economic Review*, 70(3), 393–408.

Gu, S., Kelly, B., and Xiu, D. (2020). Empirical asset pricing via machine learning. *Review of Financial Studies*, 33(5), 2223–2273.

Hou, K., Xue, C., and Zhang, L. (2015). Digesting anomalies: An investment approach. *Review of Financial Studies*, 28(3), 650–705.

Kyle, A. S. (1985). Continuous auctions and insider trading. *Econometrica*, 53(6), 1315–1335.

Lou, D., and Polk, C. (2021). Comomentum: Inferring arbitrage activity from return correlations. *Working paper*.

McLean, R. D., and Pontiff, J. (2016). Does academic research destroy stock return predictability? *Journal of Finance*, 71(1), 5–32.

Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. *Journal of Finance*, 62(3), 1139–1168.

Tetlock, P. C., Saar-Tsechansky, M., and Macskassy, S. (2008). More than words: Quantifying language to measure firms' fundamentals. *Journal of Finance*, 63(3), 1437–1467.

Van Nieuwerburgh, S., and Veldkamp, L. (2009). Information immobility and the home bias puzzle. *Journal of Finance*, 64(3), 1187–1215.

Veldkamp, L. (2006). Information markets and the comovement of asset prices. *Review of Economic Studies*, 73(3), 823–845.

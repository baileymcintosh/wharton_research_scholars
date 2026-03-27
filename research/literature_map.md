# Literature Map for `Valuing and Pricing Financial Datasets`

## What this folder is doing

This repo now contains:

- your project outline in `docs/project_outline.pdf`
- a categorized paper library in `papers/`
- a machine-readable catalog with titles, abstracts, links, and local file paths in `papers/metadata/paper_catalog.json` and `papers/metadata/paper_catalog.csv`

At the time this note was written, the library contains 25 curated papers and 15 locally stored PDFs. The remaining papers are still cataloged with metadata and source links even when a direct PDF was not openly downloadable.

## Bottom line

Your project question is strong, but there is an important overlap risk: Farboodi, Singal, Veldkamp, and Venkateswaran, **"Valuing Financial Data" (2021)**, is already very close to your topic. That does not kill your project. It means your comparative advantage has to be made explicit.

The cleanest way to differentiate your paper is:

1. Make the bridge from **predictive power to cash-flow value** the centerpiece.
2. Push beyond private valuation to an explicit theory of **dataset price formation**.
3. Make **adoption, crowding, alpha decay, and exclusivity** central objects rather than side constraints.
4. Treat a dataset as a priced asset whose value depends on both **signal quality** and **how many other investors monetize the same signal**.

If you do that clearly, your paper can sit next to `Valuing Financial Data` rather than merely restating it.

## Recommended framing

A good one-sentence framing for the paper is:

> A financial dataset should be valued not by forecast accuracy alone, but by the incremental cash flows it enables after accounting for investor heterogeneity, trading frictions, and equilibrium erosion from shared adoption.

That framing is consistent with your outline and helps separate your contribution from pure ML forecasting papers and from pure information-efficiency theory.

## Literature strands

### 1. Costly information, endogenous information acquisition, and informational efficiency

- **Grossman and Stiglitz (1980), "On the Impossibility of Informationally Efficient Markets."** Local PDF: `papers/costly_information/1980_grossman_stiglitz_impossibility_of_informationally_efficient_markets.pdf`  
  Core idea: if information is costly, prices cannot be perfectly informative in equilibrium because someone must earn rents from acquiring information.  
  Use in your paper: this is the foundational justification for why datasets can have positive economic value at all.

- **Veldkamp (2006), "Information Markets and the Comovement of Asset Prices."** Local PDF: `papers/costly_information/2006_veldkamp_information_markets_and_comovement_of_asset_prices.pdf`  
  Core idea: investors endogenously choose what information to buy, and that choice creates systematic patterns in prices.  
  Use in your paper: this helps you model datasets as economic goods with endogenous demand rather than passive inputs.

- **García and Vanden (2009), "Information Acquisition and Mutual Funds."** Local PDF: `papers/costly_information/2009_garcia_vanden_information_acquisition_and_mutual_funds.pdf`  
  Core idea: active investors choose how much information to acquire subject to costs and expected benefits.  
  Use in your paper: directly supports an investor-specific willingness-to-pay object for data.

- **Van Nieuwerburgh and Veldkamp (2009), "Information Immobility and the Home Bias Puzzle."** Local PDF: `papers/costly_information/2009_van_nieuwerburgh_veldkamp_information_immobility_and_home_bias.pdf`  
  Core idea: investors learn more about assets they already specialize in, so information acquisition becomes uneven across investors and assets.  
  Use in your paper: strong support for your heterogeneity claim that the same dataset has different value to different users.

- **Avdis (2016), "Information Tradeoffs in Dynamic Financial Markets."** Metadata only in catalog.  
  Core idea: dynamic trading changes the value of information because timing, liquidity, and strategic interaction matter.  
  Use in your paper: useful if you add a dynamic extension in which dataset value depends on holding period or rebalance frequency.

- **Hanson and Sunderam (2013), "Are There Too Many Safe Securities? Securitization and the Incentives for Information Production."** Metadata only in catalog.  
  Core idea: market design can distort incentives to produce information.  
  Use in your paper: helpful for an extension on the supply side of datasets and incentives for creating new data products.

### 2. Value of information and direct data valuation

- **Kadan and Manela (2018), "Estimating the Value of Information."** Metadata only in catalog.  
  Core idea: information can be assigned a measurable economic value rather than treated as an abstract concept.  
  Use in your paper: cite this as a key bridge between decision-theoretic value-of-information ideas and finance.

- **Farboodi, Singal, Veldkamp, and Venkateswaran (2021), "Valuing Financial Data."** Local PDF: `papers/alternative_data/2021_farboodi_singal_veldkamp_venkateswaran_valuing_financial_data.pdf`  
  Core idea: the value of a financial dataset depends on investor characteristics, trading horizon, other data already owned, and market liquidity.  
  Use in your paper: this is the closest existing paper. You should explicitly position your contribution relative to it. The strongest distinction is to emphasize **pricing**, **shared adoption**, and **equilibrium alpha erosion** much more than they do.

### 3. Predictive power, forecasting, and empirical signal extraction

- **Hou, Xue, and Zhang (2015), "Digesting Anomalies: An Investment Approach."** Local PDF: `papers/prediction_asset_pricing/2015_hou_xue_zhang_digesting_anomalies.pdf`  
  Core idea: many return patterns can be understood through a disciplined investment-based framework instead of anomaly-by-anomaly storytelling.  
  Use in your paper: useful for disciplining what counts as genuine incremental predictive content rather than noisy in-sample fit.

- **Gu, Kelly, and Xiu (2020), "Empirical Asset Pricing via Machine Learning."** Local PDF: `papers/prediction_asset_pricing/2020_gu_kelly_xiu_empirical_asset_pricing_via_machine_learning.pdf`  
  Core idea: ML can materially improve return forecasts by exploiting nonlinearities and interactions.  
  Use in your paper: motivates why modern datasets can improve prediction, but also highlights that better prediction is not the same thing as higher economic value.

- **Green, Hand, and Zhang (2017), "The Characteristics that Provide Independent Information about Average U.S. Monthly Stock Returns."** Metadata only in catalog.  
  Core idea: many candidate predictors are redundant; a smaller subset contains the independent information.  
  Use in your paper: supports the idea that a new dataset’s value is incremental and conditional on the buyer’s existing information set.

### 4. Alternative data, text, media, and data abundance

- **Tetlock (2007), "Giving Content to Investor Sentiment: The Role of Media in the Stock Market."** Local PDF: `papers/alternative_data/2007_tetlock_giving_content_to_investor_sentiment.pdf`  
  Core idea: textual media content predicts market outcomes and contains tradable information.  
  Use in your paper: good early example of a dataset with measurable predictive power that could be economically monetized.

- **Tetlock, Saar-Tsechansky, and Macskassy (2008), "More Than Words: Quantifying Language to Measure Firms' Fundamentals."** Local PDF: `papers/alternative_data/2008_tetlock_saar_tsechansky_macskassy_more_than_words.pdf`  
  Core idea: text-based signals predict both fundamentals and returns.  
  Use in your paper: especially useful for your proposed bridge from prediction of fundamentals to investor cash flows.

- **Begenau, Farboodi, and Veldkamp (2018), "Big Data in Finance and the Growth of Large Firms."** Local PDF: `papers/alternative_data/2018_begenau_farboodi_veldkamp_big_data_in_finance.pdf`  
  Core idea: data and scale interact, which can favor larger firms and alter market structure.  
  Use in your paper: helps motivate why AUM and implementation scale matter for dataset value.

- **Cao, Jiang, Lei, and Zhou (2024), "Applied AI for Finance and Accounting: Alternative Data and Opportunities."** Metadata only in catalog.  
  Core idea: current review of how alternative data is being used in finance and accounting.  
  Use in your paper: useful for motivation and contemporary examples, not for the core theory.

- **Hansen and Borch (2022), "Alternative Data and Sentiment Analysis: Prospecting Non-standard Data in Machine Learning-driven Finance."** Metadata only in catalog.  
  Core idea: modern finance increasingly relies on nontraditional, rapidly decaying, and difficult-to-scale information sources.  
  Use in your paper: helpful for motivating exclusivity, timeliness, and decay as economically relevant dataset characteristics.

### 5. Limits to arbitrage, capacity, crowding, and alpha decay

- **Shleifer and Vishny (1997), "The Limits of Arbitrage."** Metadata only in catalog.  
  Core idea: even when mispricing exists, informed traders may be unable or unwilling to fully eliminate it because of funding and agency frictions.  
  Use in your paper: this prevents a naive conclusion that all information should be fully arbitraged away immediately.

- **Berk and Green (2004), "Mutual Fund Flows and Performance in Rational Markets."** Local PDF: `papers/crowding_alpha_decay/2004_berk_green_mutual_fund_flows_and_performance.pdf`  
  Core idea: capital flows chase skill until abnormal returns are competed away.  
  Use in your paper: an excellent template for why dataset value should fall as more capital adopts the same signal.

- **Chen, Hong, Huang, and Kubik (2004), "Does Fund Size Erode Mutual Fund Performance? The Role of Liquidity and Organization."** Metadata only in catalog.  
  Core idea: scale creates implementation frictions and can reduce performance.  
  Use in your paper: directly supports a nonlinearity between AUM and the monetizable value of information.

- **Duffie (2010), "Asset Price Dynamics with Slow-Moving Capital."** Metadata only in catalog.  
  Core idea: capital does not instantly flow to opportunities, which shapes how fast mispricing is corrected.  
  Use in your paper: useful for a dynamic extension where alpha decay is gradual rather than instantaneous.

- **Gromb and Vayanos (2012), "Deliberate Limits to Arbitrage."** Local PDF: `papers/crowding_alpha_decay/2012_gromb_vayanos_deliberate_limits_to_arbitrage.pdf`  
  Core idea: strategic traders may choose not to fully eliminate mispricing because doing so affects their own future profitability.  
  Use in your paper: highly relevant if you want a richer equilibrium pricing section in which sophisticated buyers internalize crowding.

- **McLean and Pontiff (2016), "Does Academic Research Destroy Stock Return Predictability?"** Local PDF: `papers/crowding_alpha_decay/2016_mclean_pontiff_research_destroy_stock_return_predictability.pdf`  
  Core idea: once return predictors become widely known, their profitability falls.  
  Use in your paper: probably the cleanest empirical analogy for alpha decay after information diffusion.

- **Lou and Polk (2021), "Comomentum: Inferring Arbitrage Activity from Return Correlations."** Local PDF: `papers/crowding_alpha_decay/2021_lou_polk_skouras_comomentum.pdf`  
  Core idea: co-movement in returns can reveal arbitrage activity and crowding.  
  Use in your paper: gives you language and empirical intuition for how shared dataset adoption can show up in prices.

- **Brown, Howard, and Lundblad (2021), "Crowded Trades and Tail Risk."** Local PDF: `papers/crowding_alpha_decay/2021_barroso_chaudhury_crowded_trades_and_tail_risk.pdf`  
  Core idea: crowded positions create fragility and left-tail exposure.  
  Use in your paper: lets you argue that dataset adoption does not only reduce alpha; it can also change payoff skewness and crash risk.

- **Jensen, Kelly, and Pedersen (2023), "Is There a Replication Crisis in Finance?"** Metadata only in catalog.  
  Core idea: many published signals weaken materially out of sample.  
  Use in your paper: useful for warning that ex ante dataset valuation should discount in-sample predictive gains.

## What this literature implies for your model

The literature points toward a simple but strong structure:

1. A dataset produces an incremental signal, not a stand-alone payoff.
2. That signal only has value through changed portfolio decisions.
3. The same signal has different value for different investors because of scale, style, costs, and existing information.
4. Shared adoption shrinks private value through crowding, lower price impact-adjusted monetization, and alpha decay.
5. Dataset price should therefore depend on signal quality, exclusivity, scalability, and expected diffusion.

That is the clean bridge from the strands above to your own framework.

## A clean contribution statement

If you want a sharper contribution paragraph, I would write it roughly as:

> Existing work shows that information is costly, that predictive models can improve forecasts, and that datasets can have investor-specific value. What is still missing is a unified framework that maps a dataset’s incremental predictive content into investor-specific cash-flow gains and then into an equilibrium market price once adoption, crowding, and alpha decay are taken into account.

That is both honest and defensible relative to the papers in this repo.

## How to draw on the literature in the actual paper

- Use **Grossman-Stiglitz**, **Veldkamp**, **García-Vanden**, and **Van Nieuwerburgh-Veldkamp** to justify why information is costly, chosen endogenously, and heterogeneously valued.
- Use **Kadan-Manela** and especially **Valuing Financial Data** to motivate why information should be measured in economic, not purely statistical, units.
- Use **Gu-Kelly-Xiu**, **Hou-Xue-Zhang**, **Green-Hand-Zhang**, and the **Tetlock** papers to motivate the first link in your chain: datasets can improve forecasts.
- Use **Berk-Green**, **Chen-Hong-Huang-Kubik**, **Duffie**, **Gromb-Vayanos**, **McLean-Pontiff**, **Lou-Polk**, and **Crowded Trades and Tail Risk** to motivate the second link: monetization is constrained and erodes with scale and diffusion.
- Use **Big Data in Finance** and the recent alternative-data reviews to motivate current relevance and why dataset markets are economically important now.

## Where your project can still add value

The strongest open spaces I see are:

- a cleaner reduced-form mapping from forecast improvement to expected trading profits
- an explicit distinction between **private value** and **market transaction price**
- a treatment of **exclusivity versus shared access** as a pricing problem
- a dynamic story in which dataset value decays as adoption spreads
- comparative statics for when a high-accuracy dataset is still low-value because it is hard to monetize

Those are all directly aligned with your current outline.

## Suggested reading order

If you want the fastest route to a serious draft, read in this order:

1. `Valuing Financial Data`
2. `On the Impossibility of Informationally Efficient Markets`
3. `Information Markets and the Comovement of Asset Prices`
4. `Estimating the Value of Information`
5. `Mutual Fund Flows and Performance in Rational Markets`
6. `Does Academic Research Destroy Stock Return Predictability?`
7. `Empirical Asset Pricing via Machine Learning`
8. `More Than Words`
9. `Crowded Trades and Tail Risk`
10. `Big data in finance and the growth of large firms`

## Practical next step

The next draft of your paper should probably add one explicit section called **"Closest Related Paper and Differentiation"** and discuss `Valuing Financial Data` directly. That will make the project much more credible because it shows you already know what the nearest neighbor is and exactly where you go beyond it.

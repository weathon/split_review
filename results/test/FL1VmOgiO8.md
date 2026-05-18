Now I have everything I need. Here is the consolidated final review:

---

## Summary

This paper proposes FB-GAN, a WGAN-GP model augmented with FinBERT-based sentiment features for stock price prediction on five major US stocks (Amazon, Apple, Microsoft, Nvidia, Adobe). News articles (headlines and summaries) from Alpha Vantage are sentiment-analyzed using FinBERT, and the resulting scores are incorporated as an additional feature alongside historical price data. The paper reports that FB-GAN with combined headline-summary sentiment achieves lower RMSE than Vanilla RNN, LSTM, GAN, and WGAN-GP baselines, and that headline-summary sentiment outperforms either headline-only or summary-only variants.

## Strengths

- **Systematic baseline comparison across five stocks and multiple model classes.** The paper evaluates Vanilla RNN, LSTM, GAN, and WGAN-GP alongside the proposed FB-GAN on the same set of stocks using the same RMSE metric. Table 1 (referenced in Section 4.1) shows that FB-GAN achieves lower RMSE than all baselines for every stock (e.g., Apple: 9.17 vs. 10.76 for WGAN-GP; Microsoft: 10.04 vs. 10.69). This provides quantitative support for the claim that the proposed model outperforms the alternatives under the reported experimental conditions.

- **Domain-appropriate sentiment model and careful preprocessing.** The paper uses FinBERT, a BERT model fine-tuned specifically for financial text, rather than a generic sentiment analyzer. Preprocessing steps include deduplication of news articles via pandas, weighting by Alpha Vantage's relevance score, and handling missing sentiment days with neutral (0) scores — these are sensible choices that reduce data quality issues.

- **Evidence that combined headline-summary sentiment outperforms either alone.** The paper reports average RMSE values of 10.81 (headline-summary), 12.32 (headline-only), and 13.07 (summary-only), with improvements of 12.3% and 17.3% respectively (Section 4.1). This supports the paper's auxiliary claim about how news article type influences predictive performance.

## Weaknesses

### Fatal
None. The issues identified below are serious but addressable in principle through additional experiments and clearer documentation.

### Major

- **Ambiguous train/test split method for time-series data.** The paper states only that "80% of the samples are used for training, and 20% are used for testing" (Sections 3.2, 3.3), without specifying whether the split is chronological (time-ordered) or random. For financial time-series forecasting, a chronological split is essential to prevent future information from leaking into training. A random split would produce artificially optimistic results by allowing the model to train on data temporally interleaved with test points. The paper does not clarify this choice, nor does it justify or describe the split procedure. This makes the reported RMSE values difficult to interpret as measures of genuine predictive performance.

- **The effect of sentiment is not isolated from architecture and feature-count differences.** The comparison between FB-GAN and WGAN-GP (the claimed baseline isolating sentiment) involves multiple uncontrolled confounds:
  - FB-GAN uses a larger architecture (generator: 3 GRU layers with 1024/512/256 units; discriminator: 3 CNN layers with 32/64/128 units), while WGAN-GP uses the same (smaller) generator and discriminator as the basic GAN (Section 3.2.4 states "the discriminator and generator are the same as basic GAN," whose exact GRU layer sizes are unspecified but were not 1024/512/256).
  - FB-GAN is trained for 160 epochs with learning rate 0.000128; WGAN-GP for 100 epochs with learning rate 0.000115.
  - FB-GAN has an additional input feature (sentiment) beyond whatever features the baseline uses.
  
  Without an ablation that compares FB-GAN against itself trained *without* the sentiment feature (same architecture, same hyperparameters), the reported 9% RMSE improvement cannot be attributed to sentiment rather than to increased model capacity, longer training, or simply having one more input dimension.

- **Sentiment signal is only present for ~17 months of the 5-year window, with no analysis of how this affects results.** News articles cover 01 Mar 2022 to 31 Jul 2023, while historical price data spans 01 Aug 2018 to 31 Jul 2023 (~3.5 years with no news, sentiment set to 0). The paper does not report whether the test set falls inside or outside the news-rich period, does not compare performance separately for periods with and without news coverage, and does not discuss how training on 3.5 years of constant-sentiment input affects the model's ability to learn from the limited window where sentiment actually varies. This makes it impossible to assess whether the sentiment feature genuinely drives improvement.

### Minor

- **No multiple runs, confidence intervals, or variance reporting.** All RMSE values in Table 1 appear to come from single runs. Given the known stochasticity of GAN training (random weight initialization, mini-batch sampling), single-run results are not reliable. The paper should report at least means and standard deviations over multiple seeds.

- **Qualitative "back-testing" relies on a single cherry-picked example.** Section 4.2 presents one news article (Amazon stock split) classified as positive with 99.9% confidence, noting a subsequent upward price movement. A single anecdotal example does not validate a claimed correlation between sentiment and price movement across the entire dataset, let alone prove that sentiment features improve prediction. The paper's claim that this "double verified our hypothesis" is an overstatement.

- **Temporal alignment of news and price data is underspecified.** The paper states "we assumed market sentiment for a particular day would have an effect on the next day's closing price" (Section 3.1.2) and that data were "combined on the basis of US Trading dates" (Figure 1). However, no timestamp granularity is disclosed. It is unclear whether news published after market close on day t was excluded from day t's sentiment calculation, and whether the alignment procedure ensures all features used to predict day t+1's close were actually available before that close. While a standard alignment is plausible, the paper does not document the procedure with sufficient detail for replication or verification.

- **Sentiment score weighting scheme design choices are unexamined.** Equation 1 maps labels to ±100/0 and averages weighted by FinBERT confidence. This treats a neutral article with 0.99 confidence the same as a neutral article with 0.51 confidence (both contribute 0), while a positive article with 0.51 confidence contributes +51. These discontinuities and the choice of ±100 scale are not justified, and FinBERT's calibration is not discussed.

### Trivial

- **Inconsistent feature enumeration.** FB-GAN is described as trained on "7 features" (Section 3.3) but only six are listed (Adj. Close, High, Low, Close, Open, and Market Sentiment Score; Volume is almost certainly the missing seventh but was lost to a parser artifact). This should be corrected for clarity.

- The comparison table (Table 1) is embedded as an image rather than rendered as text, which limits accessibility.

## Nice-to-Haves

- Report the fraction of trading days with non-zero sentiment for each stock, and check whether prediction errors correlate with the presence or absence of news.
- Segment the evaluation into pre-news (Aug 2018–Feb 2022) and news-rich (Mar 2022–Jul 2023) periods to test whether sentiment-driven improvements concentrate in the latter.
- Consider a simpler continuous sentiment scoring approach (e.g., using FinBERT's raw probability distribution across classes) rather than the ±100/0 discretization.

## Removed Points

These points were flagged for removal; they are listed here for transparency but should not be considered valid weaknesses.

1. **"FinBERT provides output between 0 and 1 but then hardcodes to ±100, losing information."** — This criticism misunderstands the pipeline. FinBERT outputs classification *labels* (positive/negative/neutral) with associated confidence scores. Mapping labels to values and weighting by confidence is a standard approach; the raw 0–1 outputs correspond to label probabilities, not a continuous sentiment score. The paper's use of these probabilities as weights in Equation 1 is appropriate.

2. **Sentiment signal only 17 months (kept as Major).** — This was kept, not removed. Already listed above.

3. **Strength Finder strength #3 (qualitative back-testing "confirms correlation").** — Removed because this conflicts with a verified weakness: a single anecdotal example does not confirm a correlation. The strength/weakness disagreement is resolved in favor of the weakness.

## Novel Insights

The reviewers converge on a core assessment that is greater than the sum of their individual points: this paper presents a reasonable pipeline (FinBERT → sentiment features → WGAN-GP) but makes the fundamental error of treating the comparison between architectures that differ in capacity, training budget, feature count, *and* the presence of sentiment as if it isolates only the last factor. The sentiment-ablation gap is a well-known pitfall in financial ML papers, and the additional ambiguity about train/test splitting compounds the problem. The paper's actual contribution — that a specific sentiment-weighted feature can improve a larger, longer-trained WGAN-GP variant — is weaker than claimed and cannot be attributed to sentiment without controlled experiments. Neither reviewer doubts that the components exist or that the pipeline can be built; the concern is whether the evaluation supports the causal claims made.

## Suggestions

1. **Adopt a strict chronological train/test split** (e.g., train on the earliest 80% of trading days, test on the most recent 20%). Report this explicitly and consider using a time-series cross-validation scheme (e.g., walk-forward validation) for robustness.

2. **Run a proper ablation**: compare FB-GAN (with sentiment) against FB-GAN trained on the *same architecture* and *same hyperparameters* but with the sentiment feature removed. This isolates the marginal contribution of sentiment from changes in model capacity, learning rate, and training epochs.

3. **Report RMSE separately for the pre-news period (Aug 2018–Feb 2022, sentiment=0) and the news-rich period (Mar 2022–Jul 2023).** If sentiment adds predictive value, the improvement should concentrate in the latter period.

4. **Run all experiments multiple times (at least 5 seeds) and report mean ± standard deviation.** This is standard practice for GAN-based methods.

5. **Document the exact temporal alignment procedure**: specify how news timestamps were normalized to trading days, whether any cutoffs were applied relative to market close times, and how the alignment ensures no look-ahead bias.

## Score and Decision

**Originality:** The combination of FinBERT sentiment features with WGAN-GP for stock prediction is not novel in isolation (prior work has used GANs with sentiment for stock prediction, as the paper itself cites). The specific architecture choices and the comparison across headline/summary/headline-summary variants provide incremental differentiation.

**Importance of research question:** Stock price prediction augmented with sentiment is a practically relevant and well-studied problem. The question is worthwhile but the paper does not advance the state of knowledge beyond what prior work has established, owing to the methodological issues.

**Claims support:** The central claims are not adequately supported. The claim that sentiment improves prediction is unsubstantiated because the ablation controlling for architecture is missing. The claim that FB-GAN outperforms baselines is weakened by the ambiguous train/test split and lack of variance reporting.

**Soundness of experiments:** Below the acceptance threshold. The missing chronological split specification, absent ablation, and single-run results are significant gaps that prevent the evaluation from being taken at face value.

**Clarity of writing:** Adequate but verbose. The methodology sections describe components in reasonable detail but omit critical experimental design choices (split method, alignment procedure).

**Value to community:** Limited without the experimental controls needed to validate the core claims. The paper would need substantial revision and additional experiments to provide reliable evidence.

**Overall:** The paper tackles a reasonable research direction but its empirical evaluation has three structural gaps — ambiguous train/test split, no ablation isolating sentiment, and no analysis of the limited sentiment window — that collectively prevent its claims from being credible. The issues are significant enough that they cannot be resolved in a conference rebuttal period; they require re-running experiments. The paper should not be accepted in its current form.

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**
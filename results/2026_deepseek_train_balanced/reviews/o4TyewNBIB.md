## Summary

FinRipple introduces a framework that augments LLMs with time-varying financial knowledge graphs (KG) via adapters and then aligns the model to market dynamics using PPO with a reward function grounded in CAPM residuals — treating the portion of returns unexplained by systematic market risk as a proxy for event-driven impacts. The paper defines the "event impact prediction" task, provides a benchmark dataset, and evaluates across multiple LLMs (llama2, vicuna, Phi-3.5, GPT variants) using R², ANOVA, refusal rates, and a portfolio backtest.

## Strengths

1. **Principled formalization of event impact prediction.** The paper formulates the task rigorously as a structured learning problem on a time-varying KG (Section 3.1, Equations 48–66), with a clear definition of the prediction function mapping company–event pairs to an impact score. This goes beyond prior work that reduces the problem to binary sentiment classification or single-stock return prediction.

2. **Comprehensive validation across multiple LLMs and metrics.** The evaluation spans 6+ LLMs of varying sizes using three complementary metrics (R² on CAPM residuals, ANOVA F-value/eta-squared, refusal-to-answer rate), plus a portfolio backtest (Tables 1–4). The ablation design (Zero-Shot → ICL → RAG → KG injection w/o alignment → FinRipple) cleanly isolates each component's contribution, and the consistent jump in R² after alignment (e.g., vicuna-7b-chat from 0.072 to 0.310) demonstrates that the RL objective is being meaningfully optimized.

3. **Diagnostic ablation with concrete failure-mode illustrations.** Section 4.4.1 and Figures 3–4 provide specific, illustrated examples of where RAG and subgraph traversal fail (industry-wide events lacking a target company, low recall of semantic-similarity-based retrieval on large graphs), substantiating why parameterized KG injection via adapters is necessary beyond what a retrieval-based approach would achieve.

4. **Time-varying KGs with economically meaningful relationship types.** The KG incorporates leadership networks, mutual fund holdings, patent relationships, and supply chains — each grounded in prior finance research — rather than relying on static industry classifications or simple co-occurrence statistics.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated proxy assumption linking CAPM residuals to event impacts.** The entire training and evaluation pipeline hinges on the claim that CAPM residuals approximate the "true influence" of financial events (Section 3.1, line 66–67). The paper provides no independent validation of this assumption — no hand-annotated ground truth for event impacts, no out-of-sample event study with known outcomes, and no analysis showing that the model's predicted impacts correspond to identifiable events rather than simply fitting residual noise. The evaluation metrics (R², ANOVA) measure how well predictions match the same CAPM residuals used in training. While this is not a strict tautology (the training reward uses cosine similarity + coverage, while evaluation uses R²), the fact that training and evaluation targets derive from the same data source means the headline numbers primarily demonstrate that the RL optimization worked — not that the model has learned about event-specific impacts. The portfolio backtest provides some external validation, but without isolating the event-prediction component from other factors (see Minor Weakness 1), it is insufficient to bridge this gap alone.

2. **Missing non-LLM baselines for the proposed benchmark.** The paper claims to establish a new task and benchmark, yet compares only LLM variants (zero-shot, ICL, RAG, ablated FinRipple). No comparisons are provided against simpler alternatives that could operate on the same KG features: linear factor models, gradient-boosted trees, LSTMs, or graph neural networks trained to predict CAPM residuals from the KG structure. Without these, the reader cannot assess whether the complex LLM pipeline adds value over substantially simpler methods, or whether the 0.34 R² ceiling is actually competitive with what a basic regression on KG features would achieve.

3. **Temporal contamination risk in dataset split.** The test set comprises ~10,000 articles from January 2020–June 2022, while the training set uses ~110,000 articles from "other years" (Section 4.1, line 120). The paper never specifies which years constitute "other years." If the training data includes articles after June 2022 (the test period endpoint), the model would have access to future information relative to the test window, creating a look-ahead contamination issue for the portfolio backtest. This ambiguity needs to be resolved.

### Minor

1. **Portfolio backtest has limited diagnostic power.** The backtest (Table 4) uses a daily long-short strategy on S&P 500 constituents from January 2020–June 2022, a period spanning the COVID crash and sharp recovery. No transaction costs or slippage are mentioned, despite daily rebalancing of the top/bottom 10% of stocks. The compared benchmarks (equal weight, volatility weight, Markowitz, min-variance) are generic allocation rules, not alternative event-prediction methods — so the backtest does not isolate whether the *event prediction* component adds value over a simple momentum or sentiment-based strategy. The strong performance could partly reflect the strategy's momentum exposure (long recent winners, short recent losers) during a trending market.

2. **Single qualitative case study for reasoning analysis.** Figure 5 presents one Chain-of-Thought example as evidence that the model "establishes connections with past news" and "provides reliable insights into the causal relationships driving market impacts." A single generated example — whose reasoning may be post-hoc plausible rather than genuinely causal — does not constitute evidence of reliable reasoning. At minimum, the paper should report the proportion of CoT outputs that contain verifiably correct causal chains on a held-out set of events with known ground-truth propagation paths.

3. **No ablation of the four KG relationship types.** The KG includes leadership networks, mutual fund holdings, patent relationships, and supply chains. The paper does not analyze which relationship types drive performance, whether all four are necessary, or whether a simpler one-hop neighbor list would suffice. This information is important for understanding the method's mechanism and for practitioners who might lack access to all four data sources.

### Trivial

None.

## Nice-to-Haves

- Using a multi-factor model (e.g., Fama-French 3-factor or 5-factor) instead of CAPM alone would produce residuals with less systematic contamination from size, value, and momentum effects, making the attribution to event impacts more defensible.
- Disclosure of the λ value in Equation 10 and key PPO/alignment hyperparameters would aid reproducibility (if these are in a stripped appendix, this is already addressed).
- Adding an out-of-sample event study — holding out known event dates and testing whether predicted impacts explain cross-sectional abnormal returns estimated on a pre-event window — would directly address the proxy validation concern.

## Removed Points

These points were flagged by the reviewers but removed for the following reasons:

- **Criticism that "CAPM is hopelessly outdated" / must use Fama-French models:** Demoted to Nice-to-Have. Using CAPM is a reasonable starting point; the paper positions itself as complementing classical models. The multifactor model suggestion is valid but does not invalidate the current results.
- **Criticism about missing hyperparameters (λ value, PPO details, LoRA rank):** Removed per Hard Rules — the parser strips appendix and supplementary material from all papers; these details likely exist in the original submission.
- **Criticism that the R² of 0.34 is "surprisingly modest" and "raises questions about optimization quality":** Removed. Financial data is inherently noisy; an R² of 0.34 for residual prediction is not obviously low for this setting, and the internally valid ablation (aligned vs. unaligned) shows substantial improvement.
- **Criticism about the KG injection stage being too simple (factual recall only):** Removed. The paper explains that KG injection teaches market *structure*, while market alignment teaches impact *magnitudes* — these serve different purposes.
- **Strengths that were generic or sycophantic (e.g., "addresses an important problem," "targets an interesting question," "makes a significant contribution to the field"):** Removed per filtering rules. Only concrete, evidence-backed strengths were retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the proxy assumption externally.** Construct a small dataset of clearly identifiable events (CEO changes, regulatory actions, product announcements) with expert-annotated impact directions and relative magnitudes across affected companies. Evaluate whether FinRipple's predictions match these annotations — this would directly test whether the model has learned about event impacts rather than just fitting CAPM residual patterns.

2. **Add at least two non-LLM baselines** to the benchmark: (a) a simple linear model regressing CAPM residuals on KG-derived features (node centrality, shortest paths to event company, relationship-type indicators), and (b) a small graph neural network trained on the KG to predict residuals. This would contextualize whether the LLM's capacity is actually needed.

3. **Clarify the temporal split.** Specify exactly which years are used for training and confirm that no training data postdates the test window (June 2022). If it does, report the backtest on a non-contaminated holdout period.

4. **Ablate the four KG relationship types** to identify which ones drive the performance gains. This would deepen the contribution and guide future practitioners.

5. **Address the portfolio backtest's ambiguities** by reporting turnover-adjusted returns (accounting for transaction costs) and comparing against a momentum-based strategy that would control for the simplest alternative explanation of the long-short returns.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
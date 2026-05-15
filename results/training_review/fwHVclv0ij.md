Now I have all the information I need. Let me carefully synthesize the review, cross-referencing every claim against the paper.

---

## Summary

This paper proposes an online change-point detection method for black-box LLMs, where the detector sequentially interacts with an LLM using prompts. The method uses a CUSUM-type statistic computed from entropy and Gini coefficient-based metrics on the response text (first-token and N-token variants), combined with a UCB-based adaptive prompt selection strategy to focus query budget on change-sensitive prompts. The approach is evaluated on synthetic data (watermark injection, model version swaps) and on daily interactions with 9 real-world LLM APIs over three months.

## Strengths

- **Addresses a timely and practically important problem**: Online detection of behavioral changes in black-box LLMs (whether from intentional updates, security tampering, or drift) is a genuine gap. The paper correctly motivates why white-box or offline methods are insufficient, and the framing of the problem as sequential interaction with a query budget is well-reasoned (Section 2).

- **Adaptive prompt selection via UCB is a principled approach**: The use of multi-armed bandit ideas to dynamically allocate queries to change-sensitive prompts is sensible. Figure 6b provides concrete evidence that the adaptive selection achieves a better ADD-ARL trade-off than random selection or any single fixed prompt, validating this module.

- **Complementary use of entropy and Gini metrics**: The paper motivates entropy (sensitive to probability spread) and Gini (sensitive to dominant outcomes) as complementary signals. Figure 3 shows both families respond to the watermark change, and the parallel monitoring scheme (Eq. 1) hedges against the possibility that some statistics are insensitive to a particular type of change (Remark 1).

- **Substantial real-world data collection effort**: Collecting daily responses from 9 major LLM APIs over three months (June–August 2024) is a significant undertaking that goes beyond static benchmarks, and could serve as a resource for the community.

## Weaknesses

### Fatal
None.

### Major

1. **N-token entropy/Gini approximation conflates marginal and joint distributions, undermining multi-token claims.** The paper defines NTE and NTG as properties of the *joint distribution* P(z₁,...,z_N|x) (Eqs. 2, 5), but the empirical implementation (Section 3.2) pools all first-N tokens across C responses into a single multiset and computes a *marginal* empirical distribution over individual tokens. The paper is transparent that this "is different from the joint distribution," but does not justify why this approximation preserves any signal about token dependencies or multi-token structure. The resulting statistic is not an estimate of the joint entropy/Gini — it discards all within-response positional dependencies. Since the paper motivates computing N>1 metrics precisely to capture multi-token patterns ("not all changes can be effectively captured by the distribution of the first token," line 70), this gap is serious: the pooled statistic could still be useful, but the paper provides no argument or experiment to show that it adds value beyond the first-token metrics, nor does it validate that the approximation captures anything the first-token metrics miss.

2. **No comparison to any baseline detection method.** The synthetic experiments (Section 4.1) show that the proposed statistics respond to changes, and the adaptive-vs-random comparison (Figure 6b) is an ablation of one component. But there is no comparison against any alternative online detection scheme — e.g., a simple sliding-window test on entropy, CUSUM on a different heuristic feature (perplexity, response length), or a pre-trained classifier. Without baselines, the claim of "effectiveness" is unsubstantiated relative to obvious alternatives. This is the most consequential evidential gap in the paper.

3. **Real-world evaluation is too thin to support the paper's claims.** For the confirmed Mistral update (Section 4.2): only one detection statistic (NTG on prompt 0) is shown (Figure 7); no detection delay, no ARL calibration, no threshold justification, no table of results across all 9 APIs or all prompts. The "unconfirmed" changes for GPT-4 Turbo and Jamba are claimed based on observed spikes in a subset of prompts (Figure 8), but no false-alarm analysis is performed — over 92 daily rounds with 20 prompts, isolated spikes are expected by chance. The pre-change historical period (June 1–5) is only 5 days, which is too short to estimate the null distribution reliably. The paper's claim of "strong evidence of unreported changes" (Abstract, Conclusion) is not supported by the evidence presented.

4. **Synthetic experiments lack statistical rigor.** The watermark experiment (Section 4.1.1) uses one prompt, one watermark strength (δ=2, γ=0.5), and appears to show a single trial. The synthetic version change results (Figure 4) show four separate cases, but each appears to be a single trace without error bars or repeated trials. The ADD-ARL curves in Figure 6b are based on 20 experiments (which is good), but the core detection results lack this kind of replication.

### Minor

- **Hyperparameter sensitivity is unexplored.** The drift parameter d=0.5 and the UCB parameter α=8 are fixed throughout, with no ablation or sensitivity analysis. The threshold b is "determined via simulation" but no details of the procedure are given. The method's performance likely depends on these choices, and the paper provides no guidance for practitioners.

- **The CUSUM statistic is described as "novel" but is a standard application.** The two-sided mean-shift CUSUM applied to normalized metric values (Eq. 3) is a textbook formulation. The paper does not claim algorithmic novelty in the CUSUM itself, but the phrasing in the Introduction ("we derive a CUSUM-type detection statistic") slightly overstates what is a straightforward adaptation.

- **Real-world data uses a fixed tokenizer (opt-125m) for models from different families.** While the paper acknowledges this for two APIs that provide their own tokenization, using a single tokenizer across diverse LLMs (Section 4.2) could introduce systematic bias in the token distributions, and the impact is not discussed.

### Trivial
None beyond formatting artifacts that are parser issues.

## Nice-to-Haves

- A synthetic experiment that systematically varies the change magnitude (e.g., watermark strength δ) and plots detection rates (AUC-style) to characterize the sensitivity of each metric.
- An experiment isolating the value of the N-token metrics: does the pooled N-token approximation actually improve detection over using only first-token metrics? This would help determine whether the NTE/NTG approximation issue is practically important or benign.
- Reporting ADD with confidence intervals for all synthetic experiments.

## Removed Points

The following points from the input reviews were removed with justification:

- **"The paper's method cannot be independently verified because models/data are not released"** (from Harsh Critic's implicit framing): The paper cites models, benchmarks, and the Mistral update announcement. Per hard rules, all cited entities are assumed to exist and be released. This concern is removed.

- **Generic strength from Strength Finder: "The paper addressed an important problem"** (without specific evidence): This is generic and conflicts with a verified weakness (limited evaluation). Moved here.

- **Strength Finder claim of "Comprehensive empirical validation"** : The real-world evaluation is not comprehensive — it is limited and anecdotal. The strength conflicts with verified weaknesses about insufficient evaluation. Moved here.

- **Various formatting/style nitpicks from Harsh Critic's section-by-section notes** (e.g., about "novel" derivation being overstated is kept as a Minor weakness above, but pure presentation notes are removed per hard rules).

- **"Missing related work"** : Per hard rules, this is removed as the reviewer cannot confirm the existence of missing references without external sources.

- **Demands for theoretical proofs of CUSOM behavior** (from Harsh Critic's "obvious next steps"): This is a nice-to-have, not a core expectation for an empirical systems paper. Moved here.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent picture: the paper identifies a real and important problem and proposes a reasonable overall framework (CUSUM on text summary statistics + UCB prompt selection), but the experimental evaluation is substantially weaker than the paper's claims would require. The NTE/NTG approximation issue is a methodological concern that the paper transparently acknowledges but does not validate, and the absence of any baseline comparison undermines the ability to assess whether the method represents an advance over simpler alternatives.

## Suggestions

1. **Add baseline comparisons.** At minimum, compare against: (a) a CUSUM using only first-token entropy (FTE), to isolate the value of the multi-token and Gini metrics; (b) a simple sliding-window threshold on mean FTE; (c) a non-adaptive version that uses a fixed random subset of K prompts each round (this is already partially done in Figure 6b but should be a full ADD-ARL comparison). Also compare against any relevant prior work on LLM change detection.

2. **Validate the N-token approximation.** Provide either a theoretical justification or an empirical ablation: show detection results using only first-token metrics (FTE, FTG) and compare to the full set including the pooled NTE/NTG. If the N-token metrics add no value, drop them or rename them to avoid the misleading "joint distribution" framing.

3. **Strengthen the real-world evaluation.** Report: (a) the threshold calibration procedure; (b) the empirical false alarm rate on a holdout pre-change period; (c) detection delay for the Mistral update across all prompts and metrics; (d) a quantitative summary table for all 9 APIs showing detection times and the number/fraction of prompts that triggered.

4. **Add error bars and multiple trials to synthetic experiments.** Report ADD/ARL with standard errors or confidence intervals (as done partially in Figure 6b). Vary the watermark strength or change magnitude to characterize the method's operating range.

5. **Conduct hyperparameter sensitivity analysis.** Study the impact of d (drift), α (UCB exploration), and the number of repeated responses C on the ADD-ARL trade-off.

## Score and Decision

The paper addresses a relevant problem and proposes a reasonable framework, but the evaluation has critical gaps: no baseline comparisons, an unvalidated approximation in one of the metric families, and real-world results that are too thin to support the claimed conclusions. The core ideas have potential, but the evidence presented does not currently meet the bar for publication.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
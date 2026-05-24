Here is my final consolidated review.

---

## Summary

This paper identifies a "self-stimulation" problem in time series forecasting—models predict the future using only historical values and thus ignore external influences. It provides a control-theoretic formulation showing that ignoring external influences creates an irreducible error bound. To address this, the paper proposes the Influence-Aware Time Series Forecasting (IATSF) paradigm, contributes a leak-free benchmark with temporally-synced textual influences, and develops FIATS, a lightweight model with channel-aware mechanisms (CASM, CAPS) that operationalizes influence-awareness. Experiments on synthetic and three real-world systems show FIATS significantly outperforms self-stimulated baselines including foundation models.

## Strengths

- **Principled problem identification and formalization**: The paper provides a clean control-theoretic framing (Propositions 2.1 and 3.1) that formalizes why self-stimulated models face an irreducible error floor when external influences are ignored. While the underlying mathematics is elementary, its application to contextualize a known empirical plateau in time series forecasting is a useful conceptual contribution.

- **Compelling synthetic validation**: On the Frequency Modulated Toy dataset (Table 1), FIATS achieves near-zero MSE (0.003–0.027) while all baselines—including billion-parameter foundation models—produce orders-of-magnitude larger errors. This directly confirms that the performance gap on this task is caused by missing influence information, not model capacity.

- **Comprehensive ablations isolating the source of gains**: Table 3 shows that removing influence inputs ("Zero News") collapses FIATS to the performance level of self-stimulated models, and removing channel descriptions ("Zero Desc.") also significantly degrades performance. This cleanly attributes the gains to the influence information and the CASM mechanism, not to model scale.

- **Consistent and substantial improvements across real-world systems**: FIATS achieves average MSE reductions of 36% on Atmospheric Physics and 44% on NYC Traffic Speed over the best self-stimulated baseline (PatchTST), demonstrating the paradigm's effectiveness beyond controlled settings.

- **New benchmark resource**: The IATSF benchmark, designed with careful consideration of temporal synchronization and leak-free influences, addresses a real gap in the multimodal TSF ecosystem and could be valuable to the community if released.

## Weaknesses

### Major

- **Missing control baseline using the same influence information in numerical form**: The core claim is that influence-awareness drives performance, but the main comparisons pit FIATS (which has access to textual influence data) against baselines with zero access to any influence information. There is no experiment where, e.g., numerical weather forecast variables (temperature, precipitation probability) are fed as exogenous channels to DLinear or PatchTST. Without this control, it is unclear whether the gains come from the qualitative richness of text or simply from having more input features. The "Zero News" ablation shows that removing text hurts FIATS, but does not answer whether a simpler, non-textual predictor using the same information would perform similarly. This gap weakens the paper's central empirical argument.

- **No statistical uncertainty reported**: No confidence intervals, standard deviations, or multiple-seed runs are reported for any result in Tables 1 or 2. Given the number of comparisons, it is impossible to assess whether the observed differences are statistically reliable. This is a standard expectation for empirical ML papers.

### Minor

- **Interpretability analysis is entirely qualitative**: The attention map analysis (Figures 3, 5) is presented as evidence that FIATS learns interpretable influence-to-channel mappings, but no quantitative validation is provided. For example, on the FM Toy system where the true sensitivity is analytically known, the paper could have correlated the learned attention weights with the ground-truth sensitivity matrix. As presented, the interpretability claims are suggestive but unsubstantiated.

- **"Leak-free" claim for weather-forecast datasets is imprecise**: The benchmark is described as "leak-free" because it uses "independently evolving influences." However, weather forecasts for the Atmospheric Physics dataset are predictions of the same atmospheric system being forecast, so they are necessarily correlated with the future target values. The paper acknowledges these are "predictions of U_f from expert sources" (Section 4.1), which is reasonable, but calling this "leak-free" without quantifying the potential correlation or discussing its implications for the theoretical framework (Proposition 3.1 assumes independent influences) is somewhat oversold.

- **"LLM-free" claim is imprecise**: FIATS is described as "LLM-free" (Section 5), but it relies on pre-trained text embeddings from models such as OpenAI, MiniLLM, and mpnet, which are language models. The paper's intended contrast is with *generative* LLMs (avoiding their variance and token overhead), but the "LLM-free" label as written is technically inaccurate and could mislead readers.

- **Qualitative failure case is not deeply analyzed**: The case study (Figure 3) mentions that FIATS misses a rainfall event "due to misaligned or absent external information," which is an honest admission of dependence on influence quality. However, the paper does not systematically analyze this failure mode or characterize how often it occurs, leaving an important practical limitation underexplored.

### Trivial

- The notation for the CASM block formula (Argmax_i(kW_K)_i) is unclearly defined in the text (Section 5 description).

## Nice-to-Haves

- An ablation that removes CASM but keeps influence information (i.e., feeds influence embeddings directly to the decoder without channel-wise attention) would help separate the benefit of channel-specific sensitivity modeling from simply having more input features.
- A systematic perturbation of influence quality (random time shifts, replacement with irrelevant text) beyond the round-robin noise experiment (Figure 6) would strengthen the robustness analysis.
- Evaluating the framework on standard benchmarks (ETT, Weather) with constructed textual influences would demonstrate broader applicability.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- *"Theory is standard control theory dressed as novel finding"* (from Harsh Critic #3): While the propositions are indeed simple, the paper's contribution lies in applying this framing to the self-stimulation problem in TSF, not in the mathematical novelty of the bounds themselves. The paper does not claim the math is novel; it claims the *identification* of the problem through this lens is novel. This criticism is too harsh for a valid weakness and would apply to many applied papers that use textbook results as motivation. Removed.

- *"Overstated claim about foundation models vs linear baselines"*: The harsh critic claims the paper inaccurately states that foundation models struggle against linear baselines, but this is a well-documented observation in the TSF literature (Zeng et al., 2023; Toner & Darlow, 2024). The paper's experiments on its own datasets confirm this phenomenon. The criticism is factually inaccurate about the paper's claim. Removed.

- *"Section 2 exposition imprecise about partial observability"*: The paper explicitly states "For analytical clarity, we assume full observability, i.e. X = Z" (Section 2.1). This is a standard simplifying assumption in theoretical frameworks. Criticizing it for not discussing partial observability is scope creep. Removed.

- *"Missing details about textual influence collection, no examples given"*: This criticism stems from missing appendix content that the parser stripped. The paper explicitly references Appendix N and Appendix O for full details. Removed per hard rule about missing appendix content.

- *"No evidence on whether text-based influences generalize better than numerical ones"*: The paper scopes its contribution as introducing the IATSF paradigm and demonstrating its viability through text. Explicitly testing whether text generalizes better than numerical influences across contexts is beyond the stated scope and would be a follow-up study. Wakened to nice-to-have.

- *"No comparison against generative LLM finetuned on the same data"*: The paper explicitly contrasts its approach with LLM-based methods and argues that using frozen text embeddings avoids the overhead of generative LLMs. Requesting this comparison is scope creep. Removed.

- *"Apply framework to standard benchmarks"*: This is a suggestion for future work, not a weakness. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviewer pool did not surface an insight that the paper itself does not already articulate.

## Suggestions

1. **Add the missing exogenous baseline**: Feed numerical weather forecast variables (temperature, precipitation probability, etc.) as additional channels to DLinear and PatchTST on the Atmospheric Physics and NYC Traffic datasets. This directly tests whether the gains come from the information itself or from its textual representation.

2. **Report confidence intervals**: Run each experiment over at least 3–5 seeds and report mean ± std for all main results. This is critical for assessing the reliability of the reported improvements.

3. **Tighten the "leak-free" language**: Explicitly discuss the relationship between weather forecasts (which are predictions of the same system) and the theoretical requirement of independent influences. Acknowledge that the benchmark is "leak-free" in the sense of not using the target system's own future observations, but that the strict independence assumption of Proposition 3.1 is an idealization.

4. **Validate attention interpretability quantitatively**: On the FM Toy dataset where the true influence-to-channel mapping is known, compute a correlation metric between the CASM attention weights and the ground-truth sensitivity matrix B. This would transform the interpretability claim from qualitative to quantitative.

5. **Evaluate failures systematically**: Instead of a single missed rainfall event, categorize and count how often FIATS fails when influence quality degrades, and characterize the conditions under which this happens.

## Score and Decision

### Calibration Anchors (all from the 13k human-review corpus)

| Path | Avg Human Score | Comparison to Paper Under Review |
|------|----------------|-----------------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/mfc6FKgtQA.md` (TGTSF, Reject) | 5.00 | Very similar paper proposing text-guided TSF with cross-attention and benchmarks. Current paper adds theoretical grounding and more thorough ablations. Slightly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4F1a8nNFGK.md` (Context is Key, Reject) | 5.00 | Similar paradigm of using textual context for forecasting. Current paper has model + theory + benchmark, making it somewhat more complete. Comparable quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QE1ClsZjOQ.md` (Dual-Forecaster, Reject) | 4.50 | Multimodal TSF with text; less rigorous methodology. Current paper is stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JYTQ6ELUVO.md` (Specialized FMs, Accept) | 6.50 | Well-executed empirical study with rigorous methodology and clear claims. Current paper is weaker in experimental rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bWcnvZ3qMb.md` (FITS, Accept) | 8.00 | Extremely clean paper with strong results and comprehensive experiments. Current paper is significantly less polished and less rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2wwPG1wpsu.md` (LST-Bench, Reject) | 2.50 | Poorly executed benchmark. Current paper is much stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1CLzLXSFNn.md` (TimeMixer++, Accept) | 8.00 | SOTA model with comprehensive evaluation across 8 tasks. Significantly stronger and more rigorous. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4NhMhElWqP.md` (DAM, Accept) | 7.00 | Foundation model with strong experimental methodology. Stronger than current paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/w8JizpeY4y.md` (Continuous Modeling, Reject) | 6.00 | Competent paper with good methodology but rejected. Current paper is slightly weaker in experimental rigor. |

**Positioning**: The paper is clearly stronger than the 2.5–4.5 papers and comparable to or slightly above the ~5.0 papers on similar topics (TGTSF, Context is Key). It adds theoretical framing absent from those papers and demonstrates a clear and convincing effect on the synthetic toy. However, it falls short of the 6.0+ papers due to the missing critical control experiment (numerical exogenous baseline) and lack of statistical rigor (no confidence intervals). The core idea is sound and the paper has real potential, but the evidence does not fully support the strength of the claims in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
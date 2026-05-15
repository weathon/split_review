Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes TEMPO, a framework that integrates STL decomposition (trend, seasonal, residual) with semi-soft prompt tuning and a frozen GPT backbone for zero-shot time series forecasting. The core idea is to decompose raw time series into components before feeding them into a pre-trained language model, and to use component-specific learnable prompts to guide adaptation. Experiments are reported on seven benchmark datasets and two multimodal datasets, including a newly introduced TETS benchmark.

## Strengths

- **Novel synthesis of statistical decomposition + pre-trained transformer + prompting**: Explicitly decomposing time series into trend/season/residual components before feeding them into a frozen GPT backbone, combined with component-specific semi-soft prompts, is a principled and underexplored approach. This differs from prior LLM-for-time-series works (e.g., One Fits All) that input raw series without such inductive biases. (Evidence: Sections 3.2, 3.3, Figure 1)

- **Interpretability via component-wise analysis**: The paper uses SHAP values on a generalized additive model to quantify each component's contribution to predictions, showing seasonal dominance on ETTm1 — a transparency rarely provided by deep forecasting models. (Evidence: Section 5.2, Figure 6)

- **Multimodal extension**: The inclusion of contextual text alongside time series (via text-derived soft prompts) is a natural and extensible design. The new TETS dataset, if properly documented, could be a useful resource. (Evidence: Section 4.2)

## Weaknesses

### Fatal
None.

### Major

1. **Zero-shot baseline configuration is not described — the paper's central empirical claim cannot be verified.**  
   The paper reports zero-shot ("many-to-one") results in Table 1 but never specifies how the non-pre-trained baselines (PatchTST, FEDformer, DLinear, Informer, ETSformer, TimesNet) were adapted for this setting. These architectures do not natively support zero-shot forecasting. The paper states only that "we adopt a uniform training methodology to ensure fair performance assessment" (line 136) without revealing what that methodology was. Were these baselines trained on the same source datasets as TEMPO? Were they evaluated directly without adaptation? Were they fine-tuned on the target (which would break the zero-shot comparison)? The reader cannot tell. Since the paper's headline claim is *superior zero-shot performance*, this omission is critical — it renders the main experimental results uninterpretable. The distinction is noted in the multimodal experiments (line 161 mentions "training from scratch" for that setting) but is absent for the main zero-shot Table 1.

2. **Ablation study covers only 2 of 7 datasets and shows non-uniform superiority.**  
   The ablation (Table 5.2) evaluates only ECL and ETTm1, leaving out ETTh1, ETTh2, ETTm2, Weather, and Traffic — 5 of the 7 datasets from the main results. Moreover, on several individual horizons (e.g., ECL-720: TEMPO MSE 0.279 vs. w/o Dec Loss 0.262 and w/o Dec MAE 0.351 vs. TEMPO 0.355; ECL-192: w/o Pro MSE 0.196 vs. TEMPO 0.198; ETTm1-720: w/o Pro MSE 0.582 vs. TEMPO 0.591), the full model is *not* the best performer. Only on average across horizons does TEMPO always lead. Combined with the missing datasets, this undermines the claim that both prompt and decomposition are "essential" and raises the possibility of cherry-picking. (Evidence: lines 189–199)

3. **TETS dataset is introduced without any meaningful description.**  
   The paper states "we introduce TETS, a new benchmark dataset built upon S&P 500 dataset combining contextual information and time series, to the community" (line 155) — and provides no further details about construction, size, train/test splits, preprocessing, or quality assurance. Since the dataset is new, the results in Table 3 are unverifiable by reviewers. A dataset contribution requires documentation that allows others to understand, reproduce, and use it. (Evidence: line 155 only)

### Minor

4. **Decomposition loss is vaguely defined.**  
   The decomposition loss $L_{Dec}$ is described as aligning "local decomposition" with "global STL decomposition observed in the training data" (lines 95–96), but what constitutes the "global" decomposition is never operationalized. Is it STL applied to the full training time series? Precomputed and stored? The ablation shows removing this loss degrades performance, but the reader cannot tell what was actually ablated. This vagueness hurts reproducibility.

5. **Theoretical framing has limited connection to the method.**  
   Theorem 3.1 shows that non-orthogonal components cannot be separated by orthogonal bases. The paper then asserts (citing one_fits_all) that self-attention learns an orthogonal transformation, motivating explicit STL decomposition. Even accepting this chain, STL itself does not produce orthogonal components — trend and season from STL can be correlated — so the theorem does not specifically justify STL over any other decomposition choice. The theoretical framing is more suggestive than logically binding.

6. **No comparison to supervised TEMPO (oracle setting).**  
   The paper does not report how TEMPO would perform if trained *with* target data — a "supervised oracle" baseline. Such a comparison would contextualize the zero-shot results (e.g., how much is lost by not seeing target data) and help validate that the model is learning meaningful representations rather than exploiting dataset artifacts.

### Trivial
- The variable $V^i$ in the problem definition (Eq. 1) is introduced as a "prompt" but treated as per-channel; later it becomes per-component. This notational inconsistency is minor but causes initial confusion.

## Nice-to-Haves
- Sensitivity analysis on patch length and stride would strengthen the methodological characterization.
- Visualizations of actual forecasts (prediction vs. ground truth) for TEMPO and baselines would help readers assess whether MSE/MAE improvements are systematic or sporadic.
- A comparison using the same decomposition + prompting strategy for other LLM backbones (GPT-2, T5, LLaMA) would isolate the benefit of TEMPO-specific components from the benefit of using any pre-trained LLM.

## Removed Points

The following points from the reviews were evaluated but removed with justification:

- **"Zero-shot description is contradictory"** (Harsh Critic, Issue 1): The reviewer claimed the paper's weather example contradicts showing ETTm1 results. This is a misreading — the paper provides weather as one example of the many-to-one protocol; for ETTm1 as target, the model would be trained on all other datasets including weather. There is no contradiction. **Removed: factually wrong.**

- **"Introduction straw man about prior works not capitalizing on patterns"** (Harsh Critic, Section-by-Section): The paper says prior works "have not fully capitalized on" trend/season patterns. This is a soft motivational statement, not a factual claim, and is common in papers introducing a new perspective. ETSformer, N-BEATS, and Autoformer do model these patterns, but the paper does not claim they don't. **Removed: mischaracterizes a generic motivation as a straw man.**

- **"Semi-soft prompt is just soft prompting with initialization, not novel"** (Harsh Critic, Section-by-Section): Whether this counts as "novel" is a subjective opinion, not a verifiable weakness. The paper clearly acknowledges its soft-prompt lineage. **Removed: opinion, not a substantive flaw.**

- **"RevIN breaks additive decomposition"** (Harsh Critic, Section-by-Section): The paper normalizes each component separately and de-normalizes the aggregate output. The additive structure is preserved through separate processing and re-combination. The reviewer's claim is not supported by the paper's actual pipeline. **Removed: misreading of the method.**

- **"SHAP analysis is trivial"** (Harsh Critic): The reviewer dismisses the SHAP analysis as uninteresting. While the findings may not be surprising, interpretability analysis is a standard and useful contribution. This is an opinion, not a methodological weakness. **Removed: subjective judgment.**

- **"Strength about ablation"** (Strength Finder): The Strength Finder lists ablation as a strength, but given the verified weaknesses (incomplete coverage, non-uniform superiority), this strength conflicts with verified weaknesses and is dropped per instructions. **Removed: conflicts with verified weakness.**

- **Various format/style nitpicks and requests for appendix content** that the PDF parser would have stripped: removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the importance of rigorously documenting zero-shot protocols for baselines — a meta-observation relevant beyond this paper — but do not generate a genuinely novel research insight.

## Suggestions

1. **Define the zero-shot protocol for every baseline in Table 1** — For each non-pre-trained baseline, specify precisely what data it was trained on, what hyperparameters were used, and how zero-shot evaluation was conducted. If baselines cannot reasonably operate in a zero-shot setting, consider re-framing the comparison or adding a transfer-learning / few-shot condition.

2. **Complete the ablation** — Add ablation results for all 7 datasets (at minimum, the averaged metrics) so the reader can assess whether the patterns on ECL and ETTm1 generalize.

3. **Document the TETS dataset** — Provide construction methodology, size statistics, train/test splits, preprocessing steps, and domain descriptions.

4. **Clarify the decomposition loss** — Define "global STL decomposition" precisely and explain how it is computed during training.

5. **Add a supervised oracle** — Train TEMPO with access to target data and report the gap between zero-shot and supervised performance.

## Score and Decision

**Originality**: 6/10 — The combination of decomposition + prompting + frozen GPT is novel, though each component is individually well-studied.  
**Importance of research question**: 7/10 — Zero-shot time series forecasting is a timely and impactful problem.  
**Claims supported**: 3/10 — The central claim of superior zero-shot performance is not adequately supported due to undocumented baseline configuration.  
**Soundness of experiments**: 3/10 — Insufficient documentation of the experimental protocol, incomplete ablation, and an undocumented new dataset.  
**Clarity of writing**: 6/10 — Methodology is clearly described; experimental setup is opaque.  
**Value to community**: 5/10 — The approach has potential, but the paper as submitted does not provide enough information for others to build on the results.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
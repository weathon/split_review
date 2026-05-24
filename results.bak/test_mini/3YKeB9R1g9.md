Now I have enough information to construct the final consolidated review.

Here is the consolidated final review:

## Summary

This paper extends the training-loss-curve (TLC) collapse phenomenon — previously shown only at small scale with vanilla Adam (Qiu et al., 2025) — to practical LLM families trained with AdamW, weight decay, co-scaling of width/depth/batch size, and μP/CompleteP. It identifies the AdamW timescale τ (jointly set by learning rate, weight decay, and batch size) as the key modulator of TLC shape, showing that collapse occurs precisely when τ, TPP (tokens-per-parameter), and the LR schedule are matched across model sizes. On this basis the paper trains the Celerity model family (300M–3.9B params) with demonstrable collapse, and demonstrates two practical applications: using collapse residuals for early detection of training pathologies, and fitting a parametric surrogate on small-scale runs to enable early stopping in hyperparameter tuning after only 10–30% of training.

## Strengths

1. **Demonstrates TLC collapse under practical LLM scaling recipes, directly addressing the gap left by Qiu et al. (2025).** Figure 4 (right) shows normalized loss curves from 111M to 3.3B parameters collapsing when TPP and τ are held fixed, spanning a ~1000× range in training FLOPs. Figure 6 further confirms collapse for Celerity at both 20 TPP and 80 TPP. This extends collapse from small-scale μP-with-vanilla-Adam to practical AdamW-with-weight-decay setups.

2. **Identifies the AdamW timescale τ as the key modulating factor of TLC shape and explains its effect via a noisy quadratic model.** Figure 3 systematically sweeps η, λ, and B and shows that curves with matching τ have nearly identical shapes — even when the underlying hyperparameters differ. Section 3 and Appendix B.3 provide an analytical expression (Eq. 3) connecting τ to the bias–variance trade-off, showing that the normalized TLC depends only on τ and t̂ after normalization.

3. **Demonstrates two concrete practical applications of collapse.** (a) Monitoring: Figure 1 (right) shows that collapse residuals flagged a numerical issue in the 1.8B run starting around 60% of training, well before the raw loss curve showed a visible upward trend near 90%. (b) Early stopping: Figure 9 shows that the "predicted best" method (aligning partial curves to a small-scale parametric surrogate) achieves near-zero loss gap relative to the true optimal λ when stopping at 10–30% of training, substantially outperforming the "current best" baseline.

4. **Introduces Celerity, a competitive LLM family trained in the collapse regime.** Celerity models (300M–3.9B) are shown in Figure 2 to sit on the accuracy/compute Pareto frontier among open models of comparable scale. Against BTLm, Celerity achieves comparable accuracy with 75% fewer training FLOPs. The paper provides a principled analysis (Figure 5) of the compute vs. parameter-efficiency trade-off when choosing TPP.

5. **Provides theoretical grounding for the empirical findings.** The noisy quadratic model (Eq. 3, Appendix B.3) formalizes how τ controls the bias–variance trade-off, and the analysis explains why the curvature factor h cancels after normalization, yielding scale-invariant normalized TLCs.

## Weaknesses

### Fatal
None.

### Major

1. **Scale is moderate (max 3.9B) despite the paper framing itself around "full-scale LLM families" and "LLM scale."** The paper correctly notes that Qiu et al. (2025) tested up to ~1B parameters and that this work goes further, but 3.9B parameters is still modest by 2026 standards (compare Llama-3 405B, Llama-2 70B). Whether collapse persists at 70B+ scales where training dynamics, gradient noise, and hardware constraints differ remains an open question. The paper's framing should match its experiment scale. — *Why it matters: The central claim that collapse is a practical tool for "billion-dollar runs" (Conclusion) requires validation at substantially larger scales than 3.9B.*

2. **Celerity's compute-efficiency frontier claim rests on cross-model comparisons with uncontrolled data mixtures and evaluation differences.** Figure 2 compares Celerity against models trained on different datasets (many use data annealing on evaluation-relevant subsets), with different token counts, and with different vocabularies/architectures. The paper acknowledges that Celerity does not use task-specific annealing, which partly addresses this concern, but the frontier claim would be much stronger with directly controlled comparisons (e.g., training a baseline on the exact same data). — *Why it matters: The Pareto frontier is a central claim about Celerity's competitiveness, but the uncontrolled confounds weaken it.*

3. **Early stopping validation is narrow and the baseline comparison is weak.** The procedure is tested on only two model sizes (1.7B, 3.3B) and only for λ sweeps. The "current best" baseline — selecting the run with lowest current loss — is known to fail when curves cross, which is precisely the scenario shown in Figure 7 (left). A more informative comparison would include: (a) power-law extrapolation of the raw (unnormalized) loss curve without collapse, (b) standard learning-curve extrapolation methods (e.g., Domhan et al. 2015, cited but not compared), or (c) multi-fidelity methods like ASHA. — *Why it matters: The practical utility of the proposed method depends on whether it improves over *reasonable* alternatives, not just over trivial baselines.*

4. **The 234 TPP breakdown (Figure 1 middle) is acknowledged but its implications are underexplored.** At 234 TPP, larger models diverge from collapse late in training, with the paper noting "loss improves disproportionately on training data, while held-out data remains aligned with projections." This means collapse can break under overtraining — which the paper itself is primarily interested in for its 234 TPP band. The paper does not characterize how to predict when collapse will fail (how many tokens at a given TPP before divergence?), nor does it provide a quantitative bound on when collapse can be trusted. — *Why it matters: Practitioners using collapse as a diagnostic need to know its reliability limits.*

### Minor

1. **Monitoring application is a single anecdote.** The detection of a numerical issue in the 1.8B run is a compelling story, but there is no systematic evaluation: how many runs were monitored, how many deviations were flagged, what was the false positive rate, and how sensitive is the method to the choice of reference curve and alignment method? The claim is an interesting observation rather than an established technique.

2. **All experiments use a single architecture family** (GPT2-like with ALiBi, SwiGLU, Squared ReLU) under μP/CompleteP with linear-decay LR. The paper provides no evidence that collapse persists under standard parameterization (e.g., Llama without μP), cosine schedules, or other architectural choices (RoPE, GQA, etc.). This limits the claimed generality.

3. **Figure 3 sweeps are all at a single model size (610M) and single TPP (80).** While the paper states "similar patterns hold across other scales and dataset sizes," this is not quantitatively demonstrated for Figure 3's τ-sweep experiments. The cross-scale collapse is shown only at select TPPs (20 in Figure 4 right), not with systematic τ variation at multiple scales.

4. **The parametric surrogate (Eq. 4) is empirically motivated but lacks a derivation from the noisy quadratic model.** The paper mentions the noisy quadratic model in Appendix B.3 but does not connect it to the form of Eq. 4. The power-law parameterization of b(τ) and q(TPP) in Eq. 5 is presented as an empirical observation without theoretical justification.

### Trivial
None.

## Nice-to-Haves

- Systematically test collapse under diverse architectures (RoPE, GQA, standard parameterization without μP) and LR schedules (cosine, constant).
- Quantify collapse fidelity with a metric (e.g., max RMS deviation of normalized curves) and report it across all TPP bands and model sizes.
- Compare early stopping against power-law extrapolation baselines and multi-fidelity HPO methods.
- Evaluate monitoring systematically by injecting controlled perturbations and measuring detection delay and false positive rate.
- Report error bars from multiple random seeds to establish whether collapse residuals are smaller than run-to-run variation.

## Removed Points

- **Bergsma et al. (2025a) being non-archival:** Removed per rules — questioning a cited reference's status is not permitted. The paper's own experiments independently validate the role of τ.
- **"Collapse at high TPP undermines core claim" (fatal framing):** The paper explicitly acknowledges the 234 TPP divergence and attributes it to overfitting. This is a documented boundary condition, not a contradiction of the thesis. Reduced from fatal framing to Major weakness #4 above (limitation not fully characterized).
- **Missing analysis of inter-run variance / error bars:** The strength finder's point about lack of error bars is noted but the harsh critic's "no analysis of inter-run variance" is generic. Moved to nice-to-have since single-run evaluation is standard in LLM pre-training experiments at this scale.
- **"No comparison of collapse tightness between Llama-2 and Celerity":** The paper's Figure 1 visually demonstrates this; a quantitative metric would be nice but not essential. Moved to nice-to-have.
- **"Normalization by final loss not fully justified":** The paper explains (p.3) that simply dividing by final loss (L̂=0) "resulted in optimal alignment across scales" based on empirical testing. This is an adequate justification. Removed.
- **"Parametric model lacks derivation":** Already included as Minor weakness #4 (empirically motivated, not derived).
- **"No discussion of computational cost":** Nice-to-have; not a core flaw.
- **Strengths dropped from Strength Finder:** "Derives analytical expression for training loss" (retained as Strength #5). "Provides practical trade-off analysis for TPP" (retained implicitly in Strength #4). "Shows fixing τ preserves ordering" (retained as part of the early stopping narrative). Generic/superlative strengths about "addressing important problems" dropped.

## Novel Insights

The harsh critic and strength finder together surface a clear picture: the paper's core contribution — that TLC collapse extends to practical LLM training and that τ is the key control — is genuinely novel and well-supported by the evidence. Where both reviewers converge is that the paper overreaches in its framing ("full scale," "billion-dollar runs," compute-efficiency frontier) relative to the actual evidence base (3.9B max, single architecture, cross-model comparisons). The most insightful tension is between the paper's practical ambitions and the narrowness of the validation: the monitoring example is a compelling proof of concept but not a validated method, and the early stopping procedure beats trivial baselines but not reasonable alternatives. These gaps do not invalidate the core phenomenon but suggest the paper would benefit from either scaling back its claims or substantially expanding the evaluation before publication.

## Suggestions

1. Scale back the framing to match the experimental evidence: replace "full-scale LLM families" with language that accurately reflects the 100M–3.9B parameter range tested.
2. For the Celerity efficiency frontier, include a controlled comparison: train a baseline with the same data mixture and comparable compute budget to isolate the effect of collapse-guided training.
3. Strengthen the early stopping evaluation by comparing against power-law extrapolation of the raw loss curve and at least one standard learning-curve extrapolation method (Domhan et al., ASHA).
4. Add a systematic evaluation of the monitoring method: a small number of injected perturbations with measured detection delay and false positive rate would transform the anecdote into a credible technique.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/1m4cKCr0vx.md` | 2.50 | R1 | Much weaker — simple scaling law for pruning, limited novelty |
| `/home/wg25r/review_agent/human_reviews_2026/anAHXnrTVW.md` | 3.00 | R1 | Weaker — proposes a metric but limited empirical validation |
| `/home/wg25r/review_agent/human_reviews_2026/dnuIoVjeGR.md` | 3.00 | R1 | Weaker — functional form for scaling laws, limited novelty |
| `/home/wg25r/review_agent/human_reviews_2026/WB2ejxmIFt.md` | 2.00 | R1 | Much weaker — theoretical framework with limited empirical support |
| `/home/wg25r/review_agent/human_reviews_2026/o94xgM0sWJ.md` | 5.00 | R1 | Weaker — novel decomposition but modest empirical improvements and small token samples |
| `/home/wg25r/review_agent/human_reviews_2026/qBAV2DEvAC.md` | 5.50 | R1 | Comparable — theory-experiment connection concerns, weaker empirical validation |
| `/home/wg25r/review_agent/human_reviews_2026/YnJ2s4WeNF.md` | 6.00 | R1 | Comparable — cleaner evaluation framework, larger models (17B), but less novel phenomenon |
| `/home/wg25r/review_agent/human_reviews_2026/vpKXTmMtBQ.md` | 5.50 | R1 | Comparable — empirical scaling law for model merging, extensive experiments but narrower scope |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` | 8.00 | R1 | Stronger — oral paper, completely different topic, no useful comparison |
| `/home/wg25r/review_agent/human_reviews_2026/UJ2UUjT2ko.md` | 8.00 | R1 | Stronger — poster paper with cleaner experiments and broader scope |

**Round 2 (Narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/3HrDPUi4jx.md` | 5.00 | R2 | Weaker — clustering-based prediction framework, less novel insight |
| `/home/wg25r/review_agent/human_reviews_2026/elB9k4nTL1.md` | 5.50 | R2 | Comparable — similar topic (μP, hyperparameter transfer), similar experiment scale, but less practical application |
| `/home/wg25r/review_agent/human_reviews_2026/vhhwY0AVgu.md` | 4.80 | R2 | Weaker — layerwise LR scheme, narrower contribution |
| `/home/wg25r/review_agent/human_reviews_2026/ZC5QBfdOw7.md` | 6.50 | R2 | Stronger — much more extensive empirical study (2000+ models), cleaner evaluation framework |
| `/home/wg25r/review_agent/human_reviews_2026/yKUbw7q1IA.md` | 6.80 | R2 | Stronger — extensive data curation experiments, strong practical contributions |
| `/home/wg25r/review_agent/human_reviews_2026/yxEop1S5le.md` | 6.50 | R2 | Stronger — cleaner empirical methodology, orthogonal topic |

**Round 1 bracket:** The paper clearly sits above the 2–3 range (weak anchors) and below the 7.5+ range (strong oral/poster papers). Initial bracket: [3.5, 7.5].

**Round 2 narrowing:** Compared against the 4.5–6.0 anchors, the paper is stronger than "Unveiling Downstream Performance" (5.0) and comparable to "Completed Hyperparameter Transfer" (5.5) in experimental scale but with more practical application. It is weaker than the 6.5+ anchors ("Text Quality Interventions" at 6.5, "Data-Efficient LLMs" at 6.8) which had much more extensive experimentation. The best anchor for direct comparison is "Revisiting Scaling Properties" (6.0, accepted poster) — that paper had a cleaner evaluation framework and larger models (17B) but studied a less novel phenomenon (downstream metric scaling). The current paper has a more novel core insight (τ-modulated collapse and its applications) but narrower validation.

**Final score: 6.0** — The paper makes a genuine empirical contribution with practical applications, but the limitations (3.9B max scale, single architecture, narrow early stopping evaluation, no controlled comparison for Celerity frontier) prevent it from reaching the next tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
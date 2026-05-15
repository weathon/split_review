Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes ADAPT, a deep continuous prompting method for vision-language models (CLIP) that learns heterogeneous context lengths across different layers via iterative pruning. Unlike standard deep prompting that uses a fixed context length at every layer, ADAPT initializes prompts with maximum length and removes unimportant tokens using saliency criteria (Snip, gradient norm, L2 norm) until a target total context budget is reached. Experiments on 11 downstream datasets report an average accuracy improvement from 79.83% to 81.70% with competitive computational efficiency.

## Strengths

- **Novel and well-motivated idea.** The observation that existing deep prompting constrains all layers to the same context length is a genuine limitation, and the proposal to relax it via pruning is clever. The paper connects this to findings about layer-wise distribution shift in pre-trained models (surgical fine-tuning), providing a principled motivation.

- **Pruning-based automatic determination of context lengths without extra parameters.** Using saliency criteria from network pruning (Snip) to score and remove prompt tokens is a clean transfer of an established technique. Table 3 compares three scoring functions and shows Snip performs best, directly validating the approach.

- **Ablation on τ_target demonstrates a clear pruning–performance trade-off.** Table 2 shows that reducing τ_target from 128 to 32 removes 77% of trainable parameters with only a 0.61% accuracy drop, while performance plateaus above 128. This is concrete evidence that the pruning identifies genuinely redundant tokens and that the method is not brittle to the budget choice.

- **Visual evidence of heterogeneous mask patterns.** Figure 3 shows that the learned binary masks exhibit substantially different sparsity patterns across layers and between the text/image branches, confirming that the method produces genuinely heterogeneous (not uniform) context lengths.

## Weaknesses

### Fatal

None.

### Major

- **The pruning mechanism is underspecified in ways that prevent reproduction.** (1) The importance score \(S_c = |\partial\mathcal{L}/\partial\mathbf{P}_{lt} \odot \mathbf{P}_{lt}|\) produces a *d-dimensional vector* (element-wise product with the gradient), but the paper never explains how this vector is reduced to a scalar for ranking tokens (sum, mean, max-pooling, or norm?). (2) The accumulation period \(n_k\) and pruning rate \(r_p\) are named (Section 3.3) but never given numerical values or schedules. (3) Algorithm 1 is referenced but appears only as an image stripped by the parser. Collectively, these omissions mean the core iterative pruning procedure cannot be faithfully reproduced from the text alone.

- **No statistical significance or variance is reported for any result.** Few-shot learning evaluations are known to have high variance across random seeds and data splits. The paper reports single numbers without confidence intervals, standard deviations, or even the number of runs. The headline 9.63% gain on Aircraft could fall within typical run-to-run noise. This undermines the reliability of all comparative claims.

### Minor

- **Ambiguous baseline reference for the headline improvement.** The abstract and Section 4.2 state "the average test accuracy increases from 79.83% to 81.70%" without specifying *which* method or aggregation 79.83% corresponds to (the best baseline? the average of all baselines? a specific method?). While Table 1 (an image in the original PDF) likely makes this clear, the prose should be explicit about the reference point.

- **Overstated characterization of baselines.** The paper claims "Baseline methods except for VPT rely on additional assistance such as knowledge distillation." This is not accurate: CoOp and MaPLe do not use knowledge distillation, and PLOT uses optimal transport, not KD. This framing inflates ADAPT's comparative advantage unnecessarily; the method stands on its own merits without this rhetorical crutch.

- **No comparison to random pruning or fixed heterogeneous context lengths.** The paper compares different saliency criteria (Table 3) but never shows whether saliency-based pruning outperforms random pruning at the same budget, or whether a manually designed schedule (e.g., linearly increasing context length with depth) could achieve similar gains. Without these baselines, the specific contribution of saliency-guided pruning is not fully isolated.

### Trivial

- **Inconsistency in prompt insertion location.** Section 3.3 states ADAPT inserts prompts "only for query and value," while the equations show prompts for key and value (Q = f_q(x), K = f_k([P,x]), V = f_v([P,x])), and Section 4.2 correctly says "key and value." A typo in Section 3.3 ("query and value") should read "key and value."

- **Mixed notation for the budget hyperparameter:** both \(\mathcal{T}_{\mathrm{target}}\) and \(\tau_{\mathrm{target}}\) are used interchangeably.

## Nice-to-Haves

- A comparison to a version of ADAPT with fixed uniform context length at the same total parameter budget would isolate the benefit of heterogeneity from the benefit of reduced parameters.
- Visualizing the per-layer context length distributions across more datasets (beyond EuroSAT) could show whether the method adapts meaningfully to different task types.
- Discussion of how the two branches' budgets are coupled/decoupled under the single constraint in Eq. 6 would clarify the optimization.

## Removed Points

These points were raised by reviewers but are removed because they are factually incorrect, misunderstand the paper, or violate the hard rules:

- **"The optimization mixes max (likelihood) and argmin (Eq 6) inconsistently."** Maximizing likelihood is equivalent to minimizing negative log-likelihood; this is standard practice, not an inconsistency.
- **"CoCoOp is a baseline that does not use knowledge distillation."** CoCoOp is not mentioned anywhere in the paper; the reviewer introduced an external baseline.
- **"Only two datasets mentioned (EuroSAT, Aircraft)."** Table 1 (an image) lists all 11 datasets; the text mentions the two with the largest gains as highlights, not as the full set.
- **Table/figure content complaints** arising from parser artifacts (missing tables, garbled text). These do not reflect the original submission.
- **Reproducibility concerns beyond the pruning underspecification** (e.g., undisclosed hyperparameters that are standard and minor). These are nitpicks about trivial implementation details.
- **Missing related work.** Cannot be verified without external sources.
- **"The connection to surgical fine-tuning is conceptual but not quantitatively supported."** The Discussion section explicitly frames this as a conceptual connection, not a quantitative experiment; requesting quantitative validation is scope creep for a discussion section.

## Novel Insights

An interesting observation that emerges from the review is that prompt pruning may actually be a *more natural* application of saliency-based pruning than network-weight pruning. As the paper notes in the related work section, concentrated pruning in one layer can cause disconnection issues in neural networks—but this problem is absent when pruning prompts, since pruning all tokens at a given layer simply reduces the effective prompt depth. This asymmetry suggests that pruning-based PEFT methods may enjoy structural advantages over pruning-based full fine-tuning, a point worth developing further.

## Suggestions

1. **Specify the pruning mechanics precisely:** explain how the vector importance score is reduced to a scalar (sum, mean, or norm), and report the values of \(n_k\) and \(r_p\) and the pruning schedule used in experiments.
2. **Report results with confidence intervals or standard deviations** over at least 3–5 random seeds/folds, consistent with standard practice in few-shot evaluation.
3. **Clarify the baseline average:** explicitly state that 79.83% is the average of [specific method(s)] across 11 datasets.
4. **Add a random-pruning baseline** to Table 3, so the reader can see whether saliency-based pruning adds value over random token removal at the same budget.
5. **Fix the typo** in Section 3.3 ("query and value" → "key and value") and unify notation for \(\tau_{\mathrm{target}}\).

## Score and Decision

The paper proposes a genuinely novel and well-motivated approach to prompt tuning. The core idea—learning heterogeneous context lengths via saliency-based pruning—is clever and supported by reasonable ablations. However, the experimental validation has two significant gaps: the pruning mechanism is underspecified to the point of preventing reproduction, and the lack of any variance reporting makes the claimed improvements unverifiable in a high-variance few-shot setting. These issues are addressable with revisions but are too significant to overlook in the current form.

**Originality:** 7/10 — novel application of pruning to prompt length heterogeneity.  
**Importance of question:** 7/10 — removing the fixed-length constraint is a genuine limitation of prior work.  
**Claims supported:** 4/10 — headline improvement is plausible but underspecified and unaccompanied by variance estimates.  
**Soundness of experiments:** 4/10 — missing statistical rigor and key baselines (random pruning).  
**Clarity:** 6/10 — core idea is clear but pruning details are missing.  
**Value to community:** 6/10 — useful idea that could inspire follow-up work if validated properly.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
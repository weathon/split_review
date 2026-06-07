## Summary

This paper proposes ReMem, a method combining Sharpness-Aware Minimization (with an unusually large perturbation radius ρ ≥ 0.05) and heuristic downweighting of top MLP blocks to improve knowledge distillation from strong pretrained vision transformers. The core contribution is identifying — through the lens of mutual information between input data and distillation targets — that top MLP blocks in strong pretrained models develop high "expertness" that bottlenecks information transfer, and showing that SAM fine-tuning plus MLP reweighting can mitigate this issue.

## Strengths

1. **MLP-vs-attention pruning diagnostic isolates the cause of MI loss (Figure 4, Section 4):** The paper prunes blocks from top to bottom separately for MLP and self-attention, revealing a distinctive turning point: pruning top MLP blocks *increases* mutual information significantly before model performance drops, whereas pruning attention blocks yields a near-linear trade-off. This cleanly attributes the information bottleneck to top MLP blocks specifically — a non-obvious finding that directly motivates the proposed reweighting.

2. **Empirical demonstration that SAM with a non-standard perturbation size improves the information-plane Pareto frontier (Figures 2–3, Section 3):** The paper shows that SAM fine-tuning shifts the (teacher error, mutual information) trade-off to a superior Pareto front compared to vanilla fine-tuning. The required perturbation size (ρ ≥ 0.05) is two orders of magnitude larger than the typical SAM setting (≈0.001) used for generalization, showing this is a distinct mechanism specifically beneficial for distillation.

3. **Scaling experiments show ReMem enables students to benefit from increasingly strong teachers, reversing the standard degradation trend (Tables 5–6, Section 6.3):** Without ReMem, student performance degrades monotonically as teacher size grows from ViT-Tiny to ViT-Large (Table 5) and as pretraining dataset scales up (Table 6). With ReMem, student performance improves consistently, and the gain is larger for stronger teachers. This directly supports the paper's central claim.

4. **Broad empirical validation across multiple dimensions (Tables 1–4, Section 6.2):** ReMem shows consistent student accuracy improvements across 16 datasets spanning natural, medical, and sensing domains; across ResNet-18, MobileNetV2, and EfficientNetV2 student architectures; across logit-matching, DIST, and patient distillation algorithms; and with both full fine-tuning and LoRA.

## Weaknesses

### Fatal
None.

### Major

1. **Mutual information estimation is never specified (Figures 1–4).** The entire diagnostic motivation — that strong pretrained models have low mutual information with their distillation targets, and that SAM fine-tuning improves it — rests on quantitative MI values plotted in Figures 1–4. Yet the paper never describes how I(X; F_T) is estimated. The only mention of an estimator is a passing reference to MINE (line 111) as an example of a "standard approach," but the paper does not state that MINE (or any specific estimator) was actually used. Standard MI estimators (MINE, InfoNCE, binning, k-NN) have severe and well-known biases in high dimensions. Without specifying the estimation procedure, the MI values in Figures 1–4 are scientifically uninterpretable, and the core diagnostic that motivates both the SAM fine-tuning and the MLP reweighting is unverifiable.

2. **No empirical comparison against prior teacher-oriented methods (Section 2).** The paper positions itself in the line of work on "student-oriented teacher training" and cites cross-fitting (Dao et al., 2021), joint teacher-student training (Park et al., 2021), Bayes-regularized training (Dong et al., 2022), and secondary-probability regularization (Yang et al., 2019). These are dismissed with the unsupported claim that they "may not be readily applied" due to computation overhead or architectural constraints. No empirical comparison is attempted, even in adapted form. The paper's main claim — that ReMem improves distillation from strong teachers — is therefore demonstrated only against the trivial baseline of doing nothing to the teacher. Without at least one adapted comparison, readers cannot assess whether ReMem offers a genuine advance or merely reflects that any teacher-side intervention helps.

3. **Evaluation protocol selects the best across many trials without a validation set or variance reporting (Section 6.1).** The paper states: "we always early stop the teacher fine-tuning at multiple checkpoints, distill student from each checkpoint, and select the best student performance across these checkpoints. We will also sweep over other teacher and student hyperparameters... We report the best student performance among these different settings." This is a max-over-trials selection protocol. No held-out validation set is mentioned anywhere in the paper. While both vanilla fine-tuning and ReMem receive the same treatment, the absolute reported numbers cannot be taken at face value, and no standard deviations or confidence intervals are reported. Moreover, ReMem introduces additional tunable hyperparameters (SAM ρ, MLP weight α), potentially giving it more degrees of freedom in the sweep. This makes it impossible to assess whether the reported gains are statistically significant or partly reflect selection bias.

### Minor

4. **Proposition 5.4 bounds mutual information for an MoE MLP, not a standard dense MLP (Section 5.2).** The bound applies to an MoE architecture with hard expert assignment via indicator vectors (Definition 5.2), not to a standard dense MLP with sparse ReLU activations. The paper relies on the "expertness" measure to argue that dense MLPs approximate MoE behavior, but the tightness of this approximation is not characterized. The theoretical grounding is therefore less direct than the presentation suggests.

5. **SAM-MI connection is purely empirical, with no mechanistic explanation (Section 3).** The paper shows that large-radius SAM improves MI and student performance (Figures 2–3) but provides no theoretical or mechanistic account of *why* this happens. This limits scientific understanding: it is unclear when the approach will generalize beyond the paper's specific experimental conditions.

6. **The value of α (MLP downweight coefficient) is not reported (Section 4).** The paper defines α (lines 141–145) but never states what value was used in experiments or whether it was tuned per dataset or fixed globally. This partially underspecifies the method.

### Trivial

7. **The numerical example (line 209) comparing 3000 bits of MI bound to 4×10^6 bits of raw pixel information compares quantities at different abstraction levels** — the MLP block processes patch embeddings, not raw pixels — and is illustrative but not rigorous.

8. **The pruning experiment (Figure 4) prunes then fine-tunes, so the measured MI change reflects both pruning and subsequent fine-tuning dynamics** — not pruning alone. The attribution of the effect to MLP block removal per se is somewhat confounded.

## Nice-to-Haves
- Comparison against at least one adapted prior teacher-oriented method (e.g., cross-fitting or Bayes-regularized training) would substantially strengthen the paper's claims.
- Reporting results with standard deviations over multiple random seeds would improve statistical reliability.
- A brief description of the MI estimation procedure used for Figures 1–4, even in a footnote, would address the most critical methodological gap.

## Removed Points
The following points from the inputs were removed (with brief justification):
- Criticisms about tables being "unreadable images" and the appendix being "stripped" — these are PDF parser artifacts, not author errors. The ablation study referenced as being in the appendix is a real component of the submission.
- Criticisms that questioned the validity of the dismissal of prior methods in a way that implied those methods don't exist — the cited methods (Dao et al., Park et al., Dong et al., Yang et al.) are real as per the paper's citations. The retained weakness is about missing empirical comparison, not existence.
- Pure formatting and style observations.
- The critique that "the introduction over-claims" because improvements are only shown relative to vanilla distillation — this is subsumed under weakness #2.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Specify the MI estimator.** Without this, Figures 1–4 are uninterpretable. A brief description of the estimator (e.g., dimensionality reduction + binning, or a neural MI estimator with architecture details) is essential.
2. **Add at least one adapted prior teacher-side method as a baseline.** Cross-fitting (Dao et al., 2021) is cited as having no architectural constraints; adapting it should be feasible.
3. **Adopt a proper validation protocol.** Use a held-out validation split for hyperparameter and checkpoint selection, and report student performance with variance across multiple runs.
4. **Report α and state whether it was tuned per dataset or fixed globally.** This is necessary for reproducibility.
5. **Characterize the tightness of the approximation from dense MLP to MoE MLP** in the expertness analysis, or qualify the theoretical claims accordingly.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>
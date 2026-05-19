Now let me do the calibration searches to score this paper properly.**Round 1 bracket: 4–7.** The paper is clearly better than the 2.5-scored papers (limited contribution, weak motivation), but doesn't reach the originality of the 8-scored analysis papers. Let me narrow within 4–7.Now I have enough information for my full review. Let me synthesize everything.

---

## Summary
APPLe (Adaptive Prompt Prototype Learning) proposes replacing a single text prompt per class with K GPT-3-generated descriptive prototypes, augmented with a learned per-class-per-prototype attention matrix (W ∈ ℝ^{C×K}) and two auxiliary losses: a maximum-prototype cross-entropy loss and a decorrelation loss. Experiments span base-to-new generalization, few-shot learning, and domain generalization across 11 datasets, with results consistently surpassing MaPLe. A training-free variant (APPLe*) uses only GPT-3 prompts at inference without any fine-tuning.

---

## Strengths

- **Consistent and significant base-to-new generalization gains across all 11 datasets.** Table 1 reports APPLe outperforms MaPLe by an average of +3.66% on new classes and +2.79% harmonic mean. The gains on challenging fine-grained datasets (FGVC-Aircraft +12.79%, DTD +7.29%) are particularly striking, directly validating that multiple prototypes capture intra-class visual variance better than a single context vector.

- **Training-free version (APPLe*) shows competitive performance without any labeled data or fine-tuning.** APPLe* achieves 74.83% HM on 11 datasets in Table 1, surpassing CoOp and Co-CoOp and nearly matching MaPLe despite using no support images. This independently validates the core claim that prompt diversity, not learned context adaptation, drives much of the generalization benefit.

- **Prototype-number ablation directly demonstrates the mechanism (Figure 4).** The monotonic increase in new-class accuracy from 1 to 50 prototypes, alongside the observation that fine-tuning a *single* prototype hurts new-class performance, grounds the multi-prototype motivation in direct empirical evidence rather than just intuition.

- **Component-level ablation in Table 3 confirms necessity of each design choice.** Piecewise addition of prototypes → training → attention → ℓ_max → ℓ_dec each shows incremental gains on ImageNet, making it clear that no single component is solely responsible for the improvement.

- **Image retrieval experiment (Table 4) provides a qualitative corroboration.** APPLe* outperforms zero-shot CLIP, CoOp, and MaPLe on mAP@50 (44.60 vs. 40.83), showing that prototype diversity improves discriminative feature alignment, not just classification accuracy.

---

## Weaknesses

### Fatal
None.

### Major

- **Training-free variant (APPLe*) is not compared to the most directly relevant prior art.** The paper explicitly acknowledges in Section 2 that Menon & Vondrick (2022) and Pratt et al. (2023) explore GPT-generated descriptor ensembles for zero-shot CLIP classification. Yet neither appears as a baseline in Table 1 or Table 2. APPLe* — which uses no labels, no fine-tuning, and just averages K GPT-3 prompts — is operationally very close to CuPL (Pratt et al., 2023). The paper's strongest headline claim, that APPLe* "surpasses all existing training-based methods on new classes," cannot be properly evaluated without knowing whether these directly comparable zero-shot baselines already achieve the same. This omission is in the experimental design, not addressable by noting that APPLe-trained adds attention and losses; those properties are specific to the trained variant, not to APPLe*.

- **The mechanism by which the trained attention matrix W generalizes to new classes is never described.** W ∈ ℝ^{C×K} is learned on base classes only (Section 4, Eq. 2). Under the base-to-new evaluation protocol in Table 1, the model is tested on held-out classes whose indices do not appear in W. The paper does not explain whether W is applied with uniform weights on new classes, whether a cross-class average is used, or some other mechanism. The +3.66% gain on new classes is one of the paper's headline results, yet the reader cannot determine whether this comes from the attention mechanism or purely from having multiple prototypes, since the ablation in Table 3 is on ImageNet (base classes only) and does not isolate this.

### Minor

- **The decorrelation loss formula (Eq. 4) is formally inconsistent with its stated motivation.** The stated goal is to "suppress the co-occurrence of multiple prototypes" (Section 4, Figure 2 caption). Eq. 4 computes an L2 norm over cosine similarities t_y^k (ground truth class prototypes), but the outer summation is indexed over c — making the sum over c redundant since y is fixed per image. In practice the loss applies an absolute-value penalty summed over K prototypes of the ground truth class, which discourages large activations on any prototype rather than specifically discouraging simultaneous high-confidence activation across multiple prototypes. The ablation confirms the loss helps (Table 3), but whether this is the intended design or a formula error is unclear. The motivation text should be reconciled with the actual formula.

- **The text in Section 5 (line "PLOT respectively gained 1.86%...") attributes the few-shot gains to PLOT rather than APPLe.** This is a substantive content error — "APPLe respectively gained..." is clearly intended — and readers unfamiliar with the method could misread this as a comparative statement about PLOT.

- **ImageNet-Adversarial regression is noted but not analyzed.** Table 2 shows APPLe underperforms on ImageNet-Adversarial, which is typically the hardest out-of-distribution setting. The paper disposes of this in a single parenthetical and offers no diagnosis. A brief analysis (e.g., whether semantically specific prototypes are more susceptible to adversarial perturbation than a generic prompt) would be informative and intellectually honest.

### Trivial
None (formatting artifacts are parser issues, not author errors).

---

## Nice-to-Haves

- The inference hyperparameter β (controlling the max-vs-average prototype trade-off in Eq. 7) is calibrated on ImageNet (Figure 5) and fixed at 0.8/0.2. Since ImageNet is also an evaluation dataset, disclosing that β is fixed globally across all 11 datasets (or clarifying if it is not) would improve transparency.
- Variance across training runs is never reported. Given that headline improvements per-dataset are often 1–3%, reporting confidence intervals or standard deviations across seeds would strengthen the claims.
- A brief description of the GPT-3 query template and example prompts would help reproducibility, given that the paper acknowledges prompt quality as a primary limitation.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"APPLe has more trainable parameters than single-prompt baselines and this invalidates the comparison"** (Harsh Critic): REMOVED. MaPLe optimizes both vision and text prompts; APPLe optimizes text prototypes plus a small attention matrix. APPLe's additional parameters (K text prototype embeddings vs. 1) are not obviously more expensive than MaPLe's cross-modal context vectors. Without actual parameter counts on both sides this is speculative, and the asymmetry does not clearly favor APPLe.

- **"GPT-3 prompt generation protocol is missing, preventing reproducibility"** (Harsh Critic): REMOVED per rules on reproducibility nitpicks about practical generation details. The paper acknowledges prompt quality as a limitation; the prompts themselves could be released separately.

- **"β may be tuned on test data"** (Harsh Critic): REMOVED as a weakness. The ablation in Figure 5 selects β = 0.8/0.2 and there is no indication this is re-tuned per-dataset. This is standard practice (fixed hyperparameter selected from ablation on a representative dataset).

- **Strength: "Training-free version challenges existing context optimization claims"** (Strength Finder): PARTIALLY RETAINED but qualified. The APPLe* result is genuine, but without CuPL/VisualDescriptions comparison the scope of the challenge is unclear.

- **Strength Finder: "Problem is important / addresses interesting question"** — REMOVED as generic; replaced by specific evidence-anchored strengths above.

---

## Novel Insights

The most noteworthy implicit finding is that fine-tuning a *single* prompt prototype hurts new-class accuracy relative to zero-shot CLIP (Figure 4), while fine-tuning multiple prototypes progressively recovers and exceeds zero-shot performance. This directly implicates prompt diversity — not learned context vectors per se — as the variable controlling generalization. This shifts responsibility for CLIP's generalization capacity away from the optimization procedure and toward the textual coverage of the prototype set, which is a non-obvious and practically useful observation about how VLM adaptation should be designed.

---

## Suggestions

1. **Add CuPL / VisualDescriptions as baselines for APPLe* in Tables 1 and 2.** If APPLe* materially outperforms those methods using the same K prompts, that directly proves the aggregation strategy is the value-add, not just prompt diversity. If it doesn't, the paper's contribution refocuses on the trained variant's attention + decorrelation design, which is still a legitimate paper.

2. **Explicitly describe how the attention matrix W is applied to new classes.** If uniform weighting is used at inference for new classes, state and ablate this directly ("APPLe without attention on new classes"). If the mechanism is different, describe it.

3. **Reconcile Eq. 4's formula with the stated motivation.** If the loss is effectively a logit-magnitude regularizer on the ground-truth class, describe it that way. If the intended formula sums over non-ground-truth classes, correct the formula. Either way, connect this to the ablation result.

---

## Score and Decision

**Calibration anchors (Round 1):**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| j1FLTvgyAh (Multi-Vision Multi-Prompt for Few-Shot CLIP) | 2.50 | R1-low | Clearly weaker: no training-free variant, narrower eval |
| ZaudLwn0Hm (Prototypical few-shot for VLM) | 2.50 | R1-low | Clearly weaker: limited scope, weaker baselines |
| pdzHpQbGrn (Active Test-Time Prompt Learning) | 2.50 | R1-low | Clearly weaker: niche setting, weak results |
| veiSkPqIXm (OpenPL benchmark) | 5.00 | R1-mid | APPLe is stronger in method and results |
| EKfcngSxwD (Task Codebook VLM) | 4.67 | R1-mid | APPLe broader scope and stronger results |
| PKICZXVY9M (OGEN OOD finetuning) | 6.00 | R1-mid | Comparable: both address CLIP generalization |
| lja4JMesmC (VITask task-specific instruction) | 6.25 | R1-mid | Somewhat comparable |
| WyEdX2R4er (Visual Data-Type Understanding) | 8.00 | R1-high | Clearly stronger: novel benchmarking contribution |
| 3i13Gev2hV (Compositional Entailment Hyperbolic VLMs) | 8.00 | R1-high | Clearly stronger: theoretical novelty |
| uAFHCZRmXk (Modality Gap CLIP analysis) | 8.00 | R1-high | Clearly stronger: deep mechanistic analysis |

**Round 1 bracket: 5.0 – 7.0**

**Calibration anchors (Round 2):**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| fRpAUgKJhT (CARPRT class-aware prompt reweighting) | 5.75 | R2 | APPLe is broader (3 tasks, 11 datasets, training-free variant) with larger gains; APPLe > CARPRT |
| wFs2E5wCw6 (TAP Tree of Attributes Prompt) | 6.40 | R2 | Very similar: LLM-generated attributes + prompt learning + 11 datasets; TAP has more structural novelty (hierarchical) but APPLe has training-free variant; roughly comparable |
| pgVMJdhgPI (FuzzyCLIP stacked prompts) | 5.25 | R2 | APPLe stronger in evaluation and breadth |
| buC4E91xZE (AnomalyCLIP) | 6.17 | R2 | Different task (anomaly detection); APPLe has comparable evaluation breadth |
| 1L9vdc7BB5 (ADAPT adaptive prompt tuning) | 5.50 | R2 | APPLe has broader evaluation and stronger reported results |
| SYnIf4LxAG (Cross-Modality Prompt Transfer) | 6.50 | R2 | Similar contribution level; cross-modality prompt transfer is arguably more novel |
| Zkq4fsyjfp (CLIP backbone ensembling) | 6.25 | R2 | APPLe slightly below: backbone ensembling is cleaner with no missing baseline issue |

**Round 2 narrowing:** APPLe sits between CARPRT (5.75, rejected) and TAP (6.40, accepted). APPLe is stronger than CARPRT in scope and results, but has the two genuine major weaknesses (missing CuPL baseline, unexplained attention on new classes) that put it below a clean accept like TAP. The missing-baseline issue is substantial enough to warrant major revisions. 

**Axis summary:**
- *Originality:* Moderate. Multi-prototype LLM-generated prompt ensembling is acknowledged to have prior art; the contribution is the attention matrix + decorrelation loss + training-free insight.
- *Importance of research question:* Solid. Base-to-new generalization is an actively studied and practically relevant problem.
- *Claims well-supported:* Partially. Trained results are well-supported; training-free results lack the key comparison.
- *Soundness of experiments:* Mostly sound; the unexplained attention behavior on new classes is a genuine gap.
- *Clarity:* Generally clear; Eq. 4 motivation/formula mismatch and the missing new-class attention explanation are the notable lapses.
- *Value to community:* Real, particularly the Figure 4 finding about single-prototype fine-tuning hurting new-class accuracy.

**Final score: 5.5** — just above the rejected CARPRT (5.75) on raw score but calibrated downward from TAP (6.40, accepted) because of the two substantive issues (missing baseline for APPLe*, unexplained attention mechanism on new classes) that make the paper's headline claims less fully supported than TAP's.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
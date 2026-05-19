Now let me do calibration searches. Let me start with bracketing.Round 1 bracket: **4 to 6.5**. OptBatch is stronger than the score-3 anchor (has a real method + experiments) but weaker than STAFF (score 6.5, which has more complete evaluation). Let me narrow.Now I have enough to write the final review. Let me synthesize.

**Calibration Summary:**
- Round 1 bracket: 4–6.5
- Round 2 anchors examined:
  - GTP / che9LCwPQM (avg 4.75, Reject): limited experiments, confusing presentation
  - ActivePrune / jBatISjqSn (avg 5.75, Reject): more comprehensive downstream evaluation
  - STAFF / FAfxvdv1Dy (avg 6.50, Accept): 3 LLMs × 3 tasks × multiple pruning rates with downstream metrics
  - DELIFT / Fty0wTcemV (avg 6.00, Accept): multi-stage with downstream metrics throughout

OptBatch sits **below** the 5.75 anchor (ActivePrune has more comprehensive downstream evaluation across 4 tasks/4 datasets) and clearly below STAFF (6.50). Its experimental coverage is similar to GTP (4.75) but with more datasets and models. The primary-metric-is-training-loss concern and the missing Hong et al. baseline keep it near the 4.5 range. Final score: **4.5**.

---

## Summary

OptBatch proposes an online batch data selection method for LLM instruction tuning that combines three components: (1) loss-based stratified sampling to maintain distribution coverage, (2) greedy diversity maximization over Hessian-approximated gradient features to reduce redundancy within each selected batch, and (3) an Adam-inspired accumulation of gradient history to stabilize selection across batches. Experiments span three datasets (NetLit, LLaMaQA, WikiMatrix), two models (LLaMa3, ChatGLM3), and multiple pruning rates, reporting primarily training loss curves plus limited downstream metrics (BLEU/ROUGE at 70% pruning) and GPT-4/human evaluation for the dialogue task.

---

## Strengths

- **Consistent loss reduction across pruning rates and datasets (Figures 3, 4, 5, 6):** OptBatch achieves the lowest training loss compared to Random, Online Hard, CCS, and InfoBatch across all four pruning rates (20%, 50%, 70%, 90%) on NetLit/ChatGLM3, and across three datasets at 70%. This breadth of comparison is a genuine empirical contribution.

- **Downstream evaluation on reference-based metrics (Tables 1–2):** At 70% pruning, OptBatch outperforms all baselines on BLEU-4, Rouge-1, Rouge-2, and Rouge-L on both LLaMaQA and WikiMatrix, demonstrating that the loss advantage translates to real capability differences on QA and translation tasks.

- **GPT-4 and human evaluation on dialogue quality (Figure 7):** For NetLit, OptBatch achieves 60.5% high-score responses in GPT-4 evaluation vs. 52.6% (CCS) and 43.5% (InfoBatch), and 61.8% in human evaluation vs. 47.5% (CCS) and 47.9% (InfoBatch). The margins are substantial and provide task-grounded evidence beyond training loss.

- **Feature ablation validating the Hessian gradient choice (Figure 9):** The comparison of embedding, gradient norm, and Hessian gradient on NetLit shows the Hessian gradient achieves the lowest loss among features, grounding the key design choice empirically.

---

## Weaknesses

### Fatal
None.

### Major

- **Training loss is the primary evaluation metric, and downstream metrics cover only one pruning rate.** The paper's headline claim—"OptBatch training at various pruning rates outperforms full dataset training" (Abstract)—is substantiated by training loss curves (Figures 3, 4, 5, 6) across four pruning rates (20%, 50%, 70%, 90%). But Tables 1–2 and Figure 7, the only downstream capability evidence, are confined to the 70% setting. Whether the loss advantage at 20%, 50%, or 90% translates into better model capabilities remains unverified. The Limitations section itself concedes: "loss is not the only metric. In the future, we will incorporate the model's performance on various downstream tasks' accuracy as an additional evaluation metric." As written, the strongest quantitative claims rest on a proxy metric the authors acknowledge is insufficient.

- **The most directly relevant baseline (Hong et al., 2024) is absent from all experiments.** The Introduction and Related Work explicitly frame OptBatch as correcting Hong et al. (2024)'s GradBatch, which "emphasizes directional diversity without considering the learnability of the data" (Section 1). The baselines are Random, Online Hard, CCS, and InfoBatch. Hong et al. (2024)'s method—the competitor OptBatch is designed to supersede—never appears in any comparison table or figure. Without this comparison, the paper's core framing claim cannot be evaluated.

- **Notational inconsistency in the Hessian gradient formula (Equations 6 vs. 7).** Section 2.2 defines the Adam update direction as **H**_t = v̂_t / (√ŝ_t + ε), where v̂_t is the bias-corrected *first* moment (momentum) and ŝ_t is the *second* moment (Equation 6). Section 3.2 then silently redefines the same symbol: "H_t = ‖g_t / √v̂_t‖_{2, axis=1}" (Equation 7), dividing by √v̂_t (the *first* moment). The text in Section 3.2 also refers to v̂_t as "the second moment estimate," compounding the confusion. The standard Adam diagonal-Hessian approximation divides by the *second* moment ŝ_t. Dividing by the first moment (gradient momentum) has no standard interpretation as a Hessian proxy. Because the paper's theoretical novelty claim is "Hessian gradient optimization to guide the selection strategy" (Abstract), this inconsistency calls the method's theoretical basis into question.

### Minor

- **InfoBatch threshold modification at high pruning rates is unspecified.** Section 4.1 states: "we increase the threshold appropriately for higher pruning rates." The amount of increase is not reported. This modification could advantage OptBatch at high pruning rates without a controlled comparison, since InfoBatch's behavior is sensitive to its threshold setting.

- **Feature ablation is limited to one dataset and one pruning rate.** Figure 9 compares embedding vs. gradient norm vs. Hessian gradient exclusively on NetLit at 70% pruning. The choice of Hessian gradient is presented as a general design principle; additional datasets or pruning rates would strengthen this claim.

- **Human evaluation sample size is unreported.** Figure 7(b) shows OptBatch at 61.8% high-score responses vs. CCS at 47.5%. The sample size and any variance estimate are not disclosed, making statistical significance impossible to assess.

### Trivial

- The exp(loss) allocation formula for stratum sizes and the procedure for setting stratum boundaries are described only in the Figure 1 caption, not in the body. A brief formal description would aid reproducibility.

---

## Nice-to-Haves

- Extend downstream evaluations (BLEU/ROUGE or GPT-4 scoring) across all four pruning rates (20%, 50%, 70%, 90%). This would directly confirm whether the training loss advantage is a real capability signal or an artifact.
- The Lipschitz gradient continuity result (Section 3.1, Equation 8) borrows directly from Sener & Savarese (2017) and Zheng et al. (2022). If theoretical grounding is claimed as a contribution, either a novel proof of the extension to gradients should be provided, or this section should be reframed as motivation rather than contribution.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **FLOPs formula omits selection overhead (Harsh Critic).** The critic claims the selection forward pass is excluded. However, inspecting Equation 9–10: `OptBatch FLOPs = B × (Li + Lo) × Ff + (1-α) × B × Lo × Fb`. The term `B × (Li + Lo) × Ff` IS the forward pass over the full batch of B samples, which is exactly the cost of computing losses for all candidates before selection. The only potentially unaccounted cost is the lm_head gradient computation for the Hessian, but Section 2.1 explicitly restricts gradients to "the lm head layer" to "minimize computational overhead." This is a modest additional cost, not the large "non-trivial fraction" the critic suggests. **Removed** as overstated.

- **Strength: Theoretical grounding via Lipschitz continuity.** While Equation 8 (Section 3.1) does appear in the paper, it is directly borrowed from prior work (Sener & Savarese; Zheng et al.) without a new proof of the gradient extension. Claiming this as a strength of OptBatch's originality is not warranted. **Removed** from strengths.

- **Strength: Quantified computational savings (Figure 8).** This is partially undermined by the fact that the comparison includes a forward-pass overhead for the Hessian gradient computation (albeit small). Kept as a supporting observation but not elevated as a major strength.

---

## Novel Insights

The paper's most actionable insight is the combination of *loss-stratified sampling* (for learnability coverage) and *gradient-space diversity maximization* (for redundancy reduction) within a single batch-level selection step, stabilized by Adam's second-moment history. This batch-level view — attending to the joint distribution of the selected subset rather than ranking individual samples — is a concrete and reproducible algorithmic contribution, even if its theoretical grounding needs clarification. The finding that a 50% pruning rate consistently achieves lower loss than 90% or 20% pruning on high-redundancy web text (Figure 6) is an interesting empirical observation about the saturation point of data redundancy in this domain.

---

## Suggestions

1. **Add downstream evaluation across all pruning rates.** At minimum, apply the BLEU/ROUGE metrics from Tables 1–2 at 20% and 90% pruning to anchor the loss-curve claims in capability evidence.
2. **Include Hong et al. (2024) GradBatch as a baseline.** The paper's core framing depends on showing it fixes GradBatch's limitation; without this comparison, the framing is unsupported.
3. **Resolve the v̂_t vs. ŝ_t inconsistency in Equation 7.** If the intention is the standard Adam Hessian approximation, replace v̂_t with ŝ_t in Eq. 7 and update the text; if the current formula is intentional, add a derivation or motivation explaining why dividing by the first moment is appropriate.
4. **Report human evaluation sample size and compute a simple significance test** (e.g., paired bootstrap or chi-squared on score distributions) for Figure 7(b).
5. **Specify the InfoBatch threshold adjustment** for high pruning rates in Section 4.1 to make the comparison reproducible and fair.

---

## Score and Decision

**Axis assessments:**
- *Originality:* Moderate. The combination of stratified sampling + diversity maximization + Adam-based stabilization is novel, though each component individually draws from existing work.
- *Importance of research question:* High. Efficient online batch selection for LLM instruction tuning is practically significant.
- *Claims well-supported:* Weak. Training loss is the primary evidence for the headline claims, and downstream evaluation covers only one pruning rate.
- *Soundness of experiments:* Moderate. Coverage across datasets and models is reasonable, but missing the key baseline and the formula inconsistency undermine confidence.
- *Clarity of writing:* Adequate. Method description is mostly clear but has gaps (stratum boundary specification, formula inconsistency).
- *Value to research community:* Moderate. The ideas are useful but the evaluation does not yet fully substantiate the claims.

**Anchor comparison:**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| EOPLy80bBm (Data Pruning Disentangled) | 3.00 | R1 | OptBatch is better: more experiments, clearer contribution |
| WDxa9hnz4p (Auto-Demo Prompting) | 2.33 | R1 | Not comparable topic |
| FAfxvdv1Dy (STAFF) | 6.50 | R1/R2 | STAFF clearly stronger: 3 LLMs × 3 tasks × multiple pruning rates with downstream metrics |
| bAFVlpFQvT (CoLM) | 6.75 | R1 | CoLM stronger: theoretical rigor, more complete evaluation |
| che9LCwPQM (GTP) | 4.75 | R2 | Comparable tier: different gaps (GTP has confusing presentation; OptBatch has metric gap) |
| jBatISjqSn (ActivePrune) | 5.75 | R2 | ActivePrune is stronger: 4 tasks, 4 datasets, clearer downstream evaluation |
| Fty0wTcemV (DELIFT) | 6.00 | R2 | DELIFT stronger: multi-stage evaluation with downstream metrics throughout |
| Mh8blXreJW (PASER) | 5.00 | R2 | Comparable or slightly above OptBatch: PASER has cleaner downstream setup |

**Round 1 bracket:** 4–6.5  
**Round 2 narrowing:** OptBatch sits close to the GTP anchor (4.75) and below the PASER anchor (5.00). The training-loss primary-metric issue and missing Hong et al. baseline are analogous to but slightly more severe than GTP's narrow experiment scope. The downstream metrics in Tables 1–2 and Figure 7 are a genuine positive differentiator from GTP. Final score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
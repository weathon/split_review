Now I have extensive calibration data. Let me produce the final consolidated review.

## Summary

The paper proposes **OptBatch**, an online batch selection method for instruction tuning that combines (1) loss-probability stratified sampling to ensure coverage across difficulty levels and (2) gradient diversity maximization within each batch. The method employs Adam-normalized gradient norms (called "Hessian gradients") as features for distance-based diversity selection. Experiments on three datasets (NetLit, LLaMaQA, WikiMatrix) with two 6-8B parameter models show OptBatch achieves lower loss at equivalent FLOPs compared to Random, Online Hard, CCS, and InfoBatch, with reported 20–40% computational savings.

---

## Strengths

1. **Consistent loss reduction across datasets and models.** Figures 3–6 show OptBatch achieving the lowest loss among all baselines on NetLit and WikiMatrix (ChatGLM3) and on LLaMaQA (both LLaMa3 and ChatGLM3) at a 70% pruning rate. Figure 4 further shows this advantage across pruning rates from 20% to 90% on NetLit. This supports the claim of robust generalization.

2. **Quantified computational savings.** Section 4.4 provides a FLOPs analysis showing that OptBatch reduces backward-pass computation by at least 30% at a 70% pruning rate. The paper reports 20–40% cost reduction, and Figure 6 shows OptBatch at α=50% achieving lower loss than full-data training, directly supporting the efficiency claim.

3. **Reference-based metric improvements on QA and translation.** Tables 1 and 2 report Bleu-4, Rouge-1, Rouge-2, and Rouge-L scores under 70% pruning. OptBatch outperforms all baselines on LLaMaQA (with both LLaMa3 and ChatGLM3) and on WikiMatrix (LLaMa3), demonstrating task-agnostic effectiveness beyond loss.

4. **Human-validated dialogue quality.** Figure 7(b) shows OptBatch achieves 61.8% high-score (4–5) responses in human evaluation, versus 47.5% for CCS and 47.9% for InfoBatch, suggesting that reduced loss translates to better character-aligned generation in a role-playing scenario.

5. **Ablation on feature representation.** Figure 9 compares embedding, gradient norm, and "Hessian gradient" as features, showing that the proposed feature choice yields the lowest loss. This provides some empirical justification for the design, though limited to comparing features within the full pipeline.

---

## Weaknesses

### Fatal
None. The core idea is reasonable, the experiments are non-trivial (8B-scale models), and the results are directionally consistent. The issues below are addressable through revision.

### Major

1. **The central evaluation metric (loss) is never specified as training-set or held-out loss.** The paper's headline claims — "loss at α=50% is lower than full data" and "20–40% computational savings" — rely entirely on the loss curves in Figures 3–6. The experimental setup (Section 4.1) does not describe a held-out test or validation set for loss evaluation. The paper mentions "validation" only for BLEU/ROUGE metrics (Section 4.3). If the loss curves are computed on the training set (or the selected subset), then lower loss could arise from selecting easier samples rather than actual generalization improvement. This ambiguity undermines the paper's primary empirical argument. The authors themselves acknowledge in the Limitations (Section 6) that "loss is not the only metric" and that future work should incorporate downstream task accuracy — but this does not resolve the ambiguity about what the current loss curves measure.

2. **Method description is insufficiently specified for reproducibility.** 
   - The number of strata \(K\) is never stated (the figure shows 3, but is this fixed?).
   - The sampling procedure is ambiguous: Step 1 says "select |S| data according to the probability of exp(loss) and calculate the number of data in each stratum" — it is unclear whether samples are drawn globally with probability proportional to exp(loss) and then grouped, or whether the batch is first partitioned into strata by loss quantiles and then samples are drawn per stratum.
   - The distance maximization across strata is described in vague language ("for strata 2 and 3, in order to select points for the new stratum, we need to consider the selected points from the previous strata"). No formal algorithm, pseudocode, or termination criterion is provided.
   - The theoretical bound in Equation (8) uses variables \(r, L_s, L, \gamma\) that are never defined or derived.

### Minor

3. **Misleading terminology: "Hessian gradient" is not a Hessian approximation.** The feature \(H_t = \|\mathbf{g}_t / \sqrt{\hat{\mathbf{v}}_t}\|\) is an Adam-normalized gradient norm, not a curvature or Hessian measure. The paper further confuses the notation by using \(\hat{\mathbf{v}}_t\) (the bias-corrected first-moment/momentum estimate) in the denominator while claiming it is "adjusted by the second moment" (Section 3.2, line 95–99). In the standard Adam formulation, the denominator uses the second-moment estimate \(\hat{\mathbf{s}}_t\). This does not invalidate the method but is mathematically misleading and should be corrected to something like "adaptive gradient norm."

4. **No statistical uncertainty reported.** All loss curves, BLEU/ROUGE tables, and GPT-4 score distributions are shown as single runs or aggregates without error bars, confidence intervals, or significance tests. The improvements in Table 1 are small (e.g., +1.58 BLEU-4 on LLaMaQA, +0.51 BLEU-4 on WikiMatrix). Standard practice in this area is to report results over multiple seeds (typically 3). While the computational cost of running 8B models is acknowledged, even a smaller-scale replication would strengthen the claims.

5. **Baseline comparison is limited for the claim of "surpassing previous state-of-the-art."** The paper compares against four baselines (Random, Online Hard, CCS, InfoBatch). While these are appropriate online methods, the related work section discusses LESS (Xia et al., 2024b) as a gradient-based offline method but does not include it in experiments. Even one comparison to a modern gradient-based method (e.g., adapting LESS to online selection or comparing to a warmup-based approach) would substantiate the SOTA claim. As presented, the claim is only supported against this specific set of baselines.

### Trivial
- Equation (7) in Section 2.2 defines \(\mathbf{H}_t\) as the Adam parameter update, but Section 3.2 redefines \(H_t\) as a scalar feature per sample. This overloaded notation is confusing.
- Figure 8 shows a bar chart of FLOPs, but the numerical values are not reported in the text.
- The GPT-4 evaluation prompt template is only referenced (Shao et al., 2023) but not provided; the human evaluation process says "annotators rectifying the scoring results" without specifying the number of annotators or inter-annotator agreement.

---

## Nice-to-Haves

- **Ablation of selection components:** The paper does not isolate the effect of (a) stratified sampling by loss vs. uniform random per stratum, (b) distance maximization vs. random selection within strata. Figure 9 compares features but holds the full pipeline fixed.
- **Qualitative analysis of selected data:** Showing examples from different strata would strengthen the "learnability" motivation.
- **Wall-clock time overhead:** The FLOPs analysis assumes full forward pass cost is always incurred, but the method also adds computation for loss evaluation, Hessian gradient computation, and distance calculations. Reporting actual wall-clock overhead would be valuable for practitioners.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper conflates learnability with loss value"** — The concept of "learnable samples" is used informally but not formally defined as a metric; the paper primarily uses it as a motivation, not a rigorous definition. This is common in motivation sections and does not invalidate the method.
- **"No ablation on K (number of strata)"** — This is a valid concern but is subsumed by the broader method-description weakness (Major #2). Duplicate.
- **"No comparison to vision or multi-modal experiments"** — The paper explicitly scopes itself to text-based instruction tuning (three datasets: dialogue, QA, translation). Scope-creep criticism removed per soft rules.
- **"The bound in Equation 8 is not used in the method design"** — While true that the bound's variables are undefined, the paper presents it as motivation for why gradient-based diversity selection has theoretical grounding (following Sener & Savarese 2017; Zheng et al. 2022), not as a design equation. The criticism overstates the role of this equation.
- **"Missing DSIR and RHO baselines"** — These are primarily pre-training data selection/importance sampling methods, not instruction-tuning or online batch selection methods. The critic's demand for these is scope-creep.
- **Strength: "Quantified computational savings with maintained performance"** — Kept as Strength #2.
- **Strength: "Ablation validating Hessian gradient feature choice"** — Kept as Strength #5 with caveat that it compares features within the full pipeline, not an ablation of selection components.
- **Generic strengths from Strength Finder** (e.g., "addresses an important problem") — Removed as generic/superficial.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the H_t notation confusion — using \(\hat{\mathbf{v}}_t\) (first moment) in the denominator while calling it "second moment" — is a specific and correct insight that is not discussed in the paper itself and points to a clarity gap in the manuscript. The synthesis of the two reviews also clarifies that the loss-curve ambiguity and the method-description incompleteness are the two most impactful weaknesses, with the "Hessian gradient" terminology concern being genuinely misleading rather than a minor naming preference.

---

## Suggestions

1. **Clarify the loss metric immediately.** State explicitly whether loss curves in Figures 3–6 are computed on a held-out test set, a validation split, or the training set. If on the training set, reframe the claims accordingly as "lower training loss at given compute budget" and include held-out evaluation (e.g., downstream task accuracy) as the primary evidence.
2. **Provide pseudocode or a step-by-step algorithm** specifying: (a) the number of strata \(K\) and how it is determined, (b) the exact stratified sampling procedure, (c) the distance-maximization algorithm (is it greedy k-center?), and (d) the distance metric used.
3. **Rename "Hessian gradient"** to "adaptive gradient norm" or "normalized gradient" and correct the denominator to use \(\hat{\mathbf{s}}_t\) (second moment) or provide a clear justification for using \(\hat{\mathbf{v}}_t\) (first moment).
4. **Add at least one modern gradient-based baseline** to support the "SOTA" claim — e.g., adapting LESS (Xia et al., 2024b) to online selection or comparing to a warmup-initialized selection.
5. **Report means and standard deviations** over at least 3 random seeds for the main BLEU/ROUGE results (Table 1 and Table 2) to establish that the improvements are statistically reliable.
6. **Define the variables** \(r, L_s, L, \gamma\) in Equation (8) or remove the equation if it is not used in the method's design or analysis.

---

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Topic: "data selection instruction tuning LLM batch sampling gradient-based"

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Disentangling Roles (EOPLy80bBm.md) | 3.00 | R1 | Study paper, no new method. OptBatch proposes a new method and has broader experiments. **OptBatch is stronger.** |
| GradSimCore (cHy00K3Och.md) | 2.50 | R1 | Weak theory, limited evaluation. **OptBatch is substantially stronger.** |
| GTP (che9LCwPQM.md) | 4.75 | R1 | Clearer method description but narrower eval. **OptBatch is slightly weaker (worse clarity, comparable eval breadth).** |
| DELIFT (Fty0wTcemV.md) | 6.00 | R1 | Comprehensive evaluation, clear method. **OptBatch is weaker.** |
| Priority on High-Quality (7qMrDf9zFU.md) | 4.75 | R1 | Clearer writing, solid experiments. **OptBatch is weaker.** |
| Self-Alignment/Instruction Backtranslation (1oijHJBRsT.md) | 8.00 | R1 | Highly impactful method with strong results. **OptBatch is far weaker.** |
| Combatting Dimensional Collapse (f4gF6AIHRy.md) | 8.00 | R1 | Thorough experiments, theoretical grounding. **OptBatch is far weaker.** |

**Initial bracket:** 3.0 – 5.0. The paper is clearly above the 2.5–3.0 papers (GradSimCore, Disentangling) but below the 4.75–6.0 papers (GTP, Priority on High-Quality, DELIFT) due to method description gaps and evaluation ambiguity.

**Round 2 (Narrowing within bracket):** 

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| BIDS (dCTGFl3lN2.md) | 4.25 | R2 | Incremental contribution (LESS + normalization). Polarizing scores (8,3,3,3). **OptBatch has a more novel method but worse presentation.** |
| SimpleStrat (yLYMFRZkdU.md) | 3.67 | R2 | Interesting idea, very limited evaluation (105 questions). **OptBatch has larger-scale evaluation but method ambiguity.** |
| Lowering Data Diversity (xlxDTVAbNM.md) | 3.50 | R2 | Focuses on synthetic tasks. **OptBatch has more practical experiments.** |
| Rethinking Data Selection (qUJsX3XMBH.md) | 4.40 | R2 | Negative finding paper, thorough experiments. **OptBatch is comparable overall with different strengths/weaknesses.** |

**Final positioning:** The paper sits between SimpleStrat (3.67) and BIDS/Rethinking Data Selection (4.25–4.40). It has a genuine new idea and non-trivial experiments (8B models, 3 datasets), but the method description incompleteness, ambiguous loss metric, and misleading terminology are more serious than the issues in the 4.0+ papers. I place it closest to the 3.67–3.5 anchors with an upward nudge for the larger-scale evaluation.

**Final Score: 3.5**

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
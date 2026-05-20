Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket:** I placed the paper in the middle band (3.5–7.5) based on comparison with weak anchors (2.5–3.4), middle anchors (3.75–6.0), and strong anchors (8.0).

**Round 2 narrowing:** Comparing more carefully:
- DELIFT (score 6.0, accepted poster) — stronger: more novel metric, more comprehensive. OptBatch is below this.
- Gauging Learnability (avg 3.25, withdrawn) — weaker methodologically. OptBatch is clearly above this.
- Rethinking Data Selection (avg 4.4, rejected) — comparable quality, OptBatch has a novel method which is a plus but has evidential gaps.
- PruneFuse (avg 4.67, rejected) — comparable quality and similar issues (computational cost, baselines).
- InstructionGPT-4 (avg 3.75, rejected) — weaker. OptBatch is stronger.

OptBatch sits near 4.5–5.0. The algorithm is sensible, experiments span 3 datasets and 2 models, and downstream evaluations exist, but training loss as primary evidence, missing baselines, and the "Hessian" misnomer are significant weaknesses.

I'll settle on **5.0** — a borderline paper with a reasonable method but significant evidential concerns.

---

## Summary

This paper proposes OptBatch, an online batch-selection method for instruction tuning that combines loss-based stratified sampling with greedy farthest-point selection on Hessian-gradient features. The idea — ensuring diversity in gradient space while also stratifying by loss to balance difficulty — is sensible and the algorithm is clearly described. Experiments on three datasets (dialogue, QA, translation) with two models (LLaMA-3-8B, ChatGLM3-6B) at multiple pruning rates show consistent loss reduction, and downstream evaluations (GPT-4 scoring, human evaluation, Bleu/Rouge) provide some evidence of generalization benefits.

## Strengths

1. **Sensible algorithm design combining stratified sampling and farthest-point selection** — OptBatch (Algorithm 1) partitions a batch by loss into strata and selects points within each stratum by greedily maximizing pairwise L2 distance in gradient space, while also considering already-selected points from previous strata. This directly addresses the limitation of prior methods (e.g., Hong et al. 2024) that focus only on directional diversity without considering sample learnability (§3.3, Algorithm 1, Figure 2).

2. **Downstream evaluations confirm response quality improvements** — On the NetLit dialogue dataset, OptBatch achieves the highest percentage of scores 4 and 5 in both GPT-4 evaluation (60.5% vs. 52.6% for CCS) and human evaluation (61.8% vs. 47.5% for CCS) (Figure 7). This provides concrete evidence that the selection method translates to better generation quality.

3. **Ablation validates the proposed feature design** — Figure 9 compares embedding, gradient norm, and the proposed Hessian gradient as features, showing the Hessian gradient achieves the lowest loss, supporting the design choice of using adaptive normalized gradients over static features (§4.2.1, Figure 9).

4. **Quantified computational savings** — Section 4.4 provides a FLOPs analysis showing that the backward pass scales by (1−α), and Figure 8 demonstrates that OptBatch achieves lower loss than full-batch training at equivalent FLOPs, supporting the claim of 20–40% computational reduction.

5. **Generalization across two model families and three tasks** — OptBatch shows consistent trends on both LLaMA3 and ChatGLM3 across dialogue, QA, and translation tasks, using both reference-based metrics (Bleu, Rouge) and human/GPT-4 evaluation (Tables 1, 2; Figures 3, 5).

## Weaknesses

### Fatal
None.

### Major

1. **Training loss as primary experimental evidence** — The main results (Figures 3–6) show "Loss" plotted against "Training example" (examples seen during training), which is almost certainly **training loss on the selected subset**. Training loss on a self-selected subset is not a meaningful measure of generalization — it primarily shows that the method selects samples that are easier to fit. The paper's Limitations section even acknowledges: "Our main experiments primarily evaluate the model's performance by observing the decrease in loss. In reality, loss is not the only metric." While downstream evaluations (GPT-4, human, Bleu/Rouge) do provide generalization evidence, they are limited to one pruning rate (70%) and one dataset for GPT-4/human eval. The loss curves, which form the backbone of §4.2 "Main Results," are not interpretable as a generalization claim. **The authors should replace training loss with held-out validation loss or downstream accuracy as the primary evidence.**

2. **Missing directly relevant baselines** — The paper cites LESS (Xia et al., 2024b) and Hong et al. (2024) as related work but does not compare against either. LESS is a well-known gradient-matching method for instruction tuning, and Hong et al. (2024) proposes online batch selection via orthogonal diversity — extremely close in spirit to OptBatch. Without these comparisons, readers cannot assess whether OptBatch advances the state of the art. The current baseline set (Random, Online Hard, CCS, InfoBatch) is too narrow.

3. **"Hessian gradient" is terminologically misleading** — Equation 8 defines \( H_t = \| \mathbf{g}_t / \sqrt{\tilde{\mathbf{v}}_t} \| \), where \(\tilde{\mathbf{v}}_t\) is Adam's second-moment estimate. This is a gradient norm normalized by the running variance estimate — a first-order adaptive rescaling, not a second-order Hessian. There is no Hessian matrix, no curvature information, and no justification for why this should be called a "Hessian gradient." The Lipschitz continuity argument (§3.1, Eq. 7) is presented as an inequality without derivation or connection to the actual selection algorithm, and the proof is deferred to a stripped appendix. This framing overclaims and undermines the credibility of the method's theoretical motivation.

4. **No statistical significance reported** — Tables 1 and 2 report Bleu-4 and Rouge scores without error bars or significance tests. The improvements over the best baseline are often small (e.g., Bleu-4 27.11 vs. 27.04 for LLaMA3; Rouge-L 39.52 vs. 38.77), making it impossible to know whether these differences are reliable.

### Minor

1. **Selection overhead not accounted for in FLOPs analysis** — The FLOPs formulas (Eq. 9–10) assume the only cost of selection is the forward pass (which is necessary anyway) and a reduced backward pass. However, computing the Hessian gradient feature requires a backward pass through the `lm_head` layer for the entire batch, which adds overhead not captured by the analysis. Wall-clock time measurements or a more detailed accounting would clarify whether the claimed 20–40% savings hold in practice.

2. **GPT-4 and human evaluation limited in scope** — These evaluations are conducted on only one dataset (NetLit) at one pruning rate. The test set size and annotation procedure for the human evaluation are not described. While the results are positive, the limited scope weakens the generality of the conclusion.

3. **Hyperparameter sensitivity not explored** — The number of strata \(K\) and the use of \(\exp(\text{loss})\) as the sampling probability are not ablated or justified. It is unclear how sensitive the method is to these choices.

### Trivial
None.

## Nice-to-Haves

- Extending the GPT-4 and human evaluation to additional datasets and pruning rates would substantially strengthen the paper.
- The theoretical section could be improved by either removing the "Hessian" language and simply calling it a normalized gradient, or providing a genuine second-order justification.
- Ablation on the number of strata \(K\) would help understand the method's sensitivity to this hyperparameter.

## Removed Points

1. **"NetLit dataset size / human evaluation procedure not described"** — The human evaluation procedure details are likely in the appendix (stripped by parser). The paper mentions "annotators" and refers to Appendix B for details. Since the appendix cannot be evaluated, this criticism is based on missing information that exists in the original submission.

2. **Criticism about CCS using loss rather than computer vision scores** — The paper explicitly states "we substitute it with loss" (§4.1), so this is a conscious adaptation, not an error.

3. **"Missing related works"** — Removed per instructions: as the meta-reviewer does not have external sources to verify existence of missing related works.

4. **Parser-related formatting issues in Figure 1** — The critic notes "garbled equations" in the figure caption that don't match the main text. These are parser artifacts and not author errors.

5. **"Proof deferred to appendix"** — The appendix is stripped by the parser; proofs exist in the original submission.

6. **Strengths about "addressing an important problem"** — Generic strengths not specific to this paper's contributions. Moved here.

## Novel Insights

None beyond the paper's own contributions. The two-reviewer synthesis does not yield observations not already present in the paper or the individual reviews.

## Suggestions

1. **Replace training loss curves with held-out validation loss or downstream task accuracy** as the primary evidence in §4.2. The current presentation gives the misleading impression that the method is evaluated on the same data it selects from.

2. **Benchmark against LESS and Hong et al. (2024)** — these are the most directly relevant baselines and are essential for positioning the contribution.

3. **Rename "Hessian gradient" to "adaptive normalized gradient"** or similar terminology, and provide a clearer justification for why Adam's second moment is useful for data selection.

4. **Add error bars or significance tests** to all table results to establish reliability of the reported improvements.

5. **Measure and report wall-clock time** per training step with and without selection to validate that the FLOPs savings translate to real speedups.

6. **Ablate the number of strata \(K\)** and the \(\exp(\text{loss})\) sampling probability to provide guidance on hyperparameter settings.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- `/home/wg25r/review_agent/human_reviews/KpC3dPumJj.md` (avg 3.25, weak) — Gauging Learnability: weaker methodology, less thorough experiments. OptBatch is stronger.
- `/home/wg25r/review_agent/human_reviews/EOPLy80bBm.md` (avg 3.00, weak) — Disentangling Roles of Representation and Selection: narrower scope, analysis paper. OptBatch is stronger.
- `/home/wg25r/review_agent/human_reviews/7DY2DFDT0T.md` (avg 2.50, weak) — EfficientSkip: different topic (sparse transformers). Not directly comparable.
- `/home/wg25r/review_agent/human_reviews/Y8DClN5ODu.md` (avg 3.40, weak) — Demonstration Distillation: different method (ICL). Not directly comparable.
- `/home/wg25r/review_agent/human_reviews/DNvzCsQG1D.md` (avg 3.75, middle) — InstructionGPT-4: narrower experiments, weaker baselines. OptBatch is stronger.
- `/home/wg25r/review_agent/human_reviews/qUJsX3XMBH.md` (avg 4.40, middle) — Rethinking Data Selection: analysis paper, rejected. OptBatch has a novel method with positive results, but comparable in overall quality.
- `/home/wg25r/review_agent/human_reviews/yLYMFRZkdU.md` (avg 3.67, middle) — SimpleStrat: different task (generation diversity). Not directly comparable.
- `/home/wg25r/review_agent/human_reviews/Fty0wTcemV.md` (avg 6.00, middle) — DELIFT: stronger paper with more novel metric, broader experiments, accepted as poster. OptBatch is weaker.
- `/home/wg25r/review_agent/human_reviews/dhAL5fy8wS.md` (avg 8.00, strong) — Data Selection via Optimal Control: much stronger theoretical foundation, oral acceptance. OptBatch is substantially weaker.
- `/home/wg25r/review_agent/human_reviews/f4gF6AIHRy.md` (avg 8.00, strong) — DiSF: stronger theory and experiments, oral acceptance. OptBatch is weaker.
- `/home/wg25r/review_agent/human_reviews/uHLgDEgiS5.md` (avg 8.00, strong) — Temporal Dependence of Data Influence: stronger theoretical contribution, oral acceptance. OptBatch is weaker.

**Round 2 (Narrowing within bracket 4–6):**
- `/home/wg25r/review_agent/human_reviews/AFMi0kUtDr.md` (avg 4.67, middle) — PruneFuse: similar issues (computational cost concerns, missing baselines), comparable quality.
- `/home/wg25r/review_agent/human_reviews/VdURgvImVn.md` (avg 4.20, middle) — Gradient-based Optimization of Dataset Mixtures: similar weaknesses (missing baselines, limited evidence), comparable quality.
- `/home/wg25r/review_agent/human_reviews/pszewhybU9.md` (avg 6.25) — InsTag: stronger analysis, accepted poster. OptBatch is weaker.
- `/home/wg25r/review_agent/human_reviews/Spp2i1hKwV.md` (avg 6.00) — IDEAL: stronger method and evaluation, accepted poster. OptBatch is weaker.

**Final position:** OptBatch sits below DELIFT (6.0) and InsTag (6.25) but above or comparable to Rethinking Data Selection (4.4), PruneFuse (4.67), and Gradient-based Optimization (4.2). The algorithm is sensible and the downstream evaluations provide some generalization evidence, but the reliance on training loss curves as primary evidence, the missing key baselines, the misleading "Hessian" terminology, and the lack of statistical significance testing are substantial weaknesses. The paper is below the acceptance threshold for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
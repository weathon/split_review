Now I have all the information I need. Let me compile the final review.

## Round-1 Bracket

I first anchored against three bands on "test-time adaptation continual learning classifier bias":

- **Weak anchors** (score < 3.5): `/home/wg25r/review_agent/human_reviews/A1JdcLawSu.md` (3.0), `lEsNGN1SjG.md` (2.0), `ZIbUx5dzfZ.md` (3.0), `HCCkCjClO0.md` (3.0)
- **Middle anchors** (3.5–7.5): `/home/wg25r/review_agent/human_reviews/fRNDDFkPiv.md` (6.75), `eXrUdcxfCw.md` (4.80), `9w3iw8wDuE.md` (7.00), `sEMJ1PLSZR.md` (6.25)
- **Strong anchors** (7.5+): `TPZRq4FALB.md` (8.0), `SctfBCLmWo.md` (8.0), `TpD2aG1h0D.md` (8.67), `uAFHCZRmXk.md` (8.0)

Initial bracket: **4.5 – 6.5**

## Round-2 Narrowing

Inside the bracket I retrieved:
- `fRNDDFkPiv.md` (6.75, Reject) — *"Controlling Forgetting with Test-Time Data in Continual Learning"* — most topically similar; split scores (5,6,8,8); rejected due to ambiguous test-time setup and missing baselines. ARC is similarly affected by test-time protocol ambiguity but has more baselines and cleaner motivation.
- `eXrUdcxfCw.md` (4.80, Reject) — *"Continual TTA by Leveraging Source Prototypes"* — limited novelty, marginal gains. ARC is clearly stronger than this.
- `DJZDgMOLXQ.md` (6.50, Accept) — *"Prediction Error-based Classification for CIL"* — strong novelty + theory, accepted. ARC is less novel theoretically.
- `1nHQRsb3Ze.md` (5.00, Reject) — *"Auxiliary Classifiers Improve Stability in CL"* — plug-in for multiple CL methods, consistent gains but seen as incremental. ARC has a similar "plug-in" profile but with stronger motivation (classifier-bias evidence).

Comparing all anchors: ARC sits between `1nHQRsb3Ze.md` (5.0) and `fRNDDFkPiv.md` (6.75) — it has a clearer motivation than the former and more baselines, but shares the latter's critical evaluation weakness (no variance estimates, underspecified protocol). The evaluation gaps prevent it from reaching the 6+ range.

---

## Summary

This paper proposes ARC (Adaptive Retention & Correction), a test-time method that mitigates classifier bias in continual learning without modifying the training procedure. ARC first uses an Out-of-Task Detection (OTD) scheme to identify past-task test samples, then applies either Adaptive Retention (online gradient update on the classifier head for correctly-classified past-task samples) or Adaptive Correction (task-based softmax rescoring for misclassified ones). Experiments on Split CIFAR-100, Split ImageNet-R, and a 5-dataset composite show that adding ARC to eight different CL methods yields consistent improvements averaging 2.7% and 2.6% in average accuracy.

## Strengths

1. **Clean decoupling of forgetting sources (Figure 3).** The paper demonstrates convincingly across six architectures (ViT-S/B/L, ResNet-18/50/101) that after full finetuning on new tasks, linear probing on frozen representations from earlier tasks maintains accuracy close to joint training, while full-classifier evaluation drops sharply. This evidence that classifier bias — not representation forgetting — dominates catastrophic forgetting in pretrained models is the paper's strongest conceptual contribution and directly motivates the ARC design.

2. **OTD validation across 8 diverse CL methods (Table 5).** The two detection assumptions (high-confidence past-task predictions are correct; low-confidence current-task predictions with a small confidence ratio are misclassified past-task data) are validated with 88.4% and 71.9% average accuracy respectively across all tested methods on Split ImageNet-R. This shows the detection framework works reliably across very different CL algorithms (memory-based, prompt-based, regularization-based).

3. **Consistent improvements across 8 methods and 3 benchmarks (Tables 1–3).** Every baseline improves with ARC, with gains of +0.7% to +6.6% on average accuracy and forgetting reductions of up to 19 percentage points. The comparison with TENT (Table 3) shows ARC outperforms this general TTA baseline across all four tested methods, confirming that the dual retention+correction strategy is better suited to the CL setting than generic test-time adaptation.

4. **Ablation studies isolate component contributions (Table 4, Figure 4).** Both Adaptive Retention and Adaptive Correction are shown to contribute positively, with retention providing 0.4–4.6% gains and correction providing 0.1–3.9% gains depending on the method and dataset. The ablation of the temperature scaling in TSS and the design of the ratio \(w\) in Assumption 2 both demonstrate the value of the specific design choices.

5. **Hyperparameter robustness (Figure 5).** Thresholds \(\beta\) (0.6–0.9) and \(\gamma\) (0.6–1.0) produce less than 2% accuracy fluctuation across four methods, suggesting ARC does not require careful tuning.

## Weaknesses

### Major

- **Missing statistical significance and variance estimates.** Every numerical result in Tables 1–4 is a single point estimate with no error bars, standard deviations, or mention of the number of independent runs. ARC involves online gradient updates conditioned on test-sample order, so performance could fluctuate with different sample permutations or random seeds. The reported improvements range from 0.7% to 6.6% — without variance estimates, the reader cannot determine whether individual gains are statistically reliable or could arise from noise. This is the most consequential weakness in the paper: the central claim of "consistent improvement" rests on the pattern of positive deltas across 8 methods, but no individual comparison is statistically grounded.

- **Underspecified evaluation protocol for test-sample ordering.** ARC operates under the assumption that test samples "arrive in an online manner" and the classifier is updated on each qualifying sample. However, the paper does not specify how test data are ordered during evaluation. Are samples from all tasks randomly interleaved? Processed task-by-task? Does the order vary across runs? Since early test samples determine the direction of classifier updates (Algorithm 1, line 4), the ordering fundamentally affects results. This makes the experiments impossible to reproduce or verify.

### Minor

- **Representation retention evidence limited to ImageNet-R (Figure 3 only).** The central claim that representation layers retain knowledge is supported exclusively on ImageNet-R with one specific pretrained model family (ImageNet-21K ViT/ResNet). No linear probing experiments are shown for CIFAR-100 or the 5-dataset composite, leaving open the question of whether the same pattern holds under different pretraining distributions or smaller scale. This does not invalidate the paper's approach, but limits the generality of the motivational evidence.

- **No analysis of computational cost or update frequency.** ARC performs a full backward pass on every test sample satisfying Assumption 1 (Adaptive Retention). The paper does not report what fraction of test samples trigger the update, the per-sample wall-clock time, or the total FLOPs overhead. The text does mention that only 1.9% of samples satisfy Assumption 2 for L2P, but says nothing about the retention-side fraction. Without this information, the practical deployability of ARC is unclear. (Note: a cost analysis would likely work in the authors' favor if the fraction is small, as the ablation suggests for some methods.)

- **Default hyperparameter values not stated.** The paper reports ablations of thresholds \(\beta\) and \(\gamma\) ranging from 0.6–0.9 and 0.6–1.0, but does not state the specific values used in the main experiments (Tables 1–3). These should be reported for reproducibility.

### Trivial

- The "Memory-Free" column in Table 1 is inconsistently labeled across methods (checkmark for DualPrompt, ambiguous symbol for iCaRL, blank for others where the implementation details suggest otherwise).

## Nice-to-Haves

- Adding an oracle upper bound (perfect task detection) would help separate OTD quality from retention/correction quality.
- Reporting precision and recall of OTD (not just accuracy of the two assumptions) would deepen the analysis of the detection step.
- Ablating test-sample ordering (random vs. task-by-task vs. worst-case) would demonstrate robustness to a practical variable.

## Removed Points

These points were flagged but are removed or demoted based on the filtering rules:

- **"Missing comparison to OOD baselines (MSP, ODIN, energy)"** — Removed. OTD is used as a detection component within ARC, not as a standalone OOD method. The paper's scope is CL debiasing, not OOD detection benchmarking. Asking for this comparison is scope creep.
- **"Only one TTA baseline (TENT); should include CoTTA/SHOT"** — Removed. The paper is a CL method with a TTA comparison as supplementary evidence. This is scope creep; the paper is not a TTA paper.
- **"5-dataset tests only four methods, missing prompt-based ones"** — Removed. L2P is tested on 5-dataset (Table 2), and L2P *is* a prompt-based method. The criticism is factually incorrect.
- **"No experiments on 50 tasks or severe domain shift (DomainNet, CORe50)"** — Removed. The paper already tests 20-task sequences, which is a standard length in the CL literature. 50 tasks is scope creep.
- **"Ambiguous Memory-Free column"** — Removed. This is a formatting artifact from PDF parsing; the original table likely had cleaner formatting.
- **"Algorithm 1 may cause error accumulation"** — Demoted from a standalone point. This is a speculative concern with no evidence in the paper that the proposed method actually suffers from error accumulation. Can be discussed but is not a verified weakness.
- **Strength Finder claims about "important problem" / generic praise** — Removed per filtering rules. Only concrete, evidence-grounded strengths are kept.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same insights as the paper itself (classifier-bias dominance, OTD validation, consistent gains with ARC), and the calibration anchors confirm that the core weakness (evaluation rigor) is a known failure mode for papers in this intersection of TTA and CL.

## Suggestions

1. **Add multiple runs with standard deviations** for all main experiments (Tables 1–4, at least 3–5 random seeds with different test-sample permutations). This is the single most important revision: without it, the empirical claims are not properly supported.
2. **Explicitly state the test-sample ordering protocol.** If samples are randomly shuffled across all tasks with a fixed seed, say so. If processed task-by-task, say so. Clarify whether the ordering is fixed or randomized across runs.
3. **Report computational cost:** the fraction of test samples triggering the retention update, per-sample wall-clock time with and without ARC, and GPU memory overhead.
4. **State the default \(\beta\) and \(\gamma\) values** used in the main experiments.
5. **Add linear probing evidence on CIFAR-100** (similar to Figure 3) to broaden the generality of the representation-retention claim.

## Score and Decision

All retrieved anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `A1JdcLawSu.md` | 3.0 | R1 | Much weaker; stability gap paper with less evidence |
| `lEsNGN1SjG.md` | 2.0 | R1 | Unrelated topic |
| `ZIbUx5dzfZ.md` | 3.0 | R1 | Unrelated topic |
| `HCCkCjClO0.md` | 3.0 | R1 | Online weight approx for CL; weaker evidence |
| `fRNDDFkPiv.md` | 6.75 | R1/R2 | Most similar (TTA for CL); same protocol ambiguity weakness; slightly stronger scores but still rejected |
| `eXrUdcxfCw.md` | 4.80 | R1/R2 | CTA prototype method; less novel, marginal gains |
| `9w3iw8wDuE.md` | 7.00 | R1 | Pure TTA paper (DeYO); stronger theory & experiments |
| `sEMJ1PLSZR.md` | 6.25 | R1 | Pure TTA paper (AEA); different setting |
| `TPZRq4FALB.md` | 8.0 | R1 | Strong TTA paper |
| `SctfBCLmWo.md` | 8.0 | R1 | Unrelated topic |
| `TpD2aG1h0D.md` | 8.67 | R1 | Meta-CL theory paper |
| `uAFHCZRmXk.md` | 8.0 | R1 | Unrelated topic |
| `7iuFxx9Ccx.md` | 6.0 | R2 | SlimTTT (resource-efficient TTT); different focus |
| `1nHQRsb3Ze.md` | 5.0 | R2 | Auxiliary classifiers for CL; similar "plug-in" profile; comparable evaluation rigor |
| `DJZDgMOLXQ.md` | 6.50 | R2 | PEC for CIL; stronger novelty + theory; accepted |
| `3Z2flzXzBY.md` | 6.40 | R2 | PASLE for TTA; different setting |

Round-1 bracket: **4.5 – 6.5**  
Round-2 narrowing: The paper is noticeably stronger than `1nHQRsb3Ze.md` (5.0, Reject — simpler method, weaker motivation) but weaker than `fRNDDFkPiv.md` (6.75, Reject — similar topic, more thorough evaluation despite same weakness) and substantially weaker than `DJZDgMOLXQ.md` (6.50, Accept — stronger theoretical grounding). The decisive gap between this paper and the 6+ anchors is the absence of statistical rigor: the most similar paper (`fRNDDFkPiv.md`) was rejected partly for the same reason.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
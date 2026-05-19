Now let me perform calibration search to anchor the score.Let me read a few of the most topically similar anchors in full:Round 1 bracket: **5.5 – 7.5**. AdaMerging clearly outperforms CABS (4.75) and SUPERMERGE (4.33) in result quality and experimental breadth. Now narrowing.Let me read the two most topically relevant anchors in detail:I have sufficient calibration data. Let me now write the full review.

---

## Summary

AdaMerging introduces an adaptive model merging scheme for multi-task learning that learns per-task or per-layer merging coefficients via entropy minimization on unlabeled test samples, without requiring access to the original training data. The core insight is that minimizing prediction entropy on unlabeled test data (Spearman correlation 0.87 with cross-entropy loss) serves as an effective surrogate objective to automatically determine merging coefficients — replacing error-prone grid search. On eight image classification tasks using CLIP ViT-B/32 and ViT-L/14, Layer-wise AdaMerging achieves 80.1% and 90.8% average accuracy respectively, representing ~11% and ~6.3% improvements over Task Arithmetic.

---

## Strengths

- **Concrete motivation for adaptive coefficients**: Figure 1 plots average accuracy vs. global coefficient λ for both Task Arithmetic and Ties-Merging, showing steep accuracy cliffs on either side of the optimal λ. This targeted empirical evidence directly motivates the need for adaptive coefficient learning rather than grid search — a specific insight not previously highlighted in the model merging literature.

- **Quantitative justification for entropy as proxy**: Section 3.2.2 and Figure 2 provide both qualitative (entropy-interval binning) and quantitative (Spearman ρ = 0.87 across all eight tasks) evidence that entropy minimization correlates with loss minimization in the multi-task merging setting, justifying the unsupervised optimization objective.

- **Substantial and consistent empirical gains**: Table 1 (ViT-B/32) shows Layer-wise AdaMerging at 80.1% vs. Task Arithmetic 69.1% (+11%) and Ties-Merging 72.4% (+7.7%). Table 2 (ViT-L/14) shows 90.8% vs. 84.5% (+6.3%) and 86.0% (+4.8%). The improvements hold across both model scales and across all per-task results with few exceptions.

- **Generality of the approach**: The method is cleanly instantiated on top of both Task Arithmetic (AdaMerging) and Ties-Merging (AdaMerging++), with both variants showing consistent gains (Table 1: 80.1%/81.1% vs. 69.1%/72.4%), demonstrating that adaptive coefficient learning is not tied to a specific base merging algorithm.

- **Interpretable layer-wise coefficient analysis**: Figure 3 shows learned coefficients are inhomogeneous across layers, with shallow layers receiving systematically lower coefficients than deep layers — consistent with the established understanding that shallow layers encode general features and deep layers encode task-specific features (Yosinski et al., 2014). This provides a mechanistically interpretable, specific insight beyond just reporting numbers.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing test-time adaptation baseline**: AdaMerging's merging coefficients are optimized on the test distribution via entropy minimization, while all baselines (Task Arithmetic, Ties-Merging, Fisher Merging, RegMean) produce fixed merged models with no access to test data. This means the observed performance gap could be partially or largely attributable to the benefit of *any* test-time adaptation, not specifically to the per-layer coefficient parameterization. A TENT-style baseline — applying entropy minimization to the merged model's parameters directly (e.g., updating batch norm or affine parameters, as in Tent) with the same budget of test-time iterations — would disentangle this. As written, the paper cannot attribute the gains to coefficient-space parameterization vs. test-time entropy minimization in general. This is the paper's most significant evidential gap.

- **The Task-wise → Layer-wise gap is unexplained**: Table 1 shows Task-wise AdaMerging at 71.1% vs. Layer-wise AdaMerging at 80.1% (+9.0%) on ViT-B/32. The paper describes this as a benefit of "more fine-grained fusion" (Section 4.2) but provides no ablation that varies coefficient granularity at a fixed adaptation budget. Layer-wise AdaMerging has $K \times L$ free parameters vs. $K$ for Task-wise, meaning it has access to far more gradient signal per adaptation step. The 9-point gap could reflect optimization advantage (more free parameters to fit the test distribution) rather than structural insight. A controlled comparison — same number of total adaptation steps, same optimizer — would be needed to attribute the gap to the architectural choice.

### Minor

- **Per-task regressions in robustness table not acknowledged**: Table 4 (robustness, ViT-B/32) shows that under Impulse Noise, AdaMerging's EuroSAT accuracy is 30.8% vs. Task Arithmetic's 49.1% (−18.3 pp); under Spatter, EuroSAT drops to 43.6% vs. 60.1% (−16.5 pp). While the aggregate averages still favor AdaMerging for these corruption types (62.8% vs. 56.1%; 69.6% vs. 62.9%), these individual regressions are substantial and go entirely unacknowledged. The paper's claim of "consistently higher robustness" is inaccurate at the per-task level for EuroSAT.

- **Claim that 0.1%–1% unlabeled test data suffices is unsupported by experiment**: Section 3.2, final paragraph, states "even if only 0.1% or 1% of unlabeled tests are available, our method can have significant performance improvements." No ablation is provided in the main text — there is no performance-vs.-sample-count curve. The main results appear to use the full test set. This assertion should be backed by quantitative evidence.

- **Optimization hyperparameters absent from main text**: Learning rate, number of iterations, optimizer, and batch size for the entropy minimization step are not reported in the main paper. For a method whose contribution is the optimization process itself, these details are essential for understanding the method's behavior and practical deployment.

### Trivial

None beyond the omitted hyperparameters already noted above.

---

## Nice-to-Haves

- An experiment forcing shallow-layer coefficients to a fixed constant and learning only deep-layer coefficients would directly test the mechanistic claim in Figure 3 (shallow layers rely on pretrained weights; deep layers rely on task-specific vectors). If this recovers most of the Layer-wise gain, it would sharpen the structural insight substantially.

- Including Ties-Merging in the robustness table (Table 4) would complete the comparison and make the robustness claim against all primary baselines rather than only Task Arithmetic.

- A per-dataset breakdown in Table 2 (ViT-L/14) comparable to Table 1 is already present — extending the same level of detail to generalization and robustness tables would improve transparency.

---

## Removed Points

*These points were flagged for removal; treat with caution:*

- **"Generalization experiments are confounded by TTA"** (Harsh critic, Issue 2): The harsh critic argues that AdaMerging's performance on unseen tasks is simply TTA adapting to those tasks. This is largely correct but actually validates the method's practical value — the paper explicitly frames AdaMerging as leveraging unlabeled test data (the abstract, Sec. 3.2). The unseen-task experiment still demonstrates something non-trivial: AdaMerging's coefficient optimization does not harm unseen-task performance and in fact improves it, which is not guaranteed. Removed as a standalone weakness because it conflates method framing with method validity.

- **"Entropy-loss correlation analysis uses test data with labels post-hoc"** (Harsh critic, Sec. 3.2 note): The analysis in Section 3.2.2 measures correlation between entropy H(Ŷ) and prediction loss L(Y,Ŷ) at a fixed model checkpoint, using the fixed merged model. The harsh critic argues this is post-hoc and doesn't verify that entropy-gradient descent leads to lower loss. While the concern is theoretically valid (correlation ≠ optimization landscape benignity), the Spearman ρ = 0.87 analysis is an accepted empirical validation technique in the TTA literature. The collapse argument (all coefficients → 0) is speculative and not demonstrated. Demoted from a major concern; retained only as background motivation for the TTA baseline request above.

- **"Unfair comparison with Fisher Merging and RegMean"** (Harsh critic, Sec. 4.2): Fisher Merging and RegMean require training data. If anything, this asymmetry *favors the baselines*, making AdaMerging's wins over them in Table 1 stronger evidence. Removed per hard rules (unfair comparison favoring the baseline is not a weakness of the paper).

- **"The 11% headline improvement is compared to the weaker baseline"** (Harsh critic, abstract note): The 11% figure (80.1% vs. 69.1%) correctly compares to Task Arithmetic, which is the primary baseline named first in the paper. Comparing to Ties-Merging gives 7.7%. The abstract accurately frames this as "compared to the current state-of-the-art task arithmetic merging scheme." This is factually accurate and not misleading. Removed.

- **"Degenerate solution concern for entropy minimization"** (Harsh critic): The concern that entropy minimization might collapse to all-zero coefficients (returning pretrained model with overconfident wrong predictions) is speculative and not observed in the experiments. Task Table 1 shows all non-trivial coefficients (Table 5, range 0.14–0.58). Removed as speculation.

---

## Novel Insights

The paper's most original contribution is not the merging framework per se, but the demonstration that entropy minimization — a tool from test-time adaptation — can be repurposed as a surrogate objective to navigate the coefficient space of merged task vectors efficiently and interpretably. The layer-wise coefficient patterns (Figure 3) provide an independent empirical confirmation of the generalization theory of deep networks (shallow = general, deep = task-specific) in a model merging context, a connection not previously explored. If a future comparison to direct TTA baselines validates that the coefficient-space parameterization (K×L scalars) achieves competitive gains to full-parameter TTA at far lower cost, this efficiency argument would be the paper's strongest contribution.

---

## Suggestions

1. Add a TENT baseline: apply entropy minimization to the batch-norm/affine parameters or full model weights of a fixed Task Arithmetic merged model. Compare adaptation quality and computational cost to AdaMerging. This single experiment would either (a) validate the coefficient-space parameterization as sufficient or (b) identify that full TTA is better, clarifying the exact contribution.

2. Add a sample efficiency curve: plot average accuracy (y-axis) vs. number of unlabeled test samples used for adaptation (x-axis, log-scale from 0.1% to 100%) to empirically support the "0.1% suffices" claim.

3. Acknowledge and analyze the EuroSAT regressions under Impulse Noise and Spatter in Table 4. Exploring why entropy minimization over-adapts EuroSAT under certain corruptions while benefiting other tasks would deepen the robustness analysis.

4. Report optimization hyperparameters (learning rate, iterations, optimizer, batch size) in the main paper or a clearly labeled setup table. For a method whose core is iterative optimization, these are essential for reproducibility.

---

## Score Calibration

**Round 1 anchors:**
| Path | Score | Round | Comparison to AdaMerging |
|---|---|---|---|
| lNtio1tdbL (ATM: Alternating Tuning and Merging) | 3.00 | R1-low | Clearly weaker: divided scores, methodological issues |
| plflYGf23L (CABS) | 4.75 | R1-mid | Weaker than AdaMerging: smaller gains, limited coverage |
| lIdc5DUplq (SUPERMERGE) | 4.33 | R1-mid | Weaker: gradient-based merging with smaller gains |
| irPcM6X5FV (Submodule Linearity) | 6.00 | R1-mid | Comparable: proposes layer-wise merging, smaller gains |
| Bq3fEAGXUL (Realistic Evaluation) | 5.33 | R1-mid | Weaker: evaluation/analysis paper, no new method |
| TPZRq4FALB (TTA multi-modal reliability) | 8.00 | R1-high | Stronger: more comprehensive TTA contribution |
| gc8QAQfXv6 (Function Vectors + CF) | 9.00 | R1-high | Much stronger: broader LLM contribution |

**Round 1 bracket: 5.5 – 7.5**

**Round 2 anchors:**
| Path | Score | Round | Comparison to AdaMerging |
|---|---|---|---|
| D7KJmfEDQP (Gradient Matching Merge) | 6.00 | R2 | Comparable: also proposes optimization-based merging, similar-scale gains, accepted |
| dj0TktJcVI (Fine-Tune Attention Only) | 6.25 | R2 | Slightly weaker: more limited gains, divided reviewer opinions |
| q3ztjJRQuJ (Task Arithmetic Trust Region) | 5.75 | R2 | Slightly weaker: rejected, smaller gains |
| dqMqAaw7Sq (DAM: Backdoor-Aware Merging) | 7.00 | R2 | Slightly stronger: addresses a broader security + performance problem |
| 9w3iw8wDuE (Entropy not enough for TTA) | 7.00 | R2 | Different domain (TTA, not merging), comparable contribution level |
| 1v7SRWsYve (MAP: Pareto Front Merging) | 6.33 | R2 | Comparable: Pareto front merging, similar breadth |
| 75PhjtbBdr (Multi-Label TTA) | 6.25 | R2 | Different domain; comparable experimental quality |

**Round 2 narrowing:** AdaMerging shows larger empirical gains than the 6.0-anchor papers (D7KJmfEDQP, irPcM6X5FV), better experimental coverage, and a novel entropy-proxy justification. However, the missing TTA baseline and unacknowledged per-task robustness regressions prevent the paper from reaching 7.0 (where papers like DAM and the entropy-not-enough TTA paper sit). AdaMerging is clearly better than the 5.75 reject (q3ztjJRQuJ) and comparable to or slightly above the 6.0–6.25 cluster of accepted merging papers.

**Final score: 6.5** — Above the model-merging cluster at 6.0–6.25 due to larger gains and better experimental breadth, but below 7.0 due to the missing TTA disentanglement baseline and unacknowledged individual regressions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
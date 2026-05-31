Now let me run calibration searches to anchor my score.**Round 1 bracket: 4–6.** The paper has a novel problem setup but evaluation weaknesses. Let me narrow within this range.Now I have enough information to write the full review. Let me compile my analysis.

---

## Summary

FF-Erase is the first machine unlearning framework tailored to Forward-Forward (FF) models, which use layer-wise greedy optimization (goodness-based training) instead of backpropagation. The paper identifies that standard gradient-ascent unlearning causes instability and model collapse in FF models due to their sensitivity to parameter tuning and independent layer-wise objectives. FF-Erase addresses this by steering each layer's goodness distribution toward a guidance model (trained on remaining data only) via KL-divergence minimization. Complementarily, the paper proposes G-MIA, a goodness-vector-based membership inference attack designed specifically for FF models, intended as the verification tool for FF unlearning. Experiments on CIFAR-10/100, MNIST, and Fashion-MNIST using TinyCNN, AlexNet, and VGG13 show that FF-Erase avoids collapse, preserves model accuracy within 1.6–3.3% of retrained accuracy, and runs 1.9–3.1× faster than retraining from scratch.

---

## Strengths

- **Genuine first-mover novelty.** To the best of reviewers' knowledge, no prior work has formalized or studied machine unlearning for FF models. The identification of unique challenges—goodness distribution instability and layer-wise independence complicating the effectiveness-utility trade-off—is clearly motivated by experimental evidence (Section 6.3, Figure 5).

- **Empirical failure mode established.** The paper systematically explores gradient ascent (GA) across six λ values (Section 6.3, Figure 5) and demonstrates that every setting either causes model collapse (λ ≥ 10⁻¹) or fails to unlearn (λ ≤ 10⁻²), with G-MIA scores remaining at 0.60–0.61 compared to RE's 0.55. This concretely establishes GA's inapplicability to FF models.

- **Guidance model ablation confirms mechanism.** Table 1's R.G.M. entry (randomly initialized guidance model) causes Acc_t to collapse from ~79% to 55.53%, demonstrating that the guidance quality—not just any KL regularization—is responsible for FF-Erase's stability. This supports the central design choice.

- **G-MIA outperforms all black-box MIAs.** Figure 3 shows that G-MIA consistently exceeds the final-layer black-box MIA (FL) across all three architectures, and specifically outperforms all white-box attacks on VGG13+CIFAR-100. The goodness vectors from all layers provide richer membership signals than the final layer alone.

- **Efficiency claim is analytically grounded and experimentally confirmed.** Equation (9) provides a closed-form time decomposition, and Table 1 confirms that FF-Erase achieves 25–35% of retraining time across configurations, consistent with the claimed speedup.

---

## Weaknesses

### Fatal
None.

### Major

- **G-MIA verification scores are near the detection floor, making quantitative effectiveness claims unreliable.** All G-MIA ACC values in Table 1 range from 0.551 (RE gold standard) to 0.621 (worst FF-Erase variant), and in Figure 4(c), from 0.5245 to 0.5520. These differences—on the order of 0.005–0.03 over a 0.5 baseline—are not supported by any variance estimates or significance tests. The claim that "FF-Erase achieves comparable unlearning effectiveness as retraining" rests on distinguishing, e.g., a G-MIA ACC of 0.556 from 0.551. With scores operating this close to the chance floor (0.50), no quantitative conclusion about relative unlearning quality can be reliably drawn. The paper should either complement the G-MIA metric with a more sensitive measure or provide statistical evidence that the observed differences are non-random.

- **Evaluation uses an unrealistically large forgetting fraction (20%), limiting generalizability.** Section 6.2 states: "we randomly sample 20% of the training data D_train as forgetting D_forget." This is an atypically large forgetting fraction—most privacy-motivated GDPR "right-to-be-forgotten" use cases involve individual data points or small user cohorts. Two consequences: (a) GA collapses under this load, making it a trivially weak baseline; (b) the efficiency advantage of FF-Erase (avoiding retraining 20% of data) is more pronounced than it would be for realistic, small-scale deletion requests. The paper's contributions would be substantially more credible if extended to small-scale forgetting (e.g., single-class removal or individual sample deletion).

- **Comparison involves only a single baseline (GA).** Section 6.2 compares FF-Erase against retraining from scratch (RE) and gradient ascent (GA) only. The paper argues in Section 2 and Appendix A that other approximate methods (SCRUB, f-SCRUB, Bad Teacher, influence-function methods) are inapplicable to FF models, but no empirical evidence for their inapplicability across multiple forgetting fractions is presented in the main body. Even a brief demonstration—showing that carefully tuned GA with gradient clipping or fine-tuning-based methods also fail—would significantly strengthen the motivation for FF-Erase.

### Minor

- **Fast-distilled guidance model is conceptually contaminated.** Equation (8) trains the guidance model θ_g by distilling from the original model θ_o, which was trained on the forgetting data. The paper states in Section 4.2 that the guidance model must be "ignorant of the forgetting data," but this requirement is violated by construction in the fast-distillation strategy—θ_g inherits θ_o's representations of forgetting samples. Table 1 shows D-variants slightly underperform R-variants on G-MIA (e.g., D-(0.3,0.5) gets 0.568 vs. R-(0.3,0.5) gets 0.569—actually similar), and the practical impact appears small, but the conceptual inconsistency is unresolved.

- **The "matches white-box attacks" claim is overstated.** Section 6.1 states G-MIA "even matches the performance of white-box attacks." This is drawn from Figure 3(c) showing VGG13+CIFAR-100, where G-MIA earns the "best overall" star. However, Figure 3(a)-(b) show that white-box attacks (GR, GAP, ST) outperform G-MIA on TinyCNN and AlexNet. The abstract and introduction should qualify that G-MIA matches white-box attacks specifically on deeper architectures and more complex datasets, not in general.

- **Eq. (1) notation is inconsistent with its prose.** Equation 1 writes g^l = ‖h^l‖₁, which reads as a scalar norm, but the surrounding text and Footnote 1 clarify that h^l ∈ ℝ^{J×d^l} and g^l is a J-dimensional column-wise L1 norm. This mismatch between the equation and the narrative will confuse readers trying to reproduce the forward computation.

- **Mini-retrained guidance model initialization is unspecified.** Section 4.2 describes the mini-retrained strategy (Eq. 7) as retraining on a subset for a fraction of epochs, but does not specify whether the student θ_g starts from a random initialization or is warm-started from θ_o. This distinction matters because warm-starting would carry forward some influence of the forgetting data—precisely what the guidance model is supposed to avoid.

### Trivial
None that apply under the hard rules.

---

## Nice-to-Haves

- **Statistical significance testing.** With G-MIA ACC differences of order 0.005–0.02, reporting confidence intervals across multiple seeds would substantially strengthen the quantitative comparisons in Table 1.

- **Independent calibration of G-MIA on a ground-truth membership set.** Evaluating G-MIA on a known-member/known-non-member split of an *unmodified* FF model (where membership is exact) would establish its precision-recall tradeoff independent of any unlearning experiment, decoupling the two contributions and removing the circularity concern.

- **Efficiency vs. quality Pareto frontier.** The ablation in Table 1 partially captures the trade-off from varying α₁ and α₂, but presenting this as a Pareto curve (time vs. G-MIA AUC or Acc_f) rather than a table would more clearly communicate where the optimal operating points lie.

- **Small-scale forgetting experiments.** Extending to individual-sample or single-class forgetting would test whether the per-layer instability argument holds at realistic GDPR scales, not just at the 20% level used in the paper.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"G-MIA is not lightweight"**: The harsh critic argues the four-step G-MIA pipeline (shadow model training, model inversion, attack classifier) contradicts the "lightweight" label. However, the paper's claimed novelty is leveraging goodness scores rather than final-layer outputs, which is a standard shadow-model MIA framework enhanced with a feature-engineering insight. The computational overhead is comparable to prior work (e.g., Shokri et al. 2017) and the "lightweight" characterization refers to the inference step rather than the setup. *Removed as a nitpick on marketing language rather than a substantive flaw.*

- **"Abstract speedup range conflates configurations"**: The critic argues the "1.9–3.1×" range blends different α₁/α₂ choices with different quality. The paper explicitly states this range and details it in Table 1; the range honestly represents the space of configurations. *Removed as cherry-picking a presentation issue.*

- **"GA trivially fails because forgetting fraction is 20%"** as an argument to remove GA as a baseline altogether: Per hard rules, we do not flag unfair comparisons that favor the baseline over the paper's method. The GA collapse at 20% deletion actually disadvantages the comparison (making FF-Erase look more necessary), not advantageous. *Retained partially as the "trivially weak baseline" note under Major weaknesses.*

- **Appendix-related weaknesses**: The harsh critic mentions that inapplicability of SCRUB/f-SCRUB is relegated to Appendix A. Per hard rules, appendix sections are not stripped selectively—the claim is noted in the main text (Section 2, Section 6.2) and detailed analysis in Appendix A is acknowledged. *Removed as appendix-based criticism.*

- **"Forgetting forward notation inconsistency is a reproducibility concern"**: The critic escalates Eq. 1's notation issue to a "reproducibility concern." Footnote 1 in the paper explicitly clarifies the column-wise L1 norm interpretation. *Retained only as a minor presentation issue, not a reproducibility concern.*

---

## Novel Insights

The key insight that the verification tool and the unlearning method should be co-designed—since standard MIAs fail on FF models just as standard unlearning methods do—is genuinely novel. The paper is among the first to observe that the per-layer goodness representation in FF models creates a richer membership signal than final-layer predictions alone, and that this same structure makes gradient-ascent unlearning unstable in ways not seen in BP models. Arguably the most valuable finding is the empirical characterization in Section 6.3: the entire landscape of GA hyperparameters collapses or fails to unlearn for FF models, motivating a fundamentally different design philosophy (guidance-model stabilization) rather than just hyperparameter tuning of existing methods.

---

## Suggestions

1. **Decouple evaluation**: Validate G-MIA on an unmodified FF model with exact ground truth membership before using it to evaluate FF-Erase. This eliminates the circular evaluation concern and strengthens both contributions independently.
2. **Add small-scale forgetting experiments**: Run experiments with 1%, 5%, and single-class forgetting to establish generalizability beyond the 20% setting.
3. **Fix Eq. 1 notation**: Explicitly write g^l ∈ ℝ^J as the column-wise L1 norm of H^l ∈ ℝ^{J×d^l} directly in the equation, eliminating the scalar-vs-vector confusion.
4. **Specify guidance model initialization** for the mini-retrained strategy to ensure reproducibility and avoid conceptual contamination concerns.
5. **Add error bars**: Run 3–5 trials and report mean ± std for G-MIA ACC/AUC in Table 1 and Figure 4 to support quantitative claims about small differences.

---

## Score and Decision

**Anchors consulted:**

| Round | Path | Avg Score | How it compares |
|---|---|---|---|
| R1 | `85X9awoVtv.md` | 2.50 | Much weaker — auditing compliance formulation without novel method |
| R1 | `Xagys9QD3T.md` | 3.00 | Weaker — PPU is straightforward label-replacement with limited novelty |
| R1 | `hwXUmwJAq5.md` | 3.00 | Weaker — gradient-label-smoothing unlearning, limited differentiation |
| R1 | `Uv7bWrIucU.md` | 4.20 | Somewhat weaker — auditing MU privacy, narrower scope than FF-Erase |
| R1 | `KvFk356RpR.md` | 4.80 | Slightly weaker — UMA attack on unlearning, but no new unlearning method |
| R1 | `iQIQT88prm.md` | 5.33 | Comparable — also integrates MIA+unlearning (Stackelberg), similar experimental gaps |
| R1 | `xmQuUqSynb.md` | 5.75 | Slightly stronger — adversarial robustness angle with more theoretical depth |
| R2 | `pUOesbrlw4.md` | 5.25 | Comparable — novel class unlearning on feature space, comparable scope |
| R2 | `wAemQcyWqq.md` | 5.67 | Slightly stronger — privacy-preserving unlearning with more elaborate framework |
| R2 | `3p4raemLAH.md` | 5.75 | Slightly stronger — SLUG single-layer method with broader evaluation |
| R2 | `LRSspInlN5.md` | 5.50 | Comparable — black-box MIA for specific model type (diffusion), similar novelty |
| R2 | `nAK26c8s9X.md` | 4.50 | Slightly weaker — incremental MIA with less problem novelty |

**Round 1 bracket: 4.5–6.0**

**Round 2 narrowing:** The closest anchors are:
- `iQIQT88prm.md` (5.33): Also co-designs MIA with unlearning, similar experimental limitations (only CIFAR datasets, no formal convergence guarantees, missing baselines). FF-Erase has a more concrete novel problem (first for FF models) and more ablations, but suffers from the near-chance metric issue.  
- `LRSspInlN5.md` (5.50): Black-box MIA for a specific model type, similar novelty profile, similar experimental depth. Comparable on most axes.
- `wAemQcyWqq.md` (5.67): More elaborate method with a cleaner evaluation framework. FF-Erase is weaker here because of the G-MIA circularity and 20% forgetting.

**Assessment:** FF-Erase sits between `iQIQT88prm.md` (5.33) and `LRSspInlN5.md` (5.50). The paper's problem novelty is genuine and the dual-contribution structure is comparable to these anchors, but the near-chance G-MIA metric and the single large-scale forgetting fraction are more problematic than the weaknesses in those anchors. The 20% forgetting concern and limited baseline comparison together form a meaningful gap in the evaluation. I score this at **5.0**.

**Decision: Reject.** The paper makes a genuine contribution—first unlearning framework for FF models—supported by reasonable methodology. However, the primary verification metric (G-MIA) operates near the chance floor (ACC 0.52–0.56), making the key quantitative claim ("FF-Erase achieves comparable unlearning effectiveness as retraining") difficult to substantiate. Combined with evaluation limited to a single, unrealistically large forgetting fraction and a single baseline, the paper needs a strengthened evaluation before it is ready for publication.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
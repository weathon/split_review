## Summary

This paper addresses the previously unexplored problem of machine unlearning for Forward-Forward (FF) trained neural networks. The authors identify that standard gradient-ascent unlearning causes model collapse on FF models due to their sensitivity to parameter tuning and layer-wise training. They propose FF-Erase, which stabilizes unlearning by minimizing KL divergence between the original model's layer-wise goodness vectors and those of a separately obtained "guidance model" trained only on remaining data. They also introduce G-MIA, a novel membership inference attack that leverages FF-specific goodness scores for black-box unlearning verification. Experiments on four datasets and four architectures show FF-Erase matches retraining in G-MIA scores (0.524 vs. 0.532) while being 1.9–3.1× faster, with a 1.6–3.3% test accuracy drop.

## Strengths

- **First formalization of FF unlearning challenges**: The paper clearly identifies two FF-specific obstacles — sensitivity to parameter tuning (which makes GA collapse) and layer-wise independent training (which complicates the effectiveness–utility trade-off). These are well-motivated in §1 and Appendix A, with empirical validation in §6.3 showing that GA, FYE, SURE, BT, and FATS all either collapse or fail to unlearn on FF models (Figures 5, 10).
- **G-MIA is a genuinely novel and effective attack for FF models**: Using only layer-wise goodness scores (a standard FF inference output), G-MIA consistently outperforms the black-box final-layer MIA (FL) and even surpasses white-box attacks (GR, GAP, ST) on deeper models like VGG13 on CIFAR-100 (Figure 3). This provides a practical verification tool that does not require access to model parameters or gradients.
- **Comprehensive experimental coverage**: Evaluation spans four datasets (MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100), four architectures (TinyCNN, AlexNet, VGG13, VGG16), and two FF training variants (CwComp, Deeperforward). The ablation study in §6.4 (Table 1) systematically quantifies the trade-off between guidance-model quality and unlearning performance across different (α₁, α₂) configurations, including a randomly initialized guidance model as a lower bound.
- **Layer-wise CKA analysis provides interpretable evidence**: Table 3 shows that FF-Erase reduces representational similarity between original and unlearned models across all layers on forgetting data, while baselines like Bad Teacher retain high similarity in shallow/middle layers and GA(λ=10) collapses entirely. This complements the G-MIA evaluation with a structural view of unlearning.

## Weaknesses

### Major

- **Unlearning evaluation relies almost entirely on a self-introduced metric (G-MIA)**: While the paper validates G-MIA against several existing MIAs (§6.1, Figure 3), the ultimate evidence that FF-Erase achieves effective unlearning is that G-MIA accuracy drops close to that of a retrained model (0.524 vs. 0.532). There is no independent calibration — for instance, measuring whether G-MIA can distinguish a retrained-from-scratch oracle from a model trained on all data, or combining G-MIA with a complementary audit (e.g., loss-trajectory MIA adapted to FF outputs). This creates a circularity risk: FF-Erase could be degrading G-MIA's attack signal rather than genuinely erasing membership information, and the paper provides no evidence to rule this out. This is the most substantive concern about the paper's central empirical claim.
- **CKA analysis reveals higher similarity than retraining at deep layers for FF-Erase variants**: The paper's own Table 3 shows that at layer 7, FF-Erase(D) and FF-Erase(R) have CKA similarities of 0.6168 and 0.6292 respectively, vs. 0.3619 for the retrained model (RE) — both marked with ↑ indicating "ineffective unlearning" by the paper's own criterion (>20% higher than RE). Similar patterns appear at layers 4–6 and 8–12. While the paper attributes this to residual feature retention (§C.2), it does not reconcile this anomaly with the claim of effective layer-wise unlearning, and the discussion (lines 1417–1421) treats these arrows as evidence that "FF-Erase(D) consistently outperforms FF-Erase(R)" without grappling with their divergence from the retrained baseline.

### Minor

- **No sensitivity analysis for key hyperparameters K, ε₁, ε₂**: The paper states that the recovery forward interval K and the early-stopping thresholds ε₁, ε₂ are "determined by the dataset" (§4.1) but provides no guidance on how practitioners should set them. Given that the method is presented as practical, this omission limits transferability. A small sensitivity sweep on K would substantially improve the paper.
- **Evaluation uses only a 20% forget ratio**: All experiments use β = 0.2 (§6). Realistic "right to be forgotten" requests typically involve much smaller forget sets (1–5%). The guidance model strategies (especially mini-retraining on 30% of remaining data) may behave very differently when the remaining data is nearly the full training set. The paper does not test this regime.
- **No direct comparison to using the guidance model itself as the unlearned model**: The paper convincingly shows that a randomly initialized guidance model is useless (R.G.M in Table 1), but does not report what happens if one simply uses the mini-retrained or fast-distilled model directly as the unlearned model after the same training budget. This would clarify how much value the KL-divergence guidance step adds beyond the guidance model training itself. This is a missing baseline rather than a fatal flaw.

### Trivial

- The abstract states that FF-Erase is 1.9–3.1× faster than retraining, but this depends on specific (α₁, α₂) choices; the main text (§4.3) appropriately contextualizes this with the 25–35% figure. The abstract could be more precise.
- G-MIA is described as "strict black-box" (§5), but it requires per-layer goodness vectors which are internal FF-specific outputs, not merely the final prediction. The paper acknowledges this access model in §5 (line 445) but the "strict black-box" label is debatable. This is a terminology issue that does not affect technical correctness.

## Nice-to-Haves

- Comparing FF-Erase against an adapted LiRA-style or loss-trajectory-based MIA on the unlearned models would strengthen confidence that the G-MIA reduction reflects genuine unlearning rather than attack degradation.
- Evaluating with smaller forget-set ratios (1–5%) would demonstrate applicability to realistic RTBF scenarios.
- A visualization of goodness-vector distributions (e.g., t-SNE or histograms) for forget-set samples before/after unlearning, alongside the guidance model and retrained model, would provide intuitive evidence that the unlearned model's representations genuinely approach a forget-free state.
- Sensitivity analysis for the recovery interval K and early-stopping thresholds ε₁, ε₂ would improve practical guidance.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"G-MIA is unverified / no independent validation" (from Harsh Critic #1, partially)**: The portion claiming G-MIA is entirely unvalidated is removed because the paper validates G-MIA against multiple existing MIAs (FL, GR, GAP, ST) in §6.1, Figure 3. The retained concern (moved to Major) is the narrower point about circularity in using G-MIA as the primary unlearning metric without calibration against an independent oracle.

2. **"Guidance model strategy makes the speed advantage conceptually uninteresting / just partial retraining" (Harsh Critic #2)**: This criticism is weakened because (a) the guidance model is not the final product — FF-Erase uses it only to steer the original model's unlearning; (b) the paper shows via the R.G.M ablation (Table 1) that a non-functional guidance model leads to catastrophic collapse (55.53% test accuracy), proving the guidance model is a genuine enabler, not a substitute; (c) using the guidance model directly as the unlearned model would yield poor accuracy since it was trained on only 30% data for 50% epochs. The retained concern (moved to Minor) is the missing baseline of directly comparing against the guidance model.

3. **"Absence of standard unlearning evaluation baselines / LiRA" (Harsh Critic #3)**: The paper does include multiple MIA baselines (FL, GR, GAP, ST) and multiple unlearning baselines (GA with various λ, Bad Teacher, FYE, SURE, FATS — Figures 5, 10 in Appendix). The claim that it uses "only the authors' own MIA" is factually incorrect. LiRA is designed for BP models and relies on loss values; adapting it to FF models is non-trivial and not an obvious missing baseline. Removed as overstatement.

4. **"GA known to be fragile even in BP networks" (Harsh Critic §-by-§)**: The paper's focus is on FF-specific collapse, not general GA fragility. The paper does discuss this in Appendix A. Removed as scope critique.

5. **"Notation unnecessarily heavy" (Harsh Critic §-by-§)**: Pure formatting/style nitpick. Removed per hard rules.

6. **"Fast-distillation may leak information about forget set into guidance model" (Harsh Critic §-by-§)**: The paper trains the fast-distilled guidance model on Dref ⊆ Dremain. The student never sees Dforget during training. The teacher (θo) has seen Dforget, but the distillation objective is evaluated only on Dref samples. This is a reasonable design that addresses the concern. Removed as misunderstanding.

7. **"White-box attack comparison may be confounded" (Harsh Critic §-by-§)**: The paper compares G-MIA against white-box attacks on the same FF models. If white-box attacks perform worse, that is evidence *for* G-MIA's effectiveness, not a fairness issue. Removed as logically backwards.

8. **Missing related works / appendix issues / formatting**: Removed per hard rules.

9. **Strength Finder — "Comprehensive cross-architecture and cross-dataset evaluation" in Supporting strengths**: This was moved to the main Strengths as it is substantive.

## Novel Insights

The observation that FF models' layer-wise goodness scores — originally designed merely as a training objective — serve as unusually informative signals for membership inference (G-MIA outperforming white-box attacks on deeper models) is genuinely novel and not obvious a priori. This suggests that FF's greedy layer-wise training may inadvertently create per-layer memorization signatures that are more accessible to black-box auditors than BP models' internal representations. This insight could generalize beyond unlearning verification to broader privacy analysis of biologically-inspired training algorithms, and may motivate future work on making goodness scores less informative.

## Suggestions

- The most impactful improvement would be adding an independent calibration of G-MIA: train shadow models on random data splits, measure G-MIA's ability to distinguish members from non-members for a fully retrained oracle, and report whether the G-MIA gap between FF-Erase and RE is statistically distinguishable. This would directly address the circularity concern.
- Include a baseline where the mini-retrained or fast-distilled guidance model is used directly as the unlearned model, to isolate the contribution of the KL-divergence guidance step.
- Add a brief discussion reconciling the higher CKA scores of FF-Erase at deep layers (Table 3, ↑ marks) with the overall unlearning claims. Even a paragraph acknowledging this as a limitation or open question would improve transparency.
- Report results for a smaller forget-set ratio (e.g., 5%) on at least one dataset to demonstrate real-world applicability.

---

**Comparison with calibration anchors:**

- **ZfdnZhOP0k (Hubble, avg 7.50, Accept Oral)**: Hubble is an exceptionally polished, large-scale resource contribution with open-source LLMs, extensive memorization studies, and community benchmarks. FF-Erase is much narrower in scope and scale, with a single-domain method and less thorough validation. The gap is substantial.
- **koKWoKaMrE (Tversky NN, avg 7.00, Accept Poster)**: A creatively novel neural network building block with strong psychological motivation. FF-Erase has comparable originality (first FF unlearning method, novel G-MIA) but less theoretical depth and weaker validation of its central claim.
- **Vc9yt0YwPw (VT Unlearning Benchmark, avg 5.50, Reject)**: The closest analog — first systematic study of unlearning in a new architecture family. That paper was rejected despite comprehensive benchmarking because findings were limited and algorithmic diversity was narrow. FF-Erase has a novel method (not just a benchmark) but similar evaluation gaps and a narrower scope.
- **xG0mQ4Xsfm (REM, avg 5.00, Accept Poster)**: A novel unlearning method with a clear taxonomy and strong results. FF-Erase has comparable novelty within its domain but weaker evaluation.
- **N8AMUF0ZeE (SPARC, avg 4.00, Reject)**: A corrective unlearning method with significant evaluation concerns and conceptual gaps. FF-Erase is stronger — it has a clearer problem motivation, better ablation studies, and a novel verification tool.
- **WNUDOLYlbh (L2UL, avg 3.00, Reject)**: A learning-based unlearning approach with conceptual circularity issues (needs retrained models to train). FF-Erase does not have this severity of problem.
- **hvTFoDsgCe (Suppressive Unlearning, avg 2.50, Withdrawn)**: A definition paper with questionable novelty and vacuous bounds. FF-Erase is substantially stronger with real empirical contributions.

FF-Erase makes real contributions — first FF unlearning method, novel G-MIA, solid empirical motivation — but the evaluation depends heavily on a self-introduced metric without independent calibration, and the CKA results show anomalies that are not adequately discussed. The paper opens a new sub-area and provides a credible baseline, which is valuable. It is stronger than the rejected 3.0–4.0 papers but does not reach the 6.0+ level of papers with more thorough validation and broader impact. It sits in the 4.5–5.5 range. Given that it has a novel method AND a novel verification tool AND comprehensive experiments, but with a significant evaluation concern (G-MIA circularity), I place it at the border of Accept Poster / Reject.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
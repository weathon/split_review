Now I have sufficient anchors for calibration. Let me compose my final review.

## Summary

This paper proposes Adversarial Perturbation Dropout (APD), a method to improve black-box adversarial transferability. During iterative attack optimization, APD computes CAM attention maps on the current adversarial example, identifies local maxima as midpoints, creates multiple versions where square perturbations around those midpoints are dropped at varying scales, averages the gradients from these versions, and uses the averaged gradient for the update. The method is integrated with five standard baselines (MI-FGSM, DIM, TIM, SIM, AAM) and the combined AA-TI-DIM, showing consistent 10–13% average ASR gains on ImageNet across seven target models.

## Strengths

- **Consistent and substantial empirical gains across multiple baselines.** Tables 1–3 show that integrating APD improves attack success rates by 10.3%–12.7% on average across baselines, with individual gains up to 19.6% (APD-AA-TI-DIM vs AA-TI-DIM on IncRes-v2, crafted on Inc-v3). The improvement holds across four normally trained and three adversarially trained target models, under both single-model and ensemble-model settings.

- **CAM-guided masking cleanly outperforms random masking.** Figure 4 directly compares CAM-guided region selection against random region selection across four source models, and CAM guidance consistently yields higher transferability. This demonstrates that the attention-guided component of the method provides genuine benefit beyond simple gradient diversification.

- **Method is simple, clearly described, and easily integrable.** The core algorithm (Section 3.4) is concisely presented with a clear update equation. APD can be added to any iterative attack by replacing the single gradient with an average over nm masked versions. This plug-and-play nature is a practical strength.

- **Ablation studies for key hyperparameters.** Figures 5 and 6 systematically explore the scale factor β, number of midpoints n, and number of scales m, showing that performance peaks at β=27 and saturates at n≈3–4 and m≈5–7, providing empirical grounding for the chosen defaults.

## Weaknesses

### Fatal
None.

### Major

- **The core mechanistic claim ("breaking synergy between perturbation regions") is asserted but not directly measured or validated.** The paper's narrative (Introduction, Section 3.3, contributions) frames APD as reducing mutual dependence between perturbation regions, drawing an analogy to neuron dropout (Srivastava et al.). However, no experiment measures whether the method actually reduces synergy—e.g., via interaction metrics, gradient correlation analysis, or controlled ablations where synergy is explicitly manipulated. The Figure 1(b) experiment on "Selective vs. Random Noise Removal" tests a different operation (removing perturbations in cross-model attention differences) and is presented qualitatively without specifying source/target model pairs, perturbation magnitudes, or quantitative results from the figure. The improvement could equally come from gradient diversity (which prior input-transformation methods already exploit), from CAM-guided augmentation being a better data augmentation strategy, or from the ensemble effect of multiple forward passes—the paper does not disambiguate these. This gap does not invalidate the empirical finding that APD works, but it means the paper's claimed contribution (understanding and breaking perturbation synergy) is not supported by the presented evidence. The method would be better framed as attention-guided gradient diversification.

- **The claim of "state-of-the-art" transferability is not substantiated by the experimental comparison.** The paper compares against MI-FGSM, DIM, TIM, SIM, AAM, and AA-TI-DIM—all published by 2021. The paper itself cites more recent works (e.g., Qin et al. 2022, Huang et al. 2019) in the introduction that are not included in the experimental comparison. Without benchmarking against more recent methods, the SOTA claim (Section 4.2: "state-of-the-art method for boosting adversarial transferability") is unverifiable from the presented evidence. Relatedly, the paper does not control for the increased computational cost of APD (which requires n×m=15 forward passes per iteration vs. 1 for the baseline). The appendix reference to a controlled-cost comparison cannot be verified from the main paper.

### Minor

- **No confidence intervals or variance estimates are reported for any attack success rates.** With 1000 images (binomial trials), reporting standard deviations or binomial confidence intervals is computationally trivial and would demonstrate that the 10–13% margins are statistically reliable. Several margins are smaller (e.g., 1.8% on MnasNet, ~0.4–0.5% in β ablation peaks), where variance information is particularly important for interpretation.

- **Evaluation scope is narrow along several dimensions.** All experiments use a single perturbation budget (ε=16, T=10, α=1.6 from MI-FGSM). It is unknown whether APD remains effective at smaller perturbations (e.g., ε=8) or with different iteration budgets. The defense models tested (feature denoising, NRP purification) do not include stronger adversarial training defenses (e.g., TRADES, AWP). The diverse architectures include only one transformer (ViT-B/16) and one compact CNN (MnasNet).

- **Several design choices lack ablation or justification.** (a) Only Grad-CAM++ is used; no comparison with Grad-CAM, Score-CAM, or other CAM variants is provided. (b) The paper states CAM is recomputed at each iteration because "attention region expands over the attack steps," but no ablation compares recomputed CAM vs. using initial CAM only, so the benefit of recomputation is unquantified. (c) The random region baseline in Figure 4 does not specify how many random regions are used or whether they match the CAM-based count, making the comparison less precise than it should be.

### Trivial

- The description of "dropping perturbations" (Section 3.4) is ambiguous: does this mean setting the perturbation in the region to zero (reverting to the clean image's pixel values), or withholding the gradient update for that region? From context, the former is intended, but this should be stated explicitly.
- The y-axis of Figure 6 is not labeled in the extracted text (captions describe "Attack Success Rates (%)" but the axis labels in the figure image are unclear).

## Nice-to-Haves

- Report wall-clock time or FLOPs to compare APD (15 forward passes/iteration) against baselines with matched compute (e.g., running MI-FGSM with 150 iterations instead of 10).
- Add an ablation where CAM-recomputation frequency is varied (every iteration vs. only at initialization) to validate the stated rationale.
- Include Grad-CAM, Score-CAM, or vanilla saliency comparisons to isolate the impact of CAM variant choice.
- Test whether APD improvements hold at smaller perturbation budgets (ε=8).
- Report failure-case analysis: does APD ever degrade white-box ASR? In which settings does APD help least?

## Removed Points

These points were raised by reviewers but are removed from the main assessment:

- **"Missing appendix / Appendix A.1 content":** REMOVED per Hard Rules: the parser strips appendices from all papers; they exist in the original submission. Criticisms reliant on appendix content being missing in the extracted text are not valid.
- **"Missing comparison against SSA, GRA, SMI-FGSM":** REMOVED per Hard Rules: the review cannot reference missing related works without external verification capability. The general point about insufficient evidence for SOTA is retained in Major.
- **"Figures embedded as images":** REMOVED: parser artifact, not an author error.
- **"Typos/grammar/formatting issues":** REMOVED: parser artifacts, not author errors.
- **"Pure hyperparameter sensitivity nitpicks":** The β ablation is provided (Figure 5); the criticism that a single β may not generalize across all settings is noted but is standard for the field. Weakened to Minor via the scope discussion above.
- **Strength about "identifies and mitigates perturbation synergy":** REMOVED per rule: strength-weakness conflict. The synergy claim is unsubstantiated (retained as Major weakness), so the strength must give way to the weakness.

## Novel Insights

The most useful observation from this review process is that the paper's empirical contribution (attention-guided gradient masking improves transferability) is separable from its conceptual narrative (breaking perturbation synergy). The empirical pattern—CAM-guided dropping outperforms random dropping—suggests that what matters is not "decoupling" per se but rather providing the optimizer with a diverse set of gradient signals that emphasize different attention sub-regions. This reframes APD as a principled augmentation of the DIM/SIM family (input transformation + gradient averaging) rather than a new mechanism. The CAM-driving advantage over random masking also implies that the quality of the attention signal matters: if CAM captures the same regions the target model will attend to, then dropping perturbations in those regions during training produces gradients that are robust even when those regions are later ignored. This is a testable prediction that the paper could verify with cross-model CAM similarity analysis.

## Suggestions

1. **Reframe the contribution.** Replace the "breaking synergy" narrative with "attention-guided gradient diversification." This is faithful to what the method actually does and does not require proving a non-obvious decoupling effect. The paper would be stronger for honestly describing its mechanism.

2. **Add variance estimates.** Report standard deviations or 95% binomial confidence intervals for all ASR tables. With 1000 images per experiment, this is trivially computable and would significantly strengthen the results.

3. **Benchmark against at least one more recent method** (published 2022–2023) to support the SOTA claim, or remove the SOTA language and position APD as a consistently effective add-on to existing input-transformation attacks.

4. **Ablate CAM recomputation** by comparing (a) recompute CAM every iteration, (b) use initial CAM only, and (c) use random fixed points. This would directly validate the recomputation claim and isolate the CAM benefit.

5. **Clarify the "dropping" operation explicitly** in Section 3.4: state whether dropped perturbations are zeroed out (reverted to clean pixel values) or whether the region is excluded from gradient computation.

---

## Score and Decision

My round-1 bracketing placed the paper between 3.5 and 7.5. Round-2 narrowing identified four relevant anchors:

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| LIMANS (fjwZHuQ3cm) | 5.50 | R2 | Stronger theoretical framework, similar empirical quality, similar weakness types. APD is weaker due to looser conceptual framing and narrower baselines. |
| LDM unrestricted attack (XjSfcJUcaA) | 4.75 | R2 | Larger ASR improvements (12–57%), more novel method, only minor weaknesses. APD compares unfavorably. |
| Unlearnable examples (Sw0O2ESxbf) | 4.75 | R2 | Strong empirical evidence with clean ablations but has algorithmic errors. APD is comparable but has a different weakness profile. |
| TATM MLLM transfer (vF4RhEPGtb) | 4.25 | R2 | Has a potentially fatal metric flaw. APD is slightly stronger since it lacks a similar methodological flaw. |

Comparing APD against these anchors: it is weaker than LIMANS (5.50) and the LDM paper (4.75), comparable to the unlearnable examples paper (4.75) though with a different weakness profile, and somewhat stronger than the TATM paper (4.25). The paper's method is sound and empirically effective, but the mechanistic claim is unsupported, the SOTA claim is unverified, and the methodological reporting has gaps common to mid-range papers. I place it at **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
## Summary

This paper proposes ALFA (Adversarial Latent Feature Augmentation), a data augmentation method for fair binary classification. ALFA generates fairness-adversarial perturbations of latent features by maximizing a covariance-based fairness constraint (Zafar et al., 2017) subject to an L∞-norm budget and Sinkhorn distance regularization, then fine-tunes the classifier on both original and perturbed features. The core conceptual insight is that training on adversarially biased features can rotate the decision boundary to cover regions where misclassification rates are disproportionately high across demographic groups.

---

## Strengths

1. **Formal connection between the attack objective and standard fairness metrics.** Proposition 3.1 proves that maximizing the covariance-based objective ℒ_fair is proportional to the mean signed-distance gap Δd_dp between demographic groups and to the sum of per-label gaps Δd_eod,y. Theorem 3.2 establishes ℒ_fair as a lower bound on ΔDP and ΔEOd under a piecewise-linear logit approximation. These results give a provable guarantee that the attack step genuinely widens fairness gaps — a level of rigor absent in prior latent-space augmentation methods such as FAAP and Fair-Mixup, which lack formal connections between their augmentation objectives and fairness outcomes.

2. **Novel conceptual approach with a clear diagnosis of prior limitations.** The idea of using fairness-adversarial attacks as a *training signal* (rather than merely as a way to degrade fairness) is genuinely counter-intuitive and well-motivated. Section 4.4.2 provides a concrete, visually supported analysis (Figure 5) of why prior methods underperform on tabular data: FAAP's GAN-based perturbations fail to reliably align with the sensitive hyperplane, and Fair-Mixup's interpolation misses the "unfair regions" where misclassification rates are skewed. The synthetic-data comparison (Figure 5) directly visualizes how ALFA's perturbed features land in the unfair regions while the competitors' do not.

3. **Multi-dataset, multi-classifier evaluation spanning tabular and image domains.** Experiments cover four tabular benchmarks (Adult, COMPAS, German, Drug) with Logistic Regression and MLP, plus CelebA with ResNet18, compared against six baselines (Fair-Mixup, TabFairGAN, FAAP, Fair-CDA, Influence-reweighing, FDR). Each configuration is run 10 times.

---

## Weaknesses

### Major

1. **Complete absence of numerical result tables.** The entire experimental evaluation rests on three raster-image Pareto frontier plots (Figures 2–4) from which no single accuracy, ΔDP, or ΔEOd value can be extracted. The paper claims that "ALFA shows the best fairness improvement in most cases" (Section 4.4.1) and that the method "consistently achieves group fairness with sacrificing minimum accuracy" (contribution 3), but a reader cannot verify the magnitude of improvements, compare methods precisely, or assess whether the reported standard deviations are large or small. Pareto frontiers are a useful complement, but for a paper whose third stated contribution is experimental validation, the absence of numerical tables is a critical gap. Figures do not substitute for numbers that the community can cite, compare, and build upon.

2. **No ablation studies isolating the method's components.** The proposed pipeline involves multiple design choices: the sign-conditional form of ℒ_fair, balanced upsampling, Sinkhorn distance regularization, and mixing weight λ. The paper provides no experiment that strips these away to measure their individual contributions. Without ablations (e.g., random perturbation vs. fairness-directed perturbation, training with balanced upsampling alone without any perturbation, varying α to test Sinkhorn sensitivity), there is no evidence that the *fairness attack objective* is responsible for the observed results rather than, say, the upsampling procedure or the fine-tuning process itself.

### Minor

1. **Theory characterizes the attack, not the core claim.** Proposition 3.1 and Theorem 3.2 prove that maximizing ℒ_fair widens signed-distance gaps (i.e., degrades fairness on the pre-trained classifier). This is correctly scoped — the abstract states "we theoretically prove that our adversarial fairness objective assuredly generates biased feature perturbation." However, the paper's headline narrative — a "counter-intuitive relationship between adversarial attacks against fairness and enhanced model fairness" — remains an intuitive claim supported only by a 2D synthetic example (Figure 5) rather than any formal analysis. A quantitative investigation of how fine-tuning actually moves the decision boundary (e.g., per-subgroup error rates before/after, boundary displacement measurements) would substantially strengthen the paper's central empirical thesis.

2. **Logistic regression operates in input space, not latent space.** The paper acknowledges this (Section 3.3, line 154: "in the Logistic Regression… the perturbation is conducted on the input space") but does not discuss the implications. For 4 of 5 datasets with the Logistic Regression base classifier, ALFA is an input-space method, yet the title, abstract, and framing consistently emphasize "latent feature augmentation." Whether the method's claimed advantages (linear decision hyperplane, controlled perturbation geometry) transfer to the input-space variant is left unexamined.

3. **CelebA setup underspecified.** The paper uses ResNet18 on CelebA but does not specify which attribute is the sensitive attribute (commonly "Male" in fairness studies), which attribute is the target Y, or the dataset split protocol. These are essential for reproducibility and for interpreting the CelebA results.

### Trivial

- Algorithm 1 is presented in a dense, hard-to-parse block.
- The notation in line 79 ($\bar{N}_{p}\,\approx\,\bar{4}\cdot\operatorname*{max}...$) contains apparent formatting artifacts.

---

## Nice-to-Haves

- Report numerical tables with accuracy, ΔDP, ΔEOd, and standard deviations for every dataset × classifier × baseline combination. Pareto frontiers can remain as visual complements.
- Include ablation studies isolating: (a) balanced upsampling only (no perturbation), (b) random perturbation in place of fairness-directed perturbation, (c) varying α (Sinkhorn weight), (d) varying λ.
- Report the specific hyperparameter values (α, ε, λ) used for each dataset/classifier configuration.
- Provide a quantitative analysis of the "rotation" mechanism: track per-subgroup error rates before and after fine-tuning, or measure how the decision boundary shifts.
- Clarify the CelebA experimental setup (sensitive attribute, target attribute, dataset split).
- Test whether differences between ALFA and baselines are statistically significant across the 10 runs.

---

## Removed Points

- **Criticism that the paper's theory "does not address the paper's central claim" (in its original strong form).** The abstract and contributions correctly scope the theory to the attack step ("we theoretically prove that our adversarial fairness objective assuredly generates biased feature perturbation"). The paper does not claim a theorem about fine-tuning improving fairness. The original framing exaggerated the mismatch. *Kept in weakened form as Minor weakness 1.*
- **Complaint that Algorithm 1 is poorly formatted / has OCR artifacts.** These are parser artifacts, not author errors. Removed per hard rules.
- **Strength Finder claim #5 about Sinkhorn distance being a strength.** This is a minor implementation choice (common in the optimal transport literature) rather than a distinctive contribution. Removed as generic.
- **"Missing related works" — not raised by any reviewer, but noted as excluded per hard rules.**
- **Harsh critic's "Strengthening the Paper on Its Own Terms" section items.** These are suggestions, not weaknesses; moved to Nice-to-Haves.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths (formal connection between attack objective and fairness metrics, interesting core idea, diagnosis of prior limitations) and weaknesses (missing quantitative evidence, no ablations, gap between theory and headline claim). The key synthesis-level observation is a structural one: the paper exhibits a disconnect between its theoretical apparatus and its main empirical thesis. The theory rigourously characterizes how the attack degrades fairness, but the paper's most striking claim — that fine-tuning on these attacks improves fairness — is supported only by intuition and a 2D synthetic visualization. The experimental section then fails to provide the quantitative evidence (tables, ablations) that would bridge this gap, leaving the central claim under-supported despite a promising conceptual foundation.

---

## Suggestions

1. **Add numerical tables.** This is the single most impactful change. Report accuracy, ΔDP, ΔEOd with standard deviations for every setting. Use the Pareto frontiers as *complements*, not replacements.
2. **Include ablations** that isolate the fairness-attack perturbation from balanced upsampling and fine-tuning. The simplest control is: train with balanced upsampling + random perturbation (same budget ε) instead of fairness-directed perturbation.
3. **Acknowledge the input-space variant** for logistic regression and discuss whether the latent-space framing's advantages still apply.
4. **Specify the CelebA setup** (sensitive attribute, target attribute, split).
5. **Report hyperparameter values** (α, ε, λ) per configuration — this is standard practice and essential for reproducibility.

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
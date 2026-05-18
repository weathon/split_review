Now I have thoroughly read and verified the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Discriminative Clipping (DC)-DPSGD, a method for handling heavy-tailed gradient noise in differentially private SGD. The core idea is to separate per-sample gradients into "body" and "tail" groups using a random projection subspace, then apply different clipping thresholds to each group to reduce clipping loss while controlling DP noise. The paper provides a convergence analysis (first high-probability bounds for heavy-tailed DPSGD under non-convex conditions, per the authors) and experiments on several datasets.

## Strengths

- **First high-probability convergence analysis for heavy-tailed DPSGD under non-convex conditions.** Theorem 1 provides a high-probability bound for classic DPSGD under sub-Weibull gradient noise, extending beyond prior sub-Gaussian assumptions. Table 1 contrasts this with existing expectation-only and high-probability SGD bounds, filling a gap identified in the related work (lines 56–59, 127–131). The paper explicitly discusses how this relates to prior DP results under heavy tails (Kamath et al. 2022, Lowy et al. 2023) in the convex setting, and correctly positions itself for the non-convex setting with sub-Weibull noise.

- **Novel discriminative clipping mechanism with provable reduction in heavy-tail dependence.** The subspace identification (Algorithm 1, Theorem 2) and dual clipping thresholds enable Theorem 3 (Uniform Bound) to reduce the heavy-tailed term from being present in the entire bound to being weighted by only a fraction \(p\) of gradients, with the \((1-p)\) fraction achieving a \(\log(\sqrt{T})\) dependence. The ablation study (Table 2) confirms that larger subspace dimension \(k\) and appropriate budget allocation improve accuracy, consistent with the theoretical error bound in Theorem 2.

- **Substantial accuracy gains on heavy-tailed datasets.** On CIFAR10-HT and ImageNette-HT, DC-DPSGD outperforms DPSGD, Auto-S, and DP-PSAC by up to 8.34%, 9.72%, and 9.55% respectively (Table 1), demonstrating that the approach translates into practical performance. These gains are especially notable on ImageNette-HT (33.70% vs. 25.36% for DPSGD), where heavy-tailed gradient noise is most severe.

- **Theoretically grounded guidance for clipping threshold selection.** Section 5.3 derives a concrete ratio \(c_1/c_2 \approx 10\) from the theoretical analysis (Theorem 3) and validates it with heatmaps (Figure 4), offering actionable hyperparameter recommendations grounded in the heavy-tail index \(\theta\).

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical justification for the subspace identification / classification step is incomplete.** Theorem 2 bounds the error between the empirical trace \(\lambda_{\mathrm{tr}}\) and its population counterpart (plus DP noise) for any single gradient. However, the method requires *ranking* all \(B\) gradients in a batch and selecting the top-\(p\) as heavy-tailed. The paper does not analyze whether the per-gradient trace error bound is sufficient to guarantee correct ordering, nor does it characterize the effect of misclassification (e.g., a body gradient mislabeled as tail, or vice versa) on the convergence bound or privacy guarantee. Theorem 3 simply assumes identification is correct with probability \(1-\delta'_m\) and weights the heavy- and light-tailed bounds by \(p\) and \(1-p\) as if classification were perfect. Without an analysis of misclassification, the theoretical link between the subspace identification mechanism and the claimed improvement is incomplete. The paper acknowledges the possibility of error (lines 268–269) but does not characterize its effect.

2. **The abstract states the main theoretical contribution in a misleading way.** The abstract claims the method "reduces the empirical gradient norm from \(\mathbb{O}(\log^{\max(0,\theta-1)}(T/\delta)\log^{2\theta}(\sqrt{T}))\) to \(\mathbb{O}(\log(\sqrt{T}))\)." However, Theorem 3 (the Uniform Bound) shows a weighted average: \(p\cdot\text{(heavy-tailed bound)} + (1-p)\cdot\text{(light-tailed bound)}\). The heavy-tailed \(\theta\)-dependent term does not disappear — it is merely confined to the \(p\)-weighted fraction. The remark after Theorem 3 clarifies this (lines 278–280), but the abstract and contribution list (line 48) omit the \(p\) weighting, creating a misleading impression of the result. This is fixable with rewording but as written it overstates the contribution.

### Minor

1. **Theorem 1 uses a circular condition on \(T\).** The statement reads "Suppose that \(T= \max{\big(m_2eB^2\log(1/\delta), \frac{n\epsilon}{\sqrt{d\log(1/\delta)}}\big)}\)" — treating \(T\) (the number of iterations, normally a free choice variable) as a function of the privacy parameters. This makes it unclear whether the bound is meaningful for a fixed computational budget. The remark (line 166) attempts to clarify by supposing \(\sqrt{T} = (n\epsilon)^{1/2}/\sqrt[4]{d\log(1/\delta)}\), but the theorem statement itself is confusing as written.

2. **Key quantities in the theorems are undefined or poorly defined.** \(\lambda_{\mathrm{max}} = \frac{\mu I(\lambda)}{\lambda} a K^2\) (line 250) uses \(I(\lambda)\) — introduced in line 244 as the tail rate function \(I(t)\) from \(\mathbb{P}(|x|>t)=\exp(-I(t))\) — but the specific evaluation \(I(\lambda)\) is not given a closed form. The constant \(\mu\) is introduced but never explained. While some of these may be standard in the heavy-tailed concentration literature cited (bakhshizadeh2023sharp), the paper should either define them or provide a clear reference within the text.

3. **The value of \(p\) (heavy-tailed ratio) is not reported in the experiments.** The algorithm takes \(p\) as an input parameter (Algorithm 1, line 222), and the theory assumes \(p \in [0.05, 0.1]\) (line 279, citing statistical properties). However, the experimental setup (lines 287–291) does not state what value of \(p\) was used for the reported results, nor does the ablation study vary \(p\). Without this information, readers cannot assess how sensitive the gains are to this parameter choice.

4. **Construction of the heavy-tailed datasets is not described.** The paper uses CIFAR10-HT and ImageNette-HT, citing cao2019learning and park2021influence, but does not describe how these datasets are constructed or why they are expected to induce heavy-tailed *gradient* noise. Since the method specifically targets gradient-level heavy tails, clarifying the dataset construction would strengthen the experimental validation.

### Trivial
- The orthogonalization procedure for the projection subspace vectors (Algorithm 1, line 229: "Extract orthogonal vectors \([v_1,...,v_k]\) from sub-Weibull distributions") is not specified beyond mentioning extraction. A brief note on how orthogonalization is performed (e.g., Gram–Schmidt) would improve reproducibility.

## Nice-to-Haves

- **A comparison with standard DPSGD using a larger fixed clipping threshold** (as suggested by prior heavy-tailed SGD work). This would help isolate whether the benefit comes from discriminative clipping specifically or simply from using a larger threshold for tail gradients.
- **A sensitivity analysis on \(p\)** (e.g., \(p \in \{0.05, 0.1, 0.15, 0.2\}\)) for at least one dataset, to assess practical difficulty of setting this parameter.
- **A discussion of the computational cost** of the subspace projection (computing traces for each gradient \(g_t(z_i)\) in a batch, lines 230–231), relative to baseline DPSGD.

## Removed Points

These points were flagged by the reviewer but are removed or downgraded after verification against the paper:

- **"Paper does not compare to Kamath et al. 2022 / Lowy et al. 2023"**: The paper *does* cite both works (line 58–59) and explicitly discusses that prior work focused on convex settings while the paper addresses non-convex settings with sub-Weibull noise. The distinction is valid and acknowledged. Table 1's comparison is against expectation-bounds from DPSGD works and high-probability bounds from non-private SGD — a different comparison axis. [Partially inaccurate criticism.]

- **"Privacy accounting claimed but not derived"**: Stating the privacy guarantee and citing the composition theorem is standard practice for conference papers. The claim that the method is \((\epsilon_{\mathrm{tr}}+\epsilon_{\mathrm{dp}},\delta)\)-DP via composition is plausible and follows standard DP composition. [Nitpick at the level expected of a conference submission.]

- **"Auto-S and DP-PSAC underperform because designed for light-tailed settings"**: This is expected and explains why the paper proposes a new method for heavy tails. It is not a weakness — the paper's contribution is precisely for settings where light-tailed methods struggle. [Not a weakness.]

- **"The paper does not discuss how the moments accountant is applied when noise for traces and gradients are on different scales"**: The paper states the privacy guarantee (Theorem, line 197–199) and allocates budget via composition (\(\epsilon = \epsilon_{\mathrm{tr}} + \epsilon_{\mathrm{dp}}\)). The moments accountant handles different noise scales through the composition theorem naturally. [Trivial — can be clarified in one sentence.]

## Novel Insights

None beyond the paper's own contributions. The reviews surface that the theoretical gap in the classification step (ranking vs. per-sample bound) is the paper's most significant weakness, but this is already partially noted by the authors (lines 268–269). The reviewers did not identify any hidden strength or overlooked implication not already stated in the paper.

## Suggestions

1. **Rewrite the abstract and contribution list** to accurately reflect the weighted-average nature of Theorem 3. E.g., "reduces the empirical gradient norm's dependence on the heavy-tail index \(\theta\) from \(\log^{\max(0,\theta-1)}(T/\delta)\log^{2\theta}(\sqrt{T})\) to just \(\log(\sqrt{T})\) for the \((1-p)\) fraction of gradients classified as light-bodied, while the \(p\) fraction retains the heavy-tailed rate."

2. **Provide a rigorous analysis of the classification step.** Either: (a) prove that the top-\(p\) by perturbed traces correctly identify heavy-tailed gradients with high probability under a gap condition on the true traces, or (b) characterize the effect of misclassification on the convergence bound and privacy guarantee (e.g., via a robustness argument).

3. **Report the value of \(p\) used in experiments** and ideally include a sensitivity analysis.

4. **Clarify the definitions** of \(I(\lambda)\), \(\mu\), and the \(T\) condition in Theorem 1. Restructure the convergence statements so that \(T\) is a free parameter satisfying a lower bound rather than being defined circularly.

## Score and Decision

The paper tackles a genuine problem (heavy-tailed gradients in DPSGD) with a novel approach and demonstrates meaningful empirical gains. However, the theoretical contribution is overclaimed in the abstract, and the central classification step lacks a rigorous justification linking the per-gradient trace bound to correct ranking and convergence under misclassification. These issues are addressable in revision but weaken the paper in its current form.

**Originality:** 7/10 — Novel combination of subspace identification and discriminative clipping is genuinely new.  
**Importance:** 7/10 — Heavy-tailed gradient noise in DPSGD is a real and under-studied problem.  
**Claims support:** 5/10 — The main theoretical claim is overstated; the classification step's justification is incomplete.  
**Soundness of experiments:** 6/10 — Gains are demonstrated but key parameters (\(p\), dataset construction) are undisclosed.  
**Clarity:** 5/10 — Theorems have undefined quantities; abstract is misleading.  
**Value to community:** 6/10 — If the theoretical gaps are filled, the approach could be practically useful.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
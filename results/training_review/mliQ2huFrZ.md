Now I have all the information I need. Let me produce the consolidated final review.

---

## Summary

This paper proposes a novel "class probability matching" (CPM) framework for label shift adaptation. Instead of matching distributions over the high-dimensional feature variable \(X\) (as done by KMM, LTF, etc.), CPM matches on the one-dimensional label variable \(Y\), reducing the matching problem to \(K\) equations. Theorem 3.1 proves equivalence with feature probability matching, so the same theoretical guarantees carry over. The resulting algorithm, CPMCN, uses BCTS-calibrated networks to estimate \(p(y|x)\) and solves a \(K\)-dimensional optimization via BFGS. On CIFAR100 under Dirichlet shift, CPMCN achieves the best MSE and accuracy across six comparisons, and its running time is orders of magnitude faster than feature-matching methods.

## Strengths

- **Novel and principled matching framework.** Matching on the label variable \(Y\) instead of the feature variable \(X\) is a genuine conceptual contribution. The derivation of Eq. (8) is mathematically sound under label shift, and Theorem 3.1 cleanly establishes equivalence with the existing feature-matching framework, inheriting its theoretical guarantees while dramatically reducing computational cost (from \(O(n_p^3)\) for KMM to \(O(n_q K^2)\) per iteration).

- **Computational advantage is real and well-demonstrated.** The complexity analysis is straightforward, and Figure 4 empirically confirms that CPMCN is orders of magnitude faster than feature-matching methods (KMM, LTF) while being comparable to or faster than prediction-matching methods (BBSL, RLLS) and EM. This directly addresses a known bottleneck in label shift adaptation.

- **Clear experimental evidence that calibration helps.** Figure 3 (ablation on CIFAR100, Dirichlet \(\alpha=10\)) shows that CPMCN without calibration performs substantially worse, while BCTS, VS, and NBVS all provide significant improvements in both ratio estimation and accuracy. This empirically validates the choice to integrate calibration, independent of any theoretical argument.

- **Strong results on the hardest benchmark.** On CIFAR100 (100 classes, the most challenging dataset), CPMCN achieves the lowest MSE_PROP, MSE_EVEN, and highest ACC across all tested Dirichlet shift severities (Table 1). The improvements are consistent and the experimental design (100 repetitions per setting) is thorough.

## Weaknesses

### Fatal
None.

### Major
- **Experimental evaluation incomplete in the main text.** The paper states it evaluates on MNIST, CIFAR10, and CIFAR100 (line 218), yet Table 1 (the only quantitative results table in the main text) contains results for CIFAR100 only. The text in lines 231–232 says "For all datasets, especially for the CIFAR100 dataset, Table 1, shows that..." — this is misleading because Table 1 does not contain results for MNIST or CIFAR10. Even if these appear in an appendix (stripped by the parser), the main text should include a summary table or at minimum explicitly reference where these results can be found. The central empirical claim of "outperforming existing methods" is only partially supported by the evidence presented in the main body.

### Minor
- **Theoretical justification for calibration reducing the bias term is imprecise.** The paper argues (Section 5, "Reduction of the Bias Error") that calibrated networks reduce the bias term \(\inf_{f\in\mathcal{F}}\mathcal{R}_p(f) - \mathcal{R}_p^*\) because they have "lower systematic bias and stronger approximation ability to \(p(y|x)\)." This conflates two distinct things: (a) the specific trained network's quality (which BCTS can improve by optimizing NLL on a validation set, mitigating overconfidence) and (b) the function class \(\mathcal{F}\)'s best-possible approximation error. The claim that calibration *reduces the bias term in the bound* as written is not rigorously justified — the bound itself is a valid mathematical statement, but the informal discussion overstates what it demonstrates. This does **not** invalidate the paper's core contributions (the CPM framework, the algorithm, the computational advantage, and the empirical results), but the theoretical framing should be tightened. The empirical evidence in Figure 3 independently supports the practical benefit of calibration.

- **Non-convex optimization without guarantees.** The objective in Eq. (11) is non-convex (the denominator is linear in \(w\)). The paper uses L-BFGS-B without analyzing convergence to a global optimum or the landscape of local minima. Theorem 5.3 guarantees uniqueness of the *population-level* solution but not of the empirical objective's stationary points. Figure 1 shows the objective decreasing to near zero on one setting, which provides some empirical validation but no systematic analysis (e.g., random restarts). This is a standard limitation in ML optimization but should be acknowledged.

- **Ad-hoc normalization of weights.** After solving Eq. (11), the paper normalizes \(\widehat{w}_k/(\sum_y \widehat{w}_y \widehat{p}(y))\) as the final estimate because the unconstrained solution may not satisfy \(\sum_y \widehat{w}_y \widehat{p}(y)=1\). This could be better handled by incorporating the constraint into the optimization (e.g., via reparameterization) or at minimum discussing why the two-step approach is justified.

### Trivial
- Lines 212–213 and 231 contain garbled superscript references ("3" appearing mid-sentence) — presumably footnote markers that the parser mangled, but they should be cleaned up.
- The "experimental results" subsection heading/substance is almost entirely image-referenced (Table 1, Figures 1–4 are inserted as images). The textual description of results beyond CIFAR100 Dirichlet is very sparse.

## Nice-to-Haves
- A summary table (or visual comparison plot) of the MNIST and CIFAR10 results in the main text. Even a single row per metric across datasets would bridge the gap.
- Random-restart experiments to probe the optimization landscape of Eq. (11) and confirm that L-BFGS-B reliably finds the global minimum.
- Reporting the source-domain cross-entropy/NLL of calibrated vs. uncalibrated networks on the validation set to directly support the "bias reduction" claim.
- A side-by-side bar plot of estimated \(\widehat{w}_y\) vs. true \(w^*\) for each method, to visualize systematic biases.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The theoretical justification for calibration is flawed and likely invalid"** (Harsh Critic, Critical Issue 1, first full paragraph). The reviewer claims calibration does not reduce cross-entropy risk and therefore cannot reduce the bias term. This is factually incorrect for held-out/validation data: BCTS optimizes NLL on a validation set and demonstrably improves probability estimates (overconfident networks have high NLL on held-out data). The reviewer's assertion that calibration "restricts the function class further" ignores that the calibrated class (BCTS layer on top of logits) contains the original network as a special case (\(T=1,\;b=0\)). The paper's discussion is *imprecise* (as noted in Minor weaknesses above) but not "invalid" — the empirical evidence in Figure 3 independently supports that calibration helps. **Demoted from "fatal/invalidates core claim" to a minor weakness about imprecise framing.**

2. **"This invalidates the paper's central theoretical message"** (same paragraph). The paper's central theoretical message is the CPM framework (matching on \(Y\) with equivalence to feature matching). The calibration discussion is secondary — even if removed entirely, the CPM framework, Theorems 3.1 and 5.3, computational advantage, and empirical results on CIFAR100 would still stand as contributions. **Overstated severity — removed.**

3. **"The paper should not be accepted in its current form"** (Overall Assessment, last paragraph). This is a reviewer's bottom-line judgment, not a weakness. The format requires a score/decision at the end; I synthesize my own bottom-line.

4. **"Strength: Comprehensive theoretical guarantees with clear justification of calibration benefits"** (Strength Finder, strength #2). This conflicts with the verified weakness that the calibration justification is imprecise. **Dropped.**

## Novel Insights

The most interesting observation from the reviews that goes beyond the paper's own claims is the tension between the paper's theoretical framing and its actual evidence. The paper tries to argue theoretically that calibration reduces the bias term in the estimation error bound (Section 5), but this argument is structurally weak because the bound depends on the function class \(\mathcal{F}\) while calibration is applied to a *specific trained network*. What the paper actually demonstrates — and what is genuinely valuable — is that calibrated probability estimates serve as better inputs to the CPM matching objective Eq. (8), because the objective directly uses \(\widehat{p}(y|X_i)\) values. This is a practical insight grounded in the specific structure of the CPM framework (the matching equations depend pointwise on the estimated probabilities), not a general theoretical claim about function classes. Reframing the calibration discussion around this operational benefit (rather than VC-dimension bound arguments) would be both more honest and more compelling.

## Suggestions

1. **Main text: add a summary table across datasets.** Create a compact table (perhaps supplementary with a main-text reference) that reports MSE_PROP, MSE_EVEN, and ACC for MNIST, CIFAR10, and CIFAR100 under at least one shift severity. This directly addresses the most serious weakness.

2. **Revise Section 5's "Reduction of the Bias Error" discussion.** Either (a) provide a rigorous argument that the function class of calibrated networks contains the original network class (so \(\inf_{\mathcal{F}_\text{cal}} \mathcal{R}_p \le \inf_{\mathcal{F}_\text{orig}} \mathcal{R}_p\)) and thus the bias term cannot increase, or (b) reframe the discussion to honestly note that the bound only parses the error into bias and variance terms, and the empirical evidence (Figure 3) is what substantiates the benefit of calibration.

3. **Acknowledge the non-convexity concern** and provide random-restart experiments to show that L-BFGS-B consistently finds the same solution across different initializations.

## Score and Decision

The paper makes a genuine contribution: the class probability matching framework is novel, theoretically grounded (Theorem 3.1), and practically beneficial (computational efficiency + strong CIFAR100 results). The main weaknesses are an incomplete experimental presentation in the main text and imprecise theoretical framing of the calibration benefit. Neither is fatal — the CPM framework does not depend on a rigorous calibration theory, and the missing results are assumed to exist in the appendix. With a compact summary table and tightened theoretical discussion, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
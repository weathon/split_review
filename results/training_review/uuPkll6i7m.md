Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me construct the final consolidated review.

## Summary
This paper introduces the notion of "certified calibration" for classifiers with certified predictions (via randomized smoothing). It makes three main contributions: (1) demonstrating that adversarial attacks can severely degrade calibration even on robust models (Table 1), (2) proposing two worst-case calibration metrics — the Certified Brier Score (CBS), which has a tight closed-form upper bound (Theorem 1), and the Approximate Certified Calibration Error (ACCE), obtained by solving a mixed-integer program with ADMM, and (3) Adversarial Calibration Training (ACT), which fine-tunes models to improve certified calibration without sacrificing certified accuracy. The CBS is a genuine certificate; the ACCE is an approximation, as explicitly acknowledged throughout the paper.

## Strengths

- **Demonstrates that calibration is severely harmed by attacks, even on certified/robust models**: Table 1 shows concretely that attacks can drive AdaECE from 3.70% to 47.23% on ImageNet (ST) and from 9.03% to 13.54% on adversarially trained models while leaving accuracy unchanged. This establishes a clear and practically relevant motivation for the work.

- **Provides an analytic, closed-form upper bound for the Certified Brier Score (CBS)**: Theorem 1 gives a tight, computable expression (Eq. 4) that depends only on per-sample correctness and the certificate bounds on confidence. This is a clean theoretical contribution that delivers a genuine certificate, not an approximation.

- **Introduces a mixed-integer programming reformulation for the Certified Calibration Error and an ADMM solver that yields tighter bounds than baselines**: The MIP (Eq. 10) jointly optimizes bin assignments and confidence values. Figure 3 shows ADMM uniformly yields higher ACCE than both dECE and Brier-confidence baselines, often by ≈0.2, supporting the claim that the solver effectively approximates the worst-case ECE better than existing alternatives.

- **Adversarial Calibration Training (ACT) improves certified calibration without harming certified accuracy**: Table 2 shows that at certified radius 1.0 on CIFAR-10, ACCE-ACT reduces ACCE from 56.36% (AT baseline) to 47.08% and CBS from 36.25% to 24.87%, while all models stay within 3% of the best certified accuracy. This is a strong qualitative improvement and demonstrates the practical value of the proposed framework.

- **Comprehensive empirical setup**: Experiments span CIFAR-10 (ResNet-110) and ImageNet (ResNet-50), multiple smoothing σ values, certified radii from 0.05 to 3.0, and both equal-width and equal-count binning schemes. This breadth strengthens the generality of the findings.

- **Clear and well-organized exposition**: The paper is logically structured, carefully defines its notation, and motivates each technical component clearly.

## Weaknesses

### Fatal
None.

### Major
- **Lack of statistical rigor (no error bars, single runs reported)**: The experimental results (Table 2, Figure 4) are reported without error bars, confidence intervals, or indication of multiple independent runs. Given the computational cost of randomized smoothing training, single runs are understandable but still limit confidence in the reported improvements. The reductions in ACCE (e.g., 56.36% → 47.08%) may be real, but without variance estimates the reader cannot assess significance. This is the paper's most significant evidential weakness.

- **No ground-truth validation of ADMM's optimality gap**: The ACCE is compared against other *approximate* baselines (dECE, Brier confidences), but never validated against the true CCE optimum, e.g., via brute-force enumeration or an exact MIP solver (Gurobi/SCIP) on a small subset (N=50). ADMM for a non-convex MIP is not guaranteed to find the global optimum, and the paper reports no optimality gap. Without such validation, the reader cannot assess whether ADMM's solutions are close to the true CCE or whether a better solver would yield substantially different numbers.

### Minor
- **Probabilistic compounding in the certificate framework is not discussed**: The confidence certificates (*l, u*) from randomized smoothing hold with probability ≥ 1−α per sample (α=0.001 is used). Theorem 1 and the MIP formulation treat these bounds as deterministic. The joint probability that all N confidence certificates hold simultaneously is (1−α)^N, which for N=2000 (used in ACCE experiments) is approximately 0.135 — substantially less than 1. This does not invalidate the framework (it is standard practice in the randomized smoothing literature), but the paper should at minimum acknowledge this compounding and discuss its implications for the reliability of the overall calibration certificates.

- **Marginal ImageNet results limit the generality of ACT findings**: The paper honestly notes that ImageNet results show only 1–2% improvement. While it correctly observes that prior calibration work often does not report ImageNet, this significantly weakens the claim that ACT broadly improves certified calibration, especially for practitioners working at scale.

- **"dECE" is not explained in the main text**: The paper compares against "dECE" (Figure 3 caption, line 256) without defining it. The reader must infer from the related work (Section 6) that it refers to the differentiable ECE of Bohdal et al. (2023, cited). A one-sentence definition in Section 5.2 would improve clarity.

### Trivial
- The paper sometimes uses "certified calibration" as an umbrella term encompassing both the genuinely certified CBS and the approximate ACCE. While the paper consistently qualifies the ACCE as "approximate" (abstract, line 27, line 142, line 271), the overarching nomenclature could give a casual reader the impression that both metrics are fully certified. A small clarification in the introduction would help.

## Nice-to-Haves
- **Ground-truth validation of ADMM**: Evaluate ADMM's optimality gap on a small subset (e.g., N=50) where the true CCE can be computed via exhaustive search or an exact MIP solver. This would greatly strengthen the ACCE contribution.
- **Multiple independent runs**: Repeat ACT fine-tuning 3+ times with different seeds and report means/standard deviations for ACCE, CBS, and certified accuracy.
- **Reliability diagrams or visualizations showing how worst-case confidence bounds translate into bin-level calibration error** would help build intuition.
- **Discussion of how to adjust for multiple testing** (e.g., Bonferroni correction) or a combined probabilistic bound for the overall calibration certificate would strengthen the theoretical framing.

## Removed Points
1. **"The ACCE is not a certificate — this undermines the paper's central claim"** (Harsh Critic Issue 1): The paper explicitly and repeatedly calls the ACCE an "approximate" bound (abstract: "approximate bounds"; line 142: "empirical, approximate certificate"; line 27: "approximate certified calibration error"; title: "Towards Certification"). The reviewer's criticism that the paper presents ACCE as a true certificate without qualification is a misreading — the paper already addresses this. The CBS, by contrast, is a genuine closed-form certificate. Removed as strawman.

2. **"No comparison to post-hoc calibration methods (temperature scaling, Platt scaling)"**: Applying post-hoc calibration to certified models would change the model's output distribution and invalidate the existing certificates on predictions and confidences. The paper's setup assumes fixed certificates; comparing against methods that break those certificates is outside scope.

3. **"Post-hoc filter [within 3% of highest certified accuracy] could bias results"**: This is a standard way to control for accuracy when comparing calibration, and the paper is transparent about it (Table 2 caption). If anything, it is a conservative choice that prevents cherry-picking models with degraded accuracy.

4. **"3.4% slower claim is suspect"**: The paper explains that ADMM primal/dual updates are cheap relative to backpropagating through the network. The reviewer provides no evidence to doubt this claim.

5. **"Does not evaluate how close ADMM comes to the true optimum even on small datasets"**: This is kept as a **Major** weakness (merged into the ground-truth validation point above) rather than removed, because while the paper acknowledges ACCE is approximate, it does not quantify the optimality gap. The point is valid but is restated more precisely in the Major weaknesses section.

6. Various generic strengths from the Strength Finder that lack specific content or conflict with verified weaknesses are dropped (e.g., generic statements about addressing important problems without specifics).

## Novel Insights
Beyond the paper's own contributions, the reviews surface an important structural observation about the limits of the proposed framework: the "certified calibration" umbrella combines a genuine closed-form certificate (CBS) with an optimization-based approximation (ACCE) whose solution quality is unvalidated, and the entire edifice rests on per-sample confidence certificates that are themselves probabilistic. These two layers of approximation — ADMM's unknown optimality gap multiplied by the unexamined joint failure probability (1−α)^N of the randomized smoothing certificates — mean that the practical reliability of the calibration guarantees is weaker than the "certified" language might suggest. Future work could address this by either developing deterministic certification methods (e.g., interval bound propagation) or by providing rigorous combined probabilistic bounds.

## Suggestions
1. Add error bars / multiple-seed runs to the main experimental results (Table 2, Figure 4).
2. Validate ADMM's optimality gap against an exact solver on a small subset (N=50–100) to quantify approximation quality.
3. Acknowledge and discuss the probabilistic compounding of the randomized smoothing confidence certificates, and provide guidance on how practitioners should interpret the resulting calibration guarantees.
4. Define "dECE" explicitly when first used in Section 5.2.
5. Consider slightly softening the title's "Certification" framing or adding a sentence to the introduction clarifying that the CBS is fully certified while the ACCE is an approximation, to avoid any potential misinterpretation.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
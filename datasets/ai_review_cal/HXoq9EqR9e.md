- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have all the verification I need. Let me write the consolidated review.

## Summary

This paper proposes FairerCLIP, a method to debias CLIP's zero-shot predictions by learning transformations of image and text features in reproducing kernel Hilbert spaces (RKHSs). The objective jointly maximizes dependence on the target attribute, minimizes dependence on a sensitive attribute, and maintains cross-modal alignment. The optimization alternates between closed-form generalized eigenvalue solves, yielding fast training. Experiments cover spurious correlations (Waterbirds, CelebA), intrinsic dependencies (CelebA high cheekbones/sex), and fairness (FairFace, CFD), comparing against several recent baselines.

## Strengths

- **Flexibility across bias types and label scenarios**: FairerCLIP is demonstrated on both spurious-correlation and intrinsic-dependency settings, and in both supervised and unsupervised modes, while prior methods specialize to one scenario. Table 1 (CelebA intrinsic) shows EOD of 0.02%/0.005% for two CLIP backbones, far below Contrastive Adapter's 1.0%/6.3%. Table 2 shows competitive or best worst-group accuracy across Waterbirds and CelebA in both label settings. Table 3 (FairFace) shows the lowest MaxSkew@1000 for sex and race across two backbones.

- **Computational efficiency**: Table 5 (runtime) shows 32 seconds on Waterbirds and 222 seconds on CelebA — 4–10× faster than most baselines and 37–93× faster than Contrastive Adapter. This is enabled by the closed-form generalized eigenvalue solution.

- **Sample efficiency under data limitation**: On CFD (597 samples, challenging zero-shot separation), Figure 2 shows FairerCLIP achieves worst-group accuracy ~55% and gap 21.8%, while all baselines nearly fail (worst-group ~10–20%, gaps 40–55%).

- **Ablation validates each objective component**: Table 4 systematically ablates the Dep(Z,Y) term (dropping WG by 14.5 points on spurious, EOD rising to 6.4% on intrinsic), the Dep(Z_I,Z_T) term (EOD rising to 0.2%), and the iterative pseudo-label update (WG dropping from 86.1% to 81.1%). These controlled experiments isolate the contribution of each term.

- **Theoretically grounded alternating optimization**: Theorem 1 derives the solution as a generalized eigenvalue problem with closed-form iterates. The proof follows from trace optimization, providing a principled foundation for the efficiency and stability claims.

## Weaknesses

### Fatal

None.

### Major

- **Missing variance for the headline intrinsic-dependency result (Table 1)**: Table 1 reports EOD values of 0.02% (ResNet-50) and 0.005% (ViT-L/14) without any standard deviations, confidence intervals, or run-to-run variation. Every other results table (Tables 2, 4) includes ± ranges. This is problematic because: (a) these near-zero EOD values are the paper's most striking claim; (b) the target (high cheekbones) and sensitive (sex) attributes are correlated in the population, creating an inherent accuracy–fairness trade-off that makes near-perfect EOD surprising; and (c) without variance, the reader cannot assess whether this is a robust finding or an artifact of a specific hyperparameter choice or seed. The authors should either provide error bars over multiple runs or explain why they cannot for this particular experiment.

- **Pseudo-labeled sensitive attribute S is unaudited**: In the "w/o labels" setting, the method relies on CLIP's zero-shot predictions for both Y and S. The objective uses a term –τ Dep(Z,S) to penalize dependence on S; if the pseudo-labeled S is noisy or itself biased, this term mis-specifies the debiasing objective. The paper does not report the accuracy of zero-shot S predictions on any dataset, does not ablate robustness to noise in S (e.g., by corrupting known S labels at varying rates), and does not analyze settings where CLIP's S predictions are poor (the CFD experiment notes S is hard to predict but does not quantify this). Since the unsupervised mode is a key selling point, this gap weakens confidence in the method's practical reliability.

### Minor

- **Ablation study conducted on only a single dataset (CelebA)**: The main-paper ablation (Table 4) covers CelebA for both spurious (blonde hair) and intrinsic (high cheekbones) settings. While the appendix likely contains additional ablations (the paper cites \cref{sec:app:abl}), showing component analysis on at least a second dataset like Waterbirds would strengthen the claim that the contributions of Dep(Z,Y) and Dep(Z_I,Z_T) are universal. This is a scope limitation of the main paper, not a fatal flaw.

- **Inconsistency between Table 1 and the main text for the ResNet-50 EOD value**: The table reports EOD = 0.02 for CLIP ResNet-50, while the text (paragraph after Table 1) states "0.002%." These differ by a factor of 10. The authors should clarify which value is correct.

- **Weaker performance on CLIP ResNet-50 in the supervised setting**: In Table 2 (w/ labels, CLIP ResNet-50), FairerCLIP achieves WG 75.4 vs 82.5 for Contrastive Adapter. The paper attributes this to ResNet-50 features containing less target information (citing the appendix), which is a plausible explanation, but the main paper provides no direct evidence for this claim. Adding a brief quantitative justification (e.g., the mutual information estimates referenced in the appendix) would strengthen the discussion.

### Trivial

None.

## Nice-to-Haves

- **State the number of RFF dimensions used in each experiment.** The paper notes RFF is used to scale kernel computation but defers all implementation details to the appendix. Explicitly stating the RFF dimension (and the number of iterations for the alternating optimization) in the main paper would aid reproducibility.
- **Briefly discuss the computational complexity in terms of RFF dimensions.** The paper notes O(n³) for full kernel matrices; with RFF the complexity is O(n·d_rff² + d_rff³). Stating this explicitly would be helpful.
- **Clarify why the regularization term γ in Eq. (6) prevents degenerate solutions** when the matrix on the left-hand side of the generalized eigenvalue problem may become indefinite due to the subtraction of τ Dep(Z,S).

## Removed Points

These points were flagged by reviewers but are not included as weaknesses in the main review for the reasons below:

- "Orth-Cali omitted from runtime table" — REMOVED. Orth-Cali is a one-shot projection method that requires no training; omitting it from a training-time comparison table is appropriate and the critic acknowledges this.
- "RFF dimensions not specified in main paper" — REMOVED per policy (deferred to appendix which is stripped by parser; standard practice).
- "Missing related works" — REMOVED per policy (no external sources to verify omissions).
- "Negative eigenvalues in generalized eigenvalue problem" — REMOVED. This is a known property of trace-ratio generalized eigenvalue problems with indefinite matrices; the regularization term γI mitigates this. The critic's own analysis acknowledges the formulation is sound. This is a presentation suggestion at best, already captured in Nice-to-Haves.
- "Geometric illustration lacks formal rigor" — REMOVED. It is explicitly described as a pedagogical illustration, not a formal proof. The paper does not claim it as evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the importance of the variance issue on Table 1 and the pseudo-label audit gap, but these are standard methodological concerns rather than novel observations about the work.

## Suggestions

1. **Report error bars for Table 1** (intrinsic dependency experiment). Multiple random seeds, different train/validation splits, or a bootstrap analysis would suffice. If the near-zero EOD is robust, this strengthens the paper; if it varies, the authors should report the range honestly and discuss the trade-off.
2. **Perform a sensitivity analysis on the pseudo-labeled S.** Simulate corrupted S labels at varying flip rates (e.g., 0%, 10%, 20%, 30%) and measure the impact on EOD and accuracy. Report the accuracy of CLIP's zero-shot S predictions on each dataset so readers can calibrate their expectations.
3. **Resolve the text/table discrepancy** for the ResNet-50 EOD value (0.02 vs 0.002).
4. **Add at least one ablation result on Waterbirds** to the main paper (or move a key appendix ablation to the main text) to support the claim that the component contributions generalize beyond CelebA.

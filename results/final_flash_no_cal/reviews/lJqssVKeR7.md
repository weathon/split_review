Now I have thoroughly read the paper and cross-referenced the reviews against the actual content. Let me synthesize the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes HiSo, a Hessian-informed zeroth-order federated optimization method that learns a diagonal preconditioner without requiring additional communication beyond the existing scalar-only framework of DeComFL. It provides convergence theory showing dimension-free rates under well-approximated Hessian assumptions, and demonstrates 1.4–5.4× speedups over DeComFL across multiple LLM fine-tuning tasks.

## Strengths

**1. Novel algorithm design that learns a diagonal preconditioner within the scalar-only communication constraint.** The paper's core algorithmic contribution is showing that the update Δx (which is available "for free" from the scalar-only reconstruction process) can be repurposed to maintain a running diagonal preconditioner H via Eq. (12), and that this H can then be used to precondition subsequent ZO gradient estimates (Eq. 8–10). This clever reuse of already-available information to obtain a Hessian-inspired preconditioner without any extra communication is a genuine algorithmic insight.

**2. Strong empirical acceleration over the state-of-the-art ZO-FL baseline.** Table 2 reports 1.4–5.4× speedups over DeComFL across OPT-350M, OPT-1.3B, and OPT-2.7B on SST-2, QQP, and SQuAD, with corresponding communication savings of 29%–80%. Table 3 shows HiSo consistently achieves the highest test accuracy among all ZO baselines (FedZO, DeComFL) while maintaining the lowest communication cost. These results are clean and consistent.

**3. Convergence guarantees that extend to multiple local updates (τ > 1).** Corollary 3 provides a convergence rate for HiSo with τ > 1 that remains independent of d and L under the well-approximated condition, whereas the paper demonstrates that DeComFL's rate becomes d-dependent in this setting. Resolving this gap is a genuine theoretical advance over the prior state-of-the-art analysis.

**4. Robustness to the Hessian smoothing hyperparameter ν.** Figure 5 shows that varying ν across {0.9, 0.95, 0.99} has negligible impact on convergence speed or final accuracy, which is valuable for practical deployment.

**5. Tighter variance analysis via effective rank and whitening.** Section 5.1 and Table 1 formalize how the whitening process (ζ = Tr(H^{-1/2}ΣH^{-1/2})) can be much smaller than Ld or even Lκ, providing a principled theoretical motivation for why Hessian-informed ZO can break the dimension-dependent barrier.

## Weaknesses

### Fatal
None.

### Major

**1. The "Hessian-informed" framing overstates what is actually established about the learned H.** The paper's central branding—"Hessian-informed," "curvature information," "global diagonal Hessian approximation"—implies that the learned H (Eq. 12) meaningfully approximates the true Hessian diagonal. In fact, H is updated via an RMSProp-style moving average of |Δx|², where Δx = g·H^{-1/2}u already depends on H itself. No argument is given—either formally or empirically—that this H converges to or correlates with the diagonal of ∇²f. The paper acknowledges this indirectly in footnote 1 ("does not imply that we calculate the full Hessian matrix") and in Section 5.2's Remarks, but the abstract, introduction, and contributions list repeatedly use "Hessian-informed" and "curvature information" without this caveat. The method's empirical success is not in question, but the gap between the name and the evidence is significant. A direct verification (e.g., computing the true Hessian diagonal on a small CNN and comparing it with the learned H) would substantially strengthen the paper.

**2. The cleanest theoretical rates (Corollary 1's O(√(ζ/mR)) independent of d and L) rely on two unverified conditions working simultaneously.** The well-approximated condition (Definition, Eq. 17) requires that Tr(H^{-1/2}ΣH^{-1/2}) ≤ ζ with ζ independent of d. The paper does not verify this condition for the H actually produced by HiSo on any real model. The only evidence is a synthetic log-normal simulation (Fig. 4) and a long-tail histogram of H entries (Fig. 5). Neither demonstrates that ζ is small on real tasks. Moreover, even under the well-approximated condition, the d-independent rate O(√(ζ/mR)) additionally requires the low-effective-rank property. Theorem 1 itself is unconditional and valid, but the paper's most headline-friendly rate rests on a stack of assumptions whose satisfaction is unconfirmed. The Remarks in Section 5.2 are transparent about this ("Although it is hard to determine if this approximation holds"), but this transparency does not reduce the gap between the advertised claim and what is actually proven.

**3. The "first such result for ZO methods in FL" claim is overstated.** DeComFL already achieved a dimension-independent rate O(√(Lκ/mR)) under the low-effective-rank assumption. HiSo's theoretical advantage is removing the L-dependence, yielding O(√(ζ/mR)). This is incremental, and obtaining it requires the additional well-approximated condition that DeComFL does not need. The paper's phrasing ("marking the first such result for ZO methods in FL") suggests a more dramatic breakthrough. Qualifying the novelty against DeComFL more precisely would improve accuracy.

**4. The "generalized scalar-only communication framework" (Algorithm 1) contribution is minor.** Algorithm 1 is essentially the DeComFL protocol with a generic placeholder Δx in place of the ZO-SGD update. The core mechanism (scalar × direction-from-seed) is unchanged from Li et al. (2025b). The observation that the framework can support algorithms beyond ZO-SGD is correct but follows directly from the fact that any update representable as scalar × fixed-direction can be plugged in. Presenting this as a separate contribution inflates what is a straightforward generalization.

### Minor

**1. The communication cost numbers in Tables 2 and 3 serve different purposes but the relationship between them is unclear.** Table 2 reports HiSo's cost at the point it matches DeComFL's best accuracy (29.30 KB for OPT-1.3B QQP), while Table 3 reports cost "until convergence" (96.67 KB for the same setting). These are not contradictory—they measure different stopping criteria—but the paper does not explain why they differ roughly by a factor of three. Clarifying the total training budget used for Table 3 (or adding a note about convergence criteria) would resolve any confusion.

**2. Missing wall-clock time and computation overhead analysis.** The paper claims communication savings as its main practical benefit, but does not report training time. The additional per-step computation (matrix-vector product with H^{-1/2} and the Hessian update) introduces non-negligible overhead, especially on client devices. The paper mentions that Appendix E includes "computation time" analysis, but the main text would benefit from a brief summary of this overhead.

**3. No ablation isolating the effect of the learned H from adaptive scaling more generally.** The natural control experiment would compare HiSo against (a) DeComFL, (b) HiSo with a fixed (non-adaptive) diagonal preconditioner, and (c) a variant that uses RMSProp-style scaling on the ZO gradient before preconditioning. Such an ablation would disentangle whether HiSo's gains come from Hessian-informed curvature adaptation or simply from per-coordinate scaling. The paper acknowledges the resemblance to RMSProp (footnote 2) but does not run this comparison.

**4. Limited hyperparameter analysis.** Only ν is ablated. The smoothing parameter μ and learning rate η are mentioned as tuned, but no sensitivity analysis is provided. The interaction between η and the magnitude of H could be important for reproducibility.

### Trivial

- The notation in Theorem 1 (ρ̄, φ̄) is dense and their interpretation as "sum of whitening Hessian eigenvalues" and "sum of approximate Hessian eigenvalues" is rough; a clearer intuitive explanation would help readers.
- Some figures (Fig. 1, Fig. 2) have low-resolution rendering and are hard to parse.

## Nice-to-Haves

- Compare against a ZO variant of RMSProp or Adam within the same scalar-only communication framework to isolate the effect of Hessian approximation from adaptive scaling.
- Measure the whitened trace Tr(H^{-1/2}ΣH^{-1/2}) on a small model (e.g., the CNN from Section 6) to empirically probe the well-approximated condition.
- Include convergence curves for the LLM experiments in the main paper (not just the appendix), to complement the round-to-match-DeComFL metric in Table 2.
- Study the effect of local update steps τ on HiSo vs. DeComFL empirically.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim about "inconsistent communication cost numbers" being contradictory:** The critic asserted that Table 2 (29.30 KB) and Table 3 (96.67 KB) for OPT-1.3B QQP are contradictory. However, Table 2 explicitly states it measures HiSo's rounds/cost to match DeComFL's best accuracy, while Table 3 reports total communication "until convergence." These are different stopping criteria, not an error. The paper could be clearer about the relationship, but the numbers are not inconsistent.
- **Harsh critic's claim that ZO-Adam variants should be baselines:** Standard ZO-Adam requires transmitting full d-dimensional momentum/adaptive states, which is outside the scalar-only communication constraint. The critic's suggestion is not directly applicable given the paper's core constraint. A ZO-RMSProp variant within the framework would be possible but the absence is not a flaw in the paper's evaluation.
- **Strength finder's claim about "first dimension-independent convergence rate for ZO-FL":** The strength finder presents this without qualification, but DeComFL already had d-independent rates. The novelty is removing L-dependence at the cost of an additional assumption. This point is retained in Weaknesses as Major issue #3 with appropriate nuance.
- **Strength finder's claim about "empirical confirmation of low-effective-rank structure":** The long-tail histogram (Fig. 5) shows the distribution of H values, not the Hessian eigenvalues. While suggestive, this is indirect evidence at best. Demoted to supporting point only.

## Novel Insights

The most interesting insight emerging from the reviews—beyond what the paper itself already states—is the tension between the paper's two core claims. The paper simultaneously argues that (a) the learned H captures meaningful curvature information (the "Hessian-informed" claim), and that (b) even if H is a poor Hessian approximation, performance merely degrades to DeComFL (the fallback guarantee in the Remarks). These two claims pull in opposite directions: if the fallback guarantee is what makes the method safe, then the Hessian-informed framing is less essential to the contribution than the paper suggests. Conversely, if the Hessian information is what drives the speedups, then the lack of direct verification is a meaningful gap. The paper would be strengthened by explicitly addressing this tension—for example, by reporting how much of the speedup survives when H is replaced by a fixed or random diagonal preconditioner.

## Suggestions

1. **Temper the "Hessian-informed" framing** to match what is actually shown. "Adaptive diagonal preconditioning" or "RMSProp-inspired ZO-FL" would be more accurate. If the "Hessian-informed" label is retained, include a direct empirical comparison (e.g., on the CNN) between the learned H and the true Hessian diagonal.
2. **Add an ablation** comparing HiSo against (a) DeComFL, (b) a version with fixed H, and (c) a ZO-RMSProp variant within the scalar-only framework.
3. **Clarify the stopping criteria** underlying Tables 2 and 3, including the total number of rounds run for the "until convergence" measurements.
4. **Report wall-clock time** (even briefly) to quantify the computational overhead of the preconditioning step.
5. **Soften the "first such result" claim** in the contributions to accurately reflect the incremental nature over DeComFL, e.g., "the first ZO-FL convergence rate independent of both d and L (under a well-approximated Hessian assumption)."

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
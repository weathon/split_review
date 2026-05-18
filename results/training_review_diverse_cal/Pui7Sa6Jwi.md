Now I have all the information needed for a thorough, verified review. Let me construct the final synthesis.

## Summary

This paper addresses distraction-robust representation learning for visual offline RL. It formalizes the problem as an ExoPOMDP and identifies that standard latent dynamics objectives (e.g., SLAC) can retain "superfluous information" from distractions. The authors propose CLEAR, which learns disentangled agent-centric (ŝ) and exogenous (ê) representations via separate encoders, and uses an inverse-dynamics regularizer (with a min-max term to suppress action-predictiveness in ê) to ensure the state representation captures only controllable factors. Empirically, CLEAR achieves strong results on DMC benchmarks with various distractions (static, video, multi-agent), particularly on the hardest 2×2 Grid setting, with qualitative evidence of successful disentanglement.

## Strengths

1. **Clear formalization and problem identification.** The paper rigorously casts visual offline RL as an ExoPOMDP and uses an information-theoretic decomposition (Eq. 2) to show that previous latent-dynamics objectives (e.g., SLAC) contain no mechanism to suppress superfluous information from distractions. This provides a clean, theoretically motivated diagnosis of why standard approaches fail under visual distractions.

2. **Strong empirical results, especially on the hardest distractions.** CLEAR achieves the highest or near-highest normalized scores across environments and distraction types (Table 1). On the hardest 2×2 Grid setting, CLEAR maintains performance close to the Clean baseline on Walker (102.7 vs 100.0) and Cheetah (83.5 vs 92.6), while nearly all baselines collapse (next best on Walker 2×2: ACRO at 69.4). This directly supports the claim that CLEAR learns representations that are largely distraction-free.

3. **Ablation study convincingly shows the regularizer is essential.** Table 3 and Figure 5 demonstrate that without the inverse-dynamics regularization, CLEAR's objective alone (J_ELBO) converges to qualitatively different local optima across seeds — "desired," "flipped," and "degenerate" solutions — with dramatically different RL scores (95.5, 38.2, 59.6). The full regularizer stabilizes training toward the desired disentanglement.

4. **Qualitative evidence supports the claimed disentanglement.** Figure 4 shows that CLEAR's mask-based decoder assigns the controllable agent to the Ŝ channel and background/distractions to the Ê channel, including on the 2×2 Grid where it correctly identifies the top-left agent as controllable. Table 2 confirms CLEAR's Ŝ has low MSE for ground-truth state regression across all distractions.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core contributions — the ExoPOMDP formalization, the problem diagnosis, the proposed method, and the empirical validation — are all sound. The weaknesses below are addressable and do not undermine the central claims.

### Minor

1. **The theoretical framing slightly overstates the formal guarantee.** The paper motivates the need for disentanglement via Eq. 2, which decomposes predictive information w.r.t. the *unobserved* ground-truth state S_t, and then pivots to a different objective (Eq. 3–4) built on learned representations. The paper explicitly acknowledges that the superfluous-information term in Eq. 2 "is conditioned on S_t which is unobservable and thus cannot be computed nor minimized directly" (line 61), so no formal link between the two formulations is established. The paper calls CLEAR "principled" and "consistent with the underlying ExoPOMDP," which is a reasonable description of a method *designed around* the ExoPOMDP structure, but it is not a provable guarantee that the specific superfluous information from Eq. 2 is eliminated. This gap between the formal motivation and the implemented objective is acknowledged by the authors themselves but weakens the strength of the theoretical claims.

2. **The min-max optimization for minimizing I(A_t; Ê_t, Ê_{t+1}) lacks analysis.** Equation 7 proposes an adversarial scheme (maximize then minimize a predictor's log-likelihood) to drive action-predictiveness out of the exogenous representation. The paper provides no discussion of convergence, no sensitivity analysis to learning rates or alternation schedules, and no empirical characterization of the min-max dynamics. The ablation shows the regularization helps overall, but the stability and robustness of this specific adversarial component are unexamined. This is not fatal — the empirical results show the method works — but it leaves a practical question open.

3. **Some empirical claims are slightly stronger than the data warrants.** The abstract says CLEAR "perform[s] consistently well across these distractions," but on Cheetah with Multiple Videos the score drops to 72.0 (vs 92.6 Clean, SE ±5.7), and on Hopper CLEAR is not always the top performer (InfoGating and ACRO match or exceed it on several distraction levels, with standard errors up to ±9.5). The paper honestly acknowledges these caveats (lines 177, 185), so this is a mild calibration issue rather than a misrepresentation. Additionally, the claim that CLEAR is "the only latent dynamics method that can consistently remove superfluous information" (line 167) is accurate when read in context (latent-dynamics methods only, which excludes ACRO/InfoGating), but could be read more broadly.

4. **The mask-based compositional decoder is an architectural assumption whose failure modes are undiscussed.** The paper states "assuming the state variables and exogenous variables occupy different parts of the visual observation" (line 134), making this assumption transparent. However, the paper does not discuss or test scenarios where this assumption breaks down (e.g., semi-transparent overlays, shadows that spatially overlap the agent, or backgrounds that move behind the agent in the same pixels). Since the ExoPOMDP formalism does not imply pixel-level separation, this architectural choice is a practical heuristic whose limitations could be made more explicit.

### Trivial

- The paper does not report computational cost (parameter count, training time) for CLEAR vs. baselines, which would be useful for practitioners.

## Nice-to-Haves

- **Empirical analysis of min-max stability.** A plot of the inverse-dynamics losses over training or a comparison to a simpler fixed penalty (e.g., an L2 penalty on the ê-to-action regression) would strengthen confidence in the adversarial scheme.
- **Test on overlapping-distraction scenarios.** Evaluating CLEAR where agent and distractions overlap in pixel space (e.g., backgrounds with moving textures behind the agent) would clarify the method's limitations and scope.
- **Comparison to a reconstruction-free baseline.** A comparison to contrastive predictive coding (CPC) or similar would isolate whether reconstruction is essential for the disentanglement or whether the regularizer drives it.
- The derivation from Eq. 3 to Eq. 4 could be expanded with intermediate algebraic steps in the main text for readability, though this is not a substantive concern.

## Removed Points

These points were flagged by reviewers but removed per the meta-review guidelines:

- **"Derivation from Eq. 3 to Eq. 4 is too compressed"** — This is about missing intermediate algebra that would be in a supplementary appendix. Per guidelines, appendix-stripped content is assumed present in the original submission.
- **"Hyperparameter choices for KL constants not reported"** — The paper states details are in Appendices G and H (line 231). Appendix content is stripped by the parser.
- **"The paper does not compare to [missing baseline]"** — Missing-related-work criticisms are not included as the meta-reviewer does not have external sources to verify their validity.
- **"Formatting/nitpick about compressed presentation"** — Formatting artifacts are parser errors, not author errors.
- **"Ground-truth state regression raises more questions than it answers"** — The paper honestly discusses this nuance (lines 198). This is an observation, not a weakness, and the paper's treatment is fair.
- **Strength Finder's generic claims** (e.g., "addressed an important problem") — Merged into specific evidenced strengths above.
- **"Related work is thorough and fair"** — This is an observation about presentation, not a strength of the paper's contribution.

## Novel Insights

The meta-review reveals that the paper's most underappreciated contribution may be the ablation study (Table 3, Figure 5), which demonstrates that even with a disentangled two-encoder architecture and reconstruction objective, the learned representations can converge to qualitatively different (flipped or degenerate) local optima across random seeds. The inverse-dynamics regularizer does not just improve performance — it eliminates structural instability in the representation learning itself. This is a deeper point than the paper explicitly emphasizes: the problem is not merely that standard objectives fail to remove distractions, but that they are underdetermined for the separation task, and the action-controllability signal is what breaks the symmetry.

## Suggestions

1. Temper the "principled" language slightly to reflect that the link between the motivating Eq. 2 decomposition and the implemented objective is intuitive and structurally motivated, not formally proven.
2. Add a brief analysis of the min-max optimization's behavior across seeds (e.g., losses over training, or a comparison to a simpler regularizer).
3. Include a limitations paragraph discussing when the pixel-level separation assumption may break and how the method could be extended.
4. Report computational cost (parameters, training time) for CLEAR and baselines to aid practical deployment decisions.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
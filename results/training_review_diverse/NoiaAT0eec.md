Thank you for the clarity. Now I have all the information I need to produce the final consolidated review. Let me synthesize everything.

## Summary

This paper introduces MI-MAE, which applies the information bottleneck (IB) principle to masked autoencoders. The authors define an information distortion for MAEs, present Theorem 2 as a generalization bound on mutual information, and derive (via Corollary 4) conditions that motivate two additional losses: an InfoNCE-based mutual information maximization loss across latent features from multiple masks, and a CLUB-based mutual information minimization loss between input and latent features. The paper claims a 400-epoch MI-MAE achieves 83.9% on ImageNet-1K, surpassing a 1600-epoch MAE by 0.5%.

## Strengths

- **Novel theoretical framing:** The paper is the first to explicitly connect the information bottleneck principle to masked autoencoders, providing a new perspective beyond contrastive-learning-based analyses. This framing is a genuine attempt at a more systematic understanding of MAE training, even if the execution falls short of rigorous.

- **Strong headline empirical result:** The claim that a 400-epoch MI-MAE (83.9% on ImageNet-1K) surpasses a 1600-epoch MAE is striking and, if properly controlled, would represent a meaningful practical advance — a fourfold reduction in pre-training time with an accuracy gain.

- **Actionable losses derived from analysis:** The paper translates the theoretical conditions into two concrete, implementable loss functions (InfoNCE for maximization, CLUB for minimization) and provides the full training algorithm. Practitioners could re-implement MI-MAE from the description.

- **Acknowledges and bridges to prior contrastive-MAE connections:** The paper explicitly discusses prior work connecting MAEs to contrastive learning (Zhang et al., Kong & Zhang, etc.) and positions its IB analysis as extending rather than ignoring that line of work.

## Weaknesses

### Major

1. **The theoretical framework is presented as rigorous but is too informal to carry the paper's claimed analytical weight.** Definitions are unconventional and their connection to standard IB formulations is unclear (e.g., Definition 1's "information distortion" as conditional mutual information between visible and masked patches given the prediction). Theorem 2 is stated without proof or derivation, introducing quantities ($r$ as bias is defined but the conditional term $I(\hat{z}; X \!\cdot\! m \mid r)$ appears without justification). The metric for $|Z-\zeta| \le \epsilon_z$ is never specified (L2 norm? KL divergence?). Corollary 4's conditions are asserted rather than derived from the preceding theory. The paper claims a "rigorous analytical framework" (Introduction, Conclusion) but the mathematics does not meet the standards the paper sets for itself.

2. **The connection from Corollary 4 to the actual losses is asserted, not derived.** The paper states "From the first condition... we can adopt InfoNCE," but does not formally show that InfoNCE's lower-bound maximization satisfies the corollary's requirement $I(\hat{z}_k; \hat{z}_i)$ is maximized, nor why InfoNCE (a particular lower-bound estimator) is the correct or unique choice. Similarly, CLUB is adopted for MI minimization without deriving that optimizing Eq. 10 satisfies the second and third conditions of Corollary 4. The theoretical motivation therefore does not uniquely or tightly constrain the loss design — it serves as a post-hoc wrapper around standard contrastive and variational MI losses rather than a derivation.

3. **The experimental protocol does not isolate the effect of the proposed MI losses from the increased number of masked views per epoch.** The method samples four masks per image per epoch; the baseline uses one. The paper reduces epochs to one-quarter to match total masked views, which is standard practice. However, without a control — training MAE with four masks per image (summing reconstruction losses) but without the MI losses — any improvement cannot be attributed to the information bottleneck objectives. It could plausibly arise from processing more diverse masked views (a known benefit in MIM literature). This is the single most important missing control and directly affects the credibility of the central empirical claim.

### Minor

1. **"Orthogonal masks" is not defined.** The method relies on generating "mutually orthogonal masks" (lines 16, 103) but never specifies what orthogonality means in this context. Non-overlapping masks would severely constrain the mask space and may affect feature diversity; the paper provides no justification for this choice over random masks.

2. **Ablation of the two MI loss terms is absent from the extracted text.** The paper claims both $\mathcal{L}_{\mathrm{max-mi}}$ and $\mathcal{L}_{\mathrm{min.mi}}$ are needed but provides no ablation study separating their contributions. (Note: this may be present in the full paper's experimental section, which was truncated by the PDF parser.)

3. **The claim that prior contrastive-MAE works "only perform on par with the original MAE" (line 46) is used to motivate the need for the IB perspective, but no comparison to those methods (e.g., U-MAE, iBoT-like approaches) is present in the extracted experimental section.** Without such comparisons, it is unclear whether MI-MAE offers advantages over existing methods that also use multi-view or contrastive objectives for MIM.

### Trivial

- The notation in Theorem 2's bound mixes $K_x$, $|Y|$, and $n_x$ in the $O(\cdot)$ term in a way that makes the bound's tightness unclear without the missing proof.
- The paper states Corollary 4's conditions, then line 140 adds a fourth point ("Additionally, we find that by optimizing Eq. 10, the third condition is also satisfied") which appears to be a commentary rather than a formal condition.

## Nice-to-Haves

- A control experiment training MAE with 4 masks per image (no MI losses) at 400 epochs would resolve the core confounding concern.
- Ablations for each loss component ($\mathcal{L}_{\mathrm{max-mi}}$ only, $\mathcal{L}_{\mathrm{min.mi}}$ only, both) would strengthen the empirical claims.
- Comparisons to other MIM variants that also use multiple masks or contrastive objectives (SimMIM, iBoT, U-MAE) would better contextualize the improvements.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"r is undefined in Theorem 2":** Removed as factually incorrect — the paper explicitly states "where r is the bias" (line 81–82). However, the broader concern that $I(\hat{z}; X\!\cdot\!m \mid r)$ is introduced without motivation is kept above.
- **Missing fine-tuning details, data splits, detection/segmentation protocols:** Removed — the experimental section is truncated by the PDF parser; these details likely exist in the original submission.
- **No confidence intervals / number of runs:** Removed — cannot be verified from the truncated experimental section; typical for large-scale vision benchmarks.
- **"The extraction truncates the experimental section":** Removed as a parser artifact, not an author error.
- **Strength Finder claimed "multi-task validation across domains":** Removed — experimental results are truncated; this claim cannot be verified. It may be legitimate but cannot be confirmed from available text.
- **Strength Finder claimed "derivation of actionable loss functions":** Weakened to "adopted" in the strengths above — the paper says "we can adopt InfoNCE," not derive it — but the overall point that the analysis motivates concrete losses is retained.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful meta-level insight: applying a formal theoretical framework (here, IB) to a well-understood empirical method (MAE) can produce actionable losses, but the credibility of the entire contribution collapses if the theory is presented as rigorous when it is not. The paper's central tension is that it wants the authority of "rigorous analytical framework" while the actual mathematics is incomplete (no proofs, undefined metrics, asserted connections). The reviews correctly identify that the paper would be more honest and no less useful if it presented the IB framing as a motivating analogy rather than a formal derivation. The missing four-mask control is a second instance of the same pattern — the paper claims a specific causal mechanism (IB losses help) but does not rule out the simplest alternative explanation (more masked views help).

## Suggestions

1. **Add the critical control experiment:** Train MAE with 4 random masks per image (summing reconstruction losses) at 400 epochs, without any MI losses. If MI-MAE beats this control, the IB losses are validated; if not, the core claim is unsupported.
2. **Downgrade the theoretical claims from "rigorous framework" to "motivating perspective" throughout the paper.** Remove the term "rigorous" and present Theorem 2 and Corollary 4 as heuristic motivation with proof sketches deferred to an appendix, rather than as formal results that the paper does not actually prove.
3. **Clarify the technical loose ends:** Define the metric for $|Z-\zeta|$, define "orthogonal masks," and state what "neighborhood" means in the latent space.
4. **Run ablations for the two MI losses individually** to validate the claim that both maximization and minimization are needed.

## Score and Decision

The paper proposes a genuinely new perspective on MAEs via the information bottleneck and makes a strong headline empirical claim. However, the theoretical presentation is substantially less rigorous than claimed, the experimental design has a clear confounding factor (mask multiplicity vs. MI losses), and the missing control experiment prevents attribution of the reported improvements. These are major weaknesses that affect the paper's core credibility. The contribution could be salvaged with the suggested control and a more honest framing of the theory, but in its current form the paper does not deliver what it promises.

**Score:** 4.5

**Decision:** Reject

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
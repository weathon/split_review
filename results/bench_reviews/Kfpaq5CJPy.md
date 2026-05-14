Now I have a comprehensive understanding of the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

This paper proposes a novel adversarial attack that constrains perturbations to a semantically meaningful low-dimensional subspace (defined via DCT, DWT, or Glow transforms) while simultaneously enforcing the standard \(L^\infty\) box constraint in pixel space. The key technical innovation is using the barrier method from nonlinear programming to avoid the intractable projection step that would be required by PGD for this intersection constraint. The authors then use these subspace-constrained attacks for adversarial training (via TRADES) and show that the DWT variant yields substantially improved robustness on CIFAR-10-C with only a small drop in clean accuracy.

## Strengths

- **Novel constrained optimization formulation**: The paper defines a perturbation space as the intersection of a low-dimensional subspace in a transformed representation and the \(L^\infty\) ball in the image domain (Eq. 2). This simultaneously captures semantic structure and pixel-level boundedness—a genuine gap in prior work, which typically enforced only one of these constraints. The paper explicitly contrasts this with prior transform-domain attacks (e.g., Duan et al., 2021; Sharma et al., 2019) that lacked pixel-space guarantees (Section 5).

- **Clever use of the barrier method**: The barrier method elegantly sidesteps the need for projection onto the complex feasible set. Figure 2 clearly illustrates why PGD-style projection fails here, and the paper includes a sanity check showing the barrier method in pixel space "operates similar to the PGD attack," validating that the approach produces correct behavior where ground truth is known (Section 4.1).

- **Generality across transform types**: The framework is demonstrated with classical linear transforms (DCT, DWT) and a nonlinear learned flow-based model (Glow), showing the method does not rely on linearity or orthogonality—only invertibility and differentiability (Section 3). This is a meaningful expansion beyond prior work that relied on orthogonal transforms for norm preservation.

- **Promising corruption robustness result with DWT AT**: Adversarial training with the barrier-dwt attack yields a 12.27% average improvement on CIFAR-10-C over standard PGD AT while sacrificing only ~1.5% clean accuracy (Table 2, Section 4.2). The comparison across different subspaces (dct, dwt, glow) reveals that not all subspaces help equally—glow AT preserves clean accuracy but underperforms vanilla on corruption—suggesting the benefit is subspace-specific rather than a generic artifact of weaker training.

## Weaknesses

### Fatal

None.

### Major

- **No control for adversary strength in the adversarial training experiment**: The subspace adversaries are inherently constrained—they operate in a \(q\)-dimensional subspace of the full \(L^\infty\) box and achieve lower attack success rates at the same \(\epsilon\) (Table 1). The paper claims the subspace constraint *per se* yields better corruption robustness (Section 4.2), but does not rule out the alternative explanation that training with a simply weaker adversary (e.g., PGD with fewer steps or a reduced effective budget, tuned to match the subspace adversary's perturbation magnitude or success rate) would confer similar benefits. This is a well-known phenomenon in adversarial training literature. The fact that different subspaces produce different corruption outcomes (dwt helps, glow does not) partially mitigates this concern, but a direct control experiment—e.g., PGD with weakened hyperparameters calibrated to match the effective perturbation strength of barrier-dwt—is absent and would be needed to fully attribute the gains to subspace semantics rather than adversary weakness. This is the most substantive experimental gap in the paper.

### Minor

- **Ambiguity in distance metric aggregation**: Section 4.1 and Table 1 report average \(L^2\) and LPIPS distances but do not specify whether these are computed over all 9,546 test images or only those where the attack succeeded. The subspace attacks have success rates as low as 86% (vs. ≥99.9% for baselines). Failed attacks may terminate with smaller perturbations, which could downward-bias the subspace attack averages. However, the LPIPS gaps are large (e.g., 0.15 for barrier-dwt vs. 0.28 for PGD at \(\epsilon=0.1\)), so the qualitative conclusion about higher perceptual similarity likely survives correction. Clarification and possibly a per-success-only recomputation would strengthen the claim.

- **Lack of constraint-violation analysis for the barrier method**: The sign-gradient update (Eq. 8) with finite step size \(\eta\) does not theoretically guarantee that iterates remain inside the feasible set \(\mathbb{A}\). The paper states that \(\eta\) "should be small enough" (line 117) but provides no empirical characterization of how often the \(L^\infty\) constraint is violated in practice, nor any sensitivity analysis over \(\eta\) and the barrier coefficient \(\mu\). The pixel-domain sanity check (barrier attack on the full box matching PGD behavior) provides some reassurance but does not substitute for direct analysis. This is a gap in understanding the method's reliability, though not one that invalidates the main results.

### Trivial

- **Insufficient training hyperparameters for reproducibility**: Section 4.2 omits the TRADES trade-off parameter \(\lambda\), learning rate schedule, weight decay, batch size, and barrier method hyperparameters (\(\mu\), \(\eta\)) used during AT training. These are needed for exact reproduction but do not affect the validity of the relative comparisons (all AT variants presumably share the same TRADES hyperparameters).

- **Underspecified DCT instantiation**: Section 3 states "12 out of 64 luminance frequencies and 51 out of 64 chrominance frequencies" are assigned to the auxiliary set but does not specify *which* frequencies or the ordering criterion, making exact reproduction of the DCT results difficult.

## Nice-to-Haves

- An experiment with standard PGD weakened (fewer steps, reduced budget, or early stopping) to match the effective perturbation magnitude of barrier-dwt, then evaluated on CIFAR-10-C, would cleanly disentangle the effect of subspace semantics from adversary weakness.

- A brief analysis or qualitative discussion of *why* DWT perturbations in particular align with common image corruptions would add insight—e.g., which frequencies are altered by real corruptions vs. the DWT adversary.

- Extending the AT evaluation to a WideResNet (standard in corruption robustness benchmarks) would strengthen the generality claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic #1 (distances computed over unsuccessful attacks as evidential flaw)**: While the ambiguity is real and noted as a minor weakness above, the harsh critic's framing that this "renders the similarity comparison invalid" and that the core claim is "unsupported" is overstated. The LPIPS gaps between subspace and baseline attacks are large enough (e.g., 0.15 vs. 0.28) that including the ~14% worst-case unsuccessful subspace attacks would not reverse the conclusion. This is a clarity issue, not a fatal methodological error.

- **Harsh Critic #4 (barrier method gradient update does not guarantee constraint satisfaction)**: The harsh critic claims this "would break the core promise of the method and invalidate the comparison." The paper includes a sanity check (barrier attack on the full pixel box matching PGD behavior) that demonstrates empirical validity. The concern is real but the harsh critic's severity judgment is disproportionate.

- **Harsh Critic on DCT underspecification as a major gap**: The harsh critic flags that DCT frequency assignment is underspecified. This is a real detail gap but is a trivial reproducibility concern, not a substantive flaw.

- **Harsh Critic on Glow training details being missing**: The paper provides Glow architecture details (3 flow levels, depth 32, 1600 epochs, batch size 512) in Section 4 (line 161). The harsh critic's claim that "architecture, optimizer, and final training loss are missing" is partially incorrect—architecture is given, and Glow training follows the standard recipe from Kingma & Dhariwal (2018), which is cited.

- **Strength Finder: "Improved perceptual similarity" as unqualified strength**: Retained but qualified in the review given the aggregation ambiguity.

- **Strength Finder: Generic "important problem" framing**: Removed as superficial.

- **Harsh Critic on missing variance measures for CIFAR-10-C**: Moved to Nice-to-Haves as this is a desirable refinement but not standard practice in corruption robustness benchmarking (CIFAR-10-C is typically reported as single-run averages across corruption types).

- **Harsh Critic on "glow AT practically maintains natural accuracy but corruption performance is worse than vanilla" as undercutting the narrative**: The paper itself acknowledges this in the limitations (line 199): "AT with S_glow does not perform well on corruption, possibly since the features learned by the flow-based model are semantically at a higher level." The paper does not claim all subspaces help; it honestly reports the negative result for glow.

- **Harsh Critic on "cherry-picked examples" in Figures 3 and 4**: The paper states these are "randomly selected" (line 173). Without evidence to the contrary, this criticism is dismissed.

## Novel Insights

The paper's finding that different representation subspaces produce qualitatively different corruption robustness outcomes—DWT AT helps substantially, DCT AT helps modestly, Glow AT does not help at all—is genuinely informative. It suggests that the alignment between the perturbation subspace and the structure of common corruptions matters, and that "weaker adversary" alone cannot explain the results (if it could, Glow AT, which has high attack success and preserves clean accuracy well, should also improve corruption robustness). This is a more nuanced finding than the paper's own narrative fully exploits, and it opens interesting questions about which representation properties confer corruption robustness.

## Suggestions

- Clarify in Section 4.1 whether distances are computed over all images or only successful attacks. If currently over all images, recompute on successful attacks only and report both. The qualitative conclusion should survive, but the precision will improve.

- Add a weakened-PGD baseline for the AT experiment: tune PGD steps/step size to match barrier-dwt's effective perturbation magnitude (or its clean accuracy after AT) and evaluate on CIFAR-10-C. This would directly address the major weakness.

- Report maximum \(L^\infty\) constraint violation across test images for the barrier method and include a brief sensitivity analysis for \(\eta\) and \(\mu\) to characterize reliability.

---

This paper introduces a genuinely novel and technically creative method for subspace-constrained adversarial attacks using the barrier method. The core idea—enforcing both semantic subspace constraints and pixel-space \(L^\infty\) bounds simultaneously—fills a clear gap in the literature. The DWT adversarial training result on CIFAR-10-C is promising and suggests practical value. However, the adversarial training experiment lacks a critical control for adversary strength, which prevents fully attributing the corruption robustness gain to the subspace semantics rather than to training with a milder adversary. The barrier method's constraint satisfaction is not empirically characterized. These gaps are addressable but significant enough to prevent full endorsement of the paper's conclusions as stated. The paper would benefit substantially from a weak-PGD control experiment and constraint-violation analysis.

**Originality**: Good—novel constrained optimization formulation using the barrier method. **Importance**: Moderate—corruption robustness is important, and the subspace approach is a fresh angle. **Claims supported**: Partially—the AT claims need stronger experimental controls. **Soundness**: Fair to good—the method is technically sound, but the evaluation has gaps. **Clarity**: Good—the paper is well-organized and the ideas are clearly explained. **Value to community**: Moderate—the barrier method technique and subspace-constrained AT approach could inspire follow-up work.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
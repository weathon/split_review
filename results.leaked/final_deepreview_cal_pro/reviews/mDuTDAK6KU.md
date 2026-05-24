Now I have a thorough understanding of the paper and can cross-check all claims. Let me write the final consolidated review.

---

## Summary

KOALA introduces a novel adversarial detection mechanism based on disagreement between two complementary nearest-prototype classifiers: one using KL divergence (sensitive to dense, low-amplitude perturbations) and one using an L₀-based metric (sensitive to sparse, high-impact changes). The paper provides a formal theorem proving that, under certain conditions on prototype separation, no norm-bounded perturbation can simultaneously fool both classifiers — forcing disagreement and thus detection. The method requires only lightweight fine-tuning on clean images. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet validate the theory (perfect detection on theorem-compliant samples) and show strong ablation results favoring the KL+L₀ combination.

## Strengths

- **Formal detection guarantee with empirical validation**: Theorem 1 provides explicit conditions (A1–A4) under which detection is guaranteed, and Experiment 1 (Table 1) confirms this: on the theorem-compliant subset, recall and precision both reach 1.0 across models and attack strengths. This is a genuinely rare combination of theory and empirical confirmation in the adversarial detection literature.

- **Demonstrated complementarity of KL and L₀ metrics**: The ablation study (Table 2) shows that on ResNet/CIFAR-10, the KL+L₀ combination achieves the highest detection F1 (0.87 at ε=2/255) compared to L₀+Cosine, KL+Cosine, and KL+L₀+Cosine — confirming that the two metrics are more effective together than other pairings.

- **Robustness gains without adversarial training**: Despite fine-tuning only on clean images, the KL+L₀ objective yields substantially higher adversarial accuracy on ResNet/CIFAR-10 than the baseline (e.g., 57.32% vs. 45.5% for PGD at ε=2/255, Table 3), and similar improvements hold across CW and AutoAttack.

- **Lightweight, plug-and-play, semantics-free design**: KOALA requires only a single fine-tuning step on an off-the-shelf encoder with clean images. It works on both ResNet-18 and CLIP ViT-B/32 with identical loss weights and no architectural changes, and operates purely on representation geometry without task-specific semantic priors.

## Weaknesses

### Major

- **No empirical comparison to any prior adversarial detector**: The paper cites numerous existing detection methods (Feature Squeezing, LID, Mahalanobis, NIC, MagNet, etc.) in the related work, but the experimental section (Tables 2–4) compares only metric-combination variants of KOALA against each other. Not a single number from a previously published detector appears. Consequently, the headline precision/recall numbers (0.94/0.81 on CIFAR-10, 0.66/0.85 on Tiny-ImageNet) are uncontextualized — the reader cannot judge whether KOALA is competitive, state-of-the-art, or substantially worse than simpler alternatives. For a paper whose central contribution is presented as a practical adversarial detector, this is a significant evidential gap.

- **The theorem is conditional and covers a minority of examples on some settings**: Theorem 1 guarantees detection only when a sufficient coordinate gap exists between the true class prototype and the adversarial class prototype. Experiment 1 shows this condition is met for only 67% of CIFAR-10 examples (ε=2/255) and just 11% of CLIP/Tiny-ImageNet examples. The paper provides no runtime mechanism to certify whether the condition holds for a given input, and no method to enforce or expand the compliant region. The theorem thus describes a conditional, post-hoc property rather than a deployable safety guarantee, and this gap between the theoretical ideal and practical operating point is not adequately acknowledged.

- **Non-standard detection metrics conflate classification accuracy with detection quality**: The TP definition (Section 4.2) counts as a true positive not only correctly flagged attacks (â=1) but also adversarial inputs that the detector misses yet the classifier still gets right (â=0, ŷ=y*). This conflates classifier robustness with detector quality and inflates the reported precision/recall beyond what a pure detection metric would give. The rationale for this choice is not discussed.

### Minor

- **No evaluation against adaptive attacks**: The attacks used (PGD, CW, AutoAttack) are standard and it is not clear whether they were generated to specifically circumvent KOALA's detection mechanism (e.g., by minimizing a joint loss targeting both heads simultaneously). Given that the central theoretical claim is that no perturbation can fool both heads, testing against an adversary that explicitly tries to do so would substantially strengthen the empirical case.

- **No hyperparameter sensitivity analysis**: The threshold τ=0.75, smoothness parameter φ=0.5, and loss weights (ω_L₀=0.9, ω_KL=0.1) are all fixed. The theorem proves existence of some τ, but a fixed value is used in practice. A study showing the detector is not brittle to these choices would strengthen the empirical case, especially since Experiment 2 on CLIP reveals a qualitatively different result when adding Cosine, suggesting metric interactions can be subtle.

- **Assumption A3 presented without empirical justification**: The condition |δ_i| ≤ (3/2)|p_i*| is described as "mild and practical," but no empirical evidence or analysis is offered to support that real adversarial perturbations satisfy this coordinate-wise bound in the normalized embedding space.

### Trivial

- No confidence intervals or standard deviations are reported for detection metrics, despite evaluations on subsets of varying sizes (Table 1).

## Nice-to-Haves

- A brief discussion of how softmax normalization of embeddings (required by KL divergence) interacts with the L₀ metric — specifically, whether sparse input-space perturbations reliably map to sparse deviations in a probability-simplex embedding — would help readers understand the method's scope and potential failure modes.

- Transforming the theorem-compliant partition into a practical runtime certification (computing prototype gaps and flagging whether the guarantee holds) would turn the conditional theorem into a deployable safety feature and clearly illustrate when KOALA can and cannot be trusted.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The proof sketch does not derive how the energy budget, the L₀-counting threshold, and the KL inner-product condition are quantitatively linked"** — This is a proof *sketch* by design; the full proof is stated to be in the appendix (which the parser strips). Demanding full derivation in the main text of a sketch is unreasonable.

- **"Missing appendix / full proofs"** — The paper explicitly states complete proofs are in appendix B. The parser strips appendix sections; this is not an author error.

- **"Attack generation protocol remains unspecified"** — Section 4.1 explicitly specifies PGD, CW, and AutoAttack with ℓ∞ constraints at ε ∈ {2/255, 4/255} and batch size 128. While additional detail on the loss function used would be helpful, the protocols are specified.

- **"The paper would benefit from explicitly disentangling detection quality from classifier degradation"** — This is already partly achieved by the separate reporting of adversarial accuracy (Tables 3–4) alongside detection metrics (Tables 1–2), and the paper itself notes the CLIP KL+L₀+Cosine case as revealing. The point has merit but is largely covered.

- **Strength about "the problem is important"** — Generic; removed as it does not cite specific evidence from this paper.

- **Formatting / typo criticisms from the harsh critic** — These are parser artifacts, not issues in the original submission.

## Novel Insights

The geometric insight that KL-divergence and L₀-based nearest-prototype decisions define complementary stability bands that are mutually exclusive under norm-bounded perturbations is genuinely novel. Unlike prior detection work that relies on empirical heuristics, KOALA provides an explicit, provable condition for when detection *must* occur. The empirical confirmation that this condition is sufficient (perfect detection on compliant samples) and the demonstration that the KL+L₀ combination outperforms other metric pairings in ablation studies both provide concrete evidence for the underlying geometric claim. This framework of complementary-metric disagreement could potentially generalize beyond adversarial detection to other robustness or OOD detection settings.

## Suggestions

- Add at least 2–3 baseline comparisons to established detectors (e.g., Feature Squeezing, LID, Mahalanobis) evaluated under identical conditions. This is the single most important improvement and would immediately contextualize KOALA's performance.
- Test against an adaptive adversary that explicitly minimizes a joint loss over both heads (e.g., weighted sum of KL and L₀ distances to a target prototype), or use a multi-objective optimizer to search for perturbations that force both heads to agree on a wrong class.
- Provide a runtime computable check for the theorem's conditions, so the detector can flag when its guarantee applies versus when it is operating in the non-compliant regime.
- Clarify and justify the non-standard TP definition, or report standard detection metrics (where TP = correctly flagged attack) alongside the current metrics.
- Include a sensitivity analysis for τ, φ, and the loss weights.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| KAWlH5pfQu | 3.00 | R1 | KOALA clearly stronger (theory + experiments vs. generic detection) |
| kz78RIVL7G | 2.60 | R1 | KOALA clearly stronger |
| YmQyEdLIkU | 5.50 | R1 | KOALA stronger (comparable theory, but KOALA has substantially better experiments) |
| kwCHcaeHrf (SPADE) | 5.50 | R1 | Comparable — SPADE has baselines; KOALA has stronger attacks tested |
| I5lcjmFmlc | 8.00 | R1 | KOALA clearly weaker (missing baselines, conditional guarantee) |
| RzdtpxL0H5 (DDAD) | 6.20 | R2 | KOALA weaker — DDAD has comprehensive baselines and adaptive attacks |
| rlsWIBDWhW | 5.50 | R2 | KOALA stronger (more novel, better theoretical grounding) |
| eT6oLkm1cm | 6.00 | R2 | Different domain; KOALA weaker in experimental completeness |

**Round 1 bracket:** 5.0–6.5. KOALA is clearly above the weak anchors (~3.0) and clearly below the strong anchors (~8.0). It is comparable to SPADE (5.50) but lacks baselines.

**Round 2 narrowing:** KOALA sits below DDAD (6.20, which had comprehensive baselines and adaptive attacks) and is comparable to or slightly below SPADE (5.50, which had baselines but weaker attack evaluation). The absence of baselines against any prior detector is the decisive factor pulling the score below these comparables.

**Final score: 5.0.** The paper has genuine intellectual merit — the geometric insight about complementary metrics, the formal theorem with empirical validation, and the clean method design — but the experimental validation is insufficient to establish KOALA as a practical detector. The absence of any baseline comparison to prior detectors, the conditional nature of the theorem (covering as few as 11% of examples on one setting), and the non-standard detection metrics together mean the central empirical claims are not adequately supported. The paper would be substantially strengthened by the additions suggested above, particularly baseline comparisons and adaptive attack evaluation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
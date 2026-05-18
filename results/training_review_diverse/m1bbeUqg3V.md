Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces HyperPg (Prototypical Gaussians on the Hypersphere), a novel prototype representation that models a truncated Gaussian distribution over cosine similarities in a hyperspherical latent space. The key idea is that prototypes learn a directional anchor vector plus scalar mean and standard deviation parameters, enabling ring-shaped activation patterns that a single point-based prototype cannot produce. The paper further proposes HyperPgNet, an architecture that learns HyperPg prototypes aligned with human-defined concepts using pixel-level annotations, and a concept extraction pipeline built on Grounding DINO and SAM2. Experiments on CUB-200-2011 and Stanford Cars show HyperPgNet outperforming ProtoPNet with substantially fewer prototypes (300 vs. 2000) and faster convergence (~40 vs. ~490 epochs).

## Strengths

- **Novel prototype representation with genuine geometric insight.** HyperPg prototypes combine the statistical flexibility of Gaussian distributions with the classification advantages of the cosine hypersphere (Section 3.3, Equations 3-4). The ring-shaped activation pattern for intermediate μ values (Figure 2) is a genuinely novel capability — a single HyperPg prototype can cover a set of vectors orthogonal to its anchor direction that would otherwise require an infinite mixture of point-based prototypes. This is achieved with only two additional scalar parameters (μ, σ), making it parameter-efficient.

- **Compelling empirical improvements over ProtoPNet with clear efficiency gains.** On CUB-200-2011, HyperPgNet without RRC loss achieves 76.5% accuracy using 300 concept-aligned prototypes in ~40 epochs, compared to ProtoPNet's 68.0% with 2000 class-based prototypes in ~490 epochs (Table 1). On Stanford Cars, the improvement is 88.6% vs. 86.4% (ProtoPNet) with a 10× prototype reduction. The convergence speed advantage (12× faster) is substantial and clearly shown in Figure 3.

- **Ablation chain demonstrating additive value of each component.** The paper provides a clean chain: ProtoPNet (L₂, 68.0%) → ProtoPNet + HyperPg (70.5%) → HyperPgNet − RRC (76.5%) → HyperPgNet + RRC (74.1%). The middle step (ProtoPNet + HyperPg) isolates the benefit of the HyperPg representation itself without concept supervision, showing that the distributional representation accounts for a meaningful portion of the gain (2.5 percentage points on CUB).

- **Practical concept extraction pipeline using foundation models.** The automated pipeline combining Grounding DINO and SAM2 (Section 5) generates pixel-level annotations for Stanford Cars in ~2 hours on a consumer GPU (NVIDIA 4060 Ti). This is a practical contribution that makes concept-aligned prototype learning feasible on datasets without existing part annotations.

- **The RRC loss provides a principled mechanism for concept alignment.** Unlike prior prototype methods that only post-hoc "push" prototypes to nearest training patches, the RRC loss (Equation 5) uses pixel-level annotations to directly constrain where prototypes activate via gradient penalties, providing causal rather than correlational alignment.

## Weaknesses

### Fatal
None.

### Major
- **Claim scope exceeds experimental breadth.** The abstract states that "HyperPgNet outperforms other prototype learning architectures," but the experimental comparison includes only one prototype architecture (ProtoPNet, plus its HyperPg variant). Multiple recent prototype methods discussed in Related Work — including ProtoPool, ProtoTree, PIPNet, Deformable ProtoPNet, ProtoGMM, and MGProto — are not empirically compared. While ProtoPNet is the canonical baseline, the wording implies broader validation than the paper provides. The claim should either be calibrated to "outperforms ProtoPNet" or supported with one or two additional comparisons under matched conditions.

### Minor
- **The RRC loss accuracy tradeoff is substantial (especially on Cars: 88.6% → 81.2%) and the claimed interpretability benefit is not systematically measured.** The paper states that the performance drop is "offset by increased transparency due to more precise concept prototypes," but provides only a single qualitative example (Figure 7). No quantitative metric — such as mean IoU between prototype gradient masks and concept annotations, or a human evaluation of prototype interpretability — is reported. Without such a metric, the claimed transparency benefit is asserted rather than demonstrated, and readers cannot assess whether the 7.4-point accuracy drop on Cars is worthwhile.

- **All results appear to be single-run point estimates without variance or statistical significance reporting.** Given the stochasticity in training and the automated concept mask generation, reporting mean ± std over multiple seeds would substantially increase confidence in the results.

- **The quality of the automated concept masks is not benchmarked.** For Stanford Cars, the pipeline uses Grounding DINO → bounding-box filtering → SAM2, but no validation (even a small manual spot-check on a random subset) is reported to confirm that generated masks correspond to the intended car parts. False positives and missed detections are likely (e.g., "wheel" in side views, "headlight" confused with reflectors), and mask noise directly affects the RRC loss behavior.

- **The list of Stanford Cars concepts is incompletely specified.** The paper states "a list of 10 car parts (e.g., wheel, headlight, radiator)" but the full list and the rationale for inclusion/exclusion are not given. This affects reproducibility.

- **No ablation comparing HyperPgNet against concept-aligned point-based prototypes trained with the same L_Den and L_RRC losses.** The "ProtoPNet + HyperPg" ablation (2000 class-based prototypes) shows the HyperPg representation helps, but the specific contribution of the distributional representation within the concept-aligned regime (300 prototypes) is not isolated. Such an ablation would cleanly separate the benefit of the HyperPg distribution from the benefit of concept-level supervision.

### Trivial
- The RRC loss in Equation 6 aggregates gradient penalties over all concepts by summing, so prototypes for rare concepts receive penalties proportional to their pixel area. Per-concept normalization would be more stable.
- The paper uses "Segformer Baseline" at 17.7% on CUB, which heavily overfits — this is a reasonable choice for an ablation control but is not a meaningful baseline in its own right.

## Nice-to-Haves
- An analysis of learned HyperPg parameters (histogram of learned μ and σ values across prototypes, with examples of ring-shaped activations for μ near 0) would demonstrate that the distributional capacity is actually used and help readers understand what kinds of concepts correspond to different μ values.
- A comparison against one additional recent prototype method (e.g., ProtoPool or PIPNet) under the same backbone and training setup would substantially strengthen the "outperforms other prototype learning architectures" claim without requiring a full survey.
- Reporting concept mask quality metrics (e.g., IoU against a small manually annotated subset) for the Stanford Cars pipeline would help interpret the RRC loss accuracy drop.

## Removed Points
These points were raised by reviewers but are removed or downgraded for the reasons indicated:
- **"The baseline implementations are not established to be strong because ProtoPNet gets 68% vs. published ~78-80% with ResNet."** — The paper uses a different backbone (Segformer) and training regime (full images, no bounding-box crops) consistently across all methods. The comparison is fair within the paper's setup. The absolute numbers differ due to these design choices, not implementation weakness. The chain of ablations using the same backbone is what matters.
- **"ProtoPNet + HyperPg gains are small"** — The 2.5% improvement on CUB and 1% on Cars with only a prototype representation swap (no concept supervision, same 2000 prototypes) is a meaningful signal that the distributional representation itself helps.
- **"No comparison to version using bounding-box crops"** — The paper deliberately adopts a full-image training regime; this is a design choice, not an omission. Demanding the opposite setup is scope creep.

## Novel Insights
The reviews surface two interesting tensions. First, the paper's strongest selling point — the ring-shaped activation pattern of HyperPg for intermediate μ values — is also its least empirically explored aspect. The paper uses this capability as an enabling mechanism without analyzing when and how learned prototypes actually exploit it. Second, the RRC loss creates a genuine accuracy-interpretability tradeoff that the paper treats as a straightforward "offset," but the 7.4-point drop on Cars suggests the relationship is more complex: noisy concept masks may cause the RRC loss to degrade prototypes for concepts that the pipeline segments poorly. A systematic analysis of which concepts suffer accuracy loss under RRC would be illuminating.

## Suggestions
1. **Calibrate the central claim.** Replace "outperforms other prototype learning architectures" with a more precise statement, e.g., "outperforms ProtoPNet and achieves strong results on two datasets while using far fewer prototypes and training steps." Alternatively, add one or two experimental comparisons against recent prototype methods under matched conditions.
2. **Quantify interpretability.** Report a systematic metric (e.g., mean IoU of prototype gradient masks with concept annotations, or prototype-concept alignment scores) to substantiate the RRC loss benefit rather than relying on a single qualitative example.
3. **Add variance reporting.** Run experiments with at least 3 random seeds and report mean ± std for all main results.
4. **Validate concept mask quality.** Report even a small manual verification (e.g., 50 random images per dataset) of the automated concept extraction pipeline's accuracy.
5. **Include a direct ablation** comparing concept-aligned HyperPgNet against an otherwise identical architecture using standard cosine point prototypes trained with the same L_Den and L_RRC losses, using the same (small) number of prototypes.

## Score and Decision

This paper introduces a genuinely novel prototype representation with clear geometric motivation and demonstrates solid empirical improvements over the canonical ProtoPNet baseline. The convergence speed advantage (12×) and prototype count reduction (6-10×) are practically significant. The main weakness is the gap between the claim of outperforming "other prototype learning architectures" and an experimental section that compares against only one such architecture. The secondary issues (no variance reporting, unquantified interpretability tradeoff, unvalidated concept masks) are individually minor but collectively indicate room for experimental rigor improvement. The core contribution is sound and the weaknesses are addressable.

**Score: 6.0**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
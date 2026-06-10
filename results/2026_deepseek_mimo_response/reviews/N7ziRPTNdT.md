Now let me write the final review:

## Summary
This paper argues that generative (decoder-based) approaches are fundamentally better positioned than non-generative (encoder-based) approaches for data-efficient compositional generalization in visual perception. The core theoretical contribution is proving that structural constraints on a decoder (F_int) are coordinate-aligned and enforceable via architecture/regularization, while the analogous constraints on an encoder (G_int) depend on the geometry of the data manifold—including unobserved OOD regions—making them infeasible to enforce in practice. Empirically, non-generative methods fail at compositional generalization on PUG datasets without massive pretraining, while generative methods using gradient-based search and replay yield significant OOD improvements.

## Strengths
- **Novel and clean theoretical asymmetry (Theorem 3.2, Eq. 3.1 vs Eq. 3.4):** The paper formally proves that when d_x ≥ d_z³, the Jacobian and Hessian of inverse generators in G_int can be essentially arbitrary (Theorem 3.2), with the remaining structure only manifesting on the tangent space of the data manifold (Eq. 3.4). This manifold-dependent constraint cannot be enforced without knowledge of OOD manifold geometry. In contrast, the decoder constraints (Eq. 3.1) are coordinate-aligned and data-independent. This asymmetry between causal and anti-causal directions is a genuinely novel formalization, extending prior identifiability work (Brady et al., 2025) and connecting to the causal learning literature (Kilbertus et al., 2018).

- **Tight theory-experiment correspondence across interaction degrees:** PUG-Object (n=0, no concept interaction) yields near-perfect OOD accuracy for all models (Fig. 5C), confirming the theory's prediction that G_int is more constrained when n=0. PUG-Background and PUG-Texture (n≥1) show non-generative methods failing without large-scale pretraining (Fig. 5A-B), consistent with Theorem 3.2. This systematic validation across varying interaction degrees strengthens both the theoretical and empirical contributions.

- **PUG-Texture as a clean test case for the theory:** On PUG-Texture, generative replay cannot be applied (slots capture objects/backgrounds, not textures), so only gradient-based search is used. The fact that search alone yields clear OOD improvements (Fig. 6B) provides a cleaner, less confounded test of the theoretical claim about the value of decoder inversion.

- **Well-motivated practical methods grounded in theory:** Both gradient-based search (Eq. 4.3) and generative replay (Eq. 4.4) are directly motivated by the theoretical framework, not ad hoc. The "System 1 → System 2" framing of encoder-initialized search (Sec. 4.1) is intuitive and well-connected to the cognitive science literature.

## Weaknesses

### Fatal
None.

### Major
- **Title overclaims relative to evidence — "required" is too strong:** The title asserts "Generation is Required for Data-Efficient Perception," but the evidence more precisely supports that generation enables compositional generalization without massive pretraining. Fig. 5 shows SigLIP2 achieves ~80% OOD accuracy on PUG-Background and ~85% on PUG-Texture using a purely non-generative approach with supervised fine-tuning (line 171-173). The paper acknowledges this requires web-scale pretraining but does not analyze *why* pretrained encoders partially succeed. If large-scale pretraining implicitly biases encoders toward structure compatible with G_int, the theoretical infeasibility argument applies specifically to encoders trained from scratch on limited data — not to encoders in general. This gap between the evidence and the headline claim is the paper's most significant issue. An analysis of whether pretrained encoders' Jacobians exhibit approximate G_int structure on the data manifold would either strengthen or appropriately qualify the central claim.

### Minor
- **No computational cost analysis for search:** The paper presents gradient-based search as a practical method (Sec. 4.1) but provides no data on convergence speed. The paper itself acknowledges that "many gradient steps are required, leading to slow or suboptimal convergence" (line 165) but provides no empirical analysis of how many steps are needed or whether the encoder initialization significantly helps. This matters for the practical viability of the "generation is required" argument.

- **No comparison to alternative generative baselines:** The related work (Sec. 6) mentions diffusion models repurposed as classifiers (Jeong et al., 2025; Wang et al., 2025) as another generative approach for compositional generalization. Even a brief comparison would help situate the proposed decoder-inversion approach relative to these alternatives.

### Trivial
None.

## Nice-to-Haves
- Quantify the data-efficiency gap: how much pretraining data would a non-generative method need to match the OOD performance of a generative method trained on ~20K images?
- Report ablation on decoder design sensitivity (the paper references §C with unstructured decoders, but the main text could briefly summarize whether results depend on F_int-structured decoders).
- A small-scale experiment on more complex data (e.g., CLEVR with more objects) would broaden the empirical impact.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Harsh critic's "empirical asymmetry" concern:** The critic claimed the comparison between generative and non-generative methods is confounded by differences in available training signal. This is removed because the asymmetry IS the paper's thesis: the decoder provides the right inductive bias, and generation (search/replay) is the mechanism to exploit it. The paper explicitly frames the non-generative approach as limited to in-domain training (Eq. 2.3) and the generative approach as leveraging decoder inversion (Eq. 2.2 + Sec. 4). This is not a confound but a feature of the comparison.
- **Harsh critic's concern about scope of theoretical framework:** The critic noted the theory is limited to F_int (Eq. 2.7). This is removed because the paper explicitly acknowledges this limitation in Sec. 7 and uses F_int because it is "the largest function class shown to enable OOD identifiability." Criticizing a theory for not applying beyond its stated assumptions is scope creep.

## Novel Insights
The paper's most novel insight is the formal proof that the enforceability of compositional generalization constraints is asymmetric between generators and their inverses in the practical regime where d_x >> d_z. While the intuition that "the causal direction is simpler" has existed in the causality literature (Janzing & Schölkopf, 2010; Kilbertus et al., 2018), this paper provides the first concrete formalization showing that constraints on the inverse function class (G_int) become manifold-dependent and therefore infeasible to enforce when the ambient dimension is high, while constraints on the forward function class (F_int) remain coordinate-aligned and data-independent. The connection between this structural asymmetry and the practical question of compositional generalization in vision is genuinely new.

## Suggestions
- Add analysis of what pretrained encoders learn that enables partial OOD success (e.g., examine whether their Jacobians approximate G_int structure on the data manifold).
- Report computational cost of search (number of iterations, wall-clock time, with vs. without encoder initialization).
- Moderate the headline claim to better match the evidence, e.g., "generation is required for data-efficient compositional generalization."

## Score and Decision

**Retrieved anchors across all rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Compositional World Models | EHmjRIA4l2.md | 3.00 | 1 | Much weaker theoretical contribution, less relevant |
| Optimal Hyperdimensional Representation | NYPJz0CL5X.md | 3.00 | 1 | Weaker, different topic area |
| Beyond Finite Data: OOD Generalization | ZbOSRZ0JXH.md | 3.00 | 1 | Empirical only, no theory |
| From Skills to Plans | q1Cv7Hp52y.md | 3.00 | 1 | Different domain, weaker |
| Provable Compositional Generalization | 7VPTUWkiDQ.md | 7.33 | 1, 2 | Most topically similar. Similar theoretical depth on identifiability but narrower scope. The under-review paper extends it with the asymmetry proof and more experiments. Paper under review is comparable or slightly stronger. |
| On Provable Length and Compositional Generalization | Hxm0hOxph2.md | 5.25 | 1 | Weaker: oversimplified models, ERM assumption, limited experiments |
| Discovering modular solutions | H98CVcX1eh.md | 6.50 | 1, 2 | Less directly relevant (hypernetworks/meta-learning), weaker theoretical results |
| Dynamics of Concept Learning | s1zO0YBEF8.md | 6.50 | 1, 2 | Weaker: SIM task is questionable proxy for compositional generalization |
| Compositional Entailment Learning | 3i13Gev2hV.md | 8.00 | 1 | Stronger but different topic (hyperbolic vision-language) |
| LVSM | QQBPWtvtcn.md | 7.67 | 1 | Different topic (view synthesis) |
| A Decade's Battle on Dataset Bias | SctfBCLmWo.md | 8.00 | 1 | Different topic (dataset bias) |
| Interpreting CLIP's Image Representation | 5Ca9sSzuDp.md | 8.00 | 1 | Different topic (interpretability) |
| Interaction Asymmetry | cCl10IU836.md | 7.00 | 2 | Same research lineage, similar mathematical framework. Under-review paper extends with the encoder-decoder asymmetry proof and has more experiments. Comparable or slightly stronger. |
| Towards a formal theory of compositionality | hKMPz3wkPV.md | 6.75 | 2 | Different approach (Kolmogorov complexity), rejected despite high individual scores |

**Round 1 bracket:** 6.5–8.0. Topical anchors in the weak band (< 3.5) are clearly weaker than the paper under review. In the middle band (3.5–7.5), the most relevant is "Provable Compositional Generalization" at 7.33, which has similar theoretical depth but narrower scope. In the strong band (> 7.5), the anchors are topically distant.

**Round 2 narrowing:** New anchors within the bracket confirmed placement. "Interaction Asymmetry" (7.00) from the same research lineage is the closest comparison — the paper under review extends its framework with the novel asymmetry proof and has more extensive experiments. "Provable Compositional Generalization" (7.33) remains the ceiling anchor given similar limitations but more careful framing.

**Final score reasoning:** The paper under review is slightly above cCl10IU836 (7.00) due to its stronger theoretical contribution (the asymmetry proof) and more extensive experiments, but slightly below 7VPTUWkiDQ (7.33) due to the overclaiming in the title. The core theoretical contribution is genuinely novel and well-supported; the experiments are well-designed and validate the theory. The major weakness (title overclaiming, missing pretrained encoder analysis) is real but does not invalidate the contribution. Score: 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
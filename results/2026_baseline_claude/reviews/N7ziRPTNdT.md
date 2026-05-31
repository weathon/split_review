## Summary

The paper investigates whether compositional generalization in visual perception can be achieved by non-generative (encoder-based) or requires generative (decoder-based) approaches. Building on prior identifiability theory for compositional data models, the authors formally analyze the function class structure of generators (F_int) and their inverses (G_int), proving that constraining encoders to G_int is generally infeasible in high-dimensional image settings while constraining decoders to F_int is architecturally and regulatorizationally straightforward. They propose gradient-based search and generative replay as practical strategies for OOD decoder inversion, and empirically validate their claims on the PUG benchmark, demonstrating that non-generative models frequently fail compositionally while generative methods with search and replay show consistent OOD improvements.

---

## Strengths

- **Novel and technically sound theoretical results**: Theorem 3.2 establishes that when d_x ≥ d_z³ (easily satisfied for images), the Jacobian and Hessian of any g ∈ G_int can be arbitrary at any point, eliminating the structured form that might otherwise be enforced through regularization or architecture. This is a genuinely new result that rigorously explains why encoder-side constraints are ill-posed, since the structure persists only on the (OOD-unobserved) data manifold tangent space (Eq. 3.4).

- **Principled asymmetry argument connecting theory to practice**: The paper cleanly explains why the constraint Eq. 3.1 on decoders is coordinate-aligned and data-independent (hence universally enforceable), while the analogous constraint Eq. 3.4 on encoders is manifold-dependent and requires knowledge of X_OOD—which is unavailable by definition. This is the crux of the theoretical contribution and it is stated clearly.

- **Systematic empirical study with controlled and diverse settings**: Testing across five pretrained base encoders (DINOv1, I-JEPA, CLIP, DINOv2, SigLIP2) plus a from-scratch ViT, three distinct ID/OOD splits (Background, Texture, Object), and ablations over supervision, slot encoding, and search/replay provides a comprehensive picture. The clean finding that PUG-Object (n=0, no slot interactions) is easy for all methods while PUG-Background (n=1, object-background interaction) is hard for non-generative methods from scratch directly mirrors the theoretical predictions.

- **Connection to causal/anti-causal learning**: Section 6 frames the results as a formal justification for Kilbertus et al.'s heuristic about generalization being easier in the causal direction—this enriches both sides of the connection and adds independent scientific value.

---

## Weaknesses

### Fatal
None.

### Major

- **The theoretical condition d_x ≥ d_z³ is unstated in terms of what it means for common models.** Theorem 3.2 requires d_x ≥ d_z³. The paper never explicitly checks or discusses when this is satisfied for typical vision settings. For a latent dimension d_z of, say, 20 (e.g., K=4 slots of 5 dims), d_z³ = 8000, which is well below standard image dimensions (~150K for 224×224 RGB). But readers working in settings with larger latent dimensions need guidance, since the result becomes vacuous if d_x < d_z³. At minimum, a concrete numerical example anchoring the condition to the experimental setup would be necessary.

- **Approximate enforcement of F_int is not theoretically analyzed.** The paper argues that constraining a decoder to F_int is "straightforward" and implements this via a cross-attention Transformer with a regularization term on attention weights (Section 5.1, Decoders). However, this is an approximation to the exact constraint (Eq. 3.1), not an exact enforcement. The gap between exact membership in F_int and approximate regularization is never analyzed—neither through quantification of how well the regularization approximates the constraint nor through its effect on the identifiability guarantee (Eq. 2.5). This leaves an important assumption unvalidated in both theory and experiment.

- **Limited experimental scale and domain.** All experiments use PUG, a synthetic 3D-rendered dataset with ≈20,000 images and simple concept compositions (10 backgrounds, 32 animals, a handful of textures). The paper's core claim—that generative methods outperform non-generative ones on compositional generalization—is demonstrated only in this restricted setting. The acknowledged gap between PUG's simplicity and real-world image complexity weakens the practical significance of the empirical findings, especially given that the core thesis concerns "human-level visual perception."

### Minor

- **Comparison fairness for generative vs. non-generative methods**: Generative methods in Fig. 6 apply replay and search on top of the same pretrained base encoders used by non-generative methods in Fig. 5. This conflates the encoder pretraining contribution with the generative inversion contribution. A more controlled comparison—e.g., using identical base encoders with and without the generative inversion step—would sharpen the attribution.

- **No analysis of search convergence or failure modes**: The gradient-based search in Eq. 4.3 requires solving a non-convex optimization, initialized by the encoder. The paper reports that search consistently improves performance but provides no analysis of convergence behavior, sensitivity to initialization quality, or failure cases where the search diverges.

### Trivial

- The n=0 special case discussion (Section 3.1, last paragraph) is somewhat tangential; it complicates the narrative without adding substantial theoretical depth in the main text.

---

## Nice-to-Haves

- A sensitivity analysis of the regularization strength in Eq. 3.2 on both ID reconstruction quality and OOD generalization performance would strengthen the practical section.
- Reporting the number of gradient steps and wall-clock cost of search at inference time would be important for practitioners considering this approach.
- An experiment using an unstructured decoder (Appendix C results referenced but not discussed in the main body) incorporated into the main results would help quantify how much of the gain is attributable to the F_int inductive bias vs. simply having a decoder for inversion.

---

## Novel Insights

The central novel insight is a formal proof that the structural constraint needed to guarantee compositional generalization for encoders (Eq. 3.3/3.4) is manifold-dependent and localized to the tangent space of X, while the analogous constraint for decoders (Eq. 3.1) is globally coordinate-aligned and data-independent. This asymmetry arises specifically in the high-dimensional setting (d_x ≥ d_z³) where the inverse of an F_int generator has no universal structured form at all—an inverse can have arbitrary Jacobians and Hessians (Theorem 3.2). This explains, in a principled identifiability-theoretic framework, what prior empirical studies have observed but could not formally attribute: non-generative methods fail compositionally because their representational structure is unconstrained in exactly the OOD regions where it matters. The connection to the causal/anti-causal principle (that the causal factorization is simpler than the anti-causal one) is neatly formalized here for the first time in the context of compositional visual perception.

---

## Suggestions

- Explicitly state in the main text a concrete numerical example (e.g., K=4 slots of m=5 dims gives d_z=20, d_z³=8000 ≪ 150K image pixels) to make Theorem 3.2's applicability to typical settings immediately clear.
- Provide a brief theoretical or empirical analysis bounding how much the approximate F_int enforcement (via cross-attention regularization) deviates from the exact constraint, and whether this approximation error affects the identifiability guarantee.
- Consider adding one experiment on a dataset with more diverse concept interactions (e.g., multi-object scenes from CLEVR or ShapeNet) to partially bridge the gap to real-world settings.
- In the discussion, explicitly address whether SigLIP2's strong non-generative OOD performance (Fig. 5) is consistent with the theory—does web-scale pretraining provide an implicit generative prior, or does it simply encounter most concept combinations in training data?

---

## Score and Decision

The paper makes a genuine theoretical contribution by proving a formal asymmetry between generator and inverse-generator function class structures that explains why compositional generalization guarantees are achievable for generative methods but not for non-generative ones. The theoretical results are technically non-trivial, the empirical study is systematic, and the practical implications (search and replay) are directly motivated by the theory and empirically effective. The primary weaknesses—limited experimental scope and an unvalidated approximation gap between exact F_int constraints and the practical decoder regularization—are real but do not invalidate the core theoretical claims or the experimental conclusions in the studied setting.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
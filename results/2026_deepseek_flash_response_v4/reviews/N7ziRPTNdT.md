## Summary

This paper provides a theoretical and empirical analysis of compositional generalization for generative (decoder-based) vs. non-generative (encoder-based) approaches to visual perception. The main theoretical contribution (Theorem 3.2) proves that when the ambient image dimension is large relative to the latent dimension, the derivative constraints needed to guarantee OOD identifiability for encoders depend on the unknown geometry of the data manifold, making enforcement infeasible — in contrast to decoders, where the same constraints are global and axis-aligned. Empirically, on the PUG photorealistic dataset, the paper shows that non-generative methods often fail at compositional generalization (especially without large-scale pretraining), while generative methods using search and generative replay yield consistent improvements in OOD accuracy across multiple pretrained backbones.

## Strengths

- **Theorem 3.2 and the formal asymmetry between F_int and G_int (Sec. 3.1).** The proof that when d_x >= d_z^3, the first and second derivatives of inverse generators in G_int can be arbitrary matrices (up to measure zero) provides a novel formal basis for why constraining encoders is fundamentally harder than constraining decoders. The result showing that the only remaining structure is projected onto the unknown data manifold (Eq. 3.4) directly motivates why *guaranteeing* compositional generalization for non-generative methods is infeasible. This contrasts cleanly with decoders in F_int, where the same constraints are global and axis-aligned (Eq. 3.1–3.2).

- **Controlled empirical validation of the n=0 special case (Sec. 5.2, Fig. 5C).** On PUG-Object, where concepts do not interact (the n=0 limiting case identified in Sec. 3.1), non-generative methods achieve near-perfect OOD accuracy despite no explicit structural constraints. This provides corroborating evidence for the theoretical analysis: the theory predicts that G_int becomes more structured when n=0, and the experiment bears this out. The contrast between PUG-Object (near-perfect) and PUG-Background/PUG-Texture (poor) isolates concept interaction as the key difficulty.

- **Systematic empirical evaluation across diverse pretrained backbones and compositional splits (Sec. 5.2, Figs. 5 and 6).** The paper evaluates five pretrained encoders (DINOv1, DINOv2, CLIP, SigLIP2, I-JEPA) plus a from-scratch ViT-S on three distinct compositional splits from the same photorealistic dataset. On PUG-Background, generative methods with replay + search substantially improve OOD accuracy across all backbones. On PUG-Texture, where replay cannot be applied, search alone yields consistent gains. This breadth rules out the explanation that results hinge on a single model or split.

## Weaknesses

### Fatal

None.

### Major

- **Central claim is overstated relative to the evidence.** The title "Generation is Required for Data-Efficient Perception" asserts necessity, but the paper's own evidence does not support this unqualified claim:
  - On PUG-Object (n=0), *all* non-generative methods achieve near-perfect OOD accuracy without any decoder inversion (Fig. 5C).
  - On PUG-Background, large-scale pretrained SigLIP2 reaches ~80% OOD accuracy without generative techniques (Fig. 5A) — far from perfect but still meaningful compositional generalization.
  - The theoretical result (Theorem 3.2) shows that *guaranteeing* compositional generalization via explicit encoder constraints is infeasible; it does *not* show that non-generative methods cannot generalize in practice. The PUG-Object results demonstrate that optimization can sometimes discover the right solution implicitly.
  
  The paper should soften its central claim to something like "generation provides more reliable compositional generalization" or "generation is required for *guaranteed* compositional generalization" with systematic hedging.

- **The practical link between theory and experiments is unvalidated.** The theory (Sec. 3) says compositional generalization requires the decoder to be in F_int. The experiments (Sec. 5.1) use a cross-attention Transformer with regularization described only as an "approximate" constraint to enforce this structure. No evidence is presented that this decoder actually lies in F_int or is close enough for the theoretical guarantees to apply. The paper mentions unstructured decoders in §C (deferred to appendix) but does not provide a head-to-head comparison showing that structured decoders benefit more from search/replay than unstructured ones. The empirical improvement from generative methods could come from search/replay being useful search strategies *regardless* of whether the decoder satisfies the F_int constraints.

### Minor

- **No statistical uncertainty reported for main experimental results.** The paper reports OOD accuracy for the "best-performing combination" of slot encoder and fine-tuning choice per base encoder, without error bars or variance across random seeds (Figs. 5, 6). With ~20k images and multiple training components, variance should be reported to assess the reliability of the reported improvements.

- **Theoretical results for n>1 are promised but not delivered.** The paper states (line 95) that "similar statements can in principle be derived for higher order derivatives for the case n > 1" but does not provide such derivations. This weakens the generality of the main theoretical claim, which is formally stated only for n=1.

- **No ablation of the search component.** The paper does not compare random initialization vs. encoder initialization for gradient-based search (Sec. 4.1), making it unclear how much of the improvement comes from the encoder's "System 1" guess vs. the gradient-based refinement itself.

### Trivial

None.

## Nice-to-Haves

- Report key accuracy numbers in text (not just in figures) to allow readers to assess effect sizes directly without zooming into figures.
- Discuss whether the threshold d_x >= d_z^3 is an artifact of the proof technique or reflects a natural geometric bound, since its practical import is unclear when d_z is unknown.
- Add an ablation comparing random initialization vs. encoder initialization for gradient-based search.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- **Criticism that the abstract conflates data efficiency with OOD generalization**: The paper's framing explicitly connects compositional generalization to data efficiency (Sec. 1, lines 27–29: "Compositional generalization... is thus essential for realizing the data efficiency of human perception"). The experiments compare from-scratch vs. pretrained models, directly addressing data efficiency. This is a standard framing in the literature.
- **Criticism that PUG-Object results "undermine the theoretical pessimism" about non-generative methods**: The paper explicitly discusses n=0 as a special case where G_int has more structure and acknowledges this makes compositional generalization "fundamentally easier" (Sec. 3.1, lines 127–128; Sec. 5.2, lines 215–216). The theory makes different predictions for n=0 vs. n≥1, so this result is *consistent* with, not contradictory to, the theory.
- **Criticism that search/replay techniques are not novel**: The paper does not claim novelty for these techniques. They are drawn from prior work (Prabhudesai et al., Wiedemer et al.) and presented as strategies motivated by the theoretical analysis. A methods paper does not need to invent new techniques.
- **Reproducibility concern about gradient search steps not being reported**: Hyperparameters such as gradient steps for search would be in Appendix B, which is stripped by the parser. Cannot evaluate from available text.
- **Criticism that the caption says replay "cannot be applied" on PUG-Texture**: The paper explicitly and correctly acknowledges this limitation (Sec. 5.2, lines 219–220). This is transparency, not a weakness.
- **Criticism about "missing quantitative backbone" / qualitative descriptions**: Figures contain the actual accuracy values; the text describes qualitative trends, which is standard practice for papers with figures.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Revise the title and central claim** to accurately reflect what the evidence supports. Options: "Generation Provides More Reliable Compositional Generalization for Visual Perception" or "Generation is Required for Guaranteed Compositional Generalization."

2. **Validate the theoretical mechanism empirically**: either (a) show that the regularized decoder approximately satisfies the F_int derivative structure (e.g., measure whether Eq. 3.1 holds for the learned decoder on in-domain data), or (b) compare structured vs. unstructured decoders head-to-head to verify that the F_int structure is responsible for the observed improvements from search/replay.

3. **Add error bars or variance information** to the main experimental results (Figs. 5, 6) to assess reliability.

4. **Ablate the search component** by comparing random initialization vs. encoder initialization for gradient-based search, to quantify the contribution of each.

---

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| hv8l922Ad7.md (disentanglement metrics) | 3.40 | R1 | Much weaker — limited scope, no theory |
| JNZ3Om6NPS.md (LLM limitations) | 2.00 | R1 | Much weaker — unsubstantiated claims |
| 7VPTUWkiDQ.md (Provable CG) | 7.33 | R1 | Directly comparable topic, cleaner narrative; our paper has more realistic experiments but overclaims |
| H98CVcX1eh.md (Modular solutions) | 6.50 | R1/R2 | Similar quality; our paper better presented, similar ambition |
| dggRphAcCj.md (GeoCon) | 6.33 | R1 | Less novel than our paper |
| s1zO0YBEF8.md (Dynamics of Concept Learning) | 6.50 | R2 | Comparable; our paper has fewer validity concerns about experimental setup |
| UVSKuh9eK5.md (CLIP CG) | 5.67 | R2/R3 | Weaker — empirical only, no theoretical contribution |
| 22ywev7zMt.md (SSL OOD) | 5.67 | R3 | Weaker — limited scope |
| hKMPz3wkPV.md (Formal theory of comp.) | 6.75 | R2 | Comparable score, rejected due to fundamental technical flaws our paper doesn't share |
| 55uj7mU7Cv.md (Identifiable UDT) | 6.25 | R3 | Different topic (domain translation) but comparable quality |
| 7oT1X8xjIk.md (Identifiability) | 5.80 | R3 | Weaker — limited experiments |

**Round-1 bracket:** 5.0 – 7.5 (the paper sits between weak anchors at ~3.0 and strong anchors at ~8.0)

**Narrowing:** After comparing against anchors in the 5.5–7.5 range, the paper is stronger than empirical-only papers (~5.67) and papers with fundamental technical flaws, but weaker than the most directly comparable "Provable CG" paper (7.33) due to overclaiming and the unvalidated theory-experiment link. The paper is comparable to the 6.50-level anchors (Discovering modular solutions, Dynamics of Concept Learning) in overall quality, but the overclaiming issue is a distinctive weakness that prevents it from reaching the 6.5+ tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
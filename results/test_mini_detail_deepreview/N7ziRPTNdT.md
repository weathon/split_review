Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper investigates whether generative (decoder-based) or non-generative (encoder-based) approaches are necessary for compositional generalization in visual perception. The authors formalize the constraints needed to guarantee compositional generalization, prove theoretically that enforcing these constraints on encoders is generally infeasible (while straightforward for decoders), propose practical generative inversion algorithms (gradient-based search and generative replay), and empirically validate on PUG datasets that generative methods significantly outperform non-generative ones on out-of-domain compositional splits.

## Strengths
1. **Theorem 3.2 provides a concrete mathematical result showing the derivative structure of inverse generators becomes unconstrained when \(d_x \gg d_z\).** The theorem proves that when \(d_x \geq d_z^3\), the first- and second-order derivatives of inverse generators can be arbitrary matrices (up to measure zero). This is a non-trivial theoretical contribution that formally grounds the intuition about why constraining encoders is harder than constraining decoders.

2. **Clear contrast between the axis-aligned structure of \(\mathcal{F}_{\text{int}}\) and the manifold-dependent structure of \(\mathcal{G}_{\text{int}}\) (Eq. 3.1 vs Eq. 3.4).** The paper shows that decoder constraints are global and coordinate-aligned (Eq. 3.1), while encoder constraints require projection onto the tangent space of the data manifold (Eq. 3.4), which is unknown for OOD regions. This contrast is the paper's theoretical centerpiece and is well articulated.

3. **Empirical validation on photorealistic PUG data showing generative methods (decoder + search/replay) consistently improve OOD accuracy by 30–50 percentage points over their non-generative counterparts.** On PUG-Background, from-scratch ViT-S/36 goes from ~20% (non-generative) to >80% (generative with replay+search). This holds across multiple base encoder backbones. The use of photorealistic controlled data (PUG) is a strength over purely synthetic evaluations common in this area.

4. **Practical inversion algorithms: gradient-based search (Sec. 4.1) and generative replay (Sec. 4.2) are clearly described and reproducible.** The paper connects these to "System 1 / System 2" reasoning concepts and provides pseudocode references.

5. **Nuanced handling of the \(n=0\) special case and PUG-Object results.** The paper acknowledges when non-generative methods can succeed (concepts without interactions), which adds depth rather than detracting from the main claim.

## Weaknesses

### Fatal
None.

### Major
1. **No error bars, confidence intervals, or variance reporting in any experimental figure.** The bar charts in Fig. 5 and Fig. 6 appear to show single numbers with no indication of variability across runs, random seeds, or data splits. Given the relatively small dataset sizes (~20k images) and the use of hyperparameter selection ("best-performing combination of slot encoder and fine-tuning choice"), the reader cannot assess the reliability or statistical significance of the reported improvements. This is a significant omission for an empirical paper making comparative claims.

2. **The "data efficiency" claim in the title is not directly tested.** The paper argues generation is needed for data-efficient perception, yet no experiment varies the amount of ID training data. The evidence for "data efficiency" is indirect: from-scratch non-generative methods fail while generative methods with replay/search succeed *at the same data scale*. But a direct test (varying dataset size, plotting learning curves) would be needed to support the data-efficiency framing. As it stands, the paper shows that generative methods improve OOD accuracy given a fixed dataset, not that they are fundamentally more data-efficient. This is a mismatch between the title/framing and the actual experimental evidence.

### Minor
1. **The theoretical argument that constraining an encoder to \(\mathcal{G}_{\text{int}}\) is "infeasible" is suggestive but not a formal impossibility proof.** The paper uses hedging language ("suggests", "generally infeasible", "tends to be infeasible") which is appropriate, but the overall narrative — reinforced by the title and Fig. 1 — pushes a harder claim. Theorem 3.2 shows derivatives can be arbitrary *locally*, but this does not preclude the existence of a practical learning procedure that implicitly yields a \(\hat{g} \in \mathcal{G}_{\text{int}}\) after training on ID data (e.g., an architecture whose inductive bias happens to work, or a regularizer that leverages ID structure in ways not requiring explicit OOD knowledge). The paper acknowledges this indirectly in the "Takeaways" paragraph ("whether compositional generalization occurs depends on whether the optimization process happens to avoid converging to such a solution"), but this undercuts the "infeasible" framing. The paper would be strengthened by explicitly tempering the infeasibility claim to match the actual logical status of the argument.

2. **Missing comparison between the best generative and best non-generative methods in a single aligned plot.** Fig. 5 (non-generative) and Fig. 6 (generative) are on different scales and use different y-axis ranges, making visual comparison difficult. The best non-generative method (SigLIP2 supervised, ~80% on PUG-Background) is not directly compared against the best generative method (SigLIP2 + replay/search, which appears to also be high). Given the paper's central claim about generative superiority, this comparison should be direct and explicit. The paper *does* provide the underlying data for comparison, but the presentation makes it harder than necessary.

3. **The decoder architecture (regularized cross-attention Transformer) is described but not ablated in the main text.** The paper mentions in passing that results with unstructured decoders are in Appendix C, but does not bring key ablation findings into the main paper. Since the decoder design is critical to the generative method's success, the reader needs to see evidence that the structured decoder matters.

4. **Computational cost of search and replay is not discussed.** Search requires multiple gradient steps per test image; replay requires training an encoder on synthetic OOD data. The paper should acknowledge the compute/accuracy trade-off.

### Trivial
- The figure captions in the extracted text are duplicated (parser artifact, not author error).
- The paper refers to "Sec. 5.2" results before introducing the section properly, but this is a minor organizational issue.

## Nice-to-Haves
- Adding a controlled experiment that varies ID training data size (e.g., 100, 500, 2000, full) and plots OOD accuracy for both a generative and non-generative method would directly test the data-efficiency claim and significantly strengthen the paper.
- Error bars on all experimental figures.
- Direct comparison of SigLIP2 supervised vs SigLIP2 generative (replay+search) in a single figure or table with aligned axes.
- Ablation of the decoder (structured vs unstructured) brought into the main paper.

## Removed Points
Weaknesses removed from the harsh critic's review with justification:

- **"The comparison between generative and non-generative methods is not properly controlled because Fig. 5 includes supervised methods while Fig. 6 uses unsupervised."** — This criticism misunderstands the paper's design. Fig. 6 *uses the same autoencoders from Fig. 5* and compares "w/o replay" (same unsupervised non-generative baseline) against "with replay" and "with replay+search." The within-figure comparison (Fig. 6) is properly controlled. The broader claim about generative vs non-generative is about the paradigm, not about specific training objectives. The paper also includes supervised non-generative methods to show that even with labels, non-generative methods struggle.

- **"The \(n=0\) case undermines the general claim."** — The paper explicitly handles \(n=0\) as a special case where \(\mathcal{G}_{\text{int}}\) is more structured, and uses PUG-Object results to confirm this prediction. This is a feature, not a flaw: the paper shows *when* the asymmetry does not arise, which adds nuance.

- **"The diffeomorphism assumption is strong and not fully justified."** — This is a scope-of-assumptions concern, not a specific weakness. The paper acknowledges this limitation in the Discussion section. Every theoretical paper in this area (Brady et al., Lachapelle et al.) makes similar assumptions.

- **"Missing detail about how encoder initializes search (full latent space vs only certain slots)."** — This is a minor implementation detail appropriate for the appendix.

- **"No comparison with diffusion-based classifiers."** — This is a nice-to-have extension, not a weakness. The paper's contribution is about the *autoencoder + search/replay* paradigm, not about all possible generative methods.

- **"The 'from scratch' comparison is not explicitly noted as using the same ViT-Small."** — The paper says "from scratch generative method... uses a ViT-S/36 base encoder trained from scratch." This is sufficiently clear.

## Novel Insights
None beyond the paper's own contributions. The reviews largely affirm the paper's own framing and identify known gaps (error bars, data efficiency testing) rather than uncovering unexpected issues.

## Suggestions
1. Add error bars / variance reporting to all experimental figures.
2. Either add a direct data-efficiency experiment (varying ID dataset size) or retitle the paper to remove the "data-efficient" claim from the title, replacing with a more accurate framing (e.g., "Generation is Required for Compositional Generalization in Visual Perception").
3. Create a single comparison figure or table directly comparing SigLIP2 supervised (best non-generative) against SigLIP2 + replay/search (best generative) on the same axis scale.
4. Temper the "infeasible" language in the title/abstract/introduction to match the hedged language in the body ("suggests", "generally not feasible").
5. Bring decoder ablation (structured vs unstructured) into the main text.

## Score and Decision

Let me calibrate against the anchors.

**Round 1 bracket:** The paper sits between the weak anchors (2.0–3.33, all rejected, clearly weaker papers) and the strong anchors (7.6–8.0, all accepted, clearly stronger papers). Narrowest plausible range: 5.0–7.5.

**Round 2 narrowing anchors:**

- **Provable Compositional Generalization for Object-Centric Learning** (7.33, Accept) — Very closely related (identifiability theory for compositional generalization in autoencoders). That paper has cleaner theoretical guarantees (provable identifiability), cleaner experiments with error bars, and a more modest title. The paper under review is *weaker* than this anchor: it lacks error bars, has a less rigorous theoretical claim, and overreaches in its title. However, it compensates somewhat with more realistic data (PUG vs synthetic) and practical algorithms (search and replay). On balance, the paper under review is ~0.5–1.0 points below this anchor.

- **Interaction Asymmetry** (7.00, Accept) — From the same research line (Brady et al. framework). Similar structure (theory → method → synthetic experiments), similar decoder architecture. The paper under review has a different focus (generative vs non-generative comparison rather than disentanglement theory), uses more realistic data, but lacks the empirical rigor of the Interaction Asymmetry paper (which at least reports some metrics across runs). The paper under review is slightly weaker (~0.5 points).

- **Discovering modular solutions** (6.50, Accept) — Different methodology (modular hypernetworks) but same compositional generalization problem. That paper has both theory and experiments, with acknowledged clarity issues. The paper under review is roughly comparable in overall quality: both have genuine contributions but notable weaknesses.

- **Dynamics of Concept Learning** (6.50, Accept) — Theoretical analysis of compositional generalization dynamics in diffusion models. Similar mix of theory and experiment. The paper under review is comparable.

**Final score determination:** The paper sits between 6.0 and 6.5. Compared to the 7.33 anchor (Provable Compositional Generalization), the paper is weaker in theoretical rigor and empirical completeness. Compared to the 6.50 anchors, it is comparable. The missing error bars, the untested "data efficiency" claim, and the overreach in the title/infeasibility framing prevent it from reaching the 7.0+ tier. I place it at **6.0**, at the lower end of the acceptable range — a solid borderline accept with a clear path to improvement.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
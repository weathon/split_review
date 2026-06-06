## Summary

This paper operationalizes the Linear Representation Hypothesis (LRH) in DINOv2 using a stable Sparse Autoencoder (SAE) with a convex-hull constraint, yielding a 32,000-unit concept dictionary from 1.4M ImageNet images (R² > 88%). Building on this dictionary, the paper makes three contributions: (1) demonstrating task-specific concept specialization ("Elsewhere" concepts for classification, border detectors for segmentation, monocular cue families for depth estimation); (2) performing geometric diagnostics showing the dictionary departs from the idealized LRH in several quantifiable ways; and (3) proposing the Minkowski Representation Hypothesis (MRH), grounding it in multi-head attention algebra and providing preliminary empirical signals consistent with it.

---

## Strengths

- **Large-scale, reproducible concept dictionary:** The stable SAE trained with a convex-hull constraint on 1.4M images yields 32,000 in-distribution concept atoms with R² > 88% (Section 2), making this the largest interactive interpretability demonstration for a vision foundation model. The explicit $D \in \text{conv}(A)$ constraint is a substantive design choice that addresses the well-known instability problem in naive SAEs.

- **Concrete, multi-method task-specialization evidence:** The paper goes beyond visualization. "Elsewhere" classification concepts are validated via causal masking (Figure 2 left — activation vanishes when the object is removed). Segmentation concepts form a visually and quantitatively tight cluster in embedding space (Figure 10), with higher-than-average absolute cosine similarity and faster eigenspectrum decay than random subsets (Figure 11). Depth concepts are disambiguated through controlled image perturbations (median blur, edge-preserving smoothing, high-pass filter), with three UMAP-visible clusters corroborated by bar-chart perturbation response patterns (Figure 3).

- **Quantitative departures from LRH are rigorously characterized:** Section 4 assembles multiple independent metrics: heavier-tailed cross-dot-product distribution versus random/Grassmannian baselines (Figure 4A), sharply decaying singular-value spectrum of D (Figure 4B), low Hoyer scores confirming distributed rather than neuron-aligned atoms (Figure 4C), weak correlation between co-activation (Z^T Z) and geometric affinity (DD^T) (Figure 13). The algebraic explanation in footnote 1 for the weak-but-positive correlation is elegant. Together, these build a genuine empirical case that pure sparse near-orthogonal feature packing is an incomplete account.

- **Positional subspace analysis is methodologically clean:** The paper trains linear decoders to extract positional subspaces layer-by-layer, documents their compression to ~2D in final layers (Figure 6), and shows that projecting tokens orthogonally to the positional subspace leaves the PCA structure largely unchanged (Figure 25), ruling out the confound that per-image smoothness is an artifact of position encoding.

- **Non-identifiability result (Proposition 2) is a practically useful theoretical contribution:** Formalizing that Minkowski decomposition is ill-posed from final activations alone—and deriving the implication that intermediate signals (attention weights, per-head outputs) are necessary—gives the interpretability community a concrete structural motivation for architecture-aware probing methods.

---

## Weaknesses

### Fatal
None.

### Major

- **Proposition 1 is algebraically trivial, yet is framed as the primary theoretical foundation of MRH.** Multi-head attention by definition computes a softmax-weighted convex combination of values per head, and summing across heads produces a Minkowski sum. The paper itself notes "This mechanism is elementary" (Section 6). Stating this as a formal proposition does not constitute an empirical discovery about how DINOv2's *learned* representations organize. The scientifically substantive question — whether the learned representations *actually* exhibit the semantic tile structure posited in Definition 1 — is not addressed by Proposition 1. The paper presents MRH as a "working hypothesis whose testable predictions we outline," which is honest framing; however, the abstract states "Multi-head attention directly implements this construction" in a way that implies evidential support stronger than "by definition, softmax produces convex weights." The framing should more clearly distinguish the algebraic fact (Prop 1) from the empirical hypothesis (do tiles align semantically?).

- **The three "empirical evidences" in Section 6 are consistent with MRH but are not specific to it.** (a) Piecewise-linear geodesics staying near the data support (Figure 26 left) is equally consistent with any smooth low-dimensional manifold, not specifically polytope-face traversal. (b) Archetypal Analysis with ~10 archetypes per image matching SAE reconstruction (Figure 26 middle) shows low effective dimensionality, but this does not establish that the tiling follows head-aligned polytopes. (c) Block structure in the Gram matrix of codes (Figure 26 right) is consistent with any clustering structure, not specifically the head-indexed tile partition of Definition 1. None of these tests the criterion that blocks align with the head tile partition {T_i}. Given that Proposition 2 simultaneously proves the decomposition is non-identifiable from activations alone, the combination leaves MRH empirically under-determined: the hypothesis cannot be confirmed or falsified with the presented evidence.

### Minor

- **The abstract uses stronger language for the "Elsewhere" mechanism than the evidence supports.** The abstract describes "object negation" and the introduction uses "conditional negation" as near-settled findings. The body text is appropriately hedged: "may support classification by outlining boundaries, encoding contrast, or distributing evidence" (Section 3), and Figure 2's caption acknowledges "another interpretation being distributed off-object evidence." The simpler hypothesis — that these concepts encode background-contrast features dependent on object-border presence — is equally consistent with the causal masking result (activation vanishing when the object patch is removed). The abstract and introduction-level framing should be brought in line with the body's hedging.

- **The alignment score that drives the entire task-specialization analysis (Section 3) is defined only in a stripped appendix (Appendix C.1), with no definition in the main text.** The paper acknowledges "the precise definition and its theoretical justification are deferred to Appendix C.1." Because this score is the load-bearing metric for the paper's core empirical claim about task-specialized concept recruitment, at least a one-sentence definition should appear in the main body so readers can evaluate whether the observed specialization could be an artifact of the metric's design.

### Trivial

- The depth estimation claim that "DINO internally encodes a diverse, interpretable set of monocular depth cues" (Section 3) is stated more broadly than the perturbation evidence strictly supports. Perturbations simultaneously change many image features, making it difficult to attribute cluster membership uniquely to named monocular cues. This is appropriately hedged elsewhere ("some concepts mix cues") but the headline claim could be qualified.

---

## Nice-to-Haves

- An ablation over the SAE hyperparameters (k = 8 active codes, c = 32,000 atoms) would strengthen confidence that the downstream task-specialization findings are robust rather than artifacts of those particular choices.
- A direct test of whether the block structure in the Gram matrix of codes (Figure 26 right) aligns with head-indexed partitions specifically (not just any clustering) would substantially strengthen MRH's empirical grounding and is the natural next step given the theoretical setup.
- Verifying "Elsewhere" concepts across more image classes and testing the background-contrast alternative (by measuring whether these concepts respond to edge-presence rather than object-presence) would turn a qualitatively suggestive finding into a more rigorous mechanistic claim.
- Checking whether the task-specific concept clusters identified in Section 3 are consistent across different linear probe architectures or training seeds would rule out the concern that the recruitment pattern is an artifact of the probing method.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: non-identifiability (Prop 2) undercuts MRH as a scientific hypothesis.** Removed as overstated. The paper explicitly labels MRH a "working hypothesis" and Proposition 2 is presented as a *practical implication* motivating structure-aware tools — not as a self-undermining result. The framing is transparent, and the point becomes a useful design principle rather than a fatal tension.
- **Harsh critic: co-activation/geometry correlation (Figure 13) as a weakness.** Removed — this was identified by the harsh critic as a *strength* ("the finding… is interesting and the algebraic explanation in footnote 1 is elegant"), and the paper analyzes it carefully. Not a weakness.
- **Harsh critic: tail-distribution SAE performance not reported.** Removed as a speculative concern. The R² > 88% aggregate is consistent with prior work; the possibility of lower performance on rare images is a generic concern for any trained model and is not anchored to a specific failure in the paper.
- **Harsh critic: k=8 and c=32,000 not ablated → downstream findings may be sensitive.** Demoted to Nice-to-Have. This is a methods nitpick for an empirical interpretability paper; the chosen values are consistent with prior work and the paper's primary claims are about what concepts *are*, not about optimal dictionary design.
- **Strength finder: "MRH empirically tested" (Appendix K, Figure 26 as direct evidence).** Retained but substantially weakened in Strengths to reflect that Figure 26 evidence is "consistent with" rather than specifically tests MRH, in light of the verified Major weakness above.

---

## Novel Insights

The most genuinely novel finding is the "Elsewhere" concept — a recurring feature class that fires off-object, is conditionally suppressed on the object itself, and disappears under causal masking of the object. If the conditional negation interpretation is correct (rather than the border-contrast alternative), this would be a qualitatively new type of learned representational primitive: a token-level signal whose semantic content is defined by the *absence* of an object at its location rather than its presence. The observation that such concepts systematically mislead attribution maps (which assume features fire where they matter) is a practically important finding for the interpretability tooling community. The clean analytic separation of positional from semantic structure (Section 5) is also a methodologically useful contribution: the demonstration that leading PCA components survive orthogonalization to the positional subspace provides a reusable diagnostic for separating position coding from semantic content in ViT-class models.

---

## Suggestions

1. **Redesign one MRH-specific test using per-head outputs.** Test whether the block structure in the Gram matrix of codes aligns specifically with head-indexed partitions (comparing against permuted-head assignments as a null). This is the minimal experiment that would differentiate MRH from a generic low-dimensional manifold account.
2. **Disambiguate the "Elsewhere" mechanism.** Run a targeted experiment: measure whether "Elsewhere" concepts respond to object-boundary contrast patches (cropped border regions without the object interior) versus blank backgrounds. If they fire to border contrast regardless of whole-object context, the simpler background-contrast explanation holds; if they require global object context, conditional negation is more defensible.
3. **Provide a one-sentence definition of the alignment score in the main text of Section 3.** Even a compact formula in the form "concept $i$'s contribution to task $t$ is measured by $\langle d_i, w_t \rangle^2$" (or whatever the actual formula is) would make the core task-specialization claim self-contained and evaluable without the appendix.
4. **Recalibrate the abstract's framing of MRH from "implements this construction" to "is algebraically consistent with this construction; whether the learned organization exhibits the semantic tile structure is an open empirical question."** This brings the abstract in line with the body's more careful treatment without diminishing the contribution.

---

## Assessment on Key Axes

**Originality:** Moderate-to-high. The SAE-based concept extraction is adapted from prior work, but applying it at this scale to a vision foundation model with systematic task-specialization analysis and the MRH formalization is a meaningful new contribution. The "Elsewhere" concept class and monocular cue family analysis are qualitatively novel findings.

**Importance of research question:** High. DINOv2 underpins a broad ecosystem of downstream vision tasks, and understanding its internal organization directly impacts how practitioners use and interpret the model.

**Claims supported by evidence:** Mixed. The empirical claims about task-specialization (Sections 3–5) are well-supported by converging quantitative evidence. The MRH theoretical claim (Section 6) is supported only by evidence consistent with but not specific to it.

**Soundness of experiments:** Good for Sections 3–5; the controlled perturbation methodology for depth cues, the causal masking for "Elsewhere" concepts, and the spectral/geometric analyses of the dictionary are all appropriately designed. Section 6 experiments are exploratory and should be presented as such.

**Clarity of writing:** Generally clear. The narrative is well-structured across three distinct parts, figures are informative, and hedging in the body text is mostly appropriate. The abstract overclaims slightly relative to the body.

**Value to the research community:** High for the empirical contributions (task-specialization analysis, 32k concept dictionary release, positional structure analysis). Moderate for MRH as currently formulated; it would increase substantially if the specific empirical predictions were tested.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>
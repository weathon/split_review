Now I have a comprehensive understanding of the paper and the reviews. Let me construct the final consolidated review.

## Summary

This paper investigates whether generative (decoder-based) or non-generative (encoder-based) approaches are better suited for compositional generalization in visual perception. The authors formalize the problem using the function class $\mathcal{F}_{\text{int}}$ (additive/polynomial generators) and prove a key structural asymmetry: constraining an encoder to belong to the inverse class $\mathcal{G}_{\text{int}}$ is infeasible in high-dimensional settings because the required constraints depend on the unknown geometry of the out-of-domain data manifold (Theorem 3.2), whereas constraining a decoder to $\mathcal{F}_{\text{int}}$ is straightforward via axis-aligned architectural or regularization biases. They then propose two practical inversion strategies—gradient-based search and generative replay—and demonstrate on PUG datasets that non-generative methods (including supervised and VAE-based approaches) often fail at compositional generalization, while the same models succeed when the decoder is inverted OOD.

## Strengths

- **Theorem 3.2 and the structural asymmetry argument (Section 3).** The paper's core theoretical contribution is clean and non-trivial. Theorem 3.2 shows that when $d_x \geq d_z^3$, the first and second derivatives of any inverse generator $g \in \mathcal{G}_{\text{int}}$ can be arbitrary matrices (up to measure zero). This formally establishes that the diagonal Hessian condition (Eq. 3.3) cannot be enforced on an encoder for high-dimensional image data without knowledge of the OOD manifold, while the analogous decoder-side constraints (Eq. 3.1) are axis-aligned and globally enforceable. The contrast between Lemma 3.1 (where $d_x = d_z$ makes encoder constraints feasible) and Theorem 3.2 (where $d_x \gg d_z$ makes them manifold-dependent) is particularly well articulated.

- **Empirical validation with internal consistency.** The experiments on PUG datasets cleanly operationalize the theory. The three-way split (PUG-Background with $n>1$, PUG-Texture, PUG-Object with $n=0$) provides a controlled testbed. The fact that all methods achieve near-perfect OOD accuracy on PUG-Object ($n=0$, where $\mathcal{G}_{\text{int}}$ is more structured) while they frequently fail on PUG-Background/Texture ($n>1$) directly validates the theoretical prediction that the difficulty of compositional generalization for non-generative methods arises from concept interactions. This internal consistency is the strongest evidence in the experimental section.

- **Generative methods with search and replay (Figures 6, Sections 4.1–4.2).** The paper demonstrates that applying gradient-based search and generative replay to the same decoder that failed when used in the autoencoder setup yields substantial OOD improvements (20–60 percentage points on PUG-Background). This cleanly isolates the role of decoder inversion, showing that the decoder's $\mathcal{F}_{\text{int}}$ inductive bias is necessary but not sufficient—it must be actually *inverted* on OOD inputs to succeed.

- **Connection to causal/anti-causal learning (Section 6).** The paper explicitly links its results to the causal principle that the generative direction (cause→effect) is structurally simpler than the anti-causal direction, providing a formal justification for conjectures in Kilbertus et al. (2018). This contextualizes the work within a broader intellectual framework.

- **Practical algorithms.** Sections 4.1–4.2 describe implementable, well-motivated strategies (gradient-based search with encoder initialization, generative replay for encoder training on synthesized OOD data) that operationalize the theoretical framework and directly enable the empirical gains in Figure 6.

## Weaknesses

### Fatal
None.

### Major
None. The criticisms that could be read as fatal (asymmetric comparison, limited scope) are either addressed by the paper's own formalism and limitations section, or do not hold up when checked against the actual experimental design (the paper tests supervised discriminative models, contrastive models, and autoencoders; all fail without OOD inversion).

### Minor
- **Title and abstract overclaim relative to the theory's scope.** The title "Generation is Required for Data-Efficient Perception" and the abstract's framing imply a universal necessity claim. However, the theory assumes that ground-truth generators belong to $\mathcal{F}_{\text{int}}$—a specific function class that captures additive/polynomial concept interactions. While $\mathcal{F}_{\text{int}}$ is the largest class known to enable OOD identifiability, the paper does not establish that real-world visual data respects $\mathcal{F}_{\text{int}}$, nor does it prove impossibility for non-generative methods under other function classes. The Limitations section (Sec. 7) does acknowledge this, but the title and abstract do not reflect the qualification. A title like "Generation Enables Data-Efficient Compositional Generalization under $\mathcal{F}_{\text{int}}$" would better match the evidence.

- **Computational cost of search and replay is not reported.** The paper advocates for *data* efficiency but does not report the wall-clock time, number of gradient steps (search), or generated dataset size (replay) required to achieve the reported gains. If replay requires generating tens of thousands of OOD images and retraining the encoder from scratch, or if search requires hundreds of gradient steps per test image, the practical efficiency argument is significantly weakened. This is a gap even for a proof-of-concept paper.

- **The definition of "non-generative" includes autoencoders with decoders, which may confuse readers.** The paper classifies VAE-based approaches as "non-generative" because the encoder "is only constructed to invert the decoder on $\mathcal{X}_{\text{ID}}$, and not on $\mathcal{X}_{\text{OOD}}$" (line 209). While this is consistent with the paper's formalism (Eq. 2.3 vs Eq. 2.2), many readers will consider any system trained end-to-end with an image decoder as generative. The paper would benefit from a more prominent explanation that the taxonomy hinges on whether the decoder is *used* for OOD inference, not on whether a decoder exists. The supervised (purely discriminative) results in Figure 5 partially address this concern by showing that even encoder-only non-generative methods fail OOD.

### Trivial
- **No statistical significance reported.** The bar charts in Figures 5 and 6 show single values without error bars or significance tests. While single-run evaluation is common for large-scale pretrained models, the absence of any variance information makes it difficult to assess the reliability of the reported OOD accuracy differences, especially for the weaker baselines where random seed variation could matter.

## Nice-to-Haves

- **Report computational cost.** Wall-clock time for search per test image, number of search steps, and size of the replay-generated training set would substantially strengthen the practical claims. If replay requires generating a large synthetic dataset, the data efficiency framing should account for this.
- **Evaluate generated OOD image quality.** The replay method's effectiveness depends on the decoder generating realistic OOD images. A human evaluation or FID/IS comparison between generated and ground-truth OOD images would strengthen the replay argument.
- **Ablate decoder architecture more prominently.** The paper states that Appendix C tests unstructured decoders, but this result should be in the main text to demonstrate that the $\mathcal{F}_{\text{int}}$ inductive bias in the decoder, not just the inversion mechanism, is responsible for the gains. (If unstructured decoder + search also works, the central role of $\mathcal{F}_{\text{int}}$ would need re-examination.)
- **Explore non-generative baselines with test-time adaptation.** The paper could clarify its position by testing whether allowing the non-generative encoder test-time finetuning (few-shot adaptation on a handful of OOD examples) changes the outcome. The paper's theoretical argument suggests this would still face the same manifold-dependence issue.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic Issue 2 (Staged Experimental Comparison).** The claim that the comparison is "rigged by definition" does not hold up against the paper. The paper tests multiple non-generative paradigms (supervised discriminative, contrastive pretrained models, autoencoders) and the comparison follows directly from the formal framework (Eq. 2.2 vs Eq. 2.3). The supervised baselines have no decoder at all, and the VAE baselines have a decoder that is not inverted OOD—both fail. The generative methods add decoder inversion, which is the paper's thesis. The critic's suggestions (test pure discriminative classifiers, contrastive models)—the paper already does this (supervised training, CLIP, SigLIP2). This criticism misunderstands the experimental design and overstates the asymmetry.
  
- **Harsh Critic Issue 3 (Ecological Validity).** The claim that the taxonomy is "arcane" is a terminology preference rather than a substantive weakness. The paper clearly defines "generative" vs "non-generative" in terms of whether the approach learns $\hat{f}$ and inverts it, or learns $\hat{g}$ directly. The paper explains the VAE case transparently. Readers may disagree with the terminology but cannot claim it is undefined or misleading.

- **"Generally infeasible" conflating difficulty with impossibility.** The paper uses hedging language ("suggests," "tends to be infeasible," "generally infeasible") and Theorem 3.2 provides a structural argument for why the constraints are manifold-dependent and thus practically unenforceable. The paper does not claim a formal impossibility proof. The critic's point is overly semantic.

- **Missing decoder ablation (already in Appendix C).** The paper explicitly states "In § C, we also report results when using unstructured decoders which are not designed to match $\mathcal{F}_{\text{int}}$." The appendix content was stripped by the parser, not absent from the submission.

- **Strength Finder's connection to causal/anti-causal learning.** While this is a genuine connection, the paper's treatment is brief (half a paragraph in Related Work). The paper does not deeply engage with the causal learning literature or derive new causal insights; it notes the connection in passing. This strength is somewhat inflated by the Strength Finder.

## Novel Insights

The review process surfaces one observation that goes beyond the paper's own contributions: the paper's internal-validity strength (the $n$=0 / $n$>1 contrast) and its external-validity weakness (the $\mathcal{F}_{\text{int}}$ assumption) are two sides of the same coin. The theory predicts that $n$, the degree of concept interaction, is the key determinant of whether non-generative methods can succeed. The empirical results bear this out on PUG data. Yet the paper does not propose a practical way to *measure* $n$ for a given real-world dataset, which would be a valuable predictive tool for practitioners deciding between generative and non-generative approaches. Bridging this gap—developing estimable proxies for the interaction degree $n$—would substantially increase the paper's practical impact. Additionally, the paper's claim that "generation is required" is really a claim about a *sufficient structural condition* for guaranteed OOD identifiability under a specific formal model, not a claim about *practical necessity* in all perception settings. Reframing the contribution around this distinction would strengthen rather than weaken the paper.

## Suggestions

1. **Qualify the title.** Change "Generation is Required for Data-Efficient Perception" to something like "Generation Enables Guaranteed Compositional Generalization under Structured Concept Interactions" or at minimum add a subtitle that acknowledges the $\mathcal{F}_{\text{int}}$ scope.

2. **Report computational budgets.** Add a table showing search steps per OOD image, replay dataset size, and wall-clock time for each method. This is essential for the data-efficiency framing.

3. **Move the unstructured decoder ablation to the main paper.** The claim that the $\mathcal{F}_{\text{int}}$ structure in the decoder is important would be much stronger if the main paper shows that unstructured decoders fail even with search/replay. Currently it's relegated to the appendix.

4. **Add error bars or individual trial markers.** Even for single-seed evaluations of pretrained models, reporting variance across random seeds for the slot encoder training would improve rigor.

5. **Add a discussion of how $n$ could be estimated or bounded for a new dataset.** This would make the theoretical framework practically actionable.

## Score and Decision

The paper makes a genuine theoretical contribution (Theorem 3.2 and the structural asymmetry analysis) that is clearly articulated and supported by internally consistent experiments. The main weaknesses are the overstated title/framing and the lack of computational cost reporting. These are real but do not undermine the core contribution. The paper is well above the acceptance threshold for a top-tier venue.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>
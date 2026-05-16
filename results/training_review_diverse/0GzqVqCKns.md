Now I have all the information needed to produce the final review. Let me synthesize carefully.

## Summary

This paper proposes using the dynamical susceptibility — a quantity from statistical physics measuring the volume of correlated token changes — as a probe of hierarchical latent structure in data undergoing forward-backward diffusion. The authors derive a mean-field theory showing that the correlation length of token changes diverges at the class phase transition in the Random Hierarchy Model (RHM), validate this with Belief Propagation experiments, and then show that qualitatively similar behavior (peaking susceptibility at a finite inversion time) appears in both text (MDLM on WikiText) and images (DDPM on ImageNet with CLIP patch embeddings).

## Strengths

- **Theoretical derivation linking hierarchical structure to diverging correlation length.** Using a mean-field approximation of the ε-process in the RHM, the paper derives that the correlation length scales as ξ ∼ |ε − ε*|^(−ν) (Equation 5) and validates this prediction via Belief Propagation experiments with excellent agreement between theory and simulation (Figure 2a-I, a-II). This provides a clean, verifiable theoretical foundation for the proposed signature.

- **Cross-modal experimental demonstration.** The paper shows that the susceptibility peaks at a finite inversion time in both text (t* ≈ 0.6T on WikiText with MDLM) and images (t* ≈ 0.6–0.7T on ImageNet with DDPM). This cross-modal consistency is the paper's strongest empirical contribution and supports the claim that hierarchical structure is a general property of natural data.

- **Control experiment distinguishing hierarchical from purely spatial correlations.** The Gaussian random field study (Section 3.3) shows that non-hierarchical data with algebraic spatial correlations produce a monotonic correlation length, not a peaked one — sharpening the attribution of the observed peaking susceptibility to hierarchical latent structure. This control is well-designed and directly strengthens the core claim.

- **Consistency across two different diffusion processes on the synthetic model.** The RHM experiments are performed for both the ε-process and masked diffusion (Figure 2a vs. 2b), showing the qualitative behavior is robust to the choice of noise mechanism. This strengthens the generality of the theoretical framework.

- **Clear visualization of the mechanism.** Figure 3 (tree changes) provides an intuitive illustration of how changes in deeper latent variables produce larger blocks of correlated token changes, directly connecting the theoretical picture to the observed data.

## Weaknesses

### Fatal
None.

### Major
None. The paper has real gaps but none that invalidate its core contribution; all are addressable.

### Minor

- **The vision observable's connection to the binary-spin theory is established only by analogy, not by argument.** The paper defines a dynamical susceptibility from the *L2 norm of CLIP embedding variations* (lines 361–366), while the theory is derived for binary spin variables (σ_i ∈ {−1, +1}) encoding exact token changes. No theoretical argument is given that this continuous quantity inherits the specific physical interpretation of the susceptibility — i.e., that its peak measures the size of cooperatively changing blocks in the same sense. The paper acknowledges this in the contribution list ("qualitative agreement") and the results are visually plausible, but the evidential chain from theory to the vision experiments is weaker than for the text or RHM experiments. This does not undermine the paper's core claim (which is multi-modal), but it means the vision evidence should be read as suggestive rather than confirmatory.

- **The text experiments do not independently verify that the susceptibility peak coincides with a measured latent-variable transition.** In the RHM, the paper directly measures the class reconstruction probability and shows it undergoes a phase transition at the same t* where susceptibility peaks (Figure 2b, referencing fig:maksing_inversion). For text, the susceptibility peak at t* ≈ 0.6T is presented as *establishing* a phase transition (line 322), but no independent measurement of semantic content, topic, or grammatical structure change is reported. Prior work (Sclocchi et al. 2024) established the class transition for images, providing independent grounding for the vision experiments; no such grounding exists for text in this paper. This weakens the claim from "confirmed" to "qualitatively consistent."

- **No error bars or confidence intervals on real-data plots (Figures 4b–c, 6a–b).** The paper reports N_R = 50 trajectories for text and 128 for images, which is adequate, but does not show variability (e.g., via bootstrapping or standard deviations). Given stochasticity in the forward-backward process and finite sample counts, the reader cannot assess whether the claimed peak at t* is robust or within noise. This is standard practice that would significantly strengthen the quantitative conclusions.

- **No limitations or caveats discussion.** The paper does not discuss potential biases introduced by the learned denoiser (vs. exact BP denoising), the dependence of results on the tokenizer/model choice, or the assumption that natural data has tree-like hierarchical structure. Adding a limitations paragraph would improve the paper's framing.

- **The claim in the abstract — "we confirm this prediction" — is stronger than the evidence warrants**, given the gaps above. "Show qualitative agreement" or "are consistent with" would be more accurate for the real-data experiments.

### Trivial

- The distance metric used for the image correlation function (Euclidean or Manhattan on the 7×7 grid?) is not explicitly stated (lines 361–366), though it can be inferred. A brief clarification would improve reproducibility.

- The paper states it uses a "${\tt GPT2}$ tokenizer" but does not specify which variant (e.g., GPT-2 BPE with what vocabulary size). Minor detail.

- The truncation of the susceptibility integral at r = 10 for text is noted in a footnote but not justified with a sensitivity analysis. A brief comment on how results behave for different cutoffs would be helpful.

## Nice-to-Haves

- For at least one real-data modality, directly measure a high-level latent variable transition (e.g., topic change in text via a topic model, or class change probability in images via classifier, as in Sclocchi et al. 2024) and show it coincides with the susceptibility peak. This would transform the evidence from qualitative to quantitative.
- For the vision experiments, explore whether thresholding the CLIP embedding variations to binary change indicators (as in the theory) yields similar results, which would strengthen the connection to the theoretical framework.
- A brief sensitivity analysis of the truncation distance r = 10 in the text experiments.

## Removed Points

These points are flagged to be removed; treat them with caution:

- The harsh critic's request for the paper to discuss "related work on criticality in neural networks and methods that directly infer latent trees from data (e.g., phylogenetic or hierarchical clustering approaches)" — removed per instruction: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
- The harsh critic's comment about missing appendix content and details — removed because appendix sections exist in the original submission but are stripped by the parser.
- The harsh critic's complaint that "the paper does not discuss whether other non‑hierarchical models (e.g., a mixture of distributions with varying resolution scales) could also produce a non‑monotonic correlation length" — partially kept in spirit but downgraded: the paper runs a Gaussian field control, which is a reasonable baseline. Demanding exhaustive testing of all possible non-hierarchical models is scope creep.
- The harsh critic's note about "tokenizer details... GPT-2 BPE" — the paper does state it uses the GPT2 tokenizer (line 322), which is sufficient for an anonymous submission; the specific vocabulary size is a minor detail. Moved to Trivial.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the harsh critic's suggestion to verify the susceptibility peak by directly measuring a latent variable transition in text (e.g., via topic model or parser) identifies the most impactful single experiment the authors could do to strengthen the empirical chain. This is not a flaw in the existing paper but a sharp articulation of where the evidence is thinnest. Additionally, the harsh critic's observation that the vision observable (L2 norms of CLIP embedding variations) departs from the binary-spin framework is a valid methodological concern that the authors should address explicitly, even if only to argue that the continuous observable is a natural generalization.

## Suggestions

- Soften the abstract's "confirm this prediction" to language like "show qualitative agreement with this prediction" or "demonstrate consistency with this prediction" for the real-data experiments.
- Add error bars (bootstrap or standard error) to Figures 4b–c and 6a–b.
- Add a limitations/discussion paragraph addressing: (i) learned vs. exact denoising, (ii) model/tokenizer dependence, (iii) the assumption of tree-structured hierarchy.
- Explicitly state the distance metric (Euclidean vs. Manhattan) used for the 2D grid in the image correlation function.
- For the vision experiments, provide a brief argument for why the L2-norm observable is a reasonable extension of the binary-spin framework, or show that thresholding to binary indicators yields similar results.

## Score and Decision

This is a solid paper with a compelling core idea and clean theoretical/synthetic validation. The real-data experiments are promising but have clear evidential gaps: the vision observable lacks a tight connection to the theory, the text experiments lack independent verification of a latent transition, and error bars are absent. These are not fatal — they do not invalidate the paper's contributions — but they prevent the paper from being as definitive as it could be. The paper would benefit from a major revision addressing these gaps, though none require new theoretical development.

Given the strengths (clean theory, cross-modal scope, good controls) and the verified weaknesses (evidential gaps in real-data experiments, missing error bars), the paper is a solid borderline accept. The contributions are real but the empirical support for the central claim in real data is preliminary rather than definitive.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
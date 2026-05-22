Now I have a thorough calibration. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions

## Score and Decision

Let me now produce the final review.

**Bracket summary:**
- Round 1 bracket: [5.5, 7.5]
- Round 2 narrowed to ~6.5 by comparing against anchors: 7.00 ("Characterizing Pattern Matching"), 6.50 ("Bidirectional Predictive Coding"), 6.00 ("Readout Representation"), 6.00 ("GenRep/Reconciling Visual Perception")

The paper's theory + empirical combination is stronger than the 6.00 papers (which have weaker theory or less convincing experiments) but slightly below the 7.00 "Characterizing Pattern Matching" paper (which has tighter formal analysis and more comprehensive experiments across architectures). The paper under review has a more fundamental question (generation vs. non-generation for visual perception) but narrower empirical scope (single dataset family) and no error bars.

Final score: 6.5

## Summary

This paper investigates whether compositional generalization in visual perception requires a generative (decoder-inversion) approach or can be achieved by non-generative (encoder-only) methods. The authors formalize the inductive biases needed for compositional generalization, prove theoretically (Theorem 3.2) that constraining an encoder to the required function class \(\mathcal{G}_{\text{int}}\) is generally infeasible when \(d_x \gg d_z\) because the required constraints depend on the unknown geometry of the data manifold, while constraining a decoder to the corresponding class \(\mathcal{F}_{\text{int}}\) is straightforward. They then introduce two practical inversion strategies — gradient-based search and generative replay — and show on photorealistic PUG datasets that generative methods substantially and consistently outperform a wide range of non-generative encoders (DINOv1/v2, CLIP, SigLIP2, I-JEPA, from-scratch) on out-of-domain compositional generalization.

## Strengths

1. **Novel theoretical result pinning down the encoder/decoder asymmetry.** Theorem 3.2 is the paper's core formal contribution: when \(d_x \geq d_z^3\), the Jacobian and Hessian of inverse generators in \(\mathcal{G}_{\text{int}}\) can be arbitrary at any point, so no regularization or architecture constraint can enforce membership in \(\mathcal{G}_{\text{int}}\) without knowledge of the data manifold's geometry in OOD regions. This goes beyond prior heuristic arguments (e.g., causal vs. anti-causal learning) by providing a concrete mathematical reason why encoder-only methods cannot *guarantee* compositional generalization. The contrast with the decoder side, where the analogous constraints are data-independent and straightforward to impose (Eq. 3.1–3.2), is clearly articulated.

2. **Consistent and controlled empirical evidence across three PUG splits.** Figure 5 shows that on PUG-Background (interacting concepts), every non-generative method achieves OOD accuracy below ~50% except SigLIP2 (~80%), while on PUG-Object (non-interacting, \(n=0\)) all methods succeed near-perfectly. This controlled comparison directly validates the paper's theoretical prediction that the difficulty is specific to *interactive* concepts. The use of six different base encoders with varying pretraining scales (from scratch through SigLIP2) strengthens the claim that the failure is not an artifact of a particular architecture or training objective.

3. **Generative methods produce substantial and robust OOD improvements.** Figure 6 demonstrates that replay lifts OOD accuracy on PUG-Background from ~20–40% to ~70–90% across all base encoders, with search providing further gains. These improvements hold for every pretrained encoder tested, despite the encoder being frozen — the gains come solely from inverting the decoder. This robustness to encoder choice is strong evidence that the generative approach to compositional generalization is practically realizable and not dependent on careful initialization.

4. **Formal connection between theory and the special case \(n=0\).** Section 3.1 notes that when concepts do not interact (\(n=0\)), \(\mathcal{G}_{\text{int}}\) has additional sparsity structure that makes compositional generalization easier. PUG-Object empirically validates this: all non-generative methods achieve near-perfect OOD accuracy despite no explicit constraints, cleanly separating the hard case (interacting concepts) from the easy case.

5. **Practical, clearly described inversion methods.** The paper provides two concrete strategies — gradient-based search (Sec. 4.1) and generative replay (Sec. 4.2) — with clear objectives (Eq. 4.3 and 4.4) and demonstrates that replay alone (an offline solution) already lifts performance substantially. This makes the generative approach actionable for practitioners.

## Weaknesses

### Major

1. **Empirical evidence confined to a single dataset family (PUG).** While PUG images are photorealistic and the three splits (background, texture, object) cleanly isolate different interaction modalities, the results may not transfer to more complex visual domains (e.g., real photographs with multiple interacting objects, lighting variations, occlusions). The paper acknowledges this limitation (Sec. 7) but does not test on any additional benchmark. The claim that "generation is required for data-efficient perception" would be substantially strengthened by even one experiment on a more naturalistic OOD benchmark (e.g., CLEVR-Style, ObjectsRoom, or a synthetic-to-real transfer scenario). This is an **evidential gap** that limits the generality of the paper's central conclusion.

2. **No statistical reliability measures.** Figures 5 and 6 report only point estimates with no error bars, standard deviations, or significance tests. While many differences are large (e.g., ~20% vs. ~80%), for comparisons where differences are smaller (e.g., PUG-Texture or the gain from search on top of replay), the significance is unclear. This weakens the empirical rigor of what is otherwise a compelling experimental narrative.

### Minor

3. **The "infeasibility" claim is argued, not formally proven as an impossibility.** Theorem 3.2 shows that the local derivative structure of \(g \in \mathcal{G}_{\text{int}}\) can be almost arbitrary when \(d_x \gg d_z\), which the paper interprets as making regularization-based enforcement impractical. However, the theorem does not prove that one *cannot* design an encoder architecture whose output space is exactly \(\mathcal{G}_{\text{int}}\), or that one cannot learn the tangent space from ID data to enforce Eq. 3.4. The paper's language ("suggests… is infeasible," "generally not feasible") is appropriately hedged, but the strength of the overall narrative sometimes outpaces what Theorem 3.2 strictly guarantees. This is a gap in theoretical conclusiveness, not a flaw in the empirical results.

4. **The \(d_x \geq d_z^3\) condition in Theorem 3.2 seems somewhat arbitrary.** It is not stated whether a smaller dimension gap (e.g., \(d_x \geq d_z^2\)) would suffice to reach the same conclusion. A tighter bound would strengthen the claim. Additionally, Lemma 3.1 is given for \(d_x = d_z\) and \(m=1\), which never holds for image data; its role as a stepping stone could be more clearly motivated.

5. **Missing analysis of search convergence.** The paper introduces gradient-based search as a method for OOD inversion but does not analyze how many gradient steps are needed, how sensitive the approach is to initialization quality, or whether failure cases occur. A brief ablation would help practitioners understand the computational cost.

### Trivial

None.

## Nice-to-Haves

- **Compare against a non-generative method also trained with replay.** The paper compares generative methods (decoder + search/replay) to non-generative (encoder-only), but does not test whether training an encoder on generated OOD images *without* a decoder also improves performance (e.g., using an external unconditional generative model to create OOD data and fine-tuning the encoder). This would help isolate whether the benefit is specific to the decoder's latent structure.
- **Ablate the decoder constraint.** Showing that when the decoder is *not* constrained to \(\mathcal{F}_{\text{int}}\) (e.g., a standard VAE decoder without slot-wise regularization), the benefits of search/replay are reduced or eliminated would confirm that the decoder architecture is a critical component.
- **Visualize or quantify the quality of replayed OOD images.** Sec. 4.2 assumes that sampling from \(p_{\tilde{z}}\) with independent slot marginals yields realistic OOD images via \(\hat{f}\), but the paper does not analyze whether generated OOD images are of sufficient quality to train an effective encoder.

## Removed Points

- **Criticism about missing appendix details (decoder regularization implementation):** The paper states "further details can be found in App. B," which the PDF parser stripped. This is a parser artifact, not an author omission.
- **Criticism about missing PUG-Object generative results:** The paper explicitly states "we do not report results on PUG-Object as all non-generative methods achieve near-perfect OOD performance… Thus, further OOD gains through search and replay are not possible." The criticism that "it would be informative to see" is noted but unreasonable to require for a ceiling-effect scenario.
- **Criticism about how the ID/OOD split is designed:** The PUG splits are clearly described in Sec. 5.1 and Fig. 7 (left). The specific choices (background combinations, texture combinations) are appropriate for the theoretical settings studied.
- **Criticism about conditioning of the "infeasibility" claim as "fatal":** The harsh critic correctly identified this as a "methodological gap" not a structural flaw; the softened language in the paper ("suggests," "generally not feasible," "tends to be infeasible") already hedges appropriately.

## Novel Insights

The sharpest insight from the merged reviews is that the paper's real contribution is not the theoretical impossibility of encoder constraints (Theorem 3.2 is suggestive, not a proof of impossibility), but rather the clean demonstration that even without any explicit encoder constraint, the *practical* difficulty of compositional generalization for non-generative methods is severe and systematic, while generative methods using the same decoder overcome it. This shifts the conversation from "can we prove encoders can't work" to "the inductive bias of decoder-based generative models naturally provides what encoders lack" — which the field should find actionable regardless of the theoretical endpoint.

## Suggestions

1. Add error bars (3+ seeds) to Figures 5 and 6 to establish statistical reliability. Given that the main differences are large, this would be a low-effort, high-impact improvement.
2. Include at least one additional OOD benchmark beyond PUG (e.g., CLEVR-Style or a synthetic-real transfer) to broaden the empirical scope.
3. Clarify the theoretical contribution's scope by replacing "infeasible" with "currently no practical method exists" to match what Theorem 3.2 actually shows, and add a brief discussion of what would constitute a proof of impossibility.

## Calibration Anchors

| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| DealNNlz94 | 3.00 | R1 | Weak, rejected paper on object-centric compositional generalization — our paper is substantially stronger |
| i0zjotaTnv | 2.00 | R1 | Weak, rejected VLM reasoning paper — much weaker than our paper |
| HjLC5fEWcI | 3.00 | R1 | Weak, withdrawn generative model paper — much weaker |
| pbMzwCnGpq | 2.50 | R1 | Weak, rejected GCD paper — much weaker |
| yi06ZiVl2H | 4.80 | R1 | Rejected paper on necessary conditions for compositional generalization — our paper has clearer theory and stronger empirical evidence |
| ADeeoMY4Dn | 4.50 | R1 | Rejected paper on transformers and compositional generalization — our paper is stronger in both theory and data |
| UBoCMU5iYV | 4.67 | R1 | Accepted poster on memorization+composition — less directly comparable, weaker theory |
| oSUjUvs999 | 4.00 | R1 | Rejected paper on visual generative model compositionality — our paper is substantially stronger |
| DM0Y0oL33T | 8.00 | R1 | Accepted oral on multimodal verification — not topically comparable |
| qOyF214xmg | 8.00 | R1 | Accepted poster on language model transduction — not topically comparable |
| HbRihpurRr | 6.50 | R2 | Accepted poster on bidirectional predictive coding (generative vs discriminative) — comparable quality, our paper has clearer theoretical contribution but narrower empirical scope |
| pODHH9DLeA | 6.00 | R2 | Accepted poster on readout representation — our paper has stronger theory and more compelling experiments |
| yKC3CaFg8K | 6.00 | R2 | Accepted poster on unifying perception and generation in diffusion — our paper has a more fundamental theoretical contribution |
| VCjlm003WL | 7.00 | R2 | Accepted poster on pattern matching limits in compositional tasks — tighter formal analysis but narrower task scope; our paper addresses a more fundamental question about visual perception |
| I3Ct1eDmVI | 6.50 | R2 | Accepted poster on hyperbolic vision-language representations — different domain |
| phRRjC0Da6 | 6.00 | R2 | Rejected paper on compositional zero-shot learning — our paper is stronger |
| iqAFhWistW | 6.00 | R2 | Accepted poster on T2I composition/reasoning benchmark — different domain |
| Zunww3FHPU | 6.50 | R2 | Accepted oral on latent space dynamics — different domain |
| s5a8zBPFfe | 6.50 | R2 | Accepted poster on Pareto VAE — different domain |
| TLSUIyBIfs | 7.00 | R2 | Accepted oral on length generalization in transformers — different domain |

Round-1 bracket: [5.5, 7.5]. Round-2 narrowing placed the paper at 6.5, positioned between accepted poster papers like Readout Representation (6.00) and GenRep (6.00) on one side, and Characterizing Pattern Matching (7.00) on the other. The paper's theoretical novelty and clean empirical demonstration are stronger than the 6.00 papers, but the narrower empirical scope (single dataset family, no error bars) keeps it below the 7.00 anchor, which features tighter formal analysis and more comprehensive experiments.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims directly against the source text. Let me produce the final consolidated review.

## Summary

This paper investigates the "modality gap" in contrastive multimodal models (e.g., CLIP) — the observation that image and text embeddings occupy disjoint regions in the shared representational space. The authors argue this gap is not fundamentally caused by modality differences, data mismatches, or architectural artifacts, but by the contrastive loss itself (proposing the term *contrastive gap*). They support this with a controlled experiment using two image encoders trained on identical image pairs, and they analyze how dimensionality and batch size exacerbate the gap. To close it, they add uniformity and alignment terms to the CLIP loss and show that fine-tuning with these terms reduces the gap and correlates with improvements on retrieval, zero-shot classification, and multimodal arithmetic.

## Strengths

1. **Clean core insight with compelling evidence**: The controlled experiment (Section 3.2) eliminates modality difference, the cone effect (via initialization alignment), and mismatched pairs as confounds, yet a gap still emerges. The two image encoders start with aligned outputs and become perfectly linearly separable after training (Table 1). This directly supports the claim that the contrastive loss itself creates the gap, independent of modality.

2. **Principled analysis of batch-size/dimensionality interplay**: Section 3.5 provides a mechanistic explanation (via the temperature-dependent approximation where the loss focuses on the nearest negative, $s_{\text{max}}$) for why small batch sizes and high dimensions worsen the gap. Figure 2 confirms the predicted trend empirically. This goes beyond prior descriptive work and gives a concrete understanding of the phenomenon.

3. **Simple and effective method to close the gap**: The proposed $\mathcal{L}_{\text{CUAXU}}$ loss (adding intra-modal uniformity, cross-modal uniformity, and alignment to $\mathcal{L}_{\text{CLIP}}$) substantially reduces both centroid distance and linear separability across dimensionalities (Figure 3). The losses are straightforward, principled (adapted from Wang & Isola 2020's unimodal theory), and can be applied via fine-tuning.

4. **Downstream task improvements correlate with gap reduction**: Fine-tuning with $\mathcal{L}_{\text{CUAXU}}$ improves zero-shot classification accuracy (Figure 5) and multimodal arithmetic SIMAT scores (Figure 6) compared to fine-tuning with $\mathcal{L}_{\text{CLIP}}$ alone, all controlled on the same MS COCO dataset. The 3D visualization (Figure 1) further provides intuitive insight into why lower-dimensional spaces naturally close the gap.

## Weaknesses

### Fatal

None.

### Major

1. **Ambiguity in the controlled experiment (Section 3.2): how is the transformation applied?**  
   The paper states that a "fixed transformation matrix" is used to translate the second image encoder's embeddings to overlap with the first encoder's "at initialization." It is not explicit whether this transformation is (a) applied once to set the initial encoder weights/initial outputs and then removed, or (b) kept as a fixed linear layer throughout training. These two interpretations lead to different conclusions about the experiment's confounds. Under interpretation (b), the fixed transformation could become mismatched as the encoders evolve and may itself contribute to the observed separation. The authors should clarify this and, ideally, run a cleaner control (e.g., train two same-architecture encoders from scratch on identical images without any transformation, verifying whether the gap emerges without pre-alignment). This ambiguity weakens the central evidence for the "contrastive gap" claim, though the claim remains plausible under both interpretations.

2. **Causal attribution of downstream gains to gap reduction is not disentangled**  
   The paper states that "closing the contrastive gap improves downstream performance" (intro bullet) and that "representational spaces with smaller contrastive gaps... correlate with higher performance" (Section 5.3). However, the gap is reduced by adding uniformity and alignment terms to the loss — and those same terms directly modify representations in ways that could independently improve downstream tasks (e.g., intra-modal uniformity spreads images apart, directly benefiting classification). The paper does not isolate gap reduction from the effects of the loss terms themselves. A stronger test would be to reduce the gap *without* modifying the loss (e.g., post-hoc translation as in Liang et al. 2022) and measure downstream performance, or to include an ablation where gap reduction is blocked while the loss terms are applied. Without this, the causal claim is overstated — the paper demonstrates correlation, not causation.

### Minor

1. **No statistical reporting (error bars, significance tests)** across any experiment (Figures 3–6). All results are point estimates. This makes it impossible to assess whether observed differences (e.g., $\mathcal{L}_{\text{CUAXU}}$ vs. $\mathcal{L}_{\text{CLIP}}$ in zero-shot accuracy, which appear small, ~0.01–0.02) are robust or due to chance. At minimum, multiple fine-tuning seeds with standard deviations should be reported.

2. **Zero-shot evaluation datasets are not named in the main text.** The paper reports "average zero-shot accuracies across all the datasets" (Section 5.3) without listing them. Without knowing which datasets were used, the breadth and relevance of the evaluation cannot be assessed from the main text alone.

3. **Inconsistency in retrieval results undermines the gap-reduction narrative.** $\mathcal{L}_{\text{CUA}}$ (which includes uniformity and alignment but not cross-modal uniformity) *reduces* the gap but *worsens* retrieval mAP@R compared to $\mathcal{L}_{\text{CLIP}}$ (Figure 4). The paper acknowledges this and attributes it to the importance of cross-modal uniformity, but this observation directly contradicts the simple "smaller gap → better performance" claim and suggests cross-modal uniformity (not gap size *per se*) is the operative factor.

4. **Lack of comparison with simpler baselines for gap reduction.** The paper discusses that increasing batch size or temperature can reduce the gap (Section 3.5) but does not test whether these simpler alternatives match or exceed the proposed loss terms. A comparison would contextualize the complexity of adding extra loss terms.

5. **Vague reporting of the final training loss.** In Section 3.2, the loss is described as "close to zero" without a numerical value. Explicitly reporting the loss and verifying that positive-pair similarity is high (e.g., average dot product) would strengthen confidence that the solution is near-optimal.

### Trivial

- Figure captions contain garbled text (parser artifact in the extracted text, not the original).  
- The linear separability metric reports "50%" as the chance baseline but uses the notation $\bar{5}0\%$ (line 60), which appears to be a rendering artifact.

## Nice-to-Haves

- An ablation study isolating the contribution of each loss term ($\mathcal{L}_{\text{Uniform}}$, $\mathcal{L}_{\text{XUniform}}$, $\mathcal{L}_{\text{Align}}$) to both gap metrics and downstream performance.
- A sensitivity analysis of the temperature parameter $\tau$ when combined with the additional loss terms.
- Extension to training from scratch (not just fine-tuning) to verify that the gap reduction and downstream benefits persist.
- Reporting per-dataset zero-shot results rather than only the average across datasets.

## Removed Points

These points from the inputs were removed with justification:

- **"Appendix is stripped, evaluation is opaque"** — Per review guidelines, missing appendix content is a parser artifact from PDF extraction, not a paper flaw. The original submission contains Appendix A.4 with evaluation details.
- **"3D experiment setup differs from high-D; not properly compared"** — This is scope creep. The 3D experiment is intended as a visualization/illustration (Section 3.3), not a rigorous experimental condition. Criticizing it for not being a controlled comparison is unwarranted.
- **"Alignment term L_Align is redundant with CLIP loss"** — This is stated as a note, not a weakness; the reviewer even acknowledges it "does no harm." It provides no actionable criticism.
- **"The gap could simply be due to the two encoders drifting apart as they optimise the contrastive loss, which is no different from training two encoders with random initialisations"** — This is factually incorrect as a criticism. The whole point of the initialization alignment is to show the gap is *created* during training rather than pre-existing. Drifting apart due to the contrastive loss *supports* the paper's thesis.
- Several generic strength descriptions from the Strength Finder (e.g., "this paper addressed an important problem") were removed as insufficiently specific or conflicting with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The key observation — that the modality gap persists even when modality difference is eliminated and that it emerges from the contrastive loss's interaction with high dimensionality and small batch sizes — is the paper's main novel insight and is reasonably supported by the evidence. The reviews do not surface additional novel perspectives that the paper itself has not already identified.

## Suggestions

1. **Clarify the Section 3.2 transformation**: Explicitly state whether the transformation matrix is applied throughout training as a fixed layer or only at initialization. Even better, add a control experiment that trains two same-architecture image encoders on identical images *without* any transformation, and report whether the gap emerges from scratch.

2. **Disentangle gap reduction from the loss terms**: Either (a) test post-hoc translation of embeddings (Liang et al. 2022) to reduce the gap without modifying the loss, measuring downstream effects, or (b) include a direct ablation where the gap is blocked (e.g., via explicit regularization on the centroid distance) while keeping the loss terms fixed.

3. **Add statistical rigor**: Run 3–5 fine-tuning seeds for all experiments and report means ± standard deviations. For zero-shot, include a table of per-dataset results in the main paper.

4. **Compare against simple baselines**: Test whether increasing batch size or temperature achieves comparable gap reduction and downstream performance to the proposed $\mathcal{L}_{\text{CUAXU}}$ loss.

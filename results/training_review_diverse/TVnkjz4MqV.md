Now I have a complete picture. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces Neural Manifold Regularization (NMR), a supervised dimensionality reduction method that embeds neural population activity into a 2D latent space regularized by the distances and densities of continuous movement labels. NMR is evaluated across 68+ sessions spanning four neural signal modalities (single units, unsorted events, three LFP bands), three movement types (center-out reaching, grid-based natural reaching, free natural reaching, attempted handwriting), multiple brain areas (M1, PMd, S1, precentral gyrus), and two species (macaque and human). Combined with a linear decoder, NMR consistently and significantly outperforms CEBRA and pi-VAE.

## Strengths

1. **Comprehensive, rigorous experimental evaluation with large-margin improvements**: NMR achieves dramatically higher explained variance than hyperparameter-optimized CEBRA and pi-VAE across nearly every setting — M1 center-out (0.88 vs 0.48 vs 0.43), PMd (0.90 vs 0.53 vs 0.37), natural movements with sorted units (0.82 vs 0.55 vs 0.45) and unsorted events (0.65 vs 0.36 vs 0.25), all with strong statistical significance (paired t-tests, multiple comparisons corrected). This evidence directly supports the claim of >50% improvement over baselines.

2. **Enables robust cross-session and cross-subject decoding with a simple linear decoder**: NMR achieves nearly twice the cross-session decoded variance of CEBRA (t=18.5, p=1.5e-47) and six times that of pi-VAE (t=21, p=1.4e-55) across 28 M1 sessions (Fig 3). The low cross-session variance (std 0.02–0.03) and successful decoding across hemispheres and years with hyperparameter-free linear regression is a genuinely impressive result.

3. **First demonstration of high-fidelity 2D latent dynamics for 2D movements**: As the paper argues, prior work required 3D or higher latent spaces even for 2D movements. NMR reveals well-aligned 2D latent dynamics for center-out reaching, random reaches, and attempted handwriting — including single-trial latent dynamics with no overlap for directions separated by 22.5° in a paralyzed patient (Fig 7b, r²=0.96). This is a novel capability.

4. **Evaluated across diverse signal modalities with computational efficiency**: NMR works on single-unit spikes, multiunit unsorted events, and LFP bands (LMP, Gamma, Beta) from macaque motor/premotor/somatosensory cortex, as well as human precentral gyrus recordings for attempted movements. NMR also runs faster than CEBRA (119 vs 163 seconds for single units, t=12, p=3e-14; 149 vs 166 seconds for unsorted events, t=3.5, p=0.001), with computational savings holding under different hyperparameters.

5. **Code is provided** (stated in the abstract), enabling reproduction and further study.

## Weaknesses

### Fatal
None.

### Major

1. **The method is inadequately specified for a methods paper.** Section 3.3 ("New Loss Function for CEBRA") — the only methods subsection visible in the extracted text — describes the loss only in conceptual, prose-based terms, referencing a figure's colorbar scale to explain how positive/negative pairs are selected. There is no formal loss equation, no explicit training objective, and no quantitative specification of the density-weighting mechanism for infrequent labels. Key details — the neural architecture, training procedure, and hyperparameter search ranges referenced as "Table 1" and "Fig 6" — appear in sections that the parser stripped (Sections 3.1, 3.2 are absent from the extracted text). While code availability partially mitigates reproducibility concerns, a methods paper's central contribution should be understandable from the paper itself without reverse-engineering code. This is the single most significant barrier to evaluating the paper's contribution. *Why this matters: without a clear, self-contained method description, novelty cannot be assessed, the contribution cannot be verified by peer reviewers, and the paper does not meet the standard for a methods publication.*

2. **No ablation or component analysis.** NMR involves at least three discernible design choices: (a) predicting labels from embeddings via linear regression and using those predictions to select positive/negative pairs through a threshold, (b) discarding samples with far-away predicted labels, and (c) applying greater force to infrequent labels via density weighting. None of these components are ablated. Without an ablation study, the paper cannot attribute the reported performance gains to any specific aspect of NMR rather than to generic factors (e.g., the auxiliary regression task itself providing regularization, different optimization dynamics, or the method being more heavily supervised). This weakens the paper's claim about what "Neural Manifold Regularization" actually achieves. *Why this matters: the paper's central contribution is a new method; without understanding which components drive improvement, the scientific contribution is unclear.*

3. **The relationship between NMR and CEBRA is ambiguous.** Section 3.3 is titled "New Loss Function for CEBRA," suggesting NMR is a modified loss applied within CEBRA's framework. Yet the experiments treat NMR, CEBRA, and pi-VAE as three separate methods compared against each other. It is never clarified whether NMR uses the same architecture as CEBRA with a different loss, a different architecture entirely, or a different training scheme. This ambiguity undermines interpretation — if NMR is a better loss for CEBRA's framework, the comparison should control for architecture; if NMR is a separate method, it needs its own full description. *Why this matters: the fairness and interpretation of the experimental comparison depend on knowing what is being compared.*

### Minor

4. **The "over 50% improvement" claim is not precisely defined.** The abstract states NMR "outperformed other dimensionality reduction methods by over 50% across 68 sessions," but does not specify whether this is relative improvement (e.g., (0.88−0.48)/0.48 ≈ 83%) or absolute improvement, nor whether the baseline is the best of the two comparators or some average. The paper should state this explicitly to avoid overclaiming.

5. **The rat hippocampus experiment is too brief to support generalizability claims.** It is mentioned in a single sentence ("The results demonstrated a 37% improvement of NMR over CEBRA (Fig 11)") with no figure, no experimental details, no statistical test, and no discussion. As presented, this result neither strengthens nor weakens the paper's core claims about hand movements. Either remove it or describe it properly.

6. **No analysis of why embeddings are stable across sessions.** The cross-session decoding results are the paper's most striking finding, yet the paper offers no mechanistic analysis of why NMR yields more consistent embeddings. Is it the 2D constraint, the density weighting reducing sensitivity to distribution shift, or something else? This is a missed opportunity to strengthen the central claim.

### Trivial

None.

## Nice-to-Haves

- A formal loss equation with clear notation would significantly improve the paper.
- An ablation study isolating the three main design choices (prediction-based pair selection, thresholding, density weighting) would directly validate the contribution.
- Explicitly stating whether "50% improvement" is relative or absolute would prevent potential misinterpretation.
- A brief analysis of embedding stability (e.g., measuring alignment of embedding manifolds directly across sessions) would turn the cross-session results from an observation into a mechanistic understanding.

## Removed Points

- *Criticism that the method is "not adequately defined" because architecture/training details are entirely absent* — Sections 3.1 and 3.2 appear to have been stripped by the parser. It is not possible to confirm from the extracted text whether those sections contained architecture and training details. However, **Section 3.3 (loss function description) is visible and is genuinely inadequate** — this criticism is retained but narrowed to the loss function specification.
- *Criticism about "ConR loss" lacking citation* — the references section was likely stripped by the parser; the citation likely exists in the original submission.
- *Criticism about formatting artifacts or garbled text (e.g., ".3)", "mathsf")* — these are parser artifacts, not author errors.
- *Generic strengths from the Strength Finder that lack specific content or conflict with verified weaknesses* — none found; all strengths listed are specific and evidence-backed.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's substantial experimental program and its thin methodological specification. The experimental results — particularly the cross-session decoding (nearly 2× CEBRA, 6× pi-VAE) and the successful 2D embedding of attempted handwriting in a paralyzed patient — appear to represent a genuine empirical advance. Yet because the method is not formally described, it is difficult for a reviewer to determine whether this advance comes from a genuinely novel algorithmic idea or from a well-tuned combination of existing building blocks (contrastive learning with thresholding, auxiliary regression, density weighting). The paper would be significantly strengthened by resolving this ambiguity — either by showing through ablation that the specific combination is novel, or by formally specifying the loss so the novelty can be evaluated on its own terms.

## Suggestions

1. **Add a formal Methods section** (or expand Section 3) with: (a) the loss function written as a mathematical equation, (b) a clear description of the neural encoder architecture (or a statement that NMR is a loss applied to a fixed architecture shared with baselines), (c) the density-weighting mechanism specified quantitatively, and (d) pseudocode or a schematic diagram of the training procedure.

2. **Clarify the relationship between NMR and CEBRA**: explicitly state whether NMR shares CEBRA's architecture, whether it is a drop-in replacement for its loss, or whether it is a completely separate framework. Adjust the experimental comparison and section title accordingly.

3. **Add at least one ablation study** isolating the main components (linear regression prediction, threshold-based pair selection, density weighting). Even a simple "w/o density weighting" or "w/o prediction-based filtering" condition on one dataset would substantially improve the paper's scientific value.

4. **Define the "over 50% improvement"** as relative vs. absolute improvement and specify the reference baseline.

5. **Either develop or remove the rat hippocampus experiment** — as presented, it does not support the generalizability claim.

6. **Add a brief discussion** analyzing why NMR yields more consistent embeddings across sessions — this would turn a striking observation into a mechanistic insight.

## Score and Decision

**Originality**: 6/10 — the combination of label prediction with contrastive pair selection is moderately novel, but the lack of formal specification and ablation makes it hard to assess true novelty.

**Importance of research question**: 8/10 — aligning 2D latent dynamics with 2D movement trajectories is a well-motivated and practically important problem for both neuroscience and BMI.

**Claims supported**: 5/10 — the experimental results support the performance claims, but the method itself is underspecified, and the lack of ablation prevents evaluation of what drives the improvement.

**Soundness of experiments**: 7/10 — extensive, multi-modal, cross-session evaluation with statistical tests and hyperparameter optimization is a strength; the ambiguity in the NMR-vs-CEBRA comparison and lack of ablation reduce confidence.

**Clarity of writing**: 4/10 — experimental sections are reasonably clear; the methods section is inadequate for a methods paper.

**Value to the research community**: 6/10 — if the method were properly specified, the paper would be a useful benchmark; in its current form, the experimental results are compelling but difficult to build upon.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
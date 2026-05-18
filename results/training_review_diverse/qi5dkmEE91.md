I have thoroughly read the paper and verified all claims. Here is the consolidated review.

---

## Summary

This paper introduces Motif Explainer Models (MEMs), a post-hoc explanation method for genomic DNNs that identifies sufficient and necessary motifs by incorporating biological prior knowledge (motifs are small, contiguous, disjoint) directly into a regularized optimization objective. MEMs produce importance scores separately optimized for sufficiency (s-MEM) and necessity (n-MEM), and the authors demonstrate on synthetic sequences with known SPI1 and CTCF motifs that MEMs outperform scramblers (the prior SOTA) at identifying the correct number of motif regions and achieving higher sufficiency/necessity scores across three logical syntax regimes (cooperation, redundancy, repression).

## Strengths

1. **Biologically motivated inductive bias.** MEMs directly encode that motifs are sparse, contiguous, and disjoint via a regularizer (Eq. 14–15) with an $\ell_1$ penalty and a $\sigma$-parameterized contiguity term. This is a principled departure from scramblers' entropy-based regularization and leads to qualitatively cleaner outputs — MEMs consistently identify 2–3 regions for cooperative syntax while scramblers detect 0–6 regions depending on threshold (Fig. 1a).

2. **Clear quantitative advantage over the SOTA across all three syntax regimes.** MEMs outperform both inclusion and occlusion scramblers on sufficiency and necessity scores while identifying the correct number of base pairs and disjoint regions. For repressive syntax with positive labels, the s-MEM identifies 15–30 base pairs in 1–1.5 regions (Fig. 3c) versus the scrambler's 15–50 base pairs in 0.5–3 regions, and the n-MEM correctly identifies 0.5–1.5 necessary regions while the occlusion scrambler finds nearly zero on average (Fig. 3b).

3. **Combined sufficiency and necessity provides richer information.** By jointly analyzing s-MEM and n-MEM outputs, the method distinguishes the three syntax types. For cooperative syntax, the pattern "2 motifs sufficient, 1 necessary" emerges; for redundant syntax, "1 sufficient, 1–2 necessary" depending on sequence content (Figs. 2e vs. 1e). This capability is not achieved by scramblers, which fail to identify disjoint motifs consistently.

4. **Rigorous synthetic ground truth.** The experiments use known SPI1 (10 bp) and CTCF (12 bp) motifs embedded in 500-bp sequences under three biologically meaningful logical rules, enabling direct comparison of explanation outputs against ground-truth motif positions — a setup where ground truth is known, which is appropriate for initial validation of an explanation method.

## Weaknesses

### Fatal
None.

### Major

1. **No direct measurement of motif-level localization accuracy.** The paper evaluates sufficiency/necessity scores, base-pair counts, and region counts, but never computes precision, recall, or intersection-over-union between the identified important base pairs and the *known ground-truth motif positions* (the 10-bp SPI1 and 12-bp CTCF instances). The ground truth is fully known in the synthetic setup, so this measurement is straightforward. Without it, the core claim that MEMs "accurately identify important motifs" is supported only indirectly — we know the *counts* and *regions* are approximately right, but not whether the *actual base pairs* align with the true motif footprints. This also means a reader cannot tell whether MEMs' advantage over scramblers is meaningful for the actual task of motif localization or is partly an artifact of the training objective (since s-MEMs and n-MEMs are trained to optimize sufficiency/necessity, and the main evaluation metrics are the same sufficiency/necessity scores). *Evidence: The paper describes evaluation metrics in Section 4 (line 184) as sufficiency, necessity, base-pair count, and region count — no precision, recall, or overlap with ground-truth positions is reported.*

2. **Evaluation only on synthetic data with a single, hand-trained predictor and clean motifs.** All experiments use a single synthetic dataset (500-bp sequences, two exact PFM-copy motifs with no degeneracy, no overlapping motif instances, no varying motif strength, no background structure) and a residual network trained on that same synthetic data. The paper makes broad claims about "interpreting complex genomic models" and "paving the way for better understanding of transcription-factor binding" (Conclusion, line 249) but includes no experiment with real ChIP-seq/ATAC-seq data, a real genomic DNN (e.g., DeepSEA, Basenji, BPNet), or a biologically realistic sequence distribution. Real genomic sequences include degenerate motif instances, overlapping motifs, variable motif strength, and complex background nucleotide composition — none of which are tested. This does not invalidate the method, but it sharply limits the strength of the broader claims. The paper would benefit from acknowledging these scope limitations explicitly and from at least one experiment demonstrating applicability to a real genomic task (e.g., motif enrichment analysis on a published DNN). *Evidence: Section 4 (line 177) describes the synthetic setup; the Conclusion (lines 247–250) makes broad claims about "interpreting complex genomic models" without caveats.*

### Minor

3. **Syntax "discovery" is a manual interpretation exercise, not an algorithmic product of MEMs.** The paper lists "Uncovering Logical Syntax via Sufficiency and Necessity" as a contribution (line 41), but the deduction of syntax in Sections 4.1.1–4.1.3 is done by the authors looking at the sizes of sufficient/necessary sets and concluding the rule by hand. There is no formal decision rule, no algorithm, and no quantitative metric for syntax identification. What MEMs provide is *accurate sufficient and necessary sets* — the human then deduces the syntax from those sets. This is a meaningful capability (since scramblers' outputs are too noisy for reliable deduction), but the paper should be precise about what MEMs contribute vs. what the human analyst contributes. A simple rule (e.g., "if sufficiency-set size = 2 and necessity-set size = 1 → cooperative") evaluated quantitatively would substantially strengthen this claim. *Evidence: The paper concludes cooperative syntax with "Thus, we can deduce..." (line 206); redundant with "Therefore, we can conclude..." (line 222); repressive with "we can ultimately deduce..." (line 240) — all manual inferences from MEM outputs.*

4. **No ablation isolating the contiguity regularizer.** The regularizer (Eq. 17) combines an $\ell_1$ sparsity penalty with a $\sigma$-based contiguity term adapted from an NLP sentiment analysis method (Brinner & Zarrieß, 2023). The paper does not test whether the $\sigma$-based contiguity term is necessary or whether simpler alternatives (e.g., total variation penalty) would work as well. An ablation comparing MEMs with the full regularizer against a version using only the $\ell_1$ penalty would isolate the value of the novel contiguity mechanism and clarify its contribution beyond sparsity.

5. **Comparison limited to scramblers.** The introduction (line 29) criticizes a broad set of methods (CAM, LIME, gradient-based, Shapley-based) for being noisy or computationally expensive, but none are included in the experimental comparison. While the authors correctly identify scramblers as the relevant SOTA model-based method, including at least one standard feature-attribution method (e.g., Integrated Gradients + a thresholding/motif-clustering pipeline) would help readers situate MEMs relative to the broader literature. This is a minor issue because comparing to the SOTA is the standard approach, but it does limit the evidence for the claim that MEMs overcome the limitations of the broader class of methods.

6. **No discussion of limitations.** The paper does not discuss what happens when motifs overlap, when motif instances are degenerate, when the predictor is imperfect, or when there are more than two motifs — all common in real genomics. A brief limitations paragraph would strengthen the paper significantly.

### Trivial

7. **Choice of hard predicted class vs. continuous output.** Definition 1 uses the hard predicted class $\hat{Y}(\mathbf{x}) = \mathbb{1}[f(\mathbf{x}) \ge 0.5]$ rather than the continuous $f(\mathbf{x})$ for defining sufficiency and necessity. This discards prediction confidence information and differs from the original Bharti et al. (2024) formulation. This is a defensible design choice, but it is uncommented and could affect sensitivity for borderline predictions.

## Nice-to-Haves

- **Automated syntax deduction rule.** A simple decision procedure based on thresholded sizes of s-MEM and n-MEM output sets (e.g., for cooperative: sufficiency-set size ≥ 2 & necessity-set size = 1 → cooperative; for redundant: sufficiency-set size = 1 & necessity-set size ∈ {1,2} → redundant) evaluated on held-out sequences would turn the manual interpretation into a reproducible, quantitative result.
- **Threshold selection guidance.** The paper evaluates across all thresholds $t$, but a user would need a concrete rule. A simple heuristic (e.g., choose $t$ based on the expected total motif length) would improve practical applicability.
- **Ablation of the contiguity regularizer** as described in Weakness 4.
- **Real-data demonstration.** Even a single experiment on a published genomic DNN with known TF motifs would dramatically increase credibility.

## Removed Points

These points were identified by the reviewers but are removed or downgraded per the review guidelines:

- **Criticism that λ₁ and λ₂ are unspecified** — Removed. The paper references Appendices A.1 and A.2 (line 184) for implementation details. The parser strips appendix content from all papers, so these hyperparameter values may be present in the original submission.
- **Criticism that scrambler normalization may disadvantage scramblers** — Removed. This is speculative with no evidence that the min-max information-content normalization actually harms scrambler performance.
- **Criticism about missing related works** — Removed. The reviewer cannot independently confirm the existence of missing references.
- **Criticism that the paper should "also cover Y / domain Z"** — Removed as scope creep. The paper's direction (motif identification + syntax) is well-defined; demands for broader coverage belong in Nice-to-Haves at most.
- **"Fatal" framing of the syntax-discovery criticism** — Downgraded to Minor. The paper's contribution is that MEMs produce accurate enough sufficient/necessary sets to *enable* syntax deduction, not that MEMs automate the deduction. The demonstration is valid even if not fully algorithmic.

## Novel Insights

The most interesting observation that emerges from reading the reviews against the paper is the mismatch between the paper's evaluation strategy and its strongest claim. The paper measures sufficiency and necessity — the same quantities its training objectives optimize — as evidence of *motif identification* accuracy. This creates a subtle circularity: the evaluation metrics are directly aligned with the training objective, so good scores on these metrics are partially unsurprising. The more informative evidence comes from the secondary metrics (counts of base pairs and disjoint regions), where the match to ground truth is less directly incentivized by the training loss and therefore more probative of genuine motif discovery. This pattern suggests that future work on model-based explanation should report at least one metric that the training procedure cannot directly optimize — precision/recall against ground-truth positions being the obvious candidate when synthetic data is used.

## Suggestions

1. **Add per-base precision/recall against ground-truth motif positions** as a primary evaluation metric. This directly measures motif identification accuracy and avoids the circularity of reporting the same sufficiency/necessity scores used in training.
2. **Add an ablation** comparing full MEMs against a version with only the $\ell_1$ penalty (no $\sigma$-contiguity term) to isolate the value of the contiguity mechanism.
3. **Formalize the syntax deduction** as a simple decision rule (e.g., threshold-based classification of the s-MEM/n-MEM set sizes) and report classification accuracy on held-out sequences.
4. **Add a limitations paragraph** acknowledging synthetic-data scope, unaddressed complexities (overlapping motifs, degeneracy, imperfect predictors), and the manual nature of syntax deduction.
5. **Tone down the broader claims** in the conclusion — the paper demonstrates a clear improvement over scramblers on synthetic data, but claims about "complex genomic models" and "understanding transcription-factor binding" should be appropriately caveated.

## Score and Decision

The paper presents a well-motivated method with a clear advantage over the SOTA in synthetic experiments. The core idea — embedding biological priors into a sufficiency/necessity explanation framework — is sound and novel. However, two evaluation gaps prevent the paper from fully supporting its claims: (1) the absence of direct motif-level localization accuracy (precision/recall against ground truth), and (2) the restriction to synthetic data with clean motifs. These are addressable but currently limit the strength of the contribution. The syntax-discovery claim also needs clearer framing as a human-interpretation exercise enabled by MEM outputs rather than an automated capability of MEMs themselves.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
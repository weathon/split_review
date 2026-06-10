## Summary

This paper proposes two synthetic datasets (SHAPES and CHARS) for controlled probing of OOD detection methods by varying individual visual attributes (color, class) independently while holding others constant. The authors evaluate 13 OOD detection methods across 10 architectures on these datasets under three controlled scenarios (OOD in color, OOD in class, OOD in both) and additionally study the effect of image corruption. The central finding is that many standard OOD methods (MSP, ODIN, MaxLogit) produce AUROC scores as low as 0.01 on color shifts — systematically assigning *higher* scores to OOD samples than ID samples — pointing to a failure mode that prior confounded benchmarks could not isolate.

## Strengths

- **Controlled per-attribute isolation of distribution shifts**: The paper's key design contribution is that SHAPES and CHARS vary exactly one visual attribute (color or class) at a time while holding all others constant, with ID and OOD attribute sets explicitly disjoint (Section 2, lines 24–31). No prior OOD benchmark offers this level of disentanglement, enabling the direct attribution of detection failures to specific attribute types.

- **Demonstration of systematic score inversion on color shifts**: The paper shows that for "OOD in color" scenarios, many methods (MSP, ODIN, MaxLogit, etc.) achieve AUROC as low as 0.01 — worse than random — with the normalized score distributions (Figure 3, line 69) confirming that OOD samples receive *higher* scores than ID samples, opposite to intended behavior. This non-obvious failure pattern could not be surfaced by benchmarks that confound multiple attribute changes.

- **Overlap-coefficient analysis of corruption effects**: The paper introduces the overlap coefficient (Eq. 1, lines 57–61) to quantify how image corruption collapses the distinction between ID and OOD score distributions. Figure 4 (line 76) shows that corruption systematically increases overlap across all 130 method-backbone combinations, supporting the conjecture that a corrupted ID image becomes indistinguishable from an OOD image.

- **Comprehensive architecture and method coverage**: The evaluation spans 10 architectures from four families (ResNet, DenseNet, ViT, WideResNet) and 13 OOD methods covering logit-based, feature-based, and energy-based approaches (Section 3.1, lines 51–53), with training from scratch on both datasets using three random seeds. This breadth provides reasonable generality within the synthetic setting.

- **Reproducibility via fixed-seed configuration pre-generation**: All image configurations are pre-generated with a fixed random seed and rendered dynamically in the dataloader (line 33), ensuring exact reproducibility of attribute sets, splits, and corruption assignments.

## Weaknesses

### Fatal
None.

### Major

1. **No tabular summary of benchmark results, and Figure 5 is referenced but never introduced.** The paper evaluates 13 methods × 10 architectures × 3 scenarios × 2 datasets × 2 corruption conditions (1,560+ combinations), yet not a single AUROC table is provided. All results are embedded in figures (Figure 2, Figure 5) with no numerical anchors in the text. A benchmark paper that does not present its own benchmark results in a usable form cannot serve its intended purpose. Furthermore, Figure 5 is referenced on line 78 ("relative to Figure 2 and Figure 5 respectively") without being introduced or captioned anywhere in the text — the reader cannot locate or interpret it. This is a structural omission for a dataset/benchmark paper.

2. **No dataset statistics are provided.** For a paper whose primary contribution is two new datasets, the absence of basic statistics is a critical gap. The paper does not report: number of ID classes per dataset, number of OOD classes, total image counts per split (train/val/ID-test/OOD-test), image resolution, color palette details, or exact size/rotation/position ranges. Section 2 (lines 24–34) describes the generation pipeline at a high level but omits all quantitative specifications needed to reproduce or use the datasets.

3. **The overlap coefficient (Eq. 1) is not properly defined.** The equation states `overlap(A,B) = |A ∩ B|` with the note "set notations used for the sake of brevity" (line 63), but the paper never specifies how continuous score densities are binarized into sets, what the domain of integration is, or how smoothing is performed. This makes the central analysis in Section 3.3 non-reproducible and the metric non-operational.

4. **The image corruption analysis aggregates all corruption types indiscriminately.** The paper mixes ten corruption types at two severity levels into a single analysis (line 33, line 76), concluding that "an ID corrupted image is as bad as an OOD image." Different corruptions (e.g., Gaussian noise vs. JPEG compression vs. snow) likely have very different effects on OOD score distributions. By aggregating across all types, the paper may be obscuring the most informative patterns. At minimum, a breakdown by corruption type is needed, or justification for why aggregation is meaningful.

5. **Hyperparameter configuration for OOD methods is not specified.** The paper states that "All OOD detection methods are implemented using the OpenOOD framework" (line 53) but does not indicate whether method-specific hyperparameters were tuned for the synthetic domain or whether OpenOOD defaults (designed for ImageNet/CIFAR-scale features) were used as-is. If defaults intended for natural-image features were applied to synthetic shapes, this alone could explain the poor performance.

### Minor

1. **The central finding (score inversion on color shifts) is reported but not diagnosed.** The paper shows that many methods systematically invert on color changes (AUROC ≈ 0.01) and attributes this to "sensitivity" to color (line 69), but offers no mechanistic analysis. Key diagnostic questions remain unaddressed: Is the inversion consistent across all OOD colors or driven by specific hues? Does the classifier learn color-based shortcuts during training? Are penultimate-layer representations forming color-based clusters? While a benchmark paper's primary deliverable is the observation itself, the lack of any diagnostic experiment limits the actionable insight the community can extract.

2. **The "OOD in both" scenario results are under-described for the uncorrupted case.** Figure 2 is described as presenting AUROC for "two OOD scenarios: OOD in color and OOD in class" (line 67). The OOD in both scenario is mentioned only through score distributions (line 69) and in the corruption analysis. Results for all three scenarios should be presented systematically for both corrupted and uncorrupted settings.

3. **Section 3.3 contains a confusing and potentially contradictory sentence.** Line 78 states: "we can observe a slight increase in the AUROC for OOD in color and OOD in both color and class cases … there is a decrease in AUROC for OOD in color scenario." These two statements about OOD in color (increase vs. decrease) need clarification — they likely refer to different reference conditions (Figure 2 vs. Figure 5) but the parallel construction is ambiguous.

4. **The overlap coefficient does not account for score directionality.** The overlap coefficient measures distribution overlap after min-max normalization (line 57), but if OOD scores are systematically *inverted* relative to ID scores (as happens with AUROC ≈ 0.01), the distributions could be well-separated (low overlap) while detection is inverted. The paper also reports AUROC, which captures direction, but the overlap analysis in Section 3.3 does not acknowledge this confound.

5. **No limitations are discussed.** A benchmark paper proposing synthetic datasets should include a frank discussion of limitations (e.g., synthetic-to-real transfer considerations, scope boundaries). The conclusion (lines 99–110) is generic and does not address limitations.

### Trivial
None.

## Nice-to-Haves

- A per-corruption-type breakdown of the overlap-coefficient analysis would substantially strengthen the corruption study.
- A simple diagnostic experiment on the color inversion (e.g., training on grayscale images, or checking whether the inversion is hue-dependent) would elevate the paper's main empirical finding from observation to insight.
- Including a discussion of how the synthetic-to-real gap might affect the interpretation of results would help the community use the benchmark appropriately.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Weakness: "The synthetic-to-real transfer gap is unaddressed."** The paper's stated scope is to probe OOD methods with controlled synthetic data, not to establish that results transfer to real images. Criticizing the absence of a real-image discussion demands the paper address a problem outside its stated contribution. Removed per scope-creep rule.
- **Weakness: "Only two of three OOD scenarios discussed for uncorrupted case."** The paper does mention OOD in both for uncorrupted images (line 69: "score distributions for OOD in color and OOD in both color and class scenarios remain similar"). The critic overstated the omission, though the presentation is indeed less complete for this scenario. Remaining concern folded into Minor weakness #2.
- **Weakness about missing related works (dSprites, 3DShapes).** Per instructions, I cannot mention missing related works without external sources to verify their relevance. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add at least one table per dataset showing AUROC for every (method, architecture, scenario) combination — this is essential for a benchmark paper and would make the results usable without requiring readers to reverse-engineer figures.
2. Provide full dataset statistics in a table: number of classes per split, image count per split, image resolution, attribute ranges (color palette, size, rotation, position).
3. Formally define the overlap coefficient with continuous-domain notation, specifying the smoothing procedure and the binarization rule.
4. Include a breakdown of corruption effects by corruption type (e.g., grouped by category: noise, blur, weather, digital) to avoid losing signal through aggregation.
5. State whether OpenOOD default hyperparameters were used or whether they were tuned for the synthetic domain.
6. Add one diagnostic experiment for the color inversion (e.g., per-hue analysis or grayscale training) to move from observation to insight.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
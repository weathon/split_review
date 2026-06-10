## Summary

This paper proposes the Patch Ranking Map (PRM), a method that applies an ensemble of feature selection (FS) methods to CNN feature maps and aggregates their selections into spatial importance matrices that rank image patches. Applied to Alzheimer's MRI classification with a ResNet50 backbone, the paper reports consistent top-patch rankings across different FS methods and reduced model size with maintained/comparable accuracy.

## Strengths

- **Cross-method consensus on top features is empirically robust**: Feature 11738 is ranked #1 by all seven FS methods (Chi2, f_regression, f_classif, RFE, etc.) independently at three different feature-set sizes (100, 400, 800). This level of inter-method agreement is non-trivial and suggests the identified features are genuinely discriminative rather than artifacts of a single selection criterion (Section 5.1, Table 3, line 110).

- **Consistent top-two patch rankings across conditions**: The same two patches [(11,7) and (6,8)] emerge as most important across three independently constructed common-feature sets (188, 65, and 12 features) and three different weighting values (ω=0.3, 0.5, 0.7) — nine configurations in total (Section 5.3, lines 127–130, Figs. 5–7). This stability is the paper's strongest empirical result.

- **Measurable model-size reduction**: Using only 100 out of 16,384 features (eliminating 23 of 64 original feature maps) while maintaining or slightly improving test accuracy (baseline 0.9642) demonstrates a concrete efficiency gain (Section 5.1, line 100, Tables 1–2).

## Weaknesses

### Major

- **Structural misalignment between claimed contribution and delivered method**: The title and abstract claim the PRM explains "the relationship among an input image…and the final classification decision" (abstract, line 4). In reality, the PRM is a dataset-level feature importance aggregation: the FS methods select features based on label correlations across the *entire training set*, producing a static feature accumulation matrix and feature ranking matrix that are the same for every test image. Two images of different classes receive the identical PRM. The method identifies which spatial regions contain task-discriminative features, but it does *not* explain why the model made a specific decision for a specific input. This is a fundamental overclaim. The paper compares itself to CAM/Grad-CAM (Section 1, line 12) without acknowledging that those methods provide *per-instance* explanations — a fundamentally different capability.

- **No evaluation against any existing explainability method**: The paper criticizes CAM-based heatmaps for not "deeply analyzing" relationships (Section 1, line 12) but provides zero comparisons — neither quantitative (deletion/insertion, pointing game, ROAR) nor qualitative (side-by-side with Grad-CAM, LIME, or SHAP) — against any existing explanation method. The experiments compare the FS-augmented model to vanilla ResNet50 only on accuracy and model size, metrics that do not evaluate explanation quality. The central contribution goes unevaluated; there is no evidence that the PRM is more informative or useful than existing alternatives.

- **Core algorithm parameters (α, β) left undefined**: The patch ranking function is θ_{ij} = ω × (β_{ij} − α_{ij}) + α_{ij} (line 127, Section 5.3). α and β are never defined anywhere in the paper. Since this function is the core of the patch-ranking algorithm, the method is irreproducible without guessing what these symbols refer to. ω is described only by its tested values, not by what it weights.

- **No per-class metrics despite severe class imbalance**: The dataset has 64 "Moderate Demented" images out of 6,400 (1%), with the majority class "Non Demented" at 3,200 (50%). Only overall test accuracy (0.9642) is reported. On a 4-class problem with this imbalance, 96%+ accuracy can be achieved by classifying everything as "Non Demented" or "Very Mild Demented." Without per-class precision, recall, F1, or a confusion matrix, the reported accuracy is uninformative about actual model quality (Section 5, line 89).

- **No statistical significance reported**: All results appear to come from a single run. No error bars, confidence intervals, or multiple seeds are reported. Given that the key "FS improves accuracy" claim is about small margins against a 96.42% baseline, variance cannot be assessed.

### Minor

- **The Alzheimer's disease analysis that motivates the paper is deferred entirely to future work**: The paper identifies patches at (11,7) and (6,8) as "most informative" but never connects them to specific brain regions or cites medical literature. The abstract promises "the relationship among brain regions associated with Alzheimer's disease…will be analyzed" (line 4); Section 7 similarly states this "will be analyzed." A paper that makes medical significance a pillar of its motivation but defers the medical analysis has not delivered that significance.

- **Single dataset**: All results are on one Alzheimer's MRI dataset. While acceptable for a methodological paper, it limits confidence in generalizability, especially given the specific dataset characteristics (128×128 resolution, 16×16 feature maps with 8×8 patches).

### Trivial

- The phrase "feature m aps" (line 47) is garbled, though this may be a parser artifact.

## Nice-to-Haves

- A qualitative comparison showing PRMs alongside Grad-CAM heatmaps for the same test images would immediately clarify whether the PRM offers complementary or superior information.
- Per-class metrics and a confusion matrix would address the class imbalance concern.
- A description of what α and β represent (even if they are simply the feature accumulation value and feature ranking value at location (i,j)) would resolve the reproducibility gap.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Algorithm 1 and Algorithm 2 are absent from the parsed text"** — The parser strips algorithmic blocks from all submissions. The original PDF likely includes them. Removed per hard rule about missing appendix/algorithm content.
- **"Definition 2's special case sentence trails off ungrammatically"** — This is a parser artifact (garbled sentence ending "because FS is not performed."). Removed per formatting-artifact rule.
- **"Definition 3 references feature maps T which is undefined"** — T is defined in Definition 1 as the top feature map. The paper says "K is the number of feature maps T," which is coherent. The critic misread this section. Removed as factually incorrect.
- **"Notation for feature ranking matrix underspecified"** — Partially overlaps with the α/β issue already listed. The RFE ranking step is adequately described (line 55). Removed to avoid duplication.
- **"The multi-phase FS algorithm is unclear"** — The concept is described adequately in line 70 and illustrated through the enumerated methods in line 98. While Algorithm 1 is not in the parsed text, the seven methods are listed explicitly. Removed — the text is sufficient for understanding.
- **Strength: "The paper addresses an important problem"** — Generic/superficial. Removed per strength filtering discipline.
- **Strength: "Specific, actionable patch-level localization"** — While the paper identifies specific coordinates (11,7), the strength overstates the actionability since the patches have not been validated against brain anatomy. Downgraded via weakness handling.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the ensemble-of-FS-methods approach produces more stable feature rankings than any single method, evidenced by feature 11738's unanimous #1 ranking across seven diverse FS algorithms. This cross-method consensus *does* strengthen the case that these are meaningful features rather than method-specific noise. However, this observation does not rescue the core weakness — that the PRM is a static task-level map rather than an instance-level explanation, and that it was never evaluated against any existing explanation method.

## Suggestions

1. Reframe the contribution honestly: the PRM is a **task-level discriminative region map** generated from an ensemble of FS methods, not a per-instance decision explanation. Rewrite the title and abstract to match.
2. Add at minimum a qualitative comparison to Grad-CAM on the same test images.
3. Define α and β explicitly, or rewrite the ranking function with transparent notation.
4. Report per-class precision/recall/F1 and a confusion matrix.
5. Add error bars over multiple runs with different random seeds.
6. Either perform the medical analysis connecting patches to brain regions, or drop the medical framing entirely and present the method on a domain-agnostic benchmark.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
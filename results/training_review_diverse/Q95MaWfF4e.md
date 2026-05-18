Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper identifies a genuine, overlooked failure mode in standard Concept Activation Vectors (CAVs): linear classifiers (SVM, logistic, ridge, lasso) optimize for class *separability*, causing their weight vectors (filters) to pick up distractor signals that diverge from the true concept *signal* direction. The authors propose pattern-CAVs, derived from Haufe et al.'s signal–distractor decomposition (a linear regression of activations onto concept labels), which isolate the concept signal. Controlled experiments on ISIC2019, Pediatric Bone Age, and FunnyBirds datasets with VGG16, ResNet18, and EfficientNet-B0 show that pattern-CAVs achieve significantly higher cosine similarity to ground-truth concept directions and improve downstream applications (TCAV sensitivity testing and RRClArC model correction).

## Strengths

- **Principled identification and fix of a real CAV failure mode:** The paper shows formally and via 2D toy experiments that separability-oriented filters diverge from the concept signal direction due to distractor components, while pattern-CAVs (Eq. 4, based on a regression of activations onto concept labels) recover the signal. The 2D toy experiments (Fig. 1, bottom) cleanly illustrate the structural divergence — this is not a tuning artifact.

- **Comprehensive quantitative evidence across architectures, layers, and datasets:** Pattern-CAVs achieve higher cosine similarity to the ground-truth concept direction across all 13 Conv layers of VGG16 on three controlled datasets (Fig. 3, top). The advantage holds across VGG16, ResNet18, and EfficientNet-B0 in TCAV (Fig. 6) and RRClArC (Table 1) experiments.

- **Hyperparameter-free and invariant to feature preprocessing:** Unlike filter-CAVs, pattern-CAVs require no tuning of regularization strength and produce identical alignment regardless of centering, max-scaling, or their combination (Fig. 4). This is a practical advantage for reproducibility and ease of use.

- **Controlled experimental design with ground-truth directions:** The insertion of artificial concepts (timestamps, brightness) with known ground-truth directions enables direct measurement of alignment (cosine similarity) and ground-truth TCAV scores, providing objective evidence beyond qualitative or proxy metrics.

- **Qualitative evidence reinforces the quantitative story:** Neuron visualizations (Fig. 2) and concept-sensitivity maps (Fig. 7) show pattern-CAVs focusing on the intended concept while filter-CAVs pick up noisy or irrelevant features. Model correction heatmaps (Fig. 8) further confirm the practical impact.

## Weaknesses

### Major

- **Hyperparameter tuning for filter-CAV baselines is underspecified.** The paper compares pattern-CAVs against four filter-CAV variants (SVM, lasso, logistic, ridge) but never states how their regularization parameters were chosen. Were they tuned via cross-validation on the CAV training set, or were defaults used? If defaults were used, the quantitative comparisons (Figs. 3–6, Table 1) may understate the best possible filter-CAV performance, and the reader cannot assess whether a well-tuned filter-CAV would close the gap. The core theoretical argument (structural divergence to optimize separability) is not harmed, but the empirical comparisons lose force. The authors should clarify the tuning procedure and, ideally, report results across a range of regularization strengths to demonstrate robustness.

- **The central claim is only tested under the assumption that distractors are independent of concept labels.** All controlled experiments enforce independence (distractors are randomly assigned to classes). In realistic scenarios where distractors are *correlated* with the concept (e.g., band-aids co-occurring with certain lesion types), the pattern-CAV estimate $\mathbb{E}[a \mid t=+1] - \mathbb{E}[a \mid t=-1]$ will also capture those spurious correlations. The paper mentions this only tangentially in the conclusion ("disentanglement of correlated concept directions" as future work) but does not test this regime. A controlled experiment with correlated distractors (even in the 2D toy setting) would clarify the boundary conditions of the method.

### Minor

- **The ResNet18 and Bone Age exceptions are acknowledged but not investigated.** All CAV variants achieve perfect TCAV scores for ResNet18 (Fig. 6), and filter-CAVs match pattern-CAVs on Bone Age biased accuracy (Table 1). The paper mentions these in passing but does not explore *why* they occur — whether due to different representational geometry, linear separability properties, or dataset-specific factors. A brief diagnostic (e.g., measuring linear separability of concept representations across architectures) would strengthen the discussion.

- **Confidence intervals are not reported for Table 1 (ClArC results).** The alignment experiments (Fig. 3) include standard errors, but the model correction results in Table 1 lack error bars or significance tests. Given the variability across seeds in finetuning, reporting standard deviations or confidence intervals would improve rigor.

- **The claim in the Limitations section about filter-CAVs being preferable for post-hoc concept bottleneck models is stated without direct experimental support.** While the paper shows filter-CAVs have higher concept separability (AUC) in Fig. 3 (bottom), the specific claim about post-hoc concept bottleneck models is not tested. This does not affect the main contribution but would benefit from a small validation experiment.

### Trivial

- The paper uses "CAV" to denote both the vector and the method, and the text occasionally jumps between "pattern", "pattern-CAV", and "pattern-based CAV" without consistent differentiation from "filter-CAV." This is a minor prose issue that does not affect comprehension.

## Nice-to-Haves

- A 2D toy experiment with distractors *correlated* with the concept label (even in 2D) would directly test the scope of the central claim regarding the independence assumption.
- Explicit grid search over regularization parameters for filter-CAVs (e.g., C ∈ {0.01, 0.1, 1, 10, 100}) would eliminate concerns about unfair comparison.
- An analysis of why ResNet18 yields perfect TCAV scores for all CAV variants (e.g., measuring concept representation linearity across architectures) would help practitioners.
- Making the controlled experiment code and data publicly available would aid reproducibility.
- Reporting error bars for the ClArC results in Table 1 would increase rigor.

## Removed Points

These points were flagged by reviewers but are factually incorrect, reflect reviewer knowledge gaps, or violate the filtering rules:

1. *"Qualitative visualizations shown for a single layer of a single model"* — **Removed (factually wrong).** The paper shows qualitative results for VGG16 (Figs. 2, 8) *and* both VGG16 and EfficientNet-B0 (Fig. 7 — concept-sensitivity maps).
2. *"Does not provide confidence intervals or statistical tests for alignment scores (Fig. 3)"* — **Removed (partially inaccurate).** Line 215 states the figure presents "including standard errors, for both CAV alignment (top) and separability (bottom)."
3. *"Code and data for controlled experiments not mentioned"* — **Downgraded to Nice-to-Haves.** Code release is a practical concern, not a scientific weakness, and the parser may have stripped a reproducibility statement.

## Novel Insights

None beyond the paper's own contributions. The reviews largely confirm the paper's framing rather than revealing unexpected implications.

## Suggestions

1. **Clarify the hyperparameter selection procedure** for all filter-CAV baselines. State whether cross-validation was used, report the selected values, and ideally show results across a sweep of regularization strengths.
2. **Add a controlled experiment with correlated distractors** (even in 2D). This would either strengthen the central claim if pattern-CAVs still win, or honestly delineate its boundary conditions.
3. **Add a brief diagnostic** to explain why ResNet18 gives perfect TCAV scores for all CAV variants. This addresses the natural reader question about model-dependence.
4. **Report bootstrap confidence intervals** for the key metrics in Table 1 across finetuning seeds.
5. **Explicitly qualify** the scope of the main claim in the Limitations section with respect to the independence assumption.

## Score and Decision

The paper makes a clean, well-motivated contribution: it identifies a genuine structural flaw in standard CAV computation, provides a principled fix with a simple closed-form solution, and demonstrates practical benefits across multiple architectures, datasets, and applications. The weaknesses (underspecified hyperparameter tuning, untested correlated-distractor regime) are significant enough to require clarification but do not undermine the core theoretical contribution. The paper merits acceptance conditional on the authors addressing the hyperparameter clarification and independence-scope qualification in revision.

**Originality:** High — the signal-vs-separability distinction for CAVs is novel and practically important.  
**Importance of question:** High — CAVs are widely used in XAI.  
**Claims supported:** Mostly well-supported; scope qualification needed for correlated-distractor regimes.  
**Soundness:** Good — controlled experiments are well-designed; the main gap is in baseline tuning documentation.  
**Clarity:** Good.  
**Value to community:** High — practitioners can immediately adopt the hyperparameter-free pattern-CAV as a drop-in replacement.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
## Summary

This paper proposes a pipeline for explainable 3D medical imaging that: (1) applies feature selection before Grad-CAM to produce sparser, more interpretable heatmaps (FS-Grad-CAM), (2) ranks 2D image patches using five defined feature/heatmap matrices, (3) fuses axial, coronal, and sagittal patch rankings into a 3D Block Ranking Map (BRM), and (4) ensembles multiple feature-selection pipelines into a hybrid BRM. The method is evaluated on ADNI (982 3D brain images, three-class AD diagnosis) and an autism dataset (286 images).

## Strengths

1. **FS-Grad-CAM produces visually cleaner heatmaps than standard Grad-CAM.** The paper shows (Section 4.1, Figures 2a-d; described in text lines 168-169) that applying feature selection before CAM-based heatmap generation eliminates highlighted patches outside the brain, whereas standard Grad-CAM using all 16,384 features highlights large irrelevant areas. This is a concrete, well-motivated improvement with direct visual evidence.

2. **Multi-plane fusion with cross-view agreement is a novel design choice.** The 3D block ranking (Algorithm 2, Step 1, line 147) requires positive ranking scores from all three anatomical planes (θⱼₖ > 0, θᵢₖ > 0, θᵢⱼ > 0) before a block is scored, acting as a spatial consistency filter. This is clearly stated and distinguishes the approach from methods that operate directly on 3D volumes.

3. **Two-dataset evaluation covering AD and autism.** The method is applied to two distinct 3D medical imaging datasets with different diseases (AD diagnosis, autism diagnosis), providing more breadth than single-dataset evaluations in this space.

## Weaknesses

### Fatal

1. **The core algorithms are not specified, making the paper incomplete as a method contribution.** Algorithm 1 (the 5-factor 2D patch ranking algorithm, lines 127-130) lists only its five input matrices — a feature distribution matrix, a feature ranking matrix, an average feature ranking matrix, a heatmap activation matrix, and a heatmap strength matrix — but presents **no body, no steps, and no description** of how these five factors are combined into a ranking score. The sections before and after (lines 125-126 and Section 3 heading at line 133) contain only motivation; the algorithm itself is entirely absent. Algorithm 2's combination function φ_ijk = f(θ_jk, θ_ik, θ_ij) is defined only as "a monotonically non-decreasing function" (line 147) with no concrete specification. Algorithm 3 (the hybrid 3D block ranking algorithm) is referenced (lines 143, 152) but never shown. A method paper that does not specify its method cannot be evaluated, reproduced, or built upon. This alone is a fatal flaw for any conference, and certainly for ICLR.

2. **No quantitative evaluation of the ranking quality and no baseline comparisons.** The "experiments" proceed as follows: (a) train CNNs on axial, coronal, and sagittal slices, (b) apply the ranking pipeline, (c) list the top-10 blocks, (d) look up each block's anatomical region using the "ebrains" tool, and (e) check whether ChatGPT and/or the literature confirm that region is disease-relevant (Sections 4.2, 5). There are **no baseline comparisons** — not against standard 2D Grad-CAM aggregated to 3D blocks, not against 3D Grad-CAM, not against a random ranking, not against a simpler aggregation rule (e.g., averaging 2D heatmaps). There are **no ablation studies** isolating the contribution of any component (feature selection, individual factors, the multi-plane fusion, the ensemble). There are **no quantitative metrics** of ranking quality — no insertion/deletion curves, no removal-based fidelity measures, no overlap with known atrophy maps, no inter-rater agreement. The sole evidence is that the top-10 blocks happen to fall in brain regions that are known from decades of neuroscience to be associated with AD and autism. At an ICLR-level venue, this is not a valid evaluation of a proposed method.

### Major

3. **Data leakage from slice-level train/test split.** 19,640 slice images are extracted from 982 3D scans (20 slices per scan; line 159), then split 70%/30% at the slice level: "13, 748 training images (i.e., 70% of the 19, 640 images) and 2, 636 testing images (i.e., 30% of the 19, 640 images)" (line 159). Slices from the same 3D scan (patient) can appear in both training and test sets. This is a well-documented leakage problem in medical imaging, and the reported testing accuracies of 0.9309–0.9897 are therefore unreliable. Since the explanations are derived from these models, the problem propagates to the ranking results.

4. **Validation via ChatGPT and literature lookup is insufficient.** The paper uses ChatGPT and publications to confirm that each identified brain area is "associated with" AD or autism (Section 4.2, lines 173-180; Section 5, line 207). The top-ranked blocks include the most canonical AD-relevant regions (hippocampus, entorhinal cortex, temporal lobe — exactly the regions one would expect any reasonable method to find). Without baselines showing that alternative ranking methods or even a random ranking would *not* also identify these regions, or that the method can discriminate AD-relevant from AD-irrelevant regions, this validation does not establish the method's effectiveness.

5. **No CNN architecture or training details are provided.** Section 4 reports testing accuracies for three CNNs (axial, coronal, sagittal) but provides zero information about architecture (depth, layer types, number of parameters), optimization (learning rate, optimizer, batch size), regularization, or any training details. This makes the experiments irreproducible.

6. **The hybrid approach's claimed benefit is unsubstantiated.** The paper states that the hybrid BRM "reduces the bias of one 3D image block ranking algorithm" (line 152) but provides no experiment comparing the outputs of single-ranking vs. hybrid-ranking to support this claim.

### Minor

- **Definition numbering errors.** Definition 6 is used twice (line 74 for "average feature ranking matrix" and line 80 for "heatmap count matrix"); Definitions 4 and 9 are missing entirely. The "feature distribution matrix" is referenced in Algorithm 1's input list (line 129) but never formally defined as a numbered definition.
- **No statistical reporting.** No confidence intervals, variance across runs, or significance tests are reported for any result.
- **The specificity of identified sub-regions is not analyzed.** The paper claims the method identifies "small 3D blocks in large 3D brain regions" (line 188) but provides no analysis showing that the sub-regions within a structure (e.g., which specific part of the hippocampus) are more precise than what conventional methods would produce.
- **Several future work items are basic validation steps.** For example, "find[ing] a precise function mapping indices to world coordinates" (future work item 5, line 227) appears to be needed for the evaluation already presented, and evaluating on "other 3D data sets" (item 7) is a standard validation step that should be part of the current contribution.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Provide the complete algorithms: the 5-factor 2D patch ranking (exactly how the five matrices are combined), the combination function f in Algorithm 2, and the hybrid Algorithm 3.
- Add a fidelity/removal evaluation: remove top-ranked vs. bottom-ranked vs. random blocks and measure the drop in classifier accuracy.
- Compare against at least one baseline (e.g., 2D Grad-CAM patches aggregated to 3D blocks, or 3D Grad-CAM).
- Perform a patient-level split and re-report classification metrics with confidence intervals.
- Provide CNN architecture and training hyperparameters sufficient for reproduction.
- Add an ablation isolating the contribution of the multi-plane fusion vs. single-plane ranking.

## Removed Points

These points were flagged by the input reviews but filtered out as invalid, noise, or not the paper's fault.

- **"Self-fulfilling" claim about brain-area ranking.** The harsh critic argued that because features outside the brain are eliminated (line 165), finding top-ranked blocks in disease-relevant brain areas is "largely a self-fulfilling result." This is inaccurate: eliminating non-brain features constrains blocks to the brain but does *not* guarantee they land in disease-relevant sub-regions such as hippocampus or entorhinal cortex. Many brain regions (cerebellum, occipital pole) are not strongly AD-associated. The finding that top-10 blocks specifically fall in known AD-relevant regions is non-trivial — though the lack of baselines means we cannot quantify the method's added value. Removed as factually overstated.

- **"Straw-man framing" about patch ranking.** The critic claimed the paper's statement that existing methods "cannot rank patches based on the number of associated features" (lines 48-49) is a straw-man. The paper's claim is specifically about ranking *by feature count* — which is indeed impossible when all patches have the same count. This is factually correct. Removed as a misunderstanding.

- **Parser artifacts (mid-sentence start, figure path placeholders, formatting issues).** Removed per hard rules.

- **Stylistic complaints (heavy notation, long future work section).** Subjective preferences, not substantive weaknesses. Removed.

- **"Notation is extremely heavy."** Style comment. Removed.

- **Strength Finder's "quantitative validation" claim.** The strength finder called the validation "quantitative"; it is not. The validation is purely qualitative (cross-referencing against literature). This strength was removed in favor of the more accurate two-dataset breadth point.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard expectation that a method paper must fully specify its algorithms and quantitatively evaluate its outputs; this is a well-known norm rather than a novel insight.

## Suggestions

1. Fully specify the 5-factor 2D patch ranking algorithm (exactly how the five matrices are combined into a ranking score), the combination function f in Algorithm 2, and the hybrid Algorithm 3.
2. Add at least one baseline comparison (e.g., aggregated 2D Grad-CAM, 3D Grad-CAM, or a random ranking) and quantitative fidelity metrics (e.g., insertion/deletion, removal-based fidelity).
3. Address the slice-level data leakage by performing a patient-level split and re-reporting classification metrics with confidence intervals.
4. Provide CNN architecture and training details sufficient for independent reproduction.
5. Add an ablation isolating the contribution of the multi-plane fusion vs. single-plane ranking.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
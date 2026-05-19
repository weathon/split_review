- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6
Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper proposes Progressive3D, a framework for text-to-3D generation from complex prompts (multiple objects with different attributes). The key idea is to decompose the generation into a sequence of local editing steps, each constrained to a user-defined 3D region, with an Overlapped Semantic Component Suppression (OSCS) technique that focuses optimization on the semantic differences between successive prompts. The method is demonstrated on DreamTime, TextMesh, Fantasia3D, and MVDream, with quantitative results on a new CSP-100 benchmark showing large improvements over DreamTime (BLIP-VQA 0.227 → 0.474, human preference 83.2% vs 16.8%).

## Strengths

- **Large, well-documented quantitative gains on the primary baseline.** Table 1 (Sec. 4.2) shows Progressive3D + DreamTime achieves BLIP-VQA 0.474 and mGPT-CoT 0.609, substantially above DreamTime alone (0.227, 0.522) and compositional baselines CEBM and A&E. The human preference result (83.2% vs 16.8% over 20 feedbacks) is consistent with the metric improvement. These gains are the paper's strongest evidence.

- **Clean ablation isolating each component's contribution.** Table 2 (Sec. 4.3) quantifies that the initialization constraint alone raises BLIP-VQA from 0.255 to 0.370, OSCS alone to 0.347, and their combination to 0.474. This cleanly demonstrates that both proposed techniques are individually beneficial and complementary.

- **OSCS technique is well-motivated and empirically validated.** Sec. 3.2 provides a clear derivation of overlapped semantic component suppression via vector projection in noise-prediction space. Figure 5 (Sec. 4.3) shows a sweep over suppression weight W, with W=0.5 producing attribute mismatching and higher W producing correct results — empirically confirming the mechanism.

- **Framework demonstrated across four different 3D representations.** Qualitative results in Figure 4 show Progressive3D integrated with DreamTime (NeRF), TextMesh (SDF), Fantasia3D (DMTet), and MVDream (multi-view NeRF), supporting the claim of representation generality at the qualitative level.

## Weaknesses

### Major

- **Quantitative evaluation is limited to a single base method (DreamTime), undermining the generality claim.** Table 1 only reports numbers for DreamTime-based variants. The paper claims Progressive3D is "general for various text-to-3D methods" (lines 8, 46, 295), but TextMesh, Fantasia3D, and MVDream appear only in qualitative figures. Without BLIP-VQA or mGPT-CoT numbers for at least one additional backbone, the generality claim is supported only by qualitative evidence, which is insufficient to rule out representation-specific confounds. The paper transparently states it uses DreamTime as the main baseline (line 244), but the claim scope exceeds the evidence.

- **Evaluation metrics are adopted from the 2D compositional T2I domain without validation for 3D renderings, and the human study is too small to independently validate them.** BLIP-VQA and mGPT-CoT (from T2I-Comp) are applied to rendered views of 3D models. While a reasonable extension, the paper provides no evidence that these metrics correlate with human judgments of 3D semantic consistency in this setting. The human preference study (Sec. 4.2) uses only 20 feedbacks, compares only DreamTime vs. Progressive3D (excluding CEBM, A&E baselines), and reports no inter-rater agreement. This combination of unvalidated proxy metrics and a small preference study weakens confidence in the headline numbers despite their large magnitude.

- **No dedicated limitations section or discussion of the method's practical constraints.** The paper has no Limitations section. Key limitations go unaddressed: (a) the user must manually decompose the prompt into an editing schedule with 3D bounding boxes — no guidance or sensitivity analysis is provided; (b) the depth-comparison heuristic for editable regions (Eq. 2) assumes the bounding box is strictly in front of existing content, and will produce empty masks if the new object is intended to be behind existing content; (c) no analysis of cumulative errors across multiple editing steps.

### Minor

- **No comparison of total computational cost.** Progressive3D decomposes generation into multiple editing steps, each training the representation for thousands of iterations. The paper does not report iteration counts per step, total iterations for the full pipeline, or equivalent iterations for the direct DreamTime baseline. Without this, the improvement could partly reflect additional optimization rather than the decomposition strategy. The large margin (0.227→0.474) makes a purely compute-driven explanation unlikely, but reporting would remove ambiguity.

- **CSP-100 dataset is insufficiently described.** The paper states it contains 100 prompts across four categories (color, shape, material, composition) but provides no statistics on category balance, complexity distribution (single vs. multiple objects), or representative examples. A table of sample prompts and category breakdowns would help assess whether the benchmark is balanced or biased toward Progressive3D's strengths.

- **Key hyperparameter τₒ is not specified.** The opacity filter threshold τₒ (Eq. 1, line 97) controls which pixels are treated as "empty" for mask computation, but its value is never reported, and no ablation studies its sensitivity.

- **Failure cases are not discussed.** The paper shows only successful results. Representative failures (e.g., mask misalignment, region-box sizing errors, shading inconsistencies across steps) would provide a more balanced assessment and help users understand the method's limitations.

### Trivial

- Line 247: "Prgressive3D" (typo, missing 'o').
- Line 248: A&E reference says "ane" but should likely be "attend-and-excite".

## Nice-to-Haves

- A runtime comparison (training time per step, total time vs. direct generation) would help practitioners assess the practical cost.
- Guidelines for effective prompt decomposition (editing order, box sizing) would increase the method's usability, given the user burden of designing the editing schedule.
- Quantitative results for at least one additional backbone (e.g., MVDream) would strengthen the generality claim.
- Reporting variance/confidence intervals on metric scores across the 100 prompts would improve statistical transparency.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No confidence intervals or significance tests"**: Reporting bootstrap confidence intervals or significance tests for large-scale benchmarks is not standard practice in this community; single-run evaluation is the norm. Demoting to removed.
- **"Introduction could show failure examples from other methods"**: A presentation suggestion, not a substantive weakness. Removed.
- **"Method assumes noise-prediction suppression translates to 3D semantic suppression without verification"**: The ablation in Figure 5 (W sweep) directly verifies this empirically. Removed as the paper already addresses it.
- **"Consistency constraint should be ablated despite being foundational"**: The paper explicitly justifies its exclusion (lines 339-340) — without this constraint, there is no local editing at all, making the ablation meaningless. Removed as a strawman.
- **"Region prompt definition details / GUI specification"**: The paper describes the 3D bounding box format ([c_x,c_y,c_z; s_x,s_y,s_z]) clearly in Sec. 3.1. Implementation details (how the user specifies coordinates) are a level of engineering detail not required for a conference paper. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an observation about the work that is not already stated or implied by the authors.

## Suggestions

1. **Expand quantitative generality**: Provide BLIP-VQA and mGPT-CoT numbers for at least one non-DreamTime backbone (e.g., MVDream) on CSP-100 to directly support the claim that the framework is representation-agnostic.
2. **Scale and document the human study**: Increase the number of annotators, include pairwise comparisons against all baselines (CEBM, A&E), and report inter-rater agreement to validate the metric numbers independently.
3. **Add a Limitations section** that candidly discusses the user-burden of prompt decomposition, the front-only assumption of the mask heuristic, and potential cumulative errors in multi-step editing.
4. **Report computational budget**: State the total number of SDS iterations (or wall-clock time) for Progressive3D and the direct DreamTime baseline per prompt, to rule out a compute-based confound.
5. **Improve CSP-110 documentation**: Provide a table of representative prompts across all four categories and a breakdown of prompt complexity distribution.

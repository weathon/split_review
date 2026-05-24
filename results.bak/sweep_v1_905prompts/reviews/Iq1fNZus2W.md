Now I have all the information I need. Let me compile the final review.

## Summary

The paper identifies redundancy in full attention for multi-condition DiTs and proposes PKA (Patch-wise and Keyword-Aware Attention), decomposing attention into PAA (position-aligned, O(N)) for spatial conditions and KSA (keyword-scoped masking) for subject conditions. With a condition KV cache and early-timestep sampling, it achieves up to 10× speedup and 5.12× VRAM reduction. Quality results are competitive—best FID/SSIM on all three tested tasks.

## Strengths

**1. Principled architectural design grounded in empirical attention analysis.** The paper does more than assert redundancy—it *shows* it. Figure 2 demonstrates that spatial-condition attention matrices are overwhelmingly diagonal, and Figure 3 shows subject-condition attention is sparse and localized. These visualizations directly motivate the two-module decomposition (PAA and KSA), giving the method a clear theoretical footing that goes beyond the ad-hoc design choices in some prior work.

**2. Large, architecturally-guaranteed efficiency gains.** Figures 7 and 8 show that as conditions grow from 1 to 16, PKA maintains near-constant latency (~25s) and VRAM (~500 MB), while baselines scale quadratically. The 10× speedup and 5.12× VRAM reduction at 16 conditions are not just empirical artifacts—they follow from the O(N) complexity of PAA and the sparsity of KSA. This is the paper's strongest claim.

**3. Competitive generative quality across multiple tasks.** Table 1 shows PKA achieves the best FID and SSIM on Subject-Canny (52.99, 0.553), Subject-Depth (62.08, 0.515), and Canny-Depth (53.01, 0.613), and best subject consistency (CLIP-I/DINOv2). The efficiency gains do not come at an obvious quality cost on these metrics.

**4. Condition KV cache is a practical contribution.** Caching condition K/V after the first denoising step (Figure 4a) is simple but effective, and not present in prior multi-condition DiT works like OminiControl2 or UniCombine. This design-level choice compounds the savings from PAA/KSA.

**5. Thorough ablation studies.** The paper compares PAA against sliding-window attention at multiple window sizes (Figure 9), ablates the KSA threshold ε (Figure 10), and validates the early-timestep sampling intuition with perturbation analysis (Figure 5). These ablations strengthen confidence in the design decisions.

## Weaknesses

### Major

**1. Baseline comparison fairness is ambiguously specified.** Section 4.1 states: *"To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA."* The sentence structure suggests this fine-tuning applies to the proposed PKA method, but the paper never states whether OminiControl2 and UniCombine undergo the same LoRA fine-tuning on the same data subset. If the baselines are used off-the-shelf (with potentially different training distributions or more data) while PKA is fine-tuned on a curated subset, the quality numbers in Table 1 would reflect data adaptation rather than architectural superiority. The efficiency comparisons (Figures 7–8) are architectural and unaffected, but the quality claims depend on this being clarified. This is the most significant open question in the paper.

**2. F1 gap on Subject-Canny is dismissed without analysis.** On the Subject-Canny task, UniCombine achieves F1 = 0.551 while PKA achieves F1 = 0.414 — a 25% relative drop on a metric measuring spatial controllability that PAA is designed to preserve. The paper calls this a *"minor exception"* and *"narrow margin"* (Section 4.2.3), but provides no hypothesis for why this degradation occurs. Since F1 on Canny-Depth is fine (0.411 vs 0.369), the issue may involve interference between PAA and KSA when a subject condition is combined with a spatial condition. The paper should at minimum offer an analysis and preferably an ablation on the Subject-Canny task to isolate the cause.

### Minor

**3. Keyword extraction for KSA is underspecified.** Section 3.2.2 states that the keyword set 𝕂 *"typically contains just 1 to 2 tokens,"* and Section 4.1 notes that the training subset ensures *"each image caption contains a descriptive keyword."* But the paper never specifies how keywords are obtained at inference time: Are they manually provided? Extracted automatically from the prompt via an algorithm? This gap affects both reproducibility and the practical generality of KSA.

**4. No statistical significance or confidence intervals.** Table 1 reports no standard deviations, confidence intervals, or significance tests. With CLIP-T differences as small as 0.002 (Subject-Canny), it is impossible to determine whether these differences are meaningful. This is common in the field but still important for a submission making quantitative claims.

**5. Early-timestep sampling validated only qualitatively.** The perturbation analysis in Figure 5 is a good motivation, but the evaluation of the strategy (Figure 11) is purely visual. No quantitative metrics (FID, controllability scores) are reported comparing different (μ, δ) settings or against the standard schedule. The claim that it *"accelerates convergence and enhances control fidelity"* is only partially supported.

**6. PAA ablation lacks quality metrics.** Figure 9 compares PAA against sliding-window attention on latency and VRAM, but no quantitative quality metric (FID, SSIM, F1) is reported—only visual inspection. Given the F1 concern on Subject-Canny, adding quality metrics to this ablation would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- **Automatic keyword extraction pipeline:** An algorithm or heuristic for extracting keywords from arbitrary prompts would make KSA more practically useful and would allow evaluation on standard benchmarks without manual annotation.
- **Condition Cache ablation:** The paper caches condition KVs after the first step. An ablation comparing this against recomputing at every step would confirm that caching does not degrade quality.
- **Ablation of early-timestep sampling with quantitative metrics:** Reporting FID or controllability scores at different (μ, δ) settings would substantiate the convergence and fidelity claims.

## Removed Points

- *"Comparison fairness is unverifiable and likely invalid"* (originally framed as Critical Issue 1 by the harsh critic): While the comparison fairness is genuinely underspecified, calling it "likely invalid" is too strong given the efficiency claims are architectural and unaffected. Demoted to Major.
- *Weaknesses about missing appendix content, missing proofs, or reproducibility nitpicks:* Removed per policy — parser strips appendices, and the paper provides adequate implementation detail for a conference submission.
- *Strength Finder's claim that "state-of-the-art quality alongside efficiency" contradicts the typical efficiency-quality trade-off:* While supported by Table 1 numbers, the baseline fairness ambiguity (Major weakness 1) tempers this claim. Still retained as a strength with the caveat noted.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify baseline setup explicitly.** In the rebuttal or revision, state: "OminiControl2 and UniCombine were fine-tuned using the same LoRA procedure on the same data subset as PKA" (if true), or clearly document the limitation if they were used off-the-shelf. This single change would resolve the most serious concern.

2. **Analyze the Subject-Canny F1 gap.** Run an ablation comparing PAA on the spatial condition alone (no subject condition) on Subject-Canny. If the F1 gap persists, it indicates PAA loses edge detail—a genuine trade-off that should be acknowledged. If the gap disappears, it implicates cross-module interference, which is an interesting design insight.

3. **Add confidence intervals to Table 1.** Report at minimum the standard deviation across multiple runs or seeds for the key metrics.

4. **Specify keyword acquisition.** Provide the algorithm or heuristic used to extract keywords from prompts, even if it is a simple rule (e.g., "we select the noun phrase describing the subject from the prompt"). Without this, KSA cannot be independently applied.

5. **Quantify the early-timestep sampling.** Add FID or controllability scores for different (μ, δ) settings to Figure 11's ablation.

## Score and Decision

**Round-1 bracket:** I placed the paper in the 5.0–6.5 range based on comparisons against calibration anchors. The weak bracket (< 3.5) includes papers like "Highlight Diffusion" (3.00) and "Partially Conditioned Patch Parallelism" (3.00) — clearly inferior in contribution depth. The strong bracket (> 7.5) includes papers like "Differential Transformer" (8.00) and "Würstchen" (8.00) — landmark papers with broader impact. The middle bracket includes "Compositional VQ Sampling" (5.25, rejected), "ViCo" (5.50, rejected), "LinFusion" (6.25, rejected), "SaRA" (6.20, accepted), "EfficientDM" (6.50, accepted), and "LEGO bricks" (6.67, accepted).

**Round-2 narrowing:** Comparing against papers in the 5.5–6.5 range:
- **ViCo (5.50, Reject):** ViCo had novelty concerns and weaker efficiency claims. PKA is stronger in both architectural novelty and demonstrated gains. PKA > ViCo.
- **SaRA (6.20, Accept):** Both are efficiency-focused papers with well-motivated methods. SaRA's weaknesses included some theoretical concerns about parameter selection; PKA's weaknesses center on evaluation ambiguity. Comparable quality of work, slight edge to SaRA for cleaner evaluation.
- **EfficientDM (6.50, Accept):** EfficientDM had strong results but some confusion in experimental reporting. PKA's method is more architecturally principled, but PKA's evaluation gaps are more concerning. Comparable.
- **LEGO bricks (6.67, Accept):** Well-received paper with clean experiments. PKA's contribution (attention sparsity for multi-condition control) is more targeted and arguably more novel for its specific problem setting, but the evaluation gaps push it slightly below.

**Final calibration:** The paper has a genuinely interesting core idea (condition-specific attention sparsity), strong efficiency results, and reasonably good quality numbers. The main drag on the score is the ambiguity in baseline comparison and the unanalyzed F1 gap — both of which are addressable but left the evidence for the quality claims weaker than it should be. I place the paper at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
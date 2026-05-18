Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper introduces Video Active Perception (VAP), a training-free method that selects key frames from long-form videos for VLM-based QA by leveraging a pre-trained video generation model (CogVideoX) as a "prior world knowledge" module. VAP generates expected video dynamics from a few initial frames plus the question/answers, then selects real frames whose latent representations diverge most from these expectations, feeding only those to a VLM. Experiments across EgoSchema, NExT-QA, ActivityNet-QA, and CLEVRER show consistent accuracy gains over standard uniform-sampling baselines and recent frame-selection methods, using far fewer frames.

## Strengths

- **State-of-the-art zero-shot accuracy across multiple benchmarks.** Table 1 reports that VAP achieves 68.1% on EgoSchema, 81.4% on NExT-QA, 64.6% on ActivityNet-QA, and 40.5% on CLEVRER, outperforming reproduced GPT-4o, Gemini 1.5 Pro, LLaVA-OV-72B, and prior frame-selection methods (VideoTree, IG-VLM, etc.) on every dataset. The results are consistently positive across four diverse benchmarks.

- **Novel and well-motivated core idea.** Using a generative model's latent representations as a prior for identifying surprising/informative frames is a clever instantiation of active perception principles. The method requires no fine-tuning of either the generation model or the VLM, making it immediately applicable to any VLM that accepts image inputs.

- **Substantial reduction in frames fed to the VLM.** VAP uses 32 frames (5 for CLEVRER) while matching or exceeding the accuracy of standard 1 fps sampling that requires 180 frames on EgoSchema (5.6× fewer), 44 frames on NExT-QA (1.5×), and 90 frames on ActivityNet-QA (2.8×). This frame reduction is clearly documented as a "frames per question" metric.

- **Simpler and more unified than prior selection methods.** Unlike VideoAgent (iterative, captioning-dependent) or VideoTree (hierarchical clustering+ captioning), VAP operates in a single selection round and requires no captioning model or complex data structure — only the generation model's encoder and similarity computation.

- **Systematic ablations on key design choices.** Tables 2 and 3 explore varying the number of selected frames and initial frames, showing that performance plateaus at 32 frames and that the method is not overly sensitive to this hyperparameter.

## Weaknesses

### Major

- **The efficiency claim is stated as "frames per question" but the total computational cost of the selection pipeline is unaccounted for, making the headline "5.6× efficiency" potentially misleading.** The paper transparently frames its efficiency metric as "frames per question" (abstract, line 4; Section 3.4, line 196). However, the selection pipeline itself has significant cost: encoding all real frames (e.g., 5,400 for EgoSchema) through the CogVideoX 3D VAE, running 50-step diffusion sampling to generate latents, and performing frame interpolation across the full video length. None of these costs are factored into the efficiency ratio. A reader could easily interpret "5.6× efficiency" as total inference savings. Without reporting wall-clock time, approximate FLOPs, or at minimum the overhead ratio, the practical deployment advantage is unclear. This does not invalidate the accuracy results, but it overstates the efficiency contribution.

- **Missing control: VAP-selected frames vs. uniformly-sampled frames at the same budget.** The paper demonstrates that VAP with 32 frames outperforms uniform sampling with many frames (e.g., 180 on EgoSchema), but this conflates two effects: (1) using fewer frames, and (2) selecting them intelligently. To isolate the value of the selection mechanism, one must compare VAP-32 against uniform-32 using the same VLM. This is a standard control for frame-selection papers and its absence is a significant evaluation gap. Figure 3 compares against other selection methods but not against the simplest baseline. Without this control, it is possible that any reasonable 32-frame selection (including uniform) would perform similarly, reducing the contribution's novelty.

### Minor

- **No analysis of selection stability or noise.** The generation process involves 50-step diffusion sampling with inherent randomness, and the 3D VAE encoding and cosine similarity computation may also vary. The paper reports only single-run results. Repeating the selection process with different random seeds (3-5 runs) and reporting accuracy variance would confirm that the method is reliable rather than lucky. This is standard practice for methods with stochastic components.

- **The "active perception" framing is query-conditioned, which differs from the classic definition.** The method conditions the generation model on the question and answer choices (Algorithm 1, lines 52-60), so the "surprising" frames are surprising relative to a prior that already knows what to look for. This is a valid and effective approach for query-driven keyframe selection, but it differs from the classic active perception formulation (Bajcsy et al., 2018) where an agent acquires data to reduce task-agnostic uncertainty about the environment. The paper partially addresses this by citing Bajcsy's definition that includes "knows why it wishes to sense," but the theoretical motivation would benefit from more precise framing as "query-conditioned surprise-based selection."

- **Calling CogVideoX "lightweight" warrants more nuance.** CogVideoX-2B has ~2B parameters and CogVideoX-5B ~5B parameters. Describing a 5B diffusion transformer as "lightweight" is relative — it is indeed smaller than a 70B+ VLM, but for many deployment scenarios it is not trivial. A more explicit discussion of the trade-off (e.g., the generation model's cost vs. the VLM savings) would improve credibility.

- **CLEVRER descriptive question performance is not transparently reported.** The paper states that VAP "achieves better accuracies on descriptive (Des.), explanatory (Exp.), counterfactual (Cou.)" on CLEVRER (Section 3.4, line 137), but does not provide per-category numbers in the text. Given that VideoTree caption-based methods might have an advantage on descriptive questions (which are less reliant on visual dynamics), reporting the exact descriptive accuracy and discussing any trade-off would strengthen the analysis.

### Trivial

- **"GPT 1.5 Pro" and "GPT 1.5 Flash" in Section 2.3 (line 81) should read "Gemini 1.5 Pro" and "Gemini 1.5 Flash"** to be consistent with the rest of the paper.

## Nice-to-Haves

- An ablation of the similarity metric (cosine vs. L2 vs. learned distance) would strengthen the method's justification.
- Reporting wall-clock time or approximate FLOPs for the full pipeline (selection + VLM) for at least one dataset would address the efficiency accounting gap.
- A brief discussion of failure cases where the generative prior produces poor predictions, and how this affects selection quality.

## Removed Points

- **Criticism about "GPT 1.5 Pro" as a substantive issue**: This is a typographical error (parser artifact / copy-editing miss), not a scientific weakness. Removed per formatting nitpick rule.
- **Criticism about baselines being "from mid-2024" undermining SOTA claim**: The paper explicitly compares against the strongest relevant methods available at the time of writing. The SOTA claim is qualified as zero-shot and within the compared set; this is standard practice. Removing as it evaluates the paper against the wrong class of expectations — a method paper is not expected to exhaustively compare against future work.
- **Criticism about VAP falling behind VideoTree on CLEVRER descriptive questions (66.5 vs 72.0)**: The paper's own text (Section 3.4, line 137) states "VAP achieves better accuracies on descriptive (Des.)" on CLEVRER. Without access to the table image to verify the reviewer's specific numbers, and given the paper explicitly claims better performance on all reported CLEVRER types, this criticism cannot be confirmed from the available text.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's strongest selling point (efficiency) is the least well-supported part of the evaluation, while its method (generative-prior-based selection) and accuracy results are clearly solid. The reviewer's suggestion to reframe as "query-conditioned surprise-based selection" rather than canonical active perception is an accurate characterization that the authors should adopt.

## Suggestions

1. **Add the missing uniform-32 baseline** — For each dataset, report the accuracy of the VLM (GPT-4o or Gemini 1.5 Pro or LLaVA-OV) using 32 uniformly sampled frames, and compare directly against VAP-32. This is the single most important control and would cleanly isolate the selection mechanism's value.

2. **Account for the selection pipeline's computational cost** — Report wall-clock time or approximate FLOPs for the full VAP pipeline (3D VAE encoding + 50-step diffusion + interpolation + similarity computation + VLM inference) side-by-side with the baseline (e.g., VLM inference on 180 uniformly sampled frames). This would either validate or appropriately bound the efficiency claim.

3. **Run a stability analysis** — Repeat the selection process 3-5 times with different random seeds on a subset (e.g., EgoSchema or CLEVRER) and report the mean and standard deviation of VLM accuracy. This would confirm the method is robust to diffusion sampling noise.

4. **Reframe the theoretical motivation** — Replace or supplement the "active perception" framing with "query-conditioned surprise-based keyframe selection," which more accurately describes what the method does. The current framing invites scrutiny that the paper does not fully satisfy.

5. **Disambiguate "efficiency"** — Explicitly state in the abstract and Section 1 that the 5.6× figure refers to frames-per-question reduction for the VLM only, and note that the selection pipeline adds overhead. This would prevent misinterpretation.

## Score and Decision

The paper presents a genuinely novel approach to efficient long-form video QA, with consistent accuracy gains across four benchmarks. The core idea — using a generative model's latent space to identify surprising frames — is clever, training-free, and VLM-agnostic. However, the evaluation has two significant gaps: (1) the efficiency claim lacks total-cost accounting, and (2) there is no uniform-sampling-at-same-budget control to isolate the selection mechanism's value. These are fixable but necessary for the paper's central contributions to be properly assessed. Given that the accuracy results are clearly positive and the conceptual contribution is solid, the paper is a candidate for acceptance contingent on addressing these gaps. A borderline reject would also be defensible if the efficiency claim is judged central; I lean toward acceptance because both gaps can be resolved at the camera-ready stage without changing the method, and the accuracy improvements are independently useful even without the efficiency framing.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
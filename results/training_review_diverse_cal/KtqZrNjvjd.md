Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

The paper introduces Video Active Perception (VAP), a training-free method that uses a lightweight text-conditioned video generation model (CogVideoX) as a prior to select the most "surprising" frames — those diverging most from generated expectations — for efficient long-form video QA with VLMs. The core idea is conceptually appealing: active perception theory is mapped to frame selection, where a generative model encodes prior world knowledge and frames that deviate most from generated latents are deemed most informative. Empirically, VAP achieves state-of-the-art zero-shot results across EgoSchema (68.1%), NExT-QA (81.4%), ActivityNet-QA (64.6%), and CLEVRER (40.5%) while using substantially fewer frames per question than standard uniform sampling with flagship VLMs.

## Strengths

- **Consistent accuracy gains across diverse benchmarks with strong efficiency improvements.** Table 1 shows VAP outperforming standard VLM baselines (GPT-4o, Gemini 1.5 Pro, LLaVA-OV-72B) on EgoSchema, NExT-QA, CLEVRER, and achieving competitive results on ActivityNet-QA, while using up to 5.6× fewer frames per question (180→32 on EgoSchema). The gains hold across three different VLM families and four dataset types (egocentric, web, causal/reasoning, synthetic), demonstrating robustness.

- **Training-free and VLM-agnostic framework with clear practical appeal.** VAP requires no fine-tuning of any VLM or generation model, operates at inference time, and works with proprietary (GPT-4o, Gemini 1.5) and open-source (LLaVA-OV-72B) VLMs. This generality is a genuine practical advantage over methods that require task-specific training or captioning pipelines.

- **Strong performance on temporal/causal reasoning tasks where frame selection matters most.** On CLEVRER explanatory and counterfactual questions, VAP achieves 154% and 71% relative gains over the caption-based VideoTree baseline (Table 1, Section 3.5). This directly supports the claim that selecting informative visual frames beats summarizing video through captions for reasoning about object interactions and causes.

- **Ablation studies validate the key design choices.** Tables 2–3 systematically vary the number of selected frames (6→48) and initial frames (6→90), showing that performance improves up to 32 frames and plateaus thereafter, providing empirical justification for the chosen hyperparameters and showing that additional frames beyond 32 are redundant.

## Weaknesses

### Fatal
None.

### Major

- **No uniform/random sampling baseline at the same frame count.** The paper's central claim — that VAP's *selection mechanism* identifies more informative frames — requires comparing VAP to uniform subsampling at the same K frames. Table 1 compares VAP (using 32 frames) against standard VLMs at 1 fps (e.g., 180 frames), conflating two distinct effects: using fewer frames vs. selecting which frames to use. Figure 3 compares VAP to other selection methods, but the simplest control — "GPT-4o with 32 uniformly sampled frames" — is absent. Without this, one cannot rule out the possibility that *any* reasonable 32-frame set would suffice on these benchmarks. This gap weakens the central claim that the surprise-based selection (rather than merely frame reduction) is responsible for the strong results.

- **No analysis of the computational overhead of the selection pipeline.** The paper defines "efficiency" solely as frames-per-question fed to the VLM, ignoring the cost of (a) 3D VAE encoding all real frames, (b) running 50-step diffusion to generate latents, (c) RIFE interpolation, and (d) cosine similarity ranking. If these steps together cost as much as or more than processing the full video with the VLM, the claimed 5.6× improvement is illusory in practical terms. The paper calls the generation model "lightweight" and RIFE "fast" but provides no wall-clock time or FLOP comparison. A practical efficiency claim requires measuring the total pipeline cost.

### Minor

- **Answer conditioning in the generation model is not discussed or controlled.** The generation model is conditioned on the question *and all answer options* (Algorithm 1, line 54). While the model does not know which answer is correct (so this is not "leakage" in the standard sense), the answer options provide contextual cues about what events/objects may be relevant. This could bias frame selection: frames showing answer-relevant events might appear more or less "surprising" depending on how the generation model processes the answer text. The paper does not discuss this or run a control experiment conditioning on the *question only*. Given that the VLM also sees answer options during inference, this is unlikely to be a fatal confound, but it should be acknowledged and ideally controlled.

- **No statistical significance or variance reporting.** Several results in Table 1 show small margins (e.g., 68.1 vs. 67.0 on EgoSchema, 40.5 vs. 39.0 on CLEVRER). Without confidence intervals, variance estimates, or significance tests, it is unclear whether these differences are meaningful or within noise.

- **No ablation of the cosine similarity selection criterion.** The choice of cosine dissimilarity between real and generated latents as the "surprise" signal is plausible but ad-hoc. An ablation comparing against L2 distance, learned similarity, or even simple frame-difference baselines would strengthen the claim that this specific formulation matters.

### Trivial

- **Qualitative analysis (Figure 4) shows VAP's frame selections are reasonable but does not compare against what uniform sampling or another baseline would have selected.** This limits the qualitative evidence for the selection mechanism's superiority.

## Nice-to-Haves

- A runtime analysis comparing total VAP pipeline time against standard VLM inference at 1 fps would substantiate the practical efficiency claim.
- A controlled experiment conditioning the generation model on question-only vs. question+answers would clarify whether answer conditioning is necessary and whether it introduces unwanted bias.
- Replacing CogVideoX with a simpler non-diffusion frame predictor (or different generation model) would test whether the effect is specific to this architecture.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Critic's Issue 1 framing as "leaking answer information" that could "invalidate the evaluation":** The generation model conditions on ALL answer options, not the correct one specifically. The VLM also sees all answer options during inference. The critic's framing of this as potential "invalidity" of the evaluation is overblown; the concern is better framed as a missing control experiment. Downgraded from fatal/major to minor.

- **"Reasoning-task claims are confounded because VideoTree uses captions":** The paper explicitly acknowledges this in Section 3.5 ("These can be particularly hard for previous frame selection models, as they rely on captioning models to extract visual information"). Showing that visual frames beat captions for reasoning is a legitimate contribution, not a confound. Removed.

- **"Lack of ablation on components" (as a major weakness):** The paper does ablate number of selected frames (Table 2) and initial frames (Table 3). While additional ablations (e.g., similarity metric, generation model choice) would strengthen the paper, claiming a complete absence is inaccurate. Downgraded to minor.

- **"Qualitative analysis is not comparative":** This is standard for qualitative analyses. Not a meaningful weakness. Removed.

- **Strength Finder's claimed strengths that conflict with verified weaknesses:** None of the strengths directly conflict with verified weaknesses; they occupy different levels of analysis (accuracy results vs. missing baselines). All kept as they are supported by the paper.

## Novel Insights

The most interesting finding to emerge from the cross-review is that the paper's main methodological strength — using a generative model as an active perception prior — is also the source of its most important unresolved questions. The reviewer correctly identifies that the surprise-based selection framing creates a tension: the generation model conditions on answer options to set expectations, but this conditioning could create a circular dependency where the frame selection is implicitly guided by the very answers the VLM is supposed to infer. This tension is not unique to this paper — it echoes a known challenge in "information bottleneck" retrieval methods where the query used for selection is the same as the downstream task's input. Resolving it (e.g., by showing that question-only conditioning works nearly as well, or that answer conditioning is providing non-trivial but appropriate context) would clarify whether VAP is genuinely selecting informative frames or benefiting from a more subtle form of task guidance. This is a worthwhile direction for follow-up work.

## Suggestions

1. **Add the critical missing baseline:** Run the same VLMs (GPT-4o, Gemini 1.5, LLaVA-OV) with K uniformly sampled frames (32 for EgoSchema/NExT-QA/ActivityNet-QA, 5 for CLEVRER) and add these results to Table 1. This directly tests whether VAP's selection mechanism adds value beyond simply using fewer frames.

2. **Measure and report total pipeline runtime** (VAE encoding + 50-step diffusion + RIFE interpolation + cosine similarity + VLM inference) vs. standard VLM inference at 1 fps on representative videos. Report both time and accuracy to substantiate the efficiency claim.

3. **Run a control experiment** where the generation model is conditioned on the *question only* (without answer options). Report how frame selection and final accuracy change. If accuracy drops, discuss why answer conditioning is appropriate (the VLM also sees answers at inference time; the generation model doesn't know which is correct). If accuracy stays similar, the method is cleaner.

4. **Add confidence intervals or bootstrap estimates** for the main results, especially where margins between methods are small (EgoSchema: 68.1 vs. 67.0; CLEVRER: 40.5 vs. 39.0).

## Score and Decision

This paper has a genuine contribution: a novel, principled approach to frame selection grounded in active perception theory, strong empirical results across multiple benchmarks, and a training-free, VLM-agnostic design. The weaknesses are real but addressable — they concern missing baselines and analyses rather than flawed methodology. The missing uniform-sampling baseline at the same frame count is the most significant gap, as it prevents isolating the value of the selection mechanism from the value of simply using fewer frames. The missing runtime analysis similarly limits the practical efficiency claim. Neither undermines the core empirical finding (VAP achieves SOTA results with fewer frames), but both reduce the precision of what can be concluded about *why* the method works.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>
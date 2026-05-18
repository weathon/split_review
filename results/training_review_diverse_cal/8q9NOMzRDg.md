Now I have a thorough understanding of the paper and all reviewer inputs. Let me construct the final consolidated review.

## Summary

This paper introduces Reconstructive Visual Instruction Tuning (Ross), which adds a vision-centric supervision signal to LMM training by reconstructing input images through a denoising objective on latent visual tokens. Unlike standard visual instruction tuning that only supervises text outputs, Ross imposes a per-token denoising loss on the visual representations (projected visual tokens), encouraging the model to preserve fine-grained visual detail. The method is evaluated across multiple backbones (Vicuna-7B/13B, Qwen2-7B), visual encoders (CLIP, SigLIP), and benchmarks, showing consistent improvements — especially on fine-grained comprehension (MMVP: +12.6 for Qwen2-7B) and hallucination benchmarks (HallusionBench: +4.1). The paper also demonstrates transfer learning to depth map understanding, where Ross improves with extra depth inputs while extrinsic assistance methods like MiDaS do not.

## Strengths

1. **Novel and well-motivated vision-centric supervision approach.** The paper identifies a genuine limitation in current LMM training — that only text tokens receive supervision — and proposes a principled solution by adding a reconstruction objective on visual representations. The "intrinsic activation" framing (improving visual representations through self-supervision rather than aggregating multiple visual experts) is a clean design choice that maintains a lightweight inference procedure.

2. **Denoising objective is convincingly shown to outperform regression for handling visual spatial redundancy.** The paper systematically demonstrates (Figure 4) that directly regressing raw RGB or latent values is suboptimal, while the denoising objective yields significant gains (e.g., MMVP: 42.2 vs 36.0 for Ross^D vs Ross^R-Latent with Qwen2-7B). This ablation directly supports the paper's central technical claim about addressing spatial redundancy, and is one of the cleanest experiments in the paper.

3. **Competitive performance against multi-expert methods with a single visual encoder.** Ross-7B uses only a single SigLIP encoder yet surpasses Cambrian-1-8B (which aggregates CLIP, SigLIP, DINOv2, and ConvNext) on HallusionBench (57.3 vs 48.7), MMVP (54.7 vs 51.3), MMBench-EN (79.0 vs 75.9), and MMBench-CN (76.1 vs 68.9). This demonstrates a meaningful win for the self-supervision over expert-aggregation paradigm.

4. **Consistent improvements across diverse configurations.** The reconstructive objective provides statistically significant gains for both Vicuna-7B and Qwen2-7B, with both CLIP and SigLIP encoders, across all six reported benchmarks (Table 5). The consistency strengthens confidence that the improvement is from the method itself rather than a lucky configuration.

5. **Quantitative evidence of increased attention to visual tokens.** The attention analysis (Table 2) provides mechanistic evidence for why the method works: the reconstructive objective significantly increases the model's attention to visual tokens (mean 2.36 vs 2.03 ×10⁻⁴, p < 10⁻⁷), aligning attention with question-relevant visual regions.

## Weaknesses

### Major

1. **Ambiguity in gradient flow and "supervising visual outputs" framing.** The paper claims to "supervise visual outputs" and writes the visual loss parameter set as $\Theta = \{\theta, \xi, \phi, \pi\}$ (Eq. 3–4), implying the LLM parameters $\theta$ receive gradients from the reconstructive loss. However, the visual tokens $\bm{x}_{i\leq N}$ are produced by $\mathcal{H}_\phi \circ \mathcal{G}_\xi(\bm{I})$ and do not mathematically depend on $\theta$ in the causal LLM formulation given in Eq. 1. The paper never clarifies whether $\bm{x}_{i\leq N}$ refers to the raw projected visual tokens or the LLM's hidden representations after processing those tokens — the latter would depend on $\theta$ but the paper does not specify this. This ambiguity undermines the claimed novelty of "supervising visual outputs" as distinct from simply adding an auxiliary loss on the visual front-end. The method clearly works empirically, but the paper would benefit from: (a) a precise computational graph showing which parameters receive gradients from $\mathcal{L}_{\mathrm{LMM}}^{\mathrm{visual}}$, and (b) reframing the contribution as "enhancing visual representations via self-supervised reconstruction" rather than "supervising visual outputs of the LMM."

2. **The "Generative vs. Reconstructive" ablation is confounded.** Table 3 compares the reconstructive method (using visual token conditions and caption data) against a generative variant (using learnable query tokens and text-to-image creation data). These differ in three dimensions simultaneously: (i) condition type (visual tokens vs. learnable queries), (ii) training data (caption vs. creation), and (iii) whether the visual loss is applied during the full training or only part of it. The paper's conclusion that "reconstructive objectives boost comprehension while generative alternatives cannot" is too strong for this comparison. A cleaner ablation would vary only the loss objective while keeping the condition and data constant (e.g., comparing reconstruction vs. generation on the same visual tokens with the same data). The paper already has a better-controlled comparison in Figure 4 (regression vs. denoising), which directly supports the denoising claim. The generative experiment adds confusion rather than clarity.

### Minor

1. **Missing training hyperparameters for the denoiser.** While the paper describes the denoiser architecture at a high level ("a stack of Transformer Encoder blocks" with self-attention and three projection layers), it does not report the number of blocks, hidden dimensions, number of attention heads, noise schedule, number of timesteps, or the loss weight $\alpha$ for the visual term relative to the text loss. Some of these details may be in the appendix (which the parser strips), but the lack of clarity about the loss weighting is important for understanding whether the method's gains come from the denoising objective itself or simply from adding an auxiliary loss of any form.

2. **The depth map claim about "extrinsic assistance approaches cannot take advantage" is slightly overbroad.** The paper tests one specific extrinsic method (appending MiDaS features) and finds it does not help. The claim should be qualified to the specific configuration tested rather than stated as a general inability of all extrinsic assistance approaches.

3. **Training data differences between ablation and main results are not fully reconciled.** The ablation study uses LLaVA-558K + Cambrian-737K, while the main comparison uses 2M caption data + 1.2M instruction data. The paper could note whether the method's relative improvements hold at the smaller data scale (Table 5 partially addresses this, but uses a different data mixture than the main table).

### Trivial

1. In Table 6, some baselines use $\ddag$ inconsistently: Cambrian-1-8B has $\ddag$ on POPE, HallusionBench, and MMBench-CN but not on MMBench-EN or SEED-Bench, despite all being from the same original paper. A footnote clarifying that numbers without $\ddag$ are taken directly from the original papers would help.

## Nice-to-Haves

- An analysis of what the denoiser learns qualitatively (e.g., visualizations of reconstructed latent tokens) would strengthen the claim about preserving fine-grained detail.
- An ablation separating pre-training only vs. SFT only application of the visual loss would clarify when the reconstruction signal is most beneficial.
- A brief note on whether the method is compatible with high-resolution image-slicing techniques (since the paper states it does not use them).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper does not specify whether the LLM backbone is frozen or fine-tuned with the visual loss.** The paper's standard training recipe (two-stage following LLaVA-v1.5) implies the full model is fine-tuned, and the equations include $\theta$ in the parameter set. While the gradient flow ambiguity is real (see Major weakness #1), the freezing/fine-tuning status of the LLM backbone is a different question and is adequately covered by the standard recipe reference.

- **Criticism about missing denoiser architecture details (number of blocks, hidden dimensions, heads) framed as a fatal flaw.** The paper provides the key architectural components and references the appendix. Given parser-stripped appendix content, this criticism is disproportionate.

- **Criticism that Table 6 mixes backbones without transparency.** The paper explicitly lists the base LLM for each row and provides a controlled ablation in Table 5. The main comparison is transparent about architecture differences.

- **Criticism that evaluation prompts differ across baselines.** The paper states all evaluations use VLMEvalKit, and marks re-evaluated numbers with $\ddag$.

- **Criticism about LLaVA-v1.5-7B POPE score matching.** The reviewer asks whether this number is from the original paper. The footnote explains that $\ddag$ denotes numbers obtained by re-evaluation, and LLaVA-v1.5-7B is marked with $\ddag$. This is clearly communicated.

- **Several formatting/style nitpicks and demands for impractical ablations** (e.g., multi-seed runs, human studies, comparisons against API-only models requiring weight access).

## Novel Insights

Beyond the paper's own contributions, the most interesting observation that emerges from the review is the *asymmetry* between the reconstructive and generative ablations: adding a reconstruction objective on visual tokens improves comprehension even when the generative variant (with learnable queries and creation data) degrades or fails to improve. This suggests that the *type* of visual supervision matters — aligning representations back to the input image (reconstruction) provides a more useful learning signal than aligning them toward a generated image (generation). This observation deserves deeper investigation than the paper currently provides; if it holds across more controlled comparisons, it would be a meaningful finding for the community.

## Suggestions

1. **Clarify the gradient flow.** Add a precise diagram or text explaining which parameters receive gradients from $\mathcal{L}_{\mathrm{LMM}}^{\mathrm{visual}}$ and under what conditions $\theta$ is updated. If $\bm{x}_{i\leq N}$ are the raw projected visual tokens (making $\partial\mathcal{L}/\partial\theta = 0$), acknowledge this and reframe the contribution as self-supervised enhancement of visual representations rather than "supervising visual outputs" of the LMM. If they are LLM-processed hidden states, state this explicitly.

2. **Report the loss weight $\alpha$ for $\mathcal{L}_{\mathrm{LMM}}^{\mathrm{visual}}$ relative to $\mathcal{L}_{\mathrm{LMM}}^{\mathrm{text}}$** and ablate its sensitivity. This is the single most important missing hyperparameter for understanding the method.

3. **Either remove or redesign the generative vs. reconstructive comparison (Table 3).** A controlled comparison keeping the condition type and data the same would be more informative. The regression vs. denoising comparison (Figure 4) already serves the paper's core argument better.

4. **Qualify the depth map claim** to refer to the specific extrinsic method tested (MiDaS feature concatenation) rather than all possible extrinsic approaches.

5. **Standardize the $\ddag$ notation in Table 6** so readers can clearly distinguish originally reported numbers from re-evaluated ones.

## Score and Decision

The paper proposes a novel and empirically effective approach to improving LMM visual representations through self-supervised reconstruction. The ablations are well-designed, the results are consistent and substantial, and the core idea is principled. The main weaknesses — the ambiguous gradient flow and the confounded generative comparison — are clarity issues that do not invalidate the empirical findings. The paper makes a genuine contribution to the community's understanding of how to train better multimodal models. I recommend acceptance with the expectation that the authors address the clarity issues in the camera-ready version.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
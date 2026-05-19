- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6
Now I have a thorough understanding of the paper and its content. Let me construct the final consolidated review.

## Summary

The paper presents **Generative World Explorer (Genex)**, a panoramic video generation framework that enables embodied agents to "imaginatively explore" large-scale 3D environments and update their beliefs without physical movement. The key technical contribution is **spherical-consistent learning (SCL)** — a regularization loss that enforces rotational coherence in equirectangular panoramic video generation. The paper formalizes imagination-driven belief revision as an extension of POMDP, and evaluates Genex on generation quality, long-horizon exploration consistency (via a novel IECC metric), 3D novel view synthesis, and embodied QA (single- and multi-agent). Results show Genex substantially outperforms baselines on generation metrics, demonstrates zero-shot generalization from synthetic to real-world scenes, and improves both LLM and human decision accuracy on an embodied QA benchmark.

## Strengths

1. **Spherical-consistent learning is a novel and effective technical contribution.** The SCL loss directly addresses the edge-discontinuity problem in equirectangular panoramic video by enforcing rotational invariance through random spherical rotations during training. Table 1 shows clear improvements: Genex (with SCL) achieves FVD 69.5 vs. 81.9 without SCL, SSIM 0.94 vs. 0.91, and LPIPS 0.03 vs. 0.05 — all on top of strong tuned baselines.

2. **Strong quantitative results across multiple evaluation dimensions.** Genex outperforms tuned six-view baselines on generation quality (Table 1), achieves IECC below 0.1 even on 20m/9-rotation paths (Figure 4), and dramatically surpasses SoTA 3D novel-view models such as Stable Zero123, SV3D, and TripoSR on object/background synthesis (Table 3: LPIPS 0.15 vs. next-best 0.50, PSNR 28.57 vs. 14.12).

3. **Demonstrated zero-shot generalization from synthetic to real-world scenes.** The model trained entirely on synthetic Genex-DB (four virtual scenes) achieves IECC ≤0.105 on Google Street View and ≤0.092 on Behavior Vision Suite indoor scenes, outperforming both the six-view baseline (0.269/0.233) and Genex without SCL (0.131/0.120), as shown in Table 2.

4. **Embodied QA results show substantial gains for both LLM agents and humans.** On 200+ scenarios, Genex (GPT-4o) achieves 85.22% single-agent and 94.87% multi-agent decision accuracy, far exceeding multimodal GPT-4o (46.10%/21.88%). Humans using Genex also outperform humans using only images (94.00% vs. 91.50% single-agent, 77.41% vs. 55.24% multi-agent), supporting the claim that imagined observations enable more informed decisions.

5. **The IECC metric is a principled evaluation tool for long-horizon exploration coherence.** Inspired by SLAM loop closure, it measures latent MSE over closed random paths. The strong correlation between IECC and FVD (Figure 5) validates the metric's utility and links generation quality to exploration consistency.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between POMDP formalism and experimental instantiation.** The paper introduces a formal "imagination-driven belief revision" framework (Eq. 3) that extends POMDP with explicit belief distributions and update operators. However, in the experiments, the LLM (GPT-4o/Gemini) serves as an implicit belief updater — it simply receives generated videos as additional observation inputs and produces decisions. No explicit belief distribution is maintained, no separate belief update operator is implemented or ablated, and the LLM is not integrated with a POMDP solver. The paper states this explicitly (Sec. 4.1: "we apply Genex for imaginative exploration and a LMM for the policy model π and belief updater b(s)"), but this does not bridge the gap. The claimed contribution is stronger than what is actually evaluated. This does not invalidate the paper (the core idea of using imagined observations to inform decisions is still demonstrated), but it means the conceptual novelty is asserted rather than empirically realized.

2. **No statistical rigor in any experiment.** All metrics across all tables (generation quality, IECC, embodied QA) are reported as point estimates without error bars, confidence intervals, standard deviations, or significance tests. For the embodied QA benchmark with only ~200 scenarios, binomial confidence intervals around accuracy scores like 85.22% and 94.87% would be wide enough to affect the reliability of comparisons. For generative metrics like FVD, SSIM, and LPIPS, variance across runs or random seeds is not reported. This undermines the reader's ability to assess the robustness of the reported improvements.

### Minor

3. **Human evaluation lacks critical details and contains unexplained results.** The paper reports human accuracy numbers (Table 5) but provides no details about the human study: number of participants, their training/familiarization with the task, whether they saw Genex-generated videos or static frames, or how inter-rater agreement was measured. Moreover, there is a striking unexplained pattern: Human with Genex achieves only 77.41% multi-agent accuracy, while Genex (GPT-4o) achieves 94.87%. If Genex "enhances cognitive abilities," this large gap is puzzling and is not discussed. The paper's claim that Genex has "potential to enhance cognitive abilities for humans" is supported by the human+Genex vs. human+image comparison (77.41% vs. 55.24%), but the discrepancy with the LLM agent warrants explanation.

4. **Missing ablation on what drives the embodied QA improvement.** The paper attributes decision-making gains to Genex's generation quality, but no control experiment tests whether *any* additional visual information would produce similar gains. Critical ablations are absent: (a) random videos of equal length, (b) videos from a simpler generation method (e.g., inpainting), or (c) ground-truth observations from the imagined location. Without these, it is unclear whether the improvement stems from Genex's specific world-modeling capabilities or simply from having more visual context.

5. **The spherical-consistent learning loss (Eq. 4) underspecifies the weighting term λ.** The paper states λ is "a weighting constant" but does not report its value or describe how it was selected. This is a small reproducibility gap in an otherwise clearly described method.

### Trivial

6. **Minor notation inconsistency in Eq. 4 description.** The text (line 134) refers to "the denoised diffused video $x_t - \epsilon_\theta(x_t, c)$" while the equation operates on the latent $z_t$ through the decoder D: $\mathcal{D}(z_t - \epsilon_\theta(z_t, c))$. The intent is clear but the notation could be aligned for clarity.

## Nice-to-Haves
- An explicit belief encoder module (e.g., a small VAE that encodes imagined observations into a belief vector) that could be ablated against the LLM-only setup, to truly operationalize the POMDP framework as a separate, inspectable component.
- A study of how the number of imagined exploration steps (distance/rotations) affects decision accuracy — does more imagination always help, or is there a saturation point?
- Error bars on all metrics (this is a "should have" rather than "nice-to-have" but I'll flag it here since it was raised independently).

## Removed Points
These points were surfaced by reviewers but excluded from the main review after verification:
- **"Unfair baselines in generation quality evaluation"** (Harsh Critic): The paper clearly separates "direct test" (untuned) from "tuned on Genex-DB" rows in Table 1 with explicit labels. Reporting zero-shot performance of off-the-shelf models alongside tuned comparisons is standard practice and does not mislead. This criticism reflects a misreading of the table.
- **"SCL loss is poorly motivated and mis-written / double-decodes"** (Harsh Critic): The motivation (edge discontinuity in equirectangular projection) is clearly stated. The equation decodes to pixel space → applies rotation (requires pixel space) → encodes to latent for the MSE loss. This is a valid design choice, not an error. The critic's "double-decode" claim is factually incorrect.
- **"Several prior works already integrate generative video" / "does not engage with visual planning works"** (Harsh Critic): The related work section (lines 56-63) explicitly discusses video-based planning works (Du et al., Yang et al., Wang et al., etc.) and distinguishes the paper's contribution (belief modeling vs. state-transition prediction). The "one of the first" claim is appropriately hedged.
- **"Missing appendix content / code release"** (Harsh Critic): Appendix sections are removed by the PDF parser. Missing code/model release is not a valid weakness per review guidelines (cited artifacts are assumed to exist).
- **"Unimodal vs. Multimodal setup confusing"** (Harsh Critic): The paper clearly defines both terms (line 375). The observation that Unimodal sometimes outperforms Multimodal is a legitimate finding the paper discusses.
- **Generic scope-creep criticisms** (Harsh Critic requesting larger datasets, more models, etc.): These do not identify specific errors.

## Novel Insights
The two reviewer inputs largely converge on the paper's main tension: the POMDP formalism presents a theoretically clean framework for belief revision via generated observations, but the experiments reduce to "LLMs perform better with extra generated video frames." Neither reviewer fully unpacks the fact that this is a *spectrum*, not a binary — the paper's framework is a meaningful conceptual contribution even if the implementation uses an LLM as a black-box belief updater. The more interesting insight is that the spherical-consistent panoramic video generation is validated both directly (generation metrics) and indirectly (decision accuracy), and the strong correlation between IECC and FVD suggests that generative coherence is a bottleneck for downstream utility — a finding that could guide future work regardless of how belief revision is implemented.

## Suggestions
1. Add error bars, confidence intervals, or standard deviations to all tabular results. For the 200-scenario embodied QA, report binomial confidence intervals.
2. Add at least one control ablation for the embodied QA: compare Genex-generated videos against (a) random frames of equal length and (b) ground-truth observations from the imagined location. This would isolate whether generation quality specifically drives the improvement.
3. Clarify the human evaluation design (number of participants, training, task format) and discuss the human vs. LLM accuracy gap in multi-agent reasoning (77.41% vs. 94.87%).
4. Specify the λ value used in Eq. 4 and describe how it was chosen.
5. Consider adding an explicit belief representation module (even a simple one) to bridge the gap between the POMDP formalism and the LLM-based implementation.

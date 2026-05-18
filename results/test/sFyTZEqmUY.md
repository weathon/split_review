Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes UniSim, a single video diffusion model trained on heterogeneous data (simulated executions, real robot logs, human activity videos, panorama scans, internet images) under a unified action-in-video-out interface. The model is formulated as an observation predictor that can be rolled out autoregressively for long-horizon interaction. The authors demonstrate three applications: (1) training a vision-language policy via hindsight relabeling that completes long-horizon tabletop tasks, (2) finetuning a low-level RL policy that achieves 81% simulated success rate vs. 58% for behavioral cloning, and (3) using generated videos to improve a video captioning model (PaLI-X) which transfers better to out-of-domain captioning benchmarks than training on real ActivityNet data. Real-robot execution is shown qualitatively for both the VLM and RL policies.

## Strengths

- **Unified action-in-video-out framework trained on radically heterogeneous data.** The paper proposes a concrete strategy for converting data from simulated executions, real robot logs, human activity videos, panorama scans, and internet text-image pairs into a common representation (T5 text embeddings + discretized controls). This is a non-trivial orchestration problem, and the paper describes the processing for each data type in Section 3.1, showing how all can be used to train a single video diffusion model.

- **Autoregressive observation prediction formulation enables multi-step interaction.** The formulation as $p(o_t | h_{t-1}, a_{t-1})$ with finite-history conditioning and autoregressive sampling (Section 3.2) is a clean design. Figure 3 shows an 8-step rollout where objects manipulated in early steps (orange placed in drawer) are preserved in later steps, and Table 1 provides quantitative ablation evidence that conditioning on 4 recent frames (FVD 211.3, IS 3.52) outperforms single-frame (FVD 315.69) or distant-frame conditioning.

- **Simulator-generated data improves video captioning and transfers better than real data.** Finetuning PaLI-X (55B) on purely generated videos achieves 84% of the real-data baseline on ActivityNet (CIDEr 46.23 vs. 54.90) and *outperforms* the real-data finetuned model on MSR-VTT (27.63 vs. 24.88), VATEX (40.03 vs. 36.01), and SMIT (20.58 vs. 16.91) (Table 4). This is a non-obvious result: training on synthetic data generalized better across domains than training on real data from a single source.

- **Both VLM and RL policies trained purely in simulation are shown to execute successfully on a real robot.** Figures 4 and 5 provide qualitative evidence of zero-shot real-robot deployment on the Language Table task. While the evidence is qualitative, demonstrating sim-to-real transfer from a learned generative simulator—rather than a hand-engineered one—is technically noteworthy.

## Weaknesses

### Fatal

None.

### Major

- **Sim-to-real transfer lacks quantitative real-world evaluation.** The paper's central claim is that policies trained purely in the simulator can be deployed zero-shot in the real world (stated in the abstract and Section 1). However, the real-robot results in Sections 4.1 and 4.2 are purely qualitative—Figures 4 and 5 show a few successful image sequences, but no real-world success rates, task completion metrics, or trial counts are reported. The quantitative results (Tables 2 and 3) are evaluated *within the simulator*. This gap matters because the sim-to-real claim is the paper's headline application and is what distinguishes this work from prior video generation models. Without knowing whether, say, the RL policy succeeds on 5/50 or 45/50 real-robot trials, the reader cannot assess whether the simulator's visual fidelity is sufficient for reliable real-world transfer, or whether the qualitative successes cherry-pick the best cases.

### Minor

- **Long-horizon visual drift is not quantified.** The paper acknowledges "limited memory" as a limitation (Section 6) and shows one 8-step rollout in Figure 3, but does not systematically measure how visual quality degrades over longer rollouts (e.g., the 20–30 step rollouts used for RL in Section 4.2). Metrics like FVD, LPIPS, or CLIP consistency as a function of rollout length would help the reader understand the practical horizon at which the simulator remains reliable. This is especially relevant because the RL training relies on simulated rollouts for on-policy optimization.

- **Confidence intervals are missing from Tables 1 and 3.** Table 1 reports FID, FVD, IS, and CLIP scores without variance estimates, making it unclear whether the reported differences (e.g., 4 recent vs. 4 distant history) are significant. Table 3 reports success rates as point estimates without intervals. (Table 2 does include ±0.13, which is good.) Multi-seed or bootstrapped estimates would strengthen confidence.

- **Data mixing strategy is not ablated.** The paper describes training on datasets that differ by orders of magnitude (e.g., ~5B LAION images vs. ~700 Habitat examples) and mentions that naively combining them can hurt low-data domains (Section 3.3), mitigated by attaching a domain identifier. However, no ablation of mixing ratios, sampling weights, or curriculum is provided. Since the claim of "universal" simulation depends on successfully combining these disparate sources, the lack of analysis on whether cross-dataset transfer actually occurs (as opposed to each domain being served by its own data partition in the model) is a gap.

### Trivial

None.

## Nice-to-Haves

- A controlled small-scale real-robot evaluation (e.g., 20–50 trials per task on Language Table with success rates) would transform the credibility of the sim-to-real claim.
- Measuring nearest-neighbor similarity between generated videos and training examples would directly address whether the simulator produces genuinely novel content or reconstructions of training clips.
- An analysis of FVD or LPIPS as a function of rollout length (1 to 50 steps) would bound the practical horizon limitation acknowledged in Section 6.
- A demonstration that the same model can consume both language instructions and low-level controls within a single rollout would better justify the "unified action space" framing.

## Removed Points

- **ActivityNet memorization claim (Critical Issue #2).** The reviewer claims "ActivityNet is listed among 'human activity videos' in the data mixture" and that "the simulator memorizes or closely reproduces training videos from ActivityNet." This is factually incorrect: ActivityNet does not appear in the training data description (Section 3.1 lists Ego4D, EPIC-KITCHENS, and Something-Something V2). ActivityNet captions are used *only* to condition the simulator for generating videos used in the captioning experiment (Section 4.3)—the generated videos are novel composites, not reproductions of training clips. The broader concern about novelty of generated content is valid but belongs in Nice-to-Haves, and the specific claim about ActivityNet being in the training set is removed.
- **"Joint training data mixture is underspecified" framed as a fatal flaw.** The paper does describe the mitigation approach (domain identifiers, Section 3.3) and acknowledges the challenge. The lack of ablation is noted under Minor above, but the reviewer's framing that "the success of the approach hinges on whether these datasets can be combined without one dominating—yet the paper gives no evidence" overstates the severity. The paper does provide evidence of successful multi-domain training: the simulator works across very different domains (Habitat, Language Table, human activity, panoramas) and the downstream tasks succeed. The missing ablation is a gap, not a structural flaw.
- **"The paper's central claim of effective zero-shot sim-to-real transfer is not supported… this is a decisive weakness" (overall assessment).** This conflates "not quantitatively measured" with "not supported." The paper provides qualitative real-robot evidence (Figures 4 and 5). While quantitative evidence would be stronger, qualitative real-robot demonstration is standard and accepted in top robotics venues. The weakness is real (Major) but not fatal.
- **Demand for error bars on Tables 1 and 3 as a "strengthening" point that could invalidate results.** The lack of confidence intervals is a meaningful concern but does not invalidate the reported improvements, which are large in magnitude (e.g., 0.58 → 0.81). This is noted as Minor above.

## Novel Insights

The reviewer critiques identify an interesting tension: the paper demonstrates that a large-scale generative model can serve as a simulator for policy learning (as evidenced by the captioning results and simulated RL improvements), but the weakest link is the final step—proving that the learned simulator actually closes the sim-to-real gap rather than just reproducing photorealism that looks good to humans. The most valuable takeaway across reviews is that the video captioning experiment (Section 4.3) may actually be the strongest evidence for the simulator's quality: if the generated videos were not visually and temporally coherent, finetuning a 55B VLM on them would not produce captioning improvements that generalize across benchmarks. This indirect validation is arguably more rigorous than the qualitative real-robot images, and the paper could lean into it more explicitly.

## Suggestions

1. Add a small-scale quantitative real-robot evaluation (20–50 trials per task on Language Table) to directly substantiate the sim-to-real claim. Even a modest number of trials with success rates would transform this from a qualitative claim to a quantitative one.
2. Report FVD or LPIPS as a function of rollout length (1–50 steps) on a held-out set to bound the practical horizon of the autoregressive formulation.
3. Add bootstrap confidence intervals or multi-seed runs to Tables 1 and 3.
4. Include a nearest-neighbor analysis between generated videos and training examples to address the novelty question directly.

## Score and Decision

The paper tackles an ambitious and timely problem—building a single interactive simulator from diverse data—and provides a reasonable architecture, a clean observation-prediction formulation, and three downstream applications with evidence ranging from qualitative (real-robot) to quantitative (captioning, simulated RL). The main weakness is the lack of quantitative real-world evaluation for the central sim-to-real claim, but given the scale and ambition of the work, the qualitative evidence is meaningful and the captioning and simulated-RL results independently demonstrate the simulator's utility. The paper would benefit from the suggested additions but is a solid contribution as-is.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
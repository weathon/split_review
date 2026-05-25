Now I have all the information I need. Let me compile the final review.

## Summary of Calibration

**Round-1 bracket**: The paper sits clearly in the mid-band (between 3.5 and 7.5). The low-band anchors (2.5–3.4) are fundamentally flawed or poorly motivated — IRIS is well above this. The high-band anchors (7.6–8.0) are large-scale architectural contributions or highly polished theoretical papers — IRIS does not match that tier.

**Round-2 narrowing**: Within the mid-band, I compared against:
- **bO31lfEdos** (5.0, Reject, "Mitigating Object Hallucination"): Human-free RL for VLMs but only one model/dataset tested. IRIS has stronger evaluation (two model sizes, three benchmarks, thorough ablations) and more novelty. IRIS is clearly better.
- **Let8OMe20n** (6.0, Accept, "Confidence-aware Reward Optimization"): Benchmark + method for T2I reward overoptimization. Solid but incremental. IRIS has comparable or greater novelty but slightly narrower model scope. Comparable quality.
- **cJQ1K2fjpD** (6.2, Accept, "Fine-Grained Verifiers"): Self-alignment using model's own visual encoder. Similar philosophy (no external data). Comparable quality and evaluation thoroughness.
- **4w99NAikOE** (6.8, Accept, "IterComp"): More comprehensive evaluation but uses external reward models. IRIS is more novel (first intrinsic-only) but less comprehensive.

**What the round-1 weakness-anchored queries showed**: Papers with baseline comparison ambiguities or missing ablation analyses typically score 4–5. However, IRIS's baseline ambiguity is minor (evidence strongly suggests re-runs were done), and its ablation study is unusually thorough. The weakness-anchored queries thus support a score in the upper-mid band.

**Final score**: 6.0. The paper has genuine novelty, thorough experiments, and competitive results. The weaknesses are real but Minor and do not threaten the core claims.

Now, the final review:

---

## Summary

This paper proposes IRIS, a reinforcement learning framework that fine-tunes autoregressive text-to-image models using *only* an intrinsic reward — negative self-certainty (NSC), defined as the forward KL divergence from the model's output distribution to the uniform distribution. The key empirical finding is that minimizing self-certainty (i.e., maximizing output uncertainty) improves image generation quality, contrary to established results in language reasoning where maximizing self-certainty helps. Experiments on Janus-Pro (1B and 7B) across GenEval, T2I-CompBench, and WISE show that IRIS achieves performance competitive with T2I-R1, a method that relies on multiple external reward models (HPSv2, DINO, GIT, ORM). Extensive ablations validate the design choices (CoT usage, direction of optimization, forward vs. backward KL, RL vs. direct optimization).

## Strengths

1. **Empirical discovery that self-certainty direction is task-dependent and opposite for T2I vs. language reasoning.** Figure 2 shows the self-certainty of image tokens in Janus-Pro-1B *decreasing* during external-reward training, while text tokens in Qwen2.5-1.5B *increase*. The ablation studies (Figures 6–7) confirm that minimizing, not maximizing, self-certainty consistently improves generation quality. This is a non-trivial finding that challenges the prevailing assumption that higher certainty is always beneficial.

2. **IRIS achieves competitive performance against external-reward baselines using no human-labeled data or domain-specific verifiers.** Table 1 reports Janus-Pro-1B + IRIS scores of 0.72 (GenEval), 0.3793 (T2I-CompBench), and 0.37 (WISE), closely matching the external-reward baseline (0.75, 0.3820, 0.38) and substantially improving over the base model (0.66, 0.3338, 0.28). On the 1B model, IRIS even outperforms T2I-R1 on WISE natural science subcategories (biology, physics, chemistry), where the external reward models lack training signal — supporting the claim that intrinsic rewards lead to broader exploration.

3. **Thorough and well-designed ablation study.** Figures 5–9 systematically isolate the effect of semantic CoTs, the sign of the self-certainty reward on text and image tokens, forward vs. backward KL divergence, and the necessity of RL over direct optimization. The collapse of direct optimization (Fig. 9) is a particularly informative result that validates the GRPO-based design.

4. **Clear and well-structured presentation.** The paper is easy to follow, the motivation is grounded in an observed empirical contrast with text-domain findings, the method section is precise, and the experimental design is laid out transparently.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline comparison transparency (Minor).** The paper identifies that T2I-R1 (Jiang et al., 2025) used an incorrect chat template and states that "we will use the correct chat template to train and evaluate the Janus-Pro models." However, it does not *explicitly* state that the T2I-R1 results in Table 1 (labeled "Janus-Pro-1B + T2I-R1 (Jiang et al., 2025)") were obtained by re-running T2I-R1 with the corrected template under the same conditions. The standard deviations in the table strongly suggest re-runs (the original paper did not report them), but the paper should state this clearly. Without explicit confirmation, a reader cannot fully rule out the possibility of a setup mismatch. This is straightforward to fix with a sentence in the rebuttal/camera-ready.

2. **Non-stationarity of the intrinsic reward is not analyzed (Minor).** The reward signal (NSC) depends on the model's own output distribution and thus changes during training, creating a moving target. The paper shows that direct optimization collapses (Fig. 9) and that GRPO mitigates this, but it does not examine: (a) how the NSC value itself evolves over training (does it increase, decrease, or stabilize?), (b) the variance of the reward across the G samples, (c) sensitivity to the group size G or the KL coefficient β, or (d) whether training remains stable beyond 800 steps. While the reported results are positive, the lack of stability analysis limits confidence in the method's robustness. Running one seed for 2000 steps and showing a reward-evolution plot would largely address this.

3. **Modest improvements on the 7B model (Minor, acknowledged).** Table 1 shows that IRIS on Janus-Pro-7B yields much smaller gains (GenEval: +0.01 vs. +0.06 for 1B; T2I-CompBench: +0.0071 vs. +0.0455; WISE: +0.02 vs. +0.09). In some subcategories (Counting, Color Attribution for GenEval; Shape, Texture for T2I-CompBench) IRIS-7B underperforms the base model. The paper attributes this to the stronger base capability, but this pattern deserves a clearer discussion: does the NSC objective trade off one kind of fidelity for another, and is the method fundamentally less effective when the base model is already strong?

4. **Single architectural family tested (Minor, acknowledged).** The paper only evaluates on Janus-Pro (autoregressive). Section 4.4 acknowledges that T2I architectures are diverse (diffusion, masked modeling, MAE-style) and leaves adaptation to future work. This is appropriate as a limitation, but it means the paper's central claim — that minimizing self-certainty improves T2I generation — is only demonstrated for one model family. The discussion could note why transferring NSC to non-autoregressive models is non-trivial (token-level distributions differ fundamentally).

### Trivial

- Computational cost (training time, GPU-hours) is not reported, which would help practitioners gauge the method's practicality.
- No failure-case analysis: are there prompts where maximizing NSC produces visually chaotic or semantically empty images? A brief qualitative discussion would be informative.

## Nice-to-Haves

- **Ablation with a fixed reference model**: Training with a frozen reference model providing NSC scores would isolate the effect of non-stationarity and clarify whether the moving target is harmful or helpful.
- **Sensitivity analysis on the number of CoT strings**: The paper uses 8 text strings per prompt; varying this (e.g., 4, 8, 16) would show whether performance saturates.
- **Direct comparison with an entropy bonus in a supervised fine-tuning setup**: The paper compares against backward KL (= entropy) within the GRPO framework (Fig. 8), but a simpler supervised fine-tuning baseline with an explicit entropy penalty would be more standard and would further isolate the benefit of the RL framework.

## Removed Points

These points were identified by the reviewers but are either factually wrong, already addressed by the paper, or are generic concerns that do not apply:

- **"Fig. 2 compares different models on different tasks; this is not a controlled experiment."** — The paper explicitly states it is comparing Qwen2.5-1.5B-Instruct (on math) with Janus-Pro-1B (on T2I). It presents this as an observational finding, not a controlled experiment. The claim is appropriately qualified. **Removed.**

- **"Effective batch size of 8 is too low for policy gradient methods."** — Batch size of 8 with G=8 generates 64 completions per step, which is standard for GRPO-style methods given the high cost of generating images with autoregressive models. This concern is generic and does not identify a concrete problem with the results. **Removed.**

- **"The paper should test a 'no text reward' baseline (removing text tokens from the reward entirely)."** — The paper's Fig. 7 already includes a "minimize image SC only" condition, which removes the text reward while keeping text tokens in the generation (necessary for CoT). **Removed.**

- **"Missing comparison with simpler intrinsic signals like entropy bonus."** — Fig. 8 directly compares forward KL (IRIS) with backward KL (= entropy maximization), which is exactly this comparison. **Removed.**

- **"Missing related works."** — The rules prohibit mentioning missing related works as a weakness. **Removed.**

- **"The paper does not discuss failure cases in detail."** — This is a generic request rather than a specific problem. It affects no core claim. **Moved to Trivial.**

## Novel Insights

Beyond the paper's own contributions, two synthetic insights emerge from combining the reviews:

1. The paper's central finding — that self-certainty direction is task-dependent — resonates with a broader principle about the role of uncertainty in generative models: tasks with **objectively verifiable** outputs (math, code) benefit from mode-seeking (low entropy, high certainty), while tasks with **subjectively evaluated** outputs (image generation, creative writing) benefit from mode-covering (high entropy, moderate uncertainty). This principle may extend beyond the T2I domain tested here and offers a useful guideline for designing intrinsic rewards across modalities.

2. The paper implicitly poses a question for the field: if an intrinsic reward (NSC) that requires *no human annotation or domain-specific verifier* can match the performance of a multi-reward pipeline (HPSv2 + DINO + GIT + ORM), then what is the marginal value of those complex external reward models? The community may need to reconsider whether the standard practice of assembling bespoke reward ensembles for T2I alignment is necessary, or whether simpler intrinsic signals suffice.

## Suggestions

1. **Clarify the baseline.** In the rebuttal/camera-ready, add an explicit sentence: "We re-ran T2I-R1 (Jiang et al., 2025) using the correct Janus-Pro chat template under the same training configuration as IRIS, and report the mean and standard deviation over three seeds." This resolves the main ambiguity.

2. **Add a reward-evolution plot.** Show the average NSC (or its image-token and text-token components) over training steps for IRIS, and compare it to the same metric during external-reward training. This directly addresses the non-stationarity concern.

3. **Run one seed for 2000 steps.** Show that performance does not collapse (or, if it does, report honestly). Even a single extended run would substantially strengthen the stability claim.

4. **Discuss the 7B model's modest gains more explicitly.** Is there a fundamental limitation (saturation, tradeoff between fidelity dimensions), or is it simply that the 7B model's base distribution is already close to optimal under the NSC metric? Include a breakdown by GenEval subcategory to illuminate where IRIS-7B loses ground.

## Score and Decision

**Round-1 bracket**: Mid-band (3.5–7.5). The paper is well above low-band anchors (fundamentally flawed papers at 2.5–3.4) and below high-band anchors (major architectural or theoretical contributions at 7.6–8.0).

**Round-2 narrowing**: Comparison with mid-band anchors — bO31lfEdos (5.0, Reject, narrower scope and evaluation); Let8OMe20n (6.0, Accept, comparable quality and contribution); cJQ1K2fjpD (6.2, Accept, similar self-alignment philosophy); 4w99NAikOE (6.8, Accept, more comprehensive but less novel). IRIS compares favorably with the 6.0–6.2 anchors.

**What the round-1 low-band anchors and weakness-anchored hits failed at**: Low-band papers had unsupported central claims, absent baselines, or evaluation that was too narrow to support the claims. The weakness-anchored queries show that papers with unclear baseline comparisons or missing stability analyses tend to score 4–5 when these issues are central. IRIS avoids the first failure (its baselines are present and standard deviations suggest proper re-runs) and the second failure is minor (the core comparative findings are not invalidated by the missing reward-evolution plot).

**Final score**: 6.0 — a solid paper with genuine novelty, thorough experiments, and competitive results, held back by a few addressable presentation gaps and missing analyses that do not threaten the core claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
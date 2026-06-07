Now I have all the calibration data I need. Let me compile the final review with the score.

**Calibration comparison:**

| Anchor | Score | Comparison to Vidar |
|--------|-------|---------------------|
| Latent Diffusion Planning | 3.40 | Vidar is much stronger — has real-world, bimanual, more comprehensive |
| AVID | 5.75 | Vidar stronger — has real-world task success, not just perceptual metrics |
| Adapting Internet Video Knowledge | 5.75 | Vidar stronger — has real-world, bimanual, much better task success rates |
| SuSIE (Zero-Shot via Image-Editing) | 6.25 | Comparable — both have real-world, but Vidar has bimanual and more tasks; SuSIE has cleaner methodology |
| Probabilistic Adaptation T2V | 6.25 | Vidar tackles a harder end-to-end robot control problem |
| Grounding Video Models to Actions | 7.33 | Vidar weaker — that paper has cleaner methodology, comprehensive evaluation, fewer confounds |

**Round 1 bracket:** 5.5 – 7.0
**Round 2 narrowing:** Vidar sits between the 5.75 and 6.25 anchors. Given its stronger results and real-world bimanual experiments compared to the 5.75 group, but more significant methodological gaps than the 6.25 group, I place it at **6.0**.

---

## Summary

Vidar proposes a three-stage pipeline for data-efficient bimanual manipulation: start from an Internet-scale video diffusion model, continue pre-training on 750K cross-embodiment robot episodes in a unified observation space, and fine-tune on ~20 minutes of target-platform demonstrations. The policy factorizes into a video generation model G and a Masked Inverse Dynamics Model (MIDM) that decodes actions from generated videos while learning action-relevant spatial masks via ℓ1 regularization without dense supervision. The paper reports strong results on RoboTwin (60.0% vs. Pi0.5's 25.0% in low-data clean) and in real-world bimanual tasks (68.2% on seen, 66.7% on unseen tasks).

## Strengths

- **Strong simulation results with a challenging multi-task setup (Table 1):** Vidar achieves 60.0% average success on RoboTwin with only 20 episodes per task, substantially outperforming Pi0.5 at 25.0%. This uses a single policy for 50 tasks, which is more demanding than the leaderboard's per-task training, and supports the claim that video-based priors enable data-efficient adaptation.

- **MIDM demonstrates clear generalization benefits (Tables 4 and 5):** Replacing MIDM with a ResNet baseline drops real-world unseen-task performance from 66.7% to 26.7% (Table 5), despite both achieving 99.9% training accuracy (Table 4). The 99.9% → 24.3% train-test gap for ResNet versus 99.9% → 49.0% for MIDM provides evidence that the masking mechanism, not just model capacity, drives generalization.

- **Decoupled architecture (Eq. 111) is a sensible design:** The factorization π = I ∘ G shifts the representation burden to the video generation model (which can leverage Internet-scale and cross-embodiment pre-training) while keeping only a lightweight inverse dynamics model to train per target platform. This makes the data-efficiency claim mechanically credible.

- **Qualitative mask visualizations are compelling (Figure 3):** The learned masks highlight robot arms, joints, and end-effectors while suppressing background clutter — including on unseen backgrounds with reflective surfaces — consistent with the claim that ℓ1 sparsity induces task-relevant attention without pixel-level labels.

## Weaknesses

### Fatal

None.

### Major

- **Open-loop vs. closed-loop confound in real-world comparisons (Table 2):** Vidar uses open-loop control ("videos are generated in a single batch, without subsequent generation after the initial run," line 203), while VPP explicitly uses closed-loop control (line 213: "new action sequences are generated and executed after previous executions"). UniPi's control mode is not stated but the original UniPi (Du et al., 2023) is a closed-loop method. Open-loop and closed-loop control have fundamentally different error characteristics. The paper never acknowledges this discrepancy, controls for it, or discusses its impact on the reported margins. This makes the headline real-world comparisons in Table 2 difficult to interpret as pure evidence for the video prior's superiority. (Note: since open-loop is typically worse than closed-loop, the bias direction likely understates Vidar's advantage — but the confound still needs acknowledgment and ideally experimental control.)

- **No ablation removing the embodied pre-training stage:** The paper's central thesis is the three-stage pipeline: Internet pre-training → embodied domain pre-training (750K episodes) → target-domain fine-tuning. But there is no experiment removing the 750K intermediate stage (i.e., Internet-scale model → direct fine-tuning on target demos). The only evidence that embodied pre-training matters is the VBench comparison in Table 3, which measures video generation quality metrics rather than task success rates. A direct ablation is essential to validate whether the 750K cross-embodiment stage actually contributes to downstream performance.

- **Missing baselines from the low-data manipulation literature:** The target regime (~3 demonstrations per task, ~20 minutes total) is precisely where methods like ACT (Zhao et al., 2023) and Diffusion Policy (Chi et al., 2023) are standard. The paper justifies baseline selection by stating VLAs struggle with so little data (line 207), but ACT and Diffusion Policy are behavior-cloning methods, not VLAs. Comparing against them would directly test whether Internet-scale video pre-training adds value beyond simple imitation learning on the same data.

- **Test-time scaling is under-specified yet accounts for a large fraction of gains:** TTS uses GPT-4o to select the best of K=3 generated videos. The paper provides essentially no detail on how GPT-4o performs this evaluation — what input representation is used, what rubric or prompt is applied, or how its judgments correlate with downstream task success. In Table 5, removing TTS causes a 23-point drop on unseen tasks (66.7% → 33.3%). Without a rigorous characterization or an ablation with a simpler reproducible evaluator, the results attributed to the video prior are partially confounded with an opaque external system. That said, even without TTS, Vidar still matches or exceeds UniPi on seen tasks (45.5% vs. 36.4%).

### Minor

- **Proprioceptive conditioning partially undermines the decoupling claim (line 93):** The paper frames the factorization π = I ∘ G as elevating the action space to the video domain to decouple from embodiment-specific action spaces. But G is conditioned on "proprioceptive traces and embodiment tokens," which are themselves embodiment-specific signals.

- **Different pipeline configurations for simulation vs. real-world:** Simulation uses Wan2.2 without TTS; real-world uses Vidu 2.0 with GPT-4o TTS. This prevents cross-domain comparison of which components matter in which domain.

- **No trial counts or variance in real-world results (Table 2):** With 232 episodes across 81 tasks, the number of trials per scenario is small, yet only point success rates are reported.

- **The w/o MIDM ablation conflates masking with model capacity:** The MIDM uses a U-Net for mask prediction plus a ResNet for action regression. The "w/o MIDM" baseline replaces everything with a single ResNet, confounding the masking mechanism with additional parameters.

### Trivial

- The abstract's claim of "~1% of typical data" is rhetorically imprecise — the baseline is never concretely defined, and different systems use vastly different data volumes.

## Nice-to-Haves

- A closed-loop variant of Vidar, or evaluating baselines in open-loop mode, to control for the control architecture confound.
- An ablation replacing GPT-4o TTS with a simpler, reproducible evaluator (e.g., CLIP cosine similarity to reference frames) to isolate TTS's contribution.
- Discussion of failure modes in the main text (currently only in Appendix E).
- Reporting whether the 750K pre-training episodes contain tasks semantically similar to the evaluation tasks, to assess potential dataset overlap.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The unified observation space is conceptually straightforward"** — This is a subjective judgment about design complexity, not a substantive weakness. The contribution is in the specific design and its empirical validation.

- **"The mechanism by which the mask emerges is not explained"** — The paper does explain it: ℓ1 sparsity regularization on the mask forces the model to use minimal, most-predictive pixels. The concern that "any masking pattern that reduces the Huber loss could emerge" is precisely the intended mechanism — the mask converges to action-relevant regions because those are the regions that reduce prediction error. Figure 3 provides evidence.

- **"VBench metrics do not directly measure physical plausibility or contact accuracy"** — True but this is a limitation of the benchmark, not a paper-specific error. The paper uses VBench as one piece of evidence among many and does not overclaim what it measures.

- **"The ℓ1 regularization vs. masking mechanism ablation"** — The mask IS the mechanism through which ℓ1 operates; these are not separable confounds.

- **"Section 3.1.2 — TTS disabled for simulation 'for better reproducibility' is odd"** — The paper's stated reason is reasonable and this is a minor implementation choice, not a weakness.

## Novel Insights

The combination of (a) decoupling video generation from action prediction via the π = I ∘ G factorization, (b) using a unified multi-view observation space for cross-embodiment pre-training, and (c) ℓ1-regularized implicit mask learning for inverse dynamics is a coherent and novel architecture. The finding that sparsity-regularized mask prediction yields semantically meaningful attention maps without dense supervision — validated qualitatively in Figure 3 on reflective, unseen backgrounds — is a practically useful observation beyond this specific paper.

## Suggestions

- The single most important experiment to add is the pre-training ablation: fine-tune the Internet-scale model directly on target demos (skipping the 750K stage) and measure task success rates. This would directly validate the paper's central claim about the three-stage pipeline.
- Add ACT and/or Diffusion Policy as baselines to contextualize whether the full pipeline is necessary.
- Document the GPT-4o evaluation protocol and report agreement between GPT-4o rankings and task success. An ablation with a deterministic evaluator would strengthen the TTS evidence.
- Discuss and ideally control for the open-loop/closed-loop discrepancy in the real-world comparisons.

## Score and Decision

**Calibration summary:**

| Round | Anchor | Score |
|-------|--------|-------|
| 1 | Latent Diffusion Planning | 3.40 |
| 1 | Solving New Tasks by Adapting Internet Video Knowledge | 5.75 |
| 1 | Grounding Video Models to Actions | 7.33 |
| 2 | AVID | 5.75 |
| 2 | SuSIE (Zero-Shot via Image-Editing) | 6.25 |
| 2 | Probabilistic Adaptation of Black-Box T2V | 6.25 |

Round 1 bracket: 5.5–7.0. Round 2 narrowed to 5.75–6.25. Vidar is clearly stronger than the 5.75 anchors (has real-world bimanual experiments and stronger task success rates) but has more significant methodological gaps than the 6.25 anchors (open/closed loop confound, missing pre-training ablation, missing behavior-cloning baselines, under-specified TTS). Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
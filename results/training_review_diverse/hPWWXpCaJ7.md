Here is my consolidated meta-review:

## Summary

GEVRM proposes a closed-loop vision-language-action (VLA) framework that uses a text-guided video diffusion model to generate future goal states (behavior planning) and prototypical contrastive learning to align current/goal state representations (state alignment), motivated by inspiration from classical internal model control (IMC). The method is evaluated on the CALVIN benchmark (standard and perturbed setting) and the Bridge dataset for goal generation quality, achieving strong results.

## Strengths

- **Highly expressive goal generation via combined spatiotemporal compression and random-mask training.** The paper's video planner uses 2D VAE (8× spatial) + 3D VAE (4× temporal) compression with a random-mask mechanism (75% weight on unmasking first h frames). This yields large improvements over GR-1 and AVDC on FID (94.47 vs. 236.75) and FVD (3.8 vs. 12.83) on the Bridge dataset (Tab. 1), and qualitative results (Fig. 3) show GEVRM reduces hallucinations under perturbation.

- **State-of-the-art performance on the standard CALVIN benchmark (ABC→D).** GEVRM achieves the best average task completion length (0.66) across all five evaluation tasks, outperforming UniPi, HiP, and GR-1* (Tab. 2). The 7-task chain success rate also shows consistent improvements.

- **Decoupled training reduces dependency on expensive action-language pairs.** The problem decomposition (Eq. 1) separates behavior planning (requires only text-video pairs) from action prediction (requires only play data without language labels), a practical advantage for leveraging large-scale internet video data.

- **Robustness to the key hyperparameter λ.** The ablation in Fig. 5b tests five values of the state-alignment loss weight and shows minimal performance variation, with λ=1 optimal — indicating the method is not brittle to tuning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The IMC framing is inspirational/analogical, not a formal integration.** The paper maps IMC components to GEVRM components (Fig. 1), but the mapping is loose. In IMC, the internal model explicitly models plant dynamics and computes a prediction-error feedback signal to cancel disturbances. Here, the "internal model" is a video generator that produces future goal states (reference inputs, not system dynamics), and the "feedback" is contrastive embedding alignment rather than a prediction-error correction mechanism. The paper's language is honest about this ("inspired by," "adjusted accordingly"), but the title and abstract claim to "integrate the IMC principle," which overstates the connection. This does not invalidate the method's empirical results but mispositions the contribution relative to control theory.

- **The source of robustness is not isolated.** The ablation for state alignment (SA) is conducted only on the *clean* environment D (Fig. 5a), not on the perturbed environments. The perturbed evaluation (Tab. 3) compares full GEVRM only against SuSIE, with no variant that removes SA. Therefore, the robustness gains in Tab. 3 cannot be definitively attributed to the contrastive alignment mechanism — they could also come from the video planner's superior goal quality, the diffusion policy's multi-modality, or interactions between components. An ablation of SA under the same perturbed conditions would substantially strengthen the paper's central claim.

- **Limited baselines on perturbed environments.** Tab. 3 compares GEVRM against SuSIE alone on the five perturbed CALVIN scenarios. UniPi, HiP, and GR-1 — which serve as baselines on the standard setting (Tab. 2) — are not evaluated under perturbations. The choice of SuSIE is justified as the SOTA augmentation-based method, but the absence of broader comparisons weakens the "state-of-the-art under perturbations" claim.

- **No statistical uncertainty reported.** No confidence intervals, standard deviations, or multi-seed results are reported for any action execution results (Tab. 2, Tab. 3). Given known variance in robot manipulation, this makes it difficult to assess the significance of the reported improvements.

### Trivial

- **Citation error.** GR-1 is correctly cited as (Wu et al., 2023) in the goal generation baselines (line 139) but incorrectly cited as (Black et al., 2023) in the action execution baselines (line 161). Black et al. (2023) is SuSIE, which is also cited on the same line.

## Nice-to-Haves

- Ablate finer-grained video generation design choices (random mask ratio, 2D vs. 3D VAE) to further understand what drives goal quality.
- Include a discussion of failure modes — what kinds of perturbations does GEVRM still struggle with?
- Report inference time, as video generation at test time could introduce latency.
- Include a more detailed limitations section to improve credibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"FVD of 3.8 seems implausibly low"** — Speculation without evidence. CALVIN is a simple simulated environment where low FVD is possible. Removed as factually unsubstantiated.
- **"SuSIE is an image-editing model, not a video generation method — the comparison is not like-for-like"** — The paper explicitly chose SuSIE as the relevant robustness baseline (augmentation-based SOTA), not as a video-generation comparison. Removed as evaluating against the wrong standard.
- **Strength: "Principled integration of IMC yields measurable robustness gains"** — Conflicts with verified weakness that the IMC mapping is loose/inspirational rather than formally principled. Removed per rule (strength-weakness conflict → weakness wins).
- **Strength: "State alignment via prototype contrastive learning is essential for robustness"** — Conflicts with verified weakness that SA's contribution to robustness specifically (vs. general performance) is not isolated on perturbed environments. Removed per same rule.
- **"Missing ablations of video generation components (random mask ratio, flow steps, VAE choice)"** — These are design choices whose absence does not threaten core claims. Moved to Nice-to-Haves.
- **"The paper does not discuss limitations / failure cases / inference time"** — Valid suggestion but not a flaw in the paper's claims. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the claimed IMC framing and the actual method, and the need for more targeted ablation under perturbations, but these are standard critical observations rather than novel insights.

## Suggestions

- Run the perturbed CALVIN evaluation with GEVRM *without* state alignment (SA) and with a simpler alignment variant (e.g., InfoNCE without prototypes) to isolate whether the specific contrastive mechanism drives robustness.
- Evaluate at least one additional baseline (e.g., GR-1 or UniPi) under the five perturbed settings to strengthen the SOTA claim.
- Report standard deviations or confidence intervals across multiple seeds for all main results.
- Correct the GR-1 citation error in Section 5.2.
- Tone down the IMC framing language (title, abstract) to "inspired by" or "drawing inspiration from" unless a formal mathematical mapping is provided.

## Score and Decision

**Originality:** The combination of video diffusion planning with contrastive state alignment is reasonably novel, though each component draws on existing techniques. The IMC framing is distinctive but not deeply realized.

**Importance of research question:** Addressing robustness to perturbations in VLA models is practically important and under-explored. The paper tackles a genuine deployment challenge.

**Claims support:** The standard CALVIN results are well-supported. The robustness claims are moderately supported — the overall system outperforms SuSIE, but the attribution to SA specifically is not isolated, and baselines are limited.

**Soundness of experiments:** The experimental design is generally sound but has gaps (missing perturbation ablation, no error bars, limited perturbed baselines). The method's effectiveness on standard CALVIN is convincing.

**Clarity of writing:** The paper is clearly written. The IMC motivation is explained, the method is described in sufficient technical detail, and the figures are helpful.

**Value to the community:** The empirical results on CALVIN (especially the 45.9% improvement in average completion length under perturbations vs. SuSIE) are useful. The decoupled training framework is a practical contribution.

**Overall:** The paper presents a method that works well on the CALVIN benchmark, with clear improvements over strong baselines in the standard setting and promising robustness results. The weaknesses are addressable and do not invalidate the core empirical contribution. The IMC framing is overstated but the underlying method and results are solid.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
## Summary

IRIS (Intrinsic Reward Image Synthesis) proposes using Negative Self-Certainty (NSC) — the negation of KL(U‖π_θ) summed over output tokens — as an intrinsic RL reward to fine-tune autoregressive text-to-image models via GRPO, without external reward models or human-labeled data. The paper's motivating observation (Figure 2) is that external-reward RL training on T2I tasks *decreases* model certainty on image tokens while the same training *increases* certainty on text tokens in language tasks — a task-dependent divergence that the authors leverage as justification for NSC. Empirical results on GenEval, T2I-CompBench, and WISE show IRIS achieves roughly 90–95% of external-reward (T2I-R1) performance across most benchmarks and model sizes.

---

## Strengths

- **Genuine motivating observation (Figure 2):** The empirical finding that external-reward RL on Janus-Pro-1B decreases image-token self-certainty (orange line, right y-axis) while the same training increases text-token self-certainty on Qwen2.5-1.5B (blue line, left y-axis) is concrete, reproducible, and non-obvious. It directly motivates the asymmetric design of NSC.

- **First intrinsic-reward RL framework for autoregressive T2I:** The paper documents meaningful improvements over the base model: +9.1%, +13.3%, +28.8% on GenEval, T2I-CompBench, and WISE for Janus-Pro-1B (Table 1), achieved without any external supervision — a practical contribution for settings where reward models are unavailable.

- **Ablation depth:** Figures 5–9 systematically verify: (a) CoT vs. no-CoT, (b) minimize vs. maximize image SC, (c) minimize vs. maximize text SC, (d) forward vs. backward KL, and (e) GRPO+NSC vs. direct NSC optimization. Especially Figure 6 is informative: maximizing image SC causes a rapid performance drop, while minimizing it improves performance, showing the reward polarity is causally important.

- **Domain generalization advantage of intrinsic rewards:** Table 1c confirms that IRIS outperforms T2I-R1 on the biology, physics, and chemistry sub-categories of WISE — categories where the external rewards used in T2I-R1 (HPSv2, DINO, GIT, ORM) have limited coverage — supporting the paper's claim that intrinsic signals enable broader exploration.

- **Responsible baseline correction:** The discovery and correction of a systematic chat-template bug in T2I-R1's official implementation (using Janus chat template keys for Janus-Pro models) is methodologically sound and clearly disclosed.

---

## Weaknesses

### Fatal

None.

### Major

- **The CoT confound is unresolved.** Both IRIS and T2I-R1 use semantic chain-of-thought: the model first generates a text description, then synthesizes the image. Figure 5 shows that CoT dramatically improves IRIS — but there is no control condition running GRPO+CoT with a constant or null reward (zero advantage). Without this control, it is impossible to cleanly separate how much of the improvement is attributable to the NSC reward signal versus the GRPO+CoT training dynamic itself (iterative rollout-based fine-tuning with diverse sampling). The ablations in Figures 6–7 do show that the *direction* of the reward matters (maximizing image SC causes collapse), which suggests NSC is not inert. But they do not rule out that GRPO+CoT with any non-trivial signal — or even constant advantage — would yield comparable gains. This is the paper's central evidential gap: the specific contribution of NSC as a quality-discriminating signal is not isolated from the joint effect of CoT structure and GRPO's distributional regularization.

### Minor

- **Performance framing is overstated in the abstract.** The abstract states IRIS achieves "performance that is competitive with or superior to external rewards." However, Table 1 shows IRIS consistently trails T2I-R1 on most headline metrics: GenEval 1B (0.72 ± 0.01 vs. 0.75 ± 0.01, outside combined error bars), WISE 1B (0.37 ± 0.01 vs. 0.38 ± 0.01), and T2I-CompBench 7B (0.3916 ± 0.0024 vs. 0.3992 ± 0.0019). The more measured caption in Figure 3 — "IRIS can achieve comparable results with T2I-R1" — is accurate; the abstract's "or superior to" is not justified by Table 1.

- **Theoretical framing in Section 3.2 contains a directional error.** Section 3.2 states: "self-certainty by the forward KL divergence, which encourages mode-covering behavior" and characterizes entropy (backward KL) as "mode-seeking and favor a single high-probability output." Entropy maximization is mode-*spreading*, not mode-seeking (mode-seeking arises when minimizing KL(π‖p)). The mathematical definitions and empirical results are correct — KL(U‖π) is indeed high when π is concentrated — but the prose explanation of forward vs. backward KL in terms of "mode-covering" vs. "mode-seeking" misapplies standard terminology and will confuse readers.

- **Direct NSC collapse (Figure 9) merits deeper analysis.** The paper shows that directly maximizing NSC (without GRPO's relative advantage formulation) causes complete model collapse by step 800 (GIT → 0.00, ORM → 0.00). The paper's explanation — "GRPO employs a more conservative strategy" — is hand-wavy. The more informative explanation is that GRPO's relative advantage normalizes rewards *within* a batch, effectively acting as a form of implicit regularization that prevents runaway optimization. This mechanistic gap matters because Figure 9 implies NSC can be "gamed" easily — the real driver of stability is GRPO's structure, not the intrinsic quality of NSC as an image quality proxy.

### Trivial

- The caption for Figure 3 says "IRIS can achieve comparable results with T2I-R1" whereas the 1B GenEval comparison (0.72 vs. 0.75) is arguably outside the margin of comparable; the caption's language in this specific case deserves a slight hedge.

---

## Nice-to-Haves

- A null-reward or constant-advantage GRPO+CoT baseline would substantially strengthen the mechanistic claim that NSC — not just the CoT+GRPO infrastructure — is the operative improvement driver. This single experiment would resolve the paper's core evidential gap.
- Qualitative analysis of what NSC selects for at the VQ-codebook level (e.g., codebook coverage statistics, token repetition rates across high-vs-low-NSC rollouts) would connect the abstract reward signal to the observed visual richness of outputs.
- Whether the corrected T2I-R1 baseline is stronger or weaker than Jiang et al.'s originally reported numbers is worth one sentence of clarification, since this affects how the performance gap should be interpreted.
- A brief comment on whether NSC-based RL could extend beyond Janus-Pro to other autoregressive T2I architectures (masked modeling, MAE-style) would increase practical relevance — the paper mentions this in §4.4 but only as a future direction.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Ablation metric circularity (Harsh Critic):** The critic argued that using HPSv2, DINO, GIT, and ORM for ablation evaluation subtly biases IRIS ablations toward T2I-R1's objective. Removed: since IRIS never trains on these metrics, using them for evaluation is standard and unbiased. All ablation configurations are evaluated on the same metrics, and the full configuration space is explored.

- **T2I-R1 correction favoring/disfavoring the baseline (Harsh Critic):** The critic raised the question of whether the chat-template fix makes T2I-R1 stronger or weaker. Removed as actionable weakness: both methods use the corrected template, so the comparison is internally consistent. This is a point of curiosity, not a methodological flaw.

- **Strength: "competitive with or superior to" (Strength Finder):** The Strength Finder characterized IRIS as matching or exceeding T2I-R1. Partially removed/demoted: Table 1 shows IRIS *trailing* T2I-R1 on most headline metrics. The trajectory in Figure 3 (1B models) shows IRIS surpassing T2I-R1 during training, but the best-checkpoint numbers in Table 1 tell a more modest story. Retained only as "~90–95% of external-reward performance" which is verifiable.

---

## Novel Insights

The most genuinely novel insight in this paper is the task-dependent inversion of self-certainty's role: the same RL training pressure that concentrates probability mass in text reasoning (producing more confident outputs that score higher on verifiable tasks) simultaneously *diffuses* probability mass in image generation (producing less confident outputs that score higher on human-preference metrics). If this observation holds robustly — and Figure 2 provides clean quantitative support — it suggests that the role of model confidence is not uniform across modalities and that the appropriate intrinsic reward may need to be modality-specific. The Figure 9 collapse result adds a secondary insight: GRPO's relative-advantage normalization is doing substantial stabilization work when the reward is non-verifiable, and intrinsic rewards may depend on this implicit regularizer more than previously appreciated.

---

## Suggestions

1. Add a GRPO+CoT+constant-reward (null advantage) ablation condition to isolate the contribution of NSC from the GRPO+CoT training infrastructure.
2. Correct the mode-seeking/mode-covering terminology in Section 3.2 — entropy maximization is mode-spreading, not mode-seeking; forward KL(U‖π) vs. backward KL(π‖U) should be characterized accurately.
3. Revise the abstract from "competitive with or superior to external rewards" to "competitive with, though slightly trailing, external rewards" — consistent with the more accurate characterization in Figure 3's caption.
4. Provide a mechanistic account in Figure 9's discussion of why GRPO stabilizes NSC optimization (relative advantage normalization as implicit regularization) rather than attributing stability to GRPO being "more conservative."

---

## Score and Decision

**Originality:** The task-dependent inversion of self-certainty and the first intrinsic-reward RL method for autoregressive T2I are genuinely new. Score: 4/5.

**Importance:** Removing the dependency on external reward models in T2I RL is practically significant. Score: 4/5.

**Claims supported:** The core claim (NSC improves T2I without external supervision) is empirically supported; the stronger claim (NSC is *the* mechanism, rather than CoT+GRPO) is not cleanly established. Performance comparisons are slightly overstated in the abstract. Score: 3/5.

**Soundness:** Ablation design is solid; the CoT confound is the main gap; theoretical framing in §3.2 has inaccuracies. Score: 3/5.

**Clarity:** Generally clear presentation; the Section 3.2 explanation of forward vs. backward KL is the main clarity issue. Score: 3/5.

**Community value:** Practical method for RL-based T2I alignment without external supervision, with broad applicability. Score: 4/5.

**Overall:** IRIS is a meaningful contribution with real empirical results. The CoT confound is the most significant evidential gap but does not invalidate the results — just limits the mechanistic interpretation. The paper is borderline-accept: the contribution is genuine, the direction is promising, and the ablations are thorough, but the central causal claim needs the missing control experiment to be fully convincing.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>
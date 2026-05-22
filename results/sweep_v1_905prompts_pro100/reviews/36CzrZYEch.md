Now I have a solid calibration picture. Let me write the review.

## Summary

This paper proposes IRIS, a reinforcement learning framework that fine-tunes autoregressive text-to-image models using only an intrinsic reward signal — the negative self-certainty (NSC, forward KL divergence from the model's output distribution to a uniform distribution). The key insight is that minimizing self-certainty (i.e., maximizing self-uncertainty) improves image generation quality, running counter to findings in text-only reasoning where maximizing self-certainty helps. Using GRPO on Janus-Pro models, IRIS achieves performance competitive with or approaching a baseline trained with four external reward models (T2I-R1), across GenEval, T2I-CompBench, and WISE benchmarks, without any domain-specific reward engineering.

## Strengths

- **Novel contribution with strong motivation**: IRIS is, to the best of the authors' knowledge, the first framework to successfully train T2I models using RL with only an intrinsic reward. The observation that autoregressive T2I models benefit from lower self-certainty (while text LLMs benefit from higher) is counterintuitive and well-motivated by the qualitative demonstrations in Figure 1, which show that confident models produce flat, uniform images while less-confident ones generate richer outputs.

- **Rigorous ablation study isolating every design choice**: Figures 5–9 provide a comprehensive set of ablations: CoT vs. no CoT, minimizing vs. maximizing image SC, minimizing vs. maximizing text SC, forward KL vs. backward KL, and RL vs. direct optimization. Each ablation cleanly isolates one variable, and the results consistently support the final IRIS configuration. The finding that direct NSC maximization causes model collapse (Figure 9) while GRPO-based optimization does not is a practically important observation.

- **Broad evaluation across benchmarks and scales**: Table 1 reports results on three complementary benchmarks (GenEval for object composition, T2I-CompBench for attribute binding, WISE for world knowledge) at two model sizes (1B and 7B), all with standard deviations. This goes beyond single-benchmark evaluation and gives a realistic picture of the method's capabilities.

- **Identifies and corrects a concrete flaw in prior work**: The paper documents and fixes an incorrect chat template used by Jiang et al. (2025) for Janus-Pro (using Janus's template instead of Janus-Pro's), improving the fairness and reproducibility of all comparisons.

- **Well-structured and clearly written**: The method section is precise, the motivation is laid out step by step, and the ablations are presented in a logical order that builds the case for the final design.

## Weaknesses

### Major

- **Task-dependence claim is based on an uncontrolled cross-model comparison**: The paper's headline observation (Figure 2) — that RL alignment increases text self-certainty for reasoning but decreases image self-certainty for T2I — compares Qwen2.5-1.5B-Instruct (a text-only LLM) against Janus-Pro-1B (a multimodal T2I model) on completely different tasks with different reward structures. These differ in architecture, training objective, output modality, and reward schema; any of these could explain the divergent self-certainty trajectories independently of any fundamental "task-dependent" property. The paper treats this as confirmed fact ("we observe and confirm that the model's self-certainty exhibits task-dependent behaviors"), which overstates what the evidence supports. The within-model ablation studies (Figures 6–7) independently verify that minimizing image SC helps and that maximizing it hurts within Janus-Pro, which is sufficient for the paper's core contribution, but the cross-task generalization claim in the second contribution bullet should be substantially tempered.

- **Validation limited to a single autoregressive model family**: All experiments use Janus-Pro (1B and 7B), an autoregressive discrete-token T2I model. The paper acknowledges (Section 4.4) that T2I architectures are diverse and that extending IRIS to other paradigms is future work, but the title and framing treat IRIS as a general T2I method. Autoregressive discrete-token models have known tendencies toward repetitive outputs, which the NSC reward may specifically counteract. Without evidence from even one non-autoregressive architecture, the claimed generality is speculative.

### Minor

- **"Enhances reasoning capabilities" claim overreaches**: The paper states that "IRIS itself can significantly enhance the reasoning capabilities of T2I models." The evidence is that IRIS with semantic CoTs outperforms IRIS without CoTs (Figure 5) and that meaningful CoTs emerge during training (Figure 4). However, this shows that CoT helps IRIS, not that IRIS specifically enhances reasoning beyond what CoT provides. The interesting and well-supported finding is that an intrinsic uncertainty reward is sufficient to induce useful CoT behavior — previously only shown with external rewards — but framing this as "enhancing reasoning capabilities" is overstated.

- **Small-magnitude advantages are described as surpassing the baseline**: The paper claims IRIS "surpasses T2I-R1" in WISE natural science categories, but the differences are tiny and mostly within error margins: Physics 0.45 vs. 0.43 (±0.02 and ±0.01), Chemistry 0.22 vs. 0.22 (±0.01). These should be described as comparable, not superior.

### Trivial

- None significant beyond the presentation issues noted above.

## Nice-to-Haves

- A human evaluation study (even small-scale, e.g., 100–200 pairwise comparisons) would substantially strengthen the claim that lower-self-certainty models produce images "more preferred by humans." The benchmarks used are automated and may not fully capture human aesthetic preferences.

- A comparison with simple decoding-time diversity interventions (e.g., increased temperature, nucleus sampling with higher p) would clarify whether the RL procedure provides benefits beyond what a well-tuned stochastic decoding strategy could achieve. The backward KL comparison (Figure 8) partially addresses this but temperature-based baselines remain untested.

- A brief discussion of failure modes or settings where NSC might be harmful (e.g., prompts requiring precise, deterministic outputs) would make the method more credible and useful to practitioners.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic #2 (limited validation scope as fatal)**: REMOVED as a fatal/major weakness because the paper explicitly scopes its contribution to autoregressive T2I models and acknowledges the diversity of T2I architectures as future work (Section 4.4). Demanding results on diffusion or masked-modeling architectures is scope creep. Retained as a minor weakness about the claim of generality.

- **Harsh Critic on ablation evaluation metrics being biased**: REMOVED. The paper uses the four external reward models only for ablation evaluation (Figures 5–9), where comparisons are between IRIS variants that share the same metric bias. For the main benchmark results (Table 1), the paper uses GenEval, T2I-CompBench, and WISE — none of which are the reward models. The paper correctly notes this distinction. The harsh critic's concern applies mainly to interpreting absolute scores in ablation plots, which the paper does not overinterpret.

- **Harsh Critic demanding error bars and significance testing**: REMOVED. Table 1 already reports standard deviations for all IRIS and T2I-R1 results (e.g., "0.72 ± 0.01"), and Figure 3 shows training curves with visible variance.

- **Strength Finder "discloses modality-dependent self-certainty behavior with empirical evidence"**: PARTIALLY REMOVED as a standalone strength. The cross-model comparison in Figure 2 is uncontrolled, so this can't be treated as strong evidence for modality/task dependence. The within-model evidence (Figures 6–7) is strong for the T2I direction specifically. Retained in the first strength bullet with appropriate caveats.

- **Strength Finder "broad evaluation"**: RETAINED but tempered — three benchmarks is good but within one architecture family.

- **Generic strengths** ("important problem," "interesting question"): REMOVED as they lack specificity.

## Novel Insights

The paper's genuinely novel insight — beyond its own stated contributions — is the empirical observation that direct gradient-based optimization of the NSC objective causes catastrophic model collapse while GRPO-based RL optimization of the same objective does not (Figure 9). This is a practically significant finding for anyone attempting to use self-certainty or entropy-based objectives in generative model training, and it provides an interesting case study of why RL-based optimization can be preferable even when the reward is fully differentiable.

## Suggestions

- Tone down the task-dependence claim. Replace "we observe and confirm that the model's self-certainty exhibits task-dependent behaviors" with language that treats Figure 2 as a motivating observation rather than a confirmed finding. The within-model ablation evidence in Figures 6–7 is sufficient to motivate the T2I-specific design without relying on the cross-model comparison.

- Clarify that the "reasoning enhancement" claim refers specifically to the emergence of useful CoTs during IRIS training without external supervision — this is a meaningful finding but should not be framed as a general reasoning improvement.

- If adding a second architecture is infeasible, strengthen the analytical argument for why NSC should help beyond autoregressive models, and explicitly scope the claims to autoregressive T2I.

## Score and Decision

**Round 1 bracketing**: Queries retrieved anchors at 2.50–3.40 (weak band), 5.00–6.80 (middle band), and 7.60–10.00 (strong band). IRIS clearly sits above the weak band because it has a genuine novel contribution with thorough empirical validation, and clearly below the strong band (Transfusion at 7.60, SANA at 8.50) which represent larger-scale, more broadly validated contributions. Initial bracket: **5.5–7.5**.

**Round 2 narrowing**: Retrieved anchors at 5.25 (Text-to-Layout RLHF), 5.75 (Scaling AR T2I), 6.00 (Confidence-aware Reward T2I), 7.25 (Motif), 7.33 (GOPS, Grounding Video). IRIS is stronger than the 6.00 paper (which has a narrower contribution and less thorough ablations), comparable to IterComp (6.80), and weaker than Motif (7.25), which has a similarly novel intrinsic-reward idea but broader environmental evaluation and stronger baseline comparisons.

**Anchor comparison summary**:
- `jQP5o1VAVc` (5.75, R2): Scaling AR T2I — empirical architecture study; IRIS is more novel and better evaluated.
- `Let8OMe20n` (6.00, R2): Confidence-aware reward for T2I — useful but incremental; IRIS has a cleaner, more general contribution.
- `kIP0duasBb` (6.67, R1): CLIP reward TTA — comparable novelty and evaluation quality; IRIS has better ablations but narrower architecture scope.
- `4w99NAikOE` (6.80, R1): IterComp — comparable (RL for T2I, good ablations, one base model); IRIS has a simpler, more general idea.
- `tmBKIecDE9` (7.25, R2): Motif — stronger paper with broader environmental evaluation; IRIS is below this.
- `SI2hI0frk6` (7.60, R1): Transfusion — large-scale multimodal model with comprehensive evaluation; IRIS is clearly below this.

**Final score**: 6.5. IRIS has a genuinely novel and clean idea, thorough ablations, and solid benchmark results that demonstrate its core claim. The overclaiming on task-dependence and limited architecture scope prevent it from reaching the 7+ range, but the paper's contribution is clearly above the 5–6 range where papers with significant evaluation gaps or incremental contributions land.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
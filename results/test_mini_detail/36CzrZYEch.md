Now I have sufficient calibration data. Let me write the consolidated review.

## Summary

The paper proposes IRIS, the first RL-based framework for finetuning autoregressive text-to-image (T2I) models using only an intrinsic reward—negative self-certainty (NSC), defined as the forward KL divergence between the model's output distribution and a uniform distribution—without any human labels, preference data, or domain-specific verifiers. The key finding is that *minimizing* self-certainty improves image generation quality, opposite to text-domain findings where maximizing self-certainty is beneficial. IRIS is evaluated on Janus-Pro (1B and 7B) across GenEval, T2I-CompBench, and WISE benchmarks, achieving results competitive with T2I-R1 which uses four external reward models.

## Strengths

1. **Counterintuitive finding validated across multiple conditions**: The paper demonstrates that minimizing self-certainty (rather than maximizing it) improves T2I generation quality. This is supported by the training dynamics observation (Figure 2: self-certainty on image tokens decreases during RL with external rewards) and, more importantly, by the causal ablation in Figure 6 where minimizing image self-certainty consistently outperforms maximizing it across all four external evaluation metrics (HPSv2, GIT, GDino, ORM). The contrast with text-domain findings where higher self-certainty is beneficial is clearly articulated and well-motivated.

2. **Competitive performance against external-reward baselines without any labeled data**: Table 1 reports that IRIS on Janus-Pro-1B achieves overall scores of 0.72 (GenEval), 0.3793 (T2I-CompBench Complex), and 0.37 (WISE), versus 0.75, 0.3820, and 0.38 for T2I-R1 (which uses four external reward models). On several subcategories IRIS matches or exceeds T2I-R1 (e.g., Color attribute binding in T2I-CompBench: 0.7946 vs 0.7924; Physics in WISE: 0.45 vs 0.43). This demonstrates that an intrinsic-only reward can approach methods relying on domain-specific verifiers.

3. **Rigorous ablations isolating each design choice**: Figures 5–9 systematically test semantic CoTs (with/without), text vs. image self-certainty direction (minimize/maximize), forward vs. backward KL divergence, and RL vs. direct optimization. All ablations use four external reward models as unbiased metrics (since IRIS never uses them in training). This methodology cleanly validates why each component of IRIS is necessary—particularly the finding that RL is essential (direct optimization collapses, Figure 9) and that forward KL outperforms backward KL (Figure 8).

4. **Correction of a known implementation error improves fairness**: Section 4.1 identifies and fixes an incorrect chat template in the T2I-R1 baseline (Janus vs. Janus-Pro templates were mixed up in the original implementation). This attention to implementation detail ensures fair comparisons and benefits reproducibility for future work building on IRIS.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Overstated "superior" claim**: The abstract and introduction claim IRIS achieves performance "competitive with or superior to external rewards." However, Table 1 shows IRIS consistently trails T2I-R1 on *overall* scores across all three benchmarks: GenEval 0.72 vs 0.75 (1B), T2I-CompBench 0.3793 vs 0.3820, WISE 0.37 vs 0.38. While IRIS excels on some subcategories (e.g., WISE Physics, T2I-CompBench Color), the overall scores favor T2I-R1. The paper's own Figure 3 caption says IRIS achieves "comparable results" with T2I-R1. The "superior" framing in the abstract is not supported by the aggregate results and should be calibrated to "competitive with" to align language with evidence.

2. **Training prompt distribution underspecified**: Section 4.1 states "we primarily follow the protocol in T2I-R1 (Jiang et al., 2025)" but does not specify the source, composition, or size of the training prompt set used for RL finetuning. This is a reproducibility concern: readers cannot assess whether the training prompts overlap with evaluation benchmarks or whether results are sensitive to prompt distribution. A brief specification (e.g., source dataset, number of prompts, filtering criteria) should be provided in the main text.

3. **Figure 2 lacks statistical variance**: The motivating observation (Figure 2) shows self-certainty decreasing on image tokens during a single training run with no error bars or confidence intervals. The y-axis range spans about 6% (18.75–20.50). While the paper's primary evidence for the direction of self-certainty comes from the causal ablations (Figures 6–7), the observational claim in Figure 2 would be strengthened by multiple seeds or explicit acknowledgment that this is a single-run observation.

### Trivial
None.

## Nice-to-Haves

- **Length normalization discussion**: The advantage estimation (Eq. 4) sums NSC tokens without normalizing by sequence length. NSC values are non-positive, so longer sequences could systematically accumulate more negative rewards. While the z-score standardization across G samples and the `1/|o_i|` factor in the GRPO objective (Eq. 3) partially mitigate this, a brief discussion or a simple control ablation would strengthen the method section and preempt a likely reviewer question.

## Removed Points

- **"Missing comparison with official T2I-R1 scores"**: The paper fixes a chat template bug in T2I-R1's implementation and reports corrected scores. This is a strength (improving fairness), not a weakness. The critic's suggestion to additionally report the original buggy scores is unnecessary — the corrected implementation is the valid baseline.
- **"Paper should note that Janus-Pro is a unified multimodal model"**: The paper already notes this in Section 3.2: "The output token o_t could be a text or image token in the multimodal LLMs."
- **"Missing human evaluation"**: Standard for this line of work; automated benchmarks are the norm for T2I evaluation.
- **Strength Finder's claim of "surpassing" external rewards**: Replaced by the more accurate "competitive with" framing above. IRIS surpasses T2I-R1 on some subcategories but trails on overall scores.

## Novel Insights

The meta-review reveals a pattern across both reviews: the paper's central contribution is robustly supported by ablations, but its headline framing is slightly misaligned with the quantitative results. The reviewers agree on the method's soundness and the value of the counterintuitive finding (minimizing > maximizing self-certainty for T2I), while correctly noting that the "superior to external rewards" claim goes beyond what Table 1 shows. The most interesting unresolved question—raised implicitly by both the paper and the reviews—is why intrinsic rewards, despite using zero domain knowledge, sometimes outperform external rewards on knowledge-intensive subcategories like natural science (WISE). This suggests external reward models have blind spots that intrinsic exploration can bypass, which is a potentially deeper insight than the paper develops.

## Suggestions

1. Calibrate the abstract and introduction wording from "competitive with or superior to" to "competitive with" or "comparable to." The data supports competitive, not superior.
2. Add a sentence specifying the training prompt source and size in Section 4.1.
3. Add error bars or multiple-seed variance to Figure 2, or explicitly note it is a single-run observation and defer to the causal ablations as the primary evidence.
4. Add a brief discussion of length bias in the advantage estimation—one paragraph or a footnote would suffice.

## Score and Decision

### Round 1 — Bracketing

| Band | Papers Retrieved | Avg Score |
|------|-----------------|-----------|
| Weak (< 3.5) | NZ5KXXDv1T, hgayrNSbri, FTpdQBoBd0, hCfhfwSfCg | 2.0–3.4 |
| Middle (3.5–7.5) | kIP0duasBb (6.67), RauUgiw7VX (4.75), tjn2YZSHUv (6.75), kNjrhD67LP (7.0) | 4.75–7.0 |
| Strong (> 7.5) | uAFHCZRmXk (8.0), SI2hI0frk6 (7.6), rmg0qMKYRQ (8.0), N8Oj1XhtYZ (8.5) | 7.6–8.5 |

**Bracket:** The paper is clearly above the weak band (scores 2–3.4) and below the strong band (7.5+). The plausible range is 5.0–7.0.

### Round 2 — Narrowing

| Anchor Paper | Score | Round | Comparison |
|-------------|-------|-------|------------|
| eC2ICbECNM (Ctrl-U) — Uncertainty-aware reward for conditional image gen | 6.00 | R2 | Very similar topic (reward-based training for image gen). IRIS has a stronger conceptual contribution (intrinsic reward, counterintuitive finding) but weaker on practical deployment. Comparable overall quality. |
| tjn2YZSHUv (Social Reward) — Million-user feedback for T2I eval | 6.75 | R1 | Social Reward has a massive dataset contribution but a simpler method. IRIS has a more novel methodological finding but smaller scale. IRIS is slightly below this anchor. |
| kNjrhD67LP (ITIT) — Unpaired data via cycle consistency | 7.00 | R1 | Strong large-scale contribution. IRIS's contribution is more focused (intrinsic reward) and less ambitious in scope. IRIS is below this anchor. |
| kIP0duasBb (CLIP Reward TTA) — RL with CLIP reward for VLM | 6.67 | R1 | Similar RL+reward paradigm. IRIS has a more surprising and specific finding (negative self-certainty direction differs by modality). Comparable quality. |
| RauUgiw7VX (Fine-grained T2I) — Semantic refinement for T2I | 4.75 | R1 | Rejected due to limited novelty and missing comparisons. IRIS is clearly stronger in novelty and experimental rigor. |

### Final Score

The paper sits between Ctrl-U (6.0) and Social Reward (6.75), closer to Ctrl-U due to IRIS's narrower experimental scope and the minor framing/reproducibility gaps. The core contribution is novel and well-supported by thorough ablations. The weaknesses are fixable without altering the contribution. **Score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
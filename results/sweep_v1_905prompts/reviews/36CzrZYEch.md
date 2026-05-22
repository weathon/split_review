Now I have sufficient calibration data. Let me synthesize everything into the final review.

## Summary
2-3 sentence summary of the paper's contribution.

IRIS proposes using negative self-certainty (NSC) — the KL divergence from the model's output distribution to a uniform distribution — as an intrinsic reward for fine-tuning autoregressive text-to-image models via GRPO. The key discovery is that minimizing self-certainty (maximizing uncertainty) improves T2I generation, directly contradicting findings from text-domain reasoning where maximizing self-certainty is beneficial. On Janus-Pro models, IRIS achieves results within one standard deviation of an external-reward baseline (T2I-R1) despite using no human labels, domain-specific verifiers, or any external feedback.

## Strengths

- **Reveals a task-dependent asymmetry in self-certainty's role.** The paper provides controlled quantitative evidence (Figure 2) that during RL alignment with external rewards, text-token self-certainty rises for LLM math reasoning (Qwen2.5-1.5B) while image-token self-certainty falls for T2I generation (Janus-Pro-1B). This is a genuinely interesting and non-obvious finding that documents a real difference between modalities.

- **Clean method that achieves competitive results with zero external supervision.** Table 1 shows that IRIS on Janus-Pro-1B attains GenEval 0.72 (vs. T2I-R1 external-reward baseline 0.75), T2I-CompBench complex 0.3793 (vs. 0.3820), and WISE 0.37 (vs. 0.38) — all within one standard deviation. This is the first demonstration that autoregressive T2I models can be improved via RL using only an intrinsic signal, with no reliance on human preference data or domain-specific verifiers.

- **Systematic ablations that isolate design choices.** Figures 5–9 provide four controlled ablation experiments: CoT usage, direction of SC optimization for image tokens, direction of SC optimization for text tokens, forward vs. backward KL, and RL vs. direct gradient optimization. Each ablation is evaluated on four independent reward models (HPSv2, GIT, GDino, ORM), making the conclusions robust to the choice of metric.

- **Transparency about an implementation inconsistency in the baseline.** Section 4.1 explicitly identifies that the official T2I-R1 codebase uses the wrong chat template (Janus instead of Janus-Pro) and corrects it, which strengthens reproducibility and prevents unfair comparisons.

## Weaknesses

### Fatal
None.

### Major

- **Single model family tested; claims of architecture agnosticism are unsupported.** The method is demonstrated only on Janus-Pro (1B and 7B). The paper states that IRIS "is agnostic to the model architecture or dataset" (Sec. 3, near Eq. 2) and "can be easily adapted to any scenario" (Sec. 4.2), but no evidence from other autoregressive T2I architectures (e.g., Show-o, VILA-U) is provided. While Janus-Pro is a reasonable choice, the breadth of the claim is not matched by the breadth of the evidence.

- **Training horizon is limited to 800 steps with no convergence evidence.** The main results (Table 1) report the best checkpoint among 100–800 steps. The learning curves (Figure 3) are still rising at 800 steps, and the ablation curves (Figures 5–9) also show upward trends. It is unclear whether performance continues to improve, plateaus, or eventually degrades with longer training. Longer runs (e.g., 2000+ steps) or evidence of convergence would significantly strengthen confidence in the method's robustness.

### Minor

- **The core perceptual claim ("visually rich and colorful images") is supported only indirectly.** The paper's qualitative narrative emphasizes that minimizing self-certainty produces images that are "more visually rich and colorful" and "better aligned with human preferences." However, the evaluation relies on automated benchmarks (GenEval, T2I-CompBench, WISE) that primarily test compositional accuracy and object presence — not visual richness or aesthetic quality per se. HPSv2 partially addresses this as a human-preference proxy for aesthetics, but a controlled human evaluation comparing IRIS, the base model, and the external-reward baseline on visual richness would directly validate the motivating intuition. The qualitative examples in Figure 1 are suggestive but not definitive.

- **Ablation evaluation uses a different protocol than the main benchmarks.** The ablation studies (Figures 5–9) evaluate on four external reward models (HPSv2, GIT, GDino, ORM) rather than on the standard benchmarks (GenEval, T2I-CompBench, WISE) used in the main results. While this is a reasonable choice given the expense of running full benchmark evaluations for every ablation, using the same benchmarks for at least one key ablation (e.g., minimizing vs. maximizing image SC) would make the narrative tighter.

- **Base model standard deviations are not reported.** In Table 1, standard deviations are given only for the RL-finetuned models (IRIS and T2I-R1) but not for base model variants. Including variances for base models would allow proper statistical comparison.

- **CoT diversity is not directly measured.** The paper argues that minimizing text-token self-certainty encourages diverse semantic CoTs but never measures CoT diversity (lexical diversity, length variation, semantic variation). Adding this analysis would strengthen the connection between the intrinsic reward and the claimed exploration benefit.

### Trivial
None.

## Nice-to-Haves
- Testing on an additional autoregressive T2I architecture (Show-o, VILA-U) would significantly strengthen generality claims.
- A controlled human preference study comparing IRIS, base model, and T2I-R1 on dimensions of visual richness, diversity, and overall preference would directly validate the core perceptual intuition.
- Longer training runs (2000+ steps) with convergence analysis would improve confidence in the method's stability.
- Reporting the original T2I-R1 numbers alongside the corrected ones would give readers a sense of how much the chat-template bug affected results.

## Removed Points
- **Weakness about missing human evaluation for the core claim**: This was partially retained as a Minor weakness (see above). The removed portion is the framing that this is a "critical issue" — the paper's benchmarks do measure meaningful aspects of image quality, and the claim about "visual richness" is supported by qualitative examples. The absence of a formal human study is a limitation but not a critical flaw, as the paper's main contribution (intrinsic reward achieving competitive performance) is evaluated through standard benchmarks.
- **Weakness about "training duration limited to 800 steps" inflated as a fatal flaw**: Retained as Major (not fatal). The best-checkpoint reporting is symmetric between IRIS and the baseline, so comparisons are fair. The issue is that the method's long-term stability is unknown.
- **Criticism about statistical significance of sub-score comparisons**: Removed — the paper does not claim statistical significance for these sub-scores, and most are within error bars. The paper's main claims are supported by aggregate scores.
- **Criticism about ablation evaluation metrics differing from main results**: Moved to Minor (above). This is a presentation choice, not a flaw in the experiment design.
- **Generic request for "simpler baselines" like entropy bonus during SFT**: Removed — this is not standard practice in this setting and would constitute a new method requiring its own justification.
- **General nitpicks about formatting, typos, or missing appendix content**: These are parser artifacts, not author errors.
- **Strength about identifying the T2I-R1 chat template issue**: Retained — this is a genuine strength showing methodological care.

## Novel Insights
Beyond the paper's own contributions, a genuinely novel synthesis from the reviews is that the self-certainty direction reversal (maximize for text, minimize for images) may reflect a deeper principle: tasks requiring objective precision (math, code) benefit from low-entropy, high-certainty output distributions, while tasks requiring perceptual richness and subjective quality (image generation) benefit from high-entropy, lower-certainty distributions that explore a wider range of plausible outputs. This suggests that "certainty" is not a universally desirable property in generative models — its role depends on whether the task demands convergent reasoning or divergent generation. The paper's Figure 2 provides rare empirical documentation of this divergence occurring during the same training procedure (GRPO) on different modalities, which is a genuinely useful data point for the field.

## Suggestions
- Add a controlled human evaluation comparing IRIS, base model, and T2I-R1 on visual richness, diversity, and preference.
- Run training for at least 2000 steps and report both best-checkpoint and final-checkpoint scores.
- Test on at least one additional autoregressive T2I architecture (e.g., Show-o) to support the claim of architecture agnosticism.
- Report standard deviations for base model evaluations in Table 1.
- Directly measure CoT diversity (e.g., lexical diversity, n-gram overlap, semantic variation) to substantiate the exploration narrative.

## Score and Decision

**Round 1 (Bracketing):** Searched across score bands for papers on RL for T2I generation with intrinsic rewards. Weak anchors (scores 3.0–3.4) were rejected papers on basic T2I fine-tuning or data augmentation — clearly inferior to IRIS. Middle anchors (scores 5.0–6.8) included Mitigating Object Hallucination with Human-Free RL (5.00, rejected), Confidence-aware Reward Optimization for T2I (6.00, accepted), IterComp (6.80, accepted), and Test-Time Adaptation with CLIP Reward (6.67, accepted). Strong anchors (scores 7.5+) were large-scale multi-modal training papers (Transfusion 7.60, IC-Light 10.00) — a different class of contribution. This placed the bracket at roughly **5.5–7.0**.

**Round 2 (Narrowing):** Searched within (5.5, 7.5) for more topically relevant anchors. Retrieved Adding Conditional Control to Diffusion Models with RL (6.50, accepted), FiSAO: Fine-Grained Self-Alignment (6.20, accepted), and Motif: Intrinsic Motivation from AI Feedback (7.25, accepted). 

- Compared to FiSAO (6.20): IRIS has a more novel core finding and cleaner experimental design.
- Compared to Adding Conditional Control (6.50): Similar quality — both have clear methods with somewhat limited evaluation breadth.
- Compared to Motif (7.25): Motif has more extensive ablations and a more surprising result (intrinsic-only outperforming extrinsic), but operates in a different domain (game-playing).

IRIS is stronger than the 6.20 anchor and comparable to the 6.50 anchor, with a more novel core finding than either. The single-architecture limitation and short training horizon prevent it from reaching the 7.0+ range. **Final score: 6.5**.

**Anchor summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| oOa3ZCtMjJ (GAN+CLIP T2I) | 3.00 | R1 | Much weaker — basic T2I method |
| TJHB4ySVZM (Data Extrapolation T2I) | 3.40 | R1 | Much weaker — limited scope |
| bO31lfEdos (Human-free RL for hallucination) | 5.00 | R1 | Weaker — single model, less novel insight |
| Let8OMe20n (Confidence-aware Reward Optimization) | 6.00 | R1/2 | Comparable — similar novelty but IRIS has more surprising finding |
| kIP0duasBb (Test-Time Adaptation with CLIP Reward) | 6.67 | R1/2 | Slightly stronger — broader task evaluation |
| 4w99NAikOE (IterComp) | 6.80 | R1/2 | Comparable — different strengths (broader evaluation vs. cleaner novelty) |
| cJQ1K2fjpD (FiSAO: Fine-Grained Self-Alignment) | 6.20 | R2 | Slightly weaker — methodology concerns, less novel |
| svp1EBA6hA (Adding Conditional Control with RL) | 6.50 | R2 | Similar — clear method, comparable evaluation scope |
| tmBKIecDE9 (Motif: Intrinsic Motivation from AI) | 7.25 | R2 | Stronger — more extensive evaluation and ablations |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
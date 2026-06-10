Now I have enough calibration data. Let me finalize the review.

**Round 1 bracket**: Based on comparison with anchors at 3.40, 5.00, 5.75, 6.00, 6.67, 6.80, 7.33 — the IRIS paper is clearly stronger than the reject papers (3.40-5.75) and comparable to the lower-accept papers (6.00-6.67). Bracket: **5.5–7.0**.

**Round 2 narrowing**: Comparing more closely:
- **vs. RLC (6.00, Accept)**: IRIS has a more novel insight (modality-dependent self-certainty), more comprehensive ablations (5 systematic studies), and more diverse benchmarks (3 vs. a few). IRIS is clearly stronger.
- **vs. Test-Time Adaptation with CLIP Reward (6.67, Accept)**: Both propose RL-based frameworks eliminating expensive supervision. IRIS has a deeper insight (counterintuitive observation about self-certainty modality-dependence) and more thorough ablations, but the overclaiming in the abstract and the ablation metric bias are notable weaknesses. Roughly comparable, maybe slightly weaker.
- **vs. IterComp (6.80, Accept)**: IterComp has stronger overall empirical results and fewer framing issues. IRIS is slightly weaker.

**Final position**: 6.5 — stronger than the 6.00 anchor (more novel, more ablations) but slightly below the 6.67 anchor due to overclaiming and ablation metric bias.

## Summary
The paper proposes IRIS, a reinforcement learning framework using Negative Self-Certainty (NSC) — the negative KL divergence between the model's output distribution and a uniform distribution — as an intrinsic reward to fine-tune autoregressive text-to-image models. The central counterintuitive finding is that, unlike language reasoning where maximizing self-certainty helps, T2I generation benefits from minimizing self-certainty. Applied to Janus-Pro (1B and 7B), IRIS is evaluated on GenEval, T2I-CompBench, and WISE against T2I-R1, which uses four external reward models.

## Strengths
- **Genuinely novel counterintuitive observation with multi-faceted evidence:** The paper provides qualitative evidence (Fig. 1: self-certainty RL produces uniform/dull images while negative self-certainty produces richer images), quantitative evidence (Fig. 2: external reward training decreases image self-certainty in Janus-Pro but increases text self-certainty in Qwen2.5), and direct ablation evidence (Fig. 6: maximizing image self-certainty causes rapid performance drop). This modality-dependent finding distinguishes the work from prior intrinsic-reward methods (Zhao et al., 2025b; Zhang et al., 2025a) that uniformly maximize self-certainty.
- **Comprehensive and well-designed ablation studies:** Section 4.3 systematically tests five design alternatives — with/without CoTs (Fig. 5), maximize vs. minimize image SC (Fig. 6), maximize vs. minimize text SC (Fig. 7), forward vs. backward KL (Fig. 8), and RL-based vs. direct gradient optimization (Fig. 9). Each ablation isolates one design variable and consistently supports the proposed configuration. The RL vs. direct optimization ablation (Fig. 9) is particularly valuable, showing that direct NSC optimization causes model collapse while GRPO remains stable.
- **Identified and corrected a concrete implementation error in the baseline:** Section 4.1 identifies that Jiang et al. (2025) used incorrect chat template keys for Janus-Pro (Janus-style "User"/"Assistant" instead of Janus-Pro-style "<User>"/"</Assistant>"), correcting this for fair comparison.
- **Meaningful performance gap closure without any external supervision:** While IRIS does not match T2I-R1 on overall scores, it recovers most of the gains from expensive external reward pipelines at zero cost. On specific sub-tasks (Position on GenEval 1B: 0.66 vs 0.64; Physics on WISE 1B: 0.45 vs 0.43), IRIS matches or exceeds T2I-R1, and the fine-grained analysis (Section 4.2) showing IRIS excels where external rewards lack domain knowledge (e.g., natural science in WISE) substantiates the generalization argument.

## Weaknesses

### Fatal
None

### Major
- **Overclaiming in abstract and framing relative to empirical evidence:** The abstract states IRIS "achieves performance that is competitive with or superior to external rewards." Table 1 shows IRIS underperforms T2I-R1 on *every* overall benchmark score: GenEval 1B 0.72 vs 0.75 (7B: 0.77 vs 0.78); WISE 1B 0.37 vs 0.38 (7B: 0.48 vs 0.50); T2I-CompBench 1B and 7B also generally favor T2I-R1. The improvement figures cited in the abstract (9.1%, 13.3%, 28.8%) and Section 4.2 are relative to the *untrained base model*, not to T2I-R1. The conclusion's claim of "even better results in the initial learning" cherry-picks a transient training phase rather than reporting final performance. This matters because the paper's value proposition is replacing external rewards with intrinsic rewards. If IRIS consistently underperforms external rewards overall, the contribution is better characterized as demonstrating that a zero-cost intrinsic signal recovers *most* of the gains — a meaningful but weaker claim that should be made honestly.

- **Ablation evaluation uses T2I-R1's own training rewards as proxy metrics:** Section 4.3 evaluates all ablations using HPSv2, DINO, ORM, and GIT — the exact four reward models used to train the T2I-R1 baseline. The paper acknowledges this ("we never use these reward models in the training objectives, so they can be simple and unbiased metrics"), but these metrics are inherently optimized for specific image properties (aesthetic appeal via HPSv2, object detection via DINO, VQA alignment via GIT/ORM) that T2I-R1 was trained to produce. This creates a systematic bias: IRIS's ablation improvements may reflect alignment with T2I-R1's optimization targets rather than genuine image quality. The ablation conclusions are likely directionally correct, but the metric choice undermines independent verification.

### Minor
- **Causal mechanism asserted but not fully disentangled:** The paper argues (a) external reward training decreases image self-certainty (Fig. 2), (b) low-self-certainty models generate richer images (Fig. 1), therefore (c) directly minimizing self-certainty should improve generation. The self-certainty decrease could be a side effect of optimization toward specific image properties rather than the active ingredient — direct NSC minimization might succeed for different reasons (e.g., preventing mode collapse in image token space). The ablations (Figs. 6-9) provide stronger direct evidence that NSC itself is key, partially addressing this, but the paper could strengthen its conceptual contribution by analyzing the mechanism more deeply.

- **"Agnostic to model architecture or dataset" claim is unvalidated:** The abstract states IRIS is "agnostic to the model architecture or dataset," but experiments are conducted only on Janus-Pro. Section 4.4 appropriately acknowledges this limitation, but the abstract frames it as a demonstrated property rather than a hypothesis.

- **No human evaluation despite acknowledging subjectivity:** The introduction states "the quality of a visual output is inherently subjective," yet no human evaluation is reported. While automated benchmarks are standard in T2I research, the gap between automated metrics and human preference is especially relevant for a method claiming to align better with human preferences.

- **No compute fairness analysis:** IRIS generates 8 text strings per query with 1 image each during GRPO. The paper does not compare compute budgets between IRIS and T2I-R1 training. Since IRIS's advantage is supposedly eliminating external reward model costs, an efficiency analysis would strengthen the practical contribution.

## Nice-to-Haves
- Analysis of failure modes: when does NSC minimization lead to degenerate images? What happens with extended RL training beyond 800 steps?
- Deeper analysis of what happens to CoT text distributions under NSC vs. SC training (the paper acknowledges the tension at lines 103-104 but does not investigate further)
- Investigation of whether NSC training specifically reduces mode collapse in image token distributions

## Removed Points
These points are flagged to be removed, treat them with caution.
- The harsh critic's original framing of "the causal mechanism connecting self-certainty to image quality is asserted, not established" was overstated — the paper provides ablation evidence beyond mere correlation (Figs. 6-9), and the critic framed it as purely correlational when it is not. Demoted to minor.
- Any concerns about formatting, typos, or parser artifacts — not author errors.
- Concerns about missing appendix content — stripped by parser, exists in original submission.

## Novel Insights
The paper's most novel insight is the modality-dependent behavior of self-certainty: maximizing it helps language reasoning but hurts image generation. This is supported by Fig. 2 (quantitative tracking during external reward training), Fig. 1 (qualitative comparison), and the ablation studies. The practical consequence — that this observation enables external-reward-free T2I training — is genuinely valuable, especially given the demonstration that IRIS recovers most of the external-reward gains at zero cost. The fine-grained analysis showing IRIS excels on tasks where external rewards lack domain knowledge (natural science in WISE) while T2I-R1 excels on tasks matching its reward models (aesthetics, spatial relations) provides a nuanced and insightful understanding of when intrinsic vs. extrinsic rewards are preferable.

## Suggestions
- Reframe the abstract and conclusion honestly: position IRIS as demonstrating that a zero-cost intrinsic signal can recover most of the gains from expensive external reward pipelines, which is practically significant.
- Add a compute/efficiency analysis comparing IRIS and T2I-R1 to quantify the practical advantage.
- Investigate the mechanism: analyze image token distribution entropy/mode structure under NSC training to understand why minimizing self-certainty helps.
- Consider evaluating ablations on at least one metric not aligned with T2I-R1's training objectives to strengthen the independence of the ablation evidence.

## Calibration Report

**Anchors retrieved:**
| Round | Paper | Avg Score | Comparison |
|-------|-------|-----------|------------|
| 1 | Data Extrapolation for T2I (TJHB4ySVZM) | 3.40 | Weak — poor motivation, IRIS clearly stronger |
| 1 | GAN+CLIP Text-to-Image (oOa3ZCtMjJ) | 3.00 | Weak — rough method combination, IRIS clearly stronger |
| 1 | Knowledge Enhanced Image Captioning (ZVOGMy8Sd8) | 3.00 | Weak — domain-specific, IRIS clearly stronger |
| 1 | Innate-Values RL (XHvguNJRbE) | 2.50 | Weak — loosely related, IRIS clearly stronger |
| 1 | Test-Time Adaptation with CLIP Reward (kIP0duasBb) | 6.67 | Strong anchor — novel RL framework, multiple tasks. IRIS has deeper insight but more overclaiming. Comparable. |
| 1 | Mitigating Object Hallucination (bO31lfEdos) | 5.00 | Middle — only one model, weaker motivation. IRIS stronger. |
| 1 | Explainable Concept Generation (9fMNxWDZsP) | 5.50 | Middle — RL preference learning, IRIS comparable or stronger |
| 1 | IterComp (4w99NAikOE) | 6.80 | Strong anchor — iterative composition T2I, strong results. IRIS slightly weaker overall. |
| 1 | Transfusion (SI2hI0frk6) | 7.60 | Very strong — major architecture paper, IRIS clearly weaker |
| 1 | CLIP Interpretation (5Ca9sSzuDp) | 8.00 | Very strong — IRIS clearly weaker |
| 1 | Compositional Entailment Learning (3i13Gev2hV) | 8.00 | Very strong — IRIS clearly weaker |
| 1 | Würstchen (gU58d5QeGv) | 8.00 | Very strong — IRIS clearly weaker |
| 2 | Learning to Reason at Pre-Training (BGnm7Lo8oW) | 5.50 | Middle — IRIS stronger (more novel insight, better ablations) |
| 2 | RLC: LM Self-Improvement (38E4yUbrgr) | 6.00 | Middle — unsupervised LM improvement, limited novelty. IRIS stronger. |
| 2 | LLMs Not Strong Abstract Reasoners (28gMnEAgl9) | 5.33 | Middle — analysis paper, different genre |
| 2 | Sequential Decision Making with LLMs (vodsIF3o7N) | 5.50 | Middle — IRIS comparable |
| 2 | Scaling Autoregressive T2I (jQP5o1VAVc) | 5.75 | Middle — scaling study, IRIS slightly stronger (more novel insight) |
| 2 | DnD-Transformer (wryFCrWB0A) | 6.20 | Middle — AR image generation, IRIS comparable |
| 2 | Reliable Random Seeds for T2I (5BSlakturs) | 7.33 | Strong — IRIS slightly weaker |

**Bracket and positioning:** Round 1 bracket: 5.5–7.0. Round 2 narrowed to 6.0–7.0. IRIS is clearly stronger than the 5.5–6.0 anchors (more novel insight, better ablations, more diverse benchmarks) but slightly below the 6.67 anchor due to overclaiming and ablation metric bias. Final score positioned at 6.5, between the 6.00 RLC anchor (IRIS is stronger) and the 6.67 CLIP-Reward anchor (IRIS is comparable but with more framing issues).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
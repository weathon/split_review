Now let me do the calibration analysis and finalize my review.

**Round 1 Bracket**: After examining anchors from low (<3.5), middle (3.5–7.5), and high (>7.5) bands, I place the paper in the **5.5–7.0** range. It is clearly stronger than the low-band papers (avg 3.0–3.4, rejected) and weaker than the top-band papers (avg 7.6+, accepted with very high scores like Transfusion and IC-Light).

**Round 2 Narrowing**: The paper compares well with mid-band anchors:
- **Let8OMe20n** (6.0, accepted): Confidence-aware Reward Optimization for T2I — similar domain but IRIS has a more novel finding (opposite SC behavior) and cleaner ablations.
- **Ugs2W5XFFo** (6.0, accepted): Information Theoretic T2I Alignment — both are self-supervised alignment methods, IRIS has stronger ablations.
- **yMHe9SRvxk** (6.0, accepted): Human-Feedback Efficient RL for Online Diffusion — IRIS is cleaner (zero external signal needed vs. this requires online human labels).
- **kIP0duasBb** (6.67, accepted): Test-Time Adaptation with CLIP Reward — tested across 3 distinct tasks, slightly more comprehensive evaluation.

**Final placement**: The paper is a solid 6.0. It has a genuinely novel finding (SC behaves oppositely in T2I vs text), strong ablations, and convincing results — but is limited to one model architecture and has some unaddressed questions about mechanism.

---

## Summary

This paper proposes IRIS, a reinforcement learning framework that fine-tunes autoregressive text-to-image models using *negative self-certainty* (NSC) — a purely intrinsic reward signal — requiring no human-labeled data, no external verifiers, and no reward models. The key insight is that, contrary to text reasoning domains where maximizing self-certainty helps, minimizing self-certainty improves T2I generation by encouraging the model to produce more visually rich and diverse outputs. The method is evaluated on Janus-Pro 1B and 7B models across three benchmarks (GenEval, T2I-CompBench, WISE), achieving performance competitive with external-reward-based training (T2I-R1). Extensive ablations isolate the contributions of the key design choices.

## Strengths

- **Novel finding that self-certainty exhibits opposite behaviors in T2I vs. text reasoning**: The paper provides quantitative evidence (Figure 2) that RL alignment with external rewards increases text self-certainty in an LLM (Qwen2.5) while decreasing image self-certainty in a multimodal LLM (Janus-Pro), and demonstrates causally via ablations that minimizing SC improves T2I. This is a genuinely interesting and non-obvious result that contrasts directly with recent text-domain findings (Zhao et al., Zhang et al.).

- **Competitive performance without any external supervision**: IRIS achieves scores within 1–3% of the external-reward baseline (T2I-R1) on all three benchmarks for both 1B and 7B models (Table 1) — despite using no human labels, domain-specific verifiers, or external reward models. For example, on Janus-Pro-1B: GenEval 0.72±0.01 vs. 0.75±0.01, WISE 0.37±0.01 vs. 0.38±0.01.

- **Systematic and informative ablation studies**: Five ablation experiments (Figures 5–9) convincingly justify each design choice: (1) CoT helps more than no CoT, (2) minimizing image SC outperforms maximizing it (which collapses), (3) minimizing text SC outperforms maximizing it, (4) forward KL (self-certainty) outperforms backward KL (entropy), and (5) the RL framework is necessary — direct NSC optimization collapses. These are evaluated using four independent external reward models never seen during IRIS training.

- **Correction of a chat-template inconsistency in the T2I-R1 baseline**: The paper identifies that prior work used the wrong chat template for Janus-Pro models, and corrects it for fair comparison.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims.

### Minor
- **Single model architecture limits generality claims**: The paper tests only Janus-Pro (an autoregressive multimodal LLM). While the authors acknowledge this in Section 4.4 and frame future work, the title and abstract assert that the method is "agnostic to the model architecture or dataset." Without testing on even one additional autoregressive T2I model (e.g., Show-o, VILA-U) or a different-scale Janus variant, this generality claim is asserted rather than demonstrated. The paper would be stronger with a second architecture, even in a small-scale experiment.

- **Length/diversity confound in the CoT vs. no-CoT ablation is not fully resolved**: The ablation in Figure 5 shows that training *with* CoT outperforms training *without* CoT. The GRPO objective already includes per-sequence length normalization ($\frac{1}{|o_i|}$) and advantage normalization is within-group, so the comparison is not confounded in the way a naive reading might suggest. However, the *mechanism* of improvement remains unclear: does CoT help because it enables diverse semantic exploration, or simply because more tokens per sequence give more gradient signal per step? The paper would benefit from analyzing whether the generated CoTs become objectively more diverse (e.g., lexical diversity metrics, length distribution) and whether this diversity correlates with image quality improvements.

- **Limited training horizon and convergence analysis**: All results use 800 training steps with effective batch size 8. The learning curves in Figure 3 are still rising or plateauing at 800 steps. The ablation in Figure 9 shows direct NSC optimization collapses after ~200 steps. There is no evidence that IRIS remains stable for longer training or at larger effective batch sizes.

- **Ablation studies lack variance reporting**: Main results in Table 1 report standard deviations (over evaluation samples, but the paper does not clarify whether these are over seeds or evaluation samples), while the ablation studies (Figures 5–9) report no variance at all. Multiple training seeds per condition would improve statistical credibility.

- **Group size not ablated**: The GRPO group size is fixed at G=8 without ablation or discussion of its impact. This matters because the advantage estimate depends entirely on within-group variance, and the small group size could lead to high-variance advantage estimates.

### Trivial
- The paper does not report computational cost (GPU hours) of IRIS versus T2I-R1, which would strengthen the practical motivation since IRIS avoids running external reward models during training.

## Nice-to-Haves
- A small experiment on a second autoregressive T2I architecture (e.g., Show-o or VILA-U) would significantly strengthen the generality claim.
- A sensitivity analysis of group size G and KL coefficient β would increase confidence in the method's robustness.
- Analysis of whether learned CoTs become more lexically diverse, and whether this diversity mediates the image quality improvements, would clarify the mechanism.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **Critic's claim about length confound in CoT vs. no-CoT comparison being a confound in the GRPO objective**: The critic argues that "the paper does not control for sequence length" and that "longer sequences naturally produce larger-magnitude rewards." However, the GRPO objective (Eq. 3) already includes $\frac{1}{|o_i|}$ normalization per sequence, and advantage normalization is within-group (separate groups per condition), so no cross-condition length bias exists in the objective. The kernel of truth (mechanism unclear) is retained as a Minor weakness.
- **Critic's point about missing details on Qwen experiment (Appx B.1)**: The paper states details are in Appendix B.1, which was stripped by the parser. This is a parser artifact, not the authors' omission.
- **Critic's speculation about reward hacking with no evidence**: The critic says "could the model learn to 'tuple'...?" without any evidence this occurs. The paper already shows RL prevents collapse.
- **Critic's request for "original T2I-R1 numbers" as reference**: The paper corrects a bug in T2I-R1's template; reporting buggy numbers as a baseline would be misleading.
- **Strength Finder's generic strengths about problem importance**: These are not specific to this paper's contribution.

## Novel Insights

The reviews highlight an interesting tension: the paper claims CoT enables "diverse semantic exploration" as the mechanism, but the no-CoT ablation does not fully isolate length effects from diversity effects because the two conditions differ in both the presence of text tokens and total sequence length. A genuinely useful follow-up would be to train IRIS with length-matched conditions — e.g., forcing the model to generate filler text of controlled length before image tokens — to disentangle whether the benefit is from exploration in CoT space or simply from longer rollouts providing more statistical signal per step. The reviews collectively suggest that the paper's ablations are its strongest asset, but they would be even stronger if they reported per-condition variance and controlled for the CoT length confound.

## Suggestions

- Add a length-controlled ablation: train IRIS with CoT but normalize the per-sequence NSC sum by sequence length in the advantage computation, or pad shorter CoTs to a fixed length, to test whether benefit comes from diverse exploration versus longer sequences.
- Test on at least one additional autoregressive T2I model (e.g., Show-o) to substantiate the generality claim.
- Report ablations with standard deviations over at least 3 training seeds.
- Ablate the GRPO group size G (e.g., G=4, 8, 16) and KL coefficient β.
- Report GPU hours and discuss the computational advantage of avoiding external reward models during training.

## Score and Decision

<score>6.0</score>
<decision>Accept</decision>
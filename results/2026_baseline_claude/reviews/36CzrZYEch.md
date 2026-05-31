## Summary

IRIS (Intrinsic Reward Image Synthesis) proposes to fine-tune autoregressive text-to-image (T2I) models using Negative Self-Certainty (NSC) — the KL divergence from uniform distribution, negated — as an intrinsic RL reward, requiring no external reward models, human labels, or domain-specific verifiers. The paper's central empirical observation is that, contrary to text reasoning where maximizing self-certainty helps, minimizing self-certainty benefits T2I generation by encouraging visually richer and more diverse images. The method applies GRPO with NSC rewards over both text (semantic CoT) and image tokens in Janus-Pro models, achieving results competitive with T2I-R1, which uses four specialized external reward models.

---

## Strengths

- **Novel and empirically grounded cross-modal insight.** The observation that self-certainty evolves in opposite directions when external rewards are applied to text reasoning (increases) vs. T2I generation (decreases) — Fig. 2 — is non-obvious and well-substantiated. The paper corroborates it through qualitative examples (Fig. 1), quantitative training curves (Fig. 2), and ablation (Figs. 6–7), forming a coherent empirical story.

- **Practically significant reward-free training.** IRIS achieves results comparable to T2I-R1 (which requires HPSv2, GroundingDINO, GIT, and ORM) without any external supervision. On WISE-1B and several subcategories of T2I-CompBench-1B, differences are within error bars. This is a meaningful practical contribution given the cost and brittleness of external reward models.

- **Thorough ablation study.** Four targeted ablations — CoT vs. no-CoT (Fig. 5), minimizing vs. maximizing image self-certainty (Fig. 6), minimizing vs. maximizing text self-certainty (Fig. 7), forward vs. backward KL (Fig. 8), RL vs. direct NSC optimization (Fig. 9) — each with four evaluation metrics, provide solid justification for every design decision.

- **Methodological transparency about baseline inconsistency.** The paper identifies and corrects an incorrect chat template used in the official T2I-R1 implementation when applied to Janus-Pro, and retrains all baselines correctly. This is a careful and honest contribution to reproducibility.

---

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency between Figure 3 and Table 1.** The alt-text/caption for Fig. 3 asserts that "IRIS with CoT achieves higher scores than T2I-R1 (external) after approximately 200 training steps" on all three benchmarks for the 1B model. Yet Table 1 shows IRIS-1B at 0.72 ± 0.01 vs. T2I-R1-1B at 0.75 ± 0.01 on GenEval — a gap of three standard deviations in favor of T2I-R1. If Table 1 reports the best checkpoint, Figure 3 should not show IRIS consistently above T2I-R1 on GenEval unless the trajectories cross and the T2I-R1 peak falls outside the plotted range. This apparent contradiction, central to the paper's main claim of being competitive, is unresolved in the text.

2. **Performance gap is larger than "competitive" framing suggests.** On the most well-known benchmark (GenEval 1B), IRIS (0.72) falls significantly behind T2I-R1 (0.75). On T2I-CompBench 7B, T2I-R1 (0.3992) outperforms IRIS (0.3916) by about twice the reported standard deviation. The abstract claims "competitive with or superior to external rewards," but IRIS only approaches parity on WISE, which is the newest and arguably least validated of the three benchmarks. The framing should be more precise about where IRIS genuinely competes and where it lags.

3. **Mechanistic explanation for why uncertainty improves image quality is shallow.** The paper observes that low-certainty models generate richer images, but the explanation ("overly confident models generate uniform and plain figures") is circular and phenomenological. It is unclear whether the NSC reward works because it (a) acts as a diversity-promoting regularizer preventing mode collapse, (b) discourages the model from mapping prompts to single prototypical images, or (c) has some deeper connection to the distributional structure of image tokens. Without at least a discussion of this mechanism, the insight is harder to generalize.

### Minor

1. **Single model architecture.** All experiments use Janus-Pro (autoregressive discrete-token LLM-style model). The paper acknowledges in Sec. 4.4 that diffusion, masked-modeling, and MAE-style T2I architectures are left for future work. Given how architecture-dependent the self-certainty measure is (requiring a discrete probability distribution over a vocabulary), the scope of the contribution should be stated more conservatively.

2. **Training is capped at 800 steps.** Both IRIS and T2I-R1 might not have converged; IRIS shows upward trends in some benchmarks at step 800. It is unclear whether longer training would close or widen the gap with T2I-R1.

3. **Semantic CoT contributes substantially but its interaction with NSC is not fully disentangled.** The ablation shows CoT helps (Fig. 5), but IRIS vs. T2I-R1 comparisons always include CoT in IRIS. It is unclear how much of the IRIS gain comes purely from the NSC reward versus the exploratory diversity introduced by the CoT procedure itself.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A detailed analysis of cases where IRIS underperforms T2I-R1 (e.g., counting, color attribution in GenEval; shape and 2D-spatial in T2I-CompBench) could strengthen the paper's understanding of when intrinsic rewards fall short.
- A longer training run (e.g., 2000 steps) would clarify whether the 800-step results are stable or transient.

---

## Novel Insights

The most genuinely novel insight is the empirical demonstration and quantification that self-certainty is task-dependent across modalities: reinforcement learning with external verifiable rewards consistently increases self-certainty in text LLMs (math/code) but decreases it in autoregressive T2I models. This suggests that image generation — even in discrete-token autoregressive models — is fundamentally different from next-token text prediction in terms of the optimal confidence regime. The corollary — that a negated self-certainty signal, requiring zero external supervision, can serve as an effective surrogate for rich external reward pipelines — challenges the assumption that reward-free RL must be inferior to reward-model-based RL in generation tasks. The observation also raises an interesting hypothesis about why the two modalities differ: visual semantics may demand ensemble-like token distributions while linguistic reasoning demands sharp, high-confidence commitments.

---

## Suggestions

- Clarify the apparent contradiction between Figure 3 (IRIS > T2I-R1 on GenEval 1B visually) and Table 1 (T2I-R1 best checkpoint = 0.75 vs IRIS = 0.72). If both methods' best checkpoints are shown in Fig. 3, explain which step each peaked at.
- Investigate whether the NSC reward's benefit persists when CoT is removed and match training conditions exactly to isolate the reward signal.
- Soften the claim of "competitive with or superior to" to be more precise: IRIS is clearly competitive on WISE, roughly comparable on T2I-CompBench, and lags on GenEval.
- Provide a short mechanistic discussion or hypothesis for why lower self-certainty benefits visual token generation (e.g., relating to the many-to-many nature of prompt-to-image mappings vs. the one-to-one nature of math solutions).

---

## Score and Decision

The paper makes a genuine and interesting empirical discovery — that self-certainty optimization has opposite effects in text reasoning and T2I generation — and builds a practically useful reward-free RL method around it. The ablation studies are solid and the methodological transparency is commendable. However, the performance advantage over T2I-R1 is mixed (IRIS trails clearly on GenEval, barely competes on others), there is a notable inconsistency between Figure 3 and Table 1, the mechanistic insight is underdeveloped, and the method is restricted to a single architecture class. These issues collectively put the paper in the borderline territory — above average for the venue but not a clear accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
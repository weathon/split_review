Now I have all the information needed to write the consolidated review. Let me synthesize.

---

## Summary

This paper proposes IRIS, the first reinforcement learning framework for autoregressive text-to-image (T2I) models that uses only an intrinsic reward signal — negative self-certainty (NSC) — without any human labels or external verifiers. The key insight is that, contrary to text reasoning where higher self-certainty is beneficial, lower self-certainty in image tokens correlates with richer, more diverse images preferred by humans. IRIS applies GRPO to maximize NSC on both text and image tokens, achieving competitive results with external-reward baselines on GenEval, T2I-CompBench, and WISE.

## Strengths

- **Novel and well-supported observation on self-certainty reversal**: The paper convincingly demonstrates through both qualitative (Figure 1) and quantitative (Figure 2) evidence that RL training with external rewards decreases image-token self-certainty in T2I models while increasing text-token self-certainty in reasoning models — a genuinely interesting finding that challenges assumptions carried over from the LLM literature.
- **Competitive performance with zero external supervision**: Table 1 and Figure 3 show IRIS achieves results close to T2I-R1 (which uses four external reward models) across three diverse benchmarks. On Janus-Pro-1B, IRIS reaches 0.72 vs. 0.75 on GenEval, 0.3793 vs. 0.3820 on T2I-CompBench, and 0.37 vs. 0.38 on WISE. The full training curves (Figure 3) show this holds across the entire training trajectory, not just at a single point.
- **Thorough and well-designed ablation studies**: Section 4.3 systematically isolates the contribution of each design choice: minimizing vs. maximizing self-certainty on text and image tokens (Figures 6–7), forward vs. backward KL (Figure 8), CoT vs. no CoT (Figure 5), and RL-based optimization vs. direct NSC maximization (Figure 9). These ablations cleanly validate the core claim that uncertainty is beneficial specifically for image generation.
- **Identification and correction of an evaluation bug in prior work**: The paper identifies that T2I-R1 used an incorrect chat template for Janus-Pro models (Section 4.1), correcting it for fair comparison — a valuable service to the community.

## Weaknesses

### Fatal

None.

### Major

- **Checkpoint selection conflated with test evaluation**: Table 1 reports "the best result of different methods among the checkpoints from 100 step to 800 step on the three benchmarks" and the table caption confirms selection by "average performance" across those same benchmarks. This means the test benchmarks (GenEval, T2I-CompBench, WISE) are used for model selection, which inflates reported scores relative to what a held-out protocol would produce. The full training curves in Figure 3 partially mitigate this concern — they show IRIS matching or exceeding T2I-R1 across most steps, not just at the cherry-picked best step — but the Table 1 numbers remain overestimates. The authors should either fix the checkpoint at a predetermined step (e.g., the final step at 800) or use a held-out prompt split for selection when reporting best-checkpoint numbers.

### Minor

- **Architectural generality is overstated**: The introduction claims IRIS is "agnostic to the model architecture or dataset," yet all experiments are conducted exclusively on Janus-Pro, an autoregressive discrete-token model. The self-certainty formulation (KL divergence over a discrete vocabulary) does not trivially transfer to continuous diffusion models. The Discussion section (4.4) partially walks this back by noting that adapting IRIS to other architectures "is an interesting direction for future research," but the claim in the introduction remains unsupported and should be appropriately qualified.

- **Missing control baseline for the RL training loop**: While the ablations compare different configurations of the NSC reward (direction on text vs. image tokens), none isolate the effect of the GRPO training loop itself from the reward signal. A baseline using the same GRPO setup with a constant or random reward would help determine whether the improvement stems from the specific NSC signal or from on-policy exploration and the KL constraint inherent in GRPO. The direct-optimization ablation (Figure 9) shows that RL is necessary, but does not show that NSC is better than any arbitrary reward.

- **No human evaluation for visual quality claims**: The paper's central narrative — that lower self-certainty yields "visually rich and colorful images" better aligned with human preferences — is supported only by automated benchmarks and proxy reward models. A small-scale human preference study or an evaluation using an orthogonal automated metric (e.g., LAION aesthetic score) would substantially strengthen the claim. This is particularly relevant since the paper argues IRIS outperforms external-reward methods specifically on categories where those external rewards are less relevant (e.g., natural science in WISE).

- **Limited quantitative analysis of CoT emergence**: The claim that intrinsic rewards alone can "guide the model to generate meaningful semantic CoTs" is supported by a single qualitative example (Figure 4). Quantitative metrics such as CoT length, lexical diversity, or relevance scores across training would strengthen this contribution.

### Trivial

- No explicit Limitations section. The Discussion (Section 4.4) touches on future work for other architectures but does not systematically discuss failure modes, when reducing confidence might hurt, or potential mode collapse risks.

## Nice-to-Haves

- A small-scale human preference study comparing IRIS vs. T2I-R1 outputs on a fixed set of diverse prompts would directly validate the qualitative claims.
- Quantitative analysis of CoT characteristics (diversity, length, relevance) across training steps.
- Discussion of failure modes: when does minimizing self-certainty hurt image quality, and how does the KL penalty to the reference model prevent degeneration?

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic claimed "the paper does not discuss a key subtlety: minimizing KL(U||π) pushes the model distribution towards uniform"** — REMOVED. The paper explicitly discusses this in Section 3.2: forward KL "encourages mode-covering behavior by rewarding probability distributions that cover multiple plausible outcomes," contrasted with entropy which is "mode-seeking," and the forward vs. backward KL is ablated in Figure 8. The paper addresses this concern.

- **Harsh Critic claimed the Figure 1 evidence is "only via a few cherry-picked examples"** — WEAKENED and moved. Figure 1 provides qualitative illustration; the quantitative evidence comes from Figures 2, 3, 6, 7, and the benchmark results. The qualitative examples supplement rather than constitute the primary evidence.

- **Strength Finder: "The method's simplicity and lack of external dependencies make it a scalable and general approach"** — Partially REMOVED as a standalone strength. While simplicity is a virtue, the scalability claim is undermined by the single-architecture evaluation (see Major weakness about architectural generality). The simplicity of the method is noted in the Summary but not listed as a standalone strength.

- **Harsh Critic: "post-hoc rationalisation of patterns in noisy per-category results without statistical tests"** — WEAKENED. The per-category discussion in Section 4.2 is interpretive rather than statistical, but the paper does not make strong causal claims from these patterns; it presents them as plausible explanations consistent with the reward design.

- **Harsh Critic: "The paper would need a substantially revised evaluation protocol to be considered for acceptance"** — WEAKENED. While the checkpoint selection issue is real (retained as Major), the full training curves in Figure 3 provide valid comparative evidence independent of the best-checkpoint selection, so the evaluation is not wholly invalidated.

## Novel Insights

The paper's most significant contribution is the empirical demonstration that self-certainty exhibits opposite behaviors across modalities: RL alignment increases self-certainty for text reasoning models but decreases it for image generation models. This task-dependent reversal has implications beyond this paper — it suggests that intrinsic reward design for multimodal models cannot simply port strategies from the LLM literature, and that different output modalities may require fundamentally different optimization signals. The finding that an intrinsic reward (NSC) alone, without any external verifier, can produce meaningful semantic chains-of-thought that improve image generation is also noteworthy and suggests underexplored connections between uncertainty-based exploration and emergent reasoning in generative models.

## Suggestions

- **Fix the checkpoint selection protocol**: The single highest-impact change: either (a) report results at a fixed step (e.g., step 800) with standard deviations across runs, or (b) hold out a subset of prompts as a validation set for checkpoint selection, keeping the test benchmarks untouched. This would make Table 1 credible without altering the core contribution.
- **Qualify the architectural generality claim**: Change "agnostic to the model architecture or dataset" to something like "designed to be adaptable across architectures" and explicitly note that the current empirical validation is limited to autoregressive discrete-token models.
- **Add a limitations subsection**: Discuss failure modes, the reliance on KL regularization to prevent mode collapse, and the open question of transferring NSC to continuous diffusion models.

## Score and Decision

**Round 1 bracketing**: Search across three bands placed the paper in the middle range (3.5–7.5), with relevant middle-band anchors at 5.00 (bO31lfEdos, human-free RL for hallucination), 6.00 (Let8OMe20n, confidence-aware reward for T2I; Y6KUBkUimC, RankDPO for T2I), and 6.20 (cJQ1K2fjpD, FiSAO self-alignment for VLMs). High-band anchors (7.5+) were clearly stronger papers (Transfusion, Würstchen). Low-band anchors were clearly weaker.

**Round 2 narrowing**: Anchors within 4.0–7.5. IRIS is clearly stronger than bO31lfEdos (5.00, Reject — limited scope, unclear motivation, output-shortening concerns) due to its novel insight and thorough ablations. IRIS is comparable to or slightly below cJQ1K2fjpD (6.20, Accept — similar self-alignment motivation but with theoretical analysis and multi-model testing). IRIS is comparable to Let8OMe20n (6.00, Accept — cleaner evaluation with human studies but more incremental contribution) and Y6KUBkUimC (6.00, Reject — stronger model coverage but mixed reviews on novelty).

The checkpoint selection issue pulls IRIS below the ~6.0 anchors, but the novel self-certainty reversal observation and thorough ablations keep it above the ~5.0 tier. **Final score: 5.5**.

**Anchor comparison summary**:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| bO31lfEdos (human-free RL hallucination) | 5.00 | R1/R2 | IRIS is stronger — more novel insight, better ablations, cleaner motivation |
| Y6KUBkUimC (RankDPO for T2I) | 6.00 | R2 | Comparable — RankDPO has broader model testing; IRIS has more fundamental insight but weaker evaluation |
| Let8OMe20n (confidence-aware reward T2I) | 6.00 | R1/R2 | Comparable — Let8OMe20n has human evaluation; IRIS has more novel observation but checkpoint issue |
| cJQ1K2fjpD (FiSAO self-alignment) | 6.20 | R2 | FiSAO slightly stronger — has theoretical analysis and multi-model testing |
| kIP0duasBb (CLIP reward TTA) | 6.67 | R1 | kIP0duasBb is stronger — well-evaluated across multiple tasks with cleaner methodology |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>
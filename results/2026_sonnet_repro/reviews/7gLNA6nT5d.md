Now I have a clear picture of the paper. Let me run calibration searches.Good. Let me read the two most topically similar anchors in detail.**Round 1 bracket: 4.5 – 6.0.** This paper is similar to 5iWim8KqBR (5.5, memory-efficient AD for ICRL, rejected) — both propose architectural improvements to AD on small grid environments with limited baselines, but the n-gram paper has clearer practical wins. It's below Pj06mxCXPl (6.67) which has theoretical backing.Now I have enough to write the final review. The paper sits between the memory-efficient AD paper (5.5, rejected) and the RA-DT paper (4.67, rejected). I'll place it at **5.0**.

---

## Summary

This paper proposes integrating n-gram induction heads (borrowed from Akyürek et al., 2024) into the Algorithm Distillation (AD) framework for in-context reinforcement learning. The core claim is that hard-coding n-gram attention patterns provides an inductive bias that reduces hyperparameter sensitivity and lowers the data requirements for in-context learning to emerge. Results are demonstrated on Dark Room, Key-to-Door (discrete 9×9 grids), and Miniworld (pixel-based 3D rooms), the last using vector quantization to enable n-gram matching over image observations.

---

## Strengths

1. **Consistent hyperparameter sensitivity reduction.** Across multiple experimental conditions in both Dark Room and Miniworld, the n-gram model reliably reaches near-optimal performance within ~15–20 random hyperparameter assignments, while the baseline requires 400+ (or fails to converge at all in low-data regimes). This is shown systematically in Figures 2, 4, 5, and 6, with the EMP metric correctly capturing the effect. The pattern is robust across the 1K/5K/10K learning-history axis and the 10/20/30-goal axis in Figure 2.

2. **Successful pixel extension via VQ.** Figure 5 shows the n-gram model significantly outperforming the baseline on Miniworld-Dark (30 goals) and Miniworld-Key-to-Door (300 goals), demonstrating that the n-gram mechanism is not restricted to discrete state spaces. The VQ pretraining pipeline (ResNet encoder-decoder → 4×4 codebook indices) is a non-trivial engineering contribution that makes the approach practically relevant for vision-based RL.

3. **N-gram hyperparameters are not brittle.** Table 1(a)–(b) show that varying n-gram length (1/2/3) and layer position ([1], [2], [1,2]) yields EMP values within overlapping confidence intervals (~0.67–0.76), supporting the claim that the added n-gram hyperparameters do not inflate the search problem.

4. **Graceful degradation under permuted masking.** Table 1(c) shows that randomly permuting the n-gram attention matrix (simulating total matching failure) recovers the same EMP as the no-n-gram baseline (0.51 ± 0.03 vs. 0.52 ± 0.02), confirming the architecture does not harm baseline performance when the mechanism fails.

---

## Weaknesses

### Fatal
None.

### Major

- **The headline 27x data-efficiency claim rests on a cross-paper comparison, not a controlled experiment.** The paper states: "for the baseline method to converge to a model with the same performance, it needs 2048 goals and 2048 learning histories [17]" (Figure 4 caption). This number comes from Laskin et al.'s original AD paper, trained under a different experimental protocol, different hyperparameter regime, and different evaluation methodology. There is no within-paper experiment in which AD is trained at 2048 goals under the authors' identical EMP protocol and compared against the n-gram model at 100 goals. Figure 1 does show within-paper head-to-head comparisons across training-goal counts (64–2048), and Figure 4 shows that the n-gram model works at 100 goals while the baseline fails under the authors' setup — these are real and meaningful results. But the "27x" multiplicative figure is not recoverable from the paper's own experiments. This inflates the headline contribution beyond what the evidence supports.

- **Only one baseline (the 2022 AD paper) is compared.** The Related Work section explicitly cites more recent ICRL methods that address the same problems — data efficiency (noise-curriculum data collection by Zisman et al. [33], data augmentation by Kirsch et al. [14]), and context efficiency (Retrieval-Augmented Decision Transformer by Schmied et al. [26]), plus Q-learning for offline ICRL (Tarasov et al. [28]). None of these are compared against. Notably, the paper *already uses* Zisman et al.'s oracle + decaying noise schedule as its own data collection pipeline for Miniworld; it is therefore unclear whether the Miniworld improvements stem from n-gram heads, the noise curriculum that generates the data, or their interaction. This is a validity concern, not a completeness concern.

### Minor

- **Small-environment scope limits generalizability.** All experiments use a 9×9 grid world (Dark Room, max 80 goals) or simple 3D rooms (Miniworld, 30–300 goals). The conclusion explicitly acknowledges XLand-Minigrid and Meta-World were not tested. In these toy environments, n-gram state matching is trivially effective — in a 9×9 grid, matching states amounts to matching grid positions, which repeat frequently in any exploratory trajectory. Whether n-gram heads continue to contribute in environments where state revisitation is rare or compositionally diverse is completely uncharacterized.

- **Figure 6 trains the two methods on different numbers of goals (50 n-gram vs. 60 baseline for Miniworld-Dark).** The caption acknowledges this is intentional, but presenting this as a head-to-head hyperparameter sensitivity comparison conflates architecture and data conditions. A cleaner comparison would hold goals fixed and vary architecture, then report data efficiency separately.

- **No mechanistic analysis of what the n-gram head attends to.** The state-only matching (matching grid positions) consistently outperforms full transition matching (matching action-reward-state tuples) throughout Figures 2 and 4, but this is left unexplained. Understanding why state matching dominates would clarify whether the n-gram head is learning a semantically useful pattern or simply acting as a structural regularizer.

### Trivial

- Table 1(c)'s permuted-mask experiment compares "permuted" vs. "baseline" (without n-gram), but does not include the working n-gram model in the same table, making the three-way comparison implicit rather than explicit.

---

## Nice-to-Haves

- A within-paper controlled data-efficiency sweep: train AD at 2048 goals under the authors' exact EMP protocol and compare to the n-gram model at 100 goals. This would make the 27x claim directly verifiable.
- A VQ quality sensitivity experiment (smaller codebook, reduced pretraining) to characterize how robust the pixel extension is to VQ failure modes, especially since Section 4.5's permuted-mask experiment addresses a related concern only partially.
- Even one comparison with a contemporary baseline (e.g., noise-curriculum-only AD without the n-gram modification, held out from the data pipeline) would substantially strengthen the positioning of the contribution.
- Attention visualizations for a well-trained n-gram model in Dark Room (showing it latching onto revisited grid positions) would provide mechanistic evidence for the claimed inductive bias.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh critic: "N-gram mechanism may find few matches in complex environments."** This is speculative and no experiment in the paper tests this regime. The paper explicitly scopes its claims to the tested environments and acknowledges the limitation in the conclusion. Removed as speculation beyond the paper's scope (though retained in Minor as a scope concern).

- **Strength finder: "Reduces total transitions by 27x compared to original AD."** Removed as a standalone strength because the 27x figure is a cross-paper comparison (flagged as a Major weakness). The within-paper improvement at 100 vs. 512 goals (Figure 1: return ~1.7 vs. ~1.6 at 128 goals for n-gram vs. baseline) is genuine but not 27x.

- **Strength finder: "Clearly bridges a gap between language-inspired induction heads and decision-making tasks."** Removed as too generic — there is no mechanistic demonstration in the paper of how the n-gram head improves credit assignment or temporal reasoning in RL beyond pattern matching.

- **Harsh critic: "Comparison against contemporary baselines is necessary for validity — missing works."** The rule prohibits citing missing related works; however, the specific comparison to Zisman et al. [33] is retained in Major because that paper is explicitly cited AND its pipeline is incorporated into this paper's own data collection, making the confound concrete and verifiable from the paper as written.

---

## Novel Insights

The most genuinely novel observation is methodological: by using EMP (Expected Maximum Performance) with a fixed gradient-step budget and random hyperparameter search, the paper provides a principled way to simultaneously evaluate maximum achievable performance and the hyperparameter sensitivity of a method. The finding that injecting a structural inductive bias (n-gram matching) reduces HP sensitivity — not just final performance — is a concrete and underexplored axis for evaluating architectural choices in ICRL. This framing, if applied more broadly with more baselines and larger environments, could be a substantive contribution to how architectural decisions in ICRL are evaluated.

---

## Suggestions

1. **Add a within-paper AD vs. n-gram sweep at 2048 goals under identical protocol.** This is the single highest-leverage fix; it would make the headline claim self-contained and verifiable.
2. **Run at least one contemporary baseline** (e.g., noise-curriculum-only AD, or Zisman et al.'s approach without n-gram heads on the same Miniworld setup) to disentangle the architecture contribution from the data collection pipeline.
3. **Include attention maps or n-gram match rate statistics** for a trained model on Dark Room to explain why state-only matching dominates over full-transition matching.
4. **Either hold training goals constant across all comparisons** or explicitly label goal-asymmetric comparisons as "data-efficiency" plots rather than "hyperparameter sensitivity" plots (Figure 6 conflates both).

---

## Score Calibration

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 5iWim8KqBR (Memory-Efficient AD for ICRL) | 5.50 | R1 | Most topically similar — also an architectural improvement to AD on grid worlds with no novel theoretical contribution and limited baselines. This paper is broadly comparable. |
| PIHPmNNp7w (Retrieval-Augmented Decision Transformer) | 4.67 | R2 | Proposes more novel mechanism (retrieval) but severely contradictory reviews. Paper under review is more internally consistent. |
| b5MCteb3w7 (Actions Speak Louder Than States in ICRL) | 4.75 | R1 | ICRL study with evaluation validity issues; paper under review has stronger experimental coherence but also missing baselines. |
| uIKZSStON3 (In-context Exploration-Exploitation for RL) | 7.25 | R1 | Accepted; addresses a harder problem (exploration-exploitation trade-off at inference time) with more principled contributions. Paper under review is clearly weaker. |
| Pj06mxCXPl (Transformers Learn TD for ICRL) | 6.67 | R1 | Accepted; includes theoretical construction showing transformers implement TD. Paper under review has no theoretical component. |
| 1lFZusYFHq (How Transformers Implement Induction Heads) | 6.20 | R2 | Rejected but scored 6.2; has approximation and optimization analysis. Paper under review has no theory. |
| R6klub5OXr (RL Algorithm Design under Data Constraints) | 5.25 | R2 | Comparable scale and scope; large-scale experiments but no novel architecture. |

**Round 1 bracket:** 4.5 – 6.0

**Round 2 narrowing:** The paper is most comparable to 5iWim8KqBR (5.5). Both are architectural modifications to AD for ICRL, tested on small environments, without theoretical backing and with limited baselines. The key differentiator: this paper has a cleaner empirical narrative (consistent HP sensitivity reduction across figures, pixel extension) but a more problematic headline claim (cross-paper 27x comparison). On balance, it lands slightly below 5iWim8KqBR because the headline result is weaker and the missing contemporary baselines are a real validity gap. Score: **5.0**.

**Axes:**
- *Originality*: Low-moderate. N-gram layer is adopted directly from Akyürek et al.; the contribution is applying it to ICRL and extending to pixels.
- *Importance of research question*: Moderate. Reducing data requirements for ICRL is a genuine problem.
- *Claims well-supported*: Partially. HP sensitivity reduction is well-supported; data efficiency headline is not.
- *Soundness of experiments*: Moderate. EMP protocol is sound; cross-paper comparison and asymmetric goal counts weaken the case.
- *Clarity of writing*: Good. Paper is clear and well-organized.
- *Value to research community*: Modest. Demonstrates a useful trick; insufficient baseline coverage to establish its position in the field.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
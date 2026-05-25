Now I have a good understanding of the calibration landscape. Let me produce the final consolidated review.

## Summary

The paper introduces IRIS, a reinforcement learning framework that uses negative self-certainty (NSC)—the forward KL divergence between the model's output distribution and a uniform distribution—as an *intrinsic* reward to fine-tune autoregressive text-to-image (T2I) models. The key insight is that contrary to text-based reasoning where higher self-certainty is beneficial, lower self-certainty produces more visually rich and diverse images that better align with human preferences. Using GRPO, IRIS achieves performance competitive with external-reward methods (T2I-R1) on GenEval, T2I-CompBench, and WISE, while requiring no human labels or domain-specific verifiers.

## Strengths

1. **First intrinsic-reward RL framework for autoregressive T2I generation.** The paper proposes a genuinely novel approach—using only the model's own self-certainty (a token-level KL divergence from uniform) as the reward signal, eliminating the need for human preference data or specialized external verifiers (Abstract, Section 3.2). This directly addresses a scalability bottleneck in T2I alignment.

2. **Competitive results without external supervision are well-demonstrated.** Table 1 and Figure 3 show that IRIS achieves overall scores close to those of T2I-R1 (external reward) on both 1B and 7B models across three diverse benchmarks. For example, on Janus-Pro-1B: GenEval 0.72 vs 0.75, T2I-CompBench 0.379 vs 0.382, WISE 0.37 vs 0.38 (all within one standard deviation on many sub-metrics). The method also surpasses the base model by substantial margins.

3. **Thorough and well-designed ablation studies.** Section 4.3 systematically validates each design choice: training with vs. without semantic CoTs (Figure 5), minimizing vs. maximizing image/text self-certainty (Figures 6–7), forward vs. backward KL (Figure 8), and RL vs. direct NSC optimization (Figure 9). All ablations are evaluated on four independent reward models, providing robust evidence for the architectural decisions.

4. **Emergent CoT reasoning from intrinsic rewards.** Figure 4 and the discussion in Section 4.2 show that IRIS encourages the model to generate meaningful semantic Chains of Thought (detailed text descriptions before image synthesis), demonstrating that intrinsic rewards can incentivize planning behavior similar to external rewards.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contribution is sound and well-supported.

### Minor

1. **Figure 2 compares different models on different tasks, weakening the central observational claim.** The paper's key motivation (that self-certainty behaves oppositely in T2I vs. text reasoning) is illustrated by Figure 2, which plots Qwen2.5-1.5B trained on math reasoning (text tokens) against Janus-Pro-1B trained on T2I (image tokens)—two different models, tasks, and reward procedures. This confound means the observed difference could stem from architectural factors, visual-token presence, or reward-sourcing differences rather than a fundamental task-dependent property. The claim that "higher self-certainty benefits objective reasoning, lower self-certainty benefits subjective generation" is also supported by the within-T2I ablations (Figures 6–7), which provide cleaner evidence for the T2I half. However, the cross-task comparison in Figure 2 is not a controlled experiment. The paper would be strengthened by acknowledging this limitation explicitly or adding a control condition.

2. **The corrected T2I-R1 baseline is presented without the original published numbers for comparison.** Section 4.1 identifies a chat-template mismatch in the official T2I-R1 implementation and corrects it, noting that "numerical results reported in our paper are different from those in Jiang et al. (2025)." However, Table 1 does not include a row showing the *original* T2I-R1 numbers from the published paper. Since the corrected baseline is effectively an author re-implementation, the reader cannot assess the magnitude of the correction's impact. Adding the original numbers (or a note on the direction and approximate size of the difference) would improve transparency.

3. **The conceptual mechanism linking NSC minimization to improved image quality remains empirically motivated rather than principled.** The paper observes that low self-certainty correlates with richer images (Figure 1) and that directly optimizing NSC without RL collapses (Figure 9), but it does not provide a satisfying explanation for *why* pushing token distributions toward uniform should yield semantically better or more aligned images rather than simply noisier ones. The discussion in Section 3.2 ("mode-covering behavior") and the GRPO advantage-normalization argument are plausible but brief. A deeper analysis—e.g., characterizing the types of image tokens that benefit from uncertainty, or connecting NSC to diversity-accuracy tradeoffs—would strengthen the paper's intellectual contribution.

4. **The method is validated on a single architecture (Janus-Pro).** As the authors acknowledge in Section 4.4, T2I architectures are diverse (continuous diffusion, masked modeling, MAE-style), and there is no guarantee that NSC behaves similarly across them. While the paper does not overclaim generality, demonstrating the method on at least one additional autoregressive T2I model (e.g., Show-o) would substantially strengthen the claims of architecture-agnosticism.

### Trivial

1. **No discussion of the computational cost of computing self-certainty.** Computing NSC requires a full softmax over the vocabulary for every token (including image tokens). For Janus-Pro's vocabulary, this is feasible but nontrivial, and the paper does not mention this cost or compare it to the cost of external-reward methods.

2. **Failure cases are not analyzed.** As the paper notes, IRIS underperforms T2I-R1 on spatial and counting tasks (Counting: 0.41 vs 0.50; Color Attribution: 0.51 vs 0.63 on 1B GenEval). Section 4.2 briefly attributes this to the presence of spatial/aesthetic external rewards in T2I-R1, but there is no deeper analysis of *when* and *why* the intrinsic reward fails, which would help users understand the method's limitations.

## Nice-to-Haves

1. **A small-scale human evaluation** (e.g., 100 diverse prompts rated by 3–5 judges) would directly validate the central claim that low self-certainty images are "more preferred by humans." The current evidence relies entirely on automated reward models (HPSv2, GIT, DINO, ORM), which are themselves imperfect proxies for human judgment.

2. **An analysis of output coherence and safety** under the uncertainty-maximizing objective would be useful, since pushing the distribution toward uniform could in principle increase the risk of nonsensical or harmful outputs, especially under distribution shift. The ethics statement is generic; a brief empirical check (e.g., measuring CLIP score or manual inspection of outlier generations) would improve trustworthiness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Correction of prior implementation error" (Strength Finder item #5):** This is a methodological integrity note (the paper discovered and fixed a chat-template mismatch in T2I-R1). It demonstrates good scientific practice but is not a *research strength* of the paper itself. Removed per the rule that compliance and procedural rigor are baseline expectations, not research contributions.

- **"Missing human evaluation" presented as a major weakness:** The paper evaluates on three established automated benchmarks (GenEval, T2I-CompBench, WISE) using standard protocols from the field. While human evaluation would be nice, its absence is not a weakness that undermines the paper's core claims, and demanding it as a condition for acceptance would impose a standard not uniformly applied in this sub-area. Moved to Nice-to-Haves.

- **"The paper does not discuss potential harmful content" (Harsh Critic):** The paper includes an ethics statement acknowledging misuse potential. A deeper discussion would be welcome but is not a standard expectation for a method paper. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The key finding—that minimizing self-certainty (rather than maximizing it) improves T2I generation, and that this can be operationalized as a fully intrinsic reward via GRPO—is the paper's core insight and is well-articulated in the paper itself.

## Suggestions

1. Add a controlled experiment for the cross-task comparison: train the *same* model (e.g., Janus-Pro-1B as a text-only LLM by using its text decoder) on both a text reasoning task and a T2I task, and show that self-certainty moves in opposite directions. Alternatively, explicitly acknowledge the uncontrolled nature of Figure 2 as a limitation.
2. Include the original T2I-R1 numbers from Jiang et al. (2025) alongside the corrected ones in Table 1, so readers can see the impact of the chat-template fix.
3. Add at least one more model (e.g., Show-o or a different autoregressive T2I architecture) to demonstrate generalizability.
4. Provide a brief analysis of failure cases—particularly on spatial/counting tasks where IRIS lags behind—to help users understand the method's limitations.

## Score and Decision

**Round-1 bracket:** Topic-anchored queries placed this paper in the middle band (3.5–7.5). Weakness-anchored queries showed that papers with uncontrolled comparisons or missing baseline numbers typically score in the 3.5–6.0 range, but the paper's strong novelty and thorough ablations push it upward within that range.

**Round-2 narrowing:** Comparison against specific anchors:
- **bO31lfEdos** (5.00, Reject): Human-free RL for object hallucination. IRIS is stronger (more comprehensive experiments, more novel contribution, better-motivated reward).
- **yMHe9SRvxk** (6.00, Accept): HERO—online human feedback RL for diffusion. Both have comparable novelty and experimental thoroughness; IRIS has better ablations but narrower architecture scope.
- **svp1EBA6hA** (6.50, Accept): CTRL—RL-based conditional control for diffusion. Both have similar methodological rigor and acceptance-level quality.
- **kIP0duasBb** (6.67, Accept): CLIP reward for test-time adaptation. IRIS is slightly weaker due to narrower task scope.

The paper sits at the lower end of the "solid accept" range. Its novel contribution and thorough experiments are clear strengths, while the modest conceptual depth of the central observation and limited architectural scope prevent it from reaching the higher tier. Score: **6.0**.

**Anchor list (all retrieved):**
| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| oOa3ZCtMjJ | 3.00 | R1-topic-low | Much weaker paper (GAN+CLIP T2I, rejected) |
| TJHB4ySVZM | 3.40 | R1-topic-low | Much weaker (data augmentation for T2I, rejected) |
| ZVOGMy8Sd8 | 3.00 | R1-topic-low | Unrelated (fashion captioning) |
| RFJGFrMvYj | 1.50 | R1-topic-low | Much weaker (two-stage diffusion, rejected) |
| kIP0duasBb | 6.67 | R1-topic-mid | Stronger (more task breadth, accepted) |
| bO31lfEdos | 5.00 | R1-topic-mid | Weaker (single model, less thorough experiments) |
| 9fMNxWDZsP | 5.50 | R1-topic-mid | Comparable (mixed reviews, rejected — RLPO for concept gen) |
| RauUgiw7VX | 4.75 | R1-topic-mid | Weaker (limited improvement, missing baselines) |
| SI2hI0frk6 | 7.60 | R1-topic-high | Much stronger (Transfusion, major architecture contribution) |
| gU58d5QeGv | 8.00 | R1-topic-high | Much stronger (Würstchen, efficient T2I architecture) |
| 3i13Gev2hV | 8.00 | R1-topic-high | Unrelated (hyperbolic VLMs) |
| WyEdX2R4er | 8.00 | R1-topic-high | Unrelated (visual data-type understanding) |
| m0Su4pLV6W | 4.50 | R1-weakness-intrinsic | Weaker (Intrinsic-ControlNet, different domain) |
| XHvguNJRbE | 2.50 | R1-weakness-intrinsic | Much weaker (IVRL, unrelated) |
| svp1EBA6hA | 6.50 | R1-weakness-intrinsic | Slightly stronger (CTRL, RL for diffusion control) |
| o2uHg0Skil | 6.25 | R1-weakness-SC-KL | Unrelated (RL safety/regularization) |
| bPO4jLOTGG | 3.67 | R1-weakness-SC-KL | Unrelated (uncertainty-aware reward models) |
| hvoVD7x7f8 | 5.00 | R1-weakness-SC-KL | Unrelated (uncertainty-aware decision transformer) |
| MNGMpHxi1I | 3.00 | R1-weakness-SC-KL | Unrelated (predictive uncertainty measures) |
| yF19SY1i8M | 6.00 | R1-weakness-baseline | Unrelated (missing scores in benchmarks) |
| LDu822E45Q | 4.25 | R1-weakness-baseline | Unrelated (benchmark design) |
| E2RyjrBMVZ | 4.17 | R1-weakness-baseline | Unrelated (variance in benchmarks) |
| tqHgSxRwiK | 3.00 | R1-weakness-uncontrolled | Unrelated (fairness in human decisions) |
| McqeEcMSzy | 3.67 | R1-weakness-uncontrolled | Unrelated (task vectors in VLMs) |
| 4ciEeIiIJ7 | 3.83 | R1-weakness-uncontrolled | Unrelated (collective disagreement in AI vision) |
| 5CHcmVzbAz | 5.00 | R2 (4.0-7.0) | Weaker (SePPO, diffusion alignment, rejected) |
| yMHe9SRvxk | 6.00 | R2 (4.0-7.0) | Comparable (HERO, accepted — similar strengths/weaknesses) |
| cJQ1K2fjpD | 6.20 | R2 (4.0-7.0) | Slightly stronger (FiSAO, token-level rewards, accepted) |

**What did the low-band anchors fail at, and does the paper under review share any of those failures?** The low-band anchors (<4.0) failed due to poor writing, unclear contributions, very narrow experiments, or fundamentally unsound methodology. The IRIS paper does not share any of those failures—it is well-written, makes a clear novel contribution, and has thorough experiments. Its weaknesses (uncontrolled comparison in Figure 2, missing original baseline numbers) are limitations within an otherwise solid paper, not structural flaws.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
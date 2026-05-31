Now let me run the calibration search to score this paper:Now I have sufficient information to write the final review.

---

## Summary

MoEP (Modular Expert Paths) proposes a decoder-only language model architecture that combines layer-level top-k routing over parallel Transformer blocks with MoE-style linear projection layers to introduce sparsity while keeping the total parameter count fixed at 28M. The model is trained and evaluated exclusively on the BabyLM strict-small track (10M words), where it achieves 49.00 macro average (excl. AoA) versus the dense GPT-2 baseline at 48.10. A SwiGLU-based variant (MoEP-SwiGLU) is also introduced at 38M parameters.

---

## Strengths

- **Parameter-matched sparsity over dense baseline**: MoEP (28M) achieves 49.00 macro average (excluding AoA) vs. its own GPT-2's 48.10 and the official BabyLM GPT-2 baseline's 46.60 (Table 1, Table 2), concretely demonstrating that sparsity at fixed parameter count can provide a measurable benefit over a dense counterpart, even if modest.

- **Faster early learning from modular routing**: Appendix A.3 training dynamics show that MoEP reaches near-peak evaluation performance at the 30M-word checkpoint, earlier and more uniformly across tasks than GPT-2. This constitutes concrete evidence of improved sample efficiency from the parallel-block routing mechanism.

- **Smooth dimensionality transitions with shrink/grow MoE blocks** (Figure 2, Section 3.2): The explicit MoE projection blocks that map between $d_L$ and $d_P$ are a thoughtful design choice to avoid abrupt information bottlenecks during dimensionality changes—a real architectural contribution over simply inserting smaller parallel layers.

---

## Weaknesses

### Fatal

None that are unambiguously verifiable from the paper text alone.

### Major

- **Misleading headline performance claim**: The paper's central claim — "MoEP achieved the highest performance across all models, including the official BabyLM baselines" (Section 5.1; also repeated in the Introduction) — depends entirely on including the AoA task, where GPT-BERT (causal) scores **−3.90** (below chance), dragging its macro average from 54.10 to 41.20. Without AoA, GPT-BERT (causal) scores 54.10 versus MoEP's 49.00 — a 5-point gap in GPT-BERT's favor. AoA scores are not available for the authors' own GPT-2 or MoEP-SwiGLU models, so no common metric covers all models. The paper partially acknowledges this by listing two macro averages and identifying GPT-2 as the "primary comparison point," but the Introduction's unqualified claim is contradicted by Table 1 itself. The actual story — MoEP modestly outperforms a parameter-matched dense GPT-2 — is valid but significantly less dramatic.

- **Likely sign-inverted load-balancing loss**: Equation 2 defines $\mathcal{L}_{\text{balance}} = -\sum_i p_i \log p_i$, which is Shannon entropy $H(p)$. Combined with a positive weight $\lambda$ in Equation 3, minimizing the total objective minimizes entropy — driving routing toward **concentrated** allocations, i.e., encouraging the very expert collapse the paper aims to prevent. Standard load-balancing approaches encourage **high** entropy (uniform routing). This is either a write-up error (while the implementation uses the correct sign) or a genuine implementation bug. Given that the paper lists avoidance of collapse as a key motivation (Section 3.4) and uses routing dynamics as evidence (Appendix A.3), the ambiguity undermines confidence in both the method's correctness and its reproducibility. The authors must clarify.

### Minor

- **Unacknowledged parameter count discrepancy for MoEP-SwiGLU**: The abstract and Section 1 foreground "keeping the total parameter count fixed" as a defining property of MoEP. Table 2 shows that MoEP-SwiGLU has 38M parameters — 35% more than the 28M baseline — without any acknowledgment in the text. Conclusions drawn from comparing MoEP-SwiGLU to 28M-parameter models (Sections 5.1, 6) are therefore on unequal footing.

- **No ablations to isolate architectural contributions**: MoEP combines (a) parallel blocks at reduced dimensionality, (b) top-k layer-level routing, and (c) MoE projection layers. The paper offers no ablation separating these components (e.g., parallel blocks without routing, routing without shrink/grow projections). The marginal gain over dense GPT-2 (49.00 vs. 48.10) could be attributed to any one of these, and without ablations the specific contribution of each design choice cannot be assessed.

- **Vague description of routing aggregation**: Section 3.3 states "the routed inputs are summed up together" without specifying whether this is a weighted sum using gating probabilities or an unweighted sum, which affects both interpretation and reproducibility.

### Trivial

- The Introduction uses "MoEP was able to outperform all BabyLM strict-small baseline models" as a flat statement (Section 1, final paragraph before contributions), whereas Table 1 requires important caveats to make this true. At minimum, the AoA dependency should be noted in the same sentence.

---

## Nice-to-Haves

- An ablation within the same BabyLM budget isolating: (i) parallel blocks without routing (all blocks active), (ii) routing without dimensionality reduction (blocks at full $d_L$), (iii) full MoEP, would dramatically strengthen the architectural claim.
- Visualization of routing distribution entropy over training (do tokens actually specialize, or does near-dense behavior emerge?) would directly validate the load-balancing claim and add interpretability depth beyond the checkpoint-level curves in Appendix A.3.
- Since BabyLM is the sole evaluation, clarifying what aspects of MoEP are specific to the small-data regime (as mentioned in Section 6) versus general would strengthen the paper's positioning.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Strength: "Stable expert/block utilization via load-balancing" (Strength Finder)**: Conflicts with the verified Major weakness on the sign-inverted loss. The model trains stably, but this cannot be attributed to a correctly formulated load-balancing objective without further clarification from the authors. Removed to avoid endorsing an unsupported causal claim.

- **Strength: "Linear vs. SwiGLU comparison provides practical insight" (Strength Finder)**: MoEP-SwiGLU has 38M parameters vs. MoEP's 28M. The conclusion that "simpler experts are better" conflates model complexity with parameter count asymmetry. This is not a reliable design insight from the data as presented.

- **"Checkpoint selection as hyperparameter tuning on the evaluation set" (Harsh Critic)**: This is a constraint of the BabyLM protocol itself, not a flaw of this paper. All participants select checkpoints under the same protocol. Removed.

- **"AoA selective reporting structural inconsistency" (Harsh Critic, framing as fatal)**: The paper explicitly acknowledges that AoA scores for GPT-2 and MoEP-SwiGLU are sourced from the official leaderboard and are absent for their own re-implementations. This is a limitation of the experimental setup but does not rise to a fatal flaw. Already captured under Major weakness on headline claim; not repeated as a separate fatal issue.

---

## Novel Insights

The harsh critic's observation about the load-balancing loss sign is the most technically consequential finding in this review: if $\mathcal{L}_{\text{balance}} = -\sum_i p_i \log p_i$ is minimized (as written in Eq. 3), the training objective drives routing to collapse rather than balance. This is an identifiable and actionable error — the optimizer is pushed to minimize Shannon entropy, which is exactly what you do *not* want when avoiding expert collapse. The practical implications are ambiguous (the model achieves reasonable results), but the discrepancy between stated intent and written formula is concrete and important. This observation alone is worth correcting before publication.

---

## Suggestions

1. **Fix or clarify Equations 2–3**: State explicitly whether the implemented loss maximizes or minimizes routing entropy, and provide the correct sign. If the current formula is as written (entropy minimization), the regularizer must be corrected to negative entropy (penalizing non-uniformity) or to a Switch-Transformer-style load-balance term.
2. **Qualify the headline claim**: Replace "outperform all BabyLM baseline models" with a claim that is defensible on a single consistent metric (excl. AoA macro average), which shows MoEP modestly outperforming the GPT-2 baseline—an honest and still meaningful result.
3. **Explicitly note MoEP-SwiGLU's parameter count**: Add one sentence acknowledging the 38M vs. 28M discrepancy and interpreting results accordingly.
4. **Add three targeted ablations** (parallel-blocks-only, routing-only, full MoEP) within the existing BabyLM budget to isolate which design choices drive gains.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to MoEP |
|---|---|---|---|
| 04RLVxDvig.md (NanoMoE) | 3.00 | R1 | Most similar — MoE-style parameter-efficient building blocks, limited evaluation, marginally narrower evaluation than BabyLM |
| 7DY2DFDT0T.md (EfficientSkip) | 2.50 | R1/R2 | Slightly weaker — transforms dense LLMs to sparse, limited compute, poor critical reception |
| 762u1p9dgg.md (MOEfication) | 3.40 | R1 | Similar scope; sparsification of dense model via MoE; limited but more complete evaluation |
| XVHXVdoV11.md (Compatible Specialization) | 3.40 | R1 | Adjacent topic, slightly stronger evaluation |
| KJLqgaixgn.md (Sparse Training) | 3.50 | R2 | Similar level; sparsity in LLM training, limited scope |
| bppG9srkpR.md (LokiLM) | 3.60 | R2 | Slightly above, but scored 1 by one reviewer |
| SznHfMwmjG.md (Feature Sparsity LM) | 3.50 | R2 | Adjacent, similar limitation |
| thqPibDg6A.md (MO-CTE) | 4.40 | R2 | Stronger — multiple datasets, 140M–750M models, deeper theoretical analysis |
| L0PciKdHsP.md (MoIN) | 4.50 | R2 | Stronger — upcycling LLMs with MoE adapters, more complete evaluation |
| sDmjlpphdB.md (MoE in Prompt Opt.) | 4.75 | R2 | Different application, comparable evaluation depth |
| uWvKBCYh4S.md (Mixture of LoRA Experts) | 5.00 | R2 | Stronger — fine-tuning setting with more comprehensive benchmarking |
| V7EiYG5DwZ.md (Mutual-Inform SMoE) | 5.75 | R1 | Stronger — principled probabilistic analysis, larger-scale evaluation |
| 4D0f16Vwc3.md (ReMoE) | 6.60 | R1 | Much stronger — fully differentiable MoE, multiple sizes, state-of-the-art results |
| Pu3c0209cx.md (Tight Clusters MoE) | 7.00 | R1 | Much stronger — rigorous theoretical + empirical analysis |
| pHOH8FVrTp.md (Async MoE) | 7.33 | R1 | Much stronger — novel asynchronous training paradigm, large-scale evaluation |
| t7P5BUKcYv.md (MoE++) | 8.00 | R1 | Far stronger — zero-computation experts, SoTA results at scale |
| vf5aUZT0Fz.md (DEPT) | 8.00 | R1 | Different topic; strong benchmark |

**Round 1 bracket**: 2.5–4.5 (paper clearly falls below mid-range MoE papers around 5–7).

**Round 2 narrowing**: MoEP is most comparable to NanoMoE (3.00) — both propose MoE-inspired architectural modules, both have limited evaluation depth, both are thin papers making modest empirical gains on small benchmarks. MoEP has a slightly more legitimate evaluation setting (BabyLM is a recognized shared task), but also carries a more consequential technical error (the load-balancing sign issue) and an actively misleading headline claim. MO-CTE (4.40) and MoIN (4.50) are clearly stronger: they have multi-dataset evaluation and more rigorous analysis. MoEP does not reach that bar.

**Final score**: 3.0 — the paper sits at the NanoMoE level. The architectural idea is coherent, and the BabyLM evaluation provides a concrete (if limited) comparison point. However, the misleading core claim, the likely sign-erroneous load-balancing formulation, the unacknowledged parameter discrepancy for the SwiGLU variant, and the absence of any ablation study together prevent this from meeting the bar for acceptance. The contribution, as it stands, is at workshop level.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>
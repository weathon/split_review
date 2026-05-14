Now let me synthesize everything into the final review.

---

## Summary

MoEP introduces a sparse decoder-only architecture that combines layer-level parallelism with Mixture-of-Experts-style top-k routing. Parallel blocks operate at reduced hidden dimension, interleaved with MoE-based shrink/grow projections, keeping total parameter count matched to a dense GPT-2 baseline (28M). Evaluated on the BabyLM strict-small track, MoEP outperforms the matched GPT-2 baseline and shows faster early specialization during training.

## Strengths

- **Genuinely novel architecture**: The combination of layer-level parallel blocks with top-k routing and dimension-shrink/grow MoE projections (Figure 2) is a new point in the design space, distinct from standard FFN-level MoE and from prior layer-level approaches like MoLE. Section 3.1–3.3 provides a clear architectural description.

- **Controlled comparison at matched parameter count**: MoEP is trained against a reproduced GPT-2 at identical 28M parameters under the same training pipeline (same data, same tokenizer, same seed, same epoch budget). Table 1 shows MoEP achieves macro average of 67.30 vs. 63.45 for the authors' GPT-2 and 61.50 for the BabyLM GPT-2 baseline (excluding AoA). This directly supports the claim that sparsity can be added without parameter inflation while improving performance.

- **Standardized evaluation pipeline**: Following the BabyLM strict-small track with its official evaluation protocol (both zero-shot and fine-tuned tasks) provides a reproducible comparison framework and facilitates future work.

- **Useful analysis of training dynamics**: Appendix A.3 provides per-checkpoint evaluation curves showing that MoEP achieves stronger early specialization (particularly on Entity Tracking and WUG) compared to GPT-2, and the paper is honest that MoEP subsequently overfits — a diagnostic practice that reveals failure modes rarely discussed in similar work.

- **Practical architecture insight**: The comparison between linear-expert MoEP and SwiGLU-expert MoEP (Table 1, Section 5.1) demonstrates that lightweight linear projections outperform SwiGLU-based experts at small scale, providing actionable guidance for resource-constrained settings.

## Weaknesses

### Fatal

None.

### Major

- **Single-run evaluation with no statistical validation**: All results in Table 1 come from a single training run with seed 42 (Table 3). No standard deviations, confidence intervals, or replicates are reported. On a 10M-word dataset with modest performance gaps between models, this makes it impossible to assess whether the reported differences are robust or attributable to seed variance. This is the most significant weakness and directly affects the reliability of the paper's headline result.

### Minor

- **Missing dense-parallel ablation to isolate sparsity effect**: The paper compares MoEP against a standard dense GPT-2, which is appropriate for the main claim (fixed-parameter performance). However, a dense variant of the parallel architecture — where all P parallel blocks are activated and their outputs averaged — would cleanly isolate whether the gains come from the parallel structure itself or specifically from sparse top-k routing. Without it, the paper cannot fully attribute the improvement to sparsity rather than to increased representational capacity from parallelism at reduced dimension.

- **No compute-cost measurement despite efficiency framing**: The abstract mentions "without overloading computation," but the paper reports only parameter counts. FLOPs per token, throughput, or latency are never measured. While the primary framing is about fixed parameter count (not compute), the repeated references to efficiency and sparsity would be strengthened by at least a theoretical FLOPs analysis. MoEP's two-level routing (experts + parallel blocks) may have non-trivial computational implications relative to the dense baseline.

- **Limited scale and unclear generalizability**: The paper is restricted to BabyLM's 10M-word corpus and 28M-parameter models. The authors appropriately acknowledge this in Section 6, noting that with "more complex data, parallel layers may no longer operate as effectively at reduced dimensionality." This is honest but means the contribution remains a proof-of-concept at small scale.

### Trivial

- The "fast evaluation" used for checkpoint selection (Section 4) is not described in sufficient detail — which tasks or subset of data it uses is unclear, creating a minor transparency concern about potential indirect selection bias.

## Nice-to-Haves

- **Multiple training runs** with mean and standard deviation across at least 3 seeds would substantially strengthen the reliability of the performance claims.

- **Dense parallel (no routing) baseline**: Activating all parallel blocks and averaging/summing their outputs would isolate the sparsity effect from the architectural change.

- **Routing utilization analysis**: Histograms or entropy statistics of expert/block routing probabilities would make the claimed "diverse computational pathways" concrete and verify that load balancing (Equations 2–3) works as intended.

- **FLOPs comparison**: A theoretical FLOPs-per-token analysis (even without wall-clock measurements) would help assess the efficiency claim.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Early-stopping undercuts the comparison"** (Harsh Critic #4): The paper states in Section 4 that both MoEP *and* GPT-2 achieve their best accuracy at the 30M-word checkpoint. The same best-checkpoint criterion is applied to all models. The critic's claim that "GPT-2 continues to improve on several tasks up to 100M" is not supported by the paper's own analysis — Appendix A.3 states GPT-2 peaks at 30M overall, with some task-level variation but no improvement in macro performance after 30M. Both models are compared under identical early-stopping conditions, so this is not a valid criticism.

- **"Missing comparison against standard dense Transformer of identical parameter count"** (part of Harsh Critic #1): This comparison is present. The authors train their own GPT-2 at 28M parameters under matched conditions, and also compare against the BabyLM GPT-2 baseline. The claim that no such comparison exists is factually incorrect.

- **"No evidence load balancing prevents collapse"** (Harsh Critic, Section-by-Section Notes): While explicit routing histograms would be nice, the model trains stably and achieves good downstream performance — this is de facto evidence that collapse does not occur. Demanding explicit routing distribution plots is a nice-to-have, not a weakness.

- **Strength Finder claim about "GPT-2 requires more tokens to converge"**: Both MoEP and GPT-2 peak at 30M words according to the paper. MoEP shows *stronger early specialization*, which is a real finding, but the claim about GPT-2 requiring more tokens is imprecise. The retained strength reflects the more accurate framing (faster early specialization).

- **Strength Finder claim that the paper's decomposition of routing loss is novel**: Load-balancing auxiliary losses (Equations 2–3) are standard in the MoE literature. Applying them at two levels is sensible but not a novel contribution. Dropped.

## Novel Insights

None beyond the paper's own contributions. The core architectural insight — that layer-level parallelism with sparse routing can match or exceed dense performance at fixed parameter count on small-scale language modeling — is the paper's own finding. Neither the harsh critic nor the strength finder surfaces a genuinely novel observation that the paper itself did not already make.

## Suggestions

- The single most impactful improvement would be running the main experiment with 3–5 different random seeds and reporting mean ± std. This alone would address the most serious weakness and substantially increase confidence in the results.

- A dense-parallel ablation (all blocks active, outputs averaged) would cleanly decompose the contribution of architectural parallelism from sparse routing, strengthening the paper's central narrative.

- Consider reporting at least a theoretical FLOPs-per-token comparison between MoEP and the dense GPT-2 baseline. Even a back-of-the-envelope analysis would help readers assess the efficiency trade-off.

- The paper would benefit from explicitly stating architectural hyperparameters (N parallel layers, P parallel blocks, d_L, d_P, E experts, top-k values) in the main text rather than only in Appendix Table 2, as these numbers are essential for understanding the architecture.

---

## Score and Decision

### Anchor Comparison

| Anchor Paper | Avg Score | Decision | Comparison to MoEP |
|---|---|---|---|
| VALM (mXMKm4pilN) | 1.50 | Reject | Significantly weaker — no baselines, no quantitative evaluation, preliminary prototype. MoEP is far more rigorous. |
| Layer-Parallel Training (G1MCI1Qp9u) | 3.50 | Reject | Weaker — unfair baselines, limited contribution, methodological gaps. MoEP has cleaner evaluation and clearer claims. |
| Fully Sparsely-Activated LLMs (0Iw52EDu82) | 4.50 | Reject | Comparable in ambition but weaker in execution — unclear definitions, missing architectural details. MoEP has a more concrete architecture and clearer results. |
| MoE Can Surpass Dense LLMs (oIdzliJAeA) | 5.00 | Accept (Oral) | Most comparable. Both ask whether sparse architectures beat dense at matched resources. That paper has much larger scale (7B models, 50T tokens) and more extensive ablations, but had significant methodological concerns from reviewers. MoEP is smaller-scale but cleaner in its comparison and more architecturally novel. |
| SparseEval (CZAzAedGSV) | 6.00 | Accept (Poster) | Stronger — comprehensive experiments across many models, clear practical gains. MoEP is narrower in scope and less thoroughly validated. |
| Optimal Sparsity of MoE (XFw2EPRUUR) | 6.50 | Accept (Oral) | Clearly stronger — systematic investigation with extensive controlled experiments, well-supported claims. MoEP has architectural novelty but thinner validation. |

MoEP sits squarely between the 4.50 reject and the 6.00 accept anchors. Its architectural novelty and clean comparison are real strengths that distinguish it from the weaker papers. However, the single-seed evaluation and missing ablations prevent it from reaching the level of the 6.0+ papers. It is most comparable to the "MoE Can Surpass Dense" paper (5.00), which was accepted (Oral) despite its own methodological gaps. MoEP brings stronger architectural novelty but at much smaller scale.

The paper makes a genuine contribution — a novel architecture combining layer-level parallelism with sparse routing — and provides credible evidence that it outperforms a matched dense baseline on a standard benchmark. The weaknesses (single seed, missing dense-parallel ablation, no compute analysis) are addressable and do not invalidate the core contribution, but they do limit the strength of the conclusions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
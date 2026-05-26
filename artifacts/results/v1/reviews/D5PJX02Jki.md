Now I have sufficient information to write the final consolidated review. Let me compose it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me synthesize everything now.

The paper proposes RoPE++, which re-incorporates the discarded imaginary component of the complex-valued dot product in Rotary Position Embeddings. It offers two configurations: RoPE++_EC (equal cache, doubled heads) and RoPE++_EH (equal heads, half cache). The idea is interesting and the mathematical derivation is clean.

**Strengths (filtered):**
1. Consistent gains on RULER/BABILong (Table 2): EC improves over vanilla RoPE by 6.2 pts (376M) and 2.0 pts (776M) on RULER average, with larger gains at longer contexts.
2. Two practical configurations with different trade-offs (Section 3.3): EC and EH offer practitioners actionable choices between performance and efficiency.
3. Compatibility with existing techniques (Table 3): RoPE++ works with Linear PI and YaRN, consistently outperforming vanilla RoPE under both.
4. Noise injection experiment (Section 5.2, Figure 5): Corrupting imaginary heads degrades RULER-4k by 5-8 pts more than corrupting real heads, providing within-model evidence for the importance of imaginary heads for long-context tasks.

**Major Weaknesses:**
1. The core claim is confounded by head count changes. RoPE++_EC doubles attention heads relative to baseline. Without an ablation comparing against a variant with the same number of heads but using standard real-only RoPE, the improvement cannot be attributed to the imaginary component specifically. RoPE++_EH also lacks a proper control (RoPE with the same reduced QKV/cache budget but all real heads). This is the central evidentiary gap.

2. The theoretical analysis (Section 3.2) relies on i.i.d. query/key assumptions and ignores softmax normalization, so the characteristic curve does not directly translate to attention weight behavior in trained models. The attention pattern visualizations (Figure 5) are anecdotal (2 heads per model), not systematic.

**Minor Weaknesses:**
- Short-context gains are small (+0.8-0.9 avg) with no confidence intervals or multiple seeds.
- Efficiency analysis (Figure 4) only covers RoPE++_EH, not EC.
- RoPE++_EH underperforms vanilla RoPE on several BABILong entries (Table 2).
- No experiments on real-world document-level tasks (LongBench, Qasper, etc.).

**Score: 4.5, Decision: Reject.** The paper presents a well-motivated idea and clean math, but the missing controlled ablation prevents proper attribution of the improvement to the imaginary component. This is a significant evidentiary gap for a method paper.## Summary

The paper proposes RoPE++, an extension of Rotary Position Embeddings that re-incorporates the imaginary component of the complex-valued dot product as a separate group of attention heads. Two configurations are introduced: RoPE++_EC (equal KV cache, doubled attention heads) and RoPE++_EH (equal head count, halved KV cache and QKV parameters). The idea is well-motivated by identifying an information loss in standard RoPE, and the mathematical derivation showing that the imaginary attention can be computed via a simple −π/2 rotation of the query is clean. Pre-training experiments at 376M and 776M show consistent gains on long-context benchmarks (RULER, BABILong) for RoPE++_EC, and comparable performance with half the cache for RoPE++_EH.

## Strengths

- **Consistent long-context gains across model sizes.** Table 2 shows RoPE++_EC improves over vanilla RoPE on RULER average by 6.2 points (376M) and 2.0 points (776M), with larger margins at longer contexts (e.g., RULER-64k: 9.0 vs. 5.5 for 376M). The BABILong improvements follow the same pattern.

- **Two practical configurations with different trade-offs.** RoPE++_EC doubles heads at the same cache cost for maximum performance; RoPE++_EH halves cache and QKV parameters while maintaining competitive results (Section 3.3, Figure 4). This gives practitioners actionable options depending on whether they prioritize accuracy or memory/latency.

- **Compatibility with existing context-extension techniques.** Section 5.3 and Table 3 show that RoPE++ (both variants) can be combined with Linear PI and YaRN and consistently outperforms vanilla RoPE under both interpolation methods on RULER and BABILong averages, demonstrating it does not conflict with standard long-context pipelines.

- **Noise injection experiment provides within-model evidence.** Section 5.2 (Figure 5) shows that corrupting imaginary attention scores with Gaussian noise (σ=1.0) degrades RULER-4k performance by 5-8 points more than the same corruption applied to real attention. While this does not address the cross-model ablation issue (below), it does confirm that within a trained RoPE++ model, the imaginary heads carry more long-context information than the real heads.

## Weaknesses

### Major

- **The central claim is confounded by head count changes, and the missing ablation prevents proper attribution.** RoPE++_EC doubles the number of attention heads relative to vanilla RoPE while keeping the QKV parameter budget fixed. The paper lacks a controlled comparison against a variant with the same number of heads (i.e., the same doubling) but where all heads use standard real-only RoPE. Without this, the observed improvements on long-context tasks cannot be attributed specifically to the *imaginary nature* of the new heads rather than to the increased head count. RoPE++_EH has a symmetric issue: comparable performance with half the resources is suggestive, but the proper control (RoPE with the same reduced QKV/cache budget but no imaginary heads) is absent. The noise injection experiment (Section 5.2) provides within-model evidence but does not substitute for this cross-model ablation — it shows imaginary heads are important in a model that already has them, not that adding them is better than adding more real heads. This is the central evidentiary gap; the paper's core claim ("re‑incorporating the imaginary component improves long‑context modeling") is not fully supported without this ablation.

- **The theoretical analysis does not convincingly connect to actual attention behavior.** Section 3.2 derives the characteristic curve of imaginary attention by averaging over assumed i.i.d. query and key vectors, showing the sine-integral does not decay with distance like the cosine variant. However, raw attention scores are normalized by softmax, so absolute score magnitude does not directly determine the attention weight distribution. The analysis also does not model the covariance structure that arises in a trained model. The attention-pattern visualizations (Figure 5) are anecdotal (two heads per model), not a systematic verification across layers and heads.

### Minor

- **Short-context gains are small and no confidence intervals are reported.** On the 9-task average (Table 1), the largest gain over vanilla RoPE is +0.9 points (376M) and +0.8 points (776M). These differences are within typical run-to-run variance at this model scale, and no multiple seeds, confidence intervals, or significance tests are provided. Single-seed results are common in LLM pretraining, but the small margins make this worth noting.

- **Efficiency analysis only covers RoPE++_EH.** Figure 4 reports memory cost and TPOT only for the EH variant. The computational cost of RoPE++_EC (which doubles query heads and requires a larger output projection W_o) is not reported, making it impossible to judge whether its performance gains come at a significant inference cost.

- **RoPE++_EH underperforms vanilla RoPE on several individual BABILong entries.** At 776M, RoPE++_EH scores lower than vanilla RoPE on 5 of 6 BABILong context lengths (e.g., 2k: 31.9 vs. 33.5; 4k: 26.5 vs. 30.7), despite having a higher average. The claim of "comparable performance" is accurate only as an aggregate — individual settings show notable degradation.

- **The description of the two variants could be clearer.** Figure 2's caption says RoPE++_EC has "key heads are halved" while the visual shows the same number of key heads as baseline (both 2), creating confusion. The text correctly describes EC as equal-cache, but this inconsistency makes the architecture harder to verify at a glance. A table listing d_model, n_heads, n_kv_heads, per-head dimension, and cache size for each variant would resolve this.

- **Only synthetic long-context benchmarks are evaluated.** RULER and BABILong are synthetic retrieval tasks. Evaluation on real-world long-document tasks (e.g., LongBench, Qasper, summarization) would better demonstrate practical value.

### Trivial

- Table 1's "Avg" column is not labeled in the header.
- The paper states the imaginary component "does not decay with distance" but the characteristic curve (sine integral) oscillates — it does not decay to zero but also does not monotonically preserve long-range information.

## Nice-to-Haves

- Extrapolation experiments beyond 64k (e.g., 128k or 256k) would strengthen the length-extrapolation claims in Section 3.4.
- Training loss/perplexity curves would help assess whether all baselines converged properly.
- Scaling to 1-2B parameters would increase confidence that the findings hold at practically relevant scales.
- An aggregated statistical summary of attention patterns across all layers and heads (e.g., average attention distance for real vs. imaginary heads) would be more informative than the current single-head heatmaps.

## Removed Points

- **Criticism about inconsistent cache accounting in RoPE++_EC (from Harsh Critic):** The critic claimed Figure 2b shows key heads halved, making the cache not equal. The figure schematic uses the same absolute numbers as baseline (2 key heads in both (a) and (b)), and the paper's text clearly states EC keeps equal cache. The caption wording is confusing but the claim is consistent — this is at most a Minor presentation issue, not the structural flaw described.
- **Criticism about questioning the existence/release status of models or benchmarks:** Removed per hard rules — all cited entities are assumed to exist.
- **Criticism about missing related works:** Removed per hard rules.
- **Reproducibility nitpicks about hyperparameters not fully disclosed:** The paper provides architecture details in Appendix C (removed from parsed version but present in original), training setup, and states code/checkpoints are released.
- **Strength Finder claim that noise injection provides "direct causal evidence":** Removed as overstated — the experiment shows within-model importance but does not address the cross-model confound. A strength cannot depend on a weakness being false.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the discarded imaginary component of RoPE's complex product can be efficiently recovered via a −π/2 query rotation and provides complementary long-context information — is the paper's own contribution. The review process does not surface additional novel observations beyond what the paper already states.

## Suggestions

1. **Add the critical ablation:** Train RoPE++_EC alongside a control variant with the same doubled head count but where every head uses standard real-only RoPE. If the imaginary-heads variant still outperforms, the core claim is supported. Similarly for EH: compare against RoPE with the same reduced QKV/cache budget but all real heads. This is the single most important addition.

2. **Tighten the theoretical analysis:** Acknowledge the i.i.d. and pre-softmax limitations explicitly. Show (analytically or via a toy model) how the characteristic curve translates to post-softmax attention weight behavior, or provide systematic empirical verification (average attention distance across all heads, ablation of the imaginary component's frequency structure).

3. **Provide a clean architecture table:** List d_model, n_heads, n_kv_heads, per-head dimension, total QKV parameters, and KV cache size for every variant and baseline. This would resolve the current ambiguity and make the efficiency claims verifiable.

4. **Report EC's efficiency costs and run multiple seeds** for at least the key comparisons (RoPE++_EC vs. vanilla RoPE on long-context) to establish significance.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Query Bucket | Comparison |
|--------|-----------|-------------|-----------|
| Round and Round We Go (RoPE analysis) | 6.20 | Topic-High | Accepted. Strong theoretical analysis of RoPE internals, limited model diversity. RoPE++ has a more applied contribution but a confound in its core claim that is absent in this anchor's analytical claims. |
| Scaling Laws of RoPE-based Extrapolation | 5.00 | Topic-Mid | Accepted. Strong theoretical framework, but evaluation limited to perplexity. RoPE++ has better empirical breadth but a more fundamental attribution issue. Comparable overall quality. |
| Why Does Effective Context Length Fall Short (STRING) | 6.50 | Topic-Mid | Accepted. Clear framework, strong results across model scales, no obvious confounds. RoPE++ does not match this bar. |
| Which Attention Heads Matter for ICL | 4.60 | Weakness (confound/attribution) | Rejected. Had confound issues (head location as confound), weak empirical results. RoPE++ has a similar confound type but stronger empirical support. Comparable score range. |
| Not All Heads Matter (KV cache) | 6.50 | Weakness (KV efficiency) | Accepted. Clear methodology, strong empirical results. RoPE++ is not comparable in rigor. |
| MCCE (missing attribution control) | 3.00 | Weakness (missing ablation) | Rejected. Fundamental attribution issues. RoPE++ shares the attribution gap but has more redeeming qualities. |

**What did the low-band topic anchors fail at?** No topic-low anchors were returned in the search band (<3.5). The closest low-scoring anchors were from the weakness-anchored queries: papers with missing ablation controls or attribution confounds scored 3.00-4.00. These papers failed because their core claims could not be causally attributed to the proposed mechanism due to missing controls. **The paper under review shares this failure mode** — while less severe than the 3.00 anchor (which had no causal evidence at all), the central claim that the imaginary component specifically drives the improvement is not adequately isolated from the head-count confound. The score must reflect this.

**Score: 4.5.** The paper has a legitimate novel idea, clean derivation, and broad experimental evaluation. However, the missing controlled ablation prevents proper attribution of the improvement to the imaginary component, which is the paper's central claim. This is a significant evidentiary gap for a method paper. The paper sits alongside other papers with similar attribution issues (e.g., "Which Attention Heads Matter for ICL" at 4.60) — not fatally flawed, but with a core weakness that the current evidence does not adequately address.

**Decision: Reject.** The paper would need the controlled ablation to substantiate its central claim and meet the evidentiary bar for a method contribution at a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
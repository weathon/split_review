Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes M-SMoE, a method to merge redundant experts in Sparse Mixture-of-Experts (SMoE) models by leveraging routing statistics (activation frequencies and router logits) to form expert groups, then merge each group via frequency-weighted averaging. The authors further observe that merged experts exhibit lower weight-space dimensionality, enabling additional compression via low-rank decomposition and structural pruning in MC-SMoE. Experiments on switch-base-32 across 8 NLP benchmarks show that M-SMoE achieves 60% memory reduction with competitive performance, and MC-SMoE reaches up to 80% memory and 20% FLOPs reduction with moderate degradation.

## Strengths

- **Novel and well-motivated approach.** Using routing statistics (activation frequencies and router logits) to guide expert merging is a fresh idea that directly addresses the expert redundancy problem in SMoE. The paper provides concrete evidence (Figure 1) of skewed expert utilization, clearly motivating the need for selective merging rather than naive averaging or uniform pruning.

- **Key insight that merging promotes compressibility.** The observation that merged experts have lower stable-rank (Figure 2), and that this makes them more amenable to further compression, is non-trivial and practically useful. Table 9 (C-SMoE vs MC-SMoE) empirically demonstrates this: MC-SMoE at 381M outperforms C-SMoE at 570M, validating that merging + compression is more effective than compression alone.

- **Thorough ablation study validating design choices.** The paper systematically ablates every component: permutation alignment (Table 8), KD contribution (Table 7), grouping method (Table 6), merging strategy frequency/uniform/Fisher (Table 8 in paper), and adaptive vs. uniform merging ratio (Table 2). These ablations provide internal validation and help isolate the contribution of each design decision.

- **Practical significance.** SMoE memory footprint is a real barrier to deployment, especially in resource-constrained scenarios. The paper addresses a genuine practical problem with a clean, implementable solution.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot and decoder-only results are promised but not presented.** The paper states it evaluates on the fairseq-moe-15b decoder-only model in zero-shot settings (Section 4.1, lines 163 and 168), and lists MRPC, WinoGrande, and OpenBookQA as zero-shot benchmarks. However, no results table for these experiments appears anywhere in the paper — all reported results are for switch-base-32 in fine-tuning mode. This is a significant evidential gap: the claims about "extensive experiments across eight benchmarks" and "superior efficiency in both fine-tuning and zero-shot settings" are only half-substantiated. The contributions regarding decoder-only and zero-shot generalization cannot be evaluated.

### Minor

- **No variance or error bars reported.** All results in Table 1 are single-point estimates. Several differences between M-SMoE and the best baseline are small (e.g., MultiRC: 75.57 vs. 75.26; WinoGrande: 61.80 vs. 61.48). Without multiple seeds or confidence intervals, it is unclear whether these differences are meaningful or within noise. That said, single-run evaluation is common practice in large-scale NLP benchmarks, so this is a minor concern rather than a major flaw.

- **"Virtually no loss" overstates the results for MC-SMoE.** The abstract and introduction claim "up to 80% memory and 20% FLOPs reduction with virtually no loss." However, MC-SMoE shows non-trivial drops on several tasks relative to Full SMoE: SST-2 (−2.4%, from 95.75 to 93.35), MultiRC (−2.21%, from 76.19 to 73.98), and WinoGrande (−2.28%, from 61.80 to 59.52). These are >2% drops, which is not "virtually no loss." The claim should be qualified per task or softened to reflect that some tasks see noticeable degradation.

- **Computational cost of permutation alignment is not discussed.** Section 3.1 describes aligning all 32 experts per layer (12 layers) using weight-matching, but the paper does not report the time or memory cost of this step, nor whether the matching is exact or approximate. Since the gain from alignment is modest (0.73–0.76% per Table 8), the cost-benefit trade-off is unclear.

- **C-SMoE vs. MC-SMoE comparison is not perfectly controlled.** Table 9 compares C-SMoE (570M) with MC-SMoE (381M). While MC-SMoE outperforming C-SMoE at a *smaller* size is evidence that merging helps, a cleaner comparison would hold the parameter count constant (e.g., compress C-SMoE to 381M) to isolate the benefit of merging vs. compression rate. The current comparison is informative but not a direct ablation of the paper's stated mechanism.

- **Stable-rank comparison lacks a naive-averaging baseline.** Figure 2 shows that merged experts have lower stable-rank, but the paper does not compare this to what would happen if experts were simply averaged uniformly (without routing-based grouping). Without this baseline, it is unclear whether the reduced dimensionality is a benefit of the proposed grouping strategy or an artifact of any averaging operation.

### Trivial
- The paper uses inconsistent capitalization ("kD" vs. "KD" in Table 7 caption).

## Nice-to-Haves
- Report hardware-measured inference latency and memory bandwidth savings, not just TFLOPs, since SMoE dispatch overhead can make TFLOPs a poor proxy for wall-clock time.
- Compare to more recent expert pruning methods (e.g., Koishekenov et al. 2023) in addition to the task-specific baseline from 2022.
- Ablate the choice of k (number of dominant experts kept) to show the performance-compression Pareto frontier.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **KD confound invalidates baseline comparisons (Harsh Critic #1).** REMOVED — factually incorrect. The paper states explicitly at line 268: "we by default use KD for all merged and compressed SMoEs, including our M-SMoE, MC-SMoE, and all baselines." The reviewer's claim that baselines were "not fine-tuned with KD" directly contradicts what the paper says. The KD ablation (Table 7) shows M-SMoE with/without KD, but the main comparison (Table 1) is controlled: all methods use KD.

2. **MC-SMoE > C-SMoE not properly controlled (Harsh Critic #3).** REMOVED as a "fatal" or "major" issue — the comparison actually supports the paper's claim: MC-SMoE (381M) outperforms C-SMoE (570M) at a *smaller* model size, which is stronger evidence than equaling at the same size. The point is retained in Minor as a suggestion for a cleaner controlled comparison, but it does not undermine the core claim.

3. **Task-Specific baseline underperformance suggests implementation issues.** REMOVED — speculation. The paper implements the baseline as described by Chen et al. (2022); it simply performs worse, which is why the authors propose a better method. No evidence of incorrect implementation.

4. **Strength Finder's claim that "Table 1 covers both supervised fine-tuning and zero-shot settings."** REMOVED — inaccurate. Table 1 only shows fine-tuning results for switch-base-32; zero-shot results for fairseq-moe-15b are absent.

5. **Generic strengths about "important problem" / "interesting question."** Removed as insufficiently specific.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a new observation about the method that the paper itself does not make.

## Suggestions
1. **Add the missing zero-shot results for fairseq-moe-15b** (on MRPC, WinoGrande, OpenBookQA) to substantiate the claims about decoder-only and zero-shot generalization. This is the single most important gap to address.
2. **Report results over multiple random seeds** (at least 3) for the main table to establish whether the small differences between M-SMoE and baselines are statistically reliable. If this is infeasible, add a caveat about single-run variance.
3. **Qualify the "virtually no loss" claim:** report per-task degradation and reserve the "virtually no loss" language for tasks where the drop is ≤1%.
4. **Add a controlled comparison** of C-SMoE and MC-SMoE at the same parameter count (e.g., compress C-SMoE to 381M) to more cleanly isolate the benefit of merging on compressibility.
5. **Report the computational overhead** of the permutation alignment step so readers can weigh its modest 0.7% gain against its cost.

## Score and Decision

The paper makes a novel contribution — routing-policy-guided expert merging for SMoE — that is well-motivated, empirically validated on 8 benchmarks for the switch-base-32 encoder-decoder model, and supported by thorough ablations. The main weakness is a significant evidential gap: zero-shot/decoder-only results are promised but absent. This is addressable and does not invalidate the core contribution. The overclaimed "virtually no loss" phrasing should also be corrected. With these addressed, the paper would be strong.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
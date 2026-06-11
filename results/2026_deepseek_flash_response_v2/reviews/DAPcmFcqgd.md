Now I have sufficient calibration data. Let me construct the final review.

## Final Calibration Assessment

**Round 1 bracket**: Between 4 and 6 — clearly above weak MoE papers (~3.0) and clearly below top-tier papers (~8.0).

**Round 2 narrowing**: Compared against MoTE (4.75), MoLE (5.00), SMEAR (6.00), MoLEx (6.33):
- MoEP's architecture is novel but its evaluation is notably weaker than all these anchors
- The key missing piece — no ablation study — is a gap that all comparable papers fill
- MoEP is closest to MoTE (4.75) but lacks MoTE's extensive ablations (56 datasets)

**Final score**: 4.5 — Research-worthy idea but insufficiently rigorous evaluation for acceptance.

**All retrieved anchors**:
- NanoMoE (3.00, R1): Toy experiments only — MoEP clearly better
- MoEfication (3.40, R1): Weak validation — MoEP clearly better
- Collective Model Intelligence (3.40, R1): Not directly comparable
- ViMoE (3.00, R1): Vision MoE study — MoEP more rigorous
- LokiLM (3.60, R1): Off-topic abstract — not comparable
- NanoLM (5.50, R1): Better-validated contribution — MoEP weaker
- Need a Small Specialized LM (6.00, R1): Better experiments — MoEP weaker
- Studying Effects of Training Data (5.50, R1): Cleaner study — MoEP weaker
- MoE++ (8.00, R1): Top-tier, thorough — MoEP far weaker
- Diff Transformer (8.00, R1): Top-tier — MoEP far weaker
- MoTE (4.75, R2): Similar MoE architecture paper with better ablations — MoEP slightly weaker
- SMEAR (6.00, R2): Cleaner evaluation — MoEP weaker
- MoLEx (6.33, R2): Broader validation — MoEP weaker
- LLM Routing (4.25, R2): Different problem — not directly comparable
- Gradient Routing (5.25, R2): Better hypothesis testing — MoEP weaker
- Fantastic Experts (4.33, R2): MoE sparsification study — comparable quality
- MoLE (5.00, R2): Similar novelty level, better experiments — MoEP slightly weaker

Now let me write the final review.

Actually, let me reconsider one more time. The paper's strengths are real - it has a novel architecture, fixes parameter count while adding sparsity, achieves competitive results on BabyLM. The weaknesses are real too - no ablation is the biggest one. But I want to make sure I'm not underrating the paper.

The paper introduces MoEP as a new architecture for sparsity with fixed parameters. The evaluation on BabyLM is legitimate - it's a standard benchmark. The results show MoEP has competitive macro averages. The idea of using reduced-dimension parallel blocks with MoE transitions is novel.

But the lack of any ablation that isolates the routing mechanism is a significant gap. Without it, the paper can't distinguish between the effect of routing and the effect of just having a different depth/width configuration. The headline claim is also somewhat overstated.

I'll stick with 4.5 - this is a borderline paper with an interesting idea but evaluation gaps that prevent acceptance in current form.Now let me compose the final review.

## Summary

MoEP proposes a decoder-only architecture that achieves token-level sparsity while keeping total parameters identical to a dense GPT-2 baseline (28M). It interleaves two full-size GPT-2 layers with a middle stack of parallel blocks operating at reduced dimensionality, using top-k routing at both the MoE shrink/grow transitions and the parallel-block level. Evaluation on the BabyLM strict-small track (~10M words) shows competitive macro averages.

## Strengths

- **Fixed-parameter sparsity is concretely demonstrated**. Table 2 shows MoEP (28M parameters) matches the GPT-2 baseline parameter count while achieving sparse token activation. This cleanly distinguishes MoEP from standard MoE approaches that substantially increase total parameters.

- **Competitive BabyLM results with transparency**. MoEP achieves the highest macro average including AoA (44.50, Table 1), and all individual task scores are reported without cherry-picking. The paper is transparent about which tasks favor which models.

- **Clean dimensionality-transition design**. The MoE shrink/grow blocks (Section 3.2) provide a principled mechanism for routing between full-size and reduced-dimension parallel layers, avoiding abrupt dimensionality changes that could cause information bottlenecks.

- **Reproducibility-oriented setup**. Shared seed, pre-tokenized data ensuring identical training examples, and released code/weights.

## Weaknesses

### Major

1. **No ablation isolates the routing mechanism — the central claim is unevaluated in isolation.** The paper compares MoEP (2 full-size dense layers + 10 reduced-dimension parallel layers with routing) against GPT-2 (12 full-size dense layers). These differ in depth (2+10 vs 12), per-layer width (384 vs 192 in parallel blocks), and the number of full-size layers (2 vs 12). Without ablations that hold the architecture constant and vary only the routing — e.g., random routing with the same sparsity pattern, dense averaging of all parallel blocks, or a single parallel block at full dimension — there is no way to attribute the observed performance to sparse routing. This is a fundamental gap because the paper's core contribution *is* the routing mechanism.

2. **Headline claim is conditionally supported but the introduction overstates it.** The abstract and introduction state MoEP "outperforms all BabyLM strict-small baseline models, including GPT-2 and GPT-BERT." This is true only when the AoA task is included in the macro average. When AoA is excluded, GPT-BERT (causal) scores 54.10 vs MoEP's 49.00 — a 5+ point deficit (Table 1). Section 5.1 does include the caveat ("when the AoA task score was included"), but the paper's framing in the abstract and introduction does not, creating a mismatch between the advertised claims and the evidence.

### Minor

3. **Missing training details that affect reproducibility.** The auxiliary loss weight values λ^block and λ^expert (Equation 3) are not reported. Only a single seed (42) is used, so there are no variance estimates — the performance differences (e.g., MoEP 49.00 vs GPT-2 48.10) could be within noise.

4. **Checkpoint selection procedure is unclearly separated from evaluation.** The paper selects the best checkpoint via "fast evaluation" and then runs "full evaluation" on that checkpoint. It does not clarify whether the fast evaluation set is independent of the official evaluation tasks. If they overlap, the reported scores are optimistically biased.

5. **Training dynamics analysis does not deliver what Contribution 3 promises.** Contribution 3 claims to "analyze expert networks routing behavior" and show "fast and stable training." The actual analysis (Appendix A.3) only shows learning curves — there is no examination of expert utilization, routing entropy, specialization across blocks, or any routing-level analysis.

6. **Load-balancing loss (Equation 2) is non-standard and un-justified.** The paper uses negative entropy (-∑ p_i log p_i) as the balancing regularizer. Standard MoE practice (Switch Transformers, DeepSeek, Mixtral) uses auxiliary losses based on load coefficient-of-variation or squared excess. The entropy formulation encourages uniform probabilities but does not directly penalize load imbalance — a router could assign uniform probabilities across a batch while still collapsing all tokens to one expert if the gate's softmax temperature is low. The paper neither justifies this choice nor compares it to alternatives.

7. **No inference efficiency metrics.** Despite framing the work around efficiency and sparsity, the paper reports no FLOPs, speed, or throughput comparisons between MoEP and the dense baseline.

### Trivial

- The top-k value for routing is stated only in the hyperparameter table (Table 2), not in the routing description in Section 3.

## Nice-to-Haves

- Multiple seeds (3+) with standard deviations to assess result stability.
- Controlled ablations as described in item 1 above (these are important enough to be in the main body).
- Ablation of the checkpoint selection procedure: report results from the final checkpoint, not just the best fast-evaluation checkpoint.
- Analysis of routing patterns (expert utilization histograms, routing entropy over training) to substantiate Contribution 3.
- Reporting λ_block and λ_expert values, and a brief justification or ablation of the entropy-based balancing loss vs. standard alternatives.

## Removed Points

These points were flagged for removal but may contain useful context:

- **"MoEP-SwiGLU undermines the approach's claim"** (Harsh Critic): This is an honest experimental result — the variant underperforms, and the paper acknowledges it. Presenting negative results is a scientific strength, not a weakness.
- **"Framing in terms of large-scale MoE is inapt"** (Harsh Critic): The paper explicitly acknowledges the small-scale limitation in the conclusion. The contextual framing in the introduction is standard practice.
- **"GPT-BERT dominates most individual tasks"** (Harsh Critic): All individual scores are reported transparently in Table 1. The paper claims the "highest count" of best-scored individual tasks (5), which is a narrow but accurate statement.
- **"The conclusion doubts whether it scales"** (Harsh Critic): Candid discussion of limitations is a strength, not a weakness.
- **"Faster convergence"** (Strength Finder): Partially supported (Appendix A.3) but not rigorously quantified.
- Generic strengths about "importance of the problem" (Strength Finder): Removed as lacking specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run controlled ablations:** Hold the MoEP architecture fixed and compare (a) top-k routing, (b) random routing with the same sparsity pattern, (c) dense averaging of all parallel blocks, and (d) a single parallel block at full dimension (d=384). This would isolate what the routing contributes.

2. **Tone down the headline claim** to accurately reflect the conditionality (AoA-included macro average). The abstract should say "outperforms GPT-2 and achieves competitive macro averages against GPT-BERT on BabyLM" rather than claiming to outperform "all" models.

3. **Report multiple seeds and variance** for all reported scores.

4. **Clarify the checkpoint selection protocol** — specify whether the fast-evaluation set is independent of the official BabyLM evaluation tasks.

5. **Report λ_block and λ_expert values** and justify the entropy-based balancing loss, or replace it with a standard alternative.

6. **Measure and report inference FLOPs** or wall-clock speed to substantiate the efficiency framing.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
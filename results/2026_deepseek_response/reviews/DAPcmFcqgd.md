Now I have sufficient calibration data. Let me finalize the review.

**Bracket Summary:**
- Round 1 bracket: The paper sits between the weak anchors (~3.0-3.4, papers with fundamental flaws) and strong anchors (~8.0, well-executed thorough papers). Middle anchors range from 4.25–6.33.
- Round 2 narrowing: The closest comparators are Q-Sparse (4.75, missing FLOPs/efficiency evidence), Inheritune (5.00, interesting idea but incomplete validation), Sparsing Law (5.25, exploratory but not comprehensive), and NanoLM (5.50, better validated). This paper has more novelty than the weakest anchors but falls short on experimental rigor compared to the 5.5-6.3 range.

Final score: **4.5**

## Summary
MoEP (Modular Expert Paths) proposes a decoder-only architecture that integrates layer-level parallel Transformer blocks with Mixture-of-Experts routing, achieving sparsity while keeping total parameters fixed (28M, matching GPT-2). The method uses a shrink → parallel layers (with top-k gating) → grow structure at reduced hidden dimension. Evaluated on BabyLM strict-small, MoEP achieves 49.00 macro average (excluding AoA), slightly outperforming its own GPT-2 baseline (48.10) and the official BabyLM GPT-2 baseline (46.60), but underperforming GPT-BERT variants (54.10, 53.65, 52.40) on the same metric.

## Strengths

1. **Novel architecture for fixed-parameter sparsity** — MoEP's design of operating parallel blocks at reduced hidden dimension (d_P=192 vs d_L=384) while keeping total parameters matched to GPT-2 (28M, Table 2) is a legitimate architectural contribution. The paper demonstrates that sparse routing can be added without blowing up the total parameter count.

2. **Controlled experimental setup** — All models use the same BPE tokenizer (16K vocab), same BabyLM strict-small training data, and an epoch-based shared seed ensuring identical example ordering. This reduces confounding variables when comparing against the paper's own GPT-2 baseline.

3. **Training dynamics analysis** — Appendix A.3 provides checkpoint-level analysis showing MoEP reaches near-optimal evaluation by 30M words, while GPT-2's best scores occur at different checkpoints for different tasks. This supports the claim that sparse routing accelerates early pattern discovery.

4. **Reproducibility** — Code and model weights are released on Hugging Face.

## Weaknesses

### Major

1. **Overclaim in the introduction about "outperform[ing] all BabyLM strict-small baseline models" (line 31)** — This unqualified claim is misleading. On the macro average excluding AoA—which reflects the bulk of the evaluation—MoEP (49.00) is substantially below GPT-BERT causal (54.10), focus-causal (53.65), and mixed-causal (52.40). The claim only holds when AoA is included (44.50 vs. 41.20/40.00/39.20), which inflates MoEP's position because GPT-BERT variants score negatively on AoA (−3.90 to +14.50). The results section (line 166) qualifies this better, but the introduction's blanket statement is inaccurate.

2. **No ablation studies** — The method combines (i) layer-level parallel blocks with top-k routing, (ii) MoE shrink/grow projections, (iii) entropy-based load-balancing loss, and (iv) a specific routing objective. No experiment removes or varies any component to measure its individual effect. Without ablations, the +0.9 point improvement over the paper's GPT-2 (49.00 vs. 48.10) cannot be attributed to the architecture versus hyperparameter tuning or random variation.

3. **No statistical significance or multiple seeds** — The reported improvement is 0.9 points on macro average with single-seed runs and no confidence intervals. This difference could easily be within noise. Standard practice in this setting is to report variance across multiple seeds.

4. **Load-balancing loss is non-standard with λ coefficients unreported** — Equation (2) defines the balancing loss as \(-\sum_i p_i \log p_i\) (entropy of routing probabilities). The paper calls this "the standard load-balancing regularizer" (line 126), but the standard MoE auxiliary loss (Switch Transformers, Fedus et al. 2022) penalizes imbalance in expert load via squared coefficient of variation or importance weighting. The entropy formulation is different and not obviously equivalent; maximizing entropy pushes routing toward uniform, which may conflict with expert specialization (the goal of MoE). The paper provides no justification, no comparison, and no expert utilization statistics. Additionally, the balancing coefficients λ^{block} and λ^{expert} from Equation (3) are never specified in the paper, preventing reproduction.

### Minor

5. **MoEP-SwiGLU comparison confounded by parameter count** — MoEP-SwiGLU has 38M parameters vs 28M for MoEP and GPT-2 (a 35% increase), yet the paper attributes its worse performance to "lightweight linear experts being more effective at small scale" (Section 5.1). This conflates architecture type with parameter scale; the conclusion is not justified.

6. **No computational cost analysis** — The paper claims "efficient sparsity" but reports no FLOPs, throughput, or inference latency comparisons. The MoE shrink/grow modules and top-k routing with parallel blocks may add overhead compared to a dense forward pass. It is unclear whether the sparsity translates to real efficiency gains.

7. **No expert utilization statistics** — Since the entire mechanism depends on stable routing, the paper should report expert load distribution, utilization histograms, or collapse metrics to validate that the entropy-based regularizer actually prevents collapse.

### Trivial

8. The balancing coefficients λ^{block} and λ^{expert} are missing from the paper and appendix.
9. Table 1 uses dashes for models not evaluated on AoA, which is explained but could be slightly clearer.

## Nice-to-Haves
- Sensitivity analysis of key hyperparameters (P, k, E).
- Comparison against a dense model operating entirely at d_P dimension to isolate the benefit of parallelism.
- FLOPs or parameter activation fraction reporting.

## Removed Points
- **"Compact not demonstrated because same params as GPT-2"** — Removed: the paper's claim is specifically about adding sparsity without *increasing* total parameters, which is demonstrated by matching GPT-2 at 28M. The parameter count equality is by design, not a weakness.
- **PaPaformer paragraph confusion** — Removed as too vague and not threatening the core contribution.
- **Table 1 AoA inconsistency / confusion complaint** — The table is clearly explained in the caption; both macro averages are reported. Removed.
- **Missing related works / missing appendix content** — Removed per rules (parser strips appendices; all papers have this).
- **Formatting/style nitpicks** — Removed per rules (parser artifacts).
- **Scaling limitation "undercuts contribution"** — The paper honestly acknowledges this limitation in Section 6; it's a reasonable scope statement, not a flaw.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Qualify the performance claim in the introduction to accurately reflect which models are outperformed under which metric (with/without AoA).
2. Add ablation experiments: (a) remove the MoE shrink/grow, (b) replace parallel-layer routing with a single dense layer, (c) remove the balancing loss.
3. Report results with 3–5 random seeds (mean ± std) for the key macro average comparison.
4. Specify λ^{block} and λ^{expert} values and justify—or replace—the entropy-based balancing loss.
5. Report throughput (tokens/sec) and FLOPs for MoEP vs. GPT-2 to substantiate the efficiency claim.
6. Report expert utilization histograms (load distribution across experts).

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): MOEfication (3.40, Reject) — MoEP is clearly stronger; has a working architecture.
- Middle band (3.5–7.5): LLM Routing w/ Benchmarks (4.25, Reject), Plan Early (6.00, Reject), RouteLLM (6.33, Accept), CoTFormer (5.75, Accept), Inheritune (5.00, Reject).
- Strong band (>7.5): MoE++ (8.00, Accept) — far more rigorous evaluation than MoEP.

**Round 2 (Narrowing within ~4–6):**
- Q-Sparse (4.75, Reject) — Similar weakness: efficiency claims without measured speedup, missing comparisons. MoEP is comparable in quality.
- Inheritune (5.00, Reject) — Clearer story and validation but also incomplete evaluation. MoEP is slightly below due to overclaiming.
- Sparsing Law (5.25, Reject) — Decent exploration but findings not comprehensive enough. Comparable quality both ways.
- NanoLM (5.50, Reject) — Better validated with clear contribution. MoEP is below this.
- Fantastic Experts (4.33, Reject) — Comprehensive study but limited novelty. MoEP has more novelty but less rigor.

**Final position:** The paper has a genuinely novel architecture and a controlled setup, placing it above the 3–4 range. However, the misleading framing in the introduction, absence of ablations, single-seed results, unreported λ coefficients, and lack of efficiency validation place it below the 5.5–6.3 range. Most comparable to Q-Sparse (4.75) and slightly below Inheritune (5.00).

**Score: 4.5** — The core architectural idea is interesting and the BabyLM evaluation is a fair testbed, but the experimental validation is insufficiently rigorous and the central performance claim is overstated. Substantial revisions are needed.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
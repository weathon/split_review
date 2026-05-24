Now I have a good calibration. Let me write the final review.

My round-1 bracket: 3.5 to 5.5, based on comparisons with "Low Rank Experts" (3.00, withdrawn), "MoEsturizer" (3.50, reject), "ReXMoE" (4.40, reject), and "MoE Can Surpass Dense" (5.00, oral accept). The current paper is stronger than the first two but comparable or slightly weaker than the latter two on experimental thoroughness.

## Summary

This paper proposes MoEP (Modular Expert Paths), a sparse decoder-only architecture that interleaves dense GPT-2 layers with a middle stack of parallel Transformer blocks operating at reduced hidden dimension, using top-k token routing at both the block level and the expert (shrink/grow projection) level. Unlike standard MoE which increases total parameters, MoEP keeps the total parameter count fixed (28M) by compensating for the additional parallel blocks through lower per-block dimensionality. The method is evaluated on the BabyLM strict-small track and compared against GPT-2 and GPT-BERT baselines. The core architectural idea—layer-level MoE with parameter-preserving sparsity—is genuinely novel and clearly presented.

## Strengths

- **Parameter-preserving sparsity**: MoEP achieves sparse token routing while keeping total parameter count identical to the dense GPT-2 baseline (28M), as shown in Table 2. This is a genuine departure from standard MoE, which inflates total parameters. The paper clearly explains that parallel blocks operate at reduced dimension (d_P) to offset the increase from additional blocks.

- **Faster early training convergence**: Appendix A.3 shows MoEP reaches its best fast-evaluation scores at 30M words, with nearly all task scores at or above their task-specific means, while GPT-2 peaks less consistently. This supports the claim that "modular sparse routing can provide better sample efficiency" (Section 5.1).

- **Controlled within-study comparison**: The authors train their own GPT-2 baseline with the same tokenizer, data, and training procedure (Section 4), and MoEP outperforms this baseline on both macro averages (49.00 vs 48.10 excluding AoA; 44.50 vs 37.40 including AoA). This provides a fairer comparison than relying solely on external leaderboard numbers.

- **Novel layer-level MoE placement**: The paper correctly identifies that layer-level expert networks are "relatively unexplored" (Section 2.2.2) and proposes a specific instantiation where parallel blocks at reduced dimension act as experts with top-k gating—distinct from the more common FFN-level or attention-level MoE.

- **Honest limitations section**: Section 6 acknowledges that training was on a small dataset and under strict compute budget, and that scaling to larger sizes and more complex data may change the relative performance profile.

## Weaknesses

### Fatal

None.

### Major

- **Macro-average computation is insufficiently explained.** The footnote to Table 1 says "the first excludes the AoA result obtained from the Hugging Face leaderboard, while the second represents the overall text-average," but the paper never defines how these are computed. A simple arithmetic mean of the 13 non-AoA columns in Table 1 yields ~52.7 for MoEP, yet the reported number is 49.0 (the same pattern holds for the authors' GPT-2: simple mean ~51.9 vs reported 48.1). This gap strongly suggests that the macro average is computed over individual sub-tasks in the BabyLM pipeline, not over the grouped columns shown. The paper must state this explicitly; otherwise, readers cannot verify the headline numbers that underpin the paper's central performance claims.

- **The Introduction makes an unqualified claim that is contradicted by the paper's own data.** The Introduction states: "Under the official evaluation, MoEP was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well." Yet on the standard macro average excluding AoA, GPT-BERT (causal) achieves **54.10**, well above MoEP's **49.00**. The claim only holds when AoA is included. Section 5.1 properly includes the qualifier "when the AoA task score was included in the Macro Average," but the Introduction does not. This inconsistency needs to be resolved by either adding the qualifier to the Introduction or framing the results more cautiously.

### Minor

- **The load-balancing loss coefficients λ^block and λ^expert are not reported.** Equation (3) defines them, and Table 3 gives training hyperparameters, but the λ values are absent. These coefficients directly affect whether the routing collapses or remains diverse, so they matter for reproducibility.

- **The "Top k: 2" entry in Table 2 does not specify whether it applies to MoE expert routing, parallel-block routing, or both.** Section 3.3 describes block-level top-k and Section 3.2 describes expert-level top-k, but only one value is given. The paper should clarify whether k_block = k_expert or they differ.

- **The Hugging Face baselines were not re-trained under controlled conditions.** While the primary comparison (own GPT-2 vs MoEP) IS controlled, the paper also compares against GPT-BERT and official GPT-2 baselines that were trained with different tokenizers, schedulers, seeds, etc. The paper should either acknowledge this limitation more prominently when making claims of "outperforming all baselines," or add controlled re-runs of GPT-BERT.

### Trivial

- The bar for "MoEP (SwiGLU)" in Table 2 has "Liner" instead of "Linear" as the MoE FF type.

## Nice-to-Haves

- **Ablation studies on architectural choices**: The paper does not analyze how varying the number of parallel blocks (P), number of experts (E), top-k value, or dimension ratio d_L/d_P affects performance. Any single ablation would strengthen the paper's claim that the design choices are sensible.

- **Wall-clock speed comparison at inference**: The paper argues MoEP activates fewer parameters per token but does not report actual inference throughput or latency relative to GPT-2.

- **Routing statistics beyond learning curves**: The paper claims to "analyze expert networks routing behavior" but only shows aggregated learning curves (Appendix A.3). Statistics on load balance (expert/block utilization histograms, routing entropy, collapse analysis) would substantiate this claim.

## Removed Points

- **"Macro-average numbers are inconsistent / arithmetic mean is 52.7 not 49.0"** — This criticism assumes the macro average is a simple mean of the 13 grouped columns. It is not; the same calculation for GPT-2 (our) gives 51.9 vs reported 48.1, confirming the macro average is computed over individual sub-tasks, not grouped columns. The issue is insufficient clarity, not numerical inconsistency. Moved to Major as "insufficiently explained."

- **"Load-balancing loss is non-standard"** — The paper uses negative entropy of average routing probabilities. While this differs from Switch Transformer's squared-load penalty, it is a standard and well-understood diversity regularizer. The paper describes it in full. The only genuine issue is missing λ values, kept as Minor.

- **"MoE expert type underspecified"** — The paper says "experts are simple linear projections" for baseline and "SwiGLU" for the variant. This is sufficiently clear.

- **"Best checkpoint selection means models not compared at same training budget"** — This is standard BabyLM practice and does not favor any particular model.

- **"Comparison to HF baselines not controlled is evidential failure"** — Exaggerated. The primary comparison with their own GPT-2 IS controlled. The HF baselines are secondary context, and the paper's strongest claims are about beating their own GPT-2.

- Strength Finder's "outperforms all BabyLM baselines when AoA is included" — This is factually true but incomplete: it doesn't note the Qualified nature (only when AoA is included, and GPT-BERT beats MoEP on the standard macro average). Removed to avoid giving a misleading impression of strength.

## Novel Insights

None beyond the paper's own contributions. The reviews (harsh critic + strength finder) surface the standard tension: the paper has a genuinely novel architectural idea with good within-study controls, but the evaluation presentation has ambiguities that undercut its strongest claims. The most interesting unasked question is whether the entropy-based balancing loss interacts differently with layer-level vs. FFN-level routing—this is specific to MoEP's dual-routing setup and not addressed.

## Suggestions

1. **Clarify macro-average computation immediately in Table 1's footnote.** State explicitly: "The macro average is computed by the BabyLM evaluation pipeline as the arithmetic mean over all individual sub-tasks (not over the grouped columns shown)." This single change resolves the most confusing issue in the paper.

2. **Add the AoA qualifier to the Introduction's performance claim.** Change "MoEP was able to outperform all BabyLM strict-small baseline models" to "MoEP was able to outperform all BabyLM strict-small baseline models when the AoA task is included in the macro average."

3. **Report λ^block and λ^expert values** in Table 3 or the appendix.

4. **Clarify whether Top k: 2 applies** to expert routing, block routing, or both.

5. **Add a small ablation**—varying P or top-k—to give the reader a sense of architectural sensitivity. Even a single extra row in Table 2 would help.

## Score and Decision

I now calibrate using my retrieved anchors.

**Round 1 bracket**: [3.5, 5.5]

**Round 2 narrow anchors considered** (in the 4.0–5.5 range):
- ReXMoE (4.40, reject): Novel MoE architecture but criticized for prefill slowdown and limited improvement over baselines. MoEP has a cleaner architecture story and equally clear evaluation, but weaker ablation coverage. MoEP is comparable or slightly weaker → score near 4.0–4.5.
- MoE Can Surpass Dense (5.00, oral accept): Large-scale (2B/7B models) but mixed reviews (4,4,4,8). MoEP is smaller-scale but asks a related question. MoEP is weaker on experimental thoroughness → score below 5.0.
- MoEsturizer (3.50, reject): Small LM MoE upcycling with limited novelty. MoEP has more architectural novelty → score above 3.5.
- "Low Rank Experts" (3.00, withdrawn): Similar parameter-matched sparsity idea but was criticized for loss spikes and load imbalance. MoEP is cleaner → score above 3.0.

The paper sits between 3.5 and 5.0 — clearly better than the weaker anchors (LoRE, MoEsturizer) but lacking the experimental scale of the 5.0 anchor. The core weakness is presentational (unclear macro average, unqualified Introduction claim) rather than methodological, so with revisions the paper could move toward 5.0. In its current form, **4.5** captures the genuine architectural contribution weighed against the presentational issues that prevent the evidence from fully supporting the claims.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
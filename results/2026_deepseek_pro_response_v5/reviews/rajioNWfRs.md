Now I have sufficient anchors. Let me finalize the review.

**Round 2 Narrowing:** The Round 2 search returned mostly unrelated papers (systems, spiking networks). The most relevant comparison anchors remain from Round 1:
- PRF (5.50, rejected): similar reset mechanism for parallelization, weaker experiments
- E34AlVLN0v/DEER (6.00, accepted): directly comparable — parallelization of non-linear sequential models
- MELODI (6.25, accepted): comparable hierarchical memory concept

TNT sits between PRF (5.50) and DEER (6.00). It has stronger experiments than PRF but its central context-parallelism claim is unvalidated, placing it below DEER which had a tighter claim-evidence match.

**Final score: 5.5, Decision: Reject**

---

## Summary
TNT proposes a two-stage training paradigm for deep memory RNN modules (e.g., Titans) that decouples training efficiency from inference performance. Stage 1 uses a hierarchical memory architecture — a global memory module for long-range context and multiple local memory modules whose states are periodically reset to a learned initialization, breaking sequential dependencies. Stage 2 fine-tunes the local modules at smaller chunk sizes for inference. The paper demonstrates up to 17× training speedup over Titans baselines while achieving better perplexity (23.13 vs. 25.07).

## Strengths
- **Core architectural innovation with empirical backing (Section 4.1.1, Eq. 6):** The periodic reset of local memory states to a learned initialization \(W_{\text{init}}\) breaks sequential dependencies that previously prevented efficient parallelization of non-linear RNNs. The ablation removing global memory (necessary because the reset discards long-range context) confirms the reset is structurally consequential: perplexity jumps from 21.04 to 25.60 (Table 3).
- **Speed-quality decoupling demonstrated convincingly (Tables 1–2):** TNT reaches target loss 17.37× faster than the most accurate Titans baseline while simultaneously improving perplexity (23.13 vs. 25.07). At matched chunk size (C_L = C = 8), TNT is 7.68× faster than Titans, isolating the architectural benefit from chunk-size effects alone.
- **Linear runtime scaling at long context lengths (Figure 4):** TNT's runtime grows from ~400ms to ~550ms across 2K–32K sequences while Titans grows from ~400ms to ~4000ms. At 32K, TNT (C_L=128) is 1.3× faster than FlashAttention — a highly optimized kernel.
- **Problem diagnosis with empirical evidence (Section 3, Figure 2):** A Titans model trained at C=64 achieves PPL 13.78 at inference C=64 but degrades to 36.45 at C=8, directly motivating the two-stage approach with concrete data.
- **Q-K Projection with constant-memory implementation (Section 4.1.2, Eq. 7):** Projecting queries onto the key subspace via a running outer-product sum addresses the compression-retrieval domain mismatch. Ablation shows removal increases PPL from 21.04 to 22.01 (Table 3).
- **Clean ablation isolates each contribution (Table 3):** Hierarchical memory, Q-K projection, and Stage 2 fine-tuning are individually ablated with clear quantitative impact.
- **Comprehensive baseline coverage (Table 2):** Compares against Titans, TTT, DeltaNet, GatedDeltaNet, and Transformers (with/without gating, with/without FlashAttention), covering both deep and linear memory architectures.

## Weaknesses

### Fatal
None.

### Major
- **Context parallelism — the paper's most prominently advertised innovation — is never experimentally validated.** The abstract states the reset mechanism "enables massive context parallelization," the introduction describes it as enabling "massive context parallelization" for non-linear RNNs, and Section 4.1.1 claims it "enables true context parallelism for the fine-grained local memory modules." The reset does theoretically break sequential dependencies, but no experiment demonstrates distributed context parallelism (e.g., varying the number of context-parallel shards or devices and measuring throughput scaling). The experiments use a TPUv4 pod with model parallelism 2 on a fixed 0.5M token batch — not context parallelism. The observed speedups in Figure 4 could be entirely attributable to larger chunk sizes and reduced sequential overhead on a single device. This is not an abstract theoretical concern; it is a gap between what the paper claims as a central contribution and what it actually demonstrates.
- **Stage 2 fine-tuning provides negligible empirical benefit despite being presented as a co-equal framework component.** The best Stage 1 model achieves 23.13 average perplexity; the best Stage 2 model achieves 23.09 — a difference of 0.04. On common-sense reasoning, Stage 1 peaks at 41.0% accuracy while Stage 2 peaks at 40.9%. For a claimed 5% compute overhead, Stage 2 produces no meaningful improvement. Section 4.2 is dedicated to this stage, and the contribution list (Section 1) presents it as a separate contribution. The evidence does not support this framing. While Stage 2 may serve the purpose of adapting models to small inference chunk sizes, the quality numbers provide no evidence of value.

### Minor
- **The headline 17× speedup is measured against the slowest Titans configuration.** Table 1 compares TNT (C_L=64, 1.12 hrs) against Titans (C=8, 19.48 hrs). Titans with C=128 trains in 3.71 hrs, reducing the speedup to roughly 3.3× against a comparable-chunk configuration. The C=8 variant is the most accurate Titans baseline (PPL 25.07 vs. 27.13 for C=256), so the comparison is defensible, but the framing in the abstract and conclusion should more precisely contextualize the speedup as applying within the RNN family specifically. The paper does acknowledge in Section 5.2 that Transformers remain faster.
- **Parameter accounting across TNT variants is opaque.** The paper states all models are 150M parameters but never explains how parameters are allocated between the global module and N local modules. When the ablation adds local modules (1→2→3→4, Table 3), perplexity improves from 21.04→20.74→20.47→20.15. If each module maintains independent capacity, these gains may partially reflect increased parameter count rather than the benefit of hierarchical multi-resolution processing.
- **The abstract states "Evaluated on Titans and TTT models," but no TNT+TTT experiments exist.** TTT appears only as a baseline in Table 2. No experiments apply TNT's hierarchical memory, Q-K projection, or two-stage training to a TTT backbone. This is a factual discrepancy between the abstract and the experimental content.

### Trivial
- The Q-K projection's O(d²) memory cost per local module is mentioned only via a reference to Appendix C (stripped in this version). A brief note in the main text would improve transparency.
- The relationship between global chunk size C_G (2048) and local shard length S_L (2048 or 4096) is not explicitly discussed, despite being the two key hyperparameters governing the hierarchy.

## Nice-to-Haves
- Benchmarks of inference throughput (tokens-per-second) for TNT vs. baseline Titans at matched parameter counts would strengthen the practical value proposition.
- Direct demonstration of context-parallel scaling (1, 2, 4, 8 shards with throughput measurement) would validate the paper's most ambitious claim.
- Error bars or variance estimates for perplexity and accuracy would help contextualize small claimed improvements, though single-run evaluation is standard at this scale.

## Removed Points
These points are flagged as removed — treat them with caution.

- **Harsh Critic: "Challenge 2 is overcharacterized relative to evidence."** The paper provides empirical support for Challenge 2 (ablation: Q-K projection removal increases PPL from 21.04 to 22.01). The critic's judgment about "overcharacterization" is subjective, not a factual error. REMOVED.
- **Harsh Critic: "Missing Table 4."** Table 4 is referenced in the text but belongs to the stripped appendix. This is a parser artifact, not an author error. REMOVED per hard rules.
- **Harsh Critic: "No error bars."** Single-run evaluation for 150M-parameter language models trained on 10B tokens is standard practice. Moved to Nice-to-Haves.
- **Harsh Critic: "Inference cost undiscussed."** The paper's focus is training efficiency. Inference cost analysis would strengthen the paper but is not central to its claims. Moved to Nice-to-Haves.
- **Strength Finder: "Stage 2 fine-tuning is cost-effective and consistently beneficial."** While Stage 2 produces consistent micro-improvements, the 0.04 PPL gain is negligible. This strength conflicts with verifiable weakness evidence (Table 2: 23.13→23.09). REMOVED.
- **Harsh Critic: "The 17× speedup is compared to the slowest baseline."** The comparison is against the most accurate Titans baseline (C=8, PPL 25.07), which is indeed the relevant quality-matched comparison. The paper also reports matched-chunk speedup (7.68×). The concern is about framing, not correctness. Weakened and retained as Minor.
- **Strength Finder: generic strengths about "problem importance."** The paper targets an important problem (deep RNN training bottlenecks), but this is a generic observation, not a paper-specific strength. REMOVED.

## Novel Insights
None beyond the paper's own contributions. The core insight — that periodic state resets in local memory modules can break sequential dependencies to enable parallelism while a global module compensates for lost context — is a genuinely novel architectural contribution to the deep RNN training literature.

## Suggestions
- **Either demonstrate context-parallel throughput scaling or soften claims.** The paper's strongest path to validating its central claim is to run TNT with 1, 2, 4, and 8 context-parallel shards and measure throughput scaling. Alternatively, the language about "massive context parallelization" should be tempered to reflect that the demonstrated gains come from larger chunk sizes and reduced sequential overhead.
- **Reframe Stage 2 as a lightweight adaptation step** rather than a co-equal framework component, given its marginal empirical benefit (0.04 PPL). The two-stage framing is currently heavier than the evidence warrants.
- **Clarify parameter allocation** across global and local modules, particularly for the multi-module ablation in Table 3.
- **Correct the abstract** to reflect that TNT was evaluated on Titans only, or add TNT+TTT experiments.

## Score and Decision

### Calibration Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| N581Nje6fH (episodic decision making) | 1.50 | R1 | Far below — not comparable |
| bntJK4NyIW (decentralized training) | 2.00 | R1 | Far below |
| 4ymHtDAlBv (FSFC RNN) | 2.33 | R1 | Far below |
| A6K4aqReoF (binary activation RNN) | 3.75 | R1 | Below — narrower scope |
| HEcbGXzIHK (episodic memory theory) | 4.25 | R1 | Below — theory-only paper |
| GrmFFxGnOR (Were RNNs All We Needed) | 5.00 | R1 | Below — limited experiments, novelty concerns |
| Hjk1tWIdvL (HASA sparse attention) | 5.00 | R2 | Below — narrower contribution |
| e1Z4NCQ146 (ProTrain) | 5.25 | R2 | Below — systems paper |
| PRF/OujTnpmAZG (parallel spiking neurons) | 5.50 | R1 | Slightly below — similar reset mechanism but weaker experiments |
| E34AlVLN0v (DEER, parallel non-linear) | 6.00 | R1 | Slightly above — comparable novelty with closer claim-evidence match |
| 7iuFxx9Ccx (Slimmable TTT) | 6.00 | R2 | Above — different topic |
| TvGPP8i18S (MELODI) | 6.25 | R1 | Above — more thorough experiments |
| LY3ukUANko (Zoology) | 6.33 | R1 | Above — more comprehensive |
| xwKt6bUkXj (emergent RNN mechanisms) | 6.75 | R2 | Above — different topic |
| tyEyYT267x (SAR diffusion) | 8.00 | R1 | Far above |

**Round 1 bracket:** 5.0–6.5  
**Round 2 narrowing:** TNT is stronger than the 5.0–5.25 anchors but weaker than the 6.0+ anchors due to its two Major weaknesses (unvalidated context parallelism claim and negligible Stage 2 benefit). The closest comparison is PRF (5.50, rejected) and DEER (6.00, accepted). TNT is comparable to PRF in having an unvalidated parallelism claim, but has stronger experiments overall. It falls below DEER, which had a tighter match between claims and evidence. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
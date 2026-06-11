Now I have a clear picture. Let me compare MoEP against the key anchors:

- **NanoMoE (3.00)**: Novel MoE building blocks, but only toy experiments and tiny text classification. MoEP has a significantly more thorough evaluation (14-task BabyLM pipeline, matched training conditions, multiple baselines), so MoEP is clearly better.
- **MoIN (4.50)**: Novel MoE concept (introvert experts), trains at 1.1B scale but doesn't consistently outperform baselines. MoEP has a cleaner controlled comparison but smaller scale. Similar tier of contribution quality.
- **PERFT (5.33)**: More comprehensive framework with extensive experiments on OLMoE-1B-7B and Mixtral-8×7B. MoEP is clearly weaker in experimental scale and thoroughness.

MoEP sits between NanoMoE (3.00) and MoIN (4.50), closer to the lower end given the intro overclaim and fragile 0.9-point margin with single seed. I'll score it **3.5**.

---

## Summary
MoEP introduces a decoder-only architecture that combines layer-level parallelism with Mixture-of-Experts top-k routing to achieve token-level sparsity while keeping total parameter count fixed (28M), matching a standard GPT-2 baseline. Evaluated on the BabyLM strict-small track across 14 tasks, MoEP shows a modest 0.9-point macro-average improvement over a matched dense GPT-2 (single seed) and demonstrates faster convergence. The paper also ablates a SwiGLU-based variant, finding that lightweight linear expert projections outperform heavier SwiGLU-based ones at this small scale.

## Strengths
- **Parameter-matched sparsity with concrete evidence**: Table 2 directly shows MoEP uses 28M total parameters, identical to the GPT-2 baseline, while introducing top-2 routing among 4 parallel blocks and 4 MoE experts — achieving sparsity without the parameter bloat that typically accompanies MoE architectures. This is a genuinely rare property in the MoE literature and a meaningful architectural contribution.
- **Clean ablation via MoEP-SwiGLU variant**: The comparison between MoEP (linear projections, 28M, peaks at 30M words) and MoEP-SwiGLU (SwiGLU projections, 38M, peaks at 80M words) yields the non-obvious and actionable insight that lightweight linear expert projections are more effective than SwiGLU at small scale, running counter to common practice in larger MoE models.
- **Honest scope delineation**: The conclusion (Section 6) explicitly acknowledges the small-data limitation and uncertainty about whether the approach scales — accurately framing the contribution as a proof-of-concept rather than overclaiming.
- **Reproducible setup**: Code released, model weights on HuggingFace, training on a single A100 in 1–2 hours, standardized BabyLM pipeline with documented hyperparameters.

## Weaknesses

### Fatal
None.

### Major
- **The introduction overclaims relative to GPT-BERT**: The introduction (line 31) states MoEP "was able to outperform all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well." This is only true when the AoA score is included in the macro average. When AoA is excluded, GPT-BERT (causal) achieves 54.10 vs. MoEP's 49.00 — a gap of over 5 points in GPT-BERT's favor. All three GPT-BERT variants outperform MoEP by 3–5 points on the AoA-excluded metric. While the Analysis section (lines 166–170) is more careful — clarifying that MoEP outperforms the GPT-2 baseline (the primary comparison) without AoA — the introduction's unqualified claim is misleading and should be corrected.

- **The improvement over the matched dense baseline is small and untested for significance**: MoEP achieves a macro average (excluding AoA) of 49.00 vs. 48.10 for the authors' own GPT-2 — a 0.9-point difference spread across 14 tasks. All models use a single random seed (42, Table 3), with no standard deviations, confidence intervals, or multiple training runs. The authors' GPT-2 also outperforms the official BabyLM GPT-2 by 1.5 points (48.10 vs. 46.60), demonstrating that training variance is meaningful at this data scale (~100M words). The central claim that sparsity provides a benefit over a dense baseline of equal parameter count is not robustly supported by the data presented.

### Minor
- **Architecture under-specification**: The routing mechanism in the Parallel Layers (line 122) is described as a "linear router shaped d_P × P" applying "top-k selection" where "routed inputs are summed up together," but it is ambiguous whether softmax is applied to router logits and whether gate scores weight the summed outputs. The values of λ^block and λ^expert (Equation 3) are never reported numerically. These gaps prevent full re-implementation from the methodology section alone.

- **Missing ablation to isolate routing benefit**: The paper does not separate the contribution of the parallel architecture from the sparse routing. Training a version where all parallel blocks are always activated (dense parallelism, no routing) would clarify whether the benefit comes from parallelism itself or from the sparsity mechanism.

- **No computational efficiency measurements**: The paper motivates sparsity through efficiency but reports no FLOP count, wall-clock throughput, or memory usage. At 28M parameters, the routing overhead may dominate any sparse-activation benefit.

- **Limited routing behavior analysis**: Contribution #3 promises to "analyze expert networks routing behavior," but the only routing-related result is that models train without collapse. There is no analysis of token-expert assignments, expert specialization, or routing pattern evolution.

- **Checkpoint selection protocol could be better justified**: The paper selects final model weights using "fast evaluation" on all checkpoints (line 152). While using a proxy metric for checkpoint selection is common, the paper would benefit from clarifying how fast evaluation differs from full evaluation to address potential circularity concerns, and ideally would use a held-out validation split.

### Trivial
- The authors' GPT-2 and MoEP-SwiGLU rows in Table 1 lack AoA scores (listed as "–"), making it impossible for the reader to verify the AoA-inclusive macro average for these models independently.
- The introduction's framing around SOTA MoE models (Llama 4, DeepSeek-R1, GPT-OSS) sets expectations that a 28M-parameter BabyLM-scale study cannot meet; narrowing the framing would improve clarity.

## Nice-to-Haves
- Multi-seed training runs (3–5 seeds) with reported means and standard deviations would substantially strengthen confidence in the results.
- Quantitative training dynamics metrics (e.g., area under the learning curve, time-to-90%-of-peak) would convert the "faster learning" claim from qualitative observation to quantitative evidence.
- A FLOPs or throughput comparison table would ground the efficiency motivation.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Figures 3 and 4 are not visible in the parsed text"** — This is a parser artifact; the original submission includes these figures. Removed per hard rule on formatting/parser issues.
- **Harsh Critic: checkpoint selection "stacks the deck"** — The paper uses fast evaluation (likely a subset of tasks) for checkpoint selection and full evaluation for final reporting, which is a standard protocol. The claim of intentional bias is unsubstantiated speculation. Removed.
- **Harsh Critic: MoEP overfitting faster "is a liability, not a strength"** — This is a subjective reframing. The paper is transparent about overfitting and presents it alongside the faster-learning observation. Removed as opinion, not factual error.
- **Harsh Critic: layer-level MoE being "relatively unexplored" overstates the gap** — The paper does cite MoLE and related work (Wu et al., 2024). The framing is a matter of degree, not error. Removed as overly picky.
- **Harsh Critic: PaPaformer comparison "difficult to parse"** — This is a writing-quality nitpick at an isolated sentence, not a substantive weakness. Removed.
- **Strength Finder: "14 diverse tasks lending credibility through breadth"** — While factually correct, this is a generic strength that applies to any BabyLM evaluation. Kept only implicitly through the evaluation discussion.

## Novel Insights
The paper's most genuinely novel empirical finding is that at small scale (~28M parameters, ~100M training words), lightweight linear expert projections in a MoE shrink/grow configuration substantially outperform SwiGLU-based alternatives — the SwiGLU variant requires nearly 3× more training data to converge (80M vs. 30M words) and still underperforms (47.70 vs. 49.00). This runs counter to the common practice of using SwiGLU in larger MoE models and provides actionable design guidance for compact sparse architectures.

## Suggestions
- Qualify the introduction's claim about outperforming all baselines to reflect that GPT-BERT is stronger when AoA is excluded, or explicitly state that the "official evaluation" (which includes AoA) is the basis for the claim and that GPT-2 is the primary architectural comparison.
- Add an ablation with dense parallelism (all parallel blocks always active, no routing) to isolate the contribution of sparsity from the parallel architecture itself.
- Report λ^block and λ^expert values and clarify the gating mechanism (softmax application, weighted vs. uniform aggregation of top-k outputs).

## Score and Decision

**Round 1 bracketing**: Retrieved anchors across five score bands. Strong reject band (1.67–2.33) contained papers with fundamental flaws. Weak band (3.00–4.40) contained MoE-architecture papers with limited experimental validation (NanoMoE 3.00, MoE compression 4.33). Middle band (5.25–6.00) contained papers with more thorough validation but issues in novelty or scope. Upper-middle band (6.33–7.33) contained accepted MoE/routing papers with strong evidence. Strong accept band (8.00) contained papers with clear, well-validated contributions. MoEP fell clearly in the 3.0–4.5 range.

**Round 2 narrowing**: Retrieved anchors inside the bracket — NanoMoE (3.00), MoIN (4.50), PERFT (5.33), and related papers. MoEP shows a more thorough evaluation than NanoMoE (which used only toy tasks), but substantially weaker empirical evidence than PERFT (which validated on OLMoE-1B-7B and Mixtral-8×7B). MoEP is most comparable to MoIN (4.50) in having an interesting idea with insufficient evidence, but MoEP's intro overclaim and fragile 0.9-point single-seed margin pull it below MoIN.

**Anchor summary**:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| NanoMoE (04RLVxDvig) | 3.00 | R1/R2 | MoEP has more thorough evaluation but similar evidence-quality issues |
| Sparse Training (KJLqgaixgn) | 3.50 | R2 | Similar tier; MoEP has cleaner architectural contribution |
| MoE cluster pre-training (thqPibDg6A) | 4.40 | R1/R2 | More sophisticated analysis; MoEP is weaker |
| MoIN (L0PciKdHsP) | 4.50 | R2 | Comparable novel-MoE-idea paper; MoEP slightly weaker due to overclaim and tiny margin |
| PERFT (PPjpGTPG5K) | 5.33 | R2 | Much stronger experiments; MoEP clearly weaker |
| NanoLM (mao3y822aM) | 5.50 | R1 | Better validated; MoEP clearly weaker |
| ReMoE (4D0f16Vwc3) | 6.60 | R1 | Strong evidence and clear contribution; MoEP much weaker |

**Final score**: 3.5 — a paper with a genuinely interesting idea and clean setup, but whose empirical evidence is too fragile (0.9-point gap, single seed) to robustly support the central claim, and whose introduction overstates results relative to GPT-BERT.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
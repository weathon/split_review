Now I have a clear picture. Let me compare:

- **NanoMoE (3.00)**: Toy experiments only, no real LM training — MoEP is clearly stronger with BabyLM evaluation
- **MO-CTE (4.40)**: Has theory but messy execution, rejected — MoEP is comparable in quality but cleaner
- **EEP (5.25)**: Thorough experiments, clearer methodology, rejected — MoEP is somewhat weaker in evaluation rigor
- **MoLEx (6.33)**: Theory + broad eval, accepted — MoEP is clearly weaker
- **"Need a Small Specialized LM?" (6.00)**: More rigorous eval, rejected — MoEP is weaker

MoEP sits between MO-CTE (4.40) and EEP (5.25). Its architecture is genuinely novel and its evaluation is transparent, but the intro overclaim, undelivered routing analysis, and absence of ablations pull it down. I'll score it at **5.0**.

---

## Summary
This paper proposes MoEP (Modular Expert Paths), a sparse decoder-only architecture that combines layer-level top-k routing across parallel Transformer blocks with MoE-style dimension shrink/grow projections. The key claim is achieving token-level sparsity while keeping total parameter count fixed at 28M — the same as the GPT-2 baseline. Evaluated on the BabyLM strict-small track across 14 tasks, MoEP matches or slightly exceeds GPT-2 while introducing sparsity.

## Strengths
- **Architectural novelty**: The combination of layer-level routing across parallel blocks at reduced dimension with MoE shrink/grow projections, while keeping total parameters fixed at 28M (matching GPT-2, per Table 2), addresses the parameter-bloat problem of standard MoE in a genuinely interesting way. This is a clean, well-motivated idea.
- **Transparent, standardized evaluation**: Table 1 reports all 14 individual task scores with two macro averages (with and without AoA), allowing readers to verify every comparison independently. The public BabyLM pipeline and matching of training conditions (shared seed, same data, epoch-based sampling, line 150) make the comparison credible.
- **Training dynamics evidence for sample efficiency**: Appendix A.3 provides checkpoint-level analysis showing MoEP reaches peak performance at 30M words with task scores clustering near task-specific means, while GPT-2's best scores are distributed across different checkpoints without converging. This is concrete, non-aggregated evidence for the claim that modular routing accelerates initial pattern discovery.
- **Reproducibility**: Hyperparameters exhaustively reported (Tables 2, 3), public BabyLM data, code and model weights released on Hugging Face, single A100 GPU (~1-2 hours training), fixed seed (42).

## Weaknesses

### Fatal
None.

### Major
- **Introduction overclaims relative to evidence**: The introduction (line 31) states MoEP "outperform[s] all BabyLM strict-small baseline models, including the GPT-2 and GPT-BERT models as well" without qualification. Table 1 directly contradicts this under the macro average excluding AoA: GPT-BERT (causal) scores 54.10, GPT-BERT (focus-causal) 53.65, and GPT-BERT (mixed-causal) 52.40, all well above MoEP's 49.00. The claim is only true when AoA is included in the average (MoEP 44.50 vs GPT-BERT 39.20–41.20). Section 5 (line 166) properly qualifies the claim, but the introduction's unqualified framing is misleading. This is easily fixable but currently undermines the paper's credibility.

- **Promised routing behavior analysis is undelivered**: Contribution 3 states "We analyze expert networks routing behavior and show that layer level parallelism enable fast and stable training" (line 39). The paper contains no routing behavior analysis — no visualizations of which parallel blocks are selected for which tokens, no specialization metrics, no load-balancing utilization outcomes. What Appendix A.3 actually provides is training dynamics analysis (when models peak, overfitting patterns, line 351: "modular routing accelerates initial pattern discovery but may not sustain improvements throughout training"). This is a different and weaker contribution than what is claimed. The paper should either deliver routing analysis or revise Contribution 3.

- **No ablation studies to isolate routing vs. parallelism**: The architecture changes multiple things relative to GPT-2 simultaneously: (a) 12 full layers → 2 full + 10 reduced-dimension parallel layers, (b) MoE shrink/grow blocks, (c) top-k routing with load-balancing, and (d) halved hidden dimension in the parallel stack. Without a non-routed parallel baseline (all blocks active, outputs averaged) or a dimension-matched dense baseline, it is impossible to determine whether the routing mechanism specifically contributes, or whether the parallel structure alone accounts for the results. The MoEP vs. GPT-2 comparison conflates routing with parallelism.

### Minor
- **AoA handling is inconsistent across models**: MoEP's macro-average lead depends heavily on its 53.70 AoA score while GPT-BERT scores range from −3.90 to 14.50. The paper provides no explanation of what AoA measures or why MoEP would excel. Moreover, the authors' GPT-2 and MoEP-SwiGLU lack AoA scores (line 197: "our GPT-2 and MoEP-SwiGLU results do not include AoA scores, which are provided in the official BabyLM leaderboard"), creating an unexplained asymmetry. To the paper's credit, both macro averages are reported transparently.

- **Load-balancing coefficients (λ^block, λ^expert) unreported**: Equation 3 defines separate λ coefficients for block and expert load balancing, but their values are never specified. These directly affect whether expert collapse occurs and are important for reproducibility.

- **No inference-time efficiency measurement**: The title and abstract emphasize "efficiency" and "sparsity," but there is no measurement of FLOPs per token, latency, or throughput relative to GPT-2. The efficiency claim remains empirically unsubstantiated.

### Trivial
- Incomplete sentence in introduction (line 15): "Recent and previous work have examined sparse and routing-based models [...] and" trails off before line 17 restarts.

## Nice-to-Haves
- A non-routed parallel baseline would cleanly isolate routing's contribution from parallelism.
- Reporting FLOPs/token or inference latency would substantiate the efficiency claim.
- An explanation for why MoEP-SwiGLU underperforms despite 80M words of training (vs. MoEP's 30M peak) would strengthen the analysis.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"Fixed-parameter claim violated by MoEP-SwiGLU"**: The abstract's claim about fixed parameter count refers to the MoEP baseline (28M = GPT-2's 28M, Table 2). MoEP-SwiGLU is presented explicitly as a variant with SwiGLU FFN experts that naturally use more parameters. The claim is correctly scoped to MoEP.
- **"Checkpoint selection creates unfair comparison"**: The paper uses best-checkpoint selection per model (line 152), which is standard practice. The paper also transparently reports different peaking points (30M for MoEP/GPT-2, 80M for MoEP-SwiGLU), which is itself an interesting finding.
- **"Garbled text" / formatting issues**: These are parser artifacts, not author errors. Removed per instructions.

## Novel Insights
The paper's finding that the lightweight linear-expert variant (MoEP, 28M) outperforms the SwiGLU-expert variant (MoEP-SwiGLU, 38M) at small scale is non-obvious and practically useful — it suggests that simple linear projections can be more parameter-efficient than SwiGLU-based FFNs under strict parameter budgets. Additionally, the training dynamics finding that MoEP peaks at 30M words and then overfits while GPT-2 shows more erratic convergence is a concrete, interesting observation about the sample-efficiency vs. generalization trade-off in sparse architectures.

## Suggestions
- Qualify the introduction's headline claim to match Section 5: specify that MoEP achieves the highest macro average when AoA is included and outperforms GPT-2 (but not all GPT-BERT variants) when excluded.
- Either provide actual routing behavior analysis (block selection distributions, specialization metrics, load-balancing outcomes) or revise Contribution 3 to accurately describe the training dynamics analysis.
- Add a non-routed parallel baseline to isolate routing's contribution from parallelism.
- Report the λ values used for load balancing.
- Add a brief explanation of the AoA task and why GPT-2 and MoEP-SwiGLU runs lack AoA scores.

---

## Calibration Summary

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| NanoMoE (04RLVxDvig) | 3.00 | R1 | MoEP is stronger — real LM training vs. toy experiments |
| MO-CTE (thqPibDg6A) | 4.40 | R2 | Comparable quality; MoEP is cleaner but MO-CTE has theory |
| EEP (TTUtPIpaol) | 5.25 | R2 | EEP stronger — more thorough experiments, clearer methodology |
| MoLEx (rWui9vLhOc) | 6.33 | R1 | MoLEx clearly stronger — theory + broader eval, accepted |
| "Small Specialized LM" (aP3OBwf8dk) | 6.00 | R2 | Stronger — more rigorous evaluation |

**Round 1 bracket**: 4.0–6.0. **Round 2 narrowing**: MoEP sits between MO-CTE (4.40) and EEP (5.25), closer to MO-CTE given similar gaps (overclaiming, missing ablation). **Final score: 5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
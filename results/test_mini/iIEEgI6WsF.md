Now I have all the information needed to write the final consolidated review.

---

## Summary

This paper identifies that FSDP's per-layer collective communication (all-gather/reduce-scatter) creates fine-grained synchronization barriers that cause significant device idle time under workload imbalance — a pervasive problem in LLM post-training where sequence lengths vary dramatically. The authors propose On-Demand Communication (ODC), which replaces these collectives with point-to-point gather and scatter-accumulate operations, effectively reframing FSDP as a decentralized parameter server. This relaxes synchronization from per-layer to per-minibatch, decouples per-device progress, and enables a simpler minibatch-level load-balancing scheme (LB-Mini). Across SFT tasks (1.5B–32B models, up to 32 GPUs), ODC achieves up to 36% throughput improvement over standard FSDP; in RL tasks the gains are up to 10%.

## Strengths

1. **Clean root-cause identification and elegant fix.** The paper formally models FSDP's bottleneck as the per-layer max over devices in Eq. 1, then directly replaces the synchronizing collectives with non-blocking point-to-point primitives. The connection to the classic parameter-server paradigm (Section 3.1, Figure 6) is insightful and gives the contribution a clear intellectual foundation beyond a mere engineering hack.

2. **Consistent and substantial empirical gains across diverse settings.** The evaluation covers two post-training paradigms (SFT and RL), three datasets with very different length distributions (LongAlign, SWE-Smith, AIME), four model scales (1.5B–32B), and device counts (8–32). The up-to-36% speedup in SFT (Figure 8) is sustained across configurations, and the trend lines are clean.

3. **Informative parametric study.** Figure 10 systematically isolates four factors (minibatch size, max length, packing ratio, device count) under controlled conditions. The results validate the paper's core thesis: ODC's advantage grows with sequence length (which exacerbates imbalance) and with device count (which increases heterogeneity).

4. **Simplified load balancing as a second-order benefit.** The observation that ODC's decoupled progress removes the need for per-microbatch balancing and enables a simpler minibatch-level scheme (LB-Mini) is both practically useful and theoretically clean. The paper correctly notes the memory-vs-compute scaling mismatch ($O(s)$ vs $O(s^2)$) that fundamentally limits microbatch-level approaches.

5. **Open-sourced implementation.** The paper commits to releasing the implementation, which supports reproducibility.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Cross-node communication mitigation not fully specified in main results.** Section 6.1 acknowledges that ODC's point-to-point primitives are significantly slower than NCCL collectives in cross-node settings (Figure 11) and discusses two mitigations: overlapping with computation and hybrid sharding. The main results (Section 5.2) rely on the standard overlapping optimization, which the paper argues is effective because computation scales as $O(s^2)$ while communication is $O(s)$. However, the paper does not explicitly state *which* mitigations are active in the main experiments, nor does it provide a timing breakdown (e.g., communication wall-clock vs. computation wall-clock per microbatch) to support the claim that "ODC shows no significant slowdown in our long-context evaluations." A reader comparing Figure 11 (where ODC is 2–3× slower cross-node) with the main speedup numbers would benefit from quantitative evidence that the overhead is indeed hidden.

2. **No formal runtime model for ODC.** Equation 1 cleanly captures FSDP's bottleneck ($\sum_m \sum_l \max_d T_{m,d,l}$), but the paper never provides the analogous expression for ODC ($\max_d \sum_m \sum_l T_{m,d,l} + \text{optimizer}$). Adding this would make the source of speedup mathematically precise and allow readers to compute a theoretical upper bound. The paper discusses the relaxation verbally, but the missing equation is a missed opportunity.

3. **RL gains are modest and the conditions for large gains are clear but underemphasized.** The 10% RL speedup (Figure 9) is much smaller than the 36% SFT headline. The paper explains this (verl implementation constraints, less tail-heavy distribution), but the gap is large enough that a casual reader could overclaim the method's universality. The paper would benefit from a sentence that directly states: "ODC's benefit is largest under heavy workload imbalance (long-tailed sequence lengths, small minibatch sizes, many devices); under near-balanced conditions the gains are modest."

4. **Maximum evaluation scale is 32 GPUs.** While the parametric study shows increasing speedup with device count (Figure 10, panel 4), extrapolating to production-scale clusters (hundreds or thousands of GPUs) is speculative. At larger scales, cross-node communication overhead could compound, potentially eroding the per-device benefits observed at 32 GPUs.

### Trivial

- The paper would benefit from a brief note on whether ODC increases peak memory relative to FSDP (the RDMA buffers are mentioned but memory impact is not quantified).
- The computational cost of LB-Mini's minibatch-level partitioning is not discussed.

## Nice-to-Haves

- Report statistical variance across multiple runs, since workload imbalance has a stochastic component.
- Provide a quantitative timing breakdown of communication vs. computation time per microbatch for a representative configuration to substantiate the claim that overlapping hides cross-node overhead.
- Include an ablation comparing ODC with pure point-to-point vs. ODC with hybrid sharding in a cross-node setting.
- A brief note on the packing algorithm's own runtime overhead (LB-Mini requires partitioning samples at minibatch level).

## Removed Points

*These points were flagged by reviewers but are not included as weaknesses in the main review because they either misunderstand the paper, are already addressed, are speculative, or violate the filtering rules.*

- **"RL results modest" as a weakness**: The paper explicitly acknowledges and explains this limitation (§5.2, lines 203–204: "implementation constraints in verl, which require identical numbers of samples per device… a less long-tailed sequence length distribution"). The authors already address it.
- **"Missing appendix" or "missing proofs in appendix"**: The parser strips these sections from all papers; they exist in the original submission.
- **"No direct comparison with hybrid-sharding mitigation"**: The main results use standard overlapping (not hybrid sharding), and the paper states this in §6.1 ("ODC retains the standard FSDP optimization of overlapping… ODC shows no significant slowdown in our long-context evaluations"). The critic's concern about "if results already include hybrid sharding" is not supported by the paper — the paper does not claim to use hybrid sharding in the main results. The point about clearer specification is already captured in Minor weakness #1 above.
- **Formatting/style nitpicks, missing related work**: Removed per hard rules.
- **Strawman "mathematical model does not capture ODC's advantage formally"**: While technically true that the equation is missing, this is already listed as Minor weakness #2 above (missed opportunity, not a flaw in the method).
- **Generic complaint about "no statistical significance"**: Moved to Nice-to-Haves; single-run evaluations are standard in systems papers at this venue.
- **"Parametric study on small scale"**: The 1.5B/8-device setting is a controlled golden configuration for factor isolation, which is standard methodology. The paper also shows scaling trends up to 32 devices.
- **Strength Finder's generic/gratuitous positives** (e.g., "well-motivated problem," "important direction"): These are dropped because they lack concrete evidence specific to the paper.

## Novel Insights

The reviews do not surface any genuinely novel re-interpretation of the paper beyond its own contributions. The key insight — that collective communication's per-layer barriers are not a training-algorithm requirement but an artifact of the communication model, and that reverting to point-to-point PS-style primitives solves the straggler problem at its root — is the paper's own contribution and is stated clearly.

## Suggestions

1. Add the formal ODC runtime expression ($\max_d \sum_m \sum_l T_{m,d,l} + \text{optimizer}$) alongside Eq. 1 to make the source of speedup mathematically precise.
2. State explicitly in the evaluation setup (Section 5.1) whether hybrid sharding is used in the main results, and add a sentence clarifying that the reported speedups use the standard overlapping optimization (not hybrid sharding).
3. Provide a timing breakdown (communication vs. computation wall-clock per microbatch) for a representative configuration to substantiate the claim that cross-node overhead is hidden by computation.
4. Add a summary sentence in the conclusion that directly bounds the conditions under which ODC provides large gains (long-tailed distributions, small batches, many devices).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing** (3 queries on "FSDP distributed training communication optimization LLM"):

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| `RHJVkaIYYa` (SPES, decentralized MoE training) | 3.00 | R1 | Much weaker — the paper's core idea is not validated at scale; rejected paper. ODC is clearly stronger. |
| `1Q2NVxcSuS` (LongShield, DP training) | 3.00 | R1 | Rejected; different sub-area but similar evaluation scale. ODC is stronger in both novelty and empirical results. |
| `RRtwIvoYoh` (GCT, gradient compression) | 2.50 | R1 | Rejected with poor scores. Not comparable in quality to ODC. |
| `yOkek71cG5` (Clapping, pipeline compression) | 3.00 | R1 | Rejected. ODC is substantially stronger. |
| `vU7pcaDypQ` (Partial Parameter Updates) | 4.00 | R1 | Rejected; limited experiments (1.3B, one setting). ODC has broader evaluation and stronger results. |
| `Ej1DYLYzFU` (NoLoCo) | 4.00 | R1 | Rejected; loss divergence issues, not practical. ODC is stronger. |
| `FF3o9flavI` (SparQ, ZO model-parallel) | 4.00 | R1 | Rejected. Different sub-area; ODC has more convincing results. |
| `6N2qFixxYZ` (DES-LOC) | **6.00** | R1 | **Key anchor.** Accept (Poster). Similar topic (communication-efficient distributed training), comparable rigor. DES-LOC has theory but experiments up to 1.7B only. ODC has better novelty (revisiting PS paradigm vs. minor optimizer modification) and broader evaluation (up to 32B, SFT+RL) but lacks theory. ODC is slightly stronger overall. |
| The three strong-band (>7.5) papers are on unrelated topics (multi-turn LLM, matrix sign methods, embodied navigation) and are not useful comparisons. | ~8.00 | R1 | Top of acceptance distribution; ODC is not at this level. |

**Round 1 bracket**: 5.0–7.0.

**Round 2 — Narrowing** (2 queries with tuned bounds on topic of "parameter server decentralized FSDP communication optimization distributed training LLM"):

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| `6N2qFixxYZ` (DES-LOC, re-retrieved) | 6.00 | R2 | As above — closest topical anchor. ODC is comparable or slightly stronger (more novelty, broader evaluation). |
| `0KXI6lDM9C` (Lower bounds for distributed optimization) | 5.50 | R2 | Accept (Poster). Pure theory paper; not directly comparable. |
| `aa14rlfR6k` (FlexRL, load balancing for VLM RL) | **5.33** | R2 | Accept (Poster). Addresses workload imbalance in RL training, similar motivation. FlexRL has weaker novelty (incremental system engineering) and lacks accuracy metrics. ODC is stronger in both contribution clarity and evaluation. |
| `h0LjpOG1jq` (Prima.cpp, heterogeneous inference) | 4.67 | R2 | Accept (Poster). Different problem (inference, not training). |
| `zrFnwRHuQo` (Single global merging in decentralized learning) | 7.50 | R2 | Accept (Oral). Theory paper with surprising results; not directly comparable. |
| `17h5Sl2EaK` (Distributed clustering algorithms) | 7.00 | R2 | Accept (Poster). Unrelated topic. |
| `c5mdo1hWrs` (FSA, sparse attention kernel) | 7.33 | R2 | Accept (Poster). Different topic (kernel implementation). |

### Final Score Determination

My round-1 bracket was **5.0–7.0**. The round-2 narrowing places ODC above FlexRL (5.33, Accept Poster) and above or at parity with DES-LOC (6.00, Accept Poster). ODC has stronger novelty than DES-LOC (revisiting PS as a conceptual contribution vs. a straightforward decoupling of sync periods) and a broader evaluation (up to 32B vs. 1.7B, multiple datasets, both SFT and RL). It is not at the level of the 7+ papers, which either have surprising theoretical results, production-scale evaluations, or both. The main limitations (moderate 32-GPU scale, no formal theory, clear-but-unquantified cross-node overhead) prevent a higher score.

**Final score: 6.5** — a solid Accept paper with a clean, novel contribution and thorough empirical validation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
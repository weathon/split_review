## Summary
This paper introduces TNT (Two-stage Non-linear Training), a training paradigm for deep memory modules (e.g., Titans) that decouples training efficiency from inference quality via hierarchical memory with periodic state resets (Stage 1) and brief high-resolution fine-tuning (Stage 2). Evaluated on 150M-parameter Titans models trained on 10B tokens, TNT achieves up to 17× faster time-to-quality compared to the best Titans baseline while simultaneously improving perplexity.

## Strengths
- **Large concrete speedup with simultaneous quality improvement (Table 1, Table 2):** TNT at C_L={64} reaches the target loss in 1.12 hours vs 19.48 hours for Titans C=8, a 17.37× speedup. Crucially, this is not a speed-quality tradeoff—TNT also improves perplexity from 25.07 (best Titans baseline) to 23.13 (best TNT Stage 1), and further to 23.09 after Stage 2. The time-to-quality metric directly supports the central claim of decoupling training efficiency from inference performance.
- **Clean ablation study isolating each component (Table 3):** The ablation systematically validates three design choices. Removing global memory causes PPL to increase from 21.04 to 25.60 (worse than plain Titans at 23.53), confirming its critical role. Removing Q-K Projection increases PPL from 21.04 to 22.01 and drops reasoning accuracy from 40.6% to 36.4%. Adding local modules shows monotonically improving PPL from 23.53 (0 locals) to 20.15 (4 locals). Each ablation isolates a specific claim.
- **Well-structured problem decomposition (Sections 3–4):** Three concrete challenges are identified (training inefficiency, compression-retrieval mismatch, chunksize sensitivity), each mapped to a specific mechanism (hierarchical memory with resets, Q-K Projection, two-stage fine-tuning). This modularity makes the contribution transparent and each piece independently verifiable.
- **Q-K Projection is technically elegant (Eq. 7):** Projects queries onto the subspace of observed keys using a rank-accumulating d×d matrix maintained as a running sum—constant state size, computable in a chunkwise-parallel manner. The ablation confirms its necessity (1-point PPL improvement, 4-point accuracy drop).

## Weaknesses

### Fatal
None.

### Major
- **Overclaiming relative to experimental evidence:** The abstract states "Evaluated on Titans and TTT models," but TTT only appears as a baseline comparator in Table 2 (at a single C=256 configuration). TNT is never instantiated with TTT or any other deep memory module, yet the paper repeatedly claims to be "a general training paradigm applicable to any deep memory module" (Section 1, Section 6). Similarly, the paper claims to "remove a critical scalability barrier," but every experiment is at 150M parameters, 10B tokens, and max 32K sequence length. The paper itself acknowledges it does not match optimized Transformer kernels (Section 5.2). The abstract's "17× faster" claim is measured against the slowest Titans configuration (C=8) in unoptimized JAX, not against competitive Transformer baselines. These claims are substantially stronger than the evidence warrants.
- **Multi-resolution ablation confounded by parameter count (Table 3):** Adding local memory modules from {8} to {4,8,16,32} improves PPL from 24.10 to 23.13, but each module adds its own independent memory with associated parameters. The paper never reports parameter counts for these configurations or includes a parameter-matched baseline (e.g., 4 modules all at C_L={8,8,8,8}) to disambiguate multi-resolution benefit from simple capacity increase. Since the multi-resolution hierarchy is one of the paper's core design claims, this confound undermines a key contribution.

### Minor
- **Self-contradictory treatment of downstream accuracy (Section 5.3):** The paper claims "higher average accuracy on common-sense reasoning tasks (41.0% vs. 39.7%)" while simultaneously cautioning that "downstream task accuracy can be subject to higher variance." Citing accuracy when it favors TNT while discounting the metric in the same sentence is inconsistent. The honest framing is that TNT roughly matches Gated Transformer quality while training much faster—a strong result without the overreach.
- **Sensitivity of shard length S_L not analyzed:** The paper uses S_L=2048 for efficiency experiments and S_L=4096 for quality experiments without explaining why or showing sensitivity. This parameter controls the parallelism-quality tradeoff (smaller S_L means more resets and more parallelism but more context loss), and deserves at least a brief sensitivity analysis.
- **Stage 2 implementation details deferred:** How many fine-tuning steps, what learning rate, whether global memory is also updated—these important details are not in the main text. The 5% compute claim (Table 4, appendix) should be at least partially verifiable from the main paper.

### Trivial
None.

## Nice-to-Haves
- Parameter-matched multi-resolution ablation comparing {4,8,16,32} against {8,8,8,8}
- Validation on TTT or another deep memory module to support the generality claim
- Position-within-shard perplexity analysis to characterize information loss at reset boundaries
- At least one experiment at 500M+ parameters to substantiate scalability claims
- Empirical measurement of query-key cosine similarity to validate the Q-K Projection hypothesis

## Removed Points
These points are flagged to be removed, treat them with caution:
- Missing comparison with Zhang et al. (2025): This is a concurrent work cited in the introduction ("combines large chunks with local attention to enhance parallelism") but absent from experiments. A direct competitor that addresses the same training efficiency problem through a different mechanism. However, cannot verify whether a fair experimental comparison is feasible given potentially different codebases and setups.
- Q-K Projection conditionality: The rank-accumulating projection matrix Σ k_τk_τ^T / ‖k_τ‖² could become poorly conditioned over long shards; this is a theoretical concern but not directly tested.

## Novel Insights
The periodic state reset mechanism for enabling context parallelism in non-linear recurrences is a genuinely novel contribution. The key insight—that local memory can be reset to a shared learned initial state without destroying information because a global memory compensates—is clean, well-motivated, and addresses a long-standing challenge in efficiently parallelizing non-linear RNNs. The Q-K Projection mechanism, projecting retrieval queries onto the compression key subspace via a constant-size running matrix, is an elegant solution to the domain mismatch problem that is likely generalizable across deep memory modules.

## Suggestions
- Remove or qualify the TTT claim from the abstract unless TTT experiments are added
- Add a parameter-matched multi-resolution ablation (4 modules at identical chunksize vs. 4 modules at different chunksizes)
- Include at least one larger-scale experiment to substantiate scalability claims
- Soften the "removes a critical scalability barrier" language or add evidence to match

## Calibration Report

**Anchors retrieved:**

| Round | Path | Avg Score | Relevance |
|-------|------|-----------|-----------|
| 1 | JOBokGDcX0.md | 2.50 | Sequence segmentation — much weaker |
| 1 | E4Fk3YuG56.md | 2.67* | Cut Cross-Entropy — misranked, actual 8.5 |
| 1 | 4ymHtDAlBv.md | 2.33 | FSFC RNN — weaker contribution |
| 1 | rnTb9dm9zx.md | 3.00 | PCPP diffusion — less relevant |
| 1 | E34AlVLN0v.md | 6.00 | Parallelizing nonlinear RNNs — most relevant, TNT clearly better structured |
| 1 | GrmFFxGnOR.md | 5.00 | Were RNNs All We Needed — simpler, rejected |
| 1 | GQGNLEHmdl.md | 6.33 | AutoChunk — comparable quality |
| 1 | kC5i5X9xrn.md | 5.00 | LightSeq — sequence parallelism, TNT better |
| 1 | tyEyYT267x.md | 8.00 | SAR diffusion — higher bar, less relevant |
| 1 | OfjIlbelrT.md | 8.00 | FlexPrefill — higher bar, less relevant |
| 1 | t7P5BUKcYv.md | 8.00 | MoE++ — higher bar, less relevant |
| 1 | vf5aUZT0Fz.md | 8.00 | DEPT — higher bar, less relevant |
| 2 | FhbZ1PQCaG.md | 5.75 | Internal memory for decision making |
| 2 | 4wk2eOKGvh.md | 6.50 | Test-Time Ensemble — solid incremental, accepted |
| 2 | XYdstv3ySl.md | 6.50 | 3D Spatial Multimodal Memory |
| 2 | fDZumshwym.md | 5.75 | Hierarchical feature sharing |
| 2 | xuxYaBMd9F.md | 5.40 | State Space Augmented Transformer |
| 2 | 88TC1AWV27.md | 6.00 | PICASO — SSM state composition, accepted |
| 2 | AL1fq05o7H.md | 6.25 | Mamba — transformative but rejected |
| 2 | iayEcORsGd.md | 7.33 | Epitopological learning |
| 2 | zA0oW4Q4ly.md | 6.00 | ReLU linear regions |
| 2 | HZndRcfyNI.md | 6.50 | Architecture-aware scaling |
| 2 | cUFIil6hEG.md | 5.75 | Accelerating training with neuron interaction |

**Round 1 bracket:** 6.0–7.0. The paper sits clearly above the 5.0 rejects (Were RNNs All We Needed, LightSeq) and above the 6.0 anchors (PICASO, DEER parallelization) in ablation quality and core mechanism novelty. Below the 7.5+ anchors which had broader evaluation and more impactful contributions.

**Round 2 narrowing:** TNT is better structured than PICASO (6.00) and the DEER paper (6.00), comparable to TTE (6.50) in overall quality but with more novel core mechanisms yet narrower evaluation. TNT's ideas are less transformative than Mamba (6.25, rejected) which had broader implications. The overclaiming (TTT in abstract, scalability barriers) and limited evaluation (150M single architecture) pull the score down from 6.5 to 6.0.

**Final score: 6.0.** The paper has genuinely novel ideas (periodic state resets, Q-K Projection) and a clean ablation study, but overclaims relative to evidence tested at a single small scale on a single architecture. Comparable to accepted 6.0 papers like PICASO and DEER parallelization, with somewhat better ablations but narrower evaluation scope.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>
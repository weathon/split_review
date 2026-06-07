Now I have a clear calibration picture. Let me finalize the review.

## Final Review

### Summary
This paper argues that standard time series forecasting suffers from a "self-stimulation" assumption — predicting the future using only historical observations while ignoring external influences. The authors formalize this through a control-theoretic framework, propose Influence-Aware Time Series Forecasting (IATSF) as a new paradigm, contribute a leak-free benchmark with temporally-synced textual influences, and introduce FIATS, an LLM-free model with channel-aware cross-attention mechanisms (CASM, CAPS). FIATS shows substantial gains over self-stimulated baselines on several datasets.

### Strengths
- **Well-designed benchmark construction**: The benchmark enforces leak-free, independently evolving textual influences with temporal synchronization, addressing known failure modes in existing multimodal TSF datasets. The three-category structure (toy, physics-based, human-driven) provides staged difficulty for evaluation.
- **CASM mechanism has a clear theoretical motivation**: Mapping channel-specific sensitivity \(c^i B^j\) from linear systems to cross-attention queries is a principled architectural choice, and the ablation (Zero Desc. in Table 3) shows it independently contributes to performance.
- **Strong empirical results on challenging datasets**: FIATS achieves large margins over baselines — 36% average MSE reduction over PatchTST on Atmospheric Physics 2014-19 and 44.3% on NYC Traffic Speed. Gains are also demonstrated on the GAUD cold-start scenario.
- **Ablation studies isolate key mechanisms**: Table 3 cleanly separates the contribution of influence data (Zero News degrades to self-stimulated performance) from the CASM mechanism (Zero Desc. degrades to an intermediate level). The embedding-swap rows show robustness to the choice of text encoder.
- **Core idea is well-motivated and sensible**: Incorporating external textual information into time series forecasting addresses a genuine limitation of the field, and the paper provides a structured approach to doing so.

### Weaknesses

#### Fatal
None.

#### Major
- **Missing baseline that isolates the architecture**: The paper's central empirical claim is that FIATS's specific architectural innovations (CASM, CAPS) are responsible for the gains. However, there is no comparison where a standard model (e.g., PatchTST, DLinear) receives the same text embeddings that FIATS uses, through a simple mechanism like concatenation or feature fusion. The "Zero News" ablation only confirms that text data is useful — it does not demonstrate that CASM/CAPS are necessary for extracting that utility. Without this baseline, the paper cannot substantiate its claim that gains "stem from principled influence modeling, not architectural complexity" (line 29). This is the single most important experiment the paper should have run.
- **Theoretical contribution is overstated**: The paper's headline framing — "through a control-theoretic lens, we formally prove that this assumption imposes a hard, mathematical barrier" — promises a nontrivial control-theoretic result. In practice, Propositions 2.1 and 3.1 are direct consequences of basic properties of conditional expectation and variance decomposition. For linear systems, Proposition 2.1 reduces to \(\text{Var}(B U_t) = B \Sigma B^\top\), which follows immediately from the model definition \(X_f = A X_h + B U_t\). No control-theoretic machinery (stability, controllability, observability, Lyapunov analysis, feedback design) is actually used. The state-space notation (A, B, C) is borrowed for exposition but the analysis does not engage with any result from control theory. The formalization is useful as a problem statement, but the paper frames it as a novel theoretical contribution, which substantially overclaims.

#### Minor
- **FIITS is never defined in the main text**: FIITS appears as a column in Table 1 and consistently performs between the self-stimulated baselines and FIATS, making it one of the most informative results in the paper. However, the term is never introduced or defined. Readers must reverse-engineer that it likely represents FIATS without influence input (analogous to the "Zero News" ablation). This is a basic clarity issue.
- **FM Toy experiment is partly tautological**: The FM Toy dataset is constructed such that influence signals directly control the output (frequency). Showing that a model with access to this signal achieves near-zero error while models without it fail is largely predetermined by the construction. While useful as a sanity check for the theoretical claims, the dramatic language ("even billion-parameter foundation models... fail spectacularly") is misleading — those models were not designed or trained for this synthetic system.
- **Atmospheric Physics dataset split unexplained**: The difference between "Atmospheric Physics 2014-19" and "Atmospheric Physics 2014-24" is never explained in the main text. The two variants show quite different baseline behaviors (e.g., on 2014-24 the gap between FIATS and FIITS at horizon 96 is only ~6%, versus ~27% on 2014-19), making the explanation important for interpreting results.
- **Interpretability claims lack quantitative evaluation**: Attention maps (Figures 3, 5) are presented as evidence that CASM learns meaningful channel-specific sensitivities. However, showing that cross-attention attends differently across channels is a property of the architecture — there is no quantitative metric to evaluate whether these attention patterns are correct or meaningful.
- **Computational cost not reported despite "lightweight" claim**: The paper positions FIATS as a "lightweight, LLM-free baseline" in contrast to LLM-based approaches, but provides no parameter counts, FLOPs, or wall-clock comparisons to substantiate this claim.
- **Rhetoric uniformly overstates heterogeneous results**: The paper uses paradigm-shifting language ("the primary path forward for meaningful progress," "decisively validate the IATSF paradigm") uniformly across all datasets, though gains are heterogeneous — Electricity Utility shows only ~5-10% improvement over PatchTST, while Atmospheric Physics 2014-19 shows ~28-36%.

#### Trivial
None.

### Nice-to-Haves
- Reporting standard deviations or confidence intervals across multiple runs would strengthen reliability, though single-run evaluation is standard in this subfield.
- Per-dataset gain attribution quantifying what fraction comes from (a) having influence data vs. (b) FIATS's specific architecture would sharpen the empirical story.

### Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic #5 (experimental details absent — lookback windows, split methodology, training hyperparameters):** These are standard appendix material. Per hard rules, removed as a trivial reproducibility nitpick.
- **Harsh Critic's statistical significance concern:** Single-run evaluation without error bars is standard practice in time series forecasting benchmarks. Moved to Nice-to-Haves.
- **Strength Finder's "control-theoretic formalization as rigorous foundation":** While the propositions are correct, the analysis is mathematically elementary. The strength is kept but downgraded; the formalization is useful as a problem statement, not as a novel theoretical result.

### Novel Insights
None beyond the paper's own contributions.

### Suggestions
- **Add the simple-text-baseline comparison.** Compare FIATS against PatchTST and DLinear augmented with the same text embeddings via simple concatenation. This would directly answer whether CASM/CAPS are necessary or whether any model benefits from text access.
- **Downscope the theoretical claims.** Reframe the control-theoretic analysis honestly as a formal problem statement that makes explicit why unobserved influences limit forecasting accuracy. This framing is useful as motivation and notation without claiming a novel mathematical result.
- **Define FIITS explicitly in the main text** and cross-reference it with the "Zero News" ablation to help readers interpret Table 1.
- **Report computational costs** (parameter counts, at minimum) to substantiate the "lightweight" claim.

### Calibration Anchor Comparison

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| TGForecaster (mfc6FKgtQA) | 5.00 | R1 | Very similar topic (text-guided TSF, cross-attention, benchmark). Our paper has better benchmark design, stronger ablations, and larger empirical margins. Paper under review is clearly stronger. |
| CiK (4F1a8nNFGK) | 5.00 | R1 | Benchmark for TSF with text. Our paper additionally contributes a novel model architecture with strong results. CiK's benchmark is broader but our paper's is more rigorous on leak-free design. Our paper is stronger. |
| ContextFormer (xW4J2QlqRx) | 5.00 | R1 | Plug-and-play context integration. Our paper has more principled architecture, better ablations, and a benchmark contribution. Our paper is stronger. |
| Dual-Forecaster (QE1ClsZjOQ) | 4.50 | R1 | Multimodal TSF with descriptive/predictive texts. Our paper has more rigorous benchmark and stronger results. |
| Channel-wise Influence (DKCtt2iqfw) | 5.50 | R2 | Channel-level influence for MTS. Limited datasets, narrow scope. Our paper is broader and stronger. |
| In-context TSP (dCcY2pyNIO) | 6.25 | R2 | Novel in-context framework for TSF. Comparable contribution level but our paper has a benchmark and better empirical gains. Our paper is slightly below due to missing baseline and theoretical overclaim. |
| Simple Baseline MTS (oANkBaVci5) | 6.75 | R2 | Clean architecture paper with thorough baseline comparisons. Tighter than our paper but narrower contribution (no benchmark, no new paradigm). Our paper is weaker due to missing baseline validation. |

**Round 1 bracket:** 5.0–7.0 based on comparison with TGForecaster (5.00), CiK (5.00), and ContextFormer (5.00).

**Round 2 narrowing:** The paper is stronger than Channel-wise Influence (5.50) but weaker than Simple Baseline MTS (6.75). Compared to In-context TSP (6.25), the paper has a broader contribution (benchmark + model) but weaker validation (missing baseline). Placed at 6.0.

**Final score justification:** The paper makes genuine contributions — a well-designed benchmark, a principled model architecture (CASM/CAPS), and strong empirical results. However, the missing baseline comparison (PatchTST/DLinear + text embeddings) is a major gap that prevents validating the central architectural claim, and the theoretical framing substantially overstates what is actually an elementary mathematical observation. These issues prevent the paper from reaching the 6.5-7.0 range where cleaner contributions reside, but its strengths place it above the 5.0 cluster of similar text-integration TSF papers that had weaker execution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>
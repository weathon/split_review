Now I have a thorough understanding of the paper and calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper proposes RoPE++, an extension of Rotary Position Embeddings that re-injects the ordinarily discarded imaginary component of the complex-valued dot product as a parallel set of attention heads. By simply rotating query vectors by −π/2 before applying standard RoPE, the method produces both real and imaginary attention scores without altering the core rotation mechanism. Two configurations are introduced: RoPE++EC (equal KV cache, doubled heads) and RoPE++EH (equal heads, halved KV cache). Pre-training experiments at 376M, 776M, and 1.5B model scales show consistent improvements over vanilla RoPE on both short-context and long-context benchmarks, with the gains growing as context length increases.

## Strengths

- **Novel and principled insight**: The paper identifies a genuinely overlooked aspect of RoPE — that the imaginary part of the complex dot product is simply discarded, and that this discarded term has favorable properties for long-range modeling. The characteristic-curve analysis (Section 3.2, Figure 1) showing the imaginary component decays much more slowly than the real component as a function of distance provides clear motivation for why recovering this term should help long-context tasks.

- **Elegant, low-overhead implementation**: The method requires only rotating query vectors by −π/2 before applying standard RoPE, with keys unchanged (Equation 4). This fits naturally into existing FlashAttention implementations, and the two configurations (EC and EH) offer practical trade-offs between memory and compute. No extra KV cache is needed for the EC variant.

- **Consistent empirical gains across multiple model scales**: Tables 1 and 2 show RoPE++EC outperforming RoPE and other position embeddings (FoPE, Pythia, ALiBi) on both short-context aggregate scores and long-context benchmarks (RULER, BABILong). The gains are consistent across 376M, 776M (main paper) and 1.5B (Appendix C) model sizes. On RULER, RoPE++EC improves average scores from 18.8→25.0 at 376M and 27.4→29.4 at 776M relative to RoPE — gains that widen at longer contexts.

- **EH variant demonstrates efficiency with competitive performance**: RoPE++EH matches or slightly exceeds vanilla RoPE performance while using half the KV cache and QKV parameters (Table 1, Table 2), with memory and TPOT benefits confirmed in Figure 4. This is a strong practical result.

- **Compatibility with existing long-context techniques**: Table 3 demonstrates that RoPE++ combines effectively with NTK scaling, Linear PI, and YaRN, consistently outperforming RoPE under each interpolation method. This suggests the imaginary extension provides orthogonal benefits.

- **Informative attention-pattern analysis**: Figure 5 provides compelling visualization that imaginary heads attend more globally while real heads focus locally, and the noise-injection experiment shows that corrupting imaginary heads degrades long-context performance more severely than corrupting real heads (an 8-point gap at 776M).

- **Convincing training dynamics**: Tables 7-9 in the appendix show that RoPE++ training loss curves nearly overlap with RoPE, converging stably and ultimately surpassing RoPE on downstream scores — addressing concerns about training stability.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are reasonably supported.

### Minor

- **No strictly capacity-matched baseline for EC**: RoPE++EC doubles the number of attention heads and the output projection W_o compared to vanilla RoPE (while keeping KV cache equal). The paper would be substantially strengthened by comparing against a RoPE model with the same total parameter count — e.g., by widening layers or increasing head count in the RoPE baseline. As it stands, some fraction of EC's gains may be attributable to increased model capacity rather than the imaginary attention structure specifically. This is mitigated by the EH results (which show benefits with *fewer* parameters) and by the fact that EC is explicitly positioned as the "equal cache" variant, but a parameter-controlled comparison remains a gap. The paper acknowledges this cost in Section 3.3 and Appendix C.2 (Table 11), which is good, but a controlled baseline would resolve the attribution question more cleanly.

- **Theoretical analysis relies on untested statistical assumptions**: The characteristic-curve derivation (Section 3.2, Appendix B) assumes query and key features are i.i.d. with nonzero mean. The paper itself notes this is "expectation-based" (line 1798 of Appendix B). While this is a standard analytical technique also used in the original RoPE paper, the gap between the i.i.d. Gaussian assumption and trained transformer feature distributions means the theoretical motivation, while suggestive, is not conclusive. The empirical results largely compensate for this, but a stronger theoretical connection would elevate the contribution.

- **Small absolute gains on short-context tasks**: In Table 1, the average score improvements over RoPE are often within 1 percentage point (e.g., 376M Short: RoPE 40.1 vs RoPE++EC 41.0). While the pattern is consistent, no variance estimates are reported, making it difficult to assess whether individual task differences are statistically meaningful. The long-context gains (Table 2) are more substantial and less affected by this concern.

### Trivial

- **Noise-ablation experiment shows correlation, not mechanism**: The experiment in Section 5.2 demonstrates that trained models rely more on imaginary heads for long-context tasks, but it does not cleanly disentangle whether this reliance arises *because of* the imaginary-attention formulation versus post-hoc specialization during training. This is an inherently difficult causal question, and the combined evidence (theory + attention patterns + ablation) is reasonably convincing, so this is a minor limitation of the analysis rather than a flaw.

## Nice-to-Haves

- A controlled comparison where a standard RoPE model is given the same total parameter budget as RoPE++EC (e.g., by increasing head count or FFN width) would more cleanly attribute gains to the imaginary extension specifically. The authors could also ablate by comparing against a dummy extension that adds extra heads with random fixed rotations rather than the principled −π/2 rotation — this would test whether the specific structure of the imaginary attention matters.

- Validation on larger model scales (e.g., 3B or 7B) would increase confidence that the gains persist, though the 1.5B results in Appendix C already provide a meaningful step beyond the 376M/776M results in the main paper.

- Reporting variance across multiple seeds for the benchmarking results would help readers assess the reliability of small-margin improvements.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The paper's central contribution is unsubstantiated / experimental design error that invalidates the headline results"** — This overstates the issue. The EC comparison controls for KV cache (the primary long-context bottleneck), and the EH variant *already* demonstrates benefits with fewer parameters and less cache than standard RoPE. The missing capacity-matched baseline for EC is a limitation but not a fatal error. The gains on long-context tasks are substantial (e.g., RULER 25.0 vs 18.8 at 376M) and unlikely to be explained purely by the doubled W_o.

- **Harsh Critic: "Theoretical motivation is insubstantial and does not distinguish the method from trivial reparameterization"** — The expectation-based analysis is a standard technique (also used by the original RoPE paper), and the paper explicitly acknowledges it is expectation-based. The imaginary attention has a principled origin (the naturally discarded term from the complex multiplication), which distinguishes it from arbitrary transformations.

- **Harsh Critic: "No baseline is provided that controls for total parameter count or computational budget... this is a basic experimental design error"** — See above. The EH variant already controls for head count while providing cache savings. Also, the harsh critic's claim that EC gains could be "entirely due to increased model width" is speculative — the doubled W_o in EC is a relatively small fraction of total parameters.

- **Harsh Critic: "The extrapolation improvement is marginal and does not lead to usable extrapolation performance"** — Section 5.3 and Appendix D.2 explicitly note that RoPE++ cannot directly extrapolate without degradation, and Figure 6 shows the perplexity does rise. The paper frames this as a slower degradation, not a solution to extrapolation. The paper is honest about this limitation.

- **Harsh Critic: "The choice of the negative imaginary part (Eq. 2) is motivated only by the subsequent expectation analysis, which is weak"** — The choice of negative imaginary part is explicitly justified (line 454: "when q_t, k_s are similar, their attention is on average larger regardless of relative distance, which is the reason why we take the negative imaginary part"). This is a clear, valid motivation.

- **Harsh Critic: "The efficiency analysis shows that EH reduces memory and latency, but this is a direct consequence of halving the number of heads—any head-count reduction would yield similar savings"** — This misrepresents the paper. The paper's claim is that RoPE++EH achieves competitive or better *performance* while halving the cache, not that halving cache is novel. The efficiency gains are presented as a practical benefit of the architecture choice, not as a novel mechanism.

- **Strength Finder (dropped): "Improved length-extrapolation behavior" as a core strength** — While the paper does claim and show slower perplexity increase (Figure 6), the paper itself acknowledges in Appendix D.2 that "RoPE++ cannot directly extrapolate like FoPE or PaTH." This is a modest benefit rather than a headline result.

- **Harsh Critic: Section-by-section notes about "overstating the case" in abstract/introduction** — These are matters of framing and rhetoric, not substantive errors. The abstract's claim that standard RoPE "discards the imaginary component... leading to a potential loss of relational details" is defensible — the paper demonstrates that the imaginary part carries useful information.

## Novel Insights

The paper's most interesting insight is that the imaginary component of RoPE's complex attention product is not merely a mathematical artifact to be discarded, but carries structural properties (slower distance-dependent decay) that make it naturally suited for long-range dependencies. This emerges cleanly from the characteristic curve analysis without requiring additional parameters or learned components. The dual-head architecture that results — where real heads capture local semantics and imaginary heads capture global context — emerges naturally from the algebra rather than being engineered. This perspective may inspire similar re-examinations of other "discarded" terms in standard deep learning components.

## Suggestions

- Add a parameter-matched RoPE baseline for EC (e.g., RoPE with increased head count or FFN width to match total parameters) to strengthen attribution. This is the single most impactful improvement the authors could make.
- Consider an ablation comparing the −π/2 imaginary attention against a control with random fixed rotations on extra heads, to demonstrate that the specific structure matters.
- Report standard deviations across at least 3 seeds for the main benchmark results in Tables 1-3.
- The expectation-based analysis could be empirically validated by measuring whether the characteristic curve actually predicts trained attention patterns — this would bridge the gap between theory and practice.

## Score and Decision

**Calibration anchors used:**

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| `1J63FJYJKg` | MrRoPE | 6.5 (Oral) | Stronger: deeper theory, training-free, larger-scale experiments on existing LLaMA models. RoPE++ has less theoretical depth and requires training from scratch. |
| `W8ZXfNaqku` | Frayed RoPE | 6.0 (Poster) | Comparable scope (1B-3B, geometric analysis). RoPE++ has more consistent results and cleaner method; Frayed RoPE has stronger geometric analysis. RoPE++ slightly below. |
| `D0u0glT060` | Deconstructing Positional Info | 7.2 (Poster) | Stronger: more comprehensive theoretical analysis across all positional encodings. RoPE++ is narrower in scope. |
| `AQo1SEElNb` | Selective RoPE | 4.5 (Poster) | RoPE++ is stronger: broader evaluation, multiple model scales, clear practical benefits. |
| `kf2mzS6xfk` | PoPE | 4.0 (Reject) | RoPE++ is clearly stronger: standard long-context benchmarks, better theoretical grounding, larger scales. |
| `U1xQiqTnBp` | TAPA | 4.0 (Reject) | RoPE++ has better evaluation breadth and practical utility, though TAPA has stronger formal theory. |
| `RlPVSeKjoc` | DroPE | 3.5 (Poster) | RoPE++ has more comprehensive experiments and evaluation. |
| `60Vj3aBnjw` | Position-Aware NTP | 3.0 (Reject) | Much weaker paper; not a close comparison. |
| `QIIrjgUnL1` | Position-Aware Attention (EPAR) | 3.0 (Reject) | Much weaker paper; not a close comparison. |

RoPE++ is a solid contribution: it identifies a genuinely overlooked aspect of RoPE, proposes a clean solution, and validates it with consistent experiments across three model scales and multiple benchmarks. The theoretical motivation, while expectation-based, is clearly presented and aligns with the empirical findings. The two-configuration design (EC/EH) offers practical deployment flexibility. The main limitation is the absence of a strict parameter-matched baseline for EC, which prevents fully clean attribution of the gains to the imaginary structure specifically. This paper is clearly stronger than the rejected papers in the calibration set (PoPE, TAPA, EPAR) and comparable to accepted posters like Frayed RoPE and Selective RoPE. I do not see any fatal flaws.

**Originality**: The idea of re-injecting the discarded imaginary component is novel within the RoPE literature. **Importance**: Position embedding design is a central topic for long-context LLMs. **Claims supported**: Mostly yes, with the caveat about parameter matching for EC. **Soundness**: Experiments are well-designed overall, with reasonable baselines and comprehensive benchmarks. **Clarity**: Well-written and easy to follow. **Value to community**: High — the method is simple and the insight may inspire further work.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
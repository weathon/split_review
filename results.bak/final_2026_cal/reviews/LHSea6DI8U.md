Now let me write the final consolidated review.

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a frequency-domain spatio-temporal backbone (FreNet + Dual-Stream Linear Graph Attention, DLGA) with a scalable contextual pattern bank that is incrementally expanded while the backbone stays frozen. The key idea is that the backbone captures stable, general patterns while the pattern bank adapts to new nodes and distributions via prompt-based gating and attention interactions. Experiments on three streaming datasets show strong gains on two traffic datasets (PEMS-Stream and CA-Stream, ~21% MAE reduction) and modest gains on one meteorological dataset (AIR-Stream, 2.35%).

## Strengths

- **Novel, well-designed architecture pairing a frequency-domain backbone with a contextual pattern bank.** The combination of FreNet (FFT with learnable frequency embedding, Eq. 6) for drift mitigation, DLGA (linear attention with random feature maps, Eq. 7–9) for efficient spatial modeling, and a three-group pattern bank with prompt-based gating (Eq. 5) is genuinely new for the CSTF setting. The design choices are principled and well-justified. The freeze-backbone, expand-pattern-bank training strategy (Eq. 4) directly addresses catastrophic forgetting, and the ablation study (Figure 4) confirms that every component contributes to performance.

- **Strong empirical results on two traffic datasets.** On PEMS-Stream and CA-Stream, STBP reduces average MAE by 21.44% and 21.93% respectively over the best baseline (EAC), with consistent gains across all horizons (3, 6, 12) and metrics (MAE, RMSE, MAPE). The few-shot experiments (Table 2) further show large, consistent improvements (e.g., MAE 13.58 vs. 16.13 on PEMS-Stream 10%), demonstrating robustness under data scarcity.

- **Comprehensive ablation and efficiency analysis.** The ablation study (Figure 4) systematically tests six variants, isolating the contribution of the backbone (w/o Backbone), the attention mechanism (w/o DLGA), and the continual learning strategy (Retrain, Online). The efficiency analysis (Figure 8) compares training time and GPU memory across all baselines and includes a toy-dataset comparison of linear vs. quadratic attention, validating the O(N) complexity claim.

- **Good clarity, code release, and interpretability.** The paper is well-written, the method is clearly described with formal definitions, and the t-SNE visualization (Figure 6) provides qualitative support for the pattern bank's ability to capture node heterogeneity. Code is publicly available.

## Weaknesses

### Major
None.

### Minor
1. **Uneven results across datasets — AIR-Stream gap is small and confidence intervals overlap.** The paper reports that STBP reduces average MAE by 2.35% on AIR-Stream (23.64 vs. 24.21 for EAC). The standard deviations (±0.23 for STBP, ±0.43 for EAC) produce overlapping 1σ intervals (STBP: [23.41, 23.87]; EAC: [23.78, 24.64]). The paper does not report statistical significance, so on this dataset the advantage could be within the noise. The abstract and introduction claim "significantly outperforms state-of-the-art baselines" without qualification; a more measured discussion of the AIR-Stream results would improve accuracy. This does not undermine the core contribution — the method is clearly effective on the two traffic datasets — but it should be acknowledged explicitly.

2. **Number of experimental runs not stated.** All results in Tables 1 and 2 include standard deviations, but Section 5.1 never states how many independent runs (seeds) these are computed over. Standard practice is 3–5 seeds. Without this information, the reader cannot assess whether the reported confidence intervals are meaningful. This is a straightforward reporting gap that should be addressed.

3. **Minor overclaim on scalability.** The abstract states that STBP "outperforms state-of-the-art baselines in both forecasting accuracy and scalability." The efficiency study (Figure 8) shows STBP is competitive with EAC on training time and memory (similar efficiency), but the CSTF baselines EAC and STKEC are also quite efficient. The claim "outperforms ... scalability" overstates the evidence; "offers competitive scalability with substantially higher accuracy" would be more precise.

### Trivial
- The ablation figure (Figure 4) lists "EAC" as a variant alongside "w/o Backbone" and "w/o DLGA," which could mislead a casual reader into thinking EAC is an ablation of STBP. The text clarifies this ("We also include EAC ... for comparison in the ablation study"), but the figure legend alone is ambiguous.
- Parameter sensitivity analysis (Figure 5) only varies the channel dimension *d*. Exploring additional hyperparameters (learning rate, number of pattern bank groups) would strengthen the analysis, though this is acceptable for a conference paper.

## Nice-to-Haves
- Statistical significance tests (e.g., paired bootstrap or t-tests) on AIR-Stream would clarify whether the 2.35% improvement is reliable or noise.
- An ablation removing only the pattern bank's *expansion* mechanism (fixing the pattern bank size rather than growing it) would isolate the value of incremental parameter expansion, complementing the existing ablations.

## Removed Points
- **"General backbone not clarified"** (from Harsh Critic): The paper explicitly defines "general" on line 115 as "independent of the number of nodes and does not rely on any predefined adjacency matrix." This criticism is already addressed by the paper.
- **"w/o Backbone ablation doesn't isolate backbone contribution"**: The paper already has the "w/o DLGA" variant which does isolate the attention contribution. The "w/o Backbone" variant tests a different question (portability of the pattern bank to other backbones), which is a valid experiment. Not a genuine weakness.
- **Strength Finder's generic strengths** (e.g., "Clear problem formulation"): These are true but superficial; dropped from the main review as they don't add discriminating evidence.
- **"Related works missing"**: No external sources to verify this; removed per instructions.

## Novel Insights

The most interesting finding is that the frequency-domain backbone (FreNet) alone — without any pattern bank — achieves performance comparable to the full EAC method under online training (Figure 4, "Online" vs. "EAC" bars). This suggests that modeling stable frequency components (periodicity and trends) is more critical for handling distributional drift than previously recognized in the CSTF literature, where most methods rely on temporal convolutions or RNNs. The subsequent large gain from adding the pattern bank on top ("Our") shows that frequency-domain stabilization and pattern-bank adaptation address complementary challenges: one handles temporal drift, the other handles node heterogeneity and forgetting.

## Suggestions
1. State the number of independent runs used to compute all standard deviations (in Section 5.1).
2. Add a brief discussion of the AIR-Stream results — acknowledge the smaller gap and note that the method's advantage is clearest on the traffic datasets.
3. Qualify the scalability claim in the abstract (e.g., "offers competitive scalability" instead of "outperforms ... scalability").
4. Clarify the ablation figure legend to distinguish EAC as an external comparison rather than an ablation variant.

## Score and Decision

**Calibration Anchors:**

| Anchor ID | Avg Score | Round | Comparison to STBP |
|---|---|---|---|
| KHlFVENw5Q (GEMFlow) | 2.50 | R1 | Much weaker; different problem (pretraining for static ST) |
| 5FOYGNXRNc (DPGNet) | 2.00 | R1 | Much weaker; basic ST prediction, no continual learning |
| ZlLOpA5rN8 (STDACN) | 3.00 | R1 | Much weaker; static ST prediction |
| vfDJiI0dbu (STM4D) | 3.00 | R1 | Different domain (autonomous driving occupancy) |
| Rw06dyqE5f (Continuous TGNN) | 4.50 | R1 | Weaker; link prediction on dynamic graphs, not ST forecasting |
| sieYp1CpYk (Randomized Reps in OCGL) | 4.00 | R1 | Weaker; simpler approach for online graph learning |
| b6Py2zy0fK (PhySTA) | 5.33 | R1 | Comparable; physics-inspired ST learning, different problem formulation |
| z45L1eYoHE (SNIP) | 5.33 | R1,R2 | Weaker; handles only single expansion stage vs. multi-stage streaming in STBP; less comprehensive evaluation |
| DjlVwQFRMb (Tramba) | 5.00 | R2 | Weaker; static traffic forecasting, no continual learning |
| 8pi1rP71qv (FlyPrompt) | 5.60 | R2 | Comparable; general CL, different domain, mixed reviews |
| fhDqFk4DgI (MMCKM) | 6.00 | R2 | Comparable methodological depth; different subproblem (micro-macro traffic modeling) |
| pW1Kg9CYyw (ℓ1LD-CTGR) | 6.40 | R2 | Different problem (graph representation, not ST forecasting) |

**Round 1 bracket:** I placed the paper between 4.5 and 7.5 based on lower-bound anchors (~2–4.5 being clearly weaker) and upper-bound anchors (8+ being unrelated, stronger papers from different domains).

**Round 2 narrowing:** The most comparable anchors — SNIP (5.33, rejected), PhySTA (5.33, accepted), MMCKM (6.00, accepted) — place STBP at the higher end of the mid-range. STBP is clearly stronger than SNIP (which handles a simpler problem setting and has a less comprehensive evaluation) and comparable to MMCKM (which was accepted with 6.0). The paper's technical novelty, thorough evaluation, and code release justify a score above the 5.33 anchors.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
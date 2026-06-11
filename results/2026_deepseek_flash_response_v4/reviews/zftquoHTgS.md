## Summary

This paper identifies the "underthinking" phenomenon in LongCoT LLMs (where models prematurely switch between reasoning thoughts without deep exploration) and proposes SmartSwitch — a training-free, plug-and-play inference framework. SmartSwitch detects thought-switching via linguistic cues, evaluates the abandoned thought using a Process Reward Model (PRM), and if the thought scores above a threshold, backtracks and inserts a "deepen prompt" to encourage deeper exploration. Experiments across 5 model scales (1.5B–32B) and 5 math benchmarks show consistent accuracy gains (up to +23.3 points) alongside reduced inference time and token usage.

## Strengths

1. **Consistent accuracy gains across all model scales and benchmarks**: Table 1 shows SmartSwitch improves pass@1 accuracy for every model (1.5B to 32B) on every benchmark, with gains as large as +23.3 points (7B model on AIME25) and +16.7 points (1.5B model on AIME25). These improvements are uniform across 25 model×benchmark entries — not cherry-picked.

2. **Simultaneous accuracy improvement and efficiency gain**: Tables 2 and 3 report that SmartSwitch reduces both average response length (e.g., −14.2% for the 32B model on AIME24) and wall-clock inference time (e.g., −35.3% for the 7B model on AIME24) while raising accuracy. This dual improvement is non-trivial: encouraging deeper thinking would naively increase token usage, but SmartSwitch prunes shallow wasteful thoughts instead.

3. **PRM-guided intervention shown essential via controlled ablation**: Table 4 compares SmartSwitch (40.0%) against an "Always Intervene" baseline that injects the deepen prompt at every thought switch without PRM scoring. "Always Intervene" degrades performance below vanilla (18.9% vs. 20.0%). This ablation directly isolates the value of selective, PRM-gated intervention.

4. **Quantitative characterization of underthinking before proposing the solution**: Section 3 defines a clear metric (Underthinking Frequency, Equation 1) and measures it across 6 models on AIME24. Figure 2 shows that underthinking frequency correlates with problem difficulty and is higher for wrong answers than correct answers across all model sizes, grounding the problem empirically.

5. **Systematic ablation of key design choices**: The paper ablates process division strategies (Table 6, 4 variants), PRM selection (Table 4), process-to-thought score mapping (6 strategies in Table 7), and the score threshold (Table 8), providing concrete evidence for design decisions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Score threshold selected on the evaluation set without held-out validation**: Table 8 shows the threshold ablation on AIME24, and the optimal τ=0.70 is used across all main results. The paper does not mention a held-out validation set for this tuning. Performance is pathologically sensitive: moving from τ=0.70 to τ=0.71 collapses accuracy from 40.0% to 30.0% on AIME24 for the 1.5B model, and similar drops occur across all five model sizes (Table 8). However, the fact that τ=0.70 is optimal across all 5 model sizes (1.5B through QwQ-32B) argues *against* random overfitting — different models would be expected to have different optimal thresholds if the signal were noise. The paper acknowledges this limitation in Section 6. Still, independent validation (e.g., tuning on one benchmark and testing on others) would substantially tighten the evidence.

2. **No confidence intervals or variance estimates on any result**: All main results (Table 1) are reported as pass@1 averaged over 32 responses without standard deviations or confidence intervals. For AIME benchmarks (~15 problems), a swing of 1–2 problems changes accuracy by ~7 points. While the largest gains (11–23 points) are clearly beyond noise, smaller gains (e.g., +0.6 to +2.0 on MATH-500, +1.6 on GaoKao) cannot be assessed for statistical reliability without variance estimates.

3. **No comparison against PRM-based reranking baselines**: SmartSwitch uses a PRM for scoring. A natural baseline — generate N responses with vanilla inference and select the best by PRM score (best-of-N or PRM-guided reranking) — is absent. Such a comparison would disentangle whether gains come from the *intervention mechanism* itself or simply from leveraging the PRM's signal. The paper compares against vanilla inference, standard prompting, and TIP, but no training-free PRM-using baseline other than Always Intervene.

4. **TIP comparison limited to one model on one benchmark**: Table 5 compares SmartSwitch against TIP only on DeepSeek-R1-Distill-Qwen-1.5B on AIME24. Results on larger models or additional benchmarks would strengthen the comparison and test whether TIP's decoding penalty becomes more effective on stronger models.

5. **Segmentation mismatch between problem analysis and method**: Section 3 segments thoughts for UF computation using a capable LLM (DeepSeek-V3), while the SmartSwitch method (Section 4) uses simple linguistic-cue-based detection during inference. The paper does not discuss how well these methods agree. If the LLM-based segmentation finds many "underthinking" instances that the cue-based detector misses, SmartSwitch's recall could be limited. (That said, the use cases differ: offline analysis can afford expensive LLM calls, while online inference needs fast detection.)

6. **Linguistic cue recall not characterized**: The Limitations section honestly notes that cue-based detection will miss implicit switches. However, no estimate is given of what fraction of switches have explicit vs. implicit markers. This would calibrate reader expectations about SmartSwitch's coverage.

### Trivial

- Table 7 shows "last process score" works best for process-to-thought aggregation, but the paper could briefly discuss why (e.g., the last process is closest to the switch point and best captures the thought's terminal potential).

## Nice-to-Haves

- A detailed cost breakdown of PRM scoring overhead vs. generation time saved would make the efficiency claims (Tables 2–3) more transparent.
- Ablating variations of the "deepen prompt" to test robustness to prompt wording.
- An estimate of what fraction of thought switches have explicit linguistic markers (vs. implicit switches) would calibrate expectations about SmartSwitch's recall.

## Removed Points

- **"UF metric conflates brevity with premature abandonment"**: The paper transparently calls UF a "heuristic" (Section 3.2, Eq. 1) and provides concurrent validity evidence (Figure 2: UF correlates with difficulty and wrong answers). The metric is a proxy, which the paper acknowledges, and is used as an investigative tool — not as the method's core criterion. Removed for being a scope-expectation mismatch: a problem-characterization metric does not need to be perfect to be useful.

- **"No comparison against compute-matched baseline" iteration of the same point in Harsh Critic's Strengthening section**: Already captured in Weakness #3 (missing PRM reranking baseline). Duplicate removed.

- **Criticism about "last process score may correlate with thought length"**: Speculative and not grounded in any evidence in the paper. Removed as speculation without support.

- **Criticism about "deepen prompt not ablated"**: Captured under Nice-to-Haves rather than a weakness. The prompt's exact wording is unlikely to be the core contribution.

- **Strength Finder's generic strengths about "problem importance"**: These are generic/superficial and removed. Only concrete, evidence-backed strengths retained.

## Novel Insights

None beyond the paper's own contributions. The observation that thought-switching can be detected via linguistic cues and evaluated with an off-the-shelf PRM, enabling a training-free intervention, is the paper's novel contribution itself.

## Suggestions

1. **Validate the threshold on held-out data**: Tune τ on one benchmark (e.g., AMC23 or a held-out subset of AIME24) and report results on the other benchmarks using that fixed threshold. This would directly address the most serious evidential concern.
2. **Add bootstrapped confidence intervals** to the main results (Table 1) to allow readers to assess which gains are statistically reliable.
3. **Include a PRM-guided best-of-N reranking baseline** to isolate the value of the intervention mechanism from simply using the PRM signal.
4. **Extend the TIP comparison** to at least one larger model and one additional benchmark.
5. **Discuss the alignment** between LLM-based segmentation (Section 3 analysis) and cue-based segmentation (Section 4 method), including an estimate of cue recall.

## Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Supervised CoT | pXIbcRPxWR.md | 2.50 | R1 (weak) | Weaker; flawed methodology, narrow experiments |
| Planning with MCTS | sdpVfWOUQA.md | 3.00 | R1 (weak) | Weaker; weak baselines, less rigorous evaluation |
| RaR (Retrieval-Augmented Reflection) | ElYRG3pJcv.md | 4.25 | R1 (mid) | Weaker; compared against weak baselines only |
| MAgICoRe | j9wBgcxa7N.md | 4.80 | R2 (mid) | Weaker; complex multi-agent approach with saturation issues |
| On Designing RL Reward | F0GNv13ojF.md | 5.17 | R2 (mid) | Comparable; both have PRM-related contributions, different focus (training vs inference) |
| Inference Scaling Laws | VNckp7JEHn.md | 5.75 | R2 (mid) | Comparable; empirical analysis paper, different focus |
| **SmartSwitch** | **zftquoHTgS.txt** | **6.0** | **—** | **This paper** |
| OpenPRM | fGIqGfmgkW.md | 6.00 | R1 (mid) | Comparable; PRM construction vs inference framework, both accepted |
| Understanding CoT via Info Theory | ouRX6A8RQJ.md | 6.40 | R1 (mid) | Comparable but rejected; limited to toy data + GSM-8K, applicability concerns |
| Don't Take Things Out of Context | W6yIKliMot.md | 6.50 | R1 (mid) | Slightly stronger; accepted, had analysis-method mismatch but well-received |
| Step-by-Step via TSMC | Ze4aPP0tIn.md | 6.60 | R2 (mid) | Slightly stronger; accepted, mild weaknesses only |
| To CoT or not to CoT | w6nlcS8Kkn.md | 6.67 | R2 (mid) | Slightly stronger; accepted, comprehensive meta-analysis |
| Repr Engineering for Reasoning | IssPhpUsKt.md | 6.80 | R1 (mid) | Slightly stronger; accepted, similar hyperparameter concerns but simpler tasks |
| Backtracking Improves Safety | Bo62NeU6VF.md | 8.00 | R1 (strong) | Stronger; different domain (safety), cleaner experimental setup |
| Take a Step Back | 3bq3jsvcQ1.md | 8.00 | R1 (strong) | Stronger; simple impressive prompting method, broad evaluation |

**Round 1 bracket**: [4.0, 7.0]. The paper is clearly above the 2.5–3.0 weak papers (which have flawed methodology or very weak evaluations) and clearly below the 8.0 papers (which have cleaner evaluations or more impactful results).

**Round 2 narrowing**: Within the 4.5–6.5 and 6.0–8.0 bands. SmartSwitch most closely resembles the 6.0–6.5 papers: it has a clear novel contribution and broad evaluation, but the threshold sensitivity concern and missing PRM-reranking baseline keep it below the ~6.8 papers. It is stronger than inference-time papers in the 4.2–5.2 range (RaR, MAgICoRe, On Designing RL Reward) because its evaluation is broader and its method is better motivated.

## Score and Decision

**Score**: 6.0 — A solid paper with a clear novel contribution (identifying and mitigating underthinking via PRM-guided backtracking), broad evaluation across 5 models × 5 benchmarks, and honest limitation disclosure. The threshold sensitivity and missing PRM-reranking baseline are real but not fatal issues that can be addressed in revision.

**Decision**: Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
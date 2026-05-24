Now I have all the information I need. Let me write the consolidated final review.

## Summary

The paper introduces Pi-CCA, a replay-free continual learning framework for vision-language models that maintains a compact "certificate" of canonical correlations and subspaces from CCA, regularizing the model to stay close to this certificate during adaptation. It achieves SOTA results across four standard VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL) among replay-free methods, often surpassing methods that use synthetic replay.

## Strengths

- **SOTA replay-free performance across four benchmarks (Tables 1-2).** Pi-CCA achieves the highest metrics on MTIL (Avg 76.8), X-TAIL (Avg 68.1), VLCL (I2T R@1 48.6), and ConStruct-VL (FA 75.2, AF 2.7) among replay-free methods, and even surpasses GIFT (which uses diffusion-based synthetic replay) on VLCL and ConStruct-VL. These results are supported by confidence intervals (Table 2).

- **Clean, well-structured ablation study (Table 3, Figure 2).** Each component is isolated with clear performance drops: removing spectral term (λ₁=0) costs 2.5 points on MTIL Avg, removing subspace term costs 2.2, and disabling covariance EMA costs 2.7. The certificate capacity Pareto analysis (Fig. 2) confirms a broad efficient ridge with a clear knee point at (k=64, h=256).

- **Novel conceptual framing with supporting analyses.** Reframing forgetting as alignment-geometry drift (rather than proxy-signal drift) is a principled perspective. The paper backs this with task-order sensitivity analysis across 20 random orders (narrow IQRs in Fig. 5), prompt invariance stress tests (Fig. 4), and a theoretical explanation (Appendix §A.4).

- **Downstream-agnostic and parameter-efficient design.** Only LoRA adapters are updated; the method is compatible with any task loss (InfoNCE, cross-entropy, etc.) and maintains constant memory via random orthonormal sketches, without generators or stored past data.

## Weaknesses

### Major

- **Suspiciously perfect correlations in Figure 3.** The paper reports Pearson r=1.00 and Spearman ρ=1.00/0.99 for relationships between geometry drift and performance drops across what appears to be 35+ hyperparameter configurations. For empirical measurements involving multiple independent sweeps (certificate size, EMAs, invariance strength, LoRA capacity, etc.), achieving r=1.00 implies zero scatter — which is inconsistent with the figure caption's mention of a "95% confidence interval shaded area" and "realistic scatter." This is the paper's primary evidence for the causal claim that alignment-geometry preservation drives retention. The authors must: (i) disclose the exact computation linking drift and performance metrics, (ii) provide bootstrapped confidence intervals on the correlations, (iii) clarify whether drift measures and performance drops share any deterministic coupling. Without this, the paper's core conceptual evidence is not credible as presented. **The main SOTA results in Tables 1-2 are independent of this figure** and remain valid, but the "why it works" narrative is weakened.

### Minor

- **"Invariant" framing vs. EMA-updated certificate (presentation gap).** The paper calls the certificate quantities "invariants" (Abstract, Section 3.2) but Eq. 13 updates them at every step via EMA (ρ←(1-α)ρ+αρ̂). The paper is transparent about the mechanism (line 146: "allow controlled plasticity"), but the "invariant" language over-promises relative to what is actually preserved. The method is better described as "regularizing drift of alignment geometry via a compact summary" rather than "preserving invariants." This does not undercut the method's effectiveness but misaligns narrative with mechanism and weakens the claimed distinction from proxy-based methods that also use moving targets.

- **Baseline comparison not controlled for adaptation setup.** The paper reports published numbers from prior work without controlling for the LoRA configuration (rank, which layers are adapted, etc.). Many baselines (ZSCL, Mod-X, C-CLIP) were originally published with different adaptation setups or full fine-tuning. Part of Pi-CCA's gains could stem from its specific LoRA configuration or the prompt perturbation augmentation (ℒ_pi is unique to Pi-CCA and provides data augmentation not used by baselines). The reported SOTA margins (e.g., 76.8 vs. 75.2 on MTIL Avg) are modest enough that uncontrolled factors could affect rankings.

- **Prompt perturbation distribution 𝒫 not fully specified in the main text.** The paper refers to "synonym swap/back-translation/template jitter" (line 237) but does not define the sampling procedure, perturbation strength scaling, or whether perturbations are applied at both train and test time. This information may exist in the (stripped) appendix, but the main text is insufficient for reproducibility of this component.

### Trivial

- The paper uses $\widehat{M}$ in Eq. 12 but the equation text appears garbled (line 142: "M^{(t)} = (∑_{v=1}^t S_v^{(t)})^{-1/2} (∑_{v=1}^t S_v^{(t)})^{-1/2}" — seems to contain a copy-paste error).
- The reproducibility statement mentions code cannot be released during review, which is common but means other researchers cannot verify implementation details.

## Nice-to-Haves

- **Test on longer task sequences** (e.g., >20 tasks). The current evaluation maxes out at 11 tasks (MTIL). Constant-memory methods like Pi-CCA should be tested to see if the certificate EMA eventually drifts too far.
- **Ablation isolating prompt perturbation gains.** Report Pi-CCA's performance without any prompt augmentation for all comparison methods to isolate whether gains come from alignment geometry or from the data augmentation effect of 𝒫.
- **Plot certificate drift over time.** Show cosine similarity between the initial pre-training certificate and the certificate at each subsequent task to visually confirm how much the "invariant" actually drifts.

## Removed Points

- **Criticism that r=1.00 implies data fabrication.** The harsh critic suggested this as a possible explanation. This is speculation; I have reclassified the issue as Major but removed the fabrication insinuation. The paper may have an explainable methodological reason (e.g., using the same underlying hyperparameter to drive both drift and performance in a near-deterministic way for a stable system). The authors need to clarify, not defend against an accusation.

- **Criticism that "mini-batch only" claim is misleading because EMA aggregates globally.** The paper states "using only mini-batch statistics" (line 60) which is accurate — the EMA aggregates mini-batch statistics (covariances) across time, not the data points themselves. This is standard replay-free practice and not misleading.

- **Criticism about missing related works, missing appendix content, missing code, formatting/style nitpicks, and speculative claims about method unfairness.** Removed per meta-review guidelines: appendix content is stripped by the parser, missing related works cannot be confirmed without external search, and formatting issues are parser artifacts.

- **Strength Finder's generic strengths** (e.g., "addressed an important problem," "targeted an interesting question"). These lack specific evidence and are removed.

## Novel Insights

The most interesting observation emerges from synthesizing Table 3 with Figure 3: the spectral and subspace terms each contribute roughly equally (2.5 and 2.2 points on MTIL Avg), but the ablation of the covariance EMA (β=0, 2.7 point drop) is the most damaging single factor — more than removing either geometry term. This suggests that reliable estimation of the cross-modal covariance (via EMA) is at least as important as the specific loss design, a nuance the paper does not highlight. Separately, the task-order robustness (Fig. 5) shows IQRs of ≈0.5-0.8 p.p., which is unusually tight for a replay-free method and suggests the certificate-based regularization genuinely anchors the model to a fixed geometry rather than being task-order-dependent.

## Suggestions

1. **Fix Figure 3 urgently.** Provide the raw scatter data, report bootstrapped 95% CIs on the correlation coefficients, and explicitly rule out deterministic coupling between drift and performance metrics. If the correlations are genuinely near-perfect (e.g., r>0.98), explain why — for instance, if both drift and ΔAvg are monotonic functions of a single varied hyperparameter, then state this directly.
2. **Rename or reframe the "invariant" language** to "alignment anchor," "geometry summary," or "slowly-evolving certificate." This better matches the EMA update mechanism and avoids overclaiming.
3. **Add a controlled comparison** where at least the top-3 baselines are re-implemented with Pi-CCA's exact LoRA configuration to show gains are not from the adapter setup.
4. **Specify the perturbation distribution 𝒫** more concretely (number of perturbations, strength ranges for each perturbation type) in the main paper.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| gc8QAQfXv6.md (Function Vectors for CF) | 9.00 | Stronger: deeper mechanistic analysis, cleaner evidence, no questionable correlations |
| 3i13Gev2hV.md (Hyperbolic VLMs) | 8.00 | Stronger: cleaner empirical evidence, novel pretraining paradigm, no evidential issues |
| sb7qHFYwBc.md (C-CLIP) | 6.50 | Comparable: same sub-area, similar SOTA reporting, but C-CLIP has no correlation-evidence issue | 
| k9NYnsC4Mq.md (PROOF) | 5.67 | Weaker: less comprehensive evaluation, inference-mismatch flaw |
| G9Ea7mlqGO.md (CLIP Online CL) | 3.80 | Weaker: narrower scope, less rigorous evaluation |
| JIlIYIHMuv.md (LVLM-CL) | 2.50 | Much weaker: poor writing, insufficient baselines, unclear contributions |

The paper makes a genuine conceptual contribution (alignment-geometry preservation via CCA certificate) and demonstrates SOTA results across diverse benchmarks. The ablation study and efficiency analysis are thorough. However, the questionable correlation evidence in Figure 3 — which supports the paper's core narrative about why the method works — is a notable weakness that prevents this from being a top-tier paper. The "invariant" framing issue and lack of controlled baseline comparisons are secondary but relevant. Relative to the C-CLIP paper (6.50) which is in the exact same sub-area with similar SOTA claims and no comparable evidential issue, this paper has stronger conceptual novelty but weaker supporting evidence for that novelty. This places it between the two.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
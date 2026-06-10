## Summary

NeuroQuant proposes a post-training quantization (PTQ) approach for implicit neural representation-based video coding (INR-VC) that aims to achieve variable-rate coding from a single pretrained model. The paper identifies that existing PTQ methods fail for non-generalized INR-VC because they assume inter-layer independence, and proposes (1) a full-Hessian sensitivity criterion Ω for mixed-precision bit allocation, (2) network-wise calibration to capture cross-layer dependencies, and (3) channel-wise quantization. Empirical results on UVG with NeRV/HNeRV/HiNeRV backbones show compression gains (27.8%/25.5%/4.8% BD-rate) and encoding speedups of up to 7.9×.

## Strengths

- **Rigorous theoretical identification of why standard PTQ fails for INR-VC**: Section 3.1 provides concrete counterexamples (Examples 1–2, Eqs. 7–8) showing that two functions with identical top Hessian eigenvalues and identical traces have different sensitivities due to off-diagonal terms, and that a *larger* weight perturbation can yield a *smaller* task loss. This cleanly exposes the failure of the inter-layer independence and isotropy assumptions underlying HAWQ, AdaRound, BRECQ, and directly motivates Theorem 1's full-Hessian criterion Ω = Δw^T H Δw.

- **Network-wise calibration is a well-motivated adaptation**: The paper provides empirical evidence (Figure 3c) that non-generalized INR-VC exhibits strong inter-layer/block dependencies, and the choice of network-wise (rather than layer/block-wise) calibration follows from this observation. The unified MSE-oriented calibration derivation (Eqs. 11–15, Remark 1) reducing to min E[||Δz^(n)||²] is clean and sound.

- **Meaningful practical efficiency gains**: The encoding speedup of up to 7.9× (Table 2) for generating new bitrate points versus retraining is a concrete practical benefit, directly substantiating the claim of 80% encoding time reduction. The variable-rate R-D curves spanning INT2–INT8 without separate retraining per bitrate are a genuine capability that prior INR-VC work lacked.

## Weaknesses

### Fatal
None.

### Major

- **The bit-allocation algorithm that delivers variable-rate control is not specified**: The paper presents the sensitivity criterion Ω (Theorem 1) and states it "enables efficient mixed-precision search using techniques like integer programming, genetic algorithms (Guo et al., 2020), or iterative approaches" (line 127). However, it never discloses which algorithm was actually used, what its hyperparameters were, or what its computational cost was. Without this, the method is under-specified to the point of irreproducibility. The reported encoding time savings (Table 2) conflate the time to run bit-allocation search with the time to calibrate QPs; if the search itself is expensive, the claimed speedups may be misleading. This is the single most important gap in the paper.

- **Internal inconsistency about INT2 performance undermines the claims**: The abstract states NeuroQuant "enables quantization down to INT2 with minimal reconstruction loss" and line 27 says "without notable performance degradation." However, line 314 states "the degradation is still noticeable below INT3. As a result, we do not recommend INT3 and below for variable-rate scenarios." These statements are directly contradictory regarding INT2. The paper never resolves this tension, and the two claims cannot both be accurate as written.

### Minor

- **No per-sequence breakdowns or measures of variability**: Results are reported only as aggregate PSNR over the UVG dataset (7 sequences). Video coding results vary substantially across sequences; without per-sequence results or confidence intervals, it is impossible to assess whether reported margins are robust or driven by a few favorable sequences.

- **Baseline comparison fairness is not adequately controlled**: The four PTQ baselines (AdaRound, BRECQ, QDrop, RDO-PTQ) were designed for general-purpose vision networks. The paper states they were run using "open-source codes" (line 231) but provides no evidence that their hyperparameters (calibration data size, number of iterations, etc.) were tuned for INR-VC models. The observed performance gap could be partly due to untuned hyperparameters rather than fundamental inapplicability of the methods. An ablation controlling for calibration setup is needed to isolate the inter-layer dependence factor the paper emphasizes.

- **Single dataset and limited metrics**: Evaluation uses only the UVG dataset (7 sequences) and only PSNR. Standard video coding evaluations typically include additional datasets (e.g., Xiph, MCL-JCV) and metrics (MS-SSIM, VMAF). This limits the generality of the results.

- **No hardware specifications for encoding time experiments**: Table 2 reports encoding times without specifying the GPU, CPU, or other hardware, making the speedup numbers difficult to contextualize or reproduce.

### Trivial
None.

## Nice-to-Haves

- Section 3.3 (variational inference framing) provides a theoretical perspective but does not drive the method design in Sections 3.1 and 3.2. It reads more as a discussion/limitations section. The space could have been more productively used to specify the bit-allocation algorithm or provide ablation studies.
- Reporting the wall-clock time and GPU memory cost of computing the sensitivity criterion Ω (which requires Hessian-vector products) would be useful for practitioners evaluating the method.
- Analysis of sensitivity to calibration data size would strengthen the PTQ claims.

## Removed Points

These points were flagged by the reviewers but are removed from the final review for the following reasons:

- *"Section 3.3 is a re-description that doesn't do work"* — Partially valid; demoted to Nice-to-Have. The section does provide a legitimate theoretical connection between NeuroQuant and variational inference/R-D optimization (Remark 2), and it acknowledges limitations. It is not a fatal flaw that the section doesn't drive design.
- *"Comparison could be unfair favoring NeuroQuant" overstated phrasing* — The core concern (baseline hyperparameters may be untuned) is legitimate and retained as a Minor weakness. The more extreme framing ("unfair in ways that favor NeuroQuant") is softened to a controlled concern about missing hyperparameter tuning evidence.
- *"The evidence base is substantially weaker than the claims demand" (in its strongest form)* — The core concern about missing per-sequence breakdowns and variance is retained. The framing that this makes evidence "unverifiable" from text is overly dramatic given that the key numbers (27.8%, 25.5%, 4.8%) are stated in text, and the image-embedded tables are a parser issue, not an author error.
- *General criticisms about missing confidence intervals for large-scale benchmarks* — Weakened: single-run evaluation is the norm for this type of benchmark.
- *"No results on standard compression metrics like MS-SSIM or VMAF"* — Retained as a limitation. This is a genuine gap, but it is not a core flaw since the paper appropriately scopes to PSNR.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard observations one would expect: the theoretical motivation is strong, the bit-allocation gap is a real reproducibility issue, and the evaluation could be more thorough. No reviewer identified a fundamentally new insight about the method or the problem that the paper itself missed.

## Suggestions

1. **Specify the bit-allocation algorithm explicitly**: Describe exactly what optimization was used (greedy iterative search, integer programming, etc.), report its computational cost separately from QP calibration, and compare against a uniform-allocation baseline at the same average bitwidth to isolate the benefit of mixed-precision allocation.
2. **Resolve the INT2/INT3 contradiction**: Clarify whether INT2 is usable with "minimal reconstruction loss" or whether degradation is "noticeable" and not recommended. Present explicit INT2 results with numbers.
3. **Add per-sequence results and variability measures**: Report PSNR per UVG sequence (e.g., as a table or box plot) to demonstrate consistency across videos.
4. **Control baseline hyperparameters**: Verify and report whether each baseline method's hyperparameters (calibration data size, number of iterations) were tuned on INR-VC validation data, and whether the observed gaps persist after tuning.
5. **Add hardware specifications and calibration data size analysis** to strengthen the experimental section.

## Score and Decision

**Score**: This is a paper with a genuinely useful core insight — that INR-VC's inter-layer dependencies invalidate standard PTQ assumptions — and reasonable technical contributions (network-wise calibration, the Ω criterion). However, the paper has two decisive weaknesses that prevent acceptance as-is: the bit-allocation algorithm is unspecified, making the method irreproducible, and there is an internal contradiction about INT2 performance that undermines confidence in the reported results. The evaluation, while positive, lacks per-sequence breakdowns, confidence measures, and adequate baseline control. The paper needs substantial revision before it meets a top-venue bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
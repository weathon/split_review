- Decision: Accept
- Avg Score: 7.20
- Scores: 8, 6, 6, 8, 8
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces NeuroQuant, a post-training quantization (PTQ) approach for variable-rate video coding with implicit neural representations (INR-VC). The key idea is to achieve variable bitrates by adjusting quantization parameters of pre-trained weights rather than retraining the entire network for each target rate. The paper proposes: (1) a sensitivity criterion Ω = Δwᵀ H Δw that captures off-diagonal Hessian information and perturbation directionality, (2) network-wise calibration to handle inter-layer dependencies in non-generalized INR-VC, and (3) channel-wise quantization steps. Experimental results on UVG show consistent gains over existing PTQ methods and QAT baselines, with up to 7.9× encoding time speedup.

## Strengths

1. **Principled sensitivity criterion accounting for inter-layer dependencies.** Section 3.1 identifies that existing Hessian-based criteria (HAWQ, HAWQ-V2) assume layer independence and isotropy, which break down for non-generalized INR-VC. The paper proposes Ω = Δwᵀ H Δw (Theorem 1) and uses Hessian-vector products to avoid explicit Hessian computation (Eq. 10). Concrete toy examples (Examples 1 and 2) demonstrate why diagonal-only criteria miss off-diagonal Hessian terms and why perturbation direction matters, providing a clear theoretical advance over prior mixed-precision methods.

2. **Network-wise calibration and channel-wise quantization derived from properties of INR-VC.** Section 3.2 uses Figure 3(c) to empirically show that inter-layer/block dependencies are significant in non-generalized INR-VC, unlike generic networks where layer/block-wise calibration suffices. The paper derives a unified MSE-oriented calibration objective (Eq. 15) and a continuous optimization framework (Eq. 16) for jointly calibrating QPs at channel granularity — a principled departure from AdaRound/BRECQ-style calibration.

3. **Substantial encoding time reduction for variable-rate operation.** Table 2 shows NeuroQuant requires 3.2 hours (HNeRV) to support a new bitrate vs. 15 hours for retraining, with even larger speedups for HiNeRV (3.8 h vs. 22 h). This directly supports the paper's central motivation: avoiding expensive retraining for each target rate.

4. **Empirical demonstration that mixed precision enables finer-grained rate control.** Figure 5 shows multiple mixed-precision operating points between uniform 4-bit and 8-bit, confirming that mixed precision yields better R-D trade-offs for a given total bitrate and offers flexibility beyond the limited discrete options of uniform bitwidth quantization.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation studies isolating the claimed contributions.** The paper proposes three main technical novelties: (i) the Ω sensitivity criterion with off-diagonal Hessian terms, (ii) network-wise calibration, and (iii) channel-wise quantization. However, no controlled experiment measures the impact of removing any of these components. Does the Ω-based mixed-precision search outperform a simpler trace-based search (e.g., HAWQ-V2)? Does network-wise calibration outperform block-wise or layer-wise calibration for INR-VC? Table 1 compares NeuroQuant to existing PTQs but those baselines differ in multiple aspects simultaneously (calibration granularity, bit allocation, optimization method). Without ablations, the improvement cannot be attributed to the paper's specific insights. This is an evidential gap: the conclusions may be correct, but the current evidence does not support attributing them to the proposed components.

2. **Calibration data construction is not specified.** The paper never describes how the calibration data for Eq. 15–16 is constructed: which frames or coordinate-pixel pairs are used, how many are used, and whether they overlap with frames on which PSNR is reported. While in non-generalized INR-VC the entire video is the training data (making some overlap inherent), the lack of any specification is a methodological gap. The paper should clarify the calibration set size, selection strategy, and whether evaluation frames are excluded from calibration.

3. **Comparison to QAT methods confounds mixed-precision with other contributions.** In Table 1, NeuroQuant uses mixed precision (marked with \*) while the QAT baselines (FFNeRV, HiNeRV) use uniform precision. Mixed precision inherently provides finer rate control and better R-D trade-offs, so the comparison conflates the benefit of mixed-precision allocation with the benefit of NeuroQuant's specific calibration and sensitivity criteria. A fairer baseline would be NeuroQuant with uniform precision to isolate the effect of the calibration and sensitivity components.

4. **R-D curves for PTQ baselines are missing from Figure 4.** Table 1 compares NeuroQuant against AdaRound, BRECQ, QDrop, and RDO-PTQ, but Figure 4 (the R-D curves) only includes direct 8-bit quantization and HiNeRV QAT — none of the task-oriented PTQ baselines appear. To substantiate the claim that NeuroQuant achieves superior variable-rate performance over "existing techniques," the R-D curves for all PTQ baselines should be included in the figure.

### Minor

1. **Mixed-precision bit-allocation search algorithm is not specified.** The paper states (Sec. 3.1) that search can use "integer programming, genetic algorithms, or iterative approaches" but never reports which method was actually used, how many configurations were evaluated, or how the constraint in Eq. 6 was enforced. It is also unclear whether the encoding times in Table 2 include the mixed-precision search time. This harms reproducibility.

2. **No statistical reporting.** The paper does not report error bars, variance, or multiple-run statistics for any experiment. While single-run evaluation is common for large-scale PTQ benchmarks, at least one experiment with multiple trials (e.g., different rounding initializations) and standard deviation would strengthen confidence in the reported gains.

3. **The variational inference perspective (Sec. 3.3) is presented as a contribution but is loosely connected to the algorithm.** The variational inference section reframes the problem but does not derive any component of NeuroQuant itself. The claim that NeuroQuant "bridges the mismatch" between representation and compression by optimizing log p(x|w̃) is equally true of any PTQ method that calibrates QPs, not specific to NeuroQuant.

### Trivial
None.

## Nice-to-Haves

- An ablation using a single model (e.g., HNeRV 1M) directly comparing uniform INT6, mixed-precision with trace-based sensitivity, mixed-precision with Ω-based sensitivity, and different calibration granularities (layer-wise, block-wise, network-wise) would directly validate the paper's theoretical claims.
- A brief discussion of how the calibration data construction aligns with standard PTQ practice for non-generalized models would address the reproducibility gap cleanly.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism about no comparison to traditional codecs (H.265, VVC)** — Scope creep. The paper is about quantization methods for INR-VC; comparing to H.265/VVC is outside the stated scope.
2. **"'Direct (Naive)' row header is misleading"** — Formatting/presentation nitpick.
3. **"Assumption that gradient w.r.t. network outputs is zero is invalid for held-out calibration data"** — The setting is non-generalized INR-VC where the model is trained on the video itself; calibration data from the same video is standard PTQ practice. The criticism overstates a standard assumption.
4. **"The paper never returns to show that real INR-VC layers exhibit cross-layer interactions"** — This is factually incorrect; Figure 3(c) explicitly shows cross-layer/block correlation statistics.
5. **"Overreaches by claiming to advance video coding technology"** — An opinion about scope of claim, not a verifiable weakness.
6. **Strengths about general importance of the problem** — Generic; removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The two reviews add no synthesis or insight not already present in the paper itself. The key tension — that the paper makes well-motivated theoretical claims but lacks the ablations to empirically validate them — is a straightforward gap identified by the Harsh Critic and is not a novel observation beyond what the paper's structure implies.

## Suggestions

1. **Add a controlled ablation study** comparing (a) uniform-precision NeuroQuant, (b) mixed-precision with trace-based sensitivity (Ω degraded to diagonal), (c) mixed-precision with Ω-based sensitivity, (d) layer-wise calibration, (e) block-wise calibration, (f) network-wise calibration, all on the same model architecture. Report mean and std over multiple runs.
2. **Specify the calibration data construction** — number of coordinate-pixel pairs, how they are sampled across frames, and whether evaluation frames are excluded.
3. **Specify the mixed-precision search algorithm** used (even if a simple greedy heuristic) and report its runtime separately from the calibration time.
4. **Include R-D curves for all PTQ baselines** (AdaRound, BRECQ, QDrop, RDO-PTQ) in Figure 4 to enable full comparison.
5. **Add a uniform-precision NeuroQuant baseline** to Table 1 to separate the benefit of mixed-precision allocation from the benefit of the calibration/sensitivity components.

Now I have a thorough understanding of the paper, the reviews, and calibration anchors. Let me compose the final consolidated review.

---

## Summary

This paper proposes HOPE (Hankel Operator parameterization), a new way to parameterize the LTI systems inside state-space models (SSMs) by directly using the Markov parameters of a Hankel matrix instead of the traditional (A, B, C) matrices. The authors connect Hankel singular value decay to SSM expressiveness, prove that random HOPE parameterizations almost surely have high numerical rank (Ω(n)) and enjoy Lipschitz stability to parameter perturbations, and claim non-decaying memory within a fixed time window. Empirical results are provided on sCIFAR-10 and a noise-padded variant.

## Strengths

- **Novel theoretical unification of SSM initialization and training difficulties via Hankel singular values.** The paper provides a clean framework (Theorem 2.1) showing that random LTI systems have low numerical rank (scaling as n^β with β<1), formally explaining why random initializations fail and why careful designs like HiPPO are needed. This goes beyond prior empirical observations by giving a rigorous characterization.

- **Provably high numerical rank under HOPE parameterization (Theorem 3.1).** This directly contrasts with the low-rank result for standard SSMs, showing that random HOPE parameterizations almost surely have numerical rank Ω(n) (ignoring log factors), eliminating the need for specialized initialization schemes.

- **Provable numerical stability to parameter perturbations (Theorem 3.2).** The transfer function of HOPE is Lipschitz in the Markov parameters with constant √n, independent of the parameter values. This is a genuine advantage over standard (A,B,C) parameterizations where stability depends on poles' proximity to the imaginary axis.

- **Parameter efficiency and clean implementation.** HOPE uses n complex parameters per LTI system vs. 3n for vanilla S4D. The nonuniform FFT-based implementation (Algorithm 1) has complexity O(L log L + nL), matching S4D.

- **Empirical validation on sCIFAR-10 and noisy-sCIFAR.** The HOPE-SSM shows robust training without special learning rate schedules, and outperforms S4D on the noise-padded long-memory variant, with empirical impulse response plots confirming non-decaying memory for t∈[0,n].

## Weaknesses

### Fatal

1. **The central LRA results are missing from Table 1.** The paper's abstract states that HOPE-SSM "demonstrates improved performance on Long-Range Arena (LRA) tasks" and the introduction claims "its performance exceeds that of its S4 and S4D counterparts" (line 83). Experiment III (line 425) says "We show the performance of our model in Table 1." The table caption (line 429) reads "Test accuracies in the Long-Range Arena of our HOPE-SSM and other models." **However, the actual table (lines 432-450) contains no row for HOPE-SSM** — it only lists DSS, S4++, Reg. S4D, Spectral SSM, Liquid S4, S5, S4, and S4D. The paper's headline empirical claim is entirely unsupported by any data. This is not a formatting artifact or parser error; the LaTeX table simply does not include HOPE results. A paper whose central contribution claims improved large-scale benchmark performance cannot be accepted when those results are absent from the submission. (Note: the Strength Finder's claim that "Table 1 shows HOPE achieves competitive or superior performance" is factually wrong — it misattributes S5's average score of 87.46 to HOPE.)

### Major

2. **The theoretical guarantees on rank and stability are proven only at initialization, with limited analysis of behavior during training.** Theorem 3.1 analyzes random Hankel matrices at initialization. Theorem 3.2 bounds perturbation sensitivity for any h. However, neither theorem formally guarantees that the numerical rank is preserved *after gradient descent updates*. The paper asserts that "a system parameterized by HOPE does not lose rank during training" (line 347) but supports this with only a single empirical histogram (Figure 5). While the empirical evidence is positive, this gap weakens the claimed theoretical advantage over S4D, whose rank preservation is also documented empirically. The paper would benefit from tracking singular values across multiple training runs and model sizes.

3. **The non-decaying memory claim is rigorously established only at Δt=1, and the extension to general Δt is heuristic.** The theoretical derivation of non-decaying memory (Section 4, Advantage III) analyzes the discrete impulse response h_k, which is non-zero for k<n. The paper states that "from a continuous-time perspective… our system's memory does not decay for t∈[0,n]" (line 365). However, when Δt≠1 (as in the noisy-sCIFAR experiment with Δt=0.1), the effective impulse response is obtained by resampling the transfer function via Algorithm 1 — the paper provides no formal analysis of whether the non-decay property survives under this resampling. The empirical results (Figure 6) do show flat impulse response for t∈[0,64], but the theoretical justification for the continuous-time claim is conflated with the discrete-time analysis. The explanation for the significant accuracy gap on noisy-sCIFAR (HOPE ~65% vs S4D ~45%) may involve other factors (e.g., optimization dynamics) beyond the claimed memory mechanism.

4. **The three initialization schemes (init_1, init_2, init_3) used throughout the motivating experiments are never defined.** Section 3 (lines 147-150) introduces init_1, init_2, init_3 as three initialization schemes for S4D's LTI systems, but never specifies what they are in terms of distributions or parameter values. From context, init_1 appears to be a random system with poles near the imaginary axis, init_2 another random variant, and init_3 HiPPO-LegS — but the reader is left to infer this from figures and captions. This hinders reproducibility and makes the "mystery" difficult to interpret precisely.

### Minor

5. **The causal link between Hankel singular value decay and task performance is heuristic, not proven.** The paper uses the ROM approximation bound to argue that fast-decaying Hankel singular values imply low expressiveness. While the paper is appropriately careful about this (calling it a "heuristic" and "protocol"), the entire motivation — that high numerical rank is necessary for SSM performance — rests on correlational evidence (Figure 3). A stronger design (e.g., systematically varying numerical rank while holding everything else fixed) would strengthen the case, though this does not invalidate the empirical results.

6. **Theorem 2.1 assumes B∘C has i.i.d. normal entries, but S4D models often use structured B and C (e.g., constant vectors).** The theorem is interesting as a theoretical statement about the random parameter space, but the assumptions may not reflect practical S4D initialization distributions, limiting the theorem's predictive power for actual S4D behavior.

7. **The paper does not report final accuracy numbers for the sCIFAR and noisy-sCIFAR experiments — only plots.** Figures 5 and 6 show accuracy curves without reporting final numerical values, making precise quantitative comparison difficult. Standard deviations are also not reported for these experiments.

### Trivial

8. The memory claim at line 365 says "from a continuous-time perspective, unlike S4D, our system's memory does not decay for t∈[0,n]" — but the reasoning uses the *discrete* impulse response h_k. While the empirical Figure 6 supports the continuous claim, the text's justification conflates the two perspectives.

## Nice-to-Haves

- A controlled experiment varying n (e.g., 32, 64, 128, 256) on a long-sequence task would directly test whether HOPE's finite memory window of n steps is the mechanism driving performance, vs. other factors in optimization.
- An ablation that trains HOPE with a forced low-rank parameterization (projecting h onto a low-dimensional subspace) would directly test the "high numerical rank is necessary" claim.
- Standard deviations and final accuracy numbers should be reported for all experiments, not just LRA.
- Testing HOPE in selective SSMs (e.g., Mamba-style architectures) would broaden the contribution beyond LTI systems.

## Removed Points

- **Criticism that missing LRA results = "the paper cannot be accepted in this form"**: This point is *kept* (it's the fatal weakness). However, the harsh critic's Additional D Needed analysis about the noisy-sCIFAR memory explanation and the "Deeper Analysis Needed" section #1 are kept as the memory weakness above but softened — the paper does provide empirical validation of non-decaying memory (Figure 6), even if the theoretical justification is incomplete.
- **Criticism about "continuous-time impulse response does not cut off at t=n"**: This is a misreading. The paper never claims the continuous-time response cuts off at t=n; it claims it does not *decay* for t∈[0,n]. The discrete response is zero for k≥n. Kept as trivial weakness #8.
- **Strength Finder's "Strong empirical performance on Long-Range Arena"**: Removed as factually false — the table does not contain HOPE results. The score 87.46 belongs to S5.
- **Criticism that the paper should report more results on multiple seeds/learning rates for HOPE rank preservation**: Kept as major weakness #2, but softened — the paper does show one example (Figure 5) and this is standard for empirical SSM papers.
- **Complaint about missing appendix content**: Removed per instructions — appendices may exist in original submission.
- **Formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

The harsh critic's point about the Δt≠1 memory analysis identifies a genuine gap that goes beyond typical reviewing: the paper's most practically relevant and novel claim (non-decaying continuous memory at any Δt) rests on a theoretical derivation that only directly applies at Δt=1, with the extension being an intuitive but unproven leap. This is exactly the kind of oversight that a reviewer with signal processing expertise would catch but a machine learning generalist might miss. The missing LRA results are a separate, even more fundamental issue. Together, these two flaws — one structural and one evidential-theoretical — mean the paper's two flagship claims are each unsupported in different ways. The strength of the theoretical framework (Hankel singular value analysis, Theorems 3.1 and 3.2, parameter efficiency) is real, but the paper overclaims on both the empirical and theoretical fronts relative to what is actually delivered.

## Suggestions

1. **Most critically: add the HOPE-SSM row to Table 1** with median and standard deviation over 5 seeds for each LRA task. Without this, the paper's headline contribution is unsubstantiated. If the LRA results were inadvertently omitted due to a formatting error, the authors should clarify this and provide the missing data.
2. Provide a formal analysis (or at minimum a clear theoretical argument) for whether the non-decaying memory property survives resampling when Δt≠1, or explicitly scope the memory claim to Δt=1.
3. Define init_1, init_2, init_3 explicitly in terms of their parameter distributions.
4. Report final numerical accuracy values (with std) for sCIFAR and noisy-sCIFAR experiments, not just plots.
5. Track numerical rank across multiple training runs and model sizes to substantiate the "does not lose rank during training" claim beyond a single histogram.

## Score and Decision

**Calibration anchors** (all from the provided calibration set):

| Anchor Path | Avg Score | Comparison to this paper |
|---|---|---|
| `GRMfXcAAFh.md` (Oscillatory SSM) | 8.00 | Both propose new SSM parameterizations, but Oscillatory SSM delivers complete experimental results including large-scale benchmarks; this paper has missing core results. **This paper is significantly weaker.** |
| `DjeQ39QoLQ.md` (Robustifying SSMs) | 6.50 | Similar theoretical depth and SSM focus, but that paper's experimental section is complete and supports its claims. **This paper is notably weaker due to missing LRA data.** |
| `sZJNkorXMk.md` (Autocorrelation Matters) | 6.67 | Both analyze SSM initialization theoretically; that paper's experiments are complete and reproducible. **This paper has a more novel parameterization but far less complete empirical support.** |
| `BwG8hwohU4.md` (StableSSM) | 5.33 | Both propose SSM reparameterizations with theory + experiments. StableSSM was rejected partly due to disconnect between theory and experiments. **This paper has a similar disconnect (missing LRA results) and is comparatively weaker.** |
| `hgjpO0H0id.md` (interplay learning/memory) | 4.00 | Both study SSM properties theoretically with limited experiments. **Comparable in completeness, but this paper's parameterization contribution is more novel.** |
| `YuFUUcSUgx.md` (You Can Train from Scratch) | 4.00 | About LRA limitations, not a new method. **Different type of contribution, but both have significant evidential gaps limiting acceptance.** |
| `6ifeGfWxtX.md` (Slashed Normal) | 3.75 | Parameterization paper with limited empirical validation. **Comparable in having a novel parameterization but incomplete empirical support.** |

Relative to these anchors, this paper sits in the 3-4 range. It has genuine theoretical novelty (Hankel operator framework, Theorems 3.1 and 3.2) and some positive empirical signals (sCIFAR, noisy-sCIFAR), but the **missing LRA results for the paper's central claim** are a fatal structural flaw that prevents acceptance. The paper cannot be published with its flagship empirical claim entirely unsubstantiated.

Even if the LRA results were added (and one assumes they would be competitive, given the quality of the rest of the paper), the memory claim at general Δt would still need better theoretical support. In its current form, the paper is a promising but incomplete draft.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>
- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me construct the consolidated review.

## Verification of Reviewer Claims Against the Paper

**Harsh Critic Claim 1** — "STREAM-T built on non-obvious design choices without mathematical justification": The paper does provide conceptual rationale (lines 62-66: 1/f fluctuation, why mean/variance would be biased) and empirical validation through toy experiments (Figs 2-4). No ablation of individual components is present in the main text. The skewness derivation references the appendix (line 69). The claim is partially valid but overstated as "critical."

**Harsh Critic Claim 2** — "skewness formula is opaque and conflates discrete sums with continuous distributions": The formula on line 71 is indeed presented without full derivation steps in the main text. The appendix is referenced. This is a clarity concern.

**Harsh Critic Claim 3** — "no analysis showing alternative simpler approaches would fail": The paper gives conceptual reasoning (line 66: low-frequency dominance biases mean/variance) but no empirical comparison. Valid minor weakness.

**Harsh Critic Claim 4** — "human evaluation relegated to appendix, not available for review": Per the rules, appendix content is stripped by the parser but exists in the original submission. Must remove this criticism.

**Harsh Critic Claim 5** — "No comparison with FVD's correlation given": The paper says "FVD remains less effective for both aspects" (line 207) — a comparative statement exists, just without the numerical values in the main text. Minor presentation issue.

**Strength Finder** — All claimed strengths are grounded in specific figures/tables. Strength 4 partially references appendix detail but the correlation values (0.9, 0.6) are in the main text. No strengths to remove.

---

## Summary

This paper proposes STREAM, a new evaluation metric for video generative models that independently assesses spatial quality (STREAM-S: fidelity and diversity) and temporal naturalness (STREAM-T). The key idea is to use per-frame image embeddings with FFT along the temporal axis to decouple spatial and temporal aspects, enabling length-agnostic evaluation. STREAM-T characterizes temporal flow via power-law distributions of Fourier amplitudes and compares their skewness distributions, while STREAM-S adapts precision/recall to video via mean FFT amplitudes.

## Strengths

- **Clean decoupling of spatial and temporal evaluation validated by controlled experiments**: Figures 2-4 demonstrate that STREAM-T remains invariant to per-frame visual noise while STREAM-S degrades proportionally, and vice versa for temporal distortions (local swaps, global swaps, stop scenes). This directly validates the core claim of independent assessment.

- **Length-agnostic evaluation demonstrated on long videos**: STREAM evaluates 128-frame videos directly, while FVD requires a sliding-window adaptation (sFVD). Table 2 reports STREAM scores for 128-frame generations, supporting the universal-applicability claim.

- **Bounded, interpretable scores enable model-level diagnostics**: STREAM-T, STREAM-F, and STREAM-D all lie in [0,1] and reveal distinct model trade-offs invisible to a single FVD score. For example, TATS has high STREAM-F (0.912) but low STREAM-D (0.085), while VideoGPT has moderate STREAM-F (0.781) but higher STREAM-D (0.327) — Table 1.

- **Systematic toy experiments with controlled confounders**: Using the CATER dataset (geometric objects on static background), the authors isolate specific spatial and temporal degradation types (local swap, global swap, stop scenes, random translation, luminance shift, color jitter, Gaussian noise) with clean, monotonic responses per type.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The STREAM-T skewness formula derivation is opaque in the main text.** The skewness formula on line 71 (`skewness = sqrt(K) * sum_ζ ζ^{(3-α)} / sqrt(C * sum_ζ ζ^{(2-α)}`) jumps from the definition of skewness to a simplified form that appears to omit the mean-centering terms (E[ζ] appears nowhere in the final expression, yet frequency ζ is always non-negative so E[ζ] > 0). The full derivation is referenced to an appendix section (`\Aref{sec:moment_generating_function}`), but the main text alone does not provide enough detail for a reader to verify the formula. While the appendix exists in the original submission, a sketch of the derivation steps — or a note about any centering/approximation assumptions — would substantially improve reproducibility and reviewer confidence.

- **No empirical ablation of STREAM-T components.** The paper provides conceptual motivation for using power-law skewness over simple mean/variance of Fourier amplitudes (low-frequency "1/f" dominance) but does not empirically compare STREAM-T against simpler alternatives (e.g., directly comparing mean skewness values across real/fake, or using variance of Fourier amplitudes). An ablation showing that each design choice (power-law fitting, skewness, histogram construction, per-dimension correlation) is necessary — and that simpler baselines fail — would strengthen the paper.

- **Human evaluation details are too sparse in the main text.** The paper reports Spearman correlations of 0.9 for realism and 0.6 for temporal coherence and states that "FVD remains less effective for both aspects" (line 207), but does not give FVD's actual correlation values in the main body. For a metric paper where human alignment is a central claim, the main text should report the FVD numbers alongside STREAM's.

### Trivial

- The algorithm pseudocode (Algorithm 1, line 85) uses `\FOR{$X\in\mathcal{X}$ and $Y\in\mathcal{Y}$}` which is ambiguous about whether the loop iterates over paired or independent samples.

## Nice-to-Haves

- An ablation comparing STREAM-T against simplified variants (e.g., directly comparing mean/variance of skewness without histogram construction, or comparing mean/variance of Fourier amplitudes without power-law transformation).
- A study of how the choice of image embedding network (beyond DINO) affects all three components of STREAM.

## Removed Points

- **"Human evaluation relegated to the appendix (not available for review)"** — Removed per the rule that appendix content is stripped by the parser but exists in the original submission. The paper correctly references the appendix for full study details.
- **"The temporal metric has a critical weakness that prevents acceptance"** — This is an overstatement. The STREAM-T design is conceptually motivated and empirically validated through controlled experiments (Figs 2-4). The derivation details are in the appendix, and the overall approach works as demonstrated.
- **"No comparison with FVD's correlation is given"** — The paper states "FVD remains less effective for both aspects," which is a comparative statement. The numerical comparison is in the appendix. This is a presentation issue, not a missing comparison.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' analyses do not surface an observation about the paper that the paper itself does not already articulate.

## Suggestions

1. Provide a brief sketch of the skewness derivation in the main text, or at minimum state any assumptions (e.g., whether ζ is zero-centered after some transformation) that lead to the simplified formula.
2. Add a small ablation table comparing STREAM-T against simpler alternatives (direct skewness mean/variance comparison, Fourier amplitude mean/variance) on at least one toy experiment (e.g., the local swap/global swap setup).
3. Include FVD's human-correlation numbers in the main text alongside STREAM's.

**Evaluation summary**: The paper addresses an important gap — the lack of decoupled spatial/temporal evaluation metrics for video generation. The core idea (per-frame image embeddings + FFT) is clean, the spatial component (STREAM-S) is well-justified, and the controlled experiments convincingly demonstrate the claimed decoupling. The temporal component (STREAM-T) has a more involved design whose full derivation is deferred to the appendix and whose design choices are not empirically ablated, but the metric as a whole demonstrably works on both toy and real data. These are addressable weaknesses and do not undermine the paper's substantive contribution.

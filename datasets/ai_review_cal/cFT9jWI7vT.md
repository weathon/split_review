- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6
Now I have a clear understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper investigates architectural sensitivity in untrained network priors (DIP) for accelerated MRI reconstruction. It identifies that shallower/wider architectures overfit more due to faster convergence of high-frequency components—not merely parameter count—and proposes two simple, architecture-agnostic remedies: (1) bandwidth-constrained input via Gaussian blur on the noise input, and (2) learnable Lipschitz regularization. Experiments show these methods lift underperforming architectures to match or surpass much larger ones, reducing the need for architectural tuning.

## Strengths

1. **Systematic identification of architectural causes of overfitting** – Section 4 (Table 2, Figure 3) carefully isolates depth, width, skip connections, kernel size, and upsampling type, demonstrating that shallower/wider architectures fail because their configuration promotes faster convergence of high frequencies, not because of parameter count. The controlled comparison of bilinear vs. nearest neighbor upsampling (Figure 2) provides concrete evidence that low-pass characteristics are the mechanism behind better generalization.

2. **Two simple, effective, architecture-agnostic remedies** – The paper proposes bandwidth-constrained input (Gaussian blur on noise, implementable in one or two lines of code) and Lipschitz regularization. Figure 5 shows these methods lift underperforming architectures (e.g., A2_64) to match or surpass the best architecture (A8_256), directly supporting the claim that architectural biases can be mitigated without modifying the architecture itself. The methods require minimal hyperparameter tuning (sigma sampled uniformly from [0.5, 2.0], λ=1 fixed).

3. **Compact model outperforms larger classic architectures** – Table 6 demonstrates that the improved A2_64 (with the proposed techniques) surpasses ConvDecoder, Deep Decoder, and the original DIP despite having far fewer parameters. This provides concrete evidence that architecture-insensitivity enables efficient deployment.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with standard overfitting-mitigation baselines for DIP** – The paper targets overfitting in untrained networks but does not compare against early stopping or self-validation via measurement splitting (Yaman et al., 2021; Wang et al., 2021), which are the most straightforward baselines for this problem. The paper discusses these methods in Related Work (Section 2) and even notes that early stopping "encourage[s] smoothness implicitly," yet never benchmarks against them. Without this comparison, the reader cannot assess whether the proposed methods offer a genuine advantage over simply stopping early or using a validation subset. The headline claim of "dramatically improving under-performing architectures" is weakened because early stopping is a trivial, default alternative that may achieve similar gains. This omission cuts across Tables 4–5 and Figure 5.

2. **No statistical variance reporting** – All quantitative results (Tables 4–6) are reported as point estimates (PSNR/SSIM averages) without standard deviations, confidence intervals, or any indication of variance across noise input draws or slices. Untrained networks are known to be sensitive to initialization. Several comparisons show very small margins (e.g., Table 4 A2_64 PD: 33.02 vs 33.07; A2_256 PD: 33.10 vs 33.14), and without error bars these differences are indistinguishable from noise. This is a significant evidential gap for an empirical paper making claims of "substantial improvement."

3. **Inconsistent upsampling choice between analysis and main experiments** – Section 4.1 demonstrates that bilinear upsampling (stronger low-pass filter) "produces more stable and better results" than nearest neighbor, and that using nearest neighbor makes architectures "more susceptible to noise and overfitting" (Section 4.2, line 104). Yet all main experiments (Section 6.2) use nearest neighbor upsampling without explicit justification. While testing on a harder baseline does not invalidate the results, the paper should justify this design choice or test both conditions. As written, the paper creates an inconsistency between its own analysis (bilinear is better) and its experimental setup (nearest neighbor is used), which undermines the coherence of the evaluation.

### Minor

1. **Overclaiming "first time" contribution** – The abstract states "for the first time, architectural biases on untrained MRI reconstruction can be mitigated without architectural modifications." This phrasing is too strong: prior work (self-validation, early stopping, subspace optimization) also addresses overfitting without architectural changes, even if through different mechanisms. The paper's core insight about frequency-domain input manipulation is novel, but the "first time" framing invites unnecessary criticism.

2. **Confusing "average median values" phrasing** – Figure 5 caption states "denotes the average median values of the results from the improved architectures." It is unclear whether this means the average of per-slice medians or the median of per-slice averages. This should be clarified.

3. **Modest marginal benefit of Lipschitz regularization in several cases** – In Tables 4 and 5, the additive gain from Lipschitz regularization on top of input filtering alone is often small (e.g., +0.04 PSNR for A2_256 on PD). The paper could more honestly characterize when each component provides meaningful benefit versus when input filtering alone suffices. A full ablation (input-only vs. Lipschitz-only vs. both) on each architecture would strengthen the claims.

4. **Table 2 reports SSIM only** – The main architectural analysis table reports only SSIM, while PSNR is also standard for MRI reconstruction and is reported in later tables. Including PSNR in Table 2 would strengthen the analysis.

5. **No sensitivity analysis for sigma in main text** – The Gaussian blur sigma is uniformly sampled from [0.5, 2.0], but the main text does not analyze how reconstruction quality varies across this range or whether the optimal sigma differs by anatomy or acceleration factor. The supplement is referenced but a brief plot in the main text would improve confidence.

### Trivial
- None of note beyond the phrasing issues mentioned above.

## Nice-to-Haves

- Compare against early stopping and self-validation baselines to clarify the advantage of the proposed methods over simpler alternatives.
- Perform an ablation on each architecture separating input filtering from Lipschitz regularization to clarify their individual and combined contributions.
- Report error bars (mean ± std) over multiple noise input realizations for key quantitative claims.
- Test whether the proposed methods also improve already well-performing architectures (e.g., A8_256 with bilinear upsampling) to fully demonstrate architecture-agnostic benefit.
- Include a brief analysis of total training time overhead for each method.

## Removed Points

These points were flagged by reviewers but are removed because they are either inaccurate, nitpicky, or scope-creep:

- **"No results for higher acceleration factors (8×, 10×)"** – Scope creep; the paper focuses on 4× acceleration and the methods are evaluated consistently.
- **"Small test set (50 slices)"** – 50 slices per dataset is standard in medical imaging; no evidence of inadequate statistical power.
- **"Ambiguous column ordering in Table 2"** – Formatting nitpick; the table image is standard for the venue.
- **"The paper should test whether ConvDecoder itself could be improved by the same remedies"** – Interesting but not required to validate the paper's claims; the paper focuses on encoder-decoder architectures.
- **"Why Gaussian kernel? What is the theoretical connection?"** – The paper provides a clear analogy to NeRF Fourier features and references prior work; the motivation is sufficient for an empirical paper.
- **"Choice of ℓ∞ norm not justified"** – Excessive technical nitpick; Lipschitz constant computation via operator norms is standard.
- **"λ sensitivity plot missing from main text"** – The supplement is referenced; including it would be nice but is not a core flaw.
- Generic strengths from Strength Finder that overlap with other strengths (e.g., "Insight linking frequency bias to architecture components is empirically grounded" merges with Strength #1).
- Strength claiming "Robust evaluation across datasets and against strong baselines" – the "strong baselines" characterization conflicts with the missing baselines weakness; the cross-dataset evaluation is real but already covered elsewhere.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the connection between the paper's approach and the known failure of high-frequency positional encodings in few-shot NeRF is worth noting but is already acknowledged in the paper (Section 5, referencing Yang et al., 2023).

## Suggestions

1. **Add early stopping and self-validation as baselines** in Tables 4–5. This is the single most impactful addition: it directly addresses whether the proposed methods offer a genuine advantage over simple, existing alternatives or are merely another way to achieve similar ends.

2. **Report variance** (mean ± std over multiple runs with different noise input realizations) for at least the key tables (4–6). Even 3 runs per condition would dramatically increase confidence.

3. **Justify the nearest neighbor choice in main experiments** or run a comparison with bilinear upsampling to show the proposed methods' benefits are not artifacts of a weakened baseline.

4. **Tone down the "first time" claim** in the abstract and introduction to avoid provably false statements. Replace with phrasing that emphasizes the novelty of the frequency-domain analysis and the specific proposed remedies.

5. **Clarify "average median values"** in Figure 5 caption and provide per-architecture ablation separating input filtering from Lipschitz regularization.

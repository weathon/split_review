Let me now carefully verify each of the harsh critic's claims against the actual paper text.

**Claim 1: "Biased gradient" analysis is mischaracterized**

The paper states (line 165): "It is evident that $i$ would always receive a weight $(i-d)$ to the gradient that is proportional to its distance to $d$. Therefore, it is difficult for the network to reach the global minimum since the gradient is biased."

And later (lines 211-224): The paper explains that at the initial stage, the varying shape of softmax output results in unstable gradient. At the later stage, even though distant indices get balanced by small probabilities, the nearby indices with similar probabilities get different gradient magnitudes due to the $(i-d)$ factor.

The harsh critic claims this is not "bias" in a meaningful statistical sense and that the $(i-d)$ factor is analogous to softmax gradients in classification. However, the paper's actual argument is more nuanced than the critic suggests: the claim is that this gradient structure makes optimization harder because nearby indices (with similar probabilities) get different gradient magnitudes based on their position relative to $d$. This is a legitimate concern about optimization difficulty, even if calling it "bias" is imprecise. The critic is partially right that the term "biased" is loaded, but the paper's empirical evidence (e.g., the gradient similarity matrices in Fig. 2) supports the claim that this gradient structure creates optimization challenges.

**Claim 2: "Impossible to converge" claim about trilinear interpolation**

Line 184: "However, whether the Laplacian or Gaussian distribution are taken for the supervision, their distribution is convex. As a result, it is impossible for the network to converge."

The paper uses the word "impossible" quite strongly. The critic correctly points out that baselines using trilinear interpolation do converge. However, the paper's argument is specifically about distribution-based supervision with trilinear interpolation — the claim is that when you try to fit a convex distribution (Gaussian/Laplacian) using trilinear-interpolated probability values (which become linear/between the grid points), the target distribution shape cannot be matched. This is about the *distribution fitting* being impossible, not about the overall network failing to train at all. So the paper's wording is too strong but the underlying point has merit — trilinear interpolation creates intermediate values that distort the convex target shape. Still, the word "impossible" is an overstatement since networks using CE + trilinear interpolation do get trained in prior work and produce usable results.

**Claim 3: Marginal improvements and no variance**

Line 353: "And we also have obtained an improvement of 0.01% on IGEV-stereo." The paper itself acknowledges the tiny improvement on IGEV. No variance or statistical significance tests are reported. This is a valid concern.

**Claim 4: Equation 8 contains an exponent error**

Line 248: $q(x)=\frac{e^{-\frac{(x-\mu)^2}{2\sigma^{2}}}}{\sum_{x} e^{-\frac{(x-\mu)^2x-\mu}{2\sigma^{2}}}}$

The denominator clearly has $(x-\mu)^2x-\mu$ instead of $(x-\mu)^2$. This is an actual typographical error in the equation. While the intended formula is obviously the discrete Gaussian normalization, the formula as written is incorrect. This is a legitimate concern, though it's likely a typo rather than reflecting a different implementation.

**Claim 5: Conflated contributions**

The paper bundles four changes and the KITTI ablations don't isolate them individually on the real dataset. This is valid but the Sceneflow ablations do test each component individually. The question is whether they transfer to KITTI.

**Claim 6: Incomplete sentence**

Line 110: "Moreover, the " — this is indeed a cut-off sentence. BUT — per my instructions, I should REMOVE formatting/writing artifact issues. This might be a genuine editing artifact or a parser artifact. Per rules, I'll treat this as a trivial formatting issue.

**Claim about duplicate gradient derivations**

Lines 154-164 (Eq. 6) and lines 200-210 (Eq. 11) appear nearly identical. This is valid — the paper does derive the same thing twice, which suggests incomplete editing.

Now let me synthesize the review.

The paper's core contributions are:
1. Sampling-Gaussian: using a Gaussian as target distribution (with extended range) for soft-argmax supervision
2. Bilinear instead of trilinear interpolation for upsampling cost volume
3. L1 + cosine similarity combined loss
4. Extended disparity range to address endpoint bias

Key verified issues:
- Eq. 8 has a typo in the normalization denominator (real but likely a typo in the writing, not in the implementation)
- The "biased gradient" terminology is imprecise — it's really about gradient structure making optimization harder, not statistical bias
- "Impossible to converge" is too strong a claim — should say "difficult to fit the target distribution"
- Improvements on strong baselines (IGEV) are marginal (0.01%)
- No variance/statistical significance reported
- The same gradient derivation appears twice
- The cut-off sentence "Moreover, the" at line 110

Let me now compose the final review.</think>Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

The paper proposes Sampling-Gaussian, a supervision method for soft-argmax-based stereo matching. Instead of training with regression loss (smooth-L1) on the soft-argmax output, they construct a discrete Gaussian target distribution over disparity indices and train the network to match it using a combined L1+cosine loss. They identify two practical issues with prior distribution-based methods—endpoint truncation biasing the distribution mean, and trilinear interpolation distorting convex target distributions—and propose fixes: extending the disparity range and switching to bilinear interpolation for upsampling the cost volume. The method is applied to five baselines (PSMNet, GwcNet, MSN3D, MSN2D, IGEV-Stereo) on Sceneflow and KITTI.

## Strengths

- **Consistent improvements across diverse baselines**: The method improves all five baselines on both Sceneflow and KITTI (Tables 1–3), including both 3D- and 2D-convolution architectures and an iterative refinement method (IGEV). This breadth of applicability is a genuine strength.
- **Preservation of inference efficiency**: Unlike prior distribution-based methods (e.g., PDS) that require non-parallelizable Top-k post-processing at inference time, Sampling-Gaussian computes the disparity directly via soft-argmax (Section 4.4, Eq. 14), maintaining the original inference pipeline unchanged.
- **Endpoint range extension is a genuine and clearly motivated insight**: The observation in Section 3.2a that truncating a symmetric distribution at $d=0$ biases its expectation is correct and the proposed fix (extending the range by $d_{ext}$) is simple and well-supported empirically (Table on range ablation).
- **Practical guidance**: The $\sigma$ ablation (Table 1) and loss combination ablation (Table on losses/λ) provide useful hyperparameter guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

- **Overstated theoretical claims weaken the paper's motivation**: The paper claims that the soft-argmax gradient is "biased" (Section 3.1, line 165: "it is difficult for the network to reach the global minimum since the gradient is biased") and that trilinear interpolation makes it "impossible for the network to converge" (Section 3.2b, line 184). The $(i-d)$ factor in the gradient is a standard property of differentiable regression (analogous to softmax gradient structure) — it is not "bias" in a statistical sense, and calling it such mischaracterizes the issue. More problematically, the claim that convergence is "impossible" with trilinear interpolation is directly contradicted by the fact that every baseline compared against (PSMNet, GwcNet, etc.) uses trilinear interpolation and converges successfully. The actual issue is that trilinear interpolation makes it harder to fit *convex-shaped target distributions*, a narrower and more defensible claim. The paper would be significantly stronger if these claims were scoped to what the evidence supports.

- **Marginal improvements on strongest baselines with no variance reporting**: On KITTI 2015, the improvement over IGEV-Stereo is 0.01 percentage points (acknowledged in the paper, line 353). No standard deviations, confidence intervals, or multi-seed experiments are reported for any result. Without variance information, improvements of this magnitude cannot be distinguished from noise, particularly on KITTI which has sparse ground truth and relatively few test images.

- **Equation 8 (the core definition of Sampling-Gaussian) contains a mathematical error in the normalization**: The denominator reads $e^{-\frac{(x-\mu)^2 x-\mu}{2\sigma^2}}$ where it should read $e^{-\frac{(x-\mu)^2}{2\sigma^2}}$. The extra $x-\mu$ factor in the exponent produces an incorrect normalization constant that differs from the discrete Gaussian distribution. While this is almost certainly a typo rather than reflecting the actual implementation, it appears in the paper's central equation and undermines confidence in the theoretical development.

- **Conflated contributions without KITTI-level ablation**: The final method bundles four distinct changes (Gaussian target, L1+cosine loss, bilinear interpolation, extended range). The ablation in Table 2 is conducted only on Sceneflow, not on KITTI where the key comparisons against prior art are made. Since the KITTI results apply all changes simultaneously, it is unclear which components drive the improvements on the more important benchmark.

### Minor

- **Redundant gradient derivation**: Equations 6 (Section 3.1) and 11 (Section 3.3) derive the same soft-argmax gradient, suggesting the sections were written independently and not unified. This is a presentation issue but not fatal.

- **The L1+cosine loss combination lacks principled justification**: The paper interprets probability distributions as vectors and combines L1 with cosine similarity (Eq. 12–13), but probability vectors summed to 1 already have constrained norms. The choice of λ=0.5 is not theoretically motivated, and the paper does not compare against standard distribution distances (KL divergence, Wasserstein) that have clearer information-theoretic interpretations. The contour plot in Fig. 4 provides geometric intuition, but the claim that this is a "vector space interpretation" adding insight beyond "compare distributions element-wise" is not strongly justified.

- **Qualitative claims are not backed by quantitative evaluation**: The paper claims (Section 5.4) that Sampling-Gaussian "effectively improves the accuracy of the model to predict small objects and details" and addresses "minority disparity," but no evaluation on thin structures, small objects, or boundary metrics is provided to quantify this.

### Trivial
None.

## Nice-to-Haves

- Multi-seed experiments with variance reporting on KITTI, which would substantially increase confidence in the marginal improvements.
- Ablation on KITTI (not just Sceneflow) isolating each component, particularly the bilinear vs. trilinear interpolation change, which alters cost volume resolution.
- Comparison against KL divergence or Wasserstein loss as alternative distribution-matching objectives, to justify the L1+cosine choice beyond the contour plot visualization.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Incomplete sentence at line 110"**: The text "Moreover, the" trailing off is an editing artifact. Per rules, formatting/presentation artifacts are removed from the main review.

- **"Related works taxonomy reads as padding"**: This is a style/presentation nitpick. Removed per rules.

- **"Demand for Middlebury or CREStereoDataset"**: Scope creep — the paper evaluates on two standard benchmarks (Sceneflow + KITTI). Requesting additional datasets is a nice-to-have, not a core flaw. Moved to Nice-to-Haves.

- **"Comparison with methods using different base architectures is confounded"**: This is the standard practice in stereo matching; distribution-based method comparisons naturally involve different base architectures. The paper compares against distribution-based priors (PDS, AcfNet, etc.) and shows the proposed method improves each baseline. Not a genuine weakness.

- **"Reproducibility concerns about equation error"**: The typo in Eq. 8 is noted as a Major issue above, but claims that it makes the method unreproducible are overblown — the intended formula is obvious from context and the code is stated to be available online.

- **"Demand for training dynamics/loss curves"**: Nice-to-have rather than a core weakness. Moved.

- **"Cross-domain improvements are marginal"**: The 0.23% improvement claimed by the harsh critic is actually a meaningful relative improvement (from 33.89% → 30.83%), and the cross-domain experiment supports generalization. Removed.

## Novel Insights

The most interesting observation that emerges from this review is that the paper's actual contributions may be more practical than theoretical. The endpoint range extension is a clean, well-motivated fix for a real distribution truncation problem. The switch from trilinear to bilinear interpolation is likely responsible for a significant portion of the improvements (since it preserves the convex shape of the target distribution). But the paper over-reaches in its theoretical framing — the "biased gradient" narrative and the "impossible to converge" claim obscure what is genuinely valuable about the method. The Sampling-Gaussian approach is best understood as a set of practical engineering improvements (Gaussian target distribution, range extension, bilinear upsampling, L1+cosine loss) that collectively improve soft-argmax stereo matching, rather than as a theoretically motivated correction to fundamental flaws in the soft-argmax gradient.

## Suggestions

1. **Rewrite the theoretical motivation**: Replace "biased gradient" with "gradient structure that makes optimization harder" and replace "impossible to converge" with "difficult to match the target convex distribution shape." The actual argument (that $(i-d)$ weighting creates oscillation near the optimum in late training) is reasonable — just tone down the claims to match the evidence.

2. **Fix Equation 8**: Correct the denominator to $e^{-\frac{(x-\mu)^2}{2\sigma^2}}$.

3. **Report variance**: Run 3–5 seeds on KITTI and report mean ± std. This is especially important given the 0.01% improvement on IGEV-Stereo.

4. **Add KITTI ablations**: At minimum, isolate the bilinear interpolation and extended range components on KITTI to show which changes matter most on the real-world benchmark.

5. **Scope the claims honestly**: Rather than "achieved state-of-the-art results" based on 0.01% improvement, acknowledge that improvements on already-strong baselines are marginal and focus on the consistency and generality of gains across baselines.

---

## Evaluation

**Originality**: The paper combines several ideas (Gaussian target, range extension, bilinear upsampling, L1+cosine loss) that are individually incremental, but the overall packaging as a plug-in for soft-argmax methods is novel enough. The theoretical motivation, however, is both the paper's main selling point and its weakest aspect.

**Importance of research question**: Distribution-based supervision for stereo matching is a relevant and somewhat underexplored topic. The practical issues identified (range truncation, interpolation distortion) are meaningful.

**Claims well supported**: Partially. The empirical results show consistent improvements, but the theoretical claims are overstated, the core equation has a typo, and marginal improvements lack variance reporting.

**Soundness of experiments**: Adequate on Sceneflow ablations, insufficient on KITTI (no ablations, no variance). The breadth of baselines is a strength.

**Clarity**: The paper has organizational issues (repeated derivations, repeated contribution listings) but is generally understandable.

**Value to community**: Moderate. The method is easy to implement, works across architectures, and maintains inference efficiency. However, the marginal improvements on strong baselines and the overclaimed theory limit the impact.

## Score and Decision

The paper presents a reasonable set of practical improvements for soft-argmax stereo matching, with consistent (if modest) gains across five baselines. However, the theoretical motivation relies on overstated claims ("biased gradient," "impossible to converge"), the central equation has a mathematical error, and the marginal improvements on the strongest baselines lack variance reporting. These are addressable but significant issues. The method itself is sound and useful, but the paper's narrative overclaims relative to the evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
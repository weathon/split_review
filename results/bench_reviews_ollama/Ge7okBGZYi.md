Now I have a thorough understanding of the paper. Let me evaluate the harsh critic's claims carefully.

**Claim 1: The paper conflates "learnable parameters" with "grid structure."** The critic argues that the K_MPE term appears because grid values are learnable, not because of grid structure. This is technically correct — the K_MPE term comes from gradients through learnable parameters, and any learnable encoding would produce an analogous term. However, the paper's actual claim is more nuanced than the critic suggests. The paper is comparing MPE (which has learnable parameters in a grid) vs FFE (which has no learnable parameters). The conclusion that they have "fundamentally different" mechanisms is accurate *as stated* — MPE uses learnable parameters, FFE does not. The question is whether this is a "mechanistic" difference about grids vs embeddings, or simply a difference about having learnable parameters vs not. The paper's wording ("the structure of their grid and not their embedding") could be clearer, but the core finding — that the learnable grid component dominates over the embedding-space component for MPE — is valid and useful.

**Claim 2: Uncontrolled parameter count.** This is a legitimate concern. The MPE adds many learnable parameters; the FFE adds none. The performance gap could be partially attributed to parameter count rather than grid structure specifically. However, this is a comparison between the two specific encodings as used in practice, not a controlled ablation. The paper acknowledges the memory cost ("at the cost of a larger memory footprint", line 37). Still, the lack of a parameter-controlled comparison is a weakness, though not fatal — the paper's claim is about how these specific encodings work through the NTK, not that grid structure is optimal per parameter.

**Claim 3: Theorem 1 provides no grid-specific insight.** The theorem is indeed a direct application of Weyl's inequality to the sum of PSD matrices, which would hold for any addition of learnable parameters. The paper's claim of "the first theoretical justification for why MPEs are able to learn finer detail" is partially overclaimed — the theorem shows that adding PSD terms raises eigenvalues, which is quite general. However, the derivation leading up to it (showing that K+ arises from the grid parameters and decomposing the MPE NTK) is specific to the MPE architecture and is a genuine contribution.

**Claim about aliasing:** The abstract says "MPEs, which use a learned grid structure, have no such limitation" regarding aliasing. The critic notes that a finite grid with bilinear interpolation will alias too. This is a valid substantive criticism — the claim is overly strong and not defended in the paper.

**Claim about quantitative 3D results:** The paper shows only spectral plots for the 3D experiments (Figure 5b), no PSNR/MS-SSIM numbers. This is valid — the paper uses two domains but only reports quantitative metrics in one.

Now let me construct the final review.</think>Now I have thoroughly read the paper. Let me synthesize the final review.

## Summary

The paper derives the neural tangent kernel (NTK) for multigrid parametric encodings (MPE) and decomposes it into a base MLP component evaluated in the embedding space and a learnable-grid component (K_MPE). Using Weyl's inequality, it proves a lower bound on MPE eigenvalues (Theorem 1), and through an ablation that removes K_MPE from the NTK, argues that MPE performance comes from its learnable grid rather than its embedding space—contrasted with Fourier feature encodings (FFE), which operate only through their embedding. Empirical validation spans 2D image regression (100 ImageNet synonym sets) and 3D implicit surface regression (3 Stanford meshes), showing 8-order-of-magnitude eigenvalue increases and 12–15 dB PSNR improvements.

## Strengths

- **Clean NTK decomposition for MPE (Equations 10–13).** The derivation clearly separates the MPE NTK into K_MLP (the base MLP kernel evaluated in the embedding space) and K_MPE (the contribution from learnable grid parameters). This decomposition is specific to the MPE architecture and enables both the theoretical bound and the empirical ablation. It is a useful formal contribution regardless of how one interprets the mechanism.

- **Empirical ablation isolating K_MPE's contribution (Figure 2).** Computing the NTK spectrum with and without the K_MPE term during training (midpoint and end) shows that removing this term collapses the spectrum nearly to baseline. This is meaningful evidence that the learnable grid parameters are the dominant source of MPE's spectral improvement, not the dimensionality or structure of the embedding space alone.

- **Broad empirical validation across images and domains.** Scaling to 100 ImageNet synonym sets (Figure 5a) and cross-domain consistency with 3D surface regression (Figure 5b) provide evidence that the spectral ordering (MPE > FFE > baseline) is robust, not an artifact of a single example.

- **Identification of FFE spectral saturation (Figure 4).** The observation that increasing FFE frequency yields diminishing spectral returns—while MPE continues to improve with finer grids—provides a practically useful characterization of FFE limitations, even without a full theoretical explanation.

## Weaknesses

### Fatal
None.

### Major

- **The "fundamentally different mechanism" claim is overstated relative to the evidence.** The paper concludes that MPE improves performance through its "grid structure" in a way "fundamentally different" from FFE (abstract, line 17–18; contributions, line 41; conclusion, line 207). What the evidence actually shows is that the NTK contribution from the *learnable parameters* (K_MPE) dominates over the K_MLP term for MPE, while FFE has no learnable parameters and therefore no analogous term. This difference stems from a *design choice* (whether the encoding includes learnable parameters), not necessarily from a grid-vs-Fourier structural distinction. Any encoding with learnable parameters would produce a structurally similar NTK decomposition. The paper does not compare MPE against a parameter-controlled alternative (e.g., FFE augmented with learnable frequencies or an auxiliary parametric layer), so the 8-order-of-magnitude eigenvalue gap and 12 dB PSNR improvement cannot be attributed specifically to grid structure rather than to the raw addition of learnable parameters. The NTK decomposition itself remains valid and useful; what is overclaimed is the *interpretive* conclusion about the mechanism being grid-specific.

- **Theorem 1 is a direct application of Weyl's inequality and provides no grid-specific insight.** The theorem states that eigenvalues of K_MLP+MPE are bounded below by eigenvalues of K_MLP plus the smallest eigenvalue of K⁺. This follows immediately from the PSD structure of the decomposed NTK and Weyl's inequality—it would hold identically for *any* addition of learnable parameters in *any* configuration, with no dependence on grid resolution, interpolation scheme, or multiresolution structure. The paper's presentation of this as "the first theoretical justification for why MPEs are able to learn finer detail and discontinuities" (contributions, line 41) substantially overstates what the theorem establishes. A theorem whose bound actually depended on grid properties (resolution, interpolation kernel, number of levels) would genuinely explain *why* MPE grids are effective.

- **Unsupported claim that MPEs have "no such limitation" regarding aliasing (abstract, line 12–13).** The abstract states FFEs are "susceptible to aliasing if pushed too far, while MPEs, which use a learned grid structure, have no such limitation." A grid of finite resolution with bilinear interpolation will alias content below the grid Nyquist frequency just as a band-limited Fourier basis cannot represent frequencies exceeding its maximum. The paper provides no analysis or evidence for this claim anywhere in the text. This should be removed or substantially qualified.

### Minor

- **No quantitative PSNR/MS-SSIM metrics reported for the 3D implicit surface regression domain (Section 5).** The 2D image regression section includes quantitative metrics (Tables 2–3), but the 3D section (Figure 5b) reports only eigenvalue spectra without corresponding reconstruction quality numbers. Given that 3D is one of two empirical domains, quantitative performance metrics should be reported.

- **The "MPE (No Grid)" ablation in Figure 2 computes the NTK of a network that has grid parameters in the forward pass but omits their gradient contribution.** The caption describes this as "purely for theoretical analysis," which is fair, but it means the ablation tests whether the *gradients through learnable parameters* contribute to the NTK—not whether "grid structure" specifically matters. The labeling ("No Grid") could mislead readers into thinking this tests grid structure rather than learnability.

### Trivial
None.

## Nice-to-Haves

- A parameter-controlled comparison (MPE vs. FFE+learnable parameters of comparable count) would significantly strengthen the attribution of performance to grid structure rather than parameter count alone.
- Extending Theorem 1 with a bound that depends on concrete grid properties (resolution, interpolation kernel, number of levels) would provide genuinely grid-specific theoretical insight.
- Per-parameter-count learning curves (PSNR vs. number of learnable parameters or wall-clock time) would clarify whether MPE's advantage is efficiency per parameter or simply a capacity effect.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The scaling analysis uses only one image" (Harsh Critic).** The paper explicitly addresses this by extending to 100 ImageNet synonym sets in a second evaluation setting. The single-image analysis is the controlled ablation; the large-scale validation is the generalization check. Both settings serve different purposes.

- **"Optuna-tuned hyperparameters are not reported, nor is wall-clock time" (Harsh Critic).** While reporting tuned hyperparameters would be helpful, this falls into the category of minor implementation details. The Optuna tuning ensures fair comparisons in practice. Missing wall-clock comparisons are a good suggestion but not a substantive weakness.

- **"The abstract's aliasing claim should be removed" (Harsh Critic).** This is kept as a valid Major weakness above—the claim is unsupported. The critic's suggestion to remove it is too strong; the proper action is to qualify it, not eliminate the discussion.

- **"The FFE vs. MPE comparison is unfair because MPE has more parameters" (Harsh Critic, stated as "asymmetric comparison favoring baseline").** This is a substantive point and is kept above as a Major weakness (overclaimed attribution), but the specific framing that the comparison is "unfair" is incorrect—per the rules, if the asymmetry favors the baseline (FFE), it makes the MPE's advantage a *stronger* point. The real issue is the *interpretation* of why MPE wins, not the fairness of the comparison.

- **Strength Finder's claim that "Figure 2 conclusively isolates the grid as the source" is overclaimed.** This conflicts with the verified weakness that the ablation isolates *learnable parameters*, not grid structure. Moved to Removed Points.

- **Strength Finder's claim that Theorem 1 provides "the first theoretical justification for MPE's superior ability to learn fine detail."** This overstates what Weyl's inequality establishes (see Major weakness above). The derivation is useful; the claim is not. Conflicts with verified weakness, so moved here.

## Novel Insights

The decomposition of the MPE NTK into K_MLP and K_MPE terms is genuinely useful and the observation that the learnable-parameter contribution dominates the embedding-space contribution is a meaningful empirical finding. However, the key insight the paper misses is that this finding speaks most directly to the distinction between *encodings with learnable parameters* vs. *encodings without*, rather than to a grid-vs-Fourier distinction per se. If the authors recast their contribution as demonstrating that adding learnable parameters to an encoding fundamentally changes how the NTK (and therefore training dynamics) operates—compared to fixed encodings like FFE that modify only the kernel entries but not its rank—the theoretical contribution would be better supported. The current framing inadvertently claims more specificity (grid structure) than the evidence warrants, while potentially undervaluing the more general and potentially more impactful observation about learnable vs. fixed encodings.

## Suggestions

- Rewrite the central claim to distinguish between "learnable-parameter-driven improvement" and "grid-structure-driven improvement," acknowledging that the current evidence supports the former more strongly than the latter.
- Remove or substantially qualify the aliasing claim in the abstract (line 12–13).
- Add quantitative PSNR/MS-SSIM results for the 3D experiments.
- If possible, add one experiment comparing MPE against an FFE with a comparable number of learnable parameters (e.g., learnable affine layer, learnable frequencies) to test whether grid structure provides benefits beyond parameter count.
- Acknowledge in the text that Theorem 1 is a consequence of the PSD decomposition and Weyl's inequality, and discuss what a grid-structure-dependent bound would look like as future work.

## Score and Decision

The paper makes a genuine contribution in deriving and decomposing the MPE NTK, and the empirical finding that the learnable grid dominates the embedding-space contribution is useful. However, the paper's central interpretive claim—that MPE's advantage comes from "grid structure" in a "fundamentally different" mechanism—is not well-supported. The theorem is a generic PSD+Weyl result, not grid-specific; the aliasing claim is unsupported; and no parameter-controlled comparison exists. These are significant overclaims that weaken confidence in the paper's conclusions. The NTK derivation and decomposition remain valuable, but the interpretive framework needs substantial revision.

**Originality:** Moderate—first NTK derivation for MPE, but the theoretical result is a straightforward application of Weyl's inequality. **Importance:** Moderate—understanding encoding mechanisms is important, but the specific claims are overclaimed. **Claim support:** Weak—the core mechanism claim is not well-isolated from confounds. **Experiments:** Adequate breadth but missing parameter controls and 3D quantitative metrics. **Clarity:** Good—the derivation is clearly presented. **Community value:** Moderate if claims are properly qualified.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
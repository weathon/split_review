## Summary

ZZEdit proposes a new zero-shot image editing paradigm that replaces the standard practice of inverting an input image all the way to near-Gaussian noise with (1) selecting an intermediate inversion latent whose UNet response to the target prompt first exceeds its response to the source prompt, and (2) a "ZigZag" process that alternates single-step denoising and inversion to gently guide this pivot toward the target while preserving background fidelity. The method is designed as a plug-in that can be applied to existing inversion-based editing methods (P2P, PnP), and experiments show consistent improvements across multiple inversion settings.

## Strengths

- **Genuinely novel paradigm with clean mathematical motivation.** The ZigZag derivation (Eq. 8, lines 127–130) formally shows that alternating inversion and denoising produces a latent that moves provably toward the target direction by a positive amount per step under the standard noise schedule. This is a principled contribution that goes beyond heuristic modifications of the inversion trajectory.

- **Well-designed ablation isolating the two components.** Fig. 4 and Table 1 separately evaluate (a) the choice of pivot point without ZigZag, (b) the same pivots with ZigZag, and (c) random pivot selection with ZigZag. This convincingly shows that both the pivot selection criterion and the ZigZag process are individually necessary for the reported gains.

- **Consistent improvements across multiple inversion settings.** Table 2 shows that applying ZZEdit to P2P and PnP under DDIM, NTI, PTI, and PnP-inversion (Ju et al., 2024) improves CLIP similarity in nearly every case while maintaining competitive background metrics. The improvement over DDIM-inversion baselines is particularly clear.

- **Empirically demonstrated failure of the standard "invert-to-Gaussian" assumption.** The pilot experiment (Sec. 4.1, Fig. 2) systematically measures guidance degree at different trajectory points and shows that the maximum is not necessarily at step T. This observation, while intuitive post-hoc, is cleanly demonstrated and directly motivates the approach.

## Weaknesses

### Major

- **"State-of-the-art" claim is unsupported by the comparison set.** The paper claims "state-of-the-art editing performance" (line 18) and places its qualitative comparison against P2P (2022), PnP (2023), Pix2Pix-Zero (2023), Instructpix2pix (2023), and MasaCtrl (2023). The quantitative comparison in Table 2 includes PnP inversion (Ju et al., 2024) as a 2024 baseline, but the paper cites Garibi et al. (2024) in its related work (line 29) — a method directly addressing inversion trajectory quality — without any quantitative or qualitative comparison against it. Since ZZEdit is itself an inversion-trajectory modification method, the absence of contemporaneous inversion-improving methods (e.g., ReNoise) from the evaluation pool undermines the "state-of-the-art" claim. The paper's core contribution — showing that ZZEdit improves the methods it builds on — is well-supported, but the broader claim is overreaching.

- **No measures of variance reported for any quantitative result.** All metrics in Tables 1 and 2 are reported as point estimates without standard deviations or any indication of variability across the 100 images in PIE-Bench. Several reported improvements are small (e.g., CLIP-mask of 0.282 vs. 0.278 for P2P+NTI+ZZEdit vs. P2P+NTI in Table 2). Without error bars, the reader cannot assess whether these differences are meaningful or within the noise of the metric. This is a standard expectation for top-venue empirical papers.

### Minor

- **The pilot experiment motivates the approach but does not validate the specific pivot selection criterion.** The pilot (Sec. 4.1) measures guidance degree as $\|\tilde{z}_t - \hat{z}_t\|$ on the reconstruction trajectory, while the pivot criterion (Sec. 4.3) selects the first step where $\|\epsilon^{tgt} - \epsilon^\emptyset\| > \|\epsilon^{src} - \epsilon^\emptyset\|$ on the inversion trajectory — different quantities in different spaces. The paper invokes the pilot as motivation but never directly shows that the pivot selected by the criterion corresponds to the high-guidance region identified in the pilot experiment. A simple overlay plot comparing the two measures across the trajectory would close this gap. The paper's empirical validation (ablation showing the criterion outperforms random pivot selection) partially mitigates this, but the conceptual link remains unverified.

- **Hyperparameter $a$ is treated as a fixed choice without task-adaptive guidance.** The ablation (Table 1, Fig. 5) tests $a \in \{0, 0.2, 0.6, 1\}$ and the main results use $a=1$ uniformly. Table 1 shows that $a=1$ yields the best CLIP scores but degrades structure preservation relative to $a=0$ or $a=0.2$. The paper's stated intuition — that "different editing examples need to corrupt the input image to different degrees for subtle editing" (line 12) — implies that $a$ should vary per edit, yet no adaptive scheme or per-type analysis is provided. This does not invalidate the method but limits its practical utility.

- **GPT-4V evaluation is mentioned but not described.** Line 213 states "We also use GPT-4V(ision) system (OpenAI, 2023) to evaluate Fig." with no details on the prompt, aggregation method, or results. This is too vague to be reproducible or interpretable.

### Trivial

- The pivot search granularity (checking only 7 discrete points in $[0.4T, 0.5T, ..., T]$) means the distribution in Fig. 6 is necessarily discrete and the pivot is identified only within ±5 steps of the optimal. The paper acknowledges this for computational reasons, but the artifact of the discrete distribution should be discussed.

## Nice-to-Haves

- A per-edit-type breakdown of pivot distribution (attribute vs. object vs. style vs. background) would directly test whether the method adapts meaningfully to edit difficulty.
- An ablation fixing the ZigZag process and varying only the pivot selection method (e.g., proposed criterion vs. maximum-guidance from pilot vs. latest-step) would isolate whether the specific criterion matters beyond picking any reasonable intermediate point.
- Comparison against ReNoise (Garibi et al., 2024), including whether ZZEdit can be applied on top of ReNoise-inverted latents, would substantially strengthen the evaluation.

## Removed Points

These points were raised in the inputs but are removed or downgraded after verification against the paper:

1. *"Compute comparison is misleading — ZZEdit costs substantially more."* The paper's claim (line 198) that when $a=1$, ZZEdit "consumes the same UNet operations as the typical 'inversion-then-editing' pipeline" refers to the main pipeline (2T UNet calls in both cases), which is mathematically correct. The pivot search overhead is acknowledged in the paper ("to save time and computation, when looking for the editing pivot, we can only search from [0.4T, 0.5T, ..., 0.9T, T]"). The marginal cost is ~14 extra UNet calls (2 per checkpoint × 7 checkpoints, since the source-conditioned call is already computed during inversion), which is modest. The harsh critic's count of 21 extra calls assumes all 3 predictions per checkpoint are marginal, which is incorrect. The core point (some overhead exists) is true but minor; it does not warrant a "misleading" characterization. **Removed as overstated.**

2. *"No comparison with training-based methods."* The paper explicitly scopes itself to zero-shot editing and situates itself within that literature (lines 10, 27). Criticizing the absence of fine-tuning methods (Imagic, DreamBooth) is scope creep. **Removed.**

3. *"Missing limitations section."* A valid suggestion but not a weakness of the paper's technical contribution. Consensus standard, not an ICLR requirement. **Removed.**

4. Several of the harsh critic's section-by-section notes (notation inconsistency in Eq. 5, parser-garbled algorithm description, suboptimal subscript notation) are formatting artifacts or presentation-level issues that do not affect the technical contribution. **Removed.**

5. Strength Finder's generic praise ("this paper addressed an important problem," "this paper targeted an interesting question") is too generic to retain. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The key insight — that intermediate inversion latents make better editing pivots than near-Gaussian noise, coupled with a ZigZag process for gradual guidance — is already well-articulated in the paper.

## Suggestions

1. **Expand the baseline set** to include ReNoise (Garibi et al., 2024) and any other contemporaneous trajectory-improvement methods. If the claim is state-of-the-art, the evidence must support it against the relevant comparison set.
2. **Report standard deviations** (or bootstrapped confidence intervals) for all metrics across the 100-image PIE-Bench dataset. Without variance information, small improvements are uninterpretable.
3. **Validate the pivot criterion directly**: plot the criterion value ($\|\epsilon^{tgt} - \epsilon^\emptyset\| - \|\epsilon^{src} - \epsilon^\emptyset\|$) alongside the guidance degree ($\|\tilde{z}_t - \hat{z}_t\|$) across the trajectory to show they correspond.
4. **Describe the GPT-4V evaluation protocol**, or remove it as an unreproducible claim.

## Score and Decision

The paper presents a genuinely novel and well-motivated paradigm with consistent empirical improvements over its chosen baselines. The ZigZag derivation is technically clean, and the ablation study convincingly separates the contributions of the pivot selection and the ZigZag process. The main weaknesses are: (1) the "state-of-the-art" claim overreaches the comparison set, (2) no measures of variance on quantitative results, and (3) the conceptual link between the pilot experiment and the pivot criterion is asserted but not directly validated. None of these are fatal — the method's contribution stands independently — but they prevent the paper from being as strong as it could be. With expanded baselines and statistical rigor, this would be a strong paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>
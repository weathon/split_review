## Summary

The paper proposes TD-Paint, which accelerates diffusion-based inpainting by replacing the scalar timestep $t$ with a pixel-wise time map: known pixels receive $t=0$ (clean) while unknown pixels receive the current step's $t$ (noisy). This keeps the conditioning region clean throughout generation, eliminating RePaint's costly resampling mechanism. The method is evaluated on CelebA-HQ, ImageNet, and Places2 across six mask types, demonstrating consistent quality improvements and a >6× speedup over RePaint.

## Strengths

1. **Novel pixel-wise time conditioning for inpainting.** The core idea — encoding per-pixel noise levels via the diffusion model's own time embedding, producing a spatial tensor $\Gamma \in \mathbb{R}^{d \times h \times w}$ instead of a scalar embedding — is clean, well-motivated, and directly addresses a real limitation of RePaint-style inpainting. This is formalized in Equations (8) and (12–14) with clear mathematical grounding.

2. **>6× inference speedup over diffusion baselines.** The paper reports average sampling time on a V100 (Section 5.4) showing TD-Paint (1000 steps, no resampling) is substantially faster than RePaint-20 (~5000 steps with resampling), MCG, and CoPaint. This directly supports the paper's core claim of faster sampling without architectural complexity.

3. **Consistent quantitative improvements across mask types and datasets.** TD-Paint outperforms RePaint-20 by 20% LPIPS on wide masks and 30% on narrow masks across CelebA-HQ, ImageNet, and Places2, with larger gains on twotime (115%) and altline (69%) settings (Section 5.2). Results are reported on 2,824–5,000 test images per dataset.

4. **Training strategy for learning variable noise levels.** The $\phi_\text{train}$ procedure (Section 4.1) samples random patch sizes (powers of two) and random known/unknown proportions, forcing the model to learn reconstruction from less-noisy to more-noisy regions. This is a non-trivial design choice that supports generalization at test time.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Algorithm 1 has an indexing bug.** On line 203, $x^{\text{unknow}}_{\phi_t} = \sqrt{\bar\alpha_{\phi_t}} x_{t-1} + \sqrt{1-\bar\alpha_{\phi_t}} \epsilon$ references $x_{t-1}$ before it is computed (line 211). On the first loop iteration ($t=T$), $x_{T-1}$ is undefined. The surrounding text (line 169: $x_{\tmap} = x^{\text{unknow}}_t \odot (1-m) + x^{\text{know}}_0 \odot m$) and standard DDPM conventions make clear that $x_t$ (or $x^{\text{unknow}}_t$) is intended, so the method remains reproducible — but the pseudocode should be corrected.

2. **"No architectural modification" claim is imprecise.** The paper states this in the abstract, lines 78, 141, and 240. However, Section 4.2 describes modifying the conditioning injection: instead of embedding scalar $t$ into vector $\gamma \in \mathbb{R}^d$, it produces a spatial tensor $\Gamma \in \mathbb{R}^{d \times h \times w}$ and applies per-pixel scale-shift normalization. While the U-Net backbone (convolutions, attention, skip connections) is indeed unchanged, the conditioning pathway is modified. Describing this as "minimal modification to the conditioning mechanism" would be more accurate.

3. **Training–inference mask mismatch not discussed.** Training uses rectangular patches (Section 4.1), while evaluation includes twotime (every-other pixel) and altline (every-other line) masks that are fundamentally non-rectangular. The paper reports large gains on these masks (115% LPIPS on twotime) without examining whether this reflects robust generalization or whether baselines are suboptimally configured for these mask shapes. A brief discussion would strengthen the paper.

4. **Comparison conflates zero-shot vs. fine-tuned regimes.** RePaint works with any pretrained unconditional model (zero-shot, no training required), while TD-Paint requires fine-tuning. The paper acknowledges this (line 86) but frames the comparison as TD-Paint being categorically superior without explicitly characterizing the practitioner's tradeoff. The results are valid, but the framing should be more measured.

5. **No variance or confidence intervals.** Percentage improvements (20%, 30%, 115%, 69%) are reported without standard deviations, confidence intervals, or significance tests. The unusually large claims (115% on twotime) would benefit from variance reporting to confirm they are not artifacts of particular baseline configurations.

### Trivial
None.

## Nice-to-Haves
- Ablate the training procedure: compare TD-Paint fine-tuned with the proposed patch-based training against a version fine-tuned with standard DDPM training using TD-Paint's inference-time conditioning, to isolate the benefit of the training strategy from the benefit of the noise model.
- Test on held-out irregular (free-form) masks to probe generalization beyond rectangular training masks.
- Compare against RePaint or MCG also fine-tuned on the same data, controlling for training budget, to separate the benefit of the proposed noise modeling from the benefit of fine-tuning itself.

## Removed Points
These points are flagged to be removed, treat them with caution:

- Harsh Critic's claim that Algorithm 1's indexing error is "fatal" and "undermines reproducibility" — while the bug is real, the surrounding text and equations clarify the intent, so the paper remains reproducible. Demoted to Minor.
- Criticism that quantitative results are "embedded in unparseable figures" — this is a parser artifact from PDF extraction; the original submission has properly rendered tables. Removed per Hard Rules.
- Several general-area sweep concerns from the Harsh Critic (speculative baseline misconfiguration, unspecified "confounders") that lack concrete anchors in the paper text. Removed because they are not tied to specific sentences/figures/equations.
- Strength Finder's claimed strength #2 ("No architectural modifications required") — this conflicts with verified Weakness #2 above; per rules, the weakness wins and the strength is dropped.
- Harsh Critic's criticism about missing limitations section — noted as a nice-to-have but not a substantive weakness; removed from the main weakness list.

## Novel Insights
None beyond the paper's own contributions. The reviews surface no genuinely novel perspective beyond the paper's core idea: the insight that the diffusion model's time conditioning can be repurposed as a per-pixel noise-level signal to keep the known region clean is the paper's own contribution, and the reviewer observations broadly confirm the idea is well-motivated and the evidence is solid but not airtight.

## Suggestions
1. **Fix Algorithm 1:** change $x_{t-1}$ to $x_t$ on line 203 to match the textual description in Section 4.1.
2. **Rephrase the architecture claim:** replace "without architectural modifications" with "without modifying the U-Net backbone" or "with minimal modification to the conditioning mechanism."
3. **Add a paragraph** discussing the training-inference mask mismatch and why the method does (or does not) generalize to non-rectangular masks.
4. **Report standard deviations** for the headline LPIPS numbers, especially the large improvements on twotime/altline masks.
5. **Add a limitations paragraph** acknowledging tradeoffs (requires fine-tuning, training on rectangular masks).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
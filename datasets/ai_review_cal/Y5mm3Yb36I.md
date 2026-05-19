- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have a clear picture of the paper. Let me write the consolidated review.

## Summary

This paper proposes a method to quantify the "originality" (or more precisely, "familiarity") of an image to a text-to-image diffusion model by counting the minimum number of tokens needed to reconstruct it via multi-token textual inversion. The authors first conduct controlled synthetic experiments to show that T2I models can generalize beyond memorization. They then extend textual inversion to multiple tokens and show, on both synthetic and real-world data, that the number of tokens required for reconstruction increases from common to rare to unseen content. The work is motivated by copyright law's originality requirement.

## Strengths

- **Multi-token textual inversion as a familiarity measure is a novel and intuitive idea.** The paper builds on existing textual inversion work in an inventive way — using token count not for personalization but as a probe into the model's latent representation of familiarity. This is a creative conceptual contribution (Section 3.1).

- **Synthetic experiments provide clean causal evidence for the token-count/familiarity relationship.** Under controlled conditions with known ground-truth distributions (Common, Rare, Unseen), the paper demonstrates a clear ordinal trend: Common → 1 token, Rare → 2–3 tokens, Unseen → 4–5 tokens (Section 5, lines 127–133). This controlled validation is the paper's strongest evidence.

- **The method requires neither training data access nor the original prompt.** As stated in the Discussion (line 161), the approach operates without access to the training data or a specific prompt, giving it a practical advantage over attribution methods like TRAK that require full training set access. This is a genuine strength for copyright-motivated applications.

## Weaknesses

### Fatal
None.

### Major

- **The "minimum number of tokens" criterion is not defined.** The paper's central quantity — the minimum number of tokens required for reconstruction (lines 131–132) — is never specified. The method generates images at each token count and computes DreamSim scores, but no threshold, plateau condition, or decision rule is stated for when "reconstruction is sufficient." Without this, the measurement is not a well-defined, replicable quantity. Different implicit thresholds would produce different token counts for the same image, undermining the quantitative results (Fig. 5 / the token frequency plot). This gap is structural: the core metric of the paper is underspecified.

- **The real-world evaluation is too thin to support the claims.** The pretrained Stable Diffusion experiments present only qualitative examples (two figures) and DreamSim averages, with no systematic evaluation: no distribution of token counts across a meaningful image corpus, no statistical test of the correlation, no comparison to any baseline (e.g., nearest-neighbor distance in a feature space, reconstruction loss of a fixed-dimensional VAE, or a simple memorization metric). The "human expert" labeling for common vs. original images is mentioned (line 137) but no details are given (number of images, annotation protocol, inter-annotator agreement). The paper claims a correlation between token count and originality in the real-world setting, but the evidence is anecdotal.

- **The confound between familiarity and visual complexity is not addressed.** The core assumption is that token count measures familiarity with the training distribution. But a crowded yet common scene (e.g., a typical city street) might require many tokens due to its visual complexity, while a simple but genuinely novel concept might require few. The synthetic experiments control for this by using simple shapes, but the real-world experiments do not attempt to measure or control for image complexity (number of objects, color/texture entropy, spatial layout, etc.). The paper's Limitations acknowledge that textual inversion "may not capture all aspects of originality in complex images" (line 171), but this does not resolve the confound — it merely states it. The claimed relationship between token count and originality remains confounded with complexity in the real-world setting.

### Minor

- **No comparison to any baseline.** Even a simple baseline — such as using DreamSim reconstruction quality at a fixed token count, or the distance to the nearest concept embedding in the CLIP space — would help contextualize the method's added value beyond existing alternatives. Currently, the paper evaluates its method in isolation.

- **No analysis of variance or statistical significance in the synthetic experiment.** The quantitative synthetic results (lines 131–133) report a clear trend (Common: 1 token, Rare: 2–3, Unseen: 4–5) but do not report error bars or a statistical test across seeds/samples. The reader cannot assess the reliability of the reported token counts.

- **The "+" category of images not reconstructable within 5 tokens is mentioned but not analyzed.** What proportion of images fall here, and what characterizes them — are they simply complex, or genuinely out-of-distribution? This could provide useful signal.

### Trivial
None.

## Nice-to-Haves

- **Define the minimum token count rigorously.** Specify either: (a) a fixed DreamSim threshold below which reconstruction is "successful," or (b) a plateau criterion (e.g., stop adding tokens when the DreamSim improvement over the previous token count is below X%). Validate with sensitivity analysis.
- **Disentangle familiarity from image complexity** in the real-world setting (e.g., by measuring complexity with image entropy or object count and controlling for it in the analysis).
- **Conduct a systematic real-world evaluation** on a larger set of images (e.g., 100–200) with multiple annotators rating familiarity/originality, and report correlation with token count, variance, and statistical significance.
- **Compare against a baseline** such as a fixed-dimensional VAE reconstruction loss, cosine distance to common CLIP concept embeddings, or nearest-neighbor distance in the DreamSim feature space.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Section 2 experiments are "confirmatory" / not novel.* The harsh critic claimed these experiments are "well-established." However, the paper explicitly notes that "the effects of textual conditioning on generalization have yet to be explored" (lines 25–26). Studying how prompting affects generalization in T2I models is a legitimate contribution of the preliminary experiments. This criticism is inaccurate.

- *Overstated contributions (aspirational language).* The harsh critic objected to phrases like "can be harnessed to build further metrics." Such aspirational language in conclusion/discussion sections is standard practice and does not constitute a substantive weakness.

- *Paper does not fully address legal originality.* The paper frames itself as "inspired by legal definitions" (abstract), not as implementing a legal test. The gap between legal originality and measured familiarity is partially acknowledged. This is not a fatal framing error — the paper could be clearer, but the harsh critic overstates this issue. Demoted to Minor (already addressed above in weakened form: the framing is ambitious relative to evidence, but not a fatal mismatch).

- *Missing related works.* I have no external sources to confirm whether relevant works were omitted.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. **Define the minimum-token-count criterion explicitly** in Section 3.1 or Section 5. State the DreamSim threshold (or plateau condition) and include a sensitivity analysis showing that the ordinal trend holds across reasonable threshold choices.
2. **Strengthen the real-world evaluation** by collecting a corpus of images with multiple human raters (labeling common vs. original) and reporting the token-count distribution, correlation coefficient, and statistical significance for at least 50–100 images.
3. **Address the complexity confound** by measuring a basic complexity proxy (e.g., number of detected objects, spatial frequency, or color entropy) for each real-world image and showing that token count predicts familiarity beyond what complexity alone predicts.
4. **Add a baseline comparison** — e.g., compare token-count-based originality to simply measuring DreamSim reconstruction distance after a fixed 1-token textual inversion. This would show whether the multi-token extrapolation adds value.
5. **Report variance** (error bars or box plots) for the synthetic quantitative experiment, and explain the "+" failure cases.

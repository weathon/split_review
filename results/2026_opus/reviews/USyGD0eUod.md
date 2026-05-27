Now let me calibrate the score with anchor papers.Round 1 bracket: This paper is most similar to 9ca9eHNrdH (Avg 7.0), a critique paper about SAEs. It is more focused (negative finding only) and somewhat narrower in contribution. Bracket: 5.5–7.## Summary

The paper applies the Adebayo-style sanity check to sparse-autoencoder (SAE) evaluation: it trains SAEs on residual-stream activations of Pythia models (70M–6.9B) and compares trained transformers against several random-weight baselines (Step-0, re-randomized including/excluding embeddings, and a Gaussian-token control). The headline finding is that aggregate auto-interpretability scores (fuzzing/detection AUROC) and several reconstruction metrics fail to clearly distinguish trained from random transformers — especially at larger scales — and the paper proposes token-distribution entropy as a complementary diagnostic plus a toy-model account of why random networks may preserve/amplify superposition.

## Strengths

- **Systematic multi-scale evaluation.** SAEs are trained across five Pythia sizes (70M–6.9B) with a consistent protocol (TopK SAEs, R=64, k=32, 100M RedPajama tokens, with a 1B-token replication in Appendix C and hyperparameter sweeps in Figure 18). The collapse of the trained/random gap with scale is shown to be a trend, not a single-model artifact.
- **Multiple, complementary null baselines.** Four variants (Step-0, re-randomized incl./excl. embeddings, Gaussian-input control) are compared. Figure 1 shows that for Pythia-6.9b all three random-weight variants nearly overlap the trained model in fuzzing AUROC while the Gaussian-token control sits at chance — robust evidence that the result is not specific to any one randomization scheme.
- **Constructive diagnostic.** Token-distribution entropy (Figure 2 row 7) is a simple, cheap latent-level statistic that does separate trained from random variants: entropy rises with layer depth for trained Pythia but stays flat for randomized models, consistent with the qualitative story that random models retain single-token detectors but do not build abstract features.
- **Honest scoping and self-criticism.** The paper explicitly flags the entropy metric as "proof-of-concept" (Conclusion), acknowledges Bricken et al. (2023) and Karvonen et al. (2024c) found the gap in their settings (Section 2), and notes the CE-loss metric does still distinguish trained from random (Section 3).

## Weaknesses

### Fatal
None.

### Major

- **Framing overshoots the evidence in the paper itself.** The title and headline framing assert that auto-interpretability metrics "do not distinguish" trained and random transformers, but Section 3 already shows (a) CE-loss score does decisively distinguish them (Figure 2 row 5; the authors explain it away as "only makes sense for the trained variant," but that is precisely the sanity check working), (b) explained variance and L1 norm partially separate randomized variants from trained, especially in larger models (Figure 2 rows 1 and 3), and (c) the gap in fuzzing AUROC is still visible in smaller models (Section 2 paragraph on Bricken et al.; Pythia-70M result). The defensible finding is narrower: *aggregate LLM-judged auto-interp scores* (fuzzing/detection) at scale fail to discriminate, while functional and reconstruction metrics still carry signal. The paper would be stronger if title/abstract/conclusion matched this narrower scope; as written, the gap between title and body weakens the contribution.

### Minor

- **Section 4 (toy-model mechanism) does explanatory work it cannot fully support.** Section 4.2's Pareto-frontier argument is suggestive, and Section 4.3 itself shows the GloVe-vs-Gaussian gap is *smaller* than the toy-superposed-vs-Gaussian gap (Figure 5b), which mildly weakens the "the input is already superposed and the random net preserves it" story. The authors flag this as speculative ("we speculate", "defer conclusions … to future work"), but the conclusion still leans on it; either tying the toy model to a measurable prediction on actual Pythia activations or demoting Section 4 explicitly to "plausibility argument" would help.
- **The entropy metric is positioned as a contribution but is only loosely validated as "abstractness."** Figure 2 row 7 establishes a real layer-trajectory difference, but the paper does not show that high-entropy latents are also causally/computationally important (e.g., via interventions). The conclusion's "targeted measures of feature 'abstractness'" is stronger than what the experiments support; the conclusion already acknowledges this with "proof-of-concept," but the abstract does not.
- **AUROC for randomized models exceeds AUROC for trained models in Pythia-6.9b (Figure 1: trained 0.79 vs. randomized 0.87).** The paper attributes this to simpler, single-token features being easier for the LLM judge. This is a sharper critique of the fuzzing/detection protocol than the paper foregrounds — if randomized models score *higher*, then fuzzing AUROC is not merely insensitive but anti-correlated with feature depth at scale. Worth surfacing in the main text.
- **Variance/seeds not on main-figure curves.** Appendix E is cited for multiple seeds, but several headline visual differences in Figure 2 (especially at smaller Pythia sizes) look small enough that variance bands would clarify which gaps are real.

### Trivial
None.

## Nice-to-Haves

- A causal/intervention follow-up on a small subset of latents (e.g., 50 high-AUROC latents from trained vs. random Pythia-160M) showing that the trained ones are computationally used and the random ones are not. This would turn the critique into a constructive diagnostic.
- A stratified AUROC-by-entropy analysis in the main text (Appendix H is mentioned), making explicit how much of the trained/random similarity is driven by easy single-token-detector latents.
- An additional null with different structural properties (e.g., permuting weights within layers) to strengthen the argument that the result is not specific to "preserve per-matrix mean/variance" nulls.
- Tighten Section 4 to one falsifiable mechanism tested on real Pythia residual streams (e.g., layer-0 vs. layer-L sparsity in random Pythia compared to the toy model).

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Strength: addresses an important problem in mechanistic interpretability."* — Generic / superficial; not specific enough to count.
- *"Randomization scheme not argued to be the right null."* — The paper provides three structurally distinct random variants (Step-0, re-randomized incl./excl. embeddings) that converge, which is a reasonable defense. Demoted from the harsh critic's Critical Issue to a Nice-to-Have.
- *"Missing variance bands is a structural problem"* — Variance results are provided in Appendix E; the paper does not hide them. Demoted to Minor.

## Novel Insights

The most useful observation that emerges across reviews is that the fuzzing/detection auto-interp pipeline appears not merely insensitive to whether a transformer is trained — at large scales it may be *anti-correlated* with feature depth, because randomized transformers yield simpler single-token-detector latents that LLM judges find easier to classify. Combined with the token-entropy result, this points toward a concrete hypothesis: aggregate auto-interp AUROC rewards easy, low-entropy latents that both trained and random models produce in abundance, and discrimination must therefore happen at the *per-latent* level (e.g., entropy- or causally-stratified AUROC) rather than via aggregate scores. Beyond this, the insights are reasonable extensions of the paper's own contributions.

## Suggestions

- Restate the headline as a claim about *auto-interpretability AUROC specifically* — not "SAE metrics" in general — and note explicitly that CE-loss score and reconstruction metrics retain discriminative signal.
- Move stratified AUROC-by-entropy analysis (currently Appendix H) into the main text; this directly explains the headline result.
- Add a small causal intervention check distinguishing trained vs. random high-AUROC latents.
- Either commit Section 4 to a falsifiable mechanistic prediction validated on Pythia or relabel it explicitly as a plausibility argument.
- Bring variance bands onto the main-text Figure 2 curves, especially for smaller Pythia where gaps are visually small.

## Axis-by-Axis Assessment

- **Originality:** Moderate. The random-baseline critique extends Adebayo et al. (2020) to SAEs and generalizes Bricken et al. (2023) and Karvonen et al. (2024c) to multi-layer Pythia at scales up to 6.9B with modern auto-interp pipelines. Incremental but timely.
- **Importance of the research question:** High for the SAE/mechanistic-interpretability subfield, which currently leans heavily on the metrics being critiqued.
- **Support of claims:** Mostly well-supported, but the title/abstract overstate relative to Figure 2 (CE loss and reconstruction metrics do partially separate trained from random).
- **Soundness of experiments:** Sound. Multiple model scales, multiple randomization variants, hyperparameter sweeps, multi-token-budget replication.
- **Clarity of writing:** Generally clear; framing inconsistency between body and abstract/conclusion is the main issue.
- **Value to the research community:** Real. The field needs this kind of calibration, and the entropy diagnostic is a useful, low-cost addition.

## Score Calibration

Anchors retrieved:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/89wVrywsIy.md` — avg 3.40, Round 1 — Sparse-circuit interpretability paper, weaker execution and clarity than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Wxl0JMgDoU.md` — avg 2.50, Round 1 — Niche SAE chess paper, far less rigorous than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9L9j5bQPIY.md` — avg 2.50, Round 1 — Idiosyncratic metanetwork paper, below this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/UbLvSPMvMA.md` — avg 1.67, Round 1 — Weak SAE-binary paper, well below this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9ca9eHNrdH.md` — avg 7.00, Rounds 1 & 2 — "Sparse Autoencoders Do Not Find Canonical Units of Analysis" — closest topical analogue: a critique paper about SAEs with two novel techniques. This paper is more focused (one negative result + one preliminary metric) and contains fewer methodological contributions than 9ca9eHNrdH, but the empirical scaling sweep is broader.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ghH6YYDs15.md` — avg 4.67, Round 1 — SAE inference theory paper; this paper is stronger empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F76bwRSLeK.md` — avg 4.80, Round 1 — The original SAE-finds-features paper; less rigorous evaluation than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZtvRqm6oBu.md` — avg 5.25, Round 1 — SAE-for-unlearning; similar empirical thoroughness, narrower contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tcsZt9ZNKD.md` — avg 8.20, Round 1 — "Scaling and evaluating sparse autoencoders" (OpenAI); much larger contribution than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I4e82CIDxv.md` — avg 8.00, Round 1 — "Sparse Feature Circuits"; much broader, more constructive contribution than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kbjJ9ZOakb.md` — avg 8.00, Round 1 — Off-topic (visual cortex); not comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nwDRD4AMoN.md` — avg 9.00, Round 1 — Off-topic (Kuramoto oscillators); not comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bXeSwrVgjN.md` — avg 6.00, Round 2 — Deletion-metrics critique paper; analogous "critique an existing evaluation" pattern. Similar level of empirical depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/62K7mALO2q.md` — avg 6.00, Round 2 — In-context learning diagnostic; similar diagnostic-paper style.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bpheRCxzb4.md` — avg 6.50, Round 2 — Information-theoretic explanation evaluation; comparable empirical framing.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/v675Iyu0ta.md` — avg 5.60, Rounds 2 & 3 — "Interpretability Illusions in Simplified Models"; very direct analogue (negative-result interpretability paper).
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1Njl73JKjB.md` — avg 7.00, Round 2 — "Towards Principled Evaluations of SAEs"; direct analogue at 7.0 with a broader evaluation framework.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/imT03YXlG2.md` — avg 6.50, Round 2 — PatchSAE on CLIP; similar empirical depth, different focus.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XAjfjizaKs.md` — avg 6.50, Round 2 — Multi-layer SAEs; similar scope and depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Hf17y6u9BC.md` — avg 6.67, Round 2 — Best practices of activation patching; similar diagnostic paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sqsGBW8zQx.md` — avg 5.75, Round 2 — Mechanistic circuits study; comparable empirical depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vsU2veUpiR.md` — avg 5.25, Round 2 — Mechanistic unlearning; less directly comparable.

**Round 1 bracket:** between 5.5 and 7.0, anchored by 9ca9eHNrdH (7.0) and v675Iyu0ta (5.6).

**Round 2 narrowing:** The most directly analogous anchors are 9ca9eHNrdH (7.0), 1Njl73JKjB (7.0), v675Iyu0ta (5.6), XAjfjizaKs (6.5), imT03YXlG2 (6.5), and Hf17y6u9BC (6.67). The 7.0 anchors offer broader contributions (multiple novel techniques or full evaluation frameworks); this paper offers one well-executed negative result plus a preliminary metric. The 6.5-tier anchors are closer matches: well-executed, focused empirical studies on SAEs/interpretability. The paper lands close to those 6.5-tier anchors, with framing issues pulling it slightly below the broader-contribution 7.0 anchors but clearly above the 5.6 anchor (v675Iyu0ta), which had a more confused empirical setup.

Final score: **6.0** — closer to the 6.5-tier anchors than to the 7.0 anchors because of the framing overshoot and the preliminary status of the entropy/toy-model contributions, but above the 5.6 "interpretability illusions" anchor because the experiments are cleaner and the result is more directly actionable for the field.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
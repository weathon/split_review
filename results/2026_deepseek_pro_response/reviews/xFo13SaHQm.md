Now let me do the final comparison. Reading the narrowed anchors, here's how I see the paper positioning:

- **UIFace (6.00):** Similar domain (face generation, identity preservation). Smaller contribution (two-stage denoising + attention injection), less comprehensive evaluation. Our paper is clearly stronger.
- **InstantPortrait (6.67):** Portrait editing with identity preservation. Good dataset, but limited to style editing (no pose/expression). Our paper has broader scope, larger dataset, more novel training approach.
- **MGFR (7.33):** Face restoration, new dataset, multi-modal guidance. Strong paper but main criticism was limited novelty. Our paper has more novel contributions (copy-paste framing, paired training, GT-aligned ID loss) and more comprehensive evaluation. However, MGFR scored 7.33 with fewer identified weaknesses.

Our paper is stronger than InstantPortrait (6.67) — we have a larger dataset, more baselines, more novel contributions, and a broader scope. It's in the same ballpark as MGFR (7.33) — both have dataset contributions, novel training strategies, and compelling results. Our paper has more novelty but also the controllability claim-evidence gap.

**Final score: 7.0**. The paper makes substantial, well-motivated contributions (dataset, benchmark, model, training paradigm) with compelling empirical evidence. The weaknesses are evidential/presentation-level rather than fundamental. The controllability claim is partially supported by the evaluation (GT-matching implicitly requires changing expression/pose) and qualitative results, though a more direct test would strengthen the paper.

Now let me write the final review.

Let me also recall all anchors:

Round 1:
- ID-Booth (3.00, Reject) — clearly weaker than our paper
- IC-Light (0.50, Accept) — anomaly, different domain
- Text To Stealthy Adversarial Face Masks (3.00, Reject) — different domain
- Unsupervised Learning of Facial Attribute Representations (3.00, Reject) — different domain
- Event-Customized Image Generation (5.00, Reject) — weaker, limited novelty
- Personalized Representation from Personalized Generation (5.60, Accept) — different domain
- Vec2Face (6.00, Accept) — comparable domain, our paper is stronger
- HiDF (4.25, Reject) — different domain
- A Decade's Battle on Dataset Bias (8.00, Accept) — different domain, not comparable
- LOKI (8.00, Accept) — different domain
- Visual Data-Type Understanding (8.00, Accept) — different domain
- CADS (8.00, Accept) — different domain

Round 2:
- UIFace (6.00, Accept) — similar domain, our paper stronger
- RAPID (6.00, Accept) — different domain
- SiDA (6.25, Accept) — different domain
- Vec2Face (6.00, Accept) — already compared
- InstantPortrait (6.67, Accept) — similar domain, our paper comparable/slightly stronger
- Ctrl-Adapter (7.00, Accept) — different domain
- MGFR (7.33, Accept) — similar domain, our paper comparable
- TEASER (7.00, Accept) — different domain

Our paper at 7.0 sits between InstantPortrait (6.67) and MGFR (7.33), which feels right.Now I have all the evidence I need. Let me write the final calibrated review.

## Summary

This paper identifies "copy-paste artifacts" — the tendency of ID-preserving generation models to directly replicate the reference face rather than synthesize identity under natural variation — as a core, previously unquantified failure mode in identity-consistent image generation. The authors contribute (1) MultiID-2M, a 500k-image paired dataset of group photos with reference images per identity; (2) MultiID-Bench, a benchmark with a principled copy-paste metric that shifts evaluation from reference-similarity (Sim(Ref)) to ground-truth-similarity (Sim(GT)); and (3) WithAnyone, a FLUX-based model trained with a GT-aligned ID loss, an InfoNCE contrastive loss with extended negatives, and a paired-training phase that breaks the reconstruction shortcut. The central empirical result is that WithAnyone sits off the fidelity–copying trade-off curve that 12 baselines all fall on, achieving top-tier identity similarity with substantially reduced copy-paste.

## Strengths

- **Identification and formalization of the copy-paste artifact with a principled evaluation shift.** The paper names a previously unquantified failure mode and provides a clean, interpretable metric M_CP (Eq. 2, Section 4) that captures the angular bias of the generated face toward the reference versus the ground truth. Crucially, the paper argues that Sim(Ref) inadvertently rewards copy-paste and proposes Sim(GT) as the primary metric instead. This re-framing is a genuine conceptual contribution that should influence how the field evaluates ID-consistent generation.

- **Paired-data training strategy that demonstrably breaks the reconstruction shortcut.** By constructing paired data where reference and target are *different* images of the same identity and training on these pairs for 50% of samples, the model is forced to learn high-level identity representations rather than low-level pixel replication. The ablation (Table 3) directly validates this: removing Phase 3 increases CP from 0.161 to 0.239 while Sim(GT) remains nearly identical (0.405 vs. 0.406).

- **Compelling empirical evidence that the fidelity–copying trade-off is broken.** Figure 5 shows a clear regression curve across 12 baselines: higher Sim(GT) correlates with higher copy-paste. WithAnyone is the sole outlier, achieving near-highest Sim(GT) (0.460) while maintaining markedly lower copy-paste than models with comparable fidelity (CP of 0.144 vs. InstantID's 0.337 at nearly identical Sim(GT)). This result holds across both single-person and multi-person subsets (Tables 1–2).

- **GT-aligned landmark trick for ID loss across all noise levels.** Prior methods restrict ID loss to low noise levels or incur costly full denoising because landmark extraction on noisy latents is unreliable. Aligning the generated image using GT landmarks before ArcFace extraction (Section 5.1, Eq. 4) is a simple, practical fix. Fig. 7 shows consistently lower ID loss across noise levels 0.2–0.8, and the ablation (Table 3) shows Sim(GT) drops from 0.405 to 0.385 without it.

- **Extended negative pool exploits labeled data for stronger contrastive signal.** Expanding InfoNCE negatives from batch size (~63) to 4096 using the labeled reference bank is a natural but effective use of the dataset's identity labels. The ablation (Table 3) confirms its importance for identity fidelity.

## Weaknesses

### Fatal

None.

### Major

- **Controllability claims outrun what the evaluation directly tests.** The paper's title promises "Controllable" generation and the abstract claims "improves controllability over pose and expression" (line 9). The primary evaluation — Sim(GT) and CP on MultiID-Bench — measures how well the model reproduces a specific ground-truth photograph given a detailed prompt describing that photograph. While this implicitly tests a form of controllability (e.g., a prompt saying "smiling" paired with a neutral reference requires the model to change expression), it does not directly test open-ended, user-directed control over individual attributes such as systematically varying expression, head pose, or gaze while holding identity constant. The evidence supports a narrower claim — identity-consistent re-rendering under varied reference–target pairs — but the paper frames it as general controllability. Either a direct controllability evaluation or more carefully scoped claims are needed.

### Minor

- **User study compares against a limited set of baselines.** The user study (Section 6.3, Fig. 8) compares WithAnyone (labeled "Cure") against UNO, iDetch, Uniformal, and OmniGen — none of the strongest face-customization baselines from Table 1. InstantID and PuLID, which achieve the highest or near-highest Sim(GT) scores (0.464 and 0.452), are absent. Even if these are single-ID methods, comparing on the single-person subset would let human raters judge whether reduced copy-paste compensates for differences in fidelity. The naming discrepancy ("Cure" vs. "WithAnyone") also suggests either inconsistency or that the study was conducted on an earlier version of the method.

- **Aesthetics degradation is not acknowledged or analyzed.** In Table 1, WithAnyone achieves the second-lowest aesthetics score (Aes = 4.783), substantially below GPT-4o (5.344), InfU (5.389), and FLUX.1 Kontext (5.319). This is never discussed, despite Phase 4 being explicitly described as "quality tuning" meant to "enhance perceptual fidelity" (line 192). The reduction in copy-paste may come at a cost to perceptual image quality — this trade-off deserves acknowledgment and analysis.

- **Phase 4 (quality tuning) is under-described for reproducibility.** The paper states that Phase 4 fine-tunes on a "curated high-quality subset augmented with generated stylized variants" (line 192) but does not specify what constitutes the high-quality subset or how the stylized variants are produced.

- **UMO is absent from the multi-person evaluation without explanation.** UMO is described in §2 (line 45) as a multi-ID method, yet it does not appear in Table 2's multi-person benchmark. The exclusion should be explicitly justified.

### Trivial

- **"DreamID" appears in Table 2 without being introduced or defined** in the baselines section (§6) or anywhere else in the main text.
- **Naming discrepancy:** the method is called "WithAnyone" throughout the main text but labeled "Cure" in the user study figure (Fig. 8).

## Nice-to-Haves

- A direct controllability evaluation that systematically varies a single attribute (e.g., expression, head pose) via prompts while holding identity constant, measured with a dedicated classifier or landmark detector.
- Analysis of the relationship between CP and Aes across methods to clarify whether the aesthetics degradation is a general phenomenon or specific to WithAnyone.
- An ablation over negative pool sizes (not just batch-only vs. 4096) to characterize how the InfoNCE loss scales with negatives.
- Inclusion of InstantID and PuLID in the user study for a stronger head-to-head comparison on the core trade-off question.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "OmniContext results mentioned only in passing without a full results table."** — Factually incorrect. The OmniContext results are presented in full in Table 1b (lines 159–178), labeled "OmniContext Single Character Subset."
- **Harsh Critic: "DynamicID exclusion rationale insufficient — should state whether authors attempted reproduction."** — The paper already states the reason on line 53: "Excluded from our experiments due to unavailability of code and pretrained models." This is a standard and sufficient justification.
- **Harsh Critic: "The ethics discussion about using names for collection vs. training sits uneasily."** — This is a philosophical nitpick. The paper articulates the distinction clearly (lines 65–66), and it is a reasonable position.
- **Harsh Critic: "435 test cases is modest" combined with "GPT-4o prior knowledge weakens the rare/long-tail claim."** — 435 cases is reasonable for a focused benchmark. The paper itself acknowledges GPT's prior knowledge in the Table 2 note (lines 200–201).
- **Harsh Critic: "4096 negative pool size is not ablated beyond batch-only (63)."** — The batch-only comparison is the relevant ablation; sweeping over pool sizes is a nice-to-have, not a weakness.
- **Harsh Critic: "CP ranking filter (Sim(GT) > 0.40) means rankings are not directly comparable across all methods."** — The paper transparently notes this filtering criterion in Table 1. It is a reasonable methodological choice.
- **Harsh Critic: "Qualitative claims about expression/pose controllability are not systematically measured."** — These are presented as qualitative observations supported by quantitative metrics (Sim(GT) measures whether the model matched the target expression/pose). The paper does not claim them as systematic measurements.
- **Strength Finder: "User study validates metric alignment with human judgment" (as a strong standalone strength).** — While the user study provides some human validation, its evidential weight is limited by the narrow baseline set. Kept as a supporting point but noted in weaknesses.

## Novel Insights

The paper's observation that the standard evaluation metric Sim(Ref) inadvertently rewards copy-paste — and that shifting to Sim(GT) reorients the entire evaluation framework — is a genuinely novel insight that should influence how the field evaluates ID-consistent generation going forward. The CP metric's normalization by the angular distance between reference and GT (Eq. 2) is a particularly elegant design choice that makes the metric interpretable across different identity–reference pairs.

## Suggestions

- Rescope the controllability claims to match what the evaluation actually demonstrates, or add a targeted experiment that directly measures attribute-level control (e.g., prompt "make this person smile" and measure expression change via a classifier).
- Add a brief analysis of the aesthetics trade-off — even a paragraph acknowledging it and hypothesizing causes would significantly improve the paper's completeness.
- Explicitly justify UMO's exclusion from Table 2 and define DreamID in the baselines section.
- Resolve the Cure/WithAnyone naming discrepancy in Fig. 8.

## Calibration

**Round 1 bracket:** 6.0–7.5 (above Vec2Face at 6.00, below the 8.00-tier papers on different topics).

**Round 2 narrowing anchors:**
- UIFace (6.00, Accept): Similar domain. Our paper has larger contributions, broader evaluation, more novelty. Our paper is stronger.
- InstantPortrait (6.67, Accept): Portrait editing with identity preservation. Our paper has broader scope, larger dataset, and more novel training. Our paper is comparable to slightly stronger.
- MGFR (7.33, Accept): Face restoration with dataset + model. Our paper has more novel contributions (copy-paste framing, paired training) but also the controllability claim gap. Our paper is comparable, slightly below MGFR's polish.

**Final score:** 7.0 — positioned between InstantPortrait (6.67) and MGFR (7.33). The paper makes substantial, well-motivated contributions (dataset, benchmark, model, training paradigm) with compelling empirical evidence. Weaknesses are primarily evidential/presentation-level rather than fundamental. The controllability claim is partially supported by the benchmark design (GT-matching implicitly requires expression/pose changes) and qualitative results, though more direct evaluation would strengthen the paper.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
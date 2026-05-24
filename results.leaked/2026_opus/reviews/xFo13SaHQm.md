Let me now calibrate against human-reviewed anchors.## Summary

The paper formalizes the "copy-paste artifact" in identity-consistent image generation — where models replicate the reference face rather than synthesize identity across pose/expression variation — and introduces a differentiable Copy-Paste metric (Eq. 2) that quantifies the relative bias of a generated embedding toward the reference vs. the ground truth. It then contributes three concrete artifacts: (1) MultiID-2M, a 500k paired multi-identity group-photo dataset with ~25k identities, (2) MultiID-Bench, an evaluation protocol that pairs Sim(GT), Sim(Ref), and CP, and (3) WithAnyone, a FLUX-based model trained with a four-phase paired-data pipeline, GT-landmark-aligned ID loss, and an InfoNCE-style ID contrastive loss with an extended (~4096) negative pool. Empirically, the model achieves Sim(GT)=0.460 (very close to the top-ranked InstantID at 0.464) while attaining a CP of 0.144 — substantially lower than other methods with comparable Sim(GT) (UMO 0.359, InstantID 0.337, PuLID 0.315), supporting the central "breaks the trade-off" claim shown in Fig. 5.

## Strengths

- **A new, well-motivated, differentiable metric for an under-quantified failure mode** (Eq. 2). Phrasing CP as the geodesic-distance bias of the generated embedding toward reference vs. ground truth gives a single principled scalar in [-1, 1] that captures what Sim(Ref) alone cannot. Fig. 2's density plot and Fig. 5's scatter make the metric's behavior intuitive.
- **Empirical evidence that the trade-off is actually broken**, not merely re-balanced. In Table 1 (single-person), Ours achieves Sim(GT)=0.460 / CP=0.144, while every other method with Sim(GT)≥0.44 has CP≥0.23 — a Pareto improvement, not a frontier slide. Table 2 (multi-person) shows the same pattern (Ours Sim(GT)=0.405 / CP=0.161 on 2-person, 0.414 / 0.171 on 3-4 person).
- **Concrete, useful dataset contribution.** The bottleneck the paper identifies (paired multi-image-per-identity supervision) is real, and 500k paired group photos with hundreds of references per celebrity is a non-trivial resource that directly enables the proposed training paradigm.
- **GT-aligned ID loss is a genuinely useful design.** Section 5.1 / Fig. 7 show that aligning ArcFace landmarks from GT rather than from noisy predictions enables loss application at all noise levels without full denoising — addressing a known issue in PortraitBooth / PuLID style losses.
- **Component contributions are individually validated.** Table 3 isolates Phase 3 paired tuning (CP rises 0.161 → 0.239 when removed) and the extended-negatives pool (Sim(GT) drops 0.405 → 0.368 when negatives are cut from 4096 to 63), giving credit to specific design choices rather than only the package.

## Weaknesses

### Fatal
None.

### Major

- **The aesthetics signal contradicts the paper's claim of "strong perceptual quality."** In Table 1, Ours has Aes=4.783 — the lowest among all 14 baselines (compare InfU 5.389, GPT-4o 5.344, FLUX.1 Kontext 5.319). The abstract claims WithAnyone "maintains strong perceptual quality"; the quantitative aesthetic metric does not support this. The user study (Fig. 8, n=10 raters, 230 groups, ranking) is the main counter-evidence, but a 10-person ranking study is thin to overturn a clear quantitative gap of ~0.5 on Aes against well-trained competitors. The paper should reconcile this directly.
- **OmniContext results undercut the generality claim.** Table 1b shows Ours at Overall=6.52, beaten by OmniGen2 (8.34), GPT-4o (8.12), FLUX.1 Kontext (7.94), DreamO (7.02), and others. The text reframes this as "best among face customization models," which is fair, but the gap to general models is large enough that the paper should be clearer that the contribution is targeted at the ID-customization regime and not at general personalization.

### Minor

- **CP metric stability when t and r are close.** Eq. 2 divides by max(θ_tr, ε). When the reference and ground truth depict the same identity in similar pose/lighting, θ_tr can be small and the denominator dominated by ε, amplifying noise in the numerator. The paper introduces ε for numerical stability but does not quantify how often θ_tr is near ε or how sensitive CP rankings are to the choice. Some sensitivity analysis would strengthen the metric.
- **Filtering CP-ranking to cases with Sim(GT) > 0.40 (single) / > 0.35 (multi)** is reasonable to avoid scoring random-face generators well on CP, but it is also an ad hoc gating that varies between subsets. Reporting CP across thresholds, or as a 2D scatter (as in Fig. 5) for all rows, would make the comparison less threshold-dependent.
- **One ablation row is awkward for the headline claim.** In Table 3, "w/o Ext. Neg." has Sim(G)=0.368 and CP=0.074 — i.e., much lower CP than the full setting (CP=0.161). The full setting clearly wins on Sim(GT), but the paper frames CP as the failure mode of interest; explaining why the chosen operating point is preferable (e.g., that w/o-ext-neg sacrifices identity) deserves an explicit sentence rather than being left to the reader.
- **User study scale.** Ten raters across 230 groups, four criteria each, is on the small side for a perceptual claim that aesthetics + prompt adherence + similarity + CP are all simultaneously improved. Inter-rater agreement or per-criterion variance would help.
- **Coverage of identities.** MultiID-2M is constructed from celebrity web data (~25k identities). The model's behavior on non-celebrity / non-public-figure references is not characterized, which is the realistic deployment setting. This is mentioned as a constraint but not empirically probed.

### Trivial

- Figure 8's method labels appear distorted in the extracted text ("Cure", "iDetch", "Uniformal"); ensuring the labels read clearly in the final PDF would help readers cross-reference the bubble chart with the tables.

## Nice-to-Haves

- A short analysis of CP vs. human CP-judgment correlation (the paper mentions a "moderate positive correlation" — quoting the actual coefficient would substantiate that CP is perceptually meaningful, not just a derived geometric quantity).
- Reporting θ_tr distribution over the benchmark — useful to validate that the denominator in Eq. 2 is generally well away from ε.
- An additional comparison on a non-celebrity identity test set (even small) would meaningfully support the generality argument.

## Removed Points

*These points were considered but dropped. Treat them with caution.*

- "The Strength Finder said 'removing extended negatives… increases CP from 0.161 to 0.074.'" — This is a misreading by the strength finder, not the paper: Table 3 shows CP *drops* to 0.074 when ext. neg. is removed, but Sim(G) also drops to 0.368. The paper itself reports the numbers correctly; this was a reviewer-side error and is not a paper weakness. (The genuine concern — that w/o-ext-neg has a lower CP — is retained above under Minor.)
- A general "metric could be measuring a proxy" critique — speculative without a concrete anchor; the paper provides a direct CP construction grounded in angular distances and validates against user-study rankings.
- A general "comparison may be unfair" sweep — the paper compares against 14 baselines including general (OmniGen2, FLUX.1 Kontext, Qwen-Image-Edit, GPT-4o) and face-specific models, on a held-out benchmark; the asymmetry that exists (e.g., GPT-4o's prior celebrity knowledge for 3+ID subsets) is explicitly flagged in the Table 2 caption.
- Generic strength "addresses an important problem" — too vague; dropped.

## Novel Insights

The most useful idea introduced beyond standard contributions is the framing of Sim(Ref) as an *adversarial* metric — a metric that, optimized naively, encourages the very copy-paste pathology it is supposed to penalize — and the corresponding shift to Sim(GT) plus a geodesic CP measure. This framing reorganizes how the field should think about identity-fidelity evaluation: "higher similarity to the conditioning input" is not monotone with "better identity-conditioned generation," and the paper's two-axis (Sim(GT), CP) view (Fig. 5) makes the previously hidden Pareto structure visible. The empirical observation that all 14 prior methods lie on a tight fitted curve in this 2D space, while paired-data + extended-negative training visibly departs from it, is itself a result.

## Suggestions

- Reconcile the Aes 4.783 number against the "strong perceptual quality" claim — either qualify the abstract or add evidence (FID/per-prompt aesthetic comparisons) that the user-study win generalizes.
- Add explicit text contrasting the full setting and w/o-ext-neg in Table 3, since the latter has lower CP; explain why the chosen operating point is the right one.
- Quantify CP's correlation with the user-study CP ranking (cite the correlation coefficient and its p-value).
- Report distribution of θ_tr and a CP sensitivity sweep over ε to nail down metric robustness.
- Add a small non-celebrity probe set (even 50–100 cases) to demonstrate that the paired-training advantage holds when the reference identity is unseen and out-of-distribution.

## Axis-wise assessment

- **Originality.** Moderate-to-high. CP as a geodesic-bias metric is a fresh formulation; GT-aligned landmark trick and extended-negative InfoNCE are useful but more incremental.
- **Importance.** High for the ID-customization subfield. Copy-paste is a widely observed but rarely quantified failure; the paper names, measures, and mitigates it.
- **Soundness of claims.** Mostly well-supported. The headline "breaks the trade-off" is empirically clear in Table 1, Table 2, and Fig. 5. The "strong perceptual quality" claim is the one that is overreached relative to Aes numbers.
- **Soundness of experiments.** Solid — 14 baselines, two benchmarks, ablations on each component, a user study. Single-run evaluation is standard for this scale.
- **Clarity.** Generally clear; Fig. 5 communicates the central message efficiently. Some ablation interpretation deserves more prose.
- **Value to community.** High — a usable benchmark, a non-trivial dataset, a metric others can adopt, and a model that materially advances ID-consistency without copy-paste.

## Calibration

Round 1 anchors retrieved (avg human scores):
- NWvsm2VxAM (3.00), 12iSWNLDzj (3.00), qW5f8TAZ4J (3.00), kCnLHHtk1y (3.00) — weak band; paper is clearly stronger.
- Bz9wjvToCS (4.40), 88Qm4fGWzX (5.00), riieAeQBJm (6.00), XhyCPEnlCa (4.25) — middle band; paper is stronger than 4-5 anchors, comparable to or above UIFace (6.00).
- bnINPG5A32 (8.00 RB-Modulation), 1aF2D2CPHi (8.00), vaEPihQsAA (7.60), u1cQYxRI1H (10.00 IC-Light) — strong band; paper is below RB-Modulation/IC-Light's methodological depth.

Round-1 bracket: **5–7.5**.

Round 2 narrowing anchors:
- jw7P4MHLWw (5.60 Personalized Representation), Mzz9i4Zf8B (5.40 CLoRA), 4GSOESJrk6 (6.00 DreamBench++), cijOBlCxMa (5.67 CustomNet), D9CRb1KZQc (5.75 Refine-by-Align), cD1kl2QKv1 (7.40 1Prompt1Story), BWuBDdXVnH (6.25 ControlAR), mDKxlfraAn (6.40 Watermarks).

Read in full: DreamBench++ (6.00) — pure benchmark contribution, comparable in scope to MultiID-Bench alone; this paper additionally contributes a dataset, metric, and model, so it should score *above* DreamBench++. 1Prompt1Story (7.40) — single methodological contribution with strong empirics; arguably more novel per-idea but narrower in scope.

This paper bundles a benchmark (DreamBench++-comparable), a dataset (substantial), a novel metric, and a model with multiple validated components. It is more comprehensive than the 6.00 anchors but its model-side novelty is more incremental than 1Prompt1Story. It lands between them, closer to the upper anchor: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
Now let me run calibration searches to properly score this paper.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

AutoCLIP proposes a lightweight inference-time modification to zero-shot CLIP-style classifiers: instead of uniform averaging of encoded class descriptors across prompt templates, it assigns per-image weights via one step of gradient ascent on a logsumexp objective. The step size is automatically determined by bisection to hit a target entropy reduction factor β, making the method effectively parameter-free in a zero-shot setting. The paper evaluates across 6 VLMs, 3 prompt strategies, 8 datasets, and K from 4–500 (990 total settings), finding improvements on ~85% of configurations at +0.45 pp average and up to +3 pp, with all computation in the embedding space and no additional encoder passes.

---

## Strengths

- **Inference-time, embedding-space adaptation with no extra encoder passes.** Algorithm 2 explicitly shows that after initial image and descriptor encodings, only a closed-form gradient step and a bisection solve are needed per sample—no backpropagation through text or image encoders. This is a qualitatively different cost regime than TPT/RLCF, which require multiple augmented views and gradient through the text encoder.

- **Automatic step-size selection via entropy control.** Section 3.4 reparameterizes the free hyperparameter as a target entropy reduction factor β, which is global and dimensionless. The ablation (Figure 5) shows performance is stable over β ∈ [0.7, 0.9] across datasets, confirming the claimed robustness.

- **Exceptionally broad evaluation (990 configurations).** The experimental grid spans 6 VLMs (RN50, ViT-B/32, ViT-B/16, ViT-L/14 CLIP, DataComp ViT-L/14, CoCa ViT-L/14), 3 prompt strategies (CLIP, DCLIP, WaffleCLIP), K ∈ {4, 10, 50, 100, 200, 500}, 8 datasets including ImageNet-C with corruption severity variation, and 7 randomness runs. This is a stronger evaluation than most comparable papers in this space.

- **Controlled synthetic analysis providing mechanistic insight.** Section 5 constructs an embedding-space simulation with controllable entanglement ρ and instance noise ε, showing AutoCLIP outperforms mean aggregation for ρ > 0.4. This predicts that smaller VLMs (more entangled text encoders) benefit more, which matches Figure 3—providing a credible explanation rather than post-hoc rationalization.

- **Interpretable weight visualization.** Figure 6 shows learned per-image prompt weights on Food101: "A drawing of…" and "A tattoo of…" consistently receive low weight, while "A photo of…" receives high weight, validating the method's core intuition.

- **Closed-form gradient derivation.** Section 3.3 provides an explicit formula for ∇_ρ logsumexp(s), enabling deployment without autograd—practically useful for edge devices.

---

## Weaknesses

### Fatal
None.

### Major

- **No quantitative comparison with ZPE (the most closely related work).** Section 3 explicitly identifies Zero-shot Prompt Ensembling (ZPE, Allingham et al.) as the single closest prior method—both assign per-prompt weights in embedding space without labeled data. The paper's advantages over ZPE (single-sample, source-free) are argued only in prose, not demonstrated empirically. While the operational difference is real, at least one shared evaluation setting would clarify whether AutoCLIP achieves comparable accuracy to ZPE in the regime where ZPE is applicable, or whether the gains merely reflect the different problem setting. This is the paper's clearest evidential gap.

### Minor

- **β default (0.85) is inconsistent with the paper's own ablation recommendation.** Section 4 states: *"Also on average, β=0.7 performs favorably and we recommend this choice for future work."* Yet all headline numbers throughout the paper are reported under β=0.85. The discrepancy is acknowledged but not acted on—the paper's primary results do not reflect its own best-practice recommendation. The difference is modest (the method is robust in [0.7, 0.9]) but the presentation is internally inconsistent, and reporting results under β=0.7 would slightly increase the reported gains.

### Trivial

- **The upper bound of 10¹⁰ in the bisection for α is justified only empirically** ("in all settings we considered") with no analysis of edge cases (e.g., very small K, nearly identical prompt similarities). A single sentence on the failure condition would improve the description.

---

## Nice-to-Haves

- A single table showing inference time per image for AutoCLIP vs. TPT vs. baseline (on at least one VLM and dataset) would make the computational advantage concrete rather than descriptive.
- The controlled setting analysis would be more convincing if it showed whether the synthetic entanglement ranking of VLMs matches the ranking of AutoCLIP's benefit sizes observed in Figure 3—connecting the simulation quantitatively to the real experiments.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Essentially no free hyperparameters" overstates the case (harsh critic, Introduction):** The paper's exact phrasing is "comes essentially without free hyperparameters," not "has zero free hyperparameters." This is a mild precision issue but qualifies as a style nitpick rather than a substantive error. The method genuinely operates with a single global scalar requiring no per-dataset tuning—keeping this as a major weakness would be disproportionate. *Removed as substantive weakness; noted only as trivial.*

- **Gains are only compared to a uniform-weight baseline, not stronger baselines (latent concern):** The paper's framing is explicitly "a plug-in inference modification to any existing zero-shot classifier," so the uniform-weight baseline is the direct and appropriate reference. Demanding comparison to methods that tune prompts or train adapters is scope creep. *Removed as a weakness.*

- **Strength: "closed-form gradient enables edge deployment"** — Technically valid, but since most inference happens on GPUs with autograd, this is a minor practical note rather than a core contribution. *Retained but demoted to supporting strength.*

---

## Novel Insights

The paper's most genuinely novel observation is the coupling between the *diversity* of the prompt set and the benefit of weighted aggregation: gains scale from Δ=0.06 at K=4 to Δ=0.57 at K=200. This is not merely an implementation detail—it implies that the prompt-weight adaptation and prompt-set diversity are complementary, and that AutoCLIP's practical value will grow as prompt generation methods like WaffleCLIP continue to scale. The controlled experiment further predicts a specific failure mode (small entanglement + large instance noise → slight degradation), which is empirically confirmed on ViT-L/14 on ImageNet-C, making the analysis genuinely falsifiable.

---

## Suggestions

1. **Re-run full evaluation under β=0.7** (the authors' own recommendation from the ablation) and report those as the primary numbers, with β=0.85 shown as a comparison point. This eliminates the internal inconsistency and likely improves all headline figures modestly.
2. **Add a single quantitative row for ZPE** in one shared experimental setting (e.g., WaffleCLIP K=100 on Food101 or ImageNet) to show directly how AutoCLIP compares to its closest competitor where overlap is possible.
3. **Add an inference-cost table** (wall-clock time per image for AutoCLIP vs. TPT vs. baseline) to make the efficiency claim concrete.

---

## Score and Decision

**Calibration:**

**Round 1 anchors:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| pdzHpQbGrn.md | 2.50 | 1 | Weak test-time prompt learning with labeled samples needed; clearly inferior to AutoCLIP |
| j1FLTvgyAh.md | 2.50 | 1 | Few-shot multi-prompt without principled aggregation; far simpler and weaker |
| Rc3RP9OoEJ.md | 5.00 | 1 | InCPL: test-time prompt tuning with clarity and comparison issues; AutoCLIP is cleaner |
| kIP0duasBb.md | 6.67 | 1 | RLCF: covers 3 tasks, requires backprop; broader scope but higher cost than AutoCLIP |
| 1aF2D2CPHi.md | 8.00 | 1 | DFKD for CLIP customization; stronger novel contribution than AutoCLIP |
| WyEdX2R4er.md | 8.00 | 1 | New VLM benchmark; different type of contribution, higher significance |
| 5Ca9sSzuDp.md | 8.00 | 1 | CLIP interpretation paper; deeper theoretical contribution |

**Round 1 bracket: 5.5–6.5**

**Round 2 anchors:**
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| fRpAUgKJhT.md | 5.75 | 2 | CARPRT: class-aware prompt reweighting for VLMs (very similar task); rejected; AutoCLIP has broader evaluation and cleaner method, but similar magnitude of gains |
| Zkq4fsyjfp.md | 6.25 | 2 | CLIP backbone adaptive ensembling; accepted; different setting (requires labeled data), similar evaluation breadth |
| NeVbEYW4tp.md | 5.00 | 2 | Self-TPT: efficient test-time prompt tuning; rejected; AutoCLIP has cleaner method and broader evaluation |
| t84UBRhhvp.md | 4.75 | 2 | SLR-AVD: text descriptor augmentation; rejected; narrower evaluation, less clean method |
| 74vnDs1R97.md | 5.80 | 2 | Visual concept transferability across VLMs; accepted; different setting but similar contribution level |

**Narrowing:** AutoCLIP is clearly better than CARPRT (5.75, rejected) due to: (a) per-image operation vs. requiring a batch, (b) much broader evaluation grid (990 settings vs. narrow), (c) controlled synthetic experiment, (d) cleaner entropy-controlled step-size design. AutoCLIP is comparable to the CLIP backbone ensembling paper (6.25, accepted) in evaluation breadth and contribution level, though that paper requires labeled data and AutoCLIP is fully zero-shot. AutoCLIP's main weakness (no ZPE comparison) is comparable in weight to the weaknesses of those borderline-accept papers.

AutoCLIP sits above CARPRT (5.75) but below RLCF (6.67). Given its clean method, genuinely broad evaluation, consistent improvements, and only one meaningful fixable gap (ZPE comparison), I place it at **6.0**—above the CARPRT threshold and consistent with the Zkq4fsyjfp.md (6.25) anchor given AutoCLIP's slightly narrower scope and missing ZPE comparison.

**Axes summary:**
- *Originality*: Moderate — per-image prompt weighting is a clear and useful idea; the entropy-control parameterization is the genuinely novel design decision; work is incremental relative to ZPE but in a meaningfully different regime.
- *Importance of research question*: Good — zero-shot inference improvements that cost nothing are practically valuable.
- *Claims well-supported*: Good — 990 settings, 7 runs, consistent finding; β inconsistency slightly undercuts the claim.
- *Soundness of experiments*: Strong — broad VLM/dataset/prompt grid, ImageNet-C robustness evaluation, ablations, controlled synthetic analysis.
- *Clarity*: Good — algorithms are precise, method well-described, controlled setting clearly explained.
- *Value to research community*: Moderate-to-good — a simple drop-in improvement with broad applicability; limited by modest absolute gains.

**Decision: Weak Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes AutoCLIP, a method that improves zero-shot CLIP classifiers by adaptively weighting prompt templates per image at inference time, entirely within the embedding space (no extra encoder passes or backpropagation). The weights are determined via a single gradient ascent step on a logsumexp aggregation objective, with an automatic step-size selection mechanism that controls the entropy of the weight distribution via a single global hyperparameter β. The method is evaluated across 6 VLMs, 8 datasets, 3 prompt strategies, and prompt counts from 4 to 500 (990 settings total), showing consistent improvement over uniform weighting in ~85% of settings with an average gain of 0.45 pp and gains up to 3 pp.

## Strengths

- **Inference-time adaptation entirely in embedding space, zero extra encoder passes.** Unlike TPT/RLCF which require multiple image augmentations and backpropagation through the text encoder, AutoCLIP operates solely on pre-computed embeddings (Algorithm 2). This is a genuine architectural advantage for deployment scenarios where compute is constrained. The paper is explicit about this: "adaptation takes place entirely in the embedding space without requiring additional forward or backward passes through the VLM's encoders" (lines 21-22).

- **Automatic step-size selection via entropy control removes dataset-specific tuning.** In a zero-shot setting there is no labeled data for tuning. AutoCLIP replaces the step-size hyperparameter with an interpretable entropy reduction factor β, and derives α via bisection. The ablation (Figure 4) shows stable performance for β∈[0.7,0.9], confirming robustness — a desirable property for zero-shot deployment.

- **Remarkably broad evaluation across 990 settings (6 models × 8 datasets × 3 prompt strategies × varying K).** AutoCLIP outperforms uniform weighting in ~85% of settings, averaged over 7 runs. The evaluation covers CLIP RN50/ViT-B-32/ViT-B-16/ViT-L-14, DataComp ViT-L-14, and CoCa ViT-L-14, plus ImageNet-C robustness. This breadth convincingly supports the claim of broad applicability.

- **Closed-form gradient (Section 3.3) enables deployment without autograd.** This is a practical advantage for edge/embedded inference where automatic differentiation may be unavailable.

- **Ablation justifies the logsumexp design choice empirically (Figure 5).** Logsumexp outperforms mean, max, and entropy objectives on all 7 datasets tested, confirming the design reasoning from Section 3.2.

- **Qualitative weight visualization (Figure 6) directly validates the intuition.** On Food101, semantically mismatched templates ("A tattoo of…") receive low weights while "A photo of…" receives high weights, confirming the method adapts to image content without supervision.

## Weaknesses

### Fatal
None.

### Major

- **Experimental comparison against ZPE is missing despite being identified as "most similar" work.** The paper explicitly states (lines 49, 21-22) that ZPE (Allingham et al., 2023) is the most closely related method and claims the advantage of operating on single samples without source-domain features. Yet zero experimental comparison is provided against ZPE or any other adaptive weighting scheme. The reader cannot tell whether AutoCLIP's embedding-space efficiency comes with a meaningful accuracy trade-off relative to the closest existing method. A comparison on a representative subset (e.g., ImageNet, Oxford Pets with 100 WaffleCLIP prompts) is needed to substantiate the claimed advantages. *This is the single most important gap in the evaluation.*

### Minor

- **No variance/error bars reported despite small average improvement of 0.45 pp.** Results are reported as means over 7 runs with no standard deviations or confidence intervals. On ImageNet/ImageNetV2 the Δ is as small as 0.1–0.2 pp, and without variance the reader cannot assess whether these small gains are systematic or within noise. The 85%-consistent directional signal across 990 settings partially mitigates this, but reporting std in at least the main table would substantially strengthen confidence.

- **β inconsistency between default (0.85) and recommended value (0.7).** The paper uses β=0.85 in all main experiments (line 130) but states that "on average, β=0.7 performs favorably and we recommend this choice for future work" (line 194). Since the ablation shows β=0.7 is better on average and more robust across datasets, it is unclear why the main results were not updated to reflect this — or why β=0.85 was retained. The claim that AutoCLIP comes "essentially without free hyperparameters" (line 41) is also slightly overstated since β is acknowledged as "the new free hyperparameter" (line 130). The paper is transparent about β and provides an ablation, but the inconsistency is confusing.

- **Ablation on number of gradient steps mentioned but data not shown.** The paper states "preliminary experiments indicate no advantage of doing more than one iteration" (line 91) but provides no quantitative evidence. A brief table or sentence with the comparison would be helpful.

- **Energy-based interpretation (line 87) mentioned but not empirically tested.** The connection to EBM via logsumexp is a nice theoretical note but is not validated (e.g., by correlating logsumexp scores with model likelihoods). This is a missed opportunity for deeper analysis, not a flaw in the core contribution.

### Trivial
None.

## Nice-to-Haves

- A quantitative comparison of per-image inference overhead (e.g., ms or FLOPs relative to the VLM forward pass) would make the efficiency claim concrete. The paper defers this to the appendix (Section A.1), but a brief number in the main text would be welcome.
- Showing weight visualizations (similar to Figure 6) for one or two additional diverse datasets (e.g., EuroSAT or ImageNet-R) in the main text would strengthen the qualitative evidence.

## Removed Points

- **Missing comparison to TPT methods as a fatal flaw**: The harsh critic framed the missing TPT comparison as the paper's "most significant weakness." This is retained as Major (not Fatal) because the paper's core contribution is improving over uniform weighting (which it demonstrates convincingly), not claiming SOTA among all TTA methods. However, the missing ZPE comparison is more serious since ZPE is structurally the closest method and the paper makes explicit comparative claims about it.
- **Criticism about missing appendix content**: Removed per hard rules (parser strips appendices from all papers).
- **Criticism about "no comparison of absolute compute cost"**: Downgraded to Nice-to-Have since the paper defers quantitative cost analysis to the appendix and claims are stated qualitatively with the right caveats.
- **Generic scope-creep criticisms** (e.g., "would the paper benefit from showing X") were removed when they demanded analysis outside the paper's stated scope.
- **Strength Finder claims about "importance of the research question"**: Removed as generic/superficial per filtering rules. The retained strengths are concrete and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful critiques (missing ZPE comparison, lack of error bars, β inconsistency) but do not contribute novel technical insights about the method itself.

## Suggestions

1. **Add ZPE as a baseline** on a representative subset (e.g., ImageNet, Oxford Pets, ImageNet-R with 100 WaffleCLIP prompts, using CLIP ViT-B-16 and ViT-L-14). This single addition would most directly address the evaluation gap.
2. **Report standard deviations** for the main results in Table 1 (or add error bars to Figure 2). Given the small deltas, this is important for establishing that improvements are systematic.
3. **Resolve the β inconsistency**: either adopt β=0.7 as default (and update main results accordingly) or clearly explain why β=0.85 was retained (e.g., as a conservative choice demonstrating robustness to suboptimal settings).
4. **Include the gradient-step ablation** as a brief note (even a single sentence with Δ values for 1 vs 2 vs 5 steps) to substantiate the claim that one step suffices.
5. **Add a concrete compute-cost number** (e.g., "AutoCLIP adds X ms per image, compared to Y ms for the VLM forward pass and Z ms for TPT").

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- `/home/wg25r/review_agent/human_reviews/pdzHpQbGrn.md` (avg 2.50, Reject) — Active TPT learning; weak anchor. AutoCLIP is substantially stronger.
- `/home/wg25r/review_agent/human_reviews/fRpAUgKJhT.md` (avg 5.75, Reject) — CARPRT: class-aware prompt reweighting. Very similar topic. AutoCLIP is cleaner (no pseudo-labels), evaluates more broadly, and has a more novel step-size mechanism. *AutoCLIP > CARPRT.*
- `/home/wg25r/review_agent/human_reviews/kIP0duasBb.md` (avg 6.67, Accept) — RLCF: TTA with CLIP reward. Stronger across multiple tasks. *AutoCLIP < RLCF.*
- `/home/wg25r/review_agent/human_reviews/3i13Gev2hV.md` (avg 8.00, Accept Oral) — Hyperbolic VLMs; very different topic, strong anchor. AutoCLIP is not at this level.

**Initial bracket:** between 5 and 7.

**Round 2 (Narrowing):**
- `/home/wg25r/review_agent/human_reviews/5Aem9XFZ0t.md` (avg 4.83, Reject) — Zero-shot concept bottleneck models; different topic, weaker paper.
- `/home/wg25r/review_agent/human_reviews/KNtcoAM5Gy.md` (avg 5.50, Reject) — BaFTA: backprop-free TTA via online clustering. Similar lightweight-adaptation space. BaFTA was rejected for insufficient novelty and incomplete ablations. *AutoCLIP > BaFTA.*
- `/home/wg25r/review_agent/human_reviews/jzzEHTBFOT.md` (avg 6.00, Accept) — C-TPT: calibration during TPT. Comparable quality and scope. Both have clear motivation, simple methods, and broad evaluation. *AutoCLIP ≈ C-TPT.*
- `/home/wg25r/review_agent/human_reviews/NeVbEYW4tp.md` (avg 5.00, Reject) — Self-TPT: efficient TPT. Had a fundamental technical flaw flagged. *AutoCLIP > Self-TPT.*

**Final bracket:** narrowed to ~5.5–6.5. AutoCLIP sits above the rejected prompt-reweighting papers (CARPRT at 5.75, BaFTA at 5.50) and is comparable to C-TPT (6.00, accepted). It falls short of RLCF (6.67, accepted) which shows stronger results across multiple tasks.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
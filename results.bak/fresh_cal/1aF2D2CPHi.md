Here is my consolidated review.

---

## Summary

This paper addresses data-free knowledge distillation (DFKD) from CLIP to a lightweight student model, enabling open-vocabulary customization using only class texts or a few example images. The key finding is that existing DFKD methods fail on CLIP because CLIP's BatchNorm statistics encode facial features from web-scale training, producing corrupted synthetic images. The authors propose an inversion pipeline based on image-text matching (bypassing BN layers), augmented by style dictionary diversification, class consistency maintaining, and meta knowledge distillation. Experiments on Caltech-101, Flower-102, and ImageNet-1K splits show that the approach outperforms DFKD baselines.

## Strengths

- **Diagnostic discovery of why DFKD fails on CLIP** (Section 3, Figs. 2–3): The paper identifies that CLIP's BatchNorm statistics encode facial features from web-crawled training data, causing standard BN-based inversion methods (DeepInversion, CMI) to produce corrupted, face-dominated synthetic images. This is supported by quantitative ablations (40–69% performance drop when BN loss is removed) and clear visual evidence. The finding is specific and actionable.

- **Novel combination of style diversification, class consistency, and meta knowledge distillation**: The three components work together to address a real failure mode. Style dictionary diversification (Sec. 4.1) increases diversity; class consistency maintaining (Eq. 4) prevents semantic drift from over-stylization; meta knowledge distillation (Eq. 5–6, Theorem 4.2) encourages style-invariant student representations by aligning gradients across styles. The ablation in Table 1 shows each component contributes positively, with meta-KD alone providing 3–9% gains.

- **Practical mitigation of text ambiguity** (Section 5.4, Table 6): The paper honestly identifies that CLIP can misinterpret short class names (e.g., "balloon flower"), and experimentally evaluates two fixes — using few-shot image prompts and LLM-generated detailed descriptions — showing accuracy improvements (e.g., 55.42% → 72.73%). This strengthens practical applicability.

- **Architectural flexibility demonstrated** (Table 5): The approach transfers across different teacher (CLIP-RN50) and student (ViT-T) architectures with accuracy within ~1.5% of the primary setting, supporting the claim of broad applicability.

## Weaknesses

### Fatal

None. The paper's core claims — that BN-based DFKD fails on CLIP and that the proposed image-text-matching pipeline works — are supported by evidence and not invalidated by any single weakness.

### Major

1. **Unusual DFKD baseline construction using test-set fine-tuning** (Section 3, line 45: "fine-tune this classifier using the testing set"). To apply existing DFKD methods (DeepInversion, CMI) to CLIP, the authors add a linear classifier on CLIP's visual encoder and fine-tune it on the test set. This means the DFKD baselines' teacher had access to test-set labels (and images for fine-tuning) — a deviation from standard data-free protocols. While the asymmetry likely *helps* the baselines (making the paper's 9.33% improvement conservative), the evaluation is not conducted under a standard, well-controlled protocol. The paper should either (a) use a held-out validation set or zero-shot CLIP as the DFKD teacher, or (b) explicitly justify why the comparison is fair despite this choice.

2. **Missing statistical significance** (all tables report single accuracy values without standard deviations or confidence intervals). Given that the synthetic dataset generation involves stochastic optimization (random initialization, text augmentation, contrastive learning), the results likely have nontrivial variance. Without multiple runs, it is unclear whether reported improvements (e.g., 3–9% from meta-KD) are statistically significant. This is standard practice for empirical papers in this field.

### Minor

3. **No ablation on the number of styles N** (fixed at N=16, Section 5.1). The meta-learning component is a core claim, but the paper does not vary N to show whether performance degrades gracefully with fewer styles or whether the method depends critically on having ~16 distinct styles. This limits understanding of the meta-KD's robustness.

4. **Reliance on a manually curated style dictionary without sensitivity analysis** (Section 4.1). The style dictionary (terms like "pattern", "illustration", "photorealism") requires human domain knowledge to construct. The paper does not evaluate how sensitive results are to dictionary composition, size, or whether automated construction (e.g., from WordNet or an LLM) would suffice. This weakens the claim of being "hands-off" data-free customization.

5. **Theorem 4.1 (covering-number bound) has a loose connection to the specific method**. The bound shows that more diverse surrogate data improves generalization if the surrogate δ-covers the real distribution. However, the paper does not estimate δ or provide evidence that the style dictionary actually achieves δ-cover. The theorem motivates diversity in general but does not directly validate the specific style dictionary design.

6. **Theorem 4.2 (gradient alignment) assumes a single inner-loop step**, while the practical implementation presumably uses multiple steps. The paper should discuss whether the analysis extends to the multi-step setting used in practice or note this as a simplification.

### Trivial

None.

## Nice-to-Haves

- Clarify the claim "outperform DFKD methods that utilize real data" (line 52). If this refers to methods with access to original training data, the comparison is apples-to-oranges and should be clearly differentiated from the main DFKD comparison.
- Include a comparison with zero-shot CLIP as a sanity check for the teacher quality (rather than only finetuned classifiers).
- Report inference speed/throughput in addition to parameters and FLOPs (Table 3).
- Consider evaluating on a broader range of student architectures (e.g., MobileNet, EfficientNet) to strengthen the architectural flexibility claim.

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper:

- **"The central claim is about a known limitation of BN-based inversion, not a discovery about CLIP specifically"** — The paper's discovery is *specific* to CLIP: that CLIP's BN statistics encode facial features from web data, which is not a generic "BN statistics don't match" observation. The visual evidence (Fig. 3) and the fact that IN-pretrained models work fine support this as a CLIP-specific finding.

- **"Unfair comparison: DFKD baselines see test data, proposed method does not"** — This asymmetry actually *helps* the baselines (they get a teacher adapted to the test distribution). The 9.33% improvement is therefore conservative, not inflated. The comparison is unconventional but not unfairly biased toward the proposed method.

- **"The paper does not cite works that discuss this limitation in general"** — Removed per meta-reviewer instructions (do not flag missing related works without external confirmation).

- **"Fatal: the method is not truly data-free" because style dictionary is manually curated** — The method IS data-free in the standard DFKD sense (no original training data used). Manually constructing a small set of style prompts (16 terms) is a far cry from requiring the original training set; it is a reasonable design choice that the paper could better evaluate, but it does not negate the "data-free" designation.

- **"Pure formatting/style nitpicks" and "typos/grammar"** — Removed as parser artifacts.

- **Generic weaknesses about missing appendix content** — The appendix sections referenced (App. A, G, H) exist in the original submission; the parser stripped them.

- **"The meta-learning objective may not capture invariant representations with only 16 tasks"** — This is speculation rather than a demonstrated flaw. The paper shows it works; the absence of an N-ablation is a valid minor weakness (included above), but the claim that it "may not work" is not a verified problem.

## Novel Insights

None beyond the paper's own contributions. The two reviewers did not produce any insight about the paper's approach, limitations, or broader implications that the authors did not already articulate.

## Suggestions

1. Re-run the DFKD baseline comparison using a teacher whose classifier is not fine-tuned on the test set (e.g., use CLIP's zero-shot logits directly as the teacher for DFKD methods, or use a validation-set-only protocol). Report whether the conclusions change.
2. Add standard deviations over at least 3 random seeds for all main results.
3. Ablate the number of styles N (e.g., N = 4, 8, 16, 32) to understand the sensitivity of the meta-KD component.
4. Include a sensitivity analysis of the style dictionary (e.g., random vs. curated terms, different sizes).
5. Clarify the "Data-Real" comparison: specify whether these are standard KD (not DFKD) baselines with training data access, and whether the comparison is intended to show that the proposed data-free method approaches data-access performance.

## Score and Decision

**Originality:** Moderate. The diagnostic finding about CLIP's BN statistics is novel; the technical components (style diversification, meta-KD) are individually known but their combination in the DFKD-for-VLMs context is new.

**Importance of research question:** High. Data-free customization from foundation models is practically important for privacy-preserving deployment.

**Claims well-supported:** Partially. The core claims are supported, but the baseline construction issue and missing statistical significance weaken the quantitative evidence.

**Soundness of experiments:** Moderate. The experiments show the method works, but the evaluation protocol has methodological concerns (test-set fine-tuning for baselines, no variance reporting).

**Clarity of writing:** Good. The paper is well-structured, and the problem motivation is clear.

**Value to community:** Moderate–high. The approach is practically useful, and the BN-statistics diagnostic is valuable for researchers working with CLIP in DFKD settings.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
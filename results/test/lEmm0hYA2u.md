Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper proposes ZeroP, a zero-shot quantization (ZSQ) framework that mixes publicly available proxy data (PD) with synthetic data (SD) for fine-tuning quantized networks, rather than relying on SD alone. The paper introduces a simple batch-normalization-statistics (BNS) distance metric for selecting an appropriate PD from a pool of candidates and evaluates the approach across 16 datasets, multiple architectures (ResNet-18/50, MobileNetV1/V2, RegNet-600MF), and bit-widths (4-bit, 5-bit). The key finding is that mixing well-chosen PD (e.g., COCO) with SD consistently and substantially outperforms pure-SD methods (e.g., +3.9% for ResNet-50 4-bit on ImageNet-1K vs. IntraQ), while remaining competitive with methods that use original data.

## Strengths

- **Novel and effective use of proxy data as direct input in ZSQ**: Rather than using PD only to guide SD generation (as in prior work on model stealing), ZeroP directly mixes PD with SD as training data for quantization fine-tuning. This is a conceptually simple but unexplored direction that yields large gains — e.g., using COCO as PD improves MobileNetV1 4-bit accuracy from 48.27% (SD-only) to 58.60% (+10.3 pp), with similar gains across architectures (Table 1, Table 2).

- **Simple and computationally cheap PD selection via BNS distance**: The BNS-distance metric (Eq. 5) enables fast selection of an effective PD using only ~1024 samples per candidate, without running full quantization. Spearman's rank correlation coefficients ≥0.75 across all architectures and bit-widths (Figure 4) confirm that BNS distance is a strong predictor of PD usefulness. The paper also documents the relationship transparently — grouping PDs by BNS distance in Table 1 and reporting exceptions where the ranking is noisy.

- **Consistent SOTA performance and generalizable integration**: ZeroP achieves the best results among pure-SD methods in 4-bit across 4 architectures on ImageNet-1K (Table 2), and the PD-mixing strategy can be plugged into existing ZSQ methods (GDFQ, Qimera, IntraQ) with consistent improvements (Table 3). The paper evaluates 16 diverse PDs (general-domain, fine-grained, medical-style, noisy, etc.), providing a thorough empirical characterization of when PD helps and when it hurts.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that PD improves ZSQ, that BNS distance is a useful selection heuristic, and that ZeroP achieves SOTA among pure-SD methods — are well-supported by the experiments.

### Minor

1. **The BNS selection method is validated only correlationally, not operationally.** The paper shows that BNS distance correlates with accuracy (Spearman ≥0.75) and groups PDs by BNS distance into performance tiers (Table 1). However, it does not test the actual selection workflow a practitioner would follow: given a limited pool of, say, 5 random PD candidates, does following the BNS rule reliably pick a PD within, e.g., 1% of the best candidate? The correlation evidence makes this likely, but the paper would be stronger with a concrete simulation. The paper acknowledges "PD with the smallest BNS distance is not always the best choice," but does not bound the risk. This is a gap in evaluating the selection method as a *decision rule* rather than just a *rank correlation metric*.

2. **The claim of "comparable performance of OD methods" is slightly overstated.** In Table 2, ZeroP is consistently below FDDA (an OD method) in 4-bit settings — e.g., ResNet-50: 72.17% vs. 73.36%. While "comparable" is not wrong (the gap is ~1.2%), the framing in the introduction ("achieves comparable performance of OD methods") suggests a closer match than the data support. The paper would be more precise by saying "competitive with" or "approaching the performance of OD methods."

3. **The t-SNE visualization (Figure 2) is suggestive but not quantitatively supported.** The claim that PD "has a better t-SNE match" than SD relies on visual inspection of 5 selected classes. A distributional distance metric (e.g., FID, MMD) over the full feature space would substantiate this claim more rigorously. As presented, the figure is primarily illustrative.

### Trivial
- The paper defers significant experimental details (e.g., 5-bit results, Pearson correlations, dataset descriptions) to the supplemental materials, which were not available for review. This is standard practice but limits thoroughness.
- Figure 2's caption invites zooming for "better visual effect," which is impractical in a printed proceedings format.

## Nice-to-Haves

- A PD-only (γ=1.0, no SD) condition in Table 3 would further isolate whether the benefit comes from PD alone or from the PD+SD combination. The current ablation compares mixing conditions (γ=0.5) with different data sources, which supports the paper's claims but leaves this question open.
- A brief qualitative discussion of what makes a good PD beyond BNS distance (e.g., domain similarity, label overlap, image statistics) would help practitioners who have only a small pool of candidate datasets.
- Testing on non-CNN architectures (e.g., Vision Transformers), which the paper acknowledges as future work (Limitations section).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Flawed comparison class — comparing only against pure-SD methods is unfair"** (Harsh Critic). Removed because: the paper's contribution IS showing that PD improves over SD-only methods, making this exactly the right comparison. The reviewer's claim that "adding real data will almost always help" is factually contradicted by the paper — many PDs hurt (SVHN, MNIST, Stanford Dogs hurt relative to baseline; Random Noise often hurts in Table 3). The paper also provides ablation controls in Table 3 (SD vs. RN vs. PD vs. OD), which the reviewer acknowledges but dismisses. The comparison class is appropriate, not flawed.

- **"Zero-shot framing conceals a substantive constraint"** (Harsh Critic). Removed because: ZSQ is standardly defined in the literature as quantization without the *original training data* (OD), which ZeroP satisfies. The paper explicitly discusses the constraint in the Limitations section ("Obtaining PD can be challenging for certain tasks. In some cases, there may be no available candidate datasets to serve as PD"). Computing BNS distance on a few thousand PD samples (M=1024 per candidate) is computationally trivial compared to the SD generation process used by pure-SD methods.

- **"The BNS selection method is circular"** (Harsh Critic). Removed because: using the pre-trained model's BNS statistics as a reference for distributional similarity is a standard and well-motivated approach in the ZSQ literature (SD generation methods themselves use BNS loss to match synthetic data to OD). The paper acknowledges the heuristic is imperfect. Calling this "circular" mischaracterizes the methodology — the BNS statistics encode what the model learned from OD, and comparing PD statistics to them is a sensible, widely-accepted proxy.

- **"The 7% to 16% improvements claim is almost tautological"** (Harsh Critic). Removed because: the paper shows these specific improvements for MobileNetV1, and not all PDs improve performance (several hurt). This is an empirical finding, not a tautology.

- **Missing PD-only (no SD) comparison** (Harsh Critic suggestion #1). Removed because: the paper's method IS specifically PD+SD mixing (Eq. 6), not PD alone. The ablation in Table 3 compares mixed conditions (γ=0.5) with different data partners, which is the right control for the proposed method. PD-only would be a different method.

## Novel Insights

The reviewer's observation that Table 3's counterexamples (Qimera + RN > Qimera + SD for MobileNetV1; PD > OD in one CIFAR-10 case) are interesting but underexplored is a genuinely useful insight. These anomalies suggest that SD quality can be so poor for some model architectures that even noise or mismatched real data provides a better training signal. The paper mentions this in passing but does not analyze the root cause. A deeper investigation of *when and why* SD generation methods fail this badly would strengthen the paper's case that PD is a necessary complement, not just a nice addition.

## Suggestions

1. Add an operational validation of the BNS selection rule: randomly sample subsets of PD candidates, apply the selection rule, and report how often the chosen PD is within 1% (or some threshold) of the best available candidate. This would strengthen the practical claims significantly without requiring new experiments.

2. Tone down the "comparable to OD methods" claim in the introduction to "competitive with" or "approaching," to better match the quantitative gap shown in Table 2.

3. Add a quantitative distributional distance (e.g., MMD or FID) between PD and OD feature distributions to complement the qualitative t-SNE visualization (Figure 2).

4. Discuss the counterexamples from Table 3 (RN > SD for MobileNetV1+Qimera) more thoroughly — this anomaly speaks directly to the limitations of current SD generation and motivates the need for PD.

## Score and Decision

This is a solid empirical paper with a clear contribution. The idea is simple yet effective, the experiments are thorough (16 PDs × multiple architectures × bit-widths), and the weaknesses are minor and addressable. The paper does not over-claim its novelty (it explicitly frames PD as a complement to SD, not a replacement), and it acknowledges its limitations honestly.

**Originality**: 6/10 — the idea is simple but the paper is the first to systematically study PD as direct input in ZSQ.
**Importance**: 7/10 — addresses a practical problem (data-free quantization) with a practical solution.
**Claims support**: 7/10 — well-supported for the core claims; minor overstatement on OD comparability.
**Soundness**: 7/10 — experiments are well-designed; selection method validation could be more operational.
**Clarity**: 7/10 — well-written and clear about contributions and limitations.
**Value**: 7/10 — the findings are directly useful to practitioners.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
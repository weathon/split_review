Now I have all the information I need. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full review.

---

Let me finalize my reasoning:

The paper addresses a genuine and interesting problem: learning to separate common and private information in multi-task neural compression using the Gray-Wyner framework. The theoretical contributions (Theorems 1 and 2) are sound and provide principled grounding. The proposed loss function (Eq. 12) with β controlling the transmit-receive tradeoff is well-motivated. The experiments, particularly the synthetic ablation (Fig 3b showing Shared > Separated > Combined) and the colored MNIST edge cases (Fig 4), cleanly demonstrate the method's capabilities.

However, several issues weaken the paper:
1. No statistical significance/variance reporting - major methodological gap
2. The hard combination rule (Eq. 14) is acknowledged to have significant tuning issues
3. Parameter counts/capacity not reported for baseline fairness
4. The theoretical quantities (interaction information, Wyner's/GK common information) are not validated in experiments

Score: 5.5 — The paper has genuine contributions but the experimental weaknesses prevent it from being a clear accept. It's stronger than papers in the ~3-4.75 range (like SWYCC, LLM Entropy) which had thinner novelties or major execution issues. It's comparable to GatedMTL (5.25) but with stronger theoretical foundations. It's clearly weaker than Lattice Transform Coding (7.2) which had rigorous experimental validation.Here is the final consolidated review:

---

## Summary

This paper proposes a learnable three-channel neural codec inspired by the Gray-Wyner network, designed to separate common and private information between two vision tasks. The authors provide theoretical bounds relating lossy Wyner and Gács-Körner common information (Theorem 1), derive a Lagrangian objective (Eq. 12) that controls the transmit–receive rate tradeoff via a single hyperparameter β, and implement a concrete architecture with a hard element-matching rule on the common channel. Experiments on synthetic data, colored MNIST, and two real vision task pairs (Cityscapes, COCO) show that the proposed method substantially reduces redundancy compared to independent coding and approaches joint coding performance.

## Strengths

1. **Principled theoretical grounding for the transmit–receive tradeoff.** Theorem 1 provides inequalities relating lossy Wyner and Gács-Körner common information via interaction information, giving a formal justification for why the two measures can differ in practice and why a tradeoff is necessary. Theorem 2 re-expresses the Gray-Wyner objective as a sum of entropy terms under deterministic encoders, establishing a clear chain from classical information theory to the implemented loss function (Eq. 12). The loss function's β parameter (β=1 for transmit, β=2 for receive, β=1.5 for balanced) is empirically validated in Figure 3a, where the common-channel rate varies as predicted.

2. **Ablation study cleanly validates architectural choices.** On the synthetic dataset (Section 4.1, Figure 3b), the proposed Shared architecture consistently outperforms both the Separated and Combined alternatives across all operating points. Since Separated uses *more* independent transforms than Shared (three vs. two), this advantage cannot be explained by capacity alone, providing direct evidence that the two-branch design with the matching mechanism for the common channel separates information more effectively than the alternatives.

3. **Edge-case experiments on colored MNIST provide controlled validation of information separation.** The method is evaluated on three synthetic PMFs (Dependent, Independent, Mixture) with known mutual information values (Section 4.2, Figure 4). On the Dependent PMF, the common channel carries most information (lowest transmit rate). On the Independent PMF, the common channel is nearly unused (lowest receive rate). The Mixture PMF, where common information is inherently hard to separate, shows intermediate behavior. This controlled experiment confirms the method correctly handles extremes of common information and demonstrates that the loss function meaningfully trades off transmit vs. receive rates.

4. **Redundancy reduction demonstrated on real vision benchmarks.** On Cityscapes (semantic segmentation + depth estimation) and COCO 2017 (object detection + keypoint detection), the proposed method achieves BD-rate improvements of –81.58% on average in transmit rate against single-task (Independent) codecs. Against the Joint baseline, the Transmit variant achieves 23.32% (Cityscapes) and 13.16% (COCO) higher BD-rate, which is substantially closer than the Independent baselines at 143.69% and 77.36%, respectively (Figure 5).

## Weaknesses

### Major

1. **No statistical significance or variance reported.** Rate-distortion curves and BD-rate improvements are presented from single training runs without error bars, multiple seeds, or any measure of variability. Given the known stochasticity in training neural codecs (random initialization, data shuffling, quantization noise), single-run results could be misleading. This is especially concerning for the Cityscapes experiments, where the authors note "an increase in distortion with the lowest compression" (line 278) and speculate about regularization being the cause — this could equally be an artifact of a single training run. Without replication, the reliability of the claimed improvements cannot be assessed. This is a standard expectation for papers making empirical claims in this field.

2. **The hard element-matching rule for combining the common channel (Eq. 14) is acknowledged to have significant tuning difficulties.** Elements that match are averaged; elements that differ are set to zero, and gradient flows only through the matching branch. The paper states that "small values of γ might result in elements of Y₀⁽¹⁾ and Y₀⁽²⁾ never matching" and "a large γ can result in degenerate distributions for Y₀⁽¹⁾ and Y₀⁽²⁾. In both cases, the common channel is underutilized" (lines 186-188). The recommended workaround — setting γ=1 and adjusting β — effectively makes β carry the burden of both the transmit-receive tradeoff and the common-channel utilization, conflating two separate design concerns. This design fragility is not an insurmountable flaw, but it is a structural concern about the method's robustness that the paper does not adequately address.

### Minor

3. **Parameter counts and model capacity not reported.** The proposed Shared architecture uses two analysis transforms, while the Joint baseline uses one. Although the Separated baseline (three transforms) partially controls for capacity, the paper does not report parameter counts, FLOPs, or training budgets for any architecture. The claimed advantages over Independent could partly reflect model capacity differences rather than architectural merit. This is less severe than the critic suggests because: (a) Separated has *more* capacity than Shared yet performs worse, and (b) Joint has *less* capacity yet performs better — so the results are not simply capacity-driven. Still, reporting these numbers would allow practitioners to assess the tradeoff and is standard practice.

4. **Theoretical quantities are not empirically validated.** Theorem 1 bounds lossy common information in terms of interaction information, and Theorem 2 re-expresses the Gray-Wyner objective using entropies. However, the experiments never estimate interaction information, Wyner's common information, or Gács-Körner common information from the learned representations. The paper is transparent about this gap — it states that "optimizing exclusively for the transmit or the receive rate does not guarantee that the common channel will produce Wyner's or Gács-Körner common information" (line 164) — but this leaves the theoretical framing disconnected from the empirical validation. The paper would be stronger as a purely empirical method paper without the heavy theoretical apparatus, or it would need to demonstrate that the learned common channel meaningfully approximates the theoretical constructs.

5. **Non-monotonic behavior in Cityscapes curves not explained.** Figure 5a shows increased distortion at the lowest compression (highest rate) for some configurations. The paper attributes this informally to "lack of regularization, provided by stronger rate constraints" (line 278). This is speculative and suggests the model is not well-behaved across the full rate range. A clear explanation or a regularization fix would strengthen the results.

### Trivial

6. The Combined architecture's poor performance on synthetic data (Figure 3b) is noted but not explained — a brief intuition about why a single analysis transform split into three channels is worse than two separate analysis transforms would help.

## Nice-to-Haves

- Replace or supplement the hard element-matching rule (Eq. 14) with a smoother, differentiable fusion mechanism (e.g., gated summation or attention-based combination) for more principled optimization.
- Compute empirical estimates of interaction information or mutual information between the learned representations and task-relevant variables, directly connecting the theory to the experiments.
- Report runtime, FLOPs, and parameter counts for all architectures to allow practitioners to assess the computational tradeoff.
- Explore β values outside (1, 2) to empirically confirm the paper's claim of suboptimality rather than stating it as a purely theoretical expectation.
- Extend to a simple non-vision domain (e.g., NLP) to broaden the scope beyond computer vision.

## Removed Points

These points from the input reviews were removed with justification:

- **Harsh critic's claim about comparison against Joint being "not sufficiently controlled" because the proposed method uses more parameters:** Partially valid but downgraded to Minor because (a) the Separated baseline has *more* capacity than Shared yet performs *worse*, and (b) Joint has *less* capacity yet performs *better* — the results are not explained by capacity alone.
- **Harsh critic's claim that describing the results as "relatively close" to Joint overstates the result:** Removed. A 13–23% BD-rate increase (Transmit variant) vs. 77–143% for Independent is genuinely close in the context of compression benchmarks.
- **Harsh critic's claim about the paper not exploring β outside (1,2):** Downgraded to Nice-to-Have. The range (1,2) is a theoretical claim, and testing values outside it is a reasonable extension but not a core weakness.
- **Harsh critic's claim about Combined architecture lacking a principled explanation:** The paper refers to Appendix C for a theoretical justification based on compatibility measures. Since the appendix is stripped by the parser, this cannot be verified, but the paper does claim to address it.
- **Strength Finder's generic strengths about the problem being "important" or "relevant":** Removed as generic/superficial. Only concrete, evidence-grounded strengths were retained.
- **Strength Finder's claim about "Optimization grounded in the Gray-Wyner theoretical framework":** Merged into strength #1 as it overlaps with the principled loss function. Not removed, just consolidated.
- **Various formatting/style nitpicks:** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's theoretical ambition and its empirical execution: Theorem 1's bounds on lossy common information are the most novel element, but the experiments validate only the rate-distortion behavior of the architecture, not the theoretical quantities themselves. Neither reviewer observed a connection the authors missed — the gap between theory and validation is acknowledged in the paper and is the principal structural weakness flagged by both reviewers.

## Suggestions

1. **Add multiple-seed results with error bars or box plots** for all rate-distortion curves. This is the single most impactful improvement — it would directly address the major methodological weakness and is standard in this field.
2. **Report parameter counts and FLOPs** for the proposed Shared architecture and all baselines (Joint, Independent, Separated, Combined) to clean the comparison.
3. **Empirically estimate interaction information or mutual information** between the learned common representation Y₀ and task-relevant variables, even approximately, to bridge the theory-experiment gap. The colored MNIST setup (Section 4.2) with known mutual information values is well-suited for this.
4. **Include a brief qualitative analysis** of what the common channel Y₀ actually encodes (e.g., attention maps, reconstruction from Y₀ alone, or a probe classifier) to illuminate the learned representation.

## Score and Decision

**Round 1 — Bracketing:** Three queries on multi-task neural compression and Gray-Wyner topics. Weak anchors (avg 2.3–3.4) were papers like SWYCC and Pruning with CMI — clearly weaker than this paper. Middle anchors (avg 5.25–7.2) included GatedMTL (5.25), Slicing MI (5.5), Compositionality (6.75), and Lattice Transform Coding (7.2). Strong anchors (avg 7.6–8.5) were high-impact papers like diffusion-based compression and generative modeling — clearly stronger. Initial bracket: **4.5–6.5**.

**Round 2 — Narrowing:** Queried the (4.5, 6.0) and (6.0, 7.5) bands. In (4.5, 6.0): LLM Entropy Models (4.75), Compression via Pre-trained Transformers (5.0), Multitask I2I Diffusion (4.75), Model Quantization (5.0) — all rejected, with thinner novelty or more severe experimental gaps. In (6.0, 7.5): Lattice Transform Coding (7.2, accepted spotlight), Cleaner Biosignals (6.6, accepted poster), Compositionality (6.75, rejected), AstroCompress (6.25, accepted poster). Reading GatedMTL (5.25), Lattice Transform Coding (7.2), and LLM Entropy (4.75) in full confirmed the placement.

The paper is stronger than the ~4.75–5.0 anchors (which have incremental novelty or major execution issues) but weaker than the ~6.6–7.2 anchors (which have rigorous experimental validation). Compared to GatedMTL (5.25, rejected), this paper has stronger theoretical novelty but a similar level of experimental methodological gaps (both lack variance reporting). The realistic comparator for acceptance is the ~6.0 boundary — papers at 6+ tend to have both clear novelty and solid empirical backing. The Gray-Wyner paper has the novelty but falls short on experimental rigor.

**Final score: 5.5** — marginally below the acceptance threshold. The theoretical contributions and the clean architectural validation on synthetic data are genuine strengths, but the lack of variance reporting, the acknowledged architectural fragility, and the theory-experiment gap prevent it from being a clear accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
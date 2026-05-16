Now I have a thorough understanding of the paper and can verify reviewer claims against the actual text. Let me compose the final review.

---

## Summary

This paper presents the first systematic empirical study of privacy risks (membership inference and attribute inference) under curriculum learning (CL). Across 9 datasets, 4 CL methods, multiple attack variants, and 4 defenses, the paper finds that CL slightly increases MIA vulnerability (0.01–2.46%), with the increase concentrated on samples the curriculum ranks as difficult. The paper also proposes Diff-Cali, a new MIA that calibrates membership scores with difficulty levels to improve TPR at low FPR, and evaluates existing defenses under CL. The core contribution is the measurement and characterization, not a new state-of-the-art method.

## Strengths

1. **First systematic study of privacy risks in CL.** The paper evaluates 9 real-world datasets (6 image, 3 tabular), 4 CL methods (bootstrapping, transfer learning, baseline, anti-curriculum), and multiple attack vectors (NN-based, metric-based, label-only MIA, and AIA), providing a comprehensive baseline absent from prior work on ML privacy. Table 2 and Figures 1–2 document the breadth.

2. **Demonstrates that CL increases MIA vulnerability disproportionately for difficult samples.** Table 2 shows meaningful CL methods raise MIA accuracy by up to 2.46% (Tiny ImageNet). More importantly, Figure 2 reveals the increase is concentrated in difficult deciles — e.g., on CIFAR100 with bootstrapping, the gap between hardest and easiest decile is 4.23% (absolute) in attack accuracy, while under normal training the gap is negligible. This disparate-impact finding is the paper's most novel insight.

3. **Identifies that ordering matters more than repetition.** The consistent contrast between bootstrapping/anti-curriculum (both use fixed order, opposite directions) and baseline (random order, fixed across epochs) isolates the contribution of data ordering vs. data repetition. Table 2 shows anti-curriculum consistently *decreases* attack accuracy while bootstrapping increases it, establishing that ordering direction — not just repetition — drives the effect.

4. **Shows CL does not increase AIA risk (important negative result).** Table 5 reports normal training yields the highest AIA accuracy (e.g., 0.107 on Place100), while CL methods produce lower values. This distinguishes CL's privacy profile from contrastive learning (where AIA increases per He et al.) and is a practically useful boundary condition.

5. **Evaluates four existing defenses under CL and quantifies trade-offs.** Table 7 shows DP-SGD drops MIA accuracy to near random (~50.5%) but severely harms target accuracy (~17%). Memguard caps NN-based MIA at 50% yet leaves label-only attacks at 81–86%. MixupMMD reduces MIA by ~8% while improving target accuracy. This head-to-head comparison is a practical contribution for deployers.

6. **Findings are robust across architectures.** Table 4 shows the same trends for ResNet-18, ResNet-34, and MobileNet — strengthening the claim that CL's privacy impact is architecture-agnostic.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The practical significance of the MIA increase is not contextualized.** The paper reports MIA accuracy improvements of 0.01–2.46% for image datasets. While the paper honestly describes these as "slightly" more vulnerable, it does not discuss what these numbers mean for an attacker — e.g., how many additional members would be identified at a fixed FPR, or whether the effect exceeds natural variance. The standard deviations are sometimes reported as 0.0000 (presumably due to rounding to 4 decimal places with STD < 0.00005), which the table caption clarifies ("entry without ± STD means the STD is less than 0.01%") but the main MIA accuracy table (Table 2) lacks this note, making the zeros look suspicious. The paper would benefit from adding a brief practical-significance discussion and adding the "less than 0.01%" note to Table 2's caption.

2. **The DP-SGD evaluation uses a large ε (124,496), limiting conclusions about privacy.** The paper transparently acknowledges this and explains it is due to 200 training epochs and ResNet-18's parameter count, citing prior work using similarly large ε. However, Finding 6 states that "DP-SGD can reverse the impact of CL on MIA" based on this evaluation. At ε ≈ 124,496 the DP guarantee is vacuous (effectively no privacy), so the claim that DP-SGD "reverses" CL's impact is only about MIA accuracy reduction — not about formal privacy protection. The paper should either (a) include at least one experiment with a meaningfully smaller ε (e.g., ε ≤ 10) to show the finding holds under a real DP guarantee, or (b) rephrase the finding to avoid implying a meaningful privacy guarantee. The paper's discussion of tunability (citing Bu et al. 2022) helps but does not resolve the gap.

3. **The memorization analysis is a reasonable approximation of the Feldman (2020) definition but does not compute the actual memorization score.** The paper cites the standard definition (Equation in Section 5.2: difference in prediction accuracy with vs. without a sample) but instead compares "not seen" (800 samples removed) to "first seen", "last seen", and "random" orderings of those 800 samples. This is a reasonable proxy for studying ordering effects on memorization, but it does not isolate memorization per the formal definition, which requires per-sample inclusion/exclusion comparisons. The paper also does not justify why 800 samples (4%) are used, or show results across more than one dataset (only CIFAR100). The KNN-Shapley analysis uses a surrogate model whose behavior may not match the deep network, a limitation the paper acknowledges.

4. **Diff-Cali's improvement is modest and its novelty is limited.** The paper acknowledges that NN-based attack achieves higher overall accuracy. Diff-Cali's edge is in TPR at low FPR (better than random below 0.045 where NN-based attack fails) and in making difficult samples more vulnerable. However, the improvement is incremental: e.g., 2.64% and 2.35% better attack accuracy for difficult samples under normal and anti-curriculum ML. The attack requires difficulty scores, which are naturally available when CL is used but may not be in other settings. The paper would be strengthened by clarifying precisely how Diff-Cali differs from Watson et al.'s calibration method beyond using CL-derived difficulty scores.

5. **LiRA, a current SOTA MIA, is not tested.** The paper discusses this omission in the limitations (citing the need for many shadow models and smaller dataset partitions). This is a reasonable justification but still leaves open whether CL's impact on MIA would be larger, smaller, or different under a stronger attack. Given that Diff-Cali's contribution is partly about improving low-FPR performance — LiRA's strength — the omission is notable.

6. **The "baseline curriculum" (random order, fixed across epochs) sometimes decreases attack accuracy** (e.g., Place100: 0.9425 vs. 0.9416). Finding 2 states "Both data ordering and data repeating make a model more vulnerable under MIA," but the baseline's effect is inconsistent. The paper acknowledges this nuance in the text ("For baseline CL, the attack accuracy decreases for Place100, whereas a slight increase is observed...") but the finding boxes oversimplify.

### Trivial

- Several tables show standard deviations of 0.0000. The defense table caption clarifies that entries without "± STD" means STD < 0.01%, but Table 2 (the main MIA accuracy table) lacks this note. Adding it would prevent confusion.
- The paper does not specify the random seeds or exact sizes of the "three disjoint parts" used for splitting datasets. While sufficient for a study of this scope, exact split sizes would aid reproducibility.

## Nice-to-Haves

- Including one DP-SGD evaluation with ε ≤ 10 would substantially strengthen the defense analysis. The paper already notes this is achievable with tuning (citing Bu et al. 2022).
- Computing actual per-sample memorization scores (Feldman definition) on a small subset would directly test whether CL increases memorization of difficult samples, rather than the current proxy analysis.
- A brief quantification of practical significance: e.g., "at a fixed 1% FPR, an attacker using CL can identify X more members per 10,000 queries compared to normal training."

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"DP-SGD accuracy cost is well-known":** The paper reports this as an observation in the context of CL, not as a claimed novel finding. Removed as a strawman.
- **"Does not specify how training/validation/test splits were created":** The paper states "three disjoint parts," which is sufficient for a benchmark paper of this scope. Removed as a nitpick.
- **"Anti-curriculum is not a realistic training method":** The paper explicitly states anti-curriculum is used "to understand the impact of data ordering and repeating" — it is an analytical tool, not presented as a practical method. Removed.
- **"Missing related works":** Per instructions, I cannot verify whether related works are missing without external sources. Removed.
- **"Abstract claims about DP-SGD significant impact" and other presentational nitpicks:** These are factual statements about results, not overclaimed novelty. Removed.
- **Complaints about stripped appendix content:** The parser strips appendix content from all papers; the original submission contains it. Removed.
- **"The paper should also discuss that the MIA effects are small":** The paper uses language like "slightly more vulnerable" and "slightly more effective" throughout, accurately characterizing the effect size. Removed as already addressed.
- **Missing proofs/figures from appendix:** Parser strips appendix content from all papers. Removed.

## Novel Insights

**Beyond the paper's own contributions**, the reviews surface an interesting tension: the paper's main empirical contribution is the *characterization* of CL's privacy impact (small on average, concentrated on difficult samples, ordering-driven), but several of the criticisms implicitly evaluate it as if it were a *method* paper requiring large effect sizes or SOTA attack performance. This mismatch suggests the paper would benefit from more explicitly framing its contribution as a measurement study — where honestly reporting small effects is itself a valid and useful finding — rather than allowing readers to expect dramatic results. The finding that CL's privacy impact is *selective* (affects MIA but not AIA, affects difficult samples more than easy ones) is structurally more interesting than the headline numbers, and this deserves greater emphasis in framing.

## Suggestions

1. Add a practical-significance discussion. For a fixed low FPR (e.g., 1%), how many more members per 10,000 queries would an attacker correctly identify under CL vs. normal training?
2. Add at least one DP-SGD experiment with ε ≤ 10 (or as close as feasible given computational constraints) to validate whether CL still increases MIA vulnerability under meaningful DP guarantees.
3. Compute actual memorization scores (per Feldman 2020) on a small subset of one dataset to validate the proxy analysis.
4. Clarify in Table 2's caption that entries without ±STD have STD < 0.01% (as done in the defense table), to avoid confusion over "0.0000" entries.
5. More clearly delimit Diff-Cali's novelty relative to Watson et al. (2021): which component is the calibration method, which component is the difficulty-score adaptation, and what would be required for the attack to work without CL-provided difficulty scores.

## Score and Decision

This paper is a solid empirical study that provides the first systematic characterization of privacy risks in curriculum learning. Its strengths — breadth of evaluation, the difficult-samples finding, the negative AIA result, the defense comparisons — outweigh its weaknesses, which are about effect size interpretation and methodological depth rather than core validity. The paper honestly reports modest effects and transparently discusses limitations. With the suggested additions (particularly a meaningful DP evaluation and practical-significance framing), it would be a valuable reference for the community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
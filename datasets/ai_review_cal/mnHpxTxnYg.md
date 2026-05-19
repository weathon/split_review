- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3
Now I have a thorough understanding of the paper and all reviewer claims. Let me verify the key claims against the paper.

**Verifying the harsh critic's claim about the paper acknowledging the vacuous bound:**

Paper lines 72-73 explicitly state: *"While Equation 1 is nice in that we can upper bound the rate... it doesn't tell us much about why in practice a classifier f that minimizes error on M might achieve low error on R: (i) f is a neural network and so Lip(f) could be very large in practice, making Equation 1 vacuous and (ii) W^1(G,T) can be quite large."*

**Verifying the mixture assumption acknowledgment:**

Paper line 84: *"The assumption G is a simple mixture distribution is a stronger assumption, and Theorem 4.1 is better viewed as showing why our Detector outperforms the random baseline by a significant margin, but is likely far from the information theoretically optimal MIA."*

**Verifying image results characterization:**

Paper lines 147-149: *"image GANs exhibit less privacy leakage on average, with AUCs that are barely above the random baseline. However, for the most meaningful metric, TPR at low FPRs, our detector-based attacks... are again able to achieve TPRs that are 2-6× higher than the random baseline."*

**Number of runs: Confirmed that image experiments do not specify number of runs** (unlike the genomic section which explicitly states "11 runs").

Now producing the final review.

---

## Summary

This paper investigates black-box membership inference attacks (MIAs) against GANs, where the adversary only has sample access to the generator (not the discriminator — a realistic threat model). The central attack trains a "Detector" network to distinguish GAN-generated samples from real distribution samples, then re-uses this detector's output as a membership inference score. An augmented variant (ADIS) incorporates distance-based features. The paper evaluates on genomic tabular data (two databases, dimensions up to 10K SNPs, two GAN architectures) and image data (four GAN architectures on CIFAR-10). The main finding is that black-box MIAs are feasible, especially on genomic data where ADIS achieves TPRs up to 10× random baseline at low FPRs, while image GANs leak substantially less information (AUCs near 0.5).

## Strengths

1. **Practical black-box threat model.** Unlike prior work assuming discriminator access, the paper addresses the realistic setting where only generator samples are available (Section 3). This fills a gap in the literature and the motivation (copyright, privacy of shared synthetic data) is clearly stated (Section 1).

2. **Thorough empirical evaluation on tabular genomic data.** The paper evaluates 7 attack methods across two genomic databases (1KG, dbGaP) at three dimensionality levels (805, 5000, 10000 SNPs), two GAN architectures (vanilla GAN, WGAN-GP), and over 11 independent training runs. ADIS achieves TPRs "as much as 10× the random baseline" at low FPRs (Section 5.2, Figure 1, Table 3). This is the strongest evidence in the paper and constitutes a genuine empirical contribution.

3. **Comprehensive comparison across data modalities and GAN architectures.** Genomic data (two databases, two GAN architectures, three dimensions) plus image data (four GAN architectures on CIFAR-10, three detector variants, two distance metrics) provides breadth. The paper compares against multiple baselines (distance-based, DOMIAS, Homer attacks) and uses best-practice evaluation metrics (log-log ROC, TPR at low FPRs) as advocated by Carlini et al. (2021).

4. **Use of best-practice MIA evaluation metrics.** The paper focuses on TPR at low FPRs (0.001, 0.005, 0.01, 0.1) rather than overall AUC, which is the appropriate standard for evaluating realistic privacy threats (Section 3, Table 3, Figures 1–2).

5. **Honest boundary-pushing on images.** The paper openly reports that image AUCs are "barely above the random baseline" (Section 6) and notes that GANs appear more private than diffusion models — even raising the question of whether this is real or reflects underdeveloped attacks (Section 7). This intellectual honesty is commendable.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Theorem 4.1 is based on an idealized assumption with limited practical connection.** The theorem assumes the generator distribution is exactly a convex combination of the training and reference distributions (G = βP + (1−β)T). This is a memorization-only model; no well-trained GAN behaves this way. The paper acknowledges this ("stronger assumption," "better viewed as showing why our Detector outperforms the random baseline" — line 84), but the gap between the assumption and practice is large enough that the theorem provides intuition at best, not formal support. This is not fatal — the paper is fundamentally empirical — but the theorem is decorative rather than substantive. The paper would be stronger if it either dropped the theorem or replaced it with a more general analysis.

2. **Number of experimental runs for image GANs is not specified.** The tabular experiments clearly state "11 training runs" (Section 5.2) and report AUC with standard deviation. For image experiments (Section 6), no such information is provided. Since the image AUCs are very close to 0.5, knowing the number of runs and variance is essential to gauge whether the reported low-FPR improvements are statistically reliable. This information may exist in the appendix (stripped by the parser) but should be stated in the main text.

3. **Modest overclaiming in the abstract for the image setting.** The abstract states that "adversaries can orchestrate non-trivial privacy attacks" across data types. On genomic data this is well-supported (10× random). On image data, the AUCs are 0.51–0.55 and TPRs are 0.02–0.06 at FPR~0.01. While statistically above random, calling this a "non-trivial privacy attack" in absolute terms (identifying ~1 in 50 training members at 1 in 200 false positives) overstates the practical threat. The paper's own body language is more measured ("AUCs that are barely above the random baseline" — line 147). The abstract and conclusion should more clearly differentiate the domain-dependent strength of the attack.

4. **Missing analysis of when detector attacks succeed or fail.** The paper observes that ADIS beats the raw Detector on some configurations but not others, and that Incept-MLP has the highest AUC but poor low-FPR performance on images (Section 6.2). These observations are stated but not probed. A brief analysis (e.g., by data dimensionality, degree of mode collapse, or GAN capacity) would strengthen the paper.

5. **The Eq. (1) Lipschitz bound is acknowledged as vacuous by the authors themselves.** The paper correctly notes (lines 72–73) that the bound is likely vacuous because Lip(f) can be large and W¹(G,T) can be large. This weakens the theoretical motivation for the detector attack's transfer from M to R. This isn't an error — the paper is transparent — but it means the only real justification for the attack's success is heuristic/empirical rather than formal.

### Trivial

- The abstract refers to "The Distinguisher" while Section 4.1 calls it "the Detector" — minor naming inconsistency.
- The claim in the Conclusion that the theorem "has applications across all privacy attacks on ML models, not just GANs" (line 170) is unsubstantiated speculation given the theorem's restrictive assumption.

## Nice-to-Haves

- A brief note on the computational cost of training the Detector (since the attacker must train a secondary network) would help practitioners assess practicality.
- A discussion of when the black-box model's requirement for "fresh samples from P" is realistic vs. problematic (e.g., for proprietary distributions). The paper mentions this can work with even a different public database (Section H in appendix) — this should be in the main text.
- Reporting variance of TPR across runs for image experiments (e.g., box plots at FPR=0.01) would strengthen the evidence.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the Lipschitz bound in Eq. (1) is vacuous.** The paper itself states this on lines 72–73 ("it doesn't tell us much... making Equation 1 vacuous"). The reviewer is repeating a limitation the authors already explicitly acknowledge. Removed as it reflects a misunderstanding of the paper's own self-awareness.
- **Criticism that Tables 3 and 6 are "not present in the provided text."** This is a parser artifact, not a paper flaw. The tables exist in the original submission.
- **Strength Finder's "Theorem 4.1 provides theoretical justification" as a core strength.** The theorem is acknowledged by the authors to rest on a strong assumption and is "better viewed as showing why our Detector outperforms the random baseline" (line 84). Presenting it as a "core strength" overstates its value. It is a minor theoretical contribution at best.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Recalibrate the language in the abstract and conclusion** to clearly differentiate the threat level across domains: strong evidence of meaningful privacy leakage on genomic tabular data (TPR up to 10× random at low FPR) versus weaker evidence on image data (2–6× random, but low absolute TPR values near 0.02–0.06).
2. **Specify the number of experimental runs for image experiments** in the main text (Section 6) and report variance (e.g., standard deviation or box plots of TPR at fixed FPRs).
3. **Either drop Theorem 4.1 or add a bridging argument** — the mixture assumption is so strong that the theorem offers little beyond the informal intuition that already motivates the attack. An alternative would be a simpler analysis based on overfitting (generator assigns higher density to training points) rather than the unrealistic mixture model.
4. **Add a brief analysis section** probing why ADIS outperforms the raw Detector on some configurations but not others, and why Incept-MLP has high AUC but poor low-FPR performance on images. Even a short paragraph of informed speculation would help.

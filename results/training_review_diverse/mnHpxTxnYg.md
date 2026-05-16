Now I have all the evidence needed to verify each reviewer claim against the paper. Here is the consolidated review.

---

## Summary

This paper studies black-box membership inference attacks (MIAs) against GANs, where the adversary only has sample access to the generator. It introduces detector-based attacks (Detector and its augmented variant ADIS) that train a classifier to distinguish GAN samples from reference samples, then use that classifier's confidence for membership inference. The paper provides theoretical motivation (Theorem 4.1) showing that under a mixture assumption, the Bayes-optimal detector yields the optimal MIA at any fixed FPR. The methods are evaluated on genomic tabular GANs (two architectures × six dataset configurations, with 11 independent runs) and on CIFAR-10 image GANs (four architectures).

## Strengths

- **Novel detector-based attack methodology with theoretical grounding**: The Detector and ADIS attacks are a clean, principled approach to black-box MIAs against GANs. Theorem 4.1 provides formal motivation: if the generator distribution is a mixture of the training and population distributions, thresholding the Bayes-optimal detector for distinguishing GAN samples from real samples yields the optimal MIA. The paper explicitly acknowledges the strength of this assumption (Section 4.1: "The assumption G is a simple mixture distribution is a stronger assumption, and Theorem 4.1 is better viewed as showing why our Detector outperforms the random baseline"), and still provides a clear link (via Lemma A.1 and Theorem 4.1) between the detection task and the membership inference task that goes beyond heuristic intuition.

- **Thorough genomic experiments with statistical rigor**: The genomic tabular experiments are well-executed. Results are averaged over 11 independent training runs (line 118, line 133) with standard deviations reported. Seven attack methods are compared across two GAN architectures (Vanilla GAN, WGAN-GP), three feature dimensions (805, 5K, 10K), and two real genomic databases (1000 Genomes, dbGaP). ADIS achieves TPRs up to 10× the random baseline at low FPRs (Table 3, Section 5.2). The choice of Hamming distance over Euclidean is empirically justified. The honest presentation of modest AUCs (0.55–0.7) as "lower privacy leakage than white-box or diffusion model attacks" (Section 5.2) is appropriate.

- **ADIS — a practical combination of detection and distance-based features**: The Augmented Detector (ADIS) augments the detector's input with distance-based statistics and the DOMIAS likelihood ratio (Section 4.1), and consistently outperforms individual methods across genomic settings (especially on WGAN-GP). This is a useful methodological contribution that practitioners can adopt.

- **Best-practice evaluation metrics**: The paper adopts log-log ROC curves and reports TPR at fixed low FPRs (0.001, 0.005, 0.01, 0.1) as recommended by Carlini et al. (2021), rather than relying on overall accuracy or AUC alone. This is a meaningful improvement over prior GAN privacy work.

## Weaknesses

### Fatal
None.

### Major

- **Image GAN experiments lack multiple independent runs and variance estimates.** The genomic experiments are explicitly run over 11 independent training runs with standard deviations (Section 5.2, line 118, Figure 1 legend). For the image experiments (Section 6), no mention of multiple runs is made. The ROC curves in Figure 2 lack error bars or confidence intervals. Since the reported AUCs are barely above 0.5 (Table 3, line 147: "AUCs that are barely above the random baseline"), and the core claim is that detector attacks achieve TPRs "2–6× higher than the random baseline" at low FPRs, single-run results could be dominated by noise. This is an **evidential gap**: the claim about image GANs may be correct, but the current evidence is insufficiently robust to be persuasive. This does not undermine the genomic results, which stand on their own.

### Minor

- **Indirect comparison to Hayes et al. (2019) leaves the source of improvement unclear.** The paper correctly notes (Section 2) that Hayes et al. previously trained a classifier to distinguish GAN samples from test samples and concluded the attack failed. The paper attributes its different conclusion to (i) genomic data, (ii) ADIS augmentation, and (iii) log-log ROC evaluation. However, without directly reproducing the Hayes et al. attack in the same settings (e.g., training the detector without ADIS and evaluating via accuracy vs. log-log ROC on the same data), it is hard to cleanly attribute the improvement to any specific factor. A head-to-head comparison would substantially strengthen the paper's claim of advancing beyond Hayes et al.

- **Theorem 4.1 provides intuition, but its practical relevance is limited by the strong mixture assumption.** The paper is transparent about this (Section 4.1), but the gap between the assumption (G is a clean mixture of training and population distributions) and reality (GANs only approximate the training distribution in complex ways) means the theorem does not directly predict the detector's performance in realistic settings. Together with Lemma A.1's Lipschitz-dependent bound (which the paper notes can be vacuous), the theoretical contribution is more motivational than predictive. The paper would benefit from a clearer statement of what the theory does and does not guarantee.

### Trivial

- **Inconsistent naming**: The abstract refers to "The Distinguisher" (line 4), while the body consistently uses "Detector" (Section 4.1). This should be harmonized.

## Nice-to-Haves

- **Add multiple independent runs for all image experiments** (5–10 seeds) and report mean AUC with standard deviations and confidence intervals on TPR at low FPRs. This is the single change that would most strengthen the paper.
- **Directly compare the Detector to the Hayes et al. (2019) classifier attack** on the same data and evaluation metrics to isolate the effect of log-log ROC evaluation from the attack design.
- **Brief discussion of computational cost**: Training a detector network adds overhead vs. distance-based attacks; a note on training time would help practitioners choose methods.
- **Analysis of what the detector learns**: An ablation or visualization (e.g., t-SNE of detector features with member/non-member labels) could strengthen intuition.
- **Brief mention of DP-GAN results in the main text** rather than only in the appendix, even as a short qualitative summary.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Theorem 4.1 weakness overstated** (from Harsh Critic's Critical Issue 3): The reviewer claimed the theorem "rests on an assumption not satisfied in practice." The paper explicitly acknowledges this limitation (Section 4.1, line 84: "The assumption G is a simple mixture distribution is a stronger assumption, and Theorem 4.1 is better viewed as showing why our Detector outperforms the random baseline"). The authors are transparent about the scope of the theoretical claim; this is properly scoped, not a weakness.
2. **"Missing related work on other black-box attacks"** (from Harsh Critic's Section-by-Section Notes): The paper covers the most relevant prior work (Hayes et al. 2019, Chen et al. 2020, van Breugel et al. 2023b, Hilprecht et al. 2019, Homer et al. 2008a). The suggestion of "loss-based attacks adapted to GANs without discriminator access via synthetic data likelihood estimation" is too vague to constitute a missing reference, and the paper cannot be faulted for not covering unspecified methods.
3. **"Proof sketch of Theorem 4.1 missing from main text"** (from Harsh Critic's Strengthening section): Rules state that missing appendix content should not be flagged — the parser strips these sections from the submission, and the proof exists in the original.
4. **Strength about "Careful attention to replication with multiple training runs"** (from Strength Finder point 6): This strength is accurate for the genomic experiments but does not hold for the image experiments (see Major weakness above). I have kept it as a genomic-specific strength, but its generality is qualified by the verified weakness.

## Novel Insights

The reviews surface two insights beyond the paper's own contributions. First, the disconnect between the rigorous genomic experiments (11 runs, std devs) and the single-run image experiments is unusual and suggests either that the authors encountered a resource constraint or that the image results are preliminary. Either way, this asymmetry in rigor is itself informative for reviewers assessing the paper's maturity. Second, the paper's honest reporting of modest AUCs (0.55–0.7) and its framing that GANs appear more private than diffusion models raises an interesting meta-question: are GANs genuinely more private, or have we simply not developed the right attacks yet? The paper explicitly flags this as future work, which is refreshingly candid.

## Suggestions

1. **Run the image experiments over at least 5 independent seeds** and report mean AUC ± std and confidence intervals on TPR at low FPRs. If a single GAN training is too expensive for multiple runs, consider sub-sampling the data or using fewer architecture variants to make replication feasible.
2. **Include a direct comparison to Hayes et al. (2019) in a single table or figure**: train a detector without ADIS augmentation, evaluate via both accuracy (their metric) and log-log ROC (your metric), on both genomic and image data. This cleanly separates the contribution of evaluation methodology from the attack design.
3. **Harmonize "The Distinguisher" (abstract) with "Detector" (body).**
4. **Add a 1–2 sentence computational cost note** in Section 5 or 6 (e.g., "Detector training adds roughly X minutes per run; distance-based attacks require only nearest-neighbor search at test time.").

## Score and Decision

This paper makes a genuine empirical contribution to understanding black-box privacy leakage from GANs. The genomic experiments are carefully designed and convincingly demonstrate that detector-based attacks achieve non-trivial TPR at low FPRs. The ADIS method and theoretical framing are valuable additions. The main weakness — lack of multiple runs for image experiments — is a significant evidential gap for the image-domain claims, but it is fixable in revision and does not invalidate the core contribution (the genomic results stand independently). The paper is honest about its limitations and uses best-practice evaluation metrics. I recommend acceptance after the authors address the image experiment reproducibility issue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
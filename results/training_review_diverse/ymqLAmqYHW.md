Now I have a thorough understanding of the paper and verified every claim. Let me write the consolidated review.

## Summary

This paper introduces the Key-Locks (K&L) backdoor attack, which proposes to reduce the "binding" between backdoor triggers and model parameters by embedding generic "locks" during training and generating per-instance "keys" via gradient descent at inference time. The paper evaluates K&L against six baseline attacks and eight defense methods across four datasets and four architectures. Its core empirical claim is that K&L is the only method that consistently penetrates all defenses tested, with strong evidence from Table 1.

## Strengths

- **Consistent penetration of all eight tested defenses across multiple datasets and architectures.** Table 1 shows K&L is the only attack among six baselines to achieve high ASR under ANP, BNP, FP, FT, I-BAU, NAD, CLP, and RNP simultaneously on CIFAR-10, CIFAR-100, GTSRB, and Tiny ImageNet using PreActResNet18. For example, on CIFAR-10 under ANP, K&L achieves 71.59% ASR while the next best method is under 10%; on Tiny ImageNet under RNP, K&L achieves 99.92% ASR. This comprehensive empirical coverage directly supports the paper's central claim.

- **Quantitative stealth evidence via attribution similarity.** Table 2 reports cosine similarity of BIG attribution maps between original and backdoored images; K&L achieves 0.9932, the highest among all methods, indicating minimal semantic disruption. Figure 4 shows K&L's STRIP entropy distribution nearly completely overlaps with clean samples.

- **Novel conceptual framework for decoupling backdoors from model parameters.** The idea of embedding generic "locks" during training and computing per-instance "keys" at inference time is a principled departure from fixed-trigger and generator-based attacks. The adjustable "level" parameter controlling perturbation vs. attack strength is a useful design knob.

## Weaknesses

### Fatal
None.

### Major

- **The "Embedding Locks" training phase is underspecified.**
  The paper references an "Embedding Locks process" (line 85) and mentions "locks loss" and "maintain loss" (Section 3.3.2) by name, but never provides a clear mathematical formulation for the training-phase losses that distinguish K&L from a standard backdoor. The closest specification is Eq. 7 in Section 3.4 (a generic dual-objective $L(x,y;W) + \lambda L(x',c_t;W)$), but the paper does not explicitly identify this as the Embedding Locks objective, nor does it specify how $x'$ (the trigger-embedded input) is constructed during the training phase. The reader cannot determine what the training procedure actually does differently from, say, BadNet or Blended. This is the paper's central technical contribution, and it is not reproducibly specified.

- **The proposed AAC/AAV metric is never defined.**
  The paper lists "introducing a new metric: the Accuracy-ASR Curve (AAC)" as a core contribution (line 30), and reports AAV values corresponding to AAC1, AAC3, AAC5 in Table 3 and Figure 3. However, the paper never states what AAC stands for beyond the name, how it is computed, what AAV means, or what the numeric thresholds (AAC1, AAC3, AAC5) represent. Without a definition, these results are uninterpretable and the claimed contribution is vacuous.

- **The ablation study is promised but results are absent.**
  Section 4.3 begins by describing four parameters (epochs, learning rate, level, attack step size) and their default settings, then the text transitions directly to the Conclusion (line 184) with no ablation results presented. The actual effect of these parameters on BA/ASR — which would directly support robustness claims — is simply not reported. The Strength Finder's assertion that this section "shows that the method maintains high BA and ASR across varied settings" is false; no such results appear in the extracted paper.

- **The core conceptual claim of "decoupling" is argued qualitatively, not demonstrated quantitatively.**
  The paper claims that K&L reduces "high binding" between trigger and model parameters, making it resistant to defenses. However, no experiment directly measures binding (e.g., showing that ASR degrades more gracefully under weight perturbation for K&L than for baselines). The key generation (Eqs. 5–6) uses the model's own parameters via gradient descent, and the "locks" reside in the model weights — the paper acknowledges this (Section 3.3.2, Property (b)). The argument that multiple locks in OOD space make defense impossible is asserted but not formalized or tested. The empirical results in Table 1 are strong, but they demonstrate *effectiveness*, not the *mechanism* of decoupling. A direct experiment comparing sensitivity to weight perturbations would substantiate the paper's central narrative.

### Minor

- **The three "requirements" for backdoor attacks are standard properties described as a contribution.** The paper states it "first systematically delineate[s] three requirements" (line 11), but these are well-known properties of backdoor attacks (stealth, efficacy, normal behavior on clean data). This is a minor overclaim rather than a substantive flaw.

- **STRIP analysis is only qualitative.** Figure 4 shows overlapping distributions between K&L and clean samples, but the paper does not quantify the overlap (e.g., with a detection rate or AUC). The visual claim is suggestive but not conclusive.

- **No perturbation magnitude reported.** The paper claims "minimal perturbation" (Property (a), line 106) and the level parameter controls perturbation budget, but average L2 or Linf distortion for K&L-generated samples is never reported. Table 2 only reports attribution similarity, which is an indirect measure.

- **Inference cost is acknowledged but not quantified.** Section 5 notes that K&L "increases the demands of computing resources," but per-instance gradient descent at inference time could be orders of magnitude slower than fixed-trigger or generator-based attacks. This is a practical limitation worth quantifying.

### Trivial
- Bold entries in Table 1 are said to indicate "successful attack," but the criterion for success (ASR above a threshold? BA preserved?) is not explicitly stated.
- The paper claims K&L "penetrates nearly all existing backdoor defense mechanisms" but tests only 8 defenses. The claim should be scoped to the defenses evaluated.

## Nice-to-Haves
- Including additional defenses beyond the 8 tested (e.g., Neural Cleanse, spectral signatures, activation clustering) would strengthen the "nearly all" claim.
- A pseudocode or algorithm box summarizing the two-phase training/inference procedure would significantly improve clarity.
- Reporting results for the other architectures (VGG19, MobileNet, EfficientNet) beyond PreActResNet18 in the main text or supplement would demonstrate generality.

## Removed Points
These points are flagged to be removed; treat them with caution:
- *"The three requirements are not leveraged by the method"* — The paper does connect requirements to method analysis in Section 3.3.2, even if the connection is qualitative.
- *"FT is trivially defeated by many attacks"* — Fine-tuning is a standard defense baseline in the backdoor literature; including it is standard practice, not inflating results.
- *"Table 1 only for PreActResNet18"* — The paper explicitly acknowledges this is due to space constraints and that other architectures were tested.
- *Strength Finder's claim that "ablation study demonstrates parameter robustness"* — This directly contradicts verified fact: no ablation results appear in the paper. Removed as factually incorrect.
- *"Decoupling is illusory because keys use model parameters"* — This overstates the case. The paper's claim is about storing backdoor *details* in the key rather than the model, which differs from requiring zero model involvement. The paper acknowledges gradient descent uses model parameters (Section 3.3.2). The concern is valid but the criticism as phrased is a mischaracterization.
- *"Missing Section 3.2 content"* — This could be a parser artifact; I cannot verify whether Section 3.2 originally contained content.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a novel perspective not already present in the paper or obvious from its framing.

## Suggestions
1. **Formally specify the Embedding Locks training objective.** Write down the exact loss functions for "locks loss" and "maintain loss" with clear notation for how poisoned samples are constructed during training. This is essential for reproducibility and is the paper's core algorithmic contribution.
2. **Define AAC and AAV clearly.** State how the Accuracy-ASR Curve is computed, what AAV stands for, and what AAC1/AAC3/AAC5 thresholds mean. Without this, the metric is meaningless.
3. **Add the missing ablation results.** The ablation study setup is described but no results follow. Even a brief table or figure summarizing the effect of the four parameters on BA/ASR is necessary.
4. **Add a direct binding measurement experiment.** Show that K&L's ASR degrades more gracefully than baseline attacks' ASR under increasing weight perturbation (pruning, noise, fine-tuning). This would directly substantiate the decoupling claim rather than relying on qualitative reasoning.
5. **Report average perturbation norms (L2/Linf)** for K&L-generated samples to support the "minimal perturbation" claim.
6. **Quantify inference cost** — report the average number of gradient steps and wall-clock time per sample for key generation — and discuss the practical limitations this imposes.

## Score and Decision

The paper presents a novel backdoor attack with impressive empirical results (Table 1). K&L is genuinely the only method among those tested that penetrates all 8 defenses, and the attribution similarity results support its stealth claim. These are real contributions.

However, the paper suffers from serious presentation and specification issues that prevent it from being accepted in its current form: (a) the core training-phase algorithm (Embedding Locks) is underspecified — key loss functions are named but not written down; (b) a proposed metric (AAC/AAV) listed as a contribution is never defined; (c) the ablation study is promised but results are absent; and (d) the central theoretical claim (decoupling/binding reduction) lacks direct experimental support, relying on qualitative argumentation. These issues collectively undermine reproducibility and verifiability of the stated contributions.

The paper has a solid empirical core and promising ideas, but it is not yet ready for publication. A major revision that formalizes the method, provides missing definitions and experiments, and scopes claims appropriately would merit strong reconsideration.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
Now I have thoroughly read the paper and verified the reviewer claims against the actual text. Let me compose the final consolidated review.

---

## Summary

This paper makes two contributions: (1) it systematically studies client-side detectability of malicious server (MS) attacks in federated learning, demonstrating that both boosted analytical and example disaggregation attacks are detectable via principled checks (introducing D-SNR for gradient-space detection), and (2) it proposes **SEAL**, a novel attack framework that avoids these detection vectors by jointly training a shared model with a secret decoder using SGD on auxiliary data. SEAL is evaluated on CIFAR10/100 (batch sizes up to 512) and ImageNet (B=64), achieving high reconstruction quality, and is shown to work under secure aggregation — settings where prior honest and malicious attacks fail or are detectable.

## Strengths

1. **Novel attack paradigm that breaks from lifting honest attacks** (backed by §4, Algorithm 1). SEAL is genuinely different from prior MS attacks: instead of using handcrafted model modifications to enable honest attack methods, it trains a secret decoder end-to-end with the shared model. This design lets SEAL disaggregate data in a hidden space (§4, Eq. 2), avoiding the gradient-space detection signal that plagues example disaggregation attacks, while also avoiding weight-space-detectable handcrafted modifications (since all weights are SGD-trained).

2. **Introduction of D-SNR as a principled detection metric** (backed by §3, Eq. 1, Fig. 1). D-SNR provides a simple, computationally cheap way to detect when a single example dominates a batch gradient — the necessary condition for example disaggregation attacks. The paper empirically shows that successful attacks (Fishing variants) always produce pathologically high D-SNR values, while non-malicious networks exhibit low values. This is a useful contribution beyond the paper's core attack, as it can serve as a client-side vulnerability warning.

3. **Local property selection via batch normalization significantly improves success probability** (backed by §4.1, Table 1). By selecting properties relative to the in-batch distribution (enabled by BN's intertwining of batch computation), SEAL achieves P(|I_rec|=1) > 0.9 for batches up to 512, a dramatic improvement over the 1/e ≈ 37% bound of the global setting used in prior work. This is a theoretically grounded and practically impactful innovation.

4. **Strong empirical results across datasets, batch sizes, and secure aggregation** (backed by §5, Tables 1-3). SEAL achieves up to 98.6% successful batches on CIFAR10/100 with PSNR up to 30, and 82.1% success on ImageNet with PSNR-All of 21.9 (outperforming Fishing on ImageNet). Under secure aggregation (C=4,8), it maintains PSNR > 25, demonstrating the first effective MS attack in this challenging setting.

5. **Identification that secure aggregation with BN is not equivalent to a large batch from one client** (backed by §4.1). This observation, overlooked in prior work, correctly identifies why secure aggregation requires a different attack design and motivates SEAL's combined local/global property approach.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Detection claims rely more on design principles than direct adversarial testing.** The paper argues SEAL avoids weight-space detection (SGD-trained weights vs. handcrafted modifications) and gradient-space detection (low D-SNR in Fig. 1). Both arguments are logically sound and supported by evidence of what SEAL *avoids*, but the paper never directly tests SEAL against a motivated defender who employs a *battery* of detection checks (e.g., weight statistic outlier detection, gradient norm analysis, behavioral tests on known benign inputs). For a paper whose positioning hinges on being "harder to detect," this gap weakens what is otherwise a convincing empirical story. Adding a detection game experiment (defender distinguishing SEAL models from natural models using multiple checks, with ROC curves) would substantially strengthen the central claim.

2. **No unified empirical comparison to prior MS attacks under identical settings.** The paper compares to Fishing only on ImageNet (claiming higher PSNR, §5) and defers additional comparison to the appendix, but there is no comprehensive benchmark table showing Fishing, CAH, Mandrake, and RTF alongside SEAL on the same architectures (ResNet18), datasets (CIFAR10/100), and batch sizes. Such a comparison would allow readers to assess whether SEAL sacrifices reconstruction quality for its detectability advantages. Given the paper's framing that prior attacks are "detectable" while SEAL is not, understanding the reconstruction trade-off is important for assessing practical threat.

3. **The claim that D-SNR captures a "fundamental limitation of all (current and future) example disaggregation attacks"** (§3) is an overstatement. The paper provides compelling empirical evidence for existing attacks (Fig. 1) but no theoretical proof that successful example disaggregation *must* produce high D-SNR in a linear layer. While the restriction to linear layers covers 98% of ResNet18 weights, this is architecture-specific, and the possibility of attacks that disaggregate through non-linear layers or carefully distribute gradient dominance across layers is neither ruled out theoretically nor explored experimentally. The paper would benefit from hedging this claim.

4. **Weight-space detection is argued but not empirically verified.** The paper states SEAL "evades weight space detection" (§4) because it trains weights via SGD rather than handcrafting modifications. This is a valid logical argument against the *specific* detection vectors of prior attacks (e.g., convolutions with single nonzero entries), but it does not empirically rule out that SGD-trained malicious weights might exhibit other statistical anomalies (e.g., unusual kernel norms, singular value distributions) that a sufficiently sophisticated defender could detect. An experiment comparing weight statistics of SEAL-trained models to naturally trained models would address this.

### Trivial
- PSNR-Top (top 37% of batches) is defined to facilitate comparison between large-batch and secure aggregation settings, but the choice of 37% (= 1/e) conflates two distinct phenomena: the probability a single image satisfies the property (P(|I_rec|=1)) and the reconstruction quality conditioned on having a property-matching image. Clarifying this interpretation would improve readability.

## Nice-to-Haves
- A detection game experiment where a defender uses multiple checks to classify batches as coming from SEAL vs. natural models would strengthen the paper's most central positioning claim.
- Failure case analysis (visualizing batches where SEAL fails to reconstruct) would help understand boundary conditions.
- An ablation isolating the contribution of joint training of $f$ vs. training only $d$ and $r$ with a fixed $f$ would clarify the importance of controlling the gradient encoding.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism about secure aggregation results contradicting theory** (from Harsh Critic point 2). The reviewer claimed Rec > 1/e contradicts P(|I_rec|=1) → 1/e. This is a misunderstanding: **Rec** (fraction of batches with PSNR > 19) is *not* the same as **P(|I_rec|=1)** (probability exactly one image satisfies the property). SEAL can reconstruct successfully even when multiple images satisfy the property, explaining empirically higher Rec. The paper explicitly defines these as separate metrics (line 247-249) and offers plausible explanations. **Removed: factually wrong.**

2. **Sub-criticism about "we see no clear ways to detect it currently" being "a statement of ignorance rather than evidence"** (Harsh Critic point 1, third bullet). This is an overly harsh characterization of a transparent and reasonable acknowledgment of limitations in the Outlook section (§6). The paper's detection claims are supported by D-SNR evidence and design arguments elsewhere; this sentence does not undermine them. **Removed: unfair characterization.**

3. **Sub-criticism that secure aggregation mechanism is deferred to "unavailable" appendix** (Harsh Critic point 2). The hard rule states to remove weaknesses about missing appendix content, as the parsing/stripping process removes appendix sections that exist in the original submission. **Removed: per instructions.**

4. **Criticism that D-SNR only tested against one detection check** (Harsh Critic point 1, second bullet, about "a battery of checks"). This is partially addressed as Weakness 1 above, but the reviewer's framing that the paper only tests D-SNR "a metric the attacker knows and can optimize against" is somewhat unfair — the whole point of D-SNR is that it measures a *necessary* condition for disaggregation, not a heuristic the attacker could easily fool. Retained as the milder Weakness 1 above.

## Novel Insights

An interesting meta-point emerges from the interplay of the two contributions: the paper shows that *any* attack that lifts honest optimization methods via example disaggregation is detectable (because disaggregation is equally visible to the client). This means the common approach of "make a malicious model to create a single-example gradient, then run an optimizer" is fundamentally insecure once the principle is known. SEAL's innovation is to collapse the two-step process (malicious modification → honest attack) into a single end-to-end learned system where disaggregation happens in a secret lower-dimensional space the client never sees. This shifts the detectability question from "is there a gradient-space anomaly?" to "are the model weights suspicious?" — and the paper's answer (SGD-trained weights without handcrafted patterns) is plausible but less rigorously tested. The paper thus reveals an interesting asymmetry: gradient-space detection is "principled" (attackers provably cannot avoid it if they rely on example disaggregation), while weight-space detection is "heuristic" (there is no proof that malicious SGD-trained weights are indistinguishable from benign ones). This asymmetry deserves more explicit discussion in the paper.

## Suggestions

1. Add a detection game experiment: train a binary classifier (or use simple statistical tests) on weight statistics (kernel norms, activation statistics, singular value distributions) to distinguish SEAL-trained models from naturally trained models of the same architecture on the same data. Report AUC/ROC. This would directly test the weight-space detectability claim.

2. Add a unified comparison table in the main paper (not appendix): run Fishing, Mandrake, and/or CAH on ResNet18 with CIFAR10 under the same batch sizes used in Table 1, and report PSNR and Rec. This would let readers assess the reconstruction quality trade-off.

3. Tone down or qualify the claim about D-SNR detecting "all future" example disaggregation attacks. Replace with "all known attacks from this class" or add a caveat about the linear layer restriction.

4. Include a brief failure analysis: show 3-5 examples where SEAL produces low-PSNR reconstructions, and discuss whether these correspond to cases where |I_rec| ≠ 1, poor training convergence, or other factors.

5. Clarify in the main text that P(|I_rec|=1) and Rec measure different things, to prevent the confusion evident in multiple reviewer readings.

## Score and Decision

Based on my assessment: the paper makes a genuinely novel contribution (a new attack paradigm for FL data stealing) with solid empirical results. The weaknesses are about incomplete validation of some claims rather than fundamental flaws. The detection claims are partially supported and could be strengthened with additional experiments, but the core technical contribution (SEAL framework, local properties, D-SNR metric) is sound and novel. The paper opens a new direction in MS attack design by breaking the pattern of lifting honest attacks.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
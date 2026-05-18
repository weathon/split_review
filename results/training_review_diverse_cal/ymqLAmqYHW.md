Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper identifies a "high binding" problem in existing backdoor attacks — the tight coupling between triggers and model parameters that makes them vulnerable to defenses — and proposes Key-Locks (K&L), which decouples the attack into an "embedding locks" training phase and a "key generation" inference phase. The K&L attack generates backdoor samples at inference time via gradient descent through the trained model, controlled by a "level" parameter that trades off perturbation size against attack success. Experiments across four datasets and eight defense mechanisms show K&L is the only method tested that achieves non-trivial attack success rates under all defenses, with strong stealth evidence from attribution visualization and STRIP entropy distributions.

## Strengths

- **Novel decoupling of backdoor triggers from model parameters to evade defenses.** The paper clearly identifies the "high binding" limitation (Section 1, Figure 1) and proposes a lock-and-key mechanism that separates the trigger generation process from the stored model parameters. This is a conceptually grounded advance over both fixed-trigger and input-dependent attacks that store backdoor information directly in model weights.

- **Superior empirical penetration of all eight tested defenses.** Table 1 demonstrates that K&L is the only attack method achieving successful attack success rates (bold entries) under every defense algorithm (ANP, BNP, FP, FT, I-BAU, NAD, CLP, RNP) across CIFAR-10, CIFAR-100, GTSRB, and Tiny ImageNet. Other methods (BadNet, Blended, Input-Aware, SSBA, WaNet, BppAttack) fail on at least one defense. This is the paper's strongest empirical claim and is well-supported.

- **Quantitative and qualitative stealth evidence.** Attribution visualization (Figure 2) and cosine similarity measurements (Table 2) show K&L samples retain higher attribution-map similarity to original images than competing attacks. The STRIP entropy analysis (Figure 4) shows K&L's backdoor samples have nearly overlapping distributions with clean data across all four datasets, while other attacks produce clearly separable distributions. These provide convergent evidence of stealth.

- **Systematic framing of three explicit requirements for successful backdoor attacks.** The paper formalizes Requirements 1–3 (semantic preservation, efficacy, normal operation without trigger) in Section 1 and uses them to ground the analysis of why high binding creates defense vulnerabilities. This framing provides a principled lens for the method design.

## Weaknesses

### Fatal
None. The paper's core claims (K&L penetrates defenses, is stealthy) are supported by the experimental evidence presented, even though some aspects of the method and metrics are incompletely defined.

### Major

- **The "Embedding Locks" process is not formally specified.** The paper's central contribution — how locks are embedded into model parameters — is described only at a conceptual level. Section 3.3.1 begins with "Following the Embedding Locks process, we obtain new model parameters W′" but never defines this process. The terms "locks loss" and "maintain loss" are used repeatedly (Sections 3.3.1–3.3.2) but are never formally introduced as specific loss terms in any equation. Section 3.4 presents a dual-objective optimization (Eq. 7: W* = arg min L(x,y;W) + λL(x′,c_t;W)) in the context of differentiating K&L from adversarial attacks, but the paper never explicitly states that this formula *is* the Embedding Locks process or which term corresponds to "locks loss" vs "maintain loss." A reader cannot determine from the text alone what makes the locks embedding different from standard backdoor training. The provided code partially mitigates this, but the methodological exposition is incomplete as a scientific contribution.

- **The AAC metric is claimed as a contribution but never defined.** The Accuracy-ASR Curve (AAC) is listed as a contribution in Section 1 and referenced in the experimental section (line 138, Table 3, Figure 3), but its construction is never specified: what are the axes? How is the curve parameterized? What do AAC1, AAC3, and AAC5 mean? How is the area computed? Additionally, the acronym "AAV" appears in line 166 ("Table 3 shows the AAV corresponding to the AAC") but is never defined. Table 3 and Figure 3 are therefore uninterpretable. A claimed contribution must be formally defined to be evaluated.

- **Ablation study setup is described but no results are reported.** Section 4.3 specifies the four parameters under study (epochs, learning rate, level, attack step size) and the default settings, but the section ends without presenting any ablation results, figures, or tables. This is a critical omission because the ablation would help validate that the "level" parameter actually controls the attack–stealth trade-off as claimed, and would demonstrate that the method is robust to hyperparameter choices.

### Minor

- **The "nearly all existing backdoor defense mechanisms" claim overstates the scope.** The paper tests 8 defense algorithms. While this is a reasonable and competitive set, the phrasing "nearly all" is hyperbolic — many other defenses exist (e.g., spectral signatures, activation clustering, neural cleanse, ABS). The paper should either qualify the scope or use more precise language.

- **The STRIP analysis (Figure 4) is purely qualitative.** The paper claims STRIP cannot distinguish K&L from clean samples but provides only visual overlap in entropy histograms. Quantitative measures (e.g., KL divergence, AUC of a STRIP-based detector) would substantially strengthen this claim.

- **Cosine similarity measurements in Table 2 lack a clean-vs-clean baseline.** The paper reports cosine similarity between attacked and original attribution maps for each method, showing K&L has the highest similarity. Without a reference value (e.g., clean image vs. itself or clean vs. clean with legal perturbations), the absolute magnitudes are hard to interpret. A clean-self baseline would calibrate the scale.

- **"High binding" is described conceptually but not formally quantified.** The paper relies on an intuitive geometric picture (Figure 1) and qualitative description. While this is acceptable for a conceptual contribution, a formal measure of binding would strengthen the claim that K&L dissolves it.

### Trivial

None worth listing beyond what is addressed above.

## Nice-to-Haves

- A pseudocode algorithm for the full K&L pipeline (locks embedding + key generation) would make the method self-contained and improve reproducibility beyond the provided code.
- Results on additional architectures beyond PreActResNet18 (the paper mentions VGG19-BN, MobileNet-v3, EfficientNet-B3 but defers them due to space) would strengthen generality, but this is scope-extension rather than a flaw.
- A formal definition of "high binding" (e.g., measuring how much the attack success rate degrades under parameter perturbation) could be used to quantitatively validate the paper's central claim about dissolving binding.

## Removed Points

These points were flagged by reviewers but removed or downgraded for the reasons stated below. Treat with caution if citing.

- **"Section 3.2 is missing / properties (a)(b)(c) were never presented."** The paper's text (line 78) shows the heading "3.2 RESEARCH PROBLEM" with content that was stripped by the parser; Section 3.3.2 explicitly references "the three properties discussed in Section 3.2" and analyzes each one. This is a parser artifact, not an author omission. **Removed per Hard Rules: parser-stripped content.**

- **"The core method is not described at all / the paper's central claim is unverifiable."** This overstates the problem. The method is partially described: the key generation via gradient descent (Section 3.3.1), the level parameter (Eq. with ε^l), and the dual-objective optimization (Section 3.4) are all presented. The gap is in the formal specification of locks embedding, not in the entire method. Downgraded from "fatal/unverifiable" to Major.

- **"Grammatical errors and unclear phrasings (e.g., 'causing it for incorrect results')."** These are parser artifacts from PDF extraction, not author errors. **Removed per Hard Rules: formatting/parser artifacts.**

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an insight that the paper itself does not already present.

## Suggestions

1. **Complete the method description.** Formally define the Embedding Locks process: specify the loss terms (locks loss, maintain loss), the full optimization objective, and how it differs from standard backdoor training. A clear equation or algorithm box for the lock-embedding phase would resolve the central ambiguity.

2. **Define the AAC metric explicitly.** State how the Accuracy-ASR Curve is constructed (parameterization, axes, area computation) and define AAC1/AAC3/AAC5. Define "AAV" or use consistent terminology. Without this, a claimed contribution cannot be evaluated.

3. **Report the ablation study results.** Add a table or figure showing the effect of each parameter (epochs, learning rate, level, attack step size) on ASR and BA. This is existing work that simply needs to be included.

4. **Add quantitative STRIP analysis.** Report a metric such as AUC of STRIP-based detection or KL divergence between clean and backdoored entropy distributions to support the qualitative claim that STRIP cannot distinguish K&L samples.

5. **Add a clean-vs-clean baseline to Table 2.** This would calibrate the cosine similarity values (e.g., clean image against itself should be 1.0) and make the comparison across methods more interpretable.

6. **Replace "nearly all" with more precise scope language** regarding the defense coverage.

## Score and Decision

The paper tackles a well-motivated problem with a conceptually novel approach, and the main experimental results (Table 1) are genuinely impressive — K&L outperforms all baselines by a wide margin across every defense. However, the paper in its current form has three significant gaps that prevent acceptance: the core method (Embedding Locks) is not formally specified, the AAC metric claimed as a contribution is never defined, and the ablation study (Section 4.3) contains only setup with no results. These are not fatal to the underlying work — the concept is clear, code is provided, and the main results are compelling — but they render the paper's scientific contribution incompletely presented. With major revision to address these gaps, this could be a strong paper. In its current form, it falls short of the completeness standard required for acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
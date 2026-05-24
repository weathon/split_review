Now I have all the information needed. Let me construct the consolidated review.

---

## Summary

TrojFair introduces a Trojan attack framework that targets fairness by embedding group-specific triggers. It comprises three modules: target-group poisoning (injects triggers into target-group samples with label flipping), non-target group anti-poisoning (attaches the same trigger to non-target samples while preserving labels to desensitize them), and fairness-attack transferable optimization (bi-level optimization on a surrogate model to amplify group accuracy disparities). The attack achieves high target-group ASR (≥88.77%), low non-target ASR, and near-identical fairness metrics on clean data across three datasets and multiple architectures.

## Strengths

1. **Strong empirical attack performance across diverse settings.** Table 1 shows T-ASR ≥ 88.77% across ISIC, Fitzpatrick17k, and FairFace with both ResNet and ViT backends, while clean accuracy drops ≤1.1% and clean-input bias (CBias) remains near the clean model's baseline bias (e.g., 0.99% vs. 0.96% for FairFace/ResNet-18). This directly supports the claimed combination of effectiveness and stealthiness.

2. **Ablation study cleanly isolates the contribution of each module.** Table 2 shows a clear decomposition: target-group poison alone yields PBias of only 1.22%; adding anti-poisoning raises it to 38.69%; adding transferable optimization further increases it to 49.63%. This empirically validates the necessity of all three components and is the strongest part of the experimental section.

3. **Effectiveness at low poisoning ratios and with diverse trigger types.** Table 4 shows that even at 1% poisoning, TrojFair achieves 87.55% T-ASR and 28.75% PBias. Table 5 shows that both patch-based and blended global triggers work, with the blended trigger achieving 69.13% PBias. This demonstrates resource efficiency and flexibility.

4. **Transferability across related CNN architectures.** Table 3 shows that a trigger optimized on ResNet-18 transfers to ResNet-34, VGG16-BN, and VGG19-BN, maintaining T-ASR ≥ 93.66% and PBias ≥ 44.03%. This provides partial support for model-agnostic operation.

## Weaknesses

### Fatal

None.

### Major

1. **No quantitative comparison to prior fairness attacks.** The paper's introduction and related work explicitly criticize prior fairness attacks (Solans et al., Jagielski et al., van et al.) as suffering from >10% accuracy drops and ~26% target ASR, positioning TrojFair as an improvement. However, the experimental section contains zero apples-to-apples comparisons against these methods on the same datasets, models, and poisoning ratios. Without this, the paper's central narrative of "improving upon" prior work is unsubstantiated. The paper reads as a strong ablation study of TrojFair rather than a paper demonstrating advancement over the state of the art. (See lines 15–16, 48–49 vs. Tables 1–5.)

2. **No empirical evaluation against standard backdoor detectors to support the stealthiness claim.** The abstract, introduction, and conclusion assert that TrojFair is resilient to conventional backdoor detectors (Neural Cleanse, ABS). However, Section 6 only tests a *modified group-aware variant* of Neural Cleanse designed by the authors, which achieves only 50–60% detection accuracy. The paper does not run Neural Cleanse, ABS, STRIP, or any other standard detector in their original form against TrojFair. The claim that existing tools "cannot detect" or "struggle to detect" TrojFair (lines 17, 342, 351) is therefore asserted without direct evidence. (See lines 17, 342–344 vs. Table 6.)

### Minor

1. **Transferability only demonstrated within the CNN family.** The paper claims "model-agnostic" operation (line 6) and mentions using "convolution and attention-based" surrogate models (line 117). However, Table 3 only shows transfer from a ResNet-18 surrogate to other CNN-based models (ResNet-34, VGG16-BN, VGG19-BN). A ViT → DeiT experiment is mentioned in a commented-out line (275) but no results appear in the main paper. The claim of cross-architecture transferability is therefore only partially supported.

2. **Bi-level optimization procedure is underspecified for reproducibility.** Equation (1) formalizes the bilevel optimization, but the paper does not specify how the inner loop (\(\arg\min_w\)) is solved — whether to convergence each outer iteration, approximated with few gradient steps, or handled via implicit differentiation. This matters because the tractability of the attack depends on this design choice.

3. **Unsupported quantitative claim about prior backdoor attacks' fairness impact.** Line 51 states that prior backdoor attacks produce an accuracy disparity "less than 0.8% for ResNet-18 when tested on the FairFace dataset" without providing a citation or experimental evidence for this specific number. While plausibly correct, it should be evidenced.

### Trivial

- "audition detectors" in the conclusion line 351 — should be "auditing detectors" (parser artifact from the original submission; the intended meaning is clear).

## Nice-to-Haves

- **Additional fairness metrics.** The evaluation relies solely on accuracy disparity (Bias = |ACC(G_t) − ACC(G_{nt})|). Checking whether the attack also preserves equalized odds, demographic parity, or other parity-based criteria on clean inputs would strengthen the stealthiness justification. This is scope-extension, not a core flaw.
- **Variance reporting.** Results are averaged over 5 runs without standard deviations or confidence intervals. Adding these would improve statistical rigor.
- **Discussion of attack limitations.** The paper does not discuss scenarios where the attack might fail (e.g., robust aggregation defenses, high group correlation). A limitations paragraph would improve scholarly depth.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Missing appendix content"* — The harsh critic notes that the appendix (stripped by the parser) might contain details about δ and m. Rule: Remove weaknesses about missing appendix content.
- *"Typos and formatting"* — Several minor formatting nits from the harsh critic (e.g., "audition" vs "auditing," line breaks) are removed per the hard rule that these are parser artifacts, not author errors.
- *"Should test more fairness metrics (equalized odds, demographic parity)"* — Moved to Nice-to-Haves. The paper explicitly scopes itself to accuracy disparity; requesting additional metrics is scope creep, not a flaw in what is presented.
- *"ISIC clean-model Bias is already 13%"* — This is an observation about the data, not a weakness of the method. The paper transparently reports this baseline; it does not undermine any claim.
- *"Bi-level optimization details about δ and m being binary/continuous"* — The paper states δ is the magnitude value and m is a mask (line 128). The level of detail is adequate for a conference paper; the absence of "binary vs. continuous" clarification is a minor omission at most, folded into the reproducibility concern above.
- *"The paper does not discuss failure scenarios"* — Moved to Nice-to-Haves; this is a scholarly polish item, not a weakness in the presented claims.
- *Strength: "Transferability across model architectures"* — This strength is retained but downgraded in force because it is only CNN-to-CNN. The strength is still valid for what is shown.

## Novel Insights

None beyond the paper's own contributions. The reviews identify the two main evidential gaps (missing baselines and missing defense evaluation) but do not offer any novel technical insight about the method or its implications that goes beyond what the authors themselves articulate.

## Suggestions

1. **Add a head-to-head comparison table** against the fairness attacks cited in the paper (Solans et al., Jagielski et al., van et al.) on at least one common dataset (e.g., FairFace) using matching poisoning ratios and model architectures. Report T-ASR, NT-ASR, PBias, and CACC drop. This single addition would transform the paper from an ablation study into a demonstrable advance over prior work.

2. **Run Neural Cleanse and ABS in their standard (group-unaware) form** against TrojFair-poisoned models and report detection rates. If they fail to detect the attack, the stealthiness claim is directly supported. If they detect it, report honestly and discuss implications.

3. **Include a cross-architecture transfer experiment** (e.g., CNN surrogate → ViT victim, or ViT surrogate → CNN victim) to better support the "model-agnostic" claim, or temper the claim to match the evidence.

## Score and Decision

This paper proposes a well-motivated, modular Trojan fairness attack with a convincing ablation study and strong results across multiple datasets and models. The two major weaknesses are the absence of comparison against prior fairness attacks (despite explicitly claiming to improve upon them) and the lack of empirical evaluation against standard backdoor detectors to substantiate the stealthiness claim. These are evidential gaps rather than structural flaws — the method itself appears sound — but they prevent the paper from making its full case in its current form.

**Originality:** Good — the idea of using group-specific trojan poisoning for fairness attacks is novel.  
**Importance:** High — fairness and security are both timely topics.  
**Claims supported:** Partially — the method's own performance is well-supported, but comparative and stealthiness claims are not.  
**Soundness:** Good for the main experiments; the defense experiment is insufficient.  
**Clarity:** Clear writing and well-structured presentation.  
**Value:** The method and ablation are contributions, but their value is diminished without proper contextualization.

<score>5.0</score>
<decision>Reject</decision>
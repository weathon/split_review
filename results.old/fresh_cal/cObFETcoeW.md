Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper revisits backdoor-based evaluation of saliency-based representation visualization (SRV) methods. It identifies that existing backdoor watermarks suffer from **trigger generalization**—potential triggers different from the one used in training can still activate the backdoor, producing inconsistent and unreliable SRV rankings. The paper proposes GLBW (Generalization-Limited Backdoor Watermark), trained via a min-max formulation where an inner maximization finds the "worst" alternative triggers and an outer minimization suppresses their effects. Experiments on CIFAR-10 and GTSRB show that GLBW reduces trigger generalization (e.g., 170× reduction in Chamfer distance on CIFAR-10) and produces consistent SRV method rankings across datasets.

## Strengths

1. **Exposes a genuine, underexplored problem in XAI evaluation.** Section 3.2 demonstrates experimentally that the existing backdoor-based evaluation (Lin et al., 2021) yields inconsistent SRV method rankings when different potential triggers (with large Chamfer distance from the original) are used, directly revealing that trigger generalization undermines the method's reliability. This is a well-motivated finding.

2. **Novel min-max formulation to limit generalization.** Section 4.3 (Eq. 2) formulates GLBW as a min-max problem that explicitly seeks and penalizes the "worst" synthesized triggers (those with both high attack effectiveness and large difference from the original trigger). This directly targets trigger generalization in a way no prior backdoor-based evaluation method has attempted. The idea is technically plausible and well-grounded in the problem analysis.

3. **Substantial empirical reduction in trigger generalization.** Table 5 reports that GLBW reduces Chamfer distance from 0.99 (vanilla watermark) to 0.001 on CIFAR-10 with Neural Cleanse-based trigger synthesis, and from 0.65 to 0.01 with TABOR, while maintaining watermark success rates above 85%. PLG (percentage of low-generalization triggers) reaches 100% in most cases. These are large, systematic improvements.

4. **Consistent evaluation rankings across datasets.** Table 6 shows that with GLBW, the average rank of six SRV methods (BP, GBP, GGCAM, OCC, FA, LIME) is consistent across CIFAR-10 and GTSRB, in contrast to the inconsistent rankings produced by vanilla watermarks (Table 4). This is the key evidence that GLBW addresses the specific failure mode identified in the paper.

5. **Robustness analysis across hyperparameters.** Figures 8–9 and Tables 7–8 show that GLBW maintains low generalization across varying watermarking rates, trigger sizes, target labels, and model architectures on CIFAR-10, indicating the method is not brittle.

## Weaknesses

### Fatal
None.

### Major

1. **The "more faithful" claim exceeds what the experiments demonstrate.** The paper's central claim is that GLBW enables "more faithful XAI evaluation." However, the experimental validation only shows that GLBW produces *consistent* rankings across datasets. Consistency is not the same as faithfulness. The paper identifies trigger generalization as a source of inconsistency and shows that GLBW reduces it, which is a meaningful improvement. But without any ground-truth reference (human-annotated saliency rankings, synthetic data with known important regions, or correlation with established evaluation methods), there is no evidence that the GLBW-based rankings are actually *correct*—only that they are stable. The logical argument (fixing inconsistency → more faithful) is plausible but not empirically validated. This gap between the claim and the evidence is the paper's most significant limitation. The title itself says "Towards Faithful," which is appropriate, but the abstract and contributions state "a more faithful XAI evaluation" as a delivered result rather than a direction.

2. **Key method details are underspecified, harming reproducibility.** The GLBW inner maximization relies on an "adaptive optimization method" to find promising synthesized triggers, described only as: "we repeat the trigger generation and adaptively adjust the μ based on the current trigger candidate until we find the promising synthesized trigger" (Section 4.3). No algorithm, pseudocode, or concrete adjustment strategy is provided. Furthermore, the overlap threshold τ (introduced in Eq. 2) and the trade-off parameter μ are central to GLBW, but their values are never reported or ablated. λ₃ and λ₄ are set to 1, but τ and μ are left unspecified. Given that the entire method hinges on this adaptive inner maximization, this constitutes a significant reproducibility gap.

### Minor

3. **The evaluation pipeline's handling of the three identified implementation limitations is unclear.** The paper lists three implementation limitations of the Lin et al. evaluation (absolute gradient handling, threshold-based selection, bounding-box IOU) in Section 1 and claims to "address" them (Contribution 1). However, the paper never explicitly describes *how* they are fixed—it only mentions using a "standardized evaluation process" (Section 5.1). A reader cannot verify whether these flaws are actually corrected or how the corrections affect results. (Section 3.1, which may have contained this information, is not present in the extracted text; the authors should ensure this is clearly described in the main body.)

4. **No statistical reporting (variance, confidence intervals).** For key results (Tables 3–8, Figures 4, 7–9), no standard deviations, confidence intervals, or significance tests are reported, even though 1,000 trigger candidates are generated with random initializations, meaning the metrics have inherent stochasticity. This makes it impossible to assess whether observed differences are meaningful.

5. **The BWTP baseline is self-designed and performs poorly as expected.** BWTP (backdoor watermark with trigger penalty) is introduced as "the most straightforward method" and unsurprisingly fails (even *increasing* generalization on CIFAR-10). While this helps motivate GLBW, the paper compares GLBW only against vanilla backdoor watermarks and this self-designed baseline. No existing techniques that might limit trigger generalization (e.g., more complex/irregular triggers, robust training approaches) are compared or discussed as alternatives.

6. **PLG threshold values are stated without justification.** The IOU thresholds for PLG (0.3 for CIFAR-10, 0.18 for GTSRB) are used to define "low generalization" but the paper offers no rationale for these specific values. Similarly, the threshold for selecting potential triggers (1.5× the original trigger's loss) is stated without justification.

### Trivial

- The sentence "3, it is mostly because its synthesized triggers are 'weak'" (appears as a fragment in the extracted text) needs cleanup.
- The Chamfer distance is acknowledged to scale with trigger size (Section 5.3), yet it is used as a primary metric. The paper correctly compensates by also reporting PLG, but the limitation should be noted earlier.

## Nice-to-Haves

- A small-scale ground-truth validation (e.g., synthetic data with known saliency regions, or correlation with human rankings on a subset) would directly support the faithfulness claim and is the most impactful addition the paper could make.
- Ablation studies on τ and μ would strengthen the method description and help users apply GLBW.
- Reporting standard deviations over multiple random seeds for all main results would improve statistical rigor.

## Removed Points

- **"BWTP is a strawman"** (from Harsh Critic, point 4, treated as stronger than Minor): This is retained as Minor point 5 (limited baselines). The critique that BWTP is "not a published baseline" is noted, but the paper frames it transparently as a naive demonstration, which is a standard practice. I removed the stronger framing (strawman accusation) because the paper never presents BWTP as a competitive baseline—it explicitly calls it an "ineffective baseline."
- **"The three implementation limitations are identified but never fixed"** (Harsh Critic, point 2, framed as a structural gap): Demoted to Minor point 3. Section 3.1 was likely present in the original submission (the paper references it) and likely describes the fixes, but was stripped by the parser. The milder retained criticism is that the paper should explicitly connect the fixes to the evaluation pipeline.
- **"Method description vague / no pseudocode"** (Harsh Critic, point 3): Retained as Major point 2 (adaptive optimization details, τ and μ values). The critique about the definition of p(d(m,m')) in BWTP is dropped because the paper says it's a probability activation function (e.g., modified Sigmoid), which is sufficient for a baseline method.
- **General area-sweep concerns** (e.g., "could the metric be measuring a proxy?", speculative gaps about confounders): Removed as unanchored speculation.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Removed. Retained only concrete, evidence-grounded strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent perspective that the paper itself does not articulate.

## Suggestions

1. **Reframe the faithfulness claim.** Change "we design a more faithful XAI evaluation" to "we design a more reliable/consistent XAI evaluation by reducing trigger generalization" unless ground-truth validation is added. The "Towards" in the title is appropriate; the body should match this modesty.
2. **Provide pseudocode or an algorithm box** for the adaptive inner-maximization procedure (μ adjustment and "promising" trigger selection). Report the specific values of τ and any initial/maximum μ used in experiments.
3. **Add confidence intervals or standard deviations** for all main quantitative results (Tables 5–8, Figures 8–9) over at least 3 random seeds.
4. **Explicitly describe how the three implementation limitations are addressed** in the evaluation pipeline. If they were described in a section that was stripped by the parser, ensure this is clear in the main body.
5. **Justify the PLG threshold values** (0.3 for CIFAR-10, 0.18 for GTSRB) or demonstrate that results are not sensitive to the specific threshold.
6. **Acknowledge the lack of ground-truth validation explicitly** as a limitation and future work direction, rather than claiming "more faithful evaluation" as a delivered result.

## Score and Decision

**Originality:** 7/10 — The trigger generalization problem in backdoor-based XAI evaluation is newly identified and measured. The GLBW min-max formulation is novel, though the individual components (min-max training, neural-cleanse-style trigger search) are adapted from prior work.

**Importance of research question:** 8/10 — Reliable automatic evaluation of XAI methods is an important and under-addressed problem. The paper tackles a meaningful obstacle to progress in this direction.

**Claims supported by evidence:** 5/10 — The claim of reduced trigger generalization is well-supported. The claim of "more faithful" evaluation is not directly validated. Method reproducibility is hindered by underspecified details (τ, μ, adaptive procedure).

**Soundness of experiments:** 6/10 — Clear experimental design with appropriate metrics. However, the lack of statistical reporting and the absence of any ground-truth comparison weaken the conclusions.

**Clarity of writing:** 7/10 — The problem motivation, analysis, and method are generally clearly described, despite some grammatical issues from parser artifacts. The main gap is in method detail specificity.

**Value to the research community:** 7/10 — The identification of trigger generalization as a confound in backdoor-based evaluation is a useful contribution. GLBW provides a practical tool for more consistent evaluations. The framework will be valuable to XAI researchers.

**Overall:** The paper identifies a real problem and proposes a technically sound solution. Its main weakness is the gap between the "more faithful" claim and what is actually demonstrated (consistent rankings). This is a meaningful contribution that, with reframing and additional method details, would be ready for publication. The paper's core technical contribution—reducing trigger generalization—is solid and well-supported.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper revisits the backdoor-based evaluation method for saliency-based representation visualization (SRV) methods. It identifies two problems with the existing approach: (1) implementation limitations (e.g., threshold-based selection, bounding-box IOU), and (2) trigger generalization — the phenomenon where potential triggers different from the original training trigger can still activate the backdoor, rendering evaluations inconsistent and unreliable. The paper proposes a generalization-limited backdoor watermark (GLBW) trained via a min-max formulation: inner maximization finds "worst" potential triggers (high attack effectiveness and dissimilarity from the original), and outer minimization suppresses their effects. Experiments show GLBW dramatically reduces trigger generalization compared to vanilla and penalty-based baselines, producing consistent SRV method rankings across datasets.

## Strengths

- **Systematic identification of trigger generalization as a fundamental flaw in existing backdoor-based XAI evaluation**: The paper provides clear empirical evidence (Figure 4, Tables 3–4) that potential triggers with large spatial distance from the original trigger can still activate backdoors, leading to inconsistent SRV rankings. This problem identification is well-motivated and directly challenges the latent assumption of prior work (Lin et al., 2021).

- **Principled min-max formulation yielding strong quantitative reduction in trigger generalization**: The GLBW training objective — finding the "worst" potential triggers via inner maximization and suppressing them via outer minimization — is a clean technical design. The empirical results in Table 5 are compelling: on CIFAR-10, Chamfer distance drops from 0.694 (vanilla) to 0.004 (GLBW) under neural cleanse, and PLG reaches 100% on both datasets, while WSR remains above 85%. These gains are observed across multiple trigger synthesis methods (neural cleanse and TABOR).

- **Comprehensive robustness analysis across key hyperparameters**: The paper systematically studies watermarking rate (Figure 8), trigger size (Table 7), target label (Table 8), and model architecture (Figure 9), showing that GLBW maintains low generalization (100% PLG) under diverse settings. This strengthens confidence in the method's practical reliability.

## Weaknesses

### Fatal
None. The paper's technical core (GLBW's ability to reduce trigger generalization) is sound and well-supported by evidence.

### Major

- **The central claim of "more faithful" XAI evaluation is unvalidated against any ground truth.** The paper asserts that GLBW yields "more faithful" evaluation primarily on the grounds that SRV method rankings are consistent across CIFAR-10 and GTSRB (Table 6). However, consistency is not faithfulness. Without comparing these rankings against human judgments, known synthetic saliency benchmarks, or even established automatic metrics (e.g., insertion/deletion), there is no evidence that GLBW-based rankings are *correct* — they could merely be consistently wrong. This is a fundamental gap: the paper's stated purpose is to improve XAI evaluation, but the evaluation of the evaluation itself is missing. The paper would benefit substantially from even a small-scale human study or comparison to perturbation-based metrics.

- **The adaptive μ optimization for inner maximization is described too vaguely for reproducibility.** The paper states: "we repeat the trigger generation and adaptively adjust the μ based on the current trigger candidate until we find the promising synthesized trigger in each inner maximization" (line 128). No convergence criteria, update rule, restart strategy, or schedule for μ is provided. Given that the inner maximization is central to GLBW's effectiveness, this level of vagueness is a significant reproducibility concern. The description is not replicable from the text alone.

### Minor

- **The novelty claim is slightly overstated.** The paper says it is "the first trying to measure and even manipulate trigger generalization" and acknowledges that Qiao et al. (2019) and Li et al. (2021a) "initially discovered trigger generalization phenomenon." The nuance is that prior work did not provide *statistical patterns* or *control* generalization, which the paper does. However, the headline claim in the contribution list (line 27) reads more broadly than the supporting text warrants. A more precise framing would strengthen credibility.

- **The diagnosis of BWTP failure is asserted without quantitative support.** The paper says BWTP synthesizes "weak" triggers that have "either a large loss value or are similar to the original trigger" (lines 115, 173). This is a plausible explanation but no quantitative comparison of the triggers produced by BWTP vs. GLBW is provided — e.g., their loss values, similarity to the original trigger, or spatial properties. Figure 7 shows the difference visually but a numerical summary would substantiate the claim.

- **Missing error bars, standard deviations, or significance tests throughout.** Tables 3–5 and Table 6 report point estimates without any indication of variance. Given that trigger synthesis involves random initialization (1,000 candidates), reporting variability across runs or initializations would be important for assessing reliability.

- **The claim about Chamfer distance and trigger size is hand-wavy.** In Section 5.3 (Table 7 analysis), the paper notes "the chamfer distance raises with the increase in trigger size. However, it is due to the properties of this distance metric and does not mean an increase in trigger generalization." This assertion is not supported by any analysis (e.g., normalized Chamfer distance). Since the paper itself introduces Chamfer distance as a metric for generalization, this dismissal needs justification.

- **The overlap threshold τ is not ablated.** The GLBW formulation (line 118) introduces τ as a hyperparameter controlling the allowed overlap between synthesized and original triggers. Despite its potential importance, τ is never varied or analyzed in the experiments.

- **Circularity concern regarding trigger synthesis methods (weakened but not eliminated).** The paper uses neural-cleans-like optimization during GLBW training, then evaluates generalization with neural cleanse, TABOR, and pixel backdoor — all gradient-based search methods. The paper partially addresses this by using multiple evaluation methods, but all share a similar algorithmic flavor. Whether GLBW limits generalization to *truly different* trigger types (e.g., non-local, semantic, or naturally occurring patterns) remains untested.

### Trivial
None.

## Nice-to-Haves

- A comparison of SRV rankings from GLBW-based evaluation against those from perturbation-based automatic metrics (e.g., insertion/deletion) to provide a reference point for "faithfulness."
- Example saliency maps (Grad-CAM, BP, LIME) for GLBW-watermarked vs. vanilla-watermarked models to visually illustrate that saliency concentrates on the original trigger region.
- Evaluation against a non-gradient-based trigger type (e.g., fixed random patches with no adversarial optimization) to strengthen the generalization-limited claim.

## Removed Points

- **Criticism that implementation fixes are not isolated from GLBW (Harsh Critic Critical Issue #3):** Removed. The paper's Section 5.1 states that *all* baselines (Vanilla, BWTP, GLBW) are compared "with standardized evaluation process." This means the implementation fixes are applied uniformly, and the comparison between Vanilla and GLBW *does* isolate the watermark effect. The critic's requested control experiment already exists in the paper's design.
- **Criticism that Section 3.1 is missing:** Removed per instructions — the parser strips sections; Section 3.1 exists in the original submission.
- **Criticism about missing appendix or proof content:** Removed per instructions — these were stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The key observation — that trigger generalization in backdoor watermarks undermines the reliability of backdoor-based XAI evaluation — is well-articulated by the paper itself. The reviews do not surface a novel angle beyond what the authors already present.

## Suggestions for Improvement

1. **Validate the "faithfulness" claim.** Add at least one of: (a) a small-scale human evaluation comparing SRV method rankings from GLBW against expert judgments, (b) comparison against perturbation-based faithfulness metrics (insertion/deletion), or (c) a synthetic experiment where ground-truth saliency is known. This single addition would transform the paper from "a method for limited-generalization backdoors" to "a validated XAI evaluation method."

2. **Provide a detailed specification of the adaptive μ procedure.** Include convergence criteria, update schedule, number of gradient steps per inner maximization, and restart strategy. If space is tight, pseudocode in the appendix would suffice.

3. **Add statistical uncertainty estimates.** Report standard deviations or confidence intervals across random initializations (at least for generalization metrics in Tables 3–5), and consider multiple training runs.

4. **Support the BWTP failure diagnosis quantitatively.** Show the loss values and Chamfer distances of the triggers synthesized by BWTP vs. GLBW to substantiate the "weak trigger" claim.

5. **Normalize Chamfer distance when analyzing trigger size effects.** Either report a size-normalized variant or explicitly compute and compare against the expected value under the null.

6. **Ablate the overlap threshold τ.** This is a free parameter in the GLBW objective and its effect on the trade-off between watermark success and generalization should be shown.

## Score and Decision

The paper identifies a genuine problem, proposes a technically sound solution (GLBW), and provides strong evidence that GLBW dramatically reduces trigger generalization — a necessary condition for reliable backdoor-based XAI evaluation. The robustness analysis across hyperparameters is thorough.

However, the paper's headline contribution — "more faithful XAI evaluation" — rests on an unvalidated leap from "consistent across datasets" to "faithful." Without any ground-truth comparison, the core claim about XAI evaluation remains unsupported. The method portion (GLBW as a generalization-limited watermark) is solid; the application portion (XAI evaluation) is incomplete. The paper would be significantly strengthened by adding even a limited validation of faithfulness.

Given this asymmetry — strong technical contribution, weak validation of the central evaluation claim — the paper is borderline in its current form.

**Score: 5.5 / 10**

**Decision: Reject** (borderline; could become a strong Accept with addition of faithfulness validation against ground truth)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
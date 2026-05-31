Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

This paper studies how LLMs of different sizes within the same model family respond to intentionally misleading in-context hints injected into multiple-choice benchmarks. Using a *Relative Accuracy Drop* metric, the authors find that across four model families (Llama, Gemma, Mistral, Phi), larger models consistently exhibit smaller performance drops under deception. Three control experiments — truthful hints, directive instructions to choose incorrectly, and question removal — collectively suggest this resilience stems from better integration of internal knowledge with prompt information rather than from ignoring cues or memorization.

---

## Strengths

1. **Cross-family scaling evidence for deception resilience.** Figure 2 shows that within four distinct model families, the Relative Accuracy Drop under deception decreases from the smaller to the larger model in each family. The thin dashed lines per-benchmark per-family show the pattern holds at the individual benchmark level, not just in aggregate. This provides consistent, within-family evidence linking parameter count to deception resistance, a relationship not studied in prior work on adversarial noise or prompt injection.

2. **Well-designed control experiments that rule out alternative explanations.** The *Directive Instruction* experiment (Figure 3) shows that larger models *follow legitimate instructions better* (exhibiting a larger drop when told to pick wrong answers), rejecting the hypothesis that larger models simply disregard in-context cues. The truthful-hint control (all models achieve near-perfect accuracy) and the *Context Removal* experiment (Figure 4-5) further strengthen the case that the observed behavior is specific to processing conflicting information, not a general tendency to ignore prompts.

3. **Clear, well-motivated methodology.** The prompt unification and alteration pipeline (Section 3) is described with sufficient detail to be replicable, and the choice of the Relative Accuracy Drop metric is explicitly motivated with a concrete example showing why absolute drop would conflate baseline differences.

---

## Weaknesses

### Fatal
None.

### Major

1. **The scaling claim rests on only two size points per family, making the trend suggestive but not robust.** Each family provides exactly one small and one large model (e.g., Llama-8B vs. Llama-70B, Gemma-2B vs. Gemma-9B). A monotonic relationship between size and resilience cannot be established from two points. The aggregation across four families showing a consistent direction helps, but without a third intermediate size in any family (or statistical tests of the trend), the observed difference could be partly driven by other factors correlated with size (training data recency, fine-tuning specifics, architectural differences). This is the paper's most significant limitation for a claim presented as a "scaling" result.

2. **The memorization control does not convincingly rule out data contamination as a confound for the size–resilience correlation.** The experiment in §4.3 shows that an uncontaminated model (DCLM-7B) and overfitted Llama-8B both perform above chance when the question is removed, with similar decay patterns. This demonstrates that *above-chance performance in the context-removal setting is not solely due to memorization*, but it does not address whether the *scaling trend* in the deception experiment could be partly driven by larger models having seen more of the test data. DCLM is only 7B — the same size as the smallest Llama — so it provides no evidence about whether the gain from 8B to 70B reflects a more robust world model or better memorization of benchmark facts. The claim that resilience is "unlikely due to memorization" (§1) overreaches the evidence presented.

### Minor

1. **The Relative Accuracy Drop metric mechanically favors higher-baseline models, and the paper does not fully disentangle this confound.** As the authors note, a 5% absolute drop from 80% yields a 6.25% relative drop, while the same absolute drop from 60% yields 8.33%. Since larger models have higher baselines, part of the observed smaller relative drop is attributable to higher baselines rather than superior *validation* of the deceptive hint. The paper reports that absolute drops also favor larger models (Figure 7 in appendix), which mitigates this concern, but a more principled treatment (e.g., regression partialling out baseline, or matched-baseline subsets) would significantly strengthen the core claim.

2. **No statistical significance or variance information is reported.** The paper should report whether the differences in Relative Accuracy Drop between size pairs within each family are statistically significant (e.g., via bootstrapped confidence intervals or paired tests across benchmarks). The shaded regions in Figure 2 are labeled as "deviation" without specifying whether they are standard deviation, standard error, or min-max range. Without this information, the reader cannot assess the reliability of the observed patterns.

3. **The Gemma family's divergent behavior in the Directive Instruction experiment (Figure 3) is noted but not analyzed.** The paper correctly identifies Gemma as an outlier — its larger model (9B) shows a *smaller* Relative Accuracy Drop under directive instructions, opposite to the other three families. The paper attributes this to Gemma being "the worst performing one on most of the original benchmarks," but this is a correlation, not an explanation. A deeper discussion of what architecture or training differences might cause this would help the reader assess whether the core deception-resistance pattern might also have family-specific caveats.

### Trivial

- The figure captions describe shaded regions as "deviation" but do not specify the type (standard deviation, standard error, or min-max). This should be clarified.

---

## Nice-to-Haves

- Testing at least one family with an intermediate size point (e.g., Llama-3.1-405B) would convert the two-point comparison into a more convincing scaling curve.
- A logit analysis comparing the probability assigned to the hinted wrong answer vs. the correct answer across model sizes would provide direct evidence of the hypothesized mechanism (differential reliance on internal knowledge vs. prompt content).
- Varying the certainty of the deceptive hint (e.g., "I think the answer is A" vs. "The correct answer is A") could reveal whether larger models are specifically more robust to less-certain suggestions — an interesting nuance the current fixed-phrasing design cannot capture.
- A per-benchmark breakdown table or scatter plot in the main text (not only the appendix) would help readers assess the consistency of the trend across benchmarks.

---

## Removed Points

These points were raised in the reviews but are removed or downgraded for the reasons given:

- *"The paper does not clearly differentiate its setting from existing adversarial noise studies"* — The paper explicitly says (line 112-113) that prior adversarial robustness work "does not address robustness with respect to parameter scaling." The differentiation is present.
- *Missing appendix/qualitative analysis* — Appendices are stripped by the parser; this is a formatting artifact.
- *"The claim of 'first empirical evidence' is too strong"* — The paper phrases it as "To our knowledge…" (§5), which is a standard caveat. The claim is about a specific type of deception (misleading hints), not general robustness to noise.
- *Request for base-model experiments* — The paper explicitly chooses instruction-tuned models and justifies the choice (§3.3). This is in-scope. Testing base models would be a separate study.
- *"Using a more forceful phrasing for the hint could yield different results"* — This is speculative and the current phrasing is a reasonable experimental choice. Could be investigated in future work.
- *Several presentation/style nitpicks* about formatting that are parser artifacts.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface any synthesis that meaningfully extends the paper's own analysis. The most interesting observation from reviewing the paper is that the cross-family consistency of the trend (across Llama, Gemma, Mistral, Phi) is genuinely striking even with only two size points per family — the within-family-per-benchmark connecting lines in Figure 2 show that the pattern reverses in almost every single case, which is stronger evidence than a simple aggregate comparison. Neither review highlighted this visual specificity.

---

## Suggestions

1. Add at least one model family with three size points (or include a scatter plot of all available model sizes from open model zoos) to convert the scaling observation from a two-point comparison into a more convincing trend.
2. Report bootstrapped confidence intervals or paired statistical tests for the difference in Relative Accuracy Drop between the small and large model in each family.
3. Explicitly model the relationship between baseline accuracy and resilience (e.g., regression or matched-baseline subsets) to separate the effect of size from the mechanical effect of higher baselines on the relative drop metric.
4. Clarify whether the "deviation" shaded in Figures 2 and 3 is standard deviation, standard error, or min-max range.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `XjkJdWOyqN.md` | 3.00 | R1 | Weaker: about word-level perturbations with less clear results |
| `hzu5luG4DC.md` | 3.00 | R1 | Weaker: adversarial defense survey-style paper |
| `KBixkDNE8p.md` | 3.00 | R1 | Weaker: Typoglycemia psychology, less rigorous |
| `BeOEmnmyFu.md` | 2.50 | R1 | Weaker: jailbreak method paper |
| `bjlTHVAkHS.md` | 4.33 | R1 | Weaker: similar topic (conflicting prompts) but messier writing and less clear methodology |
| `YaRzuMaubS.md` | 4.00 | R1 | Different scope (formal definition of deception), less empirical |
| `1OkVexYLct.md` | 4.33 | R1 | Different scope (Othello world model probing) |
| `RTHbao4Mib.md` | 6.25 | R1 | Comparable: both are evaluation/analysis papers; this one has more extensive experiments but also significant missing-related-work issues. Current paper is cleaner but thinner. |
| `syThiTmWWm.md` | 7.75 | R1 | Stronger: novel method with surprising results, oral-level |
| `6Mxhg9PtDE.md` | 9.50 | R1 | Stronger: highly impactful finding about safety alignment |
| `tc90LV0yRL.md` | 8.67 | R1 | Stronger: comprehensive framework, oral-level |
| `bNt7oajl2a.md` | 8.00 | R1 | Stronger: novel benchmark with thorough analysis |
| `72H3w4LHXM.md` | 5.00 | R2 | Weaker: automatic pipeline paper with limited novelty |
| `0sJ8TqOLGS.md` | 5.25 | R2 | Weaker: critical thinking evaluation with writing/analysis issues |
| `9ceadCJY4B.md` | 5.67 | R2 | Slightly weaker: well-written but limited novelty (prior sycophancy work). Current paper has more novel angle. |
| `wvFnqVVUhN.md` | 6.25 | R2 | Different domain (VLM jailbreaks), method paper |
| `sULAwlAWc1.md` | 7.00 | R2 | Stronger: novel attack method with comprehensive experiments |
| `r42tSSCHPh.md` | 7.00 | R2 | Stronger: simple but impactful method, extensive evaluation |

**Round 1 bracket:** between 4.0 and 7.0.

**Final score determination:** The paper sits between the rejected analysis papers at ~5.0–5.7 and the accepted poster at 6.25. It is cleaner and better-motivated than "Intuitive or Dependent?" (4.33) and "LLM Spark" (5.25). Compared to "Ask Again, Then Fail" (5.67), it has stronger novelty but thinner empirical evidence. Compared to "LLMs Often Say One Thing and Do Another" (6.25, accepted), it has clearer methodology and better controls but fewer experiments and thinner evidence for its core claim. The paper's main weakness is the two-point-per-family scaling evidence — a genuine limitation that prevents the paper from being a strong accept — but the consistent cross-family pattern and thoughtful control experiments make it a reasonable borderline contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
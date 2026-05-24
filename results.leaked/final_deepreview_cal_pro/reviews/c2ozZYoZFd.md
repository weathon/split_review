Now I have all the data I need. Let me compile the final review.

Round 1 bracket: The paper sits above the ~4.0 memorization critique papers and below the ~8.0 strong methodological contributions, with the most relevant comparisons in the 5.75–6.75 range.

Round 2 narrowed it further. The paper is comparable to "On Evaluating the Durability of Safeguards" (6.50) — a detailed critique with case studies and derived lessons — and slightly stronger than "(Mis)Fitting Scaling Laws" (5.75). However, the current paper has a few sections where its own standards aren't fully met (Sec 2.4, Sec 4.3), which pull it down somewhat from the 6.50 anchor. I'd place it at 6.0.

---

## Summary

This paper presents a detailed re-examination of an ICLR 2025 Oral paper that introduced `min-p` sampling. Across four lines of evidence — human evaluations, NLP benchmark evaluations, LLM-as-a-Judge evaluations, and community adoption claims — the authors demonstrate that the original paper's evidence does not support its central claim that `min-p` consistently outperforms existing samplers. The strongest contributions are (1) the discovery that one-third of the human evaluation data (for basic sampling) was omitted without justification, (2) a large-scale hyperparameter sweep on GSM8K across 9 models with a Best-of-N analysis showing `min-p`'s advantage vanishes when hyperparameter tuning is equalized, and (3) documentation that the original paper's GitHub-stars claims were unsubstantiated and retracted. The paper closes with six actionable lessons for rigorous empirical ML research.

## Strengths

- **Discovery of omitted data and flawed statistics in the human evaluation (Section 2.1–2.2):** The paper reveals that the original study excluded scores for basic sampling (one-third of all collected data) without mention or justification. Including these data, applying proper multiple-comparison correction (Bonferroni, Intersection-Union Test), and visualizing with confidence intervals (Figure 1, Table 1) show that `min-p` is indistinguishable from baselines in nearly all settings. This finding is publicly confirmed by the original authors and is unambiguous.

- **Controlled hyperparameter sweep with Best-of-N analysis (Section 3.1):** An extensive sweep across 9 models, 31 temperatures, 6 hyperparameters per sampler, and 3 random seeds (~6000 A100-hours) demonstrates that `min-p` does not outperform other samplers when the volume of hyperparameter tuning is equalized (Figures 4, 5). The Best-of-N methodology is a principled, transferable technique for controlling hyperparameter search budget and detecting potential cherry-picking. This is the paper's strongest empirical contribution.

- **Verification and retraction of adoption metrics (Section 5):** The paper's scrutiny directly led to the retraction of the original paper's claim of 54k GitHub repositories and 1.1M stars — which three of four ICLR reviewers had cited as their main justification for endorsement. This is a concrete, high-impact outcome.

- **Comprehensive scope across four evidence lines:** Unlike typical reproducibility papers that focus on one experiment, this work systematically dismantles every category of evidence the original paper offered — human studies, NLP benchmarks, LLM judges, and community adoption — making the overall case substantially more convincing than any single re-analysis would be.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Asymmetric rigor in analyzing the new human evaluation (Section 2.4):** The paper demands rigorous statistical testing from the original study yet analyzes the authors' new (camera-ready) human evaluation almost entirely through a scatter plot (Figure 3) and an asserted numerical discrepancy (5.80 vs. 7.80), without reporting any statistical tests, confidence intervals, or multiple-comparison corrections. The conclusion that `min-p` offers "no apparent advantage" is not backed by the same standard of evidence the paper requires of its target. This is a real inconsistency, though the section plays a supplementary role (the new study was added in response to this paper's feedback) and the visual evidence in Figure 3 is reasonably clear. Still, applying even a simple set of paired t-tests would bring this section into alignment with the paper's own standards.

- **Thin evidence for the selective reporting claim in the LLM-as-a-Judge section (Section 4.3):** The accusation that "the higher of two scores was reported for min-p but the lower of two scores for top-p" rests on a single Telegram link shared by the original first author. The paper does not present the full set of results, establish a consistent selection protocol, or rule out benign explanations (the reported differences are small: 52.01 vs 50.14 for min-p, and 50.07 vs 50.43 for top-p — all near 50%). For a paper that trains such a critical lens on its subject, this section lacks commensurate transparency. The paper's own language in the abstract ("appear to have reported results inconsistently") is appropriately hedged, but the section would benefit from presenting a fuller picture or softening the framing further.

- **Qualitative annotation methodology under-described (Section 2.3):** The manual annotation of human evaluators' preference responses (Figure 2) is described too briefly. The paper states it "manually annotated the qualitative responses" and "publicly posted our annotations" but does not report the number of responses, annotation guidelines, or how ambiguous or partial preferences were handled. Given that this figure is used to argue the original paper mischaracterized qualitative feedback, more methodological detail is warranted.

### Trivial

- **Scope boundary in the human evaluation re-analysis could be clearer:** The paper focuses on the "high" diversity setting for well-reasoned justifications (the original authors' own advice, misconfigured low-diversity hyperparameters, and the fact that the `min-p` claim is about the quality–diversity tradeoff). However, the language occasionally blurs the boundary — stating that the original claim is invalidated "across all settings" when the low-diversity condition was excluded from the re-analysis for methodological reasons. An explicit qualification here would preempt scope questions and strengthen the argument.

- **GSM8K is the only benchmark swept:** The paper acknowledges this limitation (line 208: "Due to our compute budget, we only evaluated GSM8K CoT") and mentions it in the Discussion. It would benefit from slightly more prominent discussion of whether the GPQA evaluations from the original paper might behave differently.

## Nice-to-Haves

- The adversarial framing — particularly the extended roll-call of "scandals" in the introduction (lines 45–55) — may distract some readers from the substantive contributions. A more measured tone would likely broaden the paper's impact as a constructive blueprint.
- The Best-of-N analysis would benefit from a short formal justification or a reference to related hyperparameter-optimization literature (e.g., random search, Bayesian optimization), helping readers adopt it in other contexts.
- The NLP benchmark sweep section could list models and modalities more transparently (the 16-panel grid in Figures 4–5 is dense and requires careful reading to navigate).

## Removed Points

*These points were flagged for removal. Treat them with caution.*

- **Harsh Critic claim that the paper's "lessons are not novel — they repackage established good practices":** This was removed as a weakness because the paper explicitly positions the lessons as derived from the case study, and the value is in the detailed instantiation, not in claiming novelty for each lesson. The lesson list is a reasonable synthesis.

- **Harsh Critic claim that the adversarial tone is a weakness:** Downgraded to Nice-to-Have. Tone is a stylistic preference, not a substantive flaw that affects the validity of the paper's claims.

- **Strength Finder: "Actionable lessons grounded in the case study" retained but noted as derivative:** The lessons are a reasonable distillation but are not independently novel beyond the case study that instantiates them.

## Novel Insights

None beyond the paper's own contributions. The most transferable insight is the Best-of-N methodology for equalizing hyperparameter search volume across compared methods — a principled, reproducible framework for fair comparison that goes beyond this specific case study and can be applied broadly in empirical ML evaluation.

## Suggestions

- Apply paired t-tests (or equivalent) with appropriate correction to the new human evaluation data in Section 2.4. Even a simple table analogous to Table 1 would close the asymmetry between the standards applied to the original study and the camera-ready supplement.
- For Section 4.3, either present a complete comparison table showing all configurations and which were reported for each sampler, or reframe the discrepancy as an inconsistency that warrants investigation rather than a confirmed case of selective reporting.
- Add a sentence or two in Section 2.3 specifying the annotation protocol: number of responses, how ambiguous preferences were coded, and inter-annotator agreement if multiple annotators were used.

## Scores and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `dIaykjbiiL` | 2.50 | 1 (low) | Much weaker — unclear contribution, major flaws |
| `OXIIFZqiiN` | 1.50 | 1 (low) | Much weaker — unclear contribution, poor presentation |
| `x8mr9zGkpr` | 3.00 | 1 (low) | Weaker — narrower scope, less rigorous analysis |
| `k0nlUXYKhX` | 2.50 | 1 (low) | Much weaker — unrelated contribution |
| `GbEmJmnQCz` | 4.40 | 1 (mid) | Similar genre but narrower analysis, more reviewer concerns |
| `lf8QQ2KMgv` | 3.75 | 1 (mid) | Similar genre but less thorough, more substantive gaps |
| `RW37MMrNAi` | 5.60 | 1 (mid) | Different genre, similar empirical thoroughness |
| `X8XQOLjLX6` | 4.50 | 1 (mid) | Narrower critique, less empirical heft |
| `et5l9qPUhm` | 8.00 | 1 (high) | Stronger — novel theoretical contribution |
| `EUSkm2sVJ6` | 7.60 | 1 (high) | Stronger — novel method with theoretical grounding |
| `PdaPky8MUn` | 8.00 | 1 (high) | Stronger — clean methodological contribution with broad impact |
| `A3YUPeJTNR` | 8.00 | 1 (high) | Stronger — novel theoretical framework |
| `bmrYu2Ekdz` | 6.50 | 2 (narrow) | Comparable — strong empirical contribution with released artifacts; current paper is slightly weaker due to uneven rigor in a few sections |
| `fXJCqdUSVG` | 6.50 | 2 (narrow) | Comparable — detailed critique with case studies and derived lessons; current paper has larger empirical scope but slightly thinner evidence in one section |
| `xI71dsS3o4` | 5.75 | 2 (narrow) | Current paper is stronger — more substantial empirical contribution and clearer findings |
| `MB53uAZKSc` | 6.25 | 2 (narrow) | Comparable in empirical scope; current paper has a sharper central claim |
| `YPIA7bgd5y` | 6.50 | 2 (narrow) | Slightly stronger — cleaner analysis with fewer methodological gaps |
| `5BCFlnfE1g` | 6.75 | 2 (narrow) | Slightly stronger — novel method plus empirical contribution |
| `icTZCUbtD6` | 6.20 | 2 (narrow) | Comparable — analysis/taxonomy contribution; current paper has more real-world impact |

**Round 1 bracket:** 5.5–7.5 based on comparison with memorization critique papers (~4.0) and strong methodological contributions (~8.0).

**Round 2 narrowing:** Within the 5.75–6.75 band, this paper is most comparable to the "On Evaluating the Durability of Safeguards" (6.50) and "PolyPythias" (6.50) anchors in terms of contribution scope and empirical heft. The uneven rigor in Sections 2.4 and 4.3 pulls it slightly below these anchors. It is clearly stronger than the "(Mis)Fitting Scaling Laws" (5.75) anchor in empirical contribution. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
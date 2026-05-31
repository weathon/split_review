## Summary

This paper presents a thorough replication/audit study of "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024), an ICLR 2025 Oral paper. The authors systematically re-examine each of the original paper's four main lines of evidence—human evaluations, NLP benchmark evaluations, LLM-as-a-Judge evaluations, and community adoption metrics—and conclude that the original paper's own data invalidate the central claim that `min-p` outperforms existing sampling methods. From this case study the authors extract a six-point blueprint for more rigorous empirical ML research, including a novel Best-of-N methodology for controlling hyperparameter volume when comparing methods.

---

## Strengths

- **Timely and impactful subject matter.** Replication studies are rare in ML and the paper directly addresses a recognized crisis in research rigor. The paper had documented real-world impact: it caused corrections to the ICLR 2025 camera-ready version, including the retraction of both major community adoption claims (54k repos, 1.1M stars) and changes to the reported human evaluation data.

- **Substantial and well-designed experimental effort.** The hyperparameter sweep on GSM8K covers 9 models × 2 stages × 4 samplers × 31 temperatures × up to 6 hyperparameters × 3 seeds (~6,000 A100-hours). The two complementary analyses—Best-of-N performance curves and the min-p vs. best-other-sampler gap—are both informative, internally consistent, and convincingly demonstrate that min-p's claimed superiority disappears when hyperparameter volume is equalized.

- **Genuinely novel methodological contribution.** The Best-of-N hyperparameter sweep analysis (subsampling equal numbers of hyperparameters per sampler and tracking the expected best performance) is a practically useful tool that can serve the broader ML community for detecting cherry-picking and ensuring fair benchmark comparisons, well beyond the min-p case study.

- **Correct and transparent statistical analysis.** The re-analysis in Section 2.2 illustrates precisely how pooling across conditions and omitting multiple-comparison corrections can produce spurious conclusions. The use of Bonferroni correction, an Intersection-Union Test (appropriate when the claim is "consistently across all conditions"), and 95% confidence interval visualizations all exemplify the statistical rigor being advocated.

- **Full data transparency and engagement.** The authors publicly shared their annotations of qualitative evaluations, engaged directly with the original authors to obtain clarifications, and documented the ongoing dialogue in the paper. This models the transparency they recommend.

---

## Weaknesses

### Fatal
None.

### Major

- **Single-paper case study limits generalizability of the "blueprint."** Section 6 presents six general lessons for empirical ML research, but all six are derived from a single paper. Each lesson is sound in isolation, but their status as a "blueprint" rather than as case-specific observations would be stronger if supported by even two or three additional examples of the same pattern across other papers. As written, the title's claim of a "blueprint" for ML research is somewhat oversold relative to the evidence base.

- **Ambiguity in the final scientific conclusion.** The paper's central conclusion—that "min-p offers no apparent advantage"—risks being interpreted as "min-p is worse than baselines" when the data more accurately support "min-p is indistinguishable from baselines." The figures (e.g., Fig. 1, Fig. 3, Fig. 5) consistently show approximate parity, not inferiority. A clearer framing of "samplers perform approximately equally" vs. "min-p is bad" would be more scientifically precise.

### Minor

- **Potential for adversarial framing bias.** Phrases such as "appears to have reported results inconsistently, favoring min-p" (Section 4.3) and "experiment seems designed in a manner that introduces a confounder" (Section 4.1) carry implicit accusations of intent. The same facts can be stated more neutrally ("the reporting was inconsistent across conditions"; "the indirect comparison design introduces a confounder"). More neutral language would strengthen the scientific credibility of the critique.

- **"Ongoing work to publish" reference (Section 4.2).** Citing unpublished ongoing work as the basis for discovery in a peer-reviewed submission is unusual and slightly weakens the verifiability of the LLM-as-a-Judge analysis.

### Trivial

- The abstract uses phrases like "invalidated by its own data" with certainty language that slightly oversimplifies the nuanced statistical story: more precisely, the data are insufficient to support the claimed superiority, rather than actively refuting it.

---

## Nice-to-Haves

- Including one or two shorter case studies from other papers to generalize the lessons would significantly strengthen the "blueprint" framing.
- A positive section acknowledging what aspects of the original paper were methodologically sound (e.g., the study design of showing outputs to annotators) would add balance and fairness.
- A table summarizing which original claims were retracted vs. left standing in the camera-ready would help readers quickly understand the final state of the scientific record.

---

## Novel Insights

The paper's most genuinely novel insight is the Best-of-N hyperparameter control methodology: by subsampling equal numbers of hyperparameter configurations across competing methods and tracking the expected best performance as a function of search volume, one can fairly assess whether a claimed advantage is due to algorithmic superiority or to the luxury of a larger hyperparameter search. This is broadly applicable to any benchmarking context where different methods have different numbers of tunable hyperparameters—a pervasive problem in ML evaluation. The practical demonstration (covering 9 models, 2 stages, 31 temperatures) shows that this analysis is computationally feasible and produces consistent, interpretable results. Additionally, the explicit demonstration that 3 of 4 reviewers and an Area Chair were primarily convinced by claims that were subsequently retracted raises important questions about the role of unverified "impact" claims in peer review.

---

## Suggestions

- **Clarify the scope of the conclusion more precisely**: distinguish "insufficient evidence of superiority" from "evidence of no superiority" versus "evidence of inferiority" across different experimental contexts.
- **Expand the blueprint with additional examples** from other recent replication controversies (even briefly) to demonstrate the lessons generalize beyond min-p.
- **Provide a formal characterization of the Best-of-N methodology**, including conditions under which it is most and least informative (e.g., when hyperparameter choices are correlated vs. independent), which would make it easier for other researchers to apply.
- **Adopt more neutral language** in Sections 4.1–4.3 when describing possible errors to avoid conflating methodological ambiguity with intentional misconduct.
- **Report effect sizes**, not just significance/non-significance, for the paired t-tests in Table 1. This would clarify whether the non-significant results reflect small or negligible differences.

---

## Score and Decision

This paper is a thorough, well-executed, and impactful replication study on a subject of broad importance to the ML community. The Best-of-N methodology is a concrete, novel, and practically useful tool. The case study is comprehensive across four lines of evidence, backed by ~6,000 A100-hours of computation, and had documented real-world impact on a high-visibility published paper. Replication studies are undervalued in ML and this is an excellent example of the genre. The main limitations—single case study, some adversarial framing—weigh against a strong accept but do not undermine the paper's fundamental value.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
## Summary

This paper presents a comprehensive reanalysis of Nguyen et al. (2024), an ICLR 2025 Oral paper introducing min-p sampling for language models. The reanalysis examines all four lines of evidence used to support min-p's claimed superiority over existing samplers and, through a combination of statistical reanalysis of the original data, a large-scale hyperparameter sweep (∼6000 A100-hours across 9 models), and documentation of retracted claims, concludes that the original paper's own data do not support its central claims. Along the way, the paper introduces a reusable "Best-of-N" methodology for fair hyperparameter-volume comparison and distills six practical lessons for rigorous empirical ML research.

---

## Strengths

- **Documented data omission changes conclusions (Section 2.1):** One-third of the human evaluation data — scores for basic sampling — was excluded from the original paper's methodology, analysis, and results. The omission was publicly confirmed by the original authors. When included, Figure 1 and Table 1 demonstrate that min-p is largely indistinguishable from both baselines.

- **Technically sound multiple-comparisons analysis (Table 1):** Using the original authors' own published data, the paper conducts 12 one-sided paired t-tests with Bonferroni correction, showing that after correction only 1 of 12 comparisons survives at α = 0.05 and none at α = 0.01. An additional Intersection-Union Test, appropriate for the original claim that min-p "consistently outperforms across all settings," yields the same negative conclusion (max p-value = 0.378). This directly contradicts the original paper's single pooled t-test.

- **Novel Best-of-N hyperparameter equalization methodology (Section 3.1):** The paper introduces and executes a controlled hyperparameter-volume analysis across 9 models × 4 samplers × 31 temperatures × 6 hyperparameters per sampler. The Best-of-N subsampling procedure equalizes the number of configurations evaluated per method, revealing that min-p's apparent advantage dissolves under fair comparison (Figures 4 and 5). This methodology is independently reusable for detecting cherry-picking in future comparisons.

- **Independent corroboration from the original authors' own new experiment (Section 2.4, Figure 3):** The original authors' new human evaluation study — conducted in response to this critique — also fails to show min-p outperforming baselines in quality, diversity, or quality-diversity tradeoff, providing convergent evidence from an independent experimental design.

- **Documented retraction of community adoption claims (Section 5):** The paper verifies that the original claims (1.1M GitHub stars, 54k repositories) cannot be substantiated — the combined stars of 8 major LM repositories total only 453k — and that the original authors retracted both figures from the Camera Ready. Crucially, 3 of 4 original reviewers and the area chair cited these figures as major justification for their endorsement.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **GPQA benchmark gap (Section 3):** The NLP benchmark reanalysis covers only GSM8K CoT, not GPQA (the other benchmark in the original paper), due to compute budget constraints. The paper is transparent about this, but the original claim "min-p achieves superior performance across benchmarks" is only partially refuted. The paper should either explicitly limit its benchmark-level conclusions to GSM8K or note what additional evidence would be needed for GPQA.

- **Section 4.3 selective-reporting framing:** The allegation that Table 3(b) of the original paper "appear[s] to have reported results inconsistently" rests on a Telegram link from the first author disclosing specific win-rate values (52.01 vs. 50.14 for min-p; 50.07 vs. 50.43 for top-p). The underlying numbers are specific and verifiable, making it a real inconsistency worth reporting. However, the inference of intentionality is not demonstrated. The section would be stronger if framed unambiguously as "an inconsistency in reporting that requires explanation" rather than implying motivated selective reporting.

### Trivial

- **"Ongoing work to publish" citation in Section 4.2:** The sentence "Closely scrutinizing (ongoing work to publish) the data revealed two more insights" references unpublished work from what appears to be the same group as supporting context. Referencing unpublished ongoing work in a submitted manuscript is methodologically awkward. This should either be incorporated as a self-contained contribution or the parenthetical removed.

- **"Blueprint" framing in the title and abstract slightly oversells the methodological contribution.** The six lessons in Section 6 — while grounded in the case study and useful — are largely consistent with established statistical best practices (Bonferroni correction, full data release, etc.). The genuine novelty is the Best-of-N methodology; the remaining lessons are restatements of existing standards. The "blueprint" label risks underselling the concrete contributions by suggesting the lessons are more novel than they are.

---

## Nice-to-Haves

- The Best-of-N hyperparameter equalization procedure (Section 3.1) is the paper's most independently reusable contribution. Presenting it as a brief self-contained specification — perhaps a short algorithm box — rather than embedding it entirely within the min-p case study would increase its accessibility for researchers who want to apply it in other contexts.

- A short analytical paragraph in Section 6 distinguishing error types (honest oversight vs. careless statistical practice vs. motivated reasoning) would sharpen the "blueprint" framing. The paper documents *what* went wrong in each case but not *what type* of error it is, which would help researchers recognize similar risks in their own work.

- If compute permits, extending the GSM8K sweep to GPQA (which has fewer examples) would complete the benchmark case and close the remaining gap.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: IUT is "more demanding than the claim requires."** The paper's use of an Intersection-Union Test alongside Bonferroni correction is technically defensible — the original paper's word "consistently" across "all settings" is precisely what the IUT tests. The Bonferroni correction alone is sufficient to make the point, but adding the IUT is not wrong and does not weaken the paper's argument. Removed as a substantive weakness.

- **Harsh critic: Possible transcription error 7.80 vs 5.80 in Table 15 (Section 2.4).** The paper raises this as an apparent reporting discrepancy in the new human evaluation data. Given that the appendix (and the table in question) are stripped from the parser output, this cannot be independently verified here. The paper raises it briefly without elaboration; it is a detail in secondary data and does not affect any core conclusion. Removed as insufficiently evidenced from the available text to constitute a real weakness.

- **Strength Finder: "Section 4.3 documents selective reporting as a concrete evidence of evaluative bias."** This is accurate as a factual description of what Section 4.3 claims, but since the selective-reporting allegation has been demoted to Minor (on grounds of speculative intent), treating it as an unambiguous strength would be inconsistent. Downgraded.

- **Harsh critic: The paper doesn't analyze *why* each error arose (taxonomy of error types).** This is a reasonable nice-to-have suggestion. Moved to Nice-to-Haves rather than treated as a weakness, since the paper's scope is to document and analyze the errors, not to psychologize their origin.

---

## Novel Insights

The Best-of-N hyperparameter equalization procedure introduced in Section 3.1 is the paper's most transferable methodological contribution. By subsampling equal numbers of hyperparameter configurations across all competing methods and tracking the maximum achievable score as a function of N, the method provides a principled, model-agnostic way to disentangle method quality from hyperparameter search effort — a confound that is pervasive in empirical ML comparisons but rarely controlled for explicitly. The finding that the entire apparent advantage of min-p on GSM8K CoT is accounted for by its having more tunable hyperparameters (min-p has a threshold parameter beyond temperature; basic sampling does not) is a striking and generalizable result: it suggests that the field routinely conflates richer hyperparameter families with better inductive biases. The paper also demonstrates, perhaps inadvertently, that the original peer review process can be substantially swayed by unverified quantitative claims (1.1M stars cited by 3 of 4 reviewers), which motivates stronger norms for verification of impact claims during review.

---

## Suggestions

1. Add a self-contained algorithmic description of the Best-of-N procedure to maximize its reuse by future reviewers and authors.
2. Add an explicit statement in the benchmark conclusions section limiting the claim to GSM8K (since GPQA was not run), or attempt GPQA if compute is available.
3. Revise Section 4.3 to frame the finding as "an inconsistency requiring explanation" rather than "apparent selective reporting," to match the strength of the available evidence (specific numbers from a Telegram message, not a documented internal selection procedure).
4. Remove or incorporate the "ongoing work to publish" parenthetical in Section 4.2.
5. Consider renaming or reframing the "blueprint" label to foreground the Best-of-N methodology as the genuinely novel contribution; the remaining six lessons can be described as validated best practices rather than novel discoveries.

---

## Assessment on Key Axes

- **Originality:** High. The Best-of-N hyperparameter equalization is a novel and reusable procedure. The paper type (documented, evidence-based critique with original experiments) is rare and valuable.
- **Importance of research question:** Very high. The paper directly addresses the credibility of a high-visibility result and, more broadly, the validity of common evaluation practices in empirical ML.
- **Claims well-supported:** High. The core factual claims (omitted data, statistical misapplication, retracted community metrics) are documented facts confirmed by the original authors. The benchmark claim is partially supported (GSM8K only). The LLM-judge section is the weakest but appropriately hedged.
- **Soundness of experiments:** High. The hyperparameter sweep is large-scale, computationally intensive, and includes robustness checks (corrected prompt formatting yielding nearly identical results). Statistical methods are applied correctly and transparently.
- **Clarity of writing:** High. The paper is well-organized, with each section corresponding to one line of evidence and a clear summary of findings. Limitations are explicitly acknowledged.
- **Value to the research community:** Very high. Both the specific finding (min-p's evidence base does not hold up) and the general methodology (Best-of-N, multiple comparisons corrections, data transparency requirements) will benefit reviewers, authors, and practitioners.

---

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>5</community_value>
</subscores>
## Summary

This paper demonstrates that aggregate correlation metrics (Krippendorff's-α, Spearman's ρ, etc.) between human and machine labels can be systematically misleading when human uncertainty varies across items. The authors stratify by human agreement levels across NLI, summarization, and preference datasets, showing that machines appear to correlate with humans *better* than humans correlate with each other on uncertain samples, but perform substantially *worse* on samples where humans fully agree. They propose a binned Jensen-Shannon Divergence metric (JS_b) and perception charts as supplementary tools, and recommend stratification as standard practice.

## Strengths

- **Stratification finding is empirically robust and practically important.** Tables 1–3 consistently show across three LLMs (Sonnet, Mistral, Llama), three task types (NLI, summarization, preference), and multiple metric families (Krippendorff's-α, % Agreement, Fleiss-κ, Randolph's-κ) that Δ = HH − H^wM^w is large and positive on perfect-agreement items but flips sign on high-uncertainty items. For example, SNLI PA=1: Δ=0.31 (HH dominates); SNLI PA<0.8: Δ=−0.34 (HM appears to surpass HH). This is a clear, reproducible demonstration of the artifact.

- **Random labeler simulation (Fig. 2) provides a clean minimal causal demonstration.** The simulation strips away LLM-specific confounds and shows that the artifact is a general property of correlation metrics under uncertainty: even a random labeler can appear to agree with the human majority when humans disagree. This directly supports the paper's central claim about stratification being necessary.

- **Theoretical grounding for why IRA metrics are mismatched for HM comparison (§2.2) is well-argued.** The observation that Krippendorff's-α requires raters to be treated as interchangeable (which humans and LLMs are not) and assumes "agreement is good, variance is bad" (inappropriate when human variation is a feature of perception-based tasks) provides a principled motivation for the paper's contributions.

- **Perception charts (Fig. 3–4) reveal concrete, actionable deficiencies that aggregate correlations conceal.** For example, Mistral achieves Krippendorff's-α of 0.49 on coherence, but the chart shows it "does not rate any item as 1 and negligible amount of items are rated 5, while humans have assigned over 24% of the items a median rating of 5" (line 275) — a range compression bias invisible in the single correlation number.

## Weaknesses

### Major

- **The proposed JS_b metric is presented as a contribution but is under-validated.** The paper reports JS_b values alongside other metrics in Tables 2–3, but never demonstrates that JS_b is *less* affected by the uncertainty artifact than standard metrics. The reader cannot tell: (a) Does JS_b remain stable when the proportion of uncertain samples changes? (b) Does it correctly identify cases where machines are genuinely poor (PA=1 rows)? (c) What does a JS_b of 0.13 mean — there is no calibration or reference values. A controlled simulation varying uncertainty levels and comparing JS_b against standard metrics is the minimal evidence needed but is absent. The paper also does not clearly address what JS_b adds over the simple stratification analysis it already performs (reporting per-stratum correlations), which already addresses the core problem. Since JS_b is one of three stated contributions, this gap weakens the paper's methodological novelty.

- **No statistical uncertainty quantification for any correlation estimate.** The paper reports single-point estimates for each stratified group. Several subgroups are very small (MT-Bench partitions with 11–26 samples, NLI "unique=3" groups with 2–3% of 10K samples ≈ 200–300 items but with 5 labels exhibiting maximum disagreement). Krippendorff's-α computed on such groups has very wide confidence intervals. The paper acknowledges resampling as a future direction (line 309) but does not compute any bootstrap CI, standard error, or significance test. This undermines confidence in whether the observed subgroup differences are real or within noise, especially for the smallest partitions where the paper's claims rely on the pattern of Δ sign changes.

### Minor

- **The stratified correlation finding is not connected to the well-known Simpson's paradox phenomenon.** The aggregate-versus-subgroup reversal shown in Tables 1–3 is a textbook instance of Simpson's paradox (aggregate trends differ from subgroup trends when subgroup sizes and effect sizes vary). Acknowledging this connection would situate the finding in established statistical theory and help readers understand *when* the artifact should be expected. The current framing implies the phenomenon is more surprising and novel than it is.

- **The random labeler simulation (Fig. 2) is rhetorically effective but the analogy to LLM behavior is imprecise without qualification.** The paper's LLMs are not random — they have uniformly high MM correlation (0.93–0.98 across all conditions, visible in Table 1). A machine that systematically agrees with one faction of humans or systematically disagrees in a structured way behaves differently from a random labeler. The paper already discusses systematic vs. random error (line 48, 304), but does not connect this distinction to the simulation, leaving the implication that LLM results in uncertain subgroups are "essentially random" when the high MM correlation suggests a different mechanism (systematic, reproducible machine judgments that diverge from humans on hard items).

- **JS_b requires many machine labels per item (20 in this paper, line 78) and bins by human median, which may obscure item-level discrepancies.** The paper acknowledges this limitation (line 261) but does not explore its practical consequences — for instance, whether 20 samples is sufficient to form reliable distributions, or how the metric behaves with fewer samples (which is the more common setting for automatic evaluation).

### Trivial

- None. The paper is well-structured and the writing is clear.

## Nice-to-Haves

- A discussion of the high MM correlation vs. varying HH correlation pattern visible in Table 1: machines agree with each other far more than humans agree on the same items. This observation could strengthen the systematic-vs-random-error framing.
- A simpler summary table showing just the PA=1 and low-PA rows with fewer metrics to visually emphasize the core pattern.

## Removed Points

- *"Tables are too dense/use too many colored highlights"* — Removed per hard rules: formatting/style nitpick.
- *"JS_b changes the question from per-item agreement to distributional resemblance"* — Removed: the paper explicitly frames JS_b as a supplement (line 247, 260), and distributional comparison is a reasonable alternative; the criticism is scope-creep.
- *"MM correlation left unexplored"* — Moved to Nice-to-Haves: it is a valid observation but more of a suggestion than a weakness.
- *"Not technically novel / perception charts are just grouped distribution plots"* — Removed: novelty is not the claim; the paper presents them as interpretability tools, and their pedagogical value is demonstrated concretely (line 275).
- *"No discussion of Simpson's paradox"* — Demoted to Minor (it is a useful connection, not a flaw in the paper's logic).
- *"The paper should accept..." etc. from Strengthening section* — Removed: these are revision suggestions, not weaknesses or strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension the paper does not fully resolve: the core empirical finding (stratification by human uncertainty reveals a systematic artifact in aggregate HM correlation) is solid and field-implicating, but the proposed remedy (JS_b) is under-developed relative to the ambition. The harshest critiques (Simpson's paradox connection, random labeler analogy imprecision) do not undermine the central finding but clarify its scope.

## Suggestions

1. **Explicitly validate JS_b** via a controlled simulation: vary the proportion of uncertain samples, introduce a known-good and known-poor machine labeler, and show that JS_b recovers the correct ranking more reliably than aggregate correlation or simple stratification.
2. **Add uncertainty quantification** — at minimum, bootstrap confidence intervals for the correlation estimates in each stratified group, especially for the small subgroups (MT-Bench partitions). This would substantially strengthen the paper's empirical rigor.
3. **Acknowledge the Simpson's paradox connection** explicitly to help readers understand when the artifact is expected and to avoid over-claiming surprise.
4. **Clarify the relationship between the random labeler simulation and the LLM results** by noting that high MM correlation (systematic behavior) distinguishes LLMs from a truly random labeler, and that the simulation serves only to illustrate the statistical mechanism in its simplest form.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
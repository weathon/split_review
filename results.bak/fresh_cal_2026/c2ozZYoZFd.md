Now I have all the verification I need. Let me write the final consolidated review.

## Summary

This paper presents a detailed case-study re-analysis of the ICLR 2025 Oral min-p sampling paper (Nguyen et al., 2024), systematically examining four lines of evidence the original paper used to support its claims. The authors show that human evaluations omitted one-third of the data and applied incorrect statistical tests, that min-p's NLP benchmark advantage disappears when controlling for hyperparameter tuning volume (via a novel Best-of-N methodology), that the LLM-as-a-Judge evaluation was methodologically under-specified and appears inconsistently reported, and that community-adoption claims were unsubstantiated and retracted. The paper distills general lessons for rigorous empirical ML research.

## Strengths

- **Novel Best-of-N hyperparameter-control methodology (Section 3.1, Figures 4–5):** The paper introduces a principled subsampling approach that equalizes the number of hyperparameter configurations searched across different samplers. Across 9 models, 31 temperatures, 6 hyperparameters per sampler, and 3 seeds (~6000 A100-hours), this analysis shows min-p is indistinguishable from baselines when hyperparameter tuning volume is controlled. This is a reusable methodological contribution beyond the case study itself.

- **Rigorous statistical re-analysis of human evaluations (Section 2, Table 1, Figure 1):** The paper corrects the original's failure to adjust for multiple comparisons, applies proper Bonferroni correction and an Intersection-Union Test, and visualizes data with 95% confidence intervals. After correction, only 1 of 12 comparisons remains significant (IUT p = 0.378), directly contradicting the original claim of consistent superiority.

- **Discovery of omitted data and mischaracterized qualitative feedback (Sections 2.1, 2.3, Figure 2):** The paper identifies that one-third of human evaluation scores (basic sampling) were excluded without justification and shows through manual annotation that basic sampling was actually preferred over min-p by human evaluators — a finding the original paper's qualitative summary inverted.

- **Verification and documentation of retracted community-adoption claims (Section 5):** The paper concretely demonstrates that the claimed 54k GitHub repositories and 1.1M stars are unsupported (major LM repositories sum to ~453k stars), and the original authors subsequently retracted these numbers from the camera-ready version. This is a clean, independently verifiable debunking.

- **Generalizable lessons (Section 6):** The paper distills six actionable lessons (controlling for hyperparameter volume, correcting for multiple comparisons, data transparency, scrutinizing qualitative summaries, methodological clarity, watching for selective reporting) that transfer beyond this single case study.

## Weaknesses

### Fatal

None.

### Major

- **Selective-reporting claim (Section 4.3) relies on non-archived evidence:** The paper states that the first author "publicly shared a Telegram link" showing differential score reporting for min-p vs. top-p, but no URL, screenshot, or archived pointer is provided. This is a serious allegation (inconsistent/selective reporting) that would ideally be backed by a citable, stable record. The rest of the LLM-as-a-Judge critique (under-specified methodology in Section 4.1, unequal hyperparameter tuning in Section 4.2, Figure 6) is well-supported by public repository data, so the overall case does not collapse without this claim. However, the paper should either archive the evidence or soften the claim's framing to reflect its current evidential basis.

### Minor

- **NLP benchmark re-analysis covers only GSM8K (Section 3):** The thorough hyperparameter sweep is restricted to GSM8K CoT (albeit with two prompt formats). The original paper also reported GPQA, and the paper's abstract states "Extensive hyperparameter sweeps on NLP benchmarks show min-p's claimed superiority vanishes" — a conclusion that would be strengthened by adding at least one more benchmark. The authors acknowledge this limitation and cite compute budget, but the generality of the counterclaim is somewhat circumscribed.

### Trivial

- **Annotations mentioned as "publicly posted" without link in main text (Section 2.3):** The paper states that qualitative annotations were "publicly posted in the same format" but the link is not visible in the main text (likely in the appendix/references, which are stripped by the parser). A few concrete URLs in the main body would improve transparency.

## Nice-to-Haves

- **Complementary mean/median analysis in Best-of-N (Section 3.1):** The Best-of-N analysis uses the *maximum* Exact Match, which is sensitive to outliers. Adding mean or median with error bars as a complementary view would strengthen the already-convincing results.
- **Brief discussion of regimes where min-p might still be useful:** The paper currently says "While `min-p` is useful as another method to try" but does not elaborate. A short paragraph on whether min-p has any niche where it excels (e.g., specific model families, temperature ranges) would add balance.

## Removed Points

- **"No explicit reproducibility statement" (harsh critic):** The paper states annotations are "publicly posted" and uses publicly available data/code from the original paper's repository. This is a minor presentation preference, not a substantive gap. Moved to Trivial.
- **"Telegram link cannot be independently verified" framed as questioning existence:** The criticism is about evidential quality, not about whether the link existed. Kept as Major with adjusted framing to focus on the lack of citable archival evidence rather than questioning existence.
- **Strength Finder's generic/self-evident strengths kept:** All listed strengths are specific, evidenced, and directly tied to paper content. None removed for being superficial.

## Novel Insights

The harsh critic's framing of the Telegram-evidence issue as a tension between making a valid methodological observation and the standards of evidence required for serious allegations is a useful meta-point. The paper is strongest where its evidence is independently reproducible (the human evaluation data re-analysis, the Best-of-N sweep, the GitHub stars verification) and weaker where it relies on unarchived communication. This observation — that the weakest link in an otherwise meticulously evidence-based critique is an evidential-standard gap — is itself a demonstration of the paper's own blueprint: the same rigor the paper demands of others should be applied to its own claims.

## Suggestions

1. Archive the Telegram communication (or an equivalent independent verification of the selective reporting claim) in a permanent repository (GitHub, Zenodo, screenshot) and cite it directly. If archiving is not possible, reframe the claim from "the authors selectively reported" to "the public data are consistent with selective reporting" and note the source as unarchived.
2. Extend the NLP sweep to at least one more benchmark (GPQA would be the natural choice given the original paper) to reduce the risk that the GSM8K results are task-specific.
3. Add URLs in the main text for the posted annotations and re-analysis code to improve transparency and reproducibility.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing (queries on re-analysis / critique papers):**

| Path | Avg Score | Round | Comparison to current paper |
|------|-----------|-------|-----------------------------|
| UKPDpKGXAi (EEG confound) | 2.00 | 1 | Weaker: limited scope, small experiments, poor presentation |
| 1CR1MTIgmq (false statements) | 0.00 | 1 | Much weaker: attack piece without scientific contribution |
| pc3cyrqNFV (battery prognostics) | 2.80 | 1 | Weaker: narrow scope, limited experiments |
| NbdCwOgk4m (hyperparameter tuning) | 4.00 | 1 | Weaker: single model size, limited evidence |
| Q7mLKxQ8qk (fast HP transfer) | 6.50 | 1 | Comparable: similar thoroughness, accepted as poster |
| VKGTGGcwl6 (LLMs multi-turn) | 8.00 | 1 | Stronger: broader scope, more extensive experiments |

**Round 1 bracket:** [5, 7]

**Round 2 — Narrowing within bracket (queries in [4.5, 6.5] and [6, 7.5]):**

| Path | Avg Score | Round | Comparison to current paper |
|------|-----------|-------|-----------------------------|
| NrSx6J6IZk (benchmark influence) | 5.00 | 2 | Weaker: less rigorous experiments, rejected |
| dlaNQM6YbZ (flaw of averages) | 4.50 | 2 | Weaker: more limited scope, rejected |
| ZHKVPkJMSI (How NOT to benchmark) | 6.00 | 2 | Comparable/slightly weaker: similar critique paper, accepted poster, but this paper has more thorough re-analysis and novel methodology |
| mq6GMkoGjh (EchoBench) | 6.00 | 2 | Different type (new benchmark), comparable overall quality |
| HyZwf1rt4s (AI review detection) | 6.00 | 2 | Different type (new dataset), comparable quality |
| tAM9SGoEmD (SafeMVDrive) | 6.00 | 2 | Different topic, comparable score |
| Wz0ILlbh9U (Temporal Generalization) | 7.00 | 2 | Slightly stronger: broader experimental coverage across 6+ tasks, accepted poster |

The paper under review sits between the "How NOT to benchmark" paper (6.0, accepted poster) and the "Temporal Generalization" paper (7.0, accepted poster). It is more methodologically novel (Best-of-N) than the former but narrower in benchmark coverage than the latter. The two fixable weaknesses (Telegram evidence, GSM8K-only) prevent it from reaching the 7+ tier but do not undermine its core contribution.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>
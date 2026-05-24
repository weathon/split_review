Now I have sufficient calibration data. Here is my consolidated final review.

---

## Summary

This paper presents a detailed case-study critique of the min‑p sampling paper (Nguyen et al., 2024, ICLR 2025 Oral), re-examining all four lines of evidence the original work used to claim min‑p's superiority. The re-analysis finds that: (1) human evaluations omitted one‑third of collected data (basic sampling scores), applied incorrect statistical tests, and mischaracterized qualitative feedback; (2) extensive GSM8K hyperparameter sweeps with a Best‑of‑N analysis show min‑p does not outperform baselines when controlling for tuning volume; (3) the LLM‑as‑a‑Judge evaluations suffer from methodological under‑specification and appear to have been reported inconsistently; and (4) the claimed community adoption numbers (54k repositories, 1.1M stars) were unsubstantiated and subsequently retracted. From this case study the paper distills six general lessons for more rigorous empirical ML research.

## Strengths

1. **Thorough, transparent re‑analysis of original human evaluation data.** The paper obtains the original data, documents the exclusion of basic sampling scores (1/3 of all collected responses), applies correct paired t‑tests with Bonferroni correction (Table 1), and conducts an Intersection‑Union Test — all clearly explained. The discovery of a likely misreported value (7.80 → 5.80) in the new human study further strengthens this section. This alone substantially undermines the original paper's central human‑evaluation claim.

2. **Discovery and documentation of the retracted community adoption claims.** Section 5 shows that the sum of stars across major LM repositories (453k) is less than half the claimed 1.1M, and that searching "min‑p" on GitHub yields many false positives. The authors publicly retracted these numbers from the camera‑ready manuscript. Because this evidence swayed reviewers, the retraction is consequential.

3. **Large‑scale controlled hyperparameter sweep with Best‑of‑N analysis.** The paper runs ~6000 A100‑hours of experiments (9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds) and applies a subsampling analysis that equalizes hyperparameter tuning volume across methods (Figs. 4‑5). This provides a reproducible template for fair method comparison and shows that min‑p does not reliably outperform top‑p, top‑k, or basic sampling.

4. **Methodological criticism of the LLM‑as‑a‑Judge evaluation (indirect comparisons, intransitivity, unequal tuning).** Section 4 correctly identifies that the original paper compared all methods indirectly against a fixed baseline (basic at τ=1.0) rather than directly, and that recent work (Xu et al., 2025) shows LLM‑judge preferences are not transitive. Figure 6 (left) compellingly visualizes that min‑p received 2–10× more hyperparameter tuning than baselines.

## Weaknesses

### Fatal
None.

### Major

- **The selective‑reporting accusation (Section 4.3) is insufficiently documented.** The paper claims that a Telegram link shows the higher of two win rates was reported for min‑p (52.01 vs. 50.14) but the lower for top‑p (50.07 vs. 50.43). No screenshot, full table, or archival snapshot of this Telegram data is provided. This is a serious allegation (intentional selective reporting), and the evidentiary bar should be higher. The paper should either provide a reproducible archive of the source data or moderate the claim to note the inconsistency without implying intent. The rest of the LLM‑as‑a‑Judge critique (indirect comparisons, intransitivity, unequal tuning) stands independently, but this specific point weakens the overall section.

### Minor

- **NLP analysis is limited to GSM8K CoT.** The original paper's most distinctive claims about min‑p's quality‑diversity tradeoff apply to creative writing, evaluated through AlpacaEval and human judgments. The current re‑analysis covers only a math reasoning benchmark. The paper explicitly acknowledges the compute limitation (~6000 A100‑hours), and the main critique does not depend on this section, but the title "Extending min‑p's NLP Benchmark Evaluations" overstates the scope. The conclusions about the NLP evidence should note this constraint more prominently.

- **Only 3 random seeds are used in the hyperparameter sweep.** While the total compute budget is large, the use of only 3 sampling seeds ({0, 1, 2}) increases variance in the results. A sensitivity analysis with more seeds for a subset of configurations would bolster confidence that the Best‑of‑N findings are not artifacts of seed choice.

- **The claim that "3 of 4 ICLR 2025 reviewers and the Area Chair identified these retracted community adoption numbers as the main justification for their strong endorsement" is stated without citation or direct documentation.** This is not central to the paper's methodological contributions, but it is a strong factual assertion about the original review process that the paper does not support with publicly accessible evidence.

### Trivial
None.

## Nice-to-Haves

- Including a small‑scale creative‑writing evaluation (e.g., LLM‑as‑a‑Judge on AlpacaEval or a similar task) would directly address the domain where min‑p's claimed advantages are most distinctive. This is acknowledged as a compute‑budget issue and is not a core flaw.
- A sensitivity analysis of the Best‑of‑N framework using alternative hyperparameter ranges (beyond those taken from the original paper) would address a natural concern about the fairness of the chosen sets.
- Direct pairwise comparisons in the LLM‑as‑a‑Judge analysis (rather than the indirect‑comparison setup) would strengthen the empirical evidence in Section 4.

## Removed Points

These points were flagged by the reviewers but removed from the main review after cross‑checking against the paper:

- **"Hyperparameter ranges differ between min‑p and top‑p, potentially biasing the Best‑of‑N analysis."** — The paper explicitly states the values were "taken from the original paper; some were lightly edited to make them more evenly distributed." Since the values originate from the original work being critiqued, this is not an unfair choice but a faithful and transparent replication. Removed.
- **"The selective‑reporting claim relies on an external Telegram link that may have been updated."** — The paper reports specific numbers from that link. The weakness about documentation quality is retained (see Major above), but the speculation about the link being updated is not grounded in anything on the page. Removed.
- **Various presentation/formatting nitpicks** — These are parser artifacts or are not substantive.
- **Strength Finder's generic strengths about the problem being "important" or "interesting."** — Generic praise without specific content. Removed.
- **Strength Finder's claim that the selective‑reporting documentation is itself a strength.** — It is partially undermined by the documentation issue noted above; the rest of the LLM‑as‑a‑Judge critique (indirect comparisons, intransitivity, unequal tuning) is valid and retained as a strength.

## Novel Insights

The harsh critic and strength finder largely recapitulate the paper's own contributions rather than adding new interpretive synthesis. The one observation worth highlighting is that the paper illustrates a recurring pattern in replication/critique studies: the strongest refutation comes not from new experiments but from careful re‑examination of the original data (omitted conditions, misuse of statistics, unverifiable claims). This meta‑insight, which the paper itself develops into its six lessons, is more valuable than the specific min‑p finding and could meaningfully shape reviewer training.

## Suggestions

1. **Document the selective‑reporting evidence more carefully.** Archive the Telegram data (screenshot or extracted table), provide the full set of win rates for all hyperparameter values of min‑p and top‑p, and clearly contrast what was reported vs. what was available. Alternatively, moderate the language to describe the inconsistency without alleging selective intent.
2. **Acknowledge the GSM8K‑only scope more explicitly in the title and abstract of Section 3.** The paper currently frames this as "extending" the original NLP evaluation; "partially extending" or "re‑analyzing on GSM8K" would be more precise.
3. **Add a small‑scale seed‑sensitivity check.** Re‑run a representative subset of configurations (e.g., 2 models × 2 temperatures × all samplers) with 10–20 seeds to confirm that the 3‑seed results are representative.
4. **Remove or substantiate the assertion about 3/4 reviewers and the AC.** If the ICLR review comments are publicly accessible, cite them. Otherwise, drop this claim as it is not needed to make the retraction impactful.
5. **Cite the Best‑of‑N precursors more explicitly.** The paper already cites Nakano et al. (2021) and Stiennon et al. (2020) in Section 3.1, but the harsh critic correctly notes the Discussion could cite them more prominently when presenting Best‑of‑N as a methodological contribution.

## Score and Decision

**Calibration anchors** (all paths relative to `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `FBkpCyujtS.md` (min‑p original paper) | 8.50 | The original min‑p paper accepted as Oral. The current paper directly refutes it. Different genre (original method vs. critique), so direct comparison is limited, but the critique paper's evidence is thorough. |
| `lf8QQ2KMgv.md` (memorization critique) | 3.75 | A replication/critique paper that was rejected. Had more methodological ambiguity and weaker evidence than the current paper. The current paper's findings (data omission, statistical errors, retracted claims) are more objective and conclusive. |
| `GbEmJmnQCz.md` (memorization critique v2) | 4.40 | Another replication/critique paper that was rejected. Reviewers raised concerns about insufficient replication of key analyses. The current paper does a more complete job of re‑examining all lines of evidence. |
| `m2NVG4Htxs.md` (data contamination) | 6.75 | A well‑received rigorous analysis paper (accepted). Similar in empirical rigor to the current paper's human evaluation re‑analysis. Both make a clear, evidence‑based case. |
| `E8gYIrbP00.md` (human uncertainty in evaluation) | 6.75 | An accepted paper critically examining evaluation methodology. Comparable genre and quality to the current paper — both identify methodological flaws in common practices. |
| `7W3GLNImfS.md` (human feedback not gold standard) | 6.50 | An accepted critique paper about human evaluation confounders. Similar rigor and impact. The current paper is slightly stronger in specificity of its findings (documented data omission, retraction). |
| `Tigr1kMDZy.md` (overthinking the truth) | 7.33 | High‑scoring accepted paper with novel findings. The current paper has less mechanistic novelty but equivalent empirical rigor. |
| `JDud6zbpFv.md` (quality‑diversity) | 8.00 | An accepted paper with a novel method and clean experiments. The current paper is in a different genre (critique vs. method proposal), but both demonstrate careful experimental practice. |

The current paper makes a well‑supported critique with one genuinely strong section (human evaluations) and one clearly documented factual finding (community adoption retraction). The NLP and LLM‑as‑a‑Judge sections are weaker but not essential to the core argument. The weaknesses identified are addressable and do not undermine the central claims. Compared to the memorization critique papers that scored in the 3–4 range and were rejected, this paper has clearer, more objective findings and fewer methodological disagreements. Compared to accepted critique/analysis papers scoring 6.5–7.0, it is of comparable quality with slightly uneven execution across sections (very strong human evaluation section, weaker selective‑reporting documentation).

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>
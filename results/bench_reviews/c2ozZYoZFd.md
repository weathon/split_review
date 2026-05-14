## Summary
This paper is a detailed case-study critique of Nguyen et al. (2024)'s "Turning Up the Heat: MIN-P Sampling" (ICLR 2025 Oral). The authors re-analyze the original work's four lines of evidence — human evaluations, NLP benchmarks (GSM8K CoT, with a ~6000 A100-hour sweep), LLM-as-judge results, and community-adoption claims — and argue that none support min-p's claimed superiority. From this case study they distill six general "blueprint" lessons for more rigorous empirical ML research.

## Strengths
- The re-analysis of the human-evaluation data is substantive and well-documented: the paper identifies that one-third of the collected scores (basic sampling) were omitted from the original Table 4 (Sec. 2.1, confirmed by the original authors), shows that the pooled single t-test was inappropriate given the cross-condition heterogeneity (Sec. 2.2), and correctly applies Bonferroni and an IUT framing (Table 1). After correction, only 1 of 12 tests is significant at α=0.05.
- The Best-of-N hyperparameter-volume controlled comparison (Sec. 3.1, Figs. 4–5) is a clean operationalization of "fair tuning budget" and is backed by a real sweep across 9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds (~6000 A100-hours). It directly demonstrates that min-p's apparent gains shrink to near-zero when each sampler is allowed equal tuning budget.
- The manual re-annotation of the qualitative free-text responses (Fig. 2) is a concrete demonstration that paper-level qualitative summaries can be checked against, and contradicted by, the underlying raw data.
- Sec. 4.2 documents a concrete tuning-budget asymmetry (~2× vs top-p, ~10× vs basic) in the LLM-as-judge experiment, and Sec. 5 documents that the headline 54k repos / 1.1M stars adoption numbers were retracted from the camera-ready after the authors' inquiry — a verifiable, factual finding.

## Weaknesses

### Fatal
None — the central technical claims (omitted basic-sampler data, mis-pooled t-test, retracted adoption numbers, tuning-budget asymmetries) are documented against the original paper's own released data.

### Major
- **The "blueprint" framing is over-generalized from n=1.** The abstract and Sec. 1 promise a "blueprint for more meticulous science" derived from a single high-visibility case. Sec. 6's six lessons (control for hyperparameter volume, correct for multiple comparisons, release data, scrutinize qualitative summaries, demand methodological clarity, watch for selective reporting) are presented as community-wide prescriptions but are supported by exactly one case. The paper is therefore in an awkward middle: too generalized to be cleanly framed as a focused replication/comment, and too narrow (one case) to support the "blueprint" claim. A multi-case meta-analysis, or a reframing as a critical replication, would resolve this.
- **The general "lessons" are largely restatements of established methodological norms.** Bonferroni correction, equivalence vs. non-rejection, reporting uncertainty, full data release, and avoiding selective reporting are textbook recommendations (and the paper itself cites Agarwal et al. 2021, the NLG-eval literature, etc.). The only arguably new methodological proposal is the hyperparameter-volume-controlled Best-of-N curve in Sec. 3.1 — and even that, as the paper notes, is an adaptation of long-standing Best-of-N analysis from RL (Nakano, Stiennon, Hughes, Schaeffer). The conceptual contribution beyond the case study is therefore thin.
- **The paper does not consistently apply the rigor it demands.** Two concrete examples: (i) the NLP-benchmark refutation is restricted to GSM8K CoT, while the original paper also evaluated GPQA; the abstract speaks of "NLP benchmark evaluations" (plural). A paper accusing others of single-benchmark fragility should at least extend to GPQA, or explicitly justify scope. (ii) Figs. 4–5 average over 150 subsampled draws but do not display confidence bands — yet Sec. 2 explicitly criticizes the original paper for failing to show uncertainty. The same standard should apply.
- **Non-rejection is read as equivalence.** The paper repeatedly slides from "we fail to reject min-p > baseline" to affirmative claims like "min-p offers no apparent advantage" / "samplers are indistinguishable" (Sec. 2.4). Proper equivalence testing (TOST, Bayesian equivalence) or reporting effect sizes with CIs would substantiate the symmetric claim; relying on non-rejection of one-sided nulls does not, and this is the same statistical lapse the paper criticizes elsewhere.

### Minor
- **One-cell evidence for "selective reporting" lesson.** Sec. 4.3 documents a single asymmetry (Table 3(b) reports the higher of two min-p scores and the lower of two top-p scores). This is a real finding, but generalizing it to blueprint lesson #6 ("watch for selective reporting") from one cell is weak. Checking the rest of Table 3(b) for the same asymmetric pattern would either strengthen or appropriately temper the claim.
- **Hyperparameter grid sensitivity is not analyzed.** The paper's grids are described as "lightly edited to make them more evenly distributed" (Sec. 3.1), but Best-of-N curves are sensitive to grid choice; a paper whose central methodological tool is hyperparameter-volume control should demonstrate robustness to its own grid.
- **Adversarial backstory is under-disclosed.** Phrases like "we publicly confirmed with the authors" and "the authors publicly told us" recur throughout. The paper's evidence is partly built on an adversarial public exchange with the original authors; making that context explicit (and, where applicable, summarizing the original authors' counter-positions) would let readers assess the dispute more symmetrically.

### Trivial
- The "18th highest-scoring submission" framing in Sec. 1 is rhetorical rather than scientific.
- Sec. 2.4's flagging of a possible 7.80 vs. 5.80 typo would be stronger if the supporting data extract were shown in the main text rather than asserted.

## Nice-to-Haves
- Extend the controlled sweep to GPQA and to at least one creative-writing/generation benchmark.
- Add equivalence tests (TOST) on the human-evaluation data to substantively support the "indistinguishable" claim.
- Add confidence bands on Figs. 4–5 over the 150 subsamples.
- Either reframe as a focused critical replication, or add at least one independent case study to back the "blueprint" framing.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- Harsh critic's framing that the paper "belongs as a comment/replication, not a standalone ICLR paper" — venue-fit is a soft judgment, partially valid but already captured in the over-generalization Major weakness above; left here to avoid double-counting.
- Strength-finder claim that the paper "models the behavior it advocates" by releasing data — generic and partially undercut by the verified Major weakness that the paper itself omits confidence bands and does not run equivalence tests.
- Generic strengths about the importance of rigor/reproducibility in ML — sycophancy-adjacent and not specific to this paper.

## Novel Insights
The most genuinely useful contribution is the operationalization of "fair tuning budget" via the hyperparameter-volume-controlled Best-of-N curve (Sec. 3.1, Figs. 4–5). While Best-of-N itself is borrowed from RL, applying it to detect inflated apparent gains from unequal hyperparameter search across competing decoding methods is a concrete, reusable diagnostic. The retraction of the 54k-repo / 1.1M-star adoption claim (Sec. 5) is also a useful object lesson about how unverified marketing-style numbers can disproportionately sway reviewers and ACs. Beyond these, the "blueprint" lessons are restatements of community norms.

## Suggestions
- Reframe the contribution: lead with the Best-of-N tuning-budget diagnostic as the methodological contribution, and present the min-p re-analysis as its case-study validation rather than as the basis for a community-wide "blueprint."
- Extend the controlled sweep to GPQA so the NLP-benchmark refutation does not itself rest on a single benchmark.
- Add TOST/equivalence tests and effect sizes with CIs to support "indistinguishable" claims symmetrically.
- Add confidence bands to Figs. 4–5 and a grid-sensitivity analysis for the Best-of-N curves.
- Disclose the adversarial public exchange in the manuscript and, where relevant, present the original authors' positions alongside.
- Check whether the Table 3(b) asymmetry generalizes across the rest of the table before promoting it to a general lesson.

## Score and Decision

**Anchor calibration** (every anchor returned, not only those read in full):
- `FBkpCyujtS.md` — avg 8.50 — *the very paper being critiqued (min-p original); accepted as Oral.* Not a direct comparable since this submission is its critique.
- `ejvf3JrZuC.md` — avg 4.25 — theory of LLM sampling, rejected; thinner empirical grounding than the paper under review.
- `tJHDw8XfeC.md` — avg 6.40 — MiniPLM (KD pretraining), accepted; standard methods paper with broader empirical coverage.
- `UXCfRU2Qs4.md` — avg 4.25 — LLMs as windows on psychopathology, rejected; weaker grounding.
- `55EO8gSCBT.md` — avg 5.50 — *"Experimental Design for Nonstationary Optimization"*, rejected; closest spirit-match (a methodology/experimental-design paper arguing for principled protocols). Comparable in scope and ambition; outcome on the boundary.
- `vyflgpwfJW.md` — avg 7.00 — DiscoveryBench, accepted; broader and more constructive contribution.
- `TY9mstpD02.md` — avg 3.50 — CriticAL, rejected; weaker.
- `9nUBh4V6SA.md` — avg 6.50 — Self-driving lab protocols, accepted; concrete framework contribution.
- `50P9TDPEsh.md` — avg 4.67 — Critique Ability of LLMs, rejected; weaker design.
- `GAXedKmbFZ.md` — avg 4.25 — Disco-Bench, rejected.
- `zpBamnxyPm.md` — avg 5.75 — "Why predicting downstream capabilities remained elusive", rejected on margin; another critical-empirical paper close in spirit and depth; useful upper anchor for this kind of contribution.
- `fj5SqqXfn1.md` — avg 5.00 — "Avoiding Pitfalls for Privacy Accounting", rejected; structurally similar (correcting community practice), comparable outcome.
- `LsZxlxA9da.md` — avg 4.00 — Boundless Socratic Learning position paper, rejected.
- `8QTpYC4smR.md` — avg 1.00 — LLM systematic review, clear reject; far weaker than the paper under review.
- `OXIIFZqiiN.md` — avg 1.50 — IGCP patch-analysis, clear reject; far weaker.
- `ICwdNpmu2d.md` — avg 1.50 — LLM stock prediction, clear reject; far weaker.
- `pf9J3GNxSe.md` — avg 4.50 — Phase transition in LLMs, rejected.

The paper under review is substantively stronger than the very-low anchors (1.0–1.5) and comparable to the closest spirit-matches — Experimental Design for Nonstationary Optimization (5.5), Avoiding Pitfalls for Privacy Accounting (5.0), and Why Predicting Downstream Capabilities Remained Elusive (5.75). It has stronger empirical work (~6000 A100-hours, full re-released data) than typical critique papers but suffers from genuine over-generalization (n=1 → "blueprint"), self-violation of its own stated standards (no CI bands, non-rejection-as-equivalence, single benchmark for the NLP leg), and thin novel methodology beyond the Best-of-N diagnostic. It does not rise to the 6.5–7.0 anchors (DiscoveryBench, self-driving labs) which present broader, more constructive frameworks.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
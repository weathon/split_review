## Summary

This paper studies the sensitivity of LLMs to prompt formatting choices (separators, casing, spacing, enumeration styles) that are claimed to be semantically equivalent. It introduces a grammar-based framework to define the space of plausible prompt formats, proposes a Thompson-sampling-based tool (FormatSpread) for efficiently estimating the performance spread over this space, and presents empirical measurements across several open-source and API-gated models on 50+ classification tasks from Super-NaturalInstructions. The core finding — that formatting alone can swing accuracy by up to 78 points on individual tasks (Table 1) and that the space is highly non-monotonic — is important and consequential for evaluation methodology in LLM research.

## Strengths

- **Concrete, extreme examples of format sensitivity.** Table 1 (lines 303–311) documents seven specific format pairs where a single-character change produces massive accuracy differences, including the standout case of task280 (removing two colons shifts LLaMA-2-13B from 0.043 to 0.826). These examples make the phenomenon tangible and falsifiable.

- **Clean non-monotonicity result.** The paper shows that 32.4% and 33.6% of atomic-change triples are monotonic for multiple-choice and non-multiple-choice tasks respectively (line 343) — essentially at the random baseline of 33.3%. This provides a rigorous justification for why local search algorithms are ill-suited for this space, and motivates the global bandit approach.

- **Well-specified grammar for the format space.** Section 3.1 (lines 65–113) defines the format space using Backus-Naur notation with explicit sets for separators, casing functions, itemizers, and spacing. This is more principled than ad-hoc perturbation, and it enables the paper's central claim about semantic equivalence to be precisely operationalized.

- **FormatSpread's efficiency advantage is clearly demonstrated.** With a budget of 51,200 evaluations, Thompson sampling estimates spread within 1 accuracy point of the true spread, versus 4 for naive sampling and 11 for UCB (line 391). This is a clean, practical result.

- **Sensitivity persists across scaling dimensions.** The scatter plots (Figures 2–4) and text (lines 187–190) show that spread does not shrink when moving from 7B→13B→70B parameters, from 1-shot to 5-shot, or from Falcon-7B to Falcon-7B-Instruct. This refutes the natural counter-hypothesis that these interventions would wash out formatting artifacts.

## Weaknesses

### Fatal

None. The paper's core methodology is sound and the phenomenon it documents is clearly real. The issues below are severe but stem from the paper's incomplete state and interpretive overreach, not from a fundamental invalidity.

### Major

1. **~35 `\tbdone` placeholders replace nearly every key quantitative result.** The following central numbers are missing from the manuscript as submitted:

   - Median spread of 7.5 accuracy points (line 186)
   - Model-reversal probabilities 0.141 and 0.140 (line 221)
   - Statistical significance percentages 76% and 47% (line 222)
   - Number of tasks used (lines 165, 292, 342, 350, 370, 378, 383, 394)
   - PCA correlation coefficients 0.424 and 0.555 (line 372)
   - ALL quantitative results for LLaMA-2-70B and GPT-3.5 (line 394 — a full paragraph of placeholders)

   A reader cannot verify the paper's headline claims because the supporting numbers are not on the page. While the paper does contain some real numbers (Table 1, the non-monotonicity percentages, the FormatSpread efficiency comparison), the claims that rely on placeholders are precisely the ones that would establish the paper's most provocative conclusions (model ranking reversals, PCA correlations, sensitivity of large models). This is not a minor formatting issue — it means the evidentiary support for several central claims is absent.

2. **The "semantic equivalence" / "spurious features" framing is asserted without adequate defense.** The paper repeatedly claims that formatting changes are "meaning-preserving" (lines 4, 15–16, 53–54, 101–103) and uses the term "spurious features" in the title. However, many of the variations in the grammar — ALL CAPS vs. lowercase descriptors, `:` vs `::` vs ` - ` separators, Roman numerals vs. letters — carry real distributional signals in the training data. A model that assigns different probabilities to `PASSAGE:` vs `passage:` is not necessarily behaving spuriously; it may be reflecting genuine linguistic patterns. The paper acknowledges this only in passing (line 96: "We intentionally only modify the casing of descriptors to guarantee semantic equivalence") without addressing the underlying objection. If the argument is that "a human annotator would find these equivalent," that is a different (and weaker) claim than the one the paper's title and framing advance. This matters because the paper draws strong normative conclusions about evaluation methodology ("researchers should report performance ranges") that depend on the "spurious" interpretation.

### Minor

1. **Scope is limited to classification tasks in few-shot settings, while the paper frames its conclusions broadly.** All 50+ tasks are classification or multiple-choice (lines 164–165), and evaluation is exclusively 1-shot or 5-shot. The title and abstract imply a general phenomenon about LLM sensitivity to prompt formatting, yet no generative tasks or zero-shot conditions are tested. The paper partially acknowledges this (line 121: "Due to ease in automatic evaluation, here we evaluate on classification tasks"; lines 431–433: "single-format evaluation may still be sufficient for many use cases"), but these qualifications appear too late and partially undercut the headline claims.

2. **No confidence intervals around spread estimates.** The "true spread" used to evaluate FormatSpread (line 389) is itself estimated from a sample of 500 formats evaluated on 250 samples each — not the infinite population. Given the paper's own non-monotonicity result, sampling variance across different sets of 500 formats is likely substantial. Without bootstrapped confidence intervals or similar uncertainty quantification, the reader cannot assess how stable the reported estimates are.

3. **Missing random search baseline for FormatSpread.** FormatSpread is compared to UCB and naive sampling but not to simple random search (drawing formats uniformly at random with the same budget). This would be a natural baseline for a highly non-monotonic space where bandit algorithms may offer no advantage. The paper's own non-monotonicity finding makes this omission more notable, not less.

4. **PCA analysis adds little to the core argument.** Showing that format identity is decodable from prompt embeddings with ≥0.98 accuracy (line 370) is unsurprising — different token sequences necessarily produce different embeddings. The claimed correlation with spread (r=0.424, line 372) uses a `\tbdone` placeholder and, even if present, the interpretive direction is unclear (does format identifiability cause performance variance, or do both stem from a common underlying property?). This section feels exploratory rather than evidential.

### Trivial

None.

## Nice-to-Haves

- A zero-shot condition would substantially strengthen the generality claims. If sensitivity is smaller or absent in zero-shot, the paper's real finding is about ICL dynamics, not formatting per se.
- Reporting compute costs for LLaMA-2-70B experiments would be useful for practitioners considering FormatSpread.
- Comparing FormatSpread against simple random search (uniform over formats with the same evaluation budget) would strengthen the tool validation.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper:

- **Formatting artifacts** (orphaned fragments, stray braces, broken characters). These are PDF extraction artifacts, not problems in the original submission. Removed per rule.
- **"Paper is not in a publishable state" as a structural/readability claim.** The specific \tbdone issue is real and retained as Major weakness 1. But claims about general brokenness conflate parser artifacts with author errors. Removed.
- **"Tool name is never revealed."** The paper uses `\toolname{}`, a LaTeX convention; the name is clearly present in the source. Parser artifact. Removed.
- **Overstatement about "first to consider Bayesian sampling for prompt optimization."** The paper's phrasing "To our knowledge" is appropriately cautious. Removed as unverifiable overreach by the reviewer.
- **"Bandit formulation assumes i.i.d. Bernoulli rewards but reward distribution changes as dataset is exhausted."** This is standard practice for bandit formulations over finite evaluation data; the paper's mini-batch procedure is a reasonable approximation. Removed as a technical nitpick that does not threaten the results.
- **"Dataset size assumption is an assumption not a fixed standard."** The paper explicitly states this as a methodological choice for comparability. Removed.
- **Several generic strengths from the Strength Finder** that were superficial (e.g., "addresses an important problem") — removed as they are not concrete, evidence-grounded claims.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's key strengths and weaknesses cleanly but do not add an independent synthetic insight.

## Suggestions

1. **Fill every `\tbdone` placeholder** before any potential resubmission. This is non-negotiable — the paper cannot be evaluated without its evidence.
2. **Defend or soften the "spurious" / "semantic equivalence" claim.** Either provide evidence (e.g., human-annotator judgments that formats are equivalent, or analysis showing that the model's sensitivity pattern does not match distributional patterns in pretraining data) or reframe the contribution as documenting sensitivity to formatting *per se* without the normative "spurious" label.
3. **Add a zero-shot condition** to at least one experiment to bound the generality of the finding.
4. **Report confidence intervals** around the spread estimates (e.g., via bootstrap over format samples).
5. **Include random search as a baseline** in the FormatSpread comparison.
6. **Tighten the PCA analysis** or remove it if it remains exploratory. Its current contribution to the paper's core claims is marginal.

---

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
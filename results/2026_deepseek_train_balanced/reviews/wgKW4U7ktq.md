## Summary

VisScience is a benchmark of 3,000 bilingual (Chinese/English) multi-modal questions equally distributed across mathematics, physics, and chemistry at the K12 level (21 subjects, 5 difficulty levels). The paper evaluates 25 MLLMs on the dataset and reports that closed-source models significantly outperform open-source ones, with best models achieving 53.4% (math), 38.2% (physics), and 47.0% (chemistry).

## Strengths

- **Genuine gap-filling**: Existing multi-modal benchmarks (MathVista, Math-Vision, MathVerse) overwhelmingly focus on mathematics. VisScience provides 1,000 multi-modal questions each for physics and chemistry — disciplines that are demonstrably underrepresented. The head-to-head comparison in Section 3.3 (e.g., only 177 visual problems in SciBench, only 1,601 of CMMMU's 12,000 questions covering these three disciplines) makes the gap concrete.

- **Systematic curation pipeline**: Starting from 450,000 questions and filtering to 3,000 through three explicit selection principles (coverage of every knowledge point, high-frequency prioritization, difficulty mixing) is more principled than simply aggregating existing datasets. The scale of the initial pool is notable.

- **Structured error analysis with per-discipline breakdown**: The error taxonomy (Figure 7) categorizing GPT-4o's errors into five types across three disciplines yields concrete findings — e.g., reasoning errors dominate all disciplines (56.5% math, 50.1% physics, 40.6% chemistry) while knowledge errors are especially prevalent in chemistry (33.2%). This provides actionable guidance beyond aggregate scores.

## Weaknesses

### Fatal
None.

### Major

1. **Conclusion contains a wrong headline number.** Line 393 states "Gemini-1.5-Pro reaches an accuracy of 30.1% in chemistry." The abstract (line 5), introduction (line 61), results section (line 222), and Table 2 (line 248) all consistently report 47.0%. The value 30.1% is actually InternVL-1.2-Plus's mathematics score (Table 2, line 272). For a benchmark paper whose core contribution is quantitative evaluation, an error in a headline result in the conclusion signals insufficient care with the data.

2. **Bilingual claim is unsubstantiated by evaluation.** The paper repeatedly emphasizes bilingualism as a key differentiator (lines 55, 71, 121, 189). However, line 222 explicitly states that all experimental results are "within the version of the Chinese language." No English-language evaluation results are reported anywhere. A central claimed advantage — cross-lingual scientific reasoning evaluation — is left completely unvalidated. The reader cannot assess whether English questions function correctly or whether performance differs across languages.

3. **GPT-4o serves as the judge for all models, including itself, without validation.** Line 218 describes GPT-4o evaluating all model responses against standard answers. This means GPT-4o judges its own outputs (scoring 51.7% math, 38.2% physics, 41.6% chemistry in Table 2). No analysis is provided of whether GPT-4o is systematically lenient toward or harsh on its own responses. For the 947 free-form questions (31.6% of the dataset), GPT-4o evaluates open-ended responses without any reported human verification or inter-rater agreement. The reliability of all reported numbers is therefore uncertain.

4. **Data provenance is critically underspecified.** Line 123 states that 450,000 questions were "sourced from K12 education" but provides no detail about the actual source — textbook publisher? online platform? proprietary collection? exam archives? The clustering methodology and selection criteria beyond three bullet-point principles (lines 125–130) are not described. The paper does not state whether VisScience will be publicly released, under what license, or at what URL. For a benchmark dataset, the data *is* the contribution; without source transparency and a release plan, the community cannot assess bias, copyright status, or reproducibility.

### Minor

1. **No per-subject breakdown for physics or chemistry.** Table 3 provides fine-grained results across 6 mathematics subjects, but no equivalent tables exist for physics (8 subjects) or chemistry (7 subjects) — 15 subjects left unbroken. This is a notable omission given the paper's emphasis on "21 subjects."

2. **Text-only vs. multi-modal comparison is not cleanly controlled.** Text-only LLMs receive only the question text (Q), while MLLMs receive both Q and image (I). The paper does not state whether text-only models received any textual description of the images. Consequently, the often-modest gap between text-only and multi-modal variants (e.g., GPT-4o text-only 38.0% vs. multi-modal 38.2% in physics) could reflect either limited reliance on visual information or an information-asymmetry in the input.

3. **Error analysis covers only GPT-4o with no inter-annotator agreement.** The error categorization (Figure 7) is done manually for one model alone, with no reported inter-annotator agreement. Extending this to at least one additional weaker model would significantly strengthen the analysis.

4. **Inconsistent subject count.** Line 59 states 21 subjects (6+8+7), but line 189 claims "22 distinct subjects."

### Trivial
None.

## Nice-to-Haves
- Validate the GPT-4o judge against human raters on a representative sample and check for self-evaluation bias.
- Report confidence intervals or error bars (with 1,000 questions per discipline, std. err. ≈ 1.6% at 50% accuracy).
- Identify and separately report a subset of questions where multi-modal accuracy substantially exceeds text-only accuracy, to demonstrate that visual information is genuinely needed.

## Removed Points
These points were flagged for removal during filtering; they should be treated with caution.

- *Harsh Critic: Claimed that the paper's third limitation ("single language") is inaccurate because CMMMU is bilingual.* — The paper uses "predominantly" (line 55), which is correct. Most benchmarks are single-language. Removed as factually incorrect about the paper.
- *Harsh Critic: Various section-by-section notes about thin data collection descriptions and missing annotation details.* — These are subsumed by the verified, stronger weaknesses above (data provenance underspecified, no English evaluation, GPT-4o judge validation). Not needed as duplicate entries.
- *Strength Finder: "Bilingual (Chinese and English) construction" as a standalone strength.* — Though Table 1 does report English question statistics, the complete absence of any English evaluation results means this strength is unsubstantiated as a practical contribution. Moved here because the construction is real but the evaluation gap dominates.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a consistent pattern: the benchmark fills a real gap (physics and chemistry are underserved) and has a principled curation pipeline, but the paper fails to deliver on its claimed advantages (bilingual evaluation, data transparency, rigorous automated evaluation) with actual evidence. The central tension is between ambitious design and incomplete execution.

## Suggestions
1. Correct the conclusion error (30.1% → 47.0% for Gemini-1.5-Pro chemistry) and audit all numerical values for consistency, including the 21 vs. 22 subject count.
2. Report English-language evaluation results, or if not feasible, clearly scope the paper to Chinese-only and temper the bilingual claim.
3. Disclose the specific source(s) of the 450,000 questions, the clustering method, and the release plan (license, URL).
4. Validate the GPT-4o judge against human raters and check for self-evaluation bias.
5. Provide per-subject breakdowns for physics and chemistry analogous to Table 3.
6. Clarify whether text-only models received any description of the images.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
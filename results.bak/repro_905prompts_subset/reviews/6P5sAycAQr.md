Now I have a clear picture. Let me write the consolidated final review.

## Summary

This paper proposes DefNTaxS, a training-free framework that uses LLMs to automatically discover taxonomic subcategories for a dataset's classes and integrates both class descriptors and taxonomic context into CLIP prompts (e.g., "fork, which has tines, commonly found among kitchen utensils"). The method achieves consistent accuracy improvements over vanilla CLIP (+5.5% average, +13.0% on EuroSAT) across seven standard benchmarks, all at a text-generation cost of $0.38.

## Strengths

1. **Consistent empirical gains across diverse benchmarks.** Table 1 shows DefNTaxS achieves the highest accuracy on 5 of 7 standard benchmarks (ImageNet, CUB, Pets, DTD, EuroSAT), with an average +2.44% over D-CLIP. The gains are most impressive on EuroSAT (+9.86% over D-CLIP), and the method works across fine-grained, texture, scene, and satellite domains.

2. **Fully automated, low-cost pipeline.** The method requires no manual prompt engineering, no model retraining, and uses GPT-4o-mini for a total text-generation cost of $0.38 (Section 4.2). This practical deployability is a genuine advantage over methods requiring manual template engineering or fine-tuning.

3. **Informative ablation studies.** The paper goes beyond a single main table to investigate key design choices: the effect of reduced taxonomic refinement (Table 2), modifications to descriptors/subcategories (Table 3), the comparison with random-character variants (Table 4), and LLM clustering vs. k-means (Table 5). These experiments surface important nuances about what drives the improvement.

4. **Clean, well-structured methodology.** The four-step pipeline (taxonomic discovery, contextual assignment, refinement, prompt enhancement) is clearly described and easy to follow. The use of LLMs for automatic subcategory discovery with completeness and non-overlap constraints is clean and principled.

## Weaknesses

### Major

1. **Central thesis is not supported by the evidence; the paper overclaims significantly.** The paper claims that taxonomic context is "essential" for robust zero-shot classification and represents a "paradigm shift" (Section 7), yet Table 4 shows that random-character subcategory labels (WaffleTaxS) perform comparably to or better than DefNTaxS on several datasets (IN: 63.24 vs. 62.96; Places: 40.05 vs. 39.34). The paper acknowledges this disconnect but does not resolve it—it speculates that "differentiation alone has an effect" but this directly contradicts the claim that *meaningful taxonomic semantics* drive the improvement. The paper also claims "six of seven benchmarks" in Section 5 (Table 1 discussion), but the data shows DefNTaxS is best on 5 of 7 (CHiLS wins on Food and Places). The "paradigm shift" and "essential" language is not warranted by the empirical evidence.

2. **The motivating problem (genuine label ambiguity) is never tested.** The paper opens with examples of "boxer" as dog vs. sport and "crane" as bird vs. equipment, but no benchmark used in the evaluation contains classes with multiple, conflicting senses. Every dataset has fixed, unambiguous labels *within* the dataset. The method is therefore evaluated on fine-grained discrimination (distinguishing similar but distinct classes) rather than on the genuine ambiguity problem it claims to solve. An experiment on a custom set with genuinely ambiguous labels (e.g., where "boxer" appears alongside both dog breeds and sports) would directly validate the motivating claim.

3. **Adding more semantic content (taxonomic descriptors) hurts performance systematically.** Table 3 shows that adding subcategory-level descriptors causes large drops across all datasets (e.g., ImageNet drops from 63.48 to 59.80, a relative loss of 5.8%). If the method's benefit came from richer taxonomic semantics, adding *more* relevant semantic information should help, not hurt. The paper speculates about CLIP's effective context window but does not investigate or resolve this. This is a significant unexplained contradiction.

4. **Statistical significance is missing from the main results (Table 1).** The ablation results in Table 4 include standard errors across 5 iterations, but the headline results in Table 1 report only point estimates. Given that the margins over D-CLIP are very small on several datasets (IN: +0.48, CUB: +0.79, Places: +0.16), the reader cannot assess whether these differences are reliable. The ablation table showing that DefNTaxS and WaffleTaxS are within error bars on several datasets further underscores this concern.

### Minor

1. **D-CLIP baseline was regenerated with GPT-4o-mini, but original numbers are not reported.** Section 4.1 notes that D-CLIP's generation was redone with GPT-4o-mini due to GPT-3 deprecation. However, the paper does not report how D-CLIP's published results compare to the re-generated version. If the new descriptors are stronger or weaker, the baseline comparison may shift.

2. **The subcategory refinement heuristic (~20 classes per subcategory) is empirically motivated but deferred to an appendix.** Section 3.3 states this threshold is based on "empirical analysis" referenced to Appendix D, which is not available. The sensitivity of results to this parameter matters—Table 2 shows that removing refinement (effectively too few subcategories) harms performance on ImageNet and Places.

3. **The performance gap on Food and Places is not discussed.** CHiLS beats DefNTaxS on Food by 2.05% (83.53 vs. 81.48) and on Places by 0.45% (40.45 vs. 40.00). These are the datasets where a hierarchical competitor (CHiLS) excels, yet the paper does not analyze what distinguishes these datasets from those where DefNTaxS wins.

4. **Claimed consistency of improvement is overstated.** The average gain over D-CLIP is 2.44%, and on ImageNet it is just 0.48%. Given the WaffleTaxS results, it is unclear how much of even this small gain is attributable to the taxonomic semantics versus the prompt diversification effect already documented in WaffleCLIP.

### Trivial

- Table bold formatting is misleading: all DefNTaxS numbers are bolded, including 81.48 on Food and 40.00 on Places where CHiLS has higher values. This makes the table harder to scan for actual SOTA results.

## Nice-to-Haves

- An experiment on a custom ambiguous-label dataset (e.g., "crane" appearing with both bird classes and construction equipment classes) would directly validate the motivating claim
- A real vs. shuffled taxonomy comparison (randomly reassigning classes to subcategories while preserving structure) would better isolate whether the specific taxonomic assignments matter
- Including standard errors in Table 1, at least for the key comparisons
- Reporting original D-CLIP published numbers alongside the GPT-4o-mini regenerated numbers for transparency

## Removed Points

- "The baseline set is somewhat dated (CuPL, WaffleCLIP, CHiLS from 2023)." — The paper includes CGPT-P (Ren et al., 2024), and the methods it compares to are the correct, widely-used baselines in this line of work. This is not a meaningful weakness given the paper's scope.

- "The paper does not analyze the computational cost of LLM calls beyond dollar amount." — Section 4.2 reports $0.38 total cost. This is sufficient for a methods paper in this area; detailed API call logging is a reproducibility detail, not a core weakness.

- "The appendix content is referenced but not available." — Parser artifacts; the appendix exists in the original submission.

- "Missing related works" — Cannot verify without external sources.

- Formatting/style nitpicks about Figure 1.

## Novel Insights

The most interesting finding in this paper is actually an unintended one: the WaffleTaxS results (Table 4) show that replacing *taxonomic* subcategory labels with random characters produces competitive performance on several datasets (ImageNet, Food, Places). This suggests that the primary benefit of DefNTaxS may come from adding *any* differentiating text per subcategory (creating token-level diversity that pushes class text embeddings apart) rather than from the semantic content of the taxonomy itself. Combined with the TaxCLIP variant (random descriptors + real taxonomy), which is clearly worse than DefNTaxS on every dataset, the evidence indicates that it is the combination of diverse class-level descriptors with *some* subcategory-level differentiation—not the specific semantic content of the taxonomy—that drives most of the gain. The paper comes close to making this observation but does not draw the conclusion, instead maintaining that taxonomic semantics are "essential." A more honest framing would position DefNTaxS as a practical prompt diversification strategy that uses LLMs to generate structure that happens to be semantically interpretable, even if the semantics are not the primary driver of performance.

## Suggestions

1. **Tone down the central claims.** Replace "essential," "paradigm shift," and "fundamental requirement" with language commensurate with the evidence: e.g., "taxonomic context provides consistent practical improvements in zero-shot classification." The paper's actual contribution (a cheap, automated method for prompt augmentation that gives modest gains) is a reasonable engineering contribution that does not need inflated rhetoric.

2. **Address the WaffleTaxS contradiction head-on.** The paper should explicitly test whether real taxonomies outperform shuffled or permuted taxonomies (randomly reassigning classes to subcategories while keeping the subcategory names and prompt structure identical). This would directly isolate whether the *semantic correctness* of the taxonomic assignment matters, or only the presence of any subcategory-level differentiation.

3. **Investigate why taxonomic descriptors hurt (Table 3).** This is a first-order mystery for the paper's thesis. A controlled experiment varying prompt length, descriptor position, and descriptor quality could determine whether this is a token-limit effect, a CLIP text-encoder artifact, or a genuine limitation of the approach.

4. **Fix the factual claim about "six of seven" benchmarks.** DefNTaxS is best on 5 of 7 (CHiLS wins on Food and Places). Correct this and discuss the two failure cases.

5. **Add standard errors to Table 1.** Even if only on a subset of key comparisons, this would significantly improve the reader's ability to assess the reliability of the reported margins.

## Score and Decision

### Round 1 — Bracketing

Three queries across three score bands (<3.5, 3.5-7.5, >7.5) on "zero-shot classification CLIP prompt engineering LLM descriptors" returned the following anchors:

| Band | Anchor | Avg Score |
|------|--------|-----------|
| <3.5 | HfJxXbXlYJ (LLM2CLIP) | 3.00 |
| <3.5 | ZVOGMy8Sd8 (Knowledge Enhanced Captioning) | 3.00 |
| <3.5 | ZaudLwn0Hm (Prototypical Evolution) | 2.50 |
| 3.5-7.5 | t84UBRhhvp (SLR-AVD) | 4.75 |
| 3.5-7.5 | B2ChNpcEzZ (DefNTaxS early version) | 4.00 |
| 3.5-7.5 | WqeRtP2T3R (Embracing Diversity) | 4.67 |
| 3.5-7.5 | w49jlMWDSA (GIST) | 5.33 |
| >7.5 | 5Ca9sSzuDp (Interpreting CLIP) | 8.00 |
| >7.5 | 1aF2D2CPHi (Open-Vocab Customization) | 8.00 |

**Initial bracket: 4.0–5.5.** The paper is clearly above the <3.5 band and clearly below the >7.5 band. The earlier version of this same paper scored 4.00; the current version is improved.

### Round 2 — Narrowing

Two queries within (3.5, 6.0) and (6.0, 7.5) on the same topic:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| B2ChNpcEzZ (DefNTaxS early) | 4.00 | Same paper, earlier version — current version is improved with more thorough ablations and more honest discussion of limitations |
| WqeRtP2T3R (Embracing Diversity) | 4.67 | Similar space; DefNTaxS has larger/clearer gains but the same WaffleCLIP-comparison issue |
| t84UBRhhvp (SLR-AVD) | 4.75 | Similar space; DefNTaxS has more thorough ablation studies and cheaper pipeline |
| w49jlMWDSA (GIST) | 5.33 | DefNTaxS is comparable — both have marginal gains but reasonable engineering contributions |
| wFs2E5wCw6 (TAP) | 6.40 | Clearly stronger — has proper prompt learning, better experimental methodology, and avoids overclaiming |
| NDLmZZWATc (DeMul) | 6.40 | Clearly stronger — has clearer novelty and better-supported claims |

The paper sits above the 4.00 early version and above the 4.67–4.75 range of similar rejected papers (better ablations, more consistent gains), but below the 6.40+ accepted papers (overclaiming issues, WaffleTaxS contradiction, missing error bars). It is most comparable to GIST (5.33, rejected) in terms of overall contribution level — a reasonable engineering method with modest gains, but overclaimed and with unanswered experimental contradictions.

**Final score: 5.0** — The paper makes a reasonable incremental contribution (automated LLM-based taxonomy discovery for prompt augmentation) with solid empirical execution, but is held back by unsupported central claims, the WaffleTaxS contradiction that undermines the core thesis, missing statistical reporting in the main results, and unexplained negative results (Table 3).

**Decision: Reject** — The paper has real strengths (clean methodology, cheap pipeline, thorough ablations), but the gap between what it claims ("essential," "paradigm shift," "fundamental advancement") and what the evidence supports (modest gains partially attributable to non-semantic differentiation) is too large. A substantially revised version with toned-down claims and a direct resolution of the semantic-content question could be competitive.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
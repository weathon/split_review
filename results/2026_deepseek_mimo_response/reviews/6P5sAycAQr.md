Now I have all the calibration data I need. Let me write the final review.

**Calibration summary:**
- Previous DefNTaxS version: 4.00 (Reject) — same paper, earlier version with fewer baselines and ablations
- Embracing Diversity: 4.67 (Reject) — similar idea (subclasses for zero-shot), marginal gains
- SLR-AVD: 4.75 (Reject) — marginal zero-shot gains from LLM descriptions
- GIST: 5.33 (Reject) — LLM-generated text for CLIP classification
- PerceptionCLIP: 6.00 (Accept) — training-free context-aware CLIP, marginal gains but cleaner claims

The current paper is clearly improved over its 4.00 predecessor but has concrete factual errors. I place it at 4.5.

---

## Summary

This paper proposes DefNTaxS, a training-free framework that uses LLMs to discover taxonomic subcategories for classes and augments CLIP prompts with both visual descriptors and taxonomic context for zero-shot image classification. The method clusters classes into subcategories, assigns classes contextually, refines granularity to ~20 classes per group, and generates natural-language prompts. Results are reported on seven standard benchmarks.

## Strengths

- **Thorough ablation study decomposing each component's contribution (Tables 2-5).** The paper systematically isolates the effects of taxonomic refinement (Table 2: without refinement, performance drops below D-CLIP), descriptors vs. taxonomic context (Table 3: "no desc." retains most performance on several datasets), semantic content vs. random differentiation (Table 4: WaffleTaxS and TaxCLIP with standard errors), and LLM vs. k-means clustering (Table 5: +0.92% average). This is genuinely informative for understanding what drives the gains.

- **Context-aware disambiguation is a concrete, well-motivated design choice (Section 3.2).** The method assigns "boxer" to different subcategories depending on whether the dataset contains other sports or dog classes — distinguishing it from CHiLS and D-CLIP which treat each class independently.

- **Extremely low deployment cost.** The total text generation cost across all seven datasets is $0.38 USD (Section 4.2), and the method requires no training or model modification, making it immediately practical as a drop-in enhancement for CLIP.

- **Consistent improvements over D-CLIP across all seven benchmarks** (Table 1, line 193: average +2.44%), with notable gains on Pets (+4.25%) and EuroSAT (+9.86%).

## Weaknesses

### Fatal
None.

### Major

- **The headline EuroSAT result does not test the paper's core contribution.** Section 3.3 (line 99) explicitly states: "For datasets with fewer than 20 classes, we use the dataset name as the single subcategory context (e.g., 'EuroSAT dataset'), as creating multiple subcategories may harm performance." EuroSAT has 10 classes, so the entire taxonomic stratification pipeline — the paper's sole novel contribution — is bypassed. Yet the abstract highlights "+13.0% absolute accuracy gain" and Section 5 (line 199) calls EuroSAT "the most compelling results" showing "taxonomic context helps distinguish land use categories." The gain derives from D-CLIP-style descriptors plus a dataset-name suffix, not from taxonomic stratification.

- **Factual error: incorrect claim of SOTA on six of seven benchmarks plus misleading table formatting.** Line 197 states "Table 1 shows DefNTaxS achieving the highest accuracy across six of seven benchmarks." CHiLS scores 83.53 vs. DefNTaxS's 81.48 on Food101, and 40.45 vs. 40.00 on Places365 (lines 190-191). DefNTaxS achieves the best on five of seven, not six. Compounding this, Table 1 bolds both CHiLS's and DefNTaxS's values on Food101 and Places365, misleadingly suggesting DefNTaxS is best on all datasets.

- **Inflated rhetoric relative to modest evidence.** The paper claims "taxonomic context as a fundamental requirement" (line 293), "essential for robust zero-shot classification" (line 179), and "a paradigm shift toward context-aware zero-shot learning" (line 297). The actual gains over D-CLIP are +0.48% (ImageNet), +0.79% (CUB), +0.16% (Places), +0.66% (ImageNetV2) — margins that could be within noise for single-run experiments, and no variance is reported for Table 1 to establish otherwise.

### Minor

- **No variance reported for main results (Table 1).** Table 4 reports standard errors across 5 iterations, demonstrating this is feasible. Table 1, where most margins over D-CLIP are under 1%, reports only single-run values, making it impossible to determine significance.

- **Baseline performance anomalies on EuroSAT are unexplained.** Nearly all baselines underperform vanilla CLIP (44.26%) on EuroSAT: E-CLIP (33.44%), W-CLIP (31.49%), CuPL (41.50%), CHiLS (42.83%). Only D-CLIP (47.36%) outperforms CLIP. This pattern is not acknowledged or discussed.

- **The refinement step, not taxonomic context per se, may be carrying the method.** Table 2 shows that without refinement, adding subcategory context degrades performance below D-CLIP (61.23% vs. 63.26% on ImageNet). The paper does not disentangle whether taxonomic context or granularity optimization is the key driver.

- **Prompt-length confound is not controlled.** DefNTaxS prompts are longer than D-CLIP prompts due to the added subcategory context. Given WaffleCLIP's finding that random characters improve performance, prompt length itself may contribute. No length-matched ablation is provided.

### Trivial
- The explanation for why k-means struggles (line 277: "the high dimensional embedding space") is speculative — k-means operates in any dimensionality and uses the same embeddings regardless of the clustering method.

## Nice-to-Haves
- A prompt-length equating ablation to isolate taxonomic content from text-length effects.
- Investigation and discussion of the EuroSAT baseline anomaly.
- Honest presentation of which benchmarks DefNTaxS wins, with corrected bold formatting.

## Removed Points
These points are flagged to be removed, treat them with caution.
- The Strength Finder's claim of "best or tied-best on 6 of 7 benchmarks" is factually wrong — verified against Table 1, DefNTaxS wins 5 of 7.
- The Strength Finder's emphasis on "+13.0% gain on EuroSAT" as direct evidence of taxonomic context's value is undermined by the fact that taxonomic stratification is bypassed for this dataset (line 99).

## Novel Insights
The ablation results reveal an interesting decomposition beyond the paper's framing: (a) refinement/granularity optimization is critical and without it, taxonomic context actually hurts (Table 2); (b) taxonomic labels alone (without descriptors) retain most performance on many datasets (Table 3, "no desc."); and (c) the relative importance of semantic content vs. structural differentiation varies by dataset (Table 4). These findings suggest the contribution may be primarily the granularity optimization step combined with structured groupings, rather than the full taxonomic context pipeline as claimed.

## Suggestions
- Correct "six of seven" to "five of seven" and fix Table 1 bold formatting to bold only actual best values per column.
- Add a clear caveat that EuroSAT uses a simplified version of the method (dataset-name context only, no taxonomic stratification).
- Report standard deviations or confidence intervals for Table 1 results.
- Tone down rhetoric to match the evidence: consistent but modest improvements over D-CLIP on most benchmarks, not a "paradigm shift."

## Reporting — Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DefNTaxS (previous version) | B2ChNpcEzZ.md | 4.00 | 1 | Same paper, earlier version — fewer baselines, worse ablations, fewer datasets. Current version is clearly improved. |
| Embracing Diversity | WqeRtP2T3R.md | 4.67 | 1 | Similar idea (subclasses for zero-shot), marginal gains, rejected. Current paper has more thorough ablations but also factual errors. |
| SLR-AVD | t84UBRhhvp.md | 4.75 | 1 | Marginal zero-shot gains from LLM-generated descriptors, rejected. |
| GIST | w49jlMWDSA.md | 5.33 | 2 | LLM-generated text for CLIP classification, requires fine-tuning, rejected. Current paper is training-free but has claim accuracy issues. |
| PerceptionCLIP | 2Oiee202rd.md | 6.00 | 2 | Training-free context-aware CLIP classification, accepted. Similar marginal gains but cleaner claims, broader evaluation. Current paper is weaker in claim accuracy. |

**Round 1 bracket: 3.5–5.5.** The paper is topically adjacent to several rejected papers in this range.

**Round 2 narrowing: 4.0–5.0.** The paper is clearly better than its 4.00 predecessor (more baselines, better ablations, clearer method), comparable to Embracing Diversity (4.67), but weaker than PerceptionCLIP (6.00) due to factual errors and inflated claims.

**Final score: 4.5.** The paper sits between its prior version (4.00) and similar rejected works (~4.75). It has a genuine contribution (taxonomic stratification for CLIP prompts) with informative ablations, but the factual errors in reporting results, misleading table formatting, inflated rhetoric, and the EuroSAT bypass issue significantly undermine trustworthiness. Without these problems, it would likely score 5.5–6.0.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
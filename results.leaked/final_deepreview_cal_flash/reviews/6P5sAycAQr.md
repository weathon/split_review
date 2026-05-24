Now I have a solid calibration picture. Let me write the final review.

**Round 1 bracket**: Between 4.0 (the previous version of this same paper, avg score 4.00, Reject) and 6.0 (PerceptionCLIP, avg 6.00, Accept).

**Round 2 narrowing**: I placed the paper between 4.5 and 6.0. Comparing to CARPRT (5.75, Reject — clean theory but marginal gains), "Embracing Diversity" (4.67, Reject — similar profile of incremental improvements with strong claims), "Hierarchical Taxonomies" (5.25, Reject), and "Tree of Attributes" (6.40, Accept — stronger method and evaluation), I position this paper around 5.0. It is improved over its predecessor (4.00) but still has significant overclaiming and the WaffleTaxS tension undercuts the central thesis, making it below the acceptance threshold.

---

## Summary

DefNTaxS proposes a training-free framework that uses an LLM to group dataset classes into semantically coherent subcategories and incorporates this "taxonomic context" into CLIP prompts for zero-shot classification. The method is clear and automated: an LLM generates subcategories, assigns classes to them, refines group sizes (~20 classes per group), and constructs natural-language prompts that combine descriptors with taxonomic context. Across seven benchmarks, DefNTaxS achieves a +5.5% average improvement over vanilla CLIP and outpaces D-CLIP by +2.44%, with the largest gains on EuroSAT (+13.0%).

## Strengths

- **Consistent accuracy improvements with a fully automated, training-free pipeline.** DefNTaxS improves over vanilla CLIP on all seven datasets (+2.1% to +13.0%) and outperforms D-CLIP on every benchmark. The method requires no manual prompt engineering, no model retraining, and no additional data — it uses one LLM call to discover subcategories and another for descriptors. The entire text generation pipeline across all benchmarks cost $0.38 USD (GPT-4o-mini), making the approach immediately deployable.

- **Informative ablation studies that disentangle semantic content from differentiation structure.** Section 6.1.3 (Table 4) compares DefNTaxS against WaffleTaxS (random subcategory labels, real descriptors) and TaxCLIP (real subcategory labels, random descriptors) over five runs with standard errors. This directly tests whether the *semantic content* of the taxonomic context or merely the *differentiation structure* drives gains. DefNTaxS outperforms WaffleTaxS on 4/7 datasets (e.g., +1.68 on Pets, +3.32 on DTD, +2.50 on EuroSAT), showing that semantic context provides real value beyond random differentiation on several benchmarks. The inclusion of standard errors in these ablations is good practice.

- **Evidence that LLM-based semantic clustering outperforms feature-space clustering.** Section 6.2 (Table 5) compares DefNTaxS against a k-means variant that clusters CLIP text embeddings instead of using LLM-derived subcategories. The LLM approach wins on all seven datasets (average +0.92%, with +3.19% on EuroSAT), isolating the LLM's ability to produce semantically coherent groupings over naive geometric clustering.

## Weaknesses

### Major

- **The paper's central thesis — that taxonomic context is "essential" and "inevitable" — is not fully supported by its own evidence.** Table 4 shows that WaffleTaxS (random subcategory labels) *outperforms* the full DefNTaxS on 3 of 7 datasets (ImageNet +0.28, CUB +0.06, Places +0.71), and the differences are within one standard error on most datasets where DefNTaxS leads. The paper acknowledges this ("mixed results") but the title, abstract, and conclusion continue to assert taxonomic context as an "inevitable need." The evidence more strongly supports a nuanced conclusion: differentiation structure matters, and semantic context helps on some — but not all — datasets. The gap between the strong framing and the actual results is the paper's most significant weakness.

- **The main results (Table 1) are reported as single-run accuracies without variance or significance estimates.** Several margins over D-CLIP are below 0.8% (ImageNet +0.48, CUB +0.79, Places +0.16, INV2 +0.66). Without confidence intervals or multiple runs, the reader cannot assess whether these small gains are signal or noise. The ablations in Table 4 correctly report means and standard errors over 5 iterations; this practice should extend to the primary comparison table.

### Minor

- **A numerical claim is incorrect.** The paper states DefNTaxS achieves "the highest accuracy across six of seven benchmarks." Table 1 shows CHiLS beats DefNTaxS on Food101 (83.53 vs. 81.48) and Places365 (40.45 vs. 40.00), making it 5 of 7 (or 6 of 8 if counting ImageNetV2). This factual error, though small, undermines trust in the handling of quantitative results.

- **The E-CLIP result on EuroSAT (33.44%) is notably lower than vanilla CLIP (44.26%).** While several other methods also underperform CLIP on EuroSAT (W-CLIP 31.49%, CuPL 41.50%, CHiLS 42.83%), suggesting EuroSAT is a hard case for complex prompt engineering, the sharp drop for E-CLIP specifically calls for an explanation. The paper should clarify which templates were used and whether the drop has a principled cause.

- **Main results use only one CLIP backbone (ViT-B/32).** The LLM vs. k-means ablation (Table 5) mentions multiple backbones, but the core evaluation does not include ViT-B/16 or ViT-L/14. Demonstrating the benefit holds across model scales would strengthen the contribution.

### Trivial

- None

## Nice-to-Haves

- **Quantify the practical impact of disambiguation.** A qualitative analysis showing concrete cases where taxonomic context corrects errors (e.g., "boxer the dog" vs. "boxer the sport") would make the contribution tangible.
- **Test sensitivity of the 20-class-per-subcategory rule.** Varying this threshold on a subset of datasets would show robustness.
- **Include a limitations discussion.** Scenarios where DefNTaxS may not help (e.g., well-separated classes, non-English labels, specialized domains) should be acknowledged.

## Removed Points

The following points from the inputs are excluded per filtering rules:

- *Missing appendix / unverifiable appendix claims*: The reviewer flagged unavailability of Appendix D for threshold verification. The appendix is present in the original submission; the parser strips it. Removed.
- *Missing prompt templates in main text*: The paper states they are in Appendix A. Removed per same rule.
- *Scope-creep requests* (e.g., adding more CLIP backbones to main results is a nice-to-have, not a core weakness — moved to Nice-to-Haves).
- *Generic concerns*: Claims about "insufficient care" in experimental setup that are not tied to a specific, verified error. Removed.
- *Strength Finder's generic strengths*: "Addressed an important problem" type statements removed. The four strengths listed above are the concrete, evidenced ones.

## Novel Insights

None beyond the paper's own contributions. The reviewers identify a genuine tension that the paper does not fully resolve: the WaffleTaxS results show that random subcategory labels sometimes work as well as the semantically meaningful ones, which undercuts the "essential" claim and suggests the grouping *structure* itself may be the primary driver, with semantic content providing an additional but dataset-dependent benefit.

## Suggestions

1. **Temper the claims** to match the evidence. Replace "essential"/"inevitable" with language that acknowledges taxonomic context is one useful tool among several, and that differentiation structure (separate from semantic content) drives a substantial portion of the gain.
2. **Add statistical significance** to Table 1 by running the main experiment 5 times and reporting means with standard errors, consistent with the ablations in Table 4.
3. **Fix the numerical claim** about "six of seven" — the paper should accurately state 5 of 7 (or clarify that ImageNetV2 is counted as an eighth benchmark).
4. **Address the E-CLIP EuroSAT result** by reporting which templates were used and explaining why it underperforms vanilla CLIP. If the drop is a known phenomenon, cite evidence; if it is an implementation issue, fix it.

## Score and Decision

**Calibration anchors used (all rounds):**

| Anchor ID | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| B2ChNpcEzZ (previous version of same paper) | 4.00 | R1 | Similar method, fewer baselines, same overclaiming issues — this version is improved but still shares core weaknesses |
| WqeRtP2T3R (Embracing Diversity) | 4.67 | R1 | Similar profile: incremental zero-shot improvements, some overclaiming — comparable quality |
| mLTbDVzHVh (Hierarchical Taxonomies) | 5.25 | R1 | Different task (continual learning) but similar mix of clear idea and limited evidence — slightly stronger |
| 2Oiee202rd (PerceptionCLIP) | 6.00 | R1 | Accepted paper on related topic (contextual attributes for CLIP) — cleaner evaluation, better-supported claims |
| fRpAUgKJhT (CARPRT) | 5.75 | R2 | Clear theory, marginal gains, rejected — comparable overall quality but DefNTaxS has weaker claim support |
| wFs2E5wCw6 (Tree of Attributes) | 6.40 | R2 | Stronger method with prompt learning and more datasets — clearly superior |
| t84UBRhhvp (Text Descriptions are Compressive) | 4.75 | R3 | Similar contribution level, rejected — comparable |

**Round 1 bracket**: 4.0 – 6.0  
**Round 2 narrowing**: The paper is better than the previous version (4.00) and "Embracing Diversity" (4.67) but weaker than CARPRT (5.75, Reject) and PerceptionCLIP (6.00, Accept). The overclaiming / evidence mismatch and the lack of statistical significance in the main table prevent this from reaching the acceptance range.  
**Final score**: 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>
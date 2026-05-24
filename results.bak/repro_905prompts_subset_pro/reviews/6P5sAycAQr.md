Now I have a thorough understanding of both the paper and its calibration context. Let me synthesize the final review.

---

## Summary

DefNTaxS proposes a training-free framework that uses an LLM to automatically cluster dataset classes into taxonomic subcategories and enrich CLIP prompts with this relational context (e.g., "boxer, which has a muscular build, commonly found among dog breeds"). Across seven standard benchmarks, it achieves an average +5.44% improvement over vanilla CLIP and +2.44% over D-CLIP, with gains up to +12.96% on EuroSAT. The framework is fully automated and costs under $0.40 in LLM calls.

## Strengths

- **Solid empirical performance with consistent gains:** DefNTaxS achieves the highest accuracy on six of seven benchmarks (Table 1), with an average +5.44% over CLIP and +2.44% over D-CLIP. The EuroSAT improvement (+12.96%) is particularly striking and suggests real disambiguation value on datasets where taxonomic context matters most.

- **Thorough ablation design:** The paper includes a meaningful set of ablations — reduced taxonomic refinement (Table 2), modified descriptors and subcategories (Table 3), random character substitutions for both subcategory labels and class descriptors (Table 4), and LLM vs. k-means clustering (Table 5). These collectively isolate the contributions of semantic content, differentiation, and clustering quality. The LLM vs. k-means comparison (mean drop of 0.92% across datasets) is particularly informative.

- **Training-free, fully automated, and practically deployable:** The entire pipeline uses only frozen CLIP and inexpensive LLM calls ($0.38 total across all datasets, Section 4.2), with no model re-training, manual prompts, or optimization data required. This makes the gains immediately usable.

- **Principled partitioning approach:** The method enforces a clean, non-overlapping partition of classes into semantically coherent subcategories (Section 3.1, Eq. 1), and the contextual assignment (Section 3.2) provides dataset-aware disambiguation (e.g., "boxer" assigned to "sports" vs. "dogs" based on co-occurring classes). This structured approach is a genuine advance over treating each class in isolation.

## Weaknesses

### Fatal
None.

### Major

- **The "essential" claim is overstated relative to the paper's own evidence.** Table 4 shows that WaffleTaxS (random characters replacing subcategory labels) matches or slightly exceeds DefNTaxS on ImageNet (+0.28), CUB (+0.06), and Places (+0.71). While DefNTaxS wins on the other four datasets and on average, the fact that random subcategory labels can sometimes match the performance of semantic taxonomic labels undermines the headline claim that taxonomic context is *essential*. The paper acknowledges in Section 6.1.3 that "differentiation alone has an effect," which is honest, but the introduction and conclusion ("essential," "fundamental requirement," "paradigm shift") do not reflect this nuance. The contribution would be stronger if framed around the finding that *structured grouping with semantic content* provides consistent (but not uniformly necessary) gains, rather than claiming indispensability.

- **Incremental novelty.** The method combines two established lines of work: LLM-generated per-class descriptors (D-CLIP) and LLM-generated hierarchical/taxonomic structure (CHiLS, CGPT-P). Adding a flat group label as a phrase modifier is a straightforward combination. While the execution is careful and the ablations are thorough, the conceptual leap is modest — the paper itself acknowledges in Section 2 that DefNTaxS "combines the strengths of LLM-generated descriptors and taxonomy-based methods." This limits its significance for a top venue.

### Minor

- **The "reduced taxonomic refinement" ablation (Table 2, Section 6.1.1) is under-described.** The paper states only that "the lack of differentiation between classes damages the ability of the VLM to distinguish between them," but does not specify exactly what was changed (e.g., how many subcategories were collapsed, whether a single broad category was used). The reader must infer the setup from surrounding context, which makes it difficult to fully assess the ablation's validity.

- **Ambiguous evaluation split terminology.** Section 4.1 states accuracy is reported on "each dataset's standard training split," which is confusing for zero-shot evaluation where test/validation splits are standard. While the CLIP baseline numbers (e.g., 58.89 on ImageNet) match known test-set values, suggesting this is a wording issue rather than a protocol problem, the phrasing should be corrected to avoid confusion.

- **The paper claims SOTA across six of seven benchmarks but CHiLS edges out DefNTaxS on Food101 (83.53 vs. 81.48) and Places365 (40.45 vs. 40.00).** While the overall mean is clearly in DefNTaxS's favor, the binary "six of seven" framing glosses over these competitive results. A more careful characterization would strengthen credibility.

### Trivial

- The "tax. desc." performance drop in Table 3 is attributed to CLIP's limited effective context window with a citation to Zhang et al. (2024). The paper appropriately notes "further investigation would be needed," but the explanation remains speculative.

## Nice-to-Haves

- A qualitative analysis showing which specific ambiguous classes are resolved by DefNTaxS (e.g., cases where "boxer" is correctly disambiguated) would strengthen the disambiguation claim and help readers understand when taxonomic context matters most vs. when differentiation alone suffices.

- Reporting performance variance across multiple LLM generations (since LLM outputs are stochastic) would address concerns about the stability of discovered subcategories and resulting accuracy.

- A comparison where the connecting phrase ("commonly found among") is removed to test whether bare subcategory names work equally well would further isolate the contribution of natural-language contextualization.

- Including standard deviations on the main results table (Table 1) would help assess whether the 0.16–1.05% margins over D-CLIP on some datasets are statistically meaningful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"CHiLS explicitly addresses ambiguity through hierarchical specification and its results are comparable"* — While CHiLS is a relevant baseline and does address ambiguity, the paper does include CHiLS in Table 1 and beats it on mean performance (61.17 vs. 57.74). The introduction's framing of prior work as "contextually blind" is somewhat strong but the paper substantiates the distinction (CHiLS uses hierarchical hyponyms without lateral semantic groupings). Kept the concern in weakened form under Minor.

- *"The ≈20 classes per subcategory claim cannot be verified because Appendix D is missing"* — Per the rules, removed. Appendix content is stripped by the parser; the original submission includes this evidence.

- *"The inclusion of ImageNetV2 gains are small (+0.66% over D-CLIP)"* — This is a valid observation but does not constitute a weakness. The +4.73% gain over CLIP on ImageNetV2 is substantial, and the purpose of including ImageNetV2 is to show generalization, not raw magnitude. Removed as a standalone criticism.

- *"The method should include a comparison where the connecting phrase is removed"* — Moved to Nice-to-Haves.

- *"Typos and formatting issues"* — Removed per formatting rules; these are parser artifacts.

## Novel Insights

The WaffleTaxS vs. TaxCLIP comparison in Table 4 reveals an interesting asymmetry: randomizing subcategory labels while keeping real descriptors (WaffleTaxS) hurts less than randomizing descriptors while keeping real subcategory labels (TaxCLIP). TaxCLIP trails DefNTaxS by an average of ~2 points while WaffleTaxS trails by ~0.8. This suggests that the taxonomic structure itself — even without meaningful labels — provides a scaffolding benefit, but the semantic *content* of class-level descriptors is comparatively harder to replace with noise. This is a more nuanced finding than the simple "descriptors vs. random" story from WaffleCLIP, and is worth highlighting as a contribution in its own right.

## Suggestions

- Reframe the contribution around the finding that structured grouping with semantic content provides consistent gains, rather than claiming taxonomic context is "essential." The WaffleTaxS results already support an honest, nuanced framing that would strengthen rather than weaken the paper.

- Add a concise description to Section 6.1.1 specifying exactly how many subcategories were used in the "reduced taxonomic refinement" condition and how they differed from the standard DefNTaxS configuration.

- Correct the "standard training split" language in Section 4.1 to accurately describe the evaluation protocol.

- Include concrete qualitative examples of disambiguation (e.g., showing which ImageNet classes benefit most from taxonomic context) to ground the "disambiguation" claim in interpretable evidence.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| B2ChNpcEzZ (DefNTaxS — earlier version) | 4.00 | R1 | Same paper; current version has improved ablations |
| WqeRtP2T3R (Diversity Zero-shot) | 4.67 | R1 | Similar novelty level, less thorough evaluation |
| t84UBRhhvp (Text Descriptions Compressive) | 4.75 | R2 | Similar domain, less comprehensive baselines |
| BLvCdxAi8W (Granularity Long-Tail) | 4.25 | R2 | Different problem, lower relevance |
| w49jlMWDSA (GIST) | 5.33 | R2 | Similar novelty, requires fine-tuning unlike DefNTaxS |
| mLTbDVzHVh (Hierarchical Taxonomies Continual) | 5.25 | R1 | Different problem (continual learning), lower relevance |
| wFs2E5wCw6 (Tree of Attributes TAP) | 6.40 | R1/R2 | More novel (learnable prompts, structured KGs); clearly above |
| eE2PXlNydB (Clustering CZSL) | 6.00 | R2 | Different problem, more novel architecture |

**Round 1 bracket:** 3.5 – 5.5 (based on the paper's own anchor at 4.00 and nearby comparables in the 4.25–5.33 range).

**Round 2 narrowing:** The paper sits between the "Diversity" paper (4.67) and GIST (5.33). It has more thorough ablations and a cleaner method than either, but comparable novelty concerns. The paper is better than its own earlier-reviewed version (4.00) due to expanded ablation studies, but the core limitations — incremental novelty and overstated claims — persist. It is clearly below TAP (6.40), which introduces learnable prompt tokens and structured knowledge graphs.

**Final score:** 4.5 — Reject. The paper is a well-executed, pragmatic contribution to the prompt-engineering literature with solid empirical results and informative ablations. However, the incremental novelty (combining descriptor-based and taxonomy-based approaches in a straightforward way) and the gap between the claimed "essential" role of taxonomic context and the WaffleTaxS evidence prevent it from meeting the bar for acceptance. A substantially revised framing and deeper analysis of *when* taxonomic context matters would position it for acceptance at a strong workshop or mid-tier venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>
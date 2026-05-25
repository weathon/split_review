## Summary

This paper addresses the under-explored task of generating images for WordNet taxonomy concepts using text-to-image (TTI) models. The authors propose a benchmark with 9 metrics (ELO from human and GPT-4 judges, Reward Model scores, Lemma/Hypernym/Cohyponym CLIP similarities, Specificity, FID, and Inception Score), evaluate 12 TTI models plus a retrieval baseline across multiple concept subsets, and release a dataset of generated images covering all WordNet 3.0 synsets. The main finding is that Playground-v2 and FLUX dominate preference-based metrics while SDXL-turbo dominates similarity-based metrics, with rankings differing from standard T2I evaluations.

## Strengths

- **Comprehensive multi-metric evaluation for an under-studied task.** The benchmark spans 9 metrics across preference-based (human ELO, GPT-4 ELO, Reward Model), taxonomy-specific similarity (Lemma, Hypernym, Cohyponym, Specificity), and standard quality/diversity (FID, IS) dimensions, evaluated on 12 models over multiple concept subsets. This breadth provides a multifaceted view of model capabilities for taxonomy image generation. (Sections 4–5, Table 2, Figure 4)

- **Release of a large-scale generated-image dataset covering the full WordNet 3.0 taxonomy.** Extending ImageNet's ~5K covered synsets to all ~80K WordNet synsets creates a useful resource for future work in taxonomy visualization, data augmentation, and automatic dataset curation. (Contributions in Section 1, Reproducibility section)

- **Transparent documentation of GPT-4-as-judge limitations.** The paper reports a strong first-option bias in GPT-4 pairwise preferences (Figure 5), the lack of per-image correlation with human judgments, and yet a useful model-level alignment (Spearman 0.88–0.92). This candid analysis is a methodological contribution that informs the broader LLM-as-judge discussion. (Section 5, Figures 4–5)

- **Specificity metric as a principled generalization of In-Subtree Probability.** By moving beyond fixed ImageNet classifiers to arbitrary taxonomy nodes via CLIP similarity, the paper provides a more flexible tool for measuring conceptual specificity that is not tied to a particular classifier. (Section 4.2)

## Weaknesses

### Fatal
None.

### Major

- **Inconsistency between the claimed validation of similarity metrics and the reported rankings.** Section 4.2 states that Hypernym CLIP-Score ranks models with Spearman ρ≈0.911 (p≤0.00004) against human evaluation. However, Table 2 shows SDXL-turbo as the top model for Hypernym Similarity across every subset, while the human ELO ranking (Figure 4, left) places SDXL-turbo at approximately 7th of 12 models (after FLUX, Playground, PixArt, SDXL, Kandinsky3, and HDT). A Spearman correlation of 0.911 between these two substantially different rankings is implausible based on the data presented. The paper does not specify which "human evaluation" is used for this correlation or whether it is computed per-model or per-concept. Since this correlation is the primary quantitative validation of the proposed taxonomy-specific metrics, the discrepancy must be resolved and clearly documented. Without clarification, the claimed alignment between the similarity metrics and human judgments is unsupported, which weakens a core contribution of the benchmark. (Section 4.2, Table 2, Figure 4)

### Minor

- **Ambiguous dataset sampling description (Section 2.2).** The description of the random WordNet split sampling procedure is contradictory as written. The text first states sampling probabilities of 0.1/0.1/0.8 for Hyponymy/Synset Mixing/Hypernymy, then introduces "probabilities of occurrence in the test set" of 1×10⁻⁵/0.05/0.1 that do not obviously produce the reported counts (828/170/204). While a plausible interpretation exists (these are per-candidate acceptance probabilities rather than final proportions), the wording is confusing and makes the dataset construction harder to reproduce than it should be.

- **Underspecified retrieval baseline.** The "Wikimedia Commons" retrieval model is listed in Table 1 with citations but is not described in the main text. Readers cannot assess how retrieval is performed (query construction, candidate selection, reranking) or whether the comparison with generative models is fair. The example in Figure 2(d) (a Buddha statue for "cigar lighter") suggests poor retrieval quality, but without a clear description, it is impossible to determine whether this reflects an inherent limitation of retrieval or a weak implementation. The paper's conclusion that "the retrieval-based approach performs poorly" depends on this baseline. (Section 3, Table 1, Figure 2)

- **Overclaimed novelty.** The abstract states "we pioneer the use of pairwise evaluation with GPT-4 feedback for image generation." This is contradicted by the paper's own citations: Chen et al. (2024a) and Cui et al. (2024) both apply GPT-4/VLMs to image evaluation. This phrase should be removed or sharply qualified. (Abstract)

- **GPT-4 position bias is acknowledged but not mitigated.** The paper documents a strong first-option bias in GPT-4 preferences (Figure 5) and reports "no correlation between raw scores for individual battles." Despite this, no mitigation is applied (e.g., swapping image order and averaging results). While GPT-4 is used as one of several metrics, the unmitigated bias weakens confidence in the GPT-4 ELO rankings and the derived conclusions. (Section 5)

- **FID computed against a non-standard reference distribution.** FID is evaluated using retrieved images (from the underspecified retrieval pipeline) as the reference set. The paper caveats this ("FID reflects the 'realness' or closeness to retrieval"), but this means the FID scores are not comparable to standard results in the literature and their interpretation depends entirely on the quality of a retrieval set that is itself unvalidated. (Section 4.3)

- **Claim of different rankings from standard T2I tasks is not quantitatively supported.** The paper states that "the ranking of models differs significantly from standard T2I tasks" and cites GenAI Arena (Jiang et al., 2024a), but no quantitative comparison table or correlation analysis is provided. This weakens a central motivation for the benchmark. (Section 1)

### Trivial

- **Inconsistent correlation values.** Figure 4 caption reports the overall Spearman correlation between human and GPT-4 model rankings as 0.92, while Section 5 states the same quantity as 0.88. These should be reconciled. (Figure 4 vs. Section 5)
- **Model count discrepancy.** Section 3 states "ten TTI models" but Table 1 lists 11 TTI models (plus one retrieval model, totaling 12). (Section 3 vs. Table 1)

## Nice-to-Haves

- A direct quantitative comparison (table and correlation) between the model rankings obtained on this benchmark and those on standard T2I benchmarks (e.g., GenAI Arena) would substantially strengthen the paper's core motivation.
- For the similarity metrics, a per-concept validation study (e.g., asking humans to rate how well each generated image represents the lemma vs. its hypernyms/cohyponyms) would be more informative than the current aggregate model-level correlation claim.
- Mitigating the GPT-4 position bias by conducting each comparison bidirectionally (both orderings) and averaging the results would improve the reliability of the GPT-4 ELO signal.
- Expanding the human annotation pool beyond 4 annotators would increase statistical power for the human preference evaluation.

## Removed Points

The following points from the inputs were removed with brief justifications:

- **"Retrieval baseline is intentionally weak"** (Harsh Critic): This is speculative; the paper cites specific references for the retrieval method, and the appendix presumably describes it. The criticism about insufficient description is kept as Minor.
- **"LLM predictions quality not analyzed"** (Harsh Critic): The paper states the matching is "described in Appendix C"; the parser strips appendices, so this criticism targets missing appendix content.
- **"Similarity metrics are not novel"** (Harsh Critic): The paper provides theoretical grounding in Appendix D (stripped); the practical contribution is the application of CLIP similarity in a taxonomy-structured way, which is a reasonable methodological contribution.
- **"Strength: similarity metrics validated by high correlations"** (Strength Finder): This directly conflicts with the verified Major weakness about the correlation discrepancy; per the rules, the weakness wins.
- **"Strength: distinct model rankings from standard T2I"** (Strength Finder): This conflicts with the verified Minor weakness that the claim is unsupported by quantitative comparison.
- **"Strength: benchmark reveals distinct model rankings"** (Strength Finder): Same as above — insufficiently supported.
- **Formatting/typographical nitpicks** (Harsh Critic): These are parser artifacts, not author errors.

## Novel Insights

The reviews collectively surface a significant and specific tension in the paper's evidence: the Spearman correlation of 0.911 claimed between Hypernym Similarity and human evaluation is inconsistent with the actual model rankings presented (SDXL-turbo #1 in Hypernym Similarity but ~#7 in human ELO). This goes beyond a generic "validation insufficient" comment — it points to a concrete numeric contradiction that the authors must resolve. If the correlation is computed per-concept or on a different subset, that needs to be stated explicitly; if it is a reporting error, it needs correction. Either way, this issue cuts to the heart of whether the taxonomy-specific metrics are validated as claimed. The secondary insight is that several of the paper's framing claims (pioneering GPT-4 evaluation, different-from-standard rankings, retrieval baseline quality) are less supported than the confident language suggests, and addressing them would significantly strengthen the benchmark's credibility.

## Suggestions

1. **Clarify the similarity-metric correlation.** Specify exactly which "human evaluation" is used, report the full ranking (all 12 models) for each similarity metric alongside the human ranking, and state whether the correlation is per-model or per-concept. If the correlation in Section 4.2 refers to a different human evaluation than the ELO procedure, describe it explicitly in the main text.

2. **Reword the dataset sampling description (Section 2.2).** Make clear that the "probabilities of occurrence" are per-candidate acceptance probabilities during sampling, not final proportions in the test set, to eliminate the apparent contradiction.

3. **Describe the retrieval baseline in the main text.** Provide at least a brief summary of how Wikimedia Commons images are queried and selected, so readers can assess the fairness of the generation-vs-retrieval comparison without consulting the appendix.

4. **Add a quantitative comparison with standard T2I rankings.** Include a table or correlation analysis showing how the model rankings from this benchmark compare to those from GenAI Arena or similar benchmarks, to support the claim that taxonomy image generation is a distinct task.

5. **Remove or qualify the "pioneer" claim** regarding GPT-4 pairwise evaluation, since the paper itself cites prior work using the same approach.

6. **Consider bidirectional GPT-4 evaluation** (swap image order) to mitigate the documented position bias, or at minimum discuss why this was not done.

## Score and Decision

The paper addresses a worthwhile and timely problem with an ambitious evaluation framework. However, the major inconsistency in the validation of the taxonomy-specific similarity metrics undermines a core contribution, and several weaker claims (pioneering novelty, retrieval comparison, ranking distinctiveness) need stronger support. The benchmark idea and released dataset have clear value, but the paper as written does not fully deliver on its claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>
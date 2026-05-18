Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me compose the final consolidated review.

## Summary

This paper investigates how zero-shot prompt variation affects latent representations in LLMs, focusing on two aspects: (1) whether prompts modify the effective dimensionality of representations (measured via IsoScore), and (2) whether prompts can be grouped by their representational geometry rather than semantic similarity (via KMeans clustering). The study covers four model families (Gemma, Phi, Zephyr, Bloomz) across three sentiment datasets. The paper reports that prompt choice influences hidden-state geometry in a model-dependent way and that clustering yields groupings that do not always align with natural-language prompt similarity.

## Strengths

- **First systematic study of zero-shot prompt impact on latent geometry.** The paper explicitly identifies that "no works have studied the impact of zero-shot prompting approaches on the geometry of latent representation" (Section 1). It fills this gap by analyzing hidden-state distributions across layers using IsoScore and clustering, providing an initial empirical characterization of how prompt formulation modifies geometric properties of representations.

- **Demonstration of stable, model-dependent clustering patterns.** The clustering methodology (KMeans with majority vote) shows that prompts produce groups that are consistent across layers (Figure 4, with reported RIS values), and Table 4 reveals that semantically similar prompts (e.g., "Movie Expressed Sentiment" vs. "Text Expressed Sentiment") are not always grouped together. This provides preliminary evidence that the model's internal grouping criteria differ from human semantic intuition.

- **Multi-model, multi-dataset empirical scope.** The study covers four model families (Gemma 2B/7B, Phi 3, Zephyr 1.6B/3B, Bloomz 560M-1.7B) across three sentiment datasets (Rotten Tomatoes, IMDB, YELP), allowing the paper to document that prompt effects on latent geometry are model-family dependent — e.g., "the evolution is smoother for the Bloomz family" (Section 5.1) and smaller models tend to have higher IsoScore.

- **Combined use of IsoScore and clustering for complementary analysis.** The dual approach — IsoScore quantifying effective dimensionality and clustering revealing structural grouping of prompts — provides both a distribution-level and a representation-level view. This combination goes beyond prior work that studies performance or single metrics in isolation.

## Weaknesses

### Fatal

None. The paper's core claims are not invalidated by any single catastrophic flaw, though they are less strongly supported than the writing suggests.

### Major

1. **IsoScore analysis lacks noise baselines and statistical rigor.** The IsoScore values are very small (0–0.006; line 133), and while Table 3 reports standard deviation as a percentage of the mean to argue the effect is "sturdy," there is no noise baseline (e.g., random splits of the same prompt condition, or repeated runs with different seeds) against which to compare observed across-prompt variation. Without knowing whether the between-prompt differences exceed what random subsampling or inherent variability would produce, the central claim that prompts "significantly modify" geometry in a "non-negligible way" is not quantitatively established. The paper also acknowledges "we cannot link the IsoScore to the performance" (line 143), yet the whole motivation for studying isotropy was its purported link to performance (Section 1, citing Ethayarajh 2019, Cai et al. 2021). This undermines the explanatory value of the IsoScore analysis.

2. **Clustering analysis lacks crucial baselines to support the "counter-intuitive" claim.** The paper interprets k' < k after majority vote as evidence that prompts are grouped by non-semantic features. However, this pattern is also what one would expect if representations are simply not perfectly separable by KMeans (which is likely given all prompts direct the model toward the same binary task). The paper does not compare against baselines such as: (a) random assignment of examples to prompts, (b) representation-level baselines from shuffled labels, or (c) an independent measure of semantic similarity between prompts (e.g., sentence-encoder embeddings). Without these, the claim that "geometrical features weakly correspond to semantic attributes" (line 179) is suggestive but not well-supported. Additionally, Table 4 reports raw co-occurrence counts (e.g., 1,525) without stating the total number of clustering trials (layers × models × runs), making it impossible to assess whether the observed co-occurrence is above chance expectation.

3. **Exact prompts are not enumerated.** The paper states prompts are based on Promptsource templates with "minor modifications" (line 115) but does not list the exact prompts, their number, or how they differ. This is a significant reproducibility gap — a reader cannot determine which prompt formulations were tested or reconstruct the experiments.

4. **No connection between RQ1 and RQ2.** The IsoScore analysis and clustering analysis are presented independently. The paper does not test whether prompts that cluster together share similar IsoScore profiles, which would strengthen the claim that geometric properties are shared and that the two analyses corroborate each other.

### Minor

1. **Title scope exceeds experimental scope.** The title "Impact of Prompt on Latent Representations in LLMs" suggests a general study, but experiments are limited to binary sentiment classification. The abstract appropriately scopes this ("binary classification tasks"), but the title remains overbroad.

2. **Qualitative performance-isotropy link without statistical backing.** The paper states "according to the figure 2 bad performance seems to be correlated with extreme isotropy" (line 154) but provides no statistical test of this claim. Given the earlier concession that "we cannot link the IsoScore to the performance" (line 143), the claim about "bad prompts destabilizing representations" remains an observational remark rather than a supported conclusion.

3. **Analysis limited to EOS token representations.** While the paper acknowledges this choice (line 50: "only the last generated representation is able to capture all contextual information"), the analysis is scoped to EOS tokens at each layer. Claims about "how prompts modify the vector distribution" should be understood as specifically about the EOS representation, not about the internal processing of prompt tokens themselves.

4. **No check for label leakage in clustering.** If some prompt phrasings systematically encode the ground-truth label words, the EOS representation might encode class information rather than prompt identity. The paper does not discuss or control for this confound.

5. **Table 4 would benefit from normalized reporting.** Reporting raw co-occurrence counts without the denominator (total clustering trials across all models and layers) limits interpretability — the reader cannot gauge whether 1,525 is large or small relative to chance.

### Trivial

- Table 2 caption ("Mean standard deviation computed over the models and the prompts for each DataSet") is ambiguous about which variance component is being reported.
- No computational budget is stated, though this is a minor omission for an empirical analysis paper.
- Some redundant phrasing (e.g., the repetition about data contamination concerning Bloomz in Section 4.1).

## Nice-to-Haves

- **Noise baseline for IsoScore:** Compute IsoScore on random halves of the same prompt condition; the variation gives a lower bound on detectable differences, making it possible to assess whether across-prompt differences are meaningful.
- **Semantic similarity baseline for clustering:** Embed the prompt templates using a standard sentence encoder and compare the resulting similarity matrix to the co-clustering matrix. If the two align poorly, that directly supports the "geometric features beyond semantics" claim.
- **Permutation test for Table 4:** Report the distribution of co-occurrence counts under random prompt-label permutations, so the reader can assess whether the observed groupings are above chance.
- **Link RQ1 and RQ2:** Check whether prompts that cluster together also have similar IsoScore profiles across layers.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Central contribution is trivially true"** (Harsh Critic Point 3, first paragraph): This mischaracterizes the paper's contribution. The paper does not merely assert that prompts affect representations (which would indeed be trivial) — it characterizes *how* they affect geometry (IsoScore patterns, layer-wise evolution, model-dependency, counter-intuitive clustering). The paper's actual contributions on lines 23–24 are more specific than the critic allows. The valid sub-concern (insufficient evidence for the claims) is already captured in Major weaknesses 1 and 2 above; the "trivially true" framing is a strawman and is removed.
- **"The paper would be more convincing if..." framing paragraphs** (Strengthening the Paper on Its Own Terms section): These are suggestions, not weaknesses of the current paper. The actionable ones are migrated to Nice-to-Haves and Suggestions above.
- **"The writing is at times redundant and contains odd phrasings"**: These are stylistic judgments that do not affect scientific content; the specific example cited ("we cannot totally state on the hypothesis since Zephyr is also trained on the datasets") is actually the paper appropriately noting a confound, not an error.

## Novel Insights

The primary novel insight across the two reviews is the convergence that the paper identifies a genuinely underexplored question (how prompt formulation affects the *geometry* of latent space, not just performance), but that the current evidence is observational and preliminary rather than confirmatory. The two analyses (IsoScore and clustering) are each missing the baselines that would turn description into explanation. A stronger version of the paper would pick one claim (e.g., the counter-intuitive clustering) and test it with the appropriate baselines and statistical controls, rather than spreading thin across two under-supported analyses. The observation that Table 3 (std as % of mean) provides the paper's best quantitative evidence for a prompt effect is worth highlighting — this is where the paper comes closest to a rigorous demonstration, and future work should build on this approach with formal statistical testing.

## Suggestions

- For the clustering analysis, add a permutation baseline: shuffle the prompt labels of each example and re-run the clustering; compare the observed k' and RIS against the distribution under random labels. This directly tests whether the "superclusters" reflect genuine structure.
- For the IsoScore analysis, add a within-prompt noise baseline: split the examples of each prompt into two random halves, compute IsoScore on each half, and report the within-prompt variance. Compare this to the across-prompt variance to establish effect size.
- List the exact prompt templates in a public repository or appendix (the paper states they derive from Promptsource, but "minor modifications" need to be specified).
- Add a semantic similarity baseline for the clustering: embed prompt texts with a standard sentence encoder (e.g., Sentence-BERT) and correlate the resulting similarity matrix with the prompt co-clustering matrix.
- Either link RQ1 and RQ2 explicitly (e.g., do prompts in the same cluster have similar IsoScore curves?) or restructure the paper to present them as independent exploratory analyses to avoid promising integration that is not delivered.

## Score and Decision

The paper tackles an interesting and underexplored question, and the multi-model, multi-dataset experimental scope is commendable. However, the evidence falls short of the claims: the IsoScore analysis lacks the statistical baselines needed to show the observed variation is systematic rather than noise, the clustering analysis lacks the baselines needed to support the "counter-intuitive" interpretation, and the two analyses operate independently without the promised integration. The contribution is preliminary — a descriptive report of interesting measurements — rather than a demonstrated finding. Major methodological additions would be required to make the results convincing. In its current form, the paper does not meet the bar for acceptance at a venue expecting rigorous empirical support for causal claims about model internals.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
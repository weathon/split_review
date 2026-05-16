Good. I've now verified the key claims against the actual text. Let me write the consolidated review.

## Summary

This paper introduces WES (Wiki Entity Summarization Benchmark), a benchmark for knowledge graph entity summarization. The core proposal is an automatic pipeline that uses Wikipedia abstracts as ground-truth summaries and maps mentions to Wikidata properties via DistilBERT cosine similarity, eliminating the need for costly human annotation. The paper also contributes a degree-proportional random walk sampling method to generate connected subgraphs that preserve graph structure, and demonstrates scalability by generating datasets with up to ~250k entities in ~512 seconds.

## Strengths

- **Scalable automatic dataset generation without human annotation**: The paper demonstrates generating datasets with up to ~250k entities and ~470k relations in under 10 minutes (512 seconds for the largest set) by leveraging Wikipedia abstracts as ground-truth summaries. This directly addresses a real bottleneck in entity summarization research, where existing benchmarks like ESBM (175 entities) and FACES (50 entities) require expensive manual annotation (Section 3.4, lines 168-171).

- **Demonstrates avoidance of frequency-based annotator bias**: The empirical evaluation (Section 4, lines 200-206) shows that on WES, frequency- and inverse-frequency-based methods score near the random baseline, while on ESBM the same methods significantly outperform random (by up to 0.34 F1 for top-10). This is concrete evidence that WES avoids the frequency bias that plagues small, human-annotated datasets.

- **Degree-proportional random walk sampling that preserves graph topology**: The sampling method (Section 3.2) adjusts the number of random walks per node based on normalized logarithmic degree, and the paper shows that the large dataset's F-score trend matches the distribution of the full Wikidata graph (lines 204-206). The connectivity restoration algorithm (Step 3, lines 164) ensures all generated datasets are connected, a property missing from existing benchmarks like FACES and LMDB.

- **Flexible and configurable generator**: Algorithm 1 (Section 3.3) allows users to specify seed nodes, random walk parameters, and dataset size, producing connected graphs with train-test-validation splits. The paper demonstrates generation for four seed sets across three scale levels (lines 152-154, 168-171).

## Weaknesses

### Fatal
None.

### Major

- **Summary annotation pipeline receives no validation**: The DistilBERT property-selection step (lines 122-125) is the linchpin of the entire benchmark — it determines which Wikidata property is assigned as the ground-truth summary relation. The paper provides zero accuracy metrics for this selection, no ablation, no human evaluation, and no comparison with the ESBM gold standard on overlapping entities. For a benchmark paper, the quality of the ground-truth labels is foundational; without any validation, readers cannot assess whether the summaries are meaningful. This is the most significant weakness.

- **Overclaimed "unbiased" label**: The paper concludes that WES is "an unbiased benchmark" (line 206), but the evidence only rules out frequency-based bias (entity/relation frequency). Other potential sources of bias are unexamined: (a) the DistilBERT property selection itself may introduce systematic errors, (b) entities mentioned early in Wikipedia abstracts may be favored over equally relevant entities mentioned later, (c) the type diversity of selected relations is not analyzed. The evidence supports "avoids the frequency-based bias present in ESBM" but not the broader claim of being unbiased.

- **Paper contains commented-out sections and editorial markup throughout**: The manuscript includes multiple `\comm{...}` blocks containing draft text (lines 19, 43-66), a commented-out Models subsection with baseline results (lines 221-297), and unprocessed `\dm`, `\am`, `\revklim` annotations throughout the body. While some content (e.g., the baseline results table) is also referenced via `\input` commands outside the comments, the presence of these author-internal annotations suggests the manuscript was not prepared for submission. This undermines reviewer confidence in the paper's completeness.

### Minor

- **Only unsupervised baselines evaluated, and only on a reduced dataset**: The empirical evaluation tests only PageRank, RELIN (2011), and LinkSum (2016) — all unsupervised methods — and only on a reduced version of the dataset (lines 212-218). No supervised or neural baselines are included, which limits the paper's demonstration that the benchmark is usable for training modern methods. The paper would be substantially stronger by showing, e.g., a GNN trained on the provided train split.

- **Graph sampling quality not quantitatively validated**: The random walk sampling aims to "preserve the original graph structure" (line 131), but the paper does not compare graph statistics (degree distribution, clustering coefficient, diameter, etc.) between the sampled subgraph and the full Wikidata graph. The only evidence is a qualitative claim that the F-score trend "is comparable to that of the entire data" (line 205), but the underlying figures are not visible in the extracted text.

- **DistilBERT property selection lacks reproducibility details**: The description (lines 122-125) says cosine similarity is computed between the abstract embedding and "embeddings of each candidate relation," but does not specify: (a) how property embeddings are generated (e.g., from property labels? descriptions? averaged over instance triples?), (b) what the candidate set of relations is, (c) whether a threshold or just argmax is used. These details are needed to reproduce the pipeline.

### Trivial
None.

## Nice-to-Haves

- A comparison of WES summaries against ESBM gold-standard summaries for the (mappable) entities appearing in both datasets would provide a direct validation of annotation quality.
- A small-scale human evaluation (e.g., 50-100 entities) where judges rate whether selected triples are relevant to the Wikipedia abstract would strengthen credibility.
- Including a simple supervised baseline (e.g., a GNN or MLP trained on the train split) would demonstrate that the benchmark is practically usable for learning.
- Providing a public link to the dataset and generator code in the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Abstract claims 'equivalent to human performance annotation agreement'"**: The harsh critic states this claim appears in the abstract/introduction. **Fact check**: This phrase appears only at line 19, inside a `\comm{...}` (commented-out) block. The actual abstract (lines 3-9) does not contain this claim. Removed as factually incorrect.

- **"Missing tables/figures from \input commands"**: The critic faults the paper for missing table statistics (from `\input{tables/existing-datasets}`) and figures (from `\input{figs/fig-statistic-*}`). These are LaTeX `\input` commands whose content is stripped by the parser; the paper as submitted would contain them. Removed per parser-artifact rule.

- **"The only mention of annotator agreement appears in a commented-out draft paragraph"**: This is true but the critic uses it to support a broader argument about missing validation. The underlying concern (no validation) is kept as a weakness; the specific framing as evidence of an explicit broken promise is removed because the promise itself wasn't in the visible text.

- **"No link or data sample provided"**: The harsh critic says the paper "provides no link or data sample." Per the rules, the existence/release status of cited resources is assumed; this criticism questions availability. Downgraded from weakness to Nice-to-Have.

- **"Not yet released" / "cannot be independently verified"**: The critic's language about missing release. Removed per hard rules.

## Novel Insights

The most striking observation that emerges from synthesizing the reviews is that the paper's central tension — automatic generation versus quality assurance — mirrors the exact problem it seeks to solve in existing benchmarks. Existing datasets are small because human annotation is expensive; this paper solves the scale problem but creates a new one: how to trust automatically generated ground truth without human verification. The paper's own evidence (frequency-based methods score near random on WES) is clever but only addresses one narrow threat to validity. The deeper insight is that benchmark construction for entity summarization faces a trilemma: human annotation (costly but trustworthy), automatic generation (scalable but unvalidated), or accepting that the benchmark serves a different purpose (e.g., relative comparison of methods rather than absolute evaluation against "correct" summaries). The paper would benefit from explicitly discussing which horn of this trilemma it chooses.

## Suggestions

1. **Validate the summary pipeline**: Add an accuracy evaluation of the DistilBERT property selection on a labeled subset (e.g., 100-200 entities with human-judged correct properties, or entities overlapping with ESBM). Report precision@1 and agreement rates.

2. **Tone down the "unbiased" claim** to "avoids frequency-based annotator bias" and discuss what forms of bias remain unexamined.

3. **Remove all `\comm{...}` blocks and editorial markup** (`\dm`, `\am`, `\revklim`) before resubmission. The Models subsection and baseline results table should be moved into the main body.

4. **Add at least one simple supervised baseline** (e.g., a GNN or even a frequency-based learned ranker) evaluated on the full large dataset to demonstrate that the benchmark supports training.

5. **Provide quantitative validation of graph sampling** by comparing degree distribution, clustering coefficient, or other graph properties of the sampled subgraph against the full Wikidata graph.

## Score and Decision

**Originality**: The automatic summary generation from Wikipedia abstracts is a novel approach to benchmark construction in this space. The degree-proportional random walk sampling is a reasonable methodological contribution.

**Importance of research question**: Entity summarization benchmarks are genuinely limited in scale and suffer from annotator bias. Addressing this is valuable.

**Claims support**: The core claims about the summaries' quality and unbiasedness are not adequately supported. The pipeline lacks validation, and the "unbiased" claim exceeds the evidence.

**Soundness of experiments**: The bias analysis is well-designed for what it checks, but the lack of pipeline validation is a significant gap. The baseline evaluation is thin (3 unsupervised methods, reduced dataset).

**Clarity of writing**: The paper is generally readable but the commented-out sections and editorial markup indicate it is a draft, not a polished submission.

**Value to community**: The generator and benchmark could be valuable if properly validated. As-is, the unknown quality of the summaries limits usefulness.

The paper addresses an important problem with a promising approach, but the lack of validation for the summary annotation pipeline — the core of the benchmark — is a significant gap that prevents acceptance at this stage. The manuscript also contains editorial artifacts suggesting it is not camera-ready. The idea merits development, but the current version does not meet the bar for publication.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**
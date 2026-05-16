Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper proposes DDLR, a dual-denoising framework for inductive knowledge graph completion that combines path-level sampling (via a path-scoring mechanism with current and remaining-path components) and edge-level sampling (via Bernoulli sampling guided by relation-rule confidence). Experiments on WN18RR, FB15k-237, and Nell-995 show SOTA or near-SOTA results across all 12 inductive splits, and ablation studies confirm both denoising components contribute meaningfully.

## Strengths

1. **Novel dual-denoising framework validated by ablation.** The paper identifies a genuine limitation in existing node-based sampling methods (which ignore both path quality and edge relevance) and addresses it with two complementary mechanisms. Table 2 shows that removing either the path-sampling or edge-sampling module consistently degrades performance across all datasets, demonstrating that both components are necessary and their combination is beneficial.

2. **Path-scoring mechanism with explicit current/remaining-path decomposition.** The scoring function \(s_{uq}^{(t)}(x)\) decomposes path importance into an accumulated current-path score and an approximated remaining-path score. Table 3 shows that ablating either subcomponent ("DDLR-w.o.-current" or "DDLR-w.o.-remain") reduces performance, confirming the design's value. The paper acknowledges the approximation challenge for the remaining path (since the answer entity is unknown) and motivates the query-relation-based proxy.

3. **Triplet-level rule confidence for edge sampling.** Using ordered relation-pair confidence (Eq. 14) to guide Bernoulli edge sampling is a principled approach to filtering irrelevant edges. Table 4 shows this triplet-level rule formulation outperforms relation-relevance alternatives (cosine similarity, KL divergence, JS divergence), and Table 2 shows that switching from triplet-level to entity-level rules (DDLR-w.o.-triplet) hurts performance.

4. **Consistent SOTA or near-SOTA empirical results.** On three standard inductive KGC benchmarks with four splits each (12 settings total), DDLR achieves best or second-best MRR and Hits@10 on every split (Table 1), outperforming strong baselines including NBFNet, RED-GNN, Adaprop, and GraPE.

## Weaknesses

### Fatal
None.

### Major

1. **Eq. 14 (single-rule confidence) is ambiguously specified.** The formula writes \(\mathcal{C}(r_{1}\Rightarrow r_{2}) = \frac{\sum_{t\in\mathcal{E}}\mathbb{1}(r_{1}\in\mathbf{E}_{r}(t) \wedge r_{2}\in\mathbf{E}_{r}(t))}{\sum_{t\in\mathcal{E}}\mathbb{1}(r_{1}\in\mathbf{E}_{r}(t))}\), where \(\mathcal{E}\) is defined as the set of triplets/facts (each a single-relation edge). If \(t\) iterates over individual triplets, then each \(t\) has exactly one relation, making the numerator zero for any distinct \(r_{1}\neq r_{2}\). The text clarifies the intended meaning ("more triplets with relation \(r_{1}\) also have \(r_{2}\)" — standard entity-pair co-occurrence counting), but the formal definition does not match this description. This is not a fatal error: the ablation studies (Tables 2, 4) independently verify that the edge-sampling component improves performance, so the *implementation* clearly computes something meaningful. However, the formula as written is formally incorrect and must be corrected before the paper can be accepted. **(Structural notation error; requires a rewrite of Eq. 14 and surrounding text.)**

### Minor

2. **Missing variance/statistical significance.** No standard deviations, confidence intervals, or significance tests are reported. Many improvements over baselines are modest (e.g., +0.3–1.0 MRR points on several splits), making it unclear whether these gains are statistically reliable. This is a standard expectation for experimental ML papers.

3. **Remaining-path approximation lacks deeper validation.** The paper uses \(\mathbf{r}_{q}^{(t)}(x,v) = \mathbf{h}_{q}^{(t)}(u,x) \otimes g([\mathbf{h}_{q}^{(t)}(u,x), \mathbf{q}])\) as an approximation for the path suffix (because the answer entity \(v\) is unknown). While the ablation in Table 3 confirms that removing this component hurts performance, this only validates that *some* signal from the remaining path helps — it does not validate that *this specific form* of approximation is reasonable or near-optimal. The paper would benefit from either a simpler baseline comparison (e.g., a learned bias per node) or a qualitative analysis showing how the approximation behaves on concrete examples like Fig. 1.

4. **Top-K for paths vs. criticism of top-K.** The paper criticizes node-based top-K methods (e.g., Adaprop) for discarding information, then uses a top-K selection for path sampling (Eq. 11) while using Bernoulli sampling (non-hard) only for edges. The paper should justify why hard top-K is acceptable for paths when it was criticized for nodes — or acknowledge this as a design limitation.

5. **Missing computational cost reporting.** The paper does not report training time, memory usage, or model size relative to baselines. Since DDLR adds two sampling steps per iteration, this information is needed for practitioners to assess practical trade-offs.

### Trivial

6. **"KBGAT (Yang et al., 2015)"** — The commonly cited KBGAT paper is Nathani et al. (2019). The reference here may be a different work or a citation error, but it does not affect the paper's contributions.

7. **Missing sensitivity analysis for \(p_{e}\) and \(p_{\tau}\).** These hyperparameters control edge sampling, listed in the search ranges but with no analysis of how performance varies with their values.

## Nice-to-Haves

- A qualitative example (extending Fig. 1) showing where the remaining-path score correctly up-weights a correct answer and where omitting it fails would strengthen the path-scoring motivation.
- Reporting results with standard deviations over 3–5 random seeds would address statistical-concern questions preemptively.
- A comparison with a simpler remaining-path baseline (e.g., a learned scalar per node) would better validate the specific form of the approximation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Cannot be independently verified / not yet released"* — Removed per hard rules: cited models and datasets are assumed to exist.
- *"Pure formatting/typo nitpicks"* (e.g., "typos, garbled text") — Removed; these are parser artifacts.
- *"Missing related work on X"* — Removed; I cannot verify existence of missing references without external sources.
- *"The paper should also cover multi-hop queries"* — Removed as scope creep; the paper explicitly scopes out multi-hop queries as future work in the conclusion.
- *The harsh critic's characterization of Eq. 14 as "structural error that prevents acceptance" / "fatal"* — Downgraded to Major. The empirical evidence (ablation studies) shows the edge-sampling component works; the issue is a notation/specification error, not a methodological invalidation. The intended meaning (entity-pair co-occurrence) is standard in KG rule mining and recoverable from context.
- *"The paper should add more methods/baselines the reviewer prefers"* — Removed; the paper's baseline selection is defensible.

## Novel Insights

The reviews surface one insight that goes beyond the paper's own framing: the tension between criticizing top-K node scoring and then applying top-K path scoring is not merely a presentation issue — it highlights an underexplored design space. The paper's real advance may not be "avoiding top-K" (since paths still use top-K) but rather improving the *quality* of the scoring function that top-K operates on, and adding a separate edge-level filter that operates via probabilistic (Bernoulli) sampling. This suggests that the contribution is better described as "better scoring + complementary edge filtering" rather than "overcoming top-K limitations."

## Suggestions

1. **Fix Eq. 14.** Rewrite the confidence definition to explicitly operate at the entity-pair level, e.g., \(\mathcal{C}(r_1 \Rightarrow r_2) = \frac{|\{(h,t): (h,r_1,t) \in \mathcal{G} \land (h,r_2,t) \in \mathcal{G}\}|}{|\{(h,t): (h,r_1,t) \in \mathcal{G}\}|}\), and clearly define \(\mathbf{E}_r\) as the set of relations for a given entity pair. The current sum-over-triplets notation is formally incorrect.

2. **Report standard deviations** for main results (Table 1) over at least 3 random seeds. Also clarify whether hyperparameters were chosen on a validation set.

3. **Acknowledge the top-K tension.** Add a sentence justifying why top-K is used for path selection while Bernoulli sampling is used for edges (e.g., "path scoring is more reliable due to the learned scoring function, while edges benefit from probabilistic selection to avoid hard loss of rare relations").

4. **Add a simple remaining-path baseline.** Compare the current remaining-path approximation against a per-node learned bias or a fixed scalar to strengthen the validation of the specific design.

## Score and Decision

This paper makes a clear contribution — a dual-denoising framework with two well-motivated components, supported by comprehensive ablation studies and strong empirical results across 12 inductive KGC settings. The main concern (Eq. 14 notation) is a specification error that requires correction but does not invalidate the method or the empirical conclusions. The remaining issues (missing variance, approximation validation depth) are addressable. The paper merits acceptance after the notational fix to Eq. 14.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
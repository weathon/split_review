Now I have all the information I need. Let me compile my final consolidated review.

---

## Summary

This paper proposes QuaCer-C, a framework for certifying LLMs' performance on knowledge-comprehension-like tasks with formal probabilistic guarantees. The key idea is to define a distribution over multi-hop reasoning prompts derived from knowledge graphs (Wikidata5m) using a probabilistic program, then apply Clopper-Pearson confidence intervals to produce high-confidence bounds on the probability of correct response. Experiments on several open-source and closed-source LLMs (Llama-3, Mistral, Phi-3, Gemini, GPT-4o) demonstrate feasibility and show that bounds are consistent with known scaling trends.

## Strengths

1. **First framework for distribution-level probabilistic certification of LLMs on KG-derived tasks.** Unlike prior benchmarking studies that report point estimates on static datasets, QuaCer-C produces provably high-confidence intervals on the probability of correct response under a specified distribution. This is a genuine methodological advance (stated in abstract, Section 3).

2. **Novel specification mechanism using probabilistic programs over knowledge graphs.** Encoding the prompt distribution as a probabilistic program (Algorithm 1) with explicit sampling steps for path length, path selection, alias selection, distractors, and shuffling makes the certification target precise and reproducible. This goes beyond ad-hoc benchmark construction (Section 3.1, Definitions 3.1–3.3).

3. **Black-box method that applies to API-access models.** By using Clopper-Pearson intervals with i.i.d. samples, the method works for both open-weight and closed-source LLMs without requiring model internals (Section 3.2). This includes Gemini and GPT-4o in the experiments.

4. **Systematic study of distractor and shuffling effects.** The paper examines three specification variants (Shuffle Distractor, Shuffle, Vanilla) and shows that these design choices meaningfully affect the certified bounds, providing insight beyond what a single accuracy number would reveal (Section 4.1, Table 1).

## Weaknesses

### Fatal
None.

### Major

1. **The framing substantially overclaims what is certified.** The paper invokes Bloom's taxonomy, TOEFL, and IELTS to motivate "knowledge comprehension" as an educational construct (intro), then operationalizes it as answering multi-hop queries from KG paths with all node contexts provided. A TOEFL reading comprehension test requires understanding connected prose, identifying main ideas, and drawing inferences from natural text — not following a pre-defined relational path through a graph with entity contexts spoon-fed. The paper's operationalization is defensible on its own terms (line 64 provides a clear definition), but the Bloom's/TOEFL/IELTS framing creates an expectation of a much broader capability. The abstract claims "the first framework to certify knowledge comprehension in LLMs," which will mislead readers who interpret "knowledge comprehension" in the educational-assessment sense. The paper should either (a) argue why KG-path-based multi-hop QA faithfully captures the educational construct, or (b) retreat to describing what is actually certified: "the probability of correct response under a specified distribution of multi-hop reasoning prompts derived from a knowledge graph." The current framing overstates the scope.

### Minor

2. **Practical utility for deployment is asserted but not grounded.** The introduction motivates formal guarantees as crucial for deploying LLMs in "critical domains such as medicine or finance." However, the certificate is a confidence interval on performance under a specific, researcher-designed prompt distribution over a specific KG subgraph. The paper does not discuss how a practitioner would bridge the gap between the certification distribution and a deployment distribution, nor does it acknowledge this as a limitation. This does not invalidate the technical contribution, but the claimed practical value is aspirational rather than demonstrated.

3. **The "baseline" comparison is a sanity check, not a meaningful evaluation.** The paper frames a static-dataset accuracy estimate (50 paths per subgraph) as a "baseline" to compare against. Since Clopper-Pearson intervals are designed to contain the true probability with at least the nominal confidence, any unbiased accuracy estimate from the same distribution will fall inside the interval by construction. This provides no evidence about the quality of the specification or the tightness of the bounds. The paper would be better served by reporting interval widths explicitly and comparing against alternative bounds (e.g., Hoeffding, Bernstein) or showing how bounds tighten with increasing sample size.

4. **The distractor sampling weights are not fully specified in the main text.** The paper states that distractors are sampled with "weighted sampling to prioritize distractor nodes closer to the path's tail" and references Algorithm 4 (appendix). While details can reside in the appendix, the main text should at minimum state the weighting scheme's objective and its effect on the prompt distribution, since the certificate is defined *relative to* that distribution. As written, a reader cannot determine from the main text alone what distribution is being certified.

### Trivial

5. **The answer validation procedure could be more explicit.** The specification says correctness is determined by whether the LLM generates "any alias of the last node" (line 102, line 109). It is not stated whether this is exact match, substring match, or alias-set membership. This is important reproducibility info.

## Nice-to-Haves

- Report interval widths explicitly alongside bounds. If widths are large (e.g., >0.2), discussing whether they are practically informative would strengthen the paper.
- Add a limitations paragraph discussing the distribution-dependence of certificates and the challenge of transferring guarantees between certification and deployment distributions.
- Compare interval widths across specification variants (Shuffle Distractor, Shuffle, Vanilla) to show which distributional choices most affect tightness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about missing tables in extracted text.** This is a PDF-parser artifact; tables exist in the original submission. [REMOVED: parser artifact]
- **Criticism that answer validation method is not described.** The paper specifies success as generating "any alias of the last node." This is sufficiently clear. [REMOVED: strawman — paper already addresses this]
- **Criticism that CoT reasoning results are mentioned but implementation is not described.** The CoT discussion appears in a section that is clearly garbled by PDF extraction. [REMOVED: parser artifact; the original paper likely contains this detail]
- **Strength Finder strength #1 phrasing as "first framework" may conflict with framing criticism.** Decided to keep this as a valid strength since the paper is genuinely novel in its approach, but the framing overclaim is separately noted as a weakness. No removal needed.
- **Criticism that the paper should add more models/baselines/benchmarks to the experiments.** The model zoo is already adequate for a methodology paper. [REMOVED: scope creep]

## Novel Insights

The harsh critic identifies a genuine tension that goes beyond the paper's own discussion: the paper invokes human educational testing (Bloom's taxonomy, TOEFL) to motivate "knowledge comprehension," but the formal specification operationalizes this as a graph-path-following task with pre-segmented entity contexts. This gap between *what educational assessments measure* and *what KG-path multi-hop QA tasks measure* is not just a naming issue — it reflects a deeper question about what it means to "certify comprehension" versus "certify performance on a structured information-retrieval-and-reasoning task." The paper's framework is well-suited to the latter but the framing claims the former. Clarifying this distinction would make the contribution both more honest and more useful, because the real value of the framework is in providing rigorous bounds on a well-specified narrow capability, not in claiming to certify a broad cognitive construct.

## Suggestions

1. **Revise the title and framing.** Replace "Certifying Knowledge Comprehension" with more precise language such as "Certifying Multi-Hop Reasoning Over Knowledge Graphs" or "Certifying LLM Performance on KG-Derived QA Distributions." If the Bloom's taxonomy framing is kept, include an explicit argument for why the operationalization is a faithful proxy.
2. **Add a limitations section** that discusses: (a) the certificate's distribution-dependence, (b) the gap between certification and deployment distributions, (c) the scope of what is actually certified.
3. **Report interval widths** and discuss when they are tight enough to be practically informative.
4. **Specify distractor sampling weights** and the answer validation procedure in the main text.
5. **Reframe the baseline** as a sanity check rather than a comparison, and consider adding ablation studies (e.g., how bounds change with n, or comparison to simple Hoeffding bounds).

## Score and Decision

The paper presents a sound and novel framework. The core technical contribution — using probabilistic programs over knowledge graphs to specify prompt distributions and Clopper-Pearson intervals to certify LLM performance — is genuine and publishable. The experiments demonstrate feasibility across a reasonable range of models. The paper's most significant flaw is the framing overclaim (weakness #1), not an error in the method itself. With revisions to scope the claims appropriately and address the minor weaknesses, this would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
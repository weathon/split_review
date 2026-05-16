Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper introduces a causal mediation analysis framework (ADCE and AICE) to quantify whether LLMs comprehend deep (semantic) structure or merely exploit surface (presentational) structure. The framework defines deep structure comprehension as the direct causal effect of deep structure on LLM outputs, proposes observable surrogates (ADCE/AICE) to address the fundamental non-estimability of the true causal effects, and evaluates 12 LLMs across 5 tasks. Key findings include: most LLMs exhibit positive ADCE indicating genuine deep structure comprehension; closed-source models rely more on deep structure while open-source models shift from surface to deep with scale; and ADCE detects spurious-correlation reliance better than accuracy.

## Strengths

1. **Well-motivated formalization of deep vs. surface comprehension via causal mediation analysis.** The paper grounds the abstract notion of "comprehension" in the causal estimands of direct and indirect effects (Section 3.1), providing a principled, task-agnostic framework that moves beyond prior work tied to specific tasks (data flow, synthetic templates) or small models.

2. **Comprehensive empirical evaluation across 12 LLMs and 5 diverse tasks.** The paper tests models spanning Llama-2/3, Mistral/Mixtral, GPT-3.5/4o, and Claude-3/3.5 on mathematics (2-digit multiplication, GSM8k), logic (Word Unscrambling, Analytic Entailment), and commonsense reasoning (CommonsenseQA), demonstrating consistently positive ADCE for non-random models (Figure 3). This breadth supports the generality claim.

3. **Reveals meaningful distinctions between model families.** The comparison of ADCE (deep) and AICE (surface) shows closed-source models (GPT, Claude) exhibit greater deep-structure reliance, while open-source models (Llama) show higher surface sensitivity that decreases with scale (Figure 5). This is a novel empirical finding that provides actionable insight for model development.

4. **Spurious correlation experiment validates ADCE's advantage over accuracy.** In the CivilComments experiment (Section 4.4, Figure 6), as spurious correlation between identity terms and toxicity increases, accuracy remains misleadingly high in the majority group while ADCE correctly declines — directly supporting the paper's theoretical claim that ADCE captures bidirectional deep-structure dependency beyond mere correctness.

5. **Theoretical connection to probability of sufficiency and necessity.** Theorem 1 shows ADCE is a weighted combination of PS and PN, formally establishing that ADCE captures both sufficiency and necessity of deep structure changes — a property accuracy lacks (Section 3.4). This provides a principled justification for why ADCE is more informative than accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **The AICE approximation lacks empirical validation.** The paper's central methodological challenge is that the oracle ICE (which requires $T=0$ and $s(T=1)$ simultaneously) is unobservable, so AICE substitutes $(T=0, s(T=0))$. The paper acknowledges this (Section 3.2: "The efficacy of this approximation hinges on the similarity") and designs intervention strategies to minimize the discrepancy. However, **no quantitative evidence is provided** that the surface structures of TE and AICE are indeed similar — neither human annotation, automated similarity metrics, nor formal bounds on the approximation error. Without this, the magnitude and direction of potential bias in ADCE are unknown. This does not invalidate the approach (the strategies are well-motivated and the results are internally consistent), but it is the single biggest gap that limits confidence in ADCE as a precise measure of deep structure comprehension.

2. **No uncertainty quantification.** Key figures reporting ADCE and AICE values (Figures 3, 5, 6) show only point estimates without confidence intervals, error bars, or variance estimates. ADCE is computed on correctly answered samples whose count varies across model-task combinations (some models have very few correct answers on hard tasks). The stability of these estimates is unknown, making it impossible to assess whether observed differences between models (e.g., closed-source vs. open-source in Figure 5) are statistically significant.

### Minor

3. **The conceptual definition of comprehension (Eq. 1) and the proposed metric (ADCE) are not tightly linked.** Eq. 1 defines comprehension as a deterministic binary property per sample (output changes *iff* deep structure changes). ADCE is a continuous population-level quantity. The paper shows the ideal case (Eq. 1 holds for all samples → ADCE = 1) and interprets larger ADCE as stronger comprehension, but does not formally derive what intermediate ADCE values mean in terms of the proportion of samples satisfying Eq. 1. The interpretation is reasonable and follows standard practice in causal inference, but the gap between the crisp definition and the continuous metric leaves room for alternative interpretations.

4. **ADCE is computed only on correctly answered samples, creating a potential selection issue in the accuracy-ADCE correlation analysis.** The pipeline restricts ADCE computation to $\mathcal{D}_c$ (samples the model got right). The paper then reports a strong linear correlation ($R^2 > 0.7$) between accuracy and ADCE across models (Section 4.2, Figure 3). However, the set of samples contributing to ADCE changes with accuracy: models with higher accuracy contribute a larger and potentially different set of samples. This compositional shift could inflate the correlation mechanically. The paper does not discuss or control for this.

5. **The SFT experiment (Section 4.3) does not disentangle ADCE improvement from accuracy improvement.** Fine-tuning Llama-3-8b on Analytic Entailment increases both ADCE and (presumably) accuracy. The paper attributes the ADCE increase to "activation of task-relevant knowledge," but ADCE could rise simply because the model answers more questions correctly (changing the composition of $\mathcal{D}_c$). A control analysis matching accuracy levels or computing ADCE on a fixed subset would strengthen the claim.

6. **CivilComments experiment lacks explicit definition of deep/surface structure in the main text.** The paper describes manipulating spurious correlations between identity terms and toxicity labels but does not specify in the main text what constitutes deep vs. surface structure for this task, nor how the intervention strategies (Mask/Rephrase) are operationalized for toxicity detection. The details are referenced to the appendix. While this is standard practice, the main text should provide enough context for the reader to evaluate the experimental design without consulting supplementary material.

### Trivial
None that survive the removal rules.

## Nice-to-Haves

- Formal bounds or empirical similarity metrics (e.g., BERTScore, human evaluation) comparing the surface structure of TE and AICE would substantially strengthen the methodological foundation.
- Bootstrap confidence intervals for ADCE and AICE estimates would allow readers to assess the reliability of cross-model comparisons.
- A derivation showing how ADCE relates to the expected proportion of samples satisfying Eq. 1 under mild assumptions would bridge the definitional gap.
- The theoretical connection to PS/PN (Theorem 1) could be leveraged more directly — e.g., testing whether empirical PN and PS values align with ADCE predictions would validate the framework.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about $d \perp s \mid \vx$ being contradictory**: The reviewer claims the conditional independence assumption is contradictory because "if $\vx$ determines both $d$ and $s$, they are not independent conditional on $\vx$." This misunderstands the paper's notation: $\vx_i := (d_i, s_i)$ means each question decomposes into deep and surface components; the conditional independence $d_i \perp\!\!\!\perp s_i \mid \vx_i$ is a standard modeling assumption in causal mediation analysis (citing Stolfo et al., 2022) and is trivially satisfied when $\vx$ determines both. The exposition could be clearer, but the assumption itself is not contradictory.

- **Criticism about the motivational experiment (Fig. 1) using only one model**: The reviewer calls this a weakness of the paper. However, Figure 1 is explicitly presented as a *motivational* experiment to illustrate the research question, not as a core result. The paper's main empirical contributions involve 12 models. This is not a substantive weakness.

- **Criticism that Theorem 1 is "tangential" and "limited novelty"**: Theorem 1 connects ADCE to the well-known PS/PN framework. While the derivation itself is not technically novel, its *application* in this context — showing that ADCE captures bidirectional sufficiency/necessity of deep structure — is used to motivate the spurious correlation experiment and to argue ADCE's superiority over accuracy. The theorem is appropriately scoped and is not claimed as a novel theoretical breakthrough.

- **Criticism about CivilComments details being "relegated to an appendix we cannot see"**: The parser strips appendices from all papers; the appendix exists in the original submission. The relevant concern (main-text completeness) is preserved in Minor weakness #6.

- **Criticism that AICE and ADCE "are measured on different intervention conditions" and comparability is questionable**: ADCE and AICE in Eq. 8 are both expectations of indicator functions over the same set of samples, on the same $[-1,1]$ scale. The paper's interpretation of relative magnitudes is standard and justified.

## Novel Insights

The reviews surface a tension that the paper itself does not fully address: the gap between the crisp philosophical definition of "comprehension" (output depends *only* on deep structure — Eq. 1) and the practical continuous metric (ADCE). This tension is common in causal inference (ideal determinism vs. probabilistic measurement) but is worth articulating because it clarifies what ADCE actually measures: the *average marginal effect* of deep structure changes on output, controlling for surface changes, which is substantively different from the strong condition in Eq. 1. A paper that directly formalizes this gap — showing that ADCE measures the *proportion of variance* in output changes attributable to deep structure rather than the deterministic condition — would strengthen the conceptual contribution.

## Suggestions

1. **Validate the AICE approximation.** Add a human evaluation or automated similarity metric (e.g., BERTScore, n-gram overlap) comparing the surface structures of TE and AICE for a random sample of interventions, and report the distribution of similarity scores. Alternatively, derive an upper bound on the discrepancy $|\text{ICE} - \text{AICE}|$ under assumptions about the intervention design. This single addition would substantially increase confidence in the metric.

2. **Add bootstrap confidence intervals** to all ADCE/AICE estimates and statistical tests (e.g., test whether the ADCE difference between model families is significant).

3. **Address the selection issue** in the accuracy-ADCE correlation by either (a) computing ADCE on a held-out set of samples that *all* models answer correctly, or (b) showing that the correlation persists when controlling for the number of correct samples, or (c) explicitly discussing this limitation.

4. **Clarify the conceptual link** between Eq. 1 and ADCE by deriving $ADCE = \mathbb{P}(\text{Eq. 1 holds})$ under suitable assumptions, or acknowledge the gap explicitly and state that ADCE measures a related but weaker property.

5. **Provide a brief in-text description** of how deep/surface interventions are operationalized for the CivilComments experiment, even if details remain in the appendix.

## Score and Decision

This paper tackles a well-motivated and timely question with a principled causal framework, comprehensive empirical evaluation, and a theoretically grounded metric. The main findings — that LLMs exhibit genuine deep structure comprehension, that closed-source models rely more on deep structure while open-source models become less surface-sensitive with scale, and that ADCE outperforms accuracy under spurious correlations — are interesting and supported by the experiments. However, the paper's central methodological vulnerability (the unvalidated AICE approximation) and the lack of uncertainty quantification prevent full confidence in the precision of the reported estimates. These issues are addressable and do not invalidate the overall contribution, but they limit the paper's current strength. I recommend acceptance with the expectation that the authors address the major concerns in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
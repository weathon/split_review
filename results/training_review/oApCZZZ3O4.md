Here is my consolidated review.

---

## Summary

This paper proposes Knowledge Graph Tuning (KGT), a method for real-time LLM personalization that modifies an external knowledge graph (ConceptNet) rather than model parameters. Given user feedback (e.g., "my dog is vegetarian"), KGT extracts personalized factual triples, then adds/removes triples from the KG based on their "reasoning probability" — how much they help the LLM produce the desired answer — while leaving all model parameters frozen. Experiments on GPT2, Llama2-7B, and Llama3-8B with CounterFact and CounterFactExtend datasets show large gains in personalization efficacy (e.g., 94.58% vs. 54.44% for fine-tuning on Llama3) alongside significant reductions in latency and GPU memory.

---

## Strengths

1. **Novel and conceptually clean contribution**: Instead of modifying model parameters (which is expensive and uninterpretable), KGT edits an external KG — adding and removing human-comprehensible triples. This reframes personalization as a KG-optimization problem, which is both efficient and transparent.

2. **Large and consistent empirical gains**: On both datasets and across all three LLMs, KGT dramatically outperforms every baseline (FT, ROME, KE, KN, MEND, no-edit) on both efficacy and paraphrase scores. On Llama3-8B (CounterFact), KGT achieves 94.58% efficacy vs. the best baseline (FT) at 54.44% (Table 1). These gains hold on the more challenging CounterFactExtend dataset (Table 2).

3. **Compelling efficiency improvements**: KGT requires only inference (no backpropagation), yielding up to 84% latency reduction and 77% GPU memory reduction compared to baselines (Table 3). For Llama3-8B, KGT uses 15.9GB GPU memory vs. 69.5GB for KE, and 0.15s latency vs. 2.05s for ROME.

4. **Scalability demonstrated**: As the query set grows, KGT maintains high efficacy (~90%) while baselines degrade sharply (Figure 4/Fig:query_size). This is essential for long-term use where personalized knowledge accumulates.

5. **Ablation shows user effort is minimal**: KGT works well even without explicit relation feedback from the user — the LLM itself can extract relations with similar or better performance (Figure 3/Fig:hf).

---

## Weaknesses

### Fatal
None.

### Major

1. **No evaluation of side effects on general knowledge** — The paper's algorithm removes triples from ConceptNet (e.g., potentially "Dog, Is, Animal") to make room for personalized facts. The paper's design principle (§4.3) is to "preserve more knowledge," yet no experiment measures whether these removals degrade the model's responses to *unrelated* queries. Without measuring retention on general factual knowledge (e.g., MMLU, a held-out set of unrelated queries, or specificity metrics), the safety of long-term personalization is unverified. This is the most significant gap in the evaluation.

2. **Loose connection between the ELBO formulation and the actual optimization algorithm** — The paper derives an ELBO objective (Eq. 2) with explicit knowledge-retrieval and knowledge-enhanced-reasoning terms. However, the actual algorithm (Alg. 1) is a greedy heuristic that ranks triples by reasoning probability P(a|q,z) and uses the combined loss only as a stopping criterion. It does not directly optimize the KL divergence term that governs retrieval probability. While the loss provides a principled stopping condition, the algorithm does not search over the KG space in a way that clearly minimizes the ELBO. The theoretical framing and the practical procedure feel somewhat decoupled.

### Minor

1. **Posterior distribution assumption is arbitrary** — The paper assumes a uniform distribution Q(z) over the K extracted personalized triples (Eq. 3). This is a reasonable default but has no empirical or theoretical justification. The paper does not analyze sensitivity to this choice (e.g., what if K is too large and some extracted relations are spurious?).

2. **Computational cost of retrieval probability normalization is not discussed** — Eq. 4 normalizes P(z|q) over all triples in G that start from e_q. In ConceptNet, entities can have many outgoing triples; the paper does not report the average size of G_{q_t} or analyze how this normalization cost scales. The 0.15s latency on Llama3 is also surprising given that Algorithm 1 computes P(a|q,z) multiple times (once per candidate triple in each iteration) — the paper should clarify the number of forward passes per query.

3. **Limited scope of personalization evaluation** — The datasets (CounterFact, CounterFactExtend) only contain factual counterfactual statements. Real personalization involves diverse user feedback: preferences, routines, opinions, procedural knowledge. The paper would benefit from acknowledging this scope limitation more explicitly and demonstrating the approach on a broader set of personalized scenarios.

### Trivial
None.

---

## Nice-to-Haves

- An analysis of how many triples are removed during optimization, and whether these removals affect other queries (the paper notes this concern but provides no data).
- A controlled comparison where baselines also have the same KG presented via in-context learning, to isolate the benefit of KG tuning from the mere presence of the KG (though the current setup already gives all models access to ConceptNet).
- Sensitivity analysis on K (number of extracted relations) and the loss threshold ε.
- Example case studies showing how reasoning probabilities change as triples are added/removed.

---

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Unfair baseline comparison: baselines do not use a KG"** — Factually incorrect. The paper states (line 231): "We equip each model with a KG, ConceptNet, to enhance the inference." All models (including baselines) have access to the same initial KG. The comparison is between parameter-tuning + KG vs. KG-tuning + KG, which is a controlled comparison.

2. **"Non-monotonic performance with model size"** — Factually incorrect. Table 2 shows KGT efficacy on CounterFactExtend is strictly increasing with model size: GPT2 (82.57%) → Llama2-7B (90.68%) → Llama3-8B (93.80%). This is monotonic.

3. **"Latency of 0.15s for KGT on Llama3 vs 0.16s on GPT2 is suspicious"** — The 0.01s difference is negligible and likely within measurement noise or due to different convergence behavior. This is a nitpick without substance.

4. **Various pure presentation/formatting/style nitpicks** (e.g., "the derivation needs more justification," "missing appendix content," references to sections stripped by the parser).

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that substantially reframes or deepens the paper's message beyond what the authors already state.

---

## Suggestions

1. **Add a side-effect evaluation:** Measure the model's performance on a general-knowledge benchmark (e.g., MMLU, a held-out subset of unrelated QA pairs) before and after personalization with KGT. Report both efficacy (on personalized queries) and retention (on general queries). This is the single most important addition to validate the method's safety for real deployment.

2. **Strengthen the ELBO-to-algorithm connection:** Either (a) derive the heuristic from the ELBO more explicitly, showing that the add/remove ordering approximates a coordinate descent on the loss, or (b) reframe the contribution as a practical algorithm inspired by the ELBO rather than derived from it. Either approach resolves the current conceptual gap.

3. **Report the number of triples added/removed per query on average**, along with the size of G_{q_t}, to help readers assess the computational cost and the degree of KG modification.

4. **Test with a broader personalization dataset** beyond counterfactual facts — e.g., incorporating user preferences or routines — to demonstrate generality.

---

## Score and Decision

**Originality:** Good — reframing personalization as KG optimization rather than parameter editing is genuinely novel.  
**Importance of question:** High — real-time, efficient, interpretable personalization is practically important.  
**Claims well-supported:** Mostly yes, but the claim of knowledge preservation lacks side-effect evaluation.  
**Soundness of experiments:** Solid in showing efficacy/efficiency; missing side-effect measurement.  
**Clarity of writing:** Clear and well-structured.  
**Value to community:** The efficiency numbers and the KG-tuning paradigm are compelling contributions that could influence future personalization work.

The core contribution is valuable, the results are strong, and the main evaluation gap (side effects on general knowledge) is addressable. The paper should not be penalized for the harsh critic's factually incorrect claims about baseline fairness.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>
Now I have a thorough understanding of the paper and can verify each claim. Let me compose the final consolidated review.

---

## Summary

This paper proposes Knowledge Graph Tuning (KGT), a method for LLM personalization that edits an external knowledge graph (ConceptNet) rather than modifying model parameters. The approach derives an ELBO-based objective with knowledge-retrieval and knowledge-enhanced-reasoning terms, then optimizes the KG through a heuristic add/remove algorithm using only LLM inference (no backpropagation). Experiments across GPT-2, Llama2-7B, and Llama3-8B show large improvements in personalization efficacy (e.g., 94.58% vs. ~54% for fine-tuning on CounterFact with Llama3-8B) alongside substantial reductions in latency and GPU memory.

## Strengths

1. **Novel and practical paradigm for LLM personalization.** Instead of modifying model parameters (which is costly and opaque), KGT edits an external KG through human-comprehensible triple additions/removals. This is a genuinely different approach from PEFT, knowledge editing, and in-context learning, and directly addresses the efficiency and interpretability challenges the paper identifies.

2. **Large and consistent empirical gains across multiple LLMs.** On CounterFact, KGT achieves 94.58% efficacy and 86.89% paraphrase score with Llama3-8B, outperforming the next-best baseline (FT at 54.44% efficacy) by roughly 40 percentage points. Similar margins hold for GPT-2 and Llama2-7B, and on the second dataset CounterFactExtend. The gains are not model-specific.

3. **Order-of-magnitude efficiency improvements.** By eliminating backpropagation, KGT reduces latency to 0.15s (vs. 0.25s for FT and 2.05s for ROME on Llama3-8B) and GPU memory to 15,904MB (vs. 36,968MB for FT). These savings are critical for real-time on-device personalization.

4. **Scalability demonstrated with increasing query set size.** Figure 3 shows that baseline methods degrade significantly as query volume grows (e.g., from ~60% to ~35% efficacy), while KGT maintains roughly 90% efficacy. This supports the claim of suitability for long-term knowledge accumulation.

5. **Explicit interpretability through transparent KG edits.** The add/remove operations produce human-readable triple changes (e.g., adding (Dog, Enjoy, Vegetable)), in contrast to the opaque parameter modifications of baselines.

## Weaknesses

### Fatal
None.

### Major

1. **Retrieval probability definition depends only on relations, creating a gap between the theoretical ELBO derivation and what the KL term can actually optimize.** Equation (6) defines \(P_{\theta,\mathcal{G}}(z|q)\) using \(P_\theta(r|\mathcal{T}_{\text{retrieve}}(q))\) in the numerator, which depends only on the relation \(r\) and not on the object entity \(e'\). Consequently, two triples with the same subject and relation but different objects — e.g., (Dog, Enjoy, Meat) and (Dog, Enjoy, Vegetable) — receive identical retrieval probabilities if both are in \(\mathcal{G}\). The KL divergence term \(\mathcal{L}_{\text{retrieve}}\) therefore cannot distinguish between these triples. The reasoning term \(\mathcal{L}_{\text{reasoning}}\) can still guide object-level discrimination through \(P(a|q,z)\), and the algorithm's add/remove operations can handle object-level preferences. But the stated ELBO-based justification is weakened: the retrieval term in the loss alone cannot achieve "high personalized knowledge retrieval probability" for the correct triple when multiple triples share a relation. The theoretical framing over-promises relative to what the formulation delivers.

2. **The optimization algorithm's loss computation is ill-specified, with a log(0) pathology.** The loss in Algorithm 1 (line 196/203/209) is \(\mathcal{L} = -\frac{1}{K}\sum_{z\in\mathcal{H}(q_t,a_t,K)} \log[P(a_t|q_t,z)P(z|q_t)]\). By the paper's own definition (Equation 6), \(P(z|q_t)=0\) if \(z\notin\mathcal{G}\). Since the candidate triples in \(\mathcal{H}(q_t,a_t,K)\) are not yet in \(\mathcal{G}\) at initialization, every term contains \(\log(0) = -\infty\), making the loss infinite. After adding one triple, the remaining \(K-1\) still contribute \(-\infty\). The break condition \(\mathcal{L}\leq\epsilon\) therefore cannot trigger until all \(K\) triples have been added, rendering the iterative addition and early-termination logic unworkable as written. The paper gives no indication of how this is handled in practice. The actual implementation almost certainly differs from the pseudocode, but the presented algorithm cannot be executed as described.

### Minor

1. **No measurement of knowledge retention across queries.** The algorithm removes triples with low reasoning probability for the *current* query, which could erase knowledge critical for previously personalized queries. The paper evaluates scalability in terms of query set size (Figure 3) but never measures whether earlier personalization persists after later queries are processed. Without this measurement, the claim of "fulfilling long-term needs" is only partially supported.

2. **KG-enhancement status of baselines is ambiguous.** The paper states "We equip each model with a KG, ConceptNet, to enhance the inference" (line 231), suggesting all models use ConceptNet. However, it is not explicitly stated whether the parameter-editing baselines (FT, ROME, KE, KN, MEND) operate on top of the same KG-enhanced LLM pipeline or on a bare LLM. If the latter, the structural advantage of having an editable external KG would partially explain the large performance gap. A clarifying statement would resolve this.

3. **"No edit" baseline reported without variance.** Tables 1 and 2 report "no edit" as a single percentage without standard deviation, while all other methods include \(\pm\) values. This is inconsistent.

### Trivial
None.

## Nice-to-Haves

- An analysis of systematic failure cases: e.g., when the subject entity is absent from ConceptNet, when the LLM cannot follow instructions for relation extraction, or sensitivity to the choice of \(K\).
- A discussion of how KG size is managed in long-term deployment. The current approach assumes unbounded growth; a practical system would need a pruning or aggregation strategy beyond per-query removal.
- Ablation isolating KGT's contribution *without* the KG (base LLM only) to disentangle the effect of KG editing from the effect of having external knowledge at inference time.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"The KG-enhanced LLM inference pipeline is underspecified"** — The paper provides instruction templates for \(P(z|q)\) and \(P(a|q,z)\), specifies entity linking via prior work (PullNet, UniKGQA), and states the model retrieves one-depth triples. The pipeline is specified at the level of detail appropriate for a research paper.
- **"Relation extraction confound (circularity)"** — The paper runs an ablation (Section 5.3.1, Figure 4) showing that user-provided relations achieve similar performance to LLM-extracted relations, directly addressing this concern.
- **"Missing dataset description for CounterFactExtend"** — The paper explicitly states "The details about our dataset can be found in \cref{app:data}." The appendix is present in the original submission (stripped by the parser).
- **"Pure formatting/style nitpicks"** — Not present in the reviewer feedback.

## Novel Insights

The reviewer's analysis surfaces an interesting subtlety: the retrieval probability formulation ties \(P(z|q)\) to the relation \(r\) alone, not the full triple. This means the KL divergence term in the ELBO optimizes for relation-level retrieval accuracy, while object-level discrimination is pushed entirely onto the reasoning term and the algorithm's add/remove heuristic. This division of labor is actually *workable* — the system still converges to the correct personalized triple — but it reveals that the two-term ELBO decomposition does not correspond cleanly to "retrieve the right triple" and "reason with the retrieved triple" as claimed. A productive revision would acknowledge this and either reformulate \(P(z|q)\) to depend on the full triple (e.g., by having the LLM generate the verbalized triple) or explicitly characterize the retrieval objective as operating over relations, with object discrimination delegated to the reasoning component.

## Suggestions

1. **Fix the retrieval probability to incorporate the object entity.** The simplest repair: define \(P_{\theta,\mathcal{G}}(z|q)\) as the probability of generating the verbalized triple (e.g., "e_q r e'") conditioned on the retrieval instruction, rather than just the relation. This would align the KL divergence term with the actual personalization objective and resolve the disconnect between the ELBO derivation and what the loss can optimize.

2. **Correct the loss computation in Algorithm 1.** The pseudocode should define the loss over only those triples in \(\mathcal{H}\) that are currently in \(\mathcal{G}\) (or, alternatively, over all of \(\mathcal{H}\) but with the convention that \(P(z|q)=0\) terms are excluded from the sum). The break condition and iterative logic would then work as intended. This is a small change to the pseudocode with no conceptual cost.

3. **Add a retention experiment.** Measure how often previously added triples remain in the KG and continue to influence responses after processing a sequence of subsequent queries. This directly addresses the long-term personalization claim.

4. **Clarify whether baselines use the same KG-enhanced pipeline.** A single sentence stating "All baselines operate on the same KG-enhanced LLM (ConceptNet + instruction-based retrieval) as KGT" or "Baselines use the base LLM without KG enhancement" would resolve the ambiguity and strengthen the comparison.

5. **Report variance for the "no edit" baseline** for consistency, or explain why it is deterministic.

## Score and Decision

The paper presents a genuinely novel approach to LLM personalization with strong empirical support and clear efficiency advantages. However, two significant weaknesses — the gap between the ELBO-derived retrieval objective and what the formulation actually achieves, and the ill-specified loss computation in the algorithm pseudocode — prevent the paper from being accepted in its current form. Both issues are addressable in revision without changing the core methodology. The contribution is real but the presentation of the method needs substantial cleanup before the paper is publishable.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
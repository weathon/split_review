- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 5, 8
Now I have a complete picture of the paper and all the reviewer claims. Let me write the final consolidated review.

---

## Summary

ToolGen unifies tool retrieval and calling into a single generative process by representing each of 46,985 real-world APIs as a unique virtual token in the LLM's vocabulary. A three-stage training pipeline (tool memorization → retrieval training → agent tuning) on Llama-3-8B equips the model to generate tool tokens directly from user queries, eliminating the need for an external retrieval module for tool selection. Experiments show strong retrieval performance (87.67 NDCG@1 in multi-domain I1, matching or exceeding complex pipeline systems like IterFeedback) and competitive end-to-end agent results.

## Strengths

- **Unified generative retrieval convincingly eliminates the similarity-based retriever for tool selection.** Table 1 shows ToolGen achieves 91.45 NDCG@1 for I2 in-domain, outperforming the trained ToolRetriever (71.18) and matching IterFeedback (89.01) — which uses multiple models and iterative feedback — while being a single model with no external retriever. The multi-domain setting is particularly convincing: ToolGen maintains 87.67 NDCG@1 (I1) vs ToolRetriever's 72.31 over the full 47k-tool search space.

- **The ablation study cleanly isolates the contribution of each training stage.** Table 3 shows that removing retrieval training collapses NDCG@1 from 87.67 to 10.17 (I1, multi-domain), while removing memorization causes only a modest drop (87.67→84.00). This provides strong evidence that the three-stage design is well-motivated and not arbitrary.

- **Near-zero hallucination of nonexistent tools under constrained decoding is a practical advantage.** Figure 1 shows ToolGen with constrained beam search generates 0% nonexistent tool tokens, while ToolLlama and GPT-3.5 hallucinate 10–50% even with ground-truth tools in the prompt. The paper transparently attributes this to constrained decoding on the fixed tool token set — a natural consequence of the vocabulary-expansion design.

- **ToolGen operates without any external retriever in the end-to-end agent setting**, while baselines rely on ToolRetriever. Table 2 (Retriever setting) shows ToolGen achieves the highest average SoPR (53.28) and SoWR (51.51) despite this disadvantage, demonstrating that the generative approach can be more effective in the full task-completion pipeline.

- **Atomic indexing's efficiency is well-demonstrated.** Figure 3 shows atomic indexing uses exactly one token per tool versus variable-length encodings for semantic/hierarchical indexing, translating to lower latency and competitive end-to-end performance (Table 4: atomic SoPR avg 55.00 vs semantic 51.87).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The "no additional retrieval step" claim in the abstract is imprecise for the full end-to-end pipeline.** The paper states (line 107): "This token is used to fetch the tool documentation, which the LLM uses to generate the necessary arguments." While this is a simple key-value lookup (not a similarity search over 47k tools), the abstract's phrasing — "with no additional retrieval step" and "integrates tool knowledge directly into the LLM's parameters" — could be read as implying that all tool knowledge is stored in parameters. The paper should clarify that the unification applies primarily to tool *selection*; argument generation still depends on externally stored documentation fetched by token ID. This does not diminish the contribution but would improve precision.

- **The turn configuration for the end-to-end comparison is explained but the effective action opportunities are not made fully transparent.** ToolGen: 16 turns = 5 action rounds (thought+action+params sequentially) + 1 final answer round. ToolLlama: 6-turn limit. Since ToolLlama generates thought+action+params in a single round, it has either 6 action rounds or (if a final answer round is needed) 5 action rounds + 1 final. The paper does not state which. The asymmetry does *not* inflate ToolGen's results (ToolGen has 5 action rounds; ToolLlama has at least as many), but the paper should directly state the effective number of action opportunities for each model so readers can verify parity.

- **Retry mechanism details are relegated to the appendix.** The paper mentions a retry mechanism (triggered on "give up" or "I'm sorry" with higher temperature) applied to all models, but the main text lacks specifics on: maximum number of retries per trajectory, the temperature schedule, and how retries interact with turn budgets. While the mechanism is stated to be symmetric, readers cannot verify this without the appendix.

- **The number of tools (k) retrieved by ToolRetriever for baselines in the Retriever setting is not reported.** In Table 2 (R. setting), baselines receive tools from ToolRetriever, but k is never stated. If k is small, ToolGen's advantage may partly stem from exploring a larger implicit candidate set; if k is large, the context-length advantage is clearer. This should be reported.

- **Statistical significance is not reported for the main results.** Several comparisons (e.g., ToolGen SoPR 53.28 vs ToolLlama 51.55 in the Retriever setting) are close. Confidence intervals or significance tests would help distinguish systematic advantages from noise. The paper notes results are averaged over 3 runs but does not report variance.

- **Scaling to very large tool sets (millions) is not discussed.** Adding one token per tool is practical for 47k tools but would be prohibitive at web scale. The paper would benefit from a brief limitations paragraph discussing vocabulary growth and potential sparse-embedding strategies.

### Trivial

None.

## Nice-to-Haves

- An end-to-end ablation (e.g., removing retrieval training and testing only memorization+agent tuning) would strengthen the isolation of each stage's contribution for the agent task, complementing the already-thorough retrieval ablation.
- The atomic indexing initialization — "average embedding of its corresponding tool name" — could be specified more precisely (e.g., tokenization strategy for tool names, whether sub-token embeddings are averaged or summed).

## Removed Points

- **Asymmetric turns inflating ToolGen's results (Critic: structural).** Removed because it is factually unsupported by the paper. ToolGen: 16 turns = 5 action rounds + 1 final. ToolLlama: 6-turn limit. Since ToolLlama generates thought+action+params per round, it has at least as many (likely 6) action rounds as ToolGen's 5. Any asymmetry favors ToolLlama, not ToolGen. The critic's claim that this "inflates ToolGen's task-completion rate" directly contradicts the paper's stated design. (A reasonable concern about *clarifying* the effective action parity is kept as a minor weakness above.)

- **Hallucination comparison is "unfair" because constrained decoding could be applied to any model.** Removed. The paper transparently attributes the zero hallucination to constrained decoding. The key insight is that ToolGen's vocabulary expansion provides a *fixed, known set of tool tokens to constrain to*, which is a genuine advantage — other models output free-form text for tool names, making constrained decoding harder to apply. The paper does not claim the zero hallucination is inherent to training; it explicitly states it is "due to its design" (constrained decoding, line 325).

- **Missing end-to-end ablation.** Moved to Nice-to-Haves. The retrieval ablation (Table 3) is already thorough, and asking for an end-to-end ablation is a strengthening suggestion, not a weakness.

- **Underspecified atomic indexing initialization.** Moved to Nice-to-Haves. Minor reproducibility point that does not affect the paper's validity.

## Novel Insights

The harsh critic's observation that the retry mechanism plus asymmetric turn budgets could interact in subtle ways is a valid methodological concern, but the paper states the mechanism is symmetric and the turn asymmetry favors ToolLlama (more action rounds), not ToolGen. The more useful insight from reading both the paper and reviews is that the paper's two contributions — (a) eliminating the similarity-based retriever for tool selection and (b) the overall end-to-end agent performance — are of different evidentiary strength. The retrieval evidence (Table 1, Table 3, multi-domain setting) is clean and convincing. The end-to-end evidence (Table 2) is real but modest in magnitude and uses a protocol that, while not unfairly biased toward ToolGen, is underspecified in ways (k value, retry details, effective action parity) that should be tightened. None beyond the paper's own contributions.

## Suggestions

1. **Clarify the "no retrieval" claim:** Replace "requires no additional retrieval step" with a precise statement like "eliminates the similarity-based retrieval step for tool selection; argument generation uses a token-ID-based lookup of tool documentation."
2. **Report effective action parity:** State explicitly how many action rounds ToolLlama gets (5 or 6) and confirm parity with ToolGen's 5 action rounds.
3. **Disclose retry parameters in the main text:** Include the max retries, temperature schedule, and how retries count toward turn limits.
4. **Report k for ToolRetriever in the R. setting.**
5. **Add confidence intervals or standard deviations** for the three evaluation runs in Table 2.
6. **Add a brief limitations paragraph** discussing vocabulary growth for larger tool sets.

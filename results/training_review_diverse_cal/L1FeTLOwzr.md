I now have a comprehensive understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces DAM (Dynamic Adapter Merging) for rehearsal-free domain-incremental video question-answering (VidQA) learning. The method combines continually-trained domain-specific adapters inserted into a frozen video-language backbone (FrozenBiLM, 1.2B params), a non-parametric router that computes domain-relevance probabilities via cosine similarity to frozen-backbone centroids, and dynamic weighted merging of the top-k adapters per test instance. The paper claims a 9.1% average accuracy improvement over the best prompt-based baseline (S-Prompts) with 1.9% less forgetting across six VidQA datasets, and extends the approach to image-based VQA with BLIP-2.

## Strengths

1. **First systematic exploration of rehearsal-free domain-incremental VidQA on large-scale models.** The paper identifies and formalizes an underexplored problem setting that goes beyond image classification DIL, and grounds it in the practical challenges of video-language model deployment (domain shift, data imbalance, temporal gaps). This is clearly stated as a first contribution in Section 1 and supported by the related work survey in Section 2.

2. **Clean, modular method with practical benefits.** DAM's design — frozen backbone + lightweight domain-specific adapters (<5% of total parameters) + non-parametric router + dynamic merging — is conceptually simple and parameter-efficient. The non-parametric router avoids the optimization stability issues of end-to-end trained routers (CODA-Prompt), as shown in Table 2 and discussed in Section 4.3.

3. **Insightful analysis of when merging helps.** Section 4.4 and the associated Table 3 provide useful evidence that dynamic adapter merging yields larger gains precisely when router accuracy is low (e.g., 4.9% improvement on MSVD where router accuracy is 51.0%; up to 30% relative improvement when router accuracy drops to 0% in the controlled study of Figure 4). This analysis goes beyond "our method works" and gives the community actionable understanding of the technique's behavior.

4. **Generality demonstrated via VQA extension.** Section 4.5 extends DAM to image-based VQA using BLIP-2 (4.1B parameters), showing that DAM outperforms S-Prompts by 4.4% with 1.2% less forgetting. This demonstrates the method's applicability beyond video.

5. **Scalability analysis across varying numbers of domains.** Figure 3 shows that DAM consistently outperforms S-Prompts on both in-distribution and out-of-distribution domains as the number of trained domains increases from 2 to 6, with normalized accuracy advantages ranging from 1.7% to 7.1%.

## Weaknesses

### Fatal

None established with full certainty from the text, but see the first Major point below — if confirmed, it would be fatal.

### Major

1. **Unexplained internal inconsistency between Table 1 and Table 3.** The harsh critic identifies a discrepancy: DAM (stated to use k=2 merging) reportedly achieves ~59.0% average accuracy in Table 1, while Table 3's "Top-2 Adapter" row — which should reflect the exact same method — is claimed to average ~47.65% based on per-dataset values read from the table image. The paper's text does not acknowledge any difference in experimental conditions between these tables, and an 11+ point gap is far too large to be explained by random seed variation (Table 1 already averages 5 runs). **If this discrepancy is real, it invalidates the paper's core empirical claims** — including the headline 9.1% improvement over S-Prompts. The authors must clarify the exact experimental conditions for each table, provide per-dataset accuracy from the same run in a consistent format, or explain the source of the discrepancy. *Note: I cannot fully verify the specific numeric values since they are contained in table images rather than the text, but the critic's reading is internally plausible and, if accurate, the inconsistency is fatal.*

2. **Headline comparison conflates adapter benefit with dynamic merging benefit.** DAM uses adapter tuning, while the primary baselines (L2P, CODA-Prompt, S-Prompts) use prompt tuning. The Ind-FT "upper bound" results in Table 1 reportedly show that even individually fine-tuned adapters (Ind-FT Adapter, ~62.1% average) substantially outperform individually fine-tuned prompts (Ind-FT Prompt, ~55.1% average) in the non-continual setting. This means a significant portion of the claimed 9.1% advantage may stem from the inherent superiority of adapters over prompts for this backbone, not from dynamic merging itself. The paper does include regularization-based baselines (EwC, LwF) that use the same adapter architecture and shows DAM beats them — this provides some evidence for the merging scheme — but the title and abstract emphasize the prompt-based comparison. An adapter-based router-only baseline (i.e., Table 3's Top-1 row) that isolates the value of merging from the value of the adapter choice is available in Table 3 but is not centered in the main narrative. The paper should either frame the comparison more precisely or provide an explicit adapter-based router-only baseline in Table 1.

3. **No standard deviations or confidence intervals reported.** Table 1 states results are "averaged from 5 runs with different random seeds" but reports only point estimates. Given the unexplained discrepancy between Table 1 and Table 3, the absence of variance reporting is especially problematic — the reader cannot assess the statistical significance of the claimed 9.1% improvement. Standards deviations are standard practice in continual learning evaluations and should be provided.

### Minor

1. **Critical architectural hyperparameter (N, number of adapters per domain) is never specified.** Section 3.1 states "for each domain s, we first inject N domain-specific adapters" but N is never given a value or even mentioned in the experimental setup (Section 4). This parameter affects parameter count and potentially merging behavior.

2. **Only one dataset ordering is tested.** Table 1 shows the order iVQA → MSVD → MSRVTT → LSMDC → ActivityNet → TGIF. Continual learning results can be sensitive to domain order. Testing at least one alternative ordering (random or reversed) would strengthen the claims of robustness.

3. **Continual initialization scheme is not ablated.** The paper asserts that initializing each new domain's adapters with the weights of the previously trained adapter "leads to a smoother parameter space" and benefits merging (Section 3.1), but no experiment isolates the effect of this design choice. Without ablation, it is unclear how much of the reported performance relies on this initialization.

4. **Novelty claim could be more precisely scoped.** The paper claims to be "the first to explore domain-incremental VidQA learning" (Section 1). Prior works (VQACL, CLCrossVQA) address VidQA DIL with rehearsal. Adding "rehearsal-free" to the novelty claim would avoid potential overclaiming, though the paper's focus is clearly distinct from those works.

### Trivial

- None significant enough to list separately.

## Nice-to-Haves

- An analysis of whether the router's predictions (computed from frozen backbone features) remain stable when features are extracted after adapter application. This would address the conceptual concern about potential misalignment between router probabilities and actual adapter suitability.
- Testing with more advanced merging methods beyond simple weighted averaging (acknowledged as a limitation by the authors in Section 5).
- Domain-order sensitivity analysis.

## Removed Points

- **"Router features will be modified by merged adapters causing misalignment"** — This specific formulation is inaccurate. The router explicitly uses features from the frozen backbone *f* (Section 3.2), not from the adapted model. The adapters are applied for final prediction but do not change what features the router "sees." The deeper conceptual point (whether frozen-backbone features adequately predict adapter relevance) is a valid discussion point but belongs in Nice-to-Haves, not as a confirmed weakness.
- **Reproducibility nitpicks** (hyperparameter details, complete training logs) — These are standard omissions in conference submissions.
- **"The paper should cover more domains/tasks"** — The paper explicitly scopes its evaluation to 6 domains, consistent with prior DIL work, and extending to 100 domains is noted as future work (Section 5). This is not a weakness of the current paper.
- **Claims about missing appendix content or proofs** — The parser strips these; they exist in the original submission.
- **Formatting/style criticisms** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no observation that the paper's own analysis (router-accuracy-dependence of merging gains, Section 4.4) does not already provide.

## Suggestions

1. **Resolve the Table 1 vs Table 3 inconsistency immediately.** Clarify whether these tables use different experimental protocols. If the numbers are correct, explain the source of the discrepancy (different checkpoints? different evaluation conditions?). Provide per-dataset accuracy for DAM in a single consistent format with standard deviations.

2. **Restructure the main comparison to isolate the merging contribution.** Add an adapter-based baseline with the same router but no merging (Top-1 selection) to Table 1. Reframe the paper's contribution around the *incremental* gain of dynamic merging over router-only adapter selection, rather than the system-level comparison against prompt-based methods. The analysis in Section 4.4 is the paper's strongest contribution and should be featured more prominently.

3. **Report standard deviations** for all main results (Tables 1, 3, 4). This is essential given the questions about numerical consistency.

4. **Specify N** (number of adapters per domain) and test at least one alternative domain ordering to demonstrate robustness.

## Score and Decision

This paper tackles a valuable and underexplored problem, proposes a clean method, and provides insightful analysis about when dynamic merging helps. However, the potential internal inconsistency between Table 1 and Table 3 is a serious concern that cannot be resolved without author clarification. If the numbers are confirmed to be accurate but the inconsistency is real, the paper's central empirical claims are unsupported. If there is a benign explanation (different experimental protocols that the paper failed to document), the remaining weaknesses (conflated comparison, missing variance, missing hyperparameter) are addressable in a revision. In its current form, the paper cannot be accepted without resolving this issue.

**Score:** The paper has genuine conceptual merit and useful analysis, but the empirical foundation is uncertain. The contribution is likely real but the reporting is not reliable enough in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>
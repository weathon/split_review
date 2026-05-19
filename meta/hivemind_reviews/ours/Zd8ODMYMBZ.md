## Summary
This paper proposes FaviComp, a training-free evidence compression method for RAG that uses ensemble decoding between a compression model (which summarizes retrieved documents) and the target model (which generates context from its parametric knowledge). By combining token logits from both models during compression, FaviComp generates compressed evidence that has lower perplexity for the target model (making it "familiar") while naturally integrating the target model's parametric knowledge. Experiments on five open-domain QA datasets show consistent improvements over existing compression baselines. The analysis includes a thoughtful decomposition via the Hits metric (evidence-relevant vs. evidence-irrelevant subsets) that directly validates the claimed mechanism.

## Strengths
- **Consistent gains across multiple datasets and target models**: FaviComp outperforms recent evidence compression baselines (RECOMP, CompAct, LongLLMLingua, etc.) on five open-domain QA datasets using three different target models (Llama3-8B, Mistral-7B, Mixtral-8x7B), with accuracy improvements up to 23.91% (Section 4.1, Tables 1/3). The consistency across models and datasets makes the result robust despite single-run evaluation.

- **Training-free and model-agnostic**: The method requires no training (no distillation, no supervised data, no reinforcement learning) and can be plugged into any RAG pipeline, unlike RECOMP-abstractive and CompAct which require expensive distillation procedures (Abstract, Sections 1, 7).

- **Direct mechanistic evidence via the α ablation**: By sweeping the ensemble coefficient α across seven values and measuring both perplexity and downstream accuracy (Section 4.2, Figure 2), the paper shows that performance peaks at α=0.5 — exactly where the compressed evidence's perplexity for the target model is lowest. This creates a causal chain: ensemble decoding → lower target-model perplexity → higher accuracy. Performance declines symmetrically when α deviates from 0.5, and the explanation (insufficient evidential knowledge at high α, insufficient familiarization at low α) is coherent and supported.

- **Hits-subset analysis cleanly demonstrates parametric knowledge integration**: On the Hits=0 subset (retrieved evidence lacks the answer), FaviComp significantly outperforms both Zero-shot Summarization and CompAct, while maintaining comparable performance on Hits=1 (Section 4.3, Figure 3). This directly validates the claim that FaviComp leverages the target model's parametric knowledge when retrieved evidence is insufficient, and does not sacrifice performance when evidence is adequate.

- **Higher compression rate than equivalently instructed zero-shot summarization**: FaviComp consistently achieves higher compression rates than Zero-shot Summarization (which is FaviComp with α=0), showing that ensemble decoding produces more concise yet effective summaries (Section 4.4). This is a concrete side-benefit.

## Weaknesses
### Fatal

None.

### Major

None.

### Minor

- **No variance or statistical significance reporting for main results**: The paper reports point estimates of accuracy (Tab. 1, Tab. 3) without error bars, standard deviations, or significance tests. While single-run evaluation on standard QA benchmarks is common practice in this subfield, the headline claim of "up to 23.91% improvement" would be much stronger with variance estimates, especially given that multi-document QA can have high variance from retrieval noise. The paper should report at minimum mean and std. dev. over multiple retrieval seeds or significance tests (e.g., bootstrap or paired tests) against the strongest baseline.

- **Computational cost of ensemble decoding is not discussed**: FaviComp requires two forward passes per token during compression (one from the compression model, one from the target model), which doubles the decoding cost of the compression stage compared to methods like Zero-shot Summarization or RECOMP (which only need a single forward pass). The paper acknowledges the method is "training-free" but does not quantify the inference-time overhead or discuss whether the accuracy gains justify the additional computational cost relative to training-based compressors that only need a single pass at inference time. A brief wall-clock time or FLOPs comparison would help practitioners assess the trade-off.

- **Compression rate vs. accuracy trade-off is not explicitly visualized**: The paper reports compression rates and accuracy separately (Section 4.4, Tab. 1) but does not provide a scatter plot or direct analysis of the accuracy-compression Pareto frontier across methods. This would be informative since different applications have different tolerance for compression-induced information loss. The current discussion is qualitative ("reranking...information loss is more significant") rather than quantitative.

### Trivial

- The extracted text shows that Section 2.3 (detailed method definition) is missing and that the prompt template referenced at line 52 is incomplete — these are extraction artifacts, but in the original submission, ensuring the ensemble equation (additive logits vs. interpolated probabilities) and the precise role of α are stated clearly would aid reproducibility.

## Suggestions
1. **Report variance**: Add standard deviations over at least 3 retrieval seeds (or bootstrapped confidence intervals) to the main results in Table 1. Include pairwise significance tests (e.g., McNemar's test or bootstrap) between FaviComp and the strongest baseline per dataset.

2. **Quantify computational cost**: Report average compression latency, inference FLOPs per query, or wall-clock time for FaviComp vs. key baselines. This is important because the method's practical utility depends on the accuracy-efficiency trade-off.

3. **Add a scatter plot of accuracy vs. compression rate**: A simple 2D plot with one point per method per dataset would visualize whether FaviComp dominates baselines on both axes or trades off one for the other.

4. **Include the controlled comparison suggested in Nice-to-Haves**: Compare against "perplexity-filtered Zero-shot Summarization" (generate k summaries, pick the one with lowest target-model perplexity) to separate the value of token-level ensemble from general perplexity reduction.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept

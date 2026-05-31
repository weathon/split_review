## Summary

This paper presents a zero-shot evaluation of 31 open-weight large language models (LLMs) on two five-class sentiment polarity benchmarks (SemEval-2017 Task 4C and SST-5). The authors measure accuracy, macro-average mean absolute error, and inference throughput (instances per second), and identify Pareto-optimal models that balance performance and cost. They claim that several open-weight LLMs outperform previous state-of-the-art results on SemEval and approach state-of-the-art on SST-5.

## Strengths

- **Comprehensive model coverage**: The evaluation spans 31 models from diverse families (Llama, Gemma, Qwen, Mistral, Phi, etc.) across a wide range of parameter scales (2B–32B), including dense and MoE architectures. This provides a useful snapshot of the current open-weight LLM landscape for sentiment analysis.
- **Appropriate ordinal metric**: The use of macro-average mean absolute error (MAE) is well-motivated for the 5-class ordinal task, as it penalizes severe misclassifications more than near misses and treats all classes equally despite dataset imbalance.
- **Pareto frontier analysis**: The paper explicitly considers the trade-off between accuracy and inference speed, identifying models that are not dominated on both dimensions. This is practically valuable for deployment decisions.

## Weaknesses

### Fatal

- **Unconvincing state-of-the-art comparison**: The paper claims to "outperform previous state-of-the-art results" on SemEval, but the baselines used are weak and outdated. For accuracy, they compare against a single unpublished BERT-based method (Das & Pedersen, 2024) that achieves 0.542. For macro-MAE, they compare against the original SemEval-2017 organizer baseline (0.481). No comparison is made to more recent fine-tuned models (e.g., RoBERTa, DeBERTa, fine-tuned LLMs) or to other published results on these benchmarks. Given that SemEval-2017 Task 4C is a well-studied dataset, it is highly likely that stronger baselines exist, making the claimed "new state-of-the-art" unsupported. This undermines the paper's central contribution.

### Major

- **Limited novelty**: The paper is essentially a benchmark of existing open-weight LLMs on two standard datasets. It does not introduce a new method, dataset, or theoretical insight. The finding that some LLMs outperform older fine-tuned BERT models is not surprising given the rapid progress in LLMs. The Pareto analysis is a useful addition but does not constitute a significant methodological contribution.
- **Inference speed metric is not standardized**: Instances per second is reported on a single GPU (RTX A5500) without controlling for batch size, quantization, or other inference optimizations. The results are therefore hardware-specific and not easily generalizable. The paper does not discuss whether models were run with the same batch size or other settings that affect throughput.
- **No error analysis or qualitative insights**: The paper reports aggregate metrics but provides no analysis of where models succeed or fail (e.g., which sentiment classes are hardest, how models handle negation or sarcasm, or why certain models perform better). This limits the depth of understanding beyond raw numbers.

### Minor

- **Prompt sensitivity not explored**: The zero-shot prompts are fixed. Different prompt formulations could significantly affect results, but no ablation or sensitivity analysis is provided.
- **Discarded instances**: The paper discards instances where the model outputs multiple integers or no integer. While the skip rate is low for top models, this could introduce bias, especially for smaller or less capable models.

### Trivial

- The paper states that "phi4-reasoning.14b" exceeded the time limit, but the model name is inconsistently formatted (sometimes "phi4-reasoning_14b").

## Nice-to-Haves

- Compare against a broader set of baselines, including fine-tuned LLMs and more recent specialized models.
- Include confidence intervals or statistical significance tests for the performance differences.
- Analyze the relationship between model size, architecture (e.g., attention mechanism), and performance on specific sentiment classes.

## Novel Insights

None beyond the paper's own contributions. The observation that some open-weight LLMs can outperform older fine-tuned models on SemEval is empirically documented but not surprising given the known capabilities of modern LLMs. The Pareto frontier analysis provides a practical guide but does not reveal unexpected trade-offs.

## Suggestions

- Substantially strengthen the state-of-the-art comparison by surveying recent literature on SemEval-2017 Task 4C and SST-5, including fine-tuned transformer models and LLM-based approaches. If the claimed SOTA is not supported, reframe the contribution as a systematic benchmark rather than a SOTA claim.
- Add an error analysis section to understand model behavior (e.g., confusion matrices, per-class performance, qualitative examples of successes and failures).
- Control for inference speed more carefully (e.g., fixed batch size, report latency per instance rather than throughput, or use a standardized benchmark like the LLM Perf Leaderboard).

## Score and Decision

**Score**: 4.0  
**Decision**: Reject

The paper has merit as a comprehensive benchmark, but the core claim of outperforming state-of-the-art is not convincingly supported due to weak baselines. The lack of novelty and limited depth of analysis further reduce its impact for a top venue like ICLR.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>
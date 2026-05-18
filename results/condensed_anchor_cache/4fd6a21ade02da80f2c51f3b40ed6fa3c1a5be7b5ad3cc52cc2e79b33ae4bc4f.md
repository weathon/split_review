- Decision: Accept
- Scores: 6, 6, 6

## Merged Review

### Summary
The paper proposes a synthetic dataset based on numerical key-value retrieval tasks and uses it to fine-tune Mistral 7B and GPT-3.5 Turbo to improve long-context information retrieval and reasoning. Fine-tuning on this dataset improves performance on MDQA and FLenQA while discouraging hallucinations. Performance on general benchmarks (MMLU, HellaSwag, GSM8K, TriviaQA, NQ-open) is largely retained, unlike baseline long-context augmentation datasets which can cause degradation.

### Strengths
- The proposed method is simple, straightforward, and effective.
- The problem addressed (improving LLM retrieval in long contexts) is meaningful and important.
- Fine-tuning on randomly sampled key-value datasets fixes the “lost-in-the-middle” phenomenon for GPT-3.5 while retaining original knowledge. The observation that finetuning with **answer templates** performs better is a useful detail.
- The synthetic dataset contains no factual information, an interesting advantage.
- The approach does not degrade performance on general evaluation benchmarks (e.g., on TriviaQA, Mistral 7B finetuned on the synthetic data causes no performance drop, while other baseline data cause drops from 2.33% to 6.19%).
- The experiments are comprehensive and effectively support the main points.
- The paper is well written and easy to follow.
- Work on improving LLMs through synthetic datasets is crucial for the community.

### Weaknesses
- **Scope of retrieval-only tasks:** The synthetic dataset targets only retrieval tasks (like MDQA), while other long-context applications (in-context learning, RAG) require *understanding* the context as a whole. Concurrent works [1,2] argue that improving only retrieval capabilities does not capture all long-context applications. Doubts about the scope of applications.
- **Claim of primacy bias mitigation not fully supported:** The claim in line 263 that “proposed data mitigates this primacy bias” is not fully supported by Fig 5(b), which still shows a descent and decreasing accuracy for middle positions. The model still exhibits some degree of primacy bias.
- **Unclear isolation of factors in MDQA comparison:** The difference between finetuning on the proposed dataset vs. MDQA arises from two factors: (a) randomization of the gold document position, and (b) complexity of English understanding. The authors should isolate these, e.g., by adding a `<Mistral-7B ft with MDQA>` row in Table 1.
- **Missing ablation for multi-key retrieval:** In Section 3.4, a possible reason MultiDocQA and IN2 outperform the proposed dataset is that those baselines require extracting information from multiple contexts. The reviewer suggests adding a task that retrieves the values of multiple keys to better capture multi-document complexity and to counteract hallucinations that MultiDocQA and IN2 seem to induce.
- **Lack of evaluation at longer context lengths:** Fine-tuning and evaluation are fixed within one sliding window (line 214). Since some works extend Mistral’s context to 32k, evaluation at longer contexts is needed. Section 3.5 takes steps, but quality evaluations still need to be included.
- **Missing comparison with positional embedding extensions:** Manipulation of positional embeddings to extend context without training is orthogonal, but works [3,4] improve Mistral’s context length while maintaining retrieval performance. Either an explanation in related work or a direct comparison is needed.
- **Inconsistent training epochs (Stage 1):** Why fine-tune Mistral 7B for 2 epochs but GPT-3.5 Turbo for 3 epochs? Is performance sensitive to the number of epochs?
- **Need for early stopping and larger dataset effects:** Does Stage 1 need early stopping? Would longer training hurt general benchmarks? Would a larger key-value dataset further improve long-context retrieval/reasoning or hurt general performance?
- **Potential benefit of multi-subkey retrieval:** Would performance further improve if also fine-tuning Mistral 7B with a multi-subkey dictionary key-value dataset? (Overlaps with multi-key point above.)
- **MDQA baseline training details unclear:** When fine-tuning with MDQA as a baseline, does the training use 20 documents with a gold document placed in some positions? If so, that may be too few samples.
- **Missing FLENQA baseline results for MDQA-finetuned model:** The paper presents fine-tuning with MDQA as a baseline in Section 3.2.1 but does not provide similar results for FLENQA in Section 3.2.2. Would conclusions remain consistent?
- **Token count mismatch for baselines in Stage 4:** How many tokens were used for training the other baselines (MultiDocQA, IN2) in Stage 4? The baselines show good performance on long-context retrieval/reasoning (especially FlenQA(cot)) and acceptable results on some general benchmarks, making it difficult to definitively claim the proposed method beats them.
- **Missing details in synthetic data generation:** Critical details on how the key-value retrieval task is generated are missing. For example, why are values 3 or 4 digits? (4 digits = 2 tokens in GPT tokenizer, 3 digits = 1 token.)
- **Limited evaluation benchmarks and backbones:** More extensive experiments are needed. Recommend evaluation on RULER [1] and LongBench [2] with different backbones such as Llama and Gemma.
- **Minor suggestion for Table 2:** Include average accuracy/gap across all datasets to clarify overall average degradation.
- **Questions that serve as missing ablations:**  
  - Could GSM8K be considered a reasoning task? TriviaQA as retrieval and reasoning? Why can’t those datasets improve performance?  
  - Was Mistral full fine-tuned or with parameter-efficient fine-tuning (e.g., LoRA)?  
  - What is the rationale for choosing the number of samples in key-value retrieval tasks?  
  - In Fig 5(b) Mistral-v0.1 is used, while in Fig 7(b) Mistral-v0.2 is used. Is there a reason for using different versions?
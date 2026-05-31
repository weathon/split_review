## Human Reviewer 1

### Summary
The paper proposes a pruning criterion for large language models based on the information entropy of the model’s output distribution. Instead of using one-hot cross-entropy (which focuses on the single next token) or relying on a separate teacher for self-distillation, the method computes per-layer entropy-based importance scores within a Taylor-style framework and prunes parameters to better preserve the model’s global output distribution. The approach is label-free, aims to maintain fidelity after pruning, and is evaluated on zero-shot benchmarks for LLaMA and Qwen-family models.

### Strengths
The authors propose a relatively simple yet reasonable approach for pruning large language models (LLMs), which uses the entropy of output distributions as an indicator of neuron importance, instead of relying solely on next-token cross-entropy. The method does not depend on additional teacher models or complex distillation procedures, making it practically appealing for real-world pruning applications. The experiments cover multiple model families (e.g., LLaMA, Qwen) and several zero-shot benchmarks, showing that the proposed approach consistently outperforms existing pruning baselines. This provides some evidence of general applicability and reliability.

### Weaknesses
1. The dataset coverage is narrow and the evaluation tasks are of low difficulty, relying on a small set of relatively simple zero-shot benchmarks. This makes it difficult to assess robustness in areas such as instruction following, multi-step reasoning, long-context understanding, or multilingual and multi-domain settings.
2. There may be a mismatch between the benchmarks and the pruned model components: if the tasks do not sufficiently engage the pruned submodules, the reported “distribution fidelity” may be overstated and external validity remains uncertain.
3. Baseline and tuning transparency is limited, with missing comparisons to stronger or more recent pruning baselines, as well as a lack of systematic hyperparameter exploration under fair alignment conditions (e.g., matched training steps and learning-rate sweeps).
4. The evaluation metrics are limited, focusing heavily on perplexity or simple zero-shot accuracy, without including direct generation results.

### Questions
1. The evaluation datasets are insufficient — they’re all too simple. The pruned parameters might not cover the activation patterns of these models, so more diverse datasets should be added.
2. In addition, the model sizes don’t seem sufficient either, for example models like Qwen3-8B.
3. For reasoning models, does the entropy criterion remain reliable?
4. The main contribution is the use of entropy for pruning, which feels rather limited.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces HFPrune (High-Fidelity Pruning), a structured pruning method for LLMs that aims to preserve model fidelity while reducing computational and memory costs, replacing the conventional loss-based Taylor pruning criterion with an information entropy–based criterion that measures the global prediction distribution of the model, instead of focusing only on the ground-truth token.

### Strengths
- Provides a label-free, holistic signal for neuron importance estimation. 
- HFPrune consistently outperforms strong baselines: LLM-Pruner, LoRAPrune, SDMPrune, on LLaMA and Qwen families.
- Comprehensive ablation studies validate the entropy criterion’s role in preserving output distributions. 
- The algorithmic description is clear and reproducible. Implementation details are systematically reported.

### Weaknesses
- The pruning ratio $\rho{mlp}$  is fixed across all MLP layers, despite entropy potentially varying per layer, this could limit the functionality of HFPrune.
- Lack a comparative discussion or empirical correlation analysis between entropy-based and Fisher-based importance scores.
- Training-time FLOPs for fine-tuning (post-pruning recovery) are omitted.

### Questions
- Can a per-layer entropy-based adaptive cutting ratio improve the trade-off between fidelity and compression?
- How does the entropy gradient behave in the low entropy versus high entropy regions of the output distribution?
- What are the effects of using entropy calculated from logits vs. softmax probabilities?

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
2

---

## Human Reviewer 3

### Summary
This paper proposes HFPrune, a structured pruning method for LLMs that replaces traditional one-hot cross-entropy with information entropy as the criterion for Taylor-based neuron importance evaluation. The authors argue that entropy-based evaluation considers the full output distribution rather than just the ground-truth token, leading to better preservation of model capabilities. The method focuses on pruning MLP modules and demonstrates consistent improvements over existing methods across LLaMA and Qwen models on zero-shot benchmarks.

### Strengths
The method avoids computational overhead of teacher models and resolves gradient initialization issues in self-distillation approaches, showing 3x speedup over SDMPrune with 31% less memory usage.

Demonstrates improvements across multiple model families (LLaMA, Qwen) and sparsity levels, with some configurations even exceeding dense model performance after fine-tuning.

The approach is straightforward to implement, requiring only standard forward-backward passes without custom kernels or auxiliary models.

### Weaknesses
The paper fundamentally lacks theoretical justification for why entropy-based importance should preserve model performance. This is not a minor omission, in my view it's a central issue that undermines the contribution's scientific rigor.

**Limited Evaluation Scope**: 
- Exclusively focuses on zero-shot QA/classification tasks
- No evaluation on reasoning, long-form generation, or conversational capabilities  
- Largest model tested is only 7B parameters
- Limited architectural diversity beyond LLaMA/Qwen families

**Methodological Limitations**:
- Uses uniform pruning ratios across layers, ignoring heterogeneous sensitivity
- Limited sparsity range testing (only 20-30%)
- The performance gains over dense models likely result from fine-tuning rather than pruning itself

**Insufficient Analysis**: 
- No explanation of which types of neurons are pruned and why (recent works have revealed super neurons, super weights, super experts etc.)
- No investigation of the relationship between entropy reduction and specific capabilities
- Missing analysis of method sensitivity to calibration data selection

**Questionable Claims**: The assertion that the method "minimizes the change of global prediction distribution" is not rigorously nor theoretically established, and the connection between this and performance preservation remains speculative.

### Questions
1. Can you provide rigorous mathematical analysis of why minimizing entropy change should preserve model capabilities better than minimizing cross-entropy change?
2. What is the information-theoretic justification for treating high-entropy neurons as more important?
3. How does your approach relate to existing theories of neural network capacity and information flow?
4. How does the method perform on reasoning tasks (GSM8K, BBH), long-context generation, and conversational AI beyond zero-shot classification?
5. Can you evaluate on larger models (70B+) and more diverse architectures to support generalizability claims?
6. What explains the performance improvements over dense models - is this due to fine-tuning effects rather than pruning benefits?
7. Why use uniform pruning ratios instead of layer-sensitive approaches?
8. How sensitive is the method to calibration data selection and size?
9. How does the method perform under more aggressive pruning (40-70% sparsity)?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper proposes HFPrune, a novel method for compressing LLMs through pruning of the MLP modules within transformer architectures. HFPrune introduces an information entropy-based criterion for evaluating neuron importance, offering a more holistic approach than traditional methods, which rely on one-hot cross-entropy loss. This entropy-based method minimizes the global prediction distribution change, effectively preserving model performance.  Extensive experiments on LLaMA and Qwen models demonstrate the effectiveness and efficiency.

### Strengths
The proposed idea is simple, straightforward, and aligns well with intuition. From the engineering perspective, it is also very easy to implement.

Extensive experiments were conducted on multiple LLM models, across diverse benchmarks, comparing the proposed method with several previous methods. The results demonstrate significant improvements in both performance and efficiency of the proposed method.

### Weaknesses
**Explanation on the Choice of Baselines**: As discussed in the Related Work section, LLM pruning is a highly focused research area with a large body of work, which can be categorized into different approaches. However, in the experimental section, only a few methods such as LLM-pruner, LoRAPrune, and LoRAP are compared, and the rationale behind choosing these baselines is not explained. It remains unclear whether the state-of-the-art methods from each category are all covered by the baselines used in this paper. If they are, an explanation should be provided; if not, more baselines should be included (or a justification should be given for why they cannot be included for a fair comparison).

**More Comparison on Efficiency**:  For Efficiency, the paper only compares the proposed method with SDMPrune, demonstrating that the proposed approach is more efficient than methods like SDMPrune, which require a teacher model. The efficiency of other methods (LLM-pruner, LoRAPrune, LoRAP) should also be compared.

**Writing Needs Improvement**:
- For example, in lines 013-014 of the Abstract: The statement "A common approach uses Taylor Expansion" does not clearly explain the field of research. It should at least mention that "it is a common approach for LLM pruning."
- In line 015 of the Abstract, the sentence "However, its reliance on one-hot cross entropy loss, ..." contains a grammatical error. It should be "it relies on" instead.
- Many more problems on writing exists

### Questions
**Regarding whether "focus on pruning MLP" is the contribution of this paper**: In lines 039-043, when explaining why the paper focuses on pruning MLP, the authors use phrases like "We find that" and "we observe that" (and then prove this in Section 5.3.3 with experiments), but these statements are also referencing previous works. Is this an innovative contribution of the paper, or is it the findings from previous works?

**considering a subset of tokens**：Between the extremes of "only consider the ground-truth label token" and "consider all possible tokens", an intermediate approach could be: only considering a subset of tokens (for example, the top K tokens with the highest probability) when evaluating neuron importance. Did the authors experiment with this approach? Experiments or discussions on this would make the paper more insightful.

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
4

### Confidence
5
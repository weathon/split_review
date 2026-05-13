# Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) have achieved remarkable success in vision understanding, reasoning, and interaction.
    However, the inference computation and memory increase progressively with the generation of output tokens during decoding, directly affecting the efficacy of MLLMs.
    Existing methods attempt to reduce the vision context redundancy to achieve efficient MLLMs. %
    Unfortunately, the efficiency benefits of the vision context reduction in the prefill stage gradually diminish during the decoding stage.
    To address this problem, we proposed a dynamic vision-language context sparsification framework \textbf{Dynamic-LLaVA}, which dynamically reduces the redundancy of vision context in the prefill stage and decreases the memory and computation overhead of the generated language context during decoding.
    Dynamic-LLaVA designs a tailored sparsification inference scheme for different inference modes, \textit{i.e.}, prefill, decoding with and without KV cache, to achieve efficient inference of MLLMs.
    In practice, Dynamic-LLaVA can reduce computation consumption by \textbf{$\sim$75\%} in the prefill stage.
    Meanwhile, throughout the entire generation process of MLLMs, Dynamic-LLaVA reduces the \textbf{$\sim$50\%} computation consumption under decoding without KV cache, while saving \textbf{$\sim$50\%} GPU memory overhead when decoding with KV cache, due to the vision-language context sparsification.
    Extensive experiments also demonstrate that Dynamic-LLaVA achieves efficient inference for MLLMs with negligible understanding and generation ability degradation or even performance gains compared to the full-context inference baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors propose Dynamic-LLaVA, a novel approach to enhance both prefilling and generation efficiency in Multimodal Large Language Models (MLLMs). The modified model employs two predictors: an image predictor that dynamically identifies and drops less significant image tokens during prefilling, and an output predictor that filters out non-essential output text tokens. When training these two predictors, the authors propose an end-to-end sparsification training pipeline, which added a mask to the original softmax attention to keep a fixed number of image tokens and generated text tokens. Additionally, the argmax is replaced by Gumbel-Softmax during backward to avoid the gradient flow problem. Extensive experiments show the effectiveness and efficiency of the proposed method.

### Strengths
1. This work pioneers the reduction of KV cache length during long text generation for MLLMs, whereas previous research has focused solely on reducing prefilled vision tokens.
2. The end-to-end sparsification training can be viewed as a novel way to enhance the token sparsity of MLLMs.
3. The paper proposed extensive experiments to show the effectiveness of the proposed method.

### Weaknesses
1. While Dynamic-LLaVA demonstrates improvements over previous approaches like FastV and PruMerge+, it requires additional post-training, which introduces extra computational overhead. In table 3, it seems that the performance of Dynmaic-LLaVA and FastV are even comparable. Therefore, for real-world deployments where computational efficiency is crucial, implementing existing methods may be more practical. However, this raises an important question: the work would benefit from a clearer justification for why a trainable approach is necessary and what specific advantages it offers over more lightweight solutions. 

2. For the output reduction, as we only need to determine whether preserving the current generated token, this pipeline is the same as some work for LLM, such as StreamingLLM [1], H2O [2]. However, the author only compare the Random and Structure strategies. Therefore, I think this is a well-defined problem for LLMs, and the current experimental results cannot convince me. 

3. The methodology section of this work requires improvement to enhance clarity and comprehension. It is currently challenging for readers to grasp the entire training and inference pipeline quickly. Additionally, several design choices related to the training process lack sufficient explanation, which may leave readers puzzled about the rationale behind them.

4. Furthermore, the name "Dynamic-LLaVA" may lead to misconceptions about the method. It implies that the system dynamically drops the KV cache at each layer; however, it should be clarified that the cache is dropped permanently and cannot be recovered in subsequent layers.

5. The training process is not aligned with the inference process for the output predictor. The former one can see all generated tokens and decide the most important ones, while the latter one can only decide whether to drop the current one based on previous context.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel method, Dynamic-LLaVA, which dynamically sparsifies visual context during the prefill stage and vision-text context during the decoding stage of Visual Language Model inference. Specifically, two learnable predictors are designed to identify important visual and language tokens. Additionally, masked softmax is applied during training, and Gumbel-softmax with a Straight-Through Gradient Estimator is used to address gradient flow issues. Furthermore, a batch-parallel strategy is introduced to enable efficient sparsification during inference in the Dynamic-LLaVA framework. Empirical experiments demonstrate that this method can compress approximately 75% of visual context and save around 50% of GPU memory for the KV cache.

### Strengths
This paper introduces a novel design for two token predictors, formulating visual and textual context compression as an end-to-end optimization problem. Techniques such as Gumbel-Softmax and the Straight-Through Gradient Estimator are employed to enhance training stability. In addition, parallel sparsification inference optimization would provide an effective solution for model serving.

### Weaknesses
1. It is unclear whether the two learnable predictors are applied to each decoder layer. If they are, do they share the same parameters or are they independently parameterized?  If not all layers, please clarify which specific decoder layers the predictors are applied to.
2. Compressing generated text is primarily beneficial for long-generation tasks. Would you please provide specific statistics on the average output length for each task they evaluated? And discuss how the benefits of their method scale with increasing output length.
3. Please quantify the additional training time and computational resources required for this method compared to direct KV cache compression approaches, as well as additional prediction overhead compared normal decoding. This would help readers better understand the tradeoffs.
4. More recent related work about KV Cache compression method should be included, such as TidalDecode (https://arxiv.org/abs/2410.05076) focusing on decoding compression. 
5. A few mathematical representations are not appropriate. For example, in section 3.1, $\mathcal{I}^I = \{ $1, 2, \cdots, N_{l}^I $}, layer index $l$ should be set for $\mathcal{I}^I $; And in section 3.3.1, all layers share the same binary masks $\mathcal{M}^I and \mathcal{M}^{OT}$? since there are no layer index $l$. 
6. The writing could be improved to make the narrative more concise and clear.

### Questions
1. Previous studies have shown that deeper layers exhibit higher attention sparsity. How is sparsification strength adjusted for different decoder layers?
2. Running predictors introduces additional latency. However, the proportion of this latency relative to overall prefill and decoding time is not disclosed. Additionally, in standard LLaVA decoding, previous KV cache is fetched, and byproduct attention scores are accumulated to assess token importance, which is quick and efficient. However, for "Online KV Cache Compression," running predictor incurs additional latency. And only the current token is used to predict all previous tokens, do you think solely performing prediction on a current token provide enough information? Have you analyzed the wrongly evicted tokens?
3. Can this method be applied to language models that utilize Group Query Attention?
4. Have you considered scenarios where long-text context is present during the prefill stage?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Dynamic-LLaVA is a framework for efficient inference in multimodal large language models, dynamically reducing vision context redundancy during the prefill and decoding stages, cutting computation by ~75% in prefill, and saving ~50% computation and memory during decoding, without significant loss in performance.  It also designs the specific training and inference strategy for parallel sparsification, making their approach more efficient.

### Strengths
1. The article has a rigorous logical structure, with precise formulations for each method and complete notation. Readers who read carefully can clearly understand the methods explained in the text.

2. The experimental results are excellent; it appears that inference speed and computational cost are significantly reduced with minimal loss in performance.

3. The method design is ingenious; selective approaches are often challenging to train, but the paper provides an effective end-to-end training method that successfully alleviates the gradient flow problem.

### Weaknesses
Although the writing is logically clear and the formulas are complete, this level of detail makes it somewhat challenging for readers.  There are too many formulas here. Perhaps reduce them a bit and add more diagrams to aid understanding. Some high-level schematic diagrams could help; Figure 2 aids understanding to some extent, but it’s still not sufficient.

### Questions
There aren’t many issues; the method in the paper is logically clear, the experiments are comprehensive, and the performance is excellent.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces Dynamic-LLaVA, a dynamic vision-language context sparsification framework aimed at enhancing the inference efficiency of mllms. The main challenge addressed is the increasing computational and memory overhead during inference, particularly as output tokens are generated, which diminishes efficiency benefits of prior vision context reduction methods. Dynamic-LLaVA reduces redundancy in both the vision and language contexts during the prefill and decoding stages, with a specialized sparsification strategy tailored for different inference modes, including decoding with and without KV cache. Experimental results demonstrate that Dynamic-LLaVA significantly reduces computational consumption—by about 75% during the prefill stage and 50% during decoding without KV cache—and saves approximately 50% of GPU memory with KV cache, all while maintaining or even improving model performance. This framework is the first to attempt simultaneous sparsification of both vision and language contexts, achieving efficient inference with negligible performance degradation.

### Strengths
1. As an article focusing on efficiency, it grasps the key point very well: solving efficiency problems from the perspective of efficiency. From the numerical results, Dynamic-LLaVA performs well in reducing computation and memory consumption, especially in the pre-filling and decoding stages, reducing the computation by about 75% and the GPU memory overhead by about 50%.

2. The **SPARSIFICATION INFERENCE** part achieves dynamic sparsification of visual and language context by introducing learned predictors, effectively reducing the computational and memory burden in different reasoning modes, making the entire generation process more efficient. I think this is a highlight. Sparsification of tokens during test time is a very useful method, and I personally believe that less is more. These sparse parts should actually improve the representation ability.

3. MaskedSoftmax is a good point to note. From my previous fine-tuning experience, since the generated $logp(y|x)$ is calculated by logits under the corresponding label $y$, the appearance of 0 value in the whole chain process is absolutely harmful. This soft labeling method is very thoughtful.

### Weaknesses
1. In the method section, the description of sparse reasoning and end-to-end training relies too much on symbolic expressions and lacks intuitive explanations. It could be aided by adding some simplified explanations or visual flowcharts to help a wider readership understand the complex technical details.
2. You can consider adding some evaluations. I personally feel that the current evaluation benchmarks are not comprehensive enough to explain the performance of MLLMs. And you should analyze as thoroughly as possible. You can refer to the Cambrian-1 [1] standard or try to apply the method to the Cambrian model.
3. In the results of the experimental section, the impact of sparsification on complex tasks (such as generating long texts or multi-round conversations) is not sufficiently verified.

### Questions
1. I am curious why it is not tested on the latest versions of llava such as llava-one-vision, llava-next, etc.
2. I don’t quite understand why Table 5 uses GQA and VQAv2 as vision evaluations. I think a more vision-centric dataset such as MMVP is needed.
3. Paper mentions that different sparsification strategies are used in the pre-filling stage and the decoding stage, but the specific differences between the two and the motivation for this design are not clear. In particular, why both visual and language context are sparsified in the decoding stage, while only visual tokens are sparsified in the pre-filling stage, what is the design consideration behind this?
4. In order to avoid unstable training when there are few samples, paper only sparses the samples whose text length exceeds a certain threshold. However, does this strategy ensure the stability of the model when facing inputs of different lengths? In actual use, will the model cause significant performance fluctuations due to changes in input length? If a model behaves unstable for certain input lengths, this may significantly limit its applicability in real-world applications.

### Soundness
2

### Presentation
3

### Contribution
2

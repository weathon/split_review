# ME-Switch: A Memory-Efficient Expert Switching Framework for Large Language Models

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
The typical process for LLM's development involves pre-training a general foundation model on massive data, followed by fine-tuning on task-specific data to obtain a series of specialized experts. Serving these experts can pose significant \revise{memory} challenges, as loading all experts onto devices is impractical, and frequent switching between experts in response to user requests can incur substantial I/O costs. 
Previous approaches decompose the expert weights as the pre-trained weights plus delta weights, followed by \jing{quantizing} the delta weights \jing{using output channel-wise step sizes} to reduce the model size. However, \jing{these methods overlook the fact that certain input channels of delta weights can cause significant quantization errors at extremely low bitwidths.}
Additionally, existing methods assume that the appropriate model for a user request is known in advance, which is not the case in practice. To this end, we introduce ME-Switch, a memory-efficient expert switching framework tailored for serving \revise{multiple LLMs}. To condense the number of bits required for describing the delta weights, we propose a salient-aware delta compression method that
\revise{first identifies which input channels of delta weights are salient based on reconstruction error and then}
employs mixed-precision quantization that selectively quantizes non-salient input channels of delta weights to extremely low bits while keeping the salient ones intact, significantly reducing storage demand while maintaining performance.
Moreover, we develop a model-level routing method that efficiently directs user queries to the most suitable expert by \revise{performing domain classification}. Extensive experiments show the promising memory efficiency and routing performance of ME-Switch. For example, when serving three models from the Mistral-7B family, ME-Switch reduces the model size by $1.74\times$ and maintains nearly lossless performance on instruction, mathematical reasoning, and code generation tasks. \jing{Furthermore, our method can efficiently serve 16 Mistral-7B models on \revise{an} NVIDIA A100 GPU.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce ME-Switch, a memory-efficient framework for serving MoE-based LLMs. Given a set of MoE models across specified domains, they present a quantization technique for deltas from the base model which they argue is better than other approaches per its retention of accuracy and effectiveness in reducing model size. The approach attempts to estimate the saliency of particular weight deltas for quantization based on a reconstruction loss-based scheme As part of the assumption that models are domain-specific, the authors train a routing model to delegate user inputs to a domain-specific model.

The authors showcase retention of performance task performance across various domains in conjunction with a reduction in GPU memory usage attributed to efficient quantization.

### Strengths
- The application of reconstruction-based quantization to input model weights is novel insofar as other methods (low rank approximation, uniform quantization) are not as effective.
- Results show minor to negligible losses in accuracy across many tasks, including some gains, though the degree to which these are due to noise is not immediately clear.
- The reduction in memory usage as compared to other baselines is somewhat compelling, although compared to baselines without any delta-based approaches, which the authors did not contribute.

### Weaknesses
 - The assumption that each LLM specializes in a distinct domain is a large one, and limits the general applicability of the authors' approach. Indeed, in many MoE-based settings, model diversity is sufficient to improve performance significantly, and task specialization is not even considered. The given assumption also requires training a domain-based router, which itself requires ablations. The authors need to argue that this setting is representative and useful.
- There are missing baselines. The sensitivity and quality of the domain-based routing setup as compared to a baseline without adaptive quantization makes it difficult to disambiguate the effect of improved quantization alone.
  - Similarly, there is no baseline that foregoes SFT or one that compares SFT without quantization or task routing. These components should be independently ablated.
- Results are defined only on a very narrow set of task domains. This makes it quite unclear how the proposed approach generalizes. Domain-specific expert setups in a general setting might involve dozens of models in a large-scale system.
- In general, the paper’s writing is redundant, i.e. the core premises, contributions, and prior work are presented multiple times each, with similar levels of depth. The authors could make room to do more experiments by removing redundant components.
- The approach with which the router is trained generalizes very poorly. A router must be trained based on a collection domain-specific models for every single setup. A router trained on a specific domain-specific set of multiple choice questions is quite specific to the input tasks.
- There is no presentation of an accuracy-memory tradeoff across approaches. This, combined with weak baselines reduces the strength of the contribution.

### Questions
- Introduction — the authors might consider reframing motivations around MoE as well and listing memory pressure as a primary motivator for LLM task specialization.
- Line 78 the "information loss" that occurs with subsequent methods can be further specified. Is this something that affects downstream accuracy, or does this refer to something else?
- Why doesn’t reconstruction loss merely end up choosing values which are closest to values which are fp16 quantized, i.e. representable with low approximation error? More analysis of reconstruction loss would be helpful to prove efficacy.
- Why is fp16 used throughout the experiments setups rather than bf16, which is supported on A100s (used in the paper) and is far more common in inference settings?
- What is the effect of using different backbones for the same task with the proposed approach?
- What additional details can be shared about the Triton kernel? What is the performance benefit of its inclusion? How is the implementation structured?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors focus on the problem of serving multiple models (fine-tuned over
the same base) together. The challenge is that each model occupies a lot of memory and 
the authors build on the idea of delta compression between the FT'ed models and the base.

Specifically, the authors proposed a mixed precision compression technique for the delta.

Moreover, the authors proposed a routing-based method to pick the right model to use
given user input.

### Strengths
- The proposed idea makes sense, and seems to work better than the baseline.

### Weaknesses
 - It would be great if both contributions can be evaluated more thoroughly against previous methods
- The second contribution could be put better into context

### Questions
1. I am a little bit confused by how the router is related to the first contribution -- 
it would be great if the authors could elaborate more? these two parts look quite
orthogonal to me.

2. There are a lot of previous work (especially for the router) tackling similar problems,
it seems that the authors only compared with the most natural baseline, but not
more advanced methods. it would be great if the authors can justify it or provide more
results.

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
This paper addresses the problem of serving multiple expert models i.e multiple models finetuned for different tasks from the same base model. Serving all fully finetuned models is expensive since they take up memory and switching these in and out of memory can be slow. Existing methods use low-rank finetuning to reduce the storage required for finetuned models, however low-rank finetuning does not match full finetuning in quality hence recent methods instead quantize the delta between the finetuned model and the base model. However, these quantization methods can lead to significant quantization errors at low bitwidths. This paper proposes a saliency aware method for quantizing delta between the finetuned and base model.  In addition, this paper suggests a dynamical routing method to determine which expert model to route user requests to when the appropriate model for a user request is not known in advance.

### Strengths
1. This paper is generally well written and easy to follow, and the problem is well-motivated.
2. Experiments are comprehensive with convincing results and there are sufficient ablations to justify different design choices.
3. The problem of serving multiple finetuned models is a very poignant problem in this era of LLMs.

### Weaknesses
Major
1.  How does the saliency based delta quantization technique in this paper differ from other non-magnitude based saliency quantization techniques like https://arxiv.org/pdf/2405.14917 ?
2. Model routing is a well studied problem! Are there other existing approaches that study model routing in the same scenario where the appropriate model is not known? How is your solution different or better than them ?

Minor
1. Related work like GPT-Zip https://openreview.net/pdf?id=hO0c2tG2xL is not cited
2. On line 46, the paper claims that no single model can master all tasks simultaneously. While this is not currently the state of affairs is there a formal proof or evidence that this is impossible?

### Questions
1. Will the code for this be open source?
2. Are there any insights on why mixed precision quantization outperforms the full precision models in certain settings?
3. Is there an estimate of how often in practice is the appropriate model not know in advance ? Is this more common than the case where it is known?

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
4

### Summary
The author contributed a memory-efficient expert-switching framework for LLMs, called ME-Switch. The framework is designed to address the challenge of LLMs' storage efficiency when serving multiple large expert models, while maintaining performance through model-level router fine-tuning and efficient distillation fine-tuning.

The proposed method applies mixed-precision quantization for delta weights to preserve model performance and enhance efficiency. This is achieved by selecting non-salient input channels based on quantization errors. Additionally, the approach incorporates a model-level router, implemented through supervised fine-tuning of a relatively small LLM, to switch between expert domain-quantized LLMs according to the user's inquiry. A detailed ablation study is included to further validate the approach.

### Strengths
- The author proposes an innovative and effective framework for improving the storage efficiency of serving multiple LLM experts.

    - This framework leverages mixed-precision quantization for delta weights, intelligently selecting non-salient channels based on quantization errors. The strategy of maintaining performance by selecting the top-k salient channels as non-quantized has been proven effective, as the accuracy surpasses baseline models across multiple domains.

    - The framework also introduces model-level routing by fine-tuning a small LLM router on domain-specific datasets, transforming the routing problem into a simpler domain classification task. This simplifies the problem and making the finetuning of small LLM router more lightweight compared to finetuning the MoE models

    - The framework implements on-demand swapping, enhancing GPU memory efficiency by loading only the quantized delta weights onto the GPU. This optimization is particularly effective for switching between large LLM experts. Combined with model-level routing and a specialized routing kernel, this approach significantly improves decoding efficiency. As demonstrated in the paper, it enables hosting up to 16 models on a single GPU, whereas the naive approach encounters out-of-memory (OOM) issues after just 4 models.


- A detailed ablation study is presented to demonstrate the effectiveness of mixed-precision quantization compared to baseline approaches across multiple domains. These experiments significantly strengthen the framework's methods. For example, the approach preserves accuracy competitively when compared to fixed-precision and low-rank adaptation methods. Furthermore, the ablation study clearly illustrates the selection of parameters, such as the number of non-quantized channels (k) and quantization bits (b). Lastly, the performance comparison with other weight quantization methods like AWQ, Random, Wanda, and Magnitude supports the intuition that selecting non-salient input channels yields the best performance.


- The clarity of writing, including the structure, figures and tables, is good. The author explains the background context and methodology in a good manner.

- The paper also discusses other important aspects, such as latency, with a comparison to MoE.
    - Model-level routing offers the advantage of requiring less intensive training compared to MoE.
    - The author employs a Triton kernel to further reduce latency.

### Weaknesses
 - The model-level router relies heavily on domain classification, which requires fine-tuning the router model on domain-specific datasets. This approach may have several disadvantages:
    - The author conducted research on at most four distinct domains for the router: mathematics, code, Chinese, and instruction. Although the router demonstrates strong classification ability for these domains, it would be worthwhile to explore its performance across more domains, particularly those with potential overlap. For example, Text Classification Experts and Sentiment Analysis Experts, or Mathematics and Physics Experts, Computer Science Experts and Data Science Experts. In such scenarios, MoE could leverage the combined knowledge of multiple experts, as it is fine-tuned based on a token-level router. A potential consequence is that, when adding a large number of experts to the MoE, fine-tuning may converge faster due to shared knowledge and parameters across domain experts. In contrast, a model-level router may struggle to distinguish between overlapping domain experts and always rely on a single expert, potentially causing overall performance degradation.
    - This approach requires the construction of a domain classification dataset, which can be inconvenient. For instance, when adding a new domain expert, the router would need to be re-trained on an updated domain dataset.
    - While the approach demonstrates effectiveness compared to other quantization methods in ablation studies, the experiment results do not include a comparison with an end-to-end token-level router approach, such as MoE baselines.

- Latency analysis: The comparison only covers up to 4 models, after which the naive implementation encounters out-of-memory (OOM) issues. It is a little subtle to conclude that latency is lower than naive model as the number of models is greater than 4.

### Questions
- The author highlights the advantages of ME-Switch over MoE, such as reduced fine-tuning work and higher efficiency. However, it would be beneficial to include a more in-depth discussion of its limitations compared to MoE models. This would provide readers with a deeper understanding of the nature of model-level routing, particularly in addressing challenges like handling overlapping expert domains and managing a larger number of models when adapting to new experts, areas where MoE models may offer distinct advantages. Notably, the latency advantage of ME-Switch is fully realized when the number of models increases.

- Latency analysis: The discussion of latency mentions that the naive implementation has a slight advantage when the number of models is fewer than 4, as shown in Figure 8, and the author attributes this to the quantization overhead. However, why does the quantization overhead stop being the dominant factor as the number of models increases? What is the trend in the profiling of quantization overhead as the number of models continues to increase? A deeper analysis of this would be valuable.

### Soundness
3

### Presentation
4

### Contribution
3

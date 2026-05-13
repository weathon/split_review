# CoreInfer: Accelerating Large Language Model Inference with Semantics-Inspired Adaptive Sparse Activation

- Decision: Reject
- Scores: 3, 8, 6, 8

## Abstract
Large language models (LLMs) with billions of parameters have sparked a new wave of exciting AI applications. However, their high computational costs and memory demands during inference pose significant challenges. Adaptive sparse activation inference, which activates only a small number of neurons for each token, offers a novel way to accelerate model inference without degrading performance, showing great potential for resource-constrained hardware devices. Nevertheless, existing methods predict activated neurons based on individual tokens with additional MLP, which involve frequent changes in activation maps and resource calls, limiting the acceleration benefits of sparse activation.
In this paper, we introduce \textbf{CoreInfer}, an MLP-free adaptive sparse activation inference method based on sentence-level prediction. Specifically, we propose the concept of sentence-wise core neurons,  which refers to the subset of neurons most critical for a given sentence, and empirically demonstrate its effectiveness. To determine the core neurons, we explore the correlation between core neurons and the sentence's semantics. Remarkably, we discovered that core neurons exhibit both stability and similarity in relation to the sentence's semantics—an insight overlooked by previous studies. Building on this finding, we further design two semantic-based methods for predicting core neurons to fit different input scenarios. In CoreInfer, the core neurons are determined during the pre-filling stage and fixed during the encoding stage, enabling zero-cost sparse inference. We evaluated the model generalization and task generalization of CoreInfer across various models and tasks. Notably, on an NVIDIA TITAN XP GPU, CoreInfer achieved a 10.33$\times$and 2.72$\times$speedup compared to the Huggingface implementation and PowerInfer, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a new sparse activation inference method based on the semantics of input sentences. It finds that the activated neurons remain relatively stable for semantically consistent sentences and thus proposes to only activate the frequently used neurons based on the input context. Experiments validate the effectiveness of the proposed method in improving throughput compared to previous predictor-based sparse activation methods.

### Strengths
1. The paper is clearly written and easy to follow.

2. The proposed method is motivated by an analysis of core neurons and semantics.

3. Experiments demonstrate that the proposed method achieves improved throughput compared to previous predictor-based methods.

### Weaknesses
1. The major concern with this paper is the general applicability of the proposed method. For user input contexts and questions, especially for long-context reasoning, it is difficult to ensure and inaccurate to assume that all inputs are semantically stable and full of relevant information. Thus, the assumption underlying the proposed method is too strong and may not be applicable in real-world applications or more challenging questions. Specifically, the method relies on the premise that input semantics are consistent enough to activate a stable set of core neurons, which is a strong assumption given the variability of natural language. This is particularly problematic in multi-turn conversations or when dealing with complex, multi-faceted questions where the semantic focus can shift significantly. Additionally, for similarity-guided prediction, core neurons are identified by finding the closest semantic groups. If this is the case, the insight of this work is generalized to the following one: similar topics will always activate the same set of core neurons, which is also a too strong assumption. Similarly, the input context may not contain only one topic.

2. As a follow-up to the above concern, the proposed method is evaluated on a limited number of tasks. It would be highly desirable for it to be evaluated on a larger set of commonsense reasoning tasks and long-context tasks, such as LongBench, to validate whether the sparsified neurons can handle more complex input contexts. The current evaluation does not sufficiently demonstrate the robustness of the method across diverse semantic inputs and reasoning challenges. Specifically, the lack of evaluation on tasks that require complex reasoning or involve multiple topics makes it difficult to assess the generalizability of the approach.

3. The proposed method is not benchmarked against predictor-based sparse activation methods in terms of task accuracy. This makes it difficult to assess the trade-offs between the proposed method and existing approaches. It is crucial to understand whether the gains in throughput come at the cost of accuracy, and how the proposed method compares to other methods that also aim to improve inference efficiency. Furthermore, the comparison should consider not only accuracy but also the computational overhead of each method, including the cost of training and inference.

4. Some design aspects of the proposed method need more clarification: (1) it is unclear how semantic similarity is computed; (2) it also remains unclear how to determine whether the input is stable. The lack of clarity on these key aspects makes it difficult to reproduce the results and understand the underlying mechanisms of the method. Specifically, the choice of semantic similarity metric and the criteria for determining input stability can significantly impact the performance of the proposed method, and these details need to be clearly specified.

### Questions
My questions are listed in the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
CoreInfer determines the top Beta neurons activated (pooling across tokens in the prefill) and then uses just these for the decoding, if these are found to be stable (if this group stays approximately the same). If these are not found to be the CoreInfer then defers to a "similarity-guided" prediction, that takes core-neurons found to be semantically similar (available in some datasets like ag_news, or found via K-means clustering).

The result is an MLP-free method of actively reducing the effective size of the FFN, only reusing these "core neurons", causing speed-ups observed up to around 10x for decoding from saved calculations and reduced need for memory movement. Similar results and accuracy is observed in several cases.

### Strengths
# Strengths

This paper investigates prediction of which neurons will be activated, stemming from an observation that similar semantics (especially per sentence) tend to have a similar set of neurons activated. The amount of savings in inference time is quite large, suggesting a high degree of sparsity in the FFN -- especially when using ReLU activation functions -- which unblock running large language models efficiently on smaller GPUs and edge-devices.

## Significance:

The FFN holding the greatest number of weights as the model increases in size, and hardware needing to begin loading early (to prevent bubbles in pipelining), this provides an excellent recipe efficient hardware decoding for LLMs.

The majority of energy being spent on off-chip DRAM f  Might be interesting to check what the average performance would be omitting this fall-back in the unstable case, while increasing the size of the accepted core-neuron group.
etching (see "Melting Point" and "MobileLLM" papers), this also provides an excellent route for running LLMs on constrained hardware.

## Clarity and Originality

The paper is very clear in it's motivations and methods, and how it differs from related works.  Prior works tend to use MLPs and learned parameters, which this paper claims add overhead which reduce the inference savings. This work focuses on two techniques for on-the-fly decoding acceleration, without additional learned parameters (maximizing speed ups and energy/memory savings of the technique in edge-inference)

### Weaknesses
The semantic stability is noted by the paper to sometimes be not strong enough to warrant restricting to neurons characterized in the prefill stage.

When this happens the authors explored finding semantic similarity to core-neuron sets already discovered, allowing for time studied into inner understanding of the LLM's "core-neuron sets" to make gains in inference speed.

Adding more clear labelling would benefit a few of the figures.  Perhaps Asterisks on Table 2 indicating on which benchmarks used the Stable vs Unstable methods.  Figure 6 preferably would have titles, to clarify which graph refers to which method, and should either be on the same graph or use the same x and y scales to make it easier to compare.

### Questions
Sentence length was found to be a distinguishing factor for when the semantics are stable enough to dynamically determine the core-neurons, would there be any data for how this transfers across very different looking tasks (e.g. programming where sentences are not as well defined) and languages with different average sentence lengths and syntax?

How does this correlate with tokenization? Namely, if the language is caught in the byte-fallback of the tokenizer (e.g. Mandarin characters for r50k Tiktoken) would the number of core neurons increase?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work proposes an activation sparsity method to accelerate LLM inference. Specifically, the method identifies core neurons at the sentence level during the pre-fill stage when the input sentence exhibits stable semantics. Furthermore, by analyzing the relationship between core neurons and semantics, the method can be adapted to tasks with variable sentences by clustering samples into distinct groups. Experimental results demonstrate a significant inference speedup with an acceptable accuracy drop.

### Strengths
1. This work has a clear motivation. In related work, token-wise sparsification and the inclusion of an additional learnable predictor both present challenges, as they lead to extra inference overhead.

2. The proposed concept of sentence-wise core neurons is novel. It's intriguing that core neurons can be directly identified in the pre-fill phase without the need for a additional predictor.

3. In the experiments, the proposed methods shows significant inference speedup with acceptable accuracy drop.

### Weaknesses
1. The proposed method involves three manually tuned hyper-parameters (alpha, beta, gamma) to determine final sentence-wise core neurons, that maybe limit its practical usage. 

2.  The claim for Fig.2(C) needs to be further justified.  I agree with the authors that Fig.2(C) shows some of the activations are close to each other for the same sentence. However, Fig.2(C) also exists some of group neurons with same color (e.g., same sentence) are located superlatively. How do the authors claim that "the distribution of core neurons of tokens in the same sentence is always closer".  

3. In the experiments, some of the results are unclear. (Please see the detailed comments in the Question below)

### Questions
Overall, I find the proposed method well-motivated and innovative. However, the current version has several areas that require further justification. Specifically, please address the following questions:

1.  Weakness.2 as shown above.

2. The speedup gain is consistent across OPT-6.7 and other LLMs. In Table 3, the proposed method achieves a 10.33x speedup over the original transformer on OPT-6.7B; however, the speedup is notably lower on other LLMs, as shown in Fig. 7. For instance, on Llama2-7B with a sequence length of 256, the speedup is around 1.6x.

3. The system memory usage needs further clarification. According to Fig. 7, the proposed method shows no system memory consumption, while the original transformer uses substantial system memory. My understanding is that the proposed method uses activation sparsity to accelerate inference in the original transformer without any system-level modifications. Could you clarify this aspect?

4. The work lacks a comparison of perplexity (PPL) or zero/few-shot accuracy. The authors focus only on hardware performance comparisons with previous works, such as Deja Vu and PowerInfer. How does the accuracy of the proposed method compare to these works? Additionally, what is the sparsity level of these other methods?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an MLP-free adaptive sparse activation inference method based on
sentence-level prediction.

### Strengths
1. The paper is easy to follow, with clear writing and presentation.
2. Evaluation results are comprehensive.

### Weaknesses
1. In lines 93-94, it should be 'nearly lossless generation'
2. How would the method scale to larger models such as LLaMA-70B in multi-GPU settings?
3. Would this method be compatible with quantization methods?
4. The authors should also discuss related works on sparse KV cache [1-4], another important direction to accelerate LLM inference.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

# Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Multimodal Large Language Models (MLLMs) have emerged as a central focus in both industry and academia, but often suffer from biases introduced by visual and language priors, which can lead to multimodal hallucination. These biases arise from the visual encoder and the Large Language Model (LLM) backbone, affecting the attention mechanism responsible for aligning multimodal inputs. Existing decoding-based mitigation methods focus on statistical correlations and \textit{overlook the causal relationships between attention mechanisms and model output}, limiting their effectiveness in addressing these biases. To tackle this issue, we propose a causal inference framework termed \textbf{\model} that applies structural \textbf{\underline{causal}} modeling to \textbf{\underline{M}}LL\textbf{\underline{M}}s, treating modality priors as a confounder between attention mechanisms and output. Specifically, by employing backdoor adjustment and counterfactual reasoning at both the visual and language attention levels, our method mitigates the negative effects of modality priors and enhances the alignment of MLLM's inputs and outputs, with a maximum score improvement of \textbf{65.3\%} on 6 VLind-Bench indicators and \textbf{164} points on MME Benchmark compared to conventional methods.
Extensive experiments validate the effectiveness of our approach while being a plug-and-play solution.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper points out problems arising from biases induced by visual and language priors in the visual encoder and the LMM backbone, and it mentions the oversight of the causal relationship between attention and the model's output. In this study, a method called CausalMM identifies modality priors as confounders, addressing them through backdoor adjustment and counterfactual reasoning.

### Strengths
- The paper is well-written and easy to read.
- Performance improvements were observed in the benchmarks used for evaluation.
- The creation of counterfactual attention in various ways is novel.

### Weaknesses
 - It is unclear if this method constitutes a backdoor adjustment. My understanding of backdoor adjustment involves identifying a confounder, then using it to reduce the confounder's impact, which differs from using counterfactuals as described here. Counterfactuals are typically used to measure natural direct effects or natural indirect effects, and I am curious if this method follows such an approach. Mathematical proof may be needed for line 225.
- Please explain which paths need to be blocked in Figure 2. It appears that the path from the image to visual attention and from text token embedding to LLM attention should be blocked, but aren’t those paths essential?
- This method seems closer to a contrastive decoding approach rather than backdoor adjustment. It appears to use counterfactual attention similarly to how negative samples are used.
- The intervention on attention to reduce the influence of defined priors as confounders seems to also reduce the impact of input on attention.

### Questions
- Line 58 mentions the VCD method as considering only statistical correlation. I thought the VCD method also accounts for causation by using negative images to identify language priors. Why do you view the VCD method as overlooking causal relationships?
- On page 5, does 'j' refer to the order of the method for creating counterfactual attention?

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
This paper addresses the problem of modality prior-induced hallucinations in Multimodal Large Language Models (MLLMs). The authors propose a causal reasoning framework, which applies structural causal modeling and counterfactual reasoning to MLLMs. By treating modality priors as confounding factors between attention mechanisms and the model's output, the approach aims to mitigate the negative effects of these priors. The method involves interventions on both visual and language attention mechanisms and is evaluated on several benchmarks.

### Strengths
1. **Perspective**: The paper introduces the idea of applying causal inference techniques to address modality prior-induced hallucinations in MLLMs, which is an interesting and potentially valuable perspective.

2. **Comprehensive Experiments**: The authors conduct experiments on multiple benchmarks, including VLind-Bench, POPE, and MME, providing a range of evaluations for their method.

3. **Ablation Studies**: Inclusion of ablation studies helps in understanding the impact of different components of the proposed method.

### Weaknesses
1. **Insufficient Theoretical Justification**: The paper lacks a deep theoretical analysis of why the proposed causal interventions lead to improved performance. The causal model is described, but the theoretical foundations and assumptions are not thoroughly explored or justified.

2. **Limited Novelty**: While the application of causal inference to MLLMs is presented as novel, causal reasoning has been previously applied in machine learning models, including language models. The paper does not sufficiently differentiate its contributions from existing work in causal inference applied to deep learning.

3. **Inadequate Comparison with Baselines**: For some evaluations(such as figure 3,5,6), the experimental evaluation compares the proposed method with only a partial set of baselines from the setup. Under many settings, the performance of this method underperform or only slightly outperform baseline methods as shown in table 1.

4. **Superficial Experimental Analysis**: The results, while showing improvements, lack statistical significance testing. Additionally, there is a lack of detailed analysis of where and why the method improves performance, making it difficult to assess the true impact.

5. **Applicability and Generalization**: The approach is tested on specific MLLMs, but it is unclear how well the method generalizes to other models. 

6. **Lack of Discussion on Limitations**: The paper does not adequately discuss the limitations or potential downsides of the proposed method, such as scenarios where it might not work well or possible negative impacts.

### Questions
1. **Theoretical Justification**: Can you provide a more detailed theoretical analysis or proofs to support the efficacy of your causal interventions? 

2. **Computational Complexity**: What is the computational overhead introduced by your method? How does it compare to the baseline models in terms of runtime and resource consumption?

3. **Generality of the Approach**: How well does your method generalize to other types of MLLMs, such as chameleon?

4. **Limitations and Failure Cases**: What are the limitations of your method? Are there scenarios where it does not perform well or might even degrade performance? How do you address potential negative impacts?

5. **Impact of Hyperparameters**: How sensitive is your method to the choice of hyperparameters involved in the interventions? Have you performed a sensitivity analysis?

6. **Robustness to Noise**: How does your method handle noisy or adversarial inputs? Does the causal framework improve robustness in such cases?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a causal inference framework called CAUSALMM, which is designed to mitigate the issue of multimodal hallucinations in Multimodal Large Language Models (MLLMs) that are often caused by biases from visual and language priors. The core idea is to treat modality priors as a confounder between the attention mechanisms and the model output, and to apply structural causal modeling to address these biases. Specifically, the authors use backdoor adjustment and counterfactual reasoning at both the visual and language attention levels to alleviate the negative effects of modality priors, thereby enhancing the alignment between the MLLM's inputs and outputs.

### Strengths
- The paper is well-written and clear motivated.
- The method is plug-and-play and does not require retraining, making it practical for existing MLLMs.
- The integration of causal inference to modify attention weights and optimize token generation in MLLMs is novel.

### Weaknesses
 - The background knowledge about causal inference is insufficient. The authors do not explain why causal inference is effective in capturing the causal impact of effective attention in MLLM output.
- Several claims lack explanations and references. The authors are advised to carefully proofread the paper and add the necessary citations. For instance:
    - Line 65: “Modality priors are one of the confounding factors in the causal path of MLLM.” Why? And what is the definition of the confounding factor?
    - Line 58-61: “existing decoding strategies……, overlooking the causal relationships among attention visual attention, language attention, modality priors, and model output.”
- In Section 3.3, the authors introduce the causal effect and the corresponding calculation of selecting the next token. But what’s next after determining the index of the next token? The authors are advised to supplement more on this point. I assume that it is going to talk about inferencing with the modified next token prediction.
- Though the proposed method is somewhat novel, the experimental results are not quite significant and robust compared with existing methods (Table 1).
- Lack of implementation details. It would be more convincing to provide more details on how to reproduce the experimental results.
- The notations should be considered more carefully. For example, in Section 3.3, it is confusing that in Line 222-223 $O$ represents the original output but in Line 226-227 it denotes the model output.

### Questions
- In Lines 58-61, the authors state that existing decoding strategies overlook the causal relationships among attention visual attention, language attention, modality priors, and model output. However, VCD [1] injects noise into the image input and acquires the output logits for contrastive decoding, which can be seen as a counterfactual intervention at the visual input. The effects of this intervention are also later shown in the attention parts and model outputs [2,3]. Could the authors make more discussion on this perspective?
- What does $\gamma$ mean in the equations in Section 3.3? More importantly, the calculation of choosing the index of the next token is not discussed. Why is it calculated in this way?
- Could you provide the results of VCD and OPERA on VLind-Bench?

[1] Leng S, Zhang H, Chen G, et al. Mitigating object hallucinations in large vision-language models through visual contrastive decoding[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 13872-13882.

[2] Xiao X, Wu B, Wang J, et al. Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment[J]. arXiv preprint arXiv:2405.17871, 2024.

[3] Chen Z, Xu C, Qi Y, et al. Mllm is a strong reranker: Advancing multimodal retrieval-augmented generation via knowledge-enhanced reranking and noise-injected training[J]. arXiv preprint arXiv:2407.21439, 2024.

### Soundness
2

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
3

### Summary
This paper introduces a causal inference framework named CausalMM. Considering the influence of visual and textual priors on the predictions of multimodal large language models (MLLMs), the authors employ backdoor adjustment and counterfactual reasoning to mitigate these priors’ effects. Specifically, they design various methods to perturb the attention layers in ViT and LLMs, such as randomization and reversal, to obtain the perturbed model predictions (counterfactual logits). They then use contrastive decoding to enhance the model’s predictive probability distribution. The method is a plug-and-play solution and demonstrates effectiveness on mainstream models and benchmarks.

### Strengths
1. This paper presents a simple yet effective method: perturbing the attention matrices in ViT or LLMs to generate counterfactual logits, and then using contrastive decoding to improve the model’s predictive probability distribution.  
    - Flexibility and Generalizability. This method is plug-and-play and offers more flexibility compared to VCD, which obtains counterfactual logits by adding noise to images. Perturbing attention allows for greater design space and importantly, can be adapted to modules of different modalities, such as ViT and LLM.
    - Simplicity and Effectiveness. Unlike VCD and its variants that often rely on Adaptive Plausibility Constraints, the proposed method does not appear to require them.
2. The experiments demonstrate the effectiveness of the method.

### Weaknesses
1. How was the hyperparameter (e.g., $\gamma$) determined? Were hyperparameters independently tuned for different benchmarks and model/method variants?
2. The choice of base models is not comprehensive. The authors selected LLaVA-1.5 and Qwen2-VL as base models to validate their method, but introducing more models would help confirm the method’s universality. For instance, a table could be added to the appendix to show the method’s cross-model generalizability.
3. Section 3.1 and Figure 2 are hard to follow. Section 3.1 introduces very complex causal relationships, but these seem not closely tied to the method. If I understand correctly, the proposed method is largely similar to VCD: it generates counterfactual logits by perturbation and improves predictions by removing this "background noise" from the normal logits, which does not necessitate such complex preliminary explanations. I would also like to mention that the $P_{effect}$ discussed in Section 3.3 might be unnecessary.
4. The equations are also hard to follow. For example, in Section 3.3, the core of the method involves logits processing, which is unrelated to softmax. Therefore, separating logits from the softmax equation and presenting them independently would be clearer and more concise.

### Questions
See Weakness 1.

### Soundness
2

### Presentation
2

### Contribution
2

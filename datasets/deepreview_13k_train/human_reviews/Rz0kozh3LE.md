# Mixture of Attentions For Speculative Decoding

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
The growth in the number of parameters of Large Language Models (LLMs) has led to a significant surge in computational requirements, making them challenging and costly to deploy.
Speculative decoding (SD) leverages smaller models to efficiently propose future tokens, which are then verified by the LLM in parallel.
Small models that utilise activations from the LLM currently achieve the fastest decoding speeds.
However, we identify several limitations of SD models including the lack of on-policyness during training and partial observability. 
To address these shortcomings, we propose a more grounded architecture for small models by introducing a Mixture of Attentions for SD.
Our novel architecture can be applied in two scenarios: a conventional single device deployment and a novel client-server deployment where the small model is hosted on a consumer device and the LLM on a server.
In a single-device scenario, we demonstrate state-of-the-art speedups improving EAGLE-2 by 9.5\% and its acceptance length by 25\%.
In a client-server setting, our experiments demonstrate: 1) state-of-the-art latencies with minimal calls to the server for different network conditions, and 2) in the event of a complete disconnection, our approach can maintain higher accuracy compared to other SD methods and demonstrates advantages over API calls to LLMs, which would otherwise be unable to continue the generation process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The method addresses two key limitations of existing SD approaches, (1) partial observability and (2) lack of on-policyness, by incorporating Layer Self-Attention (LSA) and Cross-Attention (CA).

### Strengths
- The client-server framework with the ability to handle disconnections positions the approach as a practical advancement for deploying LLMs.

- The introduction of LSA and CA layers to mitigate partial observability and improve on-policyness makes sense.

### Weaknesses
1. The paper does not thoroughly justify the choice of parameter configurations and its training in its experiments.  As discussed in the Yi et al. (2024), the training dataset and the choice of number of parameters can significantly affect the SD performance, but this paper does not [A].

[A] Yi et al., 2024. Towards Fast Multilingual LLM Inference: Speculative Decoding and Specialized Drafters, EMNLP 2024-main.

2. Discussions for the memory-bound nature of LLM is required in the paper.

3. The effectiveness of the proposed method on models having 3B~13B parameters is unclear. Current experiments focus on relatively smaller models, and the results may not hold for state-of-the-art LLMs, which typically exhibit different scaling dynamics and memory behavior.

4. Typo? line 466.

5. Parallel to Medusa, actually there are concurrent works regrading non-autoregressive heads for SD. It would be good to put discussions for those areas.

- Gloeckle et al. (2024), Better & Faster Large Language Models via Multi-token Prediction.

- Stern et al. (2024), Blockwise Parallel Decoding for Deep Autoregressive Models

- Kim et al. (2024), Accelerating Blockwise Parallel Language Models with Draft Refinement. (https://openreview.net/forum?id=KT6F5Sw0eg)

### Questions
See Weakness.

Will update the score after looking at the results of Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a method, Mixture of Attentions for SD, which improves upon the standard SD approach that is used to increase LLM efficiency. The improvements are specifically targeting the partial observability and lack of on-policyness problems of traditional SD. The Mixture of Attentions method is shown to lead to improvements for a single device, but the paper also shows its efficiency/accuracy benefits to a client-server setting.

### Strengths
The organization and flow of the paper is very good. The background section is particularly thorough and helpful.

The problem is well-explained (e.g. partial observability and lack of on-policyness are both detailed when explaining the methodology) so it is made clear what exactly the Mixture of Attentions method is aiming to solve. Additionally, the related work is well-addressed. It is clear exactly how this work is different from prior solutions.

It is great that the client-server scenario is tested in a practical setting with different devices (having different resource capacities) and the devices have distance between them. This setting is not only realistic, but it is also well-explained in the text.

There is good theoretical support in the Methodology section, which provides additional justification for the proposed method being superior to the current SOTA (EAGLE, Medusa).

The thorough experiment detail (particularly in the appendix) makes the method highly reproducible.

### Weaknesses
The experimentation is very narrow, especially since it only focuses on one model architecture and the improvements over EAGLE seem relatively small and inconsistent. It is therefore not convincing that this method would be effective more generally.

It is not very clear why this problem/contribution is important. The paper would be stronger if the method was motivated by some real-world example where SD may be used, but would lead to significant problems that Mixture of Attentions would mitigate. I understand that the computational requirements of LLMs is an issue, but the introduction could do a better job of explaining why SD should be focused on as a solution for the computational expense and therefore is important to build improvements for. It is also difficult to understand how this work can be have a broader impact or inspire future work. The future work that is suggested at the end of the conclusion seems very specific and narrow. Essentially, the contribution just seems very narrow.

### Questions
Why did you choose to only experiment with LLama3-8B-Instruct? It is good that there is justification for only comparing to EAGLE (and not Medusa or Tandem Transformers), but there is no justification for your LLama model choice. How do you think your method would work with other architectures?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on an LLM acceleration technique called Speculative Decoding, which leverages efficient models (smaller but less capable) to draft future tokens, which are verified by the LLM (more capable but much less efficient) in parallel. In particular, it addresses the limitations of previous methods by proposing a Mixture of Attentions architecture on top of a prior work EAGLE to improve its performance. They demonstrate the effectiveness of their approach in both a single-device setting and a novel client-server setting, achieving speedups and improved accuracy. They also present a framework for using LLMs on edge devices, allowing for offline text generation with minimal dependence on a server.

### Strengths
- The work improves above EAGLE-2 and seems to achieve state-of-the-art results.
- The work provides a good background on speculative decoding
- The work proposes an interesting client-server setup that fits well with the speculative decoding technique

### Weaknesses
 - The work lacks an overall view and clear statements that can improve readability.
    - Method intuition: the method section only lays out the information of each component but does not provide an overall view of the proposed method as well as motivating intuitions for each design. The necessary intuitive descriptions are also not found in the appendix.
    - Experiment result: the work only compares to one prior work, EAGLE-2, as a baseline, but did not provide information on how well EAGLE-2 compares with other prior works.
    - the hyperparameter N is used many times. Giving it a name can help readability.
- This work overlooks overall performance metrics, concentrating instead on metrics specific to the speculative decoding framework, such as acceptance length. This focus may inadvertently encourage adversarial scenarios where the smaller model aims merely to deceive the larger model into accepting its outputs rather than genuinely enhancing result quality.
- The work neglects analysis of the time/computational complexity of its method. 
- The ablation study compares different hyperparameters but does not ablate the other components. Thus, the importance and contributions of the designs in Section 3.1 and Section 3.3 is not provided.

### Questions
(also see weaknesses)
- The experiment on N is arbitrarily set to 0, 1, 3. Why not continuously evaluate 0,1,2.... to the number of layers in the large model?
- In the client-server mode with N > 0, are the last layers of the large model copied onto the client side?

### Soundness
4

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
The paper proposes an improved architecture for speculative decoding, which incorporates Layer Self-Attention and Cross-Attention mechanisms to address common limitations like partial observability and lack of on-policy training. Experimental results demonstrate that this approach achieves state-of-the-art speed and accuracy in single-device and client-server deployments, maintaining high accuracy even during disconnections. The limitation analysis of SD in the paper provides insights into this field.

### Strengths
(1) The limitation analysis of SD in the paper is very interesting, it links the limitation of SD (e.g., the SD may still give different predictions compared to only using the large model even when the previous tokens are all accepted ) with theoretical analysis, i.e., partial observability. This may provide further insights of optimizing SD algorithms.

(2) It is a very good point that the paper design and evaluate the scenario that the small model is on a resource-limited client and the large model is on the server. It is a very realistic scenario to use SD.

(3) The paper uses SOTA models such as Llama-3 for evaluation. Also the benchmarks used (e.g., HumanEval, MT-Bench) are challenging enough for evaluation.

### Weaknesses
(1) The link between the limitation of SD and the proposed attention-based method is not clear enough. Why Layer Self-Attention can solve partial observability? Further intuitive explanations or theoretical analyses are needed.

(2) Authors mention that their work is based on a SOTA SD method named EAGLE. Then my concern is, is the proposed algorithm transferable to other SD algorithms? For example, can the algorithm be applied to non-self-draft SD? The point here is that, if the algorithm can be applied to most of the SD frameworks, there will be more contribution. Otherwise, it's just an optimization of one of the previous works.

(3) No accuracy is displayed in the experiment section. I know that this is common in SD papers. However, when I was trying SD codes, I found that the SD performance is usually not as good as the large model, which is the purpose of SD. Thus, because this paper aims to solve problems such as partial observability, will it also increase the performance of SD, in addition to the efficiency? I believe experiments related to this point will make the paper more convincing.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
2

### Contribution
3

# MoLEx: Mixture of Layer Experts for Fine-tuning with Sparse Upcycling

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
Large-scale pre-training of deep models, followed by fine-tuning them to adapt to downstream tasks, has become the cornerstone of natural language processing (NLP). The prevalence of vast corpses of data coupled with computational resources has led to large models with a considerable number of parameters. While the massive size of these models has led to remarkable success in many NLP tasks, a detriment is the expense required to retrain all the base model's parameters for the adaptation to each task or domain. Parameter Efficient Fine-Tuning (PEFT) provides a highly effective solution for this challenge by minimizing the number of parameters required to be trained in adjusting to the new task while maintaining the quality of the model. While existing methods have achieved impressive results, they mainly focus on adapting a subset of parameters using adapters, weight reparameterization, and prompt engineering. In this paper, we study layers as extractors of different types of linguistic information that are valuable when used in conjunction with each other. We then propose the Mixture of Layer Experts (MoLEx), a novel Sparse Mixture of Experts (SMoE) whose experts are layers in the pre-trained model. In particular, MoLEx is applied at each layer of the pre-trained model. It performs a conditional computation of a mixture of layers during fine-tuning to provide the model with more structural knowledge about the data. By providing an avenue for information exchange between layers, MoLEx enables the model to make a more well-informed prediction for the downstream task, leading to better fine-tuning results with the same number of effective parameters. As experts can be processed in parallel, MoLEx introduces minimal additional computational overhead. We empirically corroborate the advantages of MoLEx when combined with popular PEFT baseline methods on a variety of downstream fine-tuning tasks, including the popular GLUE benchmark for natural language understanding (NLU) as well as the natural language generation (NLG) End-to-End Challenge (E2E).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new approach to fine-tune LLMs. PEFT is becoming a mainstream method to adapt general-purpose model to specific tasks.MoLEx, proposed by the authors, aims at improving PEFT through leveraging pre-trained model layers and MoE to provide the model with more structural knowledge about the data. This method enhances information exchange between layers, leading to better predictions with minimal computational overhead. Experiments show that MoLEx is a more efficient technique to fine tune models.

### Strengths
1. The paper has clearly explained the benefits of using MoLEx to sparse upcycling models and its robustness as an ensemble model. Theoretical proof has laid good foundation for the idea.
2. The idea of exploiting MoE to improve the efficiency of LLM fine-tuning is a novel idea and a problem worth to research.
3. The experiments are well designed and show comprehensive results on the proposed idea. Although I do think it is necessary to further expand to more models and tasks, the promising results are a good start.

### Weaknesses
1. I am a bit confused by the inference time. I can understand MoE inference can be accelerated with parallel/distributed computation. But it also means using more resources. It is better to clarify what is the fair comparison in terms of the efficiency with naive PEFT models.


### Questions
1. How to determine K in top-K and the number of experts  in the upcycling process. I know Top-1 is widely used number. But I am not sure in this paper, how will it impact the performance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduced a Mixture of Layer Experts (MoLEx), which leverages layers as experts to facilitate the exchange of linguistic information and improve a model’s fine-tuning and transfer knowledge ability. 
In particular, the author proposed a structural change to the architecture of the model which is compatible with PEFT method while maintaining the same number of effective parameters. 
Experimental results demonstrated that MoLEx significantly improves performance across a range of downstream tasks, including the GLUE benchmark and the E2E Challenge, while incurring minimal additional computational overhead and scales well with model size.

### Strengths
I think this paper is a good upgrade in the field of Parameter Efficient Fine-Tuning.
Comparing with predominant method (Lora),  it achieve significant improvement on a few data-set with almost the same cost (speed, memory, parameter size).
Also I like the theoretical proof to justify the robustness of MoLEx in a simplified model and the empirical evidence provided.

### Weaknesses
1.My major concern of this paper is the linguistic analysis part.  One of the main claim of this paper is "relevant linguistic information is captured by selected experts".  I think it's very intuitive and hard to explain. In Figure1, the author tried to connect some linguistic feature with different layers in a probing task. But I am not quite convinced by the analysis, I think most NLP task involves different level of linguistic information, so it's hard to say one task focus more on certain part of information and the proposed method could facilitate the process.  So would like to see more discussion on this direction or if there is another angle to explain where the performance gain is coming from.

2.I feel the real computational cost of the proposed model is larger than Lora, but the parallelism makes the final speed the same. Is there any statics on this issue?

3.One small issue is the presentation of Lemma and Theorem looks a little messy, the alignment and layout could be adjusted to make it easy to read.

### Questions
please see weakness part

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents MoLEx, a simple and effective method that does not alter the model's structure or add extra parameters. Instead, it treats all layers as experts and introduces a router at each layer to select the top k layers for activation. Extensive experiments on RoBERTa and GPT-2 demonstrate the strong performance of MoLEx.

### Strengths
This paper introduces a novel sMoE model whose experts are layers in the pre-trained model. MoLEx is a simple yet effective approach without additional expert parameters.

### Weaknesses
Weaknesses & Questions

1. The introduction of this paper does not effectively convey the motivation for the proposed MoLEx method. I would appreciate it if the authors could briefly clarify the limitations of existing sMoE methods and explain the specific problems that the proposed approach aims to address.

2. The methods section of this paper relies heavily on mathematical formulas, whereas the MoLEx method itself is relatively straightforward. I suggest that the authors consider providing a method diagram to complement the mathematical expressions, as this could facilitate a better understanding of the proposed method.

3. I believe there are some unclear aspects in the implementation of the method presented in this paper. Specifically, when mixing layers, is the paper using  $x_{t+1}=x_t+\alpha u_{t}(x_{t})+(1-\alpha) u_{l}(x_{t})$, where $u_{l}$ is the top-1 layer selected by the router, to obtain $u_{t+1}$? Or is it treating the low-rank matrices $A$ and $B$ from LoRA as experts to derive $x_{t+1}$ through $x_{t+1}=x_{t}+u_{t}(x_{t})+\alpha B_{t}(A_{t}(x_{t})) + (1-\alpha) B_{l}(A_{l}(x_{t}))$? I also hope the authors can add relevant training details in the methods or implementation section to clarify this.

4. Referring to point three, I believe the authors' assessment of efficiency may be inaccurate regardless of the method used. The claim that "these layer experts can be computed in parallel and do not increase the computational time" (lines 494-495) seems misleading. Since each input must undergo forward computations through two layers in the case of top-1, the total computational load will inevitably increase, not just due to the additional computations from the gate layer. Therefore, it may not be appropriate to assert that there is no impact on efficiency solely based on parallel computation. I encourage the authors to reassess their evaluation of efficiency, particularly by considering results from single-GPU inference. Furthermore, a more detailed analysis of the time overhead during training is needed, as the inference time increase suggests a potential impact on training efficiency as well.

5. The descriptions of the trainable parameters for LoRA and MoLEx in Tables 1 and 2 may be misleading. It could lead readers to believe that MoLEx has no additional trainable parameters compared to LoRA. However, the inclusion of the gate layer, regardless of its parameter count, should be represented to accurately reflect the differences. I encourage the authors to provide a clear comparison of the trainable parameters in the tables.

6. The authors utilized eight A100 GPUs for their experiments, but models like RoBERTa and GPT-2 seem somewhat outdated at this point. I suggest that the authors consider expanding their experiments to include more recent LLMs, such as Qwen-2.5 or Llama-3.1, to enhance the credibility of their findings. Additionally, evaluating these models using popular current assessment methods like MMLU, GSM8K, and HumanEval would provide valuable insights. The current evaluation using perplexity is insufficient to demonstrate the effectiveness of the method on downstream tasks.

7. The MoLEx method proposed in this paper appears to be adaptable to various models and training methods. However, it was only validated under the LoRA method. I suggest that the authors include experiments with full parameter training to provide a more comprehensive evaluation of the method's effectiveness.

8. Current sMoE models applied to LLMs typically operate at the token level, where different experts are activated for each input token. However, the appendix of this paper states that MoLEx employs a sentence-level approach, with all tokens in a batch going through the same experts. It would be valuable for the authors to further explore how MoLEx performs in a token-level activation context, as this could provide insights into its adaptability and effectiveness in such scenarios.

9. Line 148 of the paper concludes that "preserving the useful information in the pre-trained model" is achievable, supported by extensive mathematical derivations. However, I believe this conclusion is not adequately reflected in the experiments. As noted in [1], parameters themselves can retain knowledge, so a catastrophic forgetting experiment is necessary to validate this claim. I suggest using benchmarks like TRACE [2] to assess whether MoLEx can mitigate the issue of catastrophic forgetting.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

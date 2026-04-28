# LoRA-Gen: Specializing Language Model via Online LoRA Generation

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Recent advances have highlighted the benefits of scaling language models to enhance performance across a wide range of NLP tasks. However, these approaches still face limitations in effectiveness and efficiency when applied to domain-specific tasks, particularly for small edge-side models.
We propose the LoRA-Gen framework, which utilizes a large cloud-side model to generate LoRA parameters for edge-side models based on task descriptions.
By employing the reparameterization technique, we merge the LoRA parameters into the edge-side model to achieve flexible specialization.
Our method facilitates knowledge transfer between models while significantly improving the inference efficiency of the specialized model by reducing the input context length.
Extensive experiments show that LoRA-Gen outperforms the conventional LoRA fine-tuning, which achieves competitive accuracy and a 2.1x speedup with TinyLLaMA-1.1B on common-sense reasoning tasks.
Besides, our method delivers a compress ratio of 10.1x with Gemma-2B on intelligent agent tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Generic LLMs often demonstrate a tradeoff between efficiency and effectiveness for domain-specific tasks or preferences. Often, we utilize parameter-efficient finetuning techniques to train task or dataset specific models, among which LoRA tuning is a very popular approach. 

In this paper, the authors propose LoRA-Gen which utilizes an online Cloud-side language model (a finetune LLM with LoRA experts) to generate meta tokens based on the task-specific system instructions; these tokens controls the composition of the parameters from the LoRa experts for the task-specific specialized language models. 

The authors empirically demonstrate that LoRA-Gen leads to several advantages over previous parameter-efficient tuning methods: 1) the system instructions are used to learn the specialized LoRA parameters, achieving context compression for the user queries, 2) more efficient than LoRA-MOE, and 3) knowledge-transfer from large cloud LLMs to specialized LMs. 

The proposed approach is evaluated on commonsense reasoning and agenic benchmarks. The results demonstrate the superiority of the approach over existing parameter-efficient finetuning techniques on the above mentioned points.

### Strengths
The proposed approach, LoRA-Gen, is a novel approach for parameter-efficient finetuning with multiple strong advantages (listed above) over previous methods. The authors strongly justify their claims with strong results and ablations on reasoning and agentic benchmarks.

### Weaknesses
Please explain “edge-side language models”. It is used throughout the paper without properly introducing it.

More explanations **with examples** are needed regarding how the meta tokens are generated and used to learn final LoRA parameters. How is each meta token associated to a transformer layer in the edge-side LM?

Add confidence intervals to your results in Table 2 and 3.

Citation issues:

Correct all citations. For example:
“in specific tasks Fu et al. (2023); Grangier et al. (2024); Shen et al. (2024)”  to “in specific tasks (Fu et al. 2023; Grangier et al. 2024; Shen et al. 2024)”
“ (e.g., LLaMA3 Touvron et al. (2023b))” to  (e.g., LLaMA3; Touvron et al. 2023b)”
“Unlike LoRA-MoE Dou et al. (2024)” to “Unlike LoRA-MoE (Dou et al. 2024)”

“consistently outperforms other fine-tuning methods across different backbone models.” ->  
LoRA-Gen performance on SIQA is inferior to other models. Also performance improvements for Gemma-2B models are not consistent.

### Questions
“consistently outperforms other fine-tuning methods across different backbone models.” ->  
LoRA-Gen performance on SIQA is inferior to other models. Also performance improvements for Gemma-2B models are not consistent.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
**Summary**: The paper presents LoRA-Gen, a layerwise LoRA-MOE approach for specialized language models. The method employs a larger teacher LM (LLaMA-8B) to convert task-specific prompts into meta tokens, which are then used to generate adapter weights for a smaller target LM. The authors demonstrate improved accuracy and reduced latency compared to baselines like LoRA and LoRA-MOE.

**Detail**: This paper proposes to use a large teacher LM (llama-8b) to transform prompts (task definition, few-shot examples etc..) into meta tokens, and train a routing model to transform meta tokens into adaptor weights and finally assemble these adaptors with the corresponding weights to a target smaller LM. With this pipeline, long task specific prompts are compressed into LoRA, and the smaller LM can use these LoRA for downstream tasks.

**Results**: This paper conducted experiments with some reasoning classification tasks and agent task. Results show their method can significantly reduce the latency and get better results.

### Strengths
1. The method presents a novel approach to compress task-specific prompts into LoRA weights. And the layerwise LoRA-MOE design is an interesting architectural contribution to the field of model adaptation
2. The reduced latency could be valuable for real-world applications, particularly in resource-constrained settings
3. The evaluation includes both classification tasks and more complex agent-based scenarios

### Weaknesses
 **Major Concerns**
1. Critical Implementation Details Missing

- The meta token generation process and their representation are not adequately explained. It is unclear whether the meta-tokens are generated in a training-free manner using only prompting or if they require a training phase. This distinction is crucial for understanding the method's complexity and applicability.
- The 'direct' method referenced in Table 8 lacks proper introduction. It's unclear how this method is implemented and how it differs from the proposed approach, making it difficult to assess the validity of the comparison.
- The cloud-side LM's role during inference requires clarification. Specifically, it is not clear if the cloud-side LM is involved in every inference or only during the generation of LoRA weights. This is important for understanding the overall latency and resource requirements of the method.
2. Questionable Latency Comparisons

The baseline methods are task-agnostic, which means they either support any task inference via prompt, or routing to task specific lora weights. But the proposed method is task specified, in my understanding, need to know which task it is processing to use its corresponding LoRA-gen weights. The latency advantages may primarily stem from task specification rather than architectural improvements. Please correct me if I'm wrong. Also, n line 259, it says "our method is cost-free during inference". I think it is not true when the testing is task agnostic. The comparison with methods like MixLoRA, which are designed for multi-task scenarios, is not entirely fair, as the proposed method is inherently task-specific. This difference in design goals makes the direct comparison of latency and performance questionable.
3. Statistical Rigor Concerns

Results lack reporting of mean and variance metrics
This is particularly crucial given:

- The use of relatively small models (1.1-2B parameters)
- Small dataset sizes (e.g., WinoGrande)
- The potential variance in few-shot learning scenarios

**Minor issues**
1. The paper incorrectly groups diverse tasks under "Commonsense Reasoning Datasets." Suggest renaming to "Reasoning Tasks" as the datasets span both commonsense and scientific reasoning
2. Sections 4.1 and 4.3 contain redundant dataset introductions and citations
3. Dataset sizes should be explicitly stated for reproducibility

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work builds upon previous LoRA-based mixture-of-experts approaches for multi-task training in large language models. In classic LoRA-MoE methods, individual LoRA modules are fine-tuned within an LLM and selected using a routing function. Here, the authors propose an alternative method, consisting in generating a cloud-based LoRA module directly from a task-specific prompt. The generated module is then integrated into a general, edge-side model using reparameterization, creating a specialized LM adapted to the task at hand.

The authors show that this method offers equivalent or improved performance across a variety of tasks, and features additional improvements, mainly in the form of significant gains in inference speed and context length over previous methods. They verify their findings across several language models and multiple tasks.

### Strengths
The paper is well-written and clear. The proposed online LoRA-Gen method is interesting and innovative, and it achieves strong empirical results, namely in terms of inference speed and compression ratio gains over the previous methods. This is mostly due to efficient inference-time specialization without additional training, which is a significant benefit for deploying models on resource-constrained devices. In addition, LoRA-Gen offers good generalization to unseen tasks thanks to knowledge transfer from large to small models, resulting in a flexible and adaptable approach.

Given these points and the clear hyperparameter setup for reproducibility, I believe that the authors' method is likely to be useful in several practical applications.

### Weaknesses
My main point of criticism of this work is that its positioning with respect to previous methods seems a bit unclear and could use some improvement. In section 3.2, the method is described as addressing three challenges: effectiveness for multi-task learning, generalization to unseen tasks, and computational complexity. The results do indicate that LoRA-Gen performs well in all three aspects, but multi-task learning gains are quite modest compared to previous methods, especially given the added complexity of the indirect LoRA generation. It seems to me that the main benefit of LoRA-Gen is its impressive inference speedup and compression gains. As a result, the authors' findings would have more strength if claims of efficiency were discussed in more detail - for example, perhaps their method can allow edge-side optimizations for model memory usage, and other efficiency metrics such as computing costs and data requirements could be taken into account.

The section on limitations is very short and could be more detailed. The online component is the major strength of this method, but it also leads to cloud dependence. For example, the authors could describe possible use cases.

The paper contains a few minor formatting/typographical errors: "Sotmax" in Eq. 4, "which maintaining" in the "Intelligent Agent Scenario" subsection of 4.3, as well as issues with the formal of several citations in the first paragraph of 4.3, which should all be easy to correct.

### Questions
In the ablation study, it is said that the average accuracy decreases by 1.2 points when the auxiliary loss is excluded from training. I am assuming that this 1.2-point difference is computed from the accuracy obtained with a loss coefficient of 0.01, but please let me know if I am mistaken. This would imply that the model performance is worse with a 0.1 loss coefficient than if it has no auxiliary loss, and that it increases as the value of alpha decreases. Have the authors tried using even lower values to see whether model performance keeps increasing past the 0.01 point?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes LoRA-Gen, a method for generating LoRA modules for reduced scale LMs using LLMs running in the cloud. Given a prompt, the method generates tokens using the LLM based on the system prompt which the method is aiming to encode. Then, the method uses these so-called "meta-tokens" to figure out weights over a set of pre-trained LoRA modules from a set of seen tasks. These LoRA weights are then distributed to the small LLM, merged in to minimize latency impact, and then used for task inference on device.

### Strengths
- The core problem statement of "utilizing a large cloud-side model to generate parameters for a smaller edge-side model to achieve
better specialization" is a very reasonable motivator for on-device specialization with fewer shortcomings from smaller models. It's also a realistic setting that could exist for real-world deployments. I haven't seen this formulation in related work and it seems a strong setting of interest.

- Hyper-networks for LoRA modules are a very interesting subject area, as they highlight, since they can enable the projection to unseen tasks which is evaluated here. I think this premise of work also has strong advantages and seems worth exploring.

### Weaknesses
 - The work is missing ablations/comparisons to the other context compression methods which they list in section 2.3, an area which was introduced for LLMs even earlier than they reference in their related works by Snell et al. in 2022. Given that most of the latency gains come primarily from using context compression, it would be necessary to see that the compression ratio and latency of *at least one other* context compression method is worse than the proposed approach to assess whether these gains are substantial v.s. prior work.

- The work doesn't engage with a clear weakness of this method which is that it requires more compute at training time than any of the baselines due to the use of the larger cloud-side model. I'd like to see a concrete comparison of the training compute cost between these different methods included so that readers can understand the degree of training compute increase.

- The work does not perform any form of statistical significance testing on the results nor does it report how data was held out for hyperparameter selection. Both of these together present a significant soundness concerns if they are not addressed.

Each of these items has associated questions below.

### Questions
Questions:

- In Section 2.3, you cover many context distillation methods such as gisting, AutoCompressors, ICAE, and 500xCompressor. Why were these not included as baselines? Especially depending on the LoRA hyperparameters, the compression ratios of such methods may be perhaps even better than LoRA-Gen so the omission of these baselines despite your awareness of them requires some justification or, preferably, at least one of these methods should be compared to. This is especially true since at least some of these methods, such as gisting, are conceptually much simpler than the method proposed here.

- How many FLOPs does it take to train LoRA Gen? How many FLOPs does it take to train each of the other baselines? In addition to inference latency, these training FLOPs are a key attribute of each method that isn't currently reported.

- Using a bootstrap significance test, is LoRA Gen a significant improvement over the baselines reported in Table 2? You can find methodological best practices for significance testing here: https://aclanthology.org/P18-1128/

- What are the validation set results for all the experiments in section 4.4? These *must* be included in the appendix to show that the hyperparameters used in the paper would be selected using validation set results rather than the test set results currently listed.

- On line 100, you reference "additionally, since it does not require the input of agent definitions during inference, it achieves a remarkable 10.1x speedup". Is this referring to the 10.1x compression ratio on the prompt? If so, this statement seems inaccurate since the prompt tokens have a lower impact on latency than generated tokens due to batching. This is doubly shown by your own latency numbers in Table 2, where LoRA-Gen reduces the latency only by 2.4x which is notably far less than 10.1x.

- I'm still a bit unclear on the term "meta-tokens" from the cloud model. As far as I can tell, these tokens are not specialized in any way for this parameter generation task but are just regular llama tokens given the prompt. Is this correct? If so, it should be explained as such rather than introducing more terminology needlessly. If they have more customized use than this, especially to encourage them to have mappings to specific layers in the downstream model, this requires a lot more explanation than the description on 216-220.

- The caption and description of Figure 1 is a bit unclear to me in the current draft. If I'm understanding correctly, the few-shot examples listed here are being used as a system prompt which is why even the baseline method is slower than LoRA-Gen. Is this correct? If so, you should make this clearer by listing that item as "Prompted Qwen"! Furthermore, the prompted method is slower at inference, but the inference cost is the *only* cost, while LoRA-Gen has a large training cost right? Do you think it's fair to compare these metrics solely along this axis, without marking that some of the methods are training free?


Misc. Typos and Suggestions:
- Throughout the work, the `\citep` tag should be used much more frequently. As a rule of thumb, if you aren't using the name of the authors as part of the text that fits grammatically, the citation should be included in parentheses. For example, on lines 148 and 149 all of these citations should be with `citep` rather than `cite`.
-  LLaMA3 Touvron et al. (2023b). This is the incorrect citation for Llama 3. The work cited is the original Llama paper, LLama 3 is Dubey et al. 2024 https://arxiv.org/abs/2407.21783
- Line 218 "by generates" should be "by generating".

### Soundness
2

### Presentation
3

### Contribution
3

# Generative Parameter Efficient Fine-Tuning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
We present \underline{G}enerative Parameter-Eff\underline{I}cient \underline{F}ine-\underline{T}uning (GIFT) for adapting pretrained Transformer backbones on downstream tasks.  GIFT learns to generate the fine-tuned weights for a layer directly  from its pretrained weights. The GIFT network is parameterized in a minimally-simple way by two linear layers (without bias terms), and is shared by different pretrained layers selected for fine-tuning (e.g., the Query layers), which result in significantly fewer trainable parameters compared to the layer-specific methods like Low-Rank Adapter (LoRA). We also show this formulation bridges parameter-efficient fine-tuning and representation fine-tuning. We perform comprehensive experiments on natural language tasks (commonsense and arithmetic reasoning, instruction tuning,  and sequence classification) and computer vision tasks (fine-grained classification). We obtain the best performance and parameter efficiency among baselines on commonsense and arithmetic reasoning, and instruction following using the Llama family of models and on visual recognition benchmarks using Vision Transformers. Notably, compared to LoRA, we obtain 5.7\% absolute increase in average accuracy with 14 times reduction of parameters on Commonsense170k using {\tt Llama-3 (8B)}, and  5.4\% absolute increase in the win rate with 4 times reduction of parameters using {\tt Llama-2 (7B)} during instruction tuning. Our GIFT also obtains a slightly higher win rate on instruction tuning than {\tt GPT 3.5 (Turbo 1106)}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a modification to the well-known lora method. Technically, as the original lora method can be formulated as $\overline{W} = W + AB$, the proposed modification changes it to $\overline{W} = W + WAB'$, with $B'$ shared across layers. The authors have discussed the relationship with ReFT, and used experiments to support the efficacy of the modifaction.

### Strengths
LoRA is now a widely adopted technique and improvements over it can make profound impacts.

### Weaknesses
Unconvincing method design

The biggest weakness to me is that the proposed method is not supported by reasonable and convincing motivations. Specifically, there are two major changes from the original LoRA:
1. sharing half of the lora weights across layers;
2. involving the original weight as an extra term into the weight delta.

However, it is unclear why these two changes are useful and how do they work to benefit. After reading the paper I cannot get a satisfying answer. This problem fundamentally limits the value of the work, as it is less likely for people to give the proposed method a try without an intuition that makes people believe it would lead to better results.

The introduction of the simple method is unnecessarily complicated

As mentioned in the summary part, the core of the proposed method is simply $\overline{W} = W + AB$ -> $\overline{W} = W + WAB'$, but the paper makes me feel that it is much more complicated.

Content organization can be better

The first section is too long. As an introduction section, it involves too many details that are hard to fully understand before reading the methodology section. I suggest only preserving the high-level ideas in this section while moving the technical details elsewhere.

Others

1. tied-lora[1] also works on lora + weight-sharing, and I suggest to add some analysis & comparisons.
2. I cannot find the information about the backbone model for visual experiments, welcome to correct me if I missed it.

### Questions
Could authors give some intuitions on why the changes proposed are beneficial?

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
3

### Summary
The paper introduces Generative Parameter-Efficient Fine-Tuning (GIFT), a method to fine-tune pretrained Transformer models with fewer parameters by generating fine-tuned weights from pretrained ones. They show this formulation can address the two questions about 1)an explicit and direct mapping between the fine-tuned model and the frozen pretrained model, 2) bridge  parameter-efficient fine-tuning and representation fine-tuning. The proposed GIFT method is designed by implementing a lightweight structure of only two linear layers, shared across selected layers in the model. Using minimal linear layers without bias, GIFT achieves significant parameter reductions compared to LoRA and performs better across some NLP and computer vision tasks, obtaining a slightly higher win rate on instruction tuning than GPT 3.5.

### Strengths
GIFT represents a unique approach to generating fine-tuned weights directly from pretrained weights, sharing parameters across layers to enhance efficiency.
Experiments demonstrate that GIFT outperforms existing PEFT methods on various natural language and computer vision tasks while using significantly fewer parameters, showing improvements in memory efficiency as well.
Tested on diverse tasks, GIFT shows effectiveness across commonsense reasoning, arithmetic, instruction following, and visual recognition tasks, reinforcing its versatility as a parameter-efficient fine-tuning approach.

### Weaknesses
Lack of some comparison settings on full finetuning:  How is the comparison results on full finetuning in Table-2 and Table-3 for commonsense reasoning and arithmetic reasoning task？Table-1 compares the full finetuning setting on Llama-2 7B for instruction following task, but table-2 and table-3 didn't reveal this setting.
Potential Scalability Concerns: Although parameter-efficient, the scalability of GIFT for larger models (beyond 8B parameters, like llama1-13B, llama3-65B) isn’t explicitly demonstrated. The experimental version of llama1-3 presented by the author is all less than or equal to 8B, leaving questions about its performance in high-scale deployment.  
Limited Ablation on Layer Selection and Configuration: GIFT’s performance maybe vary depending on which layers are selected for fine-tuning. While some experiments address this, there is minimal ablation on different layer selection and the comparison between Lora with the same layers.
Some models compared are not newly advanced enough : Table-1 shows the result of fine-tuning Llama-2 7B with GIFT for instruction following task, but the compared gpt series is GPT 3.5 Turbo, a little bit outmoded. How is the comparison result of GIFT among some newly advanced models like gpt4o or others？

### Questions
See weaknesses.

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
This paper proposes a new fine-tuning method called Generative Parameter-Efficient Fine-tuning (GIFT), which trains two linear layers to project the pre-trained weight matrices into fine-tuned weights. The authors argue that it offers a unifying perspective on PEFT and representation-efficient fine-tuning (ReFT) approaches by projecting pre-trained weights linearly. The results demonstrate that GIFT improves performance while using fewer parameters compared to previous parameter-efficient fine-tuning (PEFT) methods, such as LoRA, ReFT, and VeRA.

### Strengths
1. This paper provides new insights into fine-tuning techniques, suggesting that the proposed Generative Parameter-Efficient Fine-Tuning (GIFT). I think it can be viewed as a specific form of Representation Fine-Tuning (ReFT), where all tokens in the selected layers share the same re-parameterization parameters. Notably, GIFT is easier to implement than ReFT, utilizing two linear layers for weight re-parameterization without explicitly modifying token embeddings.

2. The performance is impressive. They achieve similar or better performance with fewer parameters comparing to the other PEFT. Validation was conducted across multiple tasks, datasets, and models, demonstrating GIFT's effectiveness and versatility.

### Weaknesses
1. In my opinion, the authors make claims about aspects that remain unexplained, which can confuse readers. The authors should provide further clarification to support these claims. For instance:

(Line 051) "but the learnable weight-residuals do not have direct information exchange with the pre-trained weights"

(Line 135) "one of the simplest updates that minimally distorts and maximally preserves the pre-trained knowledge is defined by Eqn.1 and Eqn.2, thanks to the low-rank factorized linear projection in the parameter space."

(Line 181) "Additionally, adding fixed random matrices with learnable scales in PEFT makes the relationship between fine-tuned models and frozen pretrained models less intuitive."

(Line 194) "Furthermore, token-level interventions lack a holistic understanding of the relationship between ReFTed models and frozen pretrained models."

2. There are issues with mathematical notation throughout the paper, making it difficult for readers to follow the ideas presented. Please refer to other PEFT papers (e.g., ReFT, LoRA) for guidance on presenting mathematical concepts clearly. For example, matrices should be represented in bold uppercase, vectors in bold lowercase, and scalars in italic lowercase. Additionally, in machine learning literature, symbols like θ (theta) and φ (phi) are conventionally used to denote model parameters, not calculations within the model.

3. The content has redundancies; for instance, the Related Work section and Section 2.1 cover similar material, leading to overlap.

### Questions
See weaknesses.

+) 

1. What did the authors want to say in Section 2.3? I think the idea behind this is similar to 2.2. What is the meaning of "accumulate" in the paragraph?

2. Please provide more details regarding the experiment in Fig. 2. Specifically, clarify the meaning of the cluster. If the authors aim to demonstrate that GIFT enhances object highlighting within the attention modules, results should be compared with those of the pretrained model for a meaningful evaluation.

### Soundness
3

### Presentation
1

### Contribution
3

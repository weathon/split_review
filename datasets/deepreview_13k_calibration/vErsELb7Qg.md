# LoRA Recycle: Towards Fine-Tuning-Free Visual Foundation Model via Double-Efficient Data-Free Meta-Learning

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
Large Language Models (LLMs) such as ChatGPT can efficiently adapt to few-shot tasks without fine-tuning, making them ideal for data-limited applications requiring real-time responses. However, this adaptability has not yet been replicated in current Visual Foundation Models (VFMs), which require explicit fine-tuning with sufficient tuning data. Low-Rank Adaptation (LoRA), an effective fine-tuning approach, adapts VFMs to specific tasks by updating extra lightweight modules. Thanks to its modularity, users can upload locally tuned LoRAs to public repositories without exposing private training data. In this paper, we explore the potential of reusing diverse pre-tuned LoRAs without accessing their private training data, to improve the few-shot adaptability of VFMs without requiring further fine-tuning. To achieve this, we propose a data-free meta-learning framework named LoRA Recycle, which distills a meta-LoRA from diverse pre-tuned LoRAs using synthetic data generated via LoRA Inversion. The VFM, once equipped with the meta-LoRA, is empowered to solve new few-shot tasks in a single forward pass without further fine-tuning, akin to the in-context learning of LLMs. To further enhance efficiency, we propose a double-efficient mechanism that uses only the foreground patches and prunes background patches in the synthetic data, significantly accelerating the meta-training process while maintaining or even improving performance. Comprehensive experiments across eight datasets within both in- and cross-domain scenarios verify the superiority of our framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed to reuse of pre-tuned LoRA techniques without the accessibility to the private data. This proposed method aims to improve the few-shot adaptability of VFMs without further fine-tuning and proposes a new data-free meta-learning framework. The experimental results on 8 datasets show the proposed method exceeds the existing literature.

### Strengths
1. Outstanding work on accelerating the meta-training process.
2. Efficient data synthesis with token pruning and meta-training with sparse tokens do a great job helping the generating and meta-learning process.

### Weaknesses
1. Based on the Lora market, this paper doesn’t get enough contribution to the pretrained Lora reusing method. The meta-learning is widely used in generalization problems, including zero-shot or few-shot learning tasks. The major contribution is not thus interesting to me.
2. Sparse tokens may break the potential correlation between foreground objects and background, this paper can’t simply think highly of this method without eliminating this potential adverse effect.
3. The token pruning in the data-efficient mechanism can also be found in other lightweight designs. Besides, I hope the authors highlight why this method is distinctive, especially when we only have generated data but not customized private data. In other words, what is the key relationship between them?
4. Several presentations are not clear or with several typos. e.g., Line 074, LoRs should be LoRAs.

### Questions
Please refer to the weakness section, my major concerns exist in the main contribution. The proposed techniques can be also widely found in other computer vision or LoRA architecture-designed papers. The authors should clearly claim why these proposed ideas contribute to this community. 

The other major concern is about the relationship between this setting and cross-domain generalization. I wonder how the domain generalization method performs on this task. It seems these method could also focuses on the metra-learning techniques.

Besides, the usage of synthetic datasets could also show a clear upper bound. Thus the authors should discuss this and the relationship between using sufficient private datasets. Or in several extreme cases, what would happen, if there were several few-shot samples available? Is there a trade-off in these application scenarios?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of reusing existing LoRAs for adapting a new VFMs to few-shot tasks without the need of original data or tuning. To achieve this, the authors propose data-free meta-learning framework. By distilling a meta-LoRA using synthetic data from LoRA Inversion, the framework enables VFMs to perform few-shot tasks in a single pass, similar to in-context learning in LLMs. Additionally, a double-efficient mechanism accelerates meta-training by focusing on foreground patches, enhancing both speed and performance. Extensive evaluations across several datasets demonstrate the framework’s effectiveness in both in-domain and cross-domain scenarios.

### Strengths
1. This work introduces an interesting task to explore the potential of reusing diverse pre-tuned LoRAs, expanding the utility of these modules beyond traditional task-specific applications. 
2. The paper is well written and easy to follow.
3. The proposed method performs well on several datasets.

### Weaknesses
1. Related Work: The paper lacks a thorough discussion on data-free knowledge distillation.

2. Limited Novelty: While the paper attempts to tackle a novel and interesting problem, the techniques employed to address it appear somewhat basic and lack innovation. The authors suggest inverting LoRA to obtain synthetic data, a standard approach commonly used in data-free KD literature. Additionally, the model training relies on basic meta-learning methods combined with ProtoNet, a technique widely applied in few-shot learning research. There does not appear to be any unique techniques specifically proposed for LoRA recycling. Furthermore, it seems plausible that this approach could be generalized to recycle various models, not just LoRA, without significant modification to the methodology. This raises questions about the uniqueness and specificity of the proposed solution. The authors could refer to the paper for a similar method: https://arxiv.org/pdf/2110.04545.

3. Limited Evaluation: The evaluation uses relatively simple, toy datasets, which may not fully showcase the robustness or generalizability of the proposed approach. To strengthen the evaluation, I recommend including more challenging datasets, such as WILDS or DomainNet, which could better test the model's performance in diverse, real-world scenarios.

4. Ablation Study: The necessity of meta-learning is unclear. An ablation study focusing on the role of meta-learning would provide valuable insights into its contribution and justify its inclusion in the model.

### Questions
1. Patch Masking vs. Token Reduction: Why is masking patches chosen over reducing the number of tokens in synthetic data generation? An explanation of the design choice here could clarify its benefits and relevance to the overall model.

2. Typo: Line 090L has a typo: "re-quiring" should be corrected to "requiring."

### Soundness
3

### Presentation
3

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
This paper addresses the challenge of extra costs and limited resources when adapting large-scale visual models to different domains, focusing on classification. The proposed method employs meta-learning to develop a meta-LoRA capable of performing classification in a single forward pass. The authors validate their approach through experiments on several datasets in a few-shot setting.

### Strengths
1. The idea of distilling knowledge from various pre-finetuned LoRAs to achieve generalized understanding without requiring access to the original datasets is intriguing.
2. The authors provide clear explanations of their methods, making the paper easy to follow.

### Weaknesses
1. The generalizability of the proposed method is questionable, as the experiments were conducted on only eight small datasets. While out-of-domain experiments were performed, the results on the ISIC and CHESTX-RAY datasets were unsatisfactory, possibly due to limited category diversity. The datasets used for evaluation, while diverse in content, lack the scale and complexity of real-world applications, raising concerns about the method's robustness in more challenging scenarios. Specifically, the limited number of classes within each dataset may not fully capture the intricacies of more complex classification tasks, potentially leading to an overestimation of the method's performance.
2. Although the motivation for the proposed method is compelling, the authors did not utilize a wide range of pre-finetuned LoRAs from the community. Instead, they constructed datasets from existing ones, which is not entirely convincing. The creation of LoRAs from existing datasets, while practical, may introduce biases or limitations that are not representative of the broader spectrum of pre-trained models available. This approach could restrict the diversity of knowledge encoded within the meta-LoRA, potentially hindering its ability to generalize to unseen domains.
3. More comparative methods should be included, such as CooP, CoCOOP, and PromptSRC, to provide a more comprehensive evaluation. The absence of comparisons with these established methods makes it difficult to assess the relative strengths and weaknesses of the proposed approach. These methods, which leverage prompt engineering and contextual learning, offer alternative strategies for few-shot classification and should be included to provide a more complete picture of the current state-of-the-art.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
Vision foundation models often require fine-tuning with large data to perform well on a few shot tasks. Develop a real-time few-shot system with minimal data in real-time. Existing LoRA techniques require fine-tuning, which makes them unsuitable for real-time response, and a large training dataset causes instability at a small scale.
The work proposes: "data free" recycling existing LoRA modules to achieve impressive few-shot performance.

### Strengths
1.	Paper is written in easy to understand manner. 

2.	The 5-way 1-shot accuracy improvement is impressive, thus proving the proposed methods utility. 

3.	Visualization provided makes understanding synthetic dataset easy. Figure 2 and Figure 3 is really well made, makes understanding paper easy. 

4.	Masking images as a means of computation efficiency is an interesting idea. As well as using the self-attention weights for pruning tokens is interesting too.

### Weaknesses
1.	**Mentioning terms without definition**, [LINE 023] “meta-LoRA” [Line 024] “LoRA Inversion”. Maybe make them italics to show emphasis as a standard procedure. 

2. When comparing with existing methods, **missing work** include  
a.	*fine-tuning  “Visual prompt tuning”* (Jia, Menglin, et al. "Visual prompt tuning." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022).  
b.	*LoRA “The Balanced-Pairwise-Affinities Feature Transform”* (Shalam, Daniel, and Simon Korman. "The Balanced-Pairwise-Affinities Feature Transform." Forty-first International Conference on Machine Learning (2024).)   
c. *Efficinet technique like Test-time prompt tuning*  (Shu, Manli, et al. "Test-time prompt tuning for zero-shot generalization in vision-language models." Advances in Neural Information Processing Systems 35 (2022): 14274-14289)  


3. **Results looks unconvincing**. Take the baselines, “LoRAHub” “MOLE” and “LoRAs Avg + Linear” their “5-way 5-shot” performance is similar to “LoRA Recycle” (inferior by 1%). These baselines are far more computationally efficient (no synthetic dataset generation and no distillation), yet give comparable performance. While LoRA Recycle performs well in the “5-way 1-shot” setting, the method doesn’t seem to highlight any special technique/method that helps in this particular result. It appears to be an unintentional benefit of the proposed method. This is more prominent in cross-domain results (Table 3). 

4. **Key Motivations are missing**:   
(a)	Why are the authors using synthetic data (“Data-free” & “avoids additional data collection”)? What’s the motivation behind it? What happens if the model uses any standard dataset like “MiniImageNet” on which these LoRA(s) are already pre-trained on (in-domain)  
(b) **Line [045] “leads to significant time overheads and increased memory usage.”** Generating synthetic dataset has a significant computation / time overhead as well. How is using synthetic dataset a better alternative than using a large scale dataset like Laion-2b as unsed in CAML? If It were to assume, synthetic images are noisy making them sparse (removing tokens) would reduce the noise and improve performance as observed in the ablation.  
(c) What's the motivation behind using LoRAs? Other methods like prompt tunning, test time augmentation, etc. are not beneficial. The technique doesn’t compare these methodologies and determining the utility of LoRAs in isolation is difficult and not well-motivated.  
(d) [Line 084] “parameter-lightweight” and “computation-efficient” [Line 085]? This approach is not lightweight, as it needs to account for the “trainable pixels” that need to be trained during LoRA inversion for generating a synthetic dataset thereby giving it a data-free status.  
(e)	[Line 086] “architecture agnostic, enabling to recycle LoRAs with heterogeneous architectures like different ranks, as a distinct advantage over existing methods.” Is it? The synthetic dataset is generated based on a gradient from VFMs. The proposed solution is based on the choice VFM. if this is still considered as architecture agnostic, most existing fine-tuning techniques like adapters and promotes are architectural agnostic.

5. **Key solutions are not solving the motivation**: The solution is to propose a real-time fine-tuning module for few-shot learning.   
(a) *Generating synthetic* data solves the data-free problem? Ablation needs to show what happens if the standard dataset like Laion-2b is used to motivate the use of synthetic dataset (and answer the data-free problem)   
(b) *Training in retrieval-based technique* (Line[228]  Synthetic few-shot task construction): Are authors claiming retrieval-based techniques help in Line[036] "few-shot tasks without the necessity for fine-tuning,"

### Questions
Please address all the weakness mentioned above

### Soundness
2

### Presentation
3

### Contribution
2

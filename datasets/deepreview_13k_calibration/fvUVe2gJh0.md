# What Matters for Model Merging at Scale?

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Model merging aims to combine multiple expert models into a more capable single model, offering benefits such as reduced storage and serving costs, improved generalization, and support for decentralized model development. 
Despite its promise, previous studies have primarily focused on merging a few small models. This leaves many unanswered questions about the effect of scaling model size and how it interplays with other key factors---like the base model quality and number of expert models---, to affect the merged model's performance.
This work systematically evaluates the utility of model merging at scale, examining the impact of these different factors. We experiment with merging fully fine-tuned models using four popular merging methods---$\mathtt{Averaging}$, $\mathtt{Task~Arithmetic}$, $\mathtt{Dare}$-$\mathtt{TIES}$, and $\mathtt{TIES}$-$\mathtt{Merging}$---across model sizes ranging from $\mathtt{1B}$ to $\mathtt{64B}$ parameters and merging up to $\mathtt{8}$ different expert models. We evaluate the merged models on both held-in tasks, i.e., the expert's training tasks, and zero-shot generalization to unseen held-out tasks.
Our wide range of experiments provide several new insights about model merging at scale and the interplay between different factors. \underline{\textit{First}}, we find that merging is more effective when experts are created from strong base models, i.e., models with good zero-shot performance, compared to pre-trained ones. \underline{\textit{Second}}, larger models facilitate easier merging.
\underline{\textit{Third}} merging consistently improves generalization capabilities. Notably, when merging eight large expert models, the merged models often generalize better compared to the multitask trained models. \underline{\textit{Fourth}}, we can better merge more expert models when working with larger models. \underline{\textit{Fifth}}, different merging methods behave very similarly at larger scales. 
Overall, our findings shed light on some interesting properties of model merging while also highlighting some limitations. We hope that this study will serve as a reference point on large-scale merging for upcoming research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper systematically analyzes the impact of different model sizes, base model quality, model merging methods, and the number of expert models on the effectiveness of model merging, and draws five key conclusions. In general, this paper is of certain significance to the model merging community.

### Strengths
- This paper systematically reveals the impact of different model sizes, quality, quantity, and merging methods on the effectiveness of model merging.
- The figures and tables in this paper are very clear.
- This paper is well organized and clearly written.

### Weaknesses
 - Some inconsistencies lack explanation:
    - (1) In Figure 1, why is multi-tasking better than single-tasking in 8B and 24B, but multi-tasking is not better than single-tasking in 1B and 64B? How does this relate to model size?
    - (2) In Figure 5 (PaLM-2-24B, PaLM-2-64B), why is the generalization performance when the number of experts is 8 not as good as when the number of experts is 6? Why does the TIES method perform worse than the pre-trained model when the number of experts increases in PaLM-2-24B?
    - (3) In Figure 6, under PaLM-2-Held-Out, 64B is significantly better than 24B. Why is 64B not as good as 24B under PaLM-2-IT-Held-Out.
    - (4) In Figure 7, why is the performance of merging 8 experts better than merging 4 and 6 experts under the Held-In-64B setting? The greater the number of tasks, shouldn't task conflicts be more serious?
- There is a lack of outlook or suggestions for future directions based on the phenomena observed in this paper.
- Lack of source code and checkpoints. As this is an evaluation paper, the author can consider open-sourcing the resources used in the paper to facilitate further reproduction and research by the model merging community.
- The author can consider adding discussions of the following related work.
    - Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities. Arxiv, 2024.
    - Fine-tuning large language models for domain adaptation: Exploration of training strategies, scaling, model merging and synergistic capabilities. Arxiv, 2024.
    - FusionBench: A Comprehensive Benchmark of Deep Model Fusion. Arxiv, 2024.
    - Arcee's MergeKit: A Toolkit for Merging Large Language Models. Arxiv, 2024.
- Some minor errors:
    - References are repeated, "Language models are super mario" appears twice, "Extend model merging from fine-tuned" appears three times, and "Model ratatouille" appears twice. The author needs to check carefully whether other references are repeated.
    - Reference year error: Ties-merging was published in NeurIPS 2023 instead of 2024. Similarly, "Task arithmetic in the tangent Space" was also published in NeurIPS 2023 instead of 2024. The author needs to check the year of other references.

### Questions
Please refer to the Weaknesses section

### Soundness
3

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
This is an empirical study paper that answers questions for model merging. The author explores research questions about model merging. 

- What is the effect of using pretrained vs. instruction-tuned base models for creating expert models for merging?
The instruction-tuned base models outperform the pretrained models in the merging process.
- Does model merging become easier or harder as the model size increases?
Larger models consistently showed better performance in merging, indicating that they are easier to merge effectively.
- How does merging affect zero-shot generalization to held-out (not seen) tasks, and how is this influenced by model size?
Those based on larger and instruction-tuned base models, has improved zero-shot generalization ability. Sometimes surpassing multitask baselines.
- How many expert models can be merged without performance loss, and how does this depend on model size?
Larger models could effectively merge more expert models without significant performance degradation, whereas smaller models experienced performance drops when merging more experts.

### Strengths
- This is a comprehensive evaluation, systematically examines multiple factors (model size, base model quality, number of experts, and merging methods) across a large-scale experimental setup, providing robust insights.

### Weaknesses
 - It seems when comparing merging pretrained "experts" and finetuned "experts", after the merging process, the pretrained one is never finetuned. I think it might be unfair to compare between a never finetuned checkpoints and a finetuned checkpoints (althrough it is a merged checkpoint). And thus, it is very natural to predict that merging finetuned "experts" is better than merging pretrained "experts".
- All the tasks (held-in and held-out) are text based. It would be better if involving some vision based tasks.
- The smallest model is 1B. It is small for text models but probably still fairly large for vision models.
- If adding vision tasks, it would be great to check both vision transformer based models and resnet based models.
- Besides, I am also wondering if the way of training the "expert" matters. e.g. Zero-shot contrastive loss for classification vs supervised learning for classification.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focused on the model merging issue, exploring various dimensions including model sizes (1B-64B parameters), merging techniques (Averaging, Task Arithmetic, TIES-Merging, Dare-TIES), and the number of expert models (up to 8). The evaluation covers both the tasks the experts were trained on (held-in tasks) and unseen tasks (zero-shot generalization).
  Different with previous studies for small model scales, the study extended the exploration to the effect of scaling model size, as well as the base model quality and number of expert models.
  Key findings include: (1) Merging is more effective when using strong instruction - tuned base models compared to pretrained ones. (2) Larger models are easier to merge. (3) Merging improves generalization capabilities, and with strong base models and increasing numbers of merged experts, the merged model can outperform multitask trained models. (4) Larger models can merge more expert models effectively.

### Strengths
1. The objective of this study is to offer profound insights regarding the scalability aspect of model merging, which indeed represents a significant direction within the realm of "scaling".
2. The research presented herein exhibits a comprehensive and meticulous experimental design, which encompasses multiple dimensions such as model sizes, merging methods, and the count of experts. The results are presented in a highly satisfactory manner. Through a sequence of well-conducted experiments, it has been clearly demonstrated that the merged model can effectively harness the diverse expert knowledge. This beneficial effect becomes more pronounced with the increase in model size and when instruction-tuned base models are utilized.
3. The paper is generally well-written and easy to follow.

### Weaknesses
1. The fact that the study's exclusive concentration lies on PaLM-based models does give rise to legitimate concerns regarding the generalizability of the findings to other architectural frameworks such as GPT, LLaMA, and Qwen. The paper lacks sufficient justification for why the observed trends should hold across diverse model architectures, especially given the known differences in pre-training methodologies and architectural nuances between these models. For example, the attention mechanisms, normalization layers, and even the specific tokenization approaches can vary significantly, potentially impacting the merging process.
2. Incomplete theoretical exploration: The paper is heavily empirical, lacking necessary theoretical analysis to explain the observed phenomena. For example, the relationship between weight disentanglement and merging effectiveness is not explored, nor is there any discussion on the loss landscape of merged models and how it relates to the individual expert models. The paper does not delve into the underlying mechanisms that cause some merging techniques to be more effective than others, or why larger models seem to merge more effectively. A deeper theoretical analysis could provide a more robust understanding of the observed trends.
3. Constraints in Experimental Design:The experimental design of the paper is primarily focused on a narrow range of model sizes (1B to 64B parameters) and a limited number of expert models (up to 8). This limited scope raises questions about the scalability of the findings to even larger models and a greater number of experts. The paper does not explore the potential for diminishing returns or even negative interference when merging a significantly larger number of models, which is a critical aspect for practical applications.

### Questions
1. What are the theoretical and practical implications that arise when the merging process extends beyond involving 8 experts? Additionally, does there exist an anticipated performance ceiling in such a context? 
2. It is of great significance to explore the following aspects: Firstly, how could the findings obtained from the current study be extrapolated and applied to other model architectures? Secondly, which specific architectural features might exert an impact on the performance of the merging process? 
3. In Section 4.3, a pertinent query arises regarding the strength of the multitask baseline. Specifically, one might question whether the multitask baseline is overly potent. For example, in the context of 6-expert merging, should the baseline be trained solely on those specific 6 tasks rather than on a combination of all 8 tasks?

### Soundness
3

### Presentation
3

### Contribution
2

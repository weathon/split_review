# C-CLIP: Multimodal Continual Learning for Vision-Language Model

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Multimodal pre-trained models like CLIP need large image-text pairs for training but often struggle with domain-specific tasks. Since retraining with specialized and historical data incurs significant memory and time costs, it is important to continually learn new domains in the open world while preserving original performance. However, current continual learning research mainly focuses on single-modal scenarios, and the evaluation criteria are insufficient without considering image-text matching performance and the forgetting of zero-shot performance. This work introduces image-caption datasets from various domains and establishes a multimodal vision-language continual learning benchmark. Then, a novel framework named C-CLIP is proposed, which not only prevents forgetting but also enhances new task learning impressively. Comprehensive experiments demonstrate that our method has strong continual learning ability across different domain image-text datasets, and has little forgetting of the original capabilities of zero-shot prediction,  significantly outperforming existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Brief Summary: The paper tackles the task of continual learning for a VLM. In particular, the authors introduce new datasets from image captioning datasets (coco, flickr30k) and the model is evaluated on a range of vision-language datasets on retrieval and zero-shot classification tasks. 

The key idea here is that the authors show that LoRA (low rank adaptation) achieves a similar effect as storing and replaying old data. Further, that contrastive learning loss reduces forgetting. 

Experiments on a number of datasets show that the proposed method (C-CLIP) trained can match or exceed full-finetuning results. Moreover, C-CLIP outperforms existing baselines by significant margins.

### Strengths
Pros:

1. The key idea of using LoRA as a replacement for memory bank and adding contrastive learning is easy to implement and is modular. As a result, it is promising that such method can be used to enable continual learning across a range of VLM models. 

2. The authors contribute dataset and benchmarks. The performance improvement over competitive baselines is very significant (in range of 7-10 points). 

3. The authors provide comprehensive set of experiments across multiple datasets and multiple baselines. The ablation study is also solid, particularly interesting is that Contrastive Loss (CKC) by itself provides significant improvement on its own (Table 4).

4. The authors provide qualitative results visualizing their model (in appendix)

### Weaknesses
Cons:

1. The authors should also show results with more multi-modal models and not just CLIP ViT-B/16, such as other CLIP variants with different backbones (say ViT-L/14). It is important to evaluate the method's robustness across different model capacities and architectures. The current evaluation is limited to a single CLIP variant, which might not generalize well to other models with different embedding spaces and pre-training procedures. For example, larger models like ViT-L/14 might exhibit different forgetting patterns or require different hyperparameter tuning for optimal performance with the proposed method.

2. The authors could also explore more vision-language tasks, in particular that of captioning/description with generative VLMs which output a description (such as LLaVA). The current evaluation focuses on retrieval and zero-shot classification, which are discriminative tasks. It is crucial to assess the method's applicability to generative tasks like captioning, where the model needs to generate coherent and contextually relevant text. Generative tasks are more sensitive to subtle changes in the model's parameters and might reveal different limitations of the proposed continual learning approach.

3.  (Minor) The authors have missed a close work [Ref1] which also explores the setting of multi-modal VLMs in continual learning setting. That said, the main contributions on modeling side are quite different.

### Questions
Q1. It is a bit unclear to me if the model is provided the task id in the data-stream. For instance, during training does it know that the task is say pet-classification or is that information hidden.

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
3

### Summary
This paper presents C-CLIP, a new continual learning framework that aims to reduce the forgetting in Vision-Language Models (VLMs) while achieving high fine tuning accuracy on new datasets, specifically focused on CLIP. The authors also introduce a benchmark for Vision-Languge Continual Learning to evaluate CLIP’s performance in retaining zero-shot capabilities while acquiring new domain knowledge. To achieve that goal, C-CLIP combines Low-Rank Adaptation (LoRA) to reduce forgetting and Contrastive Knowledge Consolidation (CKC) to retain old knowledge. Experiments show that C-CLIP achieves high accuracy in downstream tasks while maintaining zero-shot classification performance across different domains.

### Strengths
The paper shows an innovative approach to continual learning within Vision-Language models, by focusing on the adaptation of new domains while retaining the zero-shot capabilities, with some key strengths:
- The integration of LoRA adapters and CKC is a good approach to achieving robust continual learning in VLMs, especifically capable of retaining zero-shot capabilities
- Experiments are performed with evaluations across a wide range of both seen and unseen domains, which highlight the method's effectiveness in preventing catastrophic forgetting.
- C-CLIP advantages against other CL methods are clearly demonstrated through detailed figures and tables, facilitating the understanding of the experimental results.
- A method that uses a Vision-Language model like CLIP in multimodal settings is highly relevant given the actual trend of focusing just on unimodal CL scenarios.

### Weaknesses
The paper also shows some weaknesses that could improve the overall result:
- While LoRA reduces significantly trainable parameters, it would be interesting and beneficial to include an analysis of the computational costs involved in using CKC during the fine tuning process.
- Although comparisons are made against baseline and some recent CL approaches, there is no comparison against other well known parameter efficient CL methods (e.g., DualPrompt, CPE-CLIP, Learning to Prompt, etc) that could strengthen the evaluation.

### Questions
- Could the C-CLIP approach be generalized to VLMs beyond CLIP, or are specific adjustments required?
- Could the authors further elaborate on why CKC avoids the trade-offs associated with other regularization methods?

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
- This paper addresses continual learning scenarios for vision-language models, focusing on cross-modal retrieval across seen and unseen datasets.
- The proposed approach combines two key components: (1) low-rank adaptation (LoRA) training with theoretical analysis of its connection to continual learning objectives, and (2) contrastive knowledge consolidation (CKC), which distills knowledge from previous task models as an auxiliary loss.
- Experimental analysis is conducted with nine vision-language datasets, including one unseen dataset, where the proposed C-CLIP consistently outperforms competitive baselines. Additional experiments on zero-shot image classification and ablation studies further validate the method's effectiveness.

### Strengths
- The application of continual learning to vision-language scenarios addresses important practical needs.
- The proposed method effectively combines LoRA with knowledge distillation for vision-language continual learning, which sounds reasonable and is supported by theoretical analysis.
- The paper presents strong experimental results across a comprehensive range of benchmarks, demonstrating consistent performance improvements over baselines and thorough evaluation across different experimental setups.

### Weaknesses
 - Delivery should be significantly improved. Here is a non-exhaustive list I have identified while reading the paper, but I believe there are plenty of points that need to be improved:
	- What CIL and MTIL stands for? (I don't find Table 1 to be really necessary, though.)
	- Figure 2 does not effectively convey what CKC is about.
	- The range covered by the y-axis in Figure 3-(c) seems too wide, making it hard to see what is happening locally. Consider normalizing and clamping. Also, it would be interesting to see if such a behavior, i.e., alignment in main and auxiliary losses, is universally observed in other tasks.
	- What does Figure 3 in L284 refer to?
	- Please assign proper variables for equation 5 and 6, instead of using $z$ everywhere. This makes the equations somewhat confounding, e.g., substituting $t$ in  $\tilde{z}_i^t$ with $t-1$ is not identical to $\tilde{z}_i^{t-1}$, etc.
	- Many typos, e.g., space is view as (L280), loss is use in the (L294), etc.
- While performance improvements in all major experiments are impressive (compared to performance gap among prior arts), it is hard to tell whether these results are reproducible and rigorously analyzed.
	- The codes are not provided, and the details in the paper may not be sufficient to fully reproduce the experiments reported.
	- Some important hyperparameters are not tested properly, e.g., $\alpha$ for LoRA integration, ratio of CKC loss and CLIP loss, etc. The performance gaps in Table 4 for each row is quite large, making it hard to understand at which point these improvements emerge.
	- Only a subset of tasks are reported in major figures, e.g., Figure 3, 4, 6, 7 and Table 4, 5. It would be beneficial to see if a similar tendency holds for the rest of the tasks during training end-to-end (at least for some crucial setups like ablation studies).
- Distillation in continual learning is not new, which was addressed in Contrastive Continual Learning (ICCV 2021) to the best of my knowledge. It would be necessary to provide some theoretical or empirical comparison between CKC and previous lines of work leveraging similar concepts.

### Questions
Please refer to the weaknesses section for major questions. Here are some minor comments about the paper:
- Eq. 23 is recursive with respect to K, could this bound serve as a meaningful bound? (could be considerably large for some nontrivial L and M?)
- L96 - cite correct paper (pioneering works, not recent ones)
- Is $h_\psi$ in L277 used elsewhere after training? Why is an identical projector used for both vision and text embeddings in equation 5?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a rich benchmark for general vision-language continual learning focused on evaluating performance degradation in zero-shot generalization as well as class-incremental performance. The paper also introduces a modified CLIP model to account for some limitations of similar models in the literature. The proposed model, C-CLIP, uses LoRA adaptation and Contrastive Knowledge Consolidation as the two main advancements of the standard CLIP backbone. The proposed model outperforms current SOTA models in preserving knowledge and zero-shot performance degradation.

### Strengths
Overall, I positively evaluate the proposed manuscript. I like the idea of proposing a complete evaluation benchmark encompassing several strategies for measuring zero-shot generalization capabilities in continual learning settings. The benchmark is rich enough to increase the challenge that continual learning literature normally faces when proposing novel models evaluated on limited and strict benchmark datasets.

### Weaknesses
(1) The introduction needs a significant extension. Authors keep claiming that vision-language continual learning is under-explored, but they missed relevant research papers. Some examples are:

- Qian et al (2023). Decouple before interact: Multi-modal prompt learning for continual visual question-answering
- Wang et al (2021). Continual learning in cross-modal retrieval
- D'Alessandro et al (2023). Multimodal Parameter-Efficient Few-Shot Class Incremental Learning
- Srinivasan et al (2022). Climb: A continual learning benchmark for vision-and-language tasks

just to name a few. I would also mention the general literature in FSCIL (Few-Shot Class-Incremental Learning) as well. All these works challenge vision-language continual learning from different perspectives and provide insightful feedback on specific problems encountered in multimodal settings. Furthermore, contrastive learning pre-training offers more nuances compared to a standard unimodal continual learning scenario, since it can solve image classification as well as pure multimodal tasks, as mentioned in the main paper. But it's clear that the burden of solving forgetting and adaptability problems is totally different in the two tasks, since in the former the language encoder needs to perform representational learning only on fixed text labels to pair with images. This consideration comes directly when considering the papers already mentioned in the current introduction and the ones I mentioned before. The proposed one is a comprehensive benchmark, but the introduction needs to clarify these concepts.

(2) I think the overall benchmark definition is confused and badly explained. First of all, the authors want to clarify the role of each benchmark evaluation aspect. Some datasets are used in a continual learning fashion, with incremental experiences, others are used without the temporal factor, and you have to reach section 5.2 to figure it out. This is a benchmark that, I assume, the authors want to propose to unify evaluation criteria across VL CL models. I suggest putting a section in the main text (a table if it is necessary) clarifying how the benchmark is made, by referring to the continual learning datasets stats (e.g. number of splits, classes per split) and datasets role (e.g. continual learning, zero-shot generalization not in continual learning scenario). If there are space issues, I think there are sections that can be sacrificed since clarifying the benchmark is crucial (e.g. "Theoretical Analysis" section can be safely moved into the appendix).

(3) Since the proposed model uses a parameter-efficient strategy, I think it's worth mentioning the whole corpus of rehearsal-free continual learning methods based on parameter-efficient tuning (e.g. prompt tuning, prefix tuning) other than standard methods like regularization-, architecture-, and replay-based ones.

(4) Is the CLIP (first line) in Table 2 fine-tuned or just frozen? In Figure 3 there is a reference to "Fine-Tune" so I guess it's fine-tuned CLIP. If this is the case, why not add frozen CLIP in all the model comparisons as a baseline? It can be helpful to verify if pre-training alone is enough to ensure an acceptable generalization and performance degradation.

(5) Line 232. "the model has no access to the task identity". It's ok but please state from the beginning that we are in a class-incremental learning scenario and thus that the benchmark is for CIL, as usual in any CL paper.

(6) Line 255. "leran" -> "learn".

(7) "single-modal scenario" is an unpopular term. I think the literature agrees with using the term "unimodal" instead.

### Questions
I think that LoRA can be compared with other parameter-efficient methods that keep the main backbone frozen like prompt-tuning (e.g. Khattak et al (2022). MaPLe: Multi-modal Prompt Learning), unless there is a particular reason with a mathematical justification for keeping LoRA. But in my opinion, eq. 4 holds with any other non-adapters parameter-efficient methods, and CKC is not constrained by the backbone adaptation. I understand that the authors might complain that LoRA is just a design choice, as any other else, but the paper lacks a clear justification for that since eq. 2 and eq. 4 hold for prompt-tuning too, and the intention here seems just preserving knowledge by freezing the backbone. CKC seems a clearer design choice on the other hand. 

Do you agree with this view, or am I missing something and maybe LoRA is already justified so there is no need to explore other parameter-efficient methods?

### Soundness
3

### Presentation
4

### Contribution
3

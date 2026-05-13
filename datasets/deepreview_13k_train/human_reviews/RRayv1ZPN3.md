# TAIL: Task-specific Adapters for Imitation Learning with Large Pretrained Models

- Decision: Accept
- Scores: 6, 6, 5, 6, 8

## Abstract
The full potential of large pretrained models remains largely untapped in control domains like robotics. 
This is mainly due to data scarcity and computational challenges associated with training or fine-tuning large models for such applications. 
Prior work mainly emphasizes either effective \emph{pretraining} of large models for decision-making or \iclrnew{single-task adaptation. But real-world problems will require data-efficient, \emph{continual adaptation} for new control tasks.} 
Recognizing these constraints, we introduce \methodlong, a framework for efficient adaptation to a stream of new control tasks.
Inspired by recent advancements in parameter-efficient fine-tuning in language domains, we explore efficient fine-tuning techniques---e.g., Bottleneck Adapters, P-Tuning, and Low-Rank Adaptation (LoRA)---in \method\ to adapt large pretrained models for new tasks with limited demonstration data. 
Our extensive experiments comparing prevalent parameter-efficient fine-tuning techniques and adaptation baselines suggest that \method\ with LoRA can achieve the best post-adaptation performance with only 1\% of the trainable parameters of full fine-tuning while avoiding catastrophic forgetting and preserving adaptation plasticity in continual learning settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new architecture named TAIL for imitation learning, which effectively adapts large pretrained models to new tasks with limited demonstration data. The main contribution of this method is to effectively incorporate lightweight adapter modules into pretrained models using various integration techniques, including parallel integration (with LoRA weights), sequential integration (Bottleneck Adapter), and prefix token integration. 

The paper provides a comprehensive comparison of these adaptation techniques on the LIBERO robotic manipulation continual learning benchmark. The results indicate that TAIL, particularly when utilizing LoRA integration, outperforms the compared methods in terms of both forward and backward transfer.

Overall, while this paper may not introduce strong technical novelty, it offers a good empirical study of lightweight continual learning techniques for imitation learning of robot control tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper includes sufficient experiments on the LIBERO benchmark, which can effectively demonstrate the advantages of employing TAIL in conjunction with the LoRA integration technique.
3. The proposed TAIL-based methods greatly outperform the conventional fine-tuning method in both forward transfer results and adaptation efficiency.

### Weaknesses
1. My primary concern is the technical novelty of this paper, although I acknowledge the significance of benchmarking and conducting an extensive empirical investigation of existing parameter-efficient fine-tuning techniques. The proposed TAIL framework, which incorporates lightweight adapters and task-specific heads, shares similarities with existing methods in continual learning and multi-task learning, as demonstrated in the paper from Rebuffi et al. (2017) titled 'Efficient Parametrization of Multi-Domain Deep Neural Networks.' Although TAIL introduces a new multi-modal, Transformer-based architecture, the core idea bears a strong resemblance to prior work. Specifically, the use of separate adapter modules for each task, while effective, is not a novel contribution and has been explored in various forms in prior literature on multi-task and continual learning. The paper lacks a detailed discussion of how TAIL's specific adapter integration techniques (LoRA, Bottleneck Adapter, Prefix Token) differ fundamentally from existing adapter-based methods, beyond the specific architecture they are applied to.
2. In Figure 4, the authors primarily compare various design choices within the TAIL framework when presenting forward adaptation results. It would be valuable if the authors could extend this analysis to include a comparison of TAIL's best performance with the state of the art in lifelong imitation learning. Furthermore, in Table 1, the comparison of TAIL's forward transfer performance with previous continual learning methods may not be fair enough. This is because EWC and ER primarily address catastrophic forgetting and may not contain task-specific model parameters. The paper does not adequately address the potential for task interference when using a shared base model, even with task-specific adapters. A more thorough analysis of how TAIL mitigates negative transfer, beyond simply demonstrating positive forward transfer, would strengthen the paper.
3. In Figure 5, a comparison between TAIL and EWC/ER may not be entirely equitable, considering that these prior methods do not assume known task IDs or retain task-specific model parameters. I would like to suggest the authors include a comparison with multi-task learning methods for a more comprehensive evaluation. The comparison should include methods that explicitly learn a shared representation across tasks, as this would provide a more robust benchmark for evaluating the effectiveness of TAIL's task-specific adapters. Furthermore, the paper should clarify whether the task IDs are used only to select the appropriate adapter or if they are also used in the training process itself, as this could impact the fairness of the comparison.

### Questions
1. Is a separate adapter $\omega_k$ trained for each task suite? My understanding is that when re-evaluating previous task suites $j$, the previously trained adapter $\omega_j$ is reloaded instead of testing the previous task on the adapter $\omega_k$ trained for the current task $k$. 
2. In Figure 4, it would be insightful to determine whether combining all integration techniques, including LoRA, Bottleneck Adapter, and Prefix Token, would yield further performance improvements.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the continual imitation learning setting where a stream of tasks arrive one at a time. Existing methods are susceptible to catastrophic forgetting or loss of model plasticity as the number of tasks increase. Consequently, the paper proposes task-specific adapters for imitation learning (TAIL), a method that uses additional per-task tuneable parameters and synthesizes them to the pretrained base model's parameters. The paper demonstrates through experiments that TAIL introduces little computational overhead and mitigates catastrophic forgetting and model plasticity problems.

### Strengths
- The paper is easy to follow generally.
- The method is very intuitive and simple---the fact that the overhead is low for a new task while mitigating catastrophic forgetting (e.g. better than experience replay) is appealing.
- The empirical analysis demonstrates that using TAIL with low-rank adaptation (LoRA) perform better than existing baselines convincingly in LIBERO, interestingly that it performs that well with rank $r = 8$.

### Weaknesses
 
**Comments**
- It appears that the number of tasks can easily explode over time since each task instruction (and initial-state distribution) corresponds to a new task. A natural extension will be to mitigate the amount of adapters based on the similarity of task instructions, as hinted in appendix. This is a critical practical concern, as the memory footprint will scale linearly with the number of distinct task instructions if not addressed.
- Since the problem setting indicates that a task definition is not w.r.t. the state-action space, it will be more convincing if there are experiments conducted on cross-embodiment (e.g. different arms or same arm with different inertial properties.) This is important to demonstrate the generalizability of the approach beyond the specific embodiment used for pre-training.
- The evaluation metric is unclear---in particular under BWT, the equation seems to be different from what is described---should the *best FWT model* be the best $F_i$ for task $i$ after seeing $k$ tasks? The current description lacks clarity on how the best FWT model is selected for each task, and how this selection affects the BWT calculation.
- For the 10 validation episodes, I believe it has been shown multiple times that validation error does not necessarily correspond to success rates [1, 2, 3]---a model may achieve high validation error while still achieving high success rate. The use of validation error as a proxy for performance is questionable, and it would be more convincing to directly evaluate performance using success rates.
- Regarding success rates, what are the baseline performances? That is, what is the success rate of the expert demonstrations? Do we expect the policy that trains purely using the task-specific data to perform better than the models in Figures 5 and 6? How would a random policy perform? Without these baselines, it is difficult to assess the absolute performance of the proposed method, and whether it is truly learning from the demonstrations or simply overfitting to the training data.

**References**
[1]: Hussenot, L., Andrychowicz, M., Vincent, D., Dadashi, R., Raichuk, A., Ramos, S., ... & Pietquin, O. (2021, July). Hyperparameter selection for imitation learning. In International Conference on Machine Learning (pp. 4511-4522). PMLR.  
[2]: Mandlekar, A., Xu, D., Wong, J., Nasiriany, S., Wang, C., Kulkarni, R., ... & Martín-Martín, R. (2021). What matters in learning from offline human demonstrations for robot manipulation. arXiv preprint arXiv:2108.03298.  
[3]: Ablett, T., Chan, B., & Kelly, J. (2023). Learning from Guided Play: Improving Exploration for Adversarial Imitation Learning with Simple Auxiliary Tasks. IEEE Robotics and Automation Letters.

### Questions
- Under subsection **Training, Adaptation, and Evaluation**, what exactly is a validation scene?
- Does ER retrain parameters from scratch, or does it continue training from the current set of parameters? Clearly if it is the latter the model will experience plasticity loss similar to the reinforcement learning setting [1].
- It appears that some tasks are repeated based on appendix. I am wondering if there is any result regarding the per-task success rate. Do we understand whether the parameters are well-adapted to specific tasks, or are they similar in performance?

**Possible typos**
- On page 2, subsection PEFT, line 5: "It is" instead of "it's".

**References**
[1]: Nikishin, E., Schwarzer, M., D’Oro, P., Bacon, P. L., & Courville, A. (2022, June). The primacy bias in deep reinforcement learning. In International conference on machine learning (pp. 16828-16847). PMLR.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the adaptation problem in continual imitation learning and proposes task-specific adapters when fine-tuning the imitation policy to new tasks. Specifically, the task-specific adapter is an add-on to the imitation policy and can be updated for each task without changing the pretrained weights in the backbone policy. As shown by the paper, this adapter can be implemented by three ways: parallel, i.e., Low-Rank Adaptation (LoRA) in this paper, sequential, i.e., Bottleneck Adapter, & prefix token, i.e., prompt-tuning. The paper evaluates the proposed adapter in LIBERO robotic manipulation continual learning benchmark and shows that LoRA adapter performs the best across all tasks.

### Strengths
### Clarity 
The structure and presentation of the paper is of very good quality. The flow of the paper is excellent with a good and appropriate structure. The underlying motivation of studying the task-specific adapters is well justified.

### Weaknesses
### Quality & Contribution
One of the main weaknesses of this paper is the lack of comprehensive empirical analysis over multiple different benchmarks, especially those used by previous baseline methods. Particularly, **the conclusions and empirical insights were drawn only from a single dataset, with no results from any other public datasets**. As the main contribution, this paper shows that the LoRA-type integration of the adapter in continual imitation learning performs the best. The paper thus concludes that they “are contrary to many results from the vision and language model literature which show that full fine-tuning works better”. However, these results are drawn based on LIBERO robotic manipulation continual learning benchmark ONLY. They have not been verified by any other datasets. It is thus unclear if and how the results and conclusions can be generalized to other robot control tasks, e.g., Franka-Kitchen.

Furthermore, it is unclear if the baseline methods have been well tuned for the LIBERO benchmark. For example, the RoboAdapter method may need to tune the adapter locations and different pre-trained representations for its optimal performance. The paper, however, seems to take the default configs, even though those configs were originally proposed for other robot tasks. To have a fair comparison with RoboAdapter, the paper should consider some of datasets used by RoboAdapter paper, i.e., Metaworld, Franka-Kitchen, and RGB-Stacking task suites, replicate the reported performance of RoboAdapter and then demonstrates on at least one of those datasets that the TAIL performs better than RoboAdapter.

### Originality & Significance
The originality of this paper can be limited and incremental.

**In terms of technique**, the adapter idea has been well studied by the RoboAdapter paper, which introduces the adapter layer (Sequential Integration in this paper) to imitation learning and considers its application in robot controls. Though the paper proposes two other adapter mechanisms, LoRA & Prefix prompt tuning, both of them are taken directly from other papers, without any substantial modifications or creative combinations to the continual imitation learning or robot control tasks.

**In terms of the empirical results**, they may not offer any in-depth understanding of using adapters in continual imitation learning and the significance can be limited. The paper mentions that TAIL with LoRA “avoiding catastrophic forgetting and preserving adaptation plasticity”. Avoiding catastrophic forgetting can be evident since the adapter weights are task-specific and not shared across different tasks. But the empirical results shed little light on the adaptation plasticity. It is unclear if and how the adaptation plasticity is preserved given that the empirical results focus only on the success rate, as in Figure 4.

### Questions
1. In appendix, “all methods share similar amount of parameters”. I’m not quite sure how to interpret this. Why all methods need to have a similar number of parameters? Even though the adapter integration mechanisms are different? Could this constraint on the number of parameters be biased towards to LoRA adapter? (since “filtering often requires a larger bottleneck size compared to that of LoRA, leading to more parameters”)

2. In the experiment Table 1, “The BWT for TAIL methods are all 0 (no catastrophic forgetting)”. Is it self-evident? since the TAIL methods produce an ensemble of models (fixed pretrained weights + task-specific adapter weights), each of which aims to solve a dedicated task and is updated independently to each other. Then why do we need to use BWT as a performance indicator. 

3. The colours for Prefix Token & Frozen cannot be easily distinguished in Figure 2.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors applied parameter-efficient fine-tuning methods, including bottleneck adapters, P-tuning, and low-rank adaptation, to the continual imitation learning task. TAIL is designed to adjust large pre-trained models for new tasks even with limited demonstration data, with GPT2 as the backbone and CLIP-based modules as encoders. It avoids issues like catastrophic forgetting by activating the corresponding adapter for that task.

### Strengths
* The paper rigorously tests TAIL with prevalent PEFT techniques on the imitating continual imitation learning task.

* TAIL’s ability to achieve superior post-adaptation performance using only 1% of the trainable parameters of full fine-tuning highlights the framework’s efficiency, making it a potentially valuable tool for resource-constrained settings.

### Weaknesses
 * The framework's capability to circumvent catastrophic forgetting is primarily attributed to its unique configuration that allows for the selection of adapters tailored to individual tasks. Its efficiency largely draws from existing PEFT methodologies, which limits the novelty and distinctiveness of the presented framework.

* Drawing a comparison between TAIL and the fine-tuning baseline methods cited in the paper is unfair. This is because TAIL is designed to learn dedicated adapters for each distinct task. Thus, the claims regarding its efficacy become less compelling. Furthermore, while Experience Replay (ER) uses all previous data, the lack of a Mixture-of-Experts (MoE) setting in the baselines may also contribute to their worse performance. The different number of trainable parameters between TAIL and the baselines also remains a concern, as the ablation studies related to LoRA's rank suggest that increased parameters do not necessarily equate to improved performance.

### Questions
* Could you show the results when setting the rank for LORA to 32, 256, 512, and 768 (the dimensionality of the embeddings and hidden states of GPT2)? The ablation studies regarding the number of parameters should be added.

* Could you provide some insights on whether combining the Lora and P-tuning can improve the performance?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work presents Task-specific Adapters for Imitation Learning (TAIL), a framework for fine-tuning control policies in continual learning setting by borrowing ideas from large language model space. The agent is trained on multiple tasks, one task at the time, and the objective is to learn the new tasks while retaining the performance in old tasks. TAIL algorithms update only a small set of parameters, inspired by parameter efficient training from language model space. The results show that TAIL combined with LoRA outperforms all tested alternatives, especially full finetuning (tuning the whole network) or other methods that fine-tune the whole network.

### Strengths
Overall nicely wrapped work. While not the most novel solution (see weaknesses), I feel the amount of results and experiments conducted here merit acceptance. I believe these results will be useful for many readers, and the instructions on how to fine-tune these models will support future work.

### Originality

Authors bring insights from language space to control space in the form of efficient finetuning algorithms, and test those algorithms in a new setting (continual learning).

### Quality

Experiments are throughout with enough ablations and baselines. The methods are evaluated from different angles (performance increase in new task, retainibility in previous tasks, number of parameters / computational requirements.)

Accurate description of the experiment setup provided in the appendix (e.g., hardware, driver versions).

### Clarity

The manuscript is written well and is clear to read.

### Significance

The insights are also helpful for simple fine-tuning of models for different tasks: results show that LoRA is also very fast to adapt in general (better than full finetuning).

The manuscript also provides a list of ablations on what settings are recommended for finetuning, which are useful for people to follow.

Given the popularity of transformer models and their adaptation in different domains, I see this work being useful for many readers. Focus on experiments that can be ran on lesser hardware (e.g., single GPU, less space) also allows more people to experiment with these features.

### Weaknesses
 - Using a separate set of weights ("adapters") per task feels bit of cheating when comparing the model against the baselines. This alone ensures that you keep high performance in the previous tasks. While the argument for this is valid (with TAIL, you only need a handful of parameters vs. full network), I'd prefer a more apples-to-apples comparison. Specifically, the baselines that do not use task-specific parameters are at a disadvantage because they must overwrite existing weights to learn new tasks, leading to catastrophic forgetting. A more rigorous comparison would involve baselines that also have the capacity to add new parameters for each task, or a method that explicitly prevents forgetting in the baselines.
- Limited to only one environment. While I understand data for right setup is hard to come by, it is hard to tell if the results generalize outside this tested environment and data. Showing results in an another type of environment would solidify these insights. The current evaluation, while thorough within the LIBERO dataset, lacks the necessary diversity to confidently assert the general applicability of the proposed method. The LIBERO dataset, while large-scale, is still a specific type of robotic manipulation task. It is unclear if the performance gains observed would translate to different robotic platforms or tasks with different dynamics or sensory inputs.
- (Minor) Proposed framework, despite having its own name, is not especially novel or specific: it is an umbrella term for existing solutions applied on the continual learning setting. This is evident from figures, where the same method (TAIL) appears multiple times, and fundamentally, all these variants are significantly different from each other. I'd perhaps call different instiations of this setup "TAIL-LoRA", instead of "TAIL (LoRA)", to signify it is LoRA applied in TAIL's fashion. The lack of a distinct core mechanism makes it difficult to pinpoint the exact source of the performance improvements. The framework essentially combines existing techniques like parameter-efficient fine-tuning with a continual learning setup, and the contribution is more of an empirical study rather than a novel algorithmic advance.

### Questions
1) Page 7, "Training, Adaptation and Evaluation" paragraph: Manuscript says "This limited data setup...". How do you consider this a "limited data" setup? Can you give context/examples what would not be "data limited" setup?

2) Page 7, last paragraph. The description of what parts were finetuned/update/adapted and when is somewhat unclear and involved. How did you come up with this setup? Could you clarify this paragraph or provide a figure to help with understand what was updated in which stage?

## Comments
- Define acornyms only once and consistently use the acornym ever since (e.g., TAIL is defined multiple times).


## Rebuttal update 20th Nov

I have read authors' answers to my questions, and I have kept my original review score.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

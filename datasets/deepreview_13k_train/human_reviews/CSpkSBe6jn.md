# Task-Adaptation Curriculum Learning

- Decision: Reject
- Scores: 3, 3, 3, 5, 5

## Abstract
A large distribution gap between a target task and pre-training tasks could undermine the task adaptation performance of pretrained models. When the target-task data are scarce, naive finetuning results in overfitting and forgetting. In various domains, skills can be transferred across semantically related tasks, among which the general-purposed ones often have more training data. Can we bridge the gap between a pre-trained model and a low-resource target task by leveraging data from other tasks? In this paper, we address the low-resource task adaptation challenge by a transfer learning curriculum, which finetunes a model on a curated sequence of intermediate tasks, thereby progressively bridging the gap between the pre-trained model and the target task. To this end, we formulate the task curriculum as a graph search problem and improve the efficiency of estimating transferability between tasks. Two search algorithms are studied, i.e., greedy best-first search and Monte Carlo tree search. We evaluate our approach, i.e., ``task-adaptation curriculum learning (TaCL)'' on two benchmark settings. Extensive evaluations on different target tasks demonstrate the effectiveness and advantages of TaCL on highly specific and low-resource downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces Task-Adaptation Curriculum Learning (TACL), a method to improve model adaptation to resource constrained target tasks by identifying and adapting model to intermediate tasks in a curriculum learning setting. The motivation is to mitigate the over-fitting issues that could rise when the amount  of target data is limited and is also characterized  by a large distribution	shift from the pre-training datasets. The authors propose to use existing publicly available datasets to define appropriate intermediate tasks and adapt the model thus battling the limited data issue. 
To this end, authors forms this problem as a graph search problem, where each task is represented as a node. Their approach identifies an optimal sequence of tasks by evaluating task transferability using two search algorithms: Greedy Best-First Search (GBFS) and Monte Carlo Tree Search (MCTS). GBFS makes local, stepwise choices for each task in the sequence, while MCTS explores the sequence space more broadly, balancing exploration and exploitation via simulations by posing it as a multi-armed bandit problem. To estimate task-transferability, they first adapt the model on the intermediate task and then evaluate on the target task and measure heuristics such as validation loss or accuracy.  Furthermore, to reduce high computational costs, the authors propose to  limit the training steps on intermediate tasks to make a quick approximation of task-transferability. 
They have conducted experiments on a 20-task and 6-task graphs with NLP benchmarks. Since their approach requires a pre-determined  graph, for the 20-task case, they compute it using previous studies and also prune the complete graph to reduce the search space.  Their experiments demonstrate that TACL significantly outperforms  naive fine-tuning and even a random order of tasks. MCTS seems to perform better most of the time.  Overall, TACL presents an effective approach to bridging gaps between pre-trained and target tasks, enhancing model generalizability across diverse task types.

### Strengths
The paper is well-written and easy to follow. The motivation is sound, and this is an important direction as the community increasingly moves toward fine-tuning from pre-trained models rather than training from scratch. Framing the problem of identifying intermediate tasks as a graph search selection is both interesting and a well-founded choice.

### Weaknesses
I have a few concerns and questions regarding the approach. First, there is a requirement for predetermined graphs, at least for GBFS. Could the authors clarify how they obtained the graph for the 6-task setting? They have explained their approach for the 20-task graph, but it’s not immediately clear how they obtained the 6-task graph. Was it generated in an almost brute-force manner, where the neighbors of a node include all tasks in the graph? Clarification on this point would be appreciated.

A major concern is that, in many domains, a predetermined task graph might not be readily available. It is also unclear how to address this issue in such settings. Additionally, I suggest that the authors consider augmentation-based baselines that address data scarcity issues or use generative models like LLMs (e.g., from [https://arxiv.org/pdf/2403.02990](https://arxiv.org/pdf/2403.02990)).

Furthermore, the idea of using similar tasks and discovering task relationships is well-studied in computer vision. For example, the CVPR 2018 best paper award-winning work on Taskonomy ([http://taskonomy.stanford.edu/](http://taskonomy.stanford.edu/)) addresses a similar problem and reveals a task graph. Please consider citing this work and discussing the connections.

The proposed solution also resembles meta-learning but lacks a meta-test update. Specifically, similar to meta-training, TACL adapts on an intermediate task, then evaluates this adaptation on the target task, akin to meta-testing. Meta-learning would use both gradients for updates, while TACL uses a simpler approach. Another relevant work, [https://arxiv.org/pdf/1911.10600](https://arxiv.org/pdf/1911.10600), addresses a similar issue and uses meta-learning to reveal the graph of task relationships, scaling to as many as 400 tasks. I recommend discussing these approaches.

I also suggest the authors comment on, or experiment with, anti-curriculum learning (i.e., training with harder tasks first). Studies such as [https://arxiv.org/abs/1707.09533](https://arxiv.org/abs/1707.09533) and [https://arxiv.org/abs/1811.00739](https://arxiv.org/abs/1811.00739), show that anti-curriculum learning can sometimes outperform standard curriculum learning.

Additionally, I am concerned that reducing the number of training steps may not be ideal for estimating the transferability score. Deep networks often exhibit grokking behavior ([https://arxiv.org/abs/2201.02177](https://arxiv.org/abs/2201.02177)) and double descent. It would be helpful to see a comparison or discussion on how these phenomena might impact the transferability scores.

A very minor point is that in a resource-constrained setting, the validation set is limited by definition, and I wonder if the heuristics are meaningful, given that they carve a portion from the training data.

Finally, there is a strong connection between TACL and continual learning. For instance, [https://arxiv.org/abs/2205.13323](https://arxiv.org/abs/2205.13323) examines the impact of task ordering in continual learning and proposes curriculum learning. Expanding the related work to include connections to continual learning would strengthen the paper.

One last critical piece missing is a baseline that updates only part of the network rather than the entire model, such as using LoRA. This approach might reduce overfitting by limiting the number of updated parameters. I suggest exploring this experiment, even for the 6-task setting, as parameter-efficient tuning is becoming as common as fine-tuning entire pre-trained models.

### Questions
Please see weaknesses section. I have listed the questions there as well.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper formulates the task curriculum as a graph search problem, aiming to identify a sequence of intermediate tasks that bridge the gap between a pre-trained model and a low-resource target task. Methodologically, the approach integrates two classic search algorithms into its framework: greedy best-first search (GBFS) and Monte Carlo tree search (MCTS). Experimental results on two NLP task sets demonstrate the proposed method's superiority over other relevant baselines.

### Strengths
1. The writing is clear and easy to follow.
2. The proposed method, TaCL, which leverages graph search as a curriculum for task adaptation, appears to be valid.

### Weaknesses
1. The contributions of this work are vague, as the idea of treating the task curriculum as a graph search problem is not novel. Additionally, two classic search algorithms (GBFS & MCTS) studied to make the contribution of the work rather limited.  
2. The evaluation baselines are sparse and do not include comparisons with more advanced methods in relevant areas, such as Curriculum Learning and Transfer Learning. Moreover, the domains of the evaluation tasks are limited, with most experiments focused on NLP tasks and the benchmarks used not being particularly advanced.
3. Important details about the method are missing, making it difficult to fully understand its implementation.

### Questions
1. What distinguishes TaCL from LoRA, particularly in the context of task adaptation for popular large language models (LLMs)?
2. How are the intermediate tasks designed—are they generated or pre-designed? Additionally, what does Q(v’) represent in Equation 6?
3. How does TaCL perform in CV or robotics tasks? How does it compare to other advanced methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper addresses the problem of model fine-tuning, aiming to bridge the gap between a pre-trained model and the low-resource target task. The authors propose to leverage other semantic relevant tasks to improve the target task performance. A task-adaptation curriculum learning (TACL) is proposed to construct a sequence of tasks to enhance fine-tuning. The task sequence selection is formulated as a graph search problem, whereas the greedy search and Monte Carlo tree search are investigated and evaluated. Experiments on two benchmarks are conducted to validate its effectiveness.

### Strengths
1. The idea of building task curriculum to enhance fine-tuning performance on target task is interesting. 
2. The paper is generally well-written and easy to follow.
3. The target performance of TACL is better than baselines.

### Weaknesses
1. While learning from task curriculum may improve the performance on the final target task, it may raise concerns about more severe forgetting and safety risks. For example, previous research [1] shows that fine-tuning may compromise the model safety. The reviewer concerns that the proposed method may exacerbate the problem by introducing a longer fine-tuning path. Therefore, it is suggested that the author should add discussion and experiments on these aspect to validate the method more comprehensively.
2. The analysis of the search results of the six-task graph (fig 5 and fig 6) is insufficient. In the analysis provided, the authors only highlight the importance of a particular task MNLI, whereas the effect of other tasks are left without discussion. Due to the reason, it is still unclear what is the key aspect of the task curriculum that leads to performance boost. It is crucial to understand the contribution of each task in the curriculum to justify the proposed method. For instance, are there specific task pairings that consistently lead to better performance, or are there tasks that consistently hinder performance? A more granular analysis of task interactions is needed.
3. In the related work section, the relevant works cited are generally published years ago. It is suggested that the authors include more recent papers.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores low-resource task adaptation using multiple auxiliary tasks within a transfer learning curriculum. In this framework, a sequence of auxiliary tasks is selected for model fine-tuning. The authors formulate the task selection process as a graph search problem, and propose two search algorithms to estimate transferability and select tasks. Experiments demonstrate the effectiveness of these algorithms in multi-task transfer learning scenarios.

### Strengths
* The paper explores the question of how to effectively select a sequence of tasks for low-resource task adaptation, a novel approach in the few-shot learning domain.
* Experiments demonstrate that the task sequence selection methods outperform full fine-tuning, providing valuable insights into the transfer learning field.
* The paper is clear structured and well-written.
* The authors emphasize the issue of computational cost and propose several improvements to address it.

### Weaknesses
The main weakness of the paper is the significance and computational burden of search algorithm.

* This paper explores of how to leverage data from auxiliary tasks for task adaptation. To address the problem, the authors consider a transfer learning curriculum framework and propose some algorithm to select task sequence. However, in each step of the sequential process, a model can learn from only one task. A more simple and straightforward approach is joint learning multi-tasks with adaptive weights for each tasks. In the joint learning process, multiple tasks can interact with each other to improve model performance.
* Another problem is the computational burden of proposed algorithms. Although authors emphasize the issue of computational cost and give some qualitative analysis in discussion, quantitative analysis about full-finetuning and proposed search algorithms is more important. As different strategies involves different training process (e.g. training steps and number of training samples).

### Questions
See my comments under weaknesses section.

Another question is as follows:
* Can the authors provide more details about the task embedding methods used in the experiments? Do these methods select only one intermediate task, or do they choose a sequence of tasks, similar to GBFS and MCTS? Additionally, why do the task embedding methods underperform GBFS and full fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper discusses the challenge of adapting pre-trained models to low-resource target tasks, especially when there is a significant distribution gap between the pre-training tasks and the target task. To address this, the authors propose a transfer learning curriculum approach called "task-adaptation curriculum learning (TaCL)" that fine-tunes the model on a sequence of intermediate tasks, progressively bridging the gap between the pre-trained model and the target task. The task curriculum is formulated as a graph search problem, and the paper studies two search algorithms: greedy best-first search and Monte Carlo tree search. The effectiveness of TaCL is evaluated on benchmark settings, showing its advantages in adapting to highly specific and low-resource downstream tasks by leveraging data from other semantically related tasks.

### Strengths
1. This paper is well-written and has a good motivation.
2. This paper investigates the challenge of adapting pre-trained models to low-resource target tasks, which is an important and interesting problem that may greatly benefit the deep learning community.
3. This paper formulated the task curriculum as a graph search problem,  which gives a fresh perspective for transfer learning.

### Weaknesses
1. The paper uses two search algorithms: greedy best-first search and Monte Carlo tree search. Both of these algorithms are proposed by the existing works, limiting the proposed method's novelty. The application of these algorithms to the task curriculum problem is not sufficiently novel, and the paper lacks a deep analysis of how these algorithms are adapted or modified for this specific problem. A more detailed explanation of the algorithm's implementation and any modifications made would be beneficial.
2. The proposed task-adaptation curriculum learning (TaCL) is quite similar to the existing work "Don't Stop Pretraining: Adapt Language Models to Domains and Tasks", a more thorough analysis and comparison with it will be favored, especially in the experiment section. The paper needs to clearly articulate the differences in methodology and experimental setup compared to this existing work. A more detailed discussion of the advantages and disadvantages of TaCL compared to this work is required.
3. This paper proposed a sequential strategy to fully exploit the existing tasks. What about a parallel strategy? For example, if we have six auxiliary tasks, we can fine-tune the first two tasks and then the next four tasks, rather than fine-tune them one by one. Will such a parallel strategy perform better? Further, we can also finetune the six auxiliary tasks together and then on the target tasks. Will such a strategy alleviate forgetting better? The paper lacks a discussion on the potential benefits and drawbacks of parallel training strategies and how they might compare to the proposed sequential approach. The exploration of alternative training strategies is needed to fully understand the limitations of the proposed method.
4. The proposed task-adaptation curriculum learning (TaCL) is much heavier than the existing transfer learning methods since it has to train on several extra tasks.  How much extra training time or cost will it bring? What about the return on investment? The paper does not provide a detailed analysis of the computational cost of the proposed method, which is a critical factor for practical applications. A thorough analysis of the computational overhead and a discussion of the trade-offs between performance gains and computational cost are needed.

### Questions
Please refer the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

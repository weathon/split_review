# LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Low-rank adaptations (LoRA) are often employed to fine-tune large language models (LLMs) for new tasks. This paper investigates LoRA composability for cross-task generalization and introduces \lorahub, a simple framework devised for the purposive assembly of LoRA modules trained on diverse given tasks, with the objective of achieving adaptable performance on unseen tasks.
With just a few examples from a new task, \lorahub can fluidly combine multiple LoRA modules, eliminating the need for human expertise and assumptions. 
Notably, the composition requires neither additional model parameters nor gradients.
Empirical results on the Big-Bench Hard benchmark suggest that \lorahub, while not surpassing the performance of in-context learning, offers a notable performance-efficiency trade-off in few-shot scenarios by employing a significantly reduced number of tokens per example during inference.
Notably, \lorahub establishes a better upper bound compared to in-context learning when paired with different demonstration examples, demonstrating its potential for future development.
Our vision is to establish a platform for LoRA modules, empowering users to share their trained LoRA modules. This collaborative approach facilitates the seamless application of LoRA modules to novel tasks, contributing to an adaptive ecosystem.co/lorahub}{\texttt{huggingface.co/lorahub}}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to improve the generalizability of LLMs to new tasks. The proposed method can be summarized as below:
1. Train several models on a set of downstream tasks (one model for each task). This is done in a parameter-efficient way using the LORA method. This results in a set of LORA models. 
2. Randomly choose a subset of the LORA models.
3. Learn a set of weights to combine these LORA models using a few (for eg, 5) samples from a new task not seen in step 1. The weights are learnt using gradient-free optimization. 
4. Use the learnt weights to generate a combination of the LORA models and combine it with the base LLMs for inference. 

The result is a method that can be used to improve generalizability when the number of samples available for a new task is very low.

### Strengths
- The paper presents an interesting way to fine-tune LLMs on tasks where the number of training examples might be very low. 
- The proposed method uses gradient-free optimization to minimize resource requirements, since the number of parameters being learnt is very low.
-The method outperforms zero-shot deployment of the base LLM.

### Weaknesses
The main weakness of the paper is its performance compared to in-context learning (ICL), as highlighted in Table. 1. The authors acknowledge this in the paper but justify by saying that their method uses fewer tokens in their fine-tuning process compared to in-context learning. However, I feel that ICL is a very straight-forward and easy way to improve generalizability and that the problem that the authors are addressing is a minor one. Further, the performance of the proposed method also weakens the paper. From a practitioner's perspective I feel that the proposed method will be less appealing to just using ICL.

### Questions
- Can the authors provide more insight into the impact of the reduced number of tokens required in the proposed method? What does that mean to a practitioner in the end? Especially considering the fact that the proposed method first needs the training of several LORA modules, the burden on a practitioner may actually be higher.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the task of employing `LoRA` (parameter-efficient low rank adapters) for few-shot learning of unseen tasks:: When only few samples are available for a new task, then training a new `LoRA` module on it may not work well. Instead, the paper considers the setting where several `LoRA` modules are available, pretrained on a set of upstream tasks $T_i$. Then, given a set of few samples for a new task, the proposed `LoRAHub` aims to learn the ideal "meta-weights" $w_i$ such that the agglomerated `LoRA` module $\sum_i w_i LoRA_{T_i }$ yields the best performance for the new few-shot task (Note that this required that all upstream `LoRA` modules have the same rank).

To optimize the weights $w$, `LoraHub` employs a gradient-free method based on combinatorial optimization, `Shiwa`, and uses it to minimize the loss on the given few-shot samples, with an additional regularization term on the weights $w$.

The proposed method is then evaluated using a `Flan-T5` backbone on the `Big-Bench Hard` benchmark. The upstream tasks are the 200 tasks originally used to instruct `Flan-T5`; however, in practice, a random subset of 20 tasks is used in each run, such that we only have 20 weights $w_i$ to tune in each run. Overall, `LoraHub` performs almost on-par with in-context learning method, with the advantage that it requires shorter input prompts hence fewer tokens to process (essentially identical to zero-shot learning).

### Strengths
- **Interesting idea and motivation**: I find the core idea of the paper very interesting with potential applications to fields such as multi-task learning or continual learning. While there are similar concurrent idea mixing mixture-of-experts with LoRA, I found the results of the paper and focus on few-shot multi-task novel and insightful.

- **Clear writing**: Overall the paper is clearly written, easy to read and understand. 

- **Detailled experimental analysis**: I found the experimental analysis (Section 5 in the paper) quite interesting and raises interesting properties as well as limitations of the proposed method.

### Weaknesses
 - **Computational cost of optimization**: Unlike In-Context Learning, `LoraHub` does not need to process additional tokens hence a reduced inference cost. However, it also adds the cost to optimize the combination weights $w$ on the input few-shot samples, in particular when many upstream tasks are available. It would be interesting to discuss the trade-off between these two costs, e.g. say we have some few-shot samples but only want to solve the associated task once, it might be more practical to use in-context learning rather than the optimization pipeline of `LoraHub` ?

- **Optimization of $w$ for many tasks and robustness of `LoRAHub`:** It's not clear to me how the optimization methods scale to a higher number of upstream LoRA modules either in terms of cost (see previous point) or performance: In **Figure 4**, we see that increasing the number of LoRA module does not always improve performance but strongly affects the variance of the outputs. This suggests that the optimization procedure is either noisy and/or does not converge well. As a consequence, it means that the number of candidate upstream LoRA modules, $N$, must be carefully selected (and the optimal $N$ even seems to be task dependent from **Figure 4**) which introduces an additional hyperparameter. This can be an important limitation for real-life applications.

- **Figure 3 and variance**: I think **Figure 3** would be much more convincing with error bars or some notion of variance. This figure's aim is to illustrate that "LoRA with few samples does not work as well as LoraHub's few-shot learning" , however the results are only available for 3 tasks, for which the assumption only holds until 20 few-shot samples;therefore it's not clear how the insight generalizes to more few-shot settings.

### Questions
- On the topic of **optimizing $w$ for many tasks**, I am wondering if authors have considered alternative techniques which might be more robust to optimization noise (beyond the prefiltering strategy mentioned in Section 7): e.g. a hierarchical approach (optimize $w$ for multiple random subsets of 20 LoRA candidates, then learn $w'$ for these agglomerated modules) or a curriculum like approach (gradually drop some of the candidates when optimizing $w$ if they are consistently given very low weights) ?

- **Question/Suggestion on Table 1**:  it is not clear to me whether Table 1 reports results averaged on 5 random seeds for *all methods* or only for `LoraHub` and whether the different random seeds impact the choice of query few-shot samples, or only optimization(e.g. initialization, and library of Lora modules). Maybe a more complete evaluation metric would be to report (avg) and (best) for all methods (or even some form of significance test) to understand how robust the other methods are to the random seed. 

- **Figure 3 and variance**: I think **Figure 3** would be much more convincing with error bars or some notion of variance. This figure's aim is to illustrate that "LoRA with few samples does not work as well as LoraHub's few-shot learning" , however the results are only available for 3 tasks, for which the assumption only holds until 20 few-shot samples;therefore it's not clear how the insight generalizes to more few-shot settings.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces LoRAHub, a method designed to enhance performance on unseen tasks by re-utilizing trained LoRA (Low Rank Approximation) parameters across different tasks. LoRAHub operates by weighting each of these parameters, learned through a minimal set of examples on unseen tasks, thereby outperforming zero-shot baselines while achieving comparable results to in-context learning.

### Strengths
1. The paper presents a novel approach to leveraging previously learned LoRA parameters to improve performance on unseen tasks.

2. It demonstrates competitive performance compared to in-context learning while outperforming zero-shot baselines, showcasing the potential of the method.

3. It would be beneficial if the authors could release the fine-tuned LoRA weight to the community.

### Weaknesses
1. The choice of using FLAN-T5-Large as the base model is questionable as a model pre-trained on unsupervised text might have been more relevant for fine-tuning / LoRA fine-tuning on upstream tasks from the FLAN collection.

2. The paper lacks clarity in explaining the rationale behind maintaining the same rank for the composed LoRA module and could benefit from exploring higher rank matrices when composing.

3. The selection of 20 LoRAs for unseen tasks seems arbitrary and might limit the method’s performance. An iterative procedure or justification for this selection would have been beneficial.

4. The absence of certain baselines, such as the average performance for BBH's top 5 upstream tasks, leaves gaps in the evaluation.

5. The baseline corresponding to the retrieval of a trained LoRAs, when given a handful of examples from unseen tasks, is missing. For example, see https://arxiv.org/abs/2302.03202

### Questions
1. Can you elaborate on the interpretation of negative coefficients for the LoRA weights?

2. Why was the decision made to maintain the same rank for the composed LoRA module? Have higher rank matrices been explored and if so, what were the findings?

3. Is the selection of 20 LoRAs for unseen tasks fixed or is there an iterative procedure to this selection? How does this choice impact the method’s performance on unseen tasks?

4. I believe the strength of the method lies in cases where there are a handful of examples from unseen tasks. If it's otherwise, that it is beneficial to use a larger number of examples, it would make sense to compare against methods like IA3 [https://arxiv.org/abs/2205.05638], which fine-tunes efficiently on few-shot examples from unseen tasks.

5. Why was FLAN-T5-Large chosen as the base model over a model pre-trained on unsupervised text? Wouldn't it be strange to fine-tune on FLAN tasks using LoRA on an already FLAN multitask-trained backbone model?

6. How does the absolute value of LoRA weight not exceeding 1.5 relate to the method's performance in section 4.2, and is there a particular significance to this threshold?

7. It would be beneficial to include parameter efficient fine-tuning and traditional fine-tuning performance in Table 1, especially with the setup of a limited number of examples.

8. Is In-Context Learning (ICL) performed on the same base Language Model (LLM), or is it conducted using larger decoder only LLMs? What are the implications of this choice on the comparison of results?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

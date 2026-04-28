# UnoLoRA: Single Low-Rank Adaptation for Efficient Multitask Fine-tuning

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Recent advances in Parameter-Efficient Fine-Tuning (PEFT) have shown Low- Rank Adaptation (LoRA) to be an effective implicit regularizer for large language models. Building on these findings, we propose UnoLoRA, a novel approach that leverages a single shared LoRA module for efficient multi-task learning. While existing methods typically use separate LoRA adaptations for each task, our approach demonstrates that a single shared adapter can effectively capture both task-specific and task-agnostic knowledge. We further introduce UnoLoRA*, an enhanced variant that employs a shared hypernetwork to generate task-specific embeddings, improving convergence and task adaptation. Our method significantly reduces trainable parameters to just 0.05% per task while maintaining competitive performance on the GLUE benchmark. Our analysis reveals that the A and B matrices in our shared LoRA adapter naturally develop complementary roles: A matrices capture generalizable features across tasks, while B matrices specialize in task-specific representations. Our results show that sharing a single LoRA adapter can achieve efficient multi-task learning while significantly reducing memory requirements, making it particularly valuable for resource-constrained applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents UnoLoRA, an approach for parameter-efficient multitask learning in large language models (LLMs) using a single Low-Rank Adaptation (LoRA) module shared across multiple tasks. Building upon LoRA as an implicit regularizer, the authors explore its application in a multitasking context, aiming to reduce the number of trainable parameters while maintaining competitive performance. The paper introduces an architecture, UnoLoRA, which integrates a shared hypernetwork that generates task-specific scaling factors.

### Strengths
- The paper conducts comprehensive experiments and analysis to verify the proposed method.
- The paper is well structured, proposing an architecture, UnoLoRA, which integrates a shared hypernetwork that generates task-specific scaling factors.

### Weaknesses
 - The experiments are conducted on T5-series models, which are from 4 years ago. Using a more recent model doesn't necessarily mean aiming for the current SOTA (state-of-the-art), but rather that the behaviors of stronger models might differ, making experiments on T5 impractical. For instance, current models, after instruction tuning, demonstrate strong zero-shot generalization across tasks, making multi-task learning less important. The choice of T5 limits the applicability of the findings to contemporary LLMs, which have significantly different architectures and pre-training objectives.
- In the first table, the method proposed in this paper does not outperform HyperFormer++, even though they have different amounts of training parameters, the average effectiveness is also quite lacking. Therefore, the experimental results of this paper are not very convincing. The lack of clear performance superiority, especially given the parameter efficiency claims, raises concerns about the practical advantages of the proposed method.

### Questions
- Why not use a self-implemented LoRA in both multi-task and single-task scenarios, since LoRA is relatively simple to implement?
- Is there a detailed efficiency analysis available?
-  How to acquire the task embeddings in the paper?

### Soundness
2

### Presentation
2

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
The paper introduces UnoLoRA, a method for parameter-efficient multitask fine-tuning of large language models (LLMs) through a shared Low-Rank Adaptation (LoRA) module. UnoLoRA leverages LoRA's implicit regularization properties to facilitate multitask learning by using a single adapter shared across all tasks, instead of separate adapters for each task. This approach drastically reduces trainable parameters to 0.05% per task while maintaining competitive performance with existing multitask methods. The model is evaluated on the GLUE benchmark and demonstrates parameter efficiency and improved generalization by capturing both shared and task-specific information. The authors further refine their method with UnoLoRA⋆, which converges faster and performs better in early training stages compared to the initial UnoLoRA.

### Strengths
- The authors conduct in-depth analyses of LoRA matrices in both single-task and multitask settings, highlighting distinctions in their properties (like effective rank and Frobenius norm) and the roles of A and B matrices. Visualizations like PCA further illustrate how UnoLoRA efficiently manages task-shared and task-specific information.
- The study’s experiments on the GLUE benchmark provide extensive evidence of UnoLoRA's effectiveness and competitive performance.

### Weaknesses
 - For the experiments on the GLUE benchmark, no repeated experiments with different random seeds were performed, and the experimental results are not completely convincing due to the randomness.
- Only the T5-base model was used for the experiment. The effectiveness of the method was not verified on larger or smaller models, nor on decoder-only models.

### Questions
- What is the relationship between Figure 2 and Figure 1? Which part of Figure 1 is the Shared Hypernetwork shown in Figure 2?
- For different tasks, does UnoLoRA only change the task embedding and keep the other parts shared between different tasks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a method called UnoLoRA, a procedure for constructing
low-rank Transformer adapters in a multi-task setting by training a network to
apply task-specific transformations to a shared adapter. In particular, while
standard LoRA parameterizes weight matrices as $W + AB^\top$ for low-rank
$A$ and $B$, UnoLoRA parameterizes them as $W + A ~\mathrm{diag}(H(t)) ~ B^\top$,
where $t$ is a task representation that includes both a discrete identifier
and example data and positional embeddings, and $H$ is a hypernetwork. A similar recipe was previously
explored by Karimi Mahabadi et al. (2021) under the name of "HyperFormers"; as
far as I can tell, the main differences are that:

- HyperFormers condition only on task IDs, while UnoLoRA conditions on example
  input data

- HyperFormers also modulate LayerNorm parameters, and not just adapters

- HyperFormers use a slightly different adapter parameterization from the modern LoRA recipe, with
  a nonlinearity in the middle

### Strengths
- Simple and seemingly effective way of parameterizing low-rank adapters in the multitask setting. The idea is timely---there have been a lot of improvements in LoRA and related schemes in the last couple of years, and revisiting conditional computation + adapter combinations seems like a promising direction.

### Weaknesses
 - Comparatively minor tweak of an existing idea. This wouldn't be an issue on
  its own, except for the fact that the various changes are not evaluated in
  a way that enables direct comparison to HyperFormers, as described below.

- Inconsistencies and missing details in the description of the method. Fig 1
  makes reference to a "Task-specific A" parameter that is not mentioned
  anywhere in the formal description of the method---is it used, and if so,
  where? Additionally, the experiments make reference to a method called
  UnoLoRA$^*$, which achieves slightly better performance than the base method
  but does not appear to be described anywhere.

- Major issues in evaluation. The paper's main results are summarized in Fig
  6(a), which show that UnoLoRA and HyperFormers both pareto-dominate training
  separate adapters for each task---UnoLoRA involves fewer parameters at the
  same level of performance, while HyperFormers give increased accuracy but are
  slightly less parameter-efficient than UnoLoRA. I have two concerns here.

    - First, the individual differences between UnoLoRA and HyperFormers are
      never individually evaluated, making it impossible to figure which (if any)
      are responsible for the performance differences.

    - Second, and more fundamentally---the whole point of adapter-based methods
      is that they provide a tunable parameter (the adapter rank) that trades
      off between accuracy and parameter count. So what we really need to see
      is the entire accuracy / efficiency curve for both model classes, rather
      than an arbitrary point on each. In fact, if I understand correctly,
      even the size of the adapter is totally incomparable between the two
      models being compared: this paper trains UnoLoRA with a rank of 8, while
      the results copied from the HyperFormers paper appear to use a rank of 24.

  Without a minimal comparison (or a complete frontier from each model), it is
  possible that all observed differences between methods result from
  incomparable hyperparameter choices.

- Major formatting issues: nearly every citation in the paper is incorrectly formatted (using \citet instead of \citep). It seems likely that this paper didn't receive even a single round of proofreading, and should not have been submitted to ICLR in its current form.

### Questions
- How does performance change as rank is varied?
- How do individual components of the method affect performance?
- What is UnoLoRA$^*$?
- Is there a task-specific $A$ matrix or not?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This article proposes a new method called UNOLORA, which utilizes shared low-rank adaptation (LoRA) modules to achieve efficient multi-task learning for large language models, and has achieved outstanding performance on the GLUE benchmark.

### Strengths
- The method proposed by the authors is simple but effective.

### Weaknesses
 - The writing and presentation is not good, for example, the caption and figure of Figure 1 seems confusing. Also the font size in the figure is too small to understand.

- The training of Shared Hypernetwork will introduce additional training cost.

- The method is only evaluated on one model, without scaling up the model size/architecture.

### Questions
- What is the difference between the UNOLora* and UNOLoRA? I haven't found the method difference in your paper?

- It required a comparation to use LoRA to multi task training.

- It is not clear why cross task relation is related to the capability of using LoRA to do multi-task learning.

### Soundness
3

### Presentation
2

### Contribution
2

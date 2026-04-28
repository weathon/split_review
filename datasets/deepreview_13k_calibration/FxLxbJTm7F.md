# Everything Everywhere All at Once: LLMs can In-Context Learn Multiple Tasks in Superposition

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable in-context learning (ICL) capabilities. In this study, we explore a surprising phenomenon related to ICL: LLMs can perform multiple, computationally distinct ICL tasks simultaneously, during a single inference call, a capability we term ``task superposition''. We provide empirical evidence of this phenomenon across various LLM families and scales and show that this phenomenon emerges even if we train the model to in-context learn one task at a time. We offer theoretical explanations that this capability is well within the expressive power of transformers. We also explore how LLMs internally compose task vectors during superposition. Furthermore, we show that larger models can solve more ICL tasks in parallel, and better calibrate their output distribution. Our findings offer insights into the latent capabilities of LLMs, further substantiate the perspective of ``LLMs as superposition of simulators'', and raise questions about the mechanisms enabling simultaneous task execution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper demonstrates evidence of task “superposition” in LLMs when doing in-context learning, i.e. that LLMs can perform, or predict tokens for, multiple tasks simultaneously when shown those tasks in-context.

The first major argument for this is an empirical study of both pre-trained and from-scratch transformers. The authors first show that, across 3 pre-trained LLMs (GPT-3.5, Llama-3 70B, and Qwen-1.5 72B), when a model is shown an equal mixture of in-context samples across 3 tasks, the output distribution of the model is often a simplex over the correct outputs for each task, i.e. the top 3 next-token predictions for each input are the correct next-tokens for each of the 3 tasks, and different models exhibit biases towards different tasks. This is in contrast to the model either failing to learn the task to perform due to conflicting information in the context, or simply outputting the answer for one of the tasks that appears in the context.

Additionally, the authors show that, when training models to perform simple ICL tasks from scratch, e.g. simple arithmetic, the probability of each task’s output is proportional to the percentage at which that task’s examples appear in the context during test-time, even after the models are trained to perform ICL on a single-task at a time.

The authors then demonstrate theoretically, through the construction of a transformer model, that a transformer with 7 layers is capable of performing task superposition over a set of in-context examples.

Finally, the authors demonstrate that “task vectors”, defined as the model representation of the final token of the ICL prompt, reflects superposition. The authors show that the task vector created by a mixture of ICL tasks appears as an interpolation of each task’s task vector in T-SNE embeddings. Additionally, they show that creating new “task vectors” by interpolating the task vectors of distinct tasks can result in the model exhibiting task superposition as well.

The authors close by analyzing the relationship between task superposition and model size. They show that larger models have output probabilities that are more calibrated with the task probabilities of the context, i.e. the output for a task which appears in 50% of the in-context samples has a 50% probability in the model output.

### Strengths
The paper presents a relatively strong argument that LLMs can perform multiple tasks simultaneously when identifying the task from context. This, in turn, provides more evidence towards the notion that ICL operates as a “mixture of experts”, identifying a distribution of tasks from context and conditioning on that distribution when outputting an answer. As a result, this paper makes some important in-roads towards improving our understanding of ICL.

The “from-scratch” experiments are particularly strong in this setting, as they show a relatively tight relationship between the distribution of tasks in-context and the predicted distribution of the model over task outputs. Additionally, the analysis of how superposition occurs in task vectors is particularly convincing in demonstrating that there does indeed seem to be some kind of “task mixture” being identified by the model, and the analysis of how model scale impacts this seems to indicate that this task mixture capability becomes more accurate as model size increases, which is particularly useful in helping us understand how LLMs do ICL.

### Weaknesses
The “core” empirical results on large, pre-trained LLMs do not leave a clear take-away that superposition is occuring. This may, in part, be due to how the results are presented, i.e. the take-away that the model spreads it’s output across the 3 task outputs relies on the probabilities for “other” outputs to be low, which it is not always. This seems to only really be true for all models in one of the four settings considered. Thus, while the paper makes a strong case that LLMs can perform multiple tasks in superposition, it does not necessary make a strong case that current LLMs will perform multiple tasks in superposition.

Finally, the usefulness of task superposition is still up for debate - the authors note in their limitations section that it’s usefulness is limited due to the lack of decoding tools that can take advantage of it. However, there is also not an analysis of how task superposition can impact task performance, and that trade-off, if it exists, is not discussed in this work. It seems intuitive that task superposition may impact the performance of the tasks being superimposed, which may also have an effect on its usefulness. In fact, it is somewhat surprising to me that task performance is not a major consideration when making the claim that models can perform many tasks simultaneously.

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

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
The paper studied a specific type of LLMs in-context learning task, which the authors termed “task superposition”.  The study is comprehensive and extensive, including theoretical analysis and in-depth empirical investigation.

### Strengths
1. The paper is clearly written and well presented.
2. The investigation towards the proposed ability is comprehensive and in-depth.

### Weaknesses
Due to the inherit hierarchical nature of the concept “task”, I think the definition of “task” is at the core of this line of work. For example, one can argue Fig 1(a) essentially only contains a single task, which is addition regardless of language, or one can also argue that it contains only two tasks, which are numerical addition and multi-lingual translation, or four tasks as defined in the paper.

Hence, with a slight change of perspective (i.e., one abstract level up), the so-called superposition of tasks ICL itself basically defines a single new task. Since we know that LLMs can do ICL for a single task, it is not surprising that LLMs can also do the (single) task of “superposition of tasks” through ICL. Therefore, the term “tasks superposition” is misleading and unclear. The paper does not sufficiently address this ambiguity, leading to a potential overstatement of the novelty of the findings. The core issue is that the definition of a 'task' is not sufficiently rigorous, allowing for multiple interpretations that undermine the central claim of 'task superposition'. For instance, the paper treats addition in different languages as separate tasks, but one could argue that these are simply different instantiations of the same underlying mathematical operation, thus constituting a single task with varied input formats. This lack of clarity makes it difficult to assess the true significance of the observed phenomenon.

Furthermore, the paper does not adequately distinguish between the proposed 'task superposition' and the known ability of LLMs to handle complex, multi-faceted instructions. If a single task is defined broadly enough to encompass multiple sub-tasks, then the observed behavior might simply be a manifestation of the model's ability to perform complex single tasks, rather than a novel form of 'superposition'. The paper needs to provide a more rigorous framework for differentiating between these two scenarios.

### Questions
1. How do you generate the output probabilities for the answers (e.g., in Fig 1(a))? Do you generate multiple outputs for a fixed prompt, then filter out the wrong ones, and count the correct ones over multiple prompts? 
2. What does it mean by "perform multiple tasks in a single inference call”, and “solve tasks in parallel”? What exactly is this “a single inference call”, is there an example?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the mechanism of in-context learning with multiple tasks. It discovers the “task superposition” of LLMs. Using both theory and pretraining experiments on toy tasks, it demonstrates the ability of LLMs to implement the “task superposition”. They also explore the composition of different task vectors and how the model size affects the “task superposition” ability.

### Strengths
1. The paper designs tasks to study the ICL with multiple tasks in LLMs. 
2. The composition of task vectors is interesting.

### Weaknesses
Overall, the paper provides multiple findings, but removing redundant findings and implementing more analysis of interesting findings would be better.

1. Some findings are redundant. Findings 1 and 5 are not surprising given previous works such as Bai et al. [2023].
2. Findings 2-4 are interesting. However, more work is required on these findings. A similar “task vectors” analysis could also be applied to finding 2. Findings 3 and 4 can also relate to the non-clibrated results in Figure 2. It would be better to emphasize these findings.

### Questions
1. Can authors demonstrate their novelty? Bai et al. [2023] have shown that “A single transformer can adaptively select different base ICL algorithms—or even perform qualitatively different tasks—on different input sequences, without any explicit prompting of the right algorithm or task.” This paper considers the mixture of different tasks with varying parameters of mixture. It is equivalent to selecting the correct algorithm that fits the mixture probability in the in-context examples.
2. Figure 2 presents that the output of LLMs is not calibrated with the in-context examples. How does this finding interplay with the results in Section 6, where the composition of task vectors is not proportional to the composition of in-context examples?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the "task superposition" phenomenon in ICL, i.e., 
LLMs can perform multiple different ICL tasks simultaneously. 
Empirically, it is observed that the phenomenon is ubiquitous across different LLMs and larger models can handle more tasks simultaneously 
and better represent the distribution of in-context tasks.
Theoretically, the authors show Transformers are expressive enough for task superposition.
They also relate task superposition to internal combinations of task vectors.

### Strengths
1. The paper introduces the interesting "task superposition" phenomenon, which provides insights on the ICL mechanism of LLMs.

2. The paper reveals an impressive correspondence between task superposition and internal combinations of task vectors.

3. The paper theoretically proves Transformers are expressive enough for task superposition.

### Weaknesses
1. The paper only illustrates the superposition phenomenon in the synthetic tasks. It seems unclear whether real-world tasks have the superposition phenomenon
or how the superposition phenomenon affects LLMs in practice. The synthetic tasks, while useful for controlled experiments, may not fully capture the complexities of real-world scenarios where tasks are often more nuanced and interconnected. The paper lacks a discussion on the potential limitations of extrapolating these findings to practical applications.

2. The theoretical explanation only considers the expressive power of Transformers. Since it has been proved that Transformers are Turing-complete, 
the theoretical result does not provide sufficient insights. The theoretical analysis focuses solely on the representational capacity of Transformers, neglecting other critical aspects such as the optimization landscape and the inductive biases that influence learning. The fact that Transformers are Turing-complete only shows they *can* represent the required functions, but not how they *learn* to do so efficiently or whether this is the mechanism actually used by LLMs.

### Questions
1. Theorem 1 states a quantitative relation between the embedding dimension, the numbers of heads, tasks, in-context examples, and example length.
Does this quantitative relation reflect how the model hyperparameters influence the task superposition capability in practice? For example, 
to perform $K$ tasks, does the model need at least $K$ heads? 

2. Could it be possible to prove the learnability of a Transformer that has the task superposition capability? Some works [1] [2] prove the learnability of ICL
under the Bayesian model of ICL.

3. Are there any insights on how the superposition phenomenon of the LLM influences real-world tasks? Is it desired or undesired? 
In the examples of the paper, an LLM with the superposition phenomenon seems to choose a random task if there are multiple different ICL tasks simultaneously.
Can this be disadvantageous in some scenarios? Could it be possible to control which task the LLM will perform?

[1] Zhang, Yufeng, Fengzhuo Zhang, Zhuoran Yang, and Zhaoran Wang. "What and how does in-context learning learn? bayesian model averaging, parameterization, and generalization." arXiv preprint arXiv:2305.19420 (2023).

[2] Wies, Noam, Yoav Levine, and Amnon Shashua. "The learnability of in-context learning." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
3

### Presentation
3

### Contribution
2

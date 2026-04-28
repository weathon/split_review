# Task Diversity Shortens the ICL Plateau

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 3, 6

## Abstract
In-context learning (ICL) describes a language model's ability to generate outputs based on a set of input demonstrations and a subsequent query. To understand this remarkable capability, researchers have studied simplified, stylized models. These studies have consistently observed long loss plateaus, during which models exhibit minimal improvement, followed by a sudden, rapid surge of learning. In this work, we reveal that training on multiple diverse ICL tasks simultaneously \emph{shortens} the loss plateaus, making each task easier to learn. This finding is surprising as it contradicts the natural intuition that the combined complexity of multiple ICL tasks would lengthen the learning process, not shorten it. Our result suggests that the recent success in large-scale training of language models may be attributed not only to the richness of the data at scale but also to the easier optimization (training) induced by the diversity of natural language training data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the impact of multi-task learning ("task diversity" in the title) on the speed of training on individual tasks in the context of In-Context Learning (ICL) of various language-modeling architectures (Transformer, Mamba, Hyena). Quite surprisingly, the results suggest that multi-task setup leads to faster training/convergence of individual tasks, compared to training on those individual tasks.

The experiments show primarily synthetic tasks, but language tasks are also included as validation. The paper also investigates different explanations for its findings, e.g., finding that the creation of Induction Heads on its own doesn't explain the results.

### Strengths
The paper showcases a good number of experiments with solid results. I also appreciate the explanation of the experimental setup, and detailed experiments with multiple tasks and models. The authors also present a good analysis of some possible explanations for the results achieved. The presentation is great, and so is the writing.

### Weaknesses
The most significant weakness of the work is the construction of the single-task baselines. In my opinion, this issue alone should justify the rejection of the paper. In short - **the experiments compare single-task models trained with batch size B with multi-task models (with k tasks) with batch size kB - k times larger batch size, and k times larger the training set/compute cost!** Then, the authors use the total number of iterations (batches) to compare models. While this is mentioned in the paper (line 177 and Appendix A), I think results should be shown with a more standard x-axis showing the number of tokens and not the number of iterations.

While the results, as initially presented, sound surprising, the fact that **multi-task models train on multiple times as much data compared to the baseline** makes the results fairly trivial or at least extremely easy to achieve positive results. Imagine this experiment: instead of training multi-task model on different tasks F1 and F2, let's set F1 to be equal to F2 (the same task twice). Such a "multi-task" model is then trained on simply a 2x bigger batch size than the baseline, and so, obviously, it converges faster in terms of iterations (but probably not faster in terms of tokens!) Of course, authors set different F1 and F2, but they are fairly similar, so I expect the results the authors get by default (if the model is not undersized wrt. problem complexity).

The paper shows model trained on 6 tasks jointly (using 6x bigger batch size). Then, convergence between 1.4x and 9.2x faster in terms of iterations (see Figure 1) is no longer surprising! In terms of tokens, that would mean a relative speed between 0.23x and 1.53x, which means multi-task learning is between **4x slower** and 1.5x faster. (Although parity tasks break this pattern, with single-task, the model ends up at a bad local minima. I'd expect the issue to be with training stability and insufficient baseline tuning, however.)

I'd expect either comparison on the same number of tokens - preferably with the same total batch sizes for both single-task and multi-task settings, as training with different batch sizes and number of batches makes the setup prone to mistuning the baseline on accident.

While there is a possibility that I don't understand something fundamental here, I'm inclined to reject the paper for the above reason. With proper comparison metrics, I believe the results are fairly trivial. What is worse, the paper in its current state is a bit misleading.

### Questions
As stated in the weakness section.
1. Why was a comparison on iterations, not total tokens, chosen?
2. Were baselines tuned for their smaller batch sizes?

### Soundness
1

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors explores how training models with ICL examples from multiple tasks simultaneously can improve the rate at which models learn the different individual tasks, even faster compared to when learning on one individual task. In particular, the authors characterize through a phenomena of the loss plateau, which is a scenario where the model's loss plateaus for a significant number of steps before observing sudden large decreases, by showing that multi-task ICL learning significantly shortens this plateau duration. They use this to conclude that this task diversity appears to aid optimization, making ICL training more efficient.

### Strengths
The manuscript very well written; the division of the paper makes it very intuitive to follow and the plots/tables are informative. The main findings are also quite interesting in how they present a setting where (if all holds) then learning various tasks at one can potentially improve the efficiency of learning a marginally or completely un-related task. The notion of measuring how the loss plateau contracts is a rather novel way of investigation and I see avenues where it could be useful for exploring the idea of other types of emergent properties in language models.

### Weaknesses
Some points made by the authors do not have completely solid grounding in the results or lack some support.

For example, on L16 and L199-202, the authors state that "multi-task ICL is easier to learn than single-task ICL is surprising as it contradicts the natural intuition that the combined complexity of multiple ICL tasks would lengthen the learning process". I'm not particularly convinced of this notion, at least in the regime within which the authors present their results. The sample is broken up into tokens, therefore the explicit rules of the functions that are being sampled for the in-context examples are likely not being directly captured in the sequence being presented. Additionally, since samples are consist of examples from a fixed function (that differs between samples), learning multiple tasks together can serve to learn more robust representations that won't as quickly over-fit to individual samples [1]. While the authors mention that they use a single linear embedding layer without a tokenizer, the core argument still stands that the model is not directly exposed to the explicit function rule but rather a sequence of input-output pairs, and thus the claim of the surprising nature of the multi-task learning benefit is not fully justified.

I also believe that to arrive at the author conclusions, further baselines need to be included. More explicit control over the exact sampling of tasks from $\mathcal{F}$, as well as the sampling of the parameters associated with the specific instance of $f$ should be necessary. For example, tasks can be sampled with uneven probability; if the shortening is consistent among different task classes but with the same sampling probabilities, then this can serve as a more explicit signal of it directly being due to the use of multiple tasks rather than a set of very few pairs of tasks that observe greater transfer compared to others.

Another particular concern of mine is that the paper is lacking in any specific formal analysis of the optimization landscape between the two settings. From my perspective, this causes a significant portion of the results, while interesting, to appear as speculative at best, which combined with the lack in explicit diversity among the different ICL tasks (either regression or boolean) to suggest a possible level of difficulty of extrapolating these observations to more general scenarios. I appreciate the examples provided in Appendix C on other natural language tasks, but given the fact that the results are somewhat inconclusive with regards to what settings multi-task ICL can help me I believe it's quite essential to investigate the differences from a optimization perspective. The current analysis in Section 4.2, while providing a plausible hypothesis, does not sufficiently demonstrate that the model is actually learning the proposed common structure, and further experimentation is needed to solidify this claim. For example, if a common structure is explicitly introduced in the data generation process, the degree to which this structure is learned could be quantified and related to the observed plateau shortening, providing a more concrete link between the hypothesis and the empirical results.

In summary: I did enjoy quite a few points about this paper, but the authors need to reformulate some critical points (or provide details to demonstrate that those are not critical). If the necessary clarifications can be provided, I am open to changing my opinion of the work but as of the moment I believe there still remains some work to be done to solidify the details in it.

### Questions
- Perhaps I am overthinking, but I want to just make sure my understanding of the training mechanism is correct. I understand that in the multi-task setting, $\mathcal{F} = \bigcup_{i=1}^k \mathcal{F}_i$ from which $f$ is sampled. Then $x_i,\dots,x_n$ is sampled from the domain of the sampled $f$. Therefore the training (for any given sample) is on any arbitrary task in the set of tasks that were selected. If this understanding is correct, please ignore the next two comments.
- Is $n$ (the number of samples from each function class) fixed at the same value for all values of $k$, or do they scale together; I apologize but I couldn't find this exact detail either in the main text or in the Appendix.
- I believe it would be useful to attempt an experiment where you can sample different functions from the same function class for constructing the tasks and see how this affects learning.
- L157: Why this complexity measure was chosen isn't particularly justified. Importantly, although you measure based on the number of learning steps, there are a number of different 
- For Section 4.2, I believe that the authors should be able to use synthetically generated data where an explicit common structure exists to better demonstrate the claims.

### Soundness
2

### Presentation
4

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
This paper examines the phenomenon of *in-context learning* (ICL) in language models, where a model learns from example inputs and outputs within a context to respond accurately to subsequent queries. Researchers have found that during ICL, models often undergo periods of minimal learning progress (“loss plateaus”) before rapidly improving. In this study, the authors show that training on a variety of diverse ICL tasks concurrently reduces these loss plateaus, making each task quicker and easier to learn. This result challenges the expectation that increased task complexity would slow down the learning process. The authors suggest that the enhanced performance of large-scale language models could be due to both the richness of large datasets and the facilitation of learning through task diversity, which helps streamline optimization.

### Strengths
This paper is clearly written. The figures and captions are easy to follow, and the motivation is clear.

### Weaknesses
The primary conclusion of this paper, “Task diversity shortens the ICL plateau,” may appear somewhat trivial. The study demonstrates that training models with multiple tasks simultaneously involves using significantly more data (i.e., training with n tasks simultaneously implies utilizing n times the amount of training data). Though these data sets pertain to different in-context learning (ICL) tasks, the observed improvements in learning efficiency could stem from the increased data volume rather than solely from “task diversity.” In this sense, the results align with well-established concepts of “knowledge transfer” in multitask learning, where it is well-documented that similar tasks can support each other’s learning. This paper essentially reinforces that ICL tasks share underlying similarities, which is trivial.

Additionally, it’s unclear how this finding can be practically applied to large language model (LLM) fine-tuning. If task diversity is indeed advantageous, does this imply a need to incorporate task-irrelevant data when fine-tuning a task-specific LLM? Clarifying this connection could greatly enhance the practical relevance of the paper’s conclusions.

Regarding the optimization argument presented in the paper, there is likely related literature supporting the benefits of multi-task training. For instance, one conclusion from the literature is that multi-task training often causes different tasks to converge at the same rate. Consequently, tasks that converge slowly when trained independently may benefit from accelerated convergence during multi-task training. This phenomenon is illustrated in Appendix C, Figure 1 of [1]. Therefore, the optimization-based justification in the paper is inadequate.

### Questions
Please refer to my weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies how multi-task learning improves in-context learning on individual tasks. Through experiments on synthetic tasks, it shows multi-task training with in-context examples shortens the loss plateaus of single in-context learning tasks, making the learning easier. The phenomenon also apears for other model architectures (Mamba) and tasks (simple natural language tasks).

### Strengths
1. The paper studies the learning dynamics of the in-context learning ability of language models, which is an important direction for understanding how language models obtain their capability.

2. "Task Diversity Shortens the ICL Plateau" is an interesting and valuable insight for designing new methods to accelerate the learning of LMs.

3. The experiments are sufficient to verfy the claims in the paper (at least in the toy settings).

### Weaknesses
1. An important property of ICL training is its generalization to unseen tasks [1,2]. This paper only shows that increasing the task diversity improves the learning tasks also in the training set. It would be better to examine how the diversity of ICL training tasks affects the ICL on unseen tasks.

2. The training tasks seems to have equal weights in the experiments (by sampling the same number of instances and balancing the losses). However, the tasks usually follow a long-tail distribution in the real-world pre-training corpus. Discussion on the setting where the tasks are unbalanced whould make the conclusions more close to the practical scenarios.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

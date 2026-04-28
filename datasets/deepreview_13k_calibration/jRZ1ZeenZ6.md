# Rational Metareasoning for Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5

## Abstract
Being prompted to engage in reasoning has emerged as a core technique for using large language models (LLMs), deploying additional inference-time compute to improve task performance. However, as LLMs increase in both size and adoption, inference costs are correspondingly becoming increasingly burdensome. How, then, might we optimize reasoning's cost-performance tradeoff?  This work introduces a novel approach based on computational models of metareasoning used in cognitive science, training LLMs to selectively use intermediate reasoning steps only when necessary. We first develop a reward function that incorporates the Value of Computation by penalizing unnecessary reasoning, then use this reward function with Expert Iteration to train the LLM. Compared to few-shot chain-of-thought prompting and STaR, our method significantly reduces inference costs (20-37\% fewer tokens generated across three models) while maintaining task performance across diverse datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to fine-tune language models with an objective that maximizes task performance while minimizing the (logarithm of) the number of tokens used. This objective is optimized with expert iteration. Results suggest that this objective does indeed help models use the extra reasoning tokens only when they're actually needed, thus reducing compute cost on easier tasks.

### Strengths
- Computational efficiency of LLM deployments is a timely topic relevant to the ICLR community.
- The proposed method is sufficiently simple that something like it might well get used in practice.
- The paper is well-written and clearly structured.

### Weaknesses
### a) Insufficient baselines and ablations -- I don't feel like I get the "shape" of the proposed method and the potential alternatives all that well.

A few notes here:

1. How necessary is rationalization (described in the paragraph on line 131)? I assume the authors only use it because it's also used in STaR, the main baseline? Relatedly (and importantly), STaR should be described in more detail in the paper, and justified as a relevant baseline -- I needed to open up the original STaR paper to remind myself of what it does.

2. Re design of the computational cost function: what happens when the cost is linear instead of logarithmic in the number of tokens? (Authors mention they tried linear cost but don't provide details.) How exactly is $\gamma$ chosen, and how sensitive is the method to this choice?

3. Did the authors try a prompting baseline such as asking the model to think however long it needs, but answer as soon as it's ready? I'd be interested in seeing this kind of baseline with a few prompt variations, as this can plausibly also help avoid spending many tokens on easy tasks & spend more tokens on harder tasks when needed -- especially in larger and more capable models. I think models might well already be tracking whether further reasoning is useful: such tracking could plausibly arise just from self-supervised pretraining on large corpora that include texts written by humans who're tracking this implicitly. (Efficiency of such a prompting baseline could be improved further with prompt distillation, but I don't think this would be important for this paper).

4. I'm also interested in variations of the proposed method with RLHF-style algorithms other than expert iteration (e.g. iterated DPO).

### b) I did not find Figures 1 and 2 particularly useful, especially the subplots on the left side. Also, is information from subplots on the right side duplicated in the tables?

1. One idea for improving the figures could be plotting task performance on the y axis and the computational cost (e.g. input + output tokens) on the x axis. It might then be clearer whether your method is on the pareto frontier, and generally help understand the performance-efficiency tradeoff.

2. Regarding Figure 2: I think here it'd be helpful to include 5-shot and/or (0-shot, CoT) benchmarks for MMLU, to get a sense of how STaR and your method compare to these.

### Questions
1. Re Section 4.3, how many expert iteration steps $n$ do you perform?

### Soundness
3

### Presentation
1

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
This paper introduces a rational metareasoning approach for LLMs, using a novel Value of Computation (VOC)-based reward function to reduce inference costs without compromising performance. Tested across diverse benchmarks, the method achieves significant token savings (20-37%) compared to standard prompting techniques. The results highlight this approach as an effective solution for cost-efficient reasoning in LLMs, though further evaluation on task variety would enhance the findings’ robustness.

### Strengths
* The paper introduces a unique rational metareasoning approach that balances inference cost with performance, addressing a crucial need in the efficient deployment of LLMs.
* The integration of the Value of Computation (VOC)-based reward function is well-designed and thoughtfully applied, showing careful consideration of LLM efficiency.
* The approach is tested across a diverse set of benchmarks, covering science knowledge, commonsense reasoning, math problem-solving, and logical deduction, as well as an out-of-domain generalization task (MMLU).
* Empirical results demonstrate notable reductions in token generation (20-37%), indicating that the method can achieve similar performance with fewer computational resources.
* The approach is valuable for scenarios where computational resources are limited, potentially benefiting applications needing cost-effective, high-quality language model outputs.

### Weaknesses
 * Limited Analysis of Time Complexity: While the paper focuses on token reduction, it lacks a rigorous analysis of the time complexity of the proposed method, particularly concerning the online reinforcement learning component. A deeper investigation into the actual time savings, including wall-clock time, would provide a clearer picture of its practical efficiency, especially when considering the overhead of the reinforcement learning process itself.
* Narrow Range of LLMs and Tasks: The method was primarily tested on a limited selection of benchmarks and model architectures, specifically focusing on smaller models like phi-2. Broader experimentation across different LLMs, including larger models with varying architectures, and a wider range of tasks, including more complex reasoning tasks, would strengthen claims about the generalizability of the approach and its applicability to real-world scenarios.
* Limited Robustness Testing: Although the results are promising, the paper lacks robustness checks to assess how performance holds under varied conditions, such as noisy inputs, adversarial examples, or tasks with varying levels of complexity. The absence of such testing makes it difficult to assess the reliability of the method in practical applications.
* Scalability Concerns: The feasibility of scaling this method to very large models or highly complex tasks is not fully addressed. The paper does not provide sufficient analysis on how the computational cost of the online reinforcement learning scales with model size and task complexity, leaving open questions about its applicability in more computationally intensive scenarios.

### Questions
### Questions
* Section 3.2: What is the likelihood of not generating a correct answer? Will this happen frequently? Any comment or justification on this?
* Are the input tokens of failed cases counted as part of the input and output tokens?
* What's the time cost of the proposed method itself, rather than the inference costs? The complexity is largely from the online reinforcement learning used in the proposed methods, i.e., EI?
*  The reliance on a single, VOC-inspired reward function might limit flexibility across diverse task types. Is there any justification on using alternative reward structures could reveal greater adaptability and robustness?

### Minors
* Line 97: Eq. 3.1 --> Eq. (2)?

### Soundness
2

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
This paper presents a method for fine-tuning large language models to enhance the cost-performance trade-off in reasoning procedure. The authors introduce a reward function that evaluates the computational value of various reasoning chains, enabling the ranking of these chains. By integrating this reward function with expert Iteration, the method trains LLMs utilizing intermediate reasoning steps selectively, employing them according to the rewards. This approach significantly reduces inference costs on specific datasets while preserving task performance.

### Strengths
1. The authors introduce an interesting problem in LLM reasoning, optimizing LLMs’ inference cost and performance at the same time. This is important issue in using LLMs especially considering the LLMs inference cost is becoming larger. 

2. The paper is well-written and easy to follow. Overall, I could follow the whole story that the authors want to present in this paper.

### Weaknesses
1. Lack experiments in more realistic datasets. LLMs are not limited to tasks in text space; they are frequently utilized as agents that interact with external tools to perform complex tasks in various environments. Incorporating experiments on more realistic datasets, such as GAIA [1] and ToolBench [2], would provide valuable insights into the model's performance in more complex reasoning scenarios. Specifically, the paper should explore scenarios where the LLM needs to use tools to gather information or perform actions, which would more accurately reflect real-world applications. The current experiments, focusing solely on text-based tasks, do not fully capture the challenges of integrating LLMs into more complex systems.

2. Currently, the method and experiments focus exclusively on CoT reasoning, generating trajectories for model fine-tuning and serving as baselines. However, CoT may not always produce the optimal trajectory and should not be considered a strong baseline. It would be beneficial to explore alternative reasoning methods for fine-tuning the models. At the very least, a discussion or justification regarding the choice of reasoning methods should be included in the paper. The paper should investigate whether the proposed reward function and fine-tuning approach can be effectively applied to more advanced reasoning techniques, such as those involving iterative refinement or backtracking. This is crucial to demonstrate the generalizability of the method beyond the limitations of CoT.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new fine-tuning approach for training LLMs to generate token-efficient and adaptive responses. The method encourages the LLM to produce longer reasoning chains only when necessary. Building on the STaR framework, it introduces a filtering step to fine-tune the model on correct answers with the highest reward, where the reward function penalises unnecessarily long responses. Experiments on a dataset constructed from a mixture of four benchmark datasets show that the method effectively reduces the token count of generated responses without sacrificing accuracy. The results also demonstrate that the method promotes adaptive behaviour, producing longer responses for more difficult questions and shorter ones for simpler questions.

### Strengths
- The paper tackles an important and underexplored problem of lowering sampling costs at inference time without sacrificing model performance in an adaptive manner.
- The proposed method shows improved performance over a set of 3 baselines, including the STaR method which is a direct ablation of Rational Metareasoning.
- The method is evaluated on a good selection of benchmark datasets.

### Weaknesses
 - The link between VOC and the latter presented approach of modified expert iteration is unclear. Sections 2 and 3 are not well connected together. Specifically, the transition from the theoretical concept of Value of Computation to the practical implementation using expert iteration lacks sufficient detail. The paper would benefit from a more explicit explanation of how the components of VOC, such as computations ($c$), beliefs ($b$), and actions ($a$), map onto the elements of the expert iteration framework, including the input ($x$), reasoning chain ($z$), and answer ($y$).
- Incremental contribution. The method is an extension of existing work (STaR). The core idea of using a reward function to penalize long reasoning chains and selecting the highest-reward chain for fine-tuning is not entirely novel. More justification or analysis of this approach's novelty would strengthen the paper. For instance, a more thorough comparison against alternative methods for controlling response length or a deeper theoretical analysis of the proposed reward function's properties could provide stronger evidence of the paper's unique contribution.
- There a few places where writing could be improved (see the writing suggestions below).
- There are a few inconsistencies or unclear statements (see the clarity comments below). For instance, the statement in Line 159 regarding the approximation of the optimal policy using rejection sampling is confusing. The notion of an optimal policy hasn't been defined, and the algorithm seems to deviate from standard rejection sampling by selecting only the single reasoning chain that maximizes the reward, rather than all chains above a certain threshold. Furthermore, there are inconsistencies in the presentation of Algorithm 1, such as the missing assignment of $\pi_0$ and the unclear subsampling of $\mathcal{D}\_n$ from $\mathcal{D}$.
- A potential limitation, not mentioned in the paper, is that while shorter responses may be preferred from the computational costs point of view, they may not necessarily be more human friendly. The paper would benefit from a small human study assessing the qualitative aspects of the generated reasoning chains with Rational Metareasoning.
- Experiments could include additional baselines and ablation studies. For example, it would be interesting to compare Metareasoning with Direct Few-Shot prompting, where the LLM is explicitly instructed to provide concise responses. Additionally, the batching technique with increasing $T$ is a design choice that should be tested in an ablation study. Finally, the proposed expert-iteration algorithm could be compared to other fine-tuning algorithms, like PPO, to better motivate the particular choice of the training method.

### Questions
1. Could the authors elaborate on how VOC translates to the setting of reasoning with LLMs? What would the computations $c$, beliefs $b$ and actions $a$ correspond to with respect to the terms presented in section 3: input $x$, reasoning chain $z$ and answer $y$?
2. Why is the LLM policy fine-tuned only with respect to the reasoning’s $\hat{z}$ that maximise the reward within the sampled batch of rasoning chains? In expert iteration, we would typically retain all reasoning chains $z_i$ for which the reward is above a certain threshold. Could the authors provide either a theoretical motivation behind their choice or run additional empirical studies comparing their training method to alternatives (e.g. expert iteration with threshold rejection, PPO) to justify the choice of the training method?
3. Is the $T$ in lines 165-169 referring to the number of fine-tunning steps used in the $\mathrm{train}(\pi, \mathcal{D}_n^*)$ subroutine at each iteration or is it the number of examples sampled from $\mathcal{D}$? 
4. How many training iterations $N$ of the algorithm are needed for convergence and what is the relationship between the compute time for policy training vs. final performance?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents an approach for optimizing small LLMs towards generating shorter chains of reasoning while maintaining capabilities. To this end, the authors designed a reward function that balances the log-likelihood of generating a target answer with the log normalized cost of the number of generating chains of thought tokens. Experiments on a number of question-answering datasets demonstrate that the proposed approach can reduce the number of output tokens while maintaining the LLM’s performance.

### Strengths
A) The paper is clear and easy to follow. Furthermore, the method is simple enough and the paper detailed enough so that it would, I believe, be easy to reproduce. 

B) The problem of reducing the number of output tokens of CoT-like approaches has practical relevance.

C) While the LLMs that were investigated are on the small end (2.7B-8B), the authors demonstrate that their approach leads to reduced number of output tokens on multiple LLMs and datasets.

D) I appreciate the inclusion of insightful qualitative results in the Appendix.

### Weaknesses
## Major
E) I appreciate the attempt to demonstrate the validity of the method for multiple chains of reasoning approaches (CoT and STaR). However, in my view, the paper is incremental, since the cost of generating chains of reasoning has already been addressed by follow up work like Zelikman et al. (2024). Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking. arXiv. https://doi.org/10.48550/arXiv.2403.09629 The authors should directly compare to Quiet-STaR, and investigate whether their approach can provide orthogonal gains.

F) In my view, the following important ablation is missing to ensure that the models are indeed retaining their ability to reason (and decompose a problem into subproblem) as opposed to relying simply on directly producing an answer. Looking at Figure 3 and Figure 4 in the Appendix, it seems to me the model learned to simply rely on its internalized knowledge (one conclusion from this could be that ARC and CommonsenseQA simply aren’t great benchmarks to assess complex reasoning capabilities). As a baseline, directly fine-tune the LLM to produce the correct answer. I also need to point out that the reduction in reasoning lengths is much less impressive on the harder reasoning benchmarks GSM8K and Proofwriter (see Table 5). Thus, my current hypothesis is that the proposed approach works well for problems that are not hard reasoning problems, but is much less effective on harder reasoning problems where we actually need more CoT-like methods.

G) Related to the above, I believe the authors should test on additional hard compositional problems such as AQUA-RAT (https://github.com/google-deepmind/AQuA).

H) Another ablation I am missing is investigating to what extent RL is really needed here. What happens if you generate chains of reasoning on the training data, ask the LLM to summarize these chains, and then directly fine-tune on this synthetically generated data?

## Minor
I) LLMs are on the smaller scale, so it remains to be seen whether gains in terms of reduced number of output tokens persist for larger models.

### Questions
I don’t have any questions, the paper was very clear.

What the authors would have to demonstrate to see an improved rating from me:
1. Compare directly to Quiet-STaR, and demonstrate whether their approach leads to orthogonal gains (E)
2. Add an ablation where the LLM is directly fine-tuned on the author’s training sets (F)
3. Demonstrate results on additional compositional reasoning benchmarks such as AQUA-RAT since ARC and CommonsenseQA aren’t informative (G)
4. Add an ablation where the LLM is used to summarize chains of reasoning and then fine-tuned on the resulting synthetic data (H)

### Soundness
3

### Presentation
3

### Contribution
2

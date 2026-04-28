# $\text{Transformer}^2$: Self-adaptive LLMs

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Self-adaptive large language models (LLMs) aim to solve the challenges posed by traditional fine-tuning methods, which are often computationally intensive and static in their ability to handle diverse tasks. We introduce $\text{Transformer}^2$, a novel self-adaptation framework that adapts LLMs for unseen tasks in real-time by selectively adjusting only the singular components of their weight matrices. During inference, $\text{Transformer}^2$ employs a two-pass mechanism: first, a dispatch system identifies the task properties, and then task-specific "expert" vectors, trained using reinforcement learning, are dynamically mixed to obtain targeted behavior for the incoming prompt. Our method consistently outperforms ubiquitous approaches such as LoRA, with fewer parameters and greater efficiency. Furthermore, $\text{Transformer}^2$ demonstrates versatility across different LLM architectures and modalities, including vision-language tasks. $\text{Transformer}^2$ represents a significant leap forward, offering a scalable, efficient solution for enhancing the adaptability and task-specific performance of LLMs, paving the way for truly dynamic, self-organizing AI systems. We provide our full source code with the submission.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the challenge that traditional fine-tuning methods are often computationally intensive and static in their ability to handle diverse tasks, this paper proposes a self-adaptation framework that adapts LLMs by selectively adjusting the singular components of their weight matrices for unseen tasks at inference time. In the training stage for each task, it trains a vector to replace the singular values for each weight matrix. In the inference stage, it first extracts the task-related “singular vectors”, then makes inference with selected task-related “singular vectors”. Compared with Lora, experiments show the effectiveness of the proposed method.

### Strengths
1.	The proposed method of finetuning LLMs within eigenspaces is highly parameter efficient, as it only needs to train r = min(m, n) parameters for each weight matrix rather than $(m+n)\times r^\prime$ learnable parameters in Lora. 
2.	The proposed method has the ability to mitigate catastrophic forgetting problem in continual learning of LLM, since it can adapt LLMs for unseen tasks at inference time by adjusting the singular components of their weight matrices.

### Weaknesses
1.	To demonstrate the effectiveness in parameter efficient finetuning domain, the experimental results are not sufficient as the paper only compares with Lora, which suffers from overfitting in their experiments. How about other parameter-efficient finetuning baselines, like Prefix Tuning, Prompt Tuning, DoRA, BOFT? Specifically, the comparison with LoRA is not convincing since LoRA, with its larger number of trainable parameters, should have the capacity to fit the target tasks better than the proposed method, unless overfitting occurs. The paper needs to clarify whether early stopping was used for LoRA to mitigate overfitting, and if so, how the early stopping strategy was determined and if it was consistent with the proposed method. Furthermore, the lack of comparison with other parameter-efficient methods like Prefix Tuning, Prompt Tuning, DoRA, and BOFT makes it difficult to assess the true novelty and effectiveness of the proposed approach.
2.	The proposed method costs more time at inference time since it needs to make inference twice to get the final generated results. Particularly, for Few-shot adaptation, it needs to perform up to 100 CEM iterations, which costs significantly more time than normal inference. The paper should provide a detailed analysis of the inference time overhead, including the time taken for both the initial task identification pass and the subsequent inference pass. This analysis should also consider the computational cost of the CEM iterations in the few-shot adaptation scenario, and how this cost scales with the number of iterations and samples. A comparison of the total inference time with other methods would be beneficial.

### Questions
1.	For evaluation, is one model with three sets of “singular vectors” utilized for all three tasks(i.e., MATH, Humaneval, ARC-Challenge) for proposed methods? For Lora, three models are selected for three tasks, respectively?
2.	It looks that the proposed method has the ability to mitigate catastrophic forgetting problem in continual learning of LLM. The author may also consider exploring this direction to underline the contribution of this work further. (This is just a suggestion.)

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Transformer2, a self-adaptive framework that enhances the adaptability of LLMs for unseen tasks in real-time. It introduces a parameter-efficient approach by adjusting only the singular components of their weight matrices. The inference is a two-pass mechanism which first identifies task properties, and then dynamically combines task-specific expert vectors. The expert vector is trained by reinforcement learning to generate task-specific response. Proposed method is shown to outperform existing parameter-efficient tuning methods like LoRA, demonstrating efficiency and versatility across different LLM architectures and multimodal tasks.

### Strengths
- Transformer2 introduces a parameter-efficient adaptation method that selectively tunes only singular components, reducing computational demands compared to full fine-tuning approaches.
- The use of a two-pass mechanism to dynamically adapt model responses enhances the real-time adaptability of LLMs for unseen tasks.
- Training expert vectors with reinforcement learning enables the model to tailor its performance, leading to improvements in task-specific outputs.
- The framework is adaptable to various LLM architectures and applicable to vision-language tasks, showcasing broad utility.

### Weaknesses
 - While the paper proposes novel methods, the description of how these components interact and integrate in practice could be clearer. Specifically, the paper lacks a detailed explanation of the information flow between the task property identification module and the dynamic expert vector combination mechanism. It's unclear how the identified task properties are encoded and used to select and combine the appropriate expert vectors. A more concrete example, perhaps illustrating the process with a specific task and its corresponding expert vector selection, would significantly enhance the reader's understanding.
- While the use of reinforcement learning to train expert vectors is an innovative aspect of the framework, it introduces significant computational overhead and complexity. This can potentially undermine the paper's claims of efficiency and raises the question of whether these additional costs were considered when comparing the method to others like LoRA. The experiments should include a detailed breakdown of this computational expense to provide a clearer picture of the method's practical applicability and efficiency. The paper should also clarify the specific RL algorithm used, the reward function, and the training procedure for the expert vectors. Without these details, it's difficult to assess the reproducibility and practical feasibility of this approach.

### Questions
Refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a self-adaptive framework called Transformer$^2$ that learns and adapts external expert modules to downstream tasks in real-time. These modules can be used to augment LLMs for specific abilities and provide more flexibility than traditional post-training approaches that directly update the LLM weights. At training time, unlike existing methods that learn the expert modules via LoRA, this paper proposes a method called SVF that tunes only the singular values of a weight matrix to reduce storage and computational costs. At test time, the Transformer$^2$ framework requires two forward passes, one to gather test-task-related signals to select and combine the expert vectors, and one to actually generate the answer with the adapted LLM. Experiments on multiple open-source LLMs and datasets show that the proposed framework outperforms existing self-adaptive methods with reduced adaptation costs.

### Strengths
1. The idea of tuning singular values is novel and beneficial for reducing storage and computational costs.
2. The idea of learning a dispatch module using the LLM itself that determines which expert modules should be used at adaptation time is interesting .
3. Extensive experiment results show the efficacy of the proposed methods.
4. Good presentation.

### Weaknesses
1. I think ablation studies in B.1 should be moved to main text because it provides a better understanding of how each component of Transformer$^2$ contributes to the performance gain. Also, is it possible to provide results for LoRA + next-token prediction in Table 5? Ideally with both attention and attention+MLP. Currently it's hard to conclude that SVF with policy gradient does not sacrifice fine-tuning performance.
2. Scaling to a large number of abilities or specialized domains might be an issue for the few-shot adaptation scheme that uses CEM to search? The computational cost of CEM, especially with a large number of expert modules, could become prohibitive, making the approach less practical for real-world applications with diverse and numerous tasks. The search space for optimal combination weights grows exponentially with the number of experts, potentially leading to a significant increase in adaptation time and resources.
3. How should we reconcile the test time performance on coding in Figure 4? The performance seems to be decreasing over time and worse than non-adapted model. This raises concerns about the stability and reliability of the adaptation process, particularly on tasks with limited training data. The observed performance degradation suggests that the adaptation might be overfitting or failing to generalize effectively in certain scenarios.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

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
This work proposes a framework called $\text{Transformer}^2$ to enable self-adaptation in LLMs.
In the initial stage of $\text{Transformer}^2$, task-specific components of the pre-trained weights are determined by leveraging SVF,  a noverl parameter-efficient fine-tuning approach.
SVF is based on learning weights for singular values after SVD decomposition on pre-trained weights.
In the second stage, $\text{Transformer}^2$ performs test-time adaptation by leveraging a few samples of test data to infer how to select or mix the task-specific components.

### Strengths
- For the most part the paper is easy to follow and well written.

- SVF reduces the parameter-count compared to standard LoRA.

- $\text{Transformer}^2$ can adapt quickly to the holdout test tasks.

- Compelling results for cross-model compatibility of task-specific components.

### Weaknesses
 - **Weak and missing baseline results**

Most results for LoRA in Table 1 show worse results than the base model, how is this possible? In [1], for example, LoRA even outperforms full fine-tuning on MBPP. A performance drop after fine-tuning indicates that something went wrong with LoRA fine-tuning, maybe suboptimal hyperparameters?  [2] demonstrates importance of learning rate (higher is often better for LoRA), [3] demonstrates sensitivity w.r.t. scaling parameter, maybe there is an issue there? Also, there is no additional info given on the rank used for LoRA and to what weight matrices LoRA is applied to, smaller rank may perform better on smaller datasets.
There have also been advances for LoRA in terms of initialization [1,4,5] that have shown to improve upon LoRA and should be considered.

Another missing baseline is IA3 [6] which is conceptually very similar to SVF as it inserts newly trainable scaling vectors in the model. Especially in scarce data regime, IA3 has shown improvements over LoRA, therefore it should be included in the paper. Finally, the MoE approaches are similar to SVF and there are extensions for LoRA [7], but those are not compared to either.

- **Fair Comparisons**

There is no fair baseline comparison for $\text{Transformer}^2$, as it leverages test samples.
For example, $\text{Transformer}^2$ (Cls-expert) and $\text{Transformer}^2$ (Prompt) leverage two forward passes, one to determine the class and another one for generation. Can the authors clarify if this additional forward pass is required for each test sample?

 $\text{Transformer}^2$ (Few-shot) even leverages few-shot exemplars of the test set for determining the weighting factors $\boldsymbol{\alpha}_k$.
Therefore a fair comparison would require the baseline to use an equal amount of compute as the $\text{Transformer}^2$ variants during inference.
To this end, I would suggest fine-tuning the pre-trained IA3 vectors on the few-shot exemplars.

Another missing comparison is to exchange SVF for the second stage with another PEFT method, e.g. LoRA, or IA3, that were trained via SFT.
This would give important insights no the necessity of SVF in combination with RL as PEFT method for the first stage.

- **Limitations**

The authors claim that $\text{Transformer}^2$ enables self-adaptive LLMs, even though a lot of components are handcrafted in their framework, i.e. reward function, number of pre-defined classes, training on a number of datasets associated with pre-defined classes, determining of weighting factors by repeated sampling. This limits applicability of the proposed framework and also questions to what extent $\text{Transformer}^2$ is truly self-adaptive. Therefore, I would suggest to caveat the claims on self-adaptiveness and discuss the mentioned limitations.

$\text{Transformer}^2$ is limited to information the LLM has obtained during pre-training, i.e. it will not work on tasks that have not been observed during pre-training. While the authors have mentioned in the conclusion that model-merging techniques may be used to overcome this issue, this is impracticable as it requires searching and applying SVF on other pre-trained models until a suitable task-specific component is found. This is a fundamental limitation of $\text{Transformer}^2$ which makes it less practical.
Another limitation that should be made more explicit is the dependence on architecture for cross-model experiments - if architecture differs this is not possible anymore.

* **Overclaiming:**
  * Claims on overfitting: 
    * line 77: "our approach mitigates the risk of overfitting" - figure 4 learning curves show otherwise
    * line 339: "highlighting the particular effectiveness of our proposed fine-tuning recipe in narrow spe-
cialized applications." - the smallest dataset is MBPP where SVF only performs better on Mistral
  * line 332: "SVF effectively fine-tunes to surpass the base performance." - figure 4 curves on coding and reasoning show otherwise
  * line 350: "all of our $\text{Transformer}^2$ adaptation strategies demonstrate improvements across all tasks for both LLAMA 3-8B-INSTRUCT and LLAMA 3-70B-INSTRUCT base models" - not true for LLAMA 3-70B-INSTRUCT on Math
  * line 355: "LoRA’s parameterization and optimization might be particularly sensitive to overfitting, especially when trained with the smaller GSM8K and MBPP-Pro datasets" - GSM8K is an order of magnitude larger than MBPP
  * line 364: "$\text{Transformer}^2$ with few-shot self-adaptation is always the highest-scoring method, providing notable improvements across all tested settings" - not true for LLAMA 3-70B-INSTRUCT on Math
  * line 408: "$\text{Transformer}^2$ could provide foundation models with new means to continually improve performance when deployed in lifelong settings." - not true if new task is not represented in the base models' weights
  * line 418: "Furthermore, they also show that using the classification expert consistently provides higher classification accuracy than vanilla prompt engineering." - not shown for LLAMA 3-70B-INSTRUCT
  * line 476: "we first proposed SVF, offering superior performance than prior fine-tuning recipes, together with reduced costs, high compositionality, and overfitting regularization" - there is evidence in figure 4 for overfitting

I recommend rephrasing the above examples which, as far as I can see, are cases of overclaiming.

### Questions
- Why is $\text{Transformer}^2$ bound to SVF as PEFT method, can it not be used with other ones, e.g. LoRA, IA3, etc.?
- Figure 7 shows approximately uniform weighting of components works well for Llama-3, how does uniform weighting work in general? This would be an insightful ablation study.
- line 252: "we find the regularization properties of SVF avoid many of the failure modes of prior less-constrained parameterizations" - What failure modes of RL in particular does SVF remedy?
- line 253: "Thus, combining these complementary components effectively enables us to avoid relying on expensive fine-tuning procedures with large hand-designed datasets as proxies, and directly maximize task performance end-to-end." - Why is this only a benefit of SVF, as it can be applied to LoRA as well? 
- How expensive is the reward labelling prior to RL finetuning?

### Soundness
2

### Presentation
3

### Contribution
2

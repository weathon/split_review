# Mitigating the Influence of Distractor Tasks in LMs with Prior-Aware Decoding

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
The broad capabilities of Language Models (LMs) can be limited by their sensitivity to distractor tasks: LMs can infer secondary tasks from the prompt in addition to the intended one, leading to unwanted outputs. For example, prompt injection attacks can cause models to deviate from explicit directives. In some ‘inverse scaling’ cases, this unwanted behaviour actually worsens as models scale up to at least 540B parameters. We present a theoretical framework that interprets LMs as a product of experts that combine multiple data generation processes. Based on this framework, we introduce prior-aware decoding (PAD) -- a simple contrastive inference method to reduce the influence of distractor tasks. We apply PAD to eleven models, across four datasets, and find improvements in 41 out of 44 task-model combinations, with a median increase in task completion proportion of 40$\%$. The results suggest a promising direction for further development towards more reliable language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of mitigating the influence of distractor tasks in Language Models (LMs), which can result in undesirable outputs. The authors characterize LMs as a product of experts, where the predictions of multiple component models are combined. Based on this framework, they introduce Prior-Aware Decoding (PAD), a contrastive inference method aimed at diminishing the impact of distractor tasks.

The paper's contributions include: 
- Providing an interpretation of language models as a product of experts to elucidate how distractor tasks lead to suboptimal performance.
- Proposing the PAD method, which involves generating logits from both the original prompt and a "weakened" prompt, and subsequently combining these logits through a linear combination.
- Conducting evaluations of PAD across 11 models and 4 datasets, demonstrating its improved performance.

### Strengths
- The paper characterized language models as a product of experts, which is an insightful approach to understanding the influence of distractor tasks. The proposed PAD method is a contrastive inference technique that addresses a critical challenge in the LM generation.
- The authors tested the PAD method across 11 different models and 4 diverse datasets, providing evidence of its effectiveness. 
- The paper is well-written and structured. The authors explain the PAD method, including descriptions of the experimental setup and results.
- This work is important in the domain of LM generation, especially as prompt-based interactions with LMs become more prevalent. Mitigating distractor tasks could help address real-world issues like prompt injections, which have implications for LM deployment in safety-critical applications.

### Weaknesses
 - Although the paper is well-written, certain aspects of the PAD method's description could be clearer. For example, the process of generating the "weakened" prompt and the rationale behind the specific linear combination used could be elaborated further.

 - They mention that their split of prompts into task/data components was unambiguous because of the tasks they selected (Line#354-355). However, splitting prompts into task/data components isn't always straightforward. And they didn't address how to handle ambiguous cases.

 - While PAD is proposed as a contrastive inference method, the specifics of the contrastive mechanism remain somewhat abstract. Expanding the mathematical formulation of PAD could clarify the contrastive steps involved, enhancing the understanding. Since contrastive methods can be sensitive to parameters (e.g., scaling factors in logits), providing insights into how these were optimized across datasets and models would help clarify PAD’s robustness across settings.

 - The evaluation focuses heavily on inverse scaling tasks, but distractor tasks can manifest in many other ways.
    - Real-world prompt injection attacks
    - More complex multi-step reasoning tasks
    - Tasks where the distinction between intended and distractor tasks is less clear

	Apart from that evaluation on more complex or noisy datasets might exhibit different behaviors under distractor influences. A discussion on how PAD handles varying levels of dataset complexity, as well as an extension of experiments on noisier or user-generated data, would enhance the applicability of the findings.

 - A discussion on PAD’s limitations—particularly whether it might fail with certain prompt structures or in multitask settings where distractor and primary tasks are closely interwoven—would provide a more balanced view of the technique’s practical applicability.

 - The paper mentions 3 cases where α=2 performs worse but doesn't analyze. It should provide detailed case studies of failure modes to help users understand when PAD might not be appropriate.

 - The PAD method requires two forward passes through the model, but the computational impact isn't discussed.

### Questions
1. Can you provide an analysis of the failure cases where PAD does not perform as expected? Understanding these cases could offer insights into the limitations of your method and suggest areas for further improvement.

2. The paper mentions that prompt splitting was "unambiguous" for your selected tasks. What about cases where the split is less clear? Could you provide guidelines for creating effective splits? Have you tested automatic methods for determining splits apart from regex?

3. What is the rationale behind the specific linear combination used to combine the logits from the original and weakened prompts? 

4. The paper mentions prompt injection attacks as an example of distractor tasks. How effective is PAD specifically in handling adversarial prompt injections? Have you tested PAD’s robustness to adversarial prompts designed to bypass typical model safeguards? 

5. Contrastive methods in LMs can sometimes lead to less diverse outputs due to stricter filtering. Have you measured whether PAD reduces diversity or creativity in model outputs, particularly in open-ended tasks?

6. Did you experiment with PAD in conjunction with other prompting techniques (e.g., chain-of-thought prompting, few-shot examples)?

### Soundness
2

### Presentation
2

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
The paper aims to mitigate the distraction problem of LLMs, where LLMs pick up on a secondary task from the prompt instead of focusing on the intended task. The authors represent an LLM as a product of an expert model and propose a contrastive inference method to reduce the influence of distractor tasks. The effectiveness of the proposed method holds for multiple LLM-task combinations spanning eleven models and four datasets.

### Strengths
1. The problem addressed by the paper is important, and it is described clearly in the paper. Distraction of LLMs due to prompt misinterpretation affects LLMs of various sizes. Mitigating this issue has wide-ranging applications.

2. The proposed method is simple and described with adequate details, which helps reproducibility. The authors plan to make the code and dataset available, which is also helpful.

3. The experiment is performed using 44 different LLM-task combinations, which demonstrates the robustness of the proposed improvement.

### Weaknesses
1. The paper lacks clarity regarding the novelty of the work compared to existing works for mitigating LLM distraction. What are the prior methods used by people to mitigate LLM distraction? It would be helpful to cite those works if there are any. If this is the first work in this direction in any sense, you can mention that too.

2. The experiment does not have strong baselines. Having a baseline based on prior methods of mitigating distraction would be very helpful. For example, what is the performance of a simple prompt-based baseline for distraction handling? The proposed method seems to assume that the portion of the prompt that leads to distraction is already known. In that case, we can design a baseline method where a simple instruction is added to the LLM prompt. The added instruction will specifically ask the model to avoid the distracting task.

3. What is the additional cost or added limitation of using the proposed contrastive method in terms of text diversity or fluency? It would be helpful to know if the system loses any desirable property due to contrastive decoding and to the extent this happens. This will add clarity to the cost-benefit analysis of the proposed method.

### Questions
See weaknesses 2 and 3.

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
3

### Summary
This work proposes a framework for decoding with priors to mitigate the problem of distractor tasks. The distractor tasks are those which could be performed mostly well without considering the full context, e.g., the task description, and thus, causing inferior performances in general especially demanding inference considering long context. This work alleviate the issue by introducing the framework of product of experts by treating a language model $p_M$ as a product of true distribution with full context $p_C$ and a model without task description $p_L$, i.e., $p_M = p_C^{\gamma^*} p_L^{1 - \gamma^*}$. It results in approximating the true model by a product of two, i.e., $p_M^{1 +
\alpha^*} p_L^{- \alpha^*}$ where $\alpha^* = (1 - \gamma^*) / \gamma^*$. Experiments with several distractor tasks, e.g., prompt injection, show that the proposed method achieves gains when appropriately setting $\alpha$ value.

### Strengths
- It is an interesting approach for inference by combining two terms, one with a full task description and the other without the task description. The method could be interpreted as scaling the model prediction $p_m$ by the ratio of the model without task description $p_M / p_L$.

- Experiments are carried out on several open models, e.g. Llama 2 GPT2, and proprietary models, e.g., GPT-3.5, presents gains when compared with inference without biasing by the scaling term.

### Weaknesses
 - The motivation of introducing the product of experts is not clear as a purpose to represent the model distribution with the product of two, true distribution and a model without a task description. It is more straightforward to represent the true distribution by the product of the model distribution and he model distribution without a task description.

- It is not clear how decoding is performed for the proprietary models, e.g., GPT-3.5, given that it demands taking product of two models during inference.

### Questions
- The motivation is not very clear to me to introduce the product of experts .It is very easy to understand the awareness of the prior, but it is not clear how that is related to the model by the product of expert.

- It is not clear how decoding is performed for the proprietary models, e.g., GPT-3.5, given that it demands taking product of two models during inference.

### Soundness
2

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
4

### Summary
This paper investigates the "inverse scaling" issue in language models (LMs), where model performance deteriorates on the intended instruction due to interference from distractor tasks. To address this, the authors propose a theoretical framework that models LMs as a "product of experts", where one expert models the intended task and the other models the distractor task. Within this framework, they introduce _prior-aware decoding_ (PAD), a simple contrastive decoding strategy aimed at minimizing the influence of distractor tasks and improving adherence to the primary instruction. Extensive experiments conducted across multiple LMs and synthetic datasets validate the efficacy of PAD.

### Strengths
1. The proposed theoretical framework for addressing "inverse scaling" provides a novel and compelling perspective.
2. The proposed PAD method is well-integrated with the theoretical framework, demonstrating both simplicity and effectiveness in empirical evaluations. 
3. A well-structured related work section highlights the unique contributions of this paper and contextualizes it within existing literature.

### Weaknesses
1. The problem definition in Section 3 appears somewhat disconnected from the main theoretical framework and the PAD method. While the authors briefly touch on total variation distance (TVD, $\delta$) in Appendix D, a deeper analysis would be beneficial. Specifically, a more comprehensive discussion on the relationship between TVD, the selection of parameter $\alpha$, and the performance of PAD could help clarify how these concepts interact and contribute to mitigating the influence of distractor tasks. This additional insight would enhance the theoretical rigor and provide a clearer link between the foundational theory and the practical implementation.
2. According to Appendix D, the $\epsilon$-$\delta$ definition in Section 3 serves as a sufficient, but not necessary, condition for identifying strong priors. However, its reliance on a strict separation between the task description $T$ and the data $D$ limits its practical applicability, particularly in settings where this separation is not feasible. Consequently, this rigid definition may not effectively guide the identification of distractor tasks in realistic scenarios. A more flexible approach to defining strong priors could better support the detection of distractor tasks and enhance the effectiveness of PAD in mitigating their influence.
3. The real-world applicability of the proposed method raises some concerns. While the authors present an alternative implementation using system prompts in Appendix C, the resulting performance gains appear limited. Additionally, the experiments predominantly rely on synthetic tasks, where strong local prior assumptions are likely to hold, which may not translate to more complex, real-world scenarios. Expanding the evaluation to include more diverse, general datasets could help to better demonstrate the robustness and effectiveness of PAD under real-world conditions, thus strengthening the paper’s practical contributions.

### Questions
Questions:

Figure 1 is somewhat confusing, as it appears to show three experts, with the logits of these experts varying with different values of $\alpha$. Redrawing this figure with only two experts, as outlined in the proposed "product of experts" framework, would make it more consistent with the PAD method and easier to interpret. Additionally, emphasizing the contribution of each expert to the overall output could improve clarity, helping readers better understand how PAD balances intended and distractor tasks through $\alpha$.

Typos:

Line 129, missing period.

Format:

The table number and title should appear before the table.

### Soundness
3

### Presentation
3

### Contribution
2

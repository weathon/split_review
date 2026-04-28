# Instance Needs More Care: Rewriting Prompts for Instances Yields Better Zero-Shot Performance

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Enabling large language models (LLMs) to perform tasks in zero-shot has been an appealing goal owing to its labor-saving (i.e., requiring no task-specific annotations); as such, zero-shot prompting approaches also enjoy better task generalizability. To improve LLMs' zero-shot performance, prior work has focused on devising more effective task instructions (e.g., ``let's think step by step'' \cite{kojima2022large}). However, we argue that, in order for an LLM to solve them correctly in zero-shot, individual test instances need more carefully designed and customized instructions. To this end, we propose PRoMTd, an approach that rewrites the task prompt for each individual test input to be more specific, unambiguous, and complete, so as to provide better guidance to the task LLM. We evaluated PRoMTd on eight datasets covering tasks including arithmetics, logical reasoning, and code generation, using GPT-4 as the task LLM. PRoMTd consistently outperforms traditional zero-shot approaches on all the datasets. Notably, we observe an absolute improvement of 10\% on the complex MATHS dataset and 5\% on the code generation task on HumanEval. In addition, we also showed that the rewritten prompt can provide better interpretability of how the LLM resolves each test instance, which can potentially be leveraged as a defense mechanism against adversarial prompting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose to rewrite a specific prompt for each test point by prompting GPT4 with demonstrations that show how to rephrase a bad prompt into a better one with a rationale and task type. With the refined prompt, we can achieve better zero-shot performance on several benchmark datasets than other relevant baselines including zero-shot Chain-Of-Thought. Moreover, such prompt rewriting method generalizes to refine tasks that are not included the demonstrations.

### Strengths
- The proposed method is simple and effective. It rewrite a prompt into clear, specific, complete and more structure prompts, which leads to improved performance.

- For rewriting a prompt, we need 10 demonstrations, which is really practical for real-world applications.

- The authors performed human evaluation to verify that the quality of the rewritten prompts becomes better.

- The authors performed ablation study to show that task type and reasons are crucial component for prompt rewriting.

### Weaknesses
 -  Compared to zero-shot prompt models, it requires extra forward pass of LLMs to rewrite a prompt. It would be better to show how much more computational cost is required than other baselines.

- It is not clear such GPT4 written prompt would be transferred to other LLMs such as Llama.

### Questions
Please see weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses a significant challenge in the application of large language models (LLMs) to zero-shot tasks – the design of task prompts that are sufficiently informative and unambiguous to guide the model to the correct solution without task-specific annotations. The authors propose PROMPTD, an innovative approach that generates customized prompts for each test instance by designing some pre-defined prompts, enhancing the LLM's ability to handle tasks across various domains including arithmetics, logical reasoning, and code generation.

### Strengths
1. The idea of dynamically rewriting prompts for individual instances is a novel and interesting approach that represents a significant departure from the more static strategies employed in prior works.

2. The reported results indicate that PROMPTD provides a substantial boost in performance, achieving an improvement of 10% on the MATH dataset and 5% on the code generation tasks in HumanEval, which is impressive and suggests that the approach has practical value.

3. By applying PROMPTD across eight different datasets, the authors demonstrate the method's general applicability, an essential characteristic for real-world deployments.

4. The paper presents an additional benefit of using PROMPTD – the rewritten prompts not only aid in task resolution but also enhance the interpretability of the LLM's decision-making process, which could be crucial for trust and reliability in AI systems.

### Weaknesses
1. The paper does not sufficiently discuss the computational overhead of the PROMPTD method. Since the approach involves generating custom prompts for each instance, there may be a significant increase in the computational cost that could limit its scalability. More importantly, the PROMPTD is quite long; can the authors make some ablation studies about it?

2: The efficacy of PROMPTD is likely highly dependent on the initial quality of the prompts it is based upon. The paper could better address how the system performs with suboptimal base prompts and the robustness of the method to variations in prompt quality.

3: While the performance improvements are impressive, the evaluation might benefit from a deeper analysis of where and why the approach fails. Understanding the limitations of PROMPTD is as important as understanding its strengths.

4: There have been so many zero-shot prompting methods recently. The paper would be strengthened by including a more comprehensive comparison with the recent state-of-the-art methods for zero-shot learning.


5. The evaluation of PROMPTD on a single new task type (sentiment classification) is a significant limitation. Given the length and complexity of the original PromptD, it is unclear how well the method would generalize to other task types. The reviewer's expectation of a more general prompt applicable to a wide array of task types is unmet. This is a critical aspect, as the creation of highly specialized prompts may not be feasible in many real-world applications.

### Questions
Same as before

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the quailty of prompts and how to improve them for better capabilities of zero-shot and few-shot in-context learning. To ahieve this, authors first define the characteristics that good prompts should have, and then proposes a method to rewrite prompts to improve their quality based on this. Effectiveness is evaluated on mathematical reasoning, code generations and those tasks in BigBench.

### Strengths
I think the tageted issue, i.e., the quality and improvements of prompts, is currently needed by both the industrial and academic communities. Improving the zero-shot or few-shot in-context learning ability of large-scale models by improving the quality of prompts still has extremely high research value in the short term. This work could be viewed as a start point for this aspect.

However, we have to realize that the research space in prompt engineering also reflects the shortcomings of the current large models. The improvement of large models in the near future will be reflected in their stronger robustness to prompts. I suggest researchers to look at this issue with a more long-term developmental perspective, instead of being satisfied with the immediate results.

### Weaknesses
I very much agree with the starting point of this article, but at the same time, I regret that this research work lacks the necessary depth. From the definition of the quality of prompts to the method of improving the quality of prompts, most of the content is confined to quantitative analysis, lacking more in-depth and specific method design. There is also no larger scale quantitative evaluation on more general downstream tasks. For readers, it is somewhat difficult to catch the technical insights and contribution so that the current version seems premature.

### Questions
Could you further clarify how you rewrite the prompts and clearly hightlight the insights in them?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

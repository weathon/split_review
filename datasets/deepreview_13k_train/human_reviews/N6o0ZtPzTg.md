# Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
In this study, we aim to enhance the arithmetic reasoning ability of Large Language Models (LLMs) through zero-shot prompt optimization. We identify a previously overlooked objective of query dependency in such optimization and elucidate two ensuing challenges that impede the successful and economical design of prompt optimization techniques. One primary issue is the absence of an effective method to evaluate prompts during inference when the golden answer is unavailable. Concurrently, learning via interactions with the LLMs to navigate the expansive natural language prompting space proves to be resource-intensive.
To address this, we introduce Prompt-OIRL, which harnesses offline inverse reinforcement learning to draw insights from offline prompting demonstration data. Such data exists as by-products when diverse prompts are benchmarked on open-accessible datasets. With Prompt-OIRL, the query-dependent prompt optimization objective is achieved by first learning an offline reward model. This model can evaluate any query-prompt pairs without accessing LLMs. Subsequently, a best-of-N strategy is deployed to recommend the optimal prompt. Our experimental evaluations across various LLM scales and arithmetic reasoning datasets underscore both the efficacy and economic viability of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to enhance the arithmetic reasoning ability of LLM via prompt optimization. Inspired by the fact that no prompt is perfect for all queries and existing online evaluations of different prompt choices are expensive, this work proposes an offline RL based prompt optimization solution. Given the existing human crafted prompts for different arithmetic reasoning datasets, a reward model without depending on LLM is trained to approximate the prediction by using LLM. Experimental evaluation on multiple arithmetic reasoning dataset with 3 different LLMs shows a strong performance.

### Strengths
This manuscript addresses a compelling issue, namely the optimization of query-dependent prompts, which is becoming increasingly relevant as Large Language Models (LLMs) see wider application across various contexts. Developing an efficient prompt strategy tailored to individual queries, without relying on costly LLM inference, is a pertinent and significant challenge. 

The method put forward is both technically robust and effectively articulated. The authors have offered a comprehensive account of their approach, with a few exceptions (see below) The empirical outcomes presented are robust and offer a positive indication of the method's potential. 

Moreover, the analysis and ensuing comparison with pertinent literature succinctly underscore the advantages and novel contributions of this research.

### Weaknesses
How does the proposed method perform when the offline prompt-alignment dataset is small? It is encouraging to observe that the method shows promise with the 10 held-out prompts and an expanded set of 100 prompts. Nevertheless, in real-world scenarios, we may encounter new tasks with a limited number of available prompts for offline data. I am curious about the method's performance across various quantities of training prompts.

Several critical technical details are absent from the main text. For example, there is little to no information about the curated offline dataset or the design principles behind the parameterized proxy reward model, among others.

Following these points, it's also vital to explore and articulate the different design choices for reward models. It is mentioned that an MLP model is less effective, yet a detailed analysis would be invaluable, assisting the reader to understand and tailor the method to their specific use cases.

Regarding the proxy reward model, a simpler, more straightforward query-dependent model, such as a nearest-neighbor based solution, could be considered. This would involve, for each query, locating the closest match whose prompt yields a correct answer and utilizing that prompt for the new query. Please consider incorporating this simpler solution as a baseline for comparison.

### Questions
What are the values of K, M and P in appendix section C.1?

### Soundness
4 excellent

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
This work proposes to optimize/choose prompts on a per-query basis to improve LLM performance on arithmetic reasoning tasks. They first identify two challenges towards this objective: a) ground truth labels are missing at inference time, making prompt evaluation challenging and b) repeated LLM interactions are costly. To overcome both of these challenges they propose Prompt-OIRL, an offline inverse reinforcement learning approach to learn a reward function per model and dataset, predicting the success of a  prompt query pair. They demonstrate empirically that this approach outperforms a range of baselines and can improve LLM performance.

### Strengths
* The query-dependent prompt optimization setting is a novel and promising direction.
* Prompt-OIRL is both more accurate and precise at assessing prompt success than LMSC for held-out and seen prompts.
* The evaluation covers a range of 3 different tasks and models of different sizes.

### Weaknesses
 * Dataset generation requires a large number of model interactions for every new task and model, as no cross-task or -model generalization has been demonstrated.
* Many experimental details remain unclear or are only discussed in the appendix. E.g. the modelling of the proxy reward is not discussed at all in the main text, with the appendix suggesting a combination of an LLM embedding of prompt and query followed by an XGBT. The specific architecture of the XGBT, its hyperparameters, and the precise method for combining prompt and query embeddings are not detailed, making it difficult to assess the robustness of this component.
* It is unclear which single prompt was used for the scarce demonstration setting in Figure 5. Crucially, there, all baseline methods were limited to this single prompt, while Prompt-OIRL could choose any of the 6 considered prompts. Similarly, a comparison to always choosing each of the considered prompts and always choosing the best one (using an oracle) is missing but would be crucial to assessing performance. The lack of an oracle comparison makes it difficult to quantify the potential benefit of the proposed method.
* The failures of Prompt-OIRL (e.g. GSM8K with LLaMA or TigerBot (Figures 20 and 21)) where it performs worse amongst all considered methods by a large margin are only shown in the appendix. Ironically this section is titled "REWARD MODELING: IMPLEMENTATION MATTERS", suggesting it should be discussed in the main text. The absence of this discussion in the main text obscures the limitations of the approach.
* While the use of LLMs for embedding computation of prompts is unproblematic when choosing the best-of-n (with n=6) fixed prompts, it might be prohibitively expensive for different policy optimization approaches requiring a substantially larger number of prompts to be embedded. This should be highlighted more prominently and not presented as a major advantage of this method. The computational cost of generating and storing these embeddings, especially for large prompt sets, needs to be addressed more thoroughly.


### Questions
### Questions
1) Can you describe in detail the modeling of the proxy reward and conduct an ablation over the approaches mentioned but rejected in Appendix C.2
2) Can you report the performance of the (on average) best (on the test set) prompt and what this prompt is for the different models and datasets? Can you similarly report the performance of always choosing the best prompt for every query (corresponding to the setting where the proxy reward models the success flawlessly)?
3) How does Prompt-OIRL differ from  BoTr Eqn.2 when trained on all considered prompts? Its description suggests that also selects the best of n prompts but it achieves worse performance in Figure 6. 
4) How does performance depend on the training data-set size given that much smaller datasets with gold-standard annotations will be available for many real-world applications?

### Comments
* The paper could benefit from a careful copywriting pass that addresses typos and grammatical errors while homogenizing the writing style.
* Figure 7 would benefit from a relative scale, especially for the "Cost with Commercial APIs". It generally seems slightly misleading to report improvements when 100 Prompts are used here while the rest of the paper considers 6 prompts. Further, it remains unclear if or how the cost of embedding the prompts and evaluating the proxy reward is considered here.

### Conclusion
The paper presents query-dependent prompt optimization as an interesting and novel approach to improving LLM performance. While multiple models and benchmarks are considered in the empirical evaluation, details remain unclear and some baselines are missing, eroding the confidence in the presented improvements. Combined with the missing details on the exact modeling of the proxy reward as well as any ablation of this key component, I am leaning toward rejecting this paper.

### Post Rebuttal Update
I have raised my score in response to the detailed rebuttal addressing my questions satisfactorily. I believe the paper could further benefit from incorporating some of these results, presented during the rebuttal.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new method called Prompt-OIRL to improve the arithmetic reasoning abilities of large language models (LLMs) through zero-shot prompt optimization. They identify query dependency as an important objective in prompt optimization, but current techniques face two key challenges: 1) the lack of effective methods to evaluate prompts without access to the golden answers, and 2) the high computational cost of exploring the vast prompt space through interactions with the LLM. To address these issues, Prompt-OIRL utilizes offline inverse reinforcement learning on existing prompting benchmark data to learn a prompt evaluation model without needing the LLM. This model can then efficiently recommend optimal prompts in a best-of-N fashion for new queries. Experiments across various LLM scales and math datasets demonstrate Prompt-OIRL's efficacy and cost-effectiveness for zero-shot prompt optimization with query dependency.

### Strengths
1. The paper is well-structured and easy to follow 
2. The idea is very interesting and the topic is important for automatic prompt engineering 
3. Query-dependent evaluation is an essential challenge that is typically ignored. The authors identify this unique issue and solve it by proposing an RL framework, which looks very promising. 
4. The experiments are strong enough to support the claims by comparing them with multiple SOTA baselines.

### Weaknesses
1.  While the method looks promising, I still expect to see potential discussion about the limitations, e.g., stability of inverse RL？ 
2. The scope is limited by arithmetic reasoning but the title seems a more generic framework that can be used to solve more broader tasks across different NLP tasks. 
3. What's the current bottleneck if the proposed framework is applied to other instruction prompt optimization tasks, listed in ORPO[1], APE[2], and APO[3] baseline methods? 
4. Without query dependence, what's the performance drop? Can you prove the necessity of that？
5. What's the current computational cost of the proposed framework？  
6. Is that possible to compare with the GPT-4 or PaLM 2 model as well？

### Questions
see weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an “offline” (not using LLM as evaluators or prompt searchers) method to search effective “query-level” prompts. This method can potentially reduce the cost of prompt searching for enhancing the arithmetic reasoning ability of LLMs.

### Strengths
In the “offline” setting, this paper conducts relatively thorough experiments and ablations to find the optimal method.

### Weaknesses
However, my main concern is that it lacks a very important comparison with “on-line” methods. If the proposed method can achieve similar (or just a little bit lower) performance compared with “on-line” methods and it is significantly cheaper, it would be a good evidence that the proposed method can potentially be useful practically.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

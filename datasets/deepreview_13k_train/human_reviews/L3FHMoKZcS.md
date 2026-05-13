# Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Prompting and in-context learning (ICL) have become efficient learning paradigms for large language models (LLMs). However, LLMs suffer from prompt brittleness and various bias factors in the prompt, including but not limited to the formatting, the choice verbalizers, and the ICL examples. To address this problem that results in unexpected performance degradation, calibration methods have been developed to mitigate the effects of these biases while recovering LLM performance. In this work, we first conduct a systematic analysis of the existing calibration methods, where we both provide a unified view and reveal the failure cases. Inspired by these analyses, we propose \emph{Batch Calibration} (BC), a simple yet intuitive method that controls the contextual bias from the batched input, unifies various prior approaches, and effectively addresses the aforementioned issues. BC is zero-shot, inference-only, and incurs negligible additional costs. In the few-shot setup, we further extend BC to allow it to \emph{learn} the contextual bias from labeled data. We validate the effectiveness of BC with PaLM 2-(S, M, L) and CLIP models and demonstrate state-of-the-art performance over previous calibration baselines across more than 10 natural language understanding and image classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the issue of bias and unexpected performance degradation in large language models (LLMs) when using prompting and in-context learning (ICL). To address this, the authors first provide a comprehensive analysis of existing calibration methods and their decision boundaries, and then propose a new calibration method called Batch Calibration (BC) with linear decision boundaries, which mitigates the bias from the batched input and is both zero-shot and inference-only. BC can be easily extended to learn the bias from labeled data, and applied to calibrate vision-language models. The authors conduct extensive experiments on over 10 natural language understanding and image classification tasks and show that BC achieves state-of-the-art results.

### Strengths
1. The proposed Batch Calibration method is simple and empirically effective.
2. Extensive experiments are conducted.

### Weaknesses
1. The proposed method is not thoroughly justified.
2. The writings could be improved in terms of the analysis of existing methods and the proposed method.

3. The authors argued that linear decision boundaries produced by calibration methods can be more robust and generalizable across tasks. This argument is not well supported theoretically and empirically. 
4. The advantage of Batch Calibration over existing methods is not thoroughly justified. Could you provide more intuitive descriptions and theoretical analysis for it?
5. The derivations of Table 1 could be provided in more details in the main contents or supplementary. Currently, it is not easy to understand.

### Questions
1. The authors argued that linear decision boundaries produced by calibration methods can be more robust and generalizable across tasks. This argument is not well supported theoretically and empirically. 
2. The advantage of Batch Calibration over existing methods is not thoroughly justified. Could you provide more intuitive descriptions and theoretical analysis for it?
3. The derivations of Table 1 could be provided in more details in the main contents or supplementary. Currently, it is not easy to understand.

### Soundness
2 fair

### Presentation
2 fair

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
The paper delves into the current challenges faced in adapting Large Language Models (LLMs) to new tasks through the method of human-designed instructions. Although these models possess a commendable ability for in-context learning (ICL) and can efficiently adapt from few-shot input-label pairs, they are significantly influenced by the choice of templates, verbalizers, and demonstrations. This results in biases that can act as barriers to creating adaptable and robust LLM applications. While several studies have tried to address these biases, a holistic analysis differentiating the merits and demerits of each approach is lacking.

### Strengths
The paper provides a thorough and systematic examination of existing calibration methods for LLMs, filling a gap in the existing research landscape. Methodologically, the introduction of Batch Calibration (BC) offers a zero-shot, inference-only calibration method that is computationally efficient, addressing a primary concern in the domain. BC proves effective in reducing prompt sensitivity, a prominent issue in LLMs, thereby facilitating easier prompt engineering.

The scope is also broadened compared to previous works like CB, which only studies GPT-2's biases.

### Weaknesses
While BC introduces minimal computational overhead, in highly resource-constrained environments, even small overheads might be significant.

The term calibration can be confusing, maybe using bias is better. At least should add a footnote to the Introduction. Another widely used notion of calibration is from the perspective of uncertainty, explainability, and reliability.

Please include model sizes and details in the paper, as the performance of ICL and prompting is quite irreproducible and context-dependent.

Please adjust the margins of subfigures in fig. 2, it's overlapped.

The liteature review of Test time tuning is a bit unnecessary as ICL itself is not a tuning method

### Questions
In fig.5, why does a strength greater than 1 consistently decrease accuracy?

How significant is the bias/miscalibration of the ICL performance? that say is the problem still relevant for models with greater scales? 
Should consider 65B llama2, GPT-3.5, GPT-4 etc as the method does not require tuning

### Soundness
2 fair

### Presentation
4 excellent

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
This paper studies model calibration in the context of LLMs (large language models). The authors first analysed the recently proposed methods with empirical results, and they also discussed the two important design principles behind those ICL calibration methods. A novel calibration method (which is termed batch calibration) is then introduced for zero-shot learning; an extended version that has a hyperparameter is proposed for fine-tuning. The authors conducted extensive experiments on multiple NLP tasks and showed superior performance as compared to the existing ICL calibration methods.

### Strengths
1. This paper addresses an important and interesting topic: calibrating LLMs in zero or few shot settings.

2. The paper gives an overview of the most relevant and recent ICL calibration methods and discusses their motivations and design principles with empirical results. 

3. The experiments are extensive, and the proposed method achieves better performance on most tasks.

### Weaknesses
1. My main concern goes to the $\textit{strength}$ parameter in BCL; the current results show $\gamma = 1$ seems to give strong performance (though not optimal) across tasks on CB and SST-2. Does this generalize to other tasks as well? It would be good to provide the optimal $\gamma$ for each task; maybe include it in Table 2? Besides, would it be more reasonable to sample \gamma in [0, 5]? The paper does not sufficiently explore the sensitivity of the model to this hyperparameter across a wider range of tasks and datasets; it is unclear if the observed performance with $\gamma=1$ is a consistent finding or an artifact of the specific tasks chosen. The current range of $\gamma$ is also not justified, and a more comprehensive exploration of the parameter space is needed to understand its impact on model performance. The lack of a clear explanation of how the optimal $\gamma$ is determined for each task and why the chosen range is appropriate further weakens the analysis.

2. There are some statements that are not well presented or supported. In Sec. 4.3, the authors claimed BC retains the performance even when using emoji pairs as verbalizers. Is there an example or result related to this specific experiment? The claim that BC maintains performance with emoji verbalizers is not sufficiently backed by empirical evidence. The paper lacks a detailed analysis of the performance of BC with different verbalizers, and it is unclear if the observed performance is consistent across different emoji pairs or if it is specific to certain combinations. Without a more detailed analysis, this claim remains unsubstantiated and weakens the overall argument.

### Questions
1. In e.q.(3), how to obtain the contextual prior $\hat{\mathbf{p}}$? 
2. How would BC work on the task other than classification? 
3. It seems the calibration perform is not stable across different model architectures in 1-shot setting on some tasks. E.g., MNLI, 75.12/         60.02/81.34 for PaLM-2-S/PaLM-2-M/PaLM-2-L. I understand that PaLM-2-S/L are based on 5 runs and PaLM-2-M result is from a single run. Could you help to understand, what causes the high perform variance, I may miss something here.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a study on calibration methods for in-context learning. The authors provide a unified and systematic analysis of existing calibration, focusing on their decision boundaries. They also investigate the common use of content-free tokens in calibration. The paper highlights the biases in language models’ predictions and proposes Batch Calibration (BC) as a zero-shot and inference-only calibration method. BC aims to accurately model the contextual bias in prompt contexts by marginalizing the language model scores. The authors extend BC to black-box few-shot learning by introducing a learnable parameter to adapt to available labeled data. The performance of BC is evaluated and compared to baseline methods, showing improved performance in various tasks.

### Strengths
This paper is technically sound and well-written (although some writing issues are listed in weaknesses). The authors' revisiting of previous methods is novel to the research community.

### Weaknesses
- For writing:
    - "Survival of the Most Influential Prompts: Efficient Black-Box Prompt Search via Clustering and Pruning" has been accepted by EMNLP-2023. Please cite it correctly. 
    - Why is the related work in section 5? Introducing it in section 2 will make readers understand the background better.
    - Unify the usage of abbreviated words. Tab. -> Table.

- When introducing BCL, the author takes some examples to make readers understand the $\gamma$. I suggest authors provide more experiments on how different $\gamma$s affect the results. Specifically, it would be beneficial to see a sensitivity analysis of $\gamma$ across different tasks and datasets, as the optimal value might vary depending on the specific context. The current examples are insufficient to fully understand the impact of this parameter.

- As shown in Figure 3, the improvement from BC to BCL seems marginal. This raises questions about the practical significance of adding the learnable parameter $\gamma$. It would be valuable to analyze the scenarios where BCL provides a substantial improvement over BC, and conversely, when it does not, to understand the conditions under which BCL is most effective. The lack of clear performance gains in Figure 3 suggests that the added complexity of BCL might not always be justified.

- Any border impact and limitation discussion?

### Questions
See weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

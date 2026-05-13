# SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection

- Decision: Accept
- Scores: 6, 6, 5, 6, 6

## Abstract
Fine-tuning on task-specific data to boost downstream performance is a crucial step for leveraging Large Language Models (LLMs). However, previous studies have demonstrated that fine-tuning the models on several adversarial samples or even benign data can greatly comprise the model's pre-equipped alignment and safety capabilities. In this work, we propose SEAL, a novel framework to enhance safety in LLM fine-tuning. SEAL learns a data ranker based on the bilevel optimization to up rank the safe and high-quality fine-tuning data and down rank the unsafe or low-quality ones. Models trained with SEAL demonstrate superior quality over multiple baselines, with $8.5\%$ and $9.7\%$ win rate increase compared to random selection respectively on \textsc{Llama-3-8b-Instruct} and \textsc{Merlinite-7b} models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- Introduces SEAL, a novel bilevel fine-tuning framework that optimally balances fine-tuning data selection to enhance model safety, even when incorporating external non-safety-aligned data.

- Demonstrates SEAL’s robust performance improvements across diverse models and datasets, outperforming existing baselines in both safety and task-specific effectiveness.

- Provides a transferable and computationally efficient solution, with open-source code to support broader adoption and further research within the community.

### Strengths
I believe that the proposed fine-tuning methodology for enhancing LLM safety addresses a timely and critical issue in AI, making it a highly suitable topic for ICLR. 

Moreover, this method has the potential to extend beyond the safety domain, offering a general and versatile approach applicable to various key areas, thereby holding significant value for the broader AI community. 

The learning and evaluation code is transparently and accessibly provided, and with further refinement post-acceptance, it can greatly benefit researchers and practitioners through ICLR, fostering impactful contributions to the field.

### Weaknesses
(1)

Comment: One of the most significant weaknesses of this study lies in the lack of a fundamental explanation for why SEAL achieves performance improvements beyond using safety-aligned data alone. For instance, if the fine-tuning dataset consists entirely of non-safety-aligned data, it remains unclear why SEAL, when using 𝛾>0, would still mitigate performance degradation in safety compared to a setup with 𝛾=0. Ideally, both should yield comparable safety performance. To address this, the authors should provide comprehensive and detailed reasoning, supported by thorough analyses. Specifically, experiments varying the proportion of non-safety-aligned data from 0% to 100% should be conducted to illustrate how SEAL performs across different scenarios. This would demonstrate the method's robustness and technical validity, thereby satisfying readers and reviewers with a more rigorous and convincing evaluation.

(2)

Comment: The paper lacks a thorough investigation of similar approaches, such as bilevel optimization techniques applied to LLMs, and does not sufficiently highlight its relative novelty. Methods like self-supervised learning or unlearning can be viewed as forms of bilevel or similar hierarchical optimization.

### Questions
Please refer to my comment for Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a data selection algorithm to protect the safety alignment of the LLM model after supervised finetuning. The proposed method is based on a bi-level optimization process, where the data are ranked by a learned ranker, such that the data points aligning with the safe dataset receives a higher rank. Experiment results show the proposed metho achieves both improved safety and task performance comparing to full supervised finetuning and random selection on various models.

### Strengths
This paper investigates an important topic: safety alignment in the supervised finetuning process of the LLM. The problem is a valid concern and the proposed data selection method is well-motivated. Although data selection is not novel by itself, the proposed method appears to be more straightforward, computation-efficient, and more effective comparing to previous methods. Experiments are conducted on various datasets and models, showing the transferability of the selected data across the models and the generalizability across the dataset. The proposed method appears to be overall effective and useful.

### Weaknesses
One potential drawback of this paper is it assume the safe dataset is readily available in the supervised finetuning process. With the safe dataset available, a straightforward idea would be directly optimize the model with a combination of safe data and task data, as formulated in Equation (4). Since this model update is also performed in the data selector training anyway, it is unclear if the data selection is realy needed to achieve improved safety. Specifically, the bi-level optimization process, where the data selector is updated based on the model's performance on both the task and safety datasets, might not be necessary. The model update in the data selector training already incorporates the safety objective, making the separate data selection step potentially redundant. A key ablation study would be to evaluate the performance of directly using the pretrained safe-aligned model for loss compression, without further updating its weight in the data selection process. This would isolate the effect of the bi-level optimization and determine if it is truly essential for the observed improvements. On the other hand, from algorithm 2 the data selector update can be based on the current model weight only. This leads to another important ablation study that we use the pretrained safe-aligned model for the loss compression directly, without further updating its weight in the data selection process. These two aspects will show if the proposed bi-level optimization is truly important to achieve the desired performance.

Besides the issue with safe data usage, the comparison against baseline data selection methods are also on the weak side. Multiple related work are listed in Sec. 2 that perform data selection for LLM safety. Yet in the experiments, only 1 data selection method, DSIR, and one additional dataset method are compared as baseline. More explaination is needed on the difference and benefit of the proposed method comparing to previous data selection methods mentioned in Sec. 2. The paper should provide a more comprehensive comparison against other data selection techniques, especially those designed for safety, to better contextualize the contribution of the proposed method. The current experimental setup does not fully demonstrate the advantages of the proposed method over existing data selection strategies.

### Questions
1. Since a safe dataset is already availlable in the training, why not just train the model with the objective in Equ. (4) to balance safety and task objective, without further effort on doing data selection?

2. Why does the target domain win rate also improve as we select data based on safety alignment?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a security-enhanced fine-tuning framework for large language models, called SEAL, which aims to address the problem of negative impact on model security alignment during the fine-tuning process. By learning a data selector based on two-layer optimization, the fine-tuning data is ranked to enhance the weight of safe and high-quality data and reduce the weight of unsafe or low-quality data, thus enhancing the safety during the fine-tuning process. SEAL is tested on multiple models and datasets, and the results show its advantages in terms of validity, flexibility, and interpretability, and compared to baseline methods such as random selection, it has a improvement in the different models with a increase in win rate and maintains good performance with a range of data selection percentages, while the data selector is transferable and reduces computational complexity.

### Strengths
1. The paper proposes a security-enhanced fine-tuning framework named SEAL, specifically designed to mitigate the negative impacts on model security alignment during the fine-tuning process.
2. SEAL employs a novel two-layer optimization method to learn a data selector, which effectively ranks fine-tuning data. This process increases the emphasis on safe and high-quality data while reducing the influence of unsafe or low-quality data, thus improving fine-tuning safety.
3. The data selector used in SEAL is transferable across different contexts, reducing computational complexity and enhancing its applicability.

### Weaknesses
1. Lack of novelty. This paper presents a method for training data selectors and weighting losses, which is very straightforward. At the same time, the paper spends a lot of time on the optimization algorithm, but the optimization algorithm itself lacks improvement and innovation compared to the referenced papers. Overall, the article's approach lacks novelty, both in the idea itself and in the optimization method.
2. For all experiments, there was no adjustment for the variance of performance given after randomization of seeds. Especially for the randomized selection method, a large number of replicated experiments are necessary. Also, there are sampling methods for the generation of large language models, and randomness is introduced here as well. Overall, the lack of repeated experiments leads to unconvincing results.
3. Apart from the baseline chosen for this paper, I don't know why the authors didn't design additional but direct baselines, such as directly letting the model be given weights or rankings through the prompt engineering.
4. The results now lack insight, for example, the HEX-PHI data actually contains 11 categories, and it would be interesting to analyze the different categories in detail and explore the limitations of the sample selection algorithm, or an analysis on other benchmark tasks to explore the balance between security and performance would be insightful. A more in-depth analysis will help us better understand the effectiveness and flaws of the method, which is very meaningful.
5. LoRA introduces additional parameters, so it is difficult to directly attribute for performance improvements. Therefore, I believe that full parameter fine-tuning should be used for all methods. Also, the models do not perform well. Sometimes it is not even better than Random.

### Questions
See Weakness.

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
4

### Summary
This work aims to enhance the fine-tuning LLMs’ safety capabilities while maintaining downstream performance. Therefore, authors design SEAN, a novel believes optimization framework to up-rank safe and high-quality fine-tuning data while down-ranking unsafe or low-quality data.  LLMs trained with SEAL demonstrate superior quality over multiple baselines, achieving an 8.5% and 9.7% increase in win rates compared to random selection on the LLAMA-3-8B-INSTRUCT and MERLINITE-7B models, respectively.

### Strengths
1. The paper is well-organized, and the methods and experiments are easy to understand.
2. The work attempts to address the safety concerns arising from LLM fine-tuning strategies, which is a very interesting and valuable issue.
3. The method of bilevel optimization is well-suited to the proposed problem.
4. The experiments roughly demonstrate the validity of the proposed method.

### Weaknesses
1. It would be better to provide more results, such as ablation studies. For example, comparing the method of fine-tuning the selector alone would be useful.
2. Some experimental results are not sufficiently explained.

### Questions
1. Could you compare the results of training the selector and LLMs separately? It is intuitive that this method seems to be more effective.
2. Could you further explain the results in Figure 3 and Figure 4. I am confused about why the performance of SEAL on the SLIMORCA dataset is not always superior to the baseline DSIR (Sometimes even worse).
3. From the current results, it is difficult to know whether the win rate improvements of SEAL are due to enhanced safety or better performance on downstream tasks. Could you provide more explanation about which datasets focus more on safety evaluation versus performance evaluation? Additionally, can you present more distinguishable results to show the model comparisons in terms of safety and performance, respectively?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces SEAL, a novel framework to enhance safety for fine-tuning of large language models. Specifically, SEAL learns a sample ranker based on a bilevel optimization to up rank the safe and high-quality fine-tuning data and down rank the unsafe or low-quality ones. Extensive experiments on natural language processing benchmarks demonstrate the effectiveness of SEAL.

### Strengths
The research direction of this paper is crucial for safe model fine-tuning. The idea of the proposed SEAL seems to be simple and effective in addressing the issue of data ranking. The paper is well-written and easy to follow.

### Weaknesses
1. The reviewer noted a performance discrepancy between PEFT training for 7B models and full fine-tuning of 2.8B models. This might be due to the fact that only the k and v matrices are trained during PEFT training, which, while enhancing robustness to catastrophic forgetting, can amplify or diminish the impact of fine-tuning on safety. Therefore, It is  recommended that the authors conduct an ablation study comparing LoRA fine-tuning that incorporates weights in both the Feed Forward Network (FFN) and Multi-Head Self-Attention (MHSA) blocks with their current PEFT approach. Specifically, the current approach of only updating the k and v matrices might be insufficient to capture the full range of safety-related nuances present in the data. An ablation study should explore the impact of updating different combinations of weight matrices, such as only FFN, only MHSA, or both, to understand the optimal configuration for safety performance. Additionally, an analysis discussing how various LoRA configurations affect the safety-performance trade-off would be beneficial. This analysis should consider the rank of the LoRA matrices, as lower ranks might lead to underfitting while higher ranks could overfit or introduce instability. The trade-off between the number of trainable parameters and the achieved safety performance needs to be thoroughly investigated.

2. The author used the memory-efficient variant of SEAL by default in the experiments. To provide a more comprehensive understanding of the impact of this choice, I suggest the authors perform a quantitative comparison of memory consumption and performance between the standard and memory-efficient SEAL variants. Including a table or figure that illustrates this comparison would help clarify the effectiveness of both approaches. This comparison should not only focus on memory consumption but also on the computational time required for each variant. Furthermore, the performance should be evaluated across multiple metrics, including both safety and general performance metrics, to provide a holistic view of the trade-offs involved. The analysis should also discuss the scalability of each variant with respect to model size and dataset size, as the memory-efficient variant might be more suitable for larger models but could potentially sacrifice some performance.

### Questions
Please see the weakness section.

### Soundness
4

### Presentation
4

### Contribution
3

# Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Prompt Tuning adapts frozen models to new tasks by prepending a few learnable embeddings to the input.
However, it struggles with tasks that suffer from data scarcity.
To address this, we explore Cross-Modality Prompt Transfer, leveraging prompts pretrained on a data-rich modality to improve performance on data-scarce tasks in another modality.
As a pioneering study, we first verify the feasibility of cross-modality prompt transfer by directly applying frozen source prompts (trained on the source modality) to the target modality task.
To empirically study cross-modality prompt transferability, we train a linear layer to adapt source prompts to the target modality, thereby boosting performance and providing ground-truth transfer results.
Regarding estimating prompt transferability, existing methods show ineffectiveness in cross-modality scenarios where the gap between source and target tasks is larger.
We address this by decomposing the gap into the modality gap and the task gap, which we measure separately to estimate the prompt transferability more accurately.
Additionally, we propose Attention Transfer to further reduce the gaps by injecting target knowledge into the prompt and reorganizing a top-transferable source prompt using an attention block.
We conduct extensive experiments involving prompt transfer from 13 source language tasks to 19 target vision tasks under three settings.
Our findings demonstrate that:
(i) cross-modality prompt transfer is feasible, supported by in-depth analysis;
(ii) measuring both the modality and task gaps is crucial for accurate prompt transferability estimation, a factor overlooked by previous studies;
(iii) cross-modality prompt transfer can significantly release the powers of prompt tuning on data-scarce tasks, as evidenced by comparisons with a newly released prompt-based benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores several aspects of prompt tuning in cross-modality settings (e.g., vision and language), focusing on feasibility, transferability estimation, and performance improvement. Specifically, the authors validate that source prompts pretrained on text data can be safely transferred to tasks in a different modality. They also propose a better metric for transferability estimation, which takes into account both modality and task gaps. Finally, the paper introduces attention transfer techniques for cross-modality prompt transfer, which are shown to perform comparably to single-modality prompt tuning algorithms such as SPT.

### Strengths
* The motivation is good.
* The overall logic and flow of the paper are clear.
* The experiments are thorough, with a detailed exploration of various aspects of cross-modality prompt tuning.

### Weaknesses
 * Although the paper claims that cross-modality prompt transfer can boost performance in data-scarce tasks, this is not convincingly demonstrated in the experiments, particularly when comparing to the SPT baseline.
* The problem itself is interesting, and some findings, such as the proposed transferability estimation metric and the connection between single-modality and cross-modality prompt tuning, are valuable. However, the advantage of cross-modality prompt tuning over single-modality methods is not convincingly established.
* The proposed transferability metric seems somewhat complex. It requires training a universal projector across tasks, which may introduce additional training costs and overhead.
* The experiments lack strong evidence to show a clear advantage of cross-modality transfer, especially in data-scarce settings.

### Questions
1. What is the training cost associated with the proposed transferability metric? How does it scale with the number of tasks or modalities?
2. What is the distribution of modality and task gaps in practice? Is there a recommended threshold to select the source prompt for transfer, instead of choosing the best?
3. Could the paper provide more concrete evidence of improvements in data-scarce tasks using the proposed cross-modality transfer approach?
4. Is there a way to make the transferability metric more efficient, reducing the need for the universal projector?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores cross-modality prompt transfer, aiming to improve the performance of prompt-tuning methods when transferring prompts across different data modalities, specifically from NLP to CV tasks. The authors propose a novel approach using attention transfer and modality gap analysis to address data scarcity challenges in the target domain. Experiments on a wide variety of tasks demonstrate the feasibility and advantages of this cross-modality prompt transfer, highlighting the potential of leveraging rich source prompts for enhancing performance in data-limited scenarios.

### Strengths
- The paper is well-organized and clearly written.
- The paper introduces a new perspective in prompt transfer by exploring cross-modal prompt adaptation
- The authors conduct a thorough analysis of the modality and task gaps, which improves the understanding of transferability in cross-modal scenarios, offering valuable insights for future research .
- Attention transfer is proposed to mitigate modality and task gaps, offering an effective way to reuse and adapt prompts across modalities. 
- The paper provides substantial experimental evidence on multiple datasets, showing that cross-modal prompt transfer can yield performance comparable to, or even surpassing, recent prompt-based benchmarks .

### Weaknesses
 - The paper would benefit from additional comparisons with same-modality prompt transfer baselines, which would help quantify the specific impact of cross-modal transfer approaches.
- The approach seems sensitive to hyperparameters, which could affect reproducibility and performance stability, particularly in diverse target environments.
- There are instances where cross-modal transfer underperforms or fails, the approach's limitations should be further discussed.

### Questions
Although the paper provides theoretical and experimental support, practical applications, particularly real-world tasks where cross-modality transfer excels, are not thoroughly discussed. Besides, the method may face scalability issues when applied to larger models or when requiring complex attention transfer setups, which could limit its applicability in more resource-intensive settings .

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
- Prompt tuning has become a popular paradigm to adapt frozen models to new tasks. 
- While prompt-transfer within the same modality has shown to been helpful, the paper argues that this area has not been thoroughly explored. 
- The paper presents an analysis on feasibility of cross-model prompt transfer which is especially relevant for data scarce modalities. The paper studies various design choices through experiments and analysis.
- L205-208: To do so, the problem is split into modality and task-based gaps and these are quantified. A new approach called attention transfer is introduced to reduce this gap which helps in improving the benchmarks. One should not have to go to the appendix to understand the intuitions behind the approach.

### Strengths
- The paper proposes an interesting idea of transferring language prompts to vision for various data-scarce tasks. The idea is interesting and seems novel.
- The paper is easy to follow for the most part. 
- Experiments are thorough. Many different ablations are presented, various design choices are explored. 
- The results seem promising and show benefit of using the approach.

### Weaknesses
While the overall idea, experiments and findings could be helpful to the community, I have the following concerns with this paper: 

- It is unclear why you want to quantify prompt transferability (equation 6) given it is a function of hyperparameters, training data etc. It would be helpful to provide some intuitions. 
- L274: What was the motivation behind chosing a IN-21k pre-trained checkpoint chosen ? Why not 1k ? Why not a language aligned model like CLIP ?  
- Intuitions: Maybe I missed this in the paper, but a discussion on why should prompts be transferrable, what is the composition of the dataset where they transfer and where they don't will be very helpful to the reader.

### Questions
Clarity: 
- L106-107: Unclear from context. 
- The discussion on the hypothesis on why cross-modal prompt transfer should even work must be discussed early to set stage for the problem and the proposed solution 
- Is this a key contribution of the paper - if so this must be discussed in the main paper rather than the appendix. 
- L269: wouldn't eq (8) increase the prompt size to > 100 ?
- How is "relative performance" defined? Given how dense the figure is, authors must include conclusion of this experiment in the caption. 
- Statistical significance: Are the improvements statistically significant ? I see that the standard deviations are reported in the appendix. Authors should include a discussion on significance of improvements in the main paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes to improve the performance of prompt tuning by exploring cross-modality prompt transfer, that is leveraging prompts pretrained on text modality to improve performance on few-shot image recognition. They first validate the effectiveness of cross-modality prompt transfer by empirical comparison between VPT, linear probing, frozen prompt transfer and projection transfer. They also propose an effective metric to estimate prompt transferability by combining modality gap and task gap scores. Finally, they propose the attention transfer which introduces the knowledge from source domain by an attention block. Experiments on VTAB-1K validate that attention transfer can improve existing SOTA method.

### Strengths
1. Most parts of the paper are clearly presented.
2. Promising results with extensive experiments.
3. Novel idea of cross-modality transfer instead of the intra-modality transfer.

### Weaknesses
My concern focuses on the effectiveness of the proposed method. (1) The proposed projection transfer and attention transfer have introduced extra parameters, the effect from extra parameters and source domain are not decomposed in the experiments in Fig.3. This makes it hard to judge if the source domain knowledge is really useful. The authors can further strengthen the experiments by 1) using random source prompt in projection transfer and attention transfer, which will make the number of learnable parameters match to that in experiments using source prompts from NLP domain, 2) using a source domain with many training data and gradually increasing the number of source training samples and inspecting if the source prompts learned with different number of source samples lead to increasing trend of improvement in projection transfer and attention transfer. (2) The effectiveness should be demonstrated using different language models, so as to validate the generalization ability. (3) The effectiveness should be demonstrated using different visual prompt tuning methods, including shallow and deep methods. (4) The accuracy on Natural subset decreases, making it hard to determine the effectiveness. Experiments on more datasets should be conducted to support the claim of this paper.

Besides, the meaning of designing a good metric estimating prompt transferability should be also clarified. GM & GT outperforms Vdata by 3 points with respect to the mean Kendall's coefficient. To what degree does such an improvement contribute to enhancing the transfer performance on VTAB-1k? The work "Qifan Wang, Yuning Mao, Jingang Wang, Hanchao Yu, Shaoliang Nie, Sinong Wang, Fuli Feng, Lifu Huang, Xiaojun Quan, Zenglin Xu, Dongfang Liu: APrompt: Attention Prompt Tuning for Efficient Adaptation of Pre-trained Language Models. EMNLP 2023: 9147-9160" also introduced attention into prompt tuning, the relationship of the proposed method to it should be also clarified.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

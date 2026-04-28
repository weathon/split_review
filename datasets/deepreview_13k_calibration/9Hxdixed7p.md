# 3D-Properties: Identifying Challenges in DPO and Charting a Path Forward

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Aligning large language models (LLMs) with human preferences has recently garnered significant attention, with Proximal Policy Optimization (PPO) being a canonical yet computationally expensive method, and Direct Preference Optimization (DPO) offering a simpler and more efficient alternative. While prior studies have explored the trade-offs between PPO and DPO, DPO remains underutilized in state-of-the-art production-level LLMs, suggesting potential limitations. In this work, we revisit DPO with a comprehensive analysis of its theoretical foundations and empirical performance, aiming to chart a path forward and bridge this gap. We identify three critical properties—termed the \textbf{3D}-properties—that arise from DPO’s learning process: \textbf{D}rastic drop in the likelihood of rejected responses, \textbf{D}egradation into response suppression, and \textbf{D}ispersion effect on unseen responses. We show that these phenomena stem from the inherent features of DPO's optimization objective, where the interaction between the gradients of chosen and rejected responses causes instability. These findings are supported by experiments on both a carefully constructed toy model and practical LLM tasks, including mathematical problem-solving and instruction following. Our work offers new insights, connecting these observations to related research while providing a theoretical explanation for the underlying mechanisms. To address the challenges posed by the \textbf{3D}-properties, we propose straightforward regularization techniques that enhance training stability and final performance. Additionally, we investigate how the distribution of paired preference data affects DPO’s efficacy, contributing to a broader understanding of how alignment models handle out-of-domain (OOD) data. We believe our findings will help guide future research toward closing the gap between reward-model-free preference learning and reward-model-based approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper titled "3D-Properties: Identifying Challenges in DPO and Charting a Path Forward" presents a thorough analysis of the DPO method used for aligning LLMs with human preferences. The authors identify and term three critical properties of DPO's learning process the 3D-properties and propose regularization techniques to address the challenges these properties present. Theoretical analyses, toy model simulations and real-world experiments demonstrate the effectiveness of the proposed method.

### Strengths
The paper is well-structured, where toy example can support their claims.
The paper offers a balanced mix of theoretical analysis and empirical evidence, which strengthens the claims made about the 3D-properties and their impact on DPO's performance.

### Weaknesses
The three observations have been widely studied by previous works. Besides, one of the proposed regularization methods, incorporating an SFT loss into the objective, has been widely used in existing preference learning approaches [1]. This limits the novelty of the paper.
Considering that there are many existing methods to solve the DPO problem proposed in this paper, there is a lack of comparison with them, such as [2] and others.
Considering the generality of the proposed constraint algorithm, some advanced preference learning algorithms, such as SimPO [3], should also be tested.
More and more general LLMs should be included for evaluation, such as Meta-Llama3.

### Questions
How to ensure that the initialization assumptions of parameter distribution can be applied to, or related to LLMs?

The detailed parameter adjustment strategy is only given in the toy experiment. What is the effect of different β values ​​in the real-world experiments?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The paper provides a comprehensive analysis of Direct Preference Optimization (DPO), examining its theoretical foundations and empirical performance to address current limitations. It identifies three perspectives—(1) Drastic drop in the likelihood of rejected responses, (2) Degradation into response suppression, and (3) Dispersion effect on unseen responses. The paper connects these observations to related research and offers a theoretical explanation for the underlying mechanisms. To improve DPO’s stability and performance, the authors propose regularization methods, including adaptive adjustment of gradient weights for chosen and rejected responses, as well as incorporating an SFT loss into the objective.

### Strengths
The topic is interesting for RLHF. 

The paper introduces effective regularization methods, including adaptive gradient weighting for chosen and rejected responses.

The experiments are well-conducted and thorough.

### Weaknesses
The study could benefit from using a wider range of LLMs.

The experiments can use more datasets except for math. 

The code is not open source, which may limit reproducibility.

### Questions
For the toy model setup, which specific model is used in the paper?

Why does the paper focus primarily on math datasets rather than exploring a wider range of tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an interesting theoretical and empirical analysis of Direct Preference Optimization (DPO) and identifies three main challenges in its optimization process, termed as “3D-properties”: Drastic drop in rejected response likelihood, Degradation into response suppression, and Dispersion effect on unseen responses. These limitations, which do not arise in RM-based approaches, impact the stability and effectiveness of DPO. To address these issues, the authors propose regularization techniques, including adaptive gradient weighting and SFT loss. They conduct experiments on toy examples as well as math reasoning and instruction-following tasks to validate the presence of the 3D-properties, the advantages of on-policy over off-policy DPO, the comparative superiority of RM-based methods, and the effectiveness of the proposed regularization technique.

### Strengths
- Significance: The paper addresses a crucial and interesting gap by analyzing the limitations of DPO
- Theoretical Analysis and Empirical Validation: The paper provides a theoretical framework alongside empirical results to validate the presence of the 3D-properties in DPO. This combined approach strengthens the findings, offering clear insights into the mechanisms driving DPO’s limitations and supporting the proposed solutions.

### Weaknesses
 - Presentation: The presentation could be improved to enhance readability. For example, the text size in Figures 2 and 3 is small, and the description of Scenarios 1-4, which is crucial for understanding the on-policy versus off-policy comparison, is currently only detailed in the appendix. Bringing this description to the main text would improve clarity.
- Experimental Design for On-Policy vs. Off-Policy Comparison: The on-policy and off-policy experiments rely on different data sources, which introduces potential confounds in the comparison. Using a more direct on-policy and off-policy setup, such as comparing historical-only data with semi-on-policy DPO (e.g., iterative DPO), would make the findings more robust.
- Parameter Tuning in Flex-DPO: Adjusting Flex-DPO requires tuning two parameters ( \beta^+  and  \beta^- ), and while Figure 4 provides some guidance, this approach may still present challenges for practical implementation due to a lack of clear tuning guidelines.
- In Section 4.2, it is mentioned that for the MATH dataset, the best and worst responses were selected by GPT-4. Why did the authors choose this method instead of directly verifying the answers? Given that GPT-4’s accuracy on MATH is only slightly above 50%, this approach seems potentially unreliable.

### Questions
- In Section 4.2, it is mentioned that for the MATH dataset, the best and worst responses were selected by GPT-4. Why did the authors choose this method instead of directly verifying the answers? Given that GPT-4’s accuracy on MATH is only slightly above 50%, this approach seems potentially unreliable.

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
This paper investigates the limitations of DPO in aligning large language models with human preferences, identifying three critical properties that hinder its performance: drastic drops in rejected response likelihood, degradation into response suppression, and dispersion effects on unseen responses. The authors provide theoretical explanations for these properties and demonstrate how they arise from DPO's objective. To address these challenges, the paper proposes regularization techniques and validates their effectiveness through experiments on both toy models and real-world language model tasks.

### Strengths
- Studying DPO degradation phenomena is important due to its widespread use. This paper originally summarizes and theoretically analyzes several degradation phenomena of DPO discovered in previous work.

- Novel comparative analysis between on-policy and off-policy DPO on toy models.

- The paper is well-written and easy to follow.

### Weaknesses
 - I think the Explanation for Property 3 is inadequate. Firstly, compared to the previous two explanations, it lacks mathematical formulation and seems to merely restate empirical phenomena. Secondly, since the optimization process is conducted in mini-batches, while the model may ensure that overflow probability won't disperse to recently seen samples, I suspect it could also disperse to samples from the preference dataset that were encountered earlier, rather than necessarily dispersing to unseen samples outside the preference dataset.

- Following the previous point, the toy model setup, as mentioned by the authors in lines 344-353, is closer to treating each input/output as a token rather than a complete prompt/response, which is not a good toy model approximation of the real situation. One possible improvement would be to maintain other settings unchanged while increasing the sample size to enable mini-batch optimization that better resembles real-world conditions, with fewer epoch repetitions.

- While the authors used self-built Poem and Slogan datasets to evaluate the model's instruction following ability and acknowledged their limited scope, these datasets are insufficient to assess the model's general instruction following capabilities. The paper lacks evaluation on widely-used benchmarks in preference optimization work, such as AlpacaEval2, Arena-Hard, and MT-Bench, which are designed to test models' general instruction following ability.

- The proposed regularization techniques lack substantial significance. The first technique, which independently adjusts beta for reject responses, shows effectiveness in the poem task, but the optimal reject beta is merely 0.02 lower than the chosen beta. Without showing gradient comparisons for this technique, it's unclear whether it actually improves performance by addressing the large gap demonstrated in Figure 2. Moreover, the second technique, SFT loss, is already a widely established regularization technique.

- I am not quite convinced by the claims in section 3.4. Although existing works are cited to establish conceptual connections between RM and DPO, the subsequent gradient analysis focuses on r, creating a gap with the previous gradient analysis that focused on $\pi$.

- The probability distributions in the bottom-right figure don't seem to match with the leftmost figure in Figure 2. In Figure 2, the unseen probability at 500 epochs approaches 1, but in Figure 1 it's all zeros. The chosen probabilities also don't quite align.

### Questions
- The probability distributions in the bottom-right figure don't seem to match with the leftmost figure in Figure 2. In Figure 2, the unseen probability at 500 epochs approaches 1, but in Figure 1 it's all zeros. The chosen probabilities also don't quite align.

### Soundness
3

### Presentation
3

### Contribution
3

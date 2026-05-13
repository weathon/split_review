# SeedLoRA: A Fusion Approach to Efficient LLM Fine-Tuning

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Despite Low-Rank Adaptation (LoRA)'s popularity for fine-tuning large models, it often exhibits a noticeable performance gap compared to full fine-tuning, particularly in complex tasks such as mathematical reasoning and code generation. Motivated by this discrepancy, we propose a novel fusion approach for LoRA fine-tuned models. Our key insight is that LoRA models trained with different random seeds on the same task often exhibit complementary strengths. In contrast to existing research that typically focuses on fusing models trained on diverse tasks, we explore the potential of combining multiple LoRA models fine-tuned on the same task with different random seeds. This intra-task fusion method aims to leverage the strengths of various fine-tuned models to create a more robust and effective adaptation. To validate our approach, we conducted comprehensive experiments across three key areas: mathematical reasoning, code generation, and general instruction-tuning tasks. The results demonstrate that our fusion method significantly enhances LoRA's performance, outperforming both standalone LoRA models and current fusion methods. Notably, this advancement substantially narrows the gap between LoRA and full fine-tuning, thus offering a more effective approach to model adaptation without the GPU memory burden of full parameter fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This study proposes SeedLoRA, an approach that aims to improve the performance of LoRA-based Parameter-Efficient Fine-Tuning (PEFT) in Large Language Models (LLMs) by merging models trained on the same task with different random seeds. While existing model merging research largely focuses on combining models trained on different tasks, this study shifts the focus to single-task model merging, highlighting its distinction from conventional multi-task model merging approaches.

SeedLoRA performs the model merging process by weighted averaging n delta models trained with different seeds and normalizing the resulting distribution using the mean and standard deviation of a specific reference model to stabilize the shifted distribution.

Through experiments, the study demonstrates that this approach outperforms conventional LoRA-based fine-tuning (LoRA, LoRA+, DoRA) and existing model merging methods (Model Soup, TIES, DARE), albeit limited to specific complex tasks such as code generation and mathematical reasoning.

### Strengths
- The motivation to integrate multiple models trained on the same task with different seeds, based on the observation that LoRA fine-tuning can sometimes exhibit significant performance differences depending on the seed, is intriguing. This aligns with established ensemble learning theories and appears to be a reasonable approach.

- From the perspective of model merging, the study introduces a novel aspect of single-task model merging. The authors' discussion of the differences compared to previous multi-task model merging provides valuable insights.

### Weaknesses
Presentation
* While the claims are clear and straightforward, making the paper understandable, the overall writing feels unpolished. Numerous issues, ranging from serious errors that hinder comprehension to minor typos, are apparent throughout the paper.
    * Figure 3: Although emphasized in Section 4.5, results for SeedLoRA are missing from the figure, and its placement is far removed from the section where it is discussed.
    * Line 296: The equation for $\hat{\sigma}$ appears to erroneously calculate it using $\mu$, which seems to be a mistake.
    * Line 71: The word “creat” is likely a typo for “create”. Additionally, many other typos and spacing issues were observed.
* Key technical details are missing or unclear. For instance, in Section 3.4, under "Step 2," there is no explanation of how the importance weight $w_i$ is determined.

Lack of Rationale and Novelty in the Technique
* Since the model weights are averaged (or weighted averaged), the overall weight distribution remains bound to the original distribution of the individual models (as is the case with Model Soup), potentially resulting in no significant shift. Moreover, in Step 3 of Section 3.4, the "reference model" is ultimately a simple average of the model weights. It is difficult to accept that such a minor distribution shift (or even no shift at all) would be practically meaningful. A theoretical analysis in the solution space or references supporting the necessity of this subtle distribution shift is needed.
* Without sufficient rationale for the proposed technique, this work may be seen as merely adapting Model Soup (which already includes some results for simple single-task merging case) to the context of LoRA fine-tuning, thereby lacking sufficient technical novelty.

Validation
* Results for full fine-tuning are missing in most tables and figures. This omission makes it difficult to assess whether the gap between LoRA-based fine-tuning and full fine-tuning has been meaningfully reduced or whether marginal improvements are being overemphasized.
* In Figure 1, LoRA appears to outperform full fine-tuning in some cases, depending on the random seed. However, results are only shown for three seeds (11, 42, 202), raising concerns that SeedLoRA’s performance improvements might also be due to luck rather than robust effectiveness.

### Questions
All of my questions are related to the points raised in the Weaknesses section.
1. In Step 2 of Section 3.4, could you clarify how the importance weight $w$ is determined?
2. Could you provide a more detailed theoretical rationale for the proposed model distribution matching?
3. To enhance reliability, could you include results using different seeds beyond 11, 42, and 202, as well as results for full fine-tuning?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new LoRA-based PEFT method for LLM. It notice that training a LoRA model based on a LLM by initializing with different seeds will result in different performance, which inspires the authors to propose a so-called seedLoRA method that merges various randomly initialized LoRA models to achieve a much better fusion model than any single LoRA model. Experimental results on code, math, and general tasks demonstrate the effectiveness of the proposed seedLoRA. Further more, the LoRA model even outperforms the full-tuning model in some subtasks.

### Strengths
1. The idea is interesting. It achieves much better performance than any single LoRA models without introducing any extra computation cost during inference.
2. This paper spends large space analyzing its motivation in Sec. 3.1- Sec. 3.3.
3. The proposed seedLoRA method is straightforward and the performence improvements are not trivial, showing significant improvements over other SOTA methods.
4.  Sec. 4.5 further analyzes the training cost, showing performance increase even in the same training cost compared with the traditional LoRA training.

### Weaknesses
1. The analysis of LoRA and full fine-tuning in Sec. 3.2 is not persuasive enough. Can only one case demonstrate the statement "different LoRA models, each trained with unique random seeds, tend to excel in distinct subdomains"? This point may be the most important insight of this paper, so more sophisticated and strict experiments or derivations should be delved into. The presented evidence relies on a single example, lacking statistical rigor and failing to account for potential confounding factors. A more robust analysis would involve multiple datasets, different model architectures, and a quantitative measure of the 'distinctness' of the subdomains where each seed excels. Furthermore, it's unclear if the observed performance variations are statistically significant or simply due to random fluctuations.
2. The description of "Step 3: Distribution Matching:" is insufficiently clear. In Eq.(5), I do not completely understand the calculation of $\tau_m$. $\hat\mu$ and $\hat\sigma$ are the mean and standard deviation of the reference model.  But how can we calculate the mean and the deviation of the best-performing individual model (only one model)? This is the most confused point of mine.

### Questions
Besides the questions proposed in weakness, several other minor questions are as below:
1. How to calculate the cosine similarity in Figure 2, Sec. 3.3?
2. "Multi-task methods, such as TIES, are designed to address interference between orthogonal models." how to understand the "interference"?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a fusion strategy for merging LoRA-tuned Large Language Models. The basic idea is to merge models trained on the same tasks with different random seeds.

### Strengths
- Introducing single-task model merging, within the domain of parameter-efficient fine-tuning for LLMs. 
- Achieving comparable performance to full fine-tuning on challenging tasks such as math reasoning and code generation.

### Weaknesses
 - Lack of novelty: The motivation is good. However, the approach for model merging is quite straightforward. It is unclear why such simple averaging or model normalization works. It lacks insights and explanations.

- Lack of clarity. The storyline was good at the beginning. I was confused by the proposed model merging or fusion. Specifically, in Line 290, it is unclear about the reference model. The authors mentioned that it can be the best-performing individual model. How do you know the best model? Model merging is supposed to be done without looking into the test data. If you merge models according to the testing performance, this is wrong!

### Questions
- Please answer the issues pointed out in the weakness.

- Lack of the whole picture: What is the limitation of your work? In addition to showing your merged model can achieve the performance of full fine-tuning, you also need to explain what the cost is, when it works and when it doesn't, and why. How many models do you need for merging to reach full fine-tuning performance?

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
3

### Summary
Parameter-Efficient Fine-tuning (PEFT) is an important direction in fine-tuning large language models (LLMs). The most popular PEFT method is LoRA. LoRA and its variants have exhibited wide performance gap compared to the full fine-tuning in LLM in some complexity tasks, such as mathematical reasoning, and code generation. The key insight brought up by this paper is that some of the limitations in performance can be addressed by exploring merging the models that are trained on the same single task with different random seeds. The core idea of the proposed SeedLoRA is a weight distribution match technique. This technique allows one to create a merged LoRA model that synergies individual strengths while preserving beneficial properties in solving some complexity tasks. This helps to narrow the performance gap with the full fine-tuning in mathematical reasoning and code generation. The proposed approach beats the other existing merging techniques such as Model Soup, TIES< and DARE in the single-task scenarios.

### Strengths
This paper introduces a novel approach to model merging. Unlike existing techniques that primarily cater to multi-task merging, the proposed method with random seed focuses on single tasks. This unique approach is particularly suitable for addressing the parameter-efficient fine-tuning problem in mathematical reasoning and code generation tasks. The innovative weight distribution matching further enhances the novelty and utility of the proposed approach.

From an experimental presentation perspective, the paper seems to have made reasonable efforts to demonstrate that the proposed approach really helps with the LLM fine-tuning on the specific LoRA weak tasks such as mathematical reasoning and code generation. The proposed approach has shown stronger results than other interesting and recent methods such as DARE, TIES, and Model Soup. From the results, it is clear that SeedLoRA beats the other standalone LorA and existing multi-task merging techniques on several tasks.

The paper does well in communicating the motivation of the proposed approach. It follows a reasonable progression and is easy to read and understand. I also find it useful to read the specific implementation details and hyperparameter settings, which improve the reproducibility of the paper.

It is important to bridge the performance gap in tasks such as mathematical reasoning and code generation for PEFT for LLMs fine-tuning. Fully fine-tuning the LLMs requires expensive GPU clusters. The previous LoRA and its variants were not good enough in some of the complex but important tasks such as mathematical reasoning and code generation. This gap in performance in mathematical reasoning and code generation fundamentally limits the progress in the field. The typical methods to address this mainly focus on multi-task scenarios, while the proposed approach focuses on single tasks. The proposed SeedLoRA appraoch provides a new perspective to narrow the performance gap in PEFT. In that sense, this paper is significantly interesting to the community.

### Weaknesses
There are some issues with the paper as well.

1. Limited impact scope. LoRA and its variants have performed well in multiple tasks and are close to full fine-tuning. The proposed SeedLoRA focuses only on complex tasks such as code generation and mathematical reasoning. The fact that the SeedLoRA only improves the performance on those particular tasks seems quite limited. Would SeedLoRA be helpful in any other tasks outside of these? What are the patterns that the proposed approach would work and that the proposed approach would not work? The experiments in this paper do not provide those answers. That would be very limited if the proposed approach only works on single tasks in code generation or mathematical reasoning.

2. Is SeedLoRA practical? A key motivation behind LoRA is its ability to fine-tune LLMs on relatively inexpensive and limited GPUs quickly. The proposed SeedLoRA, however, would significantly increase the time required to obtain multiple models for a single task, raising concerns about its practicality. The number of models needed for a single task is also unclear, further questioning the feasibility of the approach.

3. The proposed distribution matching algorithm focuses on rescaling the weights by matching the mean and standard deviation, which implies that the model weights have a specific distribution pattern. This seems to be oversimplifying the model weight distribution. It is clear that one could have different options, such as looking into the K-L divergence. Those alternative directions and experiments are missing. It is unclear why the proposed approach makes a technical choice in equation (5).

### Questions
1. It is cool that the proposed model merging technique works, but i am wondering if the simple ensemble technique would work the same. Let's say we can train the model with different architecture, and then just use the mixture of the experts, would that beat the proposed approach? 

2. It is not clear if the random seeds are impacting only the model weight initialization or also on the data distribution order.

3. What's the computational cost overhead to train the proposed approach? How would that compared against the baseline approaches.

4. Does the proposed approach need to apply the merging on all the weights?

### Soundness
4

### Presentation
3

### Contribution
3

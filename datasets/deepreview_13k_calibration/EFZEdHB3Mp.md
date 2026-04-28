# DynaPrompt: Dynamic Test-Time Prompt Tuning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Test-time prompt tuning enhances zero-shot generalization of vision-language models but tends to ignore the relatedness among test samples during inference. Online test-time prompt tuning provides a simple way to leverage the information in previous test samples, albeit with the risk of prompt collapse due to error accumulation. To enhance test-time prompt tuning, we propose DynaPrompt, short for dynamic test-time prompt tuning, exploiting relevant data distribution information while reducing error accumulation. Built on an online prompt buffer, DynaPrompt adaptively selects and optimizes the relevant prompts for each test sample during tuning. Specifically, we introduce a dynamic prompt selection strategy based on two metrics: prediction entropy and probability difference. For unseen test data information, we develop dynamic prompt appending, which allows the buffer to append new prompts and delete the inactive ones. By doing so, the prompts are optimized to exploit beneficial information on specific test data, while alleviating error accumulation. Experiments on fourteen datasets demonstrate the effectiveness of dynamic test-time prompt tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a dynamic test-time prompt tuning approach that enhances zero-shot generalization in vision-language models. It leverages the beneficial information from previous online samples to adaptively select and optimize prompts, reducing error accumulation and improving model performance across various datasets.

### Strengths
1. The paper is well-organized and easy to follow. 
2. The proposed DynaPrompt effectively mitigates error accumulation, a prevalent challenge in online test-time tuning，leading to more stable performance across sequential test samples while exploiting beneficial information from prior online test samples.
3. Despite the increased time costs associated with larger prompt buffer sizes, the experimental outcomes confirm the  effectiveness of the proposed method.

### Weaknesses
1. In prompt learning, the initial prompts might affect the final performance. I wonder whether a similar situation can occur with the proposed method. The authors are encouraged to conduct related experiments.
2. Could the proposed method be extended to incorporate visual prompts, thereby evolving into a multimodal approach? Additionally, when integrated with MaPLe, is the method only applied to the textual branch?

### Questions
1. I am curious about how the order for each round in the 'Sensitivity to test time sample order' section was set.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses fundamental issues in test-time prompt tuning, specifically focusing on the selection, updating, appending, and deletion of prompts. The authors introduce an innovative dynamic test-time prompt tuning approach, which incorporates two novel prompt evaluation metrics alongside a prompt buffer modification strategy. Extensive experimental results underscore the effectiveness of the proposed method.

### Strengths
1. The paper is well-structured and easy to follow, with the three technical components clearly and accessibly presented.
2. The proposed method is well-reasoned, employing dynamic prompt selection and updating mechanisms that are both effective and distinct from prior studies, which primarily focus on data manipulation.
3. The experiments are thorough, and the results convincingly demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The range of comparison methods could be expanded, as the paper overlooks one relevant comparison method [1].
2. Both the prediction entropy metric and probability difference metric provide insights into model prediction confidence, though from different perspectives. It is unclear why entropy is specifically used to measure relevance while difference is used to maintain diversity. Why does the direct combination of these two types of prompts yield effective results? Would a two-step prompt selection process, satisfying both conditions simultaneously, be more advantageous?
3. Details regarding the data augmentation set  $X_n$  are insufficiently discussed in this paper.

### Questions
Please refer to the `Weaknesses` section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new test-time prompt tuning method called DynaPrompt, which leverages a dynamic prompt buffer to extract beneficial information from online test samples while reducing error accumulation. The method adaptively selects and optimizes prompts for each test sample, enabling the selected prompts to integrate relevant information from previous test samples, thus improving the prediction performance of the current sample. Experimental results demonstrate that this method performs effectively across multiple benchmark datasets.

### Strengths
1. This paper propose a dynamic prompting method that utilizes useful information from online test samples while mitigating the problem of error accumulation.
2. DynaPrompt improves the adaptive capability of the model by introducing a dynamic prompt selection strategy that adaptively selects and optimizes relevant prompts for each test sample based on two metrics: predictive entropy and probability difference.
3. During the dynamic prompt selection process, if no suitable prompts can be found, DynaPrompt employs a dynamic prompt appending strategy to append new initial prompts to the set of prompts and remove the least active prompts, thus effectively incorporating information from the new data distribution.

### Weaknesses
1.  The computational complexity increases, and the authors' approach requires dynamic updating and selection of cues at each stage, whether it introduces more computational time.
2.  The authors' approach demonstrates the advantages of dynamic prompting, however did the authors consider whether comparable performance could also be achieved if online testing was performed from scratch using a prompt length comparable to that of the final model.

### Questions
1. It is recommended that the authors add ablation experiments to further demonstrate the validity of the methodology by performing online tests from scratch using the same prompt lengths as the final model and performing performance comparisons.
2. The author's paper mentions deleting the prompt, does the author mean that the entire prompt is deleted in its entirety, or does he mean that only the parameters of the prompt are set to zero?

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
5

### Summary
This paper introduces DynaPrompt, a test-time prompt-tuning (TPT) approach that exploit information from previous test samples while avoiding error accumulation. While naively adapting TPT to the online setting lead to collapse, DynaPrompt leverages a dynamic buffer of prompts and optimize only the most relevant prompts for each test sample. Furthermore, DynaPrompt introduces only one additional hyper-parameter, the buffer size, thanks to an adaptative thresholding strategy.  DynaPrompt demonstrate consistent improvement over TPT and its variants (CoOp+TPT, MaPLe+TPT) making it a simple and effective alternative.

### Strengths
- **Motivation**: The authors made a good job motivating the paper, illustrating the potential benefit of moving to the on-line scenario while showing the non-triviality of extending TPT to this setup.
- **Contribution**: The technical contribution of the paper is simple and effectively solve a clearly identified issue.
- **Clarity**: The paper is easy to follow and arguments are clearly articulated.
- **Experiments**: The experiments are convincing and show consistent improvements over the baselines.

### Weaknesses
 - **Missing experiments** : Some experiments are missing like evaluating on different backbones and more importantly evaluation on the Imagenet dataset. I will consider raising my score if results on the Imagenet dataset are added.

### Questions
- Unless I missed it, it seems that there is no results on the Imagenet dataset. Could you provide results on the Imagenet dataset ?  
- Could you provide evaluation results on other CLIP vision backbones such as ViT-B/32 or Resnet-50 ?
- Why did you not included results for CoOp + DynaPrompt in Table 2 ?
- If I understand your method correctly, the buffer initially contains only one prompt initialized as ‘a photo of a’. For a given test sample, if your selection criteria (entropy and probability difference) are not met, a new prompt is initialized with ‘a photo of a’; otherwise, selected past prompts are used for optimization. I’m curious whether you considered initializing a set of prompts from the beginning and using your selection criteria to optimize subsets of this buffer. Initially, all prompts would be identical, but a small degree of randomness at the start could help address this issue. Do you think collapse would occur in that scenario? An experimental result would be helpful, but your thoughts or intuition on this would be sufficient.

### Soundness
3

### Presentation
3

### Contribution
3

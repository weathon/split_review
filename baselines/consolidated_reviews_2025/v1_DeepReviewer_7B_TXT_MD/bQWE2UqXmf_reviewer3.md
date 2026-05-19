### Summary

This paper proposes a new method for detecting AI-generated text. The method is based on the observation that LLMs tend to rewrite human-written text less than AI-generated text when asked to rewrite it. The authors propose to use this property to detect AI-generated text by measuring the rewriting distance between the original and rewritten text. The authors evaluate their method on multiple datasets and show that it outperforms existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The authors provide a comprehensive evaluation of their method on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on manually crafted prompts, and the performance is sensitive to the choice of prompts. While the authors explore some variations, a more systematic approach to prompt engineering could be beneficial. Specifically, the lack of a principled method for selecting prompts introduces a potential source of bias and limits the generalizability of the approach. The current reliance on manual selection makes it difficult to determine the optimal set of prompts for different datasets or tasks, and the observed sensitivity to prompt variations suggests that the method's performance may not be robust to changes in the prompt design.
- The paper could benefit from more in-depth analysis of why the proposed method works. While the empirical results are strong, a deeper theoretical understanding of the underlying mechanisms would strengthen the contribution. For example, it would be valuable to understand how the rewriting process differs for human and AI-generated text at a more fundamental level, and what specific linguistic or structural properties are captured by the proposed method. The current analysis focuses primarily on empirical results, without providing a clear explanation of the underlying mechanisms.

### Suggestions

The authors should explore more systematic approaches to prompt engineering, rather than relying on manual selection. This could involve techniques such as automated prompt optimization or the use of a diverse set of prompts that are designed to capture a wide range of rewriting behaviors. For example, the authors could investigate the use of prompt ensembles, where multiple prompts are used in parallel, and the results are combined to improve robustness. Furthermore, a more detailed analysis of the prompt space is needed to understand the sensitivity of the method to different prompt variations. This could involve techniques such as ablation studies, where specific components of the prompts are removed or modified to assess their impact on detection performance. The goal should be to develop a more principled approach to prompt engineering that is less reliant on manual selection and more robust to changes in the prompt design.

To strengthen the theoretical understanding of the method, the authors should investigate the specific linguistic and structural properties that are captured by the rewriting process. This could involve analyzing the changes made by the rewriting process at a more fine-grained level, and comparing the patterns of changes for human and AI-generated text. For example, the authors could investigate the types of edits that are most likely to be made by human writers versus AI generators, and how these edits differ in terms of their length, complexity, and semantic content. This analysis could provide insights into the underlying mechanisms of the method and help to explain why it works. Furthermore, the authors should explore the relationship between the rewriting process and the underlying generation process of the text, to better understand the differences between human and AI-generated content.

Finally, the authors should consider the potential for adversarial attacks that could manipulate the rewriting process to evade detection. This could involve techniques such as prompt optimization or the generation of adversarial examples that are designed to minimize detection performance. The goal should be to develop a more robust and reliable method that is less sensitive to changes in the rewriting model and less vulnerable to adversarial attacks. This could involve exploring techniques such as adversarial training or robust optimization to make the method more resilient to such attacks.

### Questions

- How does the method perform when the AI-generated content is specifically trained to evade detection? Could the prompts be made more robust to such adversarial cases?
- Have you considered using different types of prompts, such as those that focus on specific linguistic features? Would this improve detection accuracy?
- Could the method be extended to detect other types of AI-generated content, such as images or audio?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

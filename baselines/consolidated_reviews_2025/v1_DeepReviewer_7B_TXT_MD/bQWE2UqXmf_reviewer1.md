### Summary

This paper proposes a novel method to detect AI-generated content by prompting LLMs to rewrite it. The core idea is that LLMs tend to modify human-written text less than AI-generated text when asked to rewrite it, allowing for detection based on the editing distance of the rewriting process. The authors introduce three rewriting prompts to capture invariance, equivariance, and uncertainty in the rewriting process, which they argue are key differentiating factors between human and AI-generated content. The method is tested across multiple domains and datasets, showing significant improvements over existing baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The core idea of using rewriting prompts to detect AI-generated content is novel and well-motivated. The observation that LLMs rewrite human text more than AI text is interesting and provides a fresh perspective on the problem.
- The experimental evaluation is thorough, covering multiple datasets and comparing against strong baselines. The results show consistent improvements over existing methods, particularly in out-of-distribution settings.
- The method is lightweight and doesn't require access to internal model parameters, making it practical for real-world deployment. Its robustness to prompt variations and rewriting model choices is also noted.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on manually crafted rewriting prompts, and the performance is sensitive to the choice of prompts. While the authors explore some variations, a more systematic approach to prompt engineering could be beneficial. Specifically, the lack of a principled method for selecting prompts introduces a potential source of bias and limits the generalizability of the approach. The current reliance on manual selection makes it difficult to determine the optimal set of prompts for different datasets or tasks, and the observed sensitivity to prompt variations suggests that the method's performance may not be robust to changes in the prompt design.
- The paper could benefit from more in-depth analysis of why the proposed method works. While the empirical results are strong, a deeper theoretical understanding of the underlying mechanisms would strengthen the contribution. For example, it would be valuable to understand how the rewriting process differs for human and AI-generated text at a more fundamental level, and what specific linguistic or structural properties are captured by the proposed method. The current analysis focuses primarily on empirical results, without providing a clear explanation of the underlying mechanisms.
- The method's reliance on LLMs for rewriting introduces a potential dependency on the quality and biases of these models. The paper acknowledges this to some extent, but a more thorough investigation of how different rewriting models affect detection performance would be valuable. Specifically, the paper should explore the impact of different LLMs on the rewriting process, and how this affects the detection performance. It is also important to consider the potential for adversarial attacks that could manipulate the rewriting process to evade detection.

### Suggestions

The authors should explore more systematic approaches to prompt engineering, rather than relying on manual selection. This could involve techniques such as automated prompt optimization or the use of a diverse set of prompts that are designed to capture a wide range of rewriting behaviors. For example, the authors could investigate the use of prompt ensembles, where multiple prompts are used in parallel, and the results are combined to improve robustness. Furthermore, a more detailed analysis of the prompt space is needed to understand the sensitivity of the method to different prompt variations. This could involve techniques such as ablation studies, where specific components of the prompts are removed or modified to assess their impact on detection performance. The goal should be to develop a more principled approach to prompt engineering that is less reliant on manual selection and more robust to changes in the prompt design.

To strengthen the theoretical understanding of the method, the authors should investigate the specific linguistic and structural properties that are captured by the rewriting process. This could involve analyzing the changes made by the rewriting process at a more fine-grained level, and comparing the patterns of changes for human and AI-generated text. For example, the authors could investigate the types of edits that are most likely to be made by human writers versus AI generators, and how these edits differ in terms of their length, complexity, and semantic content. This analysis could provide insights into the underlying mechanisms of the method and help to explain why it works. Furthermore, the authors should explore the relationship between the rewriting process and the underlying generation process of the text, to better understand the differences between human and AI-generated content.

Finally, the authors should conduct a more thorough investigation of the impact of different rewriting models on detection performance. This should include a systematic evaluation of a range of LLMs, including both open-source and proprietary models, to assess the robustness of the method to variations in the rewriting model. The authors should also explore the potential for adversarial attacks that could manipulate the rewriting process to evade detection. This could involve techniques such as prompt optimization or the generation of adversarial examples that are designed to minimize detection performance. The goal should be to develop a more robust and reliable method that is less sensitive to changes in the rewriting model and less vulnerable to adversarial attacks.

### Questions

- How does the method perform when the AI-generated content is specifically trained to evade detection? Could the prompts be made more robust to such adversarial cases?
- Have you considered using different types of prompts, such as those that focus on specific linguistic features? Would this improve detection accuracy?
- Could the method be extended to detect other types of AI-generated content, such as images or audio?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

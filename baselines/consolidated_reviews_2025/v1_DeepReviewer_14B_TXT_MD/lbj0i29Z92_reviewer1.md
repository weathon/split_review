### Summary

This paper proposes a novel iterative self-improvement scheme for LLMs, which applies to both the actor and the judge. Building on the previous Self-Rewarding work, the authors introduce an additional step to refine the judge's ability, referred to as the meta-rewarding/judge step. In this step, the model acts as its own judge (called the meta-judge), evaluating its judgments and using this self-assessment to improve its judging capabilities. This enhancement allows the model to better align and follow instructions without human intervention. On multiple instruction-following benchmarks, the proposed method demonstrates a significant improvement over the Self-Rewarding baseline.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

* The method is well-motivated and clearly described. 
* The authors provide ablation studies to show the effectiveness of each component. 
* The improvement is significant, with the proposed method outperforming the Self-Rewarding baseline by a large margin on AlpacaEval 2 and Arena-Hard.

### Weaknesses

#### Some Related Works


#### comment

 * The proposed method is very similar to Self-Rewarding. While this is not a critical issue, as the paper presents clear improvements over the previous method, it does limit the novelty of the contribution. 
* The method is complex and involves multiple steps, which could make it difficult to implement and reproduce. 
* The evaluation is limited to a single model, Llama-3-8B-Instruct, which restricts the generalizability of the results.
* The paper lacks a thorough analysis of the computational resources required for training. This makes it difficult to assess the practical feasibility of the method, especially for researchers with limited access to computational resources.

### Suggestions

The authors should consider exploring alternative methods to enhance the novelty of their approach. While the improvements over Self-Rewarding are significant, the core methodology remains largely incremental. One potential direction could be to investigate different meta-judging mechanisms, perhaps incorporating techniques from other areas of machine learning, such as adversarial training or contrastive learning. This could lead to a more distinct and innovative approach to self-improvement in LLMs. Furthermore, the authors should provide a more detailed breakdown of the computational costs associated with each step of their method. This should include not only the total training time but also the memory requirements and the number of GPU hours needed. Such information is crucial for researchers who wish to reproduce the results or adapt the method to their own settings. A clear understanding of the computational demands will also help in assessing the scalability of the approach.

To address the complexity of the method, the authors should aim to simplify the implementation process. This could involve providing more detailed pseudocode or a step-by-step guide that outlines the key stages of the algorithm. Furthermore, the authors could consider releasing a well-documented codebase that allows other researchers to easily replicate their findings. This would not only enhance the reproducibility of the work but also facilitate further research in this area. The authors should also consider expanding their evaluation to include a wider range of models, including models with different architectures and sizes. This would provide a more comprehensive understanding of the method's generalizability and robustness. Specifically, it would be beneficial to evaluate the method on models that are both smaller and larger than the Llama-3-8B-Instruct model used in the current study. This would help to determine whether the method is equally effective across different model scales.

Finally, the authors should investigate the impact of different hyperparameter settings on the performance of their method. This could involve conducting a sensitivity analysis to determine which parameters have the most significant influence on the results. This would provide valuable insights into the robustness of the method and help other researchers to fine-tune the algorithm for their specific applications. Additionally, the authors should consider comparing their method to other state-of-the-art self-improvement techniques, beyond just the Self-Rewarding baseline. This would provide a more comprehensive evaluation of the method's strengths and weaknesses and help to establish its position within the broader landscape of LLM self-improvement.

### Questions

* Could the authors provide more details on the computational resources required for training? This information would be valuable for researchers interested in reproducing the results or adapting the method to their own settings.

* Have the authors considered applying the method to other models? Evaluating the method on a wider range of models would help to establish its generalizability and robustness.

* What is the impact of different hyperparameter settings on the performance of the method? A sensitivity analysis could provide valuable insights into the robustness of the approach.

### Rating

6

### Confidence

4

**********

# CAMEx: Curvature-aware Merging of Experts

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Existing methods for merging experts during model training and fine-tuning predominantly rely on Euclidean geometry, which assumes a flat parameter space. This assumption can limit the model's generalization ability, especially during the pre-training phase, where the parameter manifold might exhibit more complex curvature. Curvature-aware merging methods typically require additional information and computational resources to approximate the Fisher Information Matrix, adding memory overhead. In this paper, we introduce CAMEx (Curvature-Aware Merging of Experts), a novel expert merging protocol that incorporates natural gradients to account for the non-Euclidean curvature of the parameter manifold. By leveraging natural gradients, CAMEx adapts more effectively to the structure of the parameter space, improving alignment between model updates and the manifold's geometry. This approach enhances both pre-training and fine-tuning, resulting in better optimization trajectories and improved generalization without the substantial memory overhead typically associated with curvature-aware methods. Our contributions are threefold: (1) CAMEx significantly outperforms traditional Euclidean-based expert merging techniques across various natural language processing tasks, leading to enhanced performance during pre-training and fine-tuning; (2) we introduce a dynamic merging architecture that optimizes resource utilization, achieving high performance while reducing computational costs, facilitating efficient scaling of large language models; and (3) we provide both theoretical and empirical evidence to demonstrate the efficiency of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents CAMEx (Curvature-Aware Merging of Experts), a novel method for merging experts in Sparse Mixture of Experts (SMoE) architectures. CAMEx leverages natural gradients to account for the non-Euclidean curvature of the parameter space, achieving more effective model alignment and improved performance.

### Strengths
1. Originality
CAMEx introduces a novel approach by leveraging natural gradients to accommodate the non-Euclidean geometry of the parameter space, moving beyond traditional Euclidean-based merging methods. This curvature-aware design aligns model updates more naturally with the parameter manifold’s structure, enhancing both optimization and generalization. Additionally, the dynamic merging architecture optimizes resource usage without performance loss, offering a new direction for efficiently scaling SMoE architectures. This geometry-aware expert merging approach represents a significant conceptual advance with potential applications in other areas of model optimization.
2. Quality
The paper is well-supported by both theoretical and empirical evidence, with robust experiments across multiple tasks demonstrating CAMEx’s effectiveness. The theoretical foundation reinforces the practical findings, adding to the reliability of the results.
3. Clarity
The paper is generally well-organized, presenting its methodology and results clearly. While some technical sections could be further optimized to enhance accessibility, the core contributions are conveyed effectively.
4. Significance
CAMEx addresses the critical need for scalable and efficient model architectures. Its consistent performance improvements across various tasks, coupled with reduced computational demands, underscore its practical impact. The success of CAMEx may also inspire further research into non-Euclidean methods within model optimization, highlighting its broader significance.
In summary, CAMEx’s originality, strong experimental support, and contribution to scalable architectures make it a technically sound and impactful addition to the field.

### Weaknesses
While CAMEx introduces a novel and promising curvature-aware approach, several areas could be improved to enhance the paper's rigor and impact.
1. Limited Baseline Comparisons
The paper primarily compares CAMEx with standard Euclidean-based and a few curvature-aware merging methods but lacks comparisons with a broader set of state-of-the-art SMoE techniques, especially recent adaptive or gradient-based approaches. Including a wider range of baselines would better contextualize CAMEx’s strengths and highlight its unique advantages.
Suggested Improvement: Expand comparisons to include additional recent methods in expert merging or routing within SMoE, particularly those emphasizing efficiency or scalability. This would reinforce CAMEx’s position within the current landscape.
2. Clarity in Theoretical Exposition
The theoretical basis for CAMEx, rooted in natural gradient theory and parameter manifold curvature, could benefit from added clarity. Specifically, the mathematical distinctions between CAMEx’s curvature-aware merging and Fisher-based methods may not be fully accessible to all readers, particularly regarding computational efficiency.
Suggested Improvement: Simplify or visually illustrate the theoretical explanation, potentially with diagrams or flowcharts, to clarify how CAMEx achieves computational advantages without sacrificing performance.
3. Limited Analysis on Hyperparameters
The paper provides only a brief discussion of key hyperparameters, such as the scaling factor α. Given that curvature-aware methods may be sensitive to parameter tuning, a more comprehensive analysis of these hyperparameters would offer valuable insights.
Suggested Improvement: Conduct a sensitivity analysis on α and other critical parameters, highlighting optimal settings across tasks. This would provide practical guidance for future users of CAMEx.

### Questions
1. Given CAMEx’s potential for scaling, have you tested its efficiency and performance on larger models? If such experiments were beyond the scope of this paper, could you provide any empirical or theoretical estimates of how CAMEx’s computational advantages scale with model size and expert count? This would better inform readers of its applicability to real-world, large-scale SMoE deployments.
2. Could you elaborate on the impact of key hyperparameters, particularly the scaling factor α, on CAMEx’s performance? A sensitivity analysis or guidance on optimal parameter settings across different tasks would be highly beneficial for practitioners looking to implement CAMEx effectively.

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
3

### Summary
The paper proposes CAMEx, a curvature-aware approach to merging experts in Sparse Mixture of Experts (SMoE) models. The work introduces a novel merging protocol that incorporates natural gradients to account for non-Euclidean parameter manifold geometry, a dynamic merging architecture that reduces computational costs while maintaining performance, and provides theoretical analysis showing how curvature-aware updates combine traditional domain-specific merging with task alignment adjustments. The empirical evaluation demonstrates consistent improvements across multiple NLP and vision tasks.

### Strengths
- The curvature-aware approach consistently outperforms traditional Euclidean-based merging methods across different tasks and architectures
- The dynamic merging architecture achieves the same number of experts but reduces FLOPs per token, providing a practical way to improve efficiency
- The Kronecker-based approximation for the curvature matrix is computationally practical and empirically effective based on ablation studies
- Strong theoretical analysis in Section 2.6 shows how gradients w.r.t curvature matrix combine domain-specific merging with an adjustment term for task loss alignment
- Thorough empirical evaluation across diverse tasks, including ablation studies examining impact of key parameters (α scaling factor, Kronecker rank)

### Weaknesses
 - Technical aspects of the method need clearer explanation - the causal segmenting approach lacks sufficient background/motivation in the main paper, key equations for merging need step-by-step walkthrough, and curvature-based updates require more detailed explanation
- Performance improvements are somewhat modest, especially on the GLUE benchmark tasks
- Training for longer appears to reduce the performance gap between proposed methods and baselines (Figure 3)
- Impact on larger model scales is not thoroughly explored - unclear if improvements would be more pronounced with models bigger than GPT-2
- Missing analysis of how different token-to-expert routing strategies might affect the method's performance

### Questions
- How does the choice of token-to-expert routing method (token-choice vs expert-choice) affect CAMEx performance?
- Would the performance improvements be more significant when training larger models?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a curvature-aware merging method using natural gradients. The experiments show that CAMEx can outperform Euclidean-based expert merging. I have read the paper several times and I really like the ideas from the paper. However, I would like to see more experimental result analysis about the model merging.

### Strengths
Curvature-aware merging is an interesting idea for expert merging.

### Weaknesses
1. In the section 3.2. "Ties-CA achieves the highest scores on SST-2 (94.61), MRPC (92.49), CoLA
(60.06), and MNLI (86.45), showing significant improvements over both the vanilla and standard
Ties models." Actually, the experiments in Table 2 don't show any significantance test. Could you present the significance test(T-test) of the improvement? Otherwise, you should reclaim these conclusions. 

2. The experiment results are not strong enough to prove the effectiveness of CAMEx. Could you show some downstream zero-out results based on your T5 model? Please refer to https://arxiv.org/abs/2405.11157. For example, the downstream results on question answering (boolq, OpenbookQA) and reasoning (BBH), 


3. The experiments only show the T5-base model. I am a little suspective that conclusions in the paper can also be generalized to other LMs. Could you show GLUE performance based on LLama-3 or phi-3( Vanilla, Ties, and Ties-CA is fine)? 

### Questions
I may miss something. What are the training datasets for table 2?

### Soundness
3

### Presentation
3

### Contribution
3

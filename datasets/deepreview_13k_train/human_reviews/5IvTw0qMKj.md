# C$^{2}$INet: Realizing Incremental Trajectory Prediction with Prior-Aware Continual Causal Intervention

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Trajectory prediction for multi-agents in complex scenarios is crucial for applications like autonomous driving. However, existing methods often overlook environmental biases, which leads to poor generalization. Additionally, hardware constraints limit the use of large-scale data across environments, and continual learning settings exacerbate the challenge of catastrophic forgetting. To address these issues, we propose the Continual Causal Intervention (C$^{2}$INet) method for generalizable multi-agent trajectory prediction within a continual learning framework. Using variational inference, we align environment-related prior with posterior estimator of confounding factors in the latent space, thereby intervening in causal correlations that affect trajectory representation. Furthermore, we store optimal variational priors across various scenarios using a memory queue, ensuring continuous debiasing during incremental task training. The proposed C$^{2}$INet enhances adaptability to diverse tasks while preserving previous task information to prevent catastrophic forgetting. It also incorporates pruning strategies to mitigate overfitting.
Comparative evaluations on three real and synthetic complex datasets against state-of-the-art methods demonstrate that our proposed method consistently achieves reliable prediction performance, effectively mitigating confounding factors unique to different scenarios. This highlights the practical value of our method for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces C2INet, a novel model designed to enhance multi-agent trajectory prediction in dynamic environments by addressing key challenges like environmental bias and catastrophic forgetting. C2INet incorporates a prior-aware memory module that stores optimal priors across tasks, enabling it to adapt incrementally to new scenarios while retaining performance on past tasks. A core component of the model is the continual causal intervention mechanism, which aims to disentangle latent confounding factors that could negatively impact prediction accuracy.

The model's design emphasizes a balance between computational efficiency and performance, employing variational inference to align environment-dependent priors with posterior estimates, thus maintaining robustness against latent biases. The inclusion of a pseudo-feature-based pruning strategy ensures the memory module remains efficient and manageable even as task volume increases. C2INet's framework is evaluated on datasets such as ETH-UCY and Stanford Drone, showcasing its strong adaptability and significant improvements in prediction metrics like Average Displacement Error (ADE) and Final Displacement Error (FDE) when compared to traditional trajectory prediction models.

### Strengths
The paper presents a novel method combining causal intervention with a continual learning framework, effectively addressing the problem of bias and forgetting in multi-task learning.

The experimental analysis demonstrates that C2INet performs robustly on multiple datasets, achieving significant improvements in trajectory prediction accuracy compared to existing methods.

The integration of the memory module and prior queue is well-motivated and effectively implemented to handle changing environments, showcasing the potential for real-world applications.

### Weaknesses
Although the paper introduces causal intervention comprehensively, some theoretical explanations, particularly regarding the optimization of KL divergence and multi-task prior adjustments, could benefit from simplification. This would make the paper more accessible to a broader audience.

The experiments are thorough but somewhat limited in terms of application diversity. The paper could be strengthened by including analyses on more varied or complex real-world scenarios, such as real-time predictions in live driving conditions.

Certain sections, such as the derivation of equations and framework details, are presented in a complex manner that may challenge the reader's understanding. A clearer and more concise explanation would enhance readability.

While the paper mentions addressing environmental biases, there is insufficient analysis of other types of potential biases in the dataset, such as sample distribution imbalance and long-tail effects. The paper does not delve deeply into how the model performs in broader contexts.

### Questions
Could the authors elaborate on how the proposed C2INet model could be implemented in practical real-world systems, especially where computational resources may be limited (e.g., embedded or low-power devices)?

Can the authors provide a more simplified explanation of the theoretical basis, particularly the optimization of KL divergence and the adjustment of priors in multi-task scenarios? This would help make the paper more accessible to a broader audience.

Is there any plan to test the generalization ability of C2INet on larger or more diverse datasets, including scenarios with real-time prediction in live driving conditions? How might the model perform in unseen or significantly different environments?

While the paper discusses mitigating environmental bias, how does C2INet handle other types of data biases, such as sample distribution imbalances or long-tail effects? Would these impact the model's performance or lead to biased predictions?

Could the authors provide more details about the computational complexity of C2INet, such as the number of parameters and resource usage? This would clarify the scalability and practicality of the model for large-scale or real-time applications.

### Soundness
2

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
3

### Summary
The study introduces C2INet, an innovative method for multi-agent trajectory prediction in intricate settings that utilizes ongoing causal intervention. C2INet integrates causal intervention and continuous learning inside a memory-enhanced framework to tackle challenges such as environmental bias, catastrophic forgetting, and hardware limitations in real-time multi-agent prediction. This method use variational inference to synchronize environment-related priors with a posterior estimator, guaranteeing precise trajectory representation by addressing confounding variables in the latent space.

C2INet's principal innovation is its ongoing learning process, which progressively adapts to new circumstances while maintaining performance on previously encountered ones. This is accomplished via a memory module that retains ideal priors across situations, therefore safeguarding essential knowledge and reducing overfitting via a pruning process. Comprehensive assessments of real-world datasets, including ETH-UCY and Stanford Drone, alongside synthetic datasets, reveal that C2INet surpasses conventional methods in predictive accuracy and resistance to task interference, attaining notable enhancements in metrics such as ADE and FDE across multiple tasks.

C2INet effectively mitigates significant shortcomings in current trajectory prediction models by integrating causal intervention with a continuous memory framework, hence guaranteeing strong performance in dynamic, multi-agent settings.

### Strengths
1. Adaptability to Multiple Scenarios:
By leveraging continual causal intervention, C2INet effectively handles confounding factors in diverse scenarios and retains information from previous tasks. This design enhances the model's adaptability to dynamic environments, making it suitable for multi-agent trajectory prediction in complex settings, such as autonomous driving and crowd monitoring.

2. Comprehensive Experimental Validation:
The paper provides extensive validation across multiple datasets (ETH-UCY, Stanford Drone, synthetic datasets) and compares C2INet with various baseline methods, including common causal intervention and continual learning approaches. The results demonstrate that C2INet outperforms traditional methods in key metrics (e.g., ADE and FDE), proving its effectiveness in handling catastrophic forgetting and improving prediction accuracy.

3. Modular Design:
C2INet’s design is modular, making it compatible with multiple baseline models (e.g., STGAT, SocialSTGCNN). This plug-and-play characteristic increases the flexibility of the approach, allowing it to be used in various model architectures and promoting wider applicability.

### Weaknesses
1. Innovative Design:
The paper introduces a novel model, C2INet, which combines causal intervention with continual learning, specifically using a memory module to retain optimal priors across different scenarios to mitigate catastrophic forgetting. This approach is relatively rare in multi-task learning and offers a degree of originality.

2. Adaptability to Multiple Scenarios:
By leveraging continual causal intervention, C2INet effectively handles confounding factors in diverse scenarios and retains information from previous tasks. This design enhances the model's adaptability to dynamic environments, making it suitable for multi-agent trajectory prediction in complex settings, such as autonomous driving and crowd monitoring.

3. Potential Limitations of the Prior Memory Module:
Although the prior memory module helps alleviate catastrophic forgetting, it heavily relies on storing priors for different tasks, which may lead to challenges in memory management and capacity. As the number of tasks grows, the memory module might struggle to scale efficiently. Additionally, the paper does not discuss how to effectively manage priority or memory compression when storage space is limited. The pruning strategy, while mentioned, lacks specifics on how similarity is calculated and what constitutes 'least contribution,' raising concerns about its practical effectiveness and potential for information loss.

4. Limitations of the Experimental Datasets:
Although the paper uses multiple datasets, these are mainly focused on specific domains (e.g., pedestrian and vehicle trajectory prediction) and lack diversity. The generalizability of the experimental results to more complex or diverse dynamic environments is unclear, limiting the method’s applicability to real-world scenarios. The datasets, while standard, do not fully capture the nuances of more complex multi-agent interactions, such as those involving non-holonomic agents or more intricate environmental constraints.

5. Complex Hyperparameter Tuning with Limited Guidance:
C2INet involves multiple key hyperparameters (e.g., the KL divergence adjustment coefficient, weights in the memory module) that significantly affect model performance, but the paper does not provide detailed guidance on tuning them. The complexity of hyperparameter tuning, combined with a lack of explicit guidelines, may hinder other researchers from reproducing and applying the method in different settings. The paper lacks a sensitivity analysis of these hyperparameters, making it difficult to understand their impact on the model's behavior and performance.

### Questions
You have not provided detailed mathematical derivations for the causal intervention section. Could you elaborate further or reference additional causal inference theories to support the method? Specifically, how do you ensure that the intervention effectively removes confounding factors, and have you considered potential causal relationships between different tasks?

What are the computational complexity and storage requirements of C2INet? How do you ensure real-time performance in hardware-constrained environments (e.g., embedded systems or mobile devices)? Is there a quantitative analysis of resource consumption, or have you tried to optimize the algorithm to reduce computational load?

As the number of tasks increases, will the storage requirements for the prior memory module become unmanageable? How do you manage priorities or compress the memory module effectively when storage space is limited? Have you considered the issue of memory overflow as the number of tasks continues to grow?

C2INet involves several key hyperparameters (e.g., the KL divergence adjustment coefficient, weights in the memory module). Could you provide insights on how to tune these hyperparameters? Have you considered an adaptive hyperparameter optimization mechanism to reduce the reliance on manual tuning?

The datasets used are mainly focused on pedestrian and vehicle trajectory prediction, which is somewhat limited in scope. Do you plan to test C2INet in more diverse and complex scenarios to evaluate its applicability and generalizability?

Given that C2INet includes multiple complex modules (e.g., memory module and causal intervention), how interpretable is the model? Do you plan to provide more intuitive visualizations or explanations to demonstrate the model’s decision-making process?

Since the paper has already discussed the situation of hardware resource constraints, has it considered other optimization methods such as hardware acceleration or knowledge distillation? What advantages does the proposed optimization method have compared to these alternative approaches?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes $C^2INet$ for trajectory prediction, introducing causal intervention to enable continuous trajectory prediction across evolving domains. To address the issue of catastrophic forgetting, they introduce a Continuity Memory Module. Experiments on three datasets demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper researches an interesting and critical problem in trajectory prediction.
2. The organization of the paper is somewhat reasonable.

### Weaknesses
Some format issue should be considered:
1. The citation format is wrongly used. 
2.  the vertical space is not proper set, especially on Page 4
3. Font size of Table 1 is too small, which is weird and does not match the main text

Some Weaknesses about the contents:
1. I’m so confused about the motivation of the work, especially the necessity of introducing causal intervention into the trajectory prediction task.

2. Existing continual learning methods also take into account the catastrophic forgetting problem by utilizing the experience replay mechanism. What are the differences between those CL methods and $C^2INet$? Can your method solve some critical problems that traditional CL methods cannot?

3. The authors use STGAT and STGCNN as backbones. They were proposed in 2016 and 2019, which are now outdated. The method should be integrated with cutting-edge backbones proposed in 2023 and 2024.

4. The results in terms of ADE/FDE on the SDD dataset are too high and seem strange. All results are above 50.0. Do you use a particular coordinate system instead of standard pixel coordinates?

5. Related works are not sufficient. More recent works from the past two years should be incorporated, such as diffusion models [1][2][3] and works with new settings [4][5].

### Questions
I’m not familiar with causal intervention, so I may not provide professional reviews on the technical part.
Questions for other parts, see weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

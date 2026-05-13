# Diffusion-Based Planning for Autonomous Driving with Flexible Guidance

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Achieving human-like driving behaviors in complex open-world environments is a critical challenge in autonomous driving. Contemporary learning-based planning approaches such as imitation learning methods often struggle to balance competing objectives and lack of safety assurance,due to limited adaptability and inadequacy in learning complex multi-modal behaviors commonly exhibited in human planning, not to mention their strong reliance on the fallback strategy with predefined rules. We propose a novel transformer-based Diffusion Planner for closed-loop planning, which can effectively model multi-modal driving behavior and ensure trajectory quality without any rule-based refinement. Our model supports joint modeling of both prediction and planning tasks under the same architecture, enabling cooperative behaviors between vehicles. Moreover, by learning the gradient of the trajectory score function and employing a flexible classifier guidance mechanism, Diffusion Planner effectively achieves safe and adaptable planning behaviors. Evaluations on the large-scale real-world autonomous planning benchmark nuPlan and our newly collected 200-hour delivery-vehicle driving dataset demonstrate that Diffusion Planner achieves state-of-the-art closed-loop performance with robust transferability in diverse driving styles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Current learning-based planning methods, such as imitation learning, often struggle with safety and adaptability, especially when dealing with the multi-modal behaviors typical of human drivers. To overcome these limitations, the authors introduce a novel transformer-based Diffusion Planner designed for closed-loop planning. This model captures multi-modal driving behaviors and ensures high-quality trajectories without relying on rule-based refinements. They integrate prediction and planning tasks within the same architecture to facilitate cooperative vehicle behaviors. Additionally, the Diffusion Planner enhances safety and adaptability by learning trajectory score gradients and utilizing a flexible classifier guidance mechanism.

### Strengths
S1. Reduces complexity  issue by collectively considering the status of key participants in the driving scenario and jointly modeling the motion prediction and closed-loop planning tasks as a future trajectory generation task.

S2. Integrating closed-loop planning with a diffusion model is an effective approach, and the use of the architecture is clearly articulated.

### Weaknesses
W1. Though PLUTO (hybrid method) performs better than Diffusion Planner in the NuPlan dataset, no comparison with PLUTO w or w/o refine is shown for the delivery-vehicle driving dataset.

W2. The paper would benefit from a more explicit and detailed statement of contributions, perhaps in a dedicated paragraph near the end of the introduction. This should clearly outline how the Diffusion Planner addresses each of the limitations mentioned and what specific novel aspects it introduces.

Minor Nitpicks

N1. A legend should be added to Appendix A, Figure 8
N2. Line 195: Conditions C could be mathematically defined

### Questions
Same as weaknesses. Additional questions:

Q1. Line 466-477, “Due to space limitations, …”, what space limitations is the author mentioning?

Q2. Could the authors elaborate on W1 and explain why PLUTO (with and without refinement) was not included in the comparisons on the delivery-vehicle driving dataset, given its strong performance on NuPlan?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel approach for autonomous driving using a transformer-based Diffusion Planner. By leveraging diffusion models, the authors address key challenges in autonomous driving, such as modeling multi-modal driving behavior and ensuring trajectory quality without relying on rule-based refinement. The approach demonstrates state-of-the-art performance on the nuPlan benchmark and a newly collected dataset.

### Strengths
The strengths of the paper are threefold.

1. The use of diffusion models in the autonomous driving planning task is novel. The authors effectively address the limitations of existing learning-based planning methods, such as handling multi-modal behaviors and out-of-distribution scenarios.

2. The paper provides a thorough explanation of the Diffusion Planner’s architecture and how it integrates prediction and planning tasks. The classifier guidance mechanism for adaptable planning behaviors is particularly well-explained.

3. The evaluations on the nuPlan benchmark and the delivery-vehicle dataset demonstrate impressive closed-loop performance, surpassing both learning-based and rule-based baselines. The method shows robust transferability, highlighting its potential for real-world applications.

### Weaknesses
The overall quality of this paper is strong. One minor area for improvement is the quantity of simulation benchmarks used. The paper evaluates planner performance solely based on the Test14 random benchmark, which consists of approximately 280 closed-loop scenarios. It would be beneficial to include additional simulation benchmarks from nuPlan, such as the Val14 benchmark and the Test14 hard benchmark, to provide a more comprehensive demonstration of the advantages of the proposed method over the baselines.

### Questions
The suggestion of improvement is stated in the *Weaknesses*. No further suggestions.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, a DiT-enabled framework is deployed to jointly tackle the motion planning task accompanying with predictions of surrounding agents for autonomous driving. Subsequently, a classifier-free gradient guidance are leveraged through a set of safety and comfortness costs during the diffusion step in guiding safe planning. Experimental results in Test14 demonstrate the effectiveness.

### Strengths
1. A novel diffusion-based framework in solving the motion planning task. Intutive DiT-enabled framework for integrated prediction and planning with costs guidance. 

2. Strong planning results delivered against state-of-the-art baselines in nuPlan.

### Weaknesses
1. Insufficient benchmark and metric comparison: 1) Additional results in other popular benchmark, such as Val14 and Test14-Hard are required to manifest the planning results under more diversed / challenging scenarios. 2) Other settings, such as closed loop reactive simulation, and open loop results are not verified.

2. Insufficient baseline comparison. Motion planning / trajectory simulation leveraging diffuision are not novel. Hence, the planning results using other diffusion strategies ([1] [2] for instance) seems needed.

### Questions
N/A.

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
3

### Summary
This paper proposes a diffusion-based motion planner for autonomous driving. The diffusion model is trained to generate joint trajectories of the ego and neighboring vehicles. Classifier guidance is introduced to regularize the safety, comfort, and feasibility of the ego vehicle's trajectory. Several practical implementation designs, such as data augmentation and normalization, are introduced to improve the model performance for closed-loop planning. Comprehensive experiments are conducted on the nuPlan benchmark.

### Strengths
The proposed model is carefully designed and extensively tailored for practical application in autonomous driving. The experiments are comprehensive, with multiple baselines and detailed ablation studies. It achieves better performance than the current state-of-the-art methods on the nuPlan leaderboard. Detailed descriptions of the model implementation and experiment design are provided. This work provides useful lessons for the community on achieving good closed-loop planning performance with diffusion-based motion planners for practical autonomous driving applications.

### Weaknesses
1. While I believe this work has good practical values for the autonomous driving community, diffusion models have been explored in several works for motion prediction, closed-loop simulation, and motion planning in autonomous driving. The authors attempted to differentiate their work from existing works by emphasizing that the diffusion model does not drive performance improvements in these cases but relies on rule-based refinement or LLM, and they claimed that they are the first to fully harness the potential of diffusion models to enhance closed-loop planning performance in autonomous driving. However, this statement is quite vague, and it is unclear what novel technical contributions the authors have made in this work. My current impression is that the proposed model combines existing techniques investigated in the literature on diffusion models and learning-based motion planning for autonomous driving (e.g., transformer architecture, classifier guidance with manually designed cost functions, data augmentation, etc.). To help the audience better appreciate their novelty and contributions, the authors may list their novel contributions at the end of the Introduction. 

2. Related to the first point, the authors should provide a more extensive review of the related literature on diffusion models for autonomous driving. The authors currently give a concise discussion in Sec. 3.2. It should be moved to the related work section and extended to be more comprehensive. In particular, the current review misses an essential line of research on diffusion models for closed-loop simulation (e.g., [1], [2], [3]). Also, some works have developed diffusion-based motion planners for nuPlan (e.g., [4], [5], and [6]; the authors cited [4][5], but they are not included as baselines). If possible, they should be included as baselines for comparison.

### Questions
1. In Table 1, the authors only reported the proposed diffusion planner with collision guidance. How does the model perform with other types of guidance, especially when multiple guidance costs are used? 

2. When multiple guidance terms are used, the guidance cost becomes a weighted sum of several cost terms. I wonder if the authors have taken special care to ensure that the scales of different cost terms and their gradients are well balanced. It would be great if the authors could discuss if the guidance performance is sensitive to energy function design and cost weights.

### Soundness
3

### Presentation
2

### Contribution
3

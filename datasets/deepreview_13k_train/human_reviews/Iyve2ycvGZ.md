# Bellman Optimal Stepsize Straightening of Flow-Matching Models

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Flow matching is a powerful framework for generating high-quality samples in various applications, especially image synthesis. However, the intensive computational demands of these models, especially during the finetuning process and sampling processes, pose significant challenges for low-resource scenarios. This paper introduces Bellman Optimal Stepsize Straightening (BOSS) technique for distilling flow-matching generative models: it aims specifically for a few-step efficient image sampling while adhering to a computational budget constraint. First, this technique involves a dynamic programming algorithm that optimizes the stepsizes of the pretrained network. Then, it refines the velocity network to match the optimal step sizes, aiming to straighten the generation paths. Extensive experimental evaluations across image generation tasks demonstrate the efficacy of BOSS in terms of both resource utilization and image quality. Our results reveal that BOSS achieves substantial gains in efficiency while maintaining competitive sample quality, effectively bridging the gap between low-resource constraints and the demanding requirements of flow-matching generative models. Our paper also fortifies the responsible development of artificial intelligence, offering a more sustainable generative model that reduces computational costs and environmental footprints.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author introduces the Bellman Optimal Step-size Straightening (BOSS) technique, a method for distilling flow-matching generative models that enhances the efficiency of image sampling within computational budget constraints. BOSS utilizes dynamic programming to optimize step sizes in a pretrained network and refines the velocity network to straighten generation paths. In this paper, the proposed method has been extensively evaluated on image generation tasks, showing that it significantly improves resource efficiency and maintains high image quality. This approach serves to reconcile the intensive computational demands of flow-matching models with low-resource availability, contributing to the sustainable development of artificial intelligence by reducing computational expenses and environmental impacts.

### Strengths
The BOSS (Bellman Optimal Step-size Straightening) method presents an innovative two-phase approach for adapting pretrained flow-matching models. This paper illustrates that BOSS can straighten the velocity network with approximately 10,000 retraining iterations, which marks a significant improvement in efficiency compared to standard practices. Consistently, BOSS achieves lower FID scores in the task of unconditional image generation across a variety of datasets, suggesting superior image quality relative to competing methods. Moreover, the paper introduces a distinctive methodology for calculating optimal sampling step sizes through dynamic programming, thereby increasing the sampling process's efficiency.

### Weaknesses
Although the paper demonstrates significant improvements in image quality and efficiency, its testing is concentrated on specific datasets. A more comprehensive comparative analysis with current state-of-the-art methods would elucidate the advancements BOSS provides, especially in efficiency and quality. Specifically, the paper lacks a comparison against a wider range of diffusion-based models and other flow-matching techniques, making it difficult to assess the true magnitude of the improvement. Additionally, while the paper addresses low-resource scenarios, it lacks a clear comparison of resource requirements such as memory usage, power consumption, or processing time, essential for evaluating BOSS's practicality for users with limited computational resources. The absence of detailed profiling data makes it challenging to understand the trade-offs between computational cost and performance gains. Furthermore, despite the method's enhancements over existing approaches, the computational intensity of the dynamic programming algorithm and the network retraining requirement could limit its utility in resource-constrained settings. The paper does not provide a detailed analysis of the time complexity of the dynamic programming algorithm, nor does it explore alternative optimization strategies that could reduce computational overhead. The scalability of BOSS, with respect to increasing dataset sizes or complexity, is also not addressed, and an evaluation of this aspect would greatly benefit the paper's comprehensiveness. It remains unclear how the method would perform on datasets with significantly larger numbers of samples or with higher image resolutions beyond 256x256, which is a critical consideration for real-world applications.

### Questions
Could the authors extend their testing to include a broader range of datasets and perform a comprehensive comparative analysis with current state-of-the-art methods to better highlight the efficiency and quality improvements of the BOSS method? 
Can the paper provide a detailed comparison of resource requirements, such as memory usage, power consumption, or processing time, to evaluate the practicality of BOSS for users with limited computational resources? 
How does the computational intensity of the dynamic programming algorithm and the network retraining requirement impact the method's applicability in resource-constrained environments?
 Additionally, has the scalability of BOSS been assessed in relation to increasing dataset sizes or complexity, and if not, would the authors consider evaluating this to enhance the paper's comprehensiveness?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Flow matching is a powerful framework for generating high-quality samples, especially in image synthesis. However, the computational demands of these models pose challenges in low-resource scenarios. This paper introduces the Bellman Optimal Step-size Straightening (BOSS) technique for efficient image sampling within a computational budget. BOSS optimizes step sizes and refines the velocity network to improve generation paths. Experimental evaluations demonstrate BOSS's effectiveness in resource utilization and image quality. It provides a sustainable solution that reduces costs and environmental footprints.

### Strengths
Not only in flow matching, but also in diffusion models, all endeavors are focused on predicting the efficiency of noise, score, and vector field. While most of them set the step size based on a heuristic principle (e.g., DDIM, DDPM), this paper explores generative models of ODE from a different perspective - the step size itself, rather than the "direction" of a specific step.

### Weaknesses
 - The baseline is too weak, as it only compares quantitatively with the fixed-step size ODE solver euler, while it doesn't compare with adaptive step size ODE solvers such as dopri5 or rk45. This comparison should be included in Table 1.
- The optimization needs to be conducted on a case-by-case basis. Additionally, the use of the dynamic programming algorithm using Gorubi may result in slow performance, rendering the method impractical. Optimization time is also not discussed in this paper.

### Questions
as above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new sampling strategy for flow-matching (flow-reflected) generative models. Formally, the authors analyze the sampling error estimation and propose to formulate the sampling process as a dynamic programming problem. Then the task is addressed by the bellman optimal schedule. Moreover, the authors proposed to re-align the velocity network along the accumulated sampling errors, which enjoys good performance.

### Strengths
1. The authors clearly present the issue of sampling error in flow-matching generation.
2. It is interesting and intuitive to formulate the sampling schedule as a dynamic programming problem. The solution is convincing.
3. This paper is well-written with clear motivations.

### Weaknesses
1. Although the main idea of this paper is interesting, this paper gives me the initial impression of being incomplete, with this incompleteness of the presentation of both the methodology and experimental sections.
2. For method Sec.3.3, the authors did not provide enough details about how to address the dynamic programming (DP) problem in practice. From the experiments, different datasets should share different sampling schedules. Moreover, how many samples are used to calculate the optimal scheduler? What will the optimal scheduler be like, if using different initial noises? The analysis of the generalization of the optimal scheduler selected by DP is very important.
3. Missing necessary discussions about diffusion sampling schedules in related works (such as [1]). Moreover, the related works are too simple, and only include some matching-flow methods.
3. Insufficient qualitative comparisons: the authors only provide qualitative comparisons of human faces.
4. No details about the velocity network re-alignment training are provided.

### Questions
Although this paper enjoys interesting idea, it suffers from incomplete related works, experimental results, analysis, and methodology/implementation details, which largely limit the quality of this paper. I think this paper needs a major revision before the publication.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

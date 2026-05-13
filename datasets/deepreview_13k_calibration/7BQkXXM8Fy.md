# What Makes a Good Diffusion Planner for Decision Making?

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 10, 6, 8

## Abstract
Diffusion models have recently shown significant potential in solving decision-making problems, particularly in generating behavior plans -- also known as diffusion planning. While numerous studies have demonstrated the impressive performance of diffusion planning, the mechanisms behind the key components of a good diffusion planner remain unclear and the design choices are highly inconsistent in existing studies. In this work, we address this issue through systematic empirical experiments on diffusion planning in an offline reinforcement learning (RL) setting, providing practical insights into the essential components of diffusion planning. We trained and evaluated over 6,000 diffusion models, identifying the critical components such as guided sampling, network architecture, action generation and planning strategy. We revealed that some design choices opposite to the common practice in previous work in diffusion planning actually lead to better performance, e.g., unconditional sampling with selection can be better than guided sampling and Transformer outperforms U-Net as denoising network. Based on these insights, we suggest a simple yet strong diffusion planning baseline that achieves state-of-the-art results on standard offline RL benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper analyses key components (guided sampling algorithms, network architectures, action generation methods, and planning strategies) critical to decision-making in diffusion planning.  The paper gives practical tips about the choices
and provides insights into the strengths and limitations of diffusion planning. The experiments in the paper are very comprehensive.

### Strengths
The experiments in the paper are very comprehensive.

### Weaknesses
Although the experiments in the paper are rich, readers still want to see how the original innovation in theory can better apply diffusion models to decision-making tasks

### Questions
No

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper presents an extensive experimental study aimed at understanding the factors that contribute to an effective diffusion planner for decision-making in offline reinforcement learning. The authors provide valuable insights into the role of various components within diffusion models. Building on these insights, they propose a straightforward yet robust diffusion planning approach that delivers state-of-the-art (SOTA) performance in standard offline RL benchmarks.

### Strengths
1. This paper is well-organized and easy to follow.
2. The empirical analysis is comprehensive, providing solid support for the conclusions. 
3. Each conclusion is accompanied by decent explanations

### Weaknesses
While the paper provides strong evidence for the effectiveness of the proposed methods on the D4RL dataset, it is unclear how generalizable these findings are to other types of decision-making problems or datasets. More diverse datasets could strengthen the claims.

### Questions
No

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the design choices in diffusion model planning within offline reinforcement learning (RL). Through experiments on over 6,000 models, the paper systematically investigates key components of diffusion planning, including sampling algorithms, network architectures, action generation methods, and planning strategies. The study finds that some design choices, such as unconditional sampling outperforming guided sampling and Transformer outperforming U-Net, lead to better performance. Based on these insights, the paper proposes a simple yet strong baseline model called Diffusion Veteran (DV), which achieves state-of-the-art results on standard offline RL benchmarks.

### Strengths
1.Comprehensive empirical study: The paper conducts a large-scale experimental study, using controlled variable methods to analyze the impact of each component on model performance, providing rich data support.
2.Innovative insights: The study reveals design choices that contrast with common practices in diffusion planning, such as the advantages of unconditional sampling and the use of Transformer, offering new directions for future research.
3.Simple yet effective baseline model: The proposed DV model is simple but performs exceptionally well, demonstrating high generalizability and effectiveness, laying a solid foundation for further research.
4.Wide applicability: The DV model performs well in multiple tasks such as maze navigation and robot manipulation, demonstrating its adaptability and broad applicability.

### Weaknesses
1.Limited exploration of long-term dependencies: While the paper discusses the importance of handling long-term dependencies using Transformer, it does not delve deeply into how this is manifested across different tasks. The related discussion could be more robust. Specifically, the paper lacks a detailed analysis of the attention patterns within the Transformer architecture across different environments. It would be beneficial to see visualizations of attention weights to understand which parts of the trajectory the model focuses on when making predictions, and how these patterns vary across tasks with different temporal structures.
2.Potential typo in Equation 2.1: There seems to be a typo on the right-hand side of Equation 2.1, where S(t−1) appears, which might be incorrect.

### Questions
1.You mention that unconditional sampling outperforms guided sampling, which contrasts with results in typical image generation tasks. Could you elaborate on the underlying reasons behind this phenomenon?
2.The paper primarily focuses on state-based tasks. Are there plans to extend the study to vision-based or goal-conditioned reinforcement learning tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors investigated the design choices for diffusion model-based offline RL methods. 
The design choices mainly focused on planning strategy, network architecture, guided sampling, and action generation (whether to generate both state and action directly, or generate only the state and estimate the action separately using an inverse dynamics model). 
The tasks used in the study were Maze2D, AntMaze, and Franka kitchen (MuJoCo locomotion also used in section 4.6).

### Strengths
This paper investigates the design choices for diffusion model-based offline RL methods and identifies effective components. Although various (algorithm/implmentation) designs have been proposed in previous research on diffusion model-based offline RL methods, their effectiveness in a unified framework has not been sufficiently explored. 
In general, the performance of reinforcement learning methods largely depends on design choices. 
Therefore, this paper, which provides insights into effective design choices, has value on the engineering front.

### Weaknesses
The number of tasks used to investigate the design choices is limited. This paper focuses on Maze2D (2 tasks), AntMaze (3 tasks), and Franka kitchen (4 tasks) (with MuJoCo locomotion tasks also included in section 4.6). However, for a paper investigating design choices, this is fewer than the number of tasks typically covered in papers accepted at ICLR (or conferences of a similar level). For instance, the paper [1] that investigated the implementation design of Offline + Online RL used 30 tasks in its study.

Moreover, the paper does not verify the insights/findings on a different set of tasks (i.e., validation tasks) from those used in the design choice investigation. This leaves uncertainty about how generalizable the insights are (or whether they are simply overfitted to the tasks examined).


[1] Ball, Philip J., et al. "Efficient online reinforcement learning with offline data." International Conference on Machine Learning. PMLR, 2023.


Minor comments:  

Line 018: 
> We trained and evaluated over 6,000 diffusion models  

I didn’t quite understand the breakdown of these 6,000 diffusion models. Were most of these models the ones trained and evaluated through the grid search mentioned in the step (1) in Section 3.2?  

Line 174: 
> (1) Conduct a comprehensive search on the key components (Sect. 3.1) by combining grid search and manual tuning to obtain the best results.  

What exactly does "manual tuning" refer to in this context?

Figure 5.  
It seems that the Transformer score for Kitchen-M doesn’t have a confidence interval. 
Also, I wasn’t clear on what the confidence intervals in the other parts of this figure represent (are they calculated based on 500 episode seeds?). 

Typoes:  
line 101: Zhang et al., 2022) In  -> Zhang et al., 2022). In  
line 158:  Chen et al., 2024)) -> Chen et al., 2024).  
line 479: planning(Sect. 4.6) -> planning (Sect. 4.6).

### Questions
Please refer to my previous comment on the weaknesses.
If either (1) validation results from tasks other than those used to investigate the design choices, or (2) validation results from 20-30 tasks were provided to support the insights on design choices, I would be inclined to recommend an Accept (assuming other reviewers do not point out any major weaknesses that I may have overlooked).

### Soundness
2

### Presentation
3

### Contribution
3

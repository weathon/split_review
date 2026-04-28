# FlickerFusion: Intra-trajectory Domain Generalizing Multi-agent Reinforcement Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Multi-agent reinforcement learning has demonstrated significant potential in addressing complex cooperative tasks across various real-world applications. However, existing MARL approaches often rely on the restrictive assumption that the number of entities (e.g., agents, obstacles) remains constant between training and inference. This overlooks scenarios where entities are dynamically removed or $\textit{added}$ $\textit{during}$ the inference trajectory—a common occurrence in real-world environments like search and rescue missions and dynamic combat situations. In this paper, we tackle the challenge of intra-trajectory dynamic entity composition under zero-shot out-of-domain (OOD) generalization, where such dynamic changes cannot be anticipated beforehand. Our empirical studies reveal that existing MARL methods suffer $\textit{significant}$ performance degradation and increased uncertainty in these scenarios. In response, we propose FlickerFusion, a novel OOD generalization method that acts as a $\textit{universally}$ applicable augmentation technique for MARL backbone methods. FlickerFusion stochastically drops out parts of the observation space, emulating being in-domain when inferenced OOD. The results show that FlickerFusion not only achieves superior inference rewards but also $\textit{uniquely}$ reduces uncertainty vis-à-vis the backbone, compared to existing methods. Benchmarks, implementations, and  model weights are organized and open-sourced at $\texttt{\href{flickerfusion305.github.io}{\textbf{flickerfusion305.github.io}}}$, accompanied by ample demo video renderings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the MARL problem that entities like teammates or adversaries are dynamically removed or added during the inference trajectory. The key idea is to dropout observation of some sampled entities at each step, denoted as flickers, and fuse these flickers to emulate a full-view across the temporal dimension. Numerical results and demos on MPEv2 demonstrate FlickerFusion’s promising performance.

### Strengths
- The idea of dropping out observation of some sampled entities at each step and fuse these flickers to emulate a full-view across the temporal dimension is inspiring.
- Authors extended the widely-used MARL benchmark MPE, which can be beneficial for relevant future research.
- FlickerFusion is compared with 11 baselines, providing sufficient and solid results.
- Demo videos clearly show how FlickerFusion works.

### Weaknesses
 - “Dropout” is the core idea and concept of this paper, but it only appears at the end of Introduction and has not been clearly defined. It would be better if authors define and emphasize it in Abstract of the beginning of Introduction, and distinguish it with the dropout operation in the neural network literature.
- Preliminaries is a bit too complex, it would be better to simplify it and relate it to the previous text, including some practical examples for illustration.
- The importance of each entity is different, but the flicker operation treats all entities equally by sampling uniformly. A module that evaluates entities’ intention / importance / uncertainty, using techniques like opponent modeling[1,2], should be developed to better guide the sampling of the flicker operation.
- The environment dynamics would change dramatically when the number of entities change. It is not clear how FlickerFusion handles this problem and realizes generalization. A clear study on this problem is vital for the application on more complex scenarios.
- The learning curves should demonstrate standard deviation.
- More related work about varying agent numbers[3] and intra-trajectory teammate shift[4] should be discussed.

### Questions
See Weaknesses.

And, for this dynamic entity number problem (in MPEv2), is it possible to build a mapping that maps the dimension-varying vector observation to images (the ones you used to render the demos), so that we can simply and directly utilize a CNN to handle the issue?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces FlickerFusion, a method designed to improve how multi-agent reinforcement learning (MARL) models generalize to environments with a dynamically changing number of agents. The approach involves randomly omitting agents’ observations during training, which helps the model perform better in new, dynamically changing environments in a zero-shot manner. The authors also present a modified version of Multi Particle Environments that supports variable numbers of agents to test their method.

### Strengths
- This paper tackles an important generalization capability in MARL.
- FlickerFusion is straightforward and can be easily integrated into various MARL frameworks.

### Weaknesses
 - MARL is generally challenging to stabilize during training. By altering observations at each timestep, this method should increase instability in principle, yet the paper does not explain how FlickerFusion manages to achieve less variability in results compared to the baseline QMIX, as shown in Table 1 and Figure 5.
- The evaluation relies solely on the Multi Particle Environments (MPE), which has a relatively simple observational setup. It remains uncertain if FlickerFusion would be effective in more complex environments such as SMAC. Specifically, the observation space in MPE is low-dimensional and contains information about the positions and velocities of other agents, which might not be representative of more complex scenarios with high-dimensional inputs such as images or more intricate state representations. The method's performance in environments requiring more sophisticated perception and reasoning remains unclear.
- Figures 3 and 5 in the paper would be more informative if they included quantiles instead of only the means.

### Questions
- In MPE, instead of randomly omitting entities, wouldn’t it make more sense to omit those farther from the ego agent based on their distance?
- How does omitting observations differ from the practice of dropping out nodes in standard neural network training?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses multi-agent reinforcement learning (MARL) with a dynamic number of entities. Unlike existing methods that introduce extra parameters, the proposed novel method, FLICKERFUSION, functions as an augmentation technique that selectively drops entities to ensure the observation space aligns with the policy network, regardless of changes in the number of entities. The experiments and ablation studies demonstrate the superior performance of the proposed method and clarify its operational mechanisms.

### Strengths
1. The issue of zero-shot out-of-domain (OOD) generalization in MARL is significant in bridging the gap between laboratory MARL research and real-world deployment.
2. The concept of FLICKERFUSION, which involves dropping out entities and recovering lost information, is novel and inspiring.
3. Although the paper uses only one series of benchmarks, MPEV2, it includes several different scenarios and baselines to demonstrate the robust performance of the proposed method.
4. The presentation is clear, and the details are effectively conveyed in the text and the Appendix.

### Weaknesses
1. The conceptualization of the paper appears to be excessive. For example, "intra-trajectory" is discussed in detail in the introduction section but is not mentioned in the methods section, which may confuse the audience. Additionally, some key points and implementations of the proposed method are not conveyed in the introduction. For instance, the technique of dropout, which is central to the method, is missing from both the abstract and the introduction, making it difficult to grasp the core mechanism early on.
2. The paper seems to overlook situations where there are different types of entities with varying lengths and/or compositions of observation space. In such cases, the stochastic dropout approach may not be effective, as it could lead to inconsistent input sizes for the policy network if not handled carefully. For instance, if one entity type has a 10-dimensional observation and another has a 20-dimensional observation, randomly dropping entities might not result in a consistent input dimension, unless the method explicitly accounts for this heterogeneity.

### Questions
1. How would the proposed method operate in situations where there are different types of entities with varying lengths and/or compositions of observation space?
2. In Figure 5, I suggest that the authors use a different line type for the proposed method to clearly distinguish FLICKERFUSION from the baselines.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces FLICKERFUSION,  a novel method aimed at enhancing out-of-domain (OOD) generalization in Multi-Agent Reinforcement Learning (MARL) environments where the composition of entities changes dynamically within a trajectory. The authors identify two significant challenges: intra-trajectory dynamic entity addition and zero-shot OOD generalization, which existing methods fail to handle effectively. FLICKERFUSION utilizes stochastic input-space dropout to maintain observation space consistency without additional parameters, achieving superior performance across a newly developed benchmark suite, MPEV2. Empirical results show that FLICKERFUSION outperforms existing approaches in both inference reward and uncertainty reduction.

### Strengths
1.The paper addresses a critical yet under-explored problem in MARL, specifically the intra-trajectory dynamic entity composition and its impact on generalization. The proposed approach, which uses entity dropout and stochastic fusion, is original and impactful.

2.The introduction of the MPEV2 benchmark enhances the paper's contribution, allowing a rigorous assessment of the proposed method. The results across various environments are convincing and demonstrate clear performance improvements.

3.The code and benchmarks are made publicly available, supporting reproducibility and further research in this domain.

4.This paper includes many baselines to  validate its efficiency.

### Weaknesses
1.This paper addresses some open problems in MARL. However, it lacks discussion on several related areas, such as multi-agent policy transfer [1] and sudden policy changes [2]. Including a more comprehensive analysis of these works could strengthen the paper.

2.The definition of OOD is unclear and too simple.

3.The use of the 'Flicker Fusion Phenomena' in this study is intriguing. However, the random masking approach might result in the loss of team semantic information. Alternative methods, such as learning to group[3] or applying the widely used mean-field theory in MARL[4], could potentially offer more advantages. Could the authors elaborate on the strengths and weaknesses of their approach compared to these methods?

4.Could this paper be further enhanced by incorporating Large Language Models (LLMs) like ChatGPT[5]?

### Questions
1.How does FLICKERFUSION perform in environments with extremely high or low densities of entity changes? Is the dropout strategy adaptable enough to handle these scenarios effectively?

2.Could this method be extended to other benchmarks, such as SMAC, MAgent, or CityFlow?

Ref

[1] Yuan L, Zhang Z, Li L, et al. A survey of progress on cooperative multi-agent reinforcement learning in open environment[J]. arXiv preprint arXiv:2312.01058, 2023.

### Soundness
3

### Presentation
3

### Contribution
3

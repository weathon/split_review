# LASeR: Towards Diversified and Generalizable Robot Design with Large Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Recent advances in Large Language Models (LLMs) have stimulated a significant paradigm shift in evolutionary optimization, where hand-crafted search heuristics are gradually replaced with LLMs serving as intelligent search operators. However, these studies still bear some notable limitations, including a challenge to balance exploitation with exploration, often leading to inferior solution diversity, as well as poor generalizability of problem solving across different task settings. These unsolved issues render the prowess of LLMs in robot design automation largely untapped. In this work, we present LASeR -- Large Language Model-Aided Evolutionary Search for Robot Design Automation. Leveraging a novel reflection mechanism termed DiRect, we elicit more knowledgeable exploratory behaviors from LLMs based on past search trajectories, reshaping the exploration-exploitation tradeoff with dual improvements in optimization efficiency and solution diversity. Additionally, with evolution fully grounded in task-related background information, we unprecedentedly uncover the inter-task reasoning capabilities of LLMs, facilitating generalizable design processes that effectively inspire zero-shot robot proposals for new applications. Our simulated experiments on voxel-based soft robots showcase distinct advantages of LASeR over competitive baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents LASeR, an framework leveraging Large Language Models (LLMs) to optimize robot design with evolutionary algorithms. The proposed approach addresses the limitations of existing LLM-driven optimization techniques, such as limited solution diversity and generalizability across tasks. LLM is employed as the intelligent search operator and diversity reflecter, instead of a tool for hyperparameter tuning. By introducing a Diversity Reflection Mechanism (DiRect), LASeR refines the exploration-exploitation tradeoff, enhancing diversity and performance of the robot design automation tasks, comparted to baselines. Through task-grounded prompts, LASeR also enables effective knowledge transfer across different robot design tasks.

### Strengths
* The paper is clear and well-structured.
* The idea of applying LLMs in generating offspring for robot design evolutionary algorithms is interesting.
* Extensive experimental results on EvoGym are provided to validate that the proposed method outforms baselines in both design efficiency/performance and diversity.

### Weaknesses
 * The experiments of the paper did not mention the time taken of the LLM-based methods for the evolutionary algorithm, which should be considered into the evaluation of robot design efficiency. 
* The similarity threshold seems to be an important hyperparameter for the proposed method, while it is not discussed in the paper. Specifically, the paper lacks a discussion on how the threshold affects the balance between exploration and exploitation within the evolutionary algorithm. The choice of this threshold likely has a significant impact on the diversity of the solutions and the overall performance of the optimization process, and a more detailed analysis is needed.
* The experiments in the paper are restricted to relatively simple voxel-based soft robots within predefined settings. The design space, while combinatorially large, is still limited in terms of complexity and real-world applicability. The paper should address the limitations of the experimental setup and discuss the potential challenges in scaling the proposed approach to more complex robot designs.
* The core method does not involve learning or fine-tuning for LLMs besides PPO utilized for the fitness evaluation. The paper does not explore the potential benefits of fine-tuning the LLM for the specific task of robot design, which could potentially lead to improved performance and generalization capabilities.

### Questions
* What considerations were taken when selecting similarity thresholds? How do you balance the diversity and performance of the generated designs?
* In Section 3.2.1, you mentioned that the fitness performance of robot designs would not change significantly after being modified by DiRect. Do you have quantative results to support this conclusion? 
* How does the computation time of LASeR compared to the baselines, including LLM-Tuner and the ones without using LLMs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors introduce LASER (Large Language Model-Aided Evolutionary Search for Robot Design Automation), a novel approach that leverages Large Language Models (LLMs) to enhance the efficiency and diversity of robot design automation. In  LASER, LLM is integrated into the bi-level optimization framework, and the LLM is prompted to be the mutation operator for generating new robot morphologies.

### Strengths
1. The authors proposed a reflection mechanism for automated robot design, DiRect, to encourage more knowledgeable exploratory behaviors from LLMs based on past search trajectories. Besides, they effectively leverage the reasoning and decision-making capabilities of LLMs to improve the inner-task transfer propagability.

### Weaknesses
1. The use of LLM as an evolutionary operator (powered by prompt engineering) is interesting, similar ideas such as "Evolution through Large Models (ELM)" and [1-2] have been proposed. The paper shows a possible pipeline of integrating LLM into the co-design process of VSR, but does not provide a deeper analysis about "Why LLM works well?". The black-box nature of LLMs can make it challenging to understand the reasoning behind the generated designs, Adding more explanations in the LLM's decision-making process would be beneficial.

2. The paper mentions experimenting with different temperatures but does not provide a detailed sensitivity analysis of different prompts. In my opinion, the explanation of the intuition of your designed prompts is more important than the proposed pipeline. 

3. This paper is missing a comparison with some important baseline algorithms.

4. The test tasks chosen for this paper are too simple to demonstrate the superiority and validity of large language models.

### Questions
1. The testing tasks such as Walker-v0 and Carrier-v0 used in the paper are too simple, can you test your method on more complex tasks ("Climber-v0", "Catcher-v0", "Thrower-v0" and "Lifter-v0"), which I think are more suitable to answer the question "Does LLM really have an advantage ?"

2. Can large language models really align a robot's design with its task performance? Is it enough to just use prompt engineering for more complex tasks? Can it be used as a surrogate model to predict the performance of a robot design? Can the authors give some explanations?

3. Can the current framework scale to more complex and larger robot designs (10x10 design space for walking)? If not, what are the potential bottlenecks? In larger design space (10 x 10), does LLM still work well? For some tasks, random combinations of voxels generated by LLM or evolutionary operators don't always work well.

4. To further improve this paper, it is better to show the designed robots by LLM and add analysis of the differences between llm-generated robot designs and  GA-generated robot designs.

5. While the paper demonstrates inter-task knowledge transfer, how well does LASER generalize to tasks that are significantly different from the ones used in the experiments? What are the limitations of this generalization?

6. The authors need to compare their approach with those that also use LLM as a mutation operator， such as openELM (Evolution through Large Models (ELM)) and more recent brain-body co-design methods (does not use LLM) which also use EvoGym platform, to show the effectiveness.

### Soundness
3

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
4

### Summary
The paper investigates the use of large language models in designing and evolving robots. To this end the paper uses an LLM to reflect and propose novel 'soft' robot designs in simulation in an evolutionary design loop. The paper compares its proposed LLM-evolution loop against different baselines and presents in-depth ablations of different effects LLM parameters have on the design loop.

### Strengths
- To the best of my knowledge the proposed framework is novel, the usage of LLMs in the problem of robot designs and their evolutions is under-researched
- The conclusions the paper makes, and its application are relevant to the robot learning community
- The paper compares its proposed approach versus several baselines
- The performed ablation studies are very interesting and insightful. I appreciate them.

### Weaknesses
Weaknesses:
- The environments in which the method is tested are relatively simple. However, I appreciate the hardness of the overall problem; designing and evolving robot hardware is not easy.
- A critical remark is that while the mean shows (in plots and tables) that the proposed method works, I think it is likely not statistically significant due to the standard deviation and the closeness of the final means.
- I think the paper could overall more critically discuss its limitations and open problems.
- The paper should probably cite and discuss this preliminary work discussing the potential of LLMs for the robot design process: Stella, Francesco, Cosimo Della Santina, and Josie Hughes. "How can LLMs transform the robotic design process?." Nature machine intelligence 5, no. 6 (2023): 561-564.

### Questions
I have no questions, overall I think the paper is in a good state and interesting to the ML/robotics community.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes and evaluates an LLM-based evolutionary operator for robot design. The proposed method distinguishes itself from prior related work by incorporating an explicit mechanism for “reflection” and “inter-task knowledge transfer” where the former intends to balance exploitation and exploration and the latter intends to exploit existing robot design datasets whilst leveraging LLMs ability for inter-task reasoning.

### Strengths
Originality

This paper demonstrates originality by identifying the need for and explicitly developing a mechanism aimed at solving lack of diversity in LLM-aided robot design processes. The idea of using existing robot design datasets and inter-task reasoning to transfer or modify it also adds originality to this work. 

Quality

The authors clearly set out their intended contributions and state their scientific hypotheses as well as the experiments they intend to test these hypotheses. The figures throughout the paper are high quality and aesthetically pleasant. The authors do a good job of covering a fairly broad portion of the related literature and providing motivations for their own work. 

Clarity

The paper is well-written and easy to follow. The methods and results figures are easy to interpret. The main method figure is done particularly well and makes it easy to understand the relatively involved, multi-step process that is the proposed algorithm. The tables throughout the paper are also well-labeled without superfluous text. 

Significance

Joint design and control of robotic systems is an important problem and provides a canonical example of a combinatorially explosive design space automated methods aspire to solve. The lack of diversity or tendency towards local optima in the morphological design process is a known limitation of evolutionary robotics broadly, so research and development in this area is crucial to advance the field.

### Weaknesses
Small design space

A 5x5, two dimensional design space makes it difficult to discover interesting structures or behaviors, rendering the implications for design (let alone robotics) somewhat unclear. The search space is much smaller than most work over the past three decades, which has been in 2D but at much higher resolution with hundreds of independent motors (https://www.roboticsproceedings.org/rss20/p100.html) or in 3D with hundreds or thousands of voxels (https://www.creativemachineslab.com/soft-robot-evolution.html). The paper would be much more compelling if LLMs were operating over a 3D space where variety in gait patterns more readily appear and the control complexity increases substantially.

Weak notions of diversity and lacking examples

The paper proposes the measure diversity in terms of the voxel space edit distance of robots and the number of distinct, high-performing robots. The latter is likely a poor measure of diversity as two robots can be highly similar while remaining distinct in terms of the precise voxel layout, and the former is difficult to interpret. Moreover, the paper provides no examples of the morphologies (and diversity) discovered by their algorithm. The overall diversity measure is the weighted average of these two metrics with weights of 1.0 and 0.1. There is no rationale for the selection of these weights outside of an anecdote that weighting the latter by 0.1 makes the two “roughly on the same scale and given equal importance”. The use of an arbitrary weighting coefficient further complicates the interpretation of the diversity metric. It would be more informative to report the edit distance, the number of distinct high performers, and the weighted average separately, allowing for a more nuanced comparison between methods. Demonstrating that LASeR outperforms on all three metrics would be more convincing, and where LASeR underperforms there may be insight into the limitations of the existing metrics.

Diversity reflection incomplete ablation

Following up on the above point, the paper reports an ablation study to test the effectiveness of their diversity reflection mechanism; however, the ablation does not elucidate whether the LLM is actually providing intelligent mutations that encourage diversity. An additional ablation study should be run wherein random mutations are made to existing designs (in parallel to LLM guided mutations). This would help demonstrate whether the diversity reflection mechanism represents an intelligent operator. The current ablation study lacks sufficient detail regarding the implementation of random voxel editing, including the number of voxels edited and how it compares to the LLM operator. Furthermore, it is unclear how Figure 13 demonstrates the superiority of the LLM operator over random mutations, especially given the negligible performance differences and the use of a single trial with potentially large differences in initialization. The fact that the performance of the random editing approach appears to improve over evolutionary time, despite the claim that random edits make designs worse, is also confusing and requires further clarification.

Early convergence

Also related to diversity, the proposed algorithm appears to converge very early relative to some other baselines in most cases. This appears to be an indication that the algorithm may be stuck in a local optima, or is it closer to a global optima? If allowed to run for longer would the other methods arrive at a similarly high performing result? If it is indeed discovering something that is close to globally optimal then the fast convergence should indicate that this task (read design space) is too easy. It also appears that when using the diversity reflection component the algorithm converges faster, which seems somewhat counter-intuitive as one would expect greater exploration to produce longer convergence times. The fact that it does not leads back to a prior question as to whether the LLM is truly modifying the design in intelligent ways that ultimately produce meaningful diversity in the population.

Marginal gains in performance

When all is said and done the proposed method produces marginal gains in performance relative to baselines. In the ablation study with and without diversity reflection performance also does not change substantially whereas the diversity does improve significantly. The diversity metric itself remains questionable (see above). The knowledge transfer mechanism also does not appear to itself demonstrate meaningful improvements relative to the LASeR without knowledge transfer.

Reproducibility

The paper states that all experiments are conducted three times and the results are averaged. Since the performance gains are relatively small, additional trials are necessary to demonstrate statistical significance of the results. The provided confidence intervals are also insufficient, and should be replaced with 95%+ confidence intervals, along with a statistical test and p-value.

Missing related work

This paper fails to discuss, compare and contrast their work with other similar methods that use LLMs to design robots, for example: https://link.springer.com/chapter/10.1007/978-981-99-3814-8_11

Choices about the control policy and its training also bears at the very least some discussion and comparison to other evolutionary robotics approaches that employ other methods, such as gradient based optimization (https://www.roboticsproceedings.org/rss20/p100.html), for the control problem.

The robot design problem reads as an afterthought and this field of work and its rich history are glossed over, pushed to the very end of the paper and the appendix.

Why is robot design important?

Why should we care about this problem?

You call your agents "robots" but failed to explain how they can transfer from 2D simulation to reality? Has this been done before? How?

Are there any implications of this work for the future of real robots?

### Questions
1. How do you justify the proposed measures of diversity and the weighted averaging used? Can you provide other measures? For example, the proportion of bodies made up of different voxel types? 

2. Can you provide concrete examples of morphologies that emerged using your method compared with others? Is the diversity in these collections immediately observable just by looking at the bodies? 

3. Can you run these experiments again several times over to provide more meaningful performance measures, confidence intervals and statistical hypothesis testing? 

4. How do you explain the early convergence of your method when a primary claim relates to encouraging population level diversity and design exploration? 

5. Can you perform additional ablation studies of the diversity reflection aspect? For example, randomly edit voxels and compare results to LLM-based editing? Can you catalog examples of LLM edits that encourage diversity through an evolutionary lineage? 

6. Can you run experiments with a larger design space? Perhaps 9x9?

### Soundness
3

### Presentation
3

### Contribution
2

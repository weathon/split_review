# Efficient Active Imitation Learning with Random Network Distillation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Developing agents for complex and underspecified tasks, where no clear objective exists, remains challenging but offers many opportunities. This is especially true in video games, where simulated players (bots) need to play realistically, and there is no clear reward to evaluate them. While imitation learning has shown promise in such domains, these methods often fail when agents encounter out-of-distribution scenarios during deployment. Expanding the training dataset is a common solution, but it becomes impractical or costly when relying on human demonstrations. This article addresses active imitation learning, aiming to trigger expert intervention only when necessary, reducing the need for constant expert input along training. We introduce Random Network Distillation DAgger (RND-DAgger), a new active imitation learning method that limits expert querying by using a learned state-based out-of-distribution measure to trigger interventions. This approach avoids frequent expert-agent action comparisons, thus making the expert intervene only when it is useful. We evaluate RND-DAgger against traditional imitation learning and other active approaches in 3D video games (racing and third-person navigation) and in a robotic locomotion task and show that RND-DAgger surpasses previous methods by reducing expert queries. \small{\url{https://sites.google

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a method to more effectively integrate human feedback with imitation learning and specifically the IL method dagger. The idea is to only request human feedback when the policy is out of distribution. The data collected by the expert is then added to a buffer for training. In doing so, the algorithm is able to more effectively utilize the experts time and feedback.

### Strengths
The research problem this work focuses on is good. Increasing the efficiency of imitation learning is an open problem and the most effective way to utilize expert data within IL. Improving the interaction between expert and policy increases the ability of IL to be used with real world problems.

The contribution of this work is ok, they propose their method and perform a study to verify their claims.

The algorithm is clearly defined and could be implemented from the information given.

The experiments run are reasonable and seem to demonstrate their method well.

The baseline comparison are all dagger variants (and BC). They are definitely reasonable comparisons.

The empirical results are good. They show a balance between expert interventions and performance which is the goal of this work.

The clarity is great. This paper was very easy to read and very clear.

### Weaknesses
The novelty of this work is minimal. As far as I understand it the methods generally used in this work are all previously known. Dagger and the OOD classifier seem to be like the main components used but are previous work.

The statistical rigor needs improvement. The metrics are only averaged over 8 seeds. Is there a reason for only this many? I feel like it should be many more.

As well, I want to see confidence intervals on Table 1.

There is no failure analysis. I wish there was one on the times the method does not perform better than the previous methods. What about those tasks makes it not as good? 

The future work and conclusion is ok. I wish there was a better future work section. I think a limitation of this work is that it works well in simulated environments but on an actual self-driving car how would this work? The car couldn’t just stop running. This could be an interesting direction of future work some like predicting beforehand that you’re going to get an out of distribution state and request input.

### Questions
I wonder are there other comparisons here? Do they all have to be dagger variants? Is there another type of “expert takeover” method that you could compare to? If I missed this in the text I apologize.

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
4

### Summary
This paper presents Random Network Distillation DAgger (RND-DAgger), an active imitation learning method that leverages RND to define an out-of-distribution states, enabling selective expert intervention and minimize the frequency of transitions between human experts and learning agent through a minimal demonstration time mechanism. The approach is evaluated across Race Car, Maze, and Half Cheetah environments.

### Strengths
- The paper presents a well-founded motivation, aiming to optimize the timing of expert interventions to reduce overall costs associated with human expertise and minimize the frequency of transitions between human experts and learning agent.
- The paper is straightforward, particularly for readers with a background in the domain of unsupervised RL.

### Weaknesses
 - **Novelty:** The paper's novelty appears constrained, as it predominantly builds upon an established novelty measure within the unsupervised RL domain. This integration approach mirrors Ensemble-Dagger, which relies on a principle similar to Disagreement in the unsupervised RL domain.

- **Limitations:** The limitations specific to this method are not sufficiently addressed. Certain limitations noted by the authors for other approaches may also apply here. For instance, the paper states, “While this approach works well when the expert is optimal and acts deterministically, it becomes problematic when dealing with humans or imperfect experts.” It is unclear how this method manages these challenges, and if not addressed, this issue should be explicitly acknowledged. Specifically, the method's reliance on state discrepancy for triggering expert interventions, while potentially robust in some scenarios, may not be universally effective. The paper lacks a discussion on scenarios where state discrepancies might not accurately reflect the need for expert intervention, such as when the agent is in a novel but safe state, or when minor state deviations are inconsequential.

- **Baselines:** The study lacks comparisons with more recent methods that similarly leverage human input for out-of-distribution states, such as RLIF [1], PATO [2], and Sirius [3]. The absence of these comparisons makes it difficult to assess the relative performance and advantages of the proposed method.

- **Time Mechanism:** This approach is reliant on two factors: RND and Minimal Expert Time. It would be valuable to assess how Minimal Expert Time operates alongside other baseline methods - a potentially straightforward inclusion. This would provide a clearer understanding of RND’s advantages over alternative metrics. For example, it is not clear if the performance gains are solely due to the RND novelty measure or if the Minimal Expert Time mechanism contributes significantly, and how this interaction compares with other methods.

- **Experiments:** Additional experiments are needed to support the authors' claims regarding task performance and context switching. From the current results (Table 1), Ensemble-Dagger performs better in RC settings but with higher context switches, whereas Lazy Dagger shows the opposite trend in HC settings. Further experiments in more challenging environments, such as Adroit [4], would provide deeper insights and strenghten the paper’s claims. Moreover, incorporating the Time Mechanism into other methods may enhance their context-switching capabilities, offering a compelling comparison. The current experimental setup does not fully explore the method's robustness across diverse task complexities and agent behaviors. The results in Table 1, for example, show that the proposed method does not consistently outperform baselines across all environments, raising questions about its general applicability.

- **Ablation Study:** The ablation study section would benefit from greater detail, as the current presentation makes it challenging to interpret the impact of various factors on learning outcomes. Specifically, the paper should provide a more granular analysis of how different components of the method, such as the RND module and the Minimal Expert Time mechanism, contribute to the overall performance.

### Questions
They are mentioned in Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper focuses on addressing the covariate-shift problem in behavioural cloning, where the agent suffers from compounding error from the predicted actions. The paper considers DAgger-like algorithms where the process includes querying an expert to add extra demonstrations, thereby increasing state-action coverage. The paper identifies a gap where existing approaches require the said expert to be present for a long period of time, which can be costly for some applications. The paper thus propose a method that considers out-of-distribution in states through random network distillation. The paper conducts experiments on three simulated environments, demonstrating that the proposed algorithm achieves similar performance as existing DAgger-like baselines, as well as the reduced number of expert queries.

### Strengths
- The idea is very simple and focuses on a gap that previous approaches do not consider (i.e. OOD states rather than action mismatch).
- The algorithm appears to be practical compared to existing approaches.

### Weaknesses
I am happy to increase the scores if these comments are addressed.

**Comments**
- I am unsure why the formulation is POMDP rather than MDP. The environments used in this paper appears to be using state-based information, in the sense that I cannot really guarantee that they are partially-observable, as opposed to using images that will be way more convincing.
	- I further believe that the current method assumes the observation aliasing is not a problem. Self-driving environment can dramatically different scene while similar actions.
	- I suggest including the CARLA environment to make this result more convincing.
- Regarding the approach, experimentally how is this algorithm different from the earlier variants since $f_{targ}$ can be $\pi_{exp}$? In other words, is LazyDAgger essentially doing RND but have a slightly higher-dimensional output space? If that is the case, then is the benefit coming from the additional "minimal demonstration time" mechanism?
- The paper can improve upon its writing quality:
	- Algorithms 3 and 4: Include the actual definition of *measure* for clarity.
	- Table 1: What do bolded and underlined terms mean? Is this taking the average or some other statistics? What about the standard error or other statistics?
	- Figure 6: What do the solid line and shaded area correspond to?
		- Also recommend the top curve to use different line style to differentiate variants easier.


### Questions
- Experiments:
	- In Figure 6, do the algorithms use same initial datasets? Does increasing in x-axis mean starting at a larger dataset? Or this corresponds to increasing size due to the conditions to query from the expert?
	- How do Figure 6e and 6f demonstrate that RND-DAgger is better in "sample-efficiency"? Context switching does not totally correspond to number of samples queries from the expert. Can the paper clarify this point?
	- On page 9, there is a claim "..., RND-DAgger is more effective at leveraging expert feedback to improve the policy." How is this statement true exactly? The policy training at the end is the same but I suppose the aggregated data is somewhat different?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors address efficient expert intervention in active imitation learning for complex, reward-free tasks like video game bots and robotic control. The proposed RND-DAgger framework uses a state-based out-of-distribution (OOD) measure to trigger expert input selectively, reducing intervention needs by focusing on critical states. Experiments in RaceCar, 3D Maze, and HalfCheetah environments demonstrate that RND-DAgger outperforms traditional methods, achieving high performance with fewer expert queries. Ablation studies highlight the importance of the stability window and historical context in reducing context switches and expert burden.

### Strengths
1. **Motivation and Intuition**: The motivation for reducing expert intervention in active imitation learning is convincing, particularly in applications where continuous expert availability is costly or impractical.

2. **Novelty**: The paper introduces the idea of leveraging Random Network Distillation (RND) to manage expert interventions, which is innovative and well-suited for identifying critical OOD states.

3. **Clarity**: The paper is well-organized, with clear explanations of both theoretical foundations and implementation details. Figure 4 effectively illustrates the RND-DAgger algorithm, and ablation studies clarify the effect of each component.

4. **Experimental Results**: The visualizations of experimental results are clear. Figure 6, for instance, provides an accessible overview of task performance and the frequency of context switches across environments, highlighting RND-DAgger’s reduced reliance on expert intervention.

5. **Reproducibility**: The author's inclusion of pseudo-code, a detailed description of the experimental setup, and an appendix for hyperparameters strengthens reproducibility. They promise to release code upon acceptance also supports this.

### Weaknesses
1. **Experiment Setup**: The environments in the main experiment, although tested on four different setups, lack sufficient diversity, limiting the evaluation of RND-DAgger’s performance across a broader set of tasks. Incorporating additional environments, such as robot manipulation or hand dexterity tasks, would enrich the setup and test the method’s adaptability in more complex, fine-grained control scenarios. The current environments, while varied in some aspects, do not fully explore the challenges of high-dimensional state spaces and intricate action dependencies that are common in real-world robotics. For example, the RaceCar environment, while dynamic, primarily involves navigation, and the HalfCheetah, while complex in its dynamics, is relatively low-dimensional compared to a multi-jointed robotic arm. A more diverse set of environments would include tasks with contact-rich interactions, object manipulation, and tasks requiring precise control of multiple degrees of freedom, which would provide a more rigorous assessment of the proposed method's robustness.

2. **Related work**: The paper needs to include comparisons to the methods that specifically designed to handle out-of-distribution scenarios, aiming to generalize to states unobserved during training without requiring expert intervention [1, 2]. Specifically, the paper should discuss how RND-DAgger compares to methods that use generative models to augment the training data with synthetic out-of-distribution states, or methods that learn an implicit representation of the state space to enable better generalization. The current discussion of related work does not adequately address the existing literature on handling OOD states in imitation learning, which is a critical aspect of the proposed method.

### Questions
1. The paper lacks necessary comparisons with methods specifically designed to address out-of-distribution scenarios, aiming to generalize to states unobserved during training without requiring expert intervention [1, 2]. Including these comparisons is essential to demonstrate the completeness of the proposed method in handling such challenges and I am willing to raise the scores.

2. While the paper presents results from four environments, the setup may lack sufficient diversity to fully assess RND-DAgger’s adaptability. Would the authors consider evaluating on additional environments, such as robot manipulation or hand dexterity tasks, which could reveal the method’s robustness and effectiveness across a broader range of complex control scenarios?

3. In which types of tasks or environments does RND-DAgger face challenges, especially with regard to state-based out-of-distribution detection?

4. How does the RND mechanism manage computational efficiency, and is it feasible to optimize it further for large-scale applications?

5. What role does the "minimal demonstration time" play in balancing expert workload and agent training quality, especially in complex environments?

[1]  Shang-Fu Chen, Hsiang-Chun Wang, Ming-Hao Hsu, Chun-Mao Lai, and Shao-Hua Sun. Diffusion model-augmented behavioral cloning. In International Conference on Machine Learning, 2024.

[2] Pete Florence, Corey Lynch, Andy Zeng, Oscar A Ramirez, Ayzaan Wahid, Laura Downs, Adrian Wong, Johnny Lee, Igor Mordatch, and Jonathan Tompson. Implicit behavioral cloning. In Conference on Robotic Learning, 2022.

### Soundness
2

### Presentation
3

### Contribution
3

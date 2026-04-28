# On Evaluation of Generative Robotic Simulations

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 8, 3, 5

## Abstract
Due to the difficulty of acquiring extensive real-world data, robot simulation has become crucial for parallel training and sim-to-real transfer, highlighting the importance of scalable simulated robotic tasks. 
Foundation models have demonstrated impressive capacities in autonomously generating feasible robotic tasks. However, this new paradigm underscores the challenge of adequately evaluating these autonomously generated tasks. 
To address this, we propose a comprehensive evaluation framework tailored to generative simulations. 
Our framework segments evaluation into three core aspects: \textbf{\textit{quality}}, \textbf{\textit{diversity}}, and \textbf{\textit{generalization}}.
For single-task quality, we evaluate the realism of the generated task and the completeness of the generated trajectories using large language models and vision-language models. In terms of diversity, we measure both task and data diversity through text similarity of task descriptions and world model loss trained on collected task trajectories. For task-level generalization, we assess the zero-shot generalization ability on unseen tasks of a policy trained with multiple generated tasks.
Experiments conducted on three representative task generation pipelines demonstrate that the results from our framework are highly consistent with human evaluations, confirming the feasibility and validity of our approach. 
The findings reveal that while metrics of quality and diversity can be achieved through certain methods, no single approach excels across all metrics, suggesting a need for greater focus on balancing these different metrics. Additionally, our analysis further highlights the common challenge of low generalization capability faced by current works.
Our anonymous website: \url{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a framework to analyze existing simulation benchmarks for embodied AI. The authors consider 3 metrics: quality, diversity, and generalization. For quality, authors analyze the realism of the generated task and the completeness of the generated trajectories. For diversity, they measure instruction diversity and trajectory diversity. For generalization, they train a diffusion policy and check success rate on unseen tasks. The results reveal that while metrics of quality and diversity can be achieved through certain methods, no single approach excels across all metrics.

### Strengths
1. The authors proposes 3 aspects (quality, diversity, and generalization) to assess current simulation benchmarks.
2. Experiments and analysis are interesting.

### Weaknesses
1. I think in addition to quality, diversity, and generalization, sim-to-real gap is a big issue that needs to be addressed/discussed when analyzing simulation benchmark. Have you considered metrics to assess how well the simulated tasks translate to real-world scenarios? Or maybe include a section on potential sim-to-real challenges for each evaluated benchmark.
2. It seems the diversity score only considers the text and trajectory. However, I think it should also consider at least visual input.
3. It seems this paper did a great job of analysis of existing benchmarks, but did not propose a new benchmark to resolve these issues.
4. It seems generalization and diversity has some connection. The diversity is to measure how out-of-distribution tasks are from each other while generalization is to measure how in-distribution tasks are with each other. I wonder whether we can use the same metric to measure these 2 things. Is it possible to investigate correlation between diversity and generalization scores? Or is it possible to potentially unify these two metrics?

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents an evaluation framework for "generative" robot simulators. Here, generative simulations are a simulator, task set, and possibly set of demonstrations for each task. The authors propose evaluating these simulations in three criteria: quality, diversity, and generalization. Task quality is evaluated by scene alignment between the task description and the scene, and also scoring the task completion video with an mLLM to see whether the associated data or policy completes the task. For task diversity, the authors evaluate the description embedding, and also a trajectory prediction error to understand the data/trajectory diversity. Finally, for generalization, the authors train policy on the training data and evaluate – seeing how well the performance is on evaluation set.

### Strengths
1. This paper is pretty timely and addresses an important recent development in simulation based robotics – generative simulations. While there are multiple such works coming out in recent months, there is no easy way to understand which one someone should use for their applications. A quantitative evaluation like the one proposed in the paper goes a long way to address this concern.

2. The three axes proposed by the authors are also reasonable – and the way to evaluate them also seems reasonable. Splitting the three criteria into the smaller sub-criteria is also pretty pertinent. 

3. The fact that the authors also do human evaluations to find alighment between the mLLM evaluations and human evaluations make their evaluation more trustworthy.

4. The task diversity evaluations are also interesting – although maybe less meaningful than the other axes since the type of tasks i.e the task class proposed by each simulator may vary a lot.

5. Finally, the authors expose interesting issues with the generalization ability in RoboGen and BBSEA – that the data generated by them is not high quality, and thus they need to improve their data quality before they can be useful.

### Weaknesses
1. There doesn't seem to be a consistent correlation with human evaluation and mLLM proposed results in Figure 3.
2. The alignment score given by the mLLMs is not calibrated – some calibration would make the results more reasonable.
3. Generalization evaluation would be more convincing if it was trained on some kind of task-conditioned multi-task policy like BAKU [1] rather than an unconditional policy like diffusion policy.

### Questions
1. Do the authors think the task diversity captures the overall size of the possible task sets in a generative simulation?
2. Would the authors be open sourcing their evaluation suite so developers of generative simulations can develop with this benchmark in mind?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an evaluation framework for simulations generated by the generative foundational model, focusing on three key metrics: (i) the realism of tasks and generated trajectories, (ii) task diversity, and (iii) generalization to new tasks. This framework indicates a correlation between expert human evaluations.

### Strengths
- This paper seeks to tackle significant challenges in robotics, especially the high costs associated with evaluating generative simulations. The proposed framework leverages the capabilities of LLMs/VLMs to automate this process.
- Certain VLM/LLM choices demonstrate a correlation with human expert evaluations of task quality, suggesting the potential effectiveness of these methods. However, some VLM/LLM show less alignment with human assessments.

### Weaknesses
 - **Clarification on Experiment Design**
  + Below are some points for clarifying the experiment setup:
  + Could the authors explain why the three selected metrics are considered essential for generative simulation? While single-task quality and task diversity are understandable, it's unclear how generalization fits within this context. How does it differ from simply having diverse tasks? The paper does not clearly define what constitutes 'generalization' in the context of generative simulation, making it difficult to assess its necessity as a distinct metric.
  + Could the authors clarify how scene alignment is evaluated? From my understanding of lines 348-350, it seems to rely on the robot's trajectory. If that’s the case, shouldn’t the quality of the generated trajectory also play a role? Additionally, I’m curious why scene alignment is based on video rather than image. The use of video for scene alignment is not well-justified, especially given that trajectory quality is not explicitly factored into the alignment score. This raises concerns about the robustness of the metric.
  + The connection between high prediction loss and task diversity is unclear. For instance, a single task could involve varied dynamics, like table rearrangement. Could the authors provide a justification for this? The paper's claim that high prediction loss directly indicates higher trajectory and visual diversity is not sufficiently supported. The prediction loss could be influenced by factors other than diversity, such as the inherent complexity of the task or the limitations of the world model itself. The paper needs to provide a more rigorous justification for this metric.

- **Fairness of Evaluation**
  + Each baseline uses a different task for evaluation, but certain tasks or simulator setups (as mentioned in lines 318-319) might inherently pose challenges for LLM/VLM-based score evaluation, potentially affecting fair comparison. The lack of a standardized task set across different baselines makes it difficult to ensure a fair comparison. The paper should address how the inherent biases of different tasks might influence the evaluation results.

### Questions
- How do humans evaluate the task? (e.g., Do they use a 1-5 scoring system, rank tasks by preference, or something else?)
- Related to the point above (in the Weaknesses section, high prediction loss), lines 274-277 weren’t clear about the exploration aspect. Could the authors clarify how diverse dynamics are connected to task diversity?

### Minor Suggestions
- Section 3.3 on Scene Alignment Score could reference prompt (A.1).
- Section 4.1.1 could refer to the detailed experiment setup in (A.2).

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the problem of evaluating autonomously generated tasks by VLM in simulation. The authors propose an evaluation strategy focusing on three aspects: the quality of individual generated tasks, the diversity of multiple generated tasks, and the generalization ability of a diffusion policy trained on the generated tasks. The approach is applied to tasks generated by RoboGen, GenSim, and BBSEA, and the evaluation scores are compared with human evaluation scores.

### Strengths
* The paper tackles an important and under-explored problem: evaluating the quality of generated tasks in a systematic way.  
* The criteria used for evaluation—task quality, task diversity, and generalization ability—are all crucial for assessing whether a generated task set is useful.

### Weaknesses
* **Clarity of contribution**: The contribution is not entirely clear. Is this the first evaluation strategy for task sets? If not, how does it compare to existing evaluation methods, such as Self-BLEU or Embedding similarity scores from RoboGen? More clarification is needed on how this approach improves upon or differs from existing evaluation techniques. Specifically, the paper should elaborate on whether the proposed metrics are indeed sufficient to measure the three aspects (task quality, diversity, and generalization). Furthermore, it should discuss whether these three aspects are comprehensive enough to evaluate the generated simulation platform. Are there any other factors not considered, such as the potential of transferring a policy learned on the generated environment to the real world or whether the difficulty distribution of generated tasks is proper for policy learning? 
* **Realism of generated tasks**: The claim regarding "evaluating the realism of generated tasks" seems overreaching. The approach measures scene alignment score, which reflects consistency between task descriptions and scene images. However, it's not clear why this metric necessarily reflects the "realism" of the generated tasks. A more thorough justification or evidence supporting this claim would strengthen the paper. For instance, what specific criteria are used to determine if a scene is realistic? How does the scene alignment score correlate with these criteria?  
* **Human evaluation details**: The paper lacks specifics on the human evaluation process. Human evaluations were conducted on 10 generated tasks, but key details are missing. How many human evaluators were involved? Were they experts in robotic tasks or general participants? What guidelines were provided to ensure consistency in ratings, particularly for scene alignment and task completion scores? Without this information, it is difficult to assess the reliability and validity of the human evaluation data.
* **Writing and presentation**: The paper could benefit from improved clarity in writing, particularly in explaining key concepts and the methodology used. For example, the definitions of "task quality," "task diversity," and "generalization ability" could be made more precise. Additionally, the methodology section could be expanded to provide more detail on how the evaluation metrics are calculated.

### Questions
1. **Pearson correlation in Figure 3**: Figure 3 shows Pearson correlation between evaluation methods and human evaluations. However, it does not quantify how much the proposed evaluation method deviates from human evaluation. Why are the scores in Figure 3 (left) generally better than those in Figure 4 (right)? Does this imply that the proposed method is more reliable for scene alignment scoring than for task completion scoring?  
2. **Figure 4 method clarification**: The paper mentions various LLM/VLM options in Section 4.1.1, but it’s unclear which one is used in Section 4.1.2 Figure 4\. Do all VLM/LLM choices yield similar results, or do specific models shows the result trend in Figure 4? For example, does RoboGen consistently outperform in task completion scores while GenSim excels in scene alignment, regardless the choice of evaluation VLM/LLM?  
3. **Line 354 clarification**: The paper attributes the shortfall in performance to the vision-language model’s “lack of access to top-view rendered data”. Is this limitation specific to the VLM used in GenSim or to the VLM used in the proposed evaluation method?  
4. **Task set generalization (Section 4.3)**: In this section, different task groups are used to measure the generalization ability (as shown in the Appendix Table 6). Given that the task groups are not identical across task sets, is it fair to conclude that GenSim exhibits better generalization while the others perform poorly? How does this variability in the definition of task groups affect the generalization conclusions?  
5. **Definition of text embedding (Line 264\)**: What is the formal definition of the text embedding e\_i​ used for task descriptions? More clarity here would help.  
6. **Image sampling (Line 246\)**: The paper mentions extracting 8 images from the trajectory video. Are these images randomly sampled, or are they evenly spaced throughout the trajectory? Does the selection method include the final frame? Could different sampling strategies affect the task completion score?

### Soundness
2

### Presentation
2

### Contribution
2

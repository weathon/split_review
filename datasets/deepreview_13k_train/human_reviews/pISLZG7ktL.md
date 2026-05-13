# Data Scaling Laws in Imitation Learning for Robotic Manipulation

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Data scaling has revolutionized fields like natural language processing and computer vision, providing models with remarkable generalization capabilities. In this paper, we investigate whether similar data scaling laws exist in robotics, particularly in robotic manipulation, and whether appropriate data scaling can yield single-task robot policies that can be deployed zero-shot for any object within the same category in any environment. To this end, we conduct a comprehensive empirical study on data scaling in imitation learning. By collecting data across numerous environments and objects, we study how a policy’s generalization performance changes with the number of training environments, objects, and demonstrations. Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol. Our findings reveal several intriguing results: the generalization performance of the policy follows a roughly \textit{power-law} relationship with the number of environments and objects. The \textit{diversity} of environments and objects is far more important than the absolute number of demonstrations; once the number of demonstrations per environment or object reaches a certain threshold, additional demonstrations have minimal effect. Based on these insights, we propose an efficient data collection strategy. With four data collectors working for one afternoon, we collect sufficient data to enable the policies for two tasks to achieve approximately 90\% success rates in novel environments with unseen objects.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors in this work construct zero-shot generalizable policies with imitation learning and propose some scaling rules that determines the performance of such policies with the amount of data that is used to train such policies. Using such predicted scaling laws, the authors then collect training data for two new tasks, and show that the laws hold for such tasks as well.

### Strengths
The authors present a compelling paper with a hypothesis that until very recently were not widely known in the field of robot learning. To summarize the strengths of the paper:

1. The focus of this paper, behavior cloning models that generalize to new objects and environments zero shot, has only very recently been shown to work, so analyzing the underlying principles that determine the success of this process is very important.
2. The authors approach this problem in a principled way, collecting a lot of data, training a number of models, and evaluating on those model in the real world over different environments is a hard but important problem.
3. The scaling law proposed by the authors seem to hold up in further examinations with two different tasks trained post-facto.
4. The visual presentation of the objects and scenes where data is collected is done wonderfully.
5. The extra tips in the appendix for practitioners for training more general policies seem to be also very helpful for further research in this direction.

### Weaknesses
While the paper is advancing robot learning in a positive directions, there are possible improvements that can be made. For example:

1. The primary issue with the paper is that it does not mention the initial conditions for the robot and the environment – and how they were varied. For example for the pouring task, it is unclear whether the cup and the red dot is located at the same relative position to the bottle, and if so, if it's sufficient for the robot to open-loop follow a training trajectory afterwards to complete the task. To understand what the authors mean by "90% success", we must have a good sense of what the task and environment variations look like. Specifically, the paper lacks details on the distribution of initial object poses, and whether the robot's starting configuration is consistent across trials. Without this information, it's difficult to assess the true generalization capability of the learned policies. For instance, if the bottle and mug are always in a similar relative position during training, the policy might be learning a simple open-loop trajectory rather than a robust pouring strategy.

2. Similarly, the authors don't create much of a variation in the task difficulty – as a result it is hard to tell if the scaling laws derived in the paper scales in a similar way with harder or easier tasks. The paper does not explore how the scaling laws might change with tasks that require more complex manipulation or longer planning horizons. For example, a task that involves navigating around obstacles or requires precise alignment of objects might exhibit different scaling behavior. The lack of task difficulty variation limits the generalizability of the findings.

3. The "new tasks" that the authors collect data for and evaluate in (towel folding, unplug charger) does not seem to be of a similar level of difficulty as the primary tasks talked about in the paper. The new tasks appear to be significantly simpler than the pouring and mouse arrangement tasks, which makes it difficult to validate the scaling laws across a diverse range of task complexities. For example, towel folding and unplugging a charger are relatively short-horizon tasks that might not require the same level of generalization as the pouring task.

### Questions
1. Why do we see the normalized score drop at the very end as the number of demonstrations are scaled?
2. What level of variation is done in the evaluation environment setup over multiple runs in the same environment on the same object?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the correlation between the size of the dataset and the task performance in behavioral cloning with Diffusion Policy. The authors mainly investigate two manipulation tasks and vary the object to be manipulated and the environment. A key finding of the paper is a power scaling law between the number of training objects / environments and the task performance. Furthermore, the authors highlight that collecting more than 50 demonstrations per environment-object combination does not further increase the performance.

### Strengths
The paper is well written and easy to follow. The experiments are clear and the results are presented well. Insights into which data is most useful and how many demonstrations are required to solve a task are certainly very helpful. I particularly like that all experiments are executed on a real robot arm in reasonably cluttered environments.

### Weaknesses
The analysis focuses mainly on two relatively simple tasks (pouring water and rearranging a computer mouse). While the paper would benefit from investigating more tasks and also including more challenging tasks, I am aware that it is quite an effort to set up additional experiments with real robots and collect large training sets.

The objects considered in the tasks are always objects of the same category (e.g., water bottles) and, thus, very similar. I believe that this is the reason why increasing the number of objects per environment in Figure 6 does not improve the task performance much. Essentially, the objects are always quite similar, while the environments differ quite significantly, and therefore, it is more important to collect data from more environments rather than with different objects in the same environment.

In Figure 6, sometimes increasing the number of objects per environment decreases the task performance quite considerably (e.g., right plot M=4). This seems quite counterintuitive. What could be the reason for this?

What is exactly is the correlation coefficient r (e.g., line 380)?

There are no standard deviations in the plots. Consider adding the standard deviations to make it easier to assess the empirical significance of the results.

Caption 7: "In the setting where we collect the maximum number of demonstrations, we examine whether the policy's performance follows a power-law relationship with the total number of demonstrations." I believe the first "demonstrations" should be something like "environment-object combinations".

Line 47/48: "[W]e aim to investigate the following fundamental question: Can appropriate data scaling produce robot policies capable of operating on nearly any object, in any environment". In my opinion the statement that the paper investigates this fundamental problem is a bit too strong since the policies learn to manipulate only objects of the same category (e.g., water bottles) in environments with similar characteristics (tabletop environments), so these policies are quite far from handling any object in any environment.

### Questions
1. In Figure 6, sometimes increasing the number of objects per environment decreases the task performance quite considerably (e.g., right plot M=4). This seems quite counterintuitive. What could be the reason for this?

2. What is exactly is the correlation coefficient r (e.g., line 380)?

3. There are no standard deviations in the plots. Consider adding the standard deviations to make it easier to assess the empirical significance of the results.

4. Caption 7: "In the setting where we collect the maximum number of demonstrations, we examine whether the policy's performance follows a power-law relationship with the total number of demonstrations." I believe the first "demonstrations" should be something like "environment-object combinations".

5. Line 47/48: "[W]e aim to investigate the following fundamental question: Can appropriate data scaling produce robot policies capable of operating on nearly any object, in any environment". In my opinion the statement that the paper investigates this fundamental problem is a bit too strong since the policies learn to manipulate only objects of the same category (e.g., water bottles) in environments with similar characteristics (tabletop environments), so these policies are quite far from handling any object in any environment.

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
This paper presents a comprehensive analysis of the robot's generalization ability to novel objects and environments related to data scaling. This identifies two main findings: (i) generalization generally follows an approximate power-law with respect to the number of of environments and objects, and (ii) increasing the diversity of objects and environments enhances performance more effectively than merely gathering more data in limited setups.

### Strengths
- This study is follows a rigorous protocol to examine scaling laws across diverse environments and objects, with a fair evaluation method to minimize evaluation bias.
- The paper presents efficient data collection strategies, which are crucial for the robot learning field, where data collection is costly and limited.
- This work plans to open-source the code, data, and model, which can be useful for future research on robot learning generalization.

### Weaknesses
 - **Details on data**
  + Considering the multiple other factors that can affect learning performance, the authors should provide data details for each environment, object, and environment-object variation. This could include specifying the number of demonstrators [1] (with their IDs), listing the data collection protocol [2], and showing relevant statistics (e.g., the number of failed demos, action variance [3], and task horizon for each demonstrator [3]). Such information would clarify that any observed variation is due solely to the environment, object, or environment-object pair rather than bias in the data itself. Specifically, the lack of information regarding the distribution of demonstrations across different demonstrators and the consistency of their performance makes it difficult to ascertain whether the observed scaling laws are genuine or are influenced by variations in demonstrator skill or behavior. For instance, if one demonstrator consistently provides higher-quality demonstrations (e.g., smoother trajectories, fewer errors), the results could be skewed. Furthermore, the absence of details on the number of failed demonstrations is concerning, as it could indicate that some environment-object pairs are inherently more challenging, which could affect the overall learning performance and the interpretation of the scaling laws. The action variance is also critical to understand the diversity of the collected data. High variance could indicate less consistent demonstrations, while low variance might suggest a lack of exploration of the action space.
  + One concern about particular data collection hardware (i.e., UMI) is that it may introduce added bias. For instance, if a specific teleoperator is highly skilled, they might gather higher-quality data by using optimal speed movements or demonstrating behaviors at the precise height where the robot is positioned. The authors could clarify this in relation to the above point.
- **Limited algorithmic variations**
  + The experiments use only a single algorithm with a single seed, which may restrict to make a comprehensive conclusion.

### Questions
- Figure 5 seems to lack an explanation of how to obtain $\alpha$ and $\beta$.
- Does each item in the heatmap in Figure 6 represent the same number of demonstrations? The relevant context was difficult to locate in the paper.
- Including an in-domain evaluation would help readers better understand the performance gap between zero-shot evaluation and in-domain data.
- Supplementary suggestion: It would be interesting to explore if the scaling law applies to environments/objects generated by the generative model [1]. Investigating this could reveal a potential gap between synthesized and real-world data and help identify the factors influencing it.

[1] Yu et al., "Scaling Robot Learning with Semantically Imagined Experience"

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors seek to establish data scaling laws for the generalisation performance of robot manipulation policies trained on individual tasks where the policy is learnt via the imitation learning. The authors focus on establishing data scaling laws with respect to two features of the training data, the number of unique objects from an individual object category (e.g. bottles) and the number of unique environments. Through collecting demonstration data with handheld grippers (UMI) and evaluating policies trained on this data using a well-defined human scoring rubric, the authors establish a power law relationship between their scoring rubric and the policy generalisation performance. In this case, generalisation performance is examined only with respect to unseen objects and environments and the policy architecture reflect current SOTA  through leveraging diffusion policies. This paper provides important insights into data scaling laws in robotics and contributes valuable discussion to understanding effective data collection strategies for learning robot manipulation policies via imitation learning.

### Strengths
- The authors effectively contribute to the discussion of scaling laws for robot learning through extensive experiments in generalisation across unseen objects and environments. 

- The authors provide practical validation of their findings through using their insights to establish optimal data collection strategies for training policies, which they demonstrate on another set of tasks. 

- The authors provide a useful discussion around evaluation criteria for task success and provide an example of defining a scoring rubric for evaluating task success on specific tasks. 

- The authors provide ample information on their experimental setup and ensure that their experiments are reproducible.

- The overall quality of the experiments and discussion is good, while there are some limitations to this work the authors address many of these limitations in their discussions and provide solid experimental evidence for their claims. This is a valuable contribution to scaling laws for robot learning, while more work needs to be done overall I find this paper to be valuable.

### Weaknesses
 - Generalisation performance is only discussed for policy learning in the single-task setting, the paper doesn't consider the multi-task setting which remains very relevant in modern robot learning applications. 

- The scale of the demonstration datasets is limited, more work is required to ensure that the scaling laws hold true at larger scales. Specifically, the number of unique objects and environments, while diverse, may not be sufficient to extrapolate the observed power law relationships to real-world scenarios with significantly greater variability. The dataset size should be benchmarked against other similar robotic manipulation datasets to provide context for the claims made.

- Generalisation performance is only discussed with respect to two criteria, the authors also argue that these criteria encapsulates all factors a policy may encounter in real-world deployment. In general, I would say that this argument is incorrect. 

"We categorize generalization into two dimensions: environment generalization and object
generalization, which essentially encompass all factors a policy may encounter during real-world
deployment."

- The authors argue that they focus on out-of-domain generalisation, however they do not quantify out-of-domain in their experiments. This is more generally a challenge for evaluating generalisation performance of machine learning experiments. It remains a weakness of the current approach as we aren't quantifying out-of-domain which makes it challenging to comment on generalisation performance. With this being said the appendix provides visuals of the objects and environments which provides sufficient evidence for data diversity to support the authors claims. A more rigorous approach would involve defining a metric that measures the distance between the training and testing distributions, allowing for a more quantitative assessment of out-of-domain generalization.

- The scoring rubric for tasks has the potential to introduce subjective bias. In spite of this potential weakness, the authors effectively argue the need for this rubric versus more rudimentary metrics such as MSE. The results of this work hinge on a readers confidence in the scoring rubric for experiments, in general I feel confident in the quality of this work, however, it is important to mention this point.

### Questions
1. I believe the following argument is flawed and would like to hear your thoughts on this point:

"We categorize generalization into two dimensions: environment generalization and object
generalization, which essentially encompass all factors a policy may encounter during real-world
deployment."

Otherwise your paper was unambiguous so I have no further questions right now, congratulations on this work and thank you for contributing it to the robot learning community.

### Soundness
3

### Presentation
4

### Contribution
4

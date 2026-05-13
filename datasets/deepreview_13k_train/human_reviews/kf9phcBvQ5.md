# Replay can provably increase forgetting

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Continual learning seeks to enable machine learning systems to solve an increasing corpus of tasks sequentially. A critical challenge for continual learning is forgetting, where the performance on previously learned tasks decreases as new tasks are introduced. One of the commonly used techniques to mitigate forgetting, sample replay, has been shown empirically to reduce forgetting by retaining some examples from old tasks and including them in new training episodes.
In this work, we provide a theoretical analysis of sample replay in an over-parameterized continual linear regression setting, where given enough replay samples, one would be able to eliminate forgetting. Our analysis focuses on replaying a few examples 
and highlights the role of the replay samples and task subspaces.
Surprisingly, we find that forgetting can be non-monotonic with respect to the number of replay samples.
We construct tasks where replay of a single example can increase forgetting and  even distributions where replay of a randomly selected sample increases forgetting on average. We provide empirical evidence that this is  a property of the tasks rather than the model used to train on them, by showing a similar behavior for a neural net equipped with SGD. 
Through experiments on a commonly used benchmark, we provide additional evidence that performance of the replay heavily depends on the choice of replay samples and the relationship between tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a theoretical study on replay-based continual learning (CL) on overparameterized linear models. In particular, this paper shows that replaying with a single example can indeed be harmful, i.e., increasing the forgetting, under certain scenarios, by constructing task sequences appropriately. Theoretical results are provided for multiple cases. Moreover, experiments are conducted on both linear models and MLPs to verify the theoretical insights.

### Strengths
1. Theory on replay-based CL is very limited and this paper provides an attempt in this direction to understand when replaying one examplar can increase forgetting.

2. The theoretical results are verified in the experiments. 

3. The presentation is clear.

### Weaknesses
1. The assumptions are too strong, particularly assumption 2.2. It is hard to justify how this can be true in practice. The assumptions 3.1 and 3.3 are also restrictive. For overparameterized linear models, assuming a constant sample norm is not widely seen. Given the fact that investigating linear models is already a restrictive setup, making these additional assumptions further weakens the importance of the theoretical results.

2. The definition of forgetting in equation 3 is based the training samples, which does not make sense at all. 

3. While the average case uses a more standard definition of forgetting on test samples, the theoretical results is only limited to a simple two-task setup.

4. The experiments are only very limited, especially for the setup with neural networks. While the theory might take more efforts with more than 2 tasks, the experiments can be easily done with more tasks, which is not the case in the paper. Besides, to convince readers that the theoretical insights can also be observed in neural networks, more experiments on larger dataset such as CIFAR should be conducted. While the theoretical results have been observed in certain scenarios, the small-scale experimental verification cannot sufficiently convince the readers that replaying with a small number of samples is often harmful in CL. Even in the experiments in this paper, replaying with one sample usually helps.

5. It is not clear how useful the theoretical results in this paper can be, as they highly depend on deliberate constructions of tasks and data.

### Questions
Please see the weaknesses above. One more question is how you handle the correlation between learned model and replay data in the average case in theory.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper analyzes replay in the realizable linear regression setting (Evron et al. 2022). The paper shows formally that replay can increase forgetting in two settings: a worst-case setting for single samples, and an average case for appropriate task sequences. Toy experiments match the theoretical results, showing increased forgetting for low replay sizes (up to 3 samples in total).

### Strengths
- The paper is well written and easy to read.
- The paper tackles an important theoretical question, that is the problem of how to analyze replay-based continual learning.

### Weaknesses
The paper makes a very strong statement: "Replay can provably increase forgetting". Results on replay may be the most robust piece of evidence in the whole continual learning literature. Therefore, I expect that claiming that replay provably increases forgetting requires exceptional evidence. I would argue that the results of the paper are more a property of the extremely limited setting than a general property of replay-based methods.
- (line 65) the paper argues that it is counter-intuitive that there are worst-case settings. However, the paper only considers very low memory sizes. It is well known that intra-task interference is an issue, as shown in the paper. Therefore, the results are not counter-intuitive but agree with the literature.
- (theoretical analysis) It is interesting to see that the analysis still somewhat generalizes to the "average-case" setting. However, this is still a very artificial setting. No one expects replay to work with a single example. There are empirical results showing it may be beneficial, but those only demonstrate that very small replay buffers may work, not that they should.
- (experimental evidence) The experiment on MNIST uses replay on a single class or on very few samples (forgetting only happens with less than 3 samples). Again, forgetting in this setting is not exactly surprising and it is not sufficient evidence for the main claim.

The paper claims that "forgetting is a property of the task rather than the model", which I don't think is sufficiently supported by the evidence, given that it only happens in a very limited setting (Split MNIST with very limited replay). Of course forgetting is partially a consequence of task interference (or intra-task interference in this case), but data does not fully explain forgetting.

Overall, I think the paper should be generalized to stronger results in a more general setting to be a useful theoretical analysis of replay.

minor:
- I think assumption labels are not updated
- L115 typo: Inverse of X_t

### Questions
See weaknesses above.

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The best-performing methods for the Continual Learning problem are currently memory-based. These methods save a percentage of examples from previous tasks that can be used in subsequent tasks. The authors perform a theoretical analysis of how example selection affects forgetting. The authors show that, given certain assumptions and constraints, there are scenarios where specific examples can cause more forgetting than not having them in the buffer. The authors show that this is particularly critical when the buffer is limited to a small number of samples per task. The authors also provide an empirical analysis using MNIST.

### Strengths
- Theoretical analyses in the area of CL are scarce. The authors identified a gap between previous work and current methods, which can help to understand the limitations and strengths of current memory-based methods, as well as help to understand some empirical results that may be unintuitive.
- The work has a clear motivation, and the authors identified a need to increase the theoretical understanding in this research area.

### Weaknesses
 - I agree with some of the authors' conclusions, but they ignore an essential body of work in CL that focused on the selection of items stored in memory. Although many of these papers focus on empirical studies, they reach similar and, in some cases, more robust conclusions than those found in this paper.
    - The authors' analysis is based on simple models and scenarios, which can often be difficult to extrapolate to more complex scenarios. If empirical results are presented, I recommend also presenting more complex scenarios (e.g., TinyImageNet) to make the results more robust. This is particularly important since it is well-known that different models and methods behave differently in more complex scenarios.
    - This is even more crucial when the assumptions of the scenarios presented in the analyses are rarely presented in more complex situations, which reduces the impact of the analyses presented.
- Something that I cannot entirely agree with the authors, but I think maybe a problem of definitions, is presented in lines 170-172, which is then stated in Remark 3.7. I do believe that it can be a problem of overfitting since in high dimensionality problems, when replaying a model with a single example, the model will tend to over-represent this sub-space, and if the class or task is representable by multiple spaces within the distribution (which is a common issue), these will be forgotten due to the overfitting of this example to a particular sub-space. In this case, overfitting and interference may be related,  but they do not rule it out completely, as the authors do. Could the authors clarify the definition of interference or overfitting? 
    - The problem lies in how the whole work is presented since the authors speak of sub-spaces that generate forgetting, which can be seen as an overfitting of the selected example. It would be good if the authors could analyse why they believe it is not overfitting.

### Questions
- From the results presented. How feasible is it that these can be extrapolated to:
    - More complex scenarios where the orthogonality assumption is not met?
    - Scenarios where the distribution of tasks/classes is not uniform? Or is it more complex, for example, when each task/class may consist of multiple sub-spaces?
    - For example, in worst-case analysis, can the adversarial example be replaced by one outside or away from the training distribution? This commonly happens in complex datasets. How similar would these results or analyses be to those presented in the paper?
- How are the task data generated in the analysis?
    - Suppose they are created from simple distributions (such as a Gaussian) without a possible relationship between the classes. In that case, it is easy to see that the interference between the tasks can be low. The restriction of the assumptions may affect the analysis presented.
    - How does the analysis behave with a possible correlation of the distributions of the different tasks?
- Can your analysis be used to propose a new method to populate the memory?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the performance of replay-based methods in an over-parameterized linear continual learning (CL) model through both theoretical analysis and experiments. The findings reveal an uncommon phenomenon: replay may negatively impact CL performance. The theoretical analysis illustrates this phenomenon in two scenarios—adversarial and random replay. In experiments, the theoretical results are verified and extended to real datasets, demonstrating that the negative effects of replay can also be observed in practice.

### Strengths
They studied the negative impact of replay in CL, which is indeed a surprising topic. Their theoretical results explained the reason of the negative impact, which is further verified in experiments.

### Weaknesses
Both theoretical(Theorem 3.6) and experimental results focus on T=2, which is not general enough. Theorem 3.2 is an extreme example, which makes the result less surprising. Furthermore, the experimental parts should at least present what will happen when T is large than 2.

### Questions
After reading your paper, I have the following questions and suggestions.
1. As I'm concerned in weaknesses, Theorem 3.2 appears to be rather extreme(two taks with three samples), making it unsurprising that there exist certain cases where replay may negatively impact the performance related to forgetting. Can you provide addtional analysis to illustrate this observation under a more general problem setup?

2. Theorem 3.6 focus the average performance in the case of only two tasks. Similar to Theorem 3.2, it demonstrates only the existence of an example, without providing a more detailed illustration of when this phenomenon occurs. As far as I know, [1] has present a closed form of forgetting and generalization error for T=2 in a similar problem setup. Based on this, one can observe that the performance of forgetting is not monotonic with respect to the size of replay. This can be interpreted as a more comprehensive conclusion regarding the impact of replay. In comparison to the aforementioned conclusion from their work, could you provide additional insights derived from your own conclusions?

3. The experiments focus on the case when T=2, which may not provide sufficient insight for practical applications. Could you conduct additional experiments for scenarios where T>2?

4. A key question that significantly influences my assessment of your paper is: Based on your theoretical and empirical findings, can you provide a more systematic characterization or discussion of the conditions under which replay is detrimental versus beneficial?

Reference:
[1] Banayeeanzade, M., Soltanolkotabi, M., & Rostami, M. (2024). Theoretical Insights into Overparameterized Models in Multi-Task and Replay-Based Continual Learning. arXiv preprint arXiv:2408.16939.

### Soundness
3

### Presentation
3

### Contribution
2

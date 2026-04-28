# B-STaR: Monitoring and Balancing Exploration and Exploitation in Self-Taught Reasoners

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
In the absence of extensive human-annotated data for complex reasoning tasks, self-improvement -- where models are trained on their own outputs -- has emerged as a primary method for enhancing performance. Recently, the approach to self-improvement has shifted toward a more dynamic, online fashion through iterative training processes. However, the critical factors underlying the mechanism of these self-improving methods remain poorly understood, such as under what conditions self-improvement is effective, and what are the bottlenecks in the current iterations.
In this work, we identify and propose methods to monitor two pivotal factors in this iterative process: (1) the model's ability to explore and generate high-quality responses among multiple candidates (exploration); and (2) the reliability of external rewards in selecting the best responses from the generated outputs (exploitation).
These factors are inherently moving targets throughout the self-improvement cycles, yet their dynamics are rarely discussed in prior research -- It remains unclear what impedes continual model enhancement after only a few iterations. 
Using mathematical reasoning as a case study, we begin with a quantitative analysis to track the dynamics of exploration and exploitation, discovering that a model's exploratory capabilities rapidly deteriorate over iterations, and the effectiveness of exploiting external rewards diminishes as well due to shifts in distribution from the original policy.
Motivated by these findings, we introduce B-STaR, a Self-Taught Reasoning framework that autonomously adjusts configurations across iterations to Balance exploration and exploitation, thereby optimizing the self-teaching effectiveness based on the current policy model and available rewards.
Our experiments in mathematical reasoning demonstrate that B-STaR not only enhances the model's exploratory capabilities throughout training but also achieves a more effective balance between exploration and exploitation, leading to superior performance. Crucially, this work deconstructs the opaque nature of self-training algorithms, elucidating the interpretable dynamics throughout the process and highlighting current limitations for future research to address.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper is addressing how to improve self-taught reasoners. It addresses the challenges of iterative self-improvement for reasoning tasks in AI models, particularly in mathematical problem-solving. With limited access to high-quality, human-annotated data, models are trained to refine themselves via generated outputs. However, performance gains often stagnate after a few iterations, with degradation in exploratory diversity and effectiveness of rewards. To counter these issues, B-STAR introduces a dynamic framework that monitors and balances exploration (generating high-quality candidate responses) and exploitation (selecting optimal responses using reward mechanisms).

Key innovations include metrics like "Pass@K" for exploration and "Best-of-K" for exploitation, which quantify the model's ability to generate diverse and correct outputs while ensuring selected outputs are useful for training. B-STAR adapts configurations such as sampling temperature and reward thresholds, adjusting them based on "query effect" scores to optimize exploration-exploitation balance iteratively. In each iteration, the algorithm dynamically adjusts configurations, specifically sampling temperature and reward thresholds, to maximize the "query effect" score, which ensures an effective balance. The model then generates multiple responses per query, selecting only those with high rewards to use as training data for the next iteration. This process is repeated across iterations, inheriting the optimizer and learning rate to maintain consistency in online training and continually improve model performance.

The experiments in B-STAR evaluate its effectiveness on mathematical reasoning and coding tasks, comparing it against other self-improvement methods like Iterative RFT and Online RFT. B-STAR consistently outperforms these baselines in generating accurate responses, as shown by higher Pass@1 and Pass@K-S scores, which indicate both accuracy and diversity in responses. In mathematical tasks, B-STAR maintains exploration across iterations, unlike other methods where diversity declines, highlighting its balanced approach to exploration and exploitation. For coding challenges, B-STAR achieves steady improvement across iterations, suggesting that dynamic configuration adjustments improve response quality over time. The experiments validate B-STAR’s approach in sustaining a higher growth rate in performance by adaptively balancing exploration and exploitation.

### Strengths
- Dynamic Balancing of Exploration and Exploitation
- Comprehensive Metrics for Monitoring
- Empirical Validation with strong results
- Insightful Analysis of Self-Improvement Dynamics

### Weaknesses
 - Reliance on fixed reward models
- complexity of configuration tuning
- limited generalization across task types
- potenitalluy saturate in long iterative training

### Questions
- address weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces B-STAR, a framework aimed at improving the self-improvement process of large language models in complex reasoning tasks, such as mathematical problem-solving and coding. The primary challenge addressed is the difficulty in balancing exploration (the model's ability to generate diverse, high-quality responses) and exploitation (the model's ability to effectively select the best responses) in iterative training processes without extensive human-labeled data.

### Strengths
**1.Identification of Balance Problem and Innovative Framework.** The introduction of dynamic parameter adjustment based on the "query effect" metric is an innovative approach to optimize performance across training iterations.

**2.Clear Explanation of Exploration and Exploitation Dynamics**: By quantifying exploration and exploitation using metrics such as Pass@K and Reward@K-S, the paper provides insights into the dynamics of these factors, which are often overlooked in self-improvement research. This deepens understanding of the critical factors for model self-improvement.

### Weaknesses
 **Limited Applicability Beyond Specific Tasks**: The paper focuses primarily on mathematical reasoning and code generation tasks, which limits the perceived applicability of B-STAR to other domains (e.g., open-domain question answering, language understanding) that query effect is hard to evaluate. And since QE is critical for following dynamical adjustment, this greatly limits the application.

**Lack of Theoretical Foundation for Query Effect Metric**: Although the query effect metric is practical for optimizing exploration and exploitation, the paper lacks a rigorous theoretical justification for this metric. This could raise questions about its generalizability and effectiveness across a broader range of tasks and model architectures. Specifically, the metric's sensitivity to the choice of the sampling strategy and the reward model is unclear. For instance, if the reward model is noisy, the query effect might be misleading, causing the dynamic parameter adjustment to be suboptimal.

**Unkown advantage over hyperparameter shift.** It seems that the final dynamics of the parameters do not fluctuate a lot. It should the excluded that most of the benefit is gain by adding an offset rather that dynamically change these parameters.

### Questions
**1.Ablation and Related Work**: From figure 4, it seems that after 1000 iterations, parameters like temperature and threshold remain constant. So essentially the dynamics freeze. *Does this imply that original hyperparameter is simply not set to optimal?* It is important to see how static shift of hyperparameter can help to fully verify the effectiveness and necessity of the proposed method. Also, there lacks an explicit discussion and reference to the line of work that dynamically change the hyperparameter.

**2.Query Effect Metric Validity**: How robust is the query effect metric across different tasks beyond mathematical reasoning and code generation? Without a theoretical foundation, is there a risk that this metric might not generalize well to other domains that require different types of exploration-exploitation balances?

**3.Reward Model Dependency**: The paper relies heavily on reward models (both answer-based and process-based). How does the performance of B-STAR change if the reward model is not well-aligned with task objectives? In cases where defining an accurate reward model is challenging, can B-STAR still maintain its effectiveness?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper is concerned with the field of self-improvement of LLMs in the context of complex reasoning tasks. Inspired by the classical RL literature, the authors identify the notions of exploration and exploitation, with their definitions adapted to the new domain, as important factors in this training procedure. They propose the B-STaR framework to address them in a dynamic way. The work first identifies factors responsible for the performance collapse observed in the self-improvement regime and then proposes to automatically adapt the training procedure to overcome it. This is done by automatically adapting two influential hyperparameters, the temperature and the reward threshold, based on the introduced query effect metric. The experimental evaluation is based on mathematical reasoning and coding tasks, showing that B-STaR leads to improved performance.

### Strengths
S1. The paper describes the underexplored notions of exploration and exploitation in the current research on self-improvement in complex reasoning tasks and empirically detects factors that are responsible for a balance between them. Based on that, a query effect metric is proposed to automatically adjust the related hyperparameters throughout training, which is shown to improve the performance in comparison to previous approaches.

S2. The intuitive approach to balancing the trade-off between exploration and exploitation is nicely supported with a series of experiments (Sections 2 and 3) that guide the reader to better understand the influential factors.

S3. A general overview of the approach is well summarized well with the pseudocode provided.

### Weaknesses
W1. My main concern about the paper is its generalizability to a broader spectrum of complex reasoning tasks. The empirical evidence is provided for two cases, one for mathematical reasoning and the other connected to coding tasks. As I am not an expert in the field, I am not aware of the number of other benchmarks that could extend the evaluation. Could the authors provide a summary of the scale of the experimental evaluation of the main papers that they compare with?

W2. The paper would strongly benefit from a more principled approach of introducing specific concepts related to self-improvement training. I would appreciate if the main or supplementary text included the definition of the SFT loss, a more detailed description of RFT, some formalization of greedy decoding, clear distinctions of trained and fixed reward functions etc. In general, formulating the paper's concepts in a mathematical language would greatly improve clarity.

W3. Some ambiguous statements are included throughout the paper which makes it difficult to follow the reasoning of the authors. For example, despite going through lines 155-160 multiple times, I was not able to grasp what the authors had in mind. Lines 167-168 mention that the distribution of candidates impacts how the reward model differentiates them, which suggests the distribution somehow influencing the reward function. I assume that the reward function is fixed and the authors meant that the distribution of candidates influences the distribution of the corresponding reward values? Or this depends on the case whether the reward is actually trained or not? I also found it hard to distinguish between the two points mentioned in lines 321-323. What is the difference between stating that `(the number of) high-quality respones among the selected ones cannot be too small' and `the percentage of the high-quality responses among the selected ones must be large enough'?I am certain that the phrasing could be improved in all of these cases.

W4. I have some concerns regarding the methodology of the empirical evaluation which is not per-se the weakness of the paper but rather of the research field. Lines 214-215 mention that, in mathematical problems, the responses are evaluated according to only the final answer and not the entire series of reasoning steps. Do I understand correctly that such evaluation would classify as correct a mathematical proof that follows wrong reasoning but arrives at some form of correct conclusion?

W5. The conclusions from Section 3.2 are based on modifying individual hyperparameters while keeping the others fixed. My concern is that the fixed values could be simply cherry-picked to fit the conclusions. Could the authors provide further motivation on why these exact fixed values should be chosen and maybe extended empirical results showing the trend for other fixed values?

W6. Tables like Table 2. should be described more extensively, along with more examples for other cases, since the adaptability of the author's approach is the main contribution of the paper. Based on Table 2. alone, it seems questionable whether any adaptation of the reward threshold parameter is necessary, since only in the beginning its value differs from other stages of the training. The increasing trend of the query effect is promising, but because only single example is provided, I am not convinced that this is always the case.

W7. Figure 6. is missing the plot for the APPS dataset. Typos: `answewrs` (line 253), `Exploration decreases over training and PRM helps retain` (line 282) <- retain what specifically?, `keeps improve` (line 295). For clarity of presentation and improved readability, the plots in Figures 5. and 6. should have the y-axis starting at zero. One could first think that plot (c) from Fig. 5 shows a higher relative improvement than plot (a) from the same figure, which does not seem to be the case after further inspection. I also strongly encourage the authors to open-source their code to allow for easy reproducibility.

### Questions
I have blended the questions into the Weaknesses part, hence will be happy if the authors address those extensively. My general impression is that the paper describes a nice idea of transfering the notions of exploration and exploitation into self-improvement regime, but struggles with clear communication along the way. Introducing the query effect and showing that it may be incorporated during training to adaptively modify two important hyperparameters seems to be a very interesting contribution to the field, but the empirical evidence does not clearly indicate the connection between the metric and the hyperparameters, and if it could not be simplified with just simple heuristical schedulers. Overall, the authors could elaborate more extensively on the theoretical and formal background of the paper's topic as well as the obtained results. As I am not an expert in this field, I am open to raising my rating if solid and broad arguments are provided.

### Soundness
3

### Presentation
2

### Contribution
2

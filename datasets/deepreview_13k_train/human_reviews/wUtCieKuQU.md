# Towards Effective Evaluations and Comparison for LLM Unlearning Methods

- Decision: Accept
- Scores: 3, 8, 5, 6

## Abstract
The imperative to eliminate undesirable data memorization underscores the significance of machine unlearning for large language models (LLMs). Recent research has introduced a series of promising unlearning methods, notably boosting the practical significance of the field. Nevertheless, adopting a proper evaluation framework to reflect the true unlearning efficacy is also essential yet has not received adequate attention. This paper seeks to improve the evaluation of LLM unlearning by addressing two key challenges---a) the robustness of evaluation metrics and b) the trade-offs between competing goals. The first challenge stems from findings that current metrics are susceptible to various red teaming scenarios. It indicates that they may not reflect the true extent of knowledge retained by LLMs but rather tend to mirror superficial model behaviors, thus prone to attacks. We address this issue by devising and assessing a series of candidate metrics, selecting the most robust ones under various types of attacks. The second challenge arises from the conflicting goals of eliminating unwanted knowledge while retaining those of others. This trade-off between unlearning and retention often fails to conform the Pareto frontier, rendering it subtle to compare the efficacy between methods that excel only in either unlearning or retention.  We handle this issue by proposing a calibration method that can restore the original performance on non-targeted data after unlearning, thereby allowing us to focus exclusively on assessing the strength of unlearning. Our evaluation framework notably enhances the effectiveness when assessing and comparing various LLM unlearning methods, further allowing us to benchmark existing works, identify their proper hyper-parameters, and explore new tricks to enhance their practical efficacy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper tested 4 popular LLM unlearning methods on the TOFU benchmark dataset and observed that there are various tradeoffs (e.g. GA unlearns better while NPO retains better). Then it motivates the authors to propose a new metric which is based on the mixing the model weights between the unlearned and original model. The reason, as far as I understand, is to achieve smooth control on the extent of unlearning. The evaluation first finds the model mixing ratio that would achieve the evaluation score (e.g. ES) on the retain set, and then uses it to calibrate unlearning metric.

### Strengths
S1: LLM unlearning and evaluation are important problems

### Weaknesses
W1: Lack of technical contribution: I think most people working in this area would agree we need more metrics and benchmark datasets. However, this paper though goes into that direction, does not really provide enough meaningful and technical contribution in my view. The paper basically tried 4 popular unlearning methods on the TOFU datasets while proposing a calibration framework (See W2). This can mostly be done in leaderboard or in a measurement paper rather than a technical paper. And findings on metric tradeoffs are mostly not surprising.

W2: Lack of justification of the calibration framework: The calibration metric lacks justification. Figure 3 seems to only tell us ES is monotonically increasing with mixing factor $\alpha$. However, the key question in proposing a metric is to ask: What does this metric measure? Does it measure the right thing? In this case, I cannot see clearly the impact of mixing model weights on the overall unlearning effectiveness. The only justification I can find is (1) being inspired by the literature on parameter disentanglement, but why is it related to unlearning? (2) The vague observation in Figure 3. Can authors explain why mixing model weights can help calibrate the unlearning metric other than just the empirical observation between ES and $\alpha$ in Figure 3? After all, this can well be a spurious correlation. In other words, why would the community trust this calibration in evaluation? 

W3: Lack of organizing clarify: The paper spends the first 6 pages motivating the calibration framework, and only 1 page introducing it and 1 page for experiments. I think people who in this area already know most of the points in the first 6 pages, it'd better to shorten it and get to the point more directly and spent more content on introducing the key idea of calibration and include more justification,

### Questions
See W2.

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
5

### Summary
This paper studies how best to evaluate LLM unlearning methods that aim to not leak the correct answers on a forget set while maintaining good performance on the rest of the training data. The literature has proposed a variety of evaluation metrics, and this paper first tackles which metric is most robust to information leaking attacks; they conclude ES, which was proposed with privacy attacks in mind, performs best in keeping the ranking before and after various attacks consistent. With ES, they then evaluated a generalized hyperparameter sweep for popular methods proposed in the literature, and conclude that methods have not significantly improved over the baseline of gradient ascent approaches. Narrowing why this is the case, they observe alternative methods either unlearn too strongly or not strongly enough to calibrate the performance on the retain set.

### Strengths
1) Extensive empirical study
2) Proposed method for improving calibration via a general hypermater boosts performance of baseline methods to seemingly SOTA
3) Mostly well-written

### Weaknesses
1) I found that certain parts of the draft could have been clearer about the benefits of model mixing. The draft does not discuss alternative calibration of retain performance, which naively could have also been done with just a sweep of the unlearning method hyperparameters. So at first I thought this was an empirical limitation. But after thinking about it I realized this is actually okay as the performance of calibration with just a hyperparameter sweep of the unlearning method is subsumed by the hyperparameter sweep including model mixing to calibrate (the former is just taking the hyperparameter in the latter where $\alpha  = 1$). Results in the appendix also suggest the hyperparameters for current unlearning methods are not sensitive enough to calibrate retain performance. In the questions section I ask clarifying questions about this and suggest edits to the text that could make this contribution clearer. 

2) The empirical results are also focused on specific values of $\tau$, i.e., retain performance should be $95-90\%$ of the performance before unlearning. While I agree “high performance” seems to be the reasonable use-case, a more complete comparison without assuming specific $\tau$ values would also identify what $\tau$ range (if ever) NPO and other methods start performing well again. I believe it is implicit from the further study in the appendix that a “low” $\tau$ range might make other methods perform better, but I believe a more quantitative statement could make the empirical study more complete. I ask about this in the questions section.

3) (minor) A more general weakness, not specific to just this paper, is whether these performative unlearning goals for LLMs should also be generalization questions; if the goal is to not predict accurately for a set of samples, and those samples come from larger distribution, should we not be evaluating a “test” performance on the larger distribution? This is generally called concept unlearning in the literature. The field may still be far away from evaluating/studying such questions, but I raise it to clarify the setup studied in this paper is not the only setting for unlearning in LLMs. The authors might consider having more discussion on different formulations of unlearning before picking the setting they study and survey.

### Questions
I look forward to discussing the below with the authors, and am willing to increase my score given clarification of the questions below.

1) In the paragraph “Is MM Proper for Calibration” what seems missing is discussion comparing this to a simpler/baseline approach, such as just tuning the original hyperparameters of the unlearning method to calibrate. From the Appendix I got the impression that the hyperparameters of many of the unlearning methods do not give enough control to calibrate, is this correct? If so, discussion (and/or a figure illustrating this) would help the argument that MM is a better way to calibrate/boost the performance of unlearning methods.

2) Related to the above, in the “Hyper-parameter configurations” paragraph in the experiments, am I correct in understanding you do the hyperparameter sweep by evaluating the performance of the hyperparameters after also applying model mixing to calibrate the performance (this seems consistent with the appendix tables)? If so, you might consider adding somewhere in the paper that this hyperparameter sweep necessarily improves over the calibrated performance of not doing model mixing; this is as not doing model mixing is captured by just picking the best hyperparameters amongst those with $\alpha = 1$. I believe this adds conceptual understanding to why model mixing is necessarily better.

3) On the discussion of why NPO and other methods do no work in the experiments section, do you have results for what $\tau$ values (if at all) other methods start performing well? I’m imagining a figure where the x-axis is calibrated $\tau$ level, and the y-axis is forget performance, and a line for each method such that when the line is the lowest explains for what $\tau$ each method is best. Alternatively, some more detailed/explicit discussion for what $\tau$ levels other methods might perform better could help give a more complete picture for when other methods work well. I agree the high $\tau$ range seems most practical, but I think the above can be done easily given results in the appendix and can add to the empirical study.

4) (minor) model mixing seems very related to the literature on model merging; you might consider surveying the literature more broadly as a reference for the method, and when/why it works.

5) (minor) If computationally feasible, could error bars/standard deviation be reported for some of the main tables; I am less concerned given the many settings tested, but this could add to the rigor of the empirical findings.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper surveys the current popular evaluation methods towards LLM unlearning. It discuss the need to cover before retain and forget performances and its trade-offs, as well as its robustness against different attacks.

The paper concludes that Extraction Strength (ES) is the recommended method for evaluation. In addition, the paper also suggest Unlearning with Control (UWC) framework to reach the best trade-off between unlearning strength and retain performance.

### Strengths
The paper have a comprehensive view of different unlearning evaluation methods and approaches them in a systematic manner from robustness and utility trade-offs.

The paper proposes a novel approach unlearning with control to better calibrate the trade-off between unlearning effectiveness and retain performance with model-mixing, which is a simple but effective mechanism.

### Weaknesses
There is a lack of justification for selecting the metric: Why does the PCC measure the metrics' robustness again attacks? In Figure 2, the plot is characterized by the test static before and after the attack for different methods, models, and forget set ratio. Why should we assume there is a linear correlation among them? The paper argues that an optimal metric should maintain its value after attacks, but the plots in Figure 2 show many points below the y=x line, indicating a decrease in metric score after the attack. This contradicts the stated goal of maintaining metric values. Furthermore, if the goal is to maintain the same score before and after the attack, why use a linear fit at all? Shouldn't the metric simply measure the distance to the identity line? A high PCC can still be obtained even if a method is highly susceptible to attacks, as long as the change in score is linear. In addition, the paper uses TOFU as unlearning dataset/task, but does not survey the metric used in the TOFU paper (truth ratio).

Weak/unclear attack methods: it is unclear the what dataset the relearn attack in figure 2 is based on (from other section I would think it is TOFU, but it is not presented until late in the paper). The setup for relearning it not clear. If the entire TOFU dataset is used for relearning, this does not seem like a realistic evaluation of unlearning robustness, as it would essentially retrain the model on the forgotten data. The relearning setup should be more nuanced to test the model's resistance to relearning specific forgotten information, rather than simply retraining on the entire dataset.

Although UWC seems like a method to manage the trade-off between unlearn and retain performance, it is not clear how it fits into unlearning evaluation pipeline.

### Questions
The statistic in figure 2 is confusing. How does model have lower score (which means better unlearning from the paper) after attacking than before?

### Soundness
2

### Presentation
1

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
The paper aims to answer the following research questions in machine unlearning: (1) What metric should be used in machine unlearning (2) what method is better in trading off unlearning and retention. The paper first presents a comparative study to understand what metric is robust (i.e., present a linear relationship before and after jailbreaking attacks), then proposes to use model mixing to for better calibration between retention and unlearning.

### Strengths
(1) The problem is well-motivated.

### Weaknesses
(1) For the metrics used for machine unlearning, The author suggests using Extraction Strength as the metrics since it exhibits linear relationship before and after different attacks. However, the evaluation is still weak to me. First of all, the attacks used in the paper are not the strongest jailbreaking attacks (like GCG attacks) and the authors also do not consider using an ensemble of strong attacks to elicit model’s knowledge, making the evaluation of the paper weak. Also, showing linear relationship before and after attack might not be a good way to measure machine unlearning before and after attack, especially if the model is backdoored or poisoned (e.g., a poisoned and backdoor model can hide their knowledge in their model parameters except when a trigger is presented or obfuscate the knowledge so that the metrics cannot used to detect unlearning). In short, there are no rigorous guarantees that using extraction strength is a valid metric under an adversarial scenario.

(2) The contribution is incremental. To me, the most novel part of the paper is that the authors use model mixing (aka model merging/souping) to control the trade-offs between retention and unlearning. All the other parts seem incremental and do not convey interesting empirical findings.

(3) The writing of the paper needs to be improved. A lot of useful details help to digest the results are shown in the appendix instead of the main text (e.g., attack methods) and the main text does not give enough concise summary to understand them. For example, I still cannot understand how we use Token Noising as an attack method (even the appendix does not give a good description of it). Also, the organization of the paper could be improved (e.g., lines 264-265 ask the reader to first read Section 6 for the experiment).

### Questions
Please provide response to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

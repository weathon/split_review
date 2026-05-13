# U-shaped and Inverted-U Scaling behind \\Emergent Abilities of Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Large language models (LLMs) have been shown to exhibit \textit{emergent abilities} in some downstream tasks, where performance seems to stagnate at first and then improve sharply and unpredictably with scale beyond a threshold. By dividing questions in the datasets according to difficulty level by average performance, we observe U-shaped scaling for hard questions, and inverted-U scaling followed by steady improvement for easy questions. Moreover, the emergence threshold roughly coincides with the point at which performance on easy questions reverts from inverse scaling to standard scaling. Capitalizing on the observable though opposing scaling trend on easy and hard questions, we propose a simple yet effective pipeline, called \textit{Slice-and-Sandwich}, to predict both the emergence threshold and model performance beyond the threshold.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper connects two well-known phenomena in deep learning, namely emergent capabilities and inverse scaling. By breaking down the scaling curve to different difficulty levels, the authors show that LLM skill emergence can be the result of an inverted-U-shaped scaling on easy questions, where the easy-questions curve cancels out the scaling on hard questions. The authors propose a method to predict emergent scaling by fitting sub-groups of the dataset separately.

### Strengths
- The main result of this paper connects two important topics in the field, inverse scaling and emergence, making it a very relevant research topic, especially since neither phenomenon is well understood.
The results on MMLU and Persian-QA are clear enough, in my opinion, to establish the existence of a connection between U-shaped scaling and emergence. Although Big-bench arithmetic and the appendix results are less clear, they do not diminish from the other results. Even if the easy-hard data split failed to visualize inverse scaling in the latter experiments, a different split might still show similar curves to MMLU.

- The proposed fitting method, slice-and-sandwich, showcases how the documented phenomenon can be used to predict emergence in practice.

- The paper is clearly written and easy to follow.

### Weaknesses
 - While the fitting method is an overall positive addition to the paper, it is less convincing than the scaling results (which are, for me, the main result of the paper). The fits shown in the main section use knowledge of the point where emergence starts, making them of little value, since predicting that point is the main reason why we care about fitting emergence. 
Appendix F2 fixes that issue by showing fits on random sections of the scaling curve before emergence, but these fits are not so convincing as a reliable method to predict the point of emergence.

- Appendix E shows the scaling curves when plotting accuracy, and attributes the difference from the main results to accuracy being a 'crude measure', which is not a satisfactory explanation to me.

- Minor correction: In the definition of $M$ (line 128), $N$ and $D$ are mixed up.

- Naming $M$ 'effective model size' is confusing for the reader, since model size is $N$ while $M$ is actually the log of compute $C$. Maybe a better name would be 'effective compute' or just 'log compute?

### Questions
- Minor correction: In the definition of $M$ (line 128), $N$ and $D$ are mixed up.

- Naming $M$ 'effective model size' is confusing for the reader, since model size is $N$ while $M$ is actually the log of compute $C$. Maybe a better name would be 'effective compute' or just 'log compute?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates explanations for LLM emergent abilities (sharp transitions from chance-level to high performance as a function of model size) and proposes a method to predict emergent performance. They show that on certain task, when questions are group by difficulty, two distinct scaling trends appear: U-shaped scaling for hard questions and inverted U-shaped followed by improvements for easy questions. This motivated a method for capabilities forecasting: fitting polynomial regression separately for easy and hard questions and then aggregating the results.

### Strengths
1. The paper addresses a very timely topic: the science of LLM evals and predictive evals. It is relevant for scientific understanding of frontier LLMs as well as for AI policy (informing capability thresholds and buffers in responsive scaling policies).
2. The paper described an interesting insight that easy and hard questions have different scaling trends and that this could explain sharp transitions of aggregate performance

### Weaknesses
1. I found the paper hard to follow. I think the clarity of writing and figures could be substantially improved. Some concrete suggestions:
(a) the name "binary Brier score" is very confusing. What's binary about it? It's continuous for each question.
(b) I think it's very confusing to say Brier score is "noisy due to insufficient confidence calibrations" (line 161). What does it mean to be sufficient? Why is this noise? Why "calibrations" in plural?
(c) what are "available choices' (line 159)? Is it the same as classes (line 139)?
(d) names for difficulty levels (e.g. 0_1502_brier) are confusing. They're okay in Python code, but I'd expect something more readable and abstracting away from distracting details (e.g. I don't really care it's 1502 questions).
(e) The colors on plot could match the semantics of difficulties, e.g. you could use a continuous color map (e.g. red-blue transition to represent easy-hard transition).
(f) plots for different datasets could be next to each other
(g) "Slide-and-sandwich approach allows the data to speak for itself" is misleading. The whole point is that you bake in more assumptions in the method.
2. The name "effective compute" is somewhat misleading if it's just log compute. Ideally, effective compute could be something like g-factor [1] or the first principal component from observational calling laws [2, 3]. It would be great to use that as a metric. Or at the very least, it should be just called "log compute".
3. Authors only evaluate their methods on 3 datasets (plus 3 more in the appendix). I don't think that's enough to justify the claim that they found a general method for capabilities forecasting and a general explanations of emergent features. BIG-Bench includes more than 200 tasks.
4. Relatedly, all of them do show emergent capabilities. I wonder how Slice-and-sandwich methods behaves on tasks that do not show emergent capabilities: does it falsely predict them? I think this is an important point: so far the authors only presented a method for emergent capabilities forecasting conditional on the presence of emergent capabilities. But in practice we don't know that in advance.
5. Overall, I'm somewhat underimpressed by predictive performance and I worry that the authors overfit to a particular set of 6 tasks. If find some patterns in a dataset and bake in this pattern as an inductive biases of your method (polynomial regression), surely you'll improve predictive performance. But will those inductive biases generalize to entirely new tasks you never looked at? The authors provide no evidence for that (unless I'm missing something, happy to be proved wrong).
6. I'm not super convinced this is a general explanation of emergent capabilities. Maybe others have different scaling trends? The whole point that a superposition of U-shaped and inverted-U shaped scaling explains emergent capabilities is also somewhat qualitative. It's not starkly clear from the plots, e.g. MMLU does not seem consistent with this explanation.
7. Consider discussing [4] as related work

### Questions
1. How were the 6 tasks you experiment on selected? What were the criteria and at what point were they selected?
2. What's the functional form of the polynomials you fit (line 416)?

### Soundness
2

### Presentation
1

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
This paper investigates the emergent behavior of large language models as their effective size increases. The authors observe that for certain downstream tasks, the continuous metric exhibits a U-shape for easier questions and an inverted U-shape for more difficult questions below the emergence threshold, with steady improvements beyond this threshold. Additionally, they propose a method for forecasting model performance beyond the emergence threshold.

### Strengths
1. The paper connects the scaling trend on easy questions with the double descent phenomenon in deep learning is quite interesting.
2. A group-wise scaling law based on difficulty level can offer more detailed insights compared to a single overall scaling curve.

### Weaknesses
1. This paper primarily focuses on the continuous Brier score as a metric, which may not fully capture the validity of the observed scaling trends. It is unclear whether these trends are specific to this single metric. To establish this phenomenon as more general, validation across other metrics is needed. Specifically, while the Brier score is useful for probabilistic predictions, it doesn't directly reflect the accuracy of the model's final choice, which is often the primary concern in multiple-choice tasks. The paper should explore metrics like top-1 accuracy, which directly measures the correctness of the model's selection, to see if the U-shaped and inverted-U scaling trends persist.

2. The writing and organization of this paper are difficult to follow. For instance, the scaling plots for various LLMs are presented without clearly specifying the types or model families used, as these details are only provided in the appendix. Additionally, the figure depicting the scaling curves lacks clarity; for example, the label '0_1502_brier' in Figure 3 is ambiguous. It appears to represent the index of data points, but using the difficulty level as a label would be more informative. The lack of clear labeling and the delayed introduction of model details make it hard to assess the generality of the findings. The main body of the paper should include a clear description of the models used and the specific difficulty levels being analyzed.

3. The proposed task in Section 4 is using data collected before the emergence threshold to forecast the occurrence of emergent abilities and the scaling trend beyond this threshold. However, the paper lacks details on how the threshold is selected and how this choice is validated. Furthermore, more explanation is needed to highlight the significance of this task. Why is predicting the scaling curve beyond the emergence threshold based on early performance trends important? The method for selecting the emergence threshold seems arbitrary, and the paper does not provide a clear justification for its choice. A more rigorous approach is needed, perhaps by analyzing the derivative of the scaling curve or using a statistical test to identify a significant change in the trend. The practical significance of predicting the scaling curve also needs to be better motivated; what specific benefits does this prediction offer beyond simply observing the curve?

4. In the experiments, a few multiple-choice datasets are utilized to demonstrate the presence of emergent behavior, but they also note that such behavior is absent in other BIG-Bench datasets, as detailed in the appendix. This raises questions about whether the observed emergence is specific to certain datasets rather than a general phenomenon. A more comprehensive analysis is needed to uncover broader patterns and clarify the characteristics of these emergent behaviors—for instance, identifying which types of tasks exhibit this emergence and which do not. This would help determine the conditions under which such emergence is applicable. The paper should investigate the characteristics of the datasets that show emergence versus those that do not. This could involve analyzing the complexity of the questions, the nature of the required reasoning, or other relevant dataset properties.

### Questions
1. The authors appear to categorize difficulty levels as easy, medium, and hard. How might the granularity of these difficulty levels affect the results?
2. In Section 4, the proposed method Slice-and-Sandwich first fits a function to the binary Brier score and then projects the forecasted scaling trend back to accuracy. I am trying to understand the benefit of this additional step. My interpretation is that fitting the binary Brier score curve is more precise, particularly for extrapolation, compared to directly fitting the accuracy curve. Could the authors elaborate on why this approach is preferred over fitting the accuracy curve directly?

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
By dividing questions according to difficulty levels, the authors observe U-shaped scaling for hard questions and inverted-U scaling for easy questions, followed by steady improvement. Then the authors propose a simple pipeline, called Slice-and-Sandwich, to predict the model performance.

### Strengths
1. The inverted-U vs. U-shape scaling seems interesting.

2. The pipeline seems to be novel. Although the basic principle of the method is fairly easy to understand, it substantially outperforms the baseline methods.

3. The experiments are diverse. The authors uses 56 LLMs to evaluate the difficulty levels, and the effectiveness of Slice-and-Sandwich is demonstrated on 6 benchmarks.

### Weaknesses
1. The fitted scaling trend is either underestimated or overestimated the actual scaling trend. Although the authors have given explanations, it should be clearly pointed out that why this  underestimation /  overestimation is acceptable. For example, the prediction error of the score of hard problems on Arithmetic benchmark (figure 7) seems actually comparable to the prediction error of the score of all problems on Arithmetic benchmark  (figure 9).

2. The authors provide possible explanations for the inverted-U vs. U-shape scaling. They provide examples of easy/hard problems and give very brief descriptions of the performance of different models. The concepts would be easier to understand if the authors can provide some specific outputs of weak/strong LLMs on easy/hard problems in the appendix. 

3. There are some typos in the paper. For example, in all figures, the authors use exactly the same color for the easiest and most difficult problems, making it a bit confusing. In line 484, $F_s^c$ should be $F_e^c$. Also, the layout of the appendix seems weird. For instance, P21 only contains a single huge image.

4. Perhaps the authors should use one sentence in the introduction section (line 53) to explain what is `binary brier score` to make it easier for readers to understand.

### Questions
1. I am interested in understanding why averaging the scaling trends of both the easy group and the hard group leads to an accurate prediction of the overall aggregate scaling trend. It's possible that with one prediction being overestimated and the other underestimated, the outcome appears to be coincidentally accurate. The author should provide further (possibly qualitative) explanation to demonstrate that the good result is not a matter of chance. If this question is resolved, I believe the soundness and contribution of the paper can be substantially improved.

2. The authors provide a separate figure for each benchmark. Would it be possible to also provide a figure that includes the results from all benchmarks?

### Soundness
3

### Presentation
2

### Contribution
3

# Pre-Memorization Train Accuracy Reliably Predicts Generalization in LLM Reasoning

- Decision: Reject
- Avg Score: 4.25
- Scores: 8, 3, 3, 3

## Abstract
When large language models (LLMs) are finetuned on reasoning tasks, they can either reduce their training loss by developing problem-solving abilities, or by simply memorizing target traces in the training data. Our work aims to better understand how this learning process shapes a model's ability to generalize. We observe that, while LLMs often perfectly memorize most target solution traces by the end of training, their predictions at intermediate checkpoints can provide valuable insights into their behavior at test time. Concretely, we introduce the concept of pre-memorization train accuracy: the accuracy of model samples for training queries prior to exactly reproducing reasoning traces in the training data. We find that the average pre-memorization train accuracy of the model is strongly predictive of its test performance, with coefficients of determination around or exceeding 0.9 across various models (Llama3-8B, Gemma2-9B), datasets (GSM8k, MATH), and training setups. Beyond this aggregate statistic, we find that the pre-memorization train accuracy of individual examples can predict the model’s sensitivity to input perturbations for those examples, allowing us to identify examples for which the model fails to learn robust solutions. A natural application of this insight is in data curation. We find that prioritizing the collection of examples with low pre-memorization accuracy leads to 1.5-2x data efficiency compared to i.i.d. data scaling, and outperforms other standard data curation techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how memorization impacts model generalization.  More precisely, the authors study how the pre memorization accuracy -- the accuracy before which an example is memorized by the model -- is particularly predictive of test performance.  The authors preform a series of experiments to quantify this phenomena, and show that it persists across different model scales and datasets.

### Strengths
Overall the experiments are convincing and the analysis is thorough.  The comparison to active learning metrics is particularly nice, although perhaps a slightly more principled set of metrics could have been chosen (e.g., an influence function that is a dot product of loss gradients).

### Weaknesses
There are no obvious weakness in the paper.   Some experiments would have been nice to see:
* in particular, having a more diverse set of model sizes would have been interesting.  Is the proposed metric still predictive for smaller models?  It seems that for small models, they may never end up memorizing the reasoning trace, and the notion of a pre-memorization accuracy does not exist.  Are there nevertheless proxy metrics available in those cases?  At what scale does the generalization emerge?
* It would be interesting to consider a more diverse set of active learning metrics.  For example, can influence functions be used to map examples to train data (as proposed in [1)?

### Questions
(see above)

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the problem-solving abilities and memorization processes of LLMs in the context of mathematical reasoning tasks. By introducing the concept of pre-memorization train accuracy, the authors establish a more effective metric for predicting the model's final test accuracy. This metric tends to serve as an indicator of training robustness and generalization capabilities. Additionally, it can be utilized to collect training data in a curriculum setting, resulting in a 1.5 to 2 times improvement in sample efficiency.

### Strengths
1. The paper highlights the discrepancy between training accuracy and test accuracy, as well as the impact of different training parameters (learning rate) on the training process, providing motivation for the methods proposed in the study.
2. The authors conduct experiments on Llama-3 8B and Gemma2 9B, aiming to demonstrate the generalizability of their method across different models.
3. The proposed method shows improvements in predicting test set accuracy and in curriculum learning scenarios compared to other baseline methods.

### Weaknesses
1. Many details are not adequately presented, such as the selection for the threshold $ p $ in pre-memorization train accuracy, as well as the contamination issues in the synthetic training data for Figure 6.
2. While the paper aims to investigate the model's generalization capabilities, all experiments utilize training and test sets from the same distribution, lacking out-of-distribution experiments.
3. In the experiments predicting testset accuracy, the comparisons with other methods are not entirely fair. The gradient variance and distance from initialization methods rely on significantly less input information during prediction, while the ATC method primarily focuses on OOD scenarios.
4. The premise of predicting model's generalization performance for other data distributions is that there is no labeled data to use from that distribution, which is also the setting for methods you compared, such as ATC. In your method, since the parameter $p$ needs to be fitted on the validation set, why not directly use the model's accuracy on this validation set to make predictions?  If we can already obtain the accuracy of the validation set, why we need to design a method to predict the test set accuracy through the training set accuracy?
5. In the curve of fitting performance changes with $p$ provided by the author, $R^2$ sometimes reaches quite low values (<0.4), making it difficult for me to judge when using average train accuracy only after the first epoch to predict the final test accuracy ($R^2$=0.5). Could the author also plot a similar curve of fitting performance changes with $p$ only after the first epoch to illustrate the importance of using multiple epochs?
6. For difficulty levels 4-5 in MATH: Given that elementary and middle school level math problems have almost been resolved, if the method cannot be proven to extend to more difficult problems, it will result in a loss of soundness.

### Questions
1. In L246-247, the authors mention that the value of $ p $ is dependent on the task and the pretrained model, but I could not find any explanation about the selection of $ p $ in the paper. How is the value of $ p $ determined, and is the correlation coefficient for predicting testset accuracy sensitive to this parameter?
2. The authors claim that this training set accuracy metric based on the training process is superior, but they lack necessary ablation studies. For instance, how would the prediction performance change if only the training set accuracy after the first epoch(rather than first m epochs) is used?
3. The experiments in Figure 5 utilize 6 epochs of training, and it is not surprising to reach such conclusions in a setting that is sufficiently overfitted. In practice, it is uncommon to choose such a high number of epochs. Can the same conclusions be drawn with a maximum of 3 epochs?
4. In L413, it is mentioned that the data collection methods used in the paper can be applied to human data. Given that there are already some large-scale open-source datasets available, could the experiments be repeated on these datasets (e.g., Numina-CoT) to verify the reproducibility of the results?
5. The experiments in Figure 6 are conducted on GSM8K and MATH at difficulty levels 1-3. Considering that these datasets are relatively easy, I am curious about the experimental results at difficulty levels 4-5 in MATH.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper seeks to understand generalisation in LLMs by introducing a metric that when applied to training examples correlate to test set performance for GSM8K and MATH. Moreover, this metric can used as proxy for example difficulty and in turn be used for curriculum learning and/or data curation.

### Strengths
The paper takes an interesting approach by using studying the CoT in GSM8K/MATH (traces as they call it) of a training example. 
By focusing on the variance of traces while maintaining the correct answer, the authors have a very nice definition of overfitting.

### Weaknesses
There are not enough details on how `p` is chosen.

By inspecting Figure 1, one could argue that the procedure of "calibrating" a `p` is simply selecting a sort of projection onto the `x=y` line which then causes the calibration of pre-memorisation train accuracy to be correlated the test accuracy. 

The different run curves w/ different learning rates are similar enough that calibrating `p` could simply cause the correlation to be high. 

Moreover, finding such `p`, we have created a list of examples which correlate high to the test set. This is a form of leakage. Specially if it needs to be calibrate for each model and task.

### Questions
* Can you elaborate further on what the impact of `p` calibration above?
* What is the impact of varying `p` on the metric value and correlation. Perhaps, would we show that we can calibrate `p` on a hold-out set of the training-set and the experiments still hold

It would be great to understand the impact of this.

### Soundness
1

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
This paper focuses on investigating how the learning process influences the reasoning ability of LLMs to generalize. Specifically, this paper introduces the concept of pre-memorization train accuracy, which is shown to have a positive correlation with test accuracy. The authors also leverage this concept to develop a novel data curation method. Extensive experiments validate the effectiveness of the proposed model compared with a set of baselines.

### Strengths
The proposed method itself is coherent and easy to follow. The authors conduct experiments on several benchmarks to validate the effectiveness of the proposed method.

### Weaknesses
1.	Overall, the motivation behind the paper is not clearly articulated. The authors introduce a new concept, termed per-memorization train accuracy, which is calculated by sampling from the model multiple times and averaging the correctness of the samples. In my view, this metric is almost equivalent to the difficulty level of the problems. When the model samples multiple times and fails to obtain correct answers, it indicates that the problem is difficult. Conversely, successful sampling suggests the problem is easier. Furthermore, the difficult level of problems is often provided in many datasets, such as MATH. The authors should discuss this straightforward metric in the main text and include comparisons in the experiments.
2.	The paper provides insufficient explanation of why the proposed metric is expected to correlate positively with test accuracy. Additionally, it lacks theoretical justification to support the effectiveness of the proposed data curation method.
3.	The authors employ only two LLMs in their experiments. To strengthen the evaluation, recently proposed dense LLMs, such as Mistral and Qwen, as well as sparse Mixture-of-Experts (MOE) models like Mixtral and DeepSeekMOE, should be included as the backbone models for comparation.
4.	Reasoning is a general ability for complex problem-solving. Beyond mathematical reasoning, there are many other important reasoning tasks, such as logical reasoning, commonsense reasoning. To comprehensively evaluate the effectiveness of the proposed method, the authors should conduct experiments on logical reasoning tasks (such as LogiQA) and commonsense reasoning tasks (such as HellaSwag and Winogrande).

### Questions
1.	Could you involve a broader range of LLMs, encompassing both dense LLMs and sparse MOE models, to provide a more comprehensive demonstration of the proposed method’s effectiveness? 
2.	Could you involve a wider variety of reasoning task to offer a more holistic demonstration of the proposed method’s effectiveness?

### Soundness
2

### Presentation
2

### Contribution
2

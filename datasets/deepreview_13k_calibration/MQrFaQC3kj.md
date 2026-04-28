# Dataset Fairness: Achievable Fairness On Your Data With Utility Guarantees

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
In machine learning fairness, training models which minimize disparity across different sensitive groups often leads to diminished accuracy, a phenomenon known as the fairness-accuracy trade-off. The severity of this trade-off fundamentally depends on dataset characteristics such as dataset imbalances or biases, and therefore using a universal fairness requirement across datasets remains questionable and can often lead to models with varying and substantially low utility. To address this, we present a computationally efficient approach to approximate the fairness-accuracy trade-off curve tailored to individual datasets, backed by rigorous statistical guarantees. By utilizing the You-Only-Train-Once (YOTO) framework, our approach mitigates the computational burden of having to train multiple models when approximating the trade-off curve. Moreover, we introduce confidence intervals around this curve, offering a statistically grounded perspective on acceptable range of fairness violations for any given accuracy threshold. Our empirical evaluation which includes applications to tabular data, computer vision and natural language datasets, underscores that our approach can guide practitioners in accuracy-constrained fairness decisions across various data modalities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Fairness-accuracy trade-off widely exists in machine learning models and fundamentally depends on dataset characteristics. Such dataset-dependent property impedes chasing universal fairness requirement across datasets. To this end, this paper proposes a computationally efficient approach to approximate the trade-off curve with statistical guarantees via adopting YOTO framework. The empirical results provide the guidelines in accuracy-constrained fairness decisions for various data modalities.

### Strengths
1.	The research problem on the fairness-accuracy trade-off is fundamental and important in machine learning fairness community.
2.	This paper is overall well-written and easy to follow.
3.	Due the unknown Pareto frontier of trade-off, the investigation of trade-off with confidence interval with statistical guarantee makes much sense to me.

### Weaknesses
1.  Motivation. Can the authors elaborate on the motivation for using a universe fairness requirement across datasets? What are the advantages of doing this?  
2.  Technique novelty. This paper introduces a computationally efficient method for estimating the trade-off. However, from my understanding, the efficiency part directly adopts YOTO framework and the confidence interval estimation only involves trivial bounds.  
3.  Pareto frontier. The achievable trade-off by YOTO may not be consistent with the ground-truth Pareto optimum. It seems that this paper is over-claimed since the true Pareto trade-off investigation is not touched. Additionally, how do you use a universe fairness requirement across datasets? The approximated trade-off seems not be a good choice since the gap between achievable trade-off by YOTO and ground-truth Pareto optimum may also be dataset-dependent. 
4.  Experiments. (a) The evaluation of the confidence interval is vague. It seems that the conservative estimation is never penalized by the current results, such as Figures 3 and 4. Which confidence interval estimation method is better? (b) In Section 3.1, the author mentioned $\lambda$ in Eq. (2) offers litter control over the accuracy, which is counter-intuitive for such regularization. Can you provide experimental results to further support this statement? (c) Is it possible to create a synthetic dataset with a known ground-truth trade-off in the experiments? Otherwise, many conclusions can only hold for the achievable trade-off by YOTO. (d) There are confidence intervals for both accuracy and fairness. How can you plot these two intervals in Figures 3 and 4? 
5.  From my understanding, the optimization for fairness with accuracy and the optimization for accuracy with fairness constraint have the same trade-off. I am curiosu why the authors select the former one and highlight the difference in the first paragraph of section 2.1.

### Questions
Please see weakness part.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a methodology to estimate the optimal fairness-accuracy trade-off curve for a given dataset and model class. The key ideas of the proposed method are two steps::


1. Use the You-Only-Train-Once (YOTO) framework to estimate the trade-off curve by training a single model. 
2. Use the YOTO result to construct confidence intervals around the estimated trade-off curve using a held-out calibration dataset. 


The claimed contributions of this paper are:
1. develop a method to calculate a range of allowed fairness violations for a given dataset and desired model accuracy. 
2. Construct confidence intervals that statistically guarantee the optimal fairness-accuracy tradeoff curve.
3. Test the proposed method when sensitive attributes are scarce in the data.
4. Test the proposed method on different types of data. The intervals contained the tradeoff curves from state-of-the-art fairness methods like regularization and adversarial learning.

### Strengths
1. The confidence intervals of fairness seem needed in the fairness domain., however, it has problems.
2. The paper is clearly written and easy to follow. The graphics effectively illustrate the key ideas.

### Weaknesses
1. The statement "For a given dataset, model class, and accuracy, the permissible range of fairness violation is x to y." in this paper is problematic. Accuracy and fairness have an inherent connection (they exhibit trade-offs) and will influence each other. So accuracy cannot be the condition for the range of fairness violation. The paper's framing suggests that one can arbitrarily fix an accuracy level and then explore a range of fairness violations, which is not how these trade-offs manifest in practice. The achievable fairness is fundamentally limited by the chosen accuracy, and vice-versa. It is more accurate to say that for a given model class and dataset, there exists a Pareto frontier of achievable accuracy-fairness pairs, and the proposed method should be evaluated in terms of how well it estimates this frontier, not a range of fairness values conditioned on a fixed accuracy.
2. How to evaluate whether the confidence interval is rational or correct? This does not seem to have ground truth for this and only visually evaluating figure 4 is not enough. There is a strong assumption that the curve learned with YOTO is the ground truth, this is not reasonable and even wrong. This strong but possibly wrong assumption is only mentioned in "In other words, under the assumption of large enough model capacity, training the loss-conditional YOTO model performs as well as the separately trained models while only requiring a single model." (Page 4). I strongly recommend treating this seriously. The paper needs to justify why the YOTO curve should be considered a reliable proxy for the true optimal trade-off curve. Without a formal justification or empirical evidence beyond visual inspection, the confidence intervals lack a solid foundation.
3. The changeable fairness-accuracy trade-offs using one model may incur ethical issues, such as generating biased outcomes for certain groups of people. Based on this, I think this paper needs further ethical review.
4. The $\mathcal{L}_{fair}$ in Eq (2) is not presented at all. This paper should present the smooth relaxation of demographic parity. The lack of a concrete definition for $\mathcal{L}_{fair}$ makes it difficult to assess the practical implications of the proposed method. The specific form of the relaxation, including any hyperparameters, can significantly impact the resulting trade-off curve, and this information is crucial for reproducibility and comparison with other methods.
5. What is the meaning of "Dataset Fairness" in the title? It seems this title is not suitable for the proposed method. The title is too broad and does not accurately reflect the paper's focus on estimating the fairness-accuracy trade-off curve. A more precise title would better communicate the paper's contribution.
6. The experimental evaluation is not convincing to me. Since the Adult data is super imbalanced and the COMPAS data is small. I would suggest adding more experiments to really evaluate the proposed method, such as on the folktable dataset at https://github.com/socialfoundations/folktables

### Questions
Please address my concerns in the Weakness part.

----
----**After rebuttal**---

I thank the authors for their response and am sorry for the late response.  The authors' response addresses part of my concerns. But 
1. The new explanation that "the lower confidence intervals presented in Proposition 3.4 depend on the gap between the YOTO achieved trade-off curve and the ground-truth trade-off curve" is essentially making a strong assumption that the YOTO should be good enough, although not group truth. I do not think this point is reasonable and grounded. 
2. The evaluation based on such small tabular data is not convincing to me, without new results presented. 

Based on the above and my original comments, I would maintain my original score.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to estimate the accuracy-fairness trade-off curve given the dataset and model class. It first uses an existing method, You-Only-Train-Once (YOTO), to get the trade-off curve efficiently without training multiple models. It then proposes a way to obtain the confidence intervals.

### Strengths
The accuracy-fairness curve is widely used in the algorithmic fairness community. How to set a range of achievable fairness violations is a practical problem. The method proposed in this paper provides us with an efficient solution for estimating the curve with two-sided confidence intervals.

### Weaknesses
1. The method is highly based on an existing method, YOTO. Although it doesn't need to train multiple models, the cost of YOTO is not discussed in this paper.
2. The accuracy-fairness curve is algorithm-agnostic. Figure 4 shows that the estimated curve has more errors when using some particular algorithmic fairness methods. However, people tend to use some algorithmic fairness methods to train the model. In that case, the practical use of the curve is concerned. 
3. The method requires an in-distribution calibration dataset and only applies to in-distribution tests.

### Questions
1. What is the L_fair in equation (2)?
2. What are the costs and limitations of YOTO?
3. Can we extend the method to be algorithm-sensitive? For example, suppose we know what algorithmic fairness method to use, can we estimate the curve for that algorithm?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

# Making Predictors More Reliable with Selective Recalibration

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
A reliable deep learning system should be able to accurately express its confidence with respect to its predictions, a quality known as calibration.
One of the most effective ways to produce reliable confidence estimates with a pre-trained model is by applying a post-hoc recalibration method.
Popular recalibration methods like temperature scaling are typically fit on a small amount of data and work in the model's output space, as opposed to the more expressive feature embedding space, and thus usually have only one or a handful of parameters.
However, the target distribution to which they are applied is often complex and difficult to fit well with such a function.
To this end we propose \textit{selective recalibration}, where a selection model learns to reject some user-chosen proportion of the data in order to allow the recalibrator to focus on regions of the input space that can be well-captured by such a model.
We provide theoretical analysis to motivate our algorithm, and test our method through comprehensive experiments on difficult medical imaging and zero-shot classification tasks.  Our results show that selective recalibration consistently leads to significantly lower calibration error than a wide range of selection and recalibration baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission proposes selective recalibration, which combines ideas from selective classification with calibration. The proposed method builds on work by Fisch et al. (2022) by optimizing rejection and calibration jointly. Experiments show that this yields better calibration for a given level of coverage than standard out-of-distribution detection methods applied separately to standard calibration methods. It also performs better in most cases than the "sequential" alternative to the joint optimization approach. Performance is evaluated for both i.i.d. settings and settings where an existing pretrained model is used in a new domain, without fine-tuning this model, by performing selective recalibration. There are also some theoretical results for a particular synthetic domain showing that better performance can be achieved with joint optimization.

### Strengths
The proposed approach makes sense, and it is plausible that joint optimization performs better than the alternatives considered.

### Weaknesses
One important baseline that is missing in the experiments is a calibration approach that is as complex as the multi-layer perceptron used in the proposed approach to perform selection. Platt scaling and temperature scaling, the calibration methods used in the experiments, have very few parameters, and discretization-based approaches are also very simple. The argument in the submission is that selective calibration can be beneficial because it may not be possible to achieve good fit for the calibration model to the entire data. However, an obvious approach to tackle this problem is to simply make the calibration model more complex: rather than using a linear logistic regression model as in Platt scaling, one can use a multi-layer perceptron with non-linear activation functions instead. This would allow the calibration model to capture more complex relationships in the data and potentially achieve better calibration without the need for selective methods.

I am also wondering about the sequential baseline used. A single epoch of calibration is performed before the selection model is trained. It is unclear why a single epoch is used. Also, it seems that improved performance could trivially be obtained by recalibrating again after the selection model has been trained. (This could be iterated, but that would probably be very similar to joint optimisation using gradient descent.) The current sequential approach seems arbitrarily designed and does not represent a strong baseline for comparison. A more thorough investigation of sequential calibration strategies is needed, including exploring multiple epochs of calibration and iterative recalibration.

No significance testing is performed and no confidence intervals are provided for estimated performance measures. This makes it difficult to assess the statistical significance of the reported improvements. The lack of uncertainty quantification also limits the practical applicability of the results, as it is unclear how much the performance might vary across different runs or datasets. The results should include statistical tests and confidence intervals to provide a more robust evaluation.

The first result in Section C.2 is disturbing: classification accuracy goes down with decreased coverage when applying the proposed method. It is unclear to me whether one would ever accept this in practical applications. This behavior suggests that the selection mechanism is not effectively identifying the instances where the model is most likely to be accurate, which is a significant concern. It raises questions about the practical utility of the proposed method if it leads to a decrease in accuracy when coverage is reduced.

Other comments and typos:

"whether an instance is correctly classifier"

"outputs, We"

Section B.2.1: what is $\tilde f$?

Section B.4.2 does not mention validation data.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper extends the selective calibration setting of Fisch et. al. (2022) to allow for joint training of both selection _and_ recalibration functions. Reliable confidence estimation is a key property for predictors operating in sensitive domains, but is not typically easy to achieve. Selective calibration combines "selective prediction" (i.e., allowing for abstention) with "calibration", in the sense that selectively calibrated predictors prioritize having calibrated predictions on the non-rejected population of inputs. Previous work by Fisch et. al. (2022) only considered optimizing the "selection" part given a fixed model. This paper follows the natural motivation of also training a recalibrator jointly, which is similar to previous work in standard selective classification such as SelectiveNet (Geifman and El-Yaniv, 2019). It is intuitive to see why such an approach would be a good idea for some input distributions and models (e.g., where the optimal calibrator across the full input space is not in the sigmoid family for Platt scaling, but is after selection). The authors also provide empirical and additional theoretical analysis by example that supports their joint design.

[1] Calibrated Selective Classification. Adam Fisch, Tommi Jaakkola, Regina Barzilay. 2022.

[2] SelectiveNet: A Deep Neural Network with an Integrated Reject Option. Yonatan Geifman, Ran El-Yaniv. 2019.

### Strengths
The paper is well written and its proposed method is well-motivated. Though it is a fairly straightforward extension of prior work (Fisch et. al. + Geifman and El-Yaniv), it also presents additional contribution in the form of a simplified selective calibration loss (S-TLBCE) which appears to work better in practice. The empirical and theoretical arguments for justifying joint vs. sequential training of $(g, h)$ is also useful.

### Weaknesses
I think that the paper does a good job at addressing the narrow question of improving selective calibration through joint selection _and_ recalibration. More broadly, I would have been excited to see a more nuanced approach to selective calibration (which Fisch et. al. also misses), in the sense that not all types of calibration error are necessarily equal. For example, under a selective recalibration framework, all of the following example rejections would be preferred (assuming that they don't have any other structure that makes recalibration easier post selection):

- reject(Predictions with confidence 95% but accuracy 90%) > reject(predictions with confidence 4% but accuracy 0%)
- reject(Predictions with confidence 80% but accuracy 100%) > reject(predictions with confidence 80% but accuracy 61%)

Obviously it depends on the application, but generally speaking it seems that rejecting the top-performing half of predictions simply because their confidences are slightly too high is not a useful strategy. Similarly for under- vs. over-confidence. Considering other calibration objectives (e.g., Decision Calibration from Zhao et. al., 2021) that are more expressive than ECE-1/ECE-2 could add significantly to this work's potential impact. 

I'm also a bit worried about the data requirement for selective recalibration to work. If labeled examples from the target domain are not available (e.g., following the setting of Fisch et. al.), can the method still produce reliable rejections? Does recalibration on the training domain help here?

Minor formatting points:
- It would be helpful to keep equation numbering for all display equations.
- Unnumbered equation for $h^\mathrm{Temp}$ would benefit from \left \right parentheses.

### Questions
- Figure 1 is a bit confusing to me. It's not easy to see what strategy the selective and selective recalibration algorithms take. The caption could use some additional clarification. For example, what is the desired coverage level? It seems like the basic strategy that is followed is to reject either the blue or the green (selective vs. selective recalibration, respectively). Though I would still expect a selective only approach to reject the mid-confidence blue examples disproportionately more than the upper/lower ranges (since this is where calibration error is highest per the reliability diagram).

- It makes sense that jointly learning selection and recalibration can help when the calibration error is too complex to be fit by the family of recalibration functions specified by Platt or temperature scaling. I'd be curious to see how this would compare to simply fitting a slightly more expressive family of calibrators (e.g., 2-layer NN), especially for data without distribution shifts.

- This is more of a half-baked suggestion than a question, but I'm curious if the authors ever experimented with the following setup. Suppose we modeled recalibration as a hard mixture of experts, where $h(x) = \sum_{i = 1}^{n} g_i(x) h_i(x)$ with $g(x)$ being 1-hot. On new distributions $p(x')$, one could "turn off" the lowest performing $g_i$ via rejection until $\sum_{i \in \text{rejected}} \mathbb{E}(g_i(x')) = \beta$. This is a generalization of the current setup with $g(x)$ being binary, and only training one $h(x)$ (as the other examples are discarded). On new distributions, however, dynamically reconfiguring this mixture (which will have been trained to fit subdomains in the training data) could prove to be effective, without the need for much new data to jointly recalibrate $h$.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to combine selective prediction and post-hoc calibration to achieve more reliable performance for classification tasks. The proposed optimization framework is based on another recent work which combines selective prediction and training-time calibration. In the proposed selective recalibration framework, a new loss function, Selective Top-Label Binary Cross Entropy (S-TLBCE) is proposed for training such a recalibrator and a selective model at the same time. The proposed approach is evaluated on real-world medical diagnosis datasets and image classification datasets, and the results show its effectiveness.

### Strengths
1. The idea of combining selective prediction and model calibration is very useful and realistic in many safety aware tasks. Also, previous work studied the combination of selective prediction and train-time calibration, the combination of selective prediction and recalibration seems more important as post-hoc calibration achieves better calibration performance generally.

2. Except for the experiments on real-world datasets, the authors also give theoretic results based on a simple and intuitive data generation model.

### Weaknesses
1. The technical novelty and overall contribution is quite limited, primarily because the combination of selective prediction and model calibration has been studied in previous work and the proposed method is a straightforward combination of existing optimization framework and recalibration model. 

2. The writing and organization of this paper are not good enough. Many places involving notations are confusing, for example, some loss functions appear in the Methodology section but are not used in the following optimization framework, and some notations are not defined before their first appearance.

3. The empirical evaluation is also limited, as a result, the effectiveness and soundness cannot be sufficiently shown. For example, some benchmark datasets for image classification, which are commonly used in the context of model calibration like SVHN/CIFAR-10, are not used in experiment section. Moreover, the experimental part does not provide sufficient information about the dataset used and the way it was divided (for training and validation), as well as the model structure.

### Questions
Please refer to the weaknesses section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an extension to a recent line of work on calibrated selective classification (Fisch et al., 2022), which consists of selectively predicting inputs so as to minimize calibration error. The authors' method jointly optimizes a selection function along with a recalibration model, so as to minimize calibration error on the selected subset of the data. They show that this approach can significantly outperform doing only selective prediction, and also show that it can outperform selection and recalibration done in sequence.

### Strengths
- **Originality:** The paper introduces an objective that combines selective classification and recalibration (S-TLBCE, Equation 8) and proves for a simple class of data distributions that the joint procedure can outperform each individual procedure. While the objective and analysis seem new, the practical advancement of this work is a straightforward extension of [1].
- **Quality:** Overall the quality of the work is good, with the problem of selective calibration being well-described/well-motivated and experiments designed appropriately to evaluate the proposed method.
- **Clarity:** The work is easy to follow, with the experiments and theory described with adequate detail for the most part.
- **Significance:** Selective classification optimizing for calibration is relatively new, being (to the best of my knowledge) largely introduced in the recent (2022) work of [1]. This paper constitutes a natural extension of [1], and while the empirical results correspond to marked improvements in some regimes, I have some reservations regarding the overall contribution of the work in the context of [1].

[1] https://arxiv.org/abs/2208.12084

### Weaknesses
## Weaknesses
1. **Novelty/improvement of proposed approach.** The approach is conceptually a minor change to the methodology of [1]. While S-TLBCE seems like a new objective in this context, it does not perform better (in fact it even performs worse on ImageNet) than the jointly optimized version of S-MMCE from [1], except for the OOD tests on CIFAR-100-C. Furthermore, the table describing these latter experiments (Table 1) is unclear - the description claims to be reporting AUC over various coverage levels but only ECE-1 and ECE-2 are reported? Also, the naive confidence-based rejection strategy (which should be described in the main paper) performs very well on the ImageNet/Camelyon17 experiments - the authors say that this strategy falls apart in the OOD case, but is this considering confidence-based rejection with recalibration (in sequence)? 


### Questions
- Several questions are stated in weaknesses above.
- Figure 1 is difficult to understand. What subsets of the data do the blue and green curves correspond to? Shouldn't there only be one curve for 1(a) and 1(b) since no selection is being done for these? 
- The definition of R-ECE seems a bit strange to me; linearly rescaling the predicted *probabilities* by $T$ will not be the same as rescaling the predicted scores, so this is not exactly temperature scaling.
- The ECE calculations in the appendix are hard to follow due to the presentation, improving spacing/detail would help here.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

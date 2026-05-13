# DOTA: Distributional Test-Time Adaptation of Vision-Language Models

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
\textcolor{blue}{Vision-language foundation models (e.g., CLIP) have shown remarkable performance across a wide range of tasks. However, deploying these models may be challenging and unreliable when significant distribution gaps exist between the training and test data. The training-free test-time dynamic adapter (TDA) is a promising approach to address this issue by storing representative test samples to guide the classification of subsequent ones. However, TDA only red naively maintains a limited number of reference samples in the cache, leading to severe test-time catastrophic forgetting when the cache is updated by dropping samples. In this paper, we propose a simple yet effective method for  Test-time Continual Adaptation (\cta). Instead of naively memorizing representative test samples, \cta continually estimates the distributions of test samples, allowing the model to adapt to the deployment environment. The test-time posterior probabilities are then computed using the estimated distributions based on Bayes' theorem for adaptation purposes. To further enhance the adaptability on the uncertain samples, we introduce a new human-machine collaboration paradigm which identifies uncertain samples, collects human-feedback, and incorporates it into the \cta framework. Extensive experiments validate that \cta enables CLIP to continually learn, resulting in a significant improvement compared to current state-of-the-art methods.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors address the problem of Test Time Adaptation of Vision Langugage models. They propose to continuously estimate the distribution of test samples, which they leverage through Bayes theorem, to make the final test predictions. They also collect human feedback to receive supervision for uncertain samples.

### Strengths
- They propose to estimate the class distributions in an online manner. 
- The adaptive fusion of zero shot text classifier based predictions and the distribution based feature similarities is simple and intuitive. 
- This being a backpropogation free approach, is very light-weight computationally, which is a great advantage for TTA.
- The paper is well written and easy to follow, however several clarifications are required.

### Weaknesses
 1. **Distributional Test Time Adaptation:** In a single image TTA setting, the whole section 3.2 is quite unclear. There is no **batch** of samples in this setting. So, how are the class distributions actually updated at each time step. Specifically, how are the mean and covariance matrices updated with a batch size of one? The paper needs to clarify if the method stores feature embeddings of past samples to compute these statistics, or if it uses an online update rule, and if so, what is the exact update equation for the mean and covariance with a single sample. Furthermore, the paper needs to clarify how the class-specific distributions are handled. Are separate distributions maintained for each class, or is a single global distribution estimated and then conditioned on the class? 

2. **Samples for distribution estimation:** Are all test samples used for updating the class distributions? Wouldn't the use of low confident/uncertain samples lead to bad parameter estimates in eqn(4)? The paper should clarify if there is any weighting or filtering of samples when updating the distribution parameters. If all samples are used, the authors need to justify why low-confidence samples do not negatively impact the distribution estimation, and if not, what is the criteria for selecting samples for distribution updates.

3. **TTA with human feedback:** While this is one of the major contribution of the paper, it appears to only result in modest improvements. 5% and 15% is a lot of data to ask labels for, from a human. However, the results improve only of the order of 1-2%. This makes the efficiency of this whole process questionable. The paper needs to provide a more thorough analysis of the cost-benefit trade-off of human feedback, and explore methods to reduce the amount of human supervision required for effective adaptation.

4. **Performance evaluation of TTA with human feedback:** As the test samples arrive in an online manner and based on uncertainty, how is the final accuracy evaluated here? Are these samples inclusive when evaluating accuracy? If so, you should be using the ground truth as predictions for actively labeled samples. Then the accuracy should be up by about 5% or 15%. As this is not the case in the results reported, are the labeled samples excluded from evaluation? This needs to be clarified. For fair comparison, all results should be reported on the complete test set, even when using human feedback. The paper needs to clearly define the evaluation protocol and justify why the reported accuracy is not inflated by the use of human-provided labels.

5. **Need stronger baselines for TTA with human feedback:** To study the role of TTA with human feedback, stronger baselines need to be established, using different selection strategies, like random, confidence, entropy etc. and report the accuracy of complete test set. As all strategies have same amount of labeled samples included, the performance improvement due these strategies as well as the gains wrt no human feedback can be assessed. The paper needs to compare the proposed method against a wider range of active learning baselines, and show that the proposed method is superior to these baselines in terms of both accuracy and the amount of human feedback required.

6. **Amount of human feedback:** 5% and 15% is a lot of supervision and this may not be feasible during test time. It's more practical to ask labels for about 1-2% of test data. Experiments with stronger baselines, with lesser supervision, with correct evaluation method, is required to actually understand and evaluate the role of human feedback in TTA. The paper should explore the performance of the proposed method with lower amounts of human feedback, and compare it against other methods under the same constraints. The paper also needs to justify the choice of 5% and 15% feedback rates, and explain why these rates are practical in real-world scenarios.

7. **Choice of hyperparameters:**
In Implementation details, it is mentioned that validation sets are used to choose the hyperparameters. However, in TTA, one does not have access to any data from the test distribution apriori. Hence, validation data is not accessible in practice. Well, if one had access to validation data for test data, it provides a lot more information and could be used for more than just hyperparameter tuning. The paper needs to clarify how the hyperparameters are chosen in a realistic TTA setting where no validation data from the target distribution is available. The paper should also analyze the sensitivity of the method to the choice of hyperparameters, and provide guidelines for selecting appropriate values for these parameters.

### Questions
1. **Test Distribution Estimation:** In line 212 and from equations (4) and (6), it is described such that a batch of test samples arrive at each time step. However, prior baselines TPT, TDA perform single image TTA. Further, in Implementation details, in line 706, it is mentioned batch size is 1. Please clarify if single image TTA is done here as well, for fair comparison. If so, what does $n$ refer to in equations (5) and (6). How are $\mu_k$ and $\sigma_k$ estimated in single image TTA. Are you storing features, as done in TTA as well, along with the statistics?

2. **Selection of uncertain samples:**
Confidence is softmax applied over the similarity scores only right? Why is there such a large discrepancy using these two similar metrics (Table 7)? Also, is this similarity and confidence estimated from zero shot classifier or the classifier proposed? And why'd you choose what you choose?

3. **Sensitivity to hyperparameters:** How sensitive is the method on the choice of the parameters $\sigma, \eta, \rho$, as it's not practical to assume access to validation data before actually doing TTA? 

4. **Human in the loop TTA:** Please refer to the weaknesses and address the relevant concerns raised.

### Soundness
2

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
5

### Summary
The author presents DOTA, a method that adapts to deployment conditions by continually estimating test sample distributions rather than memorizing them. Using Bayes’ theorem, Dota computes posterior probabilities for real-time adaptation. A human-in-the-loop feature also gathers feedback on uncertain samples, enhancing adaptability. Experiments show Dota outperforms current methods with continuous test-time learning.

### Strengths
1. This paper is well written and easy to follow.
2. The idea is interesting,  the motivation of this paper is clear as well as the novelty of the method.
3. The proposed method is extensively tested against prior work and outperforms on a variety of tasks/baselines.

### Weaknesses
1. This paper does not include a detailed case study focused on a particular domain or a challenging dataset.
2. This paper does not include experiments assessing the model's sensitivity to hyperparameters. A detailed analysis of hyperparameter tuning could offer valuable insights into the robustness and generalizability of the proposed approach.
3. The paper could benefit from additional visualizations illustrating Test-time adaption with human feedback

### Questions
1. This paper is novel and interesting; would you consider making the code open source?
2. In Table 1, for ResNet-50, DOTA’s performance is only slightly better than TDA, with an average improvement of just 0.15%. I would like to understand the reason for this marginal gain.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The article addresses the problem of test-time adaptation of vision-language models. Differently from previous works (e.g., TDA, Karmanov et al. 2024) that use a cache to store samples, the proposed method, DOTA, stores an online estimate of the statistics (mean and variance) of each class of interest.  These statistics are then used during inference to refine standard CLIP predictions.  An active learning strategy exploiting this statistic is also proposed to improve the performance of the model further, asking a user to annotate the least confident examples. Experiments on a wide range of tasks show the efficacy of this approach.

### Strengths
1. DOTA revisits principles in the literature on continual learning via nearest class mean classifiers (e.g., [a,b]) for improving the performance of VLMs at test time. Overall the approach is easy to implement and can be considered a valid baseline for future works, performing continuous TTA without the need for storing a cache, as in TDA.

2. The article is well-structured and easy to follow, guiding the reader through all the design choices. 

3. DOTA is effective (as shown in the comparisons with TDA, e.g., Tab. 1 and Tab. 2) and computationally cheap (as shown in Tab. 3). 

4. Fig. 3 provides an analysis of how the performance of the two models (TDA and DOTA) vary w.r.t. the number of samples, showing the advantages of the latter.

**References**:

[a] Mensink, Thomas, et al. "Distance-based image classification: Generalizing to new classes at near-zero cost." IEEE transactions on pattern analysis and machine intelligence 35.11 (2013): 2624-2637.

[b] Bendale, Abhijit, and Terrance Boult. "Towards open world recognition." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015.

### Weaknesses
 1. DOTA continually updates its estimates of the statistics. Those might be affected by various factors linked to the experimental protocol, (e.g., order of the classes in the stream, batch size) as well as hyperparameters choice (i.e., the initial variance value, the shrinkage $\epsilon$, $\lambda$'s hyperparameters). Currently, the article does not provide too many insights on these factors, with the analysis mostly limited to the active learning percentile (i.e., Fig. 3). To assess the robustness of the model and provide a thorough study of its performance, it would be interesting to show results across multiple data ordering (i.e., currently it is not clear how many orders have been tested) and whether the performance changes w.r.t. the particular stream considered, even on the edge-cases where the data is non-i.i.d. [c]. Moreover, the hyperparameters may impact the speed of adaptation (e.g., variance initialization, $epsilon$) as well as how much the pretrained model is considered (e.g., $\lambda$s): studying their impact is essential to fully evaluate the complexity of the approach and potential difficulties in applying it on real-world scenarios. 

2. While TPT and DiffTPT are strong models for test-time adaptation, they work on the episodic setting, i.e., where adaptation is held out on a single sample, and then the model is reset to its previous state. The possibility of storing/using test-time data (assuming coherence in the sequence) is a non-negligible advantage that DOTA has (and that it shares with TDA). This makes both the "continual adaptation" mark on TPT (Tables 1 and 2) potentially misleading, as well as TDA the only true baseline acting under the same priors of DOTA. To make the results stronger, it would be beneficial to add more baselines, such as DMN [d]. 

3. Following on the previous points, adapting to an evolving stream is a much more nuanced problem, where correlation between consecutive data may play an important role. Thus, various TTA settings with different types of stream and data dependencies (e.g., practical TTA [e], universal TTA [f]) could have been considered to further show the effectiveness of the approach. 

4. A key motivation behind DOTA relies on the test-time forgetting of TDA (lines 52-56). However, there are no experiments demonstrating this point (beyond the quantitative advantages of DOTA). An analysis clearly showing this phenomenon (and how DOTA is more robust to it) would strengthen the motivation behind the approach. 

5. The active learning strategy proposed to refine the performance for uncertain samples (Section 3.3) is a nice addition to make the approach more coherent but it lacks competitors. For instance, also TDA could employ a similar strategy (as the update of the cache is based on the confidence of the predictions). Moreover: (i) the accuracy with random feedback is also very close to those achieved with the proposed strategy (e.g., 0.6% gap on average in Tab. 6, 5% percentile); (ii) for the confidence-based scoring to work, the model is assumed to be calibrated, something not always true and that needs a proper discussion [g]; (iii) in Tab. 7 the accuracy of the random baseline is not reported: this is an important reference to put results into perspective.  

6. Related work (Section 2) provides a limited discussion on the various types of TTA settings (e.g., [e,f]) as well as on previous methods employing online updates of statistics for continual learning/open world recognition [b] or prototype-based few-shot learning [I,j]. Expanding the discussion would help to better contextualize the work in the current literature.

**Minors**: 

- Footnote 1 hints that the model could be applied beyond CLIP. However, there are no experiments confirming this claim. It would have been more thorough to show other models (e.g., SigLIP [h]) to support it.

- Table 4 shows the results only for DOTA. It would be interesting to see the same analysis for the other baselines (e.g., TDA) to contextualize/provide a reference for the results.

### Questions
1. How does the performance change w.r.t. the data stream?
2. What is the impact of the various hyper parameter?
3. How does the test-time forgetting phenomenon happen?
4. How does the model compare with other baselines, e.g., DMN?
5. How does the work relate to existing ones on prototypical networks and the various TTA settings?

### Soundness
2

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
4

### Summary
The authors propose a Distributional Test-time Adaptation (DOTA) method, which adapt the pretrained Vision-language foundation models (e.g., CLIP) to the test target domain by estimating the distributions of different categories for test samples continually. The authors further introduce a human feedback collaboration method which identifies uncertain samples to further enhance the adaptability. Extensive experiments on diverse datasets validate the effectiveness of the proposed method.

### Strengths
1. The writing and figures are good and easy to understand.

2. The DistributiOnal Test-time Adaptation (DOTA) method for Vision-language foundation models without BP is simple yet effective during testing in new target domain, achieving a significant improvement compared to current state-of-the-art methods in most of the datasets.

3. This paper first define the test-time adaptation problem with human feedback, allows the test-time adaptation for uncertain samples with human feedback.

4. An adaptive final fusion probability is introduced to mitigate the potential negative impact when the number of test samples is insufficient.

### Weaknesses
1. The proposed method estimate the data distribution of samples in the current test environment during testing, but there lack some evidence or visualization. Why updating the feature distribution for different categories works better?

2. The DOTA method seems somewhat similar to the T3A method [R1], which continually maintains a memory bank for prototypes during the testing stage. Could the authors clarify and analysis the difference and the advantages of the proposed method?

[R1] Test-Time Classifier Adjustment Module for Model-Agnostic Domain Generalization

3. The proposed method seems works for not only VLMs but also other models in all classification tasks. Is it suitable for traditional TTA or Domain Generalization tasks?

4. There could give more details and explanation about the $f_k(x)$ in Eq.(3).

5. The uncertainty estimation method is simple. Is there any other uncertainty estimation method (like entropy) better?

6. There missing an ablation study for the adaptive fusion probability.

### Questions
see the Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

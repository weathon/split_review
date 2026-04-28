# Can We Predict Performance of Large Models across Vision-Language Tasks?

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 6, 3

## Abstract
Evaluating large vision-language models (LVLMs) is very expensive, due to the high computational costs and the wide variety of tasks. The good news is that if we already have some observed performance scores, we may be able to infer unknown ones. In this study, we propose a new framework for predicting unknown performance scores based on observed ones from other LVLMs or tasks. We first formulate the performance prediction as a matrix completion task. Specifically, we construct a sparse performance matrix $\boldsymbol{R}$, where each entry $R_{mn}$ represents the performance score of the $m$-th model on the $n$-th dataset. By applying probabilistic matrix factorization (PMF) with Markov chain Monte Carlo (MCMC), we can complete the performance matrix, that is, predict unknown scores. Additionally, we estimate the uncertainty of performance prediction based on MCMC. Practitioners can evaluate their models on untested tasks with higher uncertainty first, quickly reducing errors in performance prediction. We further introduce several improvements to enhance PMF for scenarios with sparse observed performance scores. In experiments, we systematically evaluate 108 LVLMs on 176 datasets from 36 benchmarks, constructing training and testing sets for validating our framework. Our experiments demonstrate the accuracy of PMF in predicting unknown scores, the reliability of uncertainty estimates in ordering evaluations, and the effectiveness of our enhancements for handling sparse data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a framework for predicting the performance of large vision-language models on held-out downstream tasks using a small set of observed task performances, i.e., evaluations for a small set of (model, dataset) tuples. They formulate this as a matrix completion problem and demonstrate that probabilistic matrix factorization (PMF) with MCMC is surprisingly effective, using a large set of 108 VLM evaluations on 176 datasets. Further, the authors demonstrate that the uncertainty estimates of PMF can be used in active evaluation to prioritize which evaluation to conduct next, outperforming random selection. Lastly, the work explores extensions of the naive Bayesian PMF model: tensor factorization to handle multiple metrics, and incorporating side information for better performance under extreme sparsity.

### Strengths
- Strong motivation: VLM evaluation is very expensive, so being able to accurately predict downstream evaluation performance from a limited set of evaluations is very valuable.
- The method is elegant and appears to work well, e.g., the correlation plots in Figure 3 look clean. It is also surprisingly effective in active evaluation, which is a very practical and exciting direction for this line of work.
- The paper is exceptionally well-written and clear.
- The evaluation uses a large set of (model, dataset) evaluations on a variety of open- and closed-source models.

### Weaknesses
The authors only consider a limited set of naive baselines for the main experiments in Figure 3. Could the authors benchmark other more sophisticated (neural) matrix completion methods, such as deep matrix factorization [1] or Graph Convolutional Matrix Completion [2]?

[1] Arora et al., 2019. Implicit Regularization in Deep Matrix Factorization. In NeurIPS. https://arxiv.org/abs/1905.13655

[2] van den Berg et al., 2018. Graph Convolutional Matrix Completion. In KDD. https://www.kdd.org/kdd2018/files/deep-learning-day/DLDay18_paper_32.pdf

### Questions
* My main concern is the limited set of baseline matrix completion methods (mentioned above).
* Evaluation of active evaluation: could you consider a more canonical active learning evaluation setup? i.e., randomly partition elements of the matrix into an initial training set, an "unlabeled pool set" (in the active learning nomenclature), and a test set, and report active learning-style curves: for each acquisition method (oracle, random, uncertainty), plot RMSE on the test set versus the number of acquisition steps, as you acquire evals in the pool set? e.g., what is done in [3].
* Comment for possible future work: because the indices of the unobserved (model, dataset) elements are known a priori (and you also have access to side information such as which image encoder was used, etc.), this setting seems to fit naturally with some transductive active learning methods, such as [4].

[3] Gal et al., 2017. Deep Bayesian Active Learning with Image Data. https://arxiv.org/abs/1703.02910

[4] Bickford-Smith et al., 2023. Prediction-Oriented Bayesian Active Learning. In AISTATS. https://proceedings.mlr.press/v206/bickfordsmith23a/bickfordsmith23a.pdf

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a framework for predicting the performance of large vision-language models (LVLMs) across multiple tasks. The main idea is to employ probabilistic matrix factorization (PMF) to estimate unknown performance scores based on a sparse set of observed scores. By formulating performance prediction as a matrix completion problem and leveraging MCMC methods to estimate prediction uncertainty, the authors aim to reduce the computational cost of evaluating large models across diverse tasks. In addition, the authors propose several enhancements to handle data sparsity, including tensor factorization for multiple performance metrics and Bayesian PMF.

### Strengths
1. The proposed method is grounded in well-established techniques of matrix factorization and probabilistic modeling. The mathematical foundation of PMF is solid, and using MCMC for uncertainty estimation is a sensible approach to prioritize evaluations. The paper demonstrates that the method can effectively predict unknown performance scores, especially when more than 10% of the data is available. 

2. Evaluating 108 LVLMs across 176 datasets demonstrates the practicality and scalability of the proposed method across a wide range of tasks.

### Weaknesses
1. The paper tackles an important problem: efficiently evaluating large-scale models as they grow in size and complexity. The idea of using matrix completion and active evaluation is interesting and, if successful, could lead to significant computational savings. However, the novelty is somewhat limited since the approach mainly builds on existing techniques like PMF, Bayesian modeling, and MCMC.

2.  Several parts of the paper lack clear explanations. For example, the differences between PMF, PTF, and Bayesian PMF are densely presented, and their respective impacts on performance are not sufficiently disentangled in the experiments. An explicit ablation study would help understand each enhancement's individual contributions. 

3. While using uncertainty to prioritize evaluations is compelling, the results show a gap between the uncertainty-based approach and the oracle method. The paper could explore why this gap exists and whether alternative heuristics could narrow it.

### Questions
1. Could you clarify how Bayesian PMF differs from standard PMF in practical terms? Specifically, how does incorporating an LKJ prior (Lewandowski et al., 2009) impact the predictions in practice?

2. Including an ablation study to better quantify the contribution of each component—such as tensor factorization, Bayesian PMF, and the use of profiles—would help clarify their respective impacts on performance.

3. There's a noticeable gap between the uncertainty-based active evaluation and the oracle method. Have you considered alternative heuristics for prioritizing evaluations that might close this gap?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Evaluating VLMs across various number of tasks is costly (as the number of benchmarks can be huge) and the model sizes can be very large as well. The paper tries to propose an approach to estimate the performance on some datasets, by converting the problem to that of sparse matrix factorization, a well studied statistical approach for matrix completion. They assume a M x N matrix, where M is the different models and N is the various tasks. Given some entries of this matrix, one can estimate the rest using matrix factorization. The paper proposes some trivial modifications to the standard PMF to fit this specific use case. While the proposed work is an application of existing techniques to this problem, it is unique and has not been done previously in this setting. The empirical results are great, and the proposed idea can be useful to the community as such, especially while practitioners are developing models and need to frequently evaluate a lot of checkpoints/variations/finetuned versions of VLMs.

### Strengths
- An interesting application of existing statistical method for the problem of estimating performance on benchmarks. 
- The work has potential for impact and being useful for the community, especially developers. 
- Easy to implement, nice and thorough empirical analysis with sufficient ablations and insights/discussions.

### Weaknesses
 - In the active evaluation, the authors order the priority of the task for evaluation based on its estimation uncertainty/deviation. But this doesn’t factor in the cost of evaluation (time) or the model size for that entry. It can be possible that estimating 2 other entries with lower uncertainty initially, and a lower combined evaluation cost turns out to be better than evaluating the entry with highest uncertainty. Curious to know if the authors explored multi-objective optimization, or tried to incorporate evaluation cost in other versions of there proposed approach. 
- As such, the work is basically applying an existing statistical technique (matrix completion) to the problem of estimating performance on benchmarks. Authors do propose some small modifications over standard matrix factorization. One can say that using matrix completion for various applications in the real world is not a novel contribution.
- It would have been much more compelling work, if the approach incorporated VLM specific ideas or benchmark specific stuff over an above the standard matrix factorization techniques.

### Questions
See the weakness section

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a framework for predicting unknown performance scores of LVLMs by formulating it as a matrix completion task using probabilistic matrix factorization with MCMC. The paper addresses the challenge of high computational costs in evaluating LVLMs and aims to reduce unnecessary evaluations by predicting performance scores based on observed ones from other models or tasks.

### Strengths
1. This paper evaluates 108 models on 176 datasets, covering a wide range of tasks and benchmarks. This systematic evaluation can provide a foundation for many future research.
2. PMF for handling sparse data, such as tensor factorization, Bayesian PMF, and the use of model and dataset profiles, seems a more robust approach to mitigate potential weaknesses in the matrix completion task.

### Weaknesses
Of course, it is statistically possible to make more robust predictions, but even humans can predict the performance level of a model to some extent just by observing certain patterns in the results. However, the reasons we still need to directly evaluate are:
1. The learning methodology may show significant weaknesses or strengths on specific benchmarks, and such frameworks cannot analyze these.
2. K-shot, certain promptings, or new evaluation methods could lead to changes in results across benchmarks, but this framework lacks insights into these aspects.

Therefore, although we can statistically predict the results to some extent without directly evaluating a new model, we still confirm the actual performance through evaluation. Moreover, even testing just 10% less in a setting where only a subset of the test set is used can significantly undermine the reliability, making it even harder to trust this framework. In short, using this framework to predict scientific conclusions presents a risk that far outweighs the cost savings.

### Questions
A more detailed analysis is needed. Conducting PMF based on different learning methodologies, evaluation pipelines, and promptings could improve the quality of the paper.

### Soundness
2

### Presentation
3

### Contribution
2

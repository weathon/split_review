# Enhancing Training Robustness through Influence Measure

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 6, 6, 5

## Abstract
In the field of machine learning, the pursuit of accurate models is ongoing. A key aspect of improving prediction performance lies in identifying which data points in the training set should be excluded and which high-quality, potentially unlabeled data points outside the training set should be incorporated to improve the model's performance on unseen data. To accomplish this, an effective metric is needed to evaluate the contribution of each data point toward enhancing overall model performance. 
This paper proposes the use of an influence measure as a metric to assess the impact of training data on test set performance. Additionally, we introduce a data selection method to optimize the training set as well as a dynamic active learning algorithm driven by the influence measure. The effectiveness of these methods is demonstrated through extensive simulations and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a local influence-like case influence measure as a metric to assess the impact of training data on test set performance. 

The measure is applied in two areas: data trimming and active learning. Based on the numerical studies, both applications help enhance the model's robustness and outperform the state-of-art strategies. 

Two approximation techniques are introduced to address the high computational cost. They reduce memory and processing requirements while maintaining effectiveness.

### Strengths
It's a useful study that includes 

1. the intuition and details of how this new influence measure is designed

2. scenarios where it can be used 

3. approximation methods that can make it really practical

Extensive examples with detailed simulation settings are included bringing persuasiveness.

### Weaknesses
1. I wonder if it is possible to provide the complexity analysis in terms of both memory and speed for the proposed method and the state-of-art strategies for examples in the paper. 

2. I am a bit confused about what robustness means in the paper. Is it about how the model would behave after removing or perturbing any data? Or its about after doing these procedures, the prediction performance is consistently better than not doing it? If it is the latter case, improving prediction performance should be a better way of describing it. 

Moreover, since we are talking about robustness, should the standard deviation of prediction accuracies in Table 2 also be included? also error bars in figure 2 and 8.

3. Unlike the influence function in Chhabra et al, it seems that there is no clear threshold or boundary that differentiates samples that positively or negatively affect the model performance. In the examples, the number/portion of samples removed is also a tunable parameter. I speculate that the accuracy won't always increase monotonically with the portion of samples removed in the training set. And sometimes, it the data are perfectly separable, there is no need to remove any of the samples. With this being said, is there a guideline on how much data should be removed when working on a real-world dataset? 

4. I don't know if the masking effect is considered or not. Is there a way to incorporate this into your procedure? 

5. I am also curious about the choice of \omega_0. In some other case influence literature, people would simply this from vector to scalar by considering it as the weight of the observation of interest. I wonder if it is treated similarly here.

### Questions
Please check the Weaknesses.

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
The paper introduces a novel influence function based method to guide the data selection for data trimming and active learning. For data trimming, the proposed method applies perturbations to samples and measures the impact on the model's performance on test data. Here if the impact on test performance from perturbations in a sample input is large, it is encouraged to exclude that instance from the training set. 
In the case of active learning, they perturb the model parameters and measure the changes in prediction for a new instance. If the changes in prediction is significant, the new instance will be added to the training data.
Authors study the effectiveness of their proposed method on synthesized and real world data sets for linear and non linear models and multiple domains. Experimental results show superior performance for the proposed method compared with other alternative approaches.

### Strengths
- The problems addressed by the paper, i.e. filtering training data and choosing new training instances for active learning to boost model performance are real world problems with significant impact on a wide range of machine learning problems with real world applications.

- Authors have provided sufficient literature review and the main claims of the paper are clear. 

- Authors propose two approximation methods for their local influence measure to reduce the computational cost of their proposed method.

- Experimental results shed light on performance of the proposed method compared with two (depending on the test data set) state of the art approaches and a baseline of the random selection.

### Weaknesses
 - The main weakness of this work is lack of ablation studies to better understand the impact of the contributions of this work on its performance.
  - For example, the first contribution of the paper is to evaluate the impact of perturbations against the model performance for the test data set. It would have been useful to see how much this slight modification is helping with improving the proposed method's performance for data trimming. Specifically, it's unclear if the observed performance gains are due to the influence function itself or the specific perturbation method applied to the test set. A comparison with a baseline that uses a standard influence function without test set perturbations would be beneficial.
  - As another example, authors utilize two approximation techniques to reduce the computational cost of their proposed method, however, there is no experiment providing more insights into the trade offs between the potential reduction in the proposed method's performance vs. the quantified computational cost reduction. The paper lacks a detailed analysis of the computational complexity of both the exact and approximate methods, making it difficult to assess the practical benefits of the approximations. Furthermore, the paper does not quantify the performance degradation, if any, associated with the approximation techniques.

### Questions
- Based on equation 1 it looks like the perturbations applied to the training instances is by adding noise to them versus changing the training data's weight/importance. Can authors explain the rationale behind picking this type of perturbation over changing training instances' weights?

### Soundness
2

### Presentation
3

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
This paper proposes a better influence measure to evaluate the impact of the training dataset on the test set. This metric mainly improves the flaws of the influence measure in Chhabra et al. (2024). The experimental results demonstrate that the FI proposed in this paper outperforms the IV metric in Chhabra et al. (2024).

### Strengths
1. The contribution of this paper is simple and clear.
2. the experimental results demonstrate that the FI proposed in this paper is superior to the IV metric in Chhabra et al. (2024).

### Weaknesses
 1. The paper claims "Our metric directly assesses the effect of small perturbations in the training samples on the model's performance on the test set", whether this leaks information about the test samples during the training process, which needs to be clarified by the authors.
2. The parameter settings in the experiments need further clarification.
3. What are the limitations of FI that need to be further explained in this paper?
4. I think the FI proposed in this paper is not enough to compare with IV only. The argument of this paper is to propose a better metric, however there are many similar metrics, such as the Shapley value. Therefore, this paper needs to further demonstrate the value of the proposed scheme.

### Questions
See Weakness.

### Soundness
3

### Presentation
2

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
This study presents a First-order Influence (FI) measure designed to enhance the generalization capabilities of supervised machine learning models. To achieve this, the proposed measure assesses the contribution of each individual training data point to the model's average performance on a given validation set. The FI measure is first applied to Data Trimming, a process that identifies and removes non-representative training data points to improve model performance. Additionally, the FI measure is utilized in Active Learning (AL) to select the most informative, unlabeled data points that will be added to the training dataset, thereby optimizing the model's learning process with limited samples, iteratively.

### Strengths
+ The proposed applications of the First-order Influence (FI) measure demonstrate superior performance compared to its recent counterparts, particularly the Influence Value (IV) method [Chhabra et al. (2024) / chhabra2024data], showcasing the effectiveness of FI against a very recent work.

@inproceedings{chhabra2024data,
  title={" What Data Benefits My Classifier?" Enhancing Model Performance and Interpretability through Influence-Based Data Selection},
  author={Chhabra, Anshuman and Li, Peizhao and Mohapatra, Prasant and Liu, Hongfu},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024}
}

### Weaknesses
 - The evaluation is conducted for binary classification with logistic regression, supplemented by additional experiments using CNN on existing image datasets. However, the analysis is somewhat limited in scope. Although this setup is based on a related ICLR work [Chhabra et al. (2024) / chhabra2024data] and compares against the method named Influence Value (IV) from that published work, I find the dataset evaluation to be relatively insufficient. To thoroughly assess the performance of using FI or related methods, I believe it is essential to test it on a diverse range of datasets with varying characteristics, which would help to confirm its strengths and potentially reveal its limitations.

- Following that, while FI appears to outperform the compared methods (IV and Random for Data Trimming; IV, Random, and Bald for Active Learning), its superiority is not necessarily absolute (at least this is not clearly shown), as performance varies across datasets. Notably, on the CelebA dataset for Data Trimming, Random actually outperforms IV and achieves results comparable to FI. This dataset-specific variation raises concerns about the generalization of the FI's performance across different datasets, leaving questions about how they would perform on other datasets.

### Questions
Q. What scenarios or conditions are likely to result in FI to underperform?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Authors propose the use of an influence measure based metric to determine the importance of samples in a dataset towards generalisation performance of models. An approach for selecting such samples for optimal training (data trimming) and an active learning based approach is also presented. Relevant metrics to this end have been introduced and evaluated on datasets.

### Strengths
The initial discussion introducing the proposed method is detailed and well motivated. Authors present the approach with sufficient rigor. The algorithms are presented well and the experimental results reported on the chosen datasets as well as the experiments conducted have been described in adequate detail with supplementary results.

### Weaknesses
My primary concern with the work presented is the limited scalability analysis of the proposed methods for larger datasets, and possibly the lack of discussion of the computational complexity of the algorithms. Practical datasets for most real-world applications could have much higher number of samples, as well as features, so it would be important to benchmark with such datasets.

It may be useful to provide accuracy results in a tabular form reported as mean +/- std. dev. as an appendix for the sake of completeness.

The authors should possibly consider making the code for the methods proposed available publicly to ensure reproducibility.

As far as the datasets where train and test sets are not explicitly provided, and authors have chosen a split to conduct the experiments and report the results, are these k-fold validated?

While a time comparison is provided in Table 7, could the authors comment on possible methods for scalability of the proposed approach for practical applications, especially when inference is required from streaming datasets in test.

The equations in the appendix could be numbered for ease of reference. Proof for Theorem 1 does not seem to be provided.

### Questions
Details of the complexity and scalability of the proposed method, and evaluation on larger datasets would help establish practical utility of the method.

Code for proposed method could be made available.

Additionally, addressing comments mentioned as weaknesses would be helpful.

### Soundness
3

### Presentation
3

### Contribution
2

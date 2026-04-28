# Lost in the Averages: Evaluating record-specific MIAs against Machine Learning models

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
Record-specific Membership Inference Attacks (MIAs) are widely used to evaluate the propensity of a machine learning (ML) model to memorize an individual record and the privacy risk its release therefore poses. Record-specific MIAs are currently evaluated the same way ML models are: on a test set of models trained on data samples that were not seen during training ($D_{eval}$). A recent large body of literature has however shown that the main risk often comes from outliers, records that are statistically different from the rest of the dataset. In this work, we argue that the traditional evaluation setup for record-specific MIAs, which includes dataset sampling as a source of randomness, incorrectly captures the privacy risk. Indeed, what is an outlier is highly specific to particular data samples, and a record that is an outlier in the training dataset will not necessarily be one in the randomly sampled test datasets. We propose to use model randomness as the only source of randomness to evaluate record-level MIAs, a setup we call *model-seeded*. Across 10 combinations of models, datasets, and attacks for predictive and generative AI, we show the per-record risk estimates given by the traditional evaluation setup to substantially differ from ones given by the *model-seeded* setup which properly account for the increased risk posed by outliers. We show that across setups the traditional evaluation method leads to a substantial number of records to be incorrectly classified as low risk, emphasizing the inadequacy of the current setup to capture the record-level risk. We then a) provide evidence that the traditional setup is an average--across datasets--of the *model-seeded* risk, validating our use of model randomness to create evaluation models and b) show how relying on the traditional setup might conceal the existence of stronger attacks. The traditional setup would indeed strongly underestimate the risk posed by the strong Differential Privacy adversary. We believe our results to convincingly show the practice of randomizing datasets to evaluate record-specific MIAs to be incorrect. We then argue that relying on model randomness, an setup we call *model-seeded* evaluation, better captures the risk posed by outliers and should be used moving forward to evaluate record-level MIAs against machine learning models, both predictive and generative.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues that recently proposed MIAs donot correctly capture the privacy risks of training samples. The main argument is that the high risk samples are often outliers, and outliers are dependent to the sampled datasets. Thus shadow models trained with randomly sampled datasets may not be able the reflect the fact that the underlying sample is an outlier in the trainingset of target model. 

To address this, the authors propose to obtain randomness by vary different weight initialization and training seeds.  The experimental results show that the proposed model-seed based approach can detect many high risk samples which are missed by traditional MIAs such as LiRA.  Moreover, when dealing with the strongest DP adversary, the proposed model-seed approach also give higher attack success rate compared with traditional ones.  

In addition, the authors also argue that TPR at low FPR metric is not relevant in evaluating per-record MIAs, thus they opt to use ROC AUC as the privacy metric.

### Strengths
1. The idea of randomizing model seeds is novel. Also the observation that randomizing training datasets in shadow models might not be able to capture whether a specific sample is an outlier in the trainingset of the target model or not, is reasonable. 

2. The paper gives a very nice and clear overview of MIAs, I appreciate it.

3. The two newly defined metrics demonstrate the improvement of model-seeded compared to traditional methods.

4. Comprehensive cross-method experiments.

### Weaknesses
1. The privacy risk calculation process is not clear enough.

2. In Figure 2a, where is the value 0.53 indicated? Is it represented by the dashed line?

3. It is unclear how exactly the privacy risk is calculated. In Algorithm 1, it states to "calculate privacy risk using a chosen metric based on the prediction set." How is this done in practice? For each sample, do you determine the best threshold that separates IN and OUT models and then use this threshold to compute the AUC?

4. The argument that TPR at low FPR is unsuitable for assessing per-record MIAs is not fully explained. Why is the TPR at low FPR, as proposed in LiRA, not appropriate for evaluating the privacy of per-record MIA?

5. The distinction between evaluating model privacy and record-level privacy needs clarification. If my understanding is correct, the authors suggest that existing MIAs generally measure how a particular target model reveals its training data's membership information, rather than focusing on the privacy risk of a specific sample when included in the training set. While I agree with the motivation for record-specific MIAs, these two cases are closely related. Whether a sample is an outlier depends not only on the data distribution but also on the deployed models. The strictest setting, following differential privacy (DP), assumes full knowledge of the dataset except for the sample being evaluated, but this approach is computationally expensive. How do you ensure that considering model randomness adequately simulates the DP case?

6. Given that the authors identify high-risk samples misclassified as low-risk by traditional MIAs, it would be beneficial to include visual examples of these samples to see if they appear as outliers by human perception.

7. How does the gap between the proposed approach and traditional MIAs change with the complexity of the datasets? In Table 1, CIFAR-10 shows the lowest miss rates. Would CIFAR-100 yield even lower miss rates? If so, would the gap between the methods diminish when applied to more complex datasets in practice?

8. What would Figure 3 look like if tested with CIFAR-10 or CIFAR-100 datasets?

### Questions
1. In Figure 2a, where is the value 0.53 indicated? Is it represented by the dashed line?

2. It is unclear how exactly the privacy risk is calculated. In Algorithm 1, it states to "calculate privacy risk using a chosen metric based on the prediction set." How is this done in practice? For each sample, do you determine the best threshold that separates IN and OUT models and then use this threshold to compute the AUC?

3. The argument that TPR at low FPR is unsuitable for assessing per-record MIAs is not fully explained. Why is the TPR at low FPR, as proposed in LiRA, not appropriate for evaluating the privacy of per-record MIA?

4. The distinction between evaluating model privacy and record-level privacy needs clarification. If my understanding is correct, the authors suggest that existing MIAs generally measure how a particular target model reveals its training data's membership information, rather than focusing on the privacy risk of a specific sample when included in the training set. While I agree with the motivation for record-specific MIAs, these two cases are closely related. Whether a sample is an outlier depends not only on the data distribution but also on the deployed models. The strictest setting, following differential privacy (DP), assumes full knowledge of the dataset except for the sample being evaluated, but this approach is computationally expensive. How do you ensure that considering model randomness adequately simulates the DP case?

5. Given that the authors identify high-risk samples misclassified as low-risk by traditional MIAs, it would be beneficial to include visual examples of these samples to see if they appear as outliers by human perception.

6. How does the gap between the proposed approach and traditional MIAs change with the complexity of the datasets? In Table 1, CIFAR-10 shows the lowest miss rates. Would CIFAR-100 yield even lower miss rates? If so, would the gap between the methods diminish when applied to more complex datasets in practice?

7. What would Figure 3 look like if tested with CIFAR-10 or CIFAR-100 datasets?

### Soundness
3

### Presentation
4

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
The paper introduces a new framework for quantifying privacy risks through membership inference attacks. The authors argued that the traditional approach assesses the effectiveness of these attacks by comparing models trained with the target data point against models trained without it, with the remaining training data randomly sampled from the data pool. In contrast, this paper proposes a refined setup: the remainder of the dataset is held constant, and the performance of the membership inference attack is evaluated based on its ability to distinguish between models trained with and without the target point while keeping all other training data identical.

### Strengths
The paper studies privacy auditing using membership inference attacks, which is an important and interesting topic.

### Weaknesses
1. The paper seems unclear about why different evaluation setups are needed. In my understanding, membership inference attacks can be framed as a game between an adversary and the model trainer, where the privacy risk is quantified by the adversary's success in this game (Ye et al. 2022, Sablayrolles et al. [1], Yeom et al. [2], Carlini et al. (2022a)). Each setup defines the privacy risk in a distinct context, such as the average privacy risk of a training algorithm or the specific privacy risk associated with a single data point. To quantitatively assess privacy risks, different setups are designed to simulate these privacy games. Traditional setups and model-seeded setups represent two distinct privacy games and, as a result, inherently measure different types of privacy risks. Therefore, comparing metrics such as RMSE and Miss Rate across these two setups is not meaningful.

2. The new proposed setups are identical to the Definition 3.4 of Section 3.4 in Ye et al. 2022 and the paper lacks discussion in this work. 

3. The paper uses ROC AUC and accuracy to assess privacy risks, which is problematic, as discussed extensively in Carlini et al. (2022a). Instead, the evaluation should include at least the true positive rate at a low false positive rate.

### Questions
1. What is the privacy game that this paper investigates, and how are the new setups designed to simulate it? (see w1). To address these comments, I would like to ask the authors to explicitly define the privacy game for the MIA settings discussed in the paper and justify why comparing metrics across setups is meaningful in this context.

2. Please compare with the evaluation setups in Definition 3.4 in Section 3.4 of Ye et al. 2022 and justify what is new compared to the existing evaluation setups. In particular, in Definition 3.4 of Ye et al. (2022), the adversary’s objective is to differentiate between models trained on fixed subsets that include the target point and those trained on the fixed subsets without the target point. Similarly, the proposed setups, as illustrated in Figure 1, aim to distinguish between a model trained on $D_{\text{target}}$ and one trained on $ D_{\text{target}}$ with $x_{\text{target}}$ replaced by $x_r$.

3. What is the relationship between the target model and the evaluation model? Specifically, are you inferring membership for a fixed target model (which relates to the privacy risk of a specific trained model), or are you using a set of evaluation models to quantify the privacy risk for a single target sample? 

4. Please also report the empirical results (Table 1) and the theoretical analysis (Theorem 1) based on the true positive rate at the low false positive rate (see w3).

### Soundness
1

### Presentation
2

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
The paper challenges the traditional method for evaluating record-specific MIA on machine learning models, which assesses privacy risks by averaging results across various datasets. This conventional method, which uses dataset sampling as a source of randomness, may not accurately capture the risks associated with outlier records. These records, which are statistically distinct, often carry higher privacy risks. To address this, the authors propose a "model-seeded" evaluation, relying on model-specific randomness rather than dataset variation. This approach is argued to be more sensitive to record-level risk, especially for outliers, thus providing a more accurate measurement of privacy threats posed by MIA.

### Strengths
The paper challenges the traditional method for evaluating record-specific MIA on machine learning models, which assesses privacy risks by averaging results across various datasets. This conventional method, which uses dataset sampling as a source of randomness, may not accurately capture the risks associated with outlier records. These records, which are statistically distinct, often carry higher privacy risks. To address this, the authors propose a "model-seeded" evaluation, relying on model-specific randomness rather than dataset variation. This approach is argued to be more sensitive to record-level risk, especially for outliers, thus providing a more accurate measurement of privacy threats posed by MIA.

### Weaknesses
1.The model-seeded method assumes that outlier status consistently correlates with higher privacy risks, a premise that might not apply universally across all datasets or model types. This limitation is also notable, as generalizing outliers as inherently high-risk without broader evidence may lead to misjudgments. If outliers do not uniformly correlate with increased privacy risks, adopting this assumption could skew privacy evaluations and limit the model-seeded approach’s applicability. Specifically, the method does not account for the possibility that some outliers might be easily predictable or have characteristics that make them less susceptible to membership inference attacks, thus potentially overestimating their risk.

2.By focusing on model-seeded evaluations, this method may potentially amplify perceived privacy risks for records that happen to exhibit outlier characteristics, which might lead to overly conservative evaluations. Though less immediately impactful, an overestimation of privacy risks could have negative implications, potentially stifling the release of data and models in scenarios where the actual privacy risk might be minimal. This is particularly concerning because the method does not provide a mechanism to differentiate between truly high-risk outliers and those that are simply statistically unusual but not vulnerable to privacy breaches.

3.The most critical limitation, as the added computational requirements could limit the adoption of the model-seeded approach in practice. Evaluating privacy risks in real-world scenarios often demands rapid processing across various models and datasets, and an overly resource-intensive method could hinder its scalability and accessibility. The paper does not provide a clear analysis of the computational overhead of the model-seeded approach compared to traditional methods, making it difficult to assess the practical feasibility of the proposed method. This lack of analysis is a significant oversight, as computational efficiency is a key factor in the adoption of any evaluation methodology.

### Questions
1.The author critiques the lack of true randomness in traditional sampling-based evaluation metrics, arguing that these metrics fail to accurately capture privacy risks in models. However, non-randomness in sampling does not necessarily lead to bias in evaluation outcomes. The issue of outliers disproportionately affecting privacy risk assessments arises primarily when the entire training dataset is consistently used across each model being attacked. By performing adequate and independent random sampling of subsets, the aggregate distribution of sampled datasets would approximate that of the full training set, reducing outlier impact. This raises a question about the necessity of model-seeded sampling in place of random sampling. When each model is trained on the complete dataset, outliers indeed amplify the privacy risk assessment. However, ensuring random sampling alone does not necessarily align the distribution between training and non-training sets for evaluation, which can potentially affect the fairness of the evaluation metrics.

2.In the Related Work section, the author overlooks key recent studies specifically addressing advancements in MIA evaluation metrics. Expanding this review to include recent literature on MIA evaluation techniques would better contextualize the current study within the broader research landscape. Additionally, the statement beginning "The standard evaluation setup for MIAs..." on Line 124, Page 3 lacks clarity on why conventional metrics fall short or what specific limitations they exhibit in this context. Providing concrete examples or detailed limitations of these standard metrics would clarify the rationale for proposing alternative methods. Comparative examples would enhance readers’ comprehension of the need for innovative evaluation approaches.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new evaluation setup, termed model-seeded evaluation, to assess privacy risks for individual records in Membership Inference Attacks (MIAs) against machine learning models. The traditional MIA evaluation setup relies on dataset sampling as a randomness source, which can obscure risks for outlier records, as these outliers may not consistently appear across sampled datasets. In contrast, the model-seeded approach keeps the dataset fixed and varies the model’s randomness (e.g., initialization seeds and training variations) to better capture privacy risks, especially for outliers. The authors validate this approach through experiments with various models, datasets, and attacks, showing that model-seeded evaluation more accurately assesses per-record privacy risks.

### Strengths
1.Clarity: The paper is well-organized.

2.Originality: The proposal of model-seeded evaluation as a way to focus on model randomness rather than dataset sampling introduces a new angle for evaluating privacy risks in MIAs.

### Weaknesses
1.Lack of Clear Novelty and Contribution: It is challenging to grasp the novelty and practical contribution of the proposed method within the scope of the ICLR main conference. This work might be more suitable for another conference focusing on evaluation methods rather than core ML contributions or a Datasets and Benchmarks Track.

2.Confusion Regarding Proposal: There is ambiguity in the proposal's application, especially regarding the handling of shadow models. For example, in "Membership Inference Attacks from First Principles" (S&P 2022), shadow models rely on training diversity achieved through different sampling. If the proposal implies keeping the majority of training data fixed and varying model seeds, this approach may fail to capture the diversity that shadow models achieve through varying data, potentially resulting in inaccurate representations of privacy risks. The core issue is that the proposed method seems to assume the attacker has access to the target model's training data, which is not a realistic assumption in the context of MIAs. This assumption fundamentally alters the threat model and makes the proposed evaluation less relevant to real-world scenarios. None of the previous MIAs [1,2,3], operate under this assumption. The use of shadow models in MIA is specifically to address the scenario where the attacker does not have access to the target model's training data. If the attacker had access to the training data, the attack would be significantly simpler, as a classifier could be trained directly on the training data versus non-training data, rendering the complexities of shadow models unnecessary. The modifications proposed in the submission are quite limited, and it is well understood by MIA researchers that if the attacker had access to the training data, attacker performance would naturally be much higher.

### Questions
I am confused by the implementation of your proposal. I would like the authors to address the following specific question:
In "Membership Inference Attacks from First Principles" (S&P 2022), shadow models are trained with IN-models and OUT-models that derive their diversity primarily from different training samples. Is your proposal to maintain most of the training data unchanged and instead vary only the model seeds and initialization weights to achieve diversity among shadow models? If so, this method might be flawed, as it could produce shadow models that do not reflect the target model's distribution accurately, especially if there are significant differences between the fixed training data for shadow models and the target model’s data.
To illustrate, Figure 3 in "Membership Inference Attacks from First Principles" shows that the variability in IN models with different training samples significantly impacts privacy risk assessments. Using fixed training data with only model randomness may lead to substantial errors in evaluating privacy risk, as it could miss the model diversity required to mimic target model behavior. Could the authors clarify this approach? If my understanding is incorrect, please correct it. Thank you.

Decision: I am giving a score of 5 (marginally below the acceptance threshold). While I appreciate the attempt at a new evaluation method, if my understanding is correct, this proposal may be inherently flawed. I look forward to the authors' responses to my concerns.

### Soundness
2

### Presentation
2

### Contribution
2

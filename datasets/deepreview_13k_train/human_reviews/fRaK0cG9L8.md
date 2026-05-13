# Evaluating Perceptual Distances Models by Fitting Binomial Distributions to Two-Alternative Forced Choice Data

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
The abstract should summarize the contents of the paper. 
  LNCS guidelines indicate it should be at least 70 and at most 150 words.
  Please include keywords as in the example below. 
  This is required for papers in LNCS proceedings.
  \keywords{First keyword \and Second keyword \and Third keyword}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a probabilistic approach to model the subjective judgment obtained from 2AFC experiments about visual quality using a binomial distribution. The goal is to evaluate perceptual distance models predicting visual quality with respect to the 2AFC experimental data. Three metrics are derived for evaluation and the results on BAPPS are shown.

### Strengths
The issue of modeling 2AFC experimental data is an interesting topic.

The proposed method enjoys simplicity.

### Weaknesses
1. The paper is not easy to follow, mainly due to lack of definition, usage inconsistency, and unusual usage of notations and symbols. For instance, $t$ in $x_0(t)$ is not defined, $T$ is not defined, $d_v$ is not defined, $N$ is not defined, $P$ and $p$ are used without clear distinction, $j$ in Fig. 1 is not defined, the arguments are not consistent in $P$ (sometimes two arguments, sometimes three arguments, sometimes no argument, arguments do not match), {$(d_0, d_1), n=j$} doesn't make much sense, etc. In addition, some sentences are not easily understood, e.g., first sentence of Section 2.1, last sentence in page 6, what does 'preferred smoothness' mean and how can it be determined, etc.

2. Although the proposed method provides (maybe) new ways to evaluate the predicted quality scores by perceptual distance models, it is not experimentally shown whether the proposed method has any advantage over existing approaches including checking whether the image preferred by a majority of human raters is predicted to have a higher quality score by a model, comparing the predicted scores to the MOS estimated using the Thurstone or Bradley-Terry model on the subjective data, etc. In fact, in Table 2, the proposed method shows very similar results to the distance-only case, so the proposed method doesn't seem advantageous. The core issue is that the paper does not clearly articulate the practical benefits of using the proposed method over simpler alternatives. The evaluation seems to only confirm what is already known about the tested distance metrics.

3. Section 4 presents experimental results, but they do not draw much meaningful conclusions. Above all, they do not prove that the proposed method is correct. Table 1 only shows that PIM, LPIPS, and DISTS are better than Euclidean, NLPD, and SSIM, which would be obvious without relying on the proposed method. Fig. 3 shows some difference among distance models, but not much more than that; it is said that humans perceive sharper differences when images are far from their reference, which I wouldn't agree. Fig. 4 is an interesting result, but it is not clear whether it can be useful practically. Fig. 5 shows the robustness of the proposed method against the choice of hyperparameters, but it does not prove that the results are correct. The experiments lack a clear objective beyond demonstrating the method's functionality, and do not provide a compelling case for its practical utility.

4. It is said that the proposed method is free from assumptions unlike existing methods. However, the proposed method also imposes certain assumptions. For instance, it is assumed that the subjective preference strictly follows the binomial distribution without any noise, the probability in the binomial distribution depends only on the quality distances and nothing else, etc. Justification on these issues would be needed. The assumption of a binomial distribution is a strong one and needs to be justified with empirical evidence or a theoretical argument. The model's simplicity might be a limitation if human perception is more complex.

5. Even though the assumptions made in the proposed method are correct, the proposed model is fitted through maximum likelihood estimation, where fitting error wouldn't be zero. How accurate is the fitting in the experiments? The fitting error could be from from the inadequacy of the model, the multimodality of the likelihood, the violation of convexity of the optimization problem, or something else. Analysis on this would be needed to justify the adequacy of the proposed model. The paper lacks a detailed analysis of the fitting process and its potential limitations. It is important to know how well the model fits the data and what the potential sources of error are.

6. Sampling for $\hat{n}$ is performed to obtain an 'upper bound' of AJ(?) and 'minimum possible' NLL. However, in Table 1, AJ with $\hat{n}$ doesn't act as an upper bound and NLL with $\hat{n}$ is not a lower bound. The meaning of the results of $\hat{n}$ should be interpreted appropriately. The same applies to Table 3.

(minor) Line 105, based off -> based on

### Questions
Please see the weaknesses.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents an approach to evaluate perceptual distance models using two-alternative forced choice (2AFC) experiments, especially with crowd-sourced data where traditional ranking methods are not applicable. The authors use a binomial distribution to model the decision-making process, estimate parameters with maximum likelihood, and propose metrics that surpass simple accuracy measures. This method offers a more robust evaluation of perceptual models compared to classical and neural network approaches.

### Strengths
1. The paper introduces a novel method for evaluating perceptual distance models using binomial distributions to model decision-making in two-alternative forced choice (2AFC) experiments, which is an innovative attempt in the field of image quality assessment.
2. The paper demonstrates the robustness of the model to changes in hyperparameters and offers insights into the interpretability of the results.

### Weaknesses
1. The paper compares the proposed method with classical and neural network methods but does not extensively compare it with the latest state-of-the-art approaches in perceptual distance modeling. Specifically, the evaluation lacks comparisons with recent models that have shown strong performance on perceptual tasks, such as those employing contrastive learning or transformer architectures, which are now common in the field.

2. The method is evaluated across different datasets, but there is insufficient evidence to demonstrate its generalizability across different types of images and distortions, particularly on traditional perceptual datasets like TID. While BAPPS is a large dataset, it is not clear if the method's performance would hold up on datasets with different characteristics, such as those with more controlled and specific types of distortions, or datasets that focus on specific image content like medical or satellite imagery. The lack of evaluation on datasets like TID, which are commonly used in the field, makes it difficult to assess the method's performance in a broader context.

3. The experimental section may lack comparative experiments to show the specific improvements of the proposed method over existing ones. The paper does not clearly demonstrate the added value of the proposed binomial modeling approach compared to simpler evaluation methods. For example, it would be beneficial to see a direct comparison of the proposed metrics with simple accuracy measures on a range of perceptual models, showing where and why the proposed metrics provide a better evaluation.

4. The paper may suffer from a lack of clarity in certain sections, Improving the organization of the content can help address this issue. Specifically, the description of the binomial model and the parameter estimation process could be more detailed and step-by-step, making it easier for readers to understand and reproduce the results. The connection between the model parameters and the perceptual distance could also be made more explicit.

### Questions
1. The authors should compare your method with state-of-the-art perceptual distance models.
2. It would be beneficial to have a more detailed and step-by-step explanation of the algorithm.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a statistical model to improve the evaluation of perceptual distance models based on crowd-sourced 2AFC (two-alternative forced choice) data. The topic is interesting but there are some serious issues with the applicability and experiment.

### Strengths
1. Rigorous Statistical Framework: By employing binomial distribution and maximum likelihood, the approach brings statistical rigor to perceptual distance model evaluation.
2. Improved Insight into Judgments: The additional metrics offer nuanced insights into how perceptual models align with human judgments, capturing nuances beyond binary agreement.

### Weaknesses
 **1. Applicability and Generalizability of the Proposed Metrics**

Could the evaluation metrics proposed in this study be extended to no-reference image quality assessment (NR-IQA) settings? In NR-IQA, pairwise comparisons, where participants judge the relative quality of two images, are common. This scenario bears similarities to 2AFC binary decision tasks and could benefit from the uncertainty modeling approach presented here. I recommend that the authors consider and discuss the metrics’ applicability in no-reference scenarios, potentially running experiments on pairwise NR-IQA datasets to further validate the transferability and generalizability of the metrics. This could significantly enhance the utility and impact of the proposed metrics in image quality assessment.

**2. Superiority Over Traditional Evaluation Metrics**

The study does not provide a clear demonstration of how the proposed metrics outperform traditional evaluation methods such as SRCC (Spearman’s Rank Correlation Coefficient), PLCC (Pearson Linear Correlation Coefficient), or KRCC (Kendall Rank Correlation Coefficient). While the authors show that deep learning models perform well using the new metrics, it is unclear whether this suffices to validate the effectiveness of the new metrics. To address this, I recommend a direct experimental comparison with these established metrics, which would highlight whether the new metrics provide additional information or improved accuracy. Moreover, it would be beneficial to discuss the potential of the new metrics to capture aspects like human judgment uncertainty and finer model differences, which traditional metrics may overlook, to enhance the credibility of this research.

**3. Dataset Selection and Applicability of Use Cases**

The experiments primarily rely on two datasets: BAPPS, which is diverse in distortion types, and CLIC, which is compression-specific. This dataset selection might limit the study’s ability to generalize the metrics’ effectiveness across different use cases. For instance, if the goal is to develop a general FR-IQA (full-reference image quality assessment) method, testing on a broader range of distortions—such as noise, blur, and color distortions—would be beneficial, possibly including datasets like TID2013 or LIVE. Conversely, if the focus is specifically on compression distortions, the paper would benefit from more explicitly discussing this application focus and how the proposed metrics could, for example, aid in choosing compression algorithms based on perceptual quality. Clearer examples or case studies illustrating how the metrics would assist in practical applications would improve the paper’s practical relevance.

**4. Relationship Between Uncertainty Modeling and MOS Distribution**

There seems to be a potential relationship between the proposed uncertainty modeling approach and MOS (Mean Opinion Score) distributions. MOS scores typically provide a more fine-grained rating (e.g., scores from 1 to 5), which offers a probabilistic view of perceived quality rather than binary decisions. I encourage the authors to explore how MOS distributions might contribute to refining the uncertainty modeling in this study, leveraging the probability distribution across the MOS scale to capture subtle perceptual differences more effectively. Discussing or experimenting with this connection could improve the interpretability and granularity of the proposed approach.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
3

### Contribution
2

# AN INFORMATION THEORETIC EVALUATION METRIC FOR STRONG UNLEARNING

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Machine unlearning (MU) aims to remove the influence of specific data from trained models, addressing privacy concerns and ensuring compliance with regulations such as the ``right to be forgotten.'' 
Evaluating strong unlearning, where the unlearned model is indistinguishable from one retrained without the forgetting data, remains a significant challenge in deep neural networks (DNNs).
Common black-box metrics, such as variants of membership inference attacks and accuracy comparisons, primarily assess model outputs but often fail to capture residual information in intermediate layers.
To bridge this gap, we introduce the Information Difference Index (IDI), a novel white-box metric inspired by information theory.
IDI quantifies retained information in intermediate features by measuring mutual information between those features and the labels to be forgotten, offering a more comprehensive assessment of unlearning efficacy.
Our experiments demonstrate that IDI effectively measures the degree of unlearning across various datasets and architectures,
providing a reliable tool for evaluating strong unlearning in DNNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a crucial and well-motivated issue in recent machine unlearning research: the inadequacy of common black-box metrics for assessing strong unlearning. To tackle this problem, the authors propose a new white-box metric called the Information Difference Index (IDI), which quantifies the residual information of the forget set in the intermediate layers of the network, providing a more comprehensive evaluation of unlearning efficacy.

### Strengths
S1. The assertion that "black-box metrics may not be sufficient for assessing strong unlearning" is well-motivated and compelling.

S2. The paper includes extensive empirical evaluations that support the claims made by the authors.

S3. The technical quality of the paper is good, and the ideas presented may be of significant interest to the machine learning community.

### Weaknesses
W1. This study seems to focus predominantly on the single-class forgetting scenario in the main text, relegating results related to other cases (e.g., random data forgetting, multi-class forgetting) to the appendices. Given that the paper aims to provide a general approach and is not limited to single-class forgetting, the authors are strongly encouraged to include essential findings from all three tasks in the main text. For instance, empirical evaluations demonstrating whether the proposed method consistently outperforms other baselines across all scenarios should be highlighted. The current presentation makes it difficult to assess the true scope and limitations of the proposed metric and unlearning approach.

W2. The head distillation (HD) approach introduced in Section 3 seems to be applicable only to the single-class forgetting task. The authors should either demonstrate HD's applicability to multi-class and random data forgetting tasks, or explicitly state its limitations if it cannot be generalized. Specifically, the method as described relies on masking logits associated with the forgotten class, which is not directly applicable when multiple classes are forgotten or when forgetting is random. The paper needs to clarify how HD would be adapted for these scenarios, or acknowledge its limited scope. Furthermore, if the generalization is possible, the authors should address whether the main observations regarding residual information and the limitations of black-box metrics are applicable in these other contexts. Specifically:
+ Would residual information still be retained within the intermediate layers of unlearned models?
+ Would black-box metrics continue to fail in capturing this residual information?

W3. I agree that a primary limitation of the proposed COLA approach is its computational burden due to the mutual information (MI) estimation process for each network layer, although this point is also noted by the authors in the paper. However, the paper could benefit from a more detailed discussion of the practical implications of this computational cost, especially in the context of large-scale models and datasets. A comparison of the computational cost with other unlearning methods would also be beneficial.

### Questions
In addition to addressing W1 and W2, the authors are also expected to answer the following questions:

Q1. In Figure 7, COLA appears to obtain a negative IDI value, which is even lower than Retrain. Does this imply that COLA is "over-unlearned”, according to the statement in Line 410?

Q2. Intuitively, for the random data forgetting task, if the retained dataset contains many samples similar to a forgotten one, residual information will likely persist within the intermediate layers. Given that the value of the Information Difference Index (IDI) heavily relies on the amount of this residual information, the authors should provide empirical evidence or theoretical analysis to demonstrate the effectiveness (or potential limitations) of IDI in random data forgetting tasks, particularly when there is a high similarity between forgotten and retained samples. This would help clarify the robustness and generalizability of the proposed metric.

### Soundness
3

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
4

### Summary
The paper address the issue that current black-box unlearning evaluation methods does not reflect the true unlearning quality -- many methods that pass such evaluation methods actually contains substantial information about the forget set, which make the unlearned model prone to relearning attacks. The paper proposes a new white-box evaluation metric based on mutual information. The estimated InfoNCE loss is used to calculate Information Difference Index (IDI) to ensure effective unlearning.

Based on this intuition the paper further proposes a new unlearning method by collapsing forgot set representation on the encoder layers then re-aligning the model. The paper demonstrated that such unlearning methods achieve low IDI compared to other unlearning methods.

### Strengths
Common unlearning metrics are known to be incomplete and not always reliable. This paper proposes a new evaluation methods for unlearning by estimation the mutual information using InfoNCE between intermediate layer features and output labels. This is a method that takes the internal behavior of the model into account, which measures unlearning at a deep level.

The paper also proposed a new unlearning methods from a similar motive. The CoLA method is able to achieve stronger unlearning compared to other unlearning methods.

### Weaknesses
One motivation for the new evaluation metric is from the concern that current metric only measures shallow unlearning which can be prone to relearning attacks, However, the paper does not present the strength of this new metric in a systematic manner. Figure 4 briefly mentioned retrain attacks but does not have the SCRUB method, it also comes before the new metric which makes it a bit confusing to read.

The evaluation method uses up to \(\ell\)-th layer and trains the rest to estimate the InfoNCE loss, which seems resource-intensive and scales poorly with the increase size of neural networks. It also requires a retrained model for IDI statistic, which seems infeasible for evaluating unlearning in practice. The reliance on a retrained model, while theoretically sound for measuring information removal, limits its practical applicability in scenarios where retraining is computationally expensive or impossible, such as with large-scale models or proprietary datasets. Furthermore, the paper does not adequately address the potential for the retrained model itself to introduce biases or artifacts that could affect the IDI metric, making it difficult to discern whether the IDI truly reflects the unlearning performance or is influenced by the retrained model's characteristics.



### Questions
In Figure 5, why does the mutual information decrease with the layers? Won't the model get more information as the features are passed through the network?

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
4

### Summary
This paper first introduces a naive machine unlearning method that modifies only the last layer of the model, achieving strong performance based on existing black-box evaluation metrics. Building on this, the author introduces a new white-box metric based on the mutual information between hidden features and labels to be forgotten. Furthermore, the paper proposes a new unlearning method, Collapse and Align (COLA), which effectively removes residual information at the feature level.

### Strengths
1. The topic of designing evaluation metrics for machine unlearning is both significant and challenging. This paper introduces a new metric based on the mutual information between the features and labels to be forgotten, effectively capturing the residual information in the unlearned model.

2. A new unlearning method inspired by the proposed evaluation metric is introduced, which is greatly appreciated.

3. The presentation is clear and easy to follow.

4. Several experiments are conducted to demonstrate the efficacy of the proposed evaluation method.

### Weaknesses
1. If I understand correctly, for each unlearned model with $L$ layers, mutual information must be estimated $3L$ times, each requiring data sampling and the training of two networks. Coupled with the time needed for retraining, the overall complexity is substantial.

2. Given the complexity, the necessity of such calculations needs further scrutiny. A simpler white-box baseline, using an MLP to train a mapping from concatenated hidden features to forget_labels and obtaining a similar metric based on equation 2, might reduce complexity. It would be interesting to see if your proposed method outperforms this baseline.

3. One benefit claimed by the author is that the proposed metric exhibits a low standard deviation. However, this seems to hold true only when the number of forgettings is low, as demonstrated in Table 1.

4. The experiments comparing IDI with white-box MIA should be expanded and included in the main manuscript rather than the appendix to allow for a fair comparison.

5. Regarding Membership Inference Attacks (MIAs), only score-based MIA is employed, while Likelihood Ratio Attack (LiRA) [1] is not.

6. There lack of literature on auditing machine unlearning.

### Questions
1. Could you explain why the sum of absolute values is not used when calculating Equations (1) and (2)?

2. Is there any possibility of encountering a near-zero denominator during the calculation in Equation (2)?

3. Could you provide a comparison of the effectiveness of computing mutual information for just the last few layers versus all layers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigate the shortcomings of current white-box unlearning evaluation method. The author use an example in class-wise unlearn to illustrate the residual information in the model. Then, they analyze the InfoNCE loss and propose the new white-box evaluation metrics called IDI. To better evaluate the model, the author proposes COLA. The extensive experiment results show the new evaluation metrics can evaluate the residual information in the model better.

### Strengths
- The topic itself is really interesting and necessary for MU.
- The experiments and plots are detailed and promising.
- The baseline method selection is relatively complete and the description of the method is complete.

### Weaknesses
 - The references need revision. For example, Model sparsity can simplify machine unlearning is the paper from NeurIPS 2023 and the author list is incorrect. 
- What MIA is used? May I ask the reason for choosing this MIA over the others, like the MIA in [2]? I guess the MIA used here is based on [1].  
- In addition to the proposed evaluation metrics, it would be more promising if the author can report 
- The existing metrics like UA, TA, which is not perfect. There are still some metrics, like ZRF [3], AUS [4], etc. Since the author wants to introduce a new and better evaluation metrics, a complete overview for the existing metrics should be necessary.
- The introduction of the proposed evaluation metrics is a little bit hard to follow because of the notation mass. For example, there are several weights in this paper, like $\theta$, $\nu$, $\eta$. Maybe a notation table can make everything clear.
- The performance in Table 1 is useful for the reader to connect your proposed method with the existing metrics. However, I wonder why there is no such a table for random forgetting.
- More baselines like Boundary Unlearning [5] should be added.
- What is your point of using HD to support your argument the black-box is insufficient? Why do you think the change in most of the parameters is a good sign of unlearning? And why do treat HD as a good method to illustrate your opinion. From my perspective, there are some probabilities that the information is controlled by the key parameters, where is those in last layer in your example. 
- From the practical perspective, I wonder whether the meaning of this work will be decreased as long as the evaluation is mostly based on the output.
- What is the meaning of $g_{n_l}(0)$ and $g_{n_l}(1)$? What is the output? Could you please give an example?
- In Table 1, there are both positive and negative IDIs. Is there any difference between the positive and negative value? 
- It seems that the proposed method needs some training. Could you please present the testing time of the proposed method?
- In the sentence of Line 358,

### Questions
- What is your point of using HD to support your argument the black-box is insufficient? Why do you think the change in most of the parameters is a good sign of unlearning? And why do treat HD as a good method to illustrate your opinion. From my perspective, there are some probabilities that the information is controlled by the key parameters, where is those in last layer in your example. 
- From the practical perspective, I wonder whether the meaning of this work will be decreased as long as the evaluation is mostly based on the output.
- What is the meaning of $g_{n_l}(0)$ and $g_{n_l}(1)$? What is the output? Could you please give an example?
- In Table 1, there are both positive and negative IDIs. Is there any difference between the positive and negative value? 
- It seems that the proposed method needs some training. Could you please present the testing time of the proposed method?
- In the sentence of Line 358,

### Soundness
3

### Presentation
3

### Contribution
2

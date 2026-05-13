# Why Fine-Tuning Struggles with Forgetting in Machine Unlearning? Theoretical Insights and a Remedial Approach

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Machine Unlearning has emerged as a significant area of research, focusing on 'removing' specific subsets of data from a trained model. Fine-tuning (FT) methods have become one of the fundamental approaches for approximating unlearning, as they effectively retain model performance. However, it is consistently observed that naive FT methods struggle to forget the targeted data. 
In this paper, we present the first theoretical analysis of FT methods for machine unlearning within a linear regression framework, providing a deeper exploration of this phenomenon. We investigate two scenarios with distinct features and overlapping features. Our findings reveal that FT models can achieve zero remaining loss yet fail to forget the forgetting data, unlike golden models (trained from scratch without the forgetting data). This analysis reveals that naive FT methods struggle with forgetting because the pretrained model retains information about the forgetting data, and the fine-tuning process has no impact on this retained information.
To address this issue, we first propose a theoretical approach to mitigate the retention of forgetting data in the pretrained model. Our analysis shows that removing the forgetting data's influence allows FT models to match the performance of the golden model. Building on this insight, we introduce a discriminative regularization term to practically reduce the unlearning loss gap between the fine-tuned model and the golden model.
Our experiments on both synthetic and real-world datasets validate these theoretical insights and demonstrate the effectiveness of the proposed regularization method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work explores a known issue with naïve fine-tuning approaches for the machine unlearning problem: it struggles to forget the targeted data. To address this problem, the authors begin by constructing a synthetic experiment (an overparameterized linear regression model) and show that, in this case, fine-tuned weights decompose into two components—one that targets the remaining data and one that can be considered the residual from the data to forget.

Based on this decomposition, they compare two approaches that aim to reduce the unwanted component in the final solution. They find both empirically and theoretically that the approach focusing on solving for the remaining data, rather than solely forgetting the target data, performs better. This observation leads them to propose a loss function that prioritizes overall accuracy over the forgetting term. The performance of this loss is empirically evaluated on a real dataset.

### Strengths
1. The overall paper is well-structured and pleasant to read.

2. The theoretical results inspired insights into the practical effect of the real loss, which were validated on a real data example. The theoretical section is strong and insightful. Supporting empirical experiments presented alongside each step to further ground the understanding are sensible, well presented, and convey each point effectively.

### Weaknesses
1. I found the presentation of the two terms in the loss (Eq. 6), with one being the main term and the other the “regularizing term,” to be problematic. Unless I am mistaken, this distinction is artificially created by placing an arbitrary cap on the regularization scaling term $\alpha \in 0-1$, which effectively upper bounds the contribution of each term to the loss. Therefore, the second point, 2) Regularization Focus, does not represent a real difference, in my opinion, and needlessly obfuscates the work (though I appreciate the desire to differentiate from previous work). The crux of the theoretical insight is that the accuracy term should be given more importance than the unlearning term. What is the procedure to tune this $\alpha$ parameter, as it is a crucial value of the experiment? This detail is missing in the main text and should definitely be included. From my understanding, the ICE-FT is effectively the same as CE-FT with $\alpha \in [1,\infty]$ instead of being restricted to $\alpha \in 0,1$. (If that is not the case, please add an explicit formula for the ICE-FT and disregard the following comment). Related to that point, the optimal $\alpha$  value for CE-FT should then be then as close as 1 as possible. Is it the case? In figure 4b, why is ICE and CE with alpha=1 not equal?

2. The experiment on the real datasets could be improved in a few areas. First, why is only one fine-tuning baseline presented? Second, details about the tuning and training procedure are missing, which are particularly important as the authors highlighted the sensitivity to the $\alpha$ parameter, and there is no single target metric to optimize for. The presentation of the results on the real datasets could also be improved. Looking at Table 2, it is hard to see how each method performs. Showing Figure 3 for all the datasets could help for example, or using UA vs. RA curves would be more convincing than presenting point predictions in a table. Additionally, the legend in Figure 4b is hidden behind the lines and has the wrong colors.

3. Assumption 3.1 and Remark 1. I found the construction of the matrices $F$ and $R$ to be a little bit vague. Shouldn’t it have some constraints on$d_f$ and $d_r$ since they $w_{f*}$ and $w_{r*}$ are to be exact solutions to both problems? The remark really feels more like a part of the assumption (similar comments apply to Remark 2 paired with Assumption 3.3). The concept of feature overlapping should be clarified, as it has a different meaning than how it is usually used. These points should be clarified to understand the limits of the conclusions we can draw from this synthetic setup.


Minor
- The discussion after Theorem 3.2 could be clarified. The constructed example is a scenario where the weights learned from the different tasks are completely orthogonal to each other, so the fine-tuning step is performed in a totally unrelated space. This is a great illustrative example to showcase how fine-tuning cannot affect the performance on the initial task. However, this is very specific to this particular crafted setting with extreme overparameterization. Therefore, it doesn’t really “suggest that the fine-tuning model is unable to forget the information it previously acquired from…” in general; it applies only to that particular model. Discussing the relations to the setup from Ding et al. (2024) would be interesting.

- The discussion following Theorem 3.2 and Theorem 3.4 feels somewhat repetitive, as the same points are made. You could instead focus more on discussing the differences between the two.
- There is no reference in the main text to the appendix.
- The norm in Eqs. 1, 2, and 3 is undefined.
- The point that "we favor the principle that regularization should prioritize remaining accuracy over unlearning accuracy" should be made before presenting the loss. Without it, the loss feels somewhat disconnected from the previous section.
- Consider introducing UA and RA earlier (perhaps as part of the problem description), as you present various results before their formal introduction.

Typos and small details/suggestions.

- (13), (38) (109), and a few others… typo inverted bracket ‘removing’ -> `removing’.
- Table 1:  FT (Fine-Tuning) Methods. -> FT (Fine-Tuning) Method ?
- In Section 2, overparameterized linear regression should be defined when it is introduced (n<<d). (also typo overparamterized)
- You could define RL and UL with mathematical notation as they are introduced.
- Theorem 3.2 , missing reference to the proof in the appendix after the  theorem statement.
- Font of Figure 1 are too small.
- Introduce the notation $y’$ as a wrong label to before Eqn. 6.
- You can drop the line ``The evaluation metrics include Unlearning Accuracy (UA), MIA-Efficacy, Retaining Accuracy (RA), Test Accuracy (TA), and RunTime'' in Table 2 caption to save space.

### Questions
1. For Figure 2a and the accompanying discussion and conclusions, it is important to note the fraction of overlapping features, as it likely has a significant impact on these aspects. Could you comment on this point?

2. Line 413: “Notably, the regularization parameter is typically constrained to the range (0, 1].” What is notable about that? Could you clarify the point of this comment? I couldn’t find any reference in (Fan et al., 2023) to bounding this parameter to that range.

3. Why is UA–RA more important than RA–TA? UA seems to relate to the training set.

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
The paper focuses on the fine-tuning based unlearning scheme, where approximate unlearning is obtained by performing additional learning steps with samples from the retained set to induce "catastrophic forgetting" of the forget set in the model. To understand failure of this technique, the paper considers the linear models and a couple of simplistic data sets where the set of non-zero features of the retain set (i) do not overlap, or (ii) partially overlap with that of the forget set. In both these cases, the theoretical results demonstrate that the fine-tuned based unlearned model (under a specific version of fine-tuning) has very different performance on the forget set compared to the gold standard unlearned model (which is retrained from scratch using only the retain set). Based on these results, the paper discusses a modification to the fine-tuning based unlearning scheme (the paper states them as forms of regularizations) where we are able to reset the parts of the model corresponding to the set of features that are only non-zero on the forget set, and demonstrates how this procedure improves unlearning performance. Based on these insights, the paper motivates the use of a fine-tuning objective for unlearning that combines both unlearning/forget accuracy and accuracy on the retain set, and empirical evaluations highlight how this combined objective improves the unlearning performance of fine-tuning while also maintaining high performance on the retain set.

### Strengths
I think one of the main strengths of this paper is the focus on the fine-tuning based unlearning schemes which have (in general) various advantages such as being relatively very efficient, and not requiring the forget set for the unlearning, which has significant practical implications.

### Weaknesses
- (W1) The paper lacks a clear connection between the theoretical "regularizations" proposed in Sections 3 and 4 and the empirical evaluations in Section 5. The proposed regularizations, along with their motivating theoretical analyses, necessitate knowledge of distinct and overlapping features, which is often unavailable in practical scenarios. Consequently, these regularization schemes are impractical. The paper fails to establish a clear link, even motivationally, between the theoretical analysis and the combined objective of unlearning/forget accuracy and retain accuracy.

- (W2) The novelty of the combined loss function for fine-tuning based unlearning is questionable. The paper acknowledges that this combined objective has been explored previously, but it attempts to differentiate between treating a term as an "objective" versus a "penalty." However, the distinction between a penalty term and the main objective in equations (6) and (7) is not convincing. Varying $\alpha$ would yield different outcomes, and there's no inherent need to restrict $\alpha \in [0,1]$. Both can often be expressed as $\lambda (\text{Retain Loss}) + (1 - \lambda) (\text{Forget Loss})$ for some $\lambda \in [0,1]$, treated as a single hyperparameter ranging from focusing on retain set loss to forget set performance. Thus, CE-FT and ICE-FT appear identical. The primary difference between (I)CE-FT and KL-FT is using KL divergence instead of cross-entropy to penalize forget set performance. Any differences between KL-FT and (I)CE-FT, if they exist, should be attributed to the use of KL divergence.

- (W3) The evaluated methods, KL-FT and (I)CE-FT, require access to the forget set, unlike vanilla FT. This negates one advantage of FT-based fine-tuning. A more comprehensive evaluation across various schemes, including efficient ones like Gradient Ascent and influence function-based schemes, is warranted. However, given the lack of a novel "method" (see W2), a thorough evaluation seems unnecessary.

### Questions
- (Q1) Forgetting in linear regression (considered in Sections 3 and 4) would be similar to random data forgetting in classification. What is a "class-wise forgetting" equivalent in the regression setup?
- (Q2) All the evaluations are performed on class-wise forgetting while the theoretical analysis is performed for regression. Is there a reason for why the random forgetting scenario is not considered in the evaluations?
- (Q3) For the results in Table 2, where we have multiple unlearning metrics, how is the hyperparamter $\alpha$ selected for (I)CE-FT and KL-FT?
- (Q4) If hyperparameter optimization is done appropriately (as mentioned above), the main difference between KL-FT and CE-FT from (unmasked) SalUn is the use of KL instead of CE with the forget set. Is there any reason / intuition why we should expect KL divergence based forget set penalty to perform better in terms of all the unlearning metrics compared to the cross-entropy based forget set penalty (that is (I)CE-FT vs KL-FT)?
- (Q5) In the overparameterized regime, the optimal solution to the learning problems (1)-(3) are not necessary singleton sets. Is there any reason we expect the $\arg \min_{\mathbf{w}}$ to be a singleton set and not a set of solutions? If it is in fact not guaranteed to be a singleton set, how does that affect unlearning results in this paper?
- (Q6) In the overlapping feature case, if $d_{\text{lap}} = d$, (that is, full overlap of features) what happens to the bounds? In this case, is there any provable difference between $L(\mathbf{w}_t, D_f)$ and $L(\mathbf{w}_g, D_f)$?

### Soundness
3

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
3

### Summary
This paper works on why the current fine-tuning unlearning method cannot perform well in many unlearning tasks. This paper provides a theoretical analysis within a linear regression framework to show when fine-tuning retains model performance on remaining data, it cannot fully remove the influence of the forgetting data. Then this paper proposes a discriminative regularization term to close the performance gap between fine-tuned model and retrained model. The experimental results validate the effectiveness of this approach in improving unlearning accuracy.

### Strengths
1. The topic of this paper is quite interesting. The fine-tuning approach is one of the mainstream approaches to unlearning. However, such methods are usually unstable across different unlearning tasks and datasets. Thus, the research on why it can fail is meaninful.
2. This paper provides a theoretical analysis of the linear regression model for the analysis.
3. The experimental results can clearly show the performance improvements compared with the other fine-tuning methods.

### Weaknesses
The total contribution of the paper is not enough:  

1. Theoretical Analysis: Target on theorem 3.2 and 3.4: this paper claims that the MSE on remaining data and forgetting data keep 0 during fine-tuning for overparameterized models. However, in real-world datasets, the model cannot fit the training data perfectly, and the two theorems are hard to extend to other larger models and datasets. In addition, such analysis is based on a regression model, while the following experiment part is mainly based on classification tasks. Whether the theoretical analysis on regression can be extended to classification still needs to be proved.  The analysis relies on the assumption that overparameterized models can achieve zero training loss, which is not realistic for complex datasets. This assumption undermines the practical relevance of the theoretical findings, as it does not account for the generalization challenges and inherent limitations of real-world models. Furthermore, the theoretical analysis focuses on mean squared error (MSE), which is not directly applicable to classification tasks where cross-entropy loss is typically used. The lack of a clear connection between the theoretical framework and the experimental setup raises concerns about the validity of the conclusions drawn from the theoretical analysis.

2. Discriminative Regularization: This paper does not explicitly show the loss of Inverse CE-FT. Is it simply to remove the hyperparameter $\alpha$ from the second term to the first term? If so, I cannot find a significant difference between Inverse CE-FT and original CE-FT. In addition, regarding the loss function of KL-FT, many other methods have tried to incorporate KL loss to align the output logits [1] or interlayer embeddings [2, 3]. Therefore, the proposed Discriminative Regularization does not show any improvement compared with previous works. The description of the Inverse CE-FT (ICE-FT) loss is unclear, and the distinction between it and the original CE-FT is not well-justified. The modification appears to be a minor adjustment of the hyperparameter, which does not constitute a significant contribution. The use of KL divergence for aligning output logits has been extensively explored in prior work, and the paper fails to demonstrate any novel aspects or improvements in its application. The lack of a clear rationale for the specific design choices of the proposed regularization terms weakens the overall contribution of the method.

3. Experiment results: This paper only conducts experiments on single-class unlearning (classes 3,6 and 9). In addition, this paper only compares the proposed method with naive fine-tuning and the loss proposed in [4]. It is not sufficient to prove the effectiveness of the proposed methods. This paper can include more SOTA unlearning methods in the recent two years and compare unlearning results in more complex settings like random sample unlearning or backdoor attack unlearning. The experimental evaluation is limited in scope, focusing only on single-class unlearning scenarios. The comparison with only naive fine-tuning and a single baseline method [4] is insufficient to demonstrate the superiority of the proposed approach. The absence of comparisons with state-of-the-art unlearning methods and evaluations on more complex unlearning tasks, such as random sample unlearning or backdoor attack unlearning, limits the generalizability and practical relevance of the experimental results.

4. The technical part of this paper needs to be improved. Some notations need to be further checked, for example, $1-n_f$ in line 194.

### Questions
1.  What do the distinct and overlap features mean? Could the author give some examples to explain it?

2.  Considering that this paper mainly conducts class-wise unlearning experiments. How do different methods perform under the evaluation of relearn time [1]?

[1]  Chundawat, Vikram S., et al. "Zero-shot machine unlearning." IEEE Transactions on Information Forensics and Security 18 (2023): 2345-2354.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper investigates machine unlearning, which aims to protect user privacy by removing specific data from trained models in response to data deletion requests. The authors examine why fine-tuning often fails to fully erase targeted data. They consider over-parameterized linear regression in the case of overlapping and no overlapping features. They propose a regularization term that diminishes the role of forgetting. Experimental results on both synthetic and real-world datasets validate that this regularization approach significantly enhances unlearning performance.

### Strengths
Studying unlearning from the perspective of overparametrizied regression is a great concept. This setting (even though questionable in practice) allows to perform theoretical analyses. 

The entire concept of introducing a regularization term to unlearning is very sound and novel. 

The experimental results show improvements if such a term is included.

### Weaknesses
The setting for the analyses is simplistic. It would be great to consider more general cases (for example strongly convex). 

I think the vast majority of the practical cases consider 100% overlapping cases which puts in question the bulk of the analyses. 

The distinct features section is a special case of the overlapping section and thus it should be omitted. I think the distinct features results are not stronger and thus they are a 'strict' special case. 

Option B is 'void' if all of the features are overlapping which captures the majority of the use cases.

### Questions
1. Why bothering with the case of non overlapping features? While such cases sometimes occur in FL they are a much more seldom occurrence in standard ML. 
2 Can the analyses be done for the strongly convex case? It seems it would require a completely different approach since a closed form expression is not available in such a case. What about a 2 layer linear network?

### Soundness
3

### Presentation
4

### Contribution
3

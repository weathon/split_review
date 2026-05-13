# Multi-scale Minimal Sufficient Representation Learning for Domain Generalization in Sleep Staging

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Deep learning-based automatic sleep staging demonstrates strong performance as a promising solution for diagnosing sleep disorders. However, deep learning models often struggle to generalize on unseen subjects due to variability in physiological signals, resulting in degraded performance in out-of-distribution scenarios. To address this issue, domain generalization approaches have recently been studied actively to ensure generalized performance on unseen domains during the training. Among those techniques, contrastive learning has proven its validity in learning domain-invariant features by aligning samples of the same class across different domains. Despite its potential, many existing methods are insufficient for extracting truly domain-invariant representations, as they do not explicitly reduce domain-relevant information embedded in the features. In this paper, we argue that addressing superfluous information is a key to bridging the domain gap. Furthermore, existing methods often neglect the multi-scale nature of sleep signals, potentially missing important temporal and spectral characteristics. To address these limitations, we propose a novel Multi-Scale Minimal Sufficient representation learning (MSMS) framework, which effectively reduces domain-relevant information while preserving essential temporal and spectral features for sleep stage classification. We evaluate our method on publicly available sleep staging benchmark datasets, SleepEDF-20 and MASS. Experimental results demonstrate that our approach consistently outperforms state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed domain generalization method for sleep staging analysis automatically. The main way to learn domain-invariant features are through contrastive learning however the problem of existing methods is unable to reduce domain relevant information embedded in the features. In addition, the claimed challenge is existing methods neglect multi-scale nature of sleep signals, missing temporal and spectral features. The paper proposes a multi-scale minimal sufficient representation learning framework. This framework has two functions, including the domain-relevant information reduction; and the temporal and spectral features for sleep stage classification.

### Strengths
-	The method and theorem seem correct
-	The writing and organization seem clear

### Weaknesses
-	One of the two main issues is the unclear motivations. In the introduction, especially the fig1a and 1b, it is ambiguous and unclear to understand your proposals. The provided figures, intended as illustrative examples, do not adequately convey the complexities of domain generalization in sleep staging. Specifically, the method for estimating genuinely domain-invariant representations is not clearly defined. How do you quantify the "domain-relevant information" supposedly embedded within the features? This requires a rigorous mathematical formulation or empirical evidence beyond the presented toy examples. A clear definition and computational method for identifying and isolating these representations are crucial for understanding the proposed approach.

-	The second of the two main issues is in the novelty. The proposed framework heavily relies on the information bottleneck principle combined with contrastive learning, both of which are well-established techniques in machine learning. While the application to sleep staging is novel, the core methodology appears to be a direct adaptation of existing methods. The paper lacks a detailed discussion on how the specific characteristics of sleep staging are incorporated into the method design. For instance, how does the model account for the unique temporal and spectral patterns associated with different sleep stages? Merely applying existing techniques to a new domain without significant methodological innovation raises concerns about the overall contribution.

-	Furthermore, the paper does not adequately address how the proposed multi-scale approach specifically handles the challenges of sleep staging. While the concept of multi-scale analysis is mentioned, its concrete implementation and its advantages over existing sleep staging methods are not thoroughly discussed. How does the multi-scale framework capture the transitions between sleep stages, which often involve subtle changes in signal characteristics?

### Questions
see weaknesses and answer please item by item.

### Soundness
3

### Presentation
2

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
This paper solves the domain adaptation problem in the context of sleep stage classification using EEG. In particular, the authors proposed  a Multi-Scale Minimal Sufficient representation learning (MSMS) framework that reduces domain-relevant information while preserving essential temporal and spectral features. Evaluations are conducted on publicly available sleep staging benchmark datasets, SleepEDF-20 and MASS to demonstrate the effectiveness of the proposed method.

### Strengths
* This problem the authors aimed to solve is practical.
* This paper is easy to follow.

### Weaknesses
 * a) Limited novelty. Although the authors spent majority of the space talking about mutual information (MI) and superfluous information. They ended up adding an extra term of domain conditioned entropy in addition to the well known contrastive loss. Adding regularisation in the context of domain adaptation is not new. For instance, Domain-Adversarial Neural Networks (DANN) added an inverse gradient to confuse features extracted from two domains. The so called MULTI-SCALE is essentially applying contrastive loss to intermediate features which is not new in both contrastive learning or domain adaptation.

* b) Poor clarity. The authors spent too much space on MI which is in the end intractable. Instead, the authors should put more focus on describing the details of how exactly their framework works. For instance, it seems that the proposed framework is a dual-stage framework, how is the second stage trained and using what data ? How is H(z|d) calculated? What is the network structure used ? 

* c) Marginal improvement. As seen in Table 1, on SleepEDF-20, the improvement over the second best approach is 0.4%. On MASS, the improvement is 0.3%. 

* d) Insufficient ablation studies. The authors proposed two novelties in this work, a regularisation term and the application of the loss function (which layers). These should be studied individually to see the contribution of each.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a new sleep staging method based on contrastive learning called MSMS. This method is inspired by the model SleepPyCo and tries to remove superfluous information from the representation of samples. This should help to reduce the domain shift in the data. The paper proposes several experiments on two classical sleep staging datasets to show the benefits of their methods over competitors.

### Strengths
- The paper tries to tackle the distribution shift in sleep staging, which is a crucial issue in the biosignal field. 
- The illustrative figures look nice.

### Weaknesses
 - Figure 1 is a bit hard to understand when not reading the paper
- The paper, in general, lacks clarity.
- Related work is unclear. The authors didn't appropriately introduce the basis of contrastive learning, making understanding their paper hard.
- The notation is a bit messy. For example, in the notation part (which should be before related work), $D_m$ represents all samples for one domain, while after $D$ seems to represent the concatenated domains. After that $D_m$ is never used.
- If adapting between subjects could be challenging, there is a more significant distribution shift between datasets. Several papers deal with adaptation between datasets [1, 2, 3]. Using sleep staging for domain generalization without generalizing it to another dataset does not seem engaging.

### Questions
- Why did you choose this architecture for your model? Does already existing work inspire you?
- The results of MSMS are slightly above other methods. Did you do a statistical test to see if the improvement is significant?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a domain generalization method for sleep stage prediction, multi-scale minimal sufficient representation learning (MSMS).
The basic approach of MSMS is learning domain-invariant representation as existing domain generalization methods.
This paper argues that the representations learned by existing methods still contain domain-relevant information called superfluous information.
Thus, the proposed method explicitly incorporates the superfluous information into the objective.
Another idea of the proposed method is learning domain-invariant representation in the final encoder output space and intermediate feature spaces because capturing multi-scale characteristics of sleep signals is important in sleep stage prediction.

### Strengths
- S1: The motivation is clear and easy to understand.
- S2: Introducing the superfluous information is interesting.

### Weaknesses
 - W1: The effectiveness of superfluous information minimization in the proposed method is not thoroughly justified. While the final loss function in Eq. (10) incorporates terms related to $I(z_i;d_i)$ and $I(z_i;v_p)$ from Eq. (3), it is unclear how the magnitude of $\alpha$ directly impacts the minimization of superfluous information. A more detailed analysis of the relationship between $\alpha$ and the superfluous information, potentially through quantitative measures, would strengthen the claim.

- W2: The roles of $I(z_i;d_i)$ and $I(z_i;v_i|v_p)$ are not clearly distinguished, despite both being described as domain-relevant information. An ablation study specifically isolating the effects of these two terms is necessary. Given the potential correlation between superfluous information and $I(z_i;d_i)$, the study should demonstrate the efficacy of using both terms, not just $I(z_i;d_i)$ alone. For instance, visualizing the feature space using t-SNE with and without each term could reveal their individual contributions to domain generalization.

- W3: The paper lacks a comparison with empirical risk minimization (ERM), which involves merging datasets from all domains and training in a supervised manner without domain labels. Including this baseline is crucial, especially considering the findings by Gulrajani et al. [1] suggesting that ERM can be a strong baseline when experiments are carefully designed. This comparison would provide a more comprehensive evaluation of the proposed method's performance.

- W4: The derivation of the minimal sufficient representation learning would benefit from a graphical model illustrating the relationships between ${x}, {v_1}, {v_2}, {z_1}, {z_2}$. This visual representation would significantly improve the understanding of the proposed framework and the interactions between its components.

- W5: The paper does not provide quantitative measures of superfluous and domain-relevant information in Tab. 1. Including these metrics, even if estimated, would offer a more concrete evaluation of the method's ability to minimize superfluous information and retain domain-relevant information. This could involve using techniques like the von Mises-Fisher distribution for estimating mutual information, especially for contrastive learning-based methods.

- W6: The description of the proposed method lacks sufficient detail regarding the computation of $H(z_i|d_i)$. Providing a step-by-step procedure, including how this term is empirically estimated, would significantly improve the paper's reproducibility. For example, detailing the use of the Stein gradient method, as mentioned in the response, would be beneficial.

- W7: Although $\lambda_1$ is set to 1 to neglect $H(z_i)$ in Eq. (25) for deriving Eq. (4), the paper does not explore the effect of varying $\lambda_1$. Conducting experiments with different $\lambda_1$ values and analyzing their impact on the model's performance would provide valuable insights into the sensitivity of the proposed method to this parameter.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

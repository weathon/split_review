# Hierarchical Gaussian Mixture Normalizing Flows Modeling for Multi-Class Anomaly Detection

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Unified anomaly detection (AD) is one of the most valuable challenges for anomaly detection, where one unified model is trained with normal samples from multiple classes with the objective to detect anomalies in these classes. For such a challenging task, popular normalizing flow (NF) based AD methods may fall into a ``homogeneous mapping'' issue, where the NF-based AD models are biased to generate similar latent representations for both normal and abnormal features, and thereby lead to a high missing rate of anomalies. In this paper, we propose a novel \textbf{H}ierarchical \textbf{G}aussian mixture normalizing flow modeling method for accomplishing unified \textbf{A}nomaly \textbf{D}etection, which we call HGAD. Our HGAD consists of two key components: inter-class Gaussian mixture modeling and intra-class mixed class centers learning. Compared to the previous NF-based AD methods, the hierarchical Gaussian mixture modeling approach can bring stronger representation capability to the latent space of normalizing flows. In this way, we can avoid mapping different class distributions into the same single Gaussian prior, thus effectively avoiding or mitigating the ``homogeneous mapping'' issue. We further indicate that the more distinguishable different class centers, the more conducive to avoiding the bias issue. Thus, we further propose a mutual information maximization loss for better structuring the latent feature space. We evaluate our method on four real-world AD benchmarks, where we can significantly improve the previous NF-based AD methods and also outperform the SOTA unified AD methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of multi-class anomaly detection using normalizing flow-based generative modeling. They address the issue of "homogeneous mapping" where latent representations corresponding to both normal and anomalous inputs could map to the same isotropic Gaussian distribution. This hinders the ability of the model to detect anomalous inputs. They propose to model the latent distribution using a Gaussian mixture, with one or multiple Gaussian components corresponding to each class, which improves the flexibility of the model. Further, they design specific loss functions to ensure that the latent Gaussian distributions corresponding to distinct classes are well separated.

### Strengths
1. Addresses an important limitation of normalizing flow-based anomaly detection methods which typically assume that the latent distribution is the standard Gaussian. Here, they motivate and explore a class-conditional Gaussian mixture distribution for the latent variable, which increases the flexibility of the model and can improve the anomaly detection performance.

2. Experiments are fairly extensive and compare with multiple recent baselines.

### Weaknesses
1. The proposed method requires labeled training data, which is not usually available in anomaly detection problems. The method hinges on knowledge of of the number of classes so that in the latent space each class is modeled with either a single Gaussian or a mixture. Since some of the compared baselines do not have use this label supervision, the comparison might be unfair.

1. The overall training objective and its individual losses are not well motivated and connected together. It's not clear why the entropy based loss is needed in Eqn 9. What exactly is the entropy being estimated here and why is it not covered by the mutual information loss? In the final objective (Eqn 11), why are only two of the terms scaled by a hyper-parameters?

1. Several issues with the notations and writing which make it hard to follow. For instance:
    - In Algorithm 1: What is meant by $\mu_y \leftarrow \mathbf{y}$? On line 3, it is denoted as $x \in X^k$, but $X^k$ is not the set of all feature maps. 
    - In Eqn 5, the Gaussian is denoted by $\mathcal{N}(\mu_y, \Sigma_y)$ and by $\mathcal{N}(z ; \mu_y, \Sigma_y)$ in the same line. 
    - In Eqn 8, it is not clear what $y'$ is and therefore what $c_{y'}$ is. Same comment for Eqn 9. 
    - The anomaly score function in section 3.4 is not clear. What is meant by $max(\sum_{k=1}^K P_k)$? Also, why is this form chosen for the score function? 
    - Referring to the last line of page 3, why is the anomaly score defined as 1 minus the probability density (which could be greater than 1)? One could simply use the log-likelihood (or its negative) as the anomaly score. 
    - In page 3, the Jacobian is defined like the gradient and it's actual expansion is never discussed in the paper. I realize that this is a standard expression for flow-based models, but it should be mentioned for clarity. 
    - The need for positional encoding is not clearly explained.

### Questions
Please see my comments and questions under Weaknesses. 

It is important to clarify in the problem setting that labeled training data are required.

A key prior work which models the latent distribution using a Gaussian mixture is not discussed. \
Semi-Supervised Learning with Normalizing Flows: 
https://proceedings.mlr.press/v119/izmailov20a/izmailov20a.pdf

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of *supervised* *multiclass* anomaly detection, where the "normal" samples may belong to a pre-defined set of classes Y, and the goal is to detect anomalous samples that do not belong to any class in Y. The authors point to drawbacks with prior reconstruction-based and normalizing-flow (NF) based approaches to multiclass anomaly detection. They then propose a new approach for alleviating these drawbacks by building on existing NF-based methods replacing their unimodal Gaussian prior with a hierarchical Gaussian mixture prior. Experimental results and ablation studies demonstrate that the proposed approach is better on average compared to prior methods.

### Strengths
- Extending existing NF-based approaches with a mixture of Gaussian prior looks like a natural approach to take for multiclass anomaly detection
- Fairly extensive experimentation with ablation studies that attempt to show the role of individual loss components

### Weaknesses
- One of my main concerns is that most of the methods compared to (e.g. UniAD, FastFlow, etc) are *unsupervised* whereas the proposed method is a *supervised* approach explicitly requiring class labels to be provided (see e.g. discussion in Appendix A.1). On the face of it, this does not seem like a fair comparison to make. It is important that the authors explicitly summarize what supervision each method uses and justify why theirs is a better approach despite requiring explicit label information to be provided during training.

- The writing and presentation is at places hard to follow. The authors are urged to present the high-level approach first before dwelling into the details of the individual loss components. Having an explicit pseudo-code stating what the supervision is for the algorithm, and how the overall optimization objective looks like would be very helpful.

- The proposed approach appears to have a lot of moving parts: there are four loss components (one for a inter-class Gaussian mixture, one for an intra-class Gaussian mixture, a mutual information based and an entropy-based loss for class diversity), with two hyper-parameters for weighting them (Appendix C). Although the authors do conduct some analysis of different hyper-parameter combinations, one if left with a feeling that the approach is highly heuristic in nature, with the gains coming largely from heavy engineering effort. Improving the writing and presentation may help boost the reader's confidence in the proposed method.

### Questions
Of the methods discussed, it appears that BGAD is supervised, but not compared to. Are there other methods you compare to in experiments which like your method are also supervised?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a normalizing flow model with hierarchical Gaussian mixture prior for unified anomaly detection, HGAD. This method achieves the SOTA unified AD performance on four datasets.

### Strengths
1. The analysis and discussion of the proposed model are detailed.

2. The experiment results are superior to the comparison methods. 

3. The experiments in both the formal paper and appendix are relatively thorough.

### Weaknesses
1. The abstraction is somewhat lengthy. Please polish the abstraction and make it concise.

2. The size of coordinate/legend in Figure 2 is too small to recognize.

3. The representation should be improved to be more professional. The explanations of some equations (eg. Eq6 and Eq9 ) are not easy-understood.

### Questions
1. Is the homogeneous mapping issue intrinsically equal to the well-known identical shortcut problem?

2. The citations might be wrong. Many citations should be placed in the brackets. Please pay attention to the difference between '\citep' and '\citet'.

3. The full name of HGAD should be listed.

4. Why the performance of multi-class case is lower than the unified case, as shown in Table 1.

5. The best performance on MVTec in Table 1 are 98.4/97.9, but 97.7/97.6 in Table 3.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a normalizing flow-based unified anomaly detection method, i.e., Hierarchical Gaussian Anomaly Detection (HGAD). By designing a loss function, the proposed method attempts to handle the intra-class diversity and inter-class separation.

### Strengths
* The proposed method can model normalizing flows with hierarchical Gaussian mixture priors on the multi-class anomaly detection task.
* The design of the proposed method can model the inter-class Gaussian mixture priors, learn class centers, and maximize mutual information.

### Weaknesses
* The presentation and the layout of the manuscript are bad. For examples,
  * Figure 2(b)/(d): The authors need to clarify the colors associated with the classes.
  * What are the $\lambda_1, \lambda_2$ in Section 4.2? It is confusing that the authors list several separate loss functions in Section 3.3 without any articulation about how to deal with these equations to achieve the goal(s). I finally found the objective function of the target goal after checking with the appendix, but the authors didn't mention anything in the main paper.
  * In Section 3.4: What did the authors mean by level-k? Additionally, since there is no access to the label in the test, which $y$ in $\mu_i^y$ will be used for the test point?
  * The limited explanation between problem formulation and the experiment setup: 
    * In Section 3.2, since the authors pointed out that Eq. (2) is used to maximize the log-likelihood of normal features, why do the normalizing flows present a large log-likelihood for both normal and abnormal features? In other words, are both normal and abnormal/anomaly observations used in this loss function?
    * In Section 4, what is the partition for the data in experiments? What are the normal classes? What are the anomaly classes? If label information (including anomalies) is used in the training, why do we call this multi-class anomaly detection? What is the difference between this with the regular multi-class classification?

* Since there are multiple goals contained in the objective function and different training strategies in the experiments, to clearly summarize the work, it would be better to use pseudocode to outline the algorithm.

* The weak support of the necessity of the intra-class centers: From Figure 3(b), I cannot see there is a significant difference among different numbers of intra-centers.

### Questions
* Section 3.1: Why $p_\theta$ is a probability rather than a density? If it is a density function, why did the authors subtract that from 1 (any motivation)? 

* Figure 3: Why is the positional encoding added to the normalizing flow? Is this necessary? Did the authors conduct the ablation study of this design?

* Bottom in Page 5: Why do not just use sample class priors to estimate $p(Y)$? Which part of the architecture in Figure 3 is used to estimate $p(Y)$? Could the authors explain in detail?

* The notations in (8), and (9) are bad. What is $\mu\_{y^\prime}$? Do you mean the center vector? Is loss (9) necessary? Why there is no penalty cost before this loss in the final object function? Did the authors conduct the ablation study for this loss function?

* The discussion in Section 3.3:
  * Could the authors further clarify this sentence: "Because our method only explicitly uses class labels, while they implicitly use class labels (see App. A)".
  * I see one loss function is designed to maximize the log-likelihood of normal observations. Why did the author claim that using a label should not be a strict condition? Did the author conduct the experiment to support this conclusion?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

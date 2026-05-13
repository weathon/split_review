# TWO STAGES DOMAIN INVARIANT REPRESENTATION LEARNERS SOLVE THE LARGE CO-VARIATE SHIFT IN UNSUPERVISED DOMAIN ADAPTATION WITH TWO DIMENSIONAL DATA DOMAINS

- Decision: Reject
- Scores: 1, 6, 3, 1, 3

## Abstract
Recent developments in the unsupervised domain adaptation (UDA) enable the unsupervised machine learning (ML) prediction for target data, thus this will accelerate real world applications with ML models such as image recognition tasks in self-driving. Researchers have reported the UDA techniques are not working well under large co-variate shift problems where e.g. supervised source data consists of handwritten digits data in monotone color and unsupervised target data colored digits data from the street view. Thus there is a need for a method to resolve co-variate shift and transfer source labelling rules under this dynamics. We perform two stages domain invariant representation learning to bridge the gap between source and target with semantic intermediate data (unsupervised). The proposed method can learn domain invariant features simultaneously between source and intermediate also intermediate and target. Finally this achieves good domain invariant representation between source and target plus task discriminability owing to source labels. This induction for the gradient descent search greatly eases learning convergence in terms of classification performance for target data even when large co-variate shift. We also derive a theorem for measuring the gap between trained models and unsupervised target labelling rules, which is necessary for the free parameters optimization. Finally we demonstrate that proposing method is superiority to previous UDA methods using 4 representative ML classification datasets including 38 UDA tasks. Our experiment will be a basis for challenging UDA problems with large co-variate shift.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes a two-stage domain invariant representation learning method to address large co-variate shifts in unsupervised domain adaptation. The approach uses intermediate, unlabeled data to create smoother transitions between source and target domains, aiming to enhance classification performance under challenging conditions. The authors claim their method outperforms existing UDA models, especially when co-variate shifts are significant.

### Strengths
The idea of utilizing intermediate data to smooth the domain adaptation process sounds reasonable.

### Weaknesses
1. Poor clarity and organization. The paper is challenging to read, with many grammatical errors, convoluted language and unclear explanations of the methodology.
2. Lack of rigorous validation: The theoretical claims, especially the effectiveness of two-stage learning and parameter optimization, lack sufficient mathematical justification and empirical support. In line 62, the authors claim that "intermediate data (unsupervised) between source and target to ensure simultaneous domain invariance between source and intermediate data and invariance between intermediate and final target data". Doesn't this imply the source and target data are domain invariant as well?
3. The text is verbose and repetitive, making it difficult to extract key insights and understand the novelty compared to prior methods.

### Questions
See weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a two-stage domain-invariant representation learning approach for UDA under large co-variate shifts. It uses intermediate unsupervised data to bridge the gap between source and target domains. Additionally, a theoretical framework is proposed for parameter tuning without requiring target labels.

### Strengths
The paper addresses a critical limitation in UDA by focusing on large co-variate shifts in two-dimensional data domains, which are common in real-world applications such as autonomous driving, human activity recognition.

### Weaknesses
1.  The main limitation of the proposed method is its dependency on an intermediate, unsupervised domain that is semantically related to both the source and target domains. This dataset may not always be available or feasible to collect, especially in real-world applications with limited resources. The requirement for a semantically related intermediate domain introduces a significant practical constraint, as the process of identifying or creating such a dataset can be complex and resource-intensive. The paper does not adequately address the challenges associated with this dependency, such as the potential for domain mismatch between the intermediate domain and the source/target domains, which could negatively impact the effectiveness of the proposed method.
2. The practical application of the proposed method is not fully demonstrated. The benefits remain largely theoretical, making it hard for readers to grasp its relevance without concrete examples of its impact on model performance. The paper lacks a thorough evaluation of the method's performance on real-world datasets, and the experiments presented do not provide sufficient evidence of the method's effectiveness in practical scenarios. The absence of detailed experimental results makes it difficult to assess the method's robustness and generalizability.
3. Lacks a deep discussion that contextualizes how this approach builds upon or diverges from existing UDA methods. An analysis/experiment can be done to show how the proposed method addresses specific limitations in prior approaches, such as domain-adversarial training or correlation alignment techniques. The paper does not provide a clear explanation of how the proposed two-stage approach compares to existing methods in terms of performance, computational cost, and robustness. A comparative analysis with other UDA techniques is needed to highlight the specific advantages and disadvantages of the proposed method.

### Questions
1. How would the method perform if an intermediate, unsupervised domain were unavailable or of low quality? Are there alternative approaches, such as synthetic data generation or transfer learning, that could help mitigate this dependency? Could the authors provide guidance on selecting or creating intermediate datasets for cases where a semantically related domain is not readily available?

2. Can the authors provide specific examples or case studies to demonstrate the practical impact of the proposed parameter tuning framework on model performance? Would an experiment isolating the effects of the parameter tuning framework help clarify its practical benefits? If so, could the authors consider adding one to the paper?

3. How does the proposed method address specific limitations of existing UDA techniques, such as domain-adversarial training or correlation alignment? Could the authors provide a comparison experiment or detailed analysis that highlights the advantages and trade-offs of this two-stage approach relative to traditional UDA methods?

4. How does the proposed method handle highly heterogeneous domains where intermediate data is noisy or contains varying domain characteristics?

5. Could the authors include ablation studies to isolate the effects of each stage in the two-stage process? This might help clarify the contributions of each component in achieving domain invariance.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a simple two-stage domain adaptation method by feeding source domain, intermediate domain and target domain into the model. The intermediate domain overcomes the large covariate shift problem that is widely a challenge of domain adaptation. This paper further proposes a free parameter indicator with reverse validation strategy.


Based on the authors' feedback and other reviewers' comments, I would reduce my final rating on this work.

### Strengths
1. The two-stage domain adaptation method, i.e. two-stage DANN sound good and interesting.
2. The reverse validation based idea is interesting and not frequent in domain adaptation community.
3. The two-stage strategy can be scalable to other method such as CORAL.

### Weaknesses
1. Domain adaptation has undergo a wide study in the past decade. However, with the multimodal large language model, domain gap has been allievated from another way, such as CLIP based [1,2]. Therefore, in this submission, the impact of this proposal may be weak.
2. There lacks sufficient comparisons to previous SOTAs in recent works [3], particularly large vision-language model based and prompt based [4].
3. The writting should be further improved for easier reading.
4. Using intermediate domain as a bridge is not new because there are a wide research in DA with intermediate state [6, 7].
5. As the algorithms of 2 stage DANN shows, the intermediate domain is required. I thinks how to obtain intermediate domain is still an open question. This is not discussed.
6. Transformer based DA models should also be discussed since it has been widely used in domain adaptation [8, 9].

### Questions
1. If the reverse validation like idea is always effective?
2. This is more like a training strategy by commenting on step-by-step manner comparing to end-to-end manner.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The authors of this manuscript propose a two-stage domain-invariant representation learning method, which uses semantic intermediate data to bridge the gap between source and target domains. This method improves classification performance even under large covariate shifts by learning domain-invariant features and optimizing task discriminability through source labels. The paper also introduces a theorem for optimizing free parameters by measuring the gap between trained models and target labeling rules. The proposed method outperforms previous UDA techniques across 38 tasks in 4 representative ML datasets.

### Strengths
1. A new approach was proposed
2. It provides an automated free-parameter tuning method without needing access to target ground truth labels.

### Weaknesses
1. English was not used properly:
    a) line 52: "did not be"
    b) line 498: "It can be read that" sounds awkward.
    ...
Lots of sentences in this manuscript are not authentic, making it hard to follow the manuscript's content. I strongly recommend authors taking times to improve the presentation of this work.

2. No related works section.

3. The x, y axis labels for figure 4-6 are not easily visible.

### Questions
Use cases of the proposed methods are too limited. It was designed for two dimensional data. What if the source and target data are in high dimensional space?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses large co-variate shift problems in UDA, particularly when dealing with two-dimensional co-variate shifts. The proposed method uses an intermediate unsupervised dataset to bridge the gap between source and target domains, learning domain-invariant features simultaneously between source-intermediate and intermediate-target pairs, which helps achieve better domain adaptation compared to direct source-target adaptation. The authors also derive a theorem for measuring the gap between trained models and unsupervised target labelling rules, which helps optimize free parameters without access to target labels. The proposed method is validated on classification 4 datasets including 38 UDA tasks.

### Strengths
1. The paper introduces a novel and effective solution to a practical challenge in machine learning by using intermediate data to bridge large domain gaps.
2. The proposed method is versatile as it can be integrated with various domain invariant representation learning techniques.
3. The authors derive a theorem for measuring the gap between trained models and unsupervised target labelling rules for hyper-parameters searching.

### Weaknesses
1.	This paper requires substantial improvement in terms of writing quality and clarity of presentation. (1) Many notations are without proper definition, (e.g., D_S, \hat{y}^S_{i,j}, N appear before being formally introduced); (2) The language is frequently imprecise and contains awkward expressions that hinder understanding. I strongly recommend the authors to thoroughly revise the mathematical notations with clear definitions and improve sentence structures and word choices for greater presentation.
2.	The authors assume the existence and availability of appropriate intermediate domains that perfectly fit their "two-dimensional domain shift" framework, but do not adequately address how to identify or construct such intermediate domains in real-world applications. For example, while it is intuitive to have MNIST-M as an intermediate domain between MNIST and SVHN, in most real-world scenarios, it is unclear: (1) How to systematically identify the two dimensions of domain shift; (2) How to obtain or construct suitable intermediate domain data; (3) What to do when clean intermediate domains are unavailable or when domain shifts are more complex than two-dimensional. Without addressing these practical concerns, the proposed method may have limited applicability in real-world domain adaptation problems.
3.	The technical novelty of the proposed method is limited. The approach is essentially a straightforward extension of existing domain-invariant learning methods. It merely splits the domain adaptation loss into two components (L_domain(S,T) + L_domain(T,T')) and applying standard adversarial training techniques, which lacks novel methodological designs in terms of loss function formulation, optimization strategy, or network architecture. The paper does not provide a theoretical justification for why this specific decomposition of the domain adaptation problem is superior to other possible decompositions or why it should lead to better generalization on the target domain. Furthermore, the method does not explore the potential impact of the order in which the domain adaptation losses are applied, which could significantly affect the final performance.
4.	The proposed parameter selection method is incremental. The proposed approach is essentially a straightforward adaptation of the existing Reverse Validation (RV) method to the two-stage domain adaptation setting, without substantial methodological innovations. The paper does not provide a rigorous analysis of the theoretical properties of the proposed parameter selection method, such as convergence or optimality. It also lacks a comparison with other parameter selection methods that may be more suitable for the two-stage domain adaptation setting.
5.	The experimental evaluation of the paper is not up to current standards in domain adaptation research. The comparisons are limited to classical UDA methods like DANNs and Deep CORAL, while ignoring numerous recent advanced techniques that have shown significant improvements in handling large domain gaps. The experimental setup also lacks a thorough ablation study to analyze the impact of different components of the proposed method, such as the choice of intermediate domain or the specific domain adaptation loss.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

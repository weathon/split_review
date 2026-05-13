# Towards Out-of-Modal Generalization without Instance-level Modal Correspondence

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
The world is understood from various modalities, such as appearance, sound, language, etc. Since each modality only partially represents objects in a certain physical meaning, leveraging additional ones is beneficial in both theory and practice. However, exploiting novel modalities normally requires cross-modal pairs corresponding to the same instance, which is extremely resource-consuming and sometimes even impossible, making knowledge exploration of novel modalities largely restricted. To seek practical multi-modal learning, here we study Out-of-Modal (OOM) Generalization as an initial attempt to generalize to an unknown modality without given instance-level modal correspondence. Specifically, we consider Semi-Supervised and Unsupervised scenarios of OOM Generalization, where the first has scarce correspondences and the second has none, and propose connect & explore (COX) to solve these problems. COX first connects OOM data and known In-Modal (IM) data through a variational information bottleneck framework to extract shared information. Then, COX leverages the shared knowledge to create emergent correspondences, which is theoretically justified from an information-theoretic perspective. As a result, the label information on OOM data emerges along with the correspondences, which help explore the OOM data with unknown knowledge, thus benefiting generalization results. We carefully evaluate the proposed COX method under various OOM generalization scenarios, verifying its effectiveness and extensibility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method for Out-of-Modal (OOM) generalization, which uses a COX framework to achieve cross-modal knowledge transfer and generalization to unknown modalities. At the same time, this paper considers both semi-supervised and unsupervised scenarios. Experiments show that this method has a certain level of effectiveness.

### Strengths
1. The motivation behind this approach is clear, and studying out-of-model (OOM) generalization is meaningful.
2. The authors provide a detailed description of the proposed method, making it easy to follow and reproduce.

### Weaknesses
1. In the theoretical analysis, the paper uses $h^*$ to represent ideal optimal classifiers. However, in practice, it is difficult to find the optimal classifier. Although the authors compared the performance of ImageBind and LanguageBind, they should conduct more experiments to demonstrate the impact of using classifiers with different levels of accuracy on the final results.
2. The paper does not theoretically or experimentally explain why using the IM Perceptor is more effective than directly performing semi-supervised or unsupervised training.
3. If using the IM Perceptor indeed improves training results as mentioned in the issues above, then for the same task, would knowing more modalities enhance the generalization of OOM?
4. The paper contains numerous writing errors, such as "OMM" in line 494. Additionally, the logic of symbol definitions in the mathematical proof section is confusing, for example, using $X^O$ to represent IM data and $X^I$ to represent OOM data.

### Questions
Please see Weaknesses.

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
4

### Summary
This paper explores a novel model generalization problem, specifically focusing on out-of-modal generalization in the absence of label and modality correspondence. The authors employ a two-stage generalization approach, first constructing modality-shared information and then focusing on modality-specific information. They propose different training losses for both semi-supervised and completely unsupervised scenarios.

### Strengths
1.The problem addressed in the paper is quite novel, and the semi-supervised scenario provides valuable insights."

2.Extensive experiments are conducted to demonstrate the effectiveness of the proposed method.

### Weaknesses
1.The paper contains several typos that affect readability and need to be corrected. Regarding line 195, it seems that the symbols for IM data $ X^O$ and OOM data $ X^I$ are used incorrectly. Also in Eq.3, why is there an integral sign before $p ( X^O, X^I ) $

2.The proof in the paper lacks rigor. How is the lower bound derived from Equation 3 to Equation 4? Although the proof draws on VIB, there are still significant discrepancies.

3.Similarly, the proof in Appendix A.1 for Equation 20, which relies on the non-negativity of the KL divergence, is not sufficiently rigorous.

4.In Section 3.2, there is a lack of necessary descriptions regarding the trained model, such as the input and output of the decoder $q( X^O, X^I)$.

### Questions
1.Does the inclusion of $L_{con}$ with label $ y $ imply that exploring connections across modalities requires the use of samples with correspondence for training?

2.In a completely unsupervised setting, the feature distributions of different modalities may differ significantly. Is the choice of the anchor method reasonable in this context?

3.Could you provide a more detailed proof regarding the upper and lower bounds in Sec 3.2? 

4.In the ablation experiments, the results of removing any module are significantly lower than those of EntMin. Would applying these two losses individually on EntMin lead to improvements?

### Soundness
2

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
This work focuses on the semi-supervised and  unsupervised scenarios of *Out-of-Model* (OOM) Generalization without given instance-level model correspondence. This work proposes an OOM generalization method based on the interactive relationship between modalities, *connect & explore* (COX), in an attempt to extract the commonality that can help partially comprehend OOM data based on IM data. It introduce a variational information bottleneck framework to connect OOM data and In-Model (IM) data and extract shared information. Finally, several sets of experiments demonstrate the effectiveness and extensibility of the proposed method.

### Strengths
This work focuses on the novel and practical issues in the field of *Out-of-Model* (OOM) generalization.

This work proposes an approach that attempts to combine common knowledge based on connections across modalities with unique knowledge of OOM data based on modality disagreement.

This work conducts multiple sets of experiments to verify the effectiveness and extensibility of the proposed method.

### Weaknesses
(i) The OOM problem has also been discussed in other works, such as IB for modality missing, cross-modal generalization, etc., ([1-5] for example) but not mentioned in the paper (nor experiments). Please explain the difference between this paper and these works. [1] Unpaired image-to-speech synthesis with multimodal information bottleneck. [2] Visual explanations of image-text representations via multi-modal information bottleneck attribution. [3] Dynamic Multimodal Information Bottleneck for Multimodality Classification. [4] SimMMDG: A simple and effective framework for multi-modal domain generalization

(ii) The work mentions "prediction uncertainty" in section 4.2, but after carefully reviewing all the contents, it is hard to find the definition or description of prediction uncertainty, while without the direct description of this concept in the experiment section for verification. It is unclear how this uncertainty is quantified or used within the proposed framework. The lack of a concrete definition makes it difficult to assess the validity of claims related to uncertainty.

(iii)The work mentions "the performance of COX is affected by the quality of IM perceptors", but only contrast the performance between ImageBind and LanguageBind in the experiment section can not fully illustrate this conclusion. The comparison between only two perceptors is insufficient to establish a general trend. The paper needs to explore a wider range of IM perceptors with varying characteristics to support this claim.

(iv) Has some loopholes, e.g.,

  - Tense and grammatical errors, e.g., "OMM data" -> "OOM data"
  - Confusing notations, e.g.,"given IM data *X<sup> O </sup>*and OOM data *X<sup> I </sup>*"

Please correct the grammatical mistakes and polish them if possible.

(v) In the experimental part, the results in Table 2 and Table 3 can not adequately illustrate this conclusion "leveraging the knowledge from IM perceptors can indeed help OOM generalization compared to using OOM data alone". How do the results in Table 2 and Table 3 show the performance improvement of the proposed method compared to the methods using only OOM data? The tables lack a direct comparison to a baseline that uses only OOM data, making it difficult to isolate the contribution of IM knowledge.

### Questions
Please see 'weakness', which simply can be summarised as:

(i) What the advantages of this work vs. previous works?

(ii) What is "prediction uncertainty" described in the article and how is it reflected? 

(iii) Can the conclusion that COX performance is affected by quality of IM perceptors be fully explained based on the final performance results of only two IM perceptors, ImageBind and LanguageBind? What are the quality differences between ImageBind and LanguageBind reflected?

(iv) How do the data in Table 2 and Table 3 reflect that leveraging the knowledge from IM perceptors can indeed help OOM generalization compared to using OOM data alone?

(v) There are some grammatical errors and confusing notations in the article. Can it be further polished and revised?

### Soundness
3

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
This paper addresses the problem of out-of-model (OOM) generation and proposes a novel technique, COX. The authors perform experiments on five datasets, comparing their method with several baseline approaches.

### Strengths
The problem statement is clear.

### Weaknesses
Insufficient and weak baselines: I am especially concerned the proposed approach's performance compared with SSL.

Some notations should be improved, and a few detailed explanations should be added.

From my understanding, the authors consider a scenario where the training data consists of two parts: IM, where both inputs and labels are available, and OOM, where only inputs are provided without any labels (unsupervised case), and only a limited amount of labeled data is present. Please correct me if I’m mistaken, but it seems that no data contains both IM and OOM inputs. In other words, there is no data where the pair (x1, x2)—representing two modalities—is known.

If the above assumption is correct, how do we sample from the joint distribution p(xO | xI)p(xI) in Equation (6)?

I find the assumption stated below Equation (1) too strong. It implies that the proposed method only applies when xO can be directly inferred from xI. For example, let’s assume a1 = a2 = a, representing the sound of a dog barking, and b1 and b2 represent images of a golden retriever and a border collie, respectively. V is a constant vector, and Y represents the class "golden retriever." While it is true that P(V|xI=a1)P(Y|xI=a1) = P(V|xI=a2)P(Y|xI=a2), given that a1 = a2, we see that P(V,Y=is_golden_retriever|xO=b1, xI=a1) does not equal P(V,Y=is_golden_retriever|xO=b2, xI=a2).

In Line 255, do h1* and h2* refer to the classifiers corresponding to modality 1 and modality 2, respectively? If so, how can they be applied to xO, which belongs to a different modality?

The baselines should be reconsidered, especially by including stronger baselines. For instance, there are many state-of-the-art semi-supervised learning (SSL) approaches, and simply adding Gaussian perturbations to the input may not be sufficient. Stronger SSL baselines are crucial, as otherwise, it could be argued that using SSL alone is enough, which raises the question, why COX? Additionally, the 'Random' baseline is too simplistic, effectively leaving the unsupervised setting in Table 2 with only one baseline.

Furthermore, for the semi-supervised case, it is not surprising that the baseline performs worse, given the very limited amount of labeled data used for training.

I would like to bring [1] to the authors' attention, which could be helpful for better understanding multimodality:

### Questions
From my understanding, the authors consider a scenario where the training data consists of two parts: IM, where both inputs and labels are available, and OOM, where only inputs are provided without any labels (unsupervised case), and only a limited amount of labeled data is present. Please correct me if I’m mistaken, but it seems that no data contains both IM and OOM inputs. In other words, there is no data where the pair (x1, x2)—representing two modalities—is known.

If the above assumption is correct, how do we sample from the joint distribution p(xO | xI)p(xI) in Equation (6)?

I find the assumption stated below Equation (1) too strong. It implies that the proposed method only applies when xO can be directly inferred from xI. For example, let’s assume a1 = a2 = a, representing the sound of a dog barking, and b1 and b2 represent images of a golden retriever and a border collie, respectively. V is a constant vector, and Y represents the class "golden retriever." While it is true that P(V|xI=a1)P(Y|xI=a1) = P(V|xI=a2)P(Y|xI=a2), given that a1 = a2, we see that P(V,Y=is_golden_retriever|xO=b1, xI=a1) does not equal P(V,Y=is_golden_retriever|xO=b2, xI=a2).

In Line 255, do h1* and h2* refer to the classifiers corresponding to modality 1 and modality 2, respectively? If so, how can they be applied to xO, which belongs to a different modality?

The baselines should be reconsidered, especially by including stronger baselines. For instance, there are many state-of-the-art semi-supervised learning (SSL) approaches, and simply adding Gaussian perturbations to the input may not be sufficient. Stronger SSL baselines are crucial, as otherwise, it could be argued that using SSL alone is enough, which raises the question, why COX? Additionally, the 'Random' baseline is too simplistic, effectively leaving the unsupervised setting in Table 2 with only one baseline. 

Furthermore, for the semi-supervised case, it is not surprising that the baseline performs worse, given the very limited amount of labeled data used for training.

I would like to bring [1] to the authors' attention, which could be helpful for better understanding multimodality:

[1] Zihui Xue et al., The Modality Focusing Hypothesis: Towards Understanding Crossmodal Knowledge Distillation, ICLR 2022.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a novel out-of-modal generalization problem that focuses on generalizing learned knowledge to unknown modalities. In addition, it considers both semi-supervised and unsupervised scenarios. The proposed connect & explore (COX) scheme tries to explore the shared and unique between modalities via variational information bottleneck. The proposed method can build connections between known and unknown modalities, further generating correspondences to explore more knowledge. The expleriments verify the effectiveness of COX.

### Strengths
1. This paper proposes a novel OOM problem, which is valuable because of the importance on generalizing exsting knowledge to unknown modalities without paired instances. 
2. The proposed COX method sounds reasonable and explores the connections between different modalities without priori knowledge. The motivation and method are clear to me. The results are convincing to me.

### Weaknesses
1. I acknowledge the novelty and value of the proposed OOM scenario. However, since the method lacks paired samples, it only shows limited effectiveness in learning shared knowledge, making it significantly inefficient in exploring unknown modalities. This is evident in the experimental results, which show a large gap compared to "aligned". Although the compared methods contain ERM and SSL, I question whether the proposed approach is better than SOTA unsupervised uni-modal solutions. Only surpassing or enhancing existing uni-modal methods with the proposed approach can make it really valuable. 
2. As I said in 1, the comparison with existing uni-modal methods is necessary.

### Questions
see in Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

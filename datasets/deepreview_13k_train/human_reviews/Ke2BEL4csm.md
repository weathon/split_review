# A Non-Contrastive Learning Framework for Sequential Recommendation with Preference-Preserving Profile Generation

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Contrastive Learning (CL) proves to be effective for learning generalizable user representations in Sequential Recommendation (SR), but it suffers from high computational costs due to its reliance on negative samples. To overcome this limitation, we propose the first Non-Contrastive Learning (NCL) framework for SR, which eliminates computational overhead of identifying and generating negative
samples. However, without negative samples, it is challenging to learn uniform representations from only positive samples, which is prone to representation collapse. Furthermore, the alignment of the learned representations may be substantially compromised because existing ad-hoc augmentations can produce positive samples that have inconsistent user preferences. To tackle these challenges, we design a novel preference-preserving profile generation method to produce high-quality positive samples for non-contrastive training. Inspired by differential privacy, our approach creates augmented user profiles that exhibit high diversity while provably retaining consistent user preferences. With larger diversity and consistency of the positive samples, our NCL framework significantly enhances the alignment and uniformity of the learned representations, which contributes to better generalization. The experimental results on various benchmark datasets and model architectures demonstrate the effectiveness of the proposed method. Finally, our investigations reveal that both uniformity and alignment play a vital role in improving generalization for SR. Interestingly, in our data-sparse setting, alignment is usually more important than uniformity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Summary:
This paper addresses the issue of high computational cost in contrastive learning (CL)-based sequential recommendation. Innovatively, it introduces non-contrastive learning into sequential recommendation. To tackle the representation collapse and alignment problems caused by solely relying on positive samples, a novel user preference-preserving profile generation method is proposed for the Non-Contrastive Learning framework for sequential recommendation (NCL-SR). NCL-SR is capable of learning generalized and robust user representations for sequential recommendation. Experimental results demonstrate that NCL-SR outperforms traditional SR models and CL-based SR models in terms of performance.

### Strengths
Strength：
1.This paper innovatively proposes a non-contrastive learning framework for sequential recommendation.
2.Inspired by Differential Privacy (DP), a theoretically guaranteed user preference-preserving data augmentation method is proposed to address representation collapse and preference inconsistency issues.
3.Two novel loss calculation methods are introduced.
4.Extensive experiments are conducted to verify the effectiveness, and the roles of feature alignment and uniformity in sequential recommendation are analyzed.

### Weaknesses
Limitation：
1.What does "s()" represent in Eq. 1? What does "f()" represent in Eq. 4?
2.What do the three polygons in the upper part of Fig. 1 represent? Why is there no corresponding polygon for the third red text?
3.During the construction of candidate user profiles, a item-level approach is adopted. How is the number of perturbations determined? Why weren't further experiments conducted to verify the effect of perturbation quantity on recommendation performance?
4.What is the split ratio of the training, validation, and test sets? Why wasn't it explicitly stated?
5.The motivation of this paper is to address the high computational cost and memory consumption in negative sample extraction of CL in SR. Why weren't further experiments conducted to verify the effect of NCL-SR on computational cost and memory consumption?
6.Further refinement of the text is needed. For instance, what is the relationship between “NCL SR” and “NCL-SR” in line 178? The term "differential privacy" in line 210 is in lowercase, while "Differential Privacy" in line 215 is in uppercase. Consistency should be maintained.

### Questions
Limitation：
1.What does "s()" represent in Eq. 1? What does "f()" represent in Eq. 4?
2.What do the three polygons in the upper part of Fig. 1 represent? Why is there no corresponding polygon for the third red text?
3.During the construction of candidate user profiles, a item-level approach is adopted. How is the number of perturbations determined? Why weren't further experiments conducted to verify the effect of perturbation quantity on recommendation performance?
4.What is the split ratio of the training, validation, and test sets? Why wasn't it explicitly stated?
5.The motivation of this paper is to address the high computational cost and memory consumption in negative sample extraction of CL in SR. Why weren't further experiments conducted to verify the effect of NCL-SR on computational cost and memory consumption?
6.Further refinement of the text is needed. For instance, what is the relationship between “NCL SR” and “NCL-SR” in line 178? The term "differential privacy" in line 210 is in lowercase, while "Differential Privacy" in line 215 is in uppercase. Consistency should be maintained.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a Non-Contrastive Learning framework for Sequential Recommendation powered by preference preserving user profile generation: NCL-SR. The NCL-SR framework eliminates the computational overhead of identifying and generating negative samples in CL. The experimental results on various benchmark datasets and model architectures demonstrate the effectiveness of the NCL-SR method.

### Strengths
+ The methodology of this paper is technically sound. The method itself is somewhat novel to me.

+ To my best of knowledge, it is the first attempt to utilize matrix cross entropy in the recommendation system.

+ The proposed NCL-SR achieves much better performance against other baseline models.

### Weaknesses
 + Fig.1. needs to be polished. For instance, it is unclear for me what is the plot meaning of the exponential mechanism with polygons in Fig.1? 

+ Why do you set the utility score as $\Delta_u = e - 1/e$? It is unclear for me. Could you please kindly provide some insights on that? 

+ Could different values of $\gamma$ affect the model performance? 

+ Some similar papers should be cited or discussed, e.g., [1] and [2].

### Questions
Please refer to the Weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors propose the first Non-Contrastive Learning (NCL) framework for Sequential Recommendation (SR). The authors design a novel preference-preserving profile generation method to produce high-quality positive samples for non-contrastive training. The paper is easy to follow and well-organized. The authors conduct extensive experiments to validate the efficacy of the proposed NCL-SR.

### Strengths
S1: The paper is easy to follow and well-organized.

S2: The authors provide theorem analysis for the proposed method which is novel and interesting to me.

S3: The authors conduct extensive experiments to validate the efficacy of the proposed NCL-SR.

### Weaknesses
W1: Some illustrations should be improved. For example, the authors should motivate why you choose Matrix Cross Entropy (MCE) against some other methods (e.g., Barlow Twin, MEC and DirectAU) for contrastive learning? Specifically, what are the theoretical or empirical advantages of MCE in the context of sequential recommendation compared to these alternatives? The paper should also discuss the potential limitations of MCE and whether other methods might be more suitable under certain conditions.

W2: Some method details are missing. For example, the calculation of $C(Z,Z’)$ in Eq.(9) should be provided to make the paper more readable. It is not clear how the centering matrix $H_B$ is constructed and applied in practice. The authors should provide a more detailed explanation of this process, including the dimensions of the matrices involved and the specific steps for computation.

W3: Since you need to figure out the eigenvalue of $\bm{V}$ in Eq.(9), how about the time complexity of your proposed method? The paper needs to clarify how the matrix logarithm is computed, especially given that it is a computationally expensive operation. The authors should discuss the practical implications of this complexity, including the scalability of the method to large datasets and the potential for approximation techniques.

### Questions
Please refer to the Weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the NCL-SR, which is designed to reduce the computational burden found in traditional Contrastive Learning apporaches by eliminating the need for negative sampling. CL methods generally require negative samples to avoid representation collapse, but this comes with high computational costs. The main contribution of NCL-SR is its preference-preserving profile generation technique, which uses differential privacy to create diverse yet consistent positive user profile samples that retain the user’s preferences. This helps to overcome challenges such as representation collapse and preference inconsistency.

### Strengths
- This paper solves a important question in traditional SR field, that CL approaches cost quite a lot computational resources. By adopting the profile augmentation method proposed in this paper, the performance of SR can even higher than those traditional CL methods.

- The authors provides theoritial guarantees for the uniformity and alignment.

### Weaknesses
 - Since the main motivation of NCL is to reduce the cost of traditional CL methods, I believe the efficiency study is needed.
- When comparing with other SR models (besides CL methods), I believe they should also be implemented with e5 for a fairer comparison.

### Questions
- The authors claim that the user profile generation is inspired by differential privacy, I wonder how it inspired the proposed framework in details? Maybe some addtional literature review might help to explain.

### Soundness
3

### Presentation
3

### Contribution
4

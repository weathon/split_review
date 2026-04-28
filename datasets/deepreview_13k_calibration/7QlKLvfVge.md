# Directional Rank Reduction for Backdoor Defense

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Recent studies have indicated the effectiveness of neuron pruning for backdoor defense. In this work, we explore the limitations of pruning-based defense through theoretical and empirical investigations. We argue that pruning-based defense necessitates the removal of neurons that affect normal performance when the effect of backdoor is entangled across normal neurons. To address this challenge, we propose an extended neuron pruning framework, named \emph{Directional Rank Reduction (\method)}. \method consists of three procedures: orthogonal transformation, pruning, and inverse transformation. Through the transformation of the feature space prior to pruning, \method is able to focus the trigger effects on a limited number of neurons for more efficient pruning with less damage, outperforming existing pruning-based defense strategies. We implement \method using Sarle's Bimodality Coefficient (SBC) which is optimized as the criterion for the transformation matrix based on the separability assumption of benign and poisoned features. Extensive experimental results demonstrate the superiority of our method. On average, our approach substantially reduces the ASR by 4.5x and increases the ACC by 1.45\% compared with the recently strong baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a rank reduction based defense against backdoor attack. Specifically, it first gives a feature-based objective to show the optimal solution to achieve the best defense effect. He then discussed the previous defense's problem based on the given objective and proposes DRR, the rank reduction based defense where aims to find a vector that would maximize the 3rd central moments of the mixed distribution. The proposed method have been verified in CIFAR10 with several backdoor methods. The result shows the proposed method could achieve a little better performance with the state-of-art defense.

### Strengths
1. The paper is well-written and easy to follow with only several typos.
2. The proposed method has some good theoretical analysis and could be meaningful for the future work.

### Weaknesses
1. Some of theoretical analysis might be not accurate. The utility function is defined using ||R-\gamma_r (R)|| and also ||R||-||γ_r (R)||. However, these two value is not strict equivalent. It also happens in the definition of E(R).
2. It is unclear why the 3rd center moment would show the best performance to measure the difference. In other words, would 2nd order moment or 1st order work as well? Since 3rd order is the main metric selected, the author should explain the choice in detail.
3. The experiment is pretty insufficient. It only covers one datasets with only one poisoning rate. I suggest the author to give a more comprehensive experiments to show their proposed method's effectiveness. Some standard setting in https://github.com/SCLBD/backdoorbench is recommended.

Minor typo:
Missing \hat{x} in the definition of E(R(l).

### Questions
Please refer to the weaknesses part. To sum, 
1. Why does ||R-\gamma_r (R)|| =||R||-||\gamma_r (R)|| along with  E(R)?
2. Why does 3rd central moment is selected?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a fascinating new method for backdoor defense in neural networks. The key idea of projecting the "toxic direction" that maximizes the difference between clean and poisoned features is novel and seems promising.

The theoretical analysis provides valuable insights into the limitations of standard neuron pruning approaches. Framing the problem as rank reduction along arbitrary directions rather than fixed neuron directions is a significant conceptual shift.

### Strengths
1. The idea of maximizing the third central moment is enjoyable. This idea yields a novel insight.
2. The connection between neuron pruning and rank reduction is also an exciting topic.
3. The visualization of the separation constant C provides good justification for the theoretical assumptions.

### Weaknesses
1.  More experiments can be conducted (BadNet, Blended, CLA, WaNet, and IAB are insufficient.) The authors can consider attacks like SIG [1] and low frequency (Smooth) [2]. Since your method also took latent separability as an assumption, Adapt-blend and Adapt-patch attacks [3] should also be considered. Evaluating robustness to adaptive attacks that try to evade the defense would be useful to understand limitations. Specifically, the current evaluation lacks a comprehensive analysis of the defense's performance against a diverse range of attack strategies. The inclusion of more sophisticated attacks, such as those that manipulate frequency components or adapt to the defense mechanism, is crucial for a thorough assessment. Furthermore, the evaluation should explore the defense's behavior under varying attack strengths and trigger complexities to provide a more nuanced understanding of its effectiveness. The absence of these evaluations limits the generalizability of the findings.
2.  The references and notations should be clarified. For example, what is the reference to Proposition 1? The current presentation lacks clarity in its referencing, making it difficult to trace the origins of key concepts and results. The absence of a clear citation for Proposition 1 raises concerns about the originality and validity of the claim. It is important to provide proper attribution to all ideas and results, and to ensure that the reader can easily locate the source material. A more detailed and consistent referencing style is needed to improve the paper's credibility and accessibility.
3.  Also, the readability and organization of this paper need to be improved. It is better if an algorithm is provided. The current structure of the paper makes it challenging to follow the proposed method. The lack of a clear algorithmic description hinders the reproducibility of the results and makes it difficult for other researchers to understand and build upon the work. A well-defined algorithm would clarify the steps involved in the method, improve the overall clarity of the paper, and facilitate its adoption by the research community.

### Questions
1.	The memory and computational complexity could be analyzed more thoroughly, especially how the approach scales with larger datasets/models. Are there ways to make the optimization more efficient?
3.	How many extension directions v_i have you used?
4.	Modifying the weight matrix may cause a performance drop in many cases. How can your projection keep the performance?
5.	The proof needs to be more rigorous. Why use the consequence of the proof in the middle of the proof?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel backdoor defense method, which utilizes rank reduction to mitigate backdoor in the model. The idea of rank reduction is interesting and brings a new insight into the area.

### Strengths
1. The idea is novel and provides a new insight.
2. This paper is technically sound and easy to follow.
3. The experimental results demonstrate its effectiveness in backdoor defense.

### Weaknesses
1.Although this work is interesting, it has a limitation. This paper assumes the defender can get access to the backdoored image. However, this is hard to get in actual situations and thus limits its use greatly. I wonder whether it works without these backdoored data.
2. The backdoor attacks that this paper test is not enough. I suggest the authors to test the newest input-specific backdoor attacks in 2022. It's important to identify whether this method can achieve SOTA.

### Questions
1.Does it work without the attacker's backdoored data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper argues that existing pruning-based defense methods can be ineffective at times and introduces Directional Rank Reduction (DRR) to identify toxic directions. In this study, the method approximates the target direction by maximizing the third central moment, supported by rigorous theoretical justification, and constructs a projection matrix to eliminate the toxic direction. DRR demonstrated outstanding performance in terms of both accuracy (ACC) and adversarial success rate (ASR).

### Strengths
1. This study shows an interesting finding that the backdoor trigger effects are not always aligned with fixed dimensions of the feature space, pruning-based methods are usually ineffective.
2. The proposed DRR method performed well on both ACC and ASR compared to other methods.

### Weaknesses
 1. In the first equation on Page 3, it seems feasible to do the defense by reducing the norm of the residual matrix to align the benign and poisoned features seems feasible. The features from benign examples move towards the backdoored features. Does the movement hurt the model's clean performance?

 2. The last equation on Page 4 has a strong assumption that all the clean examples are centered around the mean of them. Namely, the method assumes that the distances from all the clean examples to the example center are the same. The examples marked as yellow in Figure 1 are distributed like a circle. However, the real-world data distribution often deviates from the assumption. The distribution could be elliptical-like. In this case, the obtained v is not optimal anymore.

 3. In the third row of Table 2, DRR achieves a better trade-off. Why it demonstrates a higher accuracy (ACC) instead of a lower ASR?

 4. This approach requires the optimization of a vector in each layer, which could be expensive. 

minor: All the equations are not numbered!

### Questions
1. "How the direction vector v is initialized in the paper, and do different initialization methods lead to varying results?

2. In Figure 2, the value of C for certain layers is not significant. Is it possible to skip some layers when computing v?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

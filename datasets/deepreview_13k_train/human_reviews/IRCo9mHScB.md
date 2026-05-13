# OMS: One More Step Noise Searching to Enhance Membership Inference Attacks for Diffusion Models

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
The data-intensive nature of Diffusion models amplifies the risks of privacy infringements and copyright disputes, particularly when training on extensive unauthorized data scraped from the Internet. Membership Inference Attacks (MIA) aim to determine whether a data sample has been utilized by the target model during training, thereby serving as a pivotal tool for privacy preservation. Current MIA employs the prediction loss to distinguish between training member samples and non-members. 
These methods assume that, compared to non-members, members, having been encountered by the model during training result in a smaller prediction loss. However, this assumption proves ineffective in diffusion models due to the randomly noise sampled during the training process. Rather than estimating the loss, our approach examines this random noise and reformulate the MIA as a noise search problem, assuming that members are more feasible to find the noise used in the training process.
We formulate this noise search process as an optimization problem and employ the fixed-point iteration to solve it. We analyze current MIA methods through the lens of the noise search framework and reveal that they rely on the first residual as the discriminative metric to differentiate members and non-members. Inspired by this observation, we introduce \textbf{OMS}, which augments existing MIA methods by iterating  \textbf{O}ne \textbf{M}ore fixed-point \textbf{S}tep to include a further residual, i.e., the second residual.   
We integrate our method into various MIA methods across different diffusion models. The experimental results validate the efficacy of our proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors explore privacy risks in diffusion models by improving MIA. Traditional MIA methods are ineffective for diffusion models due to noise in training. This paper proposes a novel noise search approach called OMS (One More Step), which refines MIA by adding a fixed-point iteration step to better distinguish between training members and non-members. This method significantly enhances MIA accuracy across various diffusion models and datasets, addressing privacy concerns in data-intensive AI models.

### Strengths
+. The paper introduces a creative reformulation of Membership Inference Attacks (MIA) as a noise search problem, which is a fresh perspective on tackling privacy risks associated with diffusion models. 
+. The proposed One More Step (OMS) enhancement to existing MIA techniques effectively improves the accuracy of identifying members in diffusion models. This additional fixed-point iteration step is a simple yet impactful modification that leverages the specific characteristics of diffusion processes.
+. The authors conducted experiments across various diffusion models and datasets, providing a robust demonstration of OMS’s effectiveness.

### Weaknesses
 -. Some statements in the paper can lead to confusion. For example, in the introduction, it is stated: “To address these privacy concerns, Membership Inference Attacks (MIA) Shokri et al. (2017) have emerged as a potential solution.” This phrasing is misleading, as MIAs themselves are privacy attacks, not solutions to privacy concerns. This could be clarified to avoid misunderstanding.
-. While the methodology of this paper is technically sound, it would benefit from a clearer explanation of the real-world implications of privacy risks in diffusion models. To strengthen the paper, it is recommended that the authors include a specific section discussing the real-world impacts of privacy risks and their potential effects on individuals or organizations, along with 1-2 concrete examples to support this discussion.
-. Some terms and technical concepts, such as “fixed-point iteration” and “convergence rate,” are introduced without sufficient background or explanation. For readers unfamiliar with these mathematical concepts, a brief definition or background could make the paper more accessible.

### Questions
Q1: Could the authors elaborate on how the noise search mechanism operates in practice? Specifically, what criteria are used to determine the optimal stopping point in the noise search process?
Q2: How well does OMS perform across different types of diffusion models, beyond those tested in the experiments? Are there specific classes of diffusion models where OMS may be less effective?

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
This paper introduces One More Step (OMS) Noise Searching, a framework to enhance Membership Inference Attacks (MIA) on diffusion models. Traditional MIA approaches rely on prediction loss differences between members and non-members, which can be ineffective for diffusion models due to random noise sampling during training. The authors propose reformulating MIA as a noise search problem, aiming to identify training noise that corresponds to specific data records. By using fixed-point iteration, the proposed method iteratively searches for this noise, leveraging the observation that member data tends to converge faster than non-member data. This process also introduces OMS, a refinement that incorporates an additional iteration to improve discrimination between member and non-member records. Experimental results on various diffusion models show that OMS significantly boosts MIA performance.

### Strengths
1.The paper proposes a unique approach to handling noise in diffusion models by shifting the MIA focus from prediction loss to noise searching. This formulation is novel within MIA related research and introduces fresh ideas on addressing privacy risks specific to diffusion models.

2.The study is thorough, with extensive experiments across different types of diffusion models (e.g., CNN-based, Transformer-based) and datasets. This breadth strengthens the paper’s empirical validity.

3.The paper is well-organized, with detailed explanations of the problem, methodology, and fixed-point iteration approach.

### Weaknesses
1.While the fixed-point iteration method is interesting, the paper could benefit from a deeper exploration of its convergence properties. Specifically, the analysis should include a more rigorous treatment of the conditions under which the iterative process converges, and whether the convergence rate is consistent across different data samples and diffusion model architectures. The current analysis lacks a detailed examination of the function being iterated, and how its properties affect the convergence behavior. A more thorough investigation into the contraction properties of the objective function would also be beneficial.

2.Additional analysis on scalability and time complexity could make the contribution more robust. The paper should provide a more detailed breakdown of the computational cost associated with the proposed One More Step (OMS) method, including the number of forward and backward passes through the diffusion model, and how this scales with the size of the dataset and the dimensionality of the input. Furthermore, the memory requirements of the method should be analyzed, particularly in relation to the storage of intermediate noise vectors during the iterative process. A comparison with the computational cost of existing Membership Inference Attack (MIA) methods would also be valuable.

### Questions
1.I’m curious about the computational requirements of the OMS approach. Could the authors provide more details on how OMS performs in terms of memory and computation time, especially when additional steps are taken?

2.Could the authors clarify how the convergence rate differs between member and non-member samples, and whether this could be generalized across various types of diffusion models? More insights into this mechanism would help to strengthen the theoretical foundation of the approach.

I am giving a score of 6 (marginally above the acceptance threshold), as the novelty and contribution appear promising and potentially meet the standards for ICLR. I will consider the expertise and feedback of other reviewers, particularly those with a stronger background in diffusion models, and may adjust my score based on additional insights or clarifications.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a way how to improve membership inference attacks (MIAs) against diffusion models (DMs). The key contribution lies in identifying that considering one step in the denoising process as a membership signal yields suboptimal results and that considering a second additional step provides a higher signal.

### Strengths
The experimental evaluation considers multiple model architectures and existing MIAs against DMs and shows a performance improvement over all of them. This highlights as well that the approach is fairly simple and can be integrated universally.

### Weaknesses
Overall, the contribution of just including an additional step into the MIAs seems comparably small. While a lot of effort it done to put the contribution into a theoretically sound presentation, it still relies on the observation made by previous MIAs that there is a noise difference between members and non-members.
I see possibilities to extend the contribution by considering the following angles:
- Analysis of disparate effect over different members: Are certain members more vulnerable? Can that be detected better with the additional step? 
- Deriving formal upper bounds on the membership risk exposed by the different points.
- Analyzing why certain datasets/attack combinations benefit more from the approach.
By incorporating such an angle, the contribution could be significantly broadened.

**Experimental Results**

I would suggest, especially for table 2, not to report the delta in absolute percentages. This makes a comparison extremely unintuitive. Instead, I suggest reporting an improvement in percent. E.g., +5.70 sounds way more impressive than +0.44 in the first row, however, the first one is not even doubling while the second one is tripling the success.



**General Presentation Issues**

I would suggest fixing the following presentation issues:
- The paper does not use \citep correctly: everywhere in the intro (and nearly everywhere else in the paper), it should be \citep instead of \cite. There is also \citet. This would be used to avoid phrases as "A significant contribution to this field is made by Matsumoto et al. Matsumoto et al. (2023).
- DDPM is not introduced as an abbreviation.
- The paper introduces the abbreviation DMs but then inconsistently still uses "diffusion models", same for MIA.
- What does it mean: "During the inference phase, due to the infeasibility of the training noise" --> what is infeasible? Getting access to the original noise?
- It would be good to give an intuition on what is "fixed-point iteration" already in the intro when first mentioning it to facilitate the reader's understanding.

### Questions
/

### Soundness
3

### Presentation
2

### Contribution
2

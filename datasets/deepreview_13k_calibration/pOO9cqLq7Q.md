# CONTRA: Conformal Prediction Region via Normalizing Flow Transformation

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
Density estimation and reliable prediction regions for outputs are crucial in supervised and unsupervised learning. While conformal prediction effectively generates coverage-guaranteed regions, it struggles with multi-dimensional outputs due to reliance on one-dimensional nonconformity scores. To address this, we introduce CONTRA: CONformal prediction region via normalizing flow TRAnsformation. CONTRA utilizes the latent spaces of normalizing flows to define nonconformity scores based on distances from the center. This allows for the mapping of high-density regions in latent space to sharp prediction regions in the output space, surpassing traditional hyperrectangular or elliptical conformal regions. Further, for scenarios where other predictive models are favored over flow-based models, we extend CONTRA to enhance any such model with a reliable prediction region by training a simple normalizing flow on the residuals. We demonstrate that both CONTRA and its extension maintain guaranteed coverage probability and outperform existing methods in generating accurate prediction regions across various datasets. We conclude that CONTRA is an effective tool for (conditional) density estimation, addressing the under-explored challenge of delivering multi-dimensional prediction regions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a new conformal prediction method for multi-dimensional regression. It is based on fitting a (conditional) normalizing flow in the space of outputs. Authors perform numerical experiments on public datasets that illustrate certain benefits of the proposed method.

### Strengths
- The proposed method makes a lot of sense as flexible estimator of conditional label distribution is obviously required to achieve optimal set size, especially in multidimensional case. 
- The results are adequately explained.
- Experimental results show certain benefits of the proposed approach in terms of prediction set size.

### Weaknesses
 - The proposed approach boils down to application of the normalizing flows to the split conformal prediction framework. There are no technical difficulties on this way. Any other conditional density estimator can be used here instead.

- All the theorems in the paper are standard (not sure, why even proofs are provided). There seems to be no theoretical contribution for the present paper.



### Questions
- Why don't you study other density estimation methods? 

- Performance of normalizing flows heavily depends on the size of the dataset. How will it influence the results of the proposed method? I think that this should be studied.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work addresses the limitation of most of the current conformal prediction algorithms which struggle with multi-dimensional outputs. The proposed method CONTRA, uses conditonal normalizing flows (CNFs) to learn a bijection, mapping a latent variable form a simple base distribution to the output variable, and then mapping the high density regions of the base distribution to the output. Using Conformal Prediction ( particularly the split conformal prediction algorithm) , CONTRA then calibrates the results to provide marignal coverage gaurantees of CP on including the true prediction region.

### Strengths
1. The writing is clear, and to the point. The contributions are presented honestly and placed well with respect to the prior work. 
2. The experiments are elaborate, and show the main metrics in CP: efficiency in terms of the size ( volume ) of the prediction sets and coverage. Both synthetic and real world datasets are considered, and the results are consistent across the two settings ( synthetic vs real-world). 
3. the output regions of CONTRA do seem to visually support the authors' claims in that they are interpretable and have smoother boundaries compared to the related work. In most settings/datasets CONTRA seems to be outperforming most other baselines ( except PCP ). 
4. They address an important and practical problem (multi-modal outputs ) which extends the applicability of Conformal Prediction. 
5. Their methods seems simple to follow and implement.
6. They introduce variation of the method, to adopt to different choices of the fitted model for the conditional density estimation.

### Weaknesses
1. PCP ~ ( a competing method) is able to outperform both variations of CONTRA and ResCONTRA in some cases in terms of providing smaller prediction regions while maintaining coverage guarantees.
2. the authors mention instances in which CONTRA could deteriorate in performance. Particularly when its hard to learn bijection well. but no results are provided to illicit the deterioration trends or to show the remedy solutions discussed by the authors can help.

### Questions
1. with respect to point 2 in the weaknesses, how do competing methods, particularly PCP, are expected to perform in cases that CONTRA is not able to perform well. A discussion ~ potentially a brief experiment on synthetic data ~ where we understand the trend of performance deterioration in CONTRA, and the effectiveness of the solutions proposed on page 10,  could illicit a more clear choice to follow in whether one should try to apply the proposed solutions or go with another method.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
CONTRA is a novel method for multi-dimensional output prediction that utilizes normalizing flows to define conformal prediction regions. By mapping high-density regions in latent space to output space, it generates more precise and connected prediction regions, avoiding the oversized or irregular regions produced by traditional methods. The paper also introduces ResCONTRA, an extension that can enhance any predictive model with reliable prediction regions. Experiments demonstrate that CONTRA not only guarantees the desired coverage but also produces prediction regions with smaller volumes and smoother boundaries, outperforming existing methods on both synthetic and real-world datasets.

### Strengths
The manuscript is generally easy to follow and includes a sufficiently comprehensive discussion of relevant prior works. Experimental results are presented well.  The proposed solution has solid theoretical foundations.

### Weaknesses
 - In line 186, how to construct the prediction region? \hat{E} is a q-dim ball, which contains infinitely many vectors, making its implementation unclear.
- More discussion about CNF will be valuable.
        1. Providing details about choosing q_1 in Appendix D will be better. Equal division? Moreover, for Bio dataset, the dim-y is only 1, that can not be split.   
         2. A possible limitation is that normalizing flows is notoriously difficult to train in high-dimensional spaces. Extending CONTRA to handle high-dimensional outputs (e.g., image generation) would significantly enhance its practicability.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a technique to compute valid prediction regions in multiple-output regression tasks. The approach is based on learning a Normalizing Flow that transforms the output conditional probability into a 'simpler' base distribution. The invertibility of the flow allows mapping valid convex intervals of the feature space, e.g. rectangles, to non-convex smooth regions in the original space.

### Strengths
- Using Normalizing Flow to improve Conformal Prediction is intriguing and flexible. 
- Normalizing Flows and their likes are increasingly popular for training generative models. The proposed method could be further improved by leveraging advances in that domain.
- Multiple-output Conformal Prediction is an important but often overlooked problem.

### Weaknesses
 - The use of Normalizing Flow is not theoretically justified. The introduction should explain the differences compared to learning more standard feature maps. Specifically, it is unclear why the invertibility constraint is necessary, and how it impacts the expressiveness of the learned mapping compared to non-invertible alternatives. The authors should provide a more detailed discussion on the theoretical properties of the chosen normalizing flow architecture, and how these properties relate to the goal of constructing valid prediction regions.
- The authors should describe in detail the overlaps between their work and Colombo 2024, which is not mentioned with other related work but seems closely related to the proposed approach. The discussion should clarify the differences in the objectives and methodologies, particularly regarding the training of the normalizing flow and the handling of marginal vs. conditional coverage. It's crucial to understand whether the proposed method offers any advantages over Colombo 2024, or if it simply provides an alternative approach with similar limitations.
- It is unclear why the proposed approach is superior to existing multiple-output Conformal Prediction approaches. The authors should provide a more rigorous comparison with methods that produce elliptical or box-shaped regions, and with more flexible methods like PCP and ST-DQR. A detailed analysis of the trade-offs between region shape, volume, and computational cost is needed to justify the proposed method's advantages.
- The authors should give more details about the invertible flow, $t_\theta$, and discuss possible overfitting or underfitting problems. Especially in comparison with other non-invertible probability maps (e.g.diffusion models). The discussion should include the number of coupling layers, the size of the hidden layers, and the optimization procedure. It is also important to discuss how the complexity of the flow impacts the quality of the prediction regions and the computational cost of the method.

### Questions
- What is the difference between the proposed approach and methods that learn a feature space map before applying CP, e.g. STDQR?
- What is the difference between using a normalizing flow as a prediction model and a model for the residuals? From Figure 1, the latter seems to produce smoother regions. Is this always the case?
- Can the method be extended to tasks with many more outputs, e.g. images?
- In practice, requiring the map to be invertible may make Normalizing Flow hard to train or less flexible than unconstrained models. Have you tried Normalizing Flow with different structures?

### Soundness
3

### Presentation
3

### Contribution
2

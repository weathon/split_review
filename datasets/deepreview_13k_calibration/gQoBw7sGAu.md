# Rare event modeling with self-regularized normalizing flows: what can we learn from a single failure?

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 6, 6, 5

## Abstract
Increased deployment of autonomous systems in fields like transportation and robotics have seen a corresponding increase in safety-critical failures. These failures can be difficult to model and debug due to the relative lack of data: compared to tens of thousands of examples from normal operations, we may have only seconds of data leading up to the failure. This scarcity makes it challenging to train generative models of rare failure events, as existing methods risk either overfitting to noise in the limited failure dataset or underfitting due to an overly strong prior. We address this challenge with CalNF, or calibrated normalizing flows, a self-regularized framework for posterior learning from limited data. CalNF achieves state-of-the-art performance on data-limited failure modeling and inverse problems and enables a first-of-a-kind case study into the root causes of the 2022 Southwest Airlines scheduling crisis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this work, the authors propose an algorithm for rare-event modeling and failure detection using normalizing flows. The motivation stems from the observation that rare events are significantly low in number, making traditional approaches like prior regularization or simple bootstrapping ineffective. To address this challenge, the authors develop an optimization pipeline that trains a normalizing flow with a built-in calibration mechanism, which identifies the optimal latent factors associated with a target (failure) dataset. The paper is supported by extensive theoretical analyses, experiments, and an interesting case study, all demonstrating the efficacy of the proposed approach.

### Strengths
The paper addresses an important and intriguing problem in modeling rare events or failures with generative models, which often struggle to generalize when trained on limited data. It is mathematically well-supported and includes relevant case studies and experiments on standard benchmarks

### Weaknesses
Refer to Questions

### Questions
* How would the performance change if the calibration procedure is conducted jointly with the training of the normalizing flow? Would this make the optimization process more challenging?
* Figure 4 needs to be referenced in the text of the paper for clarity.
* Can this framework be extended to problems where the calibration label is continuous-valued? Understanding this extension would be useful, as many scientific applications involve real-valued outputs or measurements.
* Could the authors elaborate on the anomaly rejection and few-shot inference experiment details? A more comprehensive explanation of these procedures would enhance the clarity and depth of the paper.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to address rare event modeling problems where failure data is in a very limited amount. Specifically, the authors propose a generative modeling framework called Calibrated Normalizing Flows (CALNF) to learn a shared representation from both normal and rare failure data. Furthermore, they leverage calibration and self-regularization processes to avoid overfitting. They provide empirical results on benchmarks and real-world cases.

### Strengths
1. The idea is intuitive and easy to understand.
2. The paper is well-organized and easy to follow.
3. The qualitative visualizations on benchmark datasets are impressive.
4. The case study on the 2022 Southwest Airlines scheduling crisis is persuasive.

### Weaknesses
1. The authors assume that failure events are not entirely disjoint from normal events, however, this might not hold in cases where failures are out-of-distribution (OoD) data. This means the failures can have drastically different characteristics from the normal ones. Can the proposed method still represent these rare events accurately in this case? Specifically, if the failure modes exhibit entirely different underlying physical processes or data generating mechanisms compared to the nominal data, the shared representation learned by the model might not be appropriate, potentially leading to inaccurate modeling of the rare events. For instance, in a system monitoring scenario, a sensor failure might produce data that is not just a deviation from normal but a completely different signal altogether.
2. Even with self-regularization, the model’s performance might still be sensitive to the selection of the number of subsamples $K$ and regularization weights $eta$. What method did you use to select $K$ and $eta$? Was it tuned manually, or is there a heuristic that works well across different failure datasets? The lack of a principled method for selecting these hyperparameters could limit the practical applicability of the proposed method. The authors should provide a more detailed analysis of the sensitivity of the model to these parameters and suggest guidelines for their selection.
3. As discussed by the authors, the proposed method introduces computation overhead. Have you considered how to extend the proposed method to high-dimensional data such as images? The computational cost associated with normalizing flows, particularly when dealing with high-dimensional data, can be a significant limitation. The authors should discuss the scalability of their approach and potential strategies to mitigate the computational burden when applied to complex datasets.

### Questions
See Weaknesses for the major concerns. Other questions:
1. Is the calibrated normalizing flows model the optimal solution? Can the proposed model generalize to other generative models such as GAN and Diffusion models?

### Soundness
3

### Presentation
3

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
This paper presents Calibrated Normalizing Flows (CALNF), a method for modeling rare failures in data-limited settings by learning robust posterior distributions through self-regularization. CALNF combines nominal and limited failure data to capture event distributions effectively, demonstrated on benchmarks like UAV control and air traffic disruptions, including an analysis of the 2022 Southwest Airlines crisis.

### Strengths
1. The CALNF framework addresses an important challenge in failure modeling by using normalizing flows for posterior learning from limited data. This approach is innovative in combining data regularization with low-dimensional embedding optimization, which could be valuable in real-world failure analysis in autonomous systems.

2. The paper tests its methodology on practical datasets, including autonomous UAV control and air traffic disruptions. This inclusion strengthens the paper’s relevance for the conference theme, as it presents an approach applicable to practical, high-impact fields.

3. The paper compares CALNF against well-established baselines, such as KL and Wasserstein regularized methods, and ensemble methods. These comparisons and detailed analyses provide a fair view of CALNF’s effectiveness, especially in data-limited scenarios

### Weaknesses
1. The dual steps of the method—learning a low-dimensional embedding and calibrating a label space—add significant complexity, which may impact reproducibility and practical use, particularly in robotics where model simplicity and speed are often crucial. Additional clarifications or simplifications could improve accessibility to a broader audience

2. Although the authors acknowledge this in the Limitations section, the increased training time due to subsampling may limit CALNF's applicability to settings requiring rapid inference, such as real-time planning and decision-making in robotics. The authors could consider discussing strategies to mitigate this cost

3. While CALNF aims to model rare failures effectively, it does not provide direct risk estimates or probability bounds for these events. Adding a framework for estimating risk or failure probabilities could enhance the utility of this approach for preemptive failure detection and mitigation

4. The paper provides some analysis around sensitivity and regularization but lacks a comprehensive discussion of how well the approach generalizes to new data. For applications in robotics and autonomous systems, where new conditions are frequently encountered, more robust guarantees on generalization could significantly strengthen the work

### Questions
1. Could you provide more theoretical insights or empirical evidence on how CALNF handles data sparsity when transferring to new or unseen data points? For applications in autonomy and robotics, understanding the model's generalization capability could be essential.

2. How sensitive is CALNF to the choice of regularization hyperparameter β and the number of subsamples K? While some sensitivity analyses are included, it would be beneficial to understand how practitioners might adapt these parameters to different problem settings with minimal fine-tuning.

3. Given the added training cost of CALNF due to subsampling, how practical is this method for real-time applications in autonomy or robotics where immediate inference might be required? Would you recommend any adjustments for faster, low-latency performance?

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
4

### Summary
In this work, the authors propose a calibrated normalizing flow method to address the rare-event modeling problem in data-constrained settings. Experimental validation demonstrates improved performance compared to the prior regularization and bootstrapping ensemble baselines.

### Strengths
The paper is well-written, and the proposed method is presented clearly. 

Experimental settings and results are described in detail, and limitations related to training costs are analyzed.
 
Extensive experimental validations across various settings demonstrate the effectiveness of the proposed method.

### Weaknesses
A subsection that clearly outlines a comprehensive literature review of recent research achievements in related work is missing.

In the primary experimental validation, the most relevant comparisons are made between prior regularization techniques (based on studies from 2020/2021) and the bootstrapping approach (from 2019). Thus, claiming that the proposed method achieves state-of-the-art performance in both the abstract and introduction (lines 63–64) seems not very convincing. The chosen baselines do not represent the current state-of-the-art in few-shot generative modeling, particularly in non-image domains, where more recent methods may offer better comparisons.

In Section 4.2, the ensemble size is set to $K=5$. Additionally, an ablation study examines both the training time and the sensitivity of CalNF to varying values of $K$ (These results are appreciated). As increasing ensemble size generally improves performance, it remains uncertain whether the proposed method maintains its superiority over ensemble baselines (as shown in Table 1) as $K$ increases. The study does not explore the performance of the ensemble method with larger values of K, which could potentially close the performance gap with the proposed method. It is also unclear how the computational cost of the proposed method scales with increasing K, especially compared to the ensemble baseline.

### Questions
**Q1:** Equation 5 and the explanation between lines 175-177 appear to present conflicting information. If minimizing the total loss leads to maximizing the KL divergence between candidate posteriors (due to the subtraction sign), wouldn’t this be against the statement that the divergence between candidate posteriors learned for each subsample should be small?

**Q2:** Could you please elaborate on why the candidate posteriors learned for each subsample should be kept small? Typically, ensemble methods enhance predictive performance by increasing the diversity among ensemble members.

**Q3:** Is there a typo in the Equation 3 where the $q_{\phi_t}$ in the DL part should be $q_{\phi}$? Should $c^*$ be in the loss $L_{cal}$ (line 178) rather than $c$?

**Q4:** Could you please elaborate on why the ensemble method can not infer the correct shape (lines 314-316) in Figure 3? The results of the ensemble and the CalNF look a bit similar.

**Q5:** In lines 112-114, some drawbacks of the ensemble method (e.g., data sensitivity issue in deep models), would the proposed method counter these issues?

**Q6:** Regarding the statements in lines 129-131, could you please provide some supportive references or explanations to illustrate the practical issues even in the case of selecting an optimal $\beta$?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Calibrated Normalizing Flows (CALNF), a novel approach to rare event modeling in data-constrained scenarios. CALNF builds on normalizing flows to learn an approximate posterior over latent variables $z$, using a blend of ensemble techniques and self-regularization. In essence, the method operates by jointly training on the complete target dataset, its subsets, and nominal data. A conditional normalizing flow is applied across both the target, nominal and subset posteriors, followed by a calibration step that optimally combines these learned posteriors to approximate the overall target distribution. By jointly learning across both subsets and the full dataset, CALNF captures the target distribution effectively while minimizing overfitting, making it more robust in settings with limited data.

While the paper presents an innovative approach to rare event modeling, the marginal performance gains over the ensemble baseline do in my opinion not justify the increased computational complexity, leading to a weak reject. For a more detailed justification, please see the comments below.

### Strengths
**Addresses an important problem:** The paper tackles the challenge of modeling rare events with limited data which is a relevant issue in many safety-critical applications.

**Theoretical Foundation:** The paper includes a theoretical analysis, such as bounding the Wasserstein distance between nominal and target posteriors, adding robustness to the method.

**Clear Presentation:** The method and its applications are well-presented, making the paper easy to read.

### Weaknesses
 **Marginal performance gains vs computational complexity**  As the authors note, Table 1 contains the main empirical results, comparing performance on four benchmark datasets between the proposed method and simpler ablated versions, including the Ensemble approach. However, the Ensemble method performs nearly as well as the proposed CALNF, with results that are statistically indistinguishable from CALNF in three out of four cases. This similarity in performance raises questions about whether the added complexity of CALNF is justified. In particular, (i) the Ensemble approach has fewer hyperparameters (only the number of ensemble components, with no regularization parameter), (ii) does not rely on nominal data, and (iii) allows parallelized training across ensemble members.

While the issue of additional hyperparameters is mitigated to some extent by the authors' ablation study in the appendix, the other limitations are more concerning. CALNF requires joint training on nominal and target data to estimate the posterior over the target distribution, adding significant complexity relative to the Ensemble method. This dependency on both data types also limits CALNF’s suitability for online or real-time applications, where training with nominal data might not be feasible, further reducing its practical applicability.

### Questions
I recommend that the authors further clarify and refine the benefits of CALNF compared to the Ensemble method, particularly addressing cases where the performance gains justify the additional complexity.

### Soundness
3

### Presentation
3

### Contribution
2

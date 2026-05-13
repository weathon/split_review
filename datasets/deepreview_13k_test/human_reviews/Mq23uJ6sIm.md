# Neural Regenerative Stochastic Differential Equation: Dropout Scheme for Neural Differential Equations

- Decision: Reject
- Scores: 6, 5, 6, 5, 6, 6

## Abstract
Neural Differential Equations (NDEs) are an excellent tool for modeling continuous-time (stochastic) dynamics, effectively handling challenges such as irregular observations, missing values, and noise. Despite their advantages, there is a lack of regularization techniques in the NDE framework, particularly those like dropout, which have been successfully implemented in other discrete neural networks, making them susceptible to overfitting. To address this research gap, we introduce Neural Regenerative Stochastic Differential Equation (NRSDE), based on alternating renewal processes, as a universally applicable regularization technique for NDEs. Our study reveals that NRSDE can effectively represent a continuous approximation of neural networks that randomly deactivate some neurons during training, similar to dropout, thereby enhancing the robustness and generalization capabilities of NDEs. Through extensive experiments, we demonstrate that NRSDE outperforms existing regularization methods for NDEs and can be applied to all existing NDE models, significantly improving their performance across various deep learning tasks, including time series classification and image classification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the lack of regularization methods for NDEs, by introducing a novel NRSDE method. Its main innovation is to incorporate the dropout mechanism into models that work in continuous time setting using a so-called alternating renewal process, a mathematical framework for modelling systems that alternate between two states over time. NRSDE is designed to be applicable to various types of NDEs. Authors discuss the relations between their approach and prior-art work. The method is extensively tested on various datasets and compared with prior-art methods. In addition, a study on sensitivity of NRSDE’s hyper-parameters is provided.

### Strengths
- Regularization techniques, such as dropout, are essential for modern AI models and thus the topic that the authors touch upon is very timely.
- The authors have provided extensive proves and mathematical details about their approach. From what I can tell, the math seems sound as well
- I appreciate that the source code is shared publicly

### Weaknesses
- The main weakness that I see with this paper is the overhead to compute the scaling factor. In machine learning workloads one would like to keep the inference (testing) phase as simple and fast as possible, as this phase is use extensively by many users and in many applications. Therefore, the requirement to compute the scaling factor with Monte Carlo Sampling (MCS) during the testphase for each and every new test sample is really not ideal. Furthermore:
    1. tuning of the scaling factor for the test phase. Line 317-320 and Appendix F.2 show that 5-10 samples are sufficient to estimate the scaling factor. This is done for a fairly simple time series dataset (google speech command). What would happen in case of image datasets?
    2. the scaling factor is one of NRSDE’s parameters. Hence, following the best practices of ML, it has to be determined (or learned) using the only training data. But, currently, as shown in Algorithm 1, it is done using test data. This issue can be possibly addressed by dedicating a subset of training data specifically for determining the scaling factor via MCS.
    3. from Table 17 in F.1, the overhead to compute the scaling factor is by no means small or negligible.
    4. from Table 18 it is unclear whether indeed 5 or 10 is sufficient. What happens for larger values?
- The choice of the tasks is suboptimal. The authors claim to address “continuous-time dynamical systems” and the second set of tasks revolves around static image classification. If one would be interested in the spatial domain of images, then at least one needs to consider videos, or some other ways to convert images into a temporal input sequence that has a continuous-time dynamical systems underlying.
Minor comments: The authors chose the same notation (.) to denote the time t and the layer k. This is an unfortunate choice and may confuse the reader.

### Questions
See the points above

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores how to use the well-known dropout technique for Neural Differential Equations (NDEs) to achieve robustness and generalizability.

### Strengths
The proposed NRSDE introduces a specialized dropout mechanism tailored for Neural Differential Equations (NDEs), which addresses a known limitation in current NDE frameworks. This regularization technique, similar to standard dropout, randomly deactivates neurons during training to enhance robustness and generalizability. The approach is with theoretical foundation. Experimental validation on multiple datasets and model types demonstrates performance improvements.

### Weaknesses
1.	The motivation of dropout-based regularization for NDEs is limited in the Introduction. For example, there are extensive regularization techniques. Why do the authors choose the dropout-based scheme for NDEs? The authors should provide stronger support from literature or experiments. 
2.	The authors employ a key concept called alternating renewal processes. However, in the Introduction, the concept is not explained explicitly and there is no citation about this process.
3.	The following statement is unclear. “Assume that $X_n$ and $Y_m$ are independent for any $n\neq m$, but can be dependent for $n=m$.”
4.	Why do you focus on the exponential alternating renewable process? Are there other options? 
5.	The authors should state the importance of the introduced baselines. Are they cutting-edge methods? Are they representative and comprehensive?
6.	As NRSDE is computationally tensive, the authors should report the computational time in the Experiments and future possible solutions to mitigate this issue in the Conclusion.

### Questions
1. What are other methods? Why do the authors choose the dropout-based scheme for NDEs?
2. What are the drawback to the alternating renewal processes? 
3. Why do you focus on the exponential alternating renewable process? Are there other options? 
4. Are the benchmark method cutting-edge? 
5. How robust is the proposed method in low-data scenarios where overfitting is a primary concern?

### Soundness
2

### Presentation
3

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
This paper addresses a significant gap in the field of Neural Differential Equations (NDEs) models by focusing on regularization techniques. The authors identify a lack of effective regularization methods for NDEs and propose a novel approach to apply dropout in this context.

### Strengths
1. Innovative application of dropout: The authors have successfully adapted the dropout technique, which is commonly used in traditional neural networks, to Neural Differential Equations (NDEs). This adaptation shows a deep understanding of both NDEs and regularization techniques, bridging the gap between these two areas of machine learning.

2. Simplicity and versatility: The proposed method is remarkably straightforward, making it highly accessible and practical. Its simplicity does not compromise its effectiveness, and importantly, it can be easily applied to a wide range of NDE-based networks. This versatility enhances the method's potential impact across various applications and research areas within the field of continuous-time deep learning.

3. Excellent readability: The paper is exceptionally well-written, making it accessible to a broad audience. The authors have succeeded in presenting complex concepts in a clear and comprehensible manner, which is crucial for the dissemination and adoption of new ideas in the scientific community.

### Weaknesses
This paper lies in its narrow focus on dropout as a regularization technique for Neural Differential Equations (NDEs). While the direct application of dropout to the network is valuable, other regularization approaches exist for NDEs, such as using solvers as regularizers. The paper concentrates too heavily on dropout, potentially overlooking these alternative methods.

### Questions
Could this dropout method also lead to improved performance in models using advanced solvers [1]? I would like to see the test accuracy performance on CIFAR-10 by applying dropout to the solver proposed in [1]. 

Also, although dropout acts as a regularizer, it shows a larger performance variance compared to other baseline models in most experiments. Why is that?

[1] MALI: A memory efficient and reverse accurate integrator for Neural ODEs

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an extension to neural differential equations that functions similarly to the classical Dropout layer in standard neural networks. The extension is based on a renewal process defined by two hyperparameters: (i) the expected number of renewals, or on-off states, within a given time interval, and (ii) the probability of an "on" state after the interval. The authors demonstrate the utility of their method across different classification tasks.

### Strengths
The use of a renewal process is a novel concept, to the best of my knowledge.

The method's applicability is shown for several baseline models.

### Weaknesses
The paper's primary weakness lies in its motivation and presentation. While the authors position neural differential equations as an ideal tool for modeling continuous-time systems, they limit their experiments to classification problems rather than exploring continuous dynamical systems. Addressing this issue is essential for recommending acceptance.

### Questions
I'm unsure on the scaling aspect with your dropout layer. Typically, scaling is applied during training, but you've chosen to apply it only during inference. Could you elaborate on this design choice?

You reference Liu et al.'s work, "How Does Noise Help Robustness? Explanation and Exploration under the Neural SDE Framework," as the closest comparable method, but I noticed it’s missing from the comparison table. Could it be added for completeness?

Could you explain in more detail the difference between the Jump Diffusion process proposed by Liu et al. in "How Does Noise Help Robustness? Explanation and Exploration under the Neural SDE Framework", Dropout as described by Look et al. in "A Deterministic Approximation to Neural SDEs", and Dropout as proposed by you?

Would it be possible to extend your algorithm to use a non-fixed-step-size solver?

Could you elaborate on your point that SDEs serve as a regularizer for NDEs? To my knowledge, SDEs are not regularizers but are used for modeling different types of dynamical systems.

Could you discuss the effect of applying dropout to weights rather than inputs?

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
3

### Summary
This paper investigates regularization techniques for NDEs, with a particular emphasis on dropout methods. The authors introduce a novel NRSDE approach, grounded in alternating renewal processes that characterize dropout dynamics through transitions between active and inactive states. The paper includes a rigorous theoretical analysis, providing guidelines for selecting dropout rates and scaling outputs during the testing phase. Extensive experiments conducted across various systems demonstrate that the proposed method outperforms existing baseline models.

### Strengths
1. The focus on regularization for NDEs is somewhat interesting.
2. The study is presented with a high level of completeness, as the proposed method, along with the hyperparameter settings and scaling mechanisms, is thoroughly developed.
3. The manuscript is well-structured and clearly written, facilitating easy comprehension for readers.

### Weaknesses
1. My primary concern is regard the motivation for developing dropout techniques for NDEs in a way just like the ``true’’ dropout mechanism for conventional neural networks. The aim/effect of dropout is to mitigate overfitting via randomly disabling a subset of neurons. In this context, the dropout strategies proposed by Liu et al. (2020) appear to be adequate. In other words, I don't know why we should maintain the dynamics during inactive states.
2. In Section 3.3, the addition of $\mathbf{c}$ for scaling requires further explanation. 
3. Determining the value of $\mathbf{c}$ through Monte Carlo simulations during the testing phase could hinder the practical applicability of the proposed method. The experimental section would benefit from including an experiment that clearly demonstrates that the observed improvements are not simply attributable to test-time optimization.

### Questions
Please refer to weaknesses

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper is about taking dropout from feedforward networks and generalizing to continuous networks defined by Neural Differential Equations.

The paper identifies how to take dropout from the discrete to the continuous regime, as well as adapting test time behavior as is done in standard dropout.

The paper is well motivated, with a mixture of theory and more intuitive explanations. The evaluation is extensive and supports the use of this method over other Neural DE regularization schemes.

### Strengths
- The paper is very nicely written, there is a good mix of intuitive explanation with diagrams and theoretical insights.
- The contribution of generalizing dropout to continuous time networks is a valuable one.
- The evaluation is extensive and the results are convincing.

### Weaknesses
- Adjusting dropout to work at test time is an important part of this method. However, the approach is computationally expensive. My understanding is that around 5 additional forward passes of the NDE are required to estimate $c$. Is this required for every test point, or does this only need to be carried out once? Table 17 in the appendix would be improved by considering 0 samples so we can see the effect of including this correction term. The table would be further improved with a larger sensitivity analysis, including 1 sample, 2 samples etc. to see exactly when $c$ becomes useful.

### Questions
- I'm curious how vanilla dropout works on these datasets, where dropout is not applied to the output of the dynamics function, only the hidden layers. That way there are still full dynamics, but the dynamics function is still regularized. Is it possible to give numbers for this vanilla baseline?

### Soundness
3

### Presentation
4

### Contribution
3

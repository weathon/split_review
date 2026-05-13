# Switch EMA: A Free Lunch for Better Flatness and Sharpness

- Decision: Reject
- Scores: 5, 8, 6, 3

## Abstract
Exponential Moving Average (EMA) is a widely used weight averaging (WA) regularization to learn flat optima for better generalizations without extra cost in deep neural network (DNN) optimization. 
Despite achieving better flatness, existing WA methods might fall into worse final performances or require extra test-time computations.
This work unveils the full potential of EMA with \textit{a single line of modification}, \textit{i.e.}, switching the EMA parameters to the original model after each epoch, dubbed as Switch EMA (SEMA). 
From both theoretical and empirical aspects, we demonstrate that SEMA can help DNNs to reach generalization optima that better trade-off between flatness and sharpness.
To verify the effectiveness of SEMA, we conduct comparison experiments with discriminative, generative, and regression tasks on vision and language datasets, including image classification, self-supervised learning, object detection and segmentation, image generation, video prediction, attribute regression, and language modeling.
Comprehensive results with popular optimizers and networks show that SEMA is a free lunch for DNN training by improving performances and boosting convergence speeds.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes SEMA methods, which apply exponential moving average (EMA) periodically at specific intervals to improve model "sharpness" and "flatness." The authors provide theoretical analysis and present extensive experimental results across various domains, including image classification, self-supervised learning, object detection, video prediction, and language modeling.

### Strengths
The authors conduct comprehensive experiments in diverse areas such as image classification, self-supervised learning, object detection, video prediction, and language modeling, highlighting the advantages of the proposed method.

### Weaknesses
## **Sharpness vs. Flatness?**
The paper introduces the concepts of sharpness and flatness but lacks precise mathematical definitions, which deviates from conventional terminology. The authors' interpretation of sharpness as the depth and flatness as the width of local minima is not rigorously defined. A more appropriate approach would involve analyzing the eigenvalues of the Hessian matrix of the loss function. Specifically, the magnitude of the eigenvalues provides information about the curvature of the loss landscape, with larger eigenvalues indicating sharper curvature and smaller eigenvalues indicating flatter curvature. Without a clear definition based on the Hessian's eigenvalues, it is difficult to assess the validity of the claims regarding the impact of SEMA on these properties.

## **Concerns over Statistical Validity**
The experimental results lack standard deviation values, and with a maximum of only three trials conducted, the statistical significance of the findings is questionable. This limited number of trials makes it challenging to ascertain the robustness of the conclusions and whether the observed improvements are consistent or due to random chance. To establish statistical significance, a larger number of trials and the inclusion of standard deviation values are necessary.

## **Some Definitions of Mathematical Terminologoies are Missing**
Several mathematical definitions are missing, which hinders the reader's comprehension.
- In eq(1), the definitions of $\Theta^{\text{OPT}}$ and $\Theta^{\text{EMA}}$ are not provided. It is unclear what these terms represent and how they are updated.
- In Proposition 1, the exact definition of variance is missing. For instance, it should be explicitly stated as $V^{(t)}_{\text{SGD}}:= \mathbb{V}(\Theta_t^{\text{SGD}})$.
- In Proposition 1, the condition for a small learning rate $\eta$ is not specified. The convergence analysis likely relies on the assumption that $\frac{2}{\eta}$ is larger than the top eigenvalue of matrix $A$ to apply Banach's fixed point theorem. Without this condition, the theoretical guarantees are incomplete.
- There are typos in lines 1082-1083, 1122-1123, and 1133 where subscripts on $\mathcal{E}$ are missing, which should be corrected for clarity.

### questions:
 - Can the author provide the mathematical definition for sharpness and flatness considered in this paper? Specifically, how are these concepts related to the eigenvalues of the Hessian matrix?
- Why does (7) implies $ E_{\text{SEMA}}<E_{\text{EMA}}<E_{\text{SGD}}$ ? Equation (7) only provides upper bounds for these terms. Comparing only upper bounds does not logically support the conclusion that $E_{\text{SEMA}}<E_{\text{EMA}}<E_{\text{SGD}}$. A more rigorous justification is needed, potentially involving lower bounds or a different analytical approach.
- In (6), which terms are hidden in the $\propto$ notation? If the hidden constant varies across iterations $t$, Proposition 2 may not guarantee convergence, even for convex functions. The hidden constant could potentially be excessively large for certain iterates, invalidating the convergence claim.

### Questions
- Can the author provide the mathematical definition for sharpness and flatness considered in this paper?
- Why does (7) implies $ E_{\text{SEMA}}<E_{\text{EMA}}<E_{\text{SGD}}$ ?
 It seems that (7) only provides upper bounds for the three terms, and I believe that comparing only upper bounds does not support the conclusion that $E_{\text{SEMA}}<E_{\text{EMA}}<E_{\text{SGD}}$.
- In (6), which terms are hidden in the $\propto$ notation?If the hidden constant is inconsistent across iterations $t$,I believe that Proposition 2 does not guarantee convergence, even for convex functions, as the hidden constant could be too large for certain iterates.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a simple yet powerful algorithm, switch exponential moving average (SEMA), to improve the stability, convergence, and generalization performance of optimization of deep neural networks using a family of stochastic gradient descent methods. SEMA is a very simple method that updates the training parameters with EMA parameters once per epoch for existing EMAs. The paper conceives the algorithm based on experimental observations but also theoretically shows that it improves optimization stability, convergence speed, and generalization error bounds. In addition, the paper evaluates SEMA on various tasks, domains, architecture, training algorithms, and optimization algorithm combinations using SEMA and confirms that it improves the baseline in all cases.

### Strengths
- The paper proposes an practical algorithm that is widely applicable and stably improves the performance of optimization of neural networks using stochastic gradient descent.
- The paper investigates the theoretical properties have been well analyzed to investigate why a simple EMA improvement is effective.
- The effectiveness of the proposed algorithm is evaluated through extensive experiments.

### Weaknesses
 - Although the experiments provided in the paper are basically extensive, further verification of the smoother decision boundary by SEMA discussed in Sec. 3.2 would be beneficial to the reader. The paper mentions the performance against fine-grained discrimination in L268, but in fact, the main focus of the experiments is on coarse-grained evaluation. For example, the performance on FGVCAircraft [a], CUB [b], Stanford Cars [c], etc., which are often used to evaluate fine-grained classification, and the evaluation of adversarial robustness, as shown in [d], would be useful.
- Since the standard deviation of the experimental results is not given, it is not possible to evaluate how stable SEMA actually is.

### Questions
Nothing to ask. Please see the weaknesses section and address the concerns.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel optimization method called SEMA, which incorporates flatness and sharpness by switching between fast and slow models at the end of each training epoch. SEMA results in faster convergence, better performance, and smoother decision-making. Extensive experiments have been conducted to demonstrate the effectiveness of SEMA in improving model performance across various scenarios, along with comprehensive and well-founded theoretical proofs.

### Strengths
1. The paper is very well written and it was easy for me to follow.
2. The paper focuses on the key issues of optimizers and creatively improves existing methods, presenting a novel approach.
3. The paper demonstrates the effectiveness of the method through extensive experiments and theoretical analysis.

### Weaknesses
1. The legend in the upper right corner of each curve plot in Figure 2 is quite small, requiring significant magnification to be readable.
2. There is no clear explanation of the data distribution visualization formats used in Figure 4 and Figure A.1.

### Questions
Why does the baseline in Figure 4 have a decision boundary represented by two lines? If the decision boundary is like this, achieving an accuracy of 0.8 seems somewhat unreasonable.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new weight averaging approach SEMA that seeks to optimize both flatness and sharpness of optima when training NNs. SEMA relies on a simple change to EMA: the EMA parameters are switched to the original model parameters after K epochs. The authors provide theoretical and empirical validation of SEMA: SEMA is evaluated across a very large number of tasks against other weight averaging techniques.

### Strengths
* The proposed change in EMA is sensible and simple; the proposed intuitions (balancing flatness and sharpness) for the change are well motivated.
* The authors propose some theoretical motivation to SEMA, including variance analysis, convergence analysis and error bounds.
* The evaluation is extremely thorough and covers an extremely large number of tasks, architectures.

### Weaknesses
 * Despite all these positive comments that show that the execution of the work was well lead, I feel that the proposed change is relatively minor to justify an acceptance to ICLR. the change is in practice a single line change, and does not significantly change the mechanisms behind EMA. The improvement to the models is relatively modest, although this may justify using SEMA as an alternative to EMA to gain a little bit in performance. On this point, I feel that including some variance across training seeds could at least provide some more information to appreciate the improvement.

### Questions
* Could the authors report variance over several seeds on some well chosen datasets to show that the improvements are at least statistically significant ?

### Soundness
3

### Presentation
3

### Contribution
2

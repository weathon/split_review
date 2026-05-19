### Summary

The paper proposes a meta-learning framework for learning the underlying dynamics of a system of ODEs. The authors claim that the proposed method is robust to OOD shifts in initial conditions and ODE parameters. The method is evaluated on three synthetic datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is well-motivated and the empirical results show that it outperforms existing methods on the considered tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The method assumes that the basis functions are known. This is a strong assumption that may not hold in practice. It would be interesting to see how the method performs when the basis functions are not known and need to be learned from data.
- The method is evaluated only on synthetic datasets. It would be interesting to see how the method performs on real-world datasets.
- The method is evaluated on ODEs with a small number of parameters. It would be interesting to see how the method performs on ODEs with a larger number of parameters.

### Suggestions

The assumption of known basis functions is a significant limitation that restricts the applicability of the proposed method. While the authors argue that domain expertise can inform the choice of basis functions, this is not always feasible or reliable in complex systems. A more robust approach would involve incorporating a mechanism for learning the basis functions directly from data, perhaps using a library of candidate functions and selecting the most relevant ones through a sparse identification process. This would not only make the method more generalizable but also allow it to discover underlying dynamics that might not be immediately apparent from prior knowledge. Furthermore, the current approach does not address the potential for overfitting when the number of basis functions is large relative to the amount of training data, which could lead to poor generalization performance, especially in OOD settings. 

The evaluation of the method on only synthetic datasets raises concerns about its practical utility. While synthetic data allows for controlled experiments, it often fails to capture the complexities and noise present in real-world data. To demonstrate the method's effectiveness, it is crucial to evaluate it on real-world datasets from diverse domains, such as climate modeling, epidemiology, or robotics. These datasets often exhibit non-stationary behavior, measurement noise, and other challenges that are not present in synthetic data. Furthermore, the method's performance should be compared against established baselines that are commonly used in these domains. This would provide a more comprehensive assessment of the method's strengths and weaknesses and its potential for real-world impact. The current evaluation also lacks a detailed analysis of the method's sensitivity to hyperparameter settings, which is crucial for practical deployment.

The evaluation on ODEs with a small number of parameters is another limitation that needs to be addressed. Many real-world systems are governed by complex ODEs with a large number of parameters, and it is unclear how the proposed method would scale to such systems. The authors should investigate the method's performance on more complex ODEs with a larger number of parameters, and analyze its computational cost and memory requirements. It would also be beneficial to explore techniques for reducing the computational burden, such as using sparse representations or low-rank approximations. Furthermore, the method's ability to handle stiff ODEs, which are common in many scientific applications, should be investigated. This would provide a more comprehensive understanding of the method's limitations and its potential for addressing real-world challenges.

### Questions

- How does the method perform when the basis functions are not known and need to be learned from data?
- How does the method perform on real-world datasets?
- How does the method perform on ODEs with a larger number of parameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

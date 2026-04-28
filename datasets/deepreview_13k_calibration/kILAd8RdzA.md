# On the Generalization and Approximation Capacities of Neural Controlled Differential Equations

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
Neural Controlled Differential Equations (NCDEs) are a state-of-the-art tool for supervised learning with irregularly sampled time series \citep{kidger2020neural}. In this article, we provide the first statistical analysis of their performance by merging the rich theory of controlled differential equations (CDE) and Lipschitz-based measures of the complexity of deep neural nets. Our first result is a generalization bound for this class of predictors that depends on the regularity of the time series data. In a second time, we leverage the continuity of the flow of CDEs to provide a detailed analysis of both the sampling-induced bias and the approximation bias. Regarding this last result, we show how classical approximation results on neural nets may transfer to NCDEs. Our theoretical results are validated through a series of experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper makes a first-of-its-kind attempt at bounding the generalization error of NCDE.

### Strengths
The analysis done is thorough and it is definitely an achievement to have setup the formalism required to compute a generalization bound like this.

### Weaknesses
In Section 4, Theorem 4.1 the upper bound for the generalization error varies with both the width and depth of the neural network and unlike Chen et al. (2019a), where the growth w.r.t the depth and width is logarithmic, in this case it’s polynomial. This exponential blow-up in the value of bound makes the whole exercise somewhat underwhelming.

Also its worth mentioning that the discretization dependence in Theorem 4.1 is through the constants K1^D and K2^D
 - and these two critical quantities don't seem defined anywhere in the main paper! This makes the theorem highly opaque!

The entire point why a generalization error bound is interesting is because it reveals the generalization error to be independent of some natural size parameter of the system. Like, most often the baseline achievement of a Rademacher bound for a neural system is to show that at a fixed depth and norm bound on the weights involved the generalization is width independent. In this bound, in this work, there is absolutely no such thing happening - the bound in Theorem 4.1 is worsening with every such parameter with which naively one would have expected worsening to happen!

The numerical Illustrations also seem incomplete in the absence of any demonstration of how well the bounds hold up in the cases mentioned there. In the bare minimum, in Figure 4 kind of experiments one would have expected to see a scatter plot of the theoretical bound and the true generalization error as the sampling gap, time and avg. max path variation is changed. Such a scatter plot would have revealed if there is at all any correlation between the theoretical bound and the truth.

### Questions
Q1.
Can the authors explain why there is an exponential degradation of the bound's dependence on width as compared to the result in Chen et al. (2019a), which seems to be the closest literature to this? Can you argue that this degradation is inevitable? 

Q2.
Can the authors point out as to what is the surprise or the non-triviality about the dependencies that are visible in the bound given in Theorem 4.1?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript presents a theoretical investigation into the generalization and approximation capacities of neural controlled differential equations (NCDEs). It aims to answer critical questions about the generalization and approximation capabilities of NCDEs and how these are affected by irregular sampling. The theoretical contributions are backed by experiments. The authors provide a rigorous mathematical framework to offer insights into the capabilities and limitations of NCDEs.

### Strengths
Originality:
The paper stands out for its focus on providing a theoretical framework for NCDEs. This can serve as a foundational work for further investigations.
Quality:
The mathematical rigor of the paper is high, with well-laid-out proofs and theoretical discussions.
Clarity:
Despite the mathematical complexity, the paper is organized in a way that progressively builds up the reader's understanding of the topic.
Significance:
The theoretical insights offered could be highly impactful, providing guidelines for both practical applications and future research in machine learning and control theory.

### Weaknesses
In Abstract: ``However, no theoretical analysis of their performance has been provided yet''. This is not true. 

The paper could do a better job of situating its contributions within the existing literature, especially to clarify its novelty.

While the focus is theoretical, some discussion on the practical implications of these theories could make the paper more well-rounded.

There are some grammar/format issues, such as, ``since y is the sum of a linear transformation of the endpoint of a CDE an a noise term ε bounded by …’’

### Questions
Could you clarify how your theoretical contributions on the approximation part diverge from existing works on the approximation ability of NCDE like [1] or [2]?

[1] Patrick Kidger. On neural differential equations. arXiv preprint arXiv:2202.02435, 2022.

[2] Patrick Kidger, James Morrill, James Foster, and Terry Lyons. Neural controlled differential equations for irregular time series. Advances in Neural Information Processing Systems, 33:6696–6707, 2020. 

What are the potential practical applications that could benefit from the theoretical insights provided in this paper? Could these insights lead to more efficient or accurate NCDE models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the generalization bound for neural-controlled differential equations(NCDE). Given an NCDE that minimizes the empirical risk from some sampled data, the author first derives a generalization bound between the empirical and expected risk given the sampling process for the input time series, and then an upper bound on the difference between the expected risk and the optimal risk from the ground truth predictor.

### Strengths
1. novel generalization bound for neural-controlled differential equations.
2. an upper bound on the excessive risk from sampling-induced bias and approximation bias.

### Weaknesses
1. The presentation in Theorem 4.1 could be improved, as it is hard to see how the bound explicitly depends on depth $q$, and discretization $D$. Right now it is hidden in the constant $C_q$ and $K_1^D, K_2^D$. It would be beneficial to have a more transparent representation of how these parameters influence the generalization bound. For instance, it would be helpful to see if the bound scales polynomially or exponentially with respect to $q$ and how the discretization step size within $D$ affects the constants $K_1^D$ and $K_2^D$. Without this explicit dependence, it is difficult to assess the practical implications of the theoretical results.
2. The experiments seem very preliminary: the sampled time series only have $K=5$ points. I am not sure how interesting it is to investigate this regime as the generalization error would be poor with this few samples. The lack of experiments with a larger number of sampled points makes it difficult to validate the theoretical bounds derived in the paper. It would be more convincing to see experiments that explore the behavior of the model with a more substantial number of data points, as this would more closely reflect practical applications. The current experiments do not provide sufficient empirical evidence to support the theoretical claims, particularly in regimes where generalization is more relevant.

### Questions
1. Any assumption on the continuous $x$, or its distribution, if it is random.
2. $|D|$ appears in Remark 3.5, but defined much later.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

# Stochastic two points method for deep model gradient free optimization

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Large foundation models, such as large language models, have performed exceptionally well in various application scenarios. 
Building or fully fine-tuning such large models is usually prohibitive due to either hardware budget or lack of access to backpropagation.
The zeroth-order methods offer a promising direction for tackling this challenge, where only forward passes are needed to update the model.   
This paper introduces an efficient Stochastic Two-Point (S2P) approach within the gradient-free regime.  
We present the theoretical convergence properties of S2P under the general and relaxed smoothness assumptions, and the derived results help understand and inherently connect the two popular types of zeroth-order methods, basic random search and stochastic three-point method.
The theoretical properties also shed light on a Variant of S2P (VS2P), through exploiting our new convergence properties that better represent the dynamics of deep models in training.
Our comprehensive empirical results show that VS2P is highly effective in optimizing objectives for deep models. It outperforms or achieves competitive performance compared to standard methods across various model types and scales.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose a stochastic two-point method for optimizing deep neural networks without resorting to gradient descent optimization techniques. Besides, the same authors propose an even accelerated version of it and compare it to other gradient-free approaches. The authors propose convergence analysis and conduct some experiments.

### Strengths
- the work proposes a new gradient-free optimization method. In a world computationally-constrained, this is prospectively a promising research path
- although I could not check the correctness, the authors make a big effort to ground the approach
- the authors even tested on a LLM

### Weaknesses
 - no comparison (apparently) with standard gradient descent approaches
- empirical analysis limited to relatively small tasks using relatively large architectures
- (minor) graphics is barely readable, and so the results

### Questions
- how is the proposed approach performing, compared with traditional gradient descent (with for example SGD or Adam)?
- how is the approach performing in more dataset-challenging scenarios where the model is not able to overfit on the given task (like ResNet-18 trained on ImageNet1k)?
- how is the approach performing with architectures without skip connections? 
- how much extra memory is the proposed approach consuming compared to other competitors?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors are striving to propose a gradient-free learning method, called Stochastic Two-Point. The method is derived from the Stochastic Three-Point approach, where the proposed method ignores the current weight within the three-point set during optimization. The authors give some theoretical analysis in regards to the convergence of the proposed two-point method. And to show the effectiveness of the proposed method, the authors give results on Cifar dataset and some nlp tasks.

### Strengths
**Strengths**

1. The paper is clearly written and easy to follow. 
2. It is interesting to see a forward-only method for optimization. Although currently such methods may give much worse results compared to bp, I think they are very promising in tackling problems in specific scenarios, such as optimizing non-differentiable loss.
3. From the experiment results, the proposed method could give comparable results.

### Weaknesses
 **Weakness**

1. This paper basically follows the paper of three point method. The key difference is that this paper ignores the current weight when solving the argmin in optimization. But in the STP method, it is crucial that the current weight gives guarantee on the monotonicity of optimization. Without such guarantee, it seems quite not likely that the method could reach a suboptimal condition, i.e. $min ||g|| \leq \epsilon$. Given that the current weight is ignored in the proposed two point method, how the authors ensure the minimization is non-increasing? I have not found any discussions in regards to the failure cases.

    I notice that the Theorem 3.1 presents a similar conclusion in regards to that in STP. The theorem actually implies that the method could reach at suboptimal under certain condition. But to my understanding, the convergence properties could be worse than the STP method, where the proposed method is proved to converge over estimation. Could the authors give detailed comparisons between the proposed method and STP, given that the two methods are quite similar.

2. I am wondering could the authors provide some evidence other than the results that the proposed method could give better approximation compared to other similar methods? That would be more substantial to support the superiority of your methods. For example, the authors could measure the distance between the optimal model and the model trained with the proposed method. 

3. Regarding the experiments, firstly the authors may need to compare some other advanced similar methods, like the MEZO (Sadhika Malladi) cited by the authors. Secondly, the evaluation performance is missing regarding training on the Cifar datasets. Thirdly, I think the authors may need to add results of using bp gradient to give reference. Fourthly, the figures are quite not friendly to read, to present clear comparison, the authors may provide tables in addition. Finally, it is highly recommended that the authors can release their code for reproductivity.

### Questions
See weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new method called Stochastic Two-Point (S2P) for gradient-free optimization of large deep models, including language models. The authors analyze the convergence properties of S2P under general and relaxed smoothness assumptions and propose a faster variant called Accelerated S2P (AS2P). Extensive experiments demonstrate that AS2P outperforms standard methods and achieves significant speed-up in training large deep models. The contributions of the paper include novel insights into query complexity and the development of an efficient optimization approach for models with limited computational resources.

### Strengths
1. This paper has provided strong theoretical support for the newly proposed algorithms S2P and AS2P.
2. This paper is generally well presented.

### Weaknesses
1. This paper does not give a convincing motivation of using L0,L1-smoothness for the proof of zeroth-order optimization algorithms, which therefore make it hard to know whether it is really necessary to give another proof (compared with using the existing ones).
2. The comparison and discussion on other existing zeroth-order optimization algorithms of this paper are limited, e.g., GLD and ZoRD.
3. The performance of the S2P and AS2P seems to be limited as they are only able to reduce the training loss slightly, which is significantly worse than the first order optimization as shown in Fig.1b.
4. While this paper is motivated by LLM training, this paper does not give any empirical experiments to show that it indeed can help solve the problem in LLM training.

### Questions
1. Why the L0,L1-smoothness will be more realistic in practice especially for the training of LLM? Any empirical or theoretical support?
2. Why the convergence proof of this paper requires that 3.2 and 3.3 are satisfied at the same time? From my understanding 3.2 can infer that L0=L and L1=0 in 3.3.
3. Can the authors provide a figure that compares the convergence w.r.t. number of queries during optimization among S2P/AS2P and other ZOO algorithms.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this submission, a zero-order optimiser, S2p, is proposed for efficient training for LLM along with theoretical analysis. Based on its theoretical findings, an accelerated version of S2P, AS2P, is studied by automatically tuning with learning rate while it is supported by two methods progressive \gama-cliplling and Automatic learning rate. The algorithm, AS2P, is tested on a variety of tasks including LLM training and some vision classification tasks with achieving noticeable improving margin for both training loss and convergence speed compared with the existing zero-order optimisers, STP and GA.

### Strengths
The proposed algorithm AS2P is compared with other zero-order-based optimisers on a variety of tasks showing a noticeable margin. 
The paper is well-written and easy to understand.

### Weaknesses
1. The theoretical results are not directly related to the good performance of AS2P. 
2. The recent work for gradient-free optimiser is not compared in the submission. For example, 
Lin T, Zheng Z, Jordan M. Gradient-free methods for deterministic and stochastic nonsmooth nonconvex optimization. Advances in Neural Information Processing Systems. 2022 Dec 6;35:26160-75.

### Questions
1. Two main practical methods, progressive \gama-cliplling and Automatic learning rate, are introduced to increase the convergence rate which is also justified by the later experiments. It is not theoretically clear why AS2P has a better convergence rate than S2P. Does it mean these two methods are derived from the based on the previous theorem? 
2. The imperial results show that the proposed algorithm especially AS2P has a better convergence rate compared with other zero-order algorithms, still first-order optimisers are commonly used in the practice, Do the authors base line for that? 
3. From theorem 3.1 and theorem 3.2, four options are provided for setting \alpha_k iteratively. So what are the differences in practice? Is AS2P a special case of Option 4? 
4. In all the experiments, AS2P outperforms GA and STP in terms of both the convergence speed and training and evaluation loss. Does the author give a fair hyperparameter tuning to all the competitors? And how the others are tuned? In the proposed theorem, there is no clear theoretical guarantee showing the convergence rate f(x)-f*(x) is improved in the paper can the author give more explanation? 
5. When the zero-order optimiser is needed for LLM training? Without using gradient information how worse the trained model will be compared with that trained gradient-based optimiser such as AdamW? 

Typo: In the last paragraph on Page 8. Figure 7(a) should be Figure 3(a)

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

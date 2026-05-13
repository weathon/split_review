# EControl: Fast Distributed Optimization with Compression and Error Control

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Modern distributed training relies heavily on communication compression to reduce the communication overhead. In this work, we study algorithms employing a popular class of contractive compressors in order to reduce communication overhead. However, the naive implementation often leads to unstable convergence or even exponential divergence due to the compression bias. Error Compensation (\algname{EC}) is an extremely popular mechanism to mitigate the aforementioned issues during the training of models enhanced by contractive compression operators. Compared to the effectiveness of \algname{EC} in the data homogeneous regime, the understanding of the practicality and theoretical foundations of \algname{EC} in the data heterogeneous regime is limited. Existing convergence analyses typically rely on strong assumptions such as bounded gradients, bounded data heterogeneity, or large batch accesses, which are often infeasible in modern machine learning applications. We resolve the majority of current issues by proposing \algname{EControl}, a novel mechanism that can regulate error compensation by controlling the strength of the feedback signal. We prove fast convergence for \algname{EControl} in standard strongly convex, general convex, and nonconvex settings without any additional assumptions on the problem or data heterogeneity. We conduct extensive numerical evaluations to illustrate the efficacy of our method and support our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a new EC algorithm for distributed training with communication compression. Unlike traditional error compensation methods where we only add the previous compression back to the compressed gradient, in EControl authors achieve a faster convergence rate by controlling the strength of the feedback signal. Authors proved the superiority of EControl from both theoretical and experimental side.

### Strengths
The algorithm design looks smart to me. By starting from the EC-ideal, the convergence rate of the compressed SGD could achieve optimal asymptotic complexity. Afterwards authors further extend this idea to general cases where h^* cannot be attained.

### Weaknesses
1. It is unknown how to combine EControl with momentum SGD. The original EF has well-developed momentum variants. EF21 has the variant of EF21-SGDM. Although the experiments include EF21-SGDM, there is no EControl + momentum provided.

2. There seems to be a strong connection between EControl and EF21. If we the compressed version of $h$ in the initialization $h_0^i = \mathcal{C}(g_0^i)$, and take $\eta = 0$, then EControl will be equivalent to EF21. In other words, with a little bit twist in the initialization, EF21 can be viewed as a special case of EControl. However, I haven't found any discussion about the relationship between EControl and EF21 like this. Furthermore, I recommend to add some ablation experiments where $\eta$ varies and gets tuned gradually closer to 0, which I guess will give a training loss curve closer to EF21.

### Questions
No

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes EControl, a novel mechanism that can regulate error compensation by controlling the strength of the feedback signal. Theoretical analysis is provided for EControl in strongly convex, general convex, and nonconvex settings without any additional assumptions on the problem or data heterogeneity. The experiments show that the proposed algorithm out-performs the baselines in large-scale vision tasks.

### Strengths
1. This paper proposes EControl, a novel mechanism that can regulate error compensation by controlling the strength of the feedback signal. 

2. Theoretical analysis is provided for EControl in strongly convex, general convex, and nonconvex settings without any additional assumptions on the problem or data heterogeneity. 

3. The experiments show that the proposed algorithm out-performs the baselines in large-scale vision tasks.

### Weaknesses
While the importance of the crucial parameter $\eta$ in EControl is discussed in section 4, its significance could benefit from a more comprehensive explanation within the main body of the paper. I would strongly recommend the inclusion of lemmas and inequalities to elucidate the pivotal role of $\eta$. Additionally, providing similars lemmas into how $h_t^i$ approximates gradient information and how the strength of the feedback signal is controlled would enhance the clarity and understanding of the proposed method.

### Questions
1. Is there a variant of EControl which is combined with momentum?

2. Could the authors give a more detailed discussion about the (theoretical) connection and comparison between EControl and EF21?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents EControl, a novel algorithm introduced to address communication compression challenges in modern distributed training. EControl utilizes contractive compressors to reduce communication overhead, effectively mitigating issues like unstable convergence and compression bias commonly associated with naive implementations. Notably, EControl's standout feature lies in its ability to regulate error compensation by controlling the feedback signal's strength, making it a valuable solution for data heterogeneous scenarios.

Unlike previous methods, EControl dispenses with impractical assumptions such as bounded gradients or data homogeneity. It demonstrates rapid convergence rates in standard convex and nonconvex settings, showcasing its adaptability and robustness. Through comprehensive numerical evaluations, the paper substantiates the effectiveness of EControl, highlighting its potential to revolutionize distributed training by alleviating communication overhead challenges and facilitating more efficient and stable model training processes.

### Strengths
The proposed method EControl does not need the assumptions such as large batchsizes and bounded gradient, it also enjoys linearly speedup, therefore, it overcomes the shortcomings of previous error-compensation framework.

### Weaknesses
-In step 6 of EC-Ideal you don't have the extra parameter \eta that you have in EControl, can you explain why for EC-Ideal this is not needed. Will EC-Ideal have the same convergence guarantees if you add \eta in step 6, with the same values as for EControl?
-Bounded variance: This assumption contradicts strong convexity. I understand it is in several works in the literature. Take for instance F(x,y,z) = zx^2 + (1-z)y^2, z follows Bernoulli (1/2), then E_z(norm(\nabla F(x,y,z) - \nabla E_z(F(x,y,z)))^2) = (x-y)^2 and this is not bounded for all x and y in R. The bounded variance assumption, while common, is restrictive. For stochastic optimization or large finite sums, access to the exact gradient is often impossible; instead, we rely on sampling, as illustrated in the provided example. This means there's no guarantee of bounded variance. Even when the exact gradient is computable, adding noise to create a stochastic gradient is unnecessary; the gradient itself can be used directly. Therefore, it's crucial to provide practical scenarios where this assumption is realistic.
-You mention in page 7 that "The asymptotic complexity of EControl in this regime with stochastic gradient is tight and cannot be improved,"  I understand for the depence on \epsilon, however can you tell why the dependence on other parameters can not be improved.
-In the experiments, how you relate \zeta to the noniddness, why for instance zeta equal to zero is iid and zeta >0 is non idd. The connection between \zeta and non-IID data is not clear, especially in overparameterized settings like neural networks. The measure \bar{\zeta} is not a good measure of heterogeneity. For instance, if $f(x) = \sum f_i(x_i)$ where $x = (x_1,...)$, then regardless of the dissimilarity of the $f_i$s, \bar{\zeta} = 0. The justification that \bar{\zeta} measures the diversity of functions $f_i$ because if all functions are the same, $f_i=f_j$ for all $i,j$, then \bar{\zeta}=0 is not convincing. Similarity between $f_i$s does not mean equality. What constitutes similarity or dissimilarity between the $f_i$s needs to be defined more precisely.
-Did you try \eta= delta/400 suggested by the theory in the experiments? why you need to fine tune it, since it is fixed by theory. Is only fixed \eta = \delta/400 that works in theory or many other values can work, this is not clear in the paper.
-Did you test with other compressors?

### Questions
Same questions related to the issues on specific lemmas or inequlities asked in "Weaknesses".

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes EControl algorithm that provably converges for strongly convex, convex, and nonconvex, with general contractive compression and with classic assumptions on the problem. It also gives experimental evaluations of EControl to show its efficacy
in practice.

### Strengths
New error compensation algorithm: EControl with theoritical gaurantees for strongly convex, general convex, and nonconvex functions
Empirical experiments to support the theoretical gaurantees and assess the efficacy of EControl.

### Weaknesses
see the section below (Questions)

### Questions
-In step 6 of EC-Ideal you don't have the extra parameter \eta that you have in EControl, can you explain why for EC-Ideal this is not needed. Will EC-Ideal have the same convergence guarantees if you add \eta in step 6, with the same values as for EControl?
-Bounded variance: This assumption contradicts strong convexity. I understand it is in several works in the literature. Take for instance F(x,y,z) = zx^2 + (1-z)y^2, z follows Bernoulli (1/2), then E_z(norm(\nabla F(x,y,z) - \nabla E_z(F(x,y,z)))^2) = (x-y)^2 and this is not bounded for all x and y in R.
-You mention in page 7 that "The asymptotic complexity of EControl in this regime with stochastic gradient is tight and cannot be improved,"  I understand for the depence on \epsilon, however can you tell why the dependence on other parameters can not be improved.
-In the experiments, how you relate \zeta to the noniddness, why for instance zeta equal to zero is iid and zeta >0 is non idd.
-Did you try \eta= delta/400 suggested by the theory in the experiments? why you need to fine tune it, since it is fixed by theory. Is only fixed \eta = \delta/400 that works in theory or many other values can work, this is not clear in the paper.
-Did you test with other compressors?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

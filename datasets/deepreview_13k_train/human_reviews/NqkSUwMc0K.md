# Private Blind Model Averaging – Distributed, Non-interactive, and Convergent

- Decision: Reject
- Scores: 1, 8, 3, 3, 3

## Abstract
Scalable distributed differentially private learning would benefit notably from reduced communication and synchronization overhead. The current best methods, based on gradient averaging, inherently require many synchronization rounds. In this work, we analyze blind model averaging for convex and smooth empirical risk minimization (ERM): each user first locally finishes training a model and then submits the model for secure averaging without any client-side online synchronization. This setting lends itself not only to data point-level privacy but also to flexible user-level privacy, where the combined impact of the user’s trained model does not depend on the number of data points used for training.

In detail, we analyze the utility side of blind model averaging for support vector machines (SVMs) and the inherently multi-class Softmax regression (SoftmaxReg). On the theory side, we use strong duality to show for SVMs that blind model averaging converges toward centralized training performance if the task is robust against L2-regularization, i.e. if increasing the regularization weight does not destroy utility. Furthermore, we provide theoretical and experimental evidence that blind averaged Softmax Regression works well: we prove strong convexity of the dual problem by proving smoothness of the primal problem. Using this result, we also conclude the first output perturbation bounds for Softmax regression. On the experimental side, we support our theoretical SVM convergence. Furthermore, we observe hints of an even more fine-granular connection between good utility of model averaging and mid-range regularization weights which lead to compelling utility-privacy-tradeoffs for SVM and Softmax regression on 3 datasets (CIFAR-10, CIFAR-100, and federated EMNIST embeddings). We additionally provide ablation for an artificially extreme non-IID scenario.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper considers *blind model averaging* for differentially private federated learning. Here, each "user" holds data for many individuals, whose privacy we wish to protect. Each user trains a model locally with privacy. These models are averaged to produce a final model.

### Strengths
This is a topic of practical and theoretical interest. I am not deeply acquainted with this literature, but to the best of my knowledge the questions considered in this submission are not fully answered by prior work.

### Weaknesses
I found this paper hard to read and do not believe it meets the necessary level of rigor.

I was often confused by the organization and informal discussion. Here are a couple issues I observed.
- Figure 1 lists "Phase I" as "local ERM training" for SVM or softmaxReg and "Phase II" as the averaging, but Section 4 is "PHASE I: DIFFERENTIALLY PRIVATE SOFTMAXREG" and doesn't include any analysis of SVMs. Then Section 5, titled "PHASE II: NON-INTERACTIVE BLIND MODEL AVERAGING (BLINDAVG)", only appears to address SVMs. Then Section 6 is "SYSTEM DESIGN OF BLINDAVG", which I would think also describes Phase II.
- Some crucial concepts appear undefined, like "honest" users or the version of SGD used.
- Definition 3.1 is where we define the "configuration," ie learning setting, but it has a number of strange features. It introduces the notation $I$ for the identity matrix and $K_{\mathrm{comp}}$ for "the number of compositions," but neither are used in the notation $\zeta(\cdots)$ that denotes the configuration. "$i$" is used, but that confuses me, since it appears to just index into the set $\{1,\ldots, w\}$. "$n$" also appears but is undefined.
- Theorem 3.2 mentions parameters $c$ and $R$ in the hypothesis but not in the conclusion; these are only tied to $\Lambda, L,$ and $\beta$ later in the text. 

On a technical level, I will focus on Theorem 5.2, which concerns the convergence of an average of SVMs, each trained on a subset of the data, to the "global" model trained on all the data. Here are a few issues around this.
1. The theorem and proof don't address the noise for privacy. I don't understand how these results relate to claims about the privately trained model.
2. The proof establishes that, for a sufficiently large $\ell_2$ penalty, the average (over the best local models) equals the best global model (ie, over all data). It's not clear why this is interesting: we can obtain an approximate version of this claim "at a glance" by noting that sufficiently high regularization will push all weights to zero. It's not clear why we should care about such a regime.
3. The theorem mentions "projected subgradient descent using weighted averaging," but it doesn't show up in the algorithms and is only mentioned, but not described, in the proof. Algorithm 3 uses projected SGD but doesn't specify what that entails.
4. I'm confused by what it means to take the average of the models, even in Definition 3.1: I don't understand the "type" of $T$, so it's not clear why $\sum_i T(D^{(i)})$ is well-defined. In the proof of Corollary K.2 it looks like we sum models in the dual space, but Algs 2 and 3 look to me like we're working in the weight space. I think this distinction matters when we talk about adding noise.
5. The theorem relies on Lemma 5.1, which (in its proof) assumes that the datasets are disjoint, i.e., no two data points are repeated across users. I don't see why this is a justified assumption, as differential privacy needs to hold for worst-case datasets.
6. Two sections in the appendix are titled "Proof of Thm 5.2", J.5.2 and K.5.2, only the latter actually contains a proof.

This submission would need substantial revisions before I would be comfortable accepting it.

### Questions
No questions.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper tackles the reduction of communication and synchronization overhead in distributed, private learning.
Focusing on differentially private (DP) empirical risk minimization for convex and smooth functions, the authors analyze a private blind model averaging technique with provable utility.
Blind model averaging is a non-interactive technique where each user only sends a single message, and a minimal amount of communication is therefore used.
The paper provides bounds and empirical results for SVMs and softmax regressions.
Supported by their theoretical findings, the authors observe that blindly averaged softmax regression outperforms blindly averaged SVMs when dealing with a large number of classes, while blindly averaged SVMs outperform gradient averaging (such as federated learning) when dealing with a large number of users.
The authors therefore conclude that, under their assumptions, blind model averaging can provide a good privacy-utility trade-off.

### Strengths
The paper tackles a relevant problem, as distributed learning is essential in privacy-preserving ML.
The overall separation of the paper's content and structure in two "phases", that is, the individual training and the averaging in the models, is conveniently presented and helps readability.
The proof of differential privacy for softmax aggregation trained with SGD follows from the proof that the objective function is strongly convex, smooth, and Lipschitz.
While details were not checked, the derivation seems sound and convincing.
The experimental evaluation supports the theoretical findings and is reasonably extensive.
I think this is overall a good manuscript which, if improved in presentation/form (see weaknesses), can be a very well rounded contribution .

### Weaknesses
 **Structure**

While the derivation of the results is quite streamlined, the many aspects of the organization of the paper should be improved.
Specifically, the introduction presents the overview of the method using symbols which have not been defined yet. While I understand the usefulness of describing the approach early on, I feel like this may be confusing. For instance, the use of \(\Lambda\), \(\beta\), and \(L\) without prior definition makes it difficult to follow the initial presentation of the method. On a similar note, the "main result" is presented in Figure 2, in the introduction. Similarly, a summary of the comparison of the proposed approach against related work is part of Section 2 (related work). In this case as well, I feel like moving the discussion of results to the experiments section would benefit readability. I think that moving the related work section to the bottom of the manuscript could also be a possibility. The subdivision of the work in several named paragraphs (that is, paragraphs which begin with bold text) does not help readability, in my opinion. Maybe using subsections for this could help to visually and conceptually separate the different parts of the contribution. Bold text is also used in figures where, I feel, it is not necessary to highlight several lines of text.


**Presentation of empirical results**

Following up on my previous comment, empirical results are difficult to parse. Firstly, the plots are very small with very tiny labels, across the whole manuscript. Secondly, the experimental results section discusses 4 research questions which have, however, not clearly been introduced before. The lack of a clear connection between the research questions and the experimental setup makes it hard to understand the motivation behind each experiment.


**Imprecise language**

The terminology used is at times imprecise (e.g., "spread" the dataset in line 103, of "perfectly converge" in line 481), or not introduced (e.g., "local DP" and "group privacy" are never introduced as concepts). Local DP and group privacy should, in my opinion, definitely be at least informally introduced in the main body. The results in figure 6 are, in this sense, pretty much impossible to parse by referencing the main text only. In fact (see for instance Section 6), the concepts "local DP" and "privacy with local aggregator" are not compatible but can be easily confused. The paper needs to clarify the distinction between these concepts, as they are used in different contexts and have different implications for privacy.


**Limitations and discussion**

I think the limitations and discussion section should be improved. While I understand that page limits may be tricky, I feel like the limitations of the contribution are unclear from the main body of the text and at least a few lines should be dedicated to it. A more thorough discussion should also mention possibile improvements and future work directions.



**Minor points**

* line 27 "we also conclude the first" -> "we also derive", maybe?
* line 146 (and others) "noised" -> "noisy"
* lines 74 and 81, are "phase I" and "phase II" inverted?

### Questions
* Can you make the connection between group-DP and local DP clearer (i.e., expand on the discussion for figure 6)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes and analyzes a privacy-preserving model averaging technique based on output perturbation. Privacy guarantees are established for Support Vector Machines and Softmax Regression. Empirical results are also presented.

### Strengths
The proposed method requires only one round of model aggregation, due to the use of output perturbation. The privacy analysis is provided and seems to be correct.

### Weaknesses
(1) The proposed method has limited applicability. For complex models, the sensitivity of model parameters is often unbounded, making it difficult to apply output perturbation effectively. Specifically, the reliance on strong convexity and bounded sensitivity severely restricts the types of models that can be used, excluding many deep learning architectures where these properties do not hold. This limitation significantly reduces the practical relevance of the proposed method.

(2) The advantages of using output perturbation over other private optimization techniques, such as DP-SGD or objective perturbation, for optimizing local models are not clear to me. While the paper emphasizes reduced communication, it does not adequately address the potential trade-offs in terms of utility. Specifically, it is unclear whether the output perturbation approach can achieve comparable accuracy to other methods, such as DP-SGD, which directly perturb the gradients and might offer better convergence properties. The paper lacks a detailed analysis of the utility-privacy trade-offs compared to these alternatives.

(3) Finally, the paper's organization and notation are somewhat disorganized.
> For instance
> - 1. In the Contributions section, the order of Phase 1 and Phase 2 is reversed.
> - 2. Some notations are unclear. For example, on line 343, the meaning of "_" is ambiguous. Additionally, the definition of the inner product between functions on line 330 should be formally stated.
> - 3. Definition D.8 is not well-articulated
> - 4. What is the meaning of ADP in Lemma K.6?

### Questions
(1) If the primary contribution is reducing communication time, could the authors elaborate on the rationale for using output perturbation to privately train local models? How does output perturbation compare to other methods, such as objective perturbation or NoisySGD, for training local models?

(2) Can the proposed method be applied to a broader range of models, beyond SVMs and Softmax classifiers?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a method called Blind Model Averaging (BlindAvg) to improve the scalability and privacy of distributed machine learning, particularly for differentially private settings. Unlike traditional gradient-averaging methods, BlindAvg allows each client to train a model independently and submit it for secure averaging without any online synchronization. This approach is shown to work effectively for convex, smooth empirical risk minimization (ERM) tasks like Support Vector Machines (SVM) and Softmax regression.

### Strengths
Scalability and Efficiency: By proposing a non-interactive learning framework, the paper addresses the high communication and synchronization costs that typically come with FL. 

Enhanced Privacy Guarantees: The BlindAvg approach integrates DP at both the data point and user levels,

### Weaknesses
1) Limited Applicability to Non-Convex Models: The theoretical convergence guarantees provided in the paper apply primarily to convex models like SVMs and smooth ERM-based models. The lack of results for non-convex models, such as deep neural networks, severely restricts BlindAvg’s applicability in modern machine learning. While the authors mention pre-training, the core method lacks theoretical justification for non-convex scenarios, which is a significant limitation given the prevalence of deep learning in practical applications. The absence of any analysis or empirical validation on non-convex models leaves a substantial gap in the paper's contribution.

2) **Fatal Presentation Problem**: The paper suffers from a significant presentation issue, as numerous variables are introduced and used without clear, standalone definitions, which considerably hinders readability. For example, variables such as $d$ (dimensionality of the input) and $c$ (input clipping bound) in line #240 are used without clear definitions, making it challenging to understand their roles in the algorithms and theoretical analysis. Beyond these examples, many other variables/names/functions/algorithms lack clarity, compounding the difficulty. This lack of clarity in variable presentation is one of the worst I’ve encountered, severely impacting the paper’s accessibility.

Presentation:
1) You should define all variables before use in your algorithm. Variable $x$ was not defined in algorithm 1. You only define $D={(x_j, y_j)}$ in the algorithm 1. If you want to loop through every $x_j$, you must specify the loop in the algorithm. Otherwise, it is ambiguous and unclear.
2) Algorithm 2. "run the client code of secure summation..." and "Run the server protocol of $\pi$" are unclear illustrations. I can see your illustration in #378-#381 and appendix D.5. However, who sent what information to whom? Who did what calculation on which variables? e.g. you can write $F(n^(i)/w\cdot f_{priv}_1, n^(i)/w\cdot f_{priv}_1)$ for secure summation. and "send $f$ to server", "receive $f$ from client". Even though you want to hide the detail of secure summation in the appendix, a certain level of abstraction should be provided in the algorithm, instead of a plain unclear illustration.
3) Figure 5. why there is "?" after "distributed"? I can only recognize it as a typo. Please use clear expressions in the figure, instead of indication. Besides, in this figure your global model and SVM-SGD both use a black solid line, which is confusing. Please be professional.

Minor:
1) Gauss mechanism -> **Gaussian** mechanism.
2) #224, for m **in** 1...M.

### Questions
N/A

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This papers addresses the problem of privacy protection in blind model averaging for convex and smooth empirical risk minimization. The performance of blind model averaging is discussed in problems of SVM and Softmax regression. The privacy approach is differential privacy.

### Strengths
The discussed problem of privacy protection is interesting and important.

### Weaknesses
1. The results are limited to convex and smooth objective functions. Given that many machine learning problems are essentially nonconvex and nonsmooth, it would be important to relax this assumption. Specifically, the reliance on strong convexity and Lipschitz smoothness is a significant limitation, as these properties are rarely satisfied in practice, particularly with complex models. The analysis should consider how the proposed approach would behave under weaker assumptions, such as local convexity or weaker smoothness conditions.

2. The applicability of the approach also seems limited. The paper only discusses SVM and Softmax regression applications. It will be interesting to know if the approach also applies to other applications, particularly deep learning applications. The current analysis lacks a clear explanation of how the proposed method could be extended to more complex models, such as neural networks with multiple layers and non-linear activation functions. The practical utility of the method is therefore questionable without such extensions.

3. The design of differential privacy seems straightforward. It is unclear if there are any challenges. The paper does not adequately address the challenges in achieving differential privacy in the context of blind model averaging. The sensitivity analysis, which is crucial for differential privacy, seems to be treated as a routine step, without discussing potential difficulties or limitations in its application to the specific problem.

### Questions
see above.

### Soundness
2

### Presentation
2

### Contribution
2

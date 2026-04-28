# Generalized Temporal Difference Learning Models for Supervised Learning

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 3, 8

## Abstract
In conventional statistical learning settings, data points are typically assumed to be independently and identically distributed (i.i.d.) according to some unknown probability distribution. Various supervised learning algorithms, such as generalized linear models, are derived by making different assumptions about the conditional distribution of the response variable given the independent variables. In this paper, we propose an alternative formulation in which data points in a typical supervised learning dataset are treated as interconnected, and we model the data sampling process by a Markov reward process. Accordingly, we view the original supervised learning problem as a classic on-policy policy evaluation problem in reinforcement learning, and introduce a generalized temporal difference (TD) learning algorithm to address it. Theoretically, we establish the convergence of our generalized TD algorithms under linear function approximation. We then explore the relationship between TD's solution and the original linear regression solution. This connection suggests that the probability transition matrix does not significantly impact optimal solutions in practice and hence can be easy to design. In our empirical evaluations, we examine critical designs of our generalized TD algorithm, and demonstrate the competitive generalization performance across a variety of benchmark datasets, including regression, binary classification, and image classification within a deep learning context.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the traditional statistical learning setting, data is assumed to be independently and identically distributed (i.i.d.) according to some unknown probability distribution. Supervised algorithms such as generalized linear models are constructed by making assumptions about the distribution of the response variable given the independent variables. The authors propose an assumption where the data is interconnected and the sampling process is a Markov reward process. This turns the supervised learning problem into an on-policy evaluation problem in reinforcement learning, which the authors address by utilizing a generalized temporal difference (TD)
learning algorithm. They theoretically prove the convergence of these algorithms under linear function approximation and explore the relationship between the generalized TD solution and the original linear regression solution. Through their experiments, they compare the generalized TD algorithm with other baseline models in regression, binary classification, and image classification tasks.

### Strengths
I appreciate that the authors provided clear background information on supervised learning and temporal difference learning before outlining the theoretical proofs. I also appreciate that the authors also provided limitations of their work within the main text.

### Weaknesses
I believe the authors could have provided a few more datasets for the regression problem and the binary classification class imbalance problem.

### Questions
N/A

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
This paper generalizes the temporal difference (TD) learning models for supervised learning with dataset treated as interconnected. To this end, this paper introduces a generalized TD learning algorithm and establishes theoretical convergence guarantees under both expected update and sample-based update. In addition, this paper also conducts experiments, which shows the generalization performance of the TD learning algorithm.

### Strengths
1. This paper proposes a new generalized TD learning algorithm and establishes theoretical convergence guarantees.

2. This paper conducts experiments which shows the generalization performance of the TD learning algorithm.

### Weaknesses
1. Assumption 2 seems to be a little strong to require $f$ is invertible. In addition, how will this assumption be when the logit $z$ is a vector? For example, when $f$ is a softmax function?

2. The algorithm 1 requires the knowledgement of transition $P$, which seems not realistic.

Minors:

In assumption 1, $D(s)$ comes without definitions and explanation.

3. The proof for Lemma 1 is not clear. The argument that continuous functions are Lipschitz continuous on bounded sets is incorrect. For example, $\sqrt{x}$ over $[0,1]$ is continuous but not Lipschitz continuous. This requires a stronger assumption and justification.

### Questions
1. I wonder how is lemma 1 derived? I think lemma 1 requires that the function $f$ is $L$-Lipschitz continuous. It seems that this can not be implied by assumption 1 and 2. 

2. I want to understand whether the transition kernel $P$ will influence the theoretical results. I do not find any term related to $P$ in theorems.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper applies reinforcement learning to solve conventional regression/supervised learning problems. In particular, the author(s) focused on classical generalized linear models and reformulated the parameter estimation with a reinforcement learning (RL) framework. This allows to apply the classical on-policy evaluation algorithm in RL to solve supervised learning. In theory, the author(s) established the convergence properties of the estimated parameters. Empirically, they further extended their methodology to deep learning.

### Strengths
As far as I can see, the strengths of the paper can be summarized as follows:

**Originality**: The idea to apply RL to solve supervised learning is relatively less explored in the literature. As the author(s) commented in the paper, existing algorithms are particularly designed for specific types of problems. To my knowledge, similar ideas have not been proposed in the literature. 

**Quality**: Compared to the existing RL algorithms to solve supervised learning problems, the solution the author(s) proposed is general and is applicable to a wide range of regression problems covering parameter estimation in both classical generalized linear models and deep learning. 

**Clarity**: The paper is easy to follow. The writing is generally clear.

### Weaknesses
In my assessment, the primary limitation of this paper stems from the effectiveness of the proposed method. From my interpretation, the recommended RL algorithm appears to be less efficient than traditional supervised learning algorithms, particularly from a theoretical standpoint. This issue considerably constrains the practicality of the presented methodology, and I will provide a comprehensive explanation below.

Let's initiate the discussion with the ordinary least square (OLS) regression problem, which is introduced at the onset of Section 3. The conventional OLS method calculates the following estimator $\widehat{\omega}_{\textrm{SL}}$ for $\omega^*$, the oracle value in the linear model,  

$$\widehat{\omega}_{\textrm{SL}}=(\sum_i x_i x_i^\top)^{-1} (\sum_i x_i y_i).$$

The mean squared error (MSE) of this estimator can be shown to be equivalent to

$$n\textrm{MSE}(\widehat{\omega}_{\textrm{SL}})=\sigma^2 \textrm{trace}(\Sigma^{-1}),$$

where $n$ denotes the sample size, $\Sigma= \mathbb{E} x_i x_i^\top$ and $\sigma^2$ denote the error variance $\mathbb{E} (y_i-x_i^\top \omega^*)^2$. It is widely recognized that the OLS estimator is the Best Linear Unbiased Estimator (BLUE), minimizing the MSE among all unbiased estimators. 

Moving on to the RL estimator, as depicted in Equation (4), the resulting estimator $\widehat{\omega}_{\textrm{RL}}$ can be expressed as

$$\Big[\sum_i x_i (x_i-\gamma x_{i+1})^\top\Big]^{-1} \Big[\sum_i x_i (y_i - \gamma y_{i+1})\Big].$$

Assuming both $x_i$ and $y_i$ are of mean zero, its MSE can be shown to equal to

$$n\textrm{MSE}(\widehat{\omega}_{\textrm{RL}})=(1+\gamma^2)\sigma^2 \textrm{trace}(\Sigma),$$

which is strictly larger than the SL-based estimator as long as $\gamma>0$. Additionally, the larger the discounted factor $\gamma$, the larger the MSE. This observation demonstrates that when tailored to linear models, the RL-based estimator exhibits statistical inefficiency in comparison to the SL-based estimator, particularly from a theoretical standpoint. A thorough examination of the closed-form expression for the RL estimator​ sheds light on the root cause of this inefficiency. In the RL estimator, the target variable encompasses both the current outcome $y_i$ (which embeds the true signal) and the future outcome $y_{i+1}$. It is crucial to note that the latter is independent of 
$x_i$ and can be perceived as an additional source of error. By adopting the RL framework, we inadvertently introduce extra noise to the outcome, ultimately compromising the efficiency of the resulting estimator.

Further considering the more extensive Generalized Linear Model (GLM), it is established that the SL-based estimator, when computed via Newton-type algorithms such as Fisher scoring, achieves efficiency, attaining the Cramer-Rao (CR) lower bound. I suspect that similar disparities are present in Generalized Linear Models (GMLs), where the RL-based estimator may not reach the CR lower bound, exhibiting reduced efficiency, due to the additional noise introduced in the target variable.

It is crucial to note that the above analysis predominantly pertains to estimators derived through Newton-type algorithms. When gradient-type algorithms are employed in conjunction with the Polyak-Ruppert averaging scheme, the resulting estimators exhibit the same asymptotic distributions as those computed via Newton's method. This leads us to the same conclusion.

### Questions
Please refer to the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors describe how to model the data sampling/generation
process, in a supervised learning framework, as a Markov reward
process. This contrasts with the established i.i.d. data assumption
used in most classifiers.
The authors consider that the data points are originated from a Markov
reward process, where the policy is fixed and the goal is to perform a
policy evaluation.
They introduce a generalized temporal-difference (TD) algorithm for this.

They proposed a mapping between the training features (X) and the
states in RL, and between the target variable (y) and the state value
function. Under this framework, the reward function can be estimated
from the differences between the output variables from successive times.
They show that under a TD framework, the updating rule can bootstrap
with the output variable of the next time.

They also provide a generalization to different types of data
by incorporating logits. They provide convergence proofs and several
empirical studies showing different aspects of the proposed approach.

### Strengths
- Relate two different learning paradigms 
- Proposes a theoretical framework
- Present several theoretical results

### Weaknesses
 - The paper is not easy to read

### Questions
The proposed approach seems only applicable to supervised
learning. How could it be extended to unsupervised learning where the
is not a clear target output.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

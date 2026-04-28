# Towards the Fundamental Limits of Knowledge Transfer over Finite Domains

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We characterize the statistical efficiency of knowledge transfer through $n$ samples from a teacher to a probabilistic student classifier with input space $\cS$ over labels $\cA$. We show that privileged information at three progressive levels accelerates the transfer. At the first level, only samples with hard labels are known, via which the maximum likelihood estimator attains the minimax rate $\sqrt{\nicefrac{|{\cS}||{\cA}|}{n}}$. The second level has the teacher probabilities of sampled labels available in addition, which turns out to boost the convergence rate lower bound to ${\nicefrac{|{\cS}||{\cA}|}{n}}$. However, under this second data acquisition protocol, minimizing a naive adaptation of the cross-entropy loss results in an asymptotically biased student. We overcome this limitation and achieve the fundamental limit by using a novel empirical variant of the squared error logit loss. The third level further equips the student with the soft labels (complete logits) on ${\cA}$ given every sampled input, thereby provably enables the student to enjoy a rate $\nicefrac{|{\cS}|}{n}$ free of $|{\cA}|$. We find any Kullback-Leibler divergence minimizer to be optimal in the last case. Numerical simulations distinguish the four learners and corroborate our theory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide minimax rates for transfer learning, expressed as the total variation between between a learner and a reference policy or a ground truth distribution, for different levels of knowledge shared with the learner and losses such as cross entropy and squared loss. They also present simulations to demonstrate the performance of their results in the various transfer settings.

### Strengths
* Their work explores various ways of sharing knowledge and allows for flexibility on how teachers can assist learners.
* Their theoretical results show that learners might not require too much data. Since their results are for commonly used losses in practice, this can be helpful in engineering other ways of knowledge sharing.

### Weaknesses
For someone who is not familiar with the literature in this field, many notations lack proper definitions or sufficient rigor. For example, there is no clear definition provided for "privileged information," and it would be beneficial for completeness to include such definitions. The technical aspects of their three settings are not distinctly emphasized. Many variables, such as $CE_{sgl}$ or $CE_{ful}$, are referenced without prior definitions. Furthermore, $\Delta(\mathcal{A} \vert \mathcal{S})$ is mentioned without an initial definition, and it's only later clarified that $\Delta(\mathcal{A})$ represents a simplex. 

It took multiple reads to understand the impact of their main contribution. This paper might need several revisions because as it stands, it is not easily understandable.

### Questions
It would be helpful to have more specific explanation for the settings of transfer using Partially Soft Labels and Soft Labels in sections 3 and 4. It looks like $\mathcal{D}$ is already generated using $(\rho \times \pi^\star)^n$. It is not clear what additional information is provided with $\pi^\star(a_i\vert s_i)$ in the case of partially soft labels.

### Soundness
2 fair

### Presentation
2 fair

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
This paper considers the problem of knowledge transfer through empirical samples from a teacher to a student. They characterize sample complexity for three different settings. The first setting is hard labels, where the student knows (input, label) samples from the teacher, the second setting is when the student knows (input, label, prob(label|input)) samples, and in the third setting, the student knows (input, label, prob(.|input)). The paper characterizes the lower bound and matching upper bounds in each of the settings, showing the statistical roles of extra information present to the student.

### Strengths
- Neat results and message

### Weaknesses
 - The tabular setting is quite basic which does not capture many practical settings when the state space is large.

### Questions
* How can these guarantees generalize to more practical settings where the state space is large? (speculation is fine)

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper attempts to create a mathematical model for a simplified version of "knowledge transfer" from a teacher to a student within the context of multi-class learning. Notably, the authors make two key assumptions: that both 1) $\mathcal{S}$ (representing the space of all possible queries a student can pose to a teacher) and 2) $\mathcal{A}$ (denoting the space of all possible answers provided by the teacher) are finite.

In mathematical terms, for each query $s\in\mathcal{S}$, let $\pi^*(\cdot\vert s)$ represent the (optimal) teacher policy, or the conditional distribution of labels for the query $s$. The student's goal is to learn $\hat{\pi}$, a finite distribution with the same complexity as $\pi^*$, using only $n$ i.i.d. queries (and answers) from the teacher, represented by the set $\\{(a_i,s_i)\\}$ for $i\in[n]$.

In this context, the authors aim to establish minimax bounds for $\mathbb{E}_{s\sim\rho}\left[\mathsf{TV}\left(\hat{\pi},\pi^*\vert\rho\right)\right]$, which measures the "$\rho$-expected total variation distance" between the teacher and student's policies. Here, $\rho$ signifies the distribution that generates queries across $\mathcal{S}$. The paper successfully derives minimax rates for this problem under three different scenarios: i) when only hard labels are provided, ii) in cases where, in addition to labels, the probability of the label from $\pi^*$ is also given, and iii) when all class probabilities are given for each query.

The paper is well-written, and it meticulously references pertinent prior research (as far as I can tell). The mathematical derivations appear sound, with no conspicuous errors. Moreover, there are several experiments, though I haven't examined them closely. Overall, this is a commendable theoretical contribution. However, I believe that the assumption of finiteness for both the "query" and "answer" spaces oversimplifies the problem, leading to bounds that might not be as intriguing as one might hope (please refer to the weaknesses section for further clarification).

My vote is a weak accept.

### Strengths
- The paper is very well-written. In particular, the "Prior Works" section stands out as highly informative.

- The problem formulation and motivations, especially the connections to Large Language Models (LLMs) and other foundational models, are immensely intriguing.

- The theoretical framework developed in this work appears robust and sufficiently rigorous for a theory paper at ICLR. I scrutinized some of the proofs and did not find any significant errors. Furthermore, the other results seem mathematically sound.

- The problem is analyzed under three distinct regimes, with the gradual introduction of additional side information to the original dataset. This approach allows the reader to observe, in a step-by-step manner, the mathematical impact of incorporating each layer of side information.

- The paper also includes some experimental validations, although I did not review them in detail.

### Weaknesses
I suppose that the assumptions regarding the finiteness of both $\mathcal{S}$ and $\mathcal{A}$ may have oversimplified the problem. Here is my interpretation of Theorems 3.1 and 3.2 (please correct me if I am mistaken):

- In essence, the paper aims to "learn" a distribution of dimension ($\vert\mathcal{S}\vert\times\vert\mathcal{A}\vert$), denoted as $\rho\times\pi^*$. By "learn," I mean the process of minimizing a specific expected total variation (TV) distance, as mentioned earlier. Let me introduce the notation $F = \vert\mathcal{S}\vert\times\vert\mathcal{A}\vert$. It is already established that having approximately $\tilde{O}(F)$ (where $\tilde{O}$ hides polylogarithmic factors) samples, denoted as $n$, is sufficient to capture almost all the probability mass within $\mathcal{S} \times \mathcal{A}$ according to the distributions $\rho$ and $\pi^*$. This can be directly derived from the coupon collector theorem. Consequently, in the worst-case scenario where both $\rho$ and $\pi^*$ are not sparse, we typically have, on average, $\tilde{O}(n/F)$ samples for each query-answer pair $(a, s)$. Consequently, the overall distribution $\rho \times \pi^*$, as well as any of its derivatives (such as the aforementioned "expected TV distance," which is the primary focus of this paper), can be approximated with an error of at most $\tilde{O}(\sqrt{F/n})$, as a direct consequence of general inequalities like Hoeffding. While this intuition provides a basic understanding of the scaling behavior, the core issue lies in the fact that the derived bounds are largely governed by the cardinalities of $\mathcal{S}$ and $\mathcal{A}$. This suggests that the analysis might not fully capture the intricacies of the learning dynamics, especially when considering more complex structures for $\mathcal{S}$ and $\mathcal{A}$.

- The bounds pertaining to other scenarios discussed in the paper can also be derived using mathematical methods similar to the ones mentioned above.

Nonetheless, I commend the authors for their precise determination of minimax rates and their detailed analysis of individual cases. It would, however, be more intriguing if the paper explored more intricate scenarios for $\mathcal{S}$ and $\mathcal{A}$. For example, one would naturally expect other (and more interesting) notions of complexity (such as VC-dimension, etc.) of distribution families $\rho$ and $\pi^*$ to show up in bounds, instead of the mere cardinality of query-answer spaces. The current analysis, while rigorous, seems to treat the problem as fundamentally tabular, potentially overlooking the nuances that would arise in more structured settings.

### Questions
Pleae see "Weaknesses" section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider the problem of knowledge transfer between a teacher (e.g., LLMs) and a student classifier (given limited privileged information). They show the fundamental limit of the transfer under three regimes: 
1. only input-label pairs are observed. The optimal rate is $\sqrt{\frac{|S||A|}{n}}$, achieved by MLE.
2. teacher probabilities of sampled labels are also available, then the optimal rate is $\frac{|S||A|}{n}$, achieved by empirical SEL loss
3. complete logits are also given, then the optimal rate is $\frac{|S|}{n}$, achieved by KL divergence minimization
Numerical simulations are also provided.

### Strengths
quality: high, provide thorough investigation under three regimes, including matching upper and lower bounds.
clarity: good, the setting is easy to under stand, and the structure of the paper is clear

### Weaknesses
The setting of "knowledge transfer" seems to be fancy. But according to the definition, the teacher distribution is considered as "ground truth" that is already given, thus the "hard labels" regime seems to fall in the common statistical learning framework. I am not sure whether tabular settings under usual statistical learning framework have been studied. Specifically, the hard label setting appears to be a standard conditional density estimation problem, where the goal is to estimate the conditional distribution \(\pi^{\star}(a|s)\) from samples \((s_i, a_i)\). The framing as "knowledge transfer" feels somewhat artificial, as the teacher is not a learned model but rather the true underlying distribution. The work does not clearly articulate how this differs from standard statistical learning problems beyond the framing of transferring knowledge from a known distribution, which is not the typical knowledge transfer scenario.

The results are fully tabular, limiting the practical applicability of the theoretical findings. While the analysis provides precise rates for the tabular case, it is unclear how these results translate to more realistic scenarios with high-dimensional or continuous input spaces. The paper lacks a discussion on the potential challenges and modifications needed to extend these results beyond the tabular setting. For instance, the optimal rates derived for the tabular case may not hold when dealing with function approximation or non-parametric models. The paper should address the limitations of the tabular analysis and discuss potential avenues for generalization.

### Questions
1. What is the main difference between your setting and the usual statistical learning setting? For example, if I change your notation in the following way: "input" $s$ change to "feature" $x$, label $a$ change to $y$, then your setting (hard labels) seems to be completely the same as the usual setting of observing data $\\{(x_i,y_i)\\}\_{i=1}^{n}$, and the goal is to predict $y$ from $x$. It seems that there is not "knowledge transfer" (unless you call the usual machine learning "knowledge transfer from ground truth").

2. The results is fully tabular. Can you generalize your results to continuous case?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

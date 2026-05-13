# Provable Privacy Attacks on Trained Shallow Neural Networks

- Decision: Reject
- Scores: 6, 8, 5, 5

## Abstract
We study what provable privacy attacks can be shown on trained, 2-layer ReLU neural networks. We explore two types of attacks; data reconstruction attacks, and membership inference attacks. We prove that theoretical results on the implicit bias of 2-layer neural networks can be used to provably reconstruct a set of which at least a constant fraction are training points in a univariate setting, and can also be used to identify with high probability whether a given point was used in the training set in a high dimensional setting. To the best of our knowledge, our work is the first to show provable vulnerabilities in this setting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper tries to show provable guarantees for data reconstruction and membership inference for nonconvex activation functions in shallow Neural networks.

### Strengths
The overall question is interesting and would certainly be of interest to the community at large. The main contribution of this paper is to show there is _some_ theoretical basis for the literature on data reconstruction and membership inference attacks. However, the results in this paper are somewhat lacklustre for reasons outlined in the next two sections.

### Weaknesses
The paper is lacking in the areas of exposition and technical details. Concepts which are central to the paper such as Gradient flow, Data Reconstruction, and Membership Inference are never formally defined, which makes the paper inaccessible to all but a very niche audience.

I have listed a set of points in the next section for the authors to clarify. In the interest of transparency, I am clearly stating my position here:
  - The paper needs more work especially in exposition (see above). At this time it reads like a first draft. For example, the assumptions and the proofs are tightly coupled with each other, without a clear basis for either. Simply based on this issue, I am recommending rejection for the paper.
  - I am open to changing my score in case I have misunderstood something regarding the assumptions. However, I again stress that such clarifications should have been in the paper to begin with, and it will probably not improve my score by a lot.

*Remark*: Judging by the previous works of Haim et al. (2023) etc. it seems to be that it is indeed possible to reconstruct data or perform MI in the settings considered. I believe that the paper stands to benefit a lot if the focus of the theoretical setting would have been to investigate the precise nature of the assumptions that allowed these attacks to take place.

1. Theorem 2.1 specifically mentions that the gradient flow in a homogenous ReLU NN _eventually converges_  (i.e., at $t\to\infty$) to a stationary point.
  - Line 146: What does gradient flow over a binary classification set formally mean?
  - Line 154: I invite the authors to explain why it is natural to assume that the existence of a point of convergence automatically implies that the function has converged. It might be a fine assumption for experimentally focused papers, but assuming convergence in a theoretical setting needs to be well motivated.
  - Does the above issue not mean that Assumption 2.1 is an extremely strong condition for a 2-layer NN?

2. I think that the proof of Theorem 3.1 is incorrect (or at the very least missing certain assertions).
  - it is stated that the real-valued function $\phi(\theta; x_1)$ cannot be the zero function because for all $i\in[n]$, $y_i\phi(\theta;x_i)\geq m$, where $m:=\min_i|{\phi(\theta;x_i)}|$, and therefore can well be $0$. The authors are therefore assuming another implicit condition, i.e., the margin should always be positive. This makes Assumption 2.1 even more untenable for 2-layer NNs in the context of Theorem 2.1.
  - Suppose $\phi(\theta; x_1)>0$. Since $\phi$ is a real-valued function, I am not understanding why $y_1\Phi(\theta;x_1)$ cannot lie in between 0 and 1. Hence the rest of the implications in the proof do not follow.
   - The crux of Assumption 2.1 should be clearly stated in the abstract of the paper and the introduction of the paper in some form.
As it stands, I am not convinced that even in the univariate case, the data can be recovered.

3. In Line 309, the authors state: "In very high dimensional settings, under many commonly used data distributions, we have that the dataset is almost orthogonal with high probability." This forms the basis for Assumption 4.1, which is critical to the rest of the proofs. This is the first time the authors have mentioned the ability to perform membership inference or data reconstruction w.r.t. well-behaved distributions. This is highly unusual and subtracts from the blackbox nature of membership inference or data reconstruction attacks.
   - For Assumption 4.1 to be considered _valid_, I would prefer if the authors included a discussion addressing the above concern.
   - The crux of Assumption 4.1 should be clearly stated in the abstract of the paper and the introduction of the paper in some form.

4. Most of the main theorems are missing a high level overview from the main paper. The authors should include a proof sketch of Theorems 3.2 and 3.3.

5. Line 474: I invite the authors to clarify the following statement - "in this section, we conducted a few experiments focusing on the membership inference problem, and observed that while our theoretical results’ assumptions do not necessarily hold, their implications are nevertheless still valid." Does this not mean that weaker assumptions would have sufficed?


## Typos and Grammatical mistakes
Line 231: "be two adjacent intervals which none of them is constant on the margin" - the authors should rewrite this sentence.

### Questions
1. Theorem 2.1 specifically mentions that the gradient flow in a homogenous ReLU NN _eventually converges_  (i.e., at $t\to\infty$) to a stationary point. 
  - Line 146: What does gradient flow over a binary classification set formally mean?
  - Line 154: I invite the authors to explain why it is natural to assume that the existence of a point of convergence automatically implies that the function has converged. It might be a fine assumption for experimentally focused papers, but assuming convergence in a theoretical setting needs to be well motivated.
  - Does the above issue not mean that Assumption 2.1 is an extremely strong condition for a 2-layer NN? 

2. I think that the proof of Theorem 3.1 is incorrect (or at the very least missing certain assertions).
  - it is stated that the real-valued function $\phi(\theta; x_1)$ cannot be the zero function because for all $i\in[n]$, $y_i\phi(\theta;x_i)\geq m$, where $m:=\min_i|{\phi(\theta;x_i)}|$, and therefore can well be $0$. The authors are therefore assuming another implicit condition, i.e., the margin should always be positive. This makes Assumption 2.1 even more untenable for 2-layer NNs in the context of Theorem 2.1.
  - Suppose $\phi(\theta; x_1)>0$. Since $\phi$ is a real-valued function, I am not understanding why $y_1\Phi(\theta;x_1)$ cannot lie in between 0 and 1. Hence the rest of the implications in the proof do not follow.
   - The crux of Assumption 2.1 should be clearly stated in the abstract of the paper and the introduction of the paper in some form.
As it stands, I am not convinced that even in the univariate case, the data can be recovered.

3. In Line 309, the authors state: "In very high dimensional settings, under many commonly used data distributions, we have that the dataset is almost orthogonal with high probability." This forms the basis for Assumption 4.1, which is critical to the rest of the proofs. This is the first time the authors have mentioned the ability to perform membership inference or data reconstruction w.r.t. well-behaved distributions. This is highly unusual and subtracts from the blackbox nature of membership inference or data reconstruction attacks. 
   - For Assumption 4.1 to be considered _valid_, I would prefer if the authors included a discussion addressing the above concern.
   - The crux of Assumption 4.1 should be clearly stated in the abstract of the paper and the introduction of the paper in some form.

4. Most of the main theorems are missing a high level overview from the main paper. The authors should include a proof sketch of Theorems 3.2 and 3.3.

5. Line 474: I invite the authors to clarify the following statement - "in this section, we conducted a few experiments focusing on the membership inference problem, and observed that while our theoretical results’ assumptions do not necessarily hold, their implications are nevertheless still valid." Does this not mean that weaker assumptions would have sufficed? 


## Typos and Grammatical mistakes
Line 231: "be two adjacent intervals which none of them is constant on the margin" - the authors should rewrite this sentence.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper describes how 2-layer neural networks have provably effective privacy attacks. The reconstruction attack they instantiate assumes complete optimization to the implicit bias solution and then analyzes the implication of the KKT conditions in cases to deduce high probability sets of training datapoints. Notably this algorithm does not require any further assumptions on the dataset, and hence presents a strong attack. The membership inference attacks impose certain restrictions on the data generating distribution, which I will summarize as “being sufficiently spread out in direction and magnitude” (i.e., orthogonal with high probability, and high magnitude relative to dimension), and is the case for common distributions. All together, these are (to the best of my knowledge) the first results on general privacy attacks against deep neural networks, and I believe also presents questions for future empirical and theoretical study.

### Strengths
1) As far as I am aware, the first general results of effective privacy attacks on neural networks, as opposed to empirical results known for specific datasets and models.
2) Surfacing assumptions required, which future work can weaken; the paper already discusses how the dimensionality assumptions may be weakened (given empirical evidence).
3) I believe the techniques in the proofs for the attacks to be novel to the private ML community

### Weaknesses
1) I think the presentation could make it more explicit what the contributions of the theory is to the broader privacy community. I attribute this mainly to the use of vague language regarding the assumptions in the main text, such as in line 45 which states “certain settings with varying assumptions”. One could instead highlight specific assumptions (e.g., the requirement for complete optimization to the implicit bias solution for the reconstruction attack, or the dimensionality and data distribution assumptions for membership inference) and contrast them with what is already known empirically. For example, the reconstruction attack relies on a very strong assumption of convergence to the implicit bias solution, which is not always the case in practice, and this should be made more explicit. Similarly, the membership inference attack relies on assumptions about the data distribution, such as orthogonality and magnitude relative to the dimension, which are not always satisfied in real-world datasets, and this should be discussed more thoroughly.

2) On presentation, I had some questions for the proofs as presented, which I believe are resolvable but I list them below in the Questions section.

### Questions
1) In the proof of Theorem 4.2, in lines 117-118 it is not clear to me how this follows without a high probability statement. The theorem states that with probability $1- \tau$ you have the training points are on the margin, and I believe some high probability argument like Lemma B.3 is implicit in the statement (and would be great to state more explicitly in the proof for completeness).


2) Similarly, at the end of the proof of Theorem 4.2, I believe you mean the final equality occurs with probability $1- 2\tau$ not $1 - \tau$.


3) In the proof of Theorem 3.2 and the existence of $x_1$, it is not clear to me how it not existing would imply the break points were the same with the stated logic. Could we not have $w_{i-1}$ be positive and hence it is determined by the margin points after the breakpoint, but $w_{i}$ can be negative and hence determined by the margin point below its breakpoint (which by assumption would be $0$). In this way they are still different given that $x_2$ exists, which is necessary as there is at least one margin point? What seems to me to be the correct proof is now noting that the breakpoint for $i+1$ would be the same as either $i$ or $i-1$, leading to a contradiction and hence needing $x_1$ to exist.


4) In Line 143 I believe you mean to say “for the sake succinctness” not “completeness” as you are summarizing the statement?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the privacy attack on 2-layer Relu activated neural network. Under the assumption that the model converges to a point that satisfies the KKT condition, this paper shows 2 attacks: 1) for the univariate case, this paper is able to recover a part of the training samples from the weights; 2) when the number of training samples $n$ is much smaller than the dimension $d$ of the training data, the output of the neural network can serve as membership inference attack. Experiments show that even n is as large as d, the membership inference attack can still work empirically.

### Strengths
This paper studies an important problem of privacy in neural networks. Theoretical analysis are provided. Experiments are conducted to support the theoretical claims. Source codes are provided.

### Weaknesses
My biggest concern is that the novelty seems to be limited.
- It is well known [1] that overparameterized neural networks can memorize training input, and it is not surprising that the training input is encoded in the model weights in some way. Actually, empirical study has shown that it is possible to reconstruct training data from model weights [2] and even model updates [3]. From this perspective, the contribution of this work seems to be limited at providing a theoretical proof. However, the proposed attack only work for the univariate case, which means the neural network is essentially a piece-wise linear function. It is not clear how this work can inspire training data reconstruction for general functions. The theoretical analysis, while rigorous, is limited by the highly constrained setting of a univariate input, which significantly reduces the practical relevance of the findings. The attack's reliance on the KKT condition, while mathematically sound, may not hold in more realistic training scenarios where convergence to such a precise point is not guaranteed.
- For the membership inference attack, in the setting where $n \ll d$, we can think that the model is able to memorize the label ($\pm 1$)
for all the $n$ samples that are seen during training, but the model does not have any idea for the remaining input , which is at least a $d-n$-dimensional subspace. So it is expected that the model output can serve as an indicator for membership. The condition on $n,d$ and the assumption of almost orthogonal training data seem to be quite limited. It is not clear if the proposed theory can help understand the membership inference attack in general case, e.g. [4]. The assumption of almost orthogonal training data, while simplifying the analysis, is a strong constraint that limits the applicability of the results to real-world datasets, which rarely exhibit such orthogonality. The theoretical analysis for membership inference relies heavily on the assumption that the training data is significantly smaller than the input dimension ($n \ll d$), which is not representative of many practical scenarios where the number of training samples is comparable to or even larger than the input dimension. This raises concerns about the generalizability of the findings.

### Questions
- The curve in Figure 1 (a) is not very smooth. If you run multiple experiments and report the average, will it be better?
- Loss is a popular metric for membership inference attack. In general trained samples shall have smaller losses than test samples. Can you explain a bit more on the relationship between loss and margin?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper looks at the problem of data reconstruction, and especially at the setting empirically discussed in [1]. The goal of the paper is to theoretically prove that reconstruction attacks are provably possible in some settings. The paper looks at data reconstruction in the univariate case (samples are one-dimensional), and also discusses membership inference attacks in the multivariate setting. The paper concludes with some experimental evidence beyond the setting covered by the technical assumptions used in the section on the membership inference attacks.

[1] https://arxiv.org/abs/2206.07758

### Strengths
The topic of data reconstruction gained reasonable popularity recently, and it is true that its theoretical understanding is lacking behind its practice. A better theoretical control of the current recovery schemes can be beneficial for the fields of privacy and security and beyond. Thus, in my opinion, the research question addressed by this paper is well motivated.

The paper implicitely tackles deep questions on the implicit bias of gradient descent algorithms on classification tasks, as the ratio of training points lying on the margin as a function of the data dimensionality (see Fig. 1a), or the output of the model at test time (see Fig. 1bc), which can be associated to the generalization error of the model itself.

### Weaknesses
First, the paper remarks multiple times that this is the first step towards understanding theoretically reconstruction attacks. This is false [2, 3]. Notice that these works (and probably other works I am not aware of) consider a different setting than the one presented in this paper, but (at least) equally interesting. I invite the authors to rephrase their narrative (see, e.g., "first step" in line 32 and "all previous works are empirical" in line 61) and to tune down this side of the contribution. On a minor level, I would invite the authors to remark in introduction that the idea of using the implicit bias of gradient descent on ReLU networks to understand data recovery is not new (see second paragraph of the introduction), as it is the core motivating idea behind the main paper the authors refer to [1].

Another weakness, in my opinion, is the high number of strong and implicit assumptions. The paper implicitely uses Theorem 2.1 from previous work to define its Assumption 2.1. This theorem assumes the loss to be small at some time, which I believe is not necessarily true (maybe the data / number of parameters have to respect some other explicit assumption), and therefore hides in which exact settings Assumption 2.1 is reasonable to be made. Can the authors elaborate, maybe in light of the results obtained in previous work on Theorem 2.1?

Another quite strong assumption made in this work is the implicit upper-bound on the number of training samples deriving from Assumption 4.1 (which translates to $n \ll \sqrt d$ in the case of the sphere). I wonder if with this number of data, it might be impossible for the model to successfully learn the task, as the output of the model at test time will approach 0, justifying why the results in Section 4 work (see for example Corollary 4.3, where at test time the outputs are small with high probability). To verify this, it would be helpful if the authors could also plot the test accuracy of the trained model in Figure 1, which will most likely decrease with $d$ as well. If it turns out that the attack success is strongly related with the test error of the model, it would be an important point to raise during the discussion.

Regarding the univariate case, I would also say it is hard to tell the effective predictive power of the results for more realistic scenarios. This setting might be qualitatively very different from the high dimensional case, and it is also difficult to evaluate how strong is the assumption that the attacker has knowledge of the margin (see line 190). Besides, I found section 3.2 a bit hard to parse at first, and I see the same problem I raised above on the implicit assumptions: what does it mean that $\Phi(\theta, x)$ is a local minimum of Eq. (1)? In which space? Is this stronger than Assumption 2.1? As the authors do not seem to be lacking in space, I would recommend adding an additional Figure in this section, where the intuition behind their results is depicted as a plot (for example, a uniivariate plot of  $\Phi(\theta, x)$ and the corresponding intersections with the margin). On top of this, it would be very helpful a brief discussion on why the results are intuitively true (see, for example, Theorem 3.2, where the reasons behind thesis seem a bit obscure).

### Questions
I asked multiple questions in the weaknesses section. I am happy to reconsider my score during the discussion time.

### Soundness
2

### Presentation
2

### Contribution
2

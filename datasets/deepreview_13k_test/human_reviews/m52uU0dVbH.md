# Constructing Adversarial Examples for Vertical Federated Learning: Optimal Client Corruption through Multi-Armed Bandit

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
Vertical federated learning (VFL), where each participating client holds a subset of data features, has found numerous applications in finance, healthcare, and IoT systems. However, adversarial attacks, particularly through the injection of adversarial examples (AEs), pose serious challenges to the security of VFL models. In this paper, we investigate such vulnerabilities through developing a novel attack to disrupt the VFL inference process, under a practical scenario where the adversary is able to \emph{adaptively corrupt a subset of clients}. We formulate the problem of finding optimal attack strategies as an online optimization problem, which is decomposed into an inner problem of adversarial example generation (AEG) and an outer problem of corruption pattern selection (CPS). Specifically, we establish the equivalence between the formulated CPS problem and a multi-armed bandit (MAB) problem, and propose the Thompson sampling with Empirical maximum reward (E-TS) algorithm for the adversary to efficiently identify the optimal subset of clients for corruption. The key idea of E-TS is to introduce an estimation of the expected maximum reward for each arm, which helps to specify a small set of \emph{competitive arms}, on which the exploration for the optimal arm is performed. This significantly reduces the exploration space, which otherwise can quickly become prohibitively large as the number of clients increases. We analytically characterize the regret bound of E-TS, and empirically demonstrate its capability of efficiently revealing the optimal corruption pattern with the highest attack success rate, under various datasets of popular VFL tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the adversarial attack in vertical federated learning inference phase. The adversary is the man-in-the-middle that can only perturbs the intermediate embeddings of the test samples sent by the clients. The authors propose an attack utilizing multi-armed bandit to dynamically choose the best subset of the clients to perturb. The goal of the adversary can be targeted (i.e., the prediction of the test sample is a specific label) and untargeted (i.e., the prediction of the test sample can be any label except a specific one). An ablation experimental study is provided to study how the different parameters (e.g., the number of corrupted channels, perturbation budget) impact the attack.

### Strengths
The paper is well-written, not hard to follow. The algorithm is clearly presented. The theoretical part seems solid with classical analysis.

### Weaknesses
However, I have some concerns on the attack design and the feasibility of the proposed method (detailed in the questions). I might misunderstand some part, but if the authors can answer my concerns, I would like to adjust my score.   For the correct stage, I would not go for the acceptance.

### Questions
Questions:
1) For the VFL inference setting, one point is not clear for me: the server broadcasts the probabilities vector back to all the clients for the inference. However, it would be more cost-saving to broadcast only the label. In this scenario, it would be harder to design attacks. Is there any reason that the client must receive the probability vector for the inference? 

2) I would like to see the discussion on how easy/difficult this attack can be noticed by the server. For me, it seems that targeted attack could be easily identified by the server. If the server observes that for test sample queries, the probability vector evolution converges to the same label, i.e., there might be an attack. Then one naïve way to mitigate this attack is that the server sends back always the probability vector obtained by using the first embedding query to avoid the training of $\eta_i^t$. Actually, I do not see the interest for the server to answer $n$ queries of the same test sample (line 10 in Algo 2) which helps the attacker to find the best perturbation.   

3) From my intuition, untargeted attack should be easier than the targeted one. If one can succeed the targeted attack with ASR $r$ on label $x$, then one would expect the untargeted one should be at least $r$ on label $y != x$. More precisely, let $r(x)$ be the targeted ASR on label $x$, the untargeted one on label $y$ should be better than $max$ {$r(x)|\forall x!=y$}. In the experiment, the results on FashionMNIST confirms this intuition, whileas the results on CIFAR-10 gives opposite observation. Could authors provide more explanation for this observation? Besides, what are the untargeted labels used in the experiments? 

4) In Figure 3c, when the query budget decreases to 500 for FashionMNIST, the targeted attack accuracy reaches almost 10%, which is equivalent to the ASR of no-attack case if the sample is randomly split in the batch.  The same observation can be found in Figure 5c when there is only one corrupted channel. Does it mean that when the query budget is limited or the number of corrupted channels is limited, applying the proposed method has smaller or even no advantage than doing nothing for targeted attack? What impacts the minimum necessary query budget and the minimum required number of corrupted channels? The complexity of the dataset, model or the scale of the system? I would like to have more insight on this problem.       

Minors:

1) The settings for each Figure are not well-indicated, especially for the ablation study. For example, in Figure 3, when we vary one parameter, what are the default values for the other parameters.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper delves into the vulnerabilities of Vertical Federated Learning (VFL)  through developing a novel attack to disrupt the VFL inference process, under a practical scenario where the adversary can adaptively corrupting a subset of clients. This paper frames this problem as an online optimization problem consisting of adversarial example generation (AEG) and corruption pattern selection (CPS). The paper equates CPS to a multi-armed bandit problem, proposing the Thompson sampling with Empirical maximum reward (E-TS) algorithm, which efficiently identifies the best clients to corrupt, backed by analytical regret bounds and empirical results showcasing its effectiveness.

### Strengths
Originality: The paper introduces a novel attack to disrupt the VFL inference process, under a practical scenario where the adversary can adaptively corrupting a subset of clients. This paper frames the attack problem as an online optimization problem consisting of adversarial example generation (AEG) and corruption pattern selection (CPS). CPS is solved by an bandit algorithm which is quite interesting and novel. 

Quality: The paper provides a rigorous analysis of the regret bound of the proposed E-TS algorithm. The paper also presents an attack algorithm for attackable instances. The paper also empirically evaluate the performance of the proposed attack on datasets with four major types of VFL tasks.

Clarity: The paper is well-written and  presents the concepts, definitions, and analyses with clarity and precision. The detailed presentation of the experimental setup and outcomes ensures comprehensibility and ease of replication for readers.

Significance: The paper characterize the regret bound of the proposed E-TS algorithm, and empirically demonstrate its capability of efficiently revealing the optimal corruption pattern with the highest attack success rate. The idea of using bandit algorithm to perform optimal attacks may have practical implications for designing efficient attack strategies.

### Weaknesses
Overall, I like the formulation of the attack problem and the idea of utilizing bandit algorithm to reveal the optimal corruption pattern. However, I have the following concerns:

1. The regret bound is a probability bound which only holds with some probabilities. However, the probabilities are not in the form like $1-p$. The probabilities depend on N and are less than $\frac{1}{2}$ for any N. If N is smaller than 10, the probabilities are further smaller than 0.07. I doubt whether this regret bound really provide enough information about the effectiveness of the proposed algorithm.

2. In Lemma 2 and Theorem 1, the regret guarantee requires that the selected warm-up rounds $t_0$ satisfies $\sqrt{\frac{t_0}{8N log(t_0)}} \ge \frac{1}{\Delta}$. As the adversary is a black-box adversary, $\Delta$ is unknown to the adversary, and there is no prior information about the choice of the $t_0$. The proper choice of $t_0$ is still a problem.

### Questions
1. See in Weakness 1. Can authors explain the choice of the probabilities and the bounds?

2. The performance of the proposed algorithm is related to the choice of $t_0$. The requirement of the prior information of $t_0$ violates the black-box setting. Can authors provide any insight into the proper choice of $t_0$ in the black-box setting?

3. In my opinion, the corruption pattern selection (CPS) problem is more like the setting of combinatorial multi-armed bandits (CMAB) with bandit feedback than MAB. Why did the author choose the model of MAB? Are there some benefits of MAB?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers adversarial attacks on Vertical Federated Learning via selection of a set of clients to corrupt, and choice of perturbations of their representations in VFL. The perturbations are subject to a bound, as also the cardinality of the selected client set.  The client subset selection problem (choosing C out of M clients to corrupt) is recast as a MAB problem, and a modified Thompson sampling approach is proposed to deal with the computational complexity (#arms Some theoretical results are presented, bounding the regret under the modified sampling method. ). Performance results are presented for several datasets.

### Strengths
VFL is an emerging area, and there has not been much work studying adversarial attacks in this setting.

### Weaknesses
The VFL setting as explained at the top of Section 2 is puzzling. This implies that a prediction query arrives simultaneously at all M clients.  But even in the given setting, why does the server need to broadcast the full probability vector, rather than the class with the maximal value? Is there a notion of a primary query client? Or is it more realistic that the query comes to the central server which then asks clients for their representations? 

What was the loss function L (in eqn (3), etc.) adopted in the experimental settings? 

Why is the constant \alpha^* needed in (4)? The later discussion in Sec 5.2 that the mean reward corresponding to the best arm (client subset) can be taken to be \alpha^* is also confusing. The adversary does not know \alpha^*, so how can it proceed to solve (4)? 

Algorithm 1:
- Please identify the inputs: t_o, {B_t, t=1,..,T} and the corresponding embeddings ….. 
- After line 11, shouldn’t there be a call to Alg 2 to compute the corrupted embeddings? 
- Line 6 should be in plural 
- Line 13: are the rewards assumed to be positive? 
- The role of \phi is not clear. Let n(t) be the number of times a given arm is played, and let r(j) denote the corresponding rewards. Then \phi = \frac{1}{n(t)} \sum_{j=1}^{n(t)} \max(r_i, i=1,…j). Why is this an useful quantity to compute
-  What is the reward? Is it merely the ASR over the batch? With reference to Remark 1 and the discussion of [Gupta et al., 2021], is the reward in this setting simply 0 or 1 (so max=1)? 
 
Experiments
Given that the value of N is small in all the settings (M takes values of 6, 7, 8 and 10, and C = 2,3,4), it would have been insightful to show how the best arm selection changes over t \in [1, T]. It would also have been insightful to show how the size of the restricted set decrease with t. 

The choice of datasets is poorly motivated for the VFL problem. The credit score and Caltech datasets are reasonable, but segmenting a CIFAR or MNIST image into segments, or an IMDB review at different clients is not reasonable. 

A value of Q=1000 is outrageously large. Servers with any reasonable security settings would turn off queries if they are repeated more than 3 or 5 times. A large Q is simply a mechanism for an adversary to learn (more samples). Q = 1000 is not a reasonable number. 
What were the default values of \beta, B^t, T and C?

The “Ablation study” is not particularly helpful. That the adversary’s success rate would increase with \beta, T, or C is obvious. This does not add any insights. Further discussion on choosing t_o would be useful. 

In Figure 1 what do the curves ‘Client 4 5’ etc. mean? Why are different client pairs shown in different plots? What is a test epoch and what does 25 attack rounds/test epoch mean? Does this mean that B^t is fixed at 25? And that T  was 30 (judging from the figures)?
There is little difference between TS and E-TS after about 5 epochs. What is the corresponding complexity comparison? The log(T) to O(1) improvement does not seem to show up here. 

Figure 2: Fashion MNIST has 7 clients; so even with all 7 clients corrupted, manifold defense does pretty well. This is a surprising and unexpected result. 

Figures 2, 3 (and parts of 1): Figures showing performance results on Credit Score or the Caltech dataset would have been more meaningful. More specifically, recognition of MNSIT / Fashion MNIST / CIFAR does not require all pieces of the full image; neither does sentiment analysis of a review; further, as noted earlier, such segmentation is unrealistic in any case. 

Figure 4: What is the setting with 16 and 28 clients? How were the images segmented? Is it meaningful to have a 28-pixel image segment at each of 28 clients? 

Theoretical results
Lemma 1, Lemma 2, and Theorem 1 appear to have an implicit large N assumption.  The lower bound on the probability is negative for N < 55, and exceeds 0.5 at about N=150. 

How does the proposed E-TS algorithm work compared to sequential arm elimination proposed in 
S. Shahrampour, M. Noshad and V. Tarokh. On Sequential Elimination Algorithms for Best-Arm Identification in Multi-Armed Bandits. IEEE Transactions on Signal Processing, vol. 65, no. 16, pp. 4281-4292, 15 Aug.15, 2017 

Is a factor 2 missing in the equation for Fact 1?

In the proof of Lemma 4, shouldn’t the = sign be <= on line 5. The transition from line 6 to line 7 (“g”) is not clear. 

Proof of Lemma 5: The fact that … towards the end of the proof is not obvious; it holds asymptotically; why does it hold for all T?

Proof of Theorem 1: Please add proof details. The terse statements are insufficient. 

Puzzling statement in Section 3: “β ∈ [0, 1] is the perturbation budget of some simple magnitude-based anomaly detector.” Whose anomaly detector, and why is it assumed to be simple?



Before (2): “taking over” should be “taken over”. 

P6, line 7: “obtain” should be “obtains”. 

The sentence about the large exploration space (below Fig 1 and Fig 2) is confusing. How are these numbers obtained?

### Questions
Please see comments under Weaknesses

--- Added after rebuttal/discussion phase -

The authors have addressed all my major concerns; they have added substantially to the Supplementary Material, and made changes as needed, including strengthening of one of the Lemmas. Based on this I have changed my score to Accept.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To me it seems the main contribution of this paper is the formulation of the adversarial attacks in the VFL setting as a MAB problem and the development of the E-TS algorithm, whose usage in practice seems unrealistic to me, considering the combinatorial structure of the problem and availability of combinatorial MAB algorithms.

### Strengths
The paper is nicely written and executed. 
Their contributions are clear and the experimental results are fairly diverse.
The formulations of the problem in (3) and (4) as a MAB problem is interesting, and to my knowledge and as per authors' claim, novel as well.
The E-TS algorithm is an interesting approach to circumvent the combinatorial structure of the problem and the authors provide regret bounds and experimental evidence as to the expected performance improvement gained from E-TS. However, I am not fully convinced to its practical utility.

### Weaknesses
The E-TS algorithm is supposed to outperform the TS algorithm via the machinery of "competitive arm set" constructed at each round. 

A critical point that leaves me in doubt about E-TS is the number of required warm-up rounds t_0 being too large to the point it renders E-TS useless, even with fairly small scale problems. This is suggested both by intuition and Lemma 2, i.e., it grows proportional to the inverse square of the minimum sub-optimality gap and to the number of total arms, which grows exponentially in number of individuals arms to be selected, therefore rendering E-TS' practical utility very limited in my opinion. For instance, I would like to see what happens when the number of clients to be selected is increased from 2 or 3 to, say, 7-8 in Figure 4. There is a vast literature on "combinatorial" MABs which could offer better solutions to this problem with lesser assumptions, e.g., by imposing and exploiting some sort of structure between the arms.

### Questions
no questions for now

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

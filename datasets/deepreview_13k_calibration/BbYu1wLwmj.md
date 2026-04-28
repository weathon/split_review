# Safe Meta-Reinforcement Learning via Dual-Method-Based Policy Adaptation: Near-Optimality and Anytime Safety Guarantee

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
This paper studies the safe meta-reinforcement learning (safe meta-RL) problem where anytime safety is ensured during the meta-test. We develop a safe meta-RL framework that consists of two modules, safe policy adaptation and safe meta-policy training, and propose efficient algorithms for the two modules. Beyond existing safe meta-RL analyses, we prove the anytime safety guarantee of policy adaptation and provide a lower bound of the expected total reward of the adapted policies compared with the optimal policies, which shows that the adapted policies are nearly optimal. Our experiments demonstrate three key advantages over existing safe meta-RL methods: (i) superior optimality, (ii) anytime safety guarantee, and (iii) high computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the problem of ensuring safety in meta-reinforcement learning (meta-RL) by proposing a framework that guarantees anytime safety during meta-testing. The approach is based on dual-method-based policy adaptation, which includes modules for safe policy adaptation and safe meta-policy training. It provides empirical results showcasing improvements over existing safe meta-RL methods in terms of optimality, safety guarantees, and computational efficiency.

### Strengths
1. The method achieves high computational efficiency, making it advantageous for scaling to complex tasks.

2. Empirical results demonstrate that the proposed method outperforms baseline approaches in terms of both optimality and safety across a variety of tasks.

### Weaknesses
1. The related work section lacks thorough investigation, e.g., some multi-task/multi-objective safe RL methods; these can be helpful for meta-safe RL.

2. The paper is not well-written and appears to rely heavily on language models for content generation, e.g. the abstract.

3. The method lacks novelty; based on my understanding, it does not present new contributions, including in the theoretical aspects. It extends primal-dual settings for meta-safe RL, similar to primal meta-safe RL (meta-CRPO).

### Questions
Why was a dual-method-based approach chosen over other constraint-handling techniques?  I guess that using any state-of-the-art safe RL baseline in meta-RL settings could also achieve good performance.

Could there be advantages to comparing it with alternatives, such as shielded RL?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed a safe meta RL framework to learn a meta policy which is safe to a new RL task. The key contributions include (i) theoretical analysis and show that anytime safety guarantee can be achieved if the initial policy is safe, (ii) theoretically analyze the tradeoff between safety guarantee and optimality, (iii) empirically validated its outperformance against other meta RL algorithms in computational efficiency and reward / safety performance.

### Strengths
1. This paper is a theoretically dense paper and its core strength lies in its theoretical derivations and insights. The paper did a good job in showing the safety guarantee (when initial policy is safe) and Theorem 1 provides key insight on the tradeoff between this safety guarantee and reward optimality.  

2. The paper did a thorough study on the shortcomings of other safe meta RL paper and identified the key area which it can improve on (i.e. computational efficiency and anytime safety guarantee.  

3. The empirical result shows that it convincingly outperforms other safe meta RL algorithms in terms of computational efficiency and reward / safety performance.

### Weaknesses
1. The experiments portion of this paper is relatively short (esp in main paper). I'd think including other experiments would further improve the paper. For example, trying out different values of $\delta_{c_i}$ (allowable constraint violation) and observe the tradeoff between reward and safety.

2. The allowable constraint violation $\delta_{c_i}$ seems like a hyper-parameter and I would appreciate further guidance on how to determine the appropriate value for a safety-constrained task. Perhaps performing experiment suggested in item (1) above could help.  

3. The paper does point out the inherent shortcoming of CPO being computationally expensive and proposed a dual method for safe policy adaptation. However, the safe policy adaptation problem outlined in Eq4 & 5 seems rather similar to Lagrangian-based online safe RL algorithm, e.g. RCPO, PPO-Lagrangian. The authors might want to illustrate how is this dual method particularly novel.  

4. To achieve anytime safety, the initial policy should already be safe. The paper could further illustrate how this is achieved. In Fig1, safe meta RL seems to start with safe policy in test env while MAML and meta-CRPO don't. I'm curious how this is achieved in practice.  

5. In Fig4, meta-CPO (blue dashed line) is not present in the humanoid task. Is there any reason why this method is missing from humanoid task only?

### Questions
Please refer to the Weakness section and I'm more than happy to discuss if there's anything I misunderstood or missed out.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the safe meta-reinforcement learning (meta-RL) problem, and proposes a novel meta-RL algorithm that achieves 1) superior optimality, 2) anytime safety, and 3) high computational efficiency. The proposed algorithm is shown theoretically to achieve monotonic improvement, near optimality, and anytime safety. Experimental results are provided to support the 3 claims.

### Strengths
The considered problem is important. The proposed algorithm has 3 key advantages including superior optimality, anytime safety, and high computational efficiency. The key advantages are justified both theoretically and empirically.

### Weaknesses
1. My most important concern about this paper is its writing.

    - While the proposed algorithm is strong, no intuition is provided when introducing the algorithm structure, making the flow of the paper not smooth.

    - The connection between the proposed approach and Meta-CRPO and Meta-CPO is not clear. Although this is briefly discussed in the appendix, I suggest connecting the proposed method with the previous approaches also when introducing the new algorithm. This makes the readers much easier to understand what the key difference in the algorithm is that makes the proposed method perform better. 

    - There is some ambiguity about some terms introduced in the paper. Please see Questions for details. 

2. The experimental results can be improved. The influence of the hyperparameters is not discussed or tested, and how to select the hyperparameters is unclear.

### Questions
1. Line 69 "Both meta-CRPO and meta-CPO provide positive upper bounds of the constraint violation". Do the authors mean $d_i > 0$ or meta-CRPO and meta-CPO cannot satisfy the constraint that the sum of $c_i$ less than $d_i$?

1. Line 129: There is a sum over $a'\in\mathcal A$ when defining the softmax policy. Does it mean that the paper only considers discrete action space?

2. Line 137: Should the $J_{c_i, \tau}(\pi)$ be $J_{c_i}(\pi)$?

3. Line 192: it is said that setting $\delta_{c_i} = 0$ for all $i$ is too strict, and to alleviate the issue, the paper set $\delta_{c_i}\geq 0$. However, in the hyperparameters provided in Table 2, why $\delta_c$ is set to $0$ in all environments?

4. Line 210: "Safety cannot be guaranteed in each step". What is the definition of "step" here?

5. Line 245: "The complete statement of Proposition 3 that...". Is this Proposition 1 instead? Same question for Line 246 "Proposition 3 shows that..."

6. Line 324: "Note that the meta-gradient in (6) does not include the computations of Hessian and inverse of Hessian w.r.t. $\phi$". Could the authors clarify the reason why the meta-gradient in (6) avoids the Hessian and what is the cost of not using Hessian?

7. Does assumption 2 imply that the state space considered in the paper needs to be discrete and finite?

8. Can the proposed algorithm work if the max accumulated cost constraint is set to $0$?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an algorithm for a safe meta-reinforcement learning problem. Specifically, the proposed algorithm ensures anytime safety during the meta-test, which consists of safe policy adaptation and safe meta-policy training modules. Theoretically, the authors prove the anytime safety guarantee of policy adaptation and show that the obtained policy is near-optimal. The authors' empirical experiments show that the proposed algorithm performs better than the baseline methods.

### Strengths
- This paper addresses an important and interesting problem. The motivation behind this problem is well-presented and easy to understand.
- The proposed algorithm is technically sound. It is easy to follow the deviation of the algorithm.
- The experiment has been well designed and the results are good. This paper sufficiently covers the necessary baseline methods including state-of-the-art methods. The benchmark tasks are Gym and Safety-Gymnasium, which are quite standard safe RL literature.

### Weaknesses
 - I have a serious concern about the theoretical results in Section 5. Specifically, I guess the authors have some misunderstanding regarding sufficient safe visits or ergodicity.
- This paper is on safe RL, which implicitly means that there is a set of states that cannot be visited (frequently). This also means that the ergodicity assumption does not hold in safe RL tasks. If I understand correctly, the authors seem to cite Moldovan and Abbeel (2012) as a piece of evidence that CMDP is ergodic in line 376. Unfortunately, however, in Moldovan and Abbeel (2012), there are opposite statements such as 

    > Almost all proposed exploration techniques presume ergodicity; authors present it as a harmless technical assumption but it rarely holds in interesting practical problems.
    
    > Unfortunately, many environments are not ergodic.

- Related to the above, I disagree with Remark 1 and Remark 2. If the authors address standard MDP, the remarks would be true. It is not true with CMDPs or safe RL. Safe RL studies should not assume ergodicity and thus actually consider "reachability" or "returnability" as in 
    - Turchetta, Matteo, Felix Berkenkamp, and Andreas Krause. "Safe exploration in finite markov decision processes with gaussian processes." Advances in neural information processing systems 29 (2016).
    - Wachi, Akifumi, and Yanan Sui. "Safe reinforcement learning in constrained markov decision processes." International Conference on Machine Learning. PMLR, 2020.
- Even worse, the authors try to propose an algorithm with almost surely. Hence, I feel Assumption 2 is incompatible with the nature of the proposed algorithm.
- The authors may want to argue that Assumption 2 still holds by setting a large $B$, but I guess such a large $B$ will lead to useless bounds on both safety and optimality.
- The authors may also want to insist that it is ok to guarantee safety only during meta-tests. However, I do not think it is reasonable to assume sufficient coverage "for any policy and any state."

### Questions
- Q1: Please tell me your thoughts about my comments in Weakness.

- Q2: Is it possible to relax Assumption 2 while maintaining the claims in Theorems?

### Soundness
1

### Presentation
2

### Contribution
2

# $\phi$-Update: A Class of Policy Update Methods with Policy Convergence Guarantee

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Inspired by the similar update pattern of softmax natural policy gradient and Hadamard policy gradient, we propose to study a general policy update rule called $\phi$-update, where $\phi$ refers to a scaling function on advantage functions. Under very mild conditions on $\phi$, the global asymptotic state value convergence of $\phi$-update is firstly established. Then we show that the policy produced by $\phi$-update indeed converges, even when there are multiple optimal policies.  This is in stark contrast to existing results where explicit   regularizations  are required to guarantee the convergence of the policy.  Since softmax natural policy gradient is an instance of $\phi$-update, it provides an affirmative answer to the question whether the policy produced by softmax natural policy gradient converges. The exact asymptotic convergence rate of state values is further established based on the policy convergence. Lastly, we establish the global linear convergence of $\phi$-update.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the convergence of $\phi$-Update, which modifies the exp in softmax of natural policy gradient method to another $\phi$ function, which is positive and monotonically increasing.

The authors studies several convergence results with exact gradient updates, including asymptotic convergence, rate of convergence, and policy convergence, and also verified the results using simulations.

### Strengths
The proposed $\phi$-update is sort of different but connected with existing methods.

The analysis is comprehensive and theoretical results are fine.

The paper is well written and easy to follow.

### Weaknesses
I am a bit concerned with the exact gradient setting. Although it is a slightly different update than softmax PG/NPG variants, it is also fair to say that the exact PG is a well understood and studied setting since Agarwal2019 and many papers after that as noted in the paper.

I understand that this is mainly theoretical work. However, one suggestion might be that some promising experimental results might show that there is a real motivation of using alternative $\phi$ transforms than standard softmax (also comparisons with existing alternatives should be included).

In terms of extending the work to neural networks, I am a bit concerned this $\phi$ transform is not easy to be extended. The proposed update is multiplicative in policy space (Line 100), and to make that compatible with NNs (say there are logits outputed for actions, and the some transforms of logits will give probabilities over actions), the $\phi$ transform needs to satisfy $\phi(a) \cdot \phi(b) = \phi(a+b)$, which  reduces back to the exp function (softmax transform). Given this, it is hard to see how the $\phi$ transform will be a very promising direction to study in function approximation settings.

### Questions
I understand that this is mainly theoretical work. However, one suggestion might be that some promising experimental results might show that there is a real motivation of using alternative $\phi$ transforms than standard softmax (also comparisons with existing alternatives should be included).

In terms of extending the work to neural networks, I am a bit concerned this $\phi$ transform is not easy to be extended. The proposed update is multiplicative in policy space (Line 100), and to make that compatible with NNs (say there are logits outputed for actions, and the some transforms of logits will give probabilities over actions), the $\phi$ transform needs to satisfy $\phi(a) \cdot \phi(b) = \phi(a+b)$, which  reduces back to the exp function (softmax transform). Given this, it is hard to see how the $\phi$ transform will be a very promising direction to study in function approximation settings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies policy parameterization for tabular MDPs using a scaling function  $\phi$, which serves as a systematic generalization of the softmax NPG method. Convergence rate proofs are provided and numerical simulations are illustrated to validate the theoretical claims.

### Strengths
The paper addresses a gap in the literature by extending policy parameterizations of tabular MDPs beyond traditional methods like softmax and escort transformations. By applying a general scaling function  $\phi $ in the policy update step, it potentially contributes to the broader understanding of policy gradient methods analyzed through the mirror descent framework given more discussion of distinction is provided.

### Weaknesses
 - While the paper claims to offer a novel analysis of general policy updates without relying on standard regularization methods such as softmax NPG, it does not clearly distinguish its approach from existing methods. Given that softmax NPG is equivalent to policy mirror descent with a Kullback-Leibler (KL) divergence regularizer (Shani et al., 2020), the paper needs to clearly explain how the proposed  $\phi $-update differs from or improves upon established mirror descent techniques. Without this distinction, the originality and necessity of the proposed analysis approach remain unclear if current theory literature can already encapsulate such approaches with a general regularize used in the mirror descent policy update step (Lan 2023).

- The paper briefly mentions the application of the proposed method in function approximation settings where  $\phi$  is induced by a neural network in Section 4.2. However, it lacks a concrete implementation example or discussion on how the necessary assumptions can be verified in practice. Including such an implementation would enhance the practical relevance and demonstrate the method’s applicability despite potentially unverifiable assumptions.

### Questions
In the context of implementing general policy parameterizations with neural networks (Section 4.2), how can the underlying assumptions of the proposed method be verified or satisfied? Specifically, is the approach compatible with input-convex neural networks (or other popular parametrization scheme for finite MDP with function approximation), and if so, how does it ensure the validity of the theoretical guarantees presented?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
phi-update

Summary: The paper proposes a new "general" class of update rules for "policy optimization" to find optimal policies in Markov Decision Processes. The new update rules takes the form $\pi'(a|s) \propto \pi(a|s) \phi( \eta(s)A^\pi(s,a))$, where $\pi'$ is the new policy, $\pi$ is the previous policy and $A^\pi$ is the advantage function of $\pi$, while $\eta(s)$ is a step-size that may depend on the state (but not on the actions), and $\phi$ is a "transfer" function that maps reals to reals. By choosing $\phi(t)=\exp(t)$ we get back the update of the "natural policy gradient" method, while $\phi(t) = (1+2t)^2 we get back the update rule of what is known as "Hadamard PG" (which is related to the "escort transform" based updates of some other previous work). In a nutshell, the new update rule unifies some previous update rules. The main result in the paper is the convergence of policies to some optimal policy and the exact asymptotic rate of value subotimality, while the stepsizes are allowed to be very general (as long as they are bounded away from zero; including adaptive stepsizes). 

Significance: There is considerable interest in the community to gain a deeper understanding of how to design effective and efficient algorithms and one line of active research looks at variations of "policy gradient" methods, or, as done in this paper, at variations of policy update rules. The contribution of this paper should thus be interpreted in this context. I think the question asked is reasonable and it deepens our understanding of policy update rule design. The results go beyond previous results in the area in a number of ways: The authors manage to remove the (annoying and, as it turns out, unnecessary) condition that the optimal actions are unique at all states. The asymptotic convergence rate result is also a nice contribution.

Soundness: I looked at the proofs at various places and did not find any problems with them and the results do look reasonable to me. I believe the results are sound.

Related work: The authors do a good job at discussing related work, except for two things: (1) the relation to the escort transform based work remains a bit unclear. (2) I feel that maybe the novelty of the proof techniques is overclaimed on the basis that the update is not given in the parameter space. However, this was only because the authors chose not to consider the parameter space updates. With a softmax parameterization, an equivalent form for the update is $\theta'(s,a)=\theta(s,a) + \log \phi( \eta(s) A^\pi(s,a))$. This also shows that the function $\psi(t) = \log(\phi(t))$ is perhaps even more fundamental to these update rules (condition (III) in the paper is indeed a condition on the rate of growth of this function in the vicinity of zero, which I feel demistifies this condition quite a bit).

Presentation: There are quite a few typos, grammatical problems (I will add a list to the end of my review in the coming days to help the authors correct the ones I found). There are also symbols used in the main text (e.g., $A^k$, $\mathcal{A}_s^k$ used in line 322, ..) with no definitions given for them as far as I could see (line 133 was maybe an attempt to define all these quantities; but it did not..). Nevertheless, these problems are relatively minor  and can be fixed in a revision easily. Also, I found that some results added little if anything. E.g., Theorems 3.5, and 3.6 are full of algorithm dependent parameters and thus have no clear interpretation (other than they also state an asymptotic rate). Thus, should they be part of the main text?

### Strengths
Interesting problem, interesting results, new insightful proofs (avoiding uniqueness of optimal action!, generalization of previous arguments, showing what was really important about the updates)

### Weaknesses
Presentation: There are quite a few typos, grammatical problems (I will add a list to the end of my review in the coming days to help the authors correct the ones I found). There are also symbols used in the main text (e.g., $A^k$, $\mathcal{A}_s^k$ used in line 322, ..) with no definitions given for them as far as I could see (line 133 was maybe an attempt to define all these quantities; but it did not..). Nevertheless, these problems are relatively minor  and can be fixed in a revision easily. Also, I found that some results added little if anything. E.g., Theorems 3.5, and 3.6 are full of algorithm dependent parameters and thus have no clear interpretation (other than they also state an asymptotic rate). Thus, should they be part of the main text?

### Questions
So what $\phi$ should we choose and how to set the step-size? It is not very clear we gained too much by the end of the paper other than seeing that there is a whole set of new update rules one could study.

I was surprised that the exact asymptotic rate does not depend on $\gamma$. But I guess $\gamma$ creeps back in through $\Delta$? Perhaps this should be discussed?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a general policy update, called the $\phi$-update, inspired by softmax NPG and Hadamard PG. Under the assumption of exact gradients, convergence is analyzed in the tabular setting. First, global asymptotic convergence is shown for the value function, as well as for the policy itself. Then, a linear rate of convergence is established. The authors provide a tabular numerical toy example to verify the tight theoretical convergence rate under exact gradients and describe how to extend the theory of $\phi$-updates to general non-tabular parameterizations.

### Strengths
**S1:**	Well-motivated new policy update.

**S2:**	Solid theoretical analysis in the exact gradient setting, both asymptotic and non-asymptotic, although I have a question regarding the linear convergence rate (see below).

**S3:**	The exact gradient rates are tight, which is verified in numerical examples.

### Weaknesses
 **W1:** The constant $\rho(\epsilon)$ is not exactly stated in terms of model parameters. How close is this constant to $1$?

**W2:** Analysis limited to exact gradient case, stochastic analysis would be interesting. 

**W3:** The authors present examples in the tabular case. It would be nice to also analyse the generalised variant presented in Sec. 4.2. It remains unclear if this version works in practical applications. 

Although I understand that this is a theoretical paper which leaves stochastic analysis and experiments to future work, it would be nice to have at least one (toy) stochastic application that verifies practical performance

**Minors:**

Typo in the definition of $\kappa(\epsilon)$? It should be $\max_{t\leq T(\epsilon)}$ as there is no $k$ apprearing within the max.

### Questions
**Q1:** Can you give a more precise description of the constant $\rho(\epsilon)$, in terms of model parameters like $\gamma$, $|\mathcal S|$ or $|\mathcal A|$? You stated yourself that in (Mei et al., 2020b) a constant $c$ appears in the softmax convergence rate which can be extremely small. (Mei et al., 2020b) state a sublinear convergence rate which can have very poor performance with respect to the discount factor (see [1]) and it would be nice to know if such a counter example can also appear for your algorithm. The term in the definition of $D_t$ looks very similar to the "bad" constant $c$ in (Mei et al., 2020b).

**Q2:** The error curves in the simulations in Fig. 2 and 3. look very smooth. Did you use the transition probabilities to calculate the exact $\phi$-updates or did you use simulations? 



[1] *Li, Gen, Yuting Wei, Yuejie Chi, and Yuxin Chen. “Softmax Policy Gradient Methods Can Take Exponential Time to Converge.” Mathematical Programming 201, no. 1–2 (September 2023): 707–802. https://doi.org/10.1007/s10107-022-01920-6.*

### Soundness
3

### Presentation
3

### Contribution
3

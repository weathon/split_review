# Magnetic Mirror Descent Self-play Preference Optimization

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Self-play methods have demonstrated remarkable success in enhancing model capabilities across various domains. In the context of Reinforcement Learning from Human Feedback (RLHF), self-play not only boosts Large Language Model (LLM) performance but also overcomes the limitations of traditional Bradley-Terry (BT) model assumptions by finding the Nash equilibrium (NE) of a preference-based, two-player constant-sum game. However, existing methods either guarantee only average-iterate convergence, incurring high storage and inference costs, or converge to the NE of a regularized game, failing to accurately reflect true human preferences. In this paper, we introduce Magnetic Preference Optimization (MPO), a novel approach capable of achieving last-iterate convergence to the NE of the original game, effectively overcoming the limitations of existing methods. Building upon Magnetic Mirror Descent (MMD), MPO attains a linear convergence rate, making it particularly suitable for fine-tuning LLMs. To ensure our algorithm is both theoretically sound and practically viable, we present a simple yet effective implementation that adapts the theoretical insights to the RLHF setting. Empirical results demonstrate that MPO can significantly enhance the performance of LLMs, highlighting the potential of self-play methods in alignment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper the authors study the problem of Reinforcement Learning from Human Feedback. As it was shown in bibliography this problem can be seen as a two-player constant sum game with Nash equilibrium as a solution. In this paper the authors study the last-iterate convergence to a Nash equilibrium in this context giving new dynamics for this. They show last-iterate convergence and give experiments that show evidence that there is improvement of the problem with their algorithm.

### Strengths
I think that it is nice to see how different areas of research are combined and results of the one area can be used to the other. In this direction the authors study/prove the last-iterate convergence to a Nash equilibrium of a game in their context, giving new techniques and ideas. Furthermore, this paper shows another example of the importance of last-iterate convergence to Nash equilibria in constant sum games.

### Weaknesses
I think the presentation of paper has space of improvement, especially in the technical/mathematical part.

In 145 line it is stated that the constant sum game has unique and symmetric Nash equilibrium in this context (which is not true for any constant-sum game in general). Do similar results hold without having the uniqueness assumption? In what exact point in the proofs the uniqueness of the Nash equilibrium is needed?

### Questions
In 145 line it is stated that the constant sum game has unique and symmetric Nash equilibrium in this context (which is not true for any constant-sum game in general). Do similar results hold without having the uniqueness assumption? In what exact point in the proofs the uniqueness of the Nash equilibrium is needed?

### Soundness
3

### Presentation
2

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
The paper presents the Magnetic Mirror Descent Self-Play Preference Optimization (MDSPO) framework, a novel approach in the field of Reinforcement Learning from Human Feedback (RLHF). It addresses the limitations of the Bradley-Terry model by reframing preference learning as a two-player constant-sum game and aims to converge to the Nash equilibrium (NE) of this game. MDSPO introduces a magnetic term to achieve linear convergence to the NE of the regularized game and provides theoretical guarantees for last-iterate convergence to the NE of the original game. The empirical results demonstrate significant improvements compared to the SFT method under the MixEval-Hard benchmark.

### Strengths
1. By using the proposed magnetic mirror descent (MMD) method, this work achieves the last iteration convergence guarantee for the NE of the game under the general preference setting, which is better than previous works.
2. The proposed MDSPO method achieves a great performance compared to the SFT method.

### Weaknesses
1. The motivation for introducing the magnetic term in MMD is currently unclear. It would be helpful to discuss the technique challenge to achieve last-iteration convergence when using mirror descent. After that, this work can show the reason why the MMD method can solve the above problem and achieve great performance, which would deepen the understanding of MMD.
2. For the experiment part, this work uses the SFT method as the baseline. It would be better to add additional experiments such as the RLHF with PPO to do a more comprehensive comparsion.

### Questions
Please see the Weakness part.

Typo: It should be $y_{<t}$ instead of $ y_{<k}$ in line 116.

### Soundness
3

### Presentation
2

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
This paper studies Reinforcement Learning from Human Feedback methods by formulating the problem as finding the Nash Equilibrium of one regularized game. By introducing the Magnetic Mirror Descent approach, they achieve linear last-iterate convergence instead of average-iterate convergence in previous works. Consequently, they provide an algorithm with a theoretical guarantee for convergence, and provide two slightly different ways for implementation (MDSPO and MDSPO-RT) with theoretical insight.

### Strengths
1. The extension from SPO to MDSPO algorithm is well-motivated, and the motivation presents well.
2. The experiment is solid, and the performance is good.
3. The idea of periodically updating the magnet policy is interesting, and the theoretical convergence result is provided.
4. In addition to MDSPO, the authors also provide a slightly different algorithm MDSPO-RT, and provide empirical comparisons.

### Weaknesses
1. The empirical part:

(1). The connection between theoretical contribution and the empirical implementation is not clear. More explanations about how the Magnetic Mirror Descent (MMD) objective induces the update rule in eq (6) would enhance the paper. For example, the first term on the right side of eq (6) appears to only involve sampling from the current policy and seems unrelated to the policy $\pi$ in the MMD update and seems could be ignored, making this equation not similar to the MMD update rule. A more detailed derivation or intuitive explanation bridging the theoretical MMD framework and the practical implementation in eq (6) would significantly improve clarity.

(2). In Line 331-333, the paper argues that the choice between MDSPO and MDSPO-RT depends on the requirements of tasks. However, it lacks further guidance on how to make this choice. The statement is too general to provide practical insight. Additionally, the empirical results only include a task where MDSPO-RT performs worse than MDSPO. Could the authors provide more insight into selecting between the two algorithms? For instance, are there specific task characteristics or metrics that would favor one over the other? A more concrete guideline, potentially with examples of scenarios where each algorithm excels, would be beneficial.

(3). Since the paper is motivated by the problem of average-iterate convergence, the empirical observation about this phenomenon and how the MDSPO alleviates this problem would significantly strengthen the work. Additionally, empirical comparisons between SPO and MDSPO seem essential for a comprehensive evaluation. Demonstrating the practical implications of the theoretical convergence properties would provide strong evidence supporting the proposed method.

3. The theoretical part: 

(1). First, Theorem 3.2 almost follows the same derivation as Theorem 3.4 in [1]. It would be clearer to state explicitly that Theorem 3.2 is a modification of [1] and include the citation prior to presenting it.

(2). The essential theoretical contribution is Lemma 3.3 and Theorem 3.4. However, the proof of these theorems could be polished. For example,  In line 976, what's the term $\langle D_{KL}(\pi_r^{\*,n+1}|| \pi_r^{\*,n}), \pi_r^{\*,n+1}, \pi^\*\rangle $ mean? I assume it's $\langle D_{KL}(\pi_r^{\*,n+1}|| \pi_r^{\*,n}), \pi_r^{\*,n+1}-\pi^\*\rangle.$ Also, in Line 992, it is unclear why the first-order optimality condition can be applied here since the first term $\nabla D_{KL}(\pi_r^{\*,n+1}|| \pi_r^{\*,n})$ doesn't depend on $\pi^\*$. Moreover, in Line 998 and 999, the 3rd and 4th terms in the inequality should involve $\pi_\*$ instead of $\pi^\*$.

(3). In footnote 4, the paper [2] suggests that one could apply optimistic mirror descent (OMD) to achieve a last-iterate guarantee. Why did the authors choose the MMD rather than the OMD? Are there some technical difficulties in directly applying OMD? A brief discussion on the rationale behind this design choice would be valuable.


### Questions
The questions are provided in the weakness part.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes mirror descent self-play preference optimization (MDSPO), which has a last-iteration convergence to the Nash equilibrium (NE) of the two-player constant-sum normal form game induced by a reinforcement learning from human feedback (RLHF) problem with non-transitive preference. In the regularized magnetic mirror descent setting, the policy converges to the regularized NE at a linear rate, which is faster than the result in previous work. By solving a series of regularized games sequentially, one can have a last-iterate convergence to the NE of the original game. The authors also give practical implementation for the theoretical algorithm and it shows an improvement in several benchmarks.

### Strengths
1. This work studies the Nash learning setting, which has broader significance than the Bradley-Terry preference setting as the preference could be arbitrarily non-transitive.
2. The guarantee of last-iteration convergence to NE has practical benefits for large language models (LLMs) as the inference time and stability (low variance) is important.
3. This paper presents the first theoretical result for last-iterate convergence to the NE of the original game, as previous result was for the regularized game.

### Weaknesses
1. The convergence rate to the original NE is not studied. The authors should either give an analysis of the convergence rate or explain why such an analysis may be challenging.



### Questions
1. The approach described in Section 3.2 seems hard to implement, since we cannot get the exact NE policy $\pi_\text{reg}^{*,n-1}$. What we have from MMD is an approximation of this NE. What will the convergence result be if the approximation error is taken into consideration?
2. In the paper "Nash Learning from Human Feedback" by Munos et. al., the algorithm Nash-MD achieves last-iterate convergence (cf. their Theorem 1) to a regularized NE. Can their algorithm be adapted to the approach in your section Section 3.2 and achieve a last-iterate convergence to the original NE?

### Soundness
3

### Presentation
2

### Contribution
2

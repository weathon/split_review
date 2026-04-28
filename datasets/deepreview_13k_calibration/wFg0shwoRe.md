# Expected Return Symmetries

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
Symmetry is an important inductive bias that can improve model robustness and generalization across many deep learning domains. In multi-agent settings, a priori known symmetries have been shown to address a fundamental coordination failure mode known as mutually incompatible symmetry breaking; e.g. in a game where two independent agents can choose to move "left" or "right", and where a reward of +1 or -1 is received when the agents choose the same action or different actions, respectively. However, the efficient and automatic discovery of environment symmetries, in particular for decentralized partially observable Markov decision processes, remains an open problem. Furthermore, environmental symmetry breaking constitutes only one type of coordination failure, which motivates the search for a more accessible and broader symmetry class. In this paper, we introduce such a broader group of previously unexplored symmetries, which we call expected return symmetries, which contains environment symmetries as a subgroup. We show that agents trained to be compatible under the group of expected return symmetries achieve better zero-shot coordination results than those using environment symmetries. As an additional benefit, our method makes minimal a priori assumptions about the structure of their environment and does not require access to ground truth symmetries.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper addresses the zero-shot coordination problem in multi-agent systems within the context of decentralized partially observable Markov decision processes. It introduces a new symmetric class, which is a class containing the previously proposed environment symmetries. The paper also presents an algorithm to find these symmetries and demonstrates that agents within this symmetric class can achieve better zero-shot coordination in decentralized partially observable Markov decision processes.

### Strengths
1. The organization of this paper is well-structured.
2. The paper conducts experiments in several zero-shot coordination tasks and gives comprehensive analysis.

### Weaknesses
As I'm not familiar with this field, it is hard for me to give constructive suggestions to the authors.

### Questions
As my understanding of this paper is limited, I hope the authors can provide an intuitive example to illustrate why their proposed symmetry class is better than the Other-Play algorithm [1].

[1] Hu, Hengyuan, et al. "“other-play” for zero-shot coordination." International Conference on Machine Learning. PMLR, 2020.

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
This work explores *symmetry in expected returns* as an inductive bias for training agents that are more capable of zero-shot coordination.

### Strengths
- The writing is clear, concise, and detailed.
- The approach is well-motivated theoretically, and seemingly well-grounded in prior literature.
- Discussion of prior work appears complete. 
- The experiments are compelling, and validate the claims made in the paper.
- Future directions are compelling. 
- Work is likely to be of interest to the broader field.

### Weaknesses
 - Limitations are not adequately addressed. I would suggested addressing this explicitly in the conclusion, between the summary and discussion of future directions. 
- Readability:
	- Figure 2 graph text is far too small.
	- What purpose do the black horizontal bars at the top and bottom of Figure 1's image serve? Seems the text would fit much better without these.

### Questions
- What are the key limitations of this approach?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends the concept of Dec-POMDP symmetry to Expected Return (ER) symmetry for the Other-Play (OP) objective. ER symmetry captures broader classes of symmetry-breaking by preserving the expected return of self-play optimal policies instead of the state, action, and observation spaces, thus increasing diversity within equivalence classes at the cost of some optimality. The authors introduce novel algorithms to discover ER symmetries and validate their effectiveness across three MARL environments with independent agents, demonstrating improvement in terms of zero-shot coordination compared to existing symmetry discovery methods.

### Strengths
+ The introduction of ER symmetry seems to be a new contribution, extending the symmetry-breaking methods beyond simple action and observation relabeling.
+ The use of various toy examples throughout the paper makes the key definitions and concepts easy to understand. 
+ The proposed approach is solid, and its effectiveness is underpinned by the with well-defined constructions of equivalence classes.

### Weaknesses
 - Despite the use of the toy examples and the effort by the authors, I feel the writing could be further improved for readability. Some sections are still a bit challenging to follow.
- The experiments largely focus on the Hanabi environment, while the results on overcook and cat/dog environments are very brief. More  complex environments, especially those with continuous action and state spaces, should be used to demonstrate the effectiveness and scalability of the ER symmetry method, which unfortunately remain unclear.
- For Hanabi, the comparisons are limited to self-play and cross-play using IPPO. How do the proposed methods compare with (i) self- or cross-play using other RL algorithms, (ii) SOTA MARL baselines in Hanabi that do not necessarily employ self- or cross-play? I'm mostly interested in seeing how the proposed algorithms compare with SOTA MARL algorithms out there.

### Questions
1. Please address the questions raised in the weakness section, regarding experiments on more complex environments and comparison with SOTA MARL baselines.
2. In the caption of Figure 2, the mean SP score for the baseline population is listed as “162.33 ± 0.14,” while the graph displays a mean of 6.74. Is this a typo? I'd suggest the authors to thoroughly check all results presented in the paper.
3. The evaluation of group properties reveals a high relative reconstruction loss (18.4%), does this violation of a group's property of closure under composition impact the performance of symmetry discovery and MARL performance greatly?
4. For real-world applications, could you elaborate on the interpretability of ER symmetries? Would it be feasible to construct more intuitive symmetry structures based on those discovered by your model, and how does this compare to the interpretability of Dec-POMDP symmetry?
5. Regarding Equation 9, how large is the deviation from optimality in practice? Specifically, what is the gap between Equation 9 and Equation 10 in your experimental results? Are these deviations minor enough to be negligible?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper generalizes the existing OP method to a more general symmetry group. They further define the group of expected return symmetries, and propose a novel method to learn expected return symmetries. The performance of the propose method significantly outperforms Dec-POMDP symmetries.

### Strengths
The introduction of expected return symmetries is novel, which is better suited for OP than Dec-POMDP symmetries. The proposed method greatly improves zero-shot coordination, significantly outperforming traditional Dec-POMDP symmetries. Moreover, expected return symmetries can be effectively applied in environments where agents act simultaneously.

### Weaknesses
1. The structure of the proposed expected return symmetries is quite similar to the state value funtion that evaluates the future expexted returns. It can be easily affected by the policies of other agents. In multi-agent settings, how the proposed method deals with non-stationary issue during self-play and cross play.
2. The authors argue that the optimal policies learned independently by an agent may not be compatible with other agents' policies during test time. It is not very clear that how the proposed method enhances the compatibility. How self-play optimal policies can differ significantly in coordination strategies.
3. The limitations of the proposed expected return symmetries should be discussed.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

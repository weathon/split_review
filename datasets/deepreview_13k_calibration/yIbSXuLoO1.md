# Set-Size Dependent Combinatorial Bandits

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
This paper introduces and studies a new variant of Combinatorial Multi-Armed Bandits (\CMAB{}), called Set-Size Dependent Combinatorial Multi-Armed Bandits (\SDMAB{}). In \SDMAB{}, each base arm is associated with a set of different reward distributions instead of a single distribution as in \CMAB{}, and the reward distribution of each base arm depends on the set size, i.e., the number of the base arms in the chosen super arm in \CMAB{}. \SDMAB{} involves a much larger exploration set of the super arms than the basic \CMAB{} model. An important property called order preservation exists in \SDMAB{}, i.e. the order of reward means of base arms is independent of set size, which widely exists in real-world applications. We propose the \SUCB{} algorithm, effectively leveraging the order preservation property to shrink the exploration set. We provide theoretical upper bound of $O\left(\max\left\{\frac{M\delta_L}{\Delta_{L}},\frac{L^2}{\Delta_S}\right\}\log(T)\right)$ for \SUCB{} which outperforms the classic \CMAB{} algorithms with regret $O\left(\frac{ML^2}{\Delta_S}\log(T)\right)$, where $M$ denotes the number of base arms, $L$ denotes the maximum number of base arms in a super arm, $\delta$ and $\Delta$ are related to the gap of arms. We also derive a lower bound which can be informally written as $\Omega\left(\max\left\{\min_{k\in[L]}\left\{\frac{(M-L)\delta_{k}}{\Delta_{k}^2}\right\},\frac{L^2}{\Delta_S}\right\}\log(T)\right)$ showing that \SUCB{} is partially tight. We conduct numerical experiments, showing the good performance of \SUCB{}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a new bandit setting, 
called Set-Size Dependent Combinatorial Multi-Armed Bandits (SSD-CMAB). The key difference between SSD-CMAB with the classical CMAB is the reward distribution associated with each base arm depends on the size of the played super arm in that round.
They propose a novel algorithm, SortUCB, for solving SSD-CMAB.

The writing is not that clear. I suggest adding a learning protocol for your proposed learning problem. Also, using more than half a page for notations is not that space efficient. It can be simplified.

### Strengths
a new setting

### Weaknesses
The writing is not that clear. I suggest adding a learning protocol for your proposed learning problem. Also, using more than half a page for notations is not that space efficient. It can be simplified.

The main concern is I am not convinced of the definition of regret. In my understanding, different rounds $t$ have different optimal arms, as the reward distributions depend on the size of the pulled super arm in that round. However, in (1), the optimal super arm is fixed.

Also, It is not fair to compare regret bounds for different settings, stated in the abstract.

Regret lower bound: partially tight? What does it not mean? Also, the derived regret lower bound is asymptotic. In addition, this work never specifies how to characterize a SSD-CMAB problem instance.

### Questions
Can SSD-CMAB be reduced to CMAB problem by setting some constraint to the super arms?

### Soundness
2

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
The paper proposes a variant of the standard CMAB that allows arms to change reward means based on the set size of the super arm, which is pulled, provided that the *order* of the arms in terms of their reward means is preserved. 

The paper tackles this new problem setup using a novel proposed algorithm SortUCB which splits the bandit process into three stages: Elimination, Sorting, and UCB Phase. SortUCB focuses on eliminating "bad" super arms fast and then focusing on a curated set of good super arms. The paper provides regret upper bounds as well as instance-dependent lower bounds on the set-size-dependent CMAB. The paper provides experimental synthetic evaluations on several baseline algorithms and showcases the improvement over them. 

The paper then extends the current algorithm to set dependent combinatorial bandit where the base arms are allowed to have different reward distributions even with the same set size and the set of super arms can be dictated by further constraints. This broadly generalizes the initial setup and makes it much more applicable. They provide another algorithm SortUCB-SD to tackle this setup using a ($n_1, n_2$)-efficiency oracle and prove regret upper bound for the same.

### Strengths
The following would contribute to the strengths of the paper:
- **Clear Writing**: The paper is well written, precise, and to the point. The paper does a good job going slowly and explaining the inner workings of the algorithms and intuitive understanding of the paper

- **Innovative Algorithmic Solutions**: The novel proposed methods SortUCB and SortUCB-SD provide attractive regret upperbounds and their performance is further bolstered using the synthetic experiments.

- **Theoretical performance guarantees**: The paper provides theoretical proof of both the regret upper bound and the partial tightness to the fundamental lower bound for the SSD-CMAB problem. 

- **Experiments**: The paper provides synthetic implementation with multiple baseline methods and showcases the prowess of the SortUCB method.

### Weaknesses
There are very few loopholes in the paper. The following are some points to work on further:

- **More justification on the Problem Setup**: The paper provides some justification on why this particular variant of CMAB is interesting and worth looking at, but it is not enough. A few dedicated paragraphs of potential application here would be a great addition. Specifically, the paper introduces a novel problem setup where the reward means of arms within a super-arm change based on the set size, while preserving the order of means. This is an interesting setup, but the paper needs to provide more concrete examples of real-world scenarios where this would be applicable. For instance, how does this model capture the dynamics of resource allocation, A/B testing, or recommendation systems, where the reward structure might change with the number of active components or users?

- **Extension to broader class seems out of place**: The paper provides a great in-depth explanation and theoretical and experimental support to SortUCB, but the same is missing for SortUCB-SD. The transition to the set-dependent combinatorial bandit problem feels abrupt and lacks the same level of thoroughness as the initial problem setup. The paper should provide more detailed theoretical analysis and experimental validation for SortUCB-SD, similar to what was done for SortUCB. This includes a more detailed discussion on the ($n_1, n_2$)-efficiency oracle and its impact on the performance of the algorithm.

- **A niche class of perfect lower and upper-bound matching**: The paper does attempt to explain in words how the regret bounds are tight. It might be better to phrase it as a corollary or a lemma on the small class of problems where it the upper and lower bound expressions are tight. Or is there a gap between the two fundamentals? The paper should explicitly state the conditions under which the upper and lower bounds match, and if there is a gap, quantify the gap and discuss its implications. This would provide a clearer understanding of the theoretical limitations of the proposed algorithms.

- **Experiment Replicability**: (Apologize if I missed this) I do not see any code files or URLs where I can run and verify the experimental evidence provided.

### Questions
Some questions for the authors : 

- **Pivoting paper around SD-CMAD**: Observing that SD-CMAB is the more generic version of SSD-CMAB, why did the authors not decide to pivot the entire discussion around SD-CMAB and provide SSD-CMAB as a special case with better performance?

- **Real-world datasets**: Is it possible to have more real-world dataset experiments? this connects with requirements for more practical/ real-world problem setups similar to SSD-CMAB. 

- **($n_1, n_2$)-efficiency oracle**: I can understand the need for such an oracle for comparison purposes. Is this a novel idea of the paper, or has this been used in essence in other literature? In either case, a thorough discussion on the same seems to be missing in the paper.

### Soundness
3

### Presentation
4

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
This paper proposes a new framework of combinatorial multi-armed bandits named Set-Size Dependent combinatorial multi-armed bandit (SSD-CMAB). In SSD-CMAB, the reward distribution of each base arm depends on the size of the chosen super arm. As a key assumption, there is an order preservation, which means that the order of the reward means of base arms is independent of the set size. This work shows upper and lower bounds of regret and shows that their proposed algorithm, SortUCB, is partially tight. Finally, it numerically evaluates SortUCB.

### Strengths
The problem setting seems novel since the ordinary CMAB assumes that the rewards of each base arm do not depend on the super arm. The SSD-CMAB framework can model some online advertising where the click rate for each ad will decrease when a large number of ads are shown to a user at once.

### Weaknesses
 - It seems that Algorithm 1 has some issues in computational complexity. $N_{S, t}$ maintains the number of times super arm $S$ has been selected. However, in general, the size of the set of super arms is exponentially large with respect to the number of base arms. Therefore, this algorithm potentially consumes an enormous amount of memory to maintain $\{N_{S, t}\}_{S = 1, \ldots, |\mathcal{A}|}$. In addition, finding the super arm with the highest value for (4) is a nonlinear optimization problem with combinatorial constraints, which is computationally heavy.
- In my understanding, combinatorial MAB means that there is a combinatorial structure in the set of super arms. However, SSD-CMAB defines a set of super arms as a subset of base arms whose cardinality is no more than a certain number. I am not sure if we can say this as a combinatorial structure.

### Questions
- Why is not the CTS algorithm from S. Wang et al. (ICML2018) compared with the SortUCB algorithm in the Experiments section? I believe this algorithm performs empirically well in semi-bandit problems.
- In Section 5 (about SD-CMAB), there is a notion of \emph{class} whose intuition is ambiguous. Taking the example of paths, what are the $K$ classes of paths?

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
4

### Summary
The authors introduce and study Set-Size Dependent Combinatorial Multi-Armed Bandits (SSD-CMAB) where each base arm is associated with a set of different reward distributions, and the reward distribution of each base arm depends on the set size. The authors propose the SortUCB algorithm, leveraging the order preservation property to reduce the exploration space and provide theoretical upper bound regret guarantees. Moreover, a lower bound is derived showing that SortUCB is relatively tight. Finally the authors conduct some numerical experiments, showing good performance of SortUCB.

### Strengths
The authors derive a lower bound for the studied problem.  

The authors derive a regret upper bound for the proposed SortUCB algorithm. 

The authors conduct some numerical analysis of the proposed approach.

### Weaknesses
 **Missing discussion/contrast/comparison with closely related works:**

It is fine that a related work section is put in the appendix. However, the main paper should cite related works at least briefly and then refer for detailed discussion in the appendix. Hence, closely related topics should not be omitted in the main paper.  

A very closely related research to this work are submodular bandits, which are a sort of CMAB, yet with submodular (more general) rewards. In such settings, the reward of arms indeed depends on the set (including its size and more, hence generalizing their setting). While some of these works were mentioned briefly in the Appendix A. We believe, due to its high relevance to their considered setting, it must be clearly discussed and highlighted in the paper with key differences and motivations.

Several works have been published tackling the CMAB with general rewards including semi-bandit (like this work) [1, 2] and even for (more general) bandit feedback [3]. These have to be discussed and the work should contrast their results to these works (theoretically and/or empirically). 

The authors should compare their work (at least empirically) to recent works on CMAB where arms depend on the set, such as submodular bandits. For example, given the consideration of a fixed cardinality constraint, recent algorithms, like [3] can be considered for comparison. 

[1] Chen, L., Harshaw, C., Hassani, H., & Karbasi, A.. (2018). Projection-Free Online Optimization with Stochastic Gradient: From Convexity to Submodularity. In Proceedings of the ICML.

[2] Takemori, S., Sato, M., Sonoda, T., Singh, J., & Ohkuma, T. (2020). Submodular bandit problem under multiple constraints. In Proceedings of the UAI. 

[3] Fourati, F., Quinn, C. J., Alouini, M. S., & Aggarwal, V. (2024). Combinatorial stochastic-greedy bandit. In Proceedings of the AAAI.

**Motivation:**

The proposed problem can be solved using the same CMAB frameworks which estimates the super arm reward directly but considering LM arms instead of M arms. While the problem shows a linear increase with increased constraint (L). The increase remains linear and in general L is not large. In recommender systems such a constraint is usually much smaller than M (L<<M). Furthermore, submodular bandits can be used to tackled these variable distributions base on the set. Hence, the motivation of the work remains unclear. 

**Approach limitations:** 

Assume a linear reward function and semi-bandit feedback, unlike other works which tackles non-linear and/or bandit feedback, which limits the applicability of these approaches. (Minor: the authors should be clear about this earlier in the paper, possibly from the introduction).

**Complexity Analysis Missing:**

The authors do not provide a time and space complexity analysis (even though the algorithm has three different phases, each requiring different complexities, and in some of these requires several comparisons with other arms and super-arms). 

**Numerical Analysis Limitations:**

Compare only with two benchmarks. CMAB (2015) and MPMAB (1985). Several combinatorial bandit algorithms have been suggested which includes their proposed setting as a special case, such as submodular bandits (mentioned in the above discussion). 

The number of arms remains limited. L=8 is fine, but larger M should be considered for more realistic comparison. 

Diverse synthetic and real-world datasets should be considered. With limited datasets/settings and a few considered methods it is very hard to justify the practicality and good empirical performance of the method. 


**Minors:**

There is an error in the abstract for the regret upper bound. Should be delta_L^2 based on their proposed theoretical results.  

Algorithm 1, line 11, mentions delete any base arm. However, it is unclear from where, R or B? I assume from R.

### Questions
How does the SortUCB compare, in practice, against submodular bandit works, given that they consider a variable arm distribution when selected within different sets? 

The remainder of the algorithm (UCB Phase) focuses solely on exploitation within the set A of L main arms. It is not clear why the considered subsets of A are only L^2 and not 2^L? The subsets that can be composed with L arms are 2^L. If so, the regret should be exponential with L and not quadratic!

### Soundness
2

### Presentation
2

### Contribution
2

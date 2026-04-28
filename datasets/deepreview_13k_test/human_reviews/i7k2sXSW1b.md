# Lipschitz Bandits in Optimal Space

- Decision: Accept
- Scores: 6, 6, 3, 6

## Abstract
This paper considers the Lipschitz bandit problem, where the set of arms is continuous and the expected reward is a Lipschitz function over the arm space. This problem has been extensively studied. Prior algorithms need to store the reward information of all visited arms, leading to significant memory consumption. We address this issue by introducing an algorithm named Log-space Lipschitz bandits (Log-Li), which achieves an optimal (up to logarithmic factors) regret of $\widetilde{O}\left(T^{\frac{d_z+1}{d_z+2}}\right)$ while only uses $O\left(\log T\right)$ bits of memory. Additionally, we provide a complexity analysis for this problem, demonstrating that $\Omega\left(\log T\right)$ bits of space are necessary for any algorithm to achieve the optimal regret. We also conduct numerical simulations, and the results show that our new algorithm achieves regret comparable to the state-of-the-art while reducing memory usage by orders of magnitude.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Log-space Lipschitz bandits (Log-Li) algorithm to address high memory usage in the Lipschitz bandit problem by achieving optimal regret with only O($\log T$) bits of memory. Next the paper provides a space lower bound for the Lipschitz bandit
problem showing that the algorithm is optimal in terms of both regret and space.

### Strengths
- The paper is well written - provides adequate motivation and highlights the technical challenges involved.
- To the best of my knowledge, the proofs in the main paper seem fine.
- The space complexity improvement is significant and makes the solution practical.

### Weaknesses
No major weakness.

### Questions
- This is regarding the novelty of the analysis. The authors say "Similar to prior research, Log-Li identifies and removes the undesirable region of the arm set while exploring and partitioning the remaining area". Could the authors provide references for these prior research. Further could the authors also provide more details on the novelty of the analysis, how it differs from existing analysis and where, if any have they used modifications of existing results.

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
This paper introduces a new algorithm for the Lipshitz bandit problem which uses only $O(\log T)$ bits of memory while achieving an optimal regret of $O(T^{\frac{d_{z} + 1}{d_{z} + 2}})$. It also showed that $\Omega(\log T)$ bits of space are necessary for any algorithm to achieve optimal regret. Finally, it numerically showed that the proposed algorithm is superior to an existing method in terms of regret while reducing memory usage sifnificantly.

### Strengths
The proposed algorithm named Log-Li (Log-space Lipschitz) algorithm achieves an optimal regret rate in the Lipschitz bandit problem while using a memory of $O(\log T)$ bits space. This is a significant improvement compared to other existing methods, which have to store information of $poly (T)$ arms. They also showed that using $O(\log T)$ bits is unavoidable if we want to achieve an optimal regret rate. From above, the Log-Li algorithm is optimal in terms of regret and space, which is the contribution of this paper.

### Weaknesses
- The only algorithm that is compared to the Log-Li algorithm is the A-BLiN algorithm. Even though other existing methods use poly(T) bits of memory space, I believe it is still necessary to empirically compare cumulative regret with them. 
- In line 176, Log-Li algorithm generates $(\frac{r_{h}}{r_{h + 1}})^{d}$ subcubes, which possibly consume large amount of memory.
- The log-Li algorithm has a larger cumulative regret than an existing method empirically.

[Missing citation]
- Stefan Magureanu, Richard Combes, and Alexandre Proutiere. Lipschitz Bandits: Regret Lower Bound and Optimal Algorithms. COLT2014.


[Minor comments]
- The authors should refer to the definition of $d_{z}$ in the abstract.
- Periods are missing, and upper and lower case letters are mixed inappropriately.
  - P9 Figure 2-> "The landscape of $\mu$." 
  - P10: Figure 4 "Logarithm of number of words saved by Log-Li and A-BLiN for different $\mu$."
  - Line 178:  Space between "for" and "each"
  - Lines 99, 208, 380: "theorem"-> "Theorem "

### Questions
- Related to the second weakness above, it seems Log-Li uses a large memory space when we partition the arm set (Line 176). How much memory does the algorithm consume in this procedure? Does it exceed memories than that used to store information of each arm?
- Isn't the "for loop" in Line 194 computationally heavy? In my understanding, the size of $\mathcal{B}$ is exponentially large in $d$, and therefore hurts the computational complexity of the Algorithm.

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
This paper proposed a novel algorithm, “Log-space Lipschitz bandits” (Log-Li), which reduces space complexity to $O(\log T)$ from $O(T)$ while achieving near-optimal regret, for the the Lipschitz bandit problem.

### Strengths
1. This paper proposed a novel algorithm (Log-Li), which reduces space complexity to $O(\log T)$ from $O(T)$ while achieving near-optimal regret. 

2. It shows that the regret achievable with this minimal memory is near optimal. 

3. The paper includes theoretical proofs for the space and regret bounds of the algorithm, complemented by experimental results demonstrating that Log-Li maintains regret close to other state-of-the-art algorithms but with significantly lower memory usage.

### Weaknesses
There are several weaknesses in the current manuscript. 

1. The authors acknowledge that Log-Li’s regret is higher and more variable than the benchmark algorithm A-BLiN (as shown in Fig .3) due to memory limitations, requiring repeated exploration of suboptimal regions.  This means that Log-Li cannot guarantee the regret performance if the required memory decreases.

2.  The evaluation is too weak to support the claim made in this paper. It only compares with one benchmark algorithm and the performance of the proposed Log-Li is even worse than that of the benchmark algorithm. 

3. The regret bound is highly dependent on the zooming dimension  $d_z$ . If  d_z  is large, the regret bound  $O(T^{\frac{d_z + 1}{d_z + 2}})$  grows close to linear in $ T$ , suggesting that the Log-Li algorithm may struggle with higher-dimensional spaces. The analysis would benefit from a more in-depth exploration of how the zooming dimension affects both regret and space efficiency in high-dimensional spaces.

4. The presentation of the current manuscript is extremely poor and unfriendly to readers. Though this reviewer may misunderstand the main technique and theoretical results, the poor presentation is an outstanding issue. From this reviewer's point of view, it is way below the standard.

### Questions
My detailed questions are as follows:

1. My first question is about the claimed "optimal regret" in this paper. As indicated in Weakness 3, the regret bound is almost linear with a large zoom dimension $d_z$. If this is the optimal upper bound, does it mean that no algorithm can achieve sublinear regret for Lipschitz bandit in high-dimensional spaces?

2. What is Doubling Edge-Length Sequence  $r_m$? And why do we need to set it as  $2^{-m+1}$? 

3. Corollary 1 implies that with  $K \geq 10$ , the probability of non-optimal cube selection exceeds  $\frac{1}{12} $. How would this probability scale as  $T$  grows large? Would the required cube size in terms of $K$ or arm space expand as  $T$ increases, potentially impacting the algorithm’s ability to achieve optimal regret in very high-dimensional spaces? 

4. In Lemma 2, you define the event  $E$  to bound the difference between the estimated and true expected reward. However, the analysis assumes that each cube in  $A_h^m$  has been played sufficiently to approximate rewards accurately. Could you clarify how this holds in scenarios with very large or complex arm spaces where  |$A_h^m| $  is substantial? Would the regret increase under limited play-per-cube situations, and if so, how could this impact your regret bound?

5. The paper states that Log-Li’s arm elimination rule requires revisiting previously eliminated areas. In practical terms, this leads to redundant exploration of suboptimal regions, increasing regret. Is there an analytical way to quantify the regret incurred from this repeated exploration? Could adding memory to store limited past elimination history potentially reduce these redundancies?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the problem of continuous armed bandit for a reward function which is Lipschitz over the action space. This setting is already well studied in the literature, and optimal regret guarantees are already well-known. The novelty of this work stays in proposing al algorithm which is also efficient on the point of view of the space complexity. 
In fact, the authors show both that their algorithm enjoys order $\log(T)$ space complexity (in number of bits) and that this is the lower bound for the setting.

### Strengths
The topic of the paper is very interesting. The setting is very interesting, and the space complexity is indeed a limitation of previous approaches for this setting.

The contribution is valuable, and the idea of the paper could bring an impact also outside of the bandit literature.

### Weaknesses
Despite I have really appriciated this work, which I think brings a valuable contribution to the bandit community, I am also convinced that this is a little bit immature for a publication at this conference.

I have reached this conlusion after reading many passages of the paper which, in my opinion, need to be deepened.
For example,
 1. In Theorem 1, the result seems to hold with a probability of $1-T^{-5}$. I was rather surprised about this, as most of the other regret bounds in this field fix a given $\delta>0$ and show that the regret is bounded by some function of $T$ multiplied by $\sqrt{\log(1/\delta)}$. At first, I tought this was because the authors were using some given technique which goes outside from usual concentration bounds used in the bandit literature. But in fact, looking at the proof of the result, it seems to me that the proof could be adapted to hold with high probability, as usual. Even if the result is correct, putting the statement in this form could affect the possibility of using this result for future work, and create confusion.
 2. The paper assumes that all arms distribution are Gaussian, even if this assumption is never used except at line 263, where in fact only _subgaussianity_ is used. Again, introducing this (very restrictive) assumption without a reason creates unnecessary confusion in anybody needing to use the results of this paper.
 3. Line 277 "By similar argument to Lemma F.1 in Sinclair et al. (2020) and Lemma 1 in Lu et al. (2019), taking a union bound over C ∈ Amh
and 1 ≤ h ≤ m ≤ Bstop finishes the proof" is not sufficiently precise to be used in a proof
 4. The proof of the space complexity bound seems to ignore the fact that the algorithm has also (according to line 192) to allocate the subcubes and to remember which of theme have already been visitied. By the way the pseudocode is written this seems to take order $2^d$ bits, and it is not clear if it can be done in less space.

In the end, I am not against the acceptance of this work, but I'm wondering if it is in the interest of the author to publish it like this or if it is better to clarify and improve the mentioned passages.

### Questions
1. Indeed, to achieve a regret bound of order $T^\alpha$ for any bandit setting, one has to be able to allocate numbers with a precision of at least $T^{\alpha-1}$, as a larger misspecification would compromise the regret bound. This already takes $O(\log(T))$ bits. Does it make the lower bound for the space complexity trivial?

### Soundness
2

### Presentation
3

### Contribution
3

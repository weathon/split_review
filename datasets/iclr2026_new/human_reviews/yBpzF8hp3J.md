## Human Reviewer 1

### Summary
This paper studies differentially private domain discovery, where each user holds a subset of items from an unknown shared domain, and the goal is to output an informative subset while preserving privacy. The authors revisit the Weighted Gaussian Mechanism (WGM) and show that, when utility is measured in terms of missing mass (the fraction of unrecovered probability mass rather than set cardinality), WGM achieves strong and in some cases near-optimal guarantees.

Key contributions include:

1. Reformulating the DP set union problem in terms of mass instead of cardinality, and proving that WGM achieves near-optimal ℓ1 missing mass on Zipfian data, and a distribution-free  ℓ∞ missing mass bound.
2. Extending the analysis to unknown-domain variants of top-k and k-hitting set, showing new utility guarantees by using WGM as a preprocessing step.
3. Conducting experiments on six real-world datasets, demonstrating that WGM-based methods outperform existing baselines in accuracy and scalability.

### Strengths
1.  **Originality**: Reformulating domain discovery in terms of missing mass provides a novel and tractable utility metric.
2.  **Quality**: The analysis is rigorous, with clear theorems and well-motivated assumptions. The near-optimal ℓ1 and distribution-free ℓ∞ guarantees add strong theoretical credibility.
3.  **Clarity**: Well-written, clear notation, and logically structured.
4.  **Significance**: The results contribute a unified framework for private domain discovery, potentially influencing future research in private data analytics and unknown-domain learning.

### Weaknesses
1.  The Zipfian assumption may restrict generality; robustness under other distributions is not fully discussed.
2.  Section 6 outlines directions but lacks concrete proposals (e.g., how adaptive subsampling might integrate into WGM).

### Questions
1.  How does WGM perform on non-Zipfian or adversarial data?
2.  How does the mechanism perform under correlated user data?
3.  Does adding Gaussian noise per element remain efficient when domain size is very large?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper studies the problem of discovering items from an unknown domain in a *differentially private* manner, under a user-level privacy guarantee.  

The main technical tool is the Weighted Gaussian Mechanism (WGM) (Gopi et al., 2020), which operates as follows:  
1. It builds a histogram over items held by all clients, normalizing each user’s contribution so that its $\ell_2$-norm is bounded by $1$.  
2. It adds Gaussian noise to the non-zero entries of the histogram.  
3. It applies a thresholding step to remove low-frequency items.  

The paper analyzes the performance of WGM under two error metrics—the $\ell_1$ and $\ell_\infty$ norms of the *missing mass*—where the analysis for the $\ell_1$ case assumes a Zipfian distribution over the domain.  

Finally, the authors extend their approach to the top-$k$ discovery and $k$-hitting set problems, and provide empirical evaluations demonstrating the effectiveness of their method.

### Strengths
The problem studied and the proposed error metrics are interesting.  

It is also good to see a systematic and thorough investigation of this topic, which helps clarify the behavior of differentially private item discovery mechanisms under various conditions.

### Weaknesses
1. Some key related works are missing and should be discussed.

2. The motivation and interpretation of the experimental design are less clear:
   * It is unclear whether the datasets used in the experiments are justified to follow the Zipfian distribution assumed in the analysis—particularly for parameters $s > 1$ (and not even $s = 1$).
  
   * It would be helpful to clarify whether the key theoretical results, such as **Theorem 3.3** and **Corollary 3.4**, are empirically validated in the experiments.

### Questions
1. It would be helpful to clarify whether the error metrics defined in **Definition 2.2** are newly proposed in this paper or have appeared in prior work. 
   If they are not novel, please include appropriate citations to previous literature.

2. The asymptotic upper and lower bounds for differentially private top-$k$ selection are already well studied. For instance:  
   * Bafna, Mitali, and Jonathan Ullman. *“The Price of Selection in Differential Privacy.”* In *Conference on Learning Theory*, pp. 151–168. PMLR, 2017.  
   * Steinke, Thomas, and Jonathan Ullman. *“Tight Lower Bounds for Differentially Private Selection.”* In *FOCS 2017*, pp. 552–563. IEEE, 2017.  

   It is known that the cumulative gap of $\tilde{O}(k^{3/2})$ between the true and selected top-$k$ scores is tight. 
   Therefore, it may not be necessary to  
   * re-prove **Lemma 4.2**, or  
   * include **Corollary 4.4**, whose lower bound is not tight.  

3. The citation for **Lemma 4.1** appears to be inaccurate.
   The equivalence between adding Gumbel noise and iteratively applying the exponential mechanism (without replacement) was shown as early as Durfee & Rogers, NeurIPS 2019.
   Moreover, their updated arXiv version (see footnote on p.11 of [arXiv:1905.4273](https://arxiv.org/pdf/1905.4273)) acknowledges that this technique was proposed even earlier.

4. In **Theorem 3.2**, it would be clearer to express $T$ in $\Theta$-notation rather than $\tilde{\Theta}$-notation, since  
   (1) $\sigma$ is already expressed in $\Theta$-notation, and  
   (2) it would make the asymptotic behavior of $T$ easier to interpret.

5. The text in **Figures 1–3** is too small to read when printed. Please consider increasing the font size for readability.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper studies several questions about user-level differentially private (DP) algorithms on an unknown domain. The dataset consists of users, each with a subset $W_i$ of items from an unknown (or enormous) universe $\mathcal{X}$ and the goal is to output a set $S$ with large overlap with the union $\bigcup_i W_i$ while maintaining DP with respect to adding/removing any given subset $W_i$. For instance, in the set union problem, the goal is to output $S$ which is a subset of the union with as large cardinality as possible. Unfortunately, for this problem, there are no known absolute utility bounds: prior works can compare algorithms but have no guarantees on the size of the output. This paper investigates a relaxed objective which is missing mass. Consider the empirical distribution over the universe given by the input dataset (the multiset union of all $W_i$) and call this vector $f$. The missing mass is defined as the $\ell_1$ norm of $ f_{\mathcal{X} \setminus S}$, the fraction of elements not contained in $S$. The authors note that $\ell_0$ norm is the normal private set union objective and the $\ell_p$ missing mass for $p > 1$ may also be of interest.

The first main result is about set union with $\ell_1$ missing mass. The authors show that the standard weighted Gaussian mechanism (WGM) from prior work achieves a missing mass guarantee if the item frequencies $f$ follow a power law (Zipfian distribution). With a Zipfian exponent $s$, a simplified version of the bound is $\tilde{O}\left(\left(\frac{\max_i |W_i|}{\epsilon N \sqrt{\Delta_0}}\right)^{(s-1)/s}\right)$ where $\Delta_0$ is the standard "contribution cap": in a preprocessing step, each $W_i$ is subsampled to keep only $\Delta_0$ elements.
Furthermore, the authors show that the $\left(\frac{1}{\epsilon N}\right)^{(s-1)/s}$ dependence is necessary for any private algorithm.
The authors show a simpler result on the $\ell_\infty$ missing mass without any Zipfian assumptions. This amounts to showing that there is a frequency threshold, above which, any item will be returned by WGM.

The authors show how to use the $\ell_\infty$ analysis to get utility bounds for top-$k$ selection and $k$-hitting set on unknown (very large) domains by first applying set union and then running a known domain algorithm. They use the $\ell_\infty$ missing mass bound from set union to get missing mass type utility bounds for top-$k$ and approximation algorithm bounds for $k$-hitting set.

### Strengths
- Achieving absolute utility bounds for private set union has been a challenge in the existing literature. By relaxing the objective to missing mass as opposed to just the cardinality of $S$ as well as introducing an assumption on the frequency distribution, the authors obtain absolute bounds on the utility of the standard WGM algorithm.

- The upper and lower bounds on Zipfian data show that different algorithmic ideas cannot significantly improve upon the basic WGM algorithm in this setting (at least in terms of missing mass).

- The authors show how these bounds can be translated to problems where set union can be used as a subroutine for the top-$k$ and $k$-hitting set problems.

- One interesting facet of the theoretical analysis is that the preprocessing step, where sets $W_i$ are subsampled to have a maximum cardinality cap, is an important factor in the bounds. In prior studies of private set union, the details of step are not thoroughly investigated.

### Weaknesses
An asymptotic bound on the missing mass of a mechanism in a specific setting would be more useful if it had implications in practice either by predicting practical performance in parameter settings or by allowing different algorithms to be compared theoretically.

- The experimental results could be significantly more in depth: this would highlight several aspects of the theoretical work. Some concrete suggestions:
  - It would be instructive to compare the theoretical error bound against empirical performance on synthetic Zipfian data.
  - It would be useful to plot the frequency distribution on the real datasets to see if they follow a power law.
  - Reporting the size distribution of $|W_i|$ would be interesting to compare the setting of $\Delta_0$ to those statistics. The theoretical result suggests that $\Delta_0$ should be set to $\max |W_i|$ though increasing $\Delta_0$ worsens performance for the Amazon games dataset and the small datasets. Is this because $\Delta_0$ has exceeded the size of any $W_i$ or for another reason?
- The statement that the gap between WGM and the policy baselines is smaller in the missing mass case compared to the $\ell_0$ cardinality case is misleading. While the gap is 5 percentage points (MM is measured as a percentage), WGM performs up to 50% worse than the baselines in some instances when measured as a ratio. This is the apples-to-apples comparison to make when commenting that "for cardinality... sequential methods often output $\approx 2X$ more items [than WGM]."
- Comparison to more baseline algorithms would also be interesting. In the theoretical results, it is very reasonable to only analyze WGM as it is a well-studied algorithm and other candidate algorithms may be very difficult to analyze. On the other hand, if an important empirical takeaway is that "WGM obtains MM within 5% of that of the policy mechanisms, in spite of their significantly more intensive computation," it would be useful to compare to other methods of Swanberg et al. and Chen et al. which offer better cardinality results while still using a similar amount of computation to WGM.
- Missing mass analysis of any other algorithm, for example the weighted Laplace mechanism to start, would be interesting.

### Questions
- Consider the statement "Note that in Theorem 3.3 the missing mass decays as the total number of items N grows. Moreover, as C decreases or s increases, the upper bound on missing mass decreases." Should the second sentence be conditional on $N$ being sufficiently large compared to $T$ and $\sigma$ (which should be the case for reasonable privacy parameter settings).

- An interesting direction would be to show that WGM is close to optimal on Zipfian data for all $\ell_p$ missing mass for $p > 1$. Is there any chance of showing something like this? Similarly, plotting missing mass as $p$ increases would be interesting, especially if the plots were significantly different for different algorithms.

- Are both changes of (1) considering missing mass and (2) Zipfian data necessary for giving an absolute utility guarantee? Is there a specific technical challenge to analyzing the cardinality of the set output by WGM on Zipfian data?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper studies several problems in differentially private domain discovery, such as missing mass, top-k selection, and k-hitting set. The authors show that the weighted Gaussian mechanism is useful for these problems. The authors also prove utility lower bounds, showing the algorithm enjoys some level of optimality. The algorithm is tested on several real-world datasets.

### Strengths
1. The proposed algorithms based on the weighted Gaussian mechanism are generally applicable to many problems for domain discovery, including finding a set of elements with small missing mass, top-k selection,and k-hitting set.
2. The lower bound results demonstrate that the algorithms are optimal to some extent. For the missing mass problem, the algorithm achieves near-optimal error in terms of privacy parameter $\epsilon$ and total number of items $N$. For top-k selection and k-hitting set, the lower bound is at least $k/\epsilon$, while the upper bounds have an additional $k^{3/2}/\epsilon$ term, 
3. Experiments are performed on many real-world datasets, and the performance is comparable or better than previous baseline algorithms.

### Weaknesses
1. It seems that the performance of the algorithm depends on the choice of user contribution $\Delta_0$, which ideally has to be close to $\max_|W_i|$. This requires prior knowledge of the maximum elements, or at least some estimate of the parameter of the Zipf distribution of the underlying dataset.
2. There is a mismatch in the upper and lower bounds for top-k selection and k-hitting set.

### Questions
1. If a good bound on $\max_|W_i|$ or the $s$ parameter of the Zipf distribution is not known a priori, is there a good way to privately find a good $\Delta_0$ for the WGM mechanism?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3
# Avoiding Pitfalls for Privacy Accounting of Subsampled Mechanisms under Composition

- Decision: Reject
- Scores: 3, 6, 8, 3

## Abstract
We consider the problem of computing tight privacy guarantees for the composition of subsampled differentially private mechanisms.
    Recent algorithms can numerically compute the privacy parameters to arbitrary precision but must be carefully applied.

    Our main contribution is to address two common points of confusion.
    First, some privacy accountants assume that the privacy guarantees for the composition of a subsampled mechanism are determined by self-composing the worst-case datasets for the uncomposed mechanism. 
    We show that this is not true in general.
    Second, Poisson subsampling is sometimes assumed to have similar privacy guarantees compared to sampling without replacement.
    We show that the privacy guarantees may in fact differ significantly between the two sampling schemes.
    In particular, we give an example of hyperparameters that result in $\varepsilon \approx 1$ for Poisson subsampling and $\varepsilon > 10$ for sampling without replacement. 
    This occurs for some parameters that could realistically be chosen for DP-SGD.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper exposes several cases where mismatches between privacy accounting and its implementation gives incorrect results. The authors show that the noise required to achieve a certain privacy guarantee can differ significantly between Poisson sampling and sampling without replacement; and that the worst-case dataset for a single iteration of a subsampled mechanism might give incorrect results for the composed mechanism. They also demonstrate issues with computing tight DP bounds under the substitution relation of neighboring datasets.

### Strengths
The paper’s findings could be highly impactful on the practice of privacy accounting, as they demonstrate that a method’s implementation should match its accounting. The paper also includes a good call-to-action on how these issues can be addressed by DP practitioners. And despite this paper being about pointing out mistakes in other works, the authors of the paper are tactful and include some interesting discussions in the paper.

### Weaknesses
While I think this paper has a powerful message, there are issues with presentation / rigor which make me question whether it’s ready for publication. For example, Proposition 11 is proved by a picture (Figure 1). I also feel that it’s hard to follow the discussion in Section 7 because the counterexample is for something that is stated without any great formality.

The paper is also a bit sparse (there is no appendix). I would have liked to see more substance. The paper does in my opinion do something very important, but in its current state I don't feel it has the solidity of an ICLR paper.

### Questions
In Theorem 10, I think there is a bit of a typo: $(1 - \gamma)P + Q$ should be $(1 - \gamma)P + \gamma Q$.

The proof of Proposition 9 seems to take for granted that we know the dominating pair for the Gaussian mechanism! But I think this should be stated formally somewhere as otherwise the “Now, from Theorem 10 we know that…” sentence is unclear.

Combining the plot and the table into a single Figure 3 seems a bit ambitious. At first glance I thought that they were related somehow, and only after reading the caption realized that they were not. I think it would be clearer to separate them into different figures.

The plot in Figure 3 could maybe also be split into two plots? It is a little hard to see the takeaways as is. It might be nice to have one plot showing Poisson for $\epsilon \in [1, 2, 5, 10]$ (to illustrate the “two regions” of high / low sampling rate) and another plot showing Poisson + WOR for $\epsilon=10$ (to illustrate the “hinge”).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies privacy accounting for compositions of subsampled DP mechanisms. The authors show that a pair of worst-case datasets for a subsampled mechanism may no longer be a worst-case after composition, and privacy accounting can be very different for different sub-sampling strategies. These findings call for more care when applying privacy accounting in practice.

### Strengths
1. Privacy accounting of DP is an important problem when applying differential privacy in practice.
2. The findings have important practical implications and help to avoid unintended privacy leakage.
3. The theoretical construction of the bad cases is solid. 
4. The presentation is clear and easy to follow.

### Weaknesses
1. The authors did not provide a viable technical solution for dealing with the worst-case dataset problem under replacement DP.
2. While constructing the bad cases on lower dimensional datasets is sufficient to demonstrate the claims, it would be nice to include empirical results on more realistic datasets to show that these pitfalls can actually appear in practice.

### Questions
For replacement DP, is there a good way to find a good approximation of privacy curves when the exact worst-case dataset is hard to obtain?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper clarifies common problems with privacy accounting. In particular, the paper shows that rigorous privacy accounting is affected by the method of sampling batches (Poisson subsampling or sampling without replacement). The paper also shows that self-composing worse-case datasets for the uncomposed mechanism is not in general valid.

### Strengths
The paper provides some novel theoretical results that develop our understanding of composition and subsampling with DP. I believe with small presentational edits (see weaknesses), this paper could serve as an important reference work for future research on subsampling with DP, as well as DP practitioners. 

In general, the presentation is very clear and the authors on the whole provide welcome intuition to support the mathematical results.

### Weaknesses
I am concerned that the paper presents somewhat of a straw-man (e.g. the two points of 'common' confusion in the abstract). It would be useful to provide evidence (even something anecdotal
) that these are common pitfalls in practice. This would make the overall contribution of the paper much more convincing.  

The two recommendations for practitioners in the discussion section are welcome but I believe spelling out the implications of this work for practitioners (who will not read through the theory in detail) merits an entire section of the paper, and would enhance its practical utility and potential impact. 

Definitions 3-5 would each benefit from a one sentence explanation for those less familiar with the prior research.

### Questions
It would be interesting to understand whether empirical privacy (e.g. measured via auditing/MIA) of Poisson subsampling and sampling with replacement differs as much as the theoretical analysis implies (e.g. epsilon =1 vs 10!). Do you have priors about this?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses potential pitfalls when using so called numerical privacy accounting to compute the $(\varepsilon,\delta)$-guarantees for compositions of DP algorithms. Especially, the paper focuses on two points (citations from the paper):

a) "some privacy accountants assume that the privacy guarantees for the composition of a subsampled mechanism are determined by self-composing the worst-case datasets for the uncomposed mechanism" 

and 

b) "Poisson subsampling is sometimes assumed to have similar privacy guarantees compared to sampling without replacement."


Some background: Using the Rényi divergence has been a popular way of analysing compositions of DP mechanisms since the works of Abadi et al. (2016) and Mironov (2017), especially due to the tightness of the RDP accounting compared to purely analytical approaches. So called numerical accounting and was proposed in works by Sommer et al. (2019), Koskela et al. (2020) and Gopi et al. (2021). It directly approximates the hockey-stick divergence and often gives tighter bounds than the RDP approach which incurs a small loss when converting the RDP parameters to $(\varepsilon,\delta)$-bounds. Zhu et al. (AISTATS 2022, https://proceedings.mlr.press/v151/zhu22c/zhu22c.pdf) set the hockey-stick divergence based methods on a more rigorous footing by introducing the concept of dominating pairs of distributions. This also allows obtaining rigorous $(\varepsilon,\delta)$-bounds for adaptive compositions of DP mechanisms.

### Strengths
Generally well-written paper and a timely topic. The auditing methods are getting all the time more accurate at estimating the $\varepsilon$-values, so it would be good to get the accurate computing of the formal guarantees right. It seems there are still no clear subsampling amplification result in the literature for, e.g., carrying out accounting using the dominating pairs of distributions in case of substitution neighbourhood relation of datasets (related to the “second pitfall”), so it makes sense to consider this problem.

### Weaknesses
All in all, I think the contribution of the paper is very limited. And I think the paper is outdated in a sense that neither of the mentioned issues are actually pitfalls in numerical accounting (explained below).

About the pitfalls:

The point a) was addressed by the work of Zhu et al. (2022) which considers the dominating pairs of distributions. As the authors point out, generally there are no neighboring datasets $X$ and $Y$ such that the $(\varepsilon,\delta)$-bound for pairs of outcomes $\big(\mathcal{M}(X),\mathcal{M}(Y)\big)$ would be $(\varepsilon,\delta)$-bounds for all neighboring datasets. Outside of the mechanisms that use additive Gaussian noise, there are numerous such examples. Consider, e.g., the exponential mechanism, for which obtaining accurate $(\varepsilon,\delta)$-bounds is very tedious:

Dong, J., Durfee, D., & Rogers, R. (2020, November). Optimal differential privacy composition for exponential mechanisms. In International Conference on Machine Learning (pp. 2597-2606). PMLR.

The issue that you don't have a worst-case pair of datasets is exactly what the definition of the dominating pairs of distribution addresses. Also, Zhu et al. (2022) also show that a tightly dominating pair distributions always exists for a given mechanism.

For the pitfall b) I agree that the claim that the pair of distributions $P = q \cdot \mathcal{N}(1,\sigma^2) + (1-q) \cdot \mathcal{N}(0,\sigma^2)$, $Q = q \cdot \mathcal{N}(-1,\sigma^2) + (1-q) \cdot \mathcal{N}(0,\sigma^2)$ gives a dominating pair of distributions in case of subsampling without replacement and substitute neighbourhood relation of datasets is not correct. I believe it is true for the Poisson subsampling in case of substitute neighbourhood relation of datasets, I think you can show this as in case of the Rényi divergence and use the analysis for the Poisson subsampling and add/remove neighborhood relation of datasets, which is given in

Mironov, I., Talwar, K., & Zhang, L. (2019). R\'enyi differential privacy of the sampled gaussian mechanism. arXiv preprint arXiv:1908.10530.

The correct bound for hockey-stick divergence in the case of subsampling without replacement and substitute neighbourhood relation of datasets is given in Proposition 30 by Zhu et al. (2022). So, as far as I see, this problem is solved, and in the most well-known software libraries that use numerical accounting and dominating pairs of distributions, namely the "autodp" by Wang et al. and "PRV accountant" by Gopi et al., Opacus and Google DP library, correct formulas are used.

I think that the claim that "Poisson subsampling is sometimes assumed to have similar privacy guarantees compared to sampling without replacement" is not true in that Proposition 30 by Zhu et al. (2022) gives bounds for both. And they are of the same form, but in of them the pair $(P,Q)$ is a dominating pair under the add/remove relation and in the other one under the substitute relation, so it is clear that the latter leads to higher $\varepsilon$-values. The bounds are in two parts and one can determine a numerical dominating pair of distributions using, e.g, methods by

Doroshenko, V., Ghazi, B., Kamath, P., Kumar, R., & Manurangsi, P. (2022). Connect the Dots: Tighter Discrete Approximations of Privacy Loss Distributions. Proceedings on Privacy Enhancing Technologies, 4, 552-570.

Ps. it seems that the worst-case data set in that Laplace example dominates for $\varepsilon \geq 0$ whereas there should be dominance for all $\varepsilon \in \mathbb{R}$ for using the composition result.

Still getting back to this:

> Due to the privacy scaling under the RDP composition theorem, it is sufficient to find the worst-case datasets for only a single iteration when using the RDP accountant. One could use a similar approach for hockey-stick divergence by computing a single (ε, δ)-DP guarantee and applying the advanced composition theorem. However, (ε, δ)-DP guarantees do not compose as well as the RDP guarantee. Therefore, the problem of determining the worst-case datasets under composition only seems to arise for exact accountants.

I believe that different RDP orders could have different worst-case pairs of datasets, similarly as you might not have a worst-case pair for the hockey-stick divergence. To get the benefit out of RDP accounting, one should keep track of several RDP orders. Often the dominating pairs of distributions are obtained by some post-processing (consider e.g. additive Laplace or Gaussian noise), and the resulting pair is a dominating pair for both Rényi and HS divergence, and often this pair is even tight in sense that it exactly gives the divergence of the mechanism evaluated on different dataset pairs (e.g., Gaussian mechanism). If we don't have a worst-case pair of datasets (consider, e.g., the exponential mechanism) but want to find tight bounds for a given divergence, I think one encounters difficulties both with Rényi and HS divergence based accounting.

(By the way, I would rather use the term numerical accounting than exact accounting when talking about the HS divergence based approach.)

> even a simple mechanism that has a worst-case pair of datasets might not have a worst-case pair of datasets under subsampling and composition.

Thinking about this, I believe that the same pair of datasets would be the worst-case pair for compositions as well as for a single call of the mechanism (at least for non-adaptive compositions, I don't think we can expect to find worst-case pairs of datasets for adaptive compositions in general). For subsampling, again, the possible difficulties when trying to find the worst-case dataset pairs would be shared by other accounting methods such as the RDP, I think.

I also share the criticism with reviewer dGjF in that Figure 1 should not be used as a proof (Proposition 11). I also think that the example with Laplace noise is a bit difficult to follow, some more formal derivation e.g. in the appendix would have helped (I suppose that could be even dealt analytically).

I think the paper has some interesting points, but still needs more work. Some constructive results would definitely strengthen the paper.

Thank you for the reply.

> Our example with the Laplace mechanism simply shows that even a simple mechanism that has a worst-case pair of datasets might not have a worst-case pair of datasets under subsampling and composition. 

I still don't fully understand why would one want to find the worst-case pair of datasets. I think it is clear that one has to consider a bound that holds for all pairs of datasets.

> You are correct that Zhu et al. give a construction of a dominating pair of distributions in Corollary 32. However, there is no implementation of this construction to the best of our knowledge.

Such a construction can also be found in "Doroshenko et al. (2022). Connect the Dots: Tighter Discrete Approximations of Privacy Loss Distributions. Proceedings on Privacy Enhancing Technologies." and it is a fairly simple algorithm. But I agree this should be addressed more thoroughly.

> Regarding implementations of accountants for the subsampled Gaussian mechanism: the “PRV accountant”/Opacus (and PLD Accountant) only computes the “remove” relation. The “autodp” and Google DP library correctly computes both the “add” and “remove” relations and takes the point-wise maximum, as in Theorem 11 of Zhu et al. 

That is an interesting observation (and perhaps someone should tell the authors), but I don't think these findings make a sufficient contribution for a paper.

> As mentioned in our response to Reviewer LTUo we conjecture that in the case of the Gaussian mechanism, it is sufficient to consider the “remove” datasets for subsampling without replacement under the substitution relation.

I think proving this (even if it holds only for the Gaussian mechanism) would strengthen the paper. 

> The privacy parameters are not assumed to be identical. However, the privacy parameters are sometimes assumed to be close as is the case between the add/remove and substitution neighboring relations. We base this claim on the fact that accountants for Poisson subsampling are often used when it is not the implemented sampling scheme.

It indeed seems to be the case that the accountants for Poisson subsampling (with remove/add neighbourhood relation) are often used when they shouldn't be. And I think the same often happens in case of RDP accountants. Anyhow, I think the differences between neighbourhood relations and sampling schemes are correctly reflected in the results of Zhu et al. (2022). I think it would be interesting to see what are (as tight as possible) dominating pairs (either numerical or analytical) in various cases.

> The RDP accountant computes the RDP guarantees of a single iteration for a given order and then applies the RDP composition theorem.

As far as I understand, the RDP accountants commonly compute the RDP guarantees for several orders and then convert the RDP-epsilons of different orders to approximate DP-guarantees using some conversion rule. 

> Due to the privacy scaling under the RDP composition theorem, it is sufficient to find the worst-case datasets for only a single iteration when using the RDP accountant. One could use a similar approach for hockey-stick divergence by computing a single (ε, δ)-DP guarantee and applying the advanced composition theorem. However, (ε, δ)-DP guarantees do not compose as well as the RDP guarantee. Therefore, the problem of determining the worst-case datasets under composition only seems to arise for exact accountants.

I don't exactly follow here. If we want to have an accurate RDP accountant, we would need to have RDP bounds for several RDP orders (the conversion in the end).

All in all I think the topic is actual and the subtleties of hockey stick vs. Rényi divergence based accountants haven't been fully addressed, but this paper does not really propose any solutions and also I think the criticism is not sharp enough to make for a paper.

### Questions
- What is special about the hockey stick divergence when thinking about the worst-case pairs of datasets and worst-case pairs of distributions? All the potential problems w.r.t. to finding the worst-case pair of distributions for the hockey-stick divergence would be problems for RDP accounting (or when using other $f$-divergences than the $\alpha$-divergence) as well, right? Commonly the worst-case pairs of distributions are 1-dimensional and can be seen as some sort of general post-processing of the outcomes from neighboring datasets, and then the worst-case distributions for the hockey-stick divergence would similarly be worst-case distributions for other $f$-divergences and for the Rényi divergence as they satisfy the data-processing inequality.

- Comment: it would be interesting to see some new results related to this topic, e.g., on how would the analytically expressed pair of dominating distributions look like under the subsampling amplification (in all cases) as the bounds of Proposition 30 by Zhu et al. (2022) (which you also cite) are given in two parts.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

# Online learning meets Adam: The Road of Interpretable Adaptive Optimizer Design

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 6, 3

## Abstract
This paper explores the theoretical foundations of Adam, a widely used adaptive optimizer. Building on recent developments in non-convex optimization and online learning, particularly the discounted-to-nonconvex conversion framework, we present two aspects of results: First, we introduce clip-free FTRL, a novel variant of the classical Follow-the-Regularized-Leader (FTRL) algorithm. Unlike scale-free FTRL and the recently proposed $\beta$-FTRL, our clip-free variant eliminates the need for clipping operations, aligning more closely with Adam's practical implementation. This modification provides deeper theoretical insights into Adam's empirical success and aligns the theoretical framework with practical implementations. By incorporating a refined analysis, our second result establishes a theoretical guarantee for the Last Iterate Convergence (LIC) under the proposed discounts-to-nonconvex conversion algorithm in LIC, which differs from the previous guarantee that has convergence evenly distributed in all iterations. Additionally, we extend this result to provide the last iterate convergence guarantee for the popular $\beta$-FTRL algorithm under the same framework. However, the derived last iterate convergence of $\beta$-FTRL reveals a persistent fixed error, potentially suggesting either limitations in popular online learning methods or the need for additional assumptions about the objective function.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies how to interoperate the Adam algorithm with discounted online learning algorithms. The authors propose an online learning algorithm that does not need the projection operation, which aligning more closely with Adam’s practical implementation. They also provide last iterate convergence guarantees for the $\beta$-FTRL algorithm, but with a non-diminishing error.

### Strengths
1. This paper studies the online learning interpretation of the Adam algorithm, which is a interesting topic. Previous interpretation (Ahn & Cutkosky, 2024) requires the clipping (projection) operation, where this paper propose to avoid this operation via a careful configurations of $\beta$, which looks like a novel contribution.  

2. The authors also provide a last iterate convergence guarantee the $\beta$-FTRL alorithm, which is a interesting result.

### Weaknesses
I have the following **major** doubts/questions:

In terms of $\beta_2$ and $\beta$: In the proof, it seems that $\beta_2$ and $\beta$ are considered as a fixed constant. However, in the Key Lemma (4.1), both $\beta_2$ and $\beta$ are time variant parameters. It leads to the following questions about the parameter $a$:  1) it seems that $a$ depend on the algorithm it self (line 292). Therefore, it is unclear to me how to find a universal $a$ to make sure such an inequality holds. It we use different $a$ at different rounds, can the proof still hold? will $\beta$ be monotone? what is the scale of a and beta? Specifically, the relationship between the time-varying nature of $\beta_2$ in Lemma 4.1 and its treatment as a constant in later proofs needs to be rigorously justified. The current presentation lacks clarity on how these two perspectives reconcile, raising concerns about the validity of the derived bounds. Furthermore, the dependence of $a$ on the algorithm itself, as indicated in line 292, introduces a circularity that needs to be addressed. A clear, non-circular definition of $a$ is crucial for the proof to be considered sound.

Line 698: $1-\beta_2^{t-1}=1/(a(t-1))$: **why is it true?** we know $\beta_2=(1-1/(a(t-1)))^{t-1}$, so $1/(a(t-1))$ should equal to $1-\beta^{1/(t-1)}_2$.  $1-\beta^{1/(t-1)}_2$ and $1-\beta_2^{t-1}$ are totally different. The stated equality at line 698 appears to be a significant error, as the correct relationship between $\beta_2$ and $a$ involves the $(t-1)$-th root, not a simple exponentiation. This discrepancy undermines the subsequent analysis and requires a thorough correction. The implications of this error on the final convergence results must be carefully re-evaluated.

Since the setting of $\beta$ is critical for achieving clip-free, I believe understanding the points mentioned above are very important to make sure the proof is rigorous.

Question on the theoretical guarantees: In Theorem 4.2, what is the dependance on $\eta$? Does $v_t$ has an upper bound?

Other comments/questions: 

Presentation: As mentioned above, I think the parameter setting is very unclear to me, and I hope the authors could provide more explanations.

### Questions
Please see the Weakness section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides an analysis of non-smooth non-convex optimization that fixes some undesirable properties of previous work in an effort to be closer to the empirically successful adam algorithm. Specifically, some recent prior work developed a similarity between certain online learning algorithms and adam using an “online to non-convex conversion”. These algorithms made use of a strange “clipping” operation - essentially clipping the adam update to some fixed diameter $D$. Moreover, the convergence to critical points is provided only for a random iterate rather than perhaps the more desirable last iterate. This paper attempts to fix both issues.

### Strengths
The approach is intuitive, and the problem is interesting. I think if the weaknesses below could be addressed I would raise my score.

### Weaknesses
I have some concerns about the correctness of the results.

Lemma 4.1: the selection of $a$ seems to be impossible in general. Why should I expect to be able to do this? If any stochastic gradient happens to be zero (i.e. imagine your final loss is a hinge-loss and you happened to have a large margin on some example), then clearly $a$ must now be $\infty$. However, $a=\infty$ derails the analysis as it forces us to move to a non-discounted regime. Moreover, this issue is not just for zero gradients, but also for gradients that are very small, say $O(1/T)$. The proposed fix of skipping updates when the gradient is zero does not resolve this issue, as it does not address the case of small but non-zero gradients. This could be addressed by adding noise or a threshold, but this would destroy adaptivity.

In Theorem 4.2 there is also a significant issue I think: it looks to me that the actual result should be $\sqrt{1-\beta_2}$ rather than $1-\beta_2$ in the numerator. Notice in line 867 to 870 in the proof it appears that the definition $\tilde{\tilde{v}}$ was applied incorrectly to get a $1-\beta_2$ outside the square root rather than inside.

In general, we should be expect this change even without looking at the proof for a mistake: notice that in the “natural” setting where $\beta_2=\beta^2$, the “correct” value for the FTRL regularizer would be $D/\sqrt{(1-\beta)^2\sum_{t=1}^T \beta_2^{T-t} v_t^2}$ for losses $(1-\beta)\beta^{T-t} v_t$. Since the provided regularizer is off by a factor $\sqrt{1-\beta}$, we should expect that to show up in the regret bound.

Regarding the last-iterate guarantee: I do not understand how it is a last-iterate guarantee. The theoretical results seem to be about still a randomly selected iterate (although admittedly with more weight on the last iterate). This still requires randomization over all iterates though, not what I usually think of when people say a last-iterate guarantee.

I also have concerns about the final bound in Theorem 5.3. It is not clear that the gradient norm goes to zero as $T \to \infty$, which would be necessary to show convergence to critical points. Specifically, with $\beta = 1 - 1/T$, we would likely need $\beta_2 \ge 1 - O(1/T)$ as well. This would cause the term $\frac{(1-\beta)^2 T}{(1-\beta^T)}\beta D\text{Regret}$ to not decay with $T$, as it would have decayed with $1-\beta_2$ rather than $\sqrt{1-\beta_2}$ in the numerator of the regret bound.

Mild stylistic comment on the proofs: there is a lot of use of $\rightarrow$ here, but I don’t know what this means. If you mean the standard "implies" $\implies$ arrow, then it is not correct since in many of these cases all the should then be pointing the other way since these arguments are often being used to prove the initial statement, not the final statement. As it is, I just completely ignored these arrows, and I recommend they be removed and/or possibly replaced with better explanation of the logic in appropriate cases.

Also, “it is equal to verify” is not proper grammar - try instead “it suffices to verify”.

### Questions
Can the issues in the proof or the last iterate guarantee be fixed?

### Soundness
1

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
2

### Summary
The paper studies the important problem of understanding ADAM's convergence for non-convex optimization problems via online learning algorithms. Specifically, the paper considers the $\beta$-FTRL which has been shown to correspond to a version of ADAM. The main technical contributions are:

1. Removing the gradient clipping present in prior works to obtain an algorithm closer to the practically implemented version of ADAM.
2. Obtaining last iterate convergence guarantees.

I want to note that I have very limited knowledge in the field of online learning.

### Strengths
The paper removes the clipping used in priors works on $\beta$-FTRL, which makes the algorithm more realistic and closer to the real ADAM algorithm.

The paper obtains last iterate convergence guarantees of the order $O(\frac{1}{\sqrt{T}})$ for a general class of non-convex optimization problems.

### Weaknesses
[1] This work does not survey prior works' results thoroughly -- i.e, it does not state the assumptions and convergence rates obtained in prior works on ADAM. Specifically, the paper should clearly delineate how its assumptions and results compare to those established in the literature for both smooth and non-smooth non-convex settings. A more comprehensive comparison would help to contextualize the significance of the paper's contributions.

[2] In Assumption 2.1, the bounded gradient assumption along with Assumption 2.2 of bounded domain seem very stringent. The bounded gradient assumption, while common, can be restrictive in practice, especially for highly non-convex functions where gradients can become arbitrarily large. Similarly, the bounded domain assumption limits the applicability of the results to problems with known constraints. It would be beneficial to explore if these assumptions can be relaxed or if the authors can provide justification for why they are necessary for their analysis. For instance, could a weaker notion of gradient boundedness be considered, such as a growth condition, or could the domain be unbounded under certain constraints on the objective function?

[3] The paper introduces the FTRL framework but does not introduce the full ADAM algorithm in detail. It would be helpful to show how it differs from the Clip-free FTRL version introduced in this paper. The paper should explicitly derive the connection between the proposed algorithm and the standard ADAM update rule, highlighting the key differences and the implications of these differences on the convergence properties. This would allow readers to better understand the practical relevance of the theoretical results.

### Questions
See weaknesses

### Soundness
3

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
3

### Summary
The paper builds on a series of existing works to provide some theoretical analysis of Adam. Existing works have shown that Adam could be framed as an instance of the online-to-nonconvex conversion from (Cutkosky et al 2023), therefore the performance of Adam could be analyzed through the dynamic regret of the online learning algorithm it corresponds to. This paper seeks to extend this argument in two ways. First, the online learning algorithm underlying Adam is analyzed without the projection to a bounded domain. Second, the paper extends the online-to-nonconvex conversion itself towards last iteration properties.

### Strengths
Analyzing Adam is one of the central topics in deep learning optimization, therefore the context of this paper is relevant to the machine learning community. As far as I can see, credits are given properly to the existing works this paper builds on.

### Weaknesses
Although this paper raises some good points, the overall quality is in my opinion below the acceptance threshold.

First, it seems that the existing works this paper builds on already analyzed discounted FTRL without projection, such as Theorem B.2 of (Ahn et al 2024). In this regard the first contribution claimed by this paper is not new. It also seems that existing works by Ahn et al used the projected version of FTRL mainly for analytical convenience, and most of their results can be derived analogously for the version without projection, if someone is willing to do the tedious extension. So it remains unclear to me what is the new insight from the first part of the paper.

The second part of the paper claims to extend the framework of Cutkosky et al to last iterate convergence, but actually the final results are not based on the last iterate, as the output still needs to be sampled from the trajectory of the iterates. Again the message here is unclear.

What's more important is that the paper claims to provide better insights on Adam, but it's unclear why the two extensions from the paper are significant in this context. I could see the paper being motivated from an analytical perspective, but for people who only want to understand why Adam is effective, what is the takeaway?

Writing needs to be thoroughly improved, as I find it hard to follow some of the arguments, such as the part of Section 4 before 4.1. There are also technicalities swept under the rug, such as the hyperparameter a in Lemma 4.1 and the associated requirements. Is there any reason we should expect those requirements to hold?

### Questions
Related to the above, the significance of the paper needs to be further justified, specifically for the purpose of understanding Adam.

### Soundness
2

### Presentation
2

### Contribution
2

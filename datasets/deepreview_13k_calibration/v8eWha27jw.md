# Accelerating Federated Learning with Quick Distributed Mean Estimation

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Distributed Mean Estimation (DME), in which clients communicate vectors to a parameter server that estimates their average, is a fundamental building block in communication-efficient federated learning. In this paper, we improve on previous DME techniques that achieve the optimal Normalized Mean Squared Error (NMSE) guarantee by asymptotically improving the complexity for either encoding or decoding (or both). To achieve this, we formalize the problem in a novel way that allows us to use off-the-shelf mathematical solvers to design the quantization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors study Distributed Mean Estimation problem (DME) where $n$ clients communicate a representation of a $d$-dimensional vector to a parameter server which estimates the vectors’ mean.

I think the overall presentation of the paper, for example providing Figure 1 is quite helpful to help readers understand the main contribution of this paper. To the best of my knowledge, related work have been covered sufficiently. 

In terms of technical contribution, this paper is built on the previous literature DRIVE and EDEN and improves Encoding and Decoding complexity bounds under similar normalized mean squared error bounds. It seems the main advantage of QUIC-FL comes from the tailored random rotation preprocessing which reduces the constant in the NMSE error bound for small values of $p$.

I have an overall positive impression about this work, while I think there are rooms for improvement that will be discussed in the following.  

The authors provide PuTorch and TensorFlow implementation and show improvements over QSGD Hadamard, and Kashin. The improvements over DRIVE and EDEN is somehow marginal. It will be also very helpful for the readers if the authors elaborate on the discussion after Theorem 3.1.

### Strengths
I think the paper is overall quite well-written. 

The related work is comprehensive. I also think it is very nice that that the authors show transparently the superiority of EDEN on low bit-width region in terms of NMSE.

I also like the overall flow of the paper including the intuition provided by authors within the algorithmic description.

### Weaknesses
The authors provide PuTorch and TensorFlow implementation and show improvements over QSGD Hadamard, and Kashin. 
The improvements over DRIVE and EDEN is somehow marginal. 

I appreciate that the authors show the superiority of EDEN on low bitwidth region in terms of NMSE.

I was just wondering whether the authors can come up with a hybrid type method that enjoys the NMSE of EDEN while have similar coding time improvements of QUIC-FL?

------------------

I appreciate the discussion after Theorem 3.1 regarding $\mathrm{E}\big[\big(Z-\hat Z\big)^2\big]$. However, it will be still great if the authors provide an explicit error bounds in terms of $b,p,d$. In the current form, it is a bit difficult to provably show the theoretical improvement.

On Table 1, the authors claim that the NMSE for QSGD is $O(d/n)$, which is wrong. It is indeed $O(\sqrt{d}/n)$ (their $n$ in their Lemma 3.1 is your $d$).

### Questions
I was just wondering whether the authors can come up with a hybrid type method that enjoys the NMSE of EDEN while have similar coding time improvements of QUIC-FL? 


Could the authors provide a more explicit bound in Theorem 3.1? 

I will be willing to increase my scores during the rebuttal period.

### Soundness
3 good

### Presentation
3 good

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
In this work, the authors propose a distributed mean estimator, namely QUIC-FL, to estimate the mean of n vectors in a distributed setting. Their method achieves the optimal $O(\frac{1}{n})$ NMSE (normalized mean squared error). They provide asymptotic improvement to either encoding complexity or decoding complexity (or both) with respect to the existing methods providing $O(\frac{1}{n})$ NMSE guarantees.

### Strengths
I found the introduction of bounded support quantization and its use to achieve $O(\frac{1}{n})$ NMSE interesting. I generally liked the presentation and clarity of the paper. The claims have been repeated at times, I believe for emphasis, but otherwise, it is a well-written paper. I also liked the way authors have placed their work with respect to the existing works. They have also provided a good set of numerical experiments to validate their theory.

### Weaknesses
The gain in accuracy seems marginal (if any) as compared to EDEN empirically. The proposed method does perform better in terms of decoding time, but decoding time is usually not a big concern when it is done in a centralized server with sufficient processing power.

I am slightly confused by the following statement on page 4.

"Empirically, sending the indices using ...as $p . \log d << 1$ in our settings, resulting in fast processing time and small bandwidth overhead."

Does this mean that $p$ is not kept constant? If that is the case, then shouldn't NMSE have an order of $O(\frac{\log d}{n})$?

### Questions
I am slightly confused by the following statement on page 4.

"Empirically, sending the indices using ...as $p . \log d << 1$ in our settings, resulting in fast processing time and small bandwidth overhead."

Does this mean that $p$ is not kept constant? If that is the case, then shouldn't NMSE have an order of $O(\frac{\log d}{n})$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel quantization algorithm with application in federated learning. The key parameters are determined via a constraint optimization problem. Notably, coordinates above the determined threshold are explicitly transmitted to the server, while other values are quantized. To simplify decoding on the server, the clients apply a common preprocessing rotation to the local vectors. This step also modifies the distribution of the coordinates to reduce quantization errors.

### Strengths
+ The overview of the state-of-the-art is well presented, with comparisons with existing methods.

+ The authors demonstrate that the encoding and decoding times of their method are comparable to those of competitors, but with greater precision.

### Weaknesses
 * The authors propose interesting contributions, although some ideas have similarities with existing work.

* The parameters of the quantization set $\mathcal{Q}_{b,p}$ are obtained by solving a problem that considers the quantiles of a truncated Gaussian distribution. In practice, do the entries of the rotated vectors follow this Gaussian distribution? Instead of considering the standard normal distribution $\mathcal{N}(0,1)$, would it be possible to approximate the coordinate distribution by a parametric distribution?

* What is the complexity of the optimization problem for determining $b, p, t_p$?

### Questions
* The parameters of the quantization set $\mathcal{Q}_{b,p}$ are obtained by solving a problem that considers the quantiles of a truncated Gaussian distribution. In practice, do the entries of the rotated vectors follow this Gaussian distribution? Instead of considering the standard normal distribution $\mathcal{N}(0,1)$, would it be possible to approximate the coordinate distribution by a parametric distribution?

* What is the complexity of the optimization problem for determining $b, p, t_p$?

**Requested Changes:**

* Page 3: "have" is probably missing between "we" and "that" at the end of the paragraph "Problems and Metric".

* Page 5: in the definition of $\mathcal{A}\_{p,m}$, I think $A\_{p,m}(i)$ should be replaced by $\mathcal{A}_{p,m}(i)$.

* Page 7: "the sender sends the message $x$", perhaps should be replaced by "the sender sends the message $R(h,x)$".

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This works addresses the problem of communication-efficient distributed mean estimation (DME), a common subroutine in distributed optimization, and improves the SOTA of quantization techniques. It proposes QUIC-FL, the first quantization scheme that is efficient in both encoding and decoding and achieves the optimal NMSE, the metric of the estimation error, of $O(1/n)$ at the same time, where $n$ is the number of clients. QUIC-FL is based on two key ideas: 1) Bounded support quantization (BSQ), which sends a few large coordinates exactly and quantizes only the rest few. 2) An optimization framework that optimizes the set of quantization values to further reduce the estimation error, based on the limiting distribution of transformed coordinates of the client vectors, i.e., the normal distribution. Furthermore, QUIC-FL discusses the usage of client-specific shared randomness and the RHT rotation to practically gain constant improvement in the estimation error. Finally, extensive experiments show advantages of QUIC-FL compared to several SOTA quantization schemes in terms of encoding time, decoding time and NMSE.

### Strengths
In terms of originality, this paper combines several existing approaches and improve the SOTA of quantization schemes.

In terms of quality, the paper analyzes and empirically shows an improved performance of the proposed QUIC-FL in terms of computational efficiency and the estimation error, against several SOTA baselines.

In terms of clarity, the paper conveys the key ideas in the design of QUIC-FL.

In terms of significance, the problem of communication-efficient DME the paper addresses is important. Improvement in quantization schemes is always welcomed.

### Weaknesses
The presentation of this draft needs to be greatly improved.

- The abstract is not informative at all. The reader has no idea about the techniques this work uses to improve DME and the novelty of the techniques after reading it. It should at least mention, for example, one idea QUIC-FL builds on is BSQ which sends exactly a few large coordinates and quantizes the rest small ones.

- In Introduction, the paragraph starting with “For example, in Suresh et al. 2017 …”, it is mentioned the entropy encoding is “compute-intensive”. How long does the decoding time of this approach take? Table 1 does not include entropy encoding as a baseline.

- It is mentioned in Introduction that the decoding procedure of “entropy encoding” from a previous work is “compute-intensive”. What is the time complexity of this decoding procedure? It seems this approach is not included in Table 1 as a baseline for comparison. A more detailed comparison, potentially including empirical timing results, would strengthen the argument for QUIC-FL's efficiency.

- The Lloyd-Max quantizer appears at several places in the work, e.g., in Introduction, and in serving as the Lower Bound in Section 3.5. However, this work does not introduce this quantizer properly. Can the authors give a brief introduction of this quantizer and in which cases is it optimal? Specifically, under what conditions does it achieve optimality, and how does it relate to the Gaussian assumption made in this work?

- The paragraph “while the above methods suggest …” is abrupt and confusing. It’d be better to move this paragraph before surveying existing quantization techniques in Introduction.

- In Section 2 preliminaries, it would be clearer if “unbiased algorithms and independent estimators” can be formally and clearly defined. Minor issue: “we that NMSE …” => “we want that NMSE …”.

- The uniform random rotation appears at several places in the work. What exactly is this rotation? Is it a uniform Gaussian random rotation? A more precise definition, potentially referencing standard techniques for generating such rotations, would improve clarity.

- In Section 3.5 “accelerating QUIC-FL with RHT”, “adversarial vectors” are mentioned but not introduced. It is confusing how the proposed approach compares against DRIVE and EDEN in terms of the application to “adversarial vectors”. A clear definition of what constitutes an "adversarial vector" in this context is needed, along with a more detailed discussion of how QUIC-FL handles such cases compared to DRIVE and EDEN.

- In Section 3.5 “accelerating QUIC-FL with RHT”, it states “the result does not have the additive NMSE term is [because] we directly analyze the error for the Hadamard-rotated coordinates”. Can the author be more formal and specific how the analysis here is different from the one in Theorem 3.1? The connection between the Hadamard rotation and the removal of the additive error term needs further elaboration.

- Several places in the work states in plain text the performance of QUIC-FL with different values of its hyperparameters. For example, in Section 3.5 “accelerating QUIC-FL with RHT”, it states the NMSE of QUIC-FL is bounded by … with $b = 1,2,3,4$. It’d be easier for the readers if those numbers can be turned into figures.

This work claims the proposed QUIC-FL has NMSE $O(1/n)$. However, by Theorem 3.1, the actual NMSE is indeed $O(1/n \cdot \sqrt{\log d / d})$. It does not seem to be OK to omit the $O(\sqrt{\log d / d})$ term and directly write $O(1/n \cdot \sqrt{\log d / d}) = O(1/n)$. The impact of the dimensionality $d$ on the overall NMSE should be explicitly addressed, especially since the $O(\sqrt{\log d / d})$ term can be significant for certain values of $d$. A more rigorous justification for claiming $O(1/n)$ NMSE is required.

$	extbf{Optimizing the quantization values. }$
In Section 3.3 “distribution-aware unbiased quantization”, this work proposes two optimization problems to find the optimal quantization values to reduce NMSE. In the first optimization problem on page 4, the notations $S(z, x)$ and $R(x)$ are a bit confusing. Are $S$ and $R$ two functions to be optimized? Is $R(x)$ essentially a vector of $2^b$ variables? Is $S(z, x)$ a continuous function?  Furthermore, how are these functions parameterized in the optimization process? A clearer explanation of the roles of $S$ and $R$ in the optimization is needed.

Similarly, in the second optimization problem (i.e., the discretized version of the first problem), is $S’(i, x)$ essentially a vector of $m \cdot 2^b$ variables to be optimized? A more explicit definition of $S'(i,x)$ and its relationship to $S(z,x)$ would be helpful.

Since the number of variables to be optimized is on the order of $2^b$, how efficient is the second optimization problem?  What is the computational complexity of solving this optimization problem, and how does it scale with $b$ and $m$?  How does this affect the practicality of the approach for different parameter settings?

$	extbf{Communication cost. }$
One concern is that the proposed QUIC-FL requires extra bits to send a few large coordinates exactly along with their indices, while the baseline quantization schemes usually allocate a fixed number of bits per coordinate. This makes QUIC-FL use more communication cost compared to the baseline. And hence it might not be fair to directly compare QUIC-FL’s NMSE against that of the baselines. How does the author compare in Table 1? Also, how does the author address this in the experiments? A more thorough analysis of the trade-off between communication cost and NMSE is needed. This could involve normalizing the NMSE by the actual number of bits transmitted for each method.

$	extbf{Optimality. }$
It is mentioned at several places that the optimal NMSE of any quantization is $O(1/n)$ (this lower bound is in terms of the number of clients only, I presume). This is not rigorous in the draft. Can the authors cite the theorems that indicates the optimality?

The draft claims QUIC-FL achieves a “near-optimal” NMSE. However, it seems this lower bound is only empirically obtained using the Lloyd-Max quantizer in Section 3.5. “Near-optimal” specifically means one can theoretically show the algorithm achieving optimality (e.g., close to a lower bound), up to a logarithmic factor. And so it might not be appropriate to claim the “near-optimality” of QUIC-FL.

### Questions
$\textbf{Optimizing the quantization values. }$
In Section 3.3 “distribution-aware unbiased quantization”, this work proposes two optimization problems to find the optimal quantization values to reduce NMSE. In the first optimization problem on page 4, the notations $S(z, x)$ and $R(x)$ are a bit confusing. Are $S$ and $R$ two functions to be optimized? Is $R(x)$ essentially a vector of $2^b$ variables? Is $S(z, x)$ a continuous function?

Similarly, in the second optimization problem (i.e., the discretized version of the first problem), is $S’(i, x)$ essentially a vector of $m \cdot 2^b$ variables to be optimized?

Since the number of variables to be optimized is on the order of $2^b$, how efficient is the second optimization problem?

$\textbf{Communication cost. }$
One concern is that the proposed QUIC-FL requires extra bits to send a few large coordinates exactly along with their indices, while the baseline quantization schemes usually allocate a fixed number of bits per coordinate. This makes QUIC-FL use more communication cost compared to the baseline. And hence it might not be fair to directly compare QUIC-FL’s NMSE against that of the baselines. How does the author compare in Table 1? Also, how does the author address this in the experiments?

$\textbf{Optimality. }$
It is mentioned at several places that the optimal NMSE of any quantization is $O(1/n)$ (this lower bound is in terms of the number of clients only, I presume). This is not rigorous in the draft. Can the authors cite the theorems that indicates the optimality? 

The draft claims QUIC-FL achieves a “near-optimal” NMSE. However, it seems this lower bound is only empirically obtained using the Lloyd-Max quantizer in Section 3.5. “Near-optimal” specifically means one can theoretically show the algorithm achieving optimality (e.g., close to a lower bound), up to a logarithmic factor. And so it might not be appropriate to claim the “near-optimality” of QUIC-FL.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

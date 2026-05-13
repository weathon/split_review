# Factor Graph Optimization of Error-Correcting Codes for Belief Propagation Decoding

- Decision: Reject
- Scores: 3, 5, 3, 8, 3

## Abstract
The design of optimal linear block codes capable of being efficiently decoded is of major concern, especially for short block lengths. 
As near capacity-approaching codes, Low-Density Parity-Check (LDPC) codes possess several advantages over
other families of codes, the most notable being its efficient decoding via Belief Propagation.
 While many LDPC code design methods exist, the development of efficient sparse codes that meet the constraints of modern short code lengths and accommodate new channel models remains a challenge.
In this work, we propose for the first time a gradient-based data-driven approach for the design of sparse codes. We develop locally optimal codes with respect to Belief Propagation decoding via the learning of the Factor graph under channel noise simulations. 
This is performed via a novel complete graph tensor representation of the Belief Propagation algorithm, optimized over finite fields via backpropagation and coupled with an efficient line-search method. 
The proposed approach is shown to outperform the decoding performance of existing popular codes by orders of magnitude and demonstrates the power of data-driven approaches for code design.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an optimization scheme of a Tanner graph for low-density parity-check (LDPC) codes. Particularly, the scheme aims to improve decoding performance by a belief propagation (BP) decoder. Since the problem is a non-convex binary optimization problem whose cost function is implicitly defined, a gradient-based approach is applied by relaxing variables and using a straight-through estimator. In addition, a grid search is proposed to find an optimal learning rate. From numerical results, the proposed method outperforms the decoding performance of existing codes.

### Strengths
* The proposed method is the first gradient-based optimization of a parity-check matrix for error-correcting codes.
* In addition, a grid-search approach for finding the learning rate is proposed, which is an alternative to the line-search approach.
* Numerical results show that optimized codes by the proposed method can be decoded more accurately than conventional codes.

### Weaknesses
The reviewer understands the motivation of the work and the numerical effectiveness of the proposed method. However, the paper contains  some flaws as follows: 

1. **Technical contributions of the proposed method** 

The contributions that the authors claim are threefold: (i) formulation of the problem, (ii) reformulation of BP in tensor fashion, and (iii) differentiable and fast optimization method for the problem. Here, the reviewer wants to evaluate each contribution in detail. 

* (i) Formulation of the problem: In the paper, Eq. (4) (or (8)) is the formulation of the problem, whose novelty is claimed by the authors. However, a similar formulation (mainly focusing on "expectation w.r.t. random codewords and noise") has already been proposed in [Choukroun & Wolf, 2024a] cited in the paper. Eq. (4) is different from [Choukroun & Wolf, 2024a] in that Eq. (4) includes the regularization terms. However, the authors do not compare the differences explicitly and claim that the whole formulation in this paper is novel. In addition, the effect of regularization needs to be included in numerical experiments. The reviewer suggests that the author carefully clarify the novelty of the formulation.

* (ii) Reformulation of BP in Tensor fashion: The reviewer does not consider this part technically novel because a similar "tensorization" technique has been used for the implementation of neural BP decoders. While the authors use a complete graph representation, this does not fundamentally change the nature of the tensor operations, and sparse matrix operations could still be used to maintain efficiency. The core idea of representing BP messages as tensors for parallel processing is not new.

* (iii) Differentiable and fast optimization method for the problem: The reviewer agrees with this point. However, there are some flaws, as shown below.

Overall, the technical contributions that the authors claim seem partly insufficient. In addition, the paper does not contain any mathematical or analytical contributions, which is obviously a weak point. 

2. **Contributions of the grid-search approach**

Related to the above point, the authors claim the novelty of the grid-search approach for learning rate. However, the reviewer wonders about the novelty due to the following reasons.

* No comparison with line-search methods: the authors claim that the conventional line-search methods assume the convexity of a cost function, and they are unsuitable for non-convex problems like Tanner graph optimization in this paper. However, the assumption is required to show the optimality of line-search methods. Practically, line-search methods are used for non-convex optimizations without assumptions. Therefore, numerical comparison in terms of optimization performance and/or execution time should be necessary to show the effectiveness of the grid-search method. The authors should compare against standard line search methods like Armijo backtracking or Wolfe conditions, which are frequently used in non-convex optimization.

* No theoretical guarantee: In contrast to the above discussion, there is no guarantee of the grid-search method for finding the optimal learning rate. It is a weakness of the proposed method. The grid search is essentially a brute-force approach, and without any theoretical justification, it is unclear why it should be preferred over other methods, especially if it is computationally expensive. The authors should provide some analysis or justification for why this approach is effective.

* Effectiveness of the grid-search approach: It is reported in Sec. 6 that an optimized matrix depends on the initial matrix, suggesting that the proposed method finds a suboptimal solution, not an optimal one. This fact may weaken the effectiveness of the method. At least, a comparison with other learning-rate optimizations will be required. The dependence on the initial matrix highlights the non-convex nature of the optimization problem and raises concerns about the robustness of the method. A more thorough investigation of the solution space is needed.

3. **Missing advantage of the gradient-based optimization**

The authors claim that the proposed gradient-based optimization is fast but no evidence is provided in the paper. How much is the method fast compared with what?

### Questions
Questions are included in the "Weakness" section. 

Suggestions: 
1. Around Line 131: Please clarify whether vectors are column or row vectors. Anyway, the dimensions of the multiplication in $H(mG)$ are incorrect. 
2. Line 157: $k=1$ should be $k=0$ because the first iterations is $2k+1=1$.
3. Eq. (4): Under $\mathbb E$, what does the expectations w.r.t. $T$ mean? Is $T$ a random variable, not a constant number? 
4. Line 197: A generator matrix is not unique in general. Is the form of the matrix fixed in this paper?
5. Line 204 etc.: $c=Gm$ should be $c=mG$ accourding to Line 131.
6. Eq. (6): "(" should be removed.
7. Eq. (8): The cumulative loss function w.r.t. iteration $t$ in (8) has been proposed in previous studies on neural BP decoders. Please add some references.
8. Line 291: What is the meaning of "sufficient statistics"? It is unclear whether the gradient is sufficiently statistical in terms of statistics. It is recommended to rephrase the term correctly. 
9. Eq. (9): What does index $i$ stand for? Since $\Omega$ represents a matrix, indices are given like $ i,j$.
10. Line 310: What is the meaning of "line-search objectives"? Is it the cost function for the optimal learning rate?
11. Line 373: The i.i.d. Gaussian mixture model is called bursty noise in this paper. It seems incorrect because bursty noise generally implies time-dependent noise. 
12. Line 457: "sparse code" should be "a sparser code" or "sparser codes."

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper deals with factor graph (or parity-check matrix, PCM) optimization of error-correcting codes for Belief Propagation (BP) decoding. Actually, this optimization is difficult as it is an integer optimization problem: the elements of the PCM are either 0 or 1 and even small changes (e.g. the replacement of one element can drastically worsen the performance). The authors propose a gradient-based data-driven approach via a novel complete graph tensor representation of the Belief Propagation algorithm. The demonstrate the efficiency of the resulting codes by simulations.

### Strengths
The main strong point are as follows:
- the first gradient-based data-driven approach via a novel complete graph tensor representation of the Belief Propagation algorithm.
- automating the process of finding a good code.

These point are indeed important as usually in practice people construct LDPC codes via heuristics, or some optimization algorithms like genetic algorithm or simulated annealing, which takes a lot of time and computational resources.

### Weaknesses
I list the main weaknesses below:
- Given that LDPC codes are known to perform poorly at short lengths due to short cycles in the Tanner graph ( the length of the minimal cycle (the girth) of the Tanner graph is O(log n) ), could the authors elaborate on their motivation for focusing on LDPC optimization for short codes? Are there specific applications or theoretical insights they hope to gain from this approach? It is well established that for short block lengths, other code families like polar codes often exhibit superior performance, especially when decoded with successive cancellation list (SCL) decoding. The choice of LDPC with BP, which is known to struggle with short cycles, requires stronger justification.
- Could the authors provide BER vs SNR (or Eb/N0) curves for their results, in addition to the current tabular format? This would allow for easier comparison with existing literature and help identify potential error floors. The tabular format, while compact, does not provide the same level of insight into the code's behavior across different noise levels, particularly the presence of error floors which are crucial for practical applications.
- To better understand the performance of your constructed codes, could you include a comparison with polar codes under SCL decoding (L=8) for short lengths? Such results can be found e.g. here https://rptu.de/channel-codes/channel-codes-database. Specifically, a comparison with state-of-the-art polar codes, which are known to perform well in the short block length regime, is necessary to contextualize the performance of the proposed LDPC codes. The provided link offers a readily available benchmark for such comparisons.
- To provide theoretical context for your results, could you compare them to the finite length achievability and converse bounds from Polyanskiy et al. (2010)? This would help situate your method's performance relative to fundamental limits. Comparing the achieved performance against theoretical bounds, such as the normal approximation to the finite-length achievability bound, is crucial to understand how close the proposed codes are to the optimal performance.
- Could you provide an analysis of the final Tanner graphs produced by your method, including metrics such as column weight distribution, minimum distance, and trapping sets? This would offer insights into the structural properties of the optimized codes. Understanding the structural properties of the optimized codes, such as the distribution of variable node degrees, the minimum distance, and the presence of trapping sets, is vital for a comprehensive evaluation.
- [Minor] You write about the generator matrix and the problems related to obtaining G from H. But for the BP decoder you can perform training on zero codeword only (as you mention later). I suggest to shift to zero codeword from the very beginning.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this study, the authors propose a method to optimize the parity check matrix (PCM) $H$ using deep learning techniques. They modified the BP decoding equations that rely on $H$ so that $H$ could become trainable. To accelerate the training process, they utilized a line search method. The proposed code optimization method has the advantage of being applicable to codes with constraints or in arbitrary channels.

### Strengths
In the field of model-based neural decoder research, previous work has focused on optimizing decoder weights with a given $H$. However, this study differentiates itself by optimizing $H$ itself, which is both novel and distinctive. The derivation of trainable BP decoding equations for $H$ is particularly commendable. The paper presents a significant amount of experimental results, demonstrating performance gains through $H$ optimization for various code types.

### Weaknesses
In this study, the authors propose a method to optimize the parity check matrix (PCM) $H$ using deep learning techniques. They modified the BP decoding equations that rely on $H$ so that $H$ could become trainable. To accelerate the training process, they utilized a line search method. The proposed code optimization method has the advantage of being applicable to codes with constraints or in arbitrary channels.

In Table 1, the optimization is performed for a wide range of initial codes, but for high-density codes like BCH, Polar, and LTE Turbo, which have their own optimized decoders instead of BP decoders, the improvements in BP performance seem less meaningful. It seems more appropriate to compare LDPC codes, but there are concerns about the "representativeness of the LDPC codes" used in the comparison. Both the MAKCAY and CCSDS codes are quite outdated (and indeed seem to show limited performance improvement). Furthermore, the PEG construction used for the LDPC PEGX code appears to be an early-stage method. In addition, The CCSDS code is known to ensure efficient encoding, but as shown in Figure 7, modifying $H$ without constraints (as it seems to have been done in Table 1) may no longer guarantee this property.

Therefore, it would be better to evaluate whether the performance can be improved for more representative LDPC codes (e.g., short-length ARJA code class or 5G LDPC codes) while maintaining the functionalities of these code types (efficient encoding, QC structure, and rate compatibility).

Additionally, a comparison with Elkelesh et al. (2019), another data-driven code construction method, does not seem fair. In Table 4, the authors compared their optimized $H$ matrix for iterations of 5 and 15, whereas the Elkelesh method was optimized at iterations of 75 and 150. Since the Elkelesh method is also a data-driven construction approach, it seems feasible to optimize it with a smaller iteration count, such as 15. A comparison under such conditions would be necessary.

The proposed method appears to be a local optimization method highly dependent on the initial $H$ matrix. As shown in Figure 7, only a small number of edges were changed in sparse cases. As the goal of code construction is to create a globally optimized $H$ for a given code length, the proposed method does not seem to align with this objective.

Additionally, I have a few questions:

1.	The purpose of showing Figure 2 is unclear. I can observe that the variation increases significantly at high SNRs; a discussion on this would be helpful.

2.	What exactly is the meaning of PEG X? In Table 1, there appear to be significant performance differences between PEG2, PEG5, and PEG10 (with PEG5 showing particularly superior performance). It would be helpful to clarify this.

3.	In line 251, it is stated that the method can be applied regardless of modulation. If there are experimental results for modulations other than BPSK, it would be useful to include them.

4.	In line 428, an experiment was proposed to optimize only $P$ while keeping III fixed in the systematic form of $H=[I P]$. However, most LDPC standards use a dual diagonal form rather than the systematic form $[I P]$. Therefore, an optimization experiment assuming the dual diagonal form would be more appropriate.

5.	Overall, the code lengths are very short, with a maximum length of 128. In this range, Polar codes are known to be superior, so the practicality of LDPC code optimization seems somewhat limited.

6.	Further research on additional properties of the modified code, such as minimum distance or cycles, is necessary.

### Questions
Additionally, I have a few questions:

1.	The purpose of showing Figure 2 is unclear. I can observe that the variation increases significantly at high SNRs; a discussion on this would be helpful.

2.	What exactly is the meaning of PEG X? In Table 1, there appear to be significant performance differences between PEG2, PEG5, and PEG10 (with PEG5 showing particularly superior performance). It would be helpful to clarify this.

3.	In line 251, it is stated that the method can be applied regardless of modulation. If there are experimental results for modulations other than BPSK, it would be useful to include them.

4.	In line 428, an experiment was proposed to optimize only $P$ while keeping III fixed in the systematic form of $H=[I P]$. However, most LDPC standards use a dual diagonal form rather than the systematic form $[I P]$. Therefore, an optimization experiment assuming the dual diagonal form would be more appropriate.

5.	Overall, the code lengths are very short, with a maximum length of 128. In this range, Polar codes are known to be superior, so the practicality of LDPC code optimization seems somewhat limited.

6.	Further research on additional properties of the modified code, such as minimum distance or cycles, is necessary.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel gradient-based data-drive approach for constructing low-density parity-check codes. The belief-propagation algorithms on sparse graph codes are reformulated into a differentiable matrix representation. The paper further relaxes the 0-1 constraints on the parity-check matrix bits into learnable continuous weights. Combined with a STE (Straight-Through Estimator) method, paper reformulate the optimization problem into a differentiable end-to-end optimization problem. The paper also proposes binary line-search method for solving the optimization problem.

### Strengths
* The paper contains a novel idea of constructing low-density parity-check codes using a end-to-end differentiable data-driven approach. The idea of using STE (an approach usually used in deep learning quantization and sparsity design) for converting the original NP-complete discrete optimization into a differentiable optimization problem is novel.
* The approach in this paper open-up a new research direction of using end-to-end differentiable optimization for constructing low-density parity-check codes.
* The proposed binary line search method is novel.
* The experimental results in the paper show that the differentiable end-to-end approach results in improved coding performance
* The paper is well-written and clear.

### Weaknesses
 * It seems that the computational complexities of the algorithm would be quadratic with respect to the code length. For example, every element of the parity-check matrix is a learnable continuous variable. Also, in the binary line search, during each optimization step, the relevant grid samples can be as large as n(n−k), which is quadratic with respect to the code length n. This quadratic scaling in both memory and computation during training is a significant concern for practical application to larger codes.
* In the experimental results, the optimizations are initialized from a known sparse codes. There is a question that whether we can start the optimization from a randomly initialized code design and still ends up with a code with outperforming decoding performance. The reliance on a good initial sparse code may limit the exploration of the design space and potentially bias the optimization towards local optima near existing codes.
* It seems that the sparsity regularization term is a L1 regularization. The paper lacks a in-depth discussion on other possible sparsity regularization and whether L1 regularization is optimal. Specifically, the paper does not explore the impact of different regularization strengths, or alternative regularization techniques such as group sparsity or elastic net regularization, which might be more suitable for enforcing specific degree distributions.
* From equation 8, it seems that the losses are equally weights at different decoding iteration steps. Because, the losses should be large at the first several iteration steps, it is my opinion that if we train the model using such equally weighted losses, we are mainly optimize the codes for its performance at the first several decoding iteration. This could lead to suboptimal performance at later iterations, which are critical for achieving low error floors.

### Questions
* For the computational complexity issues, could authors provide more discussions on how to lower the computational costs or future directions on lowering the computational costs?
* The paper shows that initializing from known sparse codes would already result in performance improvements. However, initializing from these known codes would probably result in codes that are very close to the existing codes. It would be interesting to see whether other types of initialization would give us more diverse or new codes that are totally different from all the hand-crafted codes and outperform the known codes. I think initializing the optimization from the all zero parity-check matrix would impose a very challenging optimization problem, because of the symmetry breaking issues. Could the authors try to initialize the optimization by random picking a code from the code ensemble satisfying a particular pair of degree distributions? Or the authors could provide a discussion on why initialization from known codes makes more sense.
* For the sparsity regularization, the authors provide very little discussions in the draft. In my opinion, the sparsity regularization may need more careful considerations. For example, what we may want to achieve is a sparse parity-check matrix satisfying a certain pair of degree distributions (or a regular LDPC code). Thus, each row(column) should be sparse with a designed number of non-zero elements. The authors could argue that a simple L1 regularization would already guarantee that the optimization would end-up with a regular code or a code satisfying a designed degree distribution, of course by providing more experimental results. Could the author try to use a combined L1 and L2 regularization, where L1 is applied to each row and each column, and L2 is applied to row weights and column weights?   
* For the loss weighting, I think the authors could try equal weighting at the beginning epochs and weight the losses at large decoding iterations more at later epochs. Or, the author could provide more discussions on why equally weighting is desired in certain senses.

In a summary, it is suggested that the authors could
* provide more discussions on how to lower the computational costs either in this paper or as a future direction
* provide more experiments on different optimization initialization or a discussion on why the current way of initialization makes more sense
* provide more experiments on using a combined L1, L2 sparsity regularization or a discussion on whether the L1 regularization already results in desired sparse parity-check matrices
* provide more experiments on using adaptive loss weighting or a discussion on justifying the current equal weighting.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a gradient-based, data-driven method for the design of sparse-graph codes tailored to belief propagation (BP) decoding. The main contribution of the paper is to learn the factor graph structure through a differentiable representation that facilitates backpropagation. Specifically, the authors start with a complete bipartite graph where the edges are learnable.

### Strengths
The proposed approach to design codes is interesting and, as the authors show, leads to codes that outperform some existing codes.

### Weaknesses
Despite that the method proposed by the authors is interesting, I believe this paper should be rejected, primarily for reasons concerning its limited contribution scope and weak experimental comparisons. My argumentation is detailed below:

1. Limited contribution: While the approach presented in the paper is conceptually interesting, the contribution of this paper is too narrow to merit  publication in a major conference like ICLR. The work is more appropriate for  a coding conference such as ISIT or ITW. I believe that this work is valuable for the coding community and deserves publication, but it lacks depth and broader impact typically expected at  a  major machine learning venue or for a major coding journal.

2. Unconvincing experiments and comparisons: The experimental results are insufficient to answer the core question this paper seeks (or should seek) to address: Does this method allow to design  codes that perform better than state-of-the-art codes? This question remains unanswered. This casts doubt on the interest of the proposed approach. The authors should compare the performance of the designed codes with that of the best available codes, as well as with relevant performance bounds. Without these comparisons, the results merely demonstrate the construction of improved codes over baselines, which still underperform relative to the best codes. This weakens the impact of the method. 

Please, see my Comment 2 in Section "questions" for some suggested comparisons.

3. Non-standard metrics: The paper reports performance using the negative natural logarithm of the BER. This is very unconventional for a coding paper (and this IS a coding paper) and complicates unnecessarily the interpretation of the results.  Standard practice in coding theory involves presenting BER or block error rate (BLER) results directly (the latter is more suitable!), which allows for clearer, more interpretable results. The authors should adhere to these standard metrics. 

Please, see my Comment 3 in Section "questions".

### Questions
1. Sections 3 and 4 can be presented in a much clearer and accessible manner. Currently, these sections make relatively straightforward concepts appear unnecessarily complex.

2. The experiments/results section should be thoroughly reworked. It is not unexpected that the authors' obtained  codes outperform the baseline codes they started with. Indeed, most of them are not particularly good codes (compared to the best-existing ones). Some of them, indeed are clearly poor codes for BP decoding. The authors should benchmark the performance of their newly-designed codes against SOTA codes.

For example, the authors should consider benchmarking their (128,64) codes with the SOTA codes reported in Figure 10 of the paper ``Efficient error-correcting codes in the short blocklength regime'' (the details of the codes are given in the paper). Without such a comparison and similar ones for other lengths, the relevance of the proposed approach is questionable.

Furthermore, the  authors should also benchmark the performance of their codes  against finite-length performance bounds, such as the Gallager's random coding bound, the random coding union bound (see same paper for details). In this sense, please report results in terms of block error rate, rather than bit error rate, as it is more relevant.

3. Rather than reporting results in terms of the negative natural logarithm of the BER, please plot BLER curves (as the ones in the paper cited above). Only in this way one is can fully understand how the proposed codes perform against SOTA codes and performance bounds. In other words, for the (128,64) codes you should reproduce Figure 10 in the paper above and include your own curves.

4. I do not see much value in the results in Figures 3, 4, 5, and 7. The results are unsurprising and provide limited insight. These results would be better suited for the appendix rather than the main body of the paper.

For example, in Figure 3 you show improvements with respect to random codes with different sparsity rates. For such lengths, random codes, particularly with higher density, are not good codes under BP decoding, so it is not surprising the your learned code works better! What do we learn from this figure that we don't know yet?

The same applies to Figure 7. I quote the paper: "We can observe that for low-density codes the modifications remain small,
since the code is already near local optimum, while for denser codes the change can be substantial". This is what any relatively knowledgeable coding expert would expect, so the figures do not bring any new insight.

### Soundness
3

### Presentation
2

### Contribution
2

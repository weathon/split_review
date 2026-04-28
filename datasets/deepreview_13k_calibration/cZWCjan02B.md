# Flash Inference: Near Linear Time Inference for Long Convolution Sequence Models and Beyond

- Decision: Accept
- Avg Score: 6.83
- Scores: 8, 5, 8, 6, 8, 6

## Abstract
While transformers have been at the core of most recent advancements in sequence generative models, their computational cost remains quadratic in sequence length.
Several subquadratic architectures have been proposed to address this computational issue. Some of them, including long convolution sequence models (LCSMs), such as Hyena, address this issue at training time but remain quadratic during inference. We propose a method for speeding up LCSMs' exact inference to quasilinear $O(L\log^2L)$ time, identify the key properties that make this possible, and propose a general framework that exploits these. Our approach, inspired by previous work on relaxed polynomial interpolation, is based on a tiling which helps decrease memory movement and share computation. It has the added benefit of allowing for almost complete parallelization across layers of the position-mixing part of the architecture. Empirically, we provide a proof of concept implementation for Hyena, which gets up to $1.6\times$ end-to-end improvement over standard inference by improving $50\times$ within the position-mixing part.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel linear-time inference algorithm for long convolution architectures like SGConv and Hyena. These models typically have a quadratic inference complexity with respect to the sequence length N, which can be prohibitive for large-scale applications.

The key insight behind the proposed approach is a clever partitioning and precomputation strategy for the contributions to the convolution of future outputs. This allows the inference complexity to be reduced to O(N log^2 N). The paper provides extensive experimental evidence demonstrating the acceleration of inference achieved by this new algorithm.

### Strengths
* As far as  I know, the interpolation perspective presented in this paper is original and inspiring. The writing is exceptionally clear, and Figure 1 has been extremely helpful in understanding the proposed method.

* The algorithm introduced in the paper largely solves the long-standing problem of quadratic inference complexity for long convolution models like SGConv and Hyena. This has been a significant bottleneck for the practical deployment of these architectures (note that there are also other long conv architectures that do not suffer from this, please see below).

### Weaknesses
This is a good paper and there is no much weakness to say about its methodology. However, I find the significance of the work depends on a line of work on long convolution architectures that the authors unfortunately have not discussed or compared.

Long convolution kernels can be contructed from smaller convolutions in a tree style hierarchical dilations such as those in WaveNet [1]. Recently, people have shown that these architectures, with nonlinearities removed and weight sharing, can be interpreted as having a wavelet based state and are competitive with SSM and long convs on sequence modeling benchmarks [2].

Crucially, these dilated convolution architectures also support linear-time inference, as detailed in [3], by maintaining a cache per layer. This allows for efficient inference without the need for techniques like FFT that are required for standard long convolutions.

Given these relevant prior results, I believe a comparison of the proposed approach to these dilated convolution models and their linear-time inference capabilities would greatly strengthen the paper. These alternative architectures offer a potentially simpler approach. As a reader of this paper, it would be nice to know when it is preferable to have a less structured long conv combined with the inference acceleration presented here.

### Questions
Please see my question above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes more efficient algorithms for auto-aggressive inference of long convolutional sequence models (LCSMs). The aggregate running time on a sequence of length $L$ is reduced from $O(L^2)$ to $O(L \log^2 L)$, and the actual wall clock time of the implemented algorithm reflects substantial increases in efficiency.

### Strengths
The paper's main strength is that it is technically sound and novel, and addresses the problem it aims to solve.
- The technical writing is clear and is helped by the inclusion of helpful graphics and rigorous algorithm boxes.
- Many considerations and variants of the core algorithm are proposed.
- An actual implementation is provided and all variants and baselines are benchmarked empirically.

There is a conception that long convolutions cannot be implemented efficiently in autoregressive inference settings, and so I do think that this paper presents an original algorithmic contribution.

### Weaknesses
While the paper provides a technical contribution, the paper's main weakness is that of significance and direction with respect to the broader field; it aims to solve a problem that I believe does not need solving. Correspondingly, the papers writing (in terms of positioning and related works / baselines) could also use improvement.

- The paper's related work is sparse and I think it is important to present the lineage of these models more carefully. The original (depth separable) LCSMs were independently developed by two lines of work: the implicit convolution (CKConv and FlexConv) line of work, and the SSM line of work (LSSL, S4, DSS/S4D, H3, MEGA/Megalodon, and many more). Even though I understand why the paper deliberately puts emphasis on LCSMs that are not SSMs, because this is where its results are most applicable to, the positioning is at times misleading (e.g. in paragraph 2 of the introduction, where LCSMs are implicitly defined as non-SSM models, even though LTI SSMs are in fact the original models that popularized LCSMs).
- It is odd that the paper is heavily anchored around the Hyena architecture, even though it does not actually do anything Hyena-specific. The experiments don't use an actual trained model or look at empirical performance, only the speed of an architecture, for which any model with a LCSM convolution (e.g. H3, to which Hyena is equivalent except for the choice of convolution kernel) could equivalently be substituted into the writing without changing the algorithmic results.
- A distinction is made that low-dimensional LTI SSMs cannot represent general LCSMs, which is true and where the paper's potential benefits can come from. However, current understanding of LCSMs is that they need to be defined using certain priors (e.g. baking in exponential decay as in SGConv and Hyena) that essentially are similar to the priors imposed by low-dimensional SSMs. Empirically, it is known that there is little difference between these models (e.g. https://arxiv.org/abs/2312.00678v1 Fig 1, which claims that H3 in fact performs better than Hyena, where the only difference is the choice of convolution kernel parameterization). Thus a major weakness of this paper is that it is currently only applicable to models that have better alternatives empirically.

Some of my other points are about the utility of such models. As of right now, there are no results that suggest that there exist general LCSMs that outperform efficient LCSMs.

6. In all benchmarks where controlled comparisons exist (e.g. not including the EVO model, where no third party reproductions exist or ablations between the Hyena parameterization vs other LCSM parameterizations), the performance of non-SSM LCSMs and SSMs are essentially the same.

7. E.g. as the authors note "S4, although primarily viewed as an SSM, is still SOTA on the Image section of the Long Range Arena tasks and requires a dimension equal to the sequence length." Actually S4 and variants (MEGA, etc.) all use a low dimensional SSM, and the majority of methods near SOTA on LRA are based on low-dimensional SSMs or equivalent. I will also point out that the authors' phrasing "although primarily viewed as an SSM" once again implies a false dichotomy between SSMs and LCSMs that is being perpetuated. *SSMs are simply a class of LCSM with additional properties.*

8. There is in fact a technical reason for this, which was touched on in the original review. As mentioned in point 4 above, *all* LCSMs have restricted expressivity. This is essentially tight, in the sense that any LCSM with $P$ parameters requires $O(PL)$ time to construct its convolution filter, so there is a fundamental tradeoff in the expressivity <-> training time of LCSMs; both implicit convolution models like CKConv/Hyena as well as SSMs attain this bound. So there is no intrinsic expressivity advantage to using a non-SSM LCSM over an SSM (unlike what is often implied by the paper; for example, pointing out that general convolutions cannot be represented by a low-dimensional SSM is misleading, as they cannot be represented by any other finite-parameter class of LCSM either). Thus the question to ask is not about expressivity but about whether a particular parameterization carries a helpful inductive bias. However, the best non-efficient LCSMs such as Hyena and SGConv actually bake in priors like exponential decay which intentionally give them inductive biases *more similar* to low-dimensional SSMs. Overall, current understanding of the community is that performant LCSMs are empirically indistinguishable from low-dimensional SSMs.

### Questions
I think the paper needs to position with respect to other types of LCSMs with more nuance. For example, it could benchmark how the proposed algorithm for general LCSMs compares to the inference speed of recurrent LCSMs; e.g. for a given sequence length $L$, at what recurrent state size does the speed of a recurrent SSM cross over the speed of the proposed algorithm? This would at least provide some more useful context for the reader interested in the pure algorithmic aspects.

However, overall, in order for this paper to be valuable to the machine learning community, it should be applied to actual models, and current understanding of LCSMs is that general LCSMs essentially do not benefit over low-dimensional LTI SSMs. The contributions are interesting from a purely algorithmic perspective, and the paper does suggest potential extensions beyond time-invariant convolutions. However, it is not clear whether this has any chance of being extended into performant models - no actual downstream model is proposed. Thus, I think that a conference such as ICLR is not the most appropriate venue for such a submission without anchoring the algorithmic contributions to real models. In order to increase my score substantially, I think the paper needs to show a practical utility, for example either
- Showing that there exist classes of models that the algorithm can be applied to that are not dominated by others (e.g. showing that some non-SSM LCSM model is actually faster or more performant than an equivalent SSM)
- Showing that there exist data-dependent extensions that outperform data-independent convolutions in modeling performance

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a method to speed-up the autoregressive inference of long convolution sequence models (LCSMs) to near linear time. The approach is based on findings from relaxed polynomial interpolation’s literature, which is gratefully adapted to convolutions.
The resulting algorithm results in important speeds-up both for the position-mixing components and end-do-end inference.

### Strengths
- The method is novel and offers interesting improvements in the inference speed of LCSMs.

- The paper offers interesting perspectives that could be used for the design of more efficient (causal, input-dependent) LCSMs in the future.

### Weaknesses
 - The main weakness of the paper is that the presentation, design decisions and final implementation of the method remains quite abstract, even after reading the paper multiple times. Given that the paper presents an inference strategy, it should be feasible to have an stand-alone implementation (at least for one layer) incorporated in the Appendix of the paper. This would give clarity to the final, concrete version of the algorithm. Specifically, while Algorithm 2 provides a high-level view of the end-to-end process, it lacks the necessary detail to understand how the core computations are performed. For instance, the exact procedure for applying the relaxed polynomial interpolation to the convolution operation is not clearly laid out in a step-by-step manner. The paper would benefit from a more detailed breakdown of how the $\tau$ function is integrated within the convolution, and how the intermediate results are stored and reused. A concrete example, detailing the data flow and transformations within a single layer, would significantly improve the clarity and reproducibility of the method.

- Next, I feel that the presentation of the paper could be improved. For example, the function $\tau$ –which is crucial for the method– remains undefined through the whole body of the paper up to Sec. 4.2, where it is briefly and loosely defined. It is mentioned that 7 possible versions were tested, but only 4 were mention-worthy. Then, it is mentioned that some are used, but it is not specified in which ranges and under which parameters one is preferred over the other. Given that this is core to the method, this should definitely be improved. The lack of a precise definition of $\tau$ early in the paper makes it difficult to follow the theoretical development and understand the practical implications of the method. The description in Section 4.2 is insufficient, as it does not provide a clear mathematical formulation or a detailed explanation of how the different implementations of $\tau$ are derived and how they relate to the relaxed polynomial interpolation. The paper should include a more rigorous treatment of $\tau$, including its mathematical properties and the specific algorithms used for its computation, along with a clear explanation of the trade-offs between the different implementations and how the optimal choice is made based on the input parameters.

### Questions
### Additional questions and observations

- Contribution 1. This is true, however, for clarity, I would recommend that the authors mention Laughing Hyena before making this claim to put in context that that method is not exact.

- Line 233. There’s a typo here that changes the whole meaning of the sentence. Please fix.

 ### Conclusion

While I believe that the core contributions of this paper are very valuable, I am not really convinced by the current presentation of the paper. I would recommend the authors to improve readability and make specific the different design decisions that make the paper. 

Do note that the contribution of this paper is rather an algorithmic one. Yet, the current very abstract depiction of the method makes it unnecessarily difficult to implement and reproduce. I am, therefore, only able to provide this paper a “weak acceptance” at this time. However, that if the authors were to improve over the weaknesses outlined here, I would be more than happy to increase my score.

### Soundness
4

### Presentation
3

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
This paper proposes a method for speeding up Long Convolution Sequence Models (LCSM)'s exact inference to quasilinear time, identifies the key properties that make this possible, and proposes a general framework that exploits these. The proposed approach is inspired by relaxed polynomial interpolation and uses a tiling method that minimizes memory movement and enhances computation sharing, allowing near-complete parallelization across layers in the architecture’s position-mixing component. Through a proof-of-concept implementation on Hyena, we demonstrate up to a 1.6× improvement in end-to-end inference time and a 50× speedup in the position-mixing part.

### Strengths
1. The paper addresses a fundamental issue in sequence models, particularly long convolution sequence models (LCSMs) like Hyena, where inference time scales quadratically with sequence length. The proposed framework reduces this to quasilinear time, achieving significant improvements by leveraging a tiling-based approach inspired by relaxed polynomial interpolation.

2. Besides speed, the paper focuses on reducing memory movement, a bottleneck in handling large models. It suggests methods for activation storage optimization and discusses adjustments for memory-constrained hardware, making the work relevant for deployment.

3. The paper presents thorough empirical results that demonstrate the proposed method's effectiveness. It reports up to 1.6x end-to-end improvement in speed for Hyena and a 50x speedup within the convolutional mixer component, which provides concrete evidence of practical impact.

### Weaknesses
1. While the study is well-documented, the experiments focus primarily on synthetic setups and Hyena. Additional tests on a broader range of sequence models, specifically those employing different mixing mechanisms, or with real-world tasks, such as language modeling or time-series forecasting, could further validate the framework’s generalizability. The current scope limits the assessment of the method's robustness across diverse model architectures and practical applications.

2. The framework's efficiency relies on data-independent filters for optimal performance. Although data-dependent filters can be supported, the paper acknowledges that doing so may lead to higher complexity, potentially doubling the computational cost due to the need for additional FFT calls, or additional constraints. This could limit the application in cases where data-dependent filters are essential, and the practical implications of this performance hit need more detailed analysis.

3. The framework assumes autoregressive causality, which could restrict its application to non-causal architectures. While the paper mentions this limitation, it would benefit from a more thorough exploration of how the framework could adapt to different model constraints, such as bidirectional processing or models that require global context without strict causal dependencies. The current assumption limits the method's applicability to a subset of sequence modeling tasks.

### Questions
1. The paper suggests applicability beyond LCSMs. Could the authors provide additional empirical results or theoretical discussion on adapting the method to different architectures, such as transformers, beyond high-level discussion?

2. While data-independent filters optimize the framework's efficiency, data-dependent filters could require modifications. Could the authors elaborate on practical adaptations to support data-dependent filters effectively, and whether the framework maintains similar efficiency in such cases?

3. The work compares primarily with the eager and lazy approaches. How does the proposed framework perform against other efficient models or architectures, such as those using efficient transformer variants?

4. The paper assumes causality in model design. Are there potential modifications to the framework that could apply it to non-causal architectures? This could expand the impact and applicability of the proposed method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces "Flash Inference", a novel framework for efficient inference in long convolution sequence models (LCSMs) employing a tiling strategy inspired by relaxed polynomial interpolation . The authors propose an algorithm that achieves quasilinear $O(L \log^2_2 L)$ time complexity for exact inference, improving upon the quadratic complexity of standard approaches without resorting to any approximation techniques. The work specifically demonstrates the method's effectiveness on Hyena architectures, achieving significant end-to-end speedup and even more significant improvement within the position-mixing component of the model. Beyond LCSMs, the authors identify key properties that enable such speedups and propose a general framework to guide future architecture design. The proposed approach further reduces memory movement and enables parallel computation across layers.

### Strengths
1. Technical Innovation and Soundness:
- The paper presents a mathematically rigorous approach to improving inference efficiency, with clear proofs and careful analysis of complexity bounds
- The implementation details are thoroughly considered, including memory optimization and parallelization strategies
2. Practical Impact:
- The achieved speedups (1.6× end-to-end, 50× for position-mixing) are significant and well-documented
- The method is exact rather than approximate, maintaining model fidelity while improving performance
- The framework extends beyond just LCSMs, providing valuable insights for future architecture design
3. Experimental Validation:
- Comprehensive empirical evaluation across different hyper parameters parameters ($B$, $M$, $D$)
- Careful ablation studies of different $\tau$ implementations
- Clear breakdown of performance improvements and their sources

### Weaknesses
1. Technical Presentation:
- The notation could be improved for clarity, particularly in handling subscripts that simultaneously indicate sequence position, feature dimension, and layer. For example, you could consider using superscripts to indicate features (channels) and/or paranthesis around the subscripts/superscripts for the layers. 
- the use of "$\mapsto$" notation on line 159 is imprecise; it should be $y\mapsto z$.
- Algorithm 1 should reference equation (3) for the definition of $\tau$ for better clarity.

2. Contextual Discussion:
- The discussion of approximate inference methods could be more nuanced. The statement about "defeating the purpose of using LCSMs instead of LTI SSMs" is overly strong, given that Hyena filters are intentionally underparameterized and some *implicit regularization* (convergence of the filters to ones that can be effectively represented by a truncated basis of complex exponential functions) is to be expected. Te reviewer suggests that the authors provide a more balanced discussion of the trade-offs between exact and approximate methods, considering the intentional underparameterization of Hyena filters and the potential benefits of implicit regularization.
- The introduction would benefit from a clearer distinction between prefilling and autoregressive generation phases in the complexity analysis. Elaborating on this could strengthen the clarity of how the method affects the performance of the system.
- The claim about "popular misconception" (line 109) regarding the realization theory of LTI systems could be better supported with appropriate citations. It is the reviewer belief that the this is not a misconception in the control theory literature as the problem of realization of LTI system has bee studied for more than 60 years  (e.g., Kalman and Ho 1960). Perhaps the authors could clarify on that.

3. Technical Specifics:
- The asymptotic complexity expressions should consistently specify the base of the logarithm ($log_2$)
- The parallelization discussion could benefit from more detailed analysis of the memory bandwidth implications
- The interesting extension to data-dependent filters, while covered in the appendix, could deserve more attention in the main text if supported by quality experiments (do we need input-dependent filters in LCSMs?)

### Questions
1. How does the performance of Flash Inference compare to existing methods when dealing with very long sequences (e.g., $L>$32K) in non synthetic scenarios? Are there specific challenges (other than memory) or additional optimizations possible at these scales?
2. Could you elaborate on how the tiling strategy might be adapted for architectures with more complex dependencies between layers? This seems particularly relevant for hybrid architectures that combine convolution and attention mechanisms.
2. The main limitation of the proposed method is certainly the linear growth of cache size with sequence lenght. How does this affect the practical benefits of exact vs approximate inference methods? In the approximate method, the cost of distillation can be amortized offline for a subsequent constant memory autoregressive generation. Moreover, one can trade additional memory (number of states in the SSM) for additional precision in representing the filters. Using a pre-trained LCSM, could you verify the accuracy-memory trade-off of the approximate vs exact method for practical sequence lengths? 
3. Have you considered how this framework might be extended to handle structured sparsity patterns in the filters? This could potentially lead to additional efficiency gains while maintaining the theoretical guarantees.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper develops a computation framework for efficient inference of long convolution sequence models (LCSMs). The proposed approach is based on relaxed polynomial interpolation, and can speed up LCSMs’ exact inference to the quasilinear time, as is shown by both complexity analysis and numerical verifications.

### Strengths
1. The paper is well-written and easy to follow. 
2. The complexity analysis regarding both the computation and memory is detailed. 
3. The experiments are also provided to numerically verify the effectiveness of the proposed method.

### Weaknesses
1. The main concern is about the novelty of this paper, particularly compared to the work by van der Hoeven and "dynamic FFT". It would be clearer if authors can provide more details about the differences or improvements of this work compared to former references. Specifically, the paper should clarify how the proposed relaxed polynomial interpolation method differs fundamentally from existing techniques like dynamic FFT, especially in terms of the underlying mathematical formulations and computational strategies. A more detailed comparison, perhaps including a table highlighting the key differences in algorithmic steps, memory access patterns, and parallelization strategies, would be beneficial.
2. The applied setting seems somewhat limited, since it currently works only for Hyena-related architectures. Does the proposed method have the potential to inspire further extensions for general state-space models (SSMs; as with an equivalent convolutional filter) and Transformers (despite reasons stated in Sec. 3.4)? It is unclear if the method's reliance on specific architectural features of Hyena limits its broader applicability. The paper should explore the theoretical limitations of applying this method to other architectures, such as those with non-convolutional layers or different types of state transitions. A discussion on the necessary conditions for the method to be effective in other models would be valuable.
3. The numerical experiments part can be strengthened by e.g. adding tests for multiple configurations of hyper-parameters. The current experiments lack a comprehensive exploration of the hyperparameter space. The paper should include a more systematic analysis of how different hyperparameter settings affect the performance of the proposed method, including the tile size, interpolation degree, and other relevant parameters. This would provide a more robust evaluation of the method's practical utility and its sensitivity to different configurations.

### Questions
1. Please kindly provide more details to the questions raised in the "Weaknesses" section. 
2. How about the case when the non-mixers’ runtime is dominant, e.g. the large MLP module is common in practice (such as Transformers in applications). Do the improvements shown in Fig. 2(a) & 3(c) become marginal? 
3. For Fig. 3(c), why is the non-mixers’ runtime less for Eager (NP) & Lazy (NP)? In addition, it seems that there is no reduction of mixers’ runtime of Hybrid compared to (Flash) FFT?

### Soundness
3

### Presentation
3

### Contribution
2

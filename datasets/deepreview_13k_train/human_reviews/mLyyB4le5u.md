# ParetoFlow: Guided Flows in Multi-Objective Optimization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
In offline multi-objective optimization (MOO), we leverage an offline dataset of designs and their associated labels to simultaneously minimize multiple objectives. 
This setting more closely mirrors complex real-world problems compared to single-objective optimization. 
Recent works mainly employ evolutionary algorithms and Bayesian optimization, with limited attention given to the generative modeling capabilities inherent in such data.
In this study, we explore generative modeling in offline MOO through flow matching, noted for its effectiveness and efficiency.
We introduce \textit{ParetoFlow}, specifically designed to guide flow sampling to approximate the Pareto front. 
Traditional predictor~(classifier) guidance is inadequate for this purpose because it models only a single objective. 
In response, we propose a \textit{multi-objective predictor guidance} module that 
assigns each sample a weight vector, representing a weighted distribution across multiple objective predictions.
A local filtering scheme is introduced to address non-convex Pareto fronts.
These weights uniformly cover the entire objective space, effectively directing sample generation towards the Pareto front.
Since distributions with similar weights tend to generate similar samples, we introduce a \textit{neighboring evolution} module to foster knowledge sharing among neighboring distributions.
This module generates offspring from these distributions, and selects the most promising one for the next iteration.
Our method achieves state-of-the-art performance across various tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents *ParetoFlow*, an innovative approach aimed at offline multi-objective optimization (MOO) that leverages the flow-matching generative modeling framework. The authors introduce two key modules: a *multi-objective predictor guidance module* that uses uniform weight vectors to direct sample generation toward approximating the Pareto front and a *neighboring evolution module* for sharing knowledge between distributions with similar objectives. These techniques are designed to improve coverage of both convex and non-convex Pareto fronts and enhance sample diversity.

### Strengths
- The integration of flow matching in offline MOO is a fresh perspective compared to the typical use of evolutionary algorithms or Bayesian optimization. This method captures the potential of generative models for addressing complex, multi-faceted optimization challenges.

- The proposed module that fosters information exchange among adjacent distributions is a standout feature. This knowledge-sharing mechanism supports enhanced exploration and refinement of solutions.

- This method was evaluated across diverse benchmarks, demonstrating state-of-the-art performance and outperforming existing MOO methods such as PROUD, LaMBO-2, and CorrVAE, especially in generating high-quality Pareto-optimal solutions.

- The provided code and training details are clear.

### Weaknesses
 - You only cited [1] to state that Flow matching outperforms Diffusion models, which I find insufficient. This is especially true in the context of multi-objective optimization, where specific problems require specialized analysis.

- Although the results on benchmarks with high-dimensional objectives, such as MO-NAS, are mentioned, there could be more detailed insights into how well the method scales with increased complexity in terms of computational cost and solution quality. Specifically, the paper lacks a detailed breakdown of the computational resources required for training and inference, making it difficult to assess the practical applicability of the method for very large-scale problems. Furthermore, while the method is evaluated on MO-NAS, there is no discussion of the specific challenges posed by the discrete nature of the search space and how the proposed approach addresses these challenges. A more detailed analysis of the encoding and decoding process for discrete architectures would be beneficial.

- The comparisons focus more on generative modeling approaches. A broader comparison that includes more traditional, non-generative MOO techniques could strengthen the context of ParetoFlow's advantages and limitations. For example, comparing against established evolutionary algorithms or decomposition-based methods would provide a more comprehensive understanding of the method's performance relative to the broader MOO landscape.

### Questions
1. How does ParetoFlow manage potential overfitting to specific tasks or datasets, given that it optimizes multiple objectives using a learned generative model?

2. Can the authors elaborate on the choice of the Das-Dennis method for generating uniform weights? Are there scenarios where alternative weight distribution methods could be more effective?

I am open to revising my score upwards if the authors can satisfactorily address these concerns during the discussion phase.

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
This paper proposes ParetoFlow, a novel method for offline multi-objective optimization (MOO) using flow matching. It introduces a multi-objective predictor guidance module and a neighboring evolution module to improve the efficiency and effectiveness of flow sampling in approximating the Pareto front. The paper presents extensive experimental results on various benchmarks, demonstrating ParetoFlow’s superior performance compared to existing MOO methods.

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed modules, multi-objective predictor guidance and neighboring evolution, provide a well-motivated approach to guiding flow sampling and promoting knowledge sharing among neighboring distributions.
3. The experimental results of ParetoFlow on various benchmarks are promising.

### Weaknesses
1. The paper mentions the computational cost of ParetoFlow but does not provide a detailed comparison with other generative modeling methods.
2. Providing some visualization results for the generated samples would be beneficial.

### Questions
1. Can the authors offer a case study for the generated architectures in terms of structure and performance on MO-NAS?
2. How to guarantee the validity of the generated samples? For instance, an architecture with the valid computational flow in the NAS task.

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
4

### Summary
This paper propose a new MOO method.

### Strengths
1. **The title is engaging and draws interest.**

2. **Overall, the paper is well-written and easy to follow.**

3. **Section 2.2 is clearly explained. However, could you elaborate on how using a normalizing flow would alter or improve the results?**

### Weaknesses
1. **Insufficient Mathematical Rigor**: The paper lacks adequate mathematical depth and rigor. Incorporating more detailed mathematical formulations, proofs, and theoretical underpinnings would strengthen the credibility and scholarly value of the work. For instance, the convergence properties of the proposed algorithm are not analyzed. A rigorous treatment of the algorithm's behavior, including conditions under which it converges to a Pareto optimal set, is missing. Furthermore, the paper does not provide a formal definition of the multi-objective optimization problem, which is essential for a clear understanding of the method's theoretical basis.

2. **Incorrect Formalization in Line 105**: The statement on line 105 is inaccurate. A Multi-Objective Optimization (MOO) problem cannot be "formally" formulated merely as a vector optimization problem. Such a formulation is more of an informal notational convenience rather than a formal definition. Clarification and correct formalism are needed here. The paper should clearly distinguish between the vector optimization problem and the MOO problem, highlighting the nuances of Pareto optimality and dominance relations.

3. **Unclear Purpose of Equation (9)**: The role and application of Equation (9) are not clearly explained. It is difficult to understand its significance and how it fits into the overall argument of the paper. Providing a thorough explanation or context for this equation would enhance comprehension. Specifically, the connection between the noise term and the exploration of the objective space is not well-established. The paper needs to clarify how the noise term influences the sampling trajectory and why this specific form of noise is chosen.

4. **Unconvincing Integration of EA and Flow Matching**: The combination of Evolutionary Algorithms (EA) and flow matching presented in the paper does not seem convincing. Additional justification, evidence, or examples demonstrating the effectiveness of this integration would help in substantiating this approach. The paper does not clearly articulate how the strengths of flow matching and EA are synergistically combined. It is unclear how the selection and mutation operators from EA are adapted to the flow matching framework and why this specific integration is superior to other possible combinations.

5. **Inappropriateness of Section 4.6 in Main Text**: Section 4.6 may not be suitable for inclusion in the main body of the paper. It might be more appropriate to place this section in an appendix or supplementary material to maintain the focus and flow of the main content.

6. **Unconvincing Experimental Results Using Hypervolume Metric**: The experiments conducted are not entirely convincing, particularly due to the exclusive use of the hypervolume (HV) metric. If alternative methods such as SMS-MOEA were employed, it is questionable whether the proposed method would perform as well as, or better than, SMS-MOEA. Including comparisons with such methods and using a variety of performance metrics could provide a more comprehensive evaluation. The paper lacks a thorough comparison with state-of-the-art MOO algorithms and does not justify the choice of the HV metric as the sole evaluation criterion. The use of other metrics like inverted generational distance (IGD) or epsilon indicator would provide a more complete picture of the algorithm's performance.

### Questions
see advantages and weakness.

### Soundness
3

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
This paper applies flow matching to offline multi-objective optimization. Authors propose a multi-objective predictor guidance module which generates weigts for each objective using Das-Dennis approach to guide the sample generation towards the Pareto front, and neighboring evolution module is proposed to enhance knowledge sharing between the generation of different weights. Experimental results show the effectiveness of the proposed method.

### Strengths
1. The concept of ParetoFlow is innovative and creative.

2. The experimental results show that the proposed method has promising performance on the tested problems and surpass the baselines.

### Weaknesses
1. The proposed method relies on the accuracy of the objective predictors, which might be a bottleneck on problems with complex landscapes and limited offline dataset.

2. It seems that the required weight vectors will grow exponentially (i.e., a problem with 10 objectives neesds at least 1024 vectors to ensure each objective has at least 2 weights). It may be time consuming to generate and sample using these weights, while less weights may not fill the PF.

### Questions
1. In Section 3.1 authors consider the case of non convex PF. I wonder whether such cases show up in the experiemnts? If so, does the designed filtering successfully process such cases?

2. In the Neighboring Update, the next state is the best one in the K nearest weight vectors, will it make a large ratio of vectors generate the same solution and lead to early convergence?

### Soundness
2

### Presentation
2

### Contribution
3

# Functional Homotopy: Smoothing Discrete Optimization via Continuous Parameters for LLM Jailbreak Attacks

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
\textcolor{red}{Warning: This paper contains potentially offensive and harmful text.}

Optimization methods are widely employed in deep learning to identify and mitigate undesired model responses. While gradient-based techniques have proven effective for image models, their application to language models is hindered by the discrete nature of the input space. This study introduces a novel optimization approach, termed the \emph{functional homotopy} method, which leverages the functional duality between model training and input generation. By constructing a series of easy-to-hard optimization problems, we iteratively solve these problems using principles derived from established homotopy methods. We apply this approach to jailbreak attack synthesis for large language models (LLMs), achieving a $20\%-30\%$ improvement in success rate over existing methods in circumventing established safe open-source models such as Llama-2 and Llama-3.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes the functional homotopy method, a novel optimization approach for LLM attacks. FH fintunes the LLM and solves a number of easy-to-hard problems, which are constructed via gradient descent. The results show a substantial improvement over different baselines.

### Strengths
- The paper is well-written and easy to follow
- The methodology is novel and well-motivated
- The proposed attack allows easy substitution of future attacks
- FH shows promising results

### Weaknesses
 - L81-82: "can retain" should be "have to retain"
- The efficiency comparison is based on the iterations instead of the runtime, which seems to be a fairer comparison.
- Missing related work. Consider including [1, 2]

### Questions
Questions:
- How much storage does it take to store all the LLMs?
- Is there ablation using another baseline for the discrete optimization for FH, e.g., AutoDAN or GCG?

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
2

### Summary
This paper introduces the Functional Homotopy (FH) Method, a novel optimization approach designed to tackle the discrete optimization challenges inherent in language models, with a specific application to synthesizing jailbreak attacks. The authors note that existing gradient-based techniques, effective in continuous spaces like image models, face difficulties when applied to the discrete token space of language models. The FH method addresses this by leveraging a functional duality between model training and input generation. The method involves transforming a difficult optimization problem into a series of easier ones, using a homotopy-based approach where model parameters and inputs are optimized in tandem. The paper demonstrates that this method achieves a significant improvement in attack success rates (20-30%) over existing techniques when tested on open-source models like Llama-2 and Llama-3.

### Strengths
The paper introduces an original optimization method, blending continuous and discrete optimization techniques in a way that has not been widely explored for language models. This approach brings a fresh perspective to the field of adversarial attacks.  The authors provide a strong theoretical foundation for their method, clearly explaining the duality between model training and input generation. The homotopy-based approach is well-grounded in optimization literature, which adds depth to the contribution. The demonstrated success of the FH method in improving attack success rates against robust language models is significant. The practical implications for AI safety research are noteworthy, especially in understanding and defending against potential vulnerabilities in LLMs. The paper is clearly written, with a logical structure that effectively guides readers through the problem, methodology, and experimental results. The use of diagrams, such as the illustration of the homotopy path, aids in understanding the method’s workings.

### Weaknesses
The paper does not thoroughly address the computational demands of the FH method. Randomly sample tokens
from the vocabulary to replace the token at that position can be time-consuming. Given the potential resource constraints in real-world applications, more details on runtime efficiency and how the method scales with model size would be beneficial.

### Questions
The authors mention issues with overfitting to specific malicious queries, especially when targeting outputs that models are trained to reject. Are there additional strategies or techniques that could be implemented to reduce this risk without compromising attack success rates?

While the method shows improvements in success rates, could the authors provide more comprehensive comparisons of computational efficiency, such as runtime and resource usage, relative to baseline methods? This would help in understanding the practical trade-offs of deploying the FH method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper trains the LLM to be less aligned and then attacks it with a greedy search for token replacements on the weaker versions of the model, gradually increasing the difficulty by reverting step by step to the aligned version.

### Strengths
1. The idea is interesting and novel in its approach to manipulating the model's parameters.
2. The empirical performance in terms of ASR appears strong.
3. The effort to provide evidence that the token gradient in GCG is not beneficial is appreciated, even though this has already been hypothesized.

### Weaknesses
1. The number of steps used for 'unalignment' must be decided beforehand. The procedure, if I understand correctly, is: conduct *N* steps to transition from parameter *p* to unaligned parameters *p'*. Then, iterate back and find an attack suffix for each *p_i* based on the previous one. This makes it difficult to determine if *p'* is sufficiently unaligned, and during the process of creating a new suffix, it is not possible to adjust to easier parameters when the attack does not seem effective.
2. The method introduces many additional hyperparameters (e.g., number of fine-tuning steps, number of GR steps per parameter set) and operational overhead, which are not discussed adequately (not even in RQ3). The authors should compare the attacks based on computational cost rather than steps, as fine-tuning is not factored into their 'step' metric.
3. The writing needs improvement. The text is often verbose, repeating the same points at different locations, and could be more concise. Additionally, there are inconsistencies in mathematical symbols, such as *p* being defined as the input (prompt) but is later used to refer to model parameters.

### Questions
1. I am curious about why the method works. I would understand if gradient optimization were involved and it was argued that the landscape is smoother, guiding the process to the next optimum. However, since the suffix is optimized with a greedy search, why is this more effective? If the main idea is just remaining at a broad minimum during random search, then the transferability from the base model to the weakest model should be higher, which does not appear to be the case.
2. In Figure 3, what does it mean for FH-GR to be a successful attack within 1 iteration? Does this mean only one parameter update, or does it start from the weakest model after *N* updates and do only one GR search?

### Review Summary:
The paper presents an interesting idea. However, in its current state, I am not in favor of accepting it. I believe more research into the method is necessary, further evidence should be gathered, and the writing should be improved. That said, I am open to revising my score if my concerns are addressed.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach called the Functional Homotopy (FH) method for solving discrete optimization problems in the context of jailbreak attacks on large language models (LLMs). The method leverages a duality between continuous model parameters and input generation, using an easy-to-hard problem-solving approach. The authors claim a 20%-30% improvement in success rates over existing methods when applied to LLMs such as Llama-2 and Llama-3.

### Strengths
* The paper introduces a novel functional homotopy method for jailbreak attacks on large language models (LLMs), building on the traditional homotopy framework used in optimization. Instead of directly solving the complex discrete optimization problem, the approach breaks it down into a series of progressively harder problems. Each solution from an easier problem is used as the starting point for the next, harder problem, which makes the optimization process smoother and more manageable.

* The experimental results show that this method delivers a 20%-30% improvement in success rates compared to baseline techniques when applied to state-of-the-art open-source models.

### Weaknesses
 * The proposed method appears overly simplistic, lacking both theoretical guarantees and in-depth analysis. The randomized search approach is basic and does not provide any assurance of optimality. Additionally, the complexity of performing a successful randomized search seems exponential with respect to the dimensionality of the problem. A formal theoretical analysis offering guarantees for the method would significantly strengthen the contribution.
* The baselines used for comparison also seem relatively weak. For instance, the gradient-based methods are naturally expected to perform poorly, given their myopic nature and disconnection from true gradient information. Furthermore, the datasets used for the experiments are small, making it difficult to draw definitive conclusions about the method’s effectiveness and efficiency. Stronger baselines would provide a more meaningful comparison.
* The algorithm's performance seems to be highly dependent on hyperparameter choices, such as the threshold, number of random search steps, and the search radius. A more comprehensive analysis on how to select these hyperparameters would provide valuable insight and improve the robustness of the proposed approach.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
3

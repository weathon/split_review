# LLaMoCo: Instruction Tuning of Large Language Models for Optimization Code Generation

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Recent research explores optimization using large language models (LLMs) by either iteratively seeking next-step solutions from LLMs or directly prompting LLMs for an optimizer. However, these approaches exhibit inherent limitations, including low operational efficiency, high sensitivity to prompt design, and a lack of domain-specific knowledge. We introduce LLaMoCo, the first instruction-tuning framework designed to adapt LLMs for solving optimization problems in a code-to-code manner. Specifically, we establish a comprehensive instruction set containing well-described problem prompts and effective optimization codes. We then develop a novel two-phase learning strategy that incorporates a contrastive learning-based warm-up procedure before the instruction-tuning phase to enhance the convergence behavior during model fine-tuning. The experiment results demonstrate that a CodeGen (350M) model fine-tuned by our LLaMoCo achieves superior optimization performance compared to GPT-4 Turbo and the other competitors across both synthetic and realistic problem sets. The fine-tuned model and the usage instructions are available at \url{https://anonymous.4open.science/r/LLaMoCo-722A}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces LLaMoCo, a framework for fine-tuning general-purpose Large Language Models (LLMs) to generate optimization code through instruction tuning. The authors construct a specialized code-to-code instruction dataset tailored for optimization tasks. They enhance the training process with techniques such as contrastive warm-up, data augmentation via rephrasing, and balanced sampling. These methods are evaluated across three pre-trained models of different sizes (S, M, L), showing significant performance improvements. An ablation study further validates the effectiveness of the proposed techniques. Overall, the paper presents a promising approach to adapting LLMs for the specialized task of optimization code generation.

### Strengths
1. Specialized Dataset Creation: The development of a tailored code-to-code instruction dataset is a significant contribution. It aligns the fine-tuning process closely with the target task and provides a valuable resource for future research in optimization code generation.
2. Innovative Training Enhancements: Implementing contrastive warm-up, data augmentation through rephrasing, and balanced sampling demonstrates a comprehensive strategy to improve model performance. These techniques address common challenges in model training, such as overfitting and data imbalance.
3. Comprehensive Evaluation and Analysis: Evaluating the framework across models of varying sizes offers insights into scalability and the impact of model complexity. The inclusion of an ablation study allows for a deeper understanding of how each training enhancement contributes to the overall performance.

### Weaknesses
1. Unexpected Performance Across Model Sizes: Table 1, 2 and 3 show that the performance of LLaMoCo-S, LLaMoCo-M and LLaMoCo-L are very similar. The results also show that LLaMoCo-S sometimes outperforms its larger counterparts (LLaMoCo-M and LLaMoCo-L), despite having significantly fewer parameters. This is counterintuitive and raises concerns about potential inefficiencies in leveraging larger model’s increased capacity.


### Questions
1. Investigate Model Performance Discrepancies: It would be beneficial to analyze why the smaller model occasionally outperforms larger ones. This could involve examining the training dynamics, learning rates, or potential overfitting issues in larger models. Providing insights or adjustments based on this analysis would strengthen the validity of the results.
2. Expand Baseline Comparisons: Could the authors add another baseline of ChatGPT o1-mini/o1-preview? Since o1-mini/o1-preview are reasoning/coding/math enhanced models. I expect it to perform better than ChatGPT 4o. These models are designed for coding tasks and would serve as competitive benchmarks to better evaluate LLaMoCo's performance. Incorporating such comparisons would contextualize LLaMoCo's performance within the broader landscape of code generation research. 
3. Enhance Robustness Evaluation: Assessing the models on out-of-distribution samples or real-world optimization problems beyond the dataset used for training could demonstrate the generalization capabilities and practical applicability of LLaMoCo, which could alleviate/address the concern of “Unexpected Performance Across Model Sizes”.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a data generation and instruction tuning method for optimization-problem-solving LLMs. The authors conduct comprehensive experiments to demonstrate the optimization capabilities of the instruction-tuned LLMs and analyze the contribution of each component of the method.

### Strengths
1. This paper introduces the first complete framework for training LLMs to solve optimization problems, including instruction-tuning dataset construction and detailed methods for training. The method is well-described and effective, making a significant contribution to the optimization community. 

2. The experiments demonstrate performance improvements on both synthetic and realistic problem sets. across different scales of LLMs, highlighting the generalization and effectiveness of LLaMoCo.

### Weaknesses
1. Lack of sufficient novelty. Several key components of the method follow prior work [1-3], particularly the instruction-tuning approach (Section 3.2), which reduces its originality. Although this paper introduces the first instruction-tuning framework for optimization tasks, it primarily applies standard training techniques. The authors should emphasize their main innovations more clearly in the paper.

2. Writing. Figure 1 does not effectively highlight the main differences between LLaMoCo and previous methods, which is overly simplified. The authors should include more details of the method. There are typos in the caption of Figure 2 (wither -> either). The capitalization of “LaTeX” in the full paper is inconsistent.

### Questions
1. What is the impact of dataset size on the training performance? Will the performance of the models continue to improve when using more data?

2. How to control the quality of the synthesized tasks? Can we ensure that unsolvable optimization problems or problems with only trivial solutions are not synthesized?

3. Why does the computational overhead of the trained models increase? (in Table 1)

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
This paper presents LLaMoCo, a pioneering framework that maps optimization problem descriptions directly to expert-level optimization code through instruction tuning. By creating a comprehensive dataset of (problem, best-solver) pairs and using a two-phase training strategy, even a small model (350M parameters) can surpass GPT-4 in selecting and generating appropriate optimizers for both synthetic and realistic optimization tasks.

### Strengths
1. 350M parameter model achieves 81.8% optimization performance vs GPT-4's 74.2% (without prompting) while using only 2.4K tokens vs 3.5K tokens.
2. Data pipeline converts 6000 problems to 32570 training pairs through systematic benchmarking of 23 optimizers across different configurations.

### Weaknesses
1. Zero-shot evaluation tested on only 8 realistic problems, requiring more cases to validate the claims.
2. GPT-4 baseline with vector search not evaluated.
3. Grid search necessity on original problems is subtle, some parameters are hard to set without careful data observation, requiring further validation of selection appropriateness.
4. The performance metric lacks a precise mathematical definition, making it difficult to assess the true impact of the method.
5. The paper does not provide sufficient analysis of the 350M parameter model's generated code quality, executability, and failure cases.
6. The relatively small performance gains observed when scaling from 350M to 7B parameters raises questions about what the model is actually learning.

### Questions
1. Further experiments needed to demonstrate the combined effect of SFT and alignment.
2. Grid search "best" performance criteria not clearly defined, benchmarking process lacks clear evaluation metrics for optimizer selection.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces LLaMoCo, a new framework for fine-tuning LLMs to solve optimization problems. The contributions of this paper are two-fold: (1) a novel fine-tuning dataset and (2) a new training warm-up strategy for training leveraging contrastive learning. Experimental evaluations demonstrate that LLaMoCo's models perform well on their held-out test set and realistic problems.

### Strengths
1. The authors have developed and plan to release a novel dataset designed to teach language models to solve optimization problems. This represents a significant contribution to both researchers and practitioners.

2. The experimental results are compelling. I especially appreciate Table 3, where the proposed method strongly performs on realistic optimization problems (rather than toy problems).

### Weaknesses
1. This paper lacks novelty. This paper primarily focuses on fine-tuning OSS LLMs for a specific domain. The main approach is straightforward from this perspective: the authors adjusted prompts (specifically, framing problem descriptions in Python or Latex) and developed a new dataset. Could authors emphasize the unique technical challenges associated with this domain?

2. The contrastive warm-up technique in this paper seems out of place. This technique does not appear to be specifically tailored to optimization problems. Could it be beneficial for fine-tuning in other domains as well? If not, what are the reasons? I would suggest separating this novel technique into a dedicated paper or clarifying how it suits the domain under discussion. The ablation study in Figure 4 is not very convincing, as it was tested with only a single configuration, making the results dependent on that specific setup.

### Questions
1. Is the current dataset format truly optimal? For instance, could leveraging CoT enhance performance? Similarly, would implementing multi-turn iterative improvements for optimization code be a promising approach?

2. Could the proposed method be compared with previous non-LLM-based automatic algorithm selection approaches? Automatic algorithm selection for optimization problems is a well-established research area with a rich body of existing work.

3. Could the specific technical challenges unique to this optimization domain be highlighted? (see Weakness 1)

4. Would it be reasonable to separate the contrastive warm-up technique into a standalone paper or clarify that this technique is highly specialized for the domain under consideration? (see Weakness 2)

### Soundness
3

### Presentation
3

### Contribution
2

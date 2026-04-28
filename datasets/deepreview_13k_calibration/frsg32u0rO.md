# Block Verification Accelerates Speculative Decoding

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Speculative decoding is an  effective method for lossless acceleration of large language models during inference. It uses a fast model to draft a block of tokens which are then verified in parallel by the target model, and provides a guarantee that the output is distributed identically to a sample from the target model. In prior works, draft verification is performed independently token-by-token. Surprisingly, we show that this approach is not optimal. We propose \emph{Block Verification}, a simple draft verification algorithm that verifies the entire block jointly and provides additional wall-clock speedup. We prove that the proposed mechanism is optimal in the expected number of tokens produced each iteration and specifically is never worse than the standard token-level verification.
Empirically, block verification provides modest but consistent wall-clock speedups over the standard token verification algorithm of 5\%-8\% in a range of tasks and datasets. 
Given that block verification does not increase code complexity, maintains the strong lossless guarantee of the standard speculative decoding verification algorithm, cannot deteriorate performance, and, in fact, consistently improves it, it can be used as a good default in speculative decoding implementations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new algorithm for draft verification for speculative decoding for LLMs. Speculative decoding is a method that accelerates the inference process of LLMs using predictive heuristics to produce “drafts” of the likely next tokens the LLM will generate. These drafts must go through a verification process to determine whether or not they should be accepted, depending on how well they fit the target model’s distribution. The authors argue that the prior state-of-the-art approach for draft verification, Token Verification, is not optimal, since it considers the tokens one by one. The authors instead propose a method to consider the tokens as a block by considering their joint probabilities. The authors also demonstrate that their method accepts more tokens on average than the original Token Verification approach, which is more efficient in the long run. Their experimental results demonstrate that despite the standard overheads of LLM inference, the Block Verification algorithm outperforms the Token Verification algorithm in terms of wall clock speedup.

### Strengths
Overall, the paper is well written and the problem is clearly stated.

The theoretical proofs are sound to the best of my knowledge.

### Weaknesses
The paper does not provide sufficient evidence that it provides a considerable speedup.
Speedup is from a higher acceptance rate. The paper is using  PALM-2-XXS and XXXS. At this model size, answers tend to be quite bad, which makes it hard for actual response evaluation.

It was not clear how the probabilities for all subblocks are calculated.

# Minor comments 

Page 7, line 336: “I.e., it measures” should be “Specifically, it measures”

Page 8, line 425: “all valid verification algorithm” should be “all valid verification algorithms”

Page 8: I think Figure 4 should be labeled as a Table instead of a figure

### Questions
- How will the speedup results scale when using larger models?

- How are probabilities of all subblocks calculated?

 - Page 7, line 334: How realistic is this experimental setting? How many drafts are usually produced during speculative decoding, and how many copies of the model would we need for evaluating?

## Post-rebuttal comment

The authors addressed the questions raised in my review, and I have increased my score accordingly.

### Soundness
4

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
This paper introduces Block Verification, a novel algorithm designed to accelerate speculative decoding in large language models. Unlike traditional token-by-token verification, Block Verification evaluates and accepts a group of tokens (a "block") together. This method achieves faster generation speeds without compromising output quality.

### Strengths
1. **Block Verification** improves efficiency by verifying token blocks rather than individual tokens in speculative decoding, preserving the same distribution.

2. Block verification achieves consistent 5–8% speedup and is broadly applicable across models and datasets.

3. Block verification is easy to implement, with minimal modifications to existing speculative decoding systems.

### Weaknesses
1. Consistency in final distribution does not guarantee identical generation sequences. For instance, the large model might generate "ABC" while the small model generates "ADC." It’s possible that in the context of "ADC," the next token’s distribution aligns between the models, but under greedy decoding, the large model should ideally follow "ABC" rather than "ADC." The authors state that block verification accepts more tokens than token verification. In the case of greedy decoding, does this imply potential token differences? Would such differences impact the accuracy of the answer, or would block verification revert to token-by-token verification?
2. The explanations of the formulas and algorithms lack intuitive clarity, making comprehension more challenging, even though the modifications from token verification are not large.

### Questions
1. In the appendix, a batch size of 8 was used to compare with tree attention. What batch size was used in the main experimental section?
2. How does the performance compare with Medusa/Eagle's static tree attention?

### Soundness
3

### Presentation
2

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
The paper introduces a novel verification algorithm called the block verification method, which enhances the efficiency of speculative decoding in large language models (LLMs). This method contrasts with the traditional Token Verification, which optimizes the verification of token blocks to increase efficiency. The study demonstrates that Block Verification outperforms existing methods regarding the expected number of generated tokens (called the block efficiency) and wall-clock times while providing a theoretical guarantee of optimal performance under given conditions. Empirical evaluations show improvements across various tasks, confirming its effectiveness without additional code complexity.

### Strengths
- The paper provides solid theoretical guarantees, ensuring that the proposed method does not compromise the output distribution.
- The experiments validate the practical benefits, with performance gains across a diverse set of tasks.
- The proposed algorithm does not increase code complexity, making it easy to integrate into existing LLM architectures.
- The paper highlights how Block Verification compares favorably to related methods, strengthening its contribution.

### Weaknesses
 - The depth of proofs might be challenging for practitioners without a strong mathematical background, potentially limiting the paper's audience.
- There is a typo in the manuscript: page 8, line 413: deocding -> decoding

### Questions
- Are there specific conditions or types of LLM architectures where the performance gains of Block Verification may be more pronounced or limited?
- How does the algorithm handle edge cases where the distributions of the drafting and target models diverge significantly?

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
4

### Summary
This paper studies the problem of optimizing speculative decoding from an algorithm level to achieve inference acceleration. The key idea behind this paper is the observation that verifies multiple draft tokens in a block jointly, rather than token-by-token, can bring improvement in mean accepted tokens, which leads to the wall-clock speedup for LLM inference. Based on the idea, the paper proposes a simple block verification algorithm, which is plug-and-play for some existing speculative decoding methods. The authors theoretically show that block verification is lossless and better than standard speculative decoding, making it a stronger default implementation of speculative decoding. The experiments demonstrate that block verification modestly but consistently improves the mean accepted tokens and the final wall-clock speedup.

### Strengths
1. The introduction of the block verification in the full distribution is clear and easy to understand, and the paper is well-written with clear explanations to the block verification algorithm.
2. This method shows great simplicity and is easy to use. It does not incur additional computation or memory overhead, and is very easy to implement. 
3. The authors theoretically show that block verification is lossless and better than standard speculative decoding, making block verification a stronger default verification for speculative decoding.

### Weaknesses
While I really appreciate the simplicity of the method, the novelty and the contributions of the paper are a little weak for me. The reasons are:

1. The motivation that *"verifying multiple draft tokens token by token is not optimal"* is very similar to the motivation in Tree Monte Carlo (TMC) [1], which alleviates the novelty of this paper. Given the empirical results that block verification only brings 5%~8% speedup, I doubt the technical contributions of block verification. The block verification seems more like a trick with theoretical support.
2. There lacks a significant discussion about the decoding temperature $T$ in LLM inference, and the authors do not report the temperature in the experiment details. **In my understanding, the block verification can only bring speedup with $T > 0$, as the block verification degenerates to the token verification in greedy decoding ($T=0$).** Please correct me if I have any misunderstanding. While speculative decoding provides maximal speedup in greedy decoding settings for some specific tasks, such as coding and math reasoning, block verification cannot provide improvement on these tasks. Besides, additional experiments to investigate the influence of different decoding temperature are necessary.
3. Currently, I think there exists a large room (more than 1 page) to conduct more experiments.
   - Experiments for more LLM combinations (e.g. Llama family [2] and Vicuna [3]) across more benchmarks (e.g. MT-Bench [4] and SpecBench [5]) **with different temperature settings**.
   - Experiments for combining block verification to some latest speculative decoding methods (e.g. Medusa [6] and Eagle [7]).

I know that conducting a wide range of evaluation experiments are costly and time consuming, and I will increase my score if the authors clearly address my concerns.

### Questions
I would like to raise some questions to improve the manuscripts.

1. Could you provide a more detailed explanation to the motivating example with partial information? You have mentioned "with block verification" in Line 124, but it is not clear how block verification works in this section.
2. Existing speculative decoding methods mainly adopt a tree-based verification manner, which can significantly enhance the mean accepted tokens. Could you provide some explanation how block verification works in a tree-based verification manner?
3. Could you provide a more detailed theoretical assumptions for Definition 1, Theorem 1 and Theorem 2? Besides, I think the section Theoretical Guarantees can be further improved by providing some intuitive explanation (e.g. why block verification is optimal for any valid draft verification algorithm), as this can help readers to understand the advantages of block verification over TMC.

### Soundness
3

### Presentation
3

### Contribution
3

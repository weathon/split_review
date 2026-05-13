# LLMs Can Plan Only If We Tell Them

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Large language models (LLMs) have demonstrated significant capabilities in natural language processing and reasoning, yet their effectiveness in autonomous planning has been under debate. While existing studies have utilized LLMs with external feedback mechanisms or in controlled environments for planning, these approaches often involve substantial computational and development resources due to the requirement for careful design and iterative backprompting. Moreover, even the most advanced LLMs like GPT-4 struggle to match human performance on standard planning benchmarks, such as the Blocksworld, without additional support. This paper investigates whether LLMs can independently generate long-horizon plans that rival human baselines. Our novel enhancements help achieve state-of-the-art results in planning benchmarks out-competing prior methods and human baselines all autonomously.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates whether Large Language Models (LLMs) can effectively generate long-horizon plans autonomously, without requiring external verification tools or complex frameworks. The authors introduce AoT+ (Algorithm-of-Thoughts Plus), an enhanced prompting technique that builds upon the original Algorithm of Thoughts (AoT) approach. The paper suggests that LLMs may possess latent planning capabilities that can be activated through appropriate structuring of the problem-solving process, without requiring external verification tools or complex frameworks.

### Strengths
The paper presents a novel perspective challenging both overly pessimistic and optimistic views of LLMs' planning capabilities.
The AoT+ innovations are creative combinations of existing ideas since it uses periodic state regeneration to manage attention/cognitive load.
There is comprehensive empirical evaluation across multiple challenging benchmarks, such as clear ablation of components through comparison of AoT vs AoT+
The paper has well-structured progression of ideas from problem motivation to solution.

### Weaknesses
The paper focuses heavily on successful cases but lacks systematic analysis of where AoT+ fails.
While the paper compares AoT vs AoT+, it doesn't fully isolate the impact of each innovation.
The AoT+ assumes we have a pddl instance of the problem, so I'm not sure if this method is scalable to general domain.

### Questions
Is there any scalable way to promote AoT+?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the planning capabilities of Large Language Models (LLMs) and presents an improved prompting technique which authors refer to as AoT+ because the method has been built on a previous method referred to as AoT. While current LLMs exhibit limited efficacy in complex planning tasks that demand multi-step, long-term reasoning, traditional methods such as Chain-of-Thought (CoT) and Tree-of-Thought (ToT) prompting encounter notable challenges due to lack of integrated error correction which limits their performance in planning scenarios. Both CoT and ToT lack the flexibility to backtrack, resulting in inadequate performance on benchmarks like Blocksworld. AoT that this paper has been built on enhances planning accuracy by incorporating human-like intuition and backtracking strategies. The proposed AoT+ technique introduces periodic structured state generation, which reiterates the problem state to help LLMs concentrate on pertinent information and reduce cognitive overload, along with random trajectory augmentation that uses random solution paths interspersed with correct steps, facilitating easier prompt creation while ensuring high accuracy. The effectiveness of AoT+ is validated through various experiments demonstrating its superior performance over existing methods across various tasks, including Blocksworld and Logistics, without the need for external verification tools. By utilizing structured prompts that help LLMs in state management and heuristic search, AoT+ also decreases token usage and computational time compared to other frameworks, enhancing its practicality for real-time applications.

### Strengths
Although the work has been built on existing AoT work, it still shows several strengths including: 
- Achieving state-of-the-art performance across complex planning benchmarks without the need for external verification tools, 
- Unlike approaches like Tree-of-Thought (ToT) that require extensive API requests and computational resources, AoT+ operates efficiently within a single-prompt framework, cutting down on token usage and latency. This improvement is also observed in AoT but token counts in AoT+ is more efficient.
- The use of random solution trajectories in AoT+ (instead of rigid, human-crafted sequences) makes it easier to generate prompts and apply the method across various planning problems.
- By leveraging memoization-inspired techniques for periodic state regeneration, AoT+ helps to improve issues around state hallucination (errors in tracking problem states), enhancing the model’s ability to stay on track over multi-step tasks.
- AoT+ demonstrates consistent performance improvements across various LLMs indicating its model agnostic nature.

### Weaknesses
Authors have done great work, and can potentially improve the paper more by addressing the following:
- In terms of presentation I expect a more clear diagram explaining different stages of the proposed method. It took me some time to get a better sense of the proposed method by going through the details in methodology section. 
- While AoT+ performs well on the benchmarks reported in the paper, evaluation on real-world planning tasks like pathfinding for robotics would strengthen the work.
- While AoT+ addresses state hallucination issues, the paper doesn’t provide a detailed error analysis of where these hallucinations occur. Identifying specific failure points would offer valuable insights for refining state-tracking strategies.

### Questions
- Can you provide specific examples of common failure modes for AoT+, particularly regarding state hallucinations? Are there particular problem types or scenarios where these issues are more prevalent?
- How interpretable are the decision paths generated by AoT+? Can users trace the model’s reasoning steps and identify where an error may have occurred in the planning sequence?
- Would incorporating intermediate reward structures within AoT+ improve long-horizon planning accuracy by incentivizing the model to reach sub-goals?

### Soundness
3

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
4

### Summary
This paper explores the capabilities of LLM in autonomous planning, addressing their previous limitations when compared to human performance. Further, this paper proposes a new prompting method that enable LLMs to generate long-horizon plans autonomously.

### Strengths
- It presents a significant advancement in the autonomous planning capabilities of LLMs, demonstrating their potential to match or exceed human performance.
- This paper proposes a prompting strategy to generate long-horizon plans.

### Weaknesses
 - First, the identification of your performance gap has already been established[1].
- However, several key baselines are missing. Although significant research addresses planning optimization strategies, much of it does not conduct experiments in the blocksworld domain [2-4]. Furthermore, baseline [5], which even operates in blocksworld, has not been directly compared.
- Given that your method relies on search-based techniques, it would be beneficial to include comparisons with MCTS-Decoding or A*, as these are also search-based approaches. Please explain why these specific search-based approaches were not included.

### Questions
See Weakness for more details.

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
This paper proposes AoT+, a new prompting technique based on the previous work AoT, in research of LLM's ability for planning. The authors analysed the limitations of previous work, such as CoT, ToT, AoT. And then as a pre-study, it is showed that using random solution traces will not degrade the performance in comparison to AoT.
The authors further hypothesised that state hallucinations are due to continuous recomputation and tracking of the current state after each action. Based on this hypothesis, the authors introduced memoization in AoT+, inspired by dynamics programming. It is further shown that the attention weighs more on non-solution steps in AoT+.
The results demonstrate AoT has satisfactory performance improvement against other baselines and reduces the token usage.

The proposed method is based on previous AoT together with memoization and random traces. The method is simple yet effective. The paper shows promising results and improvement in comparison with baselines.  However, The paper itself lacks explanation in implementation of the proposed method. For example, it is unknown that how the authors interweave the correct solution path with random trajectories in 4.1 or how is memoization done in 4.2. Furthermore, the experiments can be done in a more consistent setting and more human performance data should be compared to support "out-competing human baselines". Until these concerns are resolved, this paper should be considered for a weak reject.

### Strengths
* The paper conducted proper experiments on attention to support the hypothesis about state hallucination. 
* The proposed method shows promising results in higher performance and lower token usages.

### Weaknesses
 * This paper would benefit from examples of AoT and AoT+, similar to how it benefits from examples of CoT.
* The observation that random in-context examples does not hurt performance is not new. For instance Min 2022 (https://arxiv.org/abs/2202.12837) presents a study of what makes ICL work. I quote from their abstract: "randomly replacing labels in the demonstrations barely hurts performance on a range of classification and multi-choice tasks, consistently over 12 different models including GPT-3".
* The authors can improve the illustration of the results by showing variance, confidences interval and other related statistical metrics, for example, in Table 3.
* The author claims that the proposed method out-competes prior methods and human baselines. However, only human performance in Logistics is compared and only AoT+ with GPT4 can slightly outperform human performance.
* Figure 1 and Figure 4 is not informative. Furthermore, the paper itself lacks descriptions of actual details of pipeline.
* Though experiments to verify random solution traces and memoization are conducted, it is noticed they are done in different models and/or domains. It would be more convincing for extra ablation study under same settings in Section 5.2 main results.
* The hypothesis in Section 4.2, "that these hallucinations stem from the LLM’s need to continuously recompute and track the current state after each action, potentially overwhelming its computational capacity as the solution trace grows longer", though partially supported by a experiment in attention, is not fully explained or validated over the length of solution trace.

### Questions
* I think there might be a grammar error with the sentence: (L339) "Table 3 demonstrates the more structured attention mechanism as a shift towards the visited states, resulting from our AoT+ approach with memoization." How is "memoization" implemented? What is the exact prompt modification? Why is this not presented in the main paper? Why does memoization prevent state identification?
* What does CoT-SC mean in Table 1? It is not explained in the paper.
* In Section 4.2: What specific version of LLaMA-13B did you use?
* For random solution trajectories, what is the percentage of solution path? 
* How do you incorporate memoization into the proposed method?
* Readability of figure 1 and figure 4 should be improved.
* Figure 3 should be referred as a Table.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores various aspects of planning and problem-solving using language models, focusing on whether LLMs can independently generate long-horizon plans that rival human baselines. The authors introduce novel enhancements to the Algorithm-of-Thoughts (AoT), termed AoT+, which achieve state-of-the-art results in planning benchmarks, surpassing prior methods and human performance—all autonomously. These enhancements, including Periodic Structured State Generation and Random Trajectory Augmentation, significantly improve LLM performance, suggesting that LLMs may have latent planning capabilities that can be unlocked through the right combination of context, structure, and guidance.

### Strengths
The paper presents a highly original approach to addressing the limitations of large language models (LLMs) in autonomous planning. It introduces the Algorithm-of-Thoughts (AoT+), an enhanced prompting technique that builds upon the Algorithm of Thoughts (AoT) approach. By activating what the authors term "System 3 thinking," a more deliberate decision-making process, the paper challenges the perceived boundaries of LLMs in complex planning tasks. The use of random solution traces and memoization to improve the performance of LLMs in planning further highlights the novelty of this work.

The paper maintains a high standard of quality in terms of its depth of analysis. It conducts experiments with a diverse set of language models and various prompting strategies, resulting in a comprehensive evaluation of the proposed methods. The authors effectively communicate complex concepts through clear figures and tables, and the structure is logical and easy to follow. The paper begins by identifying the limitations of prior work, proceeds to verify the efficacy of the proposed techniques through experiments, and concludes with an extensive evaluation of its findings.

By addressing LLMs’ limitations in planning tasks and proposing novel enhancements, this paper significantly contributes to advancing the problem-solving and decision-making capabilities of language models.

### Weaknesses
AoT+ requires explicitly restating and caching the current problem state throughout the solution process, which introduces additional complexity. This can demand extra effort in crafting effective state representations, and may be particularly challenging in tasks where the state is difficult to define or capture, such as in ALFWorld. Specifically, the method's reliance on a complete and accurate representation of the state at each step could lead to error propagation if the state representation is flawed or incomplete, potentially hindering performance in complex environments where the state is not easily observable or definable. The need to maintain a cache of these states also introduces a memory overhead, which could be a limiting factor for very long planning horizons or in resource-constrained settings.

Regarding the token count comparison table, it would be more comprehensive to include other baselines, such as CoT and AoT, to provide a fuller comparison. This would allow for a more nuanced understanding of the computational cost of AoT+ relative to other established methods, and help to contextualize the trade-offs between performance and resource usage. Without these comparisons, it is difficult to assess whether the performance gains of AoT+ justify the increased token usage.

The paper does not specify which version of the Claude model is used in the main experiments (Claude 3.5, Sonnet?). Providing this information would enhance clarity and reproducibility. The lack of specificity makes it difficult for other researchers to replicate the results and verify the claims made in the paper. Furthermore, the absence of this information raises questions about the generalizability of the findings across different model versions.

The paper lacks details on the implementation of memoization, which makes it somewhat unclear. The specific mechanisms for storing and retrieving cached states are not described, which makes it difficult to understand how the system avoids redundant computations and ensures consistency. This lack of clarity hinders the reproducibility of the work and makes it difficult to assess the practical implications of the memoization strategy.

### Questions
Why might using random trajectories, rather than carefully crafted ones, provide greater flexibility and generalizability as prompting strategies for planning problems? In the context of this paper, crafting examples for Blocksworld as well as other tasks appears relatively straightforward and requires minimal effort.

What considerations should be made when representing complex states, such as those in environments like ALFWorld?

How is memoization actually incorporated in AoT+? Does it involve cache the tokens for problem definitions?

### Soundness
4

### Presentation
3

### Contribution
4

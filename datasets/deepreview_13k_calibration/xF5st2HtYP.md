# Adaptive Strategy Evolution for Generating Tailored Jailbreak Prompts against Black-Box Safety-Aligned LLMs

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
While safety-aligned Large Language Models (LLMs) have been secured by extensive alignment with human feedback, they remain vulnerable to jailbreak attacks that exploit prompt manipulation to generate harmful outputs. Investigating these jailbreak methods, particularly in black-box scenarios, allows us to explore the inherent limitations of such LLMs and provides insights into possible improvements. However, existing black-box jailbreak methods either overly rely on red-teaming LLMs to execute sophisticated reasoning tasks, such as diagnosing failure cases, determining improvement directions, and rewriting prompts, which pushes them beyond their inherent capabilities and introduces uncertainty and inefficiency into the refinement process, or they are confined to rigid, manually predefined strategy spaces, limiting their performance ceiling. To enable a sustained and deterministic exploration with clear directional guidance, we propose the novel Adaptive Strategy Evolution (ASE) framework. Specifically, ASE innovatively decomposes jailbreak strategies into modular key components, dramatically enhancing both the flexibility and expansiveness of the strategy space. This also allows us to shift focus from directly optimizing prompts to optimizing the jailbreak strategies. Then, by leveraging a genetic algorithm (GA) for strategy components' selection and mutation, ASE could replace the uncertainties of LLM-based self-adjustment with a more systematic and deterministic optimization process. Additionally, we have also designed a new fitness evaluation, that emphasizes the independence of scoring criteria, provides highly accurate and reliable feedback, enabling precise and targeted refinement of jailbreak strategies. Experimental results further demonstrate that ASE achieves superior jailbreak success rates (JSR) compared to existing state-of-the-art methods, especially against the most advanced safety-aligned LLMs like  GPT-4o, Claude-3.5, and even o1.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
They present a novel approach to jailbreaking LLMs in black-box settings by leveraging evolutionary algorithms. The ASE framework divides jailbreak strategies into four modular components—Role, Content Support, Context, and Communication Skills—expanding the possible strategy combinations and enabling dynamic adaptation.

### Strengths
1.	Adapts insights from evolutionary algorithms to LLM jailbreaking, breaking down the pipeline into four distinct components.

2.	Positive experimental results: Experimental outcomes show that ASE achieves higher JSRs with fewer queries compared to existing methods across several models.

### Weaknesses
I appreciate the authors’ efforts but would like to point out the following:

1.	The design in **Component-Level Strategy Space** seems artificial and arbitrary. The authors argue that “these components perfectly align with how humans are more easily persuaded,” which is a strong statement lacking evidence. In designing red-teaming algorithms for LLMs, significantly more investigation is needed to justify such a design beyond human-like analogies and heuristics, which do not align with academic rigor. The choice of Role, Content Support, Context, and Communication Skills as the four components appears to be based on intuition rather than a systematic analysis of the factors that influence LLM vulnerability. There is no clear explanation of why these specific components were chosen over other possible categorizations, nor is there a discussion of how these components interact with each other to achieve a jailbreak. This lack of a rigorous, empirically-driven basis for the component design is a significant weakness.

2.	Regarding the **Fitness Evaluation**, the design also relies on heuristics that make the algorithm feel less reliable, particularly with features like “keyword matching.” What advantages does this offer compared to a reward model that labels the answer’s harmfulness? The use of keyword matching as a component of the fitness function introduces a potential source of brittleness and bias. Keyword matching is a superficial approach that may fail to capture the nuances of harmful content, leading to both false positives and false negatives in the evaluation of jailbreak attempts. This reliance on a simplistic heuristic undermines the robustness of the fitness evaluation and raises concerns about the reliability of the results.

3.	In terms of the **experiments**, I believe the focus is misplaced. The authors make strong claims about “expanding the search space and allowing for precise, efficient strategy refinement,” yet I could not find any specific evidence to support this. The paper's algorithm, compared with other works, centers on adaptive evolution, but only JSR is shown. What about the structure and behavior variations within the population? I could not find compelling evidence to justify the complex design of such an evolution algorithm, which seems to introduce a high barrier to practical use and deployment. The experimental results primarily focus on Jailbreak Success Rate (JSR) and query efficiency, but lack a detailed analysis of the evolutionary process itself. There is no discussion of how the population of jailbreak strategies evolves over time, what types of strategies emerge, and how the different components of the strategies are combined and modified. This lack of insight into the evolutionary dynamics makes it difficult to assess the effectiveness and efficiency of the proposed approach.

4. **Scalability and computational cost** are concerned, given the computationally intensive nature of population-based algorithms.

### Questions
- The authors propose breaking down jailbreak strategies into Role, Content Support, Context, and Communication Skills, claiming these align with persuasive human behaviors. How can we be sure these components genuinely improve jailbreak efficacy, given the lack of empirical justification? Could there be other, more effective component structures, or are these simply intuitive choices without systematic validation?

- If the initial population is not well-chosen, could ASE converge to suboptimal solutions, reducing its effectiveness?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the limitations of current jailbreak methods for safety-aligned Large Language Models (LLMs), particularly in black-box scenarios where models are resistant to prompt manipulation for harmful outputs.  The authors argue that existing methods often either depend too heavily on red-teaming LLMs (pushing their reasoning capacities) or rely on rigid, manually predefined strategies, which limits their adaptability and effectiveness.  To address this, they introduce the Adaptive Strategy Evolution (ASE) framework, which decomposes jailbreak strategies into modular components and optimizes these through a genetic algorithm.  This approach provides a structured, deterministic path to refining jailbreak methods, along with a new scoring system for feedback, resulting in higher jailbreak success rates (JSR) compared to existing approaches.

### Strengths
1. This paper is well-written and easy to understand.
2. As a black-box jailbreak method, the ASE framework is well-performed.
3. The method is simple and effective.

### Weaknesses
 1. I concern on the complexity and resource requirements. ASE’s reliance on genetic algorithms and modular strategy decomposition could be computationally intensive, which might limit its practical applicability for smaller research teams or resource-constrained environments. Is it possible for you to provide runtime, or memory usage, or hardware specifications used for the experiments.  Additionally, suggesting a comparison of these requirements to existing methods.
2. No other obvious weakness.

### Questions
1. See weakness. How does the computational cost of ASE compare to existing jailbreak methods, particularly in large-scale testing scenarios? If you have enough to rebuttal, please compare ASE's scalability to that of baseline methods as the dataset size increases.
2. I wonder whether you have tried to propose a defense framework against ASE? How existing defense mechanisms might perform against ASE？

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
5

### Summary
This paper introduces a new jailbreak method for large language models, namely ASE. It involves three key steps. First, it decomposes jailbreak strategies into four modules, each of which can be implemented differently. This process constitutes a large search space. ASE then utilizes a genetic algorithm to perform optimization in this space, with a newly designed fitness function. The authors demonstrated the effectiveness of ASE on two tasks, in which it exhibited superior performance compared to previous methods when attacking closed-source models like GPT-4.

### Strengths
- The decomposition of jailbreak strategies into different independent modules appears novel.
- The evaluation is thorough.

### Weaknesses
 - After reading the manuscript, I find this work to resemble more of an engineering design. For example, the authors did not introduce in detail how each component in the search space can be implemented. While there is a table in the appendix describing this, I wonder what protocols or criteria were employed to design this space. Without this information, it is hard to be convinced that rigorous efforts were involved in this design; it seems more like a demo that could be generated by simply prompting an LLM. Also, while the authors regarded their fitness function as a contribution, the four-point scoring with an additional term is a basic engineering trick—all that’s needed is to replace the evaluation prompt for the LLM with a more fine-grained one, which could itself be generated by an LLM. Finally, the core of the proposed method is a basic GA, which may be too straightforward for a prestigious conference like ICLR. More importantly, the authors did not address questions like why they specifically chose GA over other large-scale optimization methods in the literature. Additionally, could the original GA be directly employed for this task, or is this the optimal design choice? There are many similar questions, but unfortunately, the authors did not discuss these matters in their manuscript.

- Building on the previous point, a major concern with using GA in jailbreaking is the number of large number queries it would require. Unlike traditional adversarial attacks, querying LLMs can be very expensive, so the total query budget should be an important consideration in jailbreaking. Although the authors discussed this as a hyperparameter, it is unclear how ASE would perform if given the same budget as previous approaches. Currently, the authors simply treat this aspect as a limitation, but this could actually be a critical consideration for practitioners that can directly influence their choice of methods. This concern further exacerbates when considering the fact that the proposed method does not perform significantly better compared to existing approaches on open-source models, which could be cheaper for employing large-scale query.

- The manuscript is not well-written. For example, there are numerous grammar issues and inappropriate expressions, which strongly affect the readability of the introduction section (for example, many simple processes and concepts introduced in the methods section are made very ambiguous and overly complex, requiring the reader to see the methods section to understand the motivations in the introduction). This can be disappointing, as the introduction is supposed to provide a clear and intuitive picture of the whole manuscript from the outset.

In addition, I list some of the presentation issues.
- Line 074: The reference to Wei et al., 2024 is generated with improper commands, leading to awkward additional brackets. The authors should consult ICLR’s official guide for LaTeX templates.
- Line 078: “Here, red-teaming LLMs act like drafting from structured outlines….” There are grammar issues with this sentence, and I could only gauge its meaning after reading it several times.
- Line 085: The “considering” part has similar issues.
- Line 137: The comma after “TAP” is redundant.

### Questions
Please see weakness.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work tackles jailbreak attacks on safety-aligned LLMs, which remain vulnerable to prompt manipulation. The proposed Adaptive Strategy Evolution (ASE) framework improves jailbreak techniques by modularizing strategies and using a genetic algorithm for systematic optimization, replacing uncertain LLM-based adjustments. ASE also introduces precise feedback, enabling targeted refinements. Results show ASE outperforms existing methods against advanced models.

### Strengths
1. ASE breaks down jailbreak strategies into modular components, significantly increasing both the flexibility and scope of the strategy space.
2. This work presents an enhanced fitness evaluation system that overcomes the drawbacks of traditional binary or overly complex scoring methods, providing accurate and reliable assessment of jailbreak prompts.

### Weaknesses
1. Some key parameters are missing. For example, how about the crossover and mutation rate in the experiment.
2. As evolutionary algorithms are inherently with randomness, it should be tested for multiple time and show the statistical results (average and std). However, I didn’t find any related result, the missing of which will lower the soundness of this work.
3. It states that this is “adaptive” while I didn’t find any “adaptive” design which refers to the strategy will update adaptively as the optimization proceeds. It seems just a normal optimization framework. Can you elaborate on how the ASE framework adapts during the optimization process? Are there any specific mechanisms that adjust the strategy or algorithm parameters based on intermediate results?
4. In line 323, “algorithm 1” should be “Algorithm 1”.

### Questions
1. As mentioned “beyond a population size of 15 and iteration count of 5, the gains in JSR become marginal.” This is an indeed small settings, therefore I am curious if the genetic algorithm is overqualified here. Maybe some simpler optimization technique can suffice, such as local search?
2. How about your search space regarding the strategy optimized by the genetic algorithm? If the search space is small then there is no need to use complex optimization techniques.

### Soundness
2

### Presentation
2

### Contribution
2

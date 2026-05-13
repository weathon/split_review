# PromptWizard: Task-Aware Prompt Optimization Framework

- Decision: Reject
- Scores: 6, 5, 3, 3, 5

## Abstract
Large language models (LLMs) have transformed AI across diverse domains, with \textit{prompting} being central to their success in guiding model outputs. However, manual prompt engineering is both labor-intensive and domain-specific, necessitating the need for automated solutions. We introduce PromptWizard, a novel, fully automated framework for discrete prompt optimization, utilizing a self-evolving, self-adapting mechanism. Through a feedback-driven critique and synthesis process, PromptWizard achieves an effective balance between exploration and exploitation, iteratively refining both prompt instructions and in-context examples to generate human-readable, task-specific prompts. This guided approach systematically improves prompt quality, resulting in superior performance across 45 tasks. PromptWizard excels even with limited training data, smaller LLMs, and various LLM architectures. Additionally, our cost analysis reveals a substantial reduction in API calls, token usage, and overall cost, demonstrating PromptWizard's efficiency, scalability, and advantages over existing prompt optimization strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
PromptWizard explores automated discrete prompt engineering by combining a genetic search process with a critique and refinement stage.  In addition, PromptWizard also adds a few-shot reasoning chain for the selected prompts.  They implemented what seems like a fairly large system and evaluated it on the BigBench Instruction Induction Benchmark, GSM8K, AQUARAT, and SVAMP.  They show significant wins in accuracy, cost, and efficiency other published systems including Instinct, InstructZero, PromptBreeder, EvoPrompt and AVE.

### Strengths
1. The proposed system appears pretty extensive and combines several techniques for discrete prompt engineering. 
1. The experimental evaluation is well done and the results show significant wins in accuracy and cost over existing systems. 
1. The ablation points to potentially significant wins from their method to construct few-shot chain-of-thought reasoning examples.

### Weaknesses
1. My primary concern with this paper is that while the results are impressive, I am struggling to identify the key-insight or transferable idea.  What makes PromptWizard better than all the systems it beats? There is an ablation but it is one paragraph and seems to suggest that reasoning and few shot examples is primary source of improvement.  
2. While the writing was reasonable, the fairly complex pipeline of evolutionary optimizers and sequential optimization made it difficult to understand how the two approaches work together.  Are they really just two sequential stages? Shouldn't the critical feedback be used in the iterative optimization. 
3. Given the incorporation of few-shot examples, I was also expecting see comparisons with DSPy but this didn't appear anywhere in the paper.

### Questions
1. What is the big idea I should take away from this paper?  
1. How does the sequential optimization interact with the iterative optimization? Is it really just a two stage pipeline?
1. How does this work compare with DSPy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new discrete prompt optimization method that automatically refines both prompt instructions and in-context examples by using LLM.

### Strengths
1. The method PW proposed in this paper optimizes both the prompt instructions and in-context examples contained in the discrete prompt, which achieves a comprehensive approach and considerable performance gains in experiments.
2. Compared to recent LLM-based prompt optimization methods, PW achieves satisfying results with much less cost of API calls.

### Weaknesses
1. Although the authors have written about the difference between PW and existing prompt optimization methods. The technical novelty of the proposed method is still somewhat weak. The approach of refining prompt instructions and selecting the most effective in-context examples are widely recognized concepts.
2. The presentation of the overall pipeline of the approach could be improved. For example, moving the main algorithm in the appendix into the main text will make the presentation clearer and avoid making readers lose among the proposed components.

### Questions
Please respond to the concerns in the "Weaknesses" part.

Q1. Regarding the calculation of the API cost of PW, how do you evaluate the performance of the current prompt instructions and selected in-context examples with such a small quantity of API calls? Because stable evaluation results of the prompts are a prerequisite for stable optimization.

Q2. What are the ablation results of solely optimizing prompt instructions and in-context examples?

Q3. Line 252: What "scoring mechanism"?

Q4. Line 256: In what case will "this process does not yield the desired count"?

### Soundness
4

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
The paper proposes a prompt optimization framework to query LLM itself to automatically evolve, reflect, and optimize the prompt in the discrete space. One innovation part is that the framework optimizes both the head prompt and few-shot examples sequentially for holistic effects. The experiments over BBH and GSM8K shows better performance over other methods, and the much lower costs in API calls and token costs.

The paper has several problems: 1) The main framework is mostly close to other works such as APO, PROMST, and PromptAgent. However, the paper did not mention these works and compare with them. 2) Critique and feedback over the errors have been claimed as one innovation point in the paper. However, this component already appears in above three works. This paper may lack correct clarification on contributions. 3) The writing is not satisfying. Sometimes very hard to follow.

### Strengths
The optimization of head prompt and few-shot example prompt together is one novel component. I have not seen this setting in other papers before. The experiments over BBH and GSM8K and some ablation studies are appreciated.

### Weaknesses
1) Overclaim of the innovation part. Actually, integrating error feedback for LLMs to refine the prompts has already been proposed in other works, such as APO (https://openreview.net/pdf?id=WRYhaSrThy), PromptAgent (https://arxiv.org/pdf/2310.16427) and PROMST (https://arxiv.org/pdf/2402.08702), etc.
2) Following above, the authors only compare with baselines like Evoprompt, PromptBreeder, and APE, which truly do not use error feedback. However, why not compare with works using error feedback such as APO? I am curious that these frameworks can achieve similar performance and low costs.
3) The shared anonymized code link cannot be accessed.
4) The specific setting of baseline methods is not illustrated. How to make sure a fair comparison like the same number of prompt sampling?
5) Many components lack analysis of why it works and lack the study over the robustness of this framework. For example, whether the wording of component prompt will influence the performance.

### Questions
In the optimization of few-shot examples, how to make sure the examples do not contain errors if relying on LLMs to synthesize?

The framework relies heavily on LLM capability to refine and reflect. Is there any components that smaller LLMs cannot work well so that the framework fails?

### Soundness
2

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
The authors proposed an automated framework for discrete prompt optimization to address the challenges of labor-intensive and domain-specific manual prompt engineering. PromptWizard employs a self-adapting mechanism that uses a feedback-driven critique and synthesis process to iteratively refine prompt instructions and in-context examples. They demonstrated the effectiveness of PromptWizard across various tasks and highlighted the method's efficiency through a detailed cost analysis.

### Strengths
1. They performed extensive experiments on benchmark tasks like BBII, BBH, and arithmetic reasoning tasks.  
2. The cost analysis demonstrates significant reductions in API calls, token usage, and overall costs, showcasing PromptWizard’s efficiency.

### Weaknesses
1. Readability is quite poor, and their contributions should be organized more clearly.  It looks like a list of various elements that were put into the algorithm for now.
2. It is difficult to identify the novelty of this work. It appears that they have integrated various existing methods. For instance, their iterative prompt refinement algorithm seems to be a combination of established techniques that originally introduced mutation, scoring, critique, and synthesis. Additionally, the self-adapting mechanism they mention is also widely used.

### Questions
1. Could you clarify the explanation of "identification of diverse examples"? What role do positive examples and negative examples play in this process?
2. Is there a specific reason why you only compared Instinct with PW in the one-shot setting, as opposed to the zero-shot setting experiment?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a prompt optimization method based on Large Language Models (LLMs) named PromptWizard. PromptWizard not only optimizes instructions but also improves demonstrations by incorporating elements such as few-shot learning, Chain-of-Thought (CoT), task intent, and expert personas. In extensive experiments, PromptWizard achieves the best performance with minimal resource consumption.

### Strengths
1. The writing of the paper is clear, and the content is easy to understand.
2. Compared to other baseline methods, PromptWizard has shown significant performance improvement.
3. This research conducted extensive experimental validation, providing thorough and reliable evidence.

### Weaknesses
1. In fact, feedback-based prompt optimization methods are already quite mature, including approaches like APO, PromptAgent, and PE2. PromptWizard is not the first feedback-driven optimization method, and the authors overlooked related works of this nature in their writing. Therefore, I recommend the authors add related work of this type.

2. Following Weakness 1, many studies have already demonstrated the strong performance of feedback-based optimization methods. I believe that a comparison with methods like APO and PromptAgent is essential. I strongly recommend that the authors supplement their discussion with comparisons to these feedback-based methods.

3. Building on Weakness 2, I noticed that the meta prompt in PromptWizard is significantly heavier compared to methods like APO. Based on my recent review of relevant works, StraGo indicated that APO has the lowest cost. Thus, PromptWizard should include a comparison with APO in terms of cost and performance.

4. I think PromptWizard seems to be a mix of different prompt design techniques. PromptWizard integrates feedback mechanisms similar to those in APO, keyword extraction techniques from AutoHint, and also combines strategies such as Chain-of-Thought (CoT), few-shot learning, and expert personas. I believe your integration doesn’t delve deeply enough into the reasons for combining these techniques. This makes the paper somewhat lacking in terms of innovation. I strongly recommend that the authors provide additional explanation for why these modules are used. If they are included in PromptWizard solely because CoT, few-shot, and expert personas can improve LLM performance, I believe that is insufficient for an academic paper.

5. Writing Weakness ：

    a) In the cost analysis section, the authors should only present the results and corresponding analysis. The detailed estimation process is more appropriate for the appendix.

    b) In Figure 6, there is an inconsistency between the Synthetic Example and Feedback. Based on my experience, when optimizing examples using LLMs, it's highly likely that scores or percentages would be involved. However, the Synthetic Example completely overlooks this aspect. I believe this example does not effectively illustrate the impact of the feedback mechanism on the synthetic example. I suggest that the authors choose a more representative example that can more intuitively demonstrate the role of feedback in the prompt optimization process.

    c) In line 482, "Ablation on Different Base LLMs." I don't think this qualifies as an ablation study; this section describes the impact of different models on PromptWizard. I suggest changing the title.

Reference:

1. Automatic Prompt Optimization with “Gradient Descent” and Beam Search (https://arxiv.org/pdf/2305.03495)
2. PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization (https://arxiv.org/pdf/2310.16427)
3. Prompt Engineering a Prompt Engineer (https://arxiv.org/pdf/2311.05661)
4. StraGo: Harnessing Strategic Guidance for Prompt Optimization (https://arxiv.org/pdf/2410.08601)

### Questions
1. How many candidate prompts does PromptWizard retain in each iteration?

2. What do "self-evolving" and "self-adaptive" refer to? How are they implemented, and why are they beneficial for balancing exploration and exploitation?

3. How is the "Deeper Exploitation of Task Nuances" mentioned in line 159 implemented?

4. Please see Weakness section.

### Soundness
3

### Presentation
2

### Contribution
2

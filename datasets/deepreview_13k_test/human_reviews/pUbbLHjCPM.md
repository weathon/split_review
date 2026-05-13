# Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models

- Decision: Accept
- Scores: 6, 8, 3, 6

## Abstract
Recent advancements in large language models (LLMs) have demonstrated that progressive refinement, 
  rather than providing a single answer, results in more accurate and thoughtful outputs. 
  However, existing methods often rely heavily on supervision signals to evaluate previous responses, making it difficult to effectively assess output quality in more open-ended scenarios. Additionally, these methods are typically designed for specific tasks, which limits their generalization to new domains.
  To address these limitations, we propose Progressive Thought Refinement (PTR), a framework that enables LLMs to progressively refine their responses. PTR operates in two phases: 
  (1) Thought data construction stage: We propose a \textit{weak and strong model collaborative selection} strategy to build a high-quality progressive refinement dataset to ensure logical consistency from thought to answers, and the answers are gradually refined in each round.
  (2) Thought-Mask Fine-Tuning Phase: 
        We design a training structure to mask the "thought" and adjust loss weights to encourage LLMs to refine prior thought, teaching them to implicitly understand "how to improve" rather than "what is correct."
        Experimental results show that PTR significantly enhances LLM performance across ten diverse tasks (avg. from 49.6\% to 53.5\%) without task-specific fine-tuning. 
        Notably, in more open-ended tasks, LLMs also demonstrate substantial improvements in the quality of responses beyond mere accuracy, suggesting that PTR truly teaches LLMs to self-improve over time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Previous methods of self-improvement tried to enhance performance within specific domains, because supervision signals are vague and hard to define and evaluate response quality in open-ended tasks. However, their key limitation lies in lack of generalizability due to high reliance on task-specific pipelines or reward models. Hence, the authors introduce PTR method, which consists of “thought data construction phase” and “weighted thought-mask fine-tuning phase”.

### Strengths
- It's easy to follow, and clear writing and presentations (including nice figures.)
- Performance improvement over iterations looks very good.
- Extensive experimental results and analysis of the proposed methods, particularly in Sections 4.3 - 4.5, and qualitative examples.

### Weaknesses
I have some concerns, and ask the authors to explain and mitigate these.

- What are the main contributions and novel points of this paper over some prior refinement works? Weak-strong model to construct refinement data without using rewards, and thought-mask strategy?
- If yes, I wonder why the authors do not compare with prior works on refinement method or approaches with verifiers. There are so many related works (as also mentioned in Related Work sections), but three methods that the authors showed look very naive. If extra feedbacks are not proper for some datasets, I think comparing in math or code reasoning, where we can easily define the rewards or feedbacks by comparing with ground truth, would be needed at least.
- As a followup question, why do all three baselines showed worse performance after iterations? I believe these baselines are not good and not well-designed, which makes it very hard to confirm the contributions of this paper.
- As I understood, thought-mask strategy is using some training dataset with masked on thought parts. How were the results when you didn't use this masking strategy, and only used refinement loss parts? I believe IFT baseline is not this case---if yes, what is the IFT method exactly? (in L.304)
- What were the experimental settings for fine-tuning? If it costs a lot, would it be better to use some extra feedbacks during inference in perspective of test-time compute efficiency?

### Questions
- To be clear, what do the authors mean about "extra feedback" exactly? Using some other tools, human or compiler feedback, or verifiers (reward models) during *inference* means extra feedback? But this method trained models that can refine their answers without any other feedbacks during inference (though they used extra feedbacks from other models during *training*.)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Progressive Thought Refinement (PTR), a framework designed to enable LLMs to iteratively improve their responses through self-refinement. PTR operates in two phases: (1) a thought data construction phase, using a weak-strong model collaboration to build high-quality thought-answer pairs, and (2) a weighted thought-mask fine-tuning phase, which encourages models to enhance responses across multiple iterations. Experimental results demonstrate PTR's effectiveness across ten diverse tasks.

### Strengths
1. The paper presents a novel framework, PTR, that enables LLMs to iteratively self-refine. The concept of self-refine/correct is a very important research direction and has attracted many recent research efforts. The paper has shown reasonable effectiveness and performance improvement in experiments, with a new and interesting framework to achieve this. 

2. The two-phase methodology, combining weak-strong model collaboration with thought-mask fine-tuning, is robustly validated across ten diverse datasets. While the demand for strong model is costly, it remains a reasonable approach in application.

3. The paper is well-organized, with clear visuals and structured explanations. The paper also provided a thorough discussion on related concepts and papers.

### Weaknesses
- The function $F_{\text{cons}}$ and $\beta_t$ in equation 3.4 is not clearly defined. Clear definitions for the components of the equation are needed in the main paper. 

- Hyperparameter complexity. while hyperparameters $\lambda_1$, $\lambda_2$, $\lambda_3$ help balance various aspects of the model's loss function, extensive tuning could limit the practical adoption of PTR. The paper would benefit from a sensitivity analysis or heuristics for setting these parameters to make the method more accessible for broader application.

- Computational overhead. The reliance on a 70B model and the multi-iteration inference adds significant computational demands for both training and inference. It would be beneficial for the authors to discuss the cost of this method (the trade-offs in performance versus efficiency).

- Despite the complexity of the PTR procedure, the performance improvement over direct prompting (iteration 1 baseline) is relatively modest. On average, PTR achieves only a 1.88% improvement by iteration 3 for Qwen. For Llama3, the most significant gains are seen in the CommonsenseQA dataset, whereas tasks such as mathematical reasoning show only minimal benefits. 

- Minor typos (e.g., correct alignment of PTR and Prompt1/2/3 in Tables 1 and 2).

### Questions
See above in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes Progressive Thought Refinement (PTR), a novel framework designed to improve the iterative reasoning capability of large language models (LLMs). PTR leverages a dual-phase approach to construct a progressive refinement dataset and then applies a thought-masking fine-tuning technique to teach LLMs to self-improve. PTR aims to enhance the generalization capability of LLMs across diverse tasks, including knowledge reasoning, code generation, and open-ended text generation, without task-specific fine-tuning. Experimental results indicate that PTR improves performance across a wide range of benchmarks, demonstrating its effectiveness in enabling models to progressively enhance response quality over multiple iterations.

### Strengths
- The paper addresses a highly relevant and timely topic within the machine learning community. Self-refinement has been perceived as an important approach for improving pre-trained LLMs.
- The authors have conducted extensive experiments, exploring the performance of their model and the baselines in different domains.

### Weaknesses
- The manuscript lacks sufficient clarity, making it challenging for readers to follow the paper
- 2 paragraphs of lines 358-467 are exactly duplicated in lines 510-520!
- Also, the claim in those paragraphs, "PTR consistently improves across iterations without signs of overfitting." is not the case in Figure 4. It looks like the performance is saturated after the first iteration and is just oscillating from iterations 2 to 10, especially in the XSsum experiment.
- Figure 1 which is supposed to show the core idea/method is unnecessarily complicated and overloaded making it hard to interpret. 
- Figure 3 has 4 plots with lots of information, small numbers w/o proper take-home messages in the caption.
-  The description for \textbf{PTR vs. Knowledge Distillation (IFT)} in line 320 is not clear and hand-wavy.
- Claiming that LLMs have intrinsic/inherence progressive refinement ability is sort of a big claim that needs more detailed investigations. 
- By looking at the average scores in Table 1, the Prompt baseline is already showing a very solid performance in the first iteration. When comparing this baseline with your method you should consider the complexity of your approach and the time analysis.

### Questions
- Have the authors investigated the effect of different losses of equation 3.4 in an ablation study?
- What is the "PRD" dataset mentioned in the paragraph of line 303?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Progressive Thought Refinement (PTR) for LLMs, focusing on iterative refinement without task-specific fine-tuning. PTR uses a weak-strong model collaboration and a unique thought-mask fine-tuning approach to refine model reasoning, showing generalization across diverse tasks.

### Strengths
+ PTR’s approach to iterative response improvement is novel, aiming to boost LLM generalization.
+ Benchmarking against established methods helps demonstrate PTR’s relative effectiveness.

### Weaknesses
- Critical information, such as data size, prompt details, and filtering strategies, is not presented clearly within the main text. Instead, these details are found only in the appendix, requiring readers to frequently refer back and forth for a complete understanding. Integrating these important details into the main text rather than the appendix will provide readers with immediate context and reduce the need for cross-referencing, enhancing readability and comprehension.

- The paper lacks clear guidelines on the optimal number of iterations for masking and fine-tuning. Accuracy fluctuates across iterations, indicating the model’s sensitivity to iteration count without sufficient explanation/justification. Establish clear guidelines on the optimal number of iterations for masking and fine-tuning.

- The paper would benefit from testing on datasets designed for reasoning and generalization evaluation, such as MMLU-Pro+ (arXiv:2409.02257), which could provide a more robust demonstration of PTR’s reasoning capabilities.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

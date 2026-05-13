# How to Correctly Do Semantic Backpropagation on Language-based Agentic Systems

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Language-based agentic systems have shown great promise in recent years, transitioning from solving small-scale research problems to being deployed in challenging real-world tasks.
However, optimizing these systems often requires substantial manual labor.
Recent studies have demonstrated that these systems can be represented as computational graphs, enabling automatic optimization. Despite these advancements, most current efforts in Graph-based Agentic System Optimization (GASO) fail to properly assign feedback to the system's components given feedback on the system's output.
To address this challenge, we formalize the concept of \textit{semantic backpropagation} with \textit{semantic gradients}---a generalization that aligns several key optimization techniques, including reverse-mode automatic differentiation and the more recent TextGrad by exploiting the relationship among nodes with a common successor.
This serves as a method for computing directional information about how changes to each component of an agentic system might improve the system's output.
To use these gradients, we propose a method called \textit{semantic gradient descent} which enables us to solve GASO effectively.
Our results on both BIG-Bench Hard and GSM8K show that our approach outperforms existing state-of-the-art methods for solving GASO problems.
A detailed ablation study on the LIAR dataset demonstrates the parsimonious nature of our method

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents a framework to extend the text-based gradient method (ask the model to refine the prompt. This series of works often formulates this refinement as a gradient decent process of the discrete prompt) for handling the graph structure, such as using multiple prompts to form an agent for problem-solving.

### Strengths
This work systematically discussed the "backpropagation" of the text-based gradient method and offered a framework to aggregate the gradients, making the text-based gradient methods close to the normal gradient descent.

### Weaknesses
The paper writing could be improved. I think placing figures and examples from the appendix into the main document could largely improve the readability. The experiment setting could be more clearly stated in the main document. I found those in the appendix, such as the initial graph for BBH, GSM8K, and LIAR. However, the number of nodes and the diameter of the graph are small, raising concerns about the proposed method's generalization ability on more complicated graphs, such as the MCTS, tree of thoughts, or wizardLM series. 

Needs more in-depth analyses, such as the robustness of the prompt templates for the forward and backward functions. It's also better to test other models than GPT4 since the GPT4 has already achieved a very high score on GSM8K and BBH. Introducing other models could also be helpful in evaluating the backward function design. If I understand correctly, the backward prompt filled with real materials (instruction, question, response, and other statements) could be very long and complicated. My concern is that the GPT4 may not follow it well.

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper falls in the vein of research that's attempting to expand the concept of "gradient-based optimization" to language-based agentic systems. Specifically, several papers have attempted to take the concept of "autodiff" and apply it to graph-based agentic systems. From my understanding, this paper is most similar to TextGrad, but identifies some improvements in TextGrad that 1. make this paper more analogous to standard autodiff,  2. improves performance by taking advantage of more information during the backwards pass.

### Strengths
Overall, I think this paper identifies a reasonable gap in the existing textual gradient-based approaches (e.g. TextGrad). Specifically, if I understand the paper correctly, the paper is saying that if you have a function `c = f(a, b)`, the autodiff rule for `da` given `dc` should also depend upon `b`, not just `a`, `c`, and `dc` (which is what TextGrad's formulation does). This follows naturally from autodiff's definition, where    say, the autodiff rule for `da` in `c = mm(a, b)` involves `b`.

The "intuitive" explanation given in the paper also makes sense to me.

This motivation for their results is also validated by their experimental results.

### Weaknesses
I personally found the presentation of the paper somewhat confusing. In particular, I think a more concrete example walking through what exactly a semantic gradient looked like would make the paper much easier to understand, particularly if it were contrasted against the gradients from TextGrad. I see the examples of the evolved prompts in the appendix (which are useful!) but I'd be interested to see how the actual gradients look like, since that's the primary way in which this paper differs from prior work.

More broadly speaking, I also find myself being somewhat skeptical of the autodiff analogy, and to what extent semantic gradients meaningfully map to autodiff. For example, for mathematical autodiff a gradient directly corresponds to how that parameter effects the output loss (assuming an epsilon step). With semantic gradients, however, there's no such correspondence like this. It's unclear if a small change in the semantic gradient space will actually lead to a corresponding improvement in the task performance, which is a key assumption for gradient-based optimization.

I would also be interested in seeing how different graph structures lead to different performance. For example, as far as I can tell, all the graphs in this paper involve only one "layer". It would be valuable to see experiments with deeper or more complex graph structures to understand the scalability and generalizability of the proposed approach.

I'd also like to see more benchmarks, as opposed to just GSM8k and BBH NLP/Algorithmic. The current benchmarks, while relevant, may not fully capture the capabilities of the proposed method across a wider range of tasks and complexities. Expanding the benchmark suite would provide a more robust evaluation.

### Questions
See above.

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
3

### Summary
To enable text optimization (omitting numerical gradients) of model outputs based on feedback, the authors propose Graph-based Agentic System Optimization (GASO). This framework formalizes the concept of semantic backpropagation with semantic gradients, generalizing several key optimization techniques, including reverse-mode automatic differentiation and TextGrad, by exploiting the relationships among nodes with a common successor. GASO demonstrates effectiveness in both the BIG-Bench Hard and GSM8K datasets.

References:

[1] TextGrad: Automatic "Differentiation" via Text.

### Strengths
1. This work follows an important line of research focused on text optimization based on natural language gradients.

2. The experimental results demonstrate significant improvements over existing semantic optimization methods, such as TextGrad.

3. The proposed method is clear and straightforward to implement.

### Weaknesses
1. The evaluation datasets are somewhat limited, comprising only BIG-Bench Hard and GSM8K. In contrast, TextGrad has been evaluated on additional datasets, including code generation, drug molecule optimization, and radiotherapy treatment plan optimization. It would be beneficial to see the potential of GASO applied to a wider range of applications, particularly those involving structured outputs and complex reasoning beyond mathematical problem-solving.

2. Since GASO incorporates additional neighboring information in its computations, the cost associated with this approach is not clearly defined. The paper lacks a detailed analysis of the computational overhead introduced by the graph-based approach, specifically in terms of memory usage and processing time. It would be valuable to understand the trade-off between computational cost and performance, especially as the number of nodes and edges in the graph increases. The current analysis does not provide sufficient information to assess the scalability of the method.

### Questions
See Weakness above.

1. Performances on other reasoning tasks, such as code generation.
2. The trade-off between performance and cost.

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
Recently, Language-based agentic systems have shown great potential in solving real-world tasks. However, these works usually relied on human-designed settings (e.g., instruction or prompt). How to enable an automatic optimization for agentic systems has been a challenge. In this paper, authors introduce a semantic backpropagation with semantic gradients, which explores how to change each component of an agentic system to improve outputs. Experimental results on BIG-Bench and GSM8K demonstrate that the proposed method can solve GASO problems.

### Strengths
This paper formulates agentic system as a computational graph task and then introduces a semantic backpropagation to optimize each component of agentic system via semantic gradient.

### Weaknesses
 **Weaknesses**

1. Although authors claim the difference between TextGrad as TextGrad use textual gradients while the proposed method is semantic gradients, it seems the proposed method still heavily relied on language features and human design (e.g., Implementation 2).
2. Authors claim that in TextGrad ignores the dependency and heterogeneity, can you provide some real cases about the nodes with dependencies and why they are failed in TextGrad? Does it matter in optimizing agentic system? Can you highlight more insights about your paper when compared with TextGrad?
3. The proposed method still relied on an evaluation system to obtain feedback. So what happen if applying this method to some open scenarios. Besides, this paper only evaluates Big-Bench and GSM8k. Can you try more datasets to validate the generalization of the proposed method like GAIA. MMLU?

### Questions
1. Can you provide some examples about semantic gradients when compared with TextGrad. From the provided code, the semantic gradient seems is still the natural language form.

### Soundness
3

### Presentation
2

### Contribution
2

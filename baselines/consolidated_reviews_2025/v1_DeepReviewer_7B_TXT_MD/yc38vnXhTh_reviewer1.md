### Summary

The authors present a method for generating human-like behavior in 3D environments. Their method, dubbed ACTOR, uses an LLM to decompose high-level goals into low-level activities, and then uses a value function to evaluate the resulting behavior. They also present a dataset of human behavior, BEHAVIORHUB, which is used to train and evaluate their method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well written and easy to follow.
2. The authors have clearly put a lot of thought into the design of their method, and the results presented in the paper are compelling.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that their method is able to generate human-like behavior in 3D environments, but the results presented in the paper are not very impressive. The generated motions are quite simplistic and do not capture the complexity of human behavior. The scenes are also very basic, lacking the clutter and detail found in real-world environments. The evaluation metrics, while standard, do not fully capture the nuances of human-like behavior, such as smoothness and naturalness of motion.
2. The authors use a large number of LLM calls to generate their results, which is a bit of a shame. It would be more efficient to use the LLM for planning and then use a smaller model to generate the actual motion. The reliance on multiple LLM calls increases the computational cost and latency, making it less practical for real-time applications. The authors should explore methods to reduce the number of LLM calls or to use the LLM more effectively for the core planning task.
3. The authors use a number of heuristics in their method, such as the use of a window size of 5 for the LLM calls. It is not clear why these heuristics were chosen, and it is possible that other values would lead to better results. The lack of ablation studies on these heuristics makes it difficult to understand their impact on the overall performance of the method. The authors should provide a more thorough justification for their design choices and conduct ablation studies to demonstrate the importance of each component.

### Suggestions

The authors should consider incorporating more sophisticated motion generation techniques to improve the realism of the generated behaviors. Instead of relying solely on motion clips, they could explore methods that generate smooth and natural-looking trajectories using techniques such as Hamiltonian Monte Carlo. This would allow for more complex and realistic movements, especially in cluttered environments. Furthermore, the authors should investigate methods for incorporating more detailed scene information into the planning process. This could involve using scene graphs or other scene representations to capture the relationships between objects and their affordances. This would allow the agent to make more informed decisions about which actions to take, leading to more realistic and contextually appropriate behavior. The evaluation metrics should also be expanded to include measures of motion smoothness and naturalness, in addition to the current metrics. This would provide a more comprehensive assessment of the quality of the generated behaviors.

To address the issue of multiple LLM calls, the authors should explore methods for integrating the LLM more tightly into the planning process. This could involve using the LLM to directly generate a sequence of actions, rather than generating individual motion clips. This would reduce the computational cost and latency of the method. The authors should also investigate methods for using the LLM to guide the motion generation process, rather than using it as a separate component. This could involve using the LLM to evaluate the quality of the generated motions and to make corrections as needed. Furthermore, the authors should conduct more thorough ablation studies on the heuristics used in their method. This would help to understand the impact of each component on the overall performance of the method. The authors should also provide a more detailed justification for their design choices, explaining why they chose the specific values for the heuristics. This would help to make the method more transparent and reproducible.

Finally, the authors should consider expanding the scope of their experiments to include more complex and realistic scenarios. This could involve using more cluttered environments, more diverse sets of objects, and more complex goals. This would help to demonstrate the robustness and generalizability of their method. The authors should also compare their method to other state-of-the-art methods for human motion generation, to provide a more comprehensive evaluation of its performance. This would help to establish the strengths and weaknesses of their method and to identify areas for future improvement.

### Questions

1. Why did you choose to use a window size of 5 for the LLM calls? It seems like this might be too small, and could lead to poor results. Would it be possible to use a larger window size, or to use the LLM more effectively for the core planning task?
2. How does your method compare to other state-of-the-art methods for human motion generation? Are there any other methods that you would like to compare your method to?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

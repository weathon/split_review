# AutoCode4Math: Learning Autonomous Code Integration for Math LLMs

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 5

## Abstract
Recent research on tool integration for math Large Language Models (LLMs)  aims to combine complementary strengths of chain-of-thought (CoT) reasoning and code execution. However, we discover a critical limitation: current tool-integrated math LLMs rely on externally dictated instructions to decide whether to use CoT or code, lacking the autonomy to choose the most appropriate method independently. This prompts us to study \emph{Autonomous Code integration } (AutoCode) for math LLMs, which enables models to \emph{independently} develop their own methodology-selection strategy in the absence of reliable supervision. To address this challenge, we propose an innovative Expectation-Maximization (EM) formulation that refines the model's decision-making through the exploration of its capabilities. This framework alternates between (a) computing a reference strategy that improves the model's belief over its capabilities through self-exploration, and (b) updating the model based on the refined belief. We further enhance this framework with an efficient implementation, incorporating a novel data synthesis strategy and off-policy reinforcement learning. Extensive experiments demonstrate that our approach, using only a public query set, significantly boosts the performance of existing math LLMs, raising accuracy by nearly 20% to 65.28%  on the challenging MATH benchmark, while reducing code executions by up to 65% .

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors address the problem of letting LLMs autonomously decide which planning strategy to use, between plain CoT and interaction with a python interpreter, in order to reliably solve math and reasoning problems. The authors correctly observe that such autonomic decision making cannot be induced via simple SFT on expert-annotated data, and therefore propose an RL strategy based on the EM algorithm, as a way to allow the model to self-explore and train itself on its own generated trajectories.

### Strengths
- The authors observation that autonomous code integration cannot be taught via simple SFT is definitely correct.
- The authors consider also multi-turn interactions featuring an interleaving of CoT and Python code execution, which is not found very often in the CoT and code execution literature.

### Weaknesses
The main weakness I can see is that it is not quite clear why the authors' EM approach is necessary. While I do agree that SFT is not sufficient for the task at hand, there are plenty of much simpler alternatives to the authors' approach, which would equally allow self-exploration and on-policy self improvement. Given how complex the authors' framework is, I feel that it is even more necessary to outline its advantage and convince readers that it is indeed worthwhile and preferable to simpler methods.

More points I wish to make:

- The author's outline of the method is extremely long and technical, and difficult to digest for any reader not already familiar with EM. Focusing more on its high-level idea and providing at least a few examples would go a long way.
- The main result table in figure 3 is honestly difficult to parse. Some lines are color-coded in blue and red, but the text and caption do not explain what this means. It's not clearly stated which lines correspond to the authors' proposed approach and which correspond to baselines. I personally would focus on comparing the author's proposal with whatever method happens to be the SOTA for the benchmarks the authors consider, in a much smaller table.
- Some typos can be found here and here, including in the abstract.

### Questions
- The authors' EM approach appears very complicated and requires a lot of moving parts, and is intended as a replacement for simple SFT. There are much simpler and proven ways of replacing SFT, such as Expert Iteration and RLHF, which can provide similar advantages in terms of self-exploration. Could the authors more clearly outline why their EM approach is preferable to these alternatives, and which advantage exactly is provided by each of its components?
- In section 2.3, the authors outline a framework for data synthesis. Fine-tuning LLMs on synthetically generated data is a proven technique for enhancing their abilities. What benefit do the other component of the EM framework bring?
- What exactly is the "standard RL" baseline mentioned in section 3.2? The authors should be a bit more specific.
- Again in section 3.2, the authors state "We conjecture that the proposed EM framework outperforms standard RL because: the
reference methodology-selection strategy helps narrow down the policy search space during training". Can the authors provide any experimental evidence for this statement?

### Soundness
3

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
3

### Summary
The paper introduces a method to train an LLM to select between use code-as-a-tool or chain-of-thought-reasoning actions, allowing the model to do some degree of inference-time search between the two actions. The training process is instantiated as an off-policy RL problem without labels for intermediate steps, by maximizing the joint probability of picking the correctness-maximizing action and correct response, decomposed into an expectation step to estimate state-action-values (via random rollouts) and a maximization step to train on the reward-weighted actions. 7B models trained using this method show improvement over just 2 iterations on the GSM8k and MATH datasets.

### Strengths
Significance: The topic addressed in this paper is exciting, with the release of o1 the community is interested in methods that can improve inference time decision making for math, especially on smaller models.
1. The results on GSM8k and MATH are interesting, over just 2 training iterations AutoCode improves performance in a stable way over baseline RL (Figure 4). 
2. The method only relies on input and outputs, not using human generated labels is useful for data bottlenecked researchers. Framing the RL actions as CoT vs. code generation addresses the gap between self-learning the optimal policy instead of behaviorally cloning (SFT) a given policy as with prior models.

### Weaknesses
Performance:
1. Assuming I followed the table in Figure 3 correctly, it seems this method does not outperform the Qwen2-Math 7B-instruct model on any math dataset, which uses a simpler training method. The authors can try to see if their method improves Qwen2-Math 7B-instruct further. The method also doesn't give significant performance gains outside of MATH and GSM8k datasets over open-source baselines.

Presentation: 
1. Section 2 is difficult to follow, it should be organized into clearer components by aligning better to Figure 2, highlighting (1) how the data is generated (expectation) and (2) how the model is trained on that data (maximization). I summarized the paper above based on my understanding, please clarify if there is misalignment.
2. The main results, Figure 3, looks like a spreadsheet screenshot, please re-organize it. I am not sure I followed the results of this figure properly (see weaknesses in performance section). Figure 4 needs to be larger.
3. Several typos, Figure 1: "sythesis" and Appendix B "referece"

### Questions
1. If you extend the AutoCode training to more iterations (Figure 4), does the performance on GSM8k and MATH continue to improve? It looks like the accuracy is still going up.
2. Why is the initial accuracy for Qwen-2-Math on GSM8k and MATH very different between Figure 3 and Figure 4? 
3. I can't view the anonymized repo, can you double check it works? I would like to see the code and try the final model.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors identify a major challenge in current training regimes where models are typically told explicitly whether to execute code. Addressing this, the paper introduces an innovative EM algorithm that allows models to choose their execution paths autonomously, either using CoT reasoning or code execution. The results are quite impressive, showing a 65.28% accuracy in mathematics-related tasks, alongside a 65% reduction in code execution. This advancement not only improves efficiency but also enhances the practical applicability of the model.

### Strengths
1. The performance of the proposed method is commendable. It even surpasses the SFT approach on the same set of math related queries, which indicates its effectiveness and potential for broader application.
2. The area of LLM reasoning with tool usage is an important topic. 
3. This paper involves many in-depth analysis on the proposed method and different experiment settings.

### Weaknesses
The organization of the second section of the paper appears somewhat confusing. It could benefit from a restructuring to enhance readability and coherence. Specifically, introducing an overarching pipeline at the beginning of the section could provide a clearer framework. And the relationship between sections 2.2 and 2.3 with section 2.1 needs to be more explicitly defined to better understand the flow and integration of ideas.

### Questions
1. Given that the proposed method primarily requires math-related queries, has there been any exploration into having the model generate its queries autonomously? This could potentially lead to self-improvement paradigm, further enhancing its effectiveness and applicability.
2. Will the authors consider open-sourcing the code? 
3. Have the authors tried larger size models? (e.g. 13B)

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
The paper, titled "AutoCode4Math: Learning Autonomous Code Integration for Math LLMs," addresses the limited ability of math-focused language models to make independent decisions on whether to use chain-of-thought (CoT) reasoning or code execution for problem-solving.
Generally, such models follow externally given instructions for choosing amongst them, narrowing their ability to operate autonomously while the integration of the best option will be done for answering the query on mathematics. To tackle it, the authors build an Expectation-Maximization framework that offers the ability for the LLM to learn autonomous code integration by furthering decision-making capacity through self-exploration. In this regard, the model alternates between self-teaching phases, E-step, after which an update derived from refined beliefs is set, M-step, to form an optimized methodology selection strategy. Experiments show that such an approach results in a significant accuracy gain when tested with lower code-execution requirements: an improved performance of nearly 20% on the MATH benchmark, with virtually a 65% reduction in code executions.

### Strengths
The study makes a significant contribution by addressing how models can autonomously choose between Proof-of-Thought (PoT) and Chain-of-Thought (CoT) approaches during mathematical problem-solving. This research identifies an important gap in current language models' ability to self-direct their reasoning strategies. Through their experiments, the authors demonstrate that incorporating autonomous decision-making in training leads to measurable performance improvements. The results validate that self-directed methodology selection, driven by expectation maximization, enhances mathematical problem-solving capabilities.

### Weaknesses
# Motivation for Using Expectation-Maximization (EM)

The paper introduces Expectation-Maximization (EM) to autonomously select between Chain of Thought (CoT) or code methodologies for solving math queries without external supervision. However, the motivation for this choice of EM remains unclear in several respects:
- Lack of Comparative Analysis: While the paper suggests EM is superior to standard reinforcement learning (RL), it does not provide a rigorous comparative analysis or an explanation of its advantages over other optimization techniques. The narrative suggests that EM holds unique benefits, but it is unclear why it is preferred over RL or simpler alternatives like supervised fine-tuning with reinforcement. Additional justification is needed to establish EM’s unique suitability for method selection in this context. Specifically, the paper lacks a clear articulation of how EM addresses the exploration-exploitation trade-off in this context compared to RL methods. It is not clear if EM's implicit policy improvement is more effective than explicit policy gradient methods in this setting.
- Efficiency Assumptions: The use of EM is partly based on the assumption that it narrows the policy search space, thereby enhancing efficiency. However, there is no empirical evidence provided to demonstrate that EM’s efficiency leads to actual performance gains in selecting between CoT and code for complex queries. Without comparative data, it is difficult to assess whether this efficiency is observed in practice or remains theoretical in this case. The paper does not quantify the reduction in search space or provide any analysis on how this reduction translates to faster convergence or better performance compared to other methods.
# Insufficient Comparison with Baselines for Model Selection
The effectiveness of AutoCode4Math’s approach to method selection would benefit from more detailed comparisons with existing baselines:
- Baseline Limitations: While current baseline models (e.g., Qwen2Math, GPT-4o, and DeepseekMath) primarily employ CoT over code for math queries, the lack of detailed performance metrics for these baselines limits the reader’s ability to assess AutoCode4Math’s advantages. Controlled comparisons with these models would help substantiate claims about AutoCode’s effectiveness in methodology selection. The paper should include metrics such as precision, recall, and F1-score for method selection to provide a more comprehensive evaluation.
- Effectiveness of Autonomous Decision-Making: The paper highlights AutoCode4Math’s advantage in reducing code executions and improving accuracy, but lacks direct performance comparisons with established models like GPT-4 and Mammoth. Quantitative evidence of accuracy improvements tied to better method selection would strengthen the claims of AutoCode4Math’s benefit. It is unclear whether the observed improvements are solely due to better method selection or other factors, such as the model's inherent capabilities or training data. A breakdown of performance gains attributed to method selection would be valuable.
- Comparisons with Standard RL Techniques: Although the paper briefly mentions an offline RL baseline, it does not detail the data, algorithm specifics, or other critical aspects of that experiment. A comparison with rejection-sampling and preference-learning-based approaches would further contextualize AutoCode4Math’s methodology and showcase its relative effectiveness. The paper should include details on the reward function, exploration strategy, and policy update mechanism used in the offline RL baseline to facilitate a fair comparison.

### Questions
### Motivation for Using EM
1. **Why is EM chosen over alternative methods like standard reinforcement learning (RL) or supervised fine-tuning?**  
   - What specific advantages does EM bring to methodology selection that simpler or more commonly used techniques cannot provide?

2. **How does EM uniquely contribute to the narrowing of the policy search space?**  
   - Could you provide empirical evidence or a theoretical basis for how EM improves efficiency in selecting between Chain of Thought (CoT) and code-based approaches?

3. **What is the theoretical or experimental basis for assuming that EM will reduce computational load or enhance efficiency in methodology selection?**  
   - How does EM’s efficiency in narrowing the search space compare to RL or other optimization methods in this particular task?

### Comparison with Baselines for Model Selection
4. **How does AutoCode4Math perform compared to current baselines, specifically in terms of method selection effectiveness?**  
   - Could you provide a detailed, controlled comparison with baseline models like Qwen2Math, GPT-4o, and DeepseekMath, showing how frequently and accurately AutoCode4Math selects CoT versus code?

5. **What improvements in accuracy or reduction in code execution does AutoCode4Math achieve over established models such as GPT-4 and Mammoth?**  
   - Are there quantitative metrics available that directly correlate the model’s method selection accuracy with overall performance improvements?

6. **Could you expand on the offline RL baseline and provide details on the data, algorithm, and setup of this experiment?**  
   - What comparisons are made with other RL methods or preference-learning-based approaches? How does AutoCode4Math fare against these methods, particularly in terms of accuracy and computational efficiency?

### Soundness
2

### Presentation
1

### Contribution
3

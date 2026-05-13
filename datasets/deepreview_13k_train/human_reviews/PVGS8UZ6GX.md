# Transformers Can Navigate Mazes With Multi-Step Prediction

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
\abstracttext

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes MLM-U, a training objective for improving multi-step prediction for transformers. Specifically, they propose to use MLM-U, an objective which predicts a span based on surrounding information, similar to the early MLM objective in fine-tuning BERT. Differently, they only use masks and don't use token substitution. Though the approach is very simple, they show that fine-tuning the transformer on two synthetic datasets (created with DFS and A*) with MLM-U objective achieves significantly better performance compared with the next-token-prediction loss usually used in decoder-only models. Besides, they find that fine-tuning with MLM-U tends to converge much faster and demonstrates much better generalization capability to unseen mazes. Their findings suggest that MLM-U objective can be effectively used to improve transformer based agents' capability in multi-step prediction.

### Strengths
1. The proposed objective MLM-U, though simple, is very effective in improving the performance of multi-step planning for maze navigation. 
2. This paper provides a detailed analysis of the convergence speed, and generalization capability of the fine-tuned model, both suggesting that the transformer fine-tuned with MLM-U tends to achieve much better performance. 
3. This paper is well-written and easy to follow.

### Weaknesses
1. Some implementation details are not clear to me. For example, when using different objectives, is it the case that MLM-U is applied to encoder-decoder architecture while next-token prediction is used for decoder-only architecture? Does the base model architecture influence the final performance (e.g., next token prediction on encoder-decoder architecture)? It is crucial to understand if the performance gains are solely due to the objective function or if the architectural choices are also a contributing factor. The paper should provide a more thorough ablation study on the model architecture to isolate the impact of the MLM-U objective.
2. The paper emphasizes the importance of RoPE positional encoding. However, the experiments related seem to be about training hyperparameters (i.e., fp16 vs. fp32). I feel it's more reasonable to compare with other positional encodings if the author wants to claim the importance of RoPE positional encoding, otherwise it might be better to call it training hyperparameter ablation. The current experiments do not sufficiently justify the claim about the specific importance of RoPE. A comparison with other positional encoding schemes, such as learned positional embeddings or sinusoidal encodings, would be necessary to validate this claim.
3. The novelty of the MLM-U objective might be small, as it has been widely explored in many encoder-decoder architecture works. While the application to multi-step planning is interesting, the core objective itself is not entirely novel. The paper should more clearly articulate the specific novelty of applying MLM-U in this context, beyond simply using it for a different task. It would be helpful to discuss how this specific application differs from prior uses of MLM-U and what unique challenges it addresses.

### Questions
Please refer to weakness.

### Soundness
2

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
In this work, the authors investigated whether Transformers can perform well in long-term planning tasks, and conduct experiments on the maze navigation task. As the conventional next-token prediction (NTP) objective is notorious about its shortcomings with navigation and planning, the authors propose to leverage MLM-U, an objective that encourages the model to learn with the entire traces in a non-autoregressive manner to better grasp the ability of multi-step planning. In fair experimental settings, the authors have demonstrated that the MLM-U objective outperforms NTP in terms of both performance and efficiency.

### Strengths
- A timely work in the field of the planning ability of Transformers. The study with the MLM-U objective is nice to read.
- The superiority of MLM-U over NTP with additional supervision from A* search traces, as well as the efficiency in the use of training data, demonstrates the effectiveness of MLM-U.

### Weaknesses
 - A general weakness point is that this work is mostly about the application of the MLM-U objective, proposed in prior work, to the maze navigation domain. This limits the novelty of the work, and further demands the empirical experiments to be more sound and sufficient.

For other points, please refer to the Questions listed below.

- The experiments do not sufficiently explore the generalization capabilities of MLM-U compared to NTP, particularly regarding varying maze sizes. The current setup, where training and testing occur on mazes of identical dimensions, fails to address how well MLM-U adapts to unseen maze complexities. This is a critical oversight, as real-world planning scenarios often involve environments of varying scales. The lack of experiments on different maze sizes limits the practical applicability of the findings.

- The analysis regarding the precision of positional encodings in Section 5.4 is not sufficiently detailed. While the authors note the importance of positional encoding precision for MLM-U, the explanation lacks depth. It is unclear why MLM-U is more sensitive to this than NTP. A more thorough investigation into the failure modes of half-precision positional encodings, perhaps by visualizing the learned representations or analyzing the gradient flow, would strengthen the analysis. The current explanation is somewhat speculative and does not provide a solid understanding of the underlying mechanisms.

- The paper does not explore the potential of using MLM-U for fine-tuning large language models (LLMs). Given the increasing prevalence of LLMs, it would be highly valuable to investigate whether MLM-U can enhance the multi-step planning capabilities of these models. The current experiments, which focus on training from scratch, do not address the practical question of how MLM-U can be integrated into existing LLM workflows. This is a significant gap, as fine-tuning is a common practice in the field, and the potential benefits of MLM-U in this context are not explored.

### Questions
- Are all of the experiments covered in this work equipped with the setting that the test data falls in distribution with the training data in terms of the size of the maze? In other words, Did the experiments on 30x30 mazes leverage the traces of 30x30 mazes for training, and further test on 30x30 mazes as well? It would be great to study the generalization of MLM-U in comparison with NTP in terms of the task difficulty. More specifically, two lines of experiments could be added:
  1. Train on traces of N_1 x N_1 mazes, then test on mazes of N_1 x N_1, N_2 x N_2, N_3 x N_3 ... (we can set N_1 < N_2 < N_3, or N_1 > N_2 > N_3; different meanings are implied).
  2. Train on traces of both N_1 x N_1 and N_2 x N_2 mazes, then test on mazes of N_1 x N_1 and N_2 x N_2. This studies whether MLM-U could exploit positive transfer or handle negative interference within data; And compare with NTP to get the understanding of which one is better.

- In Section 5.4, why would the precision of the positional encoding especially matter in this MLM-U training paradigm? Is it related the difficulty of training with the MLM-U objective? More analysis on the failed training dynamics with half-precision positional encodings will further contribute to the soundness of the paper.

- In this work, the Transformer models are trained from scratch using NTP or MLM-U objectives. However, I believe the contributions of the work would be much greater if the authors conduct experiments with LLMs in the finetuning stage: Instead of leveraging the NTP objective in SFT, try using MLM-U and discover whether the most capable open-sourced LLMs nowadays like LLaMa 3.1 could be empowered with the multi-step prediction ability. Then an interesting further question would be whether using MLM-U instead of NTP in the SFT stage would be harmful to other SFT data that is to be trained with the NTP objective. I encourage the authors to conduct additional experiments to respond with at least the first question (the utility of MLM-U in the SFT stage for OSS LLMs like LLaMa) to further improve this work.

I would consider raising my scores if the authors address my concerns properly.

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
This paper explores the applicability of MLM-U (Masked Language Modeling + Uniformly Sampled Masking Ratios) to training transformers to perform simple maze navigation tasks. It finds that compared to next token prediction, MLM-U based transformers can more accurately navigate mazes, completing 93.8% of 30x30 mazes, while next-token prediction models complete only 18.8% (with training on 3K epochs of 100K mazes). Further, MLM-U based transformers are more data and training efficient, saturating navigation accuracy on 5x5 mazes 2x faster than next-token prediction (training efficiency), and with almost 4x fewer training mazes.

### Strengths
- The paper tackles an interesting and challenging issue—transformers' limitations in long-term planning.
- The application of MLM-U to the task is well-motivated, and it seems logical and reasonable that using MLM-U-based approaches would improve the performance on maze navigation tasks.
- The paper clearly demonstrates that MLM-U is more efficient as a training procedure than next token prediction given the setup, and the gains reported in the paper are quite impressive.
- The scaling results are impressive, suggesting that this is a promising direction of research for larger models, and more complex tasks.
- As far as I am aware, no existing work has clearly demonstrated the effects of MLM-U, or MLM-based training approaches on maze prediction tasks.
- The paper is generally well-structured, and the visualizations (e.g., maze complexity graphs, accuracy charts) are helpful.

### Weaknesses
While the paper does have some notable strengths, there are also several weaknesses:
- Some of the key setup and explanation details are missing from the paper, for example: What is the input representation of the mazes (does it match the Lehnert paper? Or are there modifications)? What is the task definition (how much information is given about the maze - is the full representation given, or only limited information, requiring the model to remember across the trajectory)? What is the definition of "navigation accuracy" (is this the same as A* solution accuracy in the Leonhart paper)? It seems like the paper overlooks some of these basics, without making reference to an identical setup, or clearly explaining in the text/appendix. 
- Given that the setup is identical to the Lehnert paper, I'm not sure that this paper actually contributes much to the conversation on long-horizon planning with transformers. While this is solid evidence that for a toy task such as A* navigation matching, adding MLM-based objectives can help improve the performance of the model, maze navigation itself does not really require foresight (especially in the full-information version of the task), and it's not clear that these results will generalize to other long-horizon planning problems. This paper would be significantly bolstered by adding additional domains (for example, In Lehnert, they solve Sokoban puzzles), or potentially other puzzle setups such as Sudoku, which might have slightly more complex mechanics and still require planning. As it stands, I think that primarily focusing on maze navigation is interesting, but perhaps too limited.
- While the motivation for the paper is that MLM-U allows the model to predict multiple steps both forward and backward, I'm not convinced that the setup actually does this. While the details are a bit thin, it seems like the the MLM approach is applied to full trajectories - which while it does encourage predicting multiple steps in the past, seems to be significantly harder to apply during the inference phase. Indeed, I'm not sure that this encourages "foresight" so much as "hindsight" or "justification", and maybe helps the model with memory instead of planning. 
- The paper has no baselines beyond next-token prediction. While the main motivation of the paper is to compare MLM-U with vanilla next token prediction, it would be good to include both the Bachmann & Nagarajan approach (predicting the entire path before gradient) and the Gloeckle approach (multiple future prediction heads) as baselines - given that both of these methods claim to be quite effective for this task, and represent comparable methods. 
- There is no statistical analysis of the data, and it seems like many of the results are drawn from a single training run on each of the methods. It would be good to see the variance of the data, particularly in Figures 3 and 4, to understand exactly how variable the convergence is (it seems like Figure 4 in particular could be susceptible to fairly high variance).

### Questions
- How is navigation accuracy defined? 
- What are the setup details (input representations, task definition, etc.)? 
- What precisely is the training algorithm for the approach? Is MLM applied to full trajectories? Or is MLM applied at each next-token prediction step? What are the sets of uniform masks used for MLM-U
- During decoding, how is the length of the initialized X determined? It seems like you need to already know the length of the final trajectory T in order to predict the masked tokens. 
- How many of the failure cases are equivalent shortest paths that are not equivalent to the deterministic approach (as discussed in Appendix. C)? Are these a significant portion of the results? 
- Are there any explicit failure modes recognized in the MLM-U examples (particularly for larger mazes) - or does MLM-U struggle with any categories of maze structure in particular (i.e. those with higher branching factors)?
- Are there any limits on data efficiency gains with MLM-U? How well does it perform on even larger mazes (perhaps 50x50 mazes)? 
- Are there data effects from using a smaller number of mazes (i.e. 100K) over a larger number of epochs (3000) rather than a larger number of mazes/more diverse set of mazes in general? How does this compare if you use more dynamic sets of mazes such as in the Lehnert paper (which uses up to 1M unique mazes)? It would be good to replicate Fig 11/12 from that paper in order to get a better idea of the training data scaling. 

Some minor comments:
- There's a couple of un-supported claims in the paper that would benefit from citation (L35: "transformers encounter challenges when tasked with planning and decision-making over extended horizon", L37: "particularly evident in tasks requiring foresight")
- Saying that masking rates are "uniform" is somewhat under-specified, and upon reading the appendix, it seems like "uniform" means that the masking rate is _drawn from a uniform distribution_. It would be good to clarify this use of terminology, and clearly specify the exact distribution used for the masking rate in MLM-U.

### Soundness
2

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
The paper "Transformers Can Navigate Mazes with Multi-Step Prediction" investigates whether an alternative training objective, termed MLM-U, can enhance transformers' maze navigation abilities compared to the standard next token prediction objective. The authors note that traditional transformers struggle with long-term planning tasks, such as navigating mazes, as they are typically trained to predict the next token based on the previous tokens. The MLM-U objective, inspired by masked language modeling, aims to explicitly predict multiple steps ahead and backward, encouraging better long-term planning.

The authors train transformers using both the standard next token prediction and MLM-U objectives to navigate various types of mazes, comparing performance across different maze complexities and transformer model sizes. They find that MLM-U significantly outperforms the next token objective in maze navigation, particularly for more complex tasks. Additionally, MLM-U demonstrates improved sample efficiency, reduced training time, and better generalization. For example, transformers trained with MLM-U achieve higher accuracy on mazes up to 30x30 in size and outperform larger transformers trained with next token prediction, even those with additional A* search trace supervision.

Key contributions of the paper include:
1. Demonstration of MLM-U's superior performance in long-term planning tasks, achieving better maze navigation accuracy across all tested maze complexities.
2. MLM-U is found to be more sample-efficient and computationally efficient than next token training.
3. Detailed exploration of the impact of model size, showing that scaling up transformers trained with MLM-U leads to significant gains in performance.

These findings suggest that modifying the learning objective to include explicit multi-step planning can significantly improve the capabilities of transformers in navigation tasks, highlighting a promising direction for further research on long-horizon planning with transformers.

### Strengths
### Originality
The paper introduces **MLM-U**, a novel training objective that encourages explicit multi-step prediction both forward and backward, enhancing transformers’ long-term planning capabilities. This approach is original in combining masked prediction with maze navigation, showcasing transformers in a novel, decision-making context.

### Quality
The study is methodologically robust, providing a controlled comparison between MLM-U and traditional next token prediction. It employs diverse maze environments and measures both **accuracy** and **training efficiency**, ensuring the findings are well-supported. The visualizations and detailed experimental analysis add credibility to the work.

### Clarity
The paper is **clearly written**, with effective motivation for MLM-U and well-organized results. Visual aids enhance understanding. Slightly more explicit detail on the training process could further improve accessibility, but overall, the flow is logical and easy to follow.

### Significance
The **MLM-U objective** significantly improves the planning capabilities of transformers, demonstrating better sample efficiency and faster convergence. This work paves the way for **more efficient models** that require fewer computational resources, potentially impacting areas like robotics and game-playing. Its contributions to extending transformers into new sequential decision-making tasks are noteworthy.

### Weaknesses
### Limited Novelty in Training Objective
MLM-U's novelty may be limited as similar multi-step prediction methods have been explored in reinforcement learning and trajectory modeling. Including a **comparative analysis** with existing methods would help strengthen the originality.

### Limited Experimental Complexity
The experiments focus only on maze navigation, which may not fully demonstrate MLM-U's broader applicability. Extending experiments to tasks requiring **complex long-term planning** (e.g., robotics or control tasks) would provide stronger evidence of general utility. Testing in **dynamic or uncertain environments** would further demonstrate robustness.

### Limited Baseline Comparisons
The paper mainly compares MLM-U against next token prediction, missing comparisons to stronger baselines like **reinforcement learning approaches** or **graph-based transformers**. Including such baselines would provide a more rigorous benchmark of MLM-U's performance.

### Scalability Concerns
The scalability analysis is limited. More discussion on **scaling challenges** and **computational trade-offs** when using larger models is needed. An ablation study on **hyperparameters** like masking ratios and model depth would help understand how to best tune MLM-U for different settings.

### Insufficient Analysis of Failure Cases
The paper lacks a detailed analysis of **failure cases**. A more in-depth examination of **common failure patterns** and scenarios where MLM-U struggles would provide valuable insights for improving the model and identifying its limitations.

### Questions
### Limited Novelty in Training Objective
- Could you provide a more detailed comparison between MLM-U and existing multi-step prediction methods? Specifically, how does MLM-U address limitations in prior approaches?

### Limited Experimental Complexity
- Can you provide results or discuss potential outcomes for applying MLM-U to tasks beyond maze navigation?
- Do you foresee any challenges or necessary modifications when extending MLM-U to dynamic or uncertain environments?

### Limited Baseline Comparisons
- Have you considered comparing MLM-U to reinforcement learning-based methods? What would be the expected advantages or drawbacks?
- Could additional baselines be included in future work to provide a clearer benchmark?

### Scalability Concerns
- Could you expand on the potential challenges when scaling MLM-U to larger models or more complex environments?
- Would it be possible to include an ablation study on hyperparameters like masking ratios to better understand their impact?

### Insufficient Analysis of Failure Cases
- Could you provide more detailed examples of MLM-U's failure cases and potential reasons behind these failures?
- What changes could be made to the model or training process to address these failure modes?

### Soundness
2

### Presentation
2

### Contribution
2

## Human Reviewer 1

### Summary
This paper proposes a way to train a decision transformer with textual descriptions. The problem setting is as follows: we are given trajectories with text labels, and we want to train a multi-task policy that can handle unseen task descriptions at test time, mainly in a zero-shot manner. To do this, the authors first encode text descriptions into a latent space using contrastive learning with behaviors. With the learned text embeddings, they train a decision transformer on the dataset trajectories. This method is called the text-guided decision transformer (TG-DT). The authors evaluate TG-DT on several HalfCheetah, Ant, and Meta-World tasks, comparing its performance with previous DT and language-conditioned RL methods.

### Strengths
* The problem setting is important and the proposed method is reasonable.
* The paper provides several ablation studies about each component of the method, which helps understand their relative importance.

### Weaknesses
* I think the biggest weakness of this paper is its empirical evaluation. The authors only evaluate their method on "classic" tasks like HalfCheetah, Ant, and Meta-World. They are not the most "natural" language-based tasks either, and it is unclear how this method works on *actual* language-based benchmarks, such as CALVIN, LIBERO, or the one used in UniPi. Evaluating on classic tasks would be fine if the paper were more theory-oriented, but since this paper is purely empirically motivated and based on scalable transformer learning, I believe it is important to demonstrate its ability on tasks that the community currently finds more relevant.
* Moreover, even on these "classic" tasks, their performance gain seems marginal (Tables 1 and 2). This makes the additional complexity introduced in this paper questionable. I suspect this might again stem from the simplicity of the evaluation tasks.
* I'm not sure the term "offline meta-RL" is appropriate. To me, the problem setting considered in this paper is simply language-conditioned RL (and/or multi-task RL), with a focus on generalization toward unseen tasks. Meta-RL typically involves additional online rollouts or task-specific offline datasets for quick *adaptation*, while this paper mainly focuses on the zero-shot setting (I know the paper also has few-shot adaptation experiments, but they are based on naive fine-tuning with no specific meta-RL techniques, unlike typical meta-RL methods like MAML, PEARL, etc.). Are there similar previous offline RL works that refer to this setting as "meta-RL"? If not, I'd encourage the authors to revise the problem statement and terminology to prevent unnecessary misunderstanding.
* (Relatively minor) The writing could generally be further improved. For example, the big picture of the method wasn't very clear at the beginning of Section 3, so TBC and TBM seem a bit ad hoc until one understands how the learned embeddings are actually used in Section 3.3. An algorithm box could help. Figure 1 is also hard to parse. From the figure, it seems the text and behavior datasets are separated (I think they're paired -- correct me if I'm wrong), and it is not immediately clear how a decision transformer plays a role in this method (from the figure, it appears that the dataset trajectory itself (in particular, without text embedding) is the input to the DT, which is not the case I suppose).

### Questions
I don't have additional questions beyond the ones raised in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes TG-DT, a framework that leverages textual task descriptions to enable zero-shot generalization to unseen tasks. The method builds upon Decision Transformer and introduces dual contrastive and matching-based objectives to jointly train a text encoder, behavior encoder, and text–behavior encoder–decoder. Experiments on Cheetah-dir, Cheetah-vel, Ant-dir, ML10, and ML45 show that TG-DT achieves improvements over baseline methods.

### Strengths
- The paper is clearly written and easy to follow.
 - The problem of generalizing to new tasks without additional demonstrations is relevant and important for data-efficient robot learning.

### Weaknesses
- Although the problem setting is meaningful, the novelty appears limited. There has been substantial recent progress in aligning natural language with embodied behaviors (e.g., vision-language-action models such as Otter [https://arxiv.org/pdf/2503.03734] and related cross-modal alignment frameworks). The conceptual contribution of TG-DT, aligning text descriptions with behaviors, may therefore be seen as incremental unless its advantages are more concretely demonstrated.
 - The experimental results show only modest gains over the baselines (e.g., as shown in Figure 3). Given the simplicity of the evaluated locomotion and meta-RL benchmarks, it is unclear whether the approach would scale to more complex tasks. The significance of the improvement is therefore limited.
 - The paper does not sufficiently explain how textual task descriptions are constructed and shared across multiple tasks, particularly when the task goals differ conceptually. Additional clarification and concrete examples of task descriptions would be helpful. Details about how templates are applied and how text variation affects generalization are needed for reproducibility.

### Questions
- The paper provides a task description template, but how is the same template applied across tasks with different objectives? Could you provide concrete examples of task descriptions used in each benchmark?
 - Do you foresee ways to improve the performance of TG-DT? If current benchmarks are saturated, have you considered evaluating on more complex or realistic task suites where text grounding may provide clearer advantages?
 - How sensitive is TG-DT to the richness or specificity of text descriptions? For example, does adding more descriptive language improve performance?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper proposes a decision transformer method guided by text to address the offline meta-reinforcement learning problem. The proposed Text-Guided Decision Transformer (TG-DT) aligns text and trajectory representations via a dual alignment mechanism, and then conditions a DT-style policy on the aligned text embedding to act on unseen tasks using only their textual descriptions. A description-guided data-sharing heuristic is optionally used to fine-tune the model with trajectories from semantically similar training tasks. Experiments on MuJoCo and Meta-World demonstrate the zero-shot and few-shot abilities of TG-DT compared with DT variant baselines.

### Strengths
- The paper introduces an interesting idea of incorporating text descriptions into meta-RL tasks to guide the DT trajectory.
- The proposed dual alignment mechanism between language descriptions and trajectory representations is novel.
- Empirical results on MuJoCo and Meta-World support the effectiveness of the proposed method in zero-shot and few-shot settings.

### Weaknesses
- The design of the proposed modules lacks detailed justification. The dual alignment mechanism and the description-guided data-sharing are not well motivated or clearly explained in the methodology section.
- The experimental results show that the proposed method achieves only marginal improvements over the baselines while potentially incurring substantial computational overhead. Moreover, the paper does not provide any comparison of computational costs between the proposed method and the baselines.
- For zero-shot settings, some baselines such as PDT and HDT are not designed for this setting, leading to unfair comparisons. For few-shot settings, although the proposed method fine-tunes the model on new tasks, it still shows unsatisfactory performance compared with the baselines.
- The results lack the standard deviation, making it difficult to evaluate the true performance of the proposed method.

### Questions
- Could you explain in more detail the design of the dual alignment mechanism and the description-guided data-sharing? What is the motivation for using these two modules?
- Could you provide the computational cost of the proposed method compared with the baselines?
- Could you elaborate on why the proposed method shows unsatisfactory performance in few-shot settings compared with the baselines even after fine-tuning?
- Could you provide the standard deviation of the results to illustrate the performance variance?
- In Tables 1 and 2, what do the “5 runs” refer to? Does it mean 5 different random seeds or 5 different trajectories?
- During inference, the proposed method encodes text descriptions using a language model. How are these language descriptions obtained? Do they rely on prior information about the unseen tasks?
- Could you discuss more related works such as [1] and [2], which also leverage language models for meta-RL tasks? What are the key differences between your method and these approaches?

[1] *Pre-trained Language Models Improve the Few-shot Prompt Ability of Decision Transformer*, 2024

[2] *LLM-Driven Policy Diffusion: Enhancing Generalization in Offline Reinforcement Learning*, 2025

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4
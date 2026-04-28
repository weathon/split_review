# GROOT-2: Weakly Supervised Multimodal Instruction Following Agents

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Developing agents that can follow multimodal instructions remains a fundamental challenge in robotics and AI. Although large-scale pre-training on unlabeled datasets has enabled agents to learn diverse behaviors, these agents often struggle with following instructions. While augmenting the dataset with instruction labels can mitigate this issue, acquiring such high-quality annotations at scale is impractical. 
To address this issue, we frame the problem as a semi-supervised learning task and introduce \agent, a multimodal instructable agent trained using a novel approach that combines weak supervision with latent variable models. Our method consists of two key components: constrained self-imitating, which utilizes large amounts of unlabeled demonstrations to enable the policy to learn diverse behaviors, and human intention alignment, which uses a smaller set of labeled demonstrations to ensure the latent space reflects human intentions. \agent’s effectiveness is validated across four diverse environments, ranging from video games to robotic manipulation, demonstrating its robust multimodal instruction-following capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a simple VAE style architecture to combine a small amount of language/return annotated data with a large demonstration-only dataset to learn a downstream policy. The authors test the method on Atari, Robotics benchmarks (Simpler and Language Table) and MineCraft. The authors compare their work to several per domain baselines and report strong improvements in MineCraft. Robotics results show smaller/statistically insignificant gains.

### Strengths
Strengths:
1. The paper is well written and easy to understand
2. The theoretical underpinnings of the work are clearly described using the R ratio diagrams. This motivates the work well.
3. The experimental suite is large and the method seems to work on a variety of benchmarks. 
4. The question of utilizing labeled and label-free demonstrations needs to be answered in order to move the needle on generalist agents.

### Weaknesses
While I enjoyed reading the paper I have several issues with the current version of the paper. It reads more like a technical report for promotion purposes, not scientific material. I enlist my qualms below:
1. **How much supervision?:** While the authors have the word “weakly supervised”, it's unclear how much supervision is actually being used. Are all tasks covered in the labeled demonstration dataset? Is there any amount of language generalization that occurs, for e.g., are any tasks solvable zero-shot? How good are the demonstrations? What if there was play data/suboptimal demonstrations in the unlabeled demonstration dataset? Would the method still work? None of these questions are answered and I think they should be added since the focus of the work is weak supervision.
2. **No ablations/experiments describing model architectures?:** How does initializing the model with something other than BERT work? What about vision inputs? No ablations on ViT architectures initializations are provided. Works like LIV (https://arxiv.org/abs/2306.00958), R3M etc are available as baselines?
3. **Returns is not language:** The choice of adding of Atari is odd - there are no language labels here. Incidentally, it is only here that details of the amount of labels are provided. What is the distribution of labels? Are they mostly high reward trajectories? If return conditioned imitation is the focus, then works like Multi-game Decision transformer, CQL and other offline methods should be added as baselines. The rest of the paper does not consider return conditioning at all, so this section feels out-of-place.
4. **Missing baseline.** A very necessary baseline, I believe, is missing here. What if you trained a classifier on all the labeled data, which conditioned on a video would generate the textual label for the video. This labeler could be subsequently used to pseudo label all the demonstration-only data. Finally, a language conditioned imitation learning agent could be trained on this pseudo-labeled data along with the labeled demonstrations. This I believe is a natural baseline to your work. This is missing.  
5. **Baselines are uninformative:** In the robotics section, why compare with RT-1? It’s trained on a different data distribution and it has a different architecture? This comparison generates more questions than answers. A clean experiment here would be retraining an open source Octo/OpenVLA model on all the labeled data only, i.e., only utilizing your labeled dataset.   
6. **Missing ablation on amount of labeled data:** While I appreciate that the method scales with unlabeled data, what happens when the amount of labeled data is varied? Afterall, this is the limiting resource for this work. 
7. Table 1 is missing error bars.

### Questions
1. How was beta_1 and beta_2  tuned? How was the R ratio controlled empirically?  
2. Does the model finetune easily? If one were to use the model for a new set of tasks, would this transfer be data efficient

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an imitation learning method for training policies that can follow multi-modal instructions (either language or a video demonstration) using data that is only partially labeled with language. Like a prior paper, GROOT, they train a VAE on the expert data to obtain an encoder that produces a latent given a reference video as well as a latent-conditioned policy that predicts actions given an observation history and the latent. In this way the latent space models the demonstrator's intentions, and the policy can be commanded with a reference video by querying a latent from the encoder. This paper extends GROOT to the case where some of the expert data is labeled with language instructions. The authors modify the encoder to additionally accept language, and they introduce a new loss term that aligns the latents produced by language with those produced by the corresponding reference videos. In this way the language labels assist in learning a more well-structured latent space. Experiments on Minecraft, Atari, SIMPLER, and Language Table demonstrate that the proposed method, GROOT-2, outperforms GROOT and other relevant baselines when commanded with language or reference videos.

### Strengths
The paper addresses an important problem since language annotations are not always easy to acquire for imitation learning datasets. The method presented is a novel modification of an existing method which adds a non-trivial new capability. The explanation of "latent space ambiguity" is a nice justification for the method. The experiments cover a wide range of simulated settings.

### Weaknesses
My main concerns are some issues with the evaluation and the presentation/writing.

**Evaluation**

- It seems a central question is whether language loss ($L_{lab}$) improves reference video following capabilities and whether the reference video loss ($L_{dem}$) improves the language following capabilities. The cleanest way to answer this question would be to train with the GROOT-2 architecture and try removing either one of these loss components but keeping dataset size the same. However, I don't see this experiment. The atari experiment only tries removing $L_{lab}$. It is crucial to understand the individual contributions of each loss term, and ablating each loss while keeping the training data constant is necessary to isolate their effects. For example, if removing $L_{lab}$ does not significantly impact video following, it would suggest that the language data is not effectively improving the latent space for video-based tasks.
- For each evaluation setting, please report what proportion of the training data is labeled with language and whether there are language labels for the tasks that were evaluated. It is important to know the degree of supervision for each task to understand how the method performs under varying levels of language annotation. For example, if some tasks have no language labels during training, it would be important to know if the method can still generalize to these tasks through the video modality.
-  Only table 2 has error bars. It'd be great to have them for all the results. The lack of error bars makes it difficult to assess the statistical significance of the results. Without them, it's hard to determine if the observed differences between methods are meaningful or due to random variation.
- Why are there dashes in Table 2? Are the numbers taken from the prior papers (and they didn't provide the per task breakdown)? If so, did their evaluation protocol match your evaluation protocol? If the baselines are not directly comparable due to different evaluation protocols, it should be clearly stated.
- In the t-SNE plots there should be a legend showing what the colors mean. Without a legend, the t-SNE plots are difficult to interpret, and it's hard to understand what the different clusters represent.
- Why was a human-normalized score used as a metric for the Minecraft experiments focused on scaling up unlabeled demos, but a different metric used in Table 1? Using different metrics across experiments makes it difficult to compare results and draw general conclusions. It would be better to use a consistent metric across all experiments or provide a clear justification for using different metrics.
- This sentence is confusing: "This enhancement may be due to the limitations of our text-demonstration data collection method, which might not include text annotations related to the Climb Mountain task." If there are no text annotations for this task, then what was the 0% unlabeled data policy trained on? It's unclear how a policy can be trained on a task if there are no associated text annotations, even when using only unlabeled data. This needs clarification.

**Presentation/Writing**

- It'd be nice to state the main questions the experiments are designed to answer at the beginning of the section. This would help the reader understand the motivation behind each experiment and the key takeaways.
- The main text should clarify whether the encoder is a single model or multiple models. It's important to know the architecture of the encoder to understand how the different modalities are processed.
- In tables 1, 2, and 3 bold the best result for each task. This would make them easier to read. Highlighting the best results would make it easier to quickly identify the best-performing method for each task.
- The related work should discuss the relationship between prior work and the proposed method rather than just listing prior work. Additional papers to discuss/cite include GRIF which attempts to align task representations from language and initial state-goal pairs as well as another work that uses videos as a task specifications.
- In the conclusion, "play data" does not typically mean data without actions, so I would avoid using this term here.

### Questions
- It seems the prior $e(z | o_1)$ is only ever input the first observation. Shouldn't the prior receive all the observations up to the current timestep $t$ like in equation 1?
- In the SIMPLER evaluation, did you use Octo-1.5 or the original Octo model? The original model actually works better on SIMPLER.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This submission introduces GROOT-2, a weakly self-supervised instruction-following agent. It is trained in two stages, with the first being pretrained on large web data and the second being fine-tuning with small amount of human annotated data. Experiments are conducted on three different benchmarks, ranging from video games to robotics. It demonstrates competitive performance against previous approaches.

### Strengths
- Good writing and illustrative examples, easy to follow.
- Sufficient evaluation on three benchmarks.
- Good analysis.

### Weaknesses
 - The idea to train latent-space conditioned policy is not novel. Although authors claim that the introduced "constrained self-imitating" and "human intention alignment" help to balance two extremes on the Pareto frontier, no ablations are showed to verity that.
- How is human annotation defined is unclear. Under the embodied AI and robotics context, human annotations usually refer to actions either collected or labeled by human. But in this work, human annotation seems to refer to high-level language instructions.
- Following the previous point, if action labels are indeed required to train the policies, how does the proposed method scale up to domains beyond video games and robot pick-and-place, where action labels are scarce?
- Experiment results seem not impressive enough. For those Minecraft tasks, the overall success rates are pretty low (only two tasks "interact" and "plant" succeed more than half). For robotics tasks, only the simple table-top picking-and-placing is demonstrated.

### Questions
1. L208: How web data come with action labels?
2. What is the task horizon in each environment?
3. Can authors show more complicated tasks? E.g., robotics tasks beyond table-top pick-and-place or real-robot experiments.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces GROOT-2, a multimodal instruction-following agent trained with a novel weakly supervised learning framework. GROOT-2 addresses the challenge of multimodal instruction adherence in agents by reducing the reliance on labeled data, which is often costly and time-intensive to obtain. Instead, the model utilizes a two-part strategy: *constrained self-imitating* and *human intention alignment*. The constrained self-imitating method enables GROOT-2 to learn diverse behaviors from large sets of unlabeled demonstrations, while the human intention alignment component aligns the latent space of the model with human intentions using a smaller, labeled dataset. The authors validate GROOT-2’s performance across multiple environments, including video games like Atari and Minecraft, as well as robotic manipulation tasks, demonstrating that it outperforms previous models (e.g., GROOT-1 and STEVE-1) in multimodal instruction-following tasks.

### Strengths
1. **Novel Semi-Supervised Framework for Multimodal Instruction-Following:** The paper introduces a novel framework for training multimodal instruction-following agents with weak supervision. By framing the challenge as a semi-supervised problem, the authors effectively reduce reliance on costly labeled data, presenting a scalable alternative to fully supervised approaches. The combination of *constrained self-imitating* for leveraging large sets of unlabeled demonstrations and *human intention alignment* to ensure the latent space aligns with human intentions is both innovative and practical. This strategy addresses common issues like *posterior collapse* and *latent space ambiguity*, which have hindered multimodal instruction adherence in prior work. The proposed weakly supervised approach extends the applicability of instruction-following agents across a broad range of tasks and environments.

2. **Comprehensive Experimental Validation Across Diverse Environments:** The authors provide a rigorous empirical evaluation of GROOT-2 across multiple environments, including Atari games, Minecraft, and robotic manipulation tasks (e.g., Language Table and Simpler Env). The paper reports detailed quantitative comparisons against baseline models, such as GROOT-1 and STEVE-1, highlighting the model’s significant improvement across task families. Furthermore, the authors support the theoretical claims about their model with a thorough analysis of the learned latent space, illustrating how human intention alignment resolves ambiguities in latent representations. The experiments are comprehensive, with comparisons against varied baselines and multiple training data scales, showing the robustness and scalability of GROOT-2.

3. **Clear and Structured Presentation:** The paper is well-organized and clearly presents the problem, the proposed approach, and the experimental results.

4. **Broad Impact and Applicability of Weakly Supervised Instruction-Following:** The weakly supervised approach proposed by GROOT-2 has implications for the development of scalable, multimodal instruction-following agents. By reducing the reliance on labeled data, this framework broadens the feasibility of deploying such agents in real-world applications, where data annotation is often prohibitively expensive. The demonstrated effectiveness of GROOT-2 across diverse environments highlights its generalizability and adaptability. The contribution is particularly significant for applications in robotics, where the ability to follow human-like instructions across varied tasks without exhaustive labeling can accelerate the adoption of robotic agents.

### Weaknesses
1. **Scalability Limitations Due to Data Requirements**  
   Although GROOT-2 successfully reduces the need for labeled data by using weak supervision, its current framework still relies on trajectory data, which includes both observations and actions. This dependence restricts the model’s scalability, as a vast amount of available data on the internet, such as play data or interaction data, often lacks explicit action information. The authors acknowledge this limitation but do not provide a concrete solution for incorporating such unlabeled play data. Addressing this issue could further expand the scalability of GROOT-2, potentially allowing it to leverage far larger datasets. Future work could explore methods for approximating or inferring actions from play data or combining GROOT-2’s framework with unsupervised or self-supervised approaches to handle action-less data. 
**Recommendation:** Exploring methods to extend the framework to utilize play data would address a core scalability limitation.

2. **Evaluation Scope for Diverse Task Complexity:**  The paper demonstrates GROOT-2’s performance across varied environments; however, within each environment, the range of tasks presented may not fully capture the complexity of real-world, open-ended tasks. For instance, while Minecraft and Atari offer diverse scenarios, it remains unclear how well GROOT-2 would perform in environments with truly unpredictable dynamics or in tasks requiring complex, multi-step reasoning. An analysis of GROOT-2’s performance on tasks of varying complexity within each benchmark environment would provide a more granular understanding of the model’s adaptability and robustness. This could involve testing tasks with multiple dependencies or obstacles to simulate more realistic scenarios. 
**Recommendation:** Evaluating GROOT-2 on tasks of varying difficulty would yield insights into the model’s robustness and real-world applicability.

### Questions
See above sections.

### Soundness
3

### Presentation
3

### Contribution
2

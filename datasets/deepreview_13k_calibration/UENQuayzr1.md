# Efficient Cross-Episode Meta-RL

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 6, 3

## Abstract
We introduce Efficient Cross-Episodic Transformers (ECET), a new algorithm for online Meta-Reinforcement Learning that addresses the challenge of enabling reinforcement learning agents to perform effectively in previously unseen tasks. We demonstrate how past episodes serve as a rich source of in-context information, which our model effectively distills and applies to new contexts. Our learned algorithm is capable of outperforming the previous state-of-the-art and provides more efficient meta-training while significantly improving generalization capabilities. Experimental results, obtained across various simulated tasks of the MuJoCo, Meta-World and ManiSkill benchmarks, indicate a significant improvement in learning efficiency and adaptability compared to the state-of-the-art. Our approach enhances the agent's ability to generalize from limited data and paves the way for more robust and versatile AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes new online Meta-RL algorithm that is able to combine intra- and cross-episodic information to better make decisions under uncertainty. Each intra-episode is encoded into a latent variable by a transformer model, which are then processed altogether by another transformer and a context-specific latent is formed. Authors claim SOTA results on Maniskill and challenging Meta-World ML45 benchmarks, surpassing previous SOTA methods.

### Strengths
- The paper reports state of the art results on challenging tasks, including challenging environment Meta-World ML45.
- The method is explained clearly and visually explained.

### Weaknesses
[W1] Authors compare their method with TrMLR, which uses RNN in the outer-loop, while authors of the proposed method use transformer. I believe that the difference in the capacity can explain the performance distinction between two methods. To my mind, it is early to claim SOTA results without trying to match architectures first. Specifically, the transformer architecture, with its inherent ability to model long-range dependencies through self-attention, might provide an unfair advantage over the RNN-based approach in TrMLR, especially in tasks requiring long-term context. The authors should have at least attempted to use a transformer or a similar architecture with comparable capacity in the outer loop of TrMLR to isolate the effect of the proposed method from the architectural differences.

[W2] A strong baseline is missing from the paper: AMAGO [1]. The [1] authors do not report the results on ML45, stating it is left for the future work. However, since the main contribution of the paper is SOTA results, I believe AMAGO should be included in the baselines. Also, mind that AMAGO was introduced in ICLR”24.

[W3] Authors do not state whether the baselines (especially TrMLR) were tuned to get the best performance out of them. Again, as the paper claims SOTA results, it is vital to have this information. The lack of clarity on the hyperparameter tuning process for the baselines makes it difficult to assess whether the reported performance differences are due to the proposed method or simply due to suboptimal hyperparameter settings for the baselines. It is crucial to ensure that all methods are evaluated under their optimal conditions to make a fair comparison.

### Questions
1. I would appreciate if authors include an additional baseline method on ML45, AMAGO [1], to ensure the result of the proposed method is indeed SOTA.
2. To justify SOTA performance, I would also like to see the experiments on TrMLR with transformer or mamba architecture as an outer-loop memory model.
3. I would also appreciate it if authors provide how many hyperparameters were swept for the baseline TrMLR method and which method for HPO was used.

Although my initial recommendation is to reject the paper, I would be happy to revise my score as the authors address my questions. 

[1] Grigsby, Jake, Linxi Fan, and Yuke Zhu. "Amago: Scalable in-context reinforcement learning for adaptive agents.”

*After rebuttal update:* I changed my score to 6 since the questions were mostly addressed, see the comments for details.

### Soundness
2

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
This paper proposes a method for learning features for meta-reinforcement learning in latent space by training a two-level hierarchy of transformer networks. The lower layer is trained to represent trajectories experienced while doing a specific task (i.e. experiencing a single MDP) while the upper layer is trained on all tasks. This method is shown to have significantly better performance than several other meta-RL methods on a variety of meta-RL benchmarks, with the primary hypothesis for this being that the proposed architecture allows the networks to learn more general features that are informative across a variety of tasks. This hypothesis is supported by some experiments showing that embedded representations learned by the proposed method tend to cluster together by task more than representations learned by other methods.

### Strengths
Paper is overall clearly written and explained.

Related work positions the paper well.

Experiments are well designed.

I am a big fan of explicit hypothesis statements, and very much appreciate this paper for being clear about what it is investigating.

The idea is relatively simple and seems like a clear opportunity for more research.

The performance is impressive and the results are quite thorough.

### Weaknesses
There are few weaknesses in my opinion. Instead, I will give some minor feedback.

- “By considering both intra-episode experiences (information within a single episode) and cross-episode experiences (information across multiple episodes), our method can learn richer meta-features for the environment.” The opposite of intra is inter, not cross. The title already contains 'cross', but consider using this term when explaining (I believe it already occurs once towards then end).

- Consider citing Bhatia et al. (RL^3: Boosting Meta Reinforcement Learning via RL inside RL^2) which also uses transformers and learns state-augmentation features for meta-RL, albeit not through inter-episode data sharing.

- Figure 2 bleeds into the margins.

- It could be clearer which baselines (or other meta-RL methods) this method is compatible with and which are mutually exclusive.

### Questions
“Hypothesis 1: ECET captures more general task features through its ability to capture intra- as well as cross-episodic experiences.” 

I recognize claims about feature generality are difficult to substantiate, and that it is somewhat of a catch-22 to try to deal with these topics experimentally. I appreciate the authors for making an attempt. I am interested in their thoughts regarding essentially more rigorous versions of such experiments.

- Do you have a definition for the generality of a task feature? How does one measure this? 

- You’ve shown that embedding vectors tend to cluster for some tasks. Do you think there are any possible confounders beyond generality of features?

- Moreover, if one were to take a more systematic and focused approach to quantifying the difference between tasks so that embeddings generated from those tasks may be compared to the embedding distances --- similar to what is presented in figure 13 but with some notion of how similar two columns/rows ought to be --- do you suspect they would encounter anything surprising?

Is there anything that makes such an experiment difficult to execute other than initially deciding how to measure difference between tasks? I agree these results seem promising w.r.t. this hypothesis, but there are definitely a few more logical steps to nail down before this can be determined without doubt (which would be an important result in it own right, of course).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new algorithm; Efficient Cross-Episodic Transformers (ECET) for online meta-reinforcement learning. Their method tackles the problem of enabling reinforcement learning agents to perform effectively in previously unseen tasks. In order to achieve that, they take past episodes and use them as in-context information, considering different task variations and single transitions by not only extracting information from within sequences of transitions but also incorporating information across sequences sampled from different episodes; thus, integrating insights from prior meta-RL research. Their main contribution is improving the generalization capabilities and providing more efficient meta training, outperforming previous state-of-the-art methods. They perform an empirical study in the Meta-World and Maniskill Benchmarks to conclude that their extended algorithm captures more general task features and outperforms the state-of-the-art in online meta-RL algorithms in few-shot adaptation to parametric variations of tasks and out-of-distribution tasks. 
Overall, this paper could be a significant algorithmic contribution, with the caveat of some clarifications on the theory and experiments. Given these clarifications in an author's response, I would be willing to increase the score.

### Strengths
For originality, the paper presents a novel method for learning meta-features through efficient cross-episode meta-RL, using a novel transformer architecture that enhances the adaptability of RL agents across diverse sets of tasks. For significance, their approach leverages intra-episode experiences and cross-episode experiences, providing a more comprehensive learning process and integrating ideas from previous meta-RL research. From a perspective of clarity and quality, their learned algorithm is capable of outperforming the previous state-of-the-art and providing more efficient meta-training while significantly improving generalization capabilities. In general, the proposed method enhances the agent’s ability to generalize from limited data supported with sufficient empirical experiments and paves the way for more robust and versatile AI systems.

The paper has some good points to highlight and summarize:
- Improving generalization capabilities and providing efficient meta-training. 
- Outperforming previous state-of-the-art methods by capturing complex, multilevel patterns in the data.
- Integrating multiple ideas from previous meta-RL research.

### Weaknesses
Based on my experience, while I truly appreciate the authors’ effort, I believe that their paper lacks novelty and can be considered as an improvement but not as a real contribution for several reasons. First of all, there is no central contribution beyond improving generalizing capabilities by introducing a new architecture and outperforming previous SOTA–which was supported in the empirical results in figures 4, 5, and 6— still, their method’s generalization to tasks that are completely different from the meta-training set remains limited as their approach is tailored to exploiting similarities as shown in hypothesis 3: ECET outperforms the state-of-the-art online meta-RL in out-of-distribution (OOD) tasks. This leads to Section 1, Related Work, it is still unclear how their method differs from other baselines in solving the same problem, specifically the TrMRL method Melo (2022), which is the closest to the authors’ proposed algorithm. In other words, the authors’ addition and value are still vague compared to previous research tackling the same research question. Having read Melo (2022), I see that their cross-episode experience equals the episodic memory system proposed in the TrMRL method. More discussion on these topics would be helpful.


Minor comments:
1. Page 6: Line 4, ‘ihas’ should be corrected.

### Questions
For the theory, there are a few steps that need clarification and further explanations on novelty. For novelty, it needs to be clarified if their method is being stated as a novel result. It looks like the method has already been shown in "Transformers are Meta-Reinforcement Learners.” There is a statement that “TrMRL is the closest baseline to our proposed method (Melo, 2022). It uses a transformer in the inner loop of the RL2 algorithm. It takes a sequence of the 5 most recent transitions as input to the transformer. We use the implementation provided by the authors.” Is your algorithm 2 somehow an extension? Is your theorem 3 completely new?

In Appendix A.2.3 Procedural Components, you mentioned that “SampleTransitions: We sample the transition sequences of length T from each episode in H. For past episodes, we randomly” You randomly did what?

There is also one concept in the algorithm that I cannot verify. How did you apply the intra-episode and cross-episode simultaneously? More about this would be illuminating

For the experiments, the following should be addressed:
- The central contribution is enhancing the generalizing capabilities. The authors concluded that their method is capable of adjusting to completely unseen tasks that share the same state and action spaces as the training tasks. Despite outperforming state-of-the-art methods in online meta-RL by efficiently compressing cross-episodic knowledge, their method’s generalization to tasks that are completely different from the meta-training set remains limited as it is tailored to exploiting similarities. I would like to see some discussions on this and I think it would be beneficial to demonstrate that empirically.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents an online Meta-RL method. The authors suggested that decomposing the encoder into an intra-episode stage (where each episode is encoded separately) and cross-episode stage (where the vectors from the previous step are encoded into a single representation of the context) should improve performance both in terms of few-shot adaptation and in-distribution and out-of-distribution generalization.
The authors validated their claim on the Meta-World and ManiSkill benchmarks and compared against popular Meta-RL benchmarks.

### Strengths
1. The paper is well written, especially the Method and Experiments sections. The formulation and explanation of the algorithm can be well understood
2. The results shown in the Experiments section look quite promising, including results over the widely used Meta-World benchmark 
3. The authors provided an open-sourced code to reproduce the results

### Weaknesses
1) My main concern regarding this work is the novelty of the proposed method. The overall algorithm is very similar to previous lines of work, especially RL2 and TrMRL with the main difference from TrMRL is the decomposition of the transformer into two stages. For this change to have a profound enough impact on the field I would expect at least one of the following: 

      a) A theoretical/analytical analysis of why this specific architecture should generalize/perform better than others. The authors gave high-level explanations (e.g lines 204-209), but I found these not rigorous enough. For example, there is no sufficient motivation for hypothesis 1 (line 368), regular recurrent architectures should also be able to capture intra and cross episodic experiences, why should we expect ECET do it better? 
      b) A more thorough empirical study showing the benefits of the chosen design, including more baselines, benchmarks, and an ablation study (more on that below)  

2) The positioning of the paper concerning related work is not clear. For example, in lines 52-53/148-149 in the Introduction Section, the authors claim that previous methods used "single transitions or sequences of transitions from the same episode" to encode the context and state that incorporating cross-episodic information is one of the novelties of the proposed method. This claim is false as many previous works (e.g. VariBAD, TrMRL...) encoded transitions from multiple episodes into a single representation. 

3) The empirical study, which is shown in Section 5, is not sufficient to support the claims of the authors (mainly hypothesis 1 and 3):  
    a) More benchmarks including ones from the original papers (e.g. VariBAD, RL2) are missing. It is not clear if the results will hold on benchmarks where sufficient hyperparameter tuning of the other baselines took place

    b) An ablation study is missing, especially over the disentangled transformer architecture

    c) Regarding hypothesis 3 - the authors did not compare to theoretical/empirical line of works in generalization in Meta-RL (e.g [1,2])

### Questions
1. In the title of the paper you suggested the method is "Efficient", but did not mention in what sense (not in the introduction at least). Do you mean in terms of time complexity (as discussed in lines 267-274)? If so, mention it in the introduction and add some results showing latency/FLOPs compared to "standard" (line 268) approaches.
2. In line 211 you mentioned you sample a sequence of $T$ transitions from each episode.\
    a) How do you sample the transitions? Uniform sampling? With replacement?\
    b) What is the chosen value for the different benchmarks? Did you test the effect of this value on the runtime/performance?\
    c) DId you also sample the transitions when running the other baselines? 
3. Why did you choose to add positional encoding to the IET?
4. What are the number of episodes, length of each episode, and $T$ in each benchmark?
5. Did you use the same hyperparameters for all benchmarks? If not, how sensitive is your method to different hyperparameters?
6. How did you choose the hyperparameters for the baselines? 
7. How many seeds did you use for the experiments in Section 5?  
8. In Figure 5 the results of TrMRL don't match the ones in the TrMRL paper. Do you have an explanation for this? Did you run this baseline as done in the original paper (connecting to questions 2c and 6)?  
9. How many learnable parameters does your architecture have compared to the other baselines (especially TrMRL)?  
10. Typo line 273: ihas -> has

### Soundness
2

### Presentation
2

### Contribution
1

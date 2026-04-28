# Mastering Syntax, Unlocking Semantics: A Mathematically Provable Two-stage Learning Process in Transformers

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
Transformers have emerged as a cornerstone across various fields with extensive applications. 
However, the training dynamics of transformers remain relatively underexplored.
In this work, we present a novel perspective on how transformers acquire knowledge during the training dynamics, inspired by the feature learning theory. 
To this end, we conceptualize each token as embodying two types of knowledge: elementary knowledge represented by syntactic information, and specialized knowledge represented by semantic information.
Building on this data structure, we rigorously prove that transformers follow a syntax-then-semantics learning paradigm, i.e., first mastering syntax in the Elementary Stage and then unlocking semantics in the subsequent Specialized Stage.
The results are derived from the training dynamics analysis and finite-time convergence within the in-context learning framework for supervised classification.
To our best knowledge, this is the \textbf{\emph{first}} rigorous result of a two-stage optimization process in transformers from a feature learning perspective. Empirical findings on real-world language datasets support the theoretical results of the two-stage learning process. 
Moreover, the spectral properties of attention weights, derived from our theoretical framework, align with the experimental observations, providing further validation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This theoretical paper examines a scenario where there are two sets of features: "easy-to-learn" features, which are learned quickly, and "hard-to-learn" features, which require more time and effort to acquire. The authors demonstrate, using a simplified transformer model with a specific learning rate schedule resembling typical approaches, that the model first learns easy-to-learn features before moving on to hard-to-learn features. They argue that easy-to-learn features correspond to general syntactic knowledge in language models, while hard-to-learn features relate to semantics, defined as specialized or domain-specific knowledge.  The empirical part is very limited, the focus is on the theory.

### Strengths
This paper presents an impressive theoretical approach to explaining an intriguing empirical observation: that learnng various phenomena often progresses through distinct stages. To my knowledge, there is limited theoretical work that delves into the mechanisms underlying this 'staged' progression, making this paper a valuable contribution to the field. The observation that easy-to-learn features are leveraged early in learning, followed by a shift to harder-to-learn features, is supported here with rigorous analysis (see my 'confusions' below though), supprting the intuition that has lacked formal backing.

### Weaknesses
1. The generative process description for the data is somewhat unclear. Based on the current explanation, it seems that the Bayes optimal classifier might not need to rely on semantic features; syntactic features appear sufficient to solve the task in an asymptotic setup. This would have undermined the notion that x2 captures specialized knowledge; specialized knowledge should provide benefits on a limited set of specific tasks, rather than being redundant to general knowledge. Figure 3 and the reference to Li et al. (2019) suggest that my interpretation is incorrect. E.g., in Li et al there’s a stochastic choice in generating features for each example (would 'easy' or 'hard' for this case)., but it is not what is happening here. This needs to be explained better.

2. I’m unclear on the rationale for assuming a block-diagonal structure (Eq. 2). In realistic settings, one wouldn't typically know which features are hard or easy in advance. This assumption seems to predetermine the separability of the feature spaces, which might not hold in practice and could limit the generalizability of the findings. The block-diagonal structure forces the model to learn independent representations for 'easy' and 'hard' features, potentially missing out on complex interactions that might exist in real-world data.

3. We normally use adaptive gradient methods rather than SGD. Would such a method, which rescales gradient components, affect the findings? For instance, might it amplify updates for weights associated with hard features (i.e., x2)? The analysis should consider the impact of adaptive methods like Adam or AdaGrad, which dynamically adjust learning rates for each parameter based on historical gradients. This could potentially alter the observed learning dynamics and the staged progression.

4. What if t the initial learning phase is skipped and we started annealing immediately? How would it affect learning dynamics? The paper should explore the sensitivity of the results to the learning rate schedule. Specifically, it should investigate what happens if the initial phase with a large learning rate is skipped, and the annealing process begins immediately. This would help determine if the staged learning is an artifact of the specific learning rate schedule or a more fundamental property of the model and data.

5. The decision to link optimization parameters (such as the learning rate in the second stage) to the data generation procedure seems unrealistic. Is the idea that this selection approximates parameters typically chosen through hyperparameter tuning? This paper demonstrates that specific parameters enable the model to acquire hard-to-learn knowledge in the later stage without undermining the easy-to-learn knowledge, but it doesn’t show that this outcome holds across a wide range of parameters or those commonly used in practice. The theoretical analysis relies on a specific relationship between optimization parameters and data generation, which is not typical in practice. It is unclear if the observed staged learning is robust to variations in these parameters or if it is an artifact of this specific setup.

6. I would discourage the authors from using terms semantics and syntax as these seem to be misleading.

More broadly, it is unclear to me if the two stages are results of the explicit choices in defining the generative process and the stage of learning, or would emerge under more broad range of settings.

Overall, to fully grasp the importance of the assumptions, a careful reading of the proofs is necessary, which was challenging for  me and would probably be challenging for conference reviewers in general. Given the paper's length (56 pages!), it seems more appropriate for a journal (e.g., JMLR).

### Questions
I posed questions in the paragraphs describing weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work presents a theoretical proof on the learning process of Transformer models can be split into two stages: a first stage focusing on learning elementary knowledge (or syntax), and a second stage focusing on learning specialized knowledge (or semantics). The theoretical proof is done in a single-layer Transformer with certain simplifications and assumptions. Empirical verification is also done on two datasets: Counterfact and HotpotQA. This work also shows an interesting spectral characteristic of the attention weights as a corollary of the proof.

### Strengths
1. This work provides a rigorous proof of the training dynamics on the single-layer transformer model.
2. Empirical verification is done on two real NLP datasets. The spectral characteristics analysis is interesting and insightful.

### Weaknesses
1. The difference between syntax and semantics in this work is basically one is easier to learn than the other as a feature. Consequently, what this paper proofs is basically Transformer models learn easier features first, and learn more complex features later. While this finding is true according to the analysis done in this paper, this proof does not lead to much new sights about Transformers, syntax/semantics or ICL. Right now, even though the proof is done on Transformers, it really feels like a general conclusion that should be held on a much broader class of models. It might be useful to add a discussion section highlighting what properties of Transformer or ICL are critical for this proof. I would also suggest shifting the focus of this paper away from the syntax/semantics contrast. The syntax/semantics aspect is more suitable to be one of the additional findings in the empirical verification part.
2. The empirical verification part of this work should be more detailed. Right now, there are no quantitative metrics about the syntax or semantics accuracy after each stage. There is also no study focusing on the actual length of the first learning stage even though the theory seems to suggest a certain length of the first learning stage.

### Questions
1. In the analysis, one key difference between the two learning stage is the constant learning rate and the annealing learning rate. Is that crucial to the proof and do you observe the same effects in practice?
2. L2 normalization is hardly used in the actual training of Transformers. How do you view this difference between the proof and the practice?

### Soundness
2

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
5

### Summary
This paper presents an innovative feature-learning-inspired approach that uses the in-context learning framework to acquire knowledge during training dynamics. The authors construct a robust mathematical framework to address the problem first, providing a rigorous and detailed analysis of training error and convergence properties. Additionally, through motivating experiments, they demonstrate a link between their theoretical findings and practical applications in NLP, showcasing the potential of their approach for real-world complex problems.

### Strengths
The paper is well-written, with a thorough review of related work and clear, thought-provoking remarks. The mathematical framework is robust, and the proofs are detailed and precise, enhancing the rigor and readability of the theoretical contributions.

### Weaknesses
While the paper presents a strong foundation, there are issues within the proofs that need further clarification. Specifically, the error bound analysis in Theorem 2 appears to contain a significant error. The derivation from line 2238 to 2243 attempts to establish an upper bound for \(K_{t_1}^1(\overline{W}_{t_1})\). However, the intermediate step where a larger upper bound (the max term) is used introduces an inaccuracy. The inequality \(\max\left(\log(2) - \frac{1}{2} ( \epsilon_{W,1} + \frac{\sqrt{d}\log(d)}{L} \epsilon_W), \log(2) + \frac{1}{2}( \epsilon_{W,1} + \frac{\sqrt{d}\log(d)}{L} \epsilon_W) \right) \le \epsilon_{W,1} + \frac{\sqrt{d}\log(d)}{L} \epsilon_W \) does not hold under the given conditions, especially as \(d\) approaches infinity. This undermines the claim that the upper bound converges to zero, casting doubt on the validity of Theorem 2 and its implications. Without addressing this core issue, the analysis may not be fully reliable.

Additionally, the experimental section lacks sufficient explanation, which would be essential for solidifying the connection between the empirical results and the theoretical framework.

Although the paper primarily focuses on the training perspective, it would benefit from an analysis of pre-trained model properties, such as error behavior, distribution shift, and generalization. This could offer more compelling insights into the applicability of the approach for NLP and related fields.

### Questions
I would appreciate and change the score if you could explain the following points.

**Theoretical Analysis and Proof:**

Your paper presents a robust theoretical framework with well-constructed proofs. However, there are a few points listed below, particularly in Theorem 2, that I found somewhat unclear.

1. ***Error Bound Analysis:*** Could you comment on the error bound for a pre-trained transformer in your framework? Specifically, how does the error behave with varying context (or prompt) lengths for such a model?

2. ***Clarification of “Easy-to-Fit” and “Hard-to-Fit” Components:*** Given the rigorous mathematical nature of your paper, a more formal explanation or intuitive insight into “easy-to-fit” versus “hard-to-fit” components would help clarify the intrinsic differences between the P and Q components. Without this, it’s challenging to grasp the core distinctions between these parts.

3. ***Explanation of Proof Steps in Theorem 2:*** Could you briefly clarify specific steps in the appendix related to Theorem 2? In particular: 
 
   - Lines 2220 to 2222: based on your notation in line 2183 of $\epsilon_W$, and the equation in equation (21), it seems from line 2220 to line 2222, you use an inequality: $\log(Poly(d)) \le \log(d)$, please explain why.

   - Lines 2228 to 2230: with your notation in line 2211 $\epsilon_W=(Poly(d))^{2/3}$, and $L=Poly(d)$, please explain how do you get $$\frac{\sqrt{d} \log(d)}{L} \epsilon_W\le \frac{\sqrt{d}\log{d}}{Poly(d)}$$

   -  Lines 2238 to 2243: in line 2238, is the max value already greater than log(2)? $$\max(\log(1+e^{-x}), \log(1+e^{x}))>log(2),\ \text{where}\ x=\epsilon_{W,1}+\sqrt{d}/L\log(d) \epsilon_W$$ Later you mention the LHS of above inequality less than $\epsilon_{W,1}+\frac{\sqrt{d}\log(d)}{L}\epsilon_W+\frac{1}{\sqrt{\log(d)}}$, the upper bound of $K_{t_1}^1(\overline{W}_{t_1})$. If so, does the upper bound of Theorem 2 align with Theorem 1 on the same constant scale, which cannot converge to zero as the dimension $d$ goes to infinity?



**Experimental Setup:**

Your motivating experiments are thoughtfully designed to link with the theoretical work. However, I have a few questions regarding the details:

1. ***Transformer Architecture:*** You mention that the practical model is based on a GPT-2 architecture. Is this still a one-layer transformer as in your theoretical analysis? If it’s not one layer, could you briefly explain how the one-layer theoretical results extend to this more complex structure? Additionally, could you specify the dimensionality $d$ used in the experiments?

2. ***Syntactic and Semantic Evaluation:*** You state that “all predictions meet syntactic requirements.” Could you clarify how this was verified? More specifically, what distinguishes syntactic from semantic evaluation in your setup? Considering the large-scale nature of your dataset, was there any metric or human evaluation to support this claim? Did you consider including plots showing accuracy over time? This could provide additional insight into the learning process.

3. ***Transition Point Analysis (T=5):*** The transition at T=5 is intriguing and seems tightly related to your theoretical findings. Would it be possible to compute an approximation of the theoretical bound (e.g., $t_1$) and compare it with this empirically observed threshold? This could help clarify the connection between your experimental and theoretical results.

4. ***Prompt Construction Details:*** 

   - Is prompt length fixed during training?
   - Could you elaborate on how the prompts are constructed in practice? Are they derived from a single dataset, such as the Counteract dataset?
   - In Figure 5, do all questions use the same prompts. Besides, are these prompts changed during training?

### Soundness
2

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
2

### Summary
This paper attempts to show that transformer language models learn in two stages: in the first, they learn syntax, and in the second, semantics. The authors justify this via mathematical proof. They study simple, one-layer transformer models, trained on data composed of two components—P and Q—where the former is easy and the latter difficult to learn. They show that given a limited number of timesteps, the model will only able to learn P at first; Q will be learned later. They analogize P to syntax, and Q to semantics. The authors then perform experiments on factual knowledge datasets to show that models do indeed learn syntax (word categories) first, but only acquire semantics (factual knowledge) later.

### Strengths
This paper engages in a seemingly rigorous theoretical analysis of learning trajectories in transformer language models, and attempts to connect this theoretical analysis to real trends in language models' learning trajectories. This is valuable, given that we still have few theoretical insights about learning in transformers that usefully transfer to real-world models.

### Weaknesses
- **Weak connection between proofs and core claims**: I do not claim to understand the proofs very well, but my understanding is that the proofs attempt to characterize the learning trajectory of a transformer-based model trained on data with an easy-to-fit component P and hard-to-fit component Q. This model (which is really composed of two sub-models working in parallel) is able to learn the P component quickly, while the Q component is learned later. This is all fine, but it is then claimed (186-188) that P aligns with the syntactic information in the corpus (easy to learn) and that Q aligns with the semantic information in the corpus (hard to learn). This assumption is unjustified: how do you know that syntax and semantics specifically should align with P and Q? It may well be that models learn in two stages (if their data are made up of components from two different distributions, one easy and one hard to learn), but how do you know that these two distributions of disparate difficulty exist in reality, or that syntax and semantics correspond to the easy/hard distributions? This assumption is really the crux of the paper, but goes unjustified.
- **Unclear what this paper believes syntax / semantics to be**: This paper claims to show that the models first learn syntactic and then semantic information, but what exactly syntactic and semantic information (or, alternatively "elementary" and "specialized" knowledge) are goes undiscussed. 
    - **Operationalization of syntactic ability**: The authors seem to operationalize models' syntactic ability as "the model predicts precisely the right category we expect", but this operationalization is flawed. Consider one example given in the paper, "The mother tongue of Danielle Darrieux is"; based on the fact that the model outputs "the" rather than "French" or "Dutch", they infer that it lacks syntactic abilities. However, such an inference is not licensed: "the" is a perfectly valid start to many continuations. For example, the sentence could continue like "The mother tongue of Danielle Darrieux is the 6th most spoken language in the world". This sentence is syntactically (and semantically) valid, even though the next token is not a language. If the authors really want to make a claim like this, they should measure the probability assigned to tokens that cannot plausibly begin a syntactically valid completion. Moreover, prior work in the field has already come up with ways of measuring models' syntactic knowledge; see syntax benchmarks like [SyntaxGym](https://aclanthology.org/2020.acl-demos.10/) and [BLiMP](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00321/96452/BLiMP-The-Benchmark-of-Linguistic-Minimal-Pairs), among many others.
    - **Syntax vs. semantics, or something else?**:  This paper only considers syntax and semantics as the two components of a given token, but in its empirical evaluations (if we take them to be valid), we only see that one specific type of syntactic knowledge (next-token category constraints) emerges prior to a specific type of "semantic" knowledge (factual / world knowledge). But this doesn't license a claim about syntax and semantics more broadly; there are many different categorizations of these datapoints that could separate these two. For one, many would consider factual/world knowledge to be something distinct from other types of semantic knowledge; see e.g. [the formal-functional distinction](https://arxiv.org/abs/2301.06627). In general, to make this broad syntax vs. semantics claim, you'd need to test more types of syntactic vs. semantic abilities.
    - **No engagement with prior work from computational linguistics studying the same question**: The (computational) linguistics literature has tackled the very question that this paper purports to answer, with similar results. [This](https://direct.mit.edu/coli/article/50/1/293/118131/Language-Model-Behavior-A-Comprehensive-Survey) is a nice summary; Section 3.3, "Language Models Learn Syntactic Rules Early in Pre-training" tackles this very question. [Other work](https://proceedings.mlr.press/v235/belrose24a.html) takes a more theoretical view on these issues.
- **Little empirical evidence for claims**: The core claim of this paper, that models learn syntactic information first and semantic information second, is a plainly empirical one. The easiest thing to do would be to simply come up with ways to measure models' syntactic and semantic knowledge at each point in training, and then plot how these abilities change over time. This would involve a variety of tasks / metrics for syntax and semantics, and careful thought about which tasks/metrics make sense. This paper only measures LM loss, which doesn't tell us anything about syntactic or semantic abilities, trains on one very limited dataset, and performs limited qualitative analysis of model abilities to make claims about syntactic / semantic abilities. This is insufficient.

### Questions
- Why do you claim (186-188) "For each individual input sample $x_i^n$ in prompt $P_n$, it is composed of two types of components: $P$ component represents easy-to-fit features, aligning with syntactic information in the corpus, and $Q$ component represents hard-to-fit features, aligning with semantic information in the corpus."? Particularly, what justifies the alignment between $P$ and $Q$ with syntax and semantics specifically? Can you prove that syntactic and semantic features (however you want to define them) are distributed in such a way that aligns with your definitions of $P$ and $Q$?
- Have you considered alternative hypotheses regarding what the easy/hard-to-learn components of examples are, besides syntax and semantics? It is important to rule these out before concluding that the model is learning syntax and semantics, specifically, in that order.
- How would you position your work relative to prior work that also suggests, using stronger empirical evaluations, that models learn syntax early on? As I see it, the "models learn syntax first" angle isn't new, and this work is better positioned as an explanation for why they do so. But this would require justifying the claim that syntax and semantics actually fulfill the conditions behind P and Q in your proofs.
- You cite (Vaswani, 2017) for the transformer model, but shouldn't this be (Vaswani et al., 2017)?
- How do you train the model using which Figure 5 was made? You say that it uses the GPT-2 architecture (this should be cited) and the counterfact dataset, but do not say anything about how the model is actually trained. I guess that you do train it, though, since you have per-epoch results, and these are not typically available for GPT-2 models

### Soundness
2

### Presentation
1

### Contribution
2

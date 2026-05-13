# Stochastic Safe Action Model Learning

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Hand-crafting models of interactive domains is challenging, especially when the dynamics of the domain are stochastic. Therefore, it's useful to be able to automatically learn such models instead. In this work, we propose an algorithm to learn stochastic planning models where the distribution over the sets of effects for each action has a small support, but the sets may set values to an arbitrary number of state attributes (a.k.a. fluents). This class captures the benchmark domains used in stochastic planning, in contrast to the prior work that assumed independence of the effects on individual fluents. Our algorithm has polynomial time and sample complexity when the size of the support is bounded by a constant. Importantly, our learning is safe in that we learn offline from example trajectories and we guarantee that actions are only permitted in states where our model of the dynamics is guaranteed to be accurate. Moreover, we guarantee approximate completeness of the model, in the sense that if the examples are achieving goals from some distribution, then with high probability there will exist plans in our learned model that achieve goals from the same distribution.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce the problem of learning an action model in a stochastic environment of a PPDDL-type planning problem. Unlike the more standard MDP formulations of RL, here the state formulation consists of a set of 'fluents' which take boolean values, and the action model describes which 'effects' can follow after taking certain actions in given 'preconditions'. Compared to previous research in learning action models, in their formulation, the stochasticity of the effects that follow certain actions can be more general. The authors then show that, under these assumptions of the stochasticity, following closely the methodology of Juba & Stern (2022), they can learn an action model using tensor decomposition. They analyze the method and show that it can be used to achieve a particular notion of 'safety' and 'approximate completeness'.

### Strengths
* The authors come up with an algorithm to learn the action model and they can then guarantee "safeness" and the "approximate completeness" of the approach.

### Weaknesses
 * The paper is unnecessarily dense at times, please consider the use of examples and captions to illustrate the main ideas, especially to new audiences.

* No experiments were performed to show the benefits of the introduced algorithm.

* It is not clear at times what the contribution is compared to Juba & Stern 2022 paper. It seems that all the proof techniques rely on that previous paper. In particular note the last sentence of the paper: "The only difference
between the proofs of these theorems and Juba & Stern (2022) is that we change the dependence on
the number of fluents |F | to the dependence on the number of effects |F |O(log r)."

* It is not clear if the stochastic model considered reflects real-world problems accurately. In particular it would be nice for the authors to give an example of a real-world problem that is captured by the particular stochastic model.


### Questions
* I'm not sure that ICLR is a good conference to submit this type of paper, it seems rather to belong to the more standard AI/planning-focused conferences.

* Is the Algorithm1 the authors' contribution, or is it also based on the Juba & Stern (2022) paper?

* It's not clear if the proposed algorithm would actually run on a computer. Have the authors tried to do so? Are there any complications?

* Minor comment: Two 'the's in the first sentence.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach based on tensor decomposition for learning stochastic action models for symbolic planning. The problem is really relevant and important, given the amount of work going on in different fields model learning like learning abstractions or learning symbolic models. 

The paper theoretically shows that the learned model is safe (or conservative) in terms of the action only applicable in a state if and only if it is permissible in the true model (but given that they learn a conservative model from a set of only positive trajectories this is not surprising).

### Strengths
- The problem is relevant, important and unsolved. 

- The approach is theoretically sound and strong.

### Weaknesses
As I mentioned, the problem is really interesting. However, the paper is equally inaccessible to a reader. The low novelty score given is because even though the paper may have novel contributions, these are not understandable for the reader.

- There are many unsubstantiated claims in the paper. Theorems and Lemmas in the paper have almost no explanations.  While I support having theoretical results in the paper, they should be complete. The readers should not be left reading some previous work to understand even the basic premise of the theoretical results of the paper (in this case [Juba and Stern, 2022]) as the paper  does not have proofs for theorems and lemmas (Theorem under 2.2, Lemma 1, Theorem 1, and Theorem 2) or defer proofs to previous work. Specifically, the reliance on external proofs makes it difficult to assess the validity and scope of the presented approach. The core theorems lack sufficient context and derivation, making it hard to grasp their implications for the proposed method. The paper should include at least a sketch of the proofs to make it self-contained.

- The notations are non-intuitive. For, e.g., the preliminaries section is meant to be make the rest of the paper understandable. However, they have unproven lemmas and theorems as well as equations with undefined symbols (superscript cross d ). In Theorem under Sec 2.2, what are a_k,b_k and c_k? The lack of clear definitions for symbols and the use of non-standard notation makes the paper unnecessarily difficult to follow. For example, the superscript cross d, which denotes repeated outer products, is not a common notation and requires additional effort to understand. The variables a_k, b_k, and c_k in Theorem under Sec 2.2 are not defined, leaving the reader to guess their meaning and role in the theorem.

- The paper attempts to solve a very intuitive problem with a very non-intuitive approach. The most intuitive thing  would have been to include a running example that makes it really easy for the readers to follow. The absence of a concrete example makes it hard to connect the theoretical framework to practical scenarios. A running example would help readers understand how the tensor decomposition approach is applied to a specific planning problem and how the learned model is used in practice. This would greatly improve the paper's accessibility.

- The next big problem with the paper is a lack of empirical evaluation. Without an empirical evaluation, there is no practical explanation to if the approach is feasible for learning real world domain models. There are plenty of PPDDL domains available to learn. The lack of empirical validation is a major weakness. Without experiments on standard PPDDL domains, it is impossible to assess the practical feasibility and performance of the proposed method. The paper should include experiments that demonstrate the approach's effectiveness in learning stochastic action models for realistic planning problems.

- The paper presents a similar functional approach as [Juba and Stern 2022] with near similar theoretical guarantees. It is not clear from the paper what is the motivation behind a different approach without any significant improvements.

### Questions
Please refer to the weaknesses highlighted in the previous section. 

The most important question is: 

- Would it be possible to provide a running example in the **main paper** to help the reader understand the paper as it is currently extremely difficult to understand. 
- Why was not empirical evaluation provided and would it be possible to provide empirical evaluation on standard PPDDL domains?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The focus of the paper is on model learning in stochastic PPDDL. Here, the overarching goal is to learn a model of the domain from trajectories. The model here specifically refers to a set of preconditions and effects of taking a particular action. The trajectories are executed with a set of policies in a domain with discrete states. Each state is characterized by a set of boolean fluents. The goal of the paper is to learn a stochastic model where the probability of each effect is extracted from the data. Previous work in this setting provides safety and approximate completeness guarantees by assuming that each effect’s action on each fluent is an independent random variable. This assumption eases the analysis. In contrast, this paper attacks a more challenging case using tools from tensor algebra. By performing a low-rank decomposition of the transition probability tensor using the method of moments, the authors are able to extract a model that is shown to satisfy safety and approximate-completeness criteria.

### Strengths
1) The contribution is novel, clear and significant. The idea of using tensor decompositions for PDDL has not been explored.

2) The method is theoretically sound.

### Weaknesses
1) The presentation and clarity needs significant improvement. As a standalone contribution, the paper should be more rigorous in terms of presentation and lacks a diligent writing style. A more scrupulous approach to explaining all the math will help presenting the paper (with the appendix).

2) It would be nice if half a page of the paper is delegated to demonstration of the method on one dataset.

3) More preliminaries and related work on the method of moments algorithm applicable to tensors is encouraged. The related work section only attributes around five papers.

4) I have some questions surrounding Lemma 1. I believe $|S|$ denotes the number of distinct elements in $S$. Is there any reason why the elements of $V$ would not be distinct? Are they necessary to be all distinct? Is all that is sufficient is that $rank(V)=r$ where $r$ satisfies Lemma 1? In that case, $rank(V)+2 rank(V^{\otimes k}) \geq 3r$? This part is unclear to the reader.

5) More illustrations similar to section 3.2 equations (2) and (3) will help improve clarity.

6) Section 4.1 is not explained properly and there are some cyclical arguments. Given that these are mainly a variation of Jennrich’s algorithm, a preliminaries section can help ease the exposition.

7) There is no explanation of what is a “generic” tensor? Is the qualification in Kruskal’s theorem?

### Questions
1) I have some questions surrounding Lemma 1. I believe $|S|$ denotes the number of distinct elements in $S$. Is there any reason why the elements of $V$ would not be distinct? Are they necessary to be all distinct? Is all that is sufficient is that $rank(V)=r$ where $r$ satisfies Lemma 1? In that case, $rank(V)+2 rank(V^{\otimes k}) \geq 3r$? This part is unclear to the reader.

2) More illustrations similar to section 3.2 equations (2) and (3) will help improve clarity.

3) Section 4.1 is not explained properly and there are some cyclical arguments. Given that these are mainly a variation of Jennrich’s algorithm, a preliminaries section can help ease the exposition.

4) There is no explanation of what is a “generic” tensor? Is the qualification in Kruskal’s theorem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study investigates a very interesting topic and introduces an algorithm for learning stochastic planning models, specifically targeting domains with dynamics that are challenging to model manually. The proposed approach could efficiently learn from example trajectories, ensuring accurate and safe action modeling.

### Strengths
1. The research topic is interesting.
2. The theoretical analysis sounds good.

### Weaknesses
1. The manuscript requires substantial improvements in writing quality, with an emphasis on a more coherent logical structure.
2. The paper contains numerous grammatical errors, even within the abstract. For instance, on page 1, there's a repeated "the", "model" in the abstract should be "models", "at some point" should be "at some points", and "some other condition is satisfied" should be "some other conditions are satisfied".
3. Ensure that abbreviations are expanded upon their first use, for example, "PPDDL".
4. Once an abbreviation has been defined, it's redundant to reintroduce it; consider the case with "Stochastic Safe Action Model (SAM)".
5. The experimental section is lacking, making it challenging to evaluate the method's effectiveness. Specifically, there is no clear description of the experimental setup, the specific domains used, or the baselines that the proposed method is compared against. The absence of quantitative results and statistical significance tests makes it difficult to assess the practical value of the proposed approach.

### Questions
1. Could you clarify the meaning of "IPC probabilistic tracks"?
2. Is there a correlation between the level of stochasticity and model performance?
3. What is the relationship between effect probabilities and sample complexity?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

# When Selection meets Intervention: Additional Complexities in Causal Discovery

- Decision: Accept
- Scores: 8, 8, 8, 8, 8

## Abstract
We address the common yet often-overlooked selection bias in interventional studies, where subjects are selectively enrolled into experiments. For instance, participants in a drug trial are usually patients of the relevant disease; A/B tests on mobile applications target existing users only, and gene perturbation studies typically focus on specific cell types, such as cancer cells. Ignoring this bias leads to incorrect causal discovery results. Even when recognized, the existing paradigm for interventional causal discovery still fails to address it. This is because subtle differences in _when_ and _where_ interventions happen can lead to significantly different statistical patterns. We capture this dynamic by introducing a graphical model that explicitly accounts for both the observed world (where interventions are applied) and the counterfactual world (where selection occurs while interventions have not been applied). We characterize the Markov property of the model, and propose a provably sound algorithm to identify causal relations as well as selection mechanisms up to the equivalence class, from data with soft interventions and unknown targets. Through synthetic and real-world experiments, we demonstrate that our algorithm effectively identifies true causal relations despite the presence of selection bias.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work shows that current theory for dealing with interventional causal discovery is insufficient under selection bias, as there are cases where the selection mechanism takes place before the intervention. The authors then propose a twin graph framework where the selection happens before the intervention and then define a Markov property on this twin graph that implies certain independences in distributions when conditioned on the selection mechanism. The authors then propose a method that constructs the graph based on the Markov property up to an equivalence class.

### Strengths
- The authors have found an interesting flaw in previous methods in the presence of selection bias
- The paper is well motivated with clear examples. Some examples can be made clearer (see below)

### Weaknesses
Some bits of the exposition are unclear.

- In example 2: This will be much more convincing if there is a numerical example that actually shows this (like example 1). Otherwise, it's not obvious to me why selection might imply that $X_1, X_3$ are dependent when conditioning on $X_2$.
- In section 3.2: It is claimed that interventional distributions are not Markovian due to the original dag due to $X_1$ not being independent of $X_3$ when $X_2$ is conditioned on. The open path here goes through $X_2^*$. However, in example 4 it is claimed that conditioning on $X_2$ automatically conditional on $X_2^*$, This seems contradictory to the previous statement, what am I missing here?
- Thm 1: If this is contrasted directly with the regular Markov property in DAGs, it will help clear up what the extra condition here is. Reading this section, the extra condition has not been motivated with respect to the examples shown. For example, how does this theorem differentiate DAGs $\mathcal{G}$ and $\mathcal{H}$.
- I don't really understand how Lemma 1 "misses key distributional information", could this be made more explicit?
- L291: Why does the twin graph have fewer degrees of freedom with the invariance constraint? And why does it lead to CIs not implied by d-separations? The claim in L293 is also not clear at all to me.
- Section 3.3: Intuitions behind the lemmas and why they are needed would greatly help here. Right now they are hardly motivated and tough to understand given the dense notation.
- Algorithm 1 step 2: how is this done? What method is used to test if the conditional distributions are the same or not?

### Questions
- In example 2: This will be much more convincing if there is a numerical example that actually shows this (like example 1). Otherwise, it's not obvious to me why selection might imply that $X_1, X_3$ are dependent when conditioning on $X_2$.
- In section 3.2: It is claimed that interventional distributions are not Markovian due to the original dag due to $X_1$ not being independent of $X_3$ when $X_2$ is conditioned on. The open path here goes through $X_2^*$. However, in example 4 it is claimed that conditioning on $X_2$ automatically conditional on $X_2^*$, This seems contradictory to the previous statement, what am I missing here?
- Thm 1: If this is contrasted directly with the regular Markov property in DAGs, it will help clear up what the extra condition here is. Reading this section, the extra condition has not been motivated with respect to the examples shown. For example, how does this theorem differentiate DAGs $\mathcal{G}$ and $\mathcal{H}$.
- I don't really understand how Lemma 1 "misses key distributional information", could this be made more explicit?
- L291: Why does the twin graph have fewer degrees of freedom with the invariance constraint? And why does it lead to CIs not implied by d-separations? The claim in L293 is also not clear at all to me.
- Section 3.3: Intuitions behind the lemmas and why they are needed would greatly help here. Right now they are hardly motivated and tough to understand given the dense notation.
- Algorithm 1 step 2: how is this done? What method is used to test if the conditional distributions are the same or not?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the issue of selection bias in interventional causal discovery, highlighting how existing methods fall short when subjects are selectively enrolled in experiments. To address this, the authors introduce a new graphical representation called "interventional twin graph" that explicitly represents both the observed world (where interventions are applied) and the counterfactual world (where selection occurs). They characterize the Markov properties of the proposed graphical model and develop an algorithm built upon FCI based on the proposed graphical model and Markov properties, named CDIS (Causal Discovery from Interventional data under potential Selection bias). The authors prove the soundness of CDIS. Experiments conducted under selection bias conditions demonstrate that CDIS outperforms baselines on synthetic datasets and uncovers novel causal relationships in real-world applications.

### Strengths
1. The selection bias in interventional experiments is an under-explored but crucial issue in causal discovery, and the authors use two clear examples to illustrate why this problem matters and why the existing methods and simply augmenting DAG fail.

2. The authors provide a solid theoretical foundation in this paper by (1) rigorously defining the interventional twin graph and characterizing its Markov properties and (2) proving the soundness of the proposed algorithm.

3. Synthetic experiments show that the proposed method outperforms baselines in handling selection bias and remains robust as the number of variables increases. It also uncovers novel causal relationships in real-world applications.

### Weaknesses
1. While the introduction of the interventional twin graph and its Markov properties is rigorous, it may be challenging for readers to grasp at first glance due to its complexity. Providing a high-level explanation to offer an intuitive understanding would greatly benefit readers. Specifically, the paper could benefit from a more detailed explanation of how the d-separation criteria are adapted to the twin graph, and how this differs from standard DAGs. The current explanation is quite dense and assumes a strong familiarity with graphical models.

2. The interventional twin graph is more complex than a simple DAG and involves additional nodes. It would be helpful if the authors discussed the computational cost of the proposed model compared to the simpler DAG, including an analysis of the algorithm's computational complexity under the new graphical model. A more detailed analysis of the number of conditional independence tests required, and how this scales with the number of variables and interventions, would be valuable. It is not clear if the additional complexity of the twin graph leads to a significant increase in computational burden.

3. The authors did not address the identifiability guarantees of the proposed method. It would be useful to know if the method can reliably identify the selection variables and under what conditions the true interventional twin graph can be identified. Specifically, are there conditions under which the selection mechanism is unidentifiable, and how does this impact the causal discovery process? A discussion of the limitations of the method in terms of identifiability would be beneficial.

4. Minor typos:
    * Line 48: "We show that existing existing graphical representation paradigms" --> "We show that existing graphical representation paradigms"
    * At the end of line 169: "models a completely different scenario" needs to be revised

### Questions
1. Please refer to the questions mentioned in Weaknesses.

2. I think theoretically the proposed framework (the proposed graphical model + algorithm) should be able to handle interventions without selection bias, but how does the proposed algorithm perform empirically compared to existing methods in scenarios without selection bias?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the limitations of current graphical models and causal discovery methods in handling pre-intervention selection bias in interventional causal discovery. To overcome these limitations, the authors propose a novel twin graph model that effectively captures both the observed world and the counterfactual world where selection occurs. The paper establishes the Markov properties of this new model and introduces a provably sound algorithm for identifying causal relationships. The effectiveness of this approach is demonstrated through synthetic and real-world experiments.

### Strengths
1. The problem of selection bias is important yet often overlooked in existing interventional causal discovery. The setting is general.
2. This paper is technically sound, with clear formulation of the causal DAG and Markov properties. 
3. The illustrative examples enhance the paper's clarity, helping readers better understand the concepts.

### Weaknesses
More comprehensive results and explanations of the empirical studies would be beneficial to support the effectiveness of the proposed algorithm. For example:
1. For the simulation, can you report the proportion of true causal edges estimated as directed edges by the algorithm? Additionally, a comparison of the output graphs with the ground truth would illustrate how the new algorithm perform differently from other methods under selection bias. Specifically, reporting precision and recall of edge direction would be more informative than just overall graph structure. It is also unclear how the simulation parameters affect the performance. For example, how does the number of samples, the sparsity of the graph, or the strength of selection bias affect the accuracy of the estimated causal graph?
2. For the gene application, can you provide more comprehensive analysis of the result? It is not clear what specific regulatory relationships are being identified and how these relationships are validated against existing biological knowledge. A more detailed discussion of the biological implications of the findings is needed. Also, the choice of genes and the specific experimental setup of the single-cell perturbation data should be justified.
3. For the education dataset, can you explain why the pre-intervention selection bias is a potential issue? Highlighting and interpreting key information of the resulting graphs would be helpful, as the current graph and variable names are difficult to follow. The description of the variables and their relationships is too vague. The specific mechanisms through which selection bias might arise in this context need to be explained more clearly, and the implications of this bias on the causal conclusions should be discussed.

Minor comments about clarity:
- The notation in this setting is dense and improvements of readability can be helpful for readers less familiar with the area. For example, "CI" in line 93 and different types of arrows in Example 7 can be clarified before their first appearance. It would also be helpful to provide a table summarizing all the notations used in the paper.
- Typos: line 48 "existing", line 295 "false".

### Questions
1. What are the main challenges that affect the precision and completeness of the algorithm? How sensitive is it to the unmeasured confounders?
2. If selection bias is detected through diagnostics, how can this information be leveraged to help causal discovery?
3. Any data points on the computational cost of the algorithm?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper considers the problem of interventional causal discovery in the context of selection bias. The paper first explains why simply augmenting the causal DAGs with a selection variable is insufficient. The paper then goes on to introduce the concept of a twin graph, in which every node is replicated in a counterfactual/"basal" world, and there is a defined set of rules by which the relationships of the basal world are constructed. Based on this construction, the paper goes on to define the set of d-separations that are implied by this model and establish the graphical criteria for Markov equivalence. The paper provides an algorithm to recover the Markov equivalence class and evaluates it on both simulated and real-world data.

### Strengths
The paper clearly lays out the problem of selection bias in causal discovery and why certain natural approaches to the problem are not sufficient. The paper also puts forward a very general solution to the problem and considers its consequences. Overall the paper is well-written, despite being notation-heavy.

### Weaknesses
One thing that was unclear to me is how complete is the paper's characterization of Markov equivalence classes in the given model. I would think that the Markov equivalence class would encode all DAGs with the same conditional independence structure (i.e. the right-hand side of the implications in Theorem 1). However, the equivalence structure is defined with respect to the left-hand side of the implications in Theorem 1. This would seem to imply that the equivalency classes are not as fine-grained as they potentially could be.

The algorithm provided also suffers from this issue, in that the authors point out that it may not be complete. It is not clear to me how useful it is to have a causal discovery algorithm that is sound but not complete. The trivial algorithm that says there are no causal relationships is sound but not useful.

The simulation study not reporting any information on completeness is disheartening. While I understand that the paper does not contain any guarantees on completeness, in the simulations there is access to the ground truth. So it is hard to see how there is no way to evaluate the ability to discover some fraction of those relationships.

At a higher level, I'm not sure how much of the framing of the paper is specific to the selection problem. It seems like the approach of the paper is tackling the more general problem of causal discovery with unobserved latent variables. If that is not the case, then the paper should explain how their methods do not generalize to the latent variable setting.

### Questions
Can you think of any ways in which you could evaluate the completeness of your proposed algorithm in the simulations? In a causal discovery paper, we should be concerned with making true discoveries, not just avoiding false discoveries.

Does the paper's approach generalize to arbitrary latent variables?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the important but overlooked problem of selection bias in interventional causal discovery, where subjects are selectively enrolled in experiments (e.g., drug trials focusing on patients with specific conditions). The authors show that existing methods for interventional causal discovery fail to properly handle selection bias, as subtle differences in when and where interventions occur can lead to inconsistent conditional indepenence relations. To address this, they introduce a novel graphical model called the "interventional twin graph" that explicitly accounts for both the observed world (where interventions are applied) and the counterfactual world (where selection occurs before interventions), along with characterizing its Markov properties and equivalence classes. They develop a provably sound algorithm called CDIS (Causal Discovery from Interventional data under potential Selection bias) that can identify causal relations and selection mechanisms from data with soft interventions and unknown targets. Through experiments on both synthetic data and real-world applications in biology and education, they demonstrate that their method achieves higher precision in identifying true causal relations compared to existing approaches when selection bias is present.

### Strengths
- This paper studies a relevant and interesting problem - both mathematically and philosophically. It considers the question: "What does selection bias actually mean" and proposes a sound answer and the necessary mathematical framework to deal with such situations.
- Based on the framework to treat selection bias, a sound and complete causal discovery algorithm is proposed.
- The method is evaluated not only on synthetic data, but on real-world examples as well. This provides some confidence that it may be useful in practical applications.

### Weaknesses
The biggest weakness I see is the presentation of the paper. The first two sections are dense, but give a good introduction and motivation to the problem, based on good illustrations in Examples 1 and 2.

However, Section 3 is the most painful piece of text I have read in a while. It relies mostly on mathematical notation to bring across the main points and lacks the contextualization in prose. I appreciate that examples are given in Section 3, but even those are a bit cryptic and fail to provide an accessible intuitive understanding. I suppose there are three main reasons for this: (1) Writing about complex SCMs is inherently difficult and a certain level of formalism is necessary - not much you can do here. (2) The amount of content in the main paper, given the page limit might a bit too much. Some of the more technical parts could be relegated to the appendix and exchanged for more contextualization. (3) The text could consider the reader's state of mind more. Some examples:

- L211f: introducing the functions $f^*$ uses the mathematical symbols for the corresponding variables in the counterfactual basal world to introduce them, but does not use the word "counterfactual". That means as a reader, I either have it in working memory, or I have to go back to the definition and jump back again to the sentence to parse it.
- As far as I can tell, abbreviations like "CI" and "MAG" aren't defined, or used before they are defined, e.g. "PAG".

Such presentation choices add unnecessary mental effort for understanding, and I would think twice if I'd go back to this paper and build on it for future work - not because it's wrong, but because of the mental effort to access the information.

### Questions
-

### Soundness
3

### Presentation
2

### Contribution
3

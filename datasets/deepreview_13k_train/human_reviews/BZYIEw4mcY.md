# Efficient and Trustworthy Causal Discovery with Latent Variables and Complex Relations

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Most traditional causal discovery methods assume that all task-relevant variables are observed, an assumption often violated in practice. Although some recent works allow the presence of latent variables, they typically assume the absence of certain special causal relations to ensure a degree of simplicity, which might also be invalid in real-world scenarios. This paper tackles a challenging and important setting where latent and observed variables are interconnected through complex causal relations. Under an assumption ensuring that latent variables leave adequate footprints in observed variables, we develop a series of novel theoretical results, leading to an efficient causal discovery algorithm which is the first one capable of handling the setting with both latent variables and complex relations within polynomial time. Our algorithm first sequentially identifies latent variables from leaves to roots and then sequentially infers causal relations from roots to leaves. Moreover, we prove trustworthiness of our algorithm, meaning that when the assumption is invalid, it can raise an error rather than draw an incorrect causal conclusion, thus preventing potential damage to downstream tasks. We demonstrate the efficacy of our algorithm through experiments. Our work significantly enhances efficiency and reliability of causal discovery in complex systems. Our source code is publicly available via this anonymous link: https://anonymous.4open.science/r/Fveds1C055gvGWsdvs345

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is concerned with learning the structure of a graphical model that may contain latent variables. In contrast to some prior art which learns an equivalence class but does not explicitly represent latent variables, this procedure aims to both identify and model the relationships with latent variables. The author employ an additive noise assumption, and provide a simple and intuitive algorithm for discovering the latent variables via tree construction. Under assumptions on the generative structure and som restrictions on the purity of the children, theoretical results are provided which give nice recovery guarantees and are in general quite complete. A small experimental evaluation is provided as well.

### Strengths
Overall, I think this paper approaches a challenging problem and provides a nice and elegant solution. The authors do a nice job of making the necessary assumption clear and carefully presenting their results. Though I have some reservations (see below), overall I consider the technical quality of this work to be quite good. Further, the problem it addresses in loosening the structural assumptions required for provable recovery. This is especially important, in my view, since these structural assumptions are unverifiable and can have an arbitrarily bad impact on the learnt structure under violations of those assumptionsl.

### Weaknesses
I found the writing in the introduction to be very hard to parse, in particular the task definition. The authors are focused on the problem of learning the structure of graph including latent variables under additive noise constraints. The description of the work in the introduction makes these points hard to follow, it also isn't immediately clear from the initial description the delineation between this and FCI and learning of other structures such as ADMGs, which allow for the presence of latent variables without explicitly representing them. It would be very useful to more clearly describe the problem. 

Most of the paper reads as a step by step walk through of the proof techniques. While this is interesting and useful, it limits the potential audience for the paper, and in many areas, obscures some of the underlying machinery. In my view, much of this should be moved to the supplement. For example, there's no central place in the text which walks through the algorithm as a whole, rather it is strewn out across the paper in analysis steps. 

Many of the proofs in the supplement lack the necessary text to provide sufficient context and intuition for the result. For example, it was not immediately clear to me why proposition 1 in App.C.2.1 implied the statement given in the remark of the main text until working it through. The results should be presented with sufficient detail such that they are reasonably easy to ingest and contextualize within the context of the paper. 

Experimental evidence is small and limited to very simple settings.

### Questions
Please see weaknesses above.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors consider the problem of causal discovery in latent variable LiNGAM models under less restrictive graphical assumptions (described in Assumption 1). Specifically, they allow for some observed variables to be connected to each other and some latent variables to be children of observed variables. They propose a two-stage recovery algorithm that primarily relies on the properties of pseudo-residuals in linear non-Gaussian models. Finally, they consider the case where the graphical assumptions are violated and evaluate the performance of the algorithm through simulations.

### Strengths
The authors provide a detailed theoretical analysis of the proposed algorithm, along with illustrative examples. They also include detailed comparisons of their assumptions and conditions with those of existing work.

### Weaknesses
The main weakness lies in the presentation of the results. Some definitions and concepts are not sufficiently motivated or explained (see Q1 and Q2 below), making certain technical details difficult to understand. Additionally, it would be helpful to include more detailed descriptions of the assumptions and theorems. For instance, in Algorithm 1, Theorem 2 appears to be used solely for partitioning $\mathbb{S}$ into $\mathbb{S}_1$, $\mathbb{S}_2$ and $\mathbb{S}_3$, rather than adding new IPs to $\mathbb{S}$. It would be helpful if this kind of explanation (or a very sketched version of Alg 1 & 2) is provided.

Specifically, the definition of neighbor is unclear. The examples on line 179 rely on the fact that $\text{Ne}^{\mathcal{H}_2}(O_1)\setminus{O_3}=\emptyset$. This indicates that $\text{Ne}^{\mathcal{H}_2}(O_1)$ does not correspond to the sibling set (which is $L_1$) nor the neighbor set in the undirected graph (which is $(O_2, O_3, O_4, O_5)$). Furthermore, the role of the augmented nodes ($O'$, $O''$) in the identification results and algorithms is not clear. My understanding is that they are only used in the algorithm, where the algorithm duplicates each observed variable with two extra copies and add non-Gaussian noises to them. It is not clear how these augmented nodes contribute to the theoretical results.

Finally, the paper lacks a clear statement on the identification guarantees of the algorithm. It is not clear whether Theorems 1-6 imply that in a linear non-Gaussian model, under Assumption 1 and rank-faithfulness, the underlying model can be uniquely identified. Similarly, it is not clear whether Theorems 7-11 imply that if Assumption 1 is not satisfied, then there will be no output.

### Questions
1. What is the exact definition of neighbor? The examples on line 179 rely on the fact that $\text{Ne}^{\mathcal{H}_2}(O_1)\setminus{O_3}=\emptyset$. This indicates that $\text{Ne}^{\mathcal{H}_2}(O_1)$ does not correspond to the sibling set (which is $L_1$) nor the neighbor set in the undirected graph (which is $(O_2, O_3, O_4, O_5)$).

2. How are the augmented nodes ($O'$, $O''$) used in the identification results and algorithms?
My understanding is that they are only used in the algorithm, where the algorithm duplicates each observed variable with two extra copies and add non-Gaussian noises to them. 

3. Are there any identification guarantees for the recovery output? Specifically, does Theorems 1-6 imply that in linear non-Gaussian model, under Assumption 1 and rank-faithfulness, the underlying model can be uniquely identified? Similarly, doesn Theorems 7-11 imply that if Assumption 1 is not satisfied, then there will be no output?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an efficient and trustworthy causal discovery method for discovering latent variable structure. The main difference compared with the previous work is that it will raise an error rather than draw an incorrect causal conclusion when the purity assumption is not met.

### Strengths
- Some theoretical results are proposed along with an efficient causal discovery algorithm.
- The overall writing is clear and well-structured.

### Weaknesses
 - Although this paper allows violating the purity assumption, the overall identification results and the algorithm mostly rely on the pure children assumption, e.g., by locating the pure children like the previous work (e.g., Jin et al., 2024). Whether the purity for identifying the causal structure necessary? What is the complete identifiability under the impurity setting?
- What is the intuition in obtaining the efficient causal discovery compared with the other works, e.g., which step is the key step in providing a faster discovering ability?

### Questions
See the weaknesses above.

### Soundness
3

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
4

### Summary
This paper considers the problem of causal discovery with latent variables, in a more general setting where the causal relations between observed variables are allowed, with some other structural assumptions (e.g., pure children). Moreover, those assumptions are claimed to be testable, i.e., when the assumptions are not satisfied, the algorithm can raise an error.

### Strengths
1. The idea to testify the graphical assumptions and give an error signal instead of giving possibly incorrect result is very significant for causal discovery with latent variables.

2. The generalization to allow edges in between observed variables is good.

### Weaknesses
Overall, the current draft's presentation **requires substantial improvement**. It's cluttered with theorem after theorem, while the core algorithm is scattered throughout and described with vague language. This makes it easy for readers (at least me) to lose track, unclear on the purpose of each theoretical statement, and difficult to assess the correctness of all the assertions. I totally understand that the work involves dense technical material and possibly complex algorithms, but this shouldn't excuse its current lack of clarity.

Here are my specific comments/questions:

1. In assumption 1., I guess what the authors meant is pure children or neighbors in the observed variables? Though the observed variables is not within the scope for definition 1.

2. For definition 2 (Identifiable pair, IP),
   - The definition heavily relies on H2, and the definition for H2 heavily relies on Vf. But so far (when definition 2 is presented) we only have "Vf is unknown", "H2 is unknown", which makes the understanding to definition 2 at that point very difficult, if not impossible.
   - Please explain every definition/theorem/algorithmic step's purpose before directly delving into the technical sides (same applies elsewhere). E.g., here what is the general purpose of H2 (instead of the technical definition on "induced subgraph of G over Vf and VC")? What does Vf's "launched in the future" mean? It's until pg.6 did I notice that the authors want to use Vf for latent variables..
   - Since VC and Vf can be updated, does the "identifiable pairs" changes in each epoch, based on different VC and Vf? Intuitively this shouldn't happen, as it seems describing something regarding the true structure. Then please show that there's no such dependence.
   - Why is it named "identifiable pairs"? Theorem 1 shows a way to sufficiently identify them from data, but are they necessarily all the pure children information that can be identified (e.g., using Adam's formulation of equivalence class)?
   - Instead of {V1, V2} ∈ S, please use e.g., (V1, V2) to indicate that they are ordered.

3. In definition 4's "Intuition", what are those "e1', e2', ..."? Are they referring to the noise added to get Oi' in O1 variables?

4. In theorem 2, what does "let {Vi1, Vi2}⊂ChH1(Vi)" mean? I understand that at the initialization epoch, ChH1(Vi) is just the corresponding two added O1 variables. But after that, does it mean "for any two variables in ChH1(Vi), the followings hold"?

5. In theorem 3, what does "∀Si ∈ S2" mean? Before this all the notations for enumerating items in S is in the form of {Vi, Vj} ∈ S. If the authors intend to express a same thing, please be consistent throughout.

Overall, for all the clarity/presentation issues that prevents me to further evaluate the work, I would appreciate it if the authors could provide:
   - A clear overview of the algorithm: What is the input? What are all the assumptions (except for the structural ones, e.g., at least there should be some faithfulness)? What is the output (to which equivalence class does it identify -- e.g., does it achieve Adam's? which parts are assumed to be correct? when (if and only if) will the algorithm give an error signal)?
   - A detailed pseudocode for the algorithm. For each step, instead of vague language (like those in the current "Updating the Active Set" paragraph), please use formal math/set language. For all the claims on the intermediate results (e.g., those reflected by condition 1, theorems 1, 2), please use "assert" lines.

--- 

Some other methodological questions:

6. Why do the authors need to add new simulated variables O1 into the system? Intuitively they couldn't give any more information than those already encoded in O0. In other words, all information found by O1 should be able to be found by O0. Could the authors please give an example where such intuition is incorrect? Otherwise the O1 seems only adding more unnecessary complexities.

7. What is the relationship between the two main constraints (Pseudo-residual and Quintuple constraint) used in this paper and the GIN condition? If they are special cases for GIN condition, why not directly use the GIN condition? Or can they identify something beyond GIN?

8. Regarding the at-least-2-pure-children assumption, can this algorithm be applied to violation cases e.g., measurement error?

9. Regarding the testability of the assumption, could the authors please give a brief review and compare to how other (linear non-Gaussian acyclic models with latents) work testify their assumptions?

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3

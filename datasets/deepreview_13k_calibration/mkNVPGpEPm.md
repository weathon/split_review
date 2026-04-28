# Associative memory and dead neurons

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
In ``Large Associative Memory Problem in Neurobiology and Machine Learning,'' Dmitry Krotov and John Hopfield introduced a general technique for the systematic construction of neural ordinary differential equations with non-increasing energy or Lyapunov function. We study this energy function and identify that it is vulnerable to the problem of dead neurons. Each point in the state space where the neuron dies is contained in a non-compact region with constant energy. In these flat regions, energy function alone does not completely determine all degrees of freedom and, as a consequence, can not be used to analyze stability or find steady states or basins of attraction. We perform a direct analysis of the dynamical system and show how to resolve problems caused by flat directions corresponding to dead neurons: (i) all information about the state vector at a fixed point can be extracted from the energy and Hessian matrix (of Lagrange function), (ii) it is enough to analyze stability in the range of Hessian matrix, (iii) if steady state touching flat region is stable the whole flat region is the basin of attraction. The analysis of the Hessian matrix can be complicated for realistic architectures, so we show that for a slightly altered dynamical system (with the same structure of steady states), one can derive a diverse family of Lyapunov functions that do not have flat regions corresponding to dead neurons. In addition, these energy functions allow one to use Lagrange functions with Hessian matrices that are not necessarily positive definite and even consider architectures with non-symmetric feedforward and feedback connections.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work investigates Lyapunov functions and stability in the Krotov and Hopfield models of associative memory. It is found that the conventional formulation suffers from a problem of dead neurons, which arises when some of the neurons’ activation functions saturate. In this situation the energy becomes independent of the state of those neurons. The authors propose a projection of the original class of models on a subspace of non-dead neurons, analyze the stability of those models, and propose a novel class of Lyapunov functions that describe those models.

### Strengths
Dense Associative Memory models have several possible formulations and admit studies of a broad class of AI models used in practice. At the same time, their Lyapunov (energy) functions remain underutilized and the shape of those energy landscapes remains under investigated. This paper tackles this exact question and analyses the stability of the dynamics and the sensitivity of the energy with respect to the state of the neurons from a novel angle. The problem of dead neurons can be a serious obstacle for training these models at scale in interesting AI applications. This work formalizes this problem, and offers a possible solution by identifying non-dead subspaces and proposing a novel class of energy functions. The paper is generally well-written, although there are small issues, which I explain below. The results presented in this work are novel and relevant to the ICLR community.

### Weaknesses
There are two issues with the way how authors introduce the problem of dead neurons (example 2, 3, 4). First, in the Krotov-Hopfield formalism, one needs to check two things:

1. Positive definiteness of the Hessian of the Lagrangian.
2. Boundness of the energy function from below.

Only when both conditions are satisfied the models under consideration have stable fixed point dynamics. The authors rightfully focus on the first requirement in their presentation, but somehow the second one is not discussed enough. For instance, please notice that the model studied in Example 2 does not have an energy bounded from below. This means that one can choose a matrix $\mathbf{W}$ such that the energy will keep decreasing to minus infinity with time, and the model will never reach a fixed point. The lower-boundness of the energy needs to be checked and discussed in the paper.

Second, Example 4 represents a situation when Lagrangian has a symmetry. Please notice (this is acknowledged in lines 194-195) that in this case there are no dead neurons, all the neurons are alive, it’s just the energy function is insensitive to the states of the variables $\mathbf{y}$ along the constant shifts of all pre-activations. I am wondering to what extent it makes sense to dub this specific example as a “dead-neuron” problem. The authors rightfully acknowledge this in lines 192-198, but I would invite the authors to consider restructuring the presentation of this example and give this specific phenomenon (Example 4) a different name, e.g. “symmetry”, “flat directions”, etc., not the dead-neuron problem.

Some typos:
1. Line 507: $E_3(\mathbf{u})$ -> $E_3(\mathbf{y})$
2. Line 509: $\Lambda(\mathbf{u})$ -> $\Lambda(\mathbf{y})$
3. Line 156-157 - subscript in $W_{21}$.
4. Line 535: Lapynov-> Lyapunov

### Questions
1. I am not sure I understood the derivation in line 284. Why does the Taylor series terminate after the second term? 
2. It seems to me that the model presented in equation 9 can be obtained from the Krotov-Hopfield model by introducing a new variable $\mathbf{y}=\mathbf{Wu}+\mathbf{b}$. Are these two classes of models equivalent under this change of variables, or does the introduction of matrix R make equation 9 more general than Krotov and Hopfield?
3. In all the derivations $\mathbf{b}$ is assumed to be time-independent. This is fine (same is true in Krotov-Hopfield). I am wondering though, if anything could be said about situations when $\mathbf{b}$ depends on time? E.g., could energy function (10) still guarantee convergences for some properties of $\mathbf{b(t)}$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work expands on the literature of modern Hopfield networks, and that of Dense associative memories. In detail, it identifies a drawbacks of the current approach developed by Krotov and Hopfield, that is, the presence of ‘dead neurons’ that cause regions of constant energy. The authors then address this problem by defining a new family of Lyapunov functions that is a variation of the original one, but does not suffer from the problem of dead neurons causing flat regions.

### Strengths
The work is well structured: it identifies a gap in the literature, and theoretically addresses it. The gap is also a significant one, as flat regions of steady states can negatively affect the retrieval of specific memories.

The stability analysis is interesting, and it seems well made. Similarly, I share the belief of the authors about the underutilisation of the Lyapunov function in the literature. Actually, I would move the discussion in the conclusion (“*The role of Lyapunov’s function is merely to provide comfort that some steady states may exist somewhere. As we show in this article, it is often a false comfort.*”) in the introduction, to make the claim of the paper clearer. 

Despite not being sure I was able to follow the math all the way, I believe the solution proposed by the authors to be correct.

### Weaknesses
The biggest cons of this work is the clarity. I found it hard to follow the computations, theorems, claims, and their consequences. The 10 pages are very dense. I would:

1) Add figures that make some concepts clearer;

2) Move some non-interesting proofs to the appendix, and leave in the main body only the computations needed to understand concepts (you could even provide proof sketches).

As I did not manage to follow the paper perfectly, I will also provide a low confidence score.

### Questions
Are there specific tasks in which you could measure the advantage of the newly proposed energy function? For example, testing how many stored memories can you perfectly retrieve, or the capacity of the model? Similarly to the many provided in Millidge et al.?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper builds on the work of Krotov and Hopfield 2020 looking at associative memories, with particular emphasis on the classical continuous Hopfield network (Hopfield 1984), the Dense Associative Memory (Krotov and Hopfield 2016), the modern continuous Hopfield network (Ramsauer et al. 2020), and the energy transformer (Hoover et al. 2023). More broadly, this paper looks at associative memories as dynamical systems, similar to neural ODEs, and investigates the impact of dead neurons on such systems. A dead neuron in this context refers to a neuron which has no effect on the model behavior due to always taking values that are in some way constant. Dead neurons can arise from many situations, but two such classes discussed in Section 2 are saturated neurons and symmetric activation functions. This paper then analyzes how dead neurons impact the degrees of freedom of a dynamical system and the Lyapunov function of the models. In particular, it is shown that the associative memories in current literature may suffer from steady states that are not stable i.e. there are dimensions of the state space (associated with each dead neuron) that are free to vary without affecting the energy. The paper then introduces new energy functions that alleviates some of the issues relating to dead neurons and shows all architectures explained by the functions in Krotov and Hopfield 2020 are also explainable using the new functions by an affine transformation of the neuron activities.

### Strengths
The work seems rigorous in its discussions, providing proofs of propositions and analyzing the proposed energy functions extensively. The work appears original, although it is mostly building off previous associative memory literature and work on dead neurons. The paper appears to be reasonably significant in the field of associative memories, and if the claims of the impact of dead neurons are true, this could represent a significant step in the analysis of neural ODEs and similar dynamical systems.

### Weaknesses
The basis of the paper, Section 2, is confusing and difficult to match up to other literature on associative memories. In particular, Equations 1 through 4, which are fundamental to the remainder of the paper, are stated to be from Krotov and Hopfield 2020, but do not appear in the form given in this paper. A rewriting of Section 2 would be beneficial to improve the clarity of the work and aid reader's understanding. Rewriting of subsequent sections to reference a clarified Section 2 would also help a reader follow each point made by this work.

The notation used in the paper is unique to other papers on associative memories, which in itself is not an issue, but there is no explanation of the notation. This is a problem when discussing other literature, as matching the discussions in this paper to other referenced papers becomes nearly impossible. In many sections, steps are taken that are not obvious to the reader and may impact the ability to follow this work. There are numerous grammatical errors throughout the manuscript that can obfuscate the meaning of sentences or entire paragraphs. It is difficult to verify the claims made in this paper due to the difficult-to-follow nature of each section.

The key ideas of the paper seem sufficient for publication, but would need to be presented in a more understandable format.

There seems to be a typo on line 044: "The most cluical requirement" should be "The most crucial requirement".

Equations 1 through 4 --- what do these correspond to in Krotov and Hopfield 2020? Looking through the cited paper, there are no equations of a similar form, have the authors of this paper rewritten something from Krotov and Hopfield 2020 in a more convenient form? If so, perhaps a brief description of what has been changed from Krotov and Hopfield 2020 (a notation translation guide) would benefit this paper. Further, Equations 1 through 4 appear to actually consist of more than four equations, some of which are constraints (such as W = W transpose). Cleaning up the formatting here such that each equation is on one line with a separate number may benefit the paper.

At the start of Section 2 the paper makes several claims about the properties of Equations 1 through 4, including important properties of the energy function in Equation 4. However, these claims are not obvious to me. Is there a reason that the "structural assumptions" of Equation 2 (is that the first or second equation on line two?) ensures the energy function exists? This discussion could be expanded slightly for readers who are not familiar with the equations set forth here.

The next paragraph continues these discussions and makes claims about the dynamical systems described by Equation 1. However, again I can not immediately see why the steady states of these differential equations can be used as memory vectors --- could this be discussed further or given a citation?

Example 1 seems somewhat ill-defined in the edge cases. The given differential equation for y_i does not apply for y_1; what is the value of the weight matrix W_{10}? Should we treat this as 0? This would line up with my expectation of the MLP with feedback connections, but the formalization does not support it. Perhaps some discussion of the edge cases here would be beneficial.

There is a slight typesetting error on line 156: The equation is currently rendered like "$ W_{12} = W_{2}1^\top $", rather than "$ W_{12} = W_{21}^\top $" i.e. the "1" on the second matrix W is not subscript. 

Example 2 is the first time that the term "dead neuron" is linked directly to the ReLU activation. Dead neurons are referenced to Lu et al. 2019 in the introduction (line 091) but perhaps a short introduction to the term to ground this work would help a reader understand where the discussion is heading. Especially considering the term is then applied to other activations in Examples 3 and 4. What exactly is meant by a neuron being dead? This could be added to the introduction. Reading on, the definition of a dead neuron appears quite late in Section 2, which is already substantially through the paper. Is there some way to introduce the key concepts of the paper earlier?

The paper seems to have a significant focus on the energy function being non-discriminative on a non-compact region of state space. It may benefit a reader's understanding to have a short discussion on what this means, especially in the context of associative memories and physics inspired models.

The proof for Proposition 1 is somewhat difficult to follow. The Taylor expansion of the Lagrangian seems to make the implicit assumption that $ L(y) = 0.5 g(y)^2 $, which perhaps could be stated explicitly in the proof even though this is a common formulation. Past this, it is not clear to me why the second term shifts by the specified quantity, and how this is compensated by a similar shift in the first term. Some more verbose discussion here could help readers follow the proof.

Much of the body of this paper hinges on the formalization of Equations 1-4. Without having this section very clearly laid out for the reader, the remainder of the paper is often difficult to follow. Is it possible to rework this initial Section 2 to improve clarity? In particular, stating notation clearly early in the paper would be very helpful. Following sections would then be able to reference back to the key statements in Section 2 with minimal confusion.

Again for Equation 5 it is not clear what Lyapunov function you are referencing in Hopfield 1984. This looks to be most similar to Equation 7 or 11 in the 1984 paper, but the lack of notation formalization in this work makes it difficult to draw parallels.

Much of Section 3 and 4, (e.g. Section 3.2), may benefit from being written into a longer paper where the authors can be more verbose in explaining each step of the mathematics.  Currently, the paper is very terse in its discussion, which is understandable considering the page limit of the conference, but this does not help a reader understand the key aspects of this mathematically dense manuscript.

Near the start of Section 4, where we discuss the value of R(u), are we assuming that no value of the matrix R(u) is zero, or that the matrix is not equal to the zero matrix (i.e. all values zero)? The manuscript is slightly unclear on this.

### Questions
There seems to be a typo on line 044: "The most cluical requirement" should be "The most crucial requirement".

Equations 1 through 4 --- what do these correspond to in Krotov and Hopfield 2020? Looking through the cited paper, there are no equations of a similar form, have the authors of this paper rewritten something from Krotov and Hopfield 2020 in a more convenient form? If so, perhaps a brief description of what has been changed from Krotov and Hopfield 2020 (a notation translation guide) would benefit this paper. Further, Equations 1 through 4 appear to actually consist of more than four equations, some of which are constraints (such as W = W transpose). Cleaning up the formatting here such that each equation is on one line with a separate number may benefit the paper.

At the start of Section 2 the paper makes several claims about the properties of Equations 1 through 4, including important properties of the energy function in Equation 4. However, these claims are not obvious to me. Is there a reason that the "structural assumptions" of Equation 2 (is that the first or second equation on line two?) ensures the energy function exists? This discussion could be expanded slightly for readers who are not familiar with the equations set forth here.

The next paragraph continues these discussions and makes claims about the dynamical systems described by Equation 1. However, again I can not immediately see why the steady states of these differential equations can be used as memory vectors --- could this be discussed further or given a citation?

Example 1 seems somewhat ill-defined in the edge cases. The given differential equation for y_i does not apply for y_1; what is the value of the weight matrix W_{10}? Should we treat this as 0? This would line up with my expectation of the MLP with feedback connections, but the formalization does not support it. Perhaps some discussion of the edge cases here would be beneficial.

There is a slight typesetting error on line 156: The equation is currently rendered like "$ W_{12} = W_{2}1^\top $", rather than "$ W_{12} = W_{21}^\top $" i.e. the "1" on the second matrix W is not subscript. 

Example 2 is the first time that the term "dead neuron" is linked directly to the ReLU activation. Dead neurons are referenced to Lu et al. 2019 in the introduction (line 091) but perhaps a short introduction to the term to ground this work would help a reader understand where the discussion is heading. Especially considering the term is then applied to other activations in Examples 3 and 4. What exactly is meant by a neuron being dead? This could be added to the introduction. Reading on, the definition of a dead neuron appears quite late in Section 2, which is already substantially through the paper. Is there some way to introduce the key concepts of the paper earlier?

The paper seems to have a significant focus on the energy function being non-discriminative on a non-compact region of state space. It may benefit a reader's understanding to have a short discussion on what this means, especially in the context of associative memories and physics inspired models.

The proof for Proposition 1 is somewhat difficult to follow. The Taylor expansion of the Lagrangian seems to make the implicit assumption that $ L(y) = 0.5 g(y)^2 $, which perhaps could be stated explicitly in the proof even though this is a common formulation. Past this, it is not clear to me why the second term shifts by the specified quantity, and how this is compensated by a similar shift in the first term. Some more verbose discussion here could help readers follow the proof.

Much of the body of this paper hinges on the formalization of Equations 1-4. Without having this section very clearly laid out for the reader, the remainder of the paper is often difficult to follow. Is it possible to rework this initial Section 2 to improve clarity? In particular, stating notation clearly early in the paper would be very helpful. Following sections would then be able to reference back to the key statements in Section 2 with minimal confusion.

Again for Equation 5 it is not clear what Lyapunov function you are referencing in Hopfield 1984. This looks to be most similar to Equation 7 or 11 in the 1984 paper, but the lack of notation formalization in this work makes it difficult to draw parallels.

Much of Section 3 and 4, (e.g. Section 3.2), may benefit from being written into a longer paper where the authors can be more verbose in explaining each step of the mathematics.  Currently, the paper is very terse in its discussion, which is understandable considering the page limit of the conference, but this does not help a reader understand the key aspects of this mathematically dense manuscript.

Near the start of Section 4, where we discuss the value of R(u), are we assuming that no value of the matrix R(u) is zero, or that the matrix is not equal to the zero matrix (i.e. all values zero)? The manuscript is slightly unclear on this.

### Soundness
2

### Presentation
3

### Contribution
3

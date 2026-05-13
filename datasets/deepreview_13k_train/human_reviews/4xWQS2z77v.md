# Exploring The Loss Landscape Of Regularized Neural Networks Via Convex Duality

- Decision: Accept
- Scores: 8, 8, 8, 8, 8

## Abstract
We discuss several aspects of the loss landscape of regularized neural networks: the structure of stationary points, connectivity of optimal solutions, path with nonincreasing loss to arbitrary global optimum, and the nonuniqueness of optimal solutions, by casting the problem into an equivalent convex problem and considering its dual. Starting from two-layer neural networks with scalar output, we first characterize the solution set of the convex problem using its dual and further characterize all stationary points. With the characterization, we show that the topology of the global optima goes through a phase transition as the width of the network changes, and construct counterexamples where the problem may have a continuum of optimal solutions. Finally, we show that the solution set characterization and connectivity results can be extended to different architectures, including two-layer vector-valued neural networks and parallel three-layer neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors present a deep and novel analysis of the loss landscape and a solution in the context of regularized neural networks. They also show that the topology of the global optima undergoes a phase transition as the width of the network changes.

### Strengths
The paper is well-written, easy to follow, and its results are clear and novel. The theoretical results stand out for their depth and clarity, as do the empirical results. The support of images is quite helpful when reading through some mathematical arguments or proofs of theoretical results.

### Weaknesses
Perhaps a deeper discussion on the topological implications of their results would be beneficial.

### Questions
No questions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this work the authors analyze multiple aspects of the loss landscape of regularized two-layer neural networks with scalar output, including the structure of stationary points, the connectivity of optimal solutions and the non uniqueness of optimal solutions. The main proof strategy is to translate the problem into an equivalent convex problem and characterize its solution set through its dual form. 
The authors show that the topology of the global optima goes through a phase transition as a function of the hidden layer width, which they term the staircase of connectivity. 
This result is extended later to networks with vector-valued outputs, and parallel deep networks of depth 3.

### Strengths
- I found the "staircase of connectivity" very insightful, particularly how the connectivity properties of the optimal solutions are connected to critical widths $m^*$ and $M^*$. This finding explains how increasing the number of neurons affects the connectedness of optimal sets, and makes the observation of mode connectivity [Garipov et al. 2018] more precise. 
- The paper generalizes its findings also to vector-valued networks and deep networks with skip connection, which provides a broader framework that can be applied across different architectures.

### Weaknesses
 - I found the "staircase of connectivity" very insightful, particularly how the connectivity properties of the optimal solutions are connected to critical widths $m^*$ and $M^*$. This finding explains how increasing the number of neurons affects the connectedness of optimal sets, and makes the observation of mode connectivity [Garipov et al. 2018] more precise.
- The paper generalizes its findings also to vector-valued networks and deep networks with skip connection, which provides a broader framework that can be applied across different architectures.

 - I found the theoretical results, for instance on the staircase of connectivity, hard to interpret in practice and would benefit from more accessible explanations. While the toy example in Example 1 illustrates the concept, the absence of labels in Figure 2, as well as the notation-heavy formulation makes it difficult for readers to grasp the results intuitively. Specifically, the connection between the theoretical constructs and their practical implications for neural network training remains unclear. The paper would benefit from a more intuitive explanation of how the critical widths $m^*$ and $M^*$ manifest in the training process and how they impact the optimization landscape.
- Although the toy examples are helpful, the paper lacks actual empirical validation of the theoretic results. I think it would add credibility to this work, if the staircase of connectivity concept would also be tested on actual neural network architectures trained on real data. It would be interesting to see how these results scale with different data distributions and larger models. The absence of empirical validation leaves a gap in understanding the practical relevance of the theoretical findings. It is unclear how the theoretical results translate to real-world scenarios, and whether the observed phase transitions are robust to different data characteristics and model architectures.
- Overall I found the work quite difficult to read due to the dense mathematical formalism. I also feel like the section on notations should not be in the appendix, but should - at least in a shortened version - be included in the main paper.

### Questions
1. Is there a way to bound or estimate the critical widths $m^*$ and $M^*$ in practice, for instance on real datasets? 
2. In line 186: What does $h$ refer to in $\text{diag}[1 (Xh \geq 0)]$ ?
3. It is not very clear to me what lines 225-226 mean. Could you perhaps rephrase it? (That $\mathcal{P}^*_{\nu^*}$ does depend on $\nu^*$, but that the specific choice of it does not matter.)
4. Figure 2 bottom: The axis labels are missing and it is not very clear to me what the red and blue lines are supposed to represent.
5. In line 351 the author mention three interpolation problems of interest, but only discuss one problem on the minimum-norm interpolation problem. What are the other two interpolation problems and can you also extend your results to these problems?
6. The paper describes a path of nonincreasing loss that connects local to global minima. Could this insight be incorporated into practical training algorithms, such as initializing weights or guiding optimizers in large-scale training?

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
In this paper, the authors apply convex duality for two-layer ReLU networks to study mode connectivity and unique minimal-norm interpolator problems, while also working to generalize this framework. Specifically, the authors have:

* identified the staircase of connectivity that describes how connectivity evolves with width;
* constructed none-unique minimal-norm interpolator by breaking the uniqueness conditions;
* generalized the optimal polytope to the general cone-constrained group LASSO problem and applied it to more complicated architectures.

### Strengths
The authors apply the new technique of convex duality to problems of connectivity and minimal-norm interpolation, which have been studied previously using other methods. This approach yields both generalizations of existing results and new insights into these problems. Overall, I believe this paper is a strong demonstration of how convex duality can be leveraged in the theoretical study of machine learning. The abstract concepts are clarified through figures and examples.

### Weaknesses
I have some concerns with the presentation of this work. Specifically:

*   If I understand correctly, the convex duality only applies to ReLU networks. This is not emphasized. The implications of this restriction on the broader applicability of the results should be discussed. For instance, how does this limitation affect the conclusions about mode connectivity when compared to networks using other activation functions like sigmoid or tanh, which do not have the same piecewise linear structure as ReLU?
*   I found Section 2 difficult to follow without prior knowledge of Pilanci & Ergen (2020). The relations between (1), (2), and (3) are mentioned but not explained (When do they have the same loss value? How do the solutions relate to each other?) Dimensions of $X$ and $y$ are not mentioned. $D_i$ is not explained. It is unclear how the convex reformulation is derived and under what conditions it holds. The lack of clarity makes it difficult to assess the validity and generality of the approach.
*   In Figure 1, is each red point truly a unique solution, or does it represent solutions equivalent under permutation (p-unique)? If they are p-unique solutions, readers may get the wrong impression. The figure should explicitly state whether the solutions are unique in parameter space or unique up to permutation. If they are p-unique, this should be clearly indicated in the caption and the main text, as it significantly impacts the interpretation of the results.
*   The lower half of Figure 2 is not explained. The figure caption should provide a detailed explanation of what is being visualized in the lower half, including the axes, the data points, and the significance of the observed patterns. Without a proper explanation, the lower half of Figure 2 is essentially meaningless to the reader.

### Questions
I wonder if the authors have any comment regarding the weaknesses.

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
3

### Summary
This paper studies the loss landscape of ReLU networks with $L_2$-regularization. The authors first study the canonical case of a two-layer  network with scalar output, and characterize the connectivity of the solution for different number of neurons. Then, the authors extend the results to a more general class of problems, including: minimal norm interpolation, vector-valued ReLU network, and parallel deep neural network.

### Strengths
1. This paper develops a general framework to characterize the global optimum of the regularized ReLU network via convex duality. From my understanding, the key contribution of this convex duality framework in Theorem 1 is that it allows one to characterize the "direction" of the weights separately in the regularized case, which is then useful for characterizing the global optimum. I believe this contribution is novel and solid. 

2. I think the framework of characterizing the global optimal is quite general even though it is restricted to ReLU network. In particular, it do not require large over-parameterization, special scaling, or special data distributions. Thus, I believe the results can be applied to other more specific settings and is potentially useful for characterizing other properties besides the connectivity of the solutions.

### Weaknesses
1.Although I believe this paper has a solid contribution, I found there's a few part I don't understand the significance:    
- I think I understand the contributions in section 3.1 and 3.2, however, I'm not sure about  In section 3.3, the authors showed that for a class of data set with dimension $=1$ that satisfies certain conditions, if the network do not have skip connection, then there are infinitely many minimal norm interpolators (which is a connected set ). I'm not sure the significance of these results, since (1) it is for a special construction of dataset. (2) it might be that those infinitely many minimal norm interpolators behave qualitatively almost the same, for example, the radius of the solution set is small. Could you discuss more on the significance of the results? Specifically, while the non-uniqueness is interesting, the practical implications are unclear. Do these different interpolators lead to significantly different function approximations, or do they essentially represent the same underlying function with minor parameter variations? A more detailed analysis of the function space behavior of these multiple interpolators is needed to understand the true impact of this result.

- In section 4, I understand the contribution of generalizing it to a vector-valued function. However, I'm not sure the significance of the results in Theorem 4. Since anyway you fixed all the other layers but only keep two consecutive layers, and technically I didn't see any difference from a two-layer network.  Could you discuss more on the significance of the results? It seems that the analysis is essentially reduced to a two-layer network by fixing the other layers. What is the added value of considering this specific deep network setup? Is there any new insight gained from this analysis that cannot be obtained from a standard two-layer network analysis? The connection to practical deep learning scenarios is not clear, and a more compelling justification is needed.

2. One main issue of the paper is the writing, especially the main part of the paper. I check the appendices, and it is much more readable. So I suggest the authors consider rearranging the content. To name a few issues\typos that confuse me when reading the main part: 

    - Line 215: and 216, what is the definition of $\mathcal{S}_i$?
    - Line 223: what the definition of "optimal model fit", what is $u_i^*, v_i^*$, and why it is unique?
    - Line 232: the triangle inequality is reversed. Also could you be more specific about the discussion between Liine 229-232?
    - The statement of Proposition 1:  First, you use $v_{i,1}$ to denote the first entry of a vector, could you specify this?  Also, you define $s_k = \sum_{i=1}^k v_{n-i+1},$ but also require $||s_k|| =1, s_n = [0,1]^\top$, could you discuss the existence of such construction? 
    - In equation (7), could you specify the dimension of the variables?

### Questions
1.  A general question is about the scope of the techniques in this paper. It seems that the techniques only apply to  two-layer ReLU networks, since the problem can be equivalently written as a convex problem with regularization. It is not applicable to other activation functions and seems hard to generalize to multi-layer cases. Thus, could you elaborate more on the universality of the techniques?

2. The results in this paper require the number of neurons $m \geq m_*$. As far as  I understand, $m_*$ is the minimal number of neurons needed to achieve the optimal model. I'm wondering what would happen if $m<m_*$? Also, in general, what is the scaling of $m_*$ depending on $n,d$? 

3. The results in Theorem 2 consider the connectivity of the optimal solution set, which is equivalent to the connectivity of a path with $0$ perturbation. What about the case that allow $\epsilon$-pertubation along the path? Is the techniques still applicable?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This manuscript proposes a characterization of the topology of the global optima in the loss landscape, focusing on regularized two-layers neural networks with free skip-connections with a partial extension to deep neural networks. The authors provide a characterization of the optimal set in terms of the width of the hidden layer, which determines a so-called "staircase of connectivity" when such a width occurs in critical values and phase transitions. The authors study the uniqueness of the minimum-norm interpolator, highlighting necessary guarantees (such as the free ski connections, bias in the training problem and unidmiensional data). An experimental study integrates the theoretical findings.

### Strengths
The paper has original content, and bridges together several concepts proposed in the literature on the topic. The method of analysis is rigorous and it gives a solid contribution to the field.

### Weaknesses
The manuscript presents some unclear sentences (e.g. line 198-199), making it difficult to fully grasp the nuances of the proposed analysis. There is a clear math error at line 232 (the triangle inequality holds with the reverse inequality; to be candid, I am quite sure it is a typo) and some symbols are not defined at all, not even in the Appendix (e.g. the symbol P, that occurs very often through the entire manuscript), which hinders the reproducibility and understanding of the theoretical framework. Furthermore, there are many references to results listed in the Appendix; if relevant, I think it might be better to put them in the main manuscript, as constantly switching to the appendix disrupts the flow of reading and makes it harder to follow the key arguments. An important reference to the characterization of loss landscapes over neural networks with regularization terms and/or skip connections is missing, also because it gives a theoretical hint on the low importance of skip connections [1]. The experimental section, while present, could benefit from more detailed explanations of the setup and the specific choices made in the implementation, making it difficult to assess the validity of the experimental results in relation to the theoretical findings.

### Questions
Can the authors proofread again the manuscript to eliminate typos, unclear sentences and missing notation?
Can they make the presentation of the result more readable, including relevant results from the Appendix?
Can they integrate the relevant existing literature in the Related Work section?

### Soundness
3

### Presentation
3

### Contribution
3

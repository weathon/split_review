# Understanding Mode Connectivity via Parameter Space Symmetry

- Decision: Reject
- Avg Score: 6.20
- Scores: 8, 6, 3, 6, 8

## Abstract
Neural network minima have been observed to be connected by curves along which train and test loss remain nearly constant, a phenomenon known as mode connectivity. 
While this has enabled applications such as model merging and fine-tuning, its theoretical explanation remains unclear. 
We propose a new approach to exploring the connectedness of minima using parameter space symmetry.
By linking the topology of symmetry groups to that of the minima, we derive the number of connected components of the minima of linear networks and show that skip connections reduce this number. 
We then examine when mode connectivity and linear mode connectivity hold or fail, using parameter symmetries which account for a significant part of the minimum.
Finally, we provide explicit expressions for connecting curves in the minima induced by symmetry. 
Using the curvature of these curves, we derive conditions under which linear mode connectivity approximately holds.
Our analysis highlights the role of continuous symmetries in understanding the neural network loss landscape.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies mode connectivity in neural networks modulo parameter space symmetries from the perspective of topology. 

Authors begin by the counting the connected components of observation that for Euclidean distance as the loss function, the minima of a deep linear network with $l$ hidden layers and invertible weight matrices has $2^{l-1}$ connected components, followed by the observation that having skip connections similar to ResNets reduces the space of connected components. 

For deep linear networks, authors show that one can reduce connected components if one takes into account for permutations. 

Authors then use layer wise scale symmetries in deep networks to show that linear mode connectivity doesn’t hold, however if one controls the weight norms for each layer, we can control the error barrier incurred by linear interpolation within the same connected component. 

Finally, authors introduce general symmetry induce curves that parameterizes the level set of the loss, authors use to curvature of the curve to give sufficient condition for when approximate linear connectivity holds.

### Strengths
- This is a well written paper and authors include sufficient background to make the paper readable for a non-expert in topology, like myself to follow all the results and make inferences.
- Authors provide a novel analysis studying mode connectivity in deep linear networks.
- Authors make a number of contributions studying necessary conditions for mode connectivity and approximate linear connectivity that can be used to understand symmetries in neural networks.

### Weaknesses
 - I see that there is no dependence on width of the network when considering the number of connected components, however permutation symmetries grows exponentially with the width of the network. This appears to be due to the fact we are studying a very simplified setting of linear networks. It’ll be useful for the readers to include a discussion on this.
- It’ll be improve the paper further to improve an example / figure for section 5.1 where permutations leads to mode connectivity.- It is well known that scale symmetries lead to a failure of linear mode connectivity however it is interesting that controlling the weight norms and control over the curvature leads to approximate linear connectivity.
    - How does this relate to  empirical solutions explored by SGD? Specially because it appears that weight decay is necessary for lmc mod permutations.

### Questions
It is well known that scale symmetries lead to a failure of linear mode connectivity however it is interesting that controlling the weight norms and control over the curvature leads to approximate linear connectivity.

- How does this relate to  empirical solutions explored by SGD? Specially because it appears that weight decay is necessary for lmc mod permutations.

### Soundness
3

### Presentation
4

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
The authors investigate mode connectivity from a mathematical perspective. Several results are obtained: (1) The number of connected components of the set of minimizers is characterized in case of linear networks with and without skip connections, where adding skip connections reduced the number of components. (2) In case of 2 layers, they show how permutations can map points to different components, thus “connecting” them and shedding light on recent empirical observations. (3) Next the authors also show that linear mode connectivity does not hold in case of ReLU networks, and that permuting the last two layers does not reduce the barrier either. (4) Finally, the authors characterize non-linear paths connecting such minima and obtain bounds on their curvature, which measures how far away one is from a “linear mode connectivity” regime.

### Strengths
1. The paper is well-organized and states all the mathematical results in the Preliminaries section, making this a largely self-contained work and thus easier to read and understand. Linear mode connectivity is still lacking a proper mathematical understanding to this day, making this submission thus a timely contribution.
2. The authors manage to gain quite some insight into the problem with rather mathematically elementary tools, relying on topological properties and results from group theory. I appreciate the result showing that skip connections reduce the number of components, which is in-line with what people observe in practice in terms of easier optimization. 
3. It is also quite nice that in case of two layers, the authors manage to show that permutations indeed connect the components back. While things in practice might be significantly more complicated than the setting considered in this work, I still believe this is a good first step towards obtaining a better understanding of this intriguing phenomenon.

### Weaknesses
1. What does it mean intuitively and geometrically if two network parameters are in the same connected component? As the authors point out, this does not imply being path-connected, so while it sounds convincing at first, it is actually not clear to me how this notion ties back to the usual geometric understanding of connectivity used in deep learning. I would appreciate if the authors could clarify things. I.e. how pathological are counter-examples of “connected but not path-connected”? Specifically, are these counter-examples measure zero sets, or do they have some non-trivial volume in parameter space? This distinction is crucial for understanding the practical implications of the theoretical results.

2. One weakness in the “large barrier” type of results is their global nature, i.e. there is no notion of what types of minima SGD actually finds. The counter-example (as far as I understood) for which a path is constructed for Prop 5.3 and 5.4 starts from a set of parameters and then constructs a new one using the rescaling symmetry. It is not clear to me how “degenerate” these solutions are in the sense that SGD might never choose them due to its implicit bias. I believe there are actually results that show that SGD prefers certain parameters out of the re-scale orbit. In general I think it would be important to better highlight that this work deals with the loss landscape in a global sense, and is not restricted to the minimizers discovered by SGD. Furthermore, it would be beneficial to discuss the implications of these global results for practical optimization scenarios. For instance, if the constructed paths are highly unlikely to be encountered by SGD, then the practical relevance of these results may be limited.

3. The word “connected” has several meanings in this work and I sometimes was confused which one is currently used in a given part of the text. E.g. when two points are in the same connected component (e.g. when mapping with permutations), this is not the same thing as when two points cannot be connected linearly etc. I feel like the manuscript could do a better job at distinguishing these things. For example, it would be helpful to consistently use distinct terminology, such as “topologically connected” for the component-based definition and “linearly connected” for the path-based definition, to avoid confusion.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the space of minima of neural networks (mostly in the linear case) via the angle of group symmetries. A number of standard results in math are listed, and then a number of small results about the structure of minima are given, with some emphasis on the role of skip connections and on the permutations. Each result highlights the role of group actions and this is the main originality of the paper. Overall, I do not see any results that are particularly striking or insightful to understand neural networks in practice. The derivations do not shed a light on any phenomenon of interest, and the presence of group actions when it is not already almost trivial is not established. As a result, while the idea of looking at things from the angle of group action is appealing and elegant, it does not bring convincing additional insight to study the hard question of the minimum landscape of nonlinear neural networks. I would encourage the authors to keep looking in this direction, but something striking would be needed for me to excited.

### Strengths
Rigorous, mathematically clean, reasonably clear article.

### Weaknesses
The paper explores the space of neural network minima, primarily in the linear case, through the lens of group symmetries. While the authors present several mathematical results, many of these are standard mathematical facts, which are then re-stated in the context of neural networks. The core idea of using group actions is interesting, but the results do not provide substantial new insights into the behavior of neural networks, particularly in non-linear settings. The derivations, while mathematically sound, do not illuminate any significant phenomena related to neural network training or generalization. The application of group actions, when not trivially obvious, lacks a clear justification and practical relevance. The paper does not simplify or clarify the complex problem of understanding the loss landscape of neural networks; instead, it adds another layer of abstraction without providing concrete benefits.

### Questions
Is there any reason to believe that there is a natural group action like the ones you explain beyond the cases where it is intuitively clear that there is one? 

Can simulations reveal the presence of group actions or the relevance of your derivations beyond the obvious cases?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a method to determine the number of components achieving zero loss in linear regression by identifying a homeomorphism between the symmetry in parameter space and the set of parameters yielding zero loss. It demonstrates that permutations can link previously isolated components and offers a novel perspective on the effectiveness of residual connections.

### Strengths
1. The concept of employing a homeomorphism to connect the general linear group with the set of parameters yielding zero loss, and quantifying the loss basins by counting the connected components, is both innovative and intriguing.
2. This paper offers a fresh rationale for the effectiveness of residual connections by examining the connected components within the minima of the loss function.
3. In Section 5.1, the paper shows that permutations can link otherwise disconnected loss minima.

### Weaknesses
1. Lack of limitations: Since the homeomorphism is specifically tailored to linear regression models, it is necessary to clearly state this limitation in the introduction.
2. The paper does not sufficiently address the practical implications of the identified connected components. While the theoretical framework is interesting, it remains unclear how this understanding can be leveraged to improve training or generalization in practice. For instance, how does knowing the number of connected components inform the choice of optimization algorithms or network architectures beyond the specific case of linear regression? The paper should discuss the potential impact of this analysis on more complex models and tasks.

### Questions
1. Is it possible to experimentally validate the results of Sec. 6? Can we confirm that the valleys of the loss lines predicted by Eq. 7 correspond to the valleys in the two-dimensional heatmap of the loss landscape?
2. Is it possible to extend the analysis to more realistic models such as ResNet, which has a softmax function, using parameter symmetry and homeomorphic mapping?

### Soundness
3

### Presentation
4

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
This paper introduces a topological framework to understand mode connectivity in general, and linear mode connectivity in particular. Initially, the authors use topological structures to calculate the number of connected components at the 0-level set of the quadratic loss for invertible multi-layer perceptrons. For one-dimensional spaces, they demonstrate that residual connections reduce the number of connected components. Subsequently, they examine the influence of permutations on connectedness and provide a setup where connectedness fails. Finally, conditions are presented for achieving low-loss curves that connect modes.

### Strengths
The paper proposes a very powerful framework to analyze properties of the loss surface of deep neural networks. In particular, understanding mode connectivity can shed light on the ways to optimize networks more efficiently. The paper generally provides clear and concise explanations of the proofs for its theorems and propositions.

### Weaknesses
However, in its current form, the paper does not fully clarify the connection between topological concepts and the loss landscape of deep neural networks. While it opens with a detailed and precise introduction to topological concepts, it then directly applies these concepts to loss surfaces and networks without discussing necessary assumptions (such as the invertibility of all networks considered). Specifically, the paper does not adequately address the implications of the invertibility assumption on the expressiveness of the networks being analyzed. Additionally, there is little exploration of how the topological concept of connected components relates to the depth of the network or which elements correspond to orbits or groups, potentially with examples. For instance, how does the number of connected components change as the network depth increases, and how do these changes relate to the network's capacity to learn complex functions? Although all this does not detract from the technical accomplishments, it may reduce the paper’s impact by making it difficult for an unprepared reader to link the framework to neural network applications.

In the final section, the concept of curvature is used without clearly defining it in this context. Further, this section could connect more directly to practical applications by demonstrating empirical curves that connect modes and align with derived formulas (e.g., regarding loss growth). A similar issue is in Section 5 concerning symmetries. The discussion on symmetries lacks concrete examples of how these symmetries manifest in practical neural network architectures and how they affect the loss landscape. The paper would benefit from a more detailed analysis of how different types of symmetries (e.g., permutation symmetries, scaling symmetries) impact the connectivity of the loss landscape.

Minor Issues:

- one of the first works on the algorithms for finding connectivity is [1], not [2]

- the parameter space (Param) is referenced in Section 3.3 before being formally defined

- please use \citep where appropriate (e.g., the last paragraph of Section 5.2)

### Questions
1 - The networks analyzed are invertible up to the output layer, meaning the output dimension matches the input dimension. How strictly is this condition required? Does switching to a one-dimensional output immediately yield negative results, as suggested in Section 5.2?

2 - According to [3], layer-wise mode connectivity is achievable. Does Proposition 5.3 contradict this result, or is there a possible connection?

3 - Is proposition about residual connections restricted to 1 dimension?

[3] Adilova, Linara, Asja Fischer, and Martin Jaggi. "Layer-wise linear mode connectivity."

### Soundness
3

### Presentation
2

### Contribution
3

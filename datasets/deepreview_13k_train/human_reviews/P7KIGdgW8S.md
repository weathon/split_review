# On the Hölder Stability of Multiset and Graph Neural Networks

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Extensive research efforts have been put into characterizing and constructing maximally separating multiset and graph neural networks. 
However, recent empirical evidence suggests the notion of separation itself doesn't capture several interesting phenomena. On the one hand, the quality of this separation may be very weak, to the extent that the embeddings of  "separable" objects might even be considered identical when using fixed finite precision. On the other hand, architectures which aren't capable of separation in theory, somehow achieve separation when taking the network to be wide enough.

In this work, we address both of these issues, by proposing a novel pair-wise separation quality analysis framework which is based on an adaptation of Lipschitz and \Holder{} stability to parametric functions. The proposed framework, which we name \emph{\Holder{} in expectation}, allows for separation quality analysis, without restricting the analysis to embeddings that can separate all the input space simultaneously. We prove that common sum-based models are lower-\Holder{} in expectation, with an exponent
 that decays rapidly with the network's depth . Our analysis leads to adversarial examples of  graphs which can be separated by three 1-WL iterations, but cannot be separated in practice by standard maximally powerful Message Passing Neural Networks (MPNNs). To remedy this, we propose two novel MPNNs with improved separation quality, one of which is lower Lipschitz in expectation. We show these MPNNs can easily classify our adversarial examples, and compare favorably with standard MPNNs on standard graph learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors study stability and separability properties of multi-set and graph neural networks. They do this by establishing Holder lower bounds on the networks, which give some guarantees on separability. They argue that uniform Holder lower bounds are too restrictive, and instead propose a notion of lower Holder in expectation, which is averaged over a probability distribution on the parameters of the network. The main results in the paper are bounds on the lower Holder exponent for different types of graph and multiset neural networks. They find that common architectures have poor exponents and separability properties and propose two new message passing neural networks with better separation properties. They provide a number of numerical experiments with their newly proposed architectures, and compare against existing methods. 

Some typos I noticed: "decays rapidly with the network’s depth .", "paces. , let W be some set of parameters", "function. we say that", "multisets (Zaheer et al., 2017) ,as well as MPNNs"

### Strengths
Deep graph neural networks is an important area of research, and there are an enormous number of different architectures that have been proposed. This paper provides some valuable insights into which networks give better separation properties. The lower Holder estimates in expectation are novel contributions to the literature, as far as I am aware. The new MPNN architectures with better separation properties are a nice contribution.

### Weaknesses
The lower bounds may be pessimistic, relying on pathological adversarial examples. It is not clear how practical the advances are, in that the worst case graphs may not be encountered in practice. The choice of the probability measure under which Holder in expectation is taken seems to be essential, yet the paper does not sufficiently discuss the implications of this choice. It is unclear how the specific parameter distributions used in the theorems are justified, and how these distributions might affect the practical relevance of the results. The paper also lacks a discussion on the sensitivity of the results to the choice of these distributions. Furthermore, while the authors provide adversarial examples, they don't explore the frequency or likelihood of these examples occurring in real-world datasets, which limits the practical impact of the theoretical findings. The connection between the proposed lower bounds and actual performance on real-world graph datasets is not sufficiently established. Finally, the definition of the Wasserstein metric on line 197 appears to have an error, using a p-norm where a 1-norm is expected for W^1.

### Questions
Holder continuity is usually used for exponents in the range [0,1]. Functions that are Holder continuous with exponents larger than 1 are trivial constant functions. It is not clear to me why the main results with \alpha > 1 are interesting. Is it because it is only the lower bound and not the upper? 

The choice of the probability measure under which Holder in expectation is taken seems to be essential. However, I don't see this appearing in the discussion or even in the proof sketches of most of the results. This was confusing to me. Even in Euclidean space, it seems it would be challenging to choose the right measure. If the data satisfied the manifold-hypothesis, for example, then a function that well-separates the data could be constant almost everywhere with respect to Lebesgue measure and thus have no lower bound with Lebesgue measure, but would have some appropriate lower bound with a measure tuned to the data.

In the definition of the Wasserstein metric on line 197 there is a p-norm on the right hand side, but it is W^1. Is this correct?

The authors give a lot of pathological adversarial examples of graphs that are difficult to separate. How practical are these examples?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work analyzes the abillity for multiset and graph neural networks to separate inputs. Due to the non-injectivity of ReLU networks, the authors introduce the property of a network being Holder in expectation over random weights (Holderness is just an extension of Lipschitz continuity with an exponential factor $\alpha$). The authors then derive the lower-Holder exponents for a variety of models, and provide preliminary empirical evidence that lower Holderness is related to network performance on some synthetic tasks.

### Strengths
Overall, this is a heavily theoretical work that I am not well-equipped to confidently review. I have given it my best effort, although I will likely defer to other reviewers' judgements.

1. I really appreciate the $\epsilon$-tree experiment. I originally had my doubts that an architecture being $\alpha$ lower-Holder in expectation over *random weight parameters* is that meaningful for the practical ability of networks to distinguish inputs. Random-weight networks hardly reflect how trained networks ultimately behave. This experiment provides examples of networks which are and aren't $\alpha$ lower-Holder in expectation and shows that this property is critical in a synthetic task.
2. The theory is extensive but generally well-presented and the headline results are clear (although I did not check the proofs in detail). Proof sketches are included where appropriate.
3. The considered problem is interesting, and I appreciate how the authors generalized their framework to both multiset analysis framework to graph neural networks.
4. It's a surprising result to me that relu sum networks are $\alpha=3/2$ lower-Holder in expectation. I would have originally guessed that they would be just $\alpha=1$ lower-Holder (Lipschitz) in expectation.

### Weaknesses
1. Some of the experimental benefits are pretty marginal (especially in table 4, where the gains are smaller than the exerimental variance).
2. While the $\epsilon$-Tree experiment provides some evidence for the importance of $\alpha$ lower-Holderness in expectation over random weights, it just includes a few anecdotal examples of architectures which do and don't work. A really convincing experiment would consist of a scalar-parameterized collection of function classes (which are in turn parameterized). Say this scalar smoothly varied the resulting $\alpha$; I'd then hope to see that as $\alpha$ increased, performance increases.
3. The paper seems rushed, and has many typos. Consider lines 145-147 for example (there are many more such mistakes). The authors should thoroughly proofread their work.
4. Related, the paper presentation is somewhat haphazard, with many text-wrapped figures and tables; these really should be combined appropriately and top-aligned to the page with no text wrapping.

### Questions
Comments and questions

1. Definition 2.1 depends on choices of $\alpha$ and $p \geq 1$. Shouldn't we be talking about whether functions are $\alpha,p$ lower-Holder in expectation instead of just $\alpha$ lower-Holder in expectation?
2. The remarks on line 162-165 don't make sense to me. Consider: "Firstly, we note that if the set of $w$ for which $f (x; w)$ is $\alpha$ lower-Hölder has positive probability, then $f(x; w)$ will be $\alpha$ lower-Hölder in expectation." I don't see why this is true. If we take $p=1$ and move $c^p$ in Definition 2.1 to the denominator of the RHS, then the $w$ for which $f(x; w)$ is $\alpha$ lower-Holder produce a value inside the expectation which is $\geq 1$. Then all we can say is that the RHS expectation is atleast the probability mass of such $w$'s that satisfy the original lower-Holder condition -- this bound cannot even be greater than $1$, which is what the LHS would become after dividing by $c^p$.
3. Is the implication of the experiments in Figure 3 that the presented bounds are tight?
4. Does the adaptive ReLU activation provide any experimental benefits?
5. Am I correct in concluding from Theorem 3.3 that any smooth activation (e.g. sigmoid) cannot be $\alpha$ lower-Holder in expectation (otherwise $\alpha$ would have to be infinity)? This seems counterintuitive; consider an activation like $a^{-1} \log(1 + e^{ax})$. This function is smooth and thus cannot be $\alpha$ lower-Holder in expectation, but in the limit $a \to \infty$ approaches the ReLU function which is $\alpha=3/2$ lower-Holder in expectation.

Minor remarks:
* Reading just theorem 3.1, it is unclear how $a$ and $b$ are related to the rest of the thoerem. I suggest writing $m_{ReLU}(\ \cdot\ ; a,b)$ in the theorem statement.
* Figures should be exported as pdfs or pgfs in order to avoid text blurring.
* There is a line of work on the abillity of GNNs to discriminate signals from a spectral theory perspective which might be worth discussing:

[a] Gama, Fernando, Joan Bruna, and Alejandro Ribeiro. "Stability properties of graph neural networks." IEEE Transactions on Signal Processing 68 (2020): 5680-5695.

[b] Pfrommer, Samuel, Alejandro Ribeiro, and Fernando Gama. "Discriminability of single-layer graph neural networks." ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2021.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a framework for quantifying the separation quality of multiset and graph neural networks (GNNs) via Hölder stability. This is motivated by recent observations that certain graph pairs, despite being theoretically distinguishable by Weisfeiler-Leman (WL)-expressive MPNNs (message passing GNNs), may have their embeddings "squashed" by GNNs, to the point that they are practically indistinguishable. The authors argue that strict lower Hölder continuity, which is only fulfilled for injective embeddings, is too restrictive as a concept and instead consider lower Hölder continuity in expectation over fixed parameter distributions. Starting with the multiset case, which appears as building blocks of MPNNs, they analyze the expected Hölder stability of popular architectures and introduce two new approaches, one based on bias scaling and the other on sorting, that improve the theoretical guarantees. They then employ these new multiset architectures in MPNNs and analyze their expected Hölder stabilities w.r.t. a WL distance, the tree mover's distance (TMD) (Chuang & Jegelka, 2022). Notably, the sort-based technique is shown to be lower Lipschitz in expectation w.r.t. the TMD. The new architectures AdaptMPNN and SortMPNN are empirically analyzed on toy and real-world datasets, demonstrating superior separation compared to popular MPNN baselines.

### Strengths
- The problem is well-motivated and I enjoyed reading the paper. To the best of my knowledge, the idea is novel, and as part of the ongoing effort to understand the geometry of MPNN embeddings, this work is a notable step.
- The theory is made quite accessible, and I particularly found the $\pm \epsilon$ example, which is used throughout the theory section, to be very instructive for a high-level understanding of the theorems.
- The presented empirical results are strong and insightful, showing that AdaptMPNN and SortMPNN can perfectly distinguish certain pairs of adversarial WL-distinguishable graphs, a task which standard MPNNs fail entirely.

### Weaknesses
In my opinion, the main weakness of the paper in its current state is that there is no theoretical analysis of the (expected) lower-Hölder properties of AdaptMPNN. While AdaptMPNN is one of the main methodological contributions of the work, only the lower-Hölder stability of the two "baselines" ReluMPNN and SmoothMPNN as well as SortMPNN are analyzed in section 4. Ideally, an outline of a worst case analysis as mentioned at the end of section 4, or at least some justification if or why there is something inherently harder about the analysis of AdaptMPNN compared to ReluMPNN might be an insightful addition to the manuscript.

I am a bit puzzled about the results for the adaptive ReLU architectures: Both in Figure 2 and Figure 3, the corresponding architectures seem to be almost perfectly lower Lipschitz on the data, behaving similarly to the sorted architectures. If I am not mistaken, however, this is not guaranteed by the theory that is derived. I am assuming that this is not a consequence of the bound from Theorem 3.2 not being tight, since it is stated in lines 308-309 that the adaptive ReLU architecture for multisets is *not* lower Lipschitz in expectation, as can be shown by some adversarial graphs. However, I couldn't find any further justification for this statement in the manuscript, as Theorem 3.2 only shows that $(p+1)/p$-lower Hölder continuity in expectation (which evaluates to $\alpha=3/2$ for the $\ell^2$ case), while Theorem 3.1 only refers to standard ReLU summation. Could you maybe point me to a proof/justification or add one, and generally comment a bit more on the performance of the adaptive ReLU methods in Figure 2 and 3?

As also mentioned in the paper (lines 344-346), there are multiple WL distances that have been suggested so far. As expected lower-Hölderness also crucially depends on the chosen distance functions, is there any particular reason why you chose the TMD?

An interesting question would be to analyze more quantitatively how the expected Hölder stability evolves over training, as the theory is only laid out for the initial parameters (and depends crucially on the initialization distributions). While the results of Table 2 suggest that the stability is preserved during training, I would find more quantitative empirical results concerning the evolvement of the Hölder stability with the NN weights during training very interesting to see. However, as this is very open-ended and potentially costly, I would like to emphasize that this is merely as a suggestion.

### Questions
- Regarding the weaknesses: Are there any major difficulties in a Hölder stability analysis of AdaptMPNN compared to ReluMPNN? If so, a short paragraph explaining this might be interesting.
- I am a bit puzzled about the results for the adaptive ReLU architectures: Both in Figure 2 and Figure 3, the corresponding architectures seem to be almost perfectly lower Lipschitz on the data, behaving similarly to the sorted architectures. If I am not mistaken, however, this is not guaranteed by the theory that is derived. I am assuming that this is not a consequence of the bound from Theorem 3.2 not being tight, since it is stated in lines 308-309 that the adaptive ReLU architecture for multisets is *not* lower Lipschitz in expectation, as can be shown by some adversarial graphs. However, I couldn't find any further justification for this statement in the manuscript, as Theorem 3.2 only shows that $(p+1)/p$-lower Hölder continuity in expectation (which evaluates to $\alpha=3/2$ for the $\ell^2$ case), while Theorem 3.1 only refers to standard ReLU summation. Could you maybe point me to a proof/justification or add one, and generally comment a bit more on the performance of the adaptive ReLU methods in Figure 2 and 3?
- As also mentioned in the paper (lines 344-346), there are multiple WL distances that have been suggested so far. As expected lower-Hölderness also crucially depends on the chosen distance functions, is there any particular reason why you chose the TMD?
- An interesting question would be to analyze more quantitatively how the expected Hölder stability evolves over training, as the theory is only laid out for the initial parameters (and depends crucially on the initialization distributions). While the results of Table 2 suggest that the stability is preserved during training, I would find more quantitative empirical results concerning the evolvement of the Hölder stability with the NN weights during training very interesting to see. However, as this is very open-ended and potentially costly, I would like to emphasize that this is merely as a suggestion.

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
This paper proposed a pairwise separation quality analysis framework to study the Lipschitz and Hölder stability of functions on multisets and graphs. The authors proposed the notion of lower-Hölder in expectation (Definition 2.1), relaxing the uniform Hölder stability to the pairwise fashion. The authors showed that sum-based models on multisets and graphs are lower-Hölder in expectation with different exponents, depending on the activation choices (Table 1). Motivated from the theoretical analysis, the authors proposed AdaptMPNN and SortMPNN, which can separate the adversarial graph pairs and demonstrated improved empirical performance to existing MPNNs on standard benchmark datasets.

### Strengths
1. The study of separation power and stability of functions on multisets and graphs is of high interest to the community.

2. The proposed notion of lower-Hölder in expectation is interesting and can explain practical performance.

3. The proposed adversarial examples (i.e., $\pm \epsilon$-multisets, $\epsilon$-trees) are instructive and very useful to illustrative the theory.

### Weaknesses
1. The proposed SortMPNN deserves more remarks and discussion; see details in the Question section.

2. Empirical Comparison between AdaptMPNN, SortMPNN versus ReluMPNN and SmoothMPNN: While the authors compare these MPNN variants in Table 2 with the synthetic $\epsilon$-Tree dataset, the authors do not include the results of ReluMPNN and SmoothMPNN on the standard benchmark datasets (e.g. TUDataset, LRGB). Including such comparison could better bridge the theoretical insights in the paper to practice. Furthermore, the choice of only using a synthetic dataset for the comparison of MPNN variants limits the practical relevance of the empirical analysis. The paper would benefit from a more comprehensive evaluation on real-world datasets to validate the claims about the proposed models.



### Questions
1. The authors claimed that "SortMPNN is the first MPNN with both upper and lower Lipschitz guarantees" (Line 120-121). However, BLIS-Net proposed by Xu et al. [1] is shown to be Bi-Lipschitz with respect to a weighted inner product space. Can the authors compare and comment the differences?

2. Theorem 3.4 (SortMPNN is uniformly upper Lipschitz
and lower Lipschitz in expectation): This result seems straightforward given results in Balan et al. (2022). Can the authors discuss this more explicitly?

3. Connections between SortMPNNs and other related models: While sort-based aggregation function is rarely used in practice (and thus the novelty of the proposed SortMPNN), we can still see its "shades" in some related works. For example, in [2] the authors experimented with a sorting-based aggregation function; in [3] the authors proposed to learn a recursive aggregation function, which could in theory mimic a recursive sorting algorithm. Can the authors comment more of these related models?


References:

[1] Xu, Charles, et al. "BLIS-Net: Classifying and Analyzing Signals on Graphs." International Conference on Artificial Intelligence and Statistics. PMLR, 2024.


[2] Duvenaud, David K., et al. "Convolutional networks on graphs for learning molecular fingerprints." Advances in neural information processing systems 28 (2015).


[3] Ong, Euan, and Petar Veličković. "Learnable commutative monoids for graph neural networks." Learning on Graphs Conference. PMLR, 2022.

### Soundness
3

### Presentation
3

### Contribution
3

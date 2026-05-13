# Laplace-Transform-Filters render spectral Graph Neural Networks transferable

- Decision: Reject
- Scores: 3, 6, 3, 6, 5

## Abstract
We introduce a new point of view on transferability of graph neural networks based on the intrinsic notion of information diffusion within graphs. This notion is adapted to considering graphs to be similar if their overall rough structures are similar, while their fine-print articulation may differ. Transferability of graph neural networks is then considered between graphs that are similar from this novel perspective on transferability. After carefully analysing transferability of single filters, the transferability properties of entire networks are relegated to the transferability characteristics of the filters employed inside their convolutional blocks. A rigorous analysis establishes our main theoretical finding: Spectral convolutional networks are transferable between graphs whose overall rough structures align, if  their filters arise as Laplace transforms of certain generalized functions. Numerical experiments illustrate and validate the theoretical findings in practice.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper investigates transferability of graph filters and graph neural networks (GNNs) from a spectral perspective. The main conclusion of the paper is that graph filters and GNNs transfer if the frequency response of the filter can be written as a Laplace transform. I want to advocate in favor of this paper but to do so the authors must provide explanations of the following points:

(1) The use of Laplace transforms as frequency representations of graph filters appear in the work of Wang et al (https://arxiv.org/abs/2106.03725 and https://arxiv.org/abs/2305.18467). These papers conclude that transferability of graph filters and GNNs require conditions on a filter's spectral representation. I.e., not all filters transfer. Only those that have some specific spectral properties that affect their ability to discriminate some frequency components. This stands in contradiction to the claim in this paper that any filter that has a Laplace transform can transfer. The authors need to explain why this is not a contradiction.

(2) The work of Wang el al is related to the work of Levie et al and Ruiz et al that the authors cite. It is also related to the work of Zhou and Lerman (https://arxiv.org/abs/1804.00099) and the work of Gama et al (https://arxiv.org/abs/1806.08829 and https://arxiv.org/pdf/1905.04497) on stability properties of graph filters, GNNs, and graph scattering transforms. In all of these papers transferability and stability properties require restrictions on the spectral properties of graph filters. The statements in this paper seem to contradict this extensive literature. The authors need to explain why it doesn't. 

I have recommended that the paper be rejected (3). However, if the authors provide satisfactory responses to the questions above, I will change my recommendation to accept (8).

### Strengths
Problem formulation and results are interesting.

### Weaknesses
This paper investigates transferability of graph filters and graph neural networks (GNNs) from a spectral perspective. The main conclusion of the paper is that graph filters and GNNs transfer if the frequency response of the filter can be written as a Laplace transform. I want to advocate in favor of this paper but to do so the authors must provide explanations of the following points:

(1) The use of Laplace transforms as frequency representations of graph filters appear in the work of Wang et al (https://arxiv.org/abs/2106.03725 and https://arxiv.org/abs/2305.18467). These papers conclude that transferability of graph filters and GNNs require conditions on a filter's spectral representation. I.e., not all filters transfer. Only those that have some specific spectral properties that affect their ability to discriminate some frequency components. This stands in contradiction to the claim in this paper that any filter that has a Laplace transform can transfer. The authors need to explain why this is not a contradiction.

(2) The work of Wang el al is related to the work of Levie et al and Ruiz et al that the authors cite. It is also related to the work of Zhou and Lerman (https://arxiv.org/abs/1804.00099) and the work of Gama et al (https://arxiv.org/abs/1806.08829 and https://arxiv.org/pdf/1905.04497) on stability properties of graph filters, GNNs, and graph scattering transforms. In all of these papers transferability and stability properties require restrictions on the spectral properties of graph filters. The statements in this paper seem to contradict this extensive literature. The authors need to explain why it doesn't.

I have recommended that the paper be rejected (3). However, if the authors provide satisfactory responses to the questions above, I will change my recommendation to accept (8).

### Questions
Please clarify points (1) and (2).

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper discusses graph transferability. 

First, GNN transferability is defined based on **graph similarity**. The authors use a comparison between $K_N$ and Dumbbell graphs to introduce a diffusion-based similarity measure, which they extend to scenarios where graphs have different numbers of nodes. In such cases, graphs with different node sets are aligned using coarsening and interpolation.

Next, based on the similarity definition above, the authors discuss the **transferability of filters** on similar graphs. They find that general polynomial filters do not satisfy transferability, whereas Laplace Transform Filters (based on exponential basis functions or resolvent basis functions) do. 

Furthermore, they explore the **transferability of LTF-based networks** on both node-level and graph-level tasks.

In the experimental section, the authors validate their findings using graphs of different resolutions and graphs sampled from the same manifold.

### Strengths
1. The authors' writing is logically rigorous.
2. The authors propose a diffusion-based similarity measure and extend it to scenarios where graphs have different numbers of nodes.
3. The authors discuss the transferability of different filters on similar graphs, finding that LTFs and LTF-based networks exhibit transferability.

### Weaknesses
Please check questions.

### Questions
Regarding the experiments on different graphs sampled from the same manifold:

Considering the definition of Bidirectional Transferability and the motivating example, it seems natural that the experiments on graphs of different resolutions would be successful. Therefore, I am more interested in the experiments on different graphs sampled from the same manifold. However, it seems that the authors only conducted experiments on a pair of graphs on the Torus manifold, is that correct? 

Additionally, I would like to ask why the final comparison in this experiment is made using transferability error, rather than demonstrating the difference between network outputs before and after transfer?

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
5

### Summary
The paper introduces a methodology to show the transferability of GNNs based on the Laplace-Transform. The paper is relevant and the topic is important. The paper is very well written and easy to follow. The main issue with the paper is the lack of intuition that it derives given that it does not use a limit object, and therefore it has to introduce the directional similarity. Also, the bounds are asymptotic, and therefore cannot be compared with any existing method (graphons, graphops, etc). Finally, the experiment section is vague when stating high and low resolution instead of varying a numerical quantity.

### Strengths
1. The paper is relevant and the topic is important. 
2. The paper is well written.

### Weaknesses
I believe there are 3 issues with the paper: the asymptotic limit model, the bound, and the implications. 

Regarding the asymptotic model, the authors consider a graph that grows in the number of nodes (L) with no particular structure. This immediately removes any form of intuition or interpretation from the graph limit. It can essentially be anything. I believe this is a limitation in the results, given that the lack of structure makes the results less interpretable. The use of the graph Laplacian as the core object of analysis, without a clear connection to a limiting object with interpretable structure, makes it difficult to understand the practical implications of the theoretical results. The lack of a specific limiting structure, such as a graphon or a manifold limit, means that the results are too general to provide concrete insights into the behavior of GNNs on real-world graphs.

With respect to the bound, the authors do not provide a rate and simply show that it converges. This limitation makes the author's results difficult to compare with existing art, and therefore the question of how this result distinguishes itself from the existing literature becomes prominent. The absence of a convergence rate makes it impossible to assess the practical relevance of the theoretical results. Without a rate, it is unclear how quickly the transferability error decreases as the graphs become more similar, making it difficult to determine whether the proposed method is superior to existing approaches. I believe this paper is too general and therefore there are no implications for the practitioner. 

Finally, I believe that the numerical experiments show that the results presented are vague. The plots are divided into high and low resolutions, but this is not a mathematical quantity. The authors should modify a continuous quantity such as the number of nodes. The use of qualitative terms like 'high' and 'low' resolution, without a clear mathematical definition, makes the experimental results difficult to interpret and reproduce. It is unclear how these resolutions relate to the underlying graph structure or the number of nodes, and therefore the experiments do not provide a strong validation of the theoretical claims. The lack of a continuous parameter sweep, such as varying the number of nodes or the graph density, makes it difficult to assess the robustness of the proposed method.

### Questions
N/A.

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
3

### Summary
The paper looks at a spectral approach for graph learning and suggests to look at diffusion patterns to compare graph similarity. The main claim is that whenever the graph convolutions have a certain spectral form, the results automatically generalize (at least in the given theoretical setting). Then, these diffusion-based filters are implemented and transferability across data modalities (QM7 with and without H atoms) is demonstrated. The same is then done for different discretizations of a torus where again the spectral method (and none of the tested message-passing networks) achieves transferability.

### Strengths
The paper is well-written and easy to read, especially for a theory-heavy paper. The problem of transferability is relevant and the suggested diffusion-based distance and its use for graph learning seem novel and interesting (while the distance is prior work, it is not widely used). 

In general, the suggested LTF filters naturally handle local expansion and local transformation which is great for applications that rely on the global structure (even though most datasets are more about the local structure).

### Weaknesses
My main criticism has to do with the setting in which "transferability" is tested. See the questions below.

Further, I have a number of small points I would like to mention:
- 35ff: small changes may have a big effect on the desired label, e.g. when computing the parity function (but also in chemistry applications). It is (to me) not clear how this transferability should be happening. 
- 166: it would be nice to have a formal definition of J here. 
- 202: how to find this mapping? It would be nice to elaborate a little here. 
- 286: why 10^0 instead of 1?
- 307f: this sentence is hard to parse, especially the end after "importantly"
- 344: J^up J^down (not down, down)
- 376: QM7 contains small molecules only, this may have an effect on how much diversity is in there.
- 400ff: what are the features of the "coarse" nodes? What kind of information is still there?
- 412: is this result surprising in any way?

### Questions
Why would you expect a network trained on molecules without H to generalize to graphs containing H atoms? Which directly leads to the question: why would such a behavior be desirable? (its different for the torus, there the setting is clear)

The experiment where hydrogens are deflected out of their equilibrium position is also interesting: I would expect unstable atoms (i.e. the ones with deflected hydrogen) to behave quite differently from their "normal" counterparts, so why is the convergence of the suggested LTF models a good thing?
448: Does this mean that the distances are simply ignored in this experiment? And if yes, why would htat be a good idea?

How was the QM7 target chosen and why only this single target? Do the results generalize to QM9 too? (e.g. between the two datasets) And how about other targets?

How is "transferability" between dissimilar graphs avoided? And is this shown somewhere? (as its part of the conclusion)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the transferability of spectral GNNs based on diffusion over graphs. The transferability is discussed between graphs which are similar from the diffusion perspective.  The approach is to analyze the transferability of each single filter, giving rise to the findings that spectral GNNs are transferable if their filters are Laplace transforms of certain generalized functions.

### Strengths
The research question concerns the interesting topic of transferability of GNNs. 
The paper is well-written and the experiments are well-conducted.

### Weaknesses
1. The definition of similarity in the diffusion sense is rather limited and discussed in the context of graph coarsening. However, the important works on similarity of graphs in the context of graph coarsening have not been considered, i.e., the following
 two:

- Andreas Loukas, Graph reduction with spectral and cut guarantees, JMLR 2019.

- Andreas Loukas, Pierre Vandergheynst, Spectrally approximating large graphs with smaller graphs, ICLR 2018.

3. An obvious limit is that the class of filtering functions is limited to the class of
__low-pass__ filters, as shown by the examples 4.2 and 4.3, which are both typical examples of low-pass graph filters. This is in fact connected to the heat diffusion equation for the distance, as those will act as low pass filter. In this regard, the transferability may not hold in general setting, as spectral GNNs may learn also high-pass filters.

4. It seems the transeferability is discussed also in the context of graph coarsening. Is this general enough to discuss the transferability of GNNs? Please elaborate on this.

5. Two important works on transferability of GNNs are not well-discussed:

1. Convergence and Stability of Graph Convolutional Networks on Large Random Graphs

2. Graphon Neural Networks and the Transferability of Graph Neural Networks

For the second work, the author only mentioned it is limited to the (very) large graph setting. This is not true. The work in fact discussed a general setting that goes beyond the graph coarsening.

### Questions
<!-- 1. The similarity of graphs from the diffusion perspective. Is this really a novel perspective? -->

2. The fundamental reason why $\lVert L - \tilde{L} \rVert$ has pitfalls in measuring the similarity between two Laplacians comes from that the spectral norm is a poor measure. Sometimes, Frobenious norm, as the sum of the eigenvalues, might be a better
 measure, but still limited. Fundamentally, one could really compare how similar two graphs are by checking the full difference matrix $L-\tilde{L}$.

3. Different graphs in this paper have been only investigated in terms of one graph can be considered as the
_coarsened_ version of another. This is effectively the problem of graph coarsening. However, a similarity notion in the context of graph coarsening has already been rigoriously studied by

- Andreas Loukas, Graph reduction with spectral and cut guarantees, JMLR 2019.

- Andreas Loukas, Pierre Vandergheynst, Spectrally approximating large graphs with smaller graphs, ICLR 2018.

- the authors there defined the notion of 
__spectrally restricted similarity__ between graphs, so to ensure the spectral similarity when performing graph coarsening.

- I do not see the authors have considered this in their work. Please note that in the above two works, rigorous definitions of spectral similarity are provided, as well as extensive theoretical results.

4. The difference between two diffusion operators is in fact to utilize an extra dimension $t$ to measure the spectral difference  than simply using the spectral norm. However, it is still a limited measure of similarity. As $t$ increases, the
 diffusion flow is approaching to the harmonic eigenvector (space) of the Laplacian. Consider a setting where two completed different graphs (but both connected) with the same number of nodes. When $t$ is large enough $t\to\infty$, the proposed similarity measure
 is essentially zero, showing two graphs are similar. This is clearly not true. Of course, this is under the assumption that $t$ is large. I wonder if this is in fact the case of Figure 9, where different molecules are similar as $t$ increases.

Related to this, I feel in 3.1 the maximum eigenvalue of L should be below 1 to ensure the diffusion will converge, right? Typically a parameter is needed there to control it. If so, then what is dominating the diffusion is maximum eigenvalue. If the latter is small, graphs will be similar in this perspective, which again is not necessarily the case.

Having said that, the authors could consider checking the more general measure from the above two works.

1. In Section 4, it is briefly discussed that typical polynomial filters would diverge due to that the norm of $L$ on the graph $G$ tends to infinity (since $w_{high}^{min}\to\infty$). Could authors elaborate on this? The spectral norm of a graph Laplacian
 should be bounded, so I do not directly see this. Moreover, this seems to contradict the claim by
_Transferability of Spectral Graph Convolutional Neural Networks, JMLR 2019_.

### Soundness
2

### Presentation
3

### Contribution
2

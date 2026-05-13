# GRASP: Generating  Graphs  via Spectral Diffusion

- Decision: Accept
- Scores: 8, 8, 6, 3, 5

## Abstract
In this paper, we present GRASP, a novel graph generative model based on 1) the spectral decomposition of the graph Laplacian matrix and 2) a diffusion process. Specifically, we propose to use a denoising model to sample eigenvectors and eigenvalues from which we can reconstruct the graph Laplacian and adjacency matrix. Using the Laplacian spectrum allows us to naturally capture the structural characteristics of the graph and work directly in the node space while avoiding the quadratic complexity bottleneck that limits the applicability of other diffusion-based methods. This, in turn, is accomplished by truncating the spectrum, which, as we show in our experiments, results in a faster yet accurate generative process and by designing a novel transformer-based architecture linear in the number of nodes. Our permutation invariant model can also handle node features by concatenating them to the eigenvectors of each node. An extensive set of experiments on both synthetic and real-world graphs demonstrates the strengths of our model against state-of-the-art alternatives.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This article introduces a denoising diffusion model for generating graphs  which will look alike graphs of a training dataset. The parameters of the model are learned in a supervised way from a dataset of graphs, and the output is a Laplacian which can be converted to a graph. The model combines 2 elements in its architecture: a first step to learn the process of spectral diffusion (the diffusion mostly connect the eigenvectors and eigenvalues to the one after 1 time step of diffusion -- the model tries to learn the way back, ie. the reverse diffusion process) and a second step which predicts the graph (which an architecture of GNN, here a PPGN from Maron et al., 2019) to generate the Laplacian (and hence the graph). The idea is that the first step provides a noisy version of the Laplacian matrix (e.g., without orthogonality of the eigenvectors ; or with a reduced number of eigenvectors and eigenvalues) and that the second step helps to recover a correct Laplacian (hence graph). The first step, relying of the general idea of denoising some diffusion model to generate new samples (from the initial work of Sohl-Dickstein et al., 2015 and ho et al., 2020); for graphs, diffusions are operated on the set of eigenvectors and eigenvalues of the Laplacian which are considered (classically) as embedding of the graphs. 

The article combines ideas coming from other works (with many points inspired by the structure SPECTRE of Martinkus et al, 2022; or by DiGress from Vignac et al., 20222). Yet the present work comes with some novelties which are well explained. For instance, the diffusion is done on a limited number $k$ of pairs of eigenvectors and eigenvalues, to reduce the memory cost of the model ; the architecture of the neural networks of the 1st step (the learning of the reverse diffusion) is original (with attention heads from eigenvalues to eigenvectors and the converse way as well). The one for the 2nd step relies on existing previous work, yet it is shown in ablative studies that it works well and is needed for good performance.
These new elements are well integrated and explained. An evaluation is carried out on both synthetic datasets, and on real-world datasets of molecular graphs, and compared to 5 or 6 baselines (depending on the experiment), both with some metrics about the relevance of the general structure of the obtained graphs, and some inspections about validity, uniqueness and novelty of the generated graphs seen as molecules. An ablation study is conducted and some additional remarks are made (about orthogonality of the obtained eigenvectors, about the use of the method to generate graphs given a target spectrum for Laplacian, and about runtime (in appendix).

### Strengths
This a  quite good article, with a good presentation and interesting ideas.
For me, the strengths of the article are:

* The article is well written, which comprehensive explanations for the method and good presentations of the architecture, the numerical experiments, the ablation study and some inspections of features of the method in 6.3 and 6.4. 

* The method builds on previous works, yet it does not feel incremental but more like a thoughtful construction to improve on ESPRIT, DIGRess or other related works.

* The scope is relevant, because it is indeed difficult to build random models of graphs from a limited dataset of graphs to generate new relevant samples. (See however my remark 2 underneath).

* The ablation study is convincing in showing why the two steps are better than only one of the two. Also, there is an interesting discussion and experimental study to see how many pairs of eigenvectors/eigenvalues of $L$ are needed to build a graph and which ones (highest or lowest eigenvalues) are the most appropriate. This element can be explored more in future work and this is an original finding of this article.

### Weaknesses
Some weaknesses are:

* The scope is not large, and the work can be seen as somehow incremental. However, these increments are good enough for an article.

* Experimental validations in Section 6 are correct albeit limited due to a small number of datasets. For real-world datasets, it would be good to have examples which are not only related to molecules. Currently, the applications seem too specific. The focus on molecular graphs limits the generalizability of the findings. It would be beneficial to see how the method performs on other types of graphs, such as social networks or citation networks, which have different structural properties and may pose different challenges for graph generation.

* The baselines used are ok, yet many results are not computed anew and taken from the published articles. Given the modest number of examples, and the small number of baselines (6 at most), the authors could have tried to re-implement all of them for better control of the reproducibility of the baselines and comparison to the present work. This reliance on reported results introduces a potential source of variability and makes it difficult to ensure a completely fair comparison. It would be more rigorous to re-implement and evaluate all baselines using the same experimental setup and data splits.

* Performance is decent, yet not far above (or not above in some cases) the competitors. Some more lines should be devoted to understand why that, and what works better in some other works for some cases. The analysis of the performance differences is lacking. A more in-depth discussion is needed to understand why the proposed method does not consistently outperform the baselines, and what specific aspects of the baselines make them more effective in certain scenarios. This should include an analysis of the strengths and weaknesses of the proposed method in relation to the baselines, and a discussion of the conditions under which each method performs best.

### Questions
Here are some remarks and questions which can help to improve the work:

* 1) the name "GRASP" is already used by several previous work in domains related to the present one: "GRASP: Graph Alignment through Spectral Signatures" of J Hermanns et al., 2021  ; or the GraSP toolbox for Graph Signal Processing (popularized thanks to the A. Ortega's book which uses it). I advise the authors to adopt a different name.

* 2) The 2nd paragraph, p.1 l. 033-042 is not really true, and particularly naive: there are now tons of works to generate random models of graphs with a variety of properties (quoting the Albert and Barabasi model from >20 years ago don't make justice to what is done in the complex network, or network science, community). What is lacking, is most of the time is the precise knowledge of which feature has to be controlled and tuned to a dataset. The present approach which tunes a model to a specific dataset is relevant because of that.

* 3) p.2 l. 071: why should a generative model "assign equal probability to each of these n! adjacency matrices." ? There can be various ways of building probabilities for graphs and why permutation does matter that much ?

* 4) Section 4: I am not certain of the usefulness of that part. This is very basic things which would be incorporated in a part with notations (such a part is missing), and the properties recalled here should be recalled while introducing the work.

* 5) p4, eq. (4): this is the reverse diffusion step, right ?

* 6) Section 5: it would be clearer to have a subsection about step 1 (possibly including 5.1 as a paragraph), then a section about step 2, and maybe a last one about the loss function and how training is done. By the way, even if these questions of training and the two loss functions are inspired by ESPRIT, it would be worth to detail that more (using the space liberated by the removal of section 4).

* 7) Experimental validations in Section 6 is good albeit limited due to a small number of datasets. For real-world datasets, it would be good to have examples which are not only related to molecules. 

* 8) Performance themselves is decent, yet, as told above: Some more lines should be devoted to understand why that, and what works better in some other works for some cases.

* 9) in 6.2: why only a threshold of 0.5 is considered ? Given that real-world graphs are often sparse, one could expect a different natural  threshold to obtain desired sparsity.

* 10) In 6.3, are the authors sure of their remark of l. 459 : "...orthonormality..... (indeed, of the eigen-decomposition of any matrix" ? There are matrices with eigendecomposition and non-orthogonal eigenvectors. Your remark holds only for normal matrices.

Edit after revision and discussions: Rating set to 8: accept, good paper

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
4

### Summary
This paper considers the problem of realistic graph generation. The
proposed approach focuses on the spectral properties of the generated
graphs, that is, the eigenvectors and eigenvalues. Roughly speaking,
the method learns a diffusion denoiser that acts on the eigenvectors
and eigenvalues jointly, in a way that respects desired equivariance
properties of graph generative models. A key step in reducing the
complexity of this procedure is to restrict the diffusion model to a
small number of eigenvectors, allowing for a linear complexity with
respect to the size of the graph. This reduced representation is
accounted for using a graph neural network.

### Strengths
This paper is for the most part well-written and easy to
understand. Indeed, a strength of the proposed approach is that the
architecture is not too different from methods that are already
popular in the literature, so I envision practitioners and other
researchers having an easy time reimplementing this.

The experimental results seem quite good. I was particularly impressed
by the fact that GRASP was able to capture graph statistics well, even
though the method starts with spectral features. The experiments were
carefully selected to demonstrate various aspects of the model's
behavior, which provided insight into the problem beyond just claiming
"SOTA" -- indeed, most of the weaknesses that I was thinking of as I
read Sections 1-5 were addressed directly in Section 6. Bravo!

### Weaknesses
I did not find this paper to suffer from any glaring weaknesses, but I
do have one concern about the idea of using a small portion of the
spectrum to reconstruct the entire graph structure. As pointed out,
different parts of the spectrum correspond to different aspects of the
graph structure, that is, local vs. global features. Of course, this
is remarked upon as a limitation by the authors, but I would
appreciate some more discussion on the sorts of graphs that can be
generated in light of this.

Suppose we have a family of graphs that statistically vary in both
their global and local properties, in a way where those properties
(global vs. local) do not have strong correlations. I would imagine
that such a family of graphs could not be captured by merely choosing
to restrict generation to the lowest or highest set of eigenpairs. I
suspect that this concern points to a deeper question about spectral
graph theory than is within the scope of this paper, but I would still
be interested to hear from the authors what sorts of graphs they
expect the proposed method is able to capture.

For instance, SBMs are largely characterized by their global
structure, where the local connections follow an Erdos-Renyi pattern
-- thus, it makes sense to generate such graphs by focusing on the
lower spectrum. On the other hand, expander graphs are known to be
very sparse, while also exhibiting certain properties that are global
in nature -- such as being well-connected in some sense. It would be
helpful to have some experiments to see if such a class of graphs
could be generated by the proposed method.

### Questions
I would be interested to hear the authors' response to my main point in the weaknesses section: what sorts of graphs do you think the method, as it is presented in the paper, would have a hard time generating?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose a new algorithm for generating graphs based on spectral decomposition by using diffusion models for the resampling of eigenvectors and eigenvalues, which has been crucial in network analysis.

### Strengths
Using the Laplacian spectrum allows us to naturally capture the structural characteristics of the graph and work directly in the node space while avoiding the quadratic complexity bottleneck that limits the applicability of other diffusionbased methods.

### Weaknesses
1) The motivation of the method is not clear. Why replacing the GAN module could lead to better results?
2) How to choose non-zero eigenvalues $k$. See also my Q2.
3) Some figures are not clear.
4) The comparison to SPECTRE is not sufficiently detailed, particularly regarding the preservation of spectral properties. It is unclear why conditioning on the spectra in SPECTRE does not guarantee that these spectral properties are present in the generated graphs, while GRASP seems to achieve this. This needs more elaboration.
5) The choice of $k$ seems inconsistent across datasets, with QM9 using $k=2$ in SPECTRE and all eigenvalues in GRASP. The impact of this choice on performance and computational cost needs more discussion.
6) The 'average errors' in Figure 7 are not clearly defined, and it is unclear how they relate to the Degree, Cluster, and Spectral metrics mentioned in the caption.

### Questions
Q1: From my understanding, the authors replace the GAN module in the pipeline of SPECTRE with the diffusion model. Therefore, it would be better to highlight the difference of the two methods. For example in section 6.4, is there any explanation why GRASP works better in preserving the network community when conditional on the spectral than SPECTRE, since both methods are based on spectral decomposition? In addition, in SPECTRE it was mentioned that conditional on the spectra the performance (section 5.1 therein) can be boosted. How is the performance of GRASP in terms of MMD compared to SPECTRE?

Q2: For methods based on spectral decomposition, it is key to choose the number of non-zero eigenvalues k. I noticed that in SPECTRE relatively smaller k such as 2 and 4 can achieve good performance, while for GRASP large k's are needed. Specifically, for the dataset, QM9 SPECTRE only used k=2, while GRASP used all the eigenvalues.  How is the performance of GRASP compared to that of SPECTRE when the number of non-zero eigenvalues is the same? How will the number of non-zero eigenvalues affect the computational time? 

Q3: Could other fast sampling algorithms of diffusion models such as DEIS, DPM-Solver++, UniPC, and so on be leveraged to improve the quality or speed of GRASP?

Q4: Figure 8 is a bit confusing. The first two graphs in the right panel seem to be the same. Some explanations may help the readers to understand why k=12 for the community and k=64 for the SBM are compared. 

Q5. For Figure 7, it is unclear what the authors mean by ‘average errors’.  In the caption, it is said that Degree, Cluster, and Spectral metrics are calculated.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
An approach using spectral properties for efficient graph diffusion followed by a reconstruction module.

### Strengths
1. Spectral information is critical for graph topology, and leveraging it directly for diffusion is an interesting approach to explore.
2. The given ablations are interesting to read and follow.
3. The sampling speed is quick, unlike previous diffusion models.
4. My main concerns while reading the paper are mentioned in the conclusion as limitations, which is clear and closes some of my issues.

### Weaknesses
1. Experimentally, some key metrics are missing for synthetic datasets, namely the VUN for the planar and for the SBM dataset. I also have some concerns about the VUN metrics for QM9 since the uniqueness does not seem to be very high while the novelty is outstanding. Both metrics do not overlap totally but reflect the diversity of generation from different perspectives. Would the codes be released later (till my review the given anonymous repo is empty) for checking this technically?

2. The introduction / related work emphasizes a lot on traditional graph generation - which may not be the most critical or related work here. More background for the spectra-based method (SPECTRE is included but it would help if there are discussions with more relevant works) can help to clarify the storyline. Generally, the writing/clarity should be improved. Another branch of method that may be related to GRASP is the 'latent diffusion' for graphs - where people may encode a graph to node features, and, different from GRASP, they may denoise based on those learned features and reconstruct the graph based on it. This method in terms of structure is very similar, and the comparison of using learned graph features, and using spectral information directly is an interesting question to check or mention in the writing.

Writing: The paper adds more discussion on GSDM but doesn’t clearly explain how your method is different. GSDM seems very similar, and this distinction is necessary to discuss in the paper. Also, diffusion-based methods have advanced a lot (both in terms of formulation and performance) since DiGress, yet there’s no discussion neither results comparison over them. This makes it hard to see where your work fits in the broader context.

Performance: The results also remain unconvincing. On Planar/SBM, VUN scores might be the most important/well-established metrics, but they are 0.15/0.49, which is not strong enough, known that current diffusion/flow based method reach already 90%+. The results of other works also adds confusion: it shows DiGress VUN as 0.65(Planar dataset)/0.13(SBM dataset), while the original DiGress paper reports 0.75/0.74. For Spectre, the VUN score drops significantly from 0.48 to 0.14 on Planar. Given that at leaset planarity is trivial to verify with existing tools, this discrepancy is hard to justify with implementation. Both Spectre and DiGress have been validated by subsequent work, so their performance should be replicable. It’s surprising that the method struggles with basic graph properties like clustering and planarity, especially since it leverages graph-specific information.

### Questions
1. The number of eigenvalues and eigenvectors being used, and using either large or small ones seem to be critical for this method - since SBM, Planar, QM9 use very different settings. Would that require lots of tuning to find the proper one? Explanations about your choice of different graph datasets can be helpful for people not familiar with graph spectra.

2. I fail to understand the information in Table 4. What do the values in the Table represent?

3. Have you considered or experimented using other information besides graph spectrals for diffusion?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a graph generative model based on the denoising diffusion probabilistic model (DDPM). The diffusion process is performed on the graph spectral domain.

### Strengths
The work combines DDPM and graph spectral decomposition for the proposed generative model. An advantage is that complexity might be reduced as it is necessary to consider the entire graph spectrum. Numerical results demonstrate that the model is effective.

### Weaknesses
1. Though combining DDPM and graph spectral decomposition is new to me, there are already works that use DDPM to generate graphs  (e.g., DiGress) and works that use SDE diffusion on graph spectrum (e.g., GSDM). In my opinion, this paper is experimenting with a different combination of diffusion approach and signal domain, which can produce useful results but lacks significant novelty.
2. The model uses the graph eigendecomposition and performs diffusion on the eigenvectors and eigenvalues. However, it is well-known that eigendecomposition (of Laplacian) is highly unstable. I think the authors should theoretically address this issue. Specifically, small perturbations in the graph structure can lead to large changes in the eigenvalues and eigenvectors, which could make the diffusion process unreliable. The paper does not discuss the potential impact of this instability on the generative process.
3. Using a part of the spectrum has the advantage of reducing complexity. However, information is lost. What is the balance between these two factors? Is it true that most of the high-frequency components are not important? The paper needs to provide a more rigorous justification for truncating the spectrum beyond simply stating it reduces complexity. What are the theoretical implications of discarding these components, and how does it affect the quality of the generated graphs?
4. Is it possible for the diffusion process to generate eigenvectors and eigenvalues that cannot be obtained from the eigendecomposition of any graph? If so, what are the implications for the validity of the generated graphs? Does this lead to graphs that do not satisfy the basic properties of a valid graph Laplacian?
5. For some datasets (e.g., QM9), the proposed method does not seem to show a clear advantage with a few performance metrics, even though the entire graph spectrum is used. One may gain more insights if the authors can also show the results when a partial graph spectrum is used. This would help to understand if the full spectrum is indeed necessary for these datasets or if a truncated version could achieve similar results with lower computational cost.
6. How to choose $k$? Is there a principled approach? The paper lacks a clear methodology for selecting the number of eigenvectors to use. A more principled approach is needed, rather than relying on empirical observations.

### Questions
See "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
2

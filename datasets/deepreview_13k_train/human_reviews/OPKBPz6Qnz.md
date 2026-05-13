# A Spectral Framework for Assessing the Geodesic Distance Between Graphs

- Decision: Reject
- Scores: 3, 3, 3, 8, 5

## Abstract
This paper presents a spectral framework for quantifying the differentiation between graph data samples by introducing a novel metric named Graph Geodesic Distance (GGD). For two different graphs with the same number of nodes, our framework leverages a spectral graph matching procedure to find node correspondence so that the geodesic distance between them can be subsequently computed by solving a generalized eigenvalue problem associated with their Laplacian matrices. For graphs of different sizes, a resistance-based spectral graph coarsening scheme is introduced to reduce the size of the larger graph while preserving the original spectral properties. We show that the proposed GGD metric can effectively quantify dissimilarities between two graphs by encapsulating their differences in key structural (spectral) properties, such as effective resistances between nodes, cuts, the mixing time of random walks, etc. Through extensive experiments comparing with the state-of-the-art metrics, such as the latest Tree-Mover's Distance (TMD) metric, the proposed GGD metric shows significantly improved performance for graph classification and stability evaluation of GNNs, especially when only partial node features are available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The aim of the authors is to propose a Geodesic Distance (i.e. an spectral-oriented metric) between 
graphs. Then they commence by reviewing a couple of classical distances (edit distance and tree-movers) 
in order to fill their gaps: lack of globality (this is not well undestood: Edit distance is global but being 
aware of this globality is NP-hard) and attribute dependence. 

As a result, the classical Laplacian oriented approach emerges. The basic idea is that Laplacian matrices are 
not positive definite matrices (PD) but they can be transformed into them by modifying their diagonals. PD is 
a requirement to use a Geodesic Distance yet proposed into the literature (Lim et al 2019). 

When the graphs do not have the same number of nodes the largest graph is reduced via resistive approaches.

### Strengths
-Relate Geodesic Distances to GNN outputs. 
-Explain structural mismatches.

### Weaknesses
 - Lack of originality:

The distance proposed is yet introduced in 

"Geometric Distance Between Positive Definite
Matrices of Different Dimensions
Lek-Heng Lim , Rodolphe Sepulchre , Fellow, IEEE, and Ke Ye". 
The authors only modify the graph Laplacians to be Positive Definite.

### Questions
None.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this work, the authors introduce a new distance between graphs (denoted GGD). This distance differs from existing distances in that it makes use of the metric of positive definite matrices, in particular the Laplacians of graphs (after regularisation of the diagonal with the addition of $\eps Id$ to make it positive), to calculate a distance between two graphs with the same number of nodes. To do this, it is first needed to solve a correspondence problem between the nodes of the two graphs; the authors simply use the method of Fan et al. from 2020 (GRAMPA). When the graphs do not have the same size, the proposed method is to reduce the size of the larger one on spectral criteria (to keep the spectrum properties of the Laplacian of the reduced graph as close as possible to the spectrum of the initial graph). More precisely, the authors choose to compress the edges with the greatest effective resistance in the graph (which puts 2 nodes together) and thus create a coarsened graph that can be controlled to be of the   the same size as the graph to be compared. The pipeline of the method is therefore to: first reduce the largest graph to the size of the smallest, then align them using a spectral method, and finally calculate the distance as one of the geodesic distances of the (Riemannian) space of (regularised) Laplacian matrices, in this case the AIRM distance. 
The rest of the paper considers this distance, GGD, for the numerical study of GNN properties and whether GGD is a good metric to replace, for example, a GNN for graph classification. The performances reported are adequate. One specific point is that the method can be based on a partial view of the characteristics of the nodes, which brings substantial gains.

### Strengths
The article has some good points in its favour:

- the idea is not too complex, the method is feasible and the three steps are well documented in the article, with a sufficient level of explanations and details.

- on the dataset studied, performance is correct and computing times are slightly reduced as compared to state-of-the-art. Also, the scaling is in O(n^3) while previous solutions based on OT have an additional multiplicative log(n) term.

- the topic is useful, in that we have now a lot of articles on GNN, yet it is not always clear how each specific model behaves. The proposed distance appears to behave in a way similar to the output of the GNN called GIN, and gives then some idea about how to compare graphs.

### Weaknesses
Despite having some strengths, I find also many weak points in this work, and currently too many to recommend it for acceptation:

* The article does not answer well the following question: is it important to consider a proper Riemannian metric (once the steps of coarsening and alignement) are done ? What would change if one uses anyone of the spectral distances between graphs instead of the third step ?

* 4.3 is supposed to explore a part this question: "CONNECTION BETWEEN GGD AND GRAPH STRUCTURAL MISMATCHES", yet I am not certain to really understand the argument. The theorem provides bound on the generalized eigenvalues used in the distance, that I understand. However, as  it only impacts the extremal eigenvalues, I have uncertainties to whether it really always impact the full AIRM distance. The authors should state more specific elements on that.

* Some choices in the method can be considered as ad hoc, and not fully argument in the text. Examples :

. Why use a Riemannian distance in the third step and never consider this structure for the 2 other ingredients of the method: coarsening and alignement. 

. Why use the GRAMPA alignment and not other ones ? (there are several of them with OT, or without)  

. How are chosen the parameters ? The choice of $\eta$ for instance does not seem to be in coherence with Lemma 4.1  (1/log n is around 1/3 for graphs with n=20 nodes, like in MUTAG dataset; I don't see why, in A.9, this leads to \eta = 0.5 in the present work). 

. Is the proposed coarsening method the best one for the task at hand ? One would have expected something based on the proposed Riemannian approach, no ? Or the use of some already well known coarsening methods (the authors quoted many themselves). Why a new one is needed ? 

. The combination of effective resistance and features seems to be completely empirical  (eq. (15)), and should be justified, at least by giving some insights about how it behaves.

* One lacks a summary of the proposed method, in form of a detailed algorithm or a pipeline.

* The numerical examples are too specific: there are not enough datasets tested (4 only) and the graphs in these datasets are always small graphs (average numbers of nodes from 18 to 47) and they correspond to molecules. All that is very specific and somehow it limits in the scope of the work to graphs representing molecules.  

* On such small datasets, a separation between train / test / validate data should be expected (here, only train / test is mentioned).

* Many paragraphs of the Appendices are in fact not useful, as they cover well known things. This inflates the article without any valid reason. (See the suggestions underneath)

* Section 3 repeats many things that were already written either in the introduction or that will be presented in greater details in Section 4. I am not certain that it's the best way to present the work.

### Questions
* In eq. (14), why are the features put there ? They should only be in (15), shouldn't they ?

* Suggestion: re-write the article to split 3 between the introduction and the Section 4 so as to avoid redundancy.

* Why are std reported for MUTAG in Table 3 and not systematically for other datasets ? Also, check How many significant digits are there, so as to report the numbers correctly in the table.

* Suggestions for the Appendices:

. My feeling is that elements in A.1, A.3 and A.8 do not really add useful elements ; either it's common knowledge (A.1), unrequired additional comments (A.3) which could be in 5.1 (for the references). 

. Then, on the Riemannian aspects (Riemannian  being mispelled in title of A.2): A.2 is to short to introduce what it means to a reader not knowing that, hence its not useful for anyone ; A.4 is not needed as everything comes from the fact that AIRM is a distance. Then, the rest follows without any surprise. 

. I question also the usefulness of A.7: given that the article does not go far in the direction of Riemannian space, telling that AIRM is the metric of choice seems to be enough (it would be more interesting if the authors would compare various distance using spectral features, and not only two from Riemannian geometry).

. Then, the rest of the appendices are useful.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes new metrics to measure two different graphs (GGD) and apply them to graph neural networks.
The GGD exploits the spectral features of two graphs if the size of the two graphs is the same. If sizes are different, GGD exploits resistance.
This paper conducts experiments to confirm that the proposed method is more effective than the other existing measures.

### Strengths
The GGD empirically outperforms the existing measures.

### Weaknesses
The proof for GGD as a distance metric is incomplete. Would GGD give zero for the same graphs but two different adjacency matrices? The proof seems to assume that "phase 1" is already done, but would "phase 1" give the same modified matrix for two different matrices? This is not about making a fuss over details; this paper needs to provide more careful theoretical analyses than the current state by giving examples.

Section 4.3, where the authors discuss the connection between GGD and the cut, is rather weak. How does it support the GGD? How does the bound of the cut ratio relate to the quality of measure of the two graphs? From the current state, these are very unclear.

It is unclear The role of the modified Laplacian matrix; I speculate that this is to obtain the inverse of the graph Laplacian, but it seems that the pseudoinverse of Laplacian is enough. Can you please explain the role of the role of modification, especially the advantage over the pseudoinverse of the graph Laplacian?

### Questions
Connected to the first weakness point, if the resistances are the same, are the two graphs the same? If not, you may have a disadvantage for such cases if you employ the resistance.

Why do you use the approximated method for the resistance-based one? If two graphs are the same, the authors use all of the eigenvectors. The resistance costs almost the same as obtaining the full eigenvectors, but for this case, the authors approximate the resistance. Why?

Suggestion: Consider sorting all the proposed steps in the algorithm environment.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new graph distance known as GGD, which relies on a Laplacian based geodesic distance. In the case of comparing same dimensional matrices, an eigenvalue problem setup is adopted. In the case of comparing matrices of different dimensions, a effective resistance based coarsening scheme is adopted. The authors show theoretical properties (the distance capturing structural properties) and conducted experiments comparing with other distances.

### Strengths
originality: the proposed approach is, to the best of my knowledge, original. 
quality: the quality of the exposition is good. The mathematical derivations (I have not checked proofs in supplement line by line) are, to my best understanding, reasonable and sound. The motivation is provided, and ample experiments/comparisons are made. Theoretical statements are relevant to the bigger picture. 
clarity: the paper is written and presented clearly. 
significance: the problem of graph metric development and graph comparison is significant, and the authors' contribution is original and considerable.

### Weaknesses
Overall, I believe the paper is written well and the contributions are sound and original. 

- while the method is developed for general metric between graphs/matrices of different dimensions, the analysis in 4.3 only consider the case of same node set with known correspondence. The general case is not considered. Is there an analogous result for the general case with different dimensions, or with node features? The statement in the introduction/abstract makes it sound like the authors have section 4.3 type structural interpretation results for general case...if no such results are available, then the wording/claim should be specified/scaled down in the intro/abstract to reflect this more accurately.

- It is unclear whether the assumption in lemma 4.2 of null(L_2) \subseteq null(L_1) is a satisfiable assumption for general graphs in practice...it seems like a very strong assumption (beyond the trivial case that the constant vector is in the null space of laplacians for connected graphs...is this what the authors are trying to get at? ) Can the authors provide examples of common graph types where this assumption holds beyond the trivial case of connected graphs? How restrictive is this assumption in practice, and how does it impact the applicability of the method to real-world graphs?

### Questions
I state my questions below: 

The authors introduce a very general framework for comparing graphs. I do not understand why they frame the abstract and the entire motivation of their paper around graph neural networks (as important as this application might be)...indeed, graph neural networks only enter as an application in the last sections of the paper...I find this emphasis in the abstract confusing. Consider revising the title and abstract to better reflect the general nature of the graph comparison framework and to more accurately represent the broader contributions of the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new graph metric based on the geodesic distance between Laplacians on the manifold of positive definite symmetric matrices. The metric is used for tasks such as graph classification.

### Strengths
1. The metric introduced is demonstrated (Fig. 1 and Tab. 1) to be more powerful in capturing graph dissimilarities.  
2. The authors have applied the metric to graph learning and showed its effectiveness.

### Weaknesses
1. My main concern is that the metric is not first introduced by the authors. It has been defined and thoroughly studied in [a]. Therefore, in this respect, the work is not considered novel and I don't think the contribution is enough for ICLR. However, some tricks introduced can be useful in practice. 
2. Is it possible to incorporate a GGD-based SVC classifier with a GNN model?
3. The benchmarks (Tab. 2) are not recent.

### Questions
Please see "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
2

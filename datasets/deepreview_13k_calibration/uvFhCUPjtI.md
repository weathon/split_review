# Beyond Spatio-Temporal Representations: Evolving Fourier Transform for Temporal Graphs

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
We present the Evolving Graph Fourier Transform (\emph{EFT}), the first invertible spectral transform that captures evolving representations on temporal graphs. 
We motivate our work by the inadequacy of existing methods for capturing the evolving graph spectra, which are also computationally expensive due to the temporal aspect along with the graph vertex domain.
We view the problem as an optimization over the Laplacian of the continuous time dynamic graph. Additionally, we propose pseudo-spectrum relaxations that decompose the transformation process, making it highly computationally efficient. 
The \eft method adeptly captures the evolving graph's structural and positional properties, making it effective for downstream tasks on evolving graphs. Hence, as a reference implementation, we develop a simple neural model induced with \eft for capturing evolving graph spectra. 
We empirically validate our theoretical findings
on a number of large-scale and standard temporal graph benchmarks and demonstrate that our model
achieves state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes an invertible spectral transform that captures evolving representations on temporal graphs. EFT is built upon the approximation of the exact solution to the variational form. They provide theoretical bounds of the difference between EFT and the exact solution to the variational form. Their experiments show that EFT effectively filter out the noise signals and enhance task performance against the baselines.

### Strengths
The strengths of this work are summarized as follows:

(1) The idea of evolving graph Fourier transform is interesting, which provides an alternative way of extracting the information within spatial temporal graphs.

(2) The theoretical properties are analyzed with provable guarantees on the approximation properties of EFT.

(3) The benchmarks comparing this method with the baselines look promising.

### Weaknesses
The weakness of this work are summarized as follows:

(1) Despite giving guarantees on the approximation part, this work does not address the theoretical guarantees of learning under this module. Hence this makes this work more like heuristic. The reviewer believes that this might be quite difficult though.

(2) The font size of the tables should be improved. This makes it hard to read. The reviewer suggests reducing presentation on the properties of EFT in proposition 5.1 to make up for the space and delay the properties of this transform to the appendix instead.

### Questions
The question is how is the complexity of computing this transform. The reviewer did not see how fast it can be computed compared with other baselines and would like to see if it can be efficiently computed empirically.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method called evolving Fourier transform (EFT) for spectral analysis of dynamic graphs that is formulated as an optimization problem over the Laplacian of the continuous time dynamic graph. At implementation level it performs vertex domain filtering via Chebyshev polynomial approximation of graph filters followed by a classical time domain filtering via Fourier transform. Although the experiments are limited but the method is novel. The paper is dense and difficult to read at times. It is a novel work but could have been presented in a more elaborated way by providing more examples, intuitions, connections to FT and GFT via examples.

### Strengths
Although the experiments are limited, the method is novel.

### Weaknesses
The paper is dense and difficult to read at times. It is a novel work but could have been presented in a more elaborated way by providing more examples, intuitions, connections to FT and GFT via examples.

A table or example for clarifying the notations will significantly improve the readability. Please provide explanations/intuitions of all the terms in Equation (4) when the EFT is defined first. 

The coupling of filtering in vertex and time domains is explained in Appendix C.2 which should be moved to the main text. 

The paper does not state its limitations, for example non-applicability to dynamic graphs with node addition or node drops.

Graph signal variation equations can be displayed with number since it the the basic term used in further analysis.

### Questions
It would help the readers if more insights are given in terms of small toy examples. What will be harmonics for ring of ring graphs (no edge addition or dropping over time)? Does this have some relation to classical Fourier transform?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper designed a new form of (approximated) Fourier Transform to analyze spatio-temporal graph signals with low computational complexity. The gist of the proposed approach lies in the decomposition of the spatial/graph domain and the temporal domain, reducing the computational complexity from $O((NT)^3)$ (performing GFT/SVD over the entire spatio-temporal domain) to $O(N^3T + NT \log(T))$. Furthermore, the proposed transform was shown to be robust to structural perturbations, and comprehensive simulations verified the utility of the transform when combined with some vanilla transformer models to perform link prediction tasks.

### Strengths
Just like in classical signal processing, it is not surprising that denoising and then reconstructing (predicting) the signal from the spectral domain can be much easier than dealing with the spatio-temporal signal directly. However, performing GFT over the entire spatio-temporal graph is typically computationally expensive, which hinders the spectrum analysis of spatio-temporal signals. This paper provided solid theoretical guarantees for using Evolving Graph Fourier Transform (EFT: DFT+GFT in order) to approximate the absolute decomposition (AD) with reasonably low approximation error. Standard properties of the transform are established in section 5.1 as well. For the simulations, it is also very interesting to see that EFT can be used within transformer models to perform sequential link prediction tasks in practice.

### Weaknesses
The idea of decoupling spatial and temporal domains in spatio-temporal data analysis is actually not new, especially for the spatio-temporal graph neural networks (ST-GCN) community. As a matter of fact, most existing ST-GCN models, no matter their design come from empirical perspectives [1, 2, 3] or theoretical perspectives [4, 5], all share the idea of graph-time decoupling to reduce the computational complexity. However, only a handful of prior works on ST-GCNs have been mentioned and discussed in the paper. I understand that the authors are considering graphs that change with time, for which most ST-GCNs are not directly applicable as they deal with static graphs, but I still believe related discussions should be added so that the readers are clearer about the contribution of this paper. Furthermore, the complexity of the proposed approach seems quite similar to those in [5]. The authors may also want to have some comments on that as well.

In addition, for the approximation of EFT to work, two extra assumptions are needed in place: 1) The rate of change of the graph with time is bounded; 2) The eigenvalues of the graph Laplacian at any given timestep and between timesteps have a multiplicity of 1. I think it is better to state these assumptions in the main text instead of the appendix to help the readers better understand the limit of the approach, as the assumptions are quite important (and intuitive) for the EFT to work.

### Questions
1. In addition to the Fourier Transform, there appears to be research interests in performing spectral clustering for dynamic networks as well [6, 7]. Since node clustering can also be used to predict missing links, what advantages and disadvantages do you think EFT will have compared to spectral clustering?

2. Just curious, beyond link prediction, what changes would we need if we also want to predict node features?

[6] Liu, Fuchen, et al. "Global spectral clustering in dynamic networks." Proceedings of the National Academy of Sciences 115.5 (2018): 927-932.

[7] Martin, Lionel, Andreas Loukas, and Pierre Vandergheynst. "Fast approximate spectral clustering for dynamic networks." International Conference on Machine Learning. PMLR, 2018.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new approach, EFT, to transform temporal graphs into the frequency domain, which can capture spectra of evolving graph structures. EFT provides solid theoretical proof of utilizing the Laplacian of the continuous time dynamic graph and pseudo-spectrum relaxations to decrease the computation cost. The downstream experiments on large-scale and standard dynamic graph datasets demonstrate the superior performance and efficiency of the proposed model.

### Strengths
1. This work proposed EFT to transform the evolving temporal graphs into the spectral domain, grounded on theoretical foundations. The EFT is very effective with the computational complexity of O(T+Tlog(T)).
2. The experiments in simulating scenarios clearly demonstrate that EFT is effective in filtering noise and amplifying useful signals in evolving temporal graphs.
3. EFT is of good interpretability; it can decompose the transform into the individual transforms of each domain to give clear relations from both the time and vertex domains.

### Weaknesses
The generalization of the proposed method needs to be clarified further. Even considering Theorem 1, the proposed method depends on the approximate \Psi_{AD}, the eigendecomposition of L_{J_d}. It is unclear whether any limitations associated with this will be introduced. Specifically, the reliance on an approximate eigendecomposition raises concerns about the stability and accuracy of the spectral transform, especially when dealing with large-scale graphs where exact eigendecomposition is computationally infeasible. The method's sensitivity to the approximation quality of \Psi_{AD} and how this impacts the downstream tasks needs further investigation. Furthermore, the method's applicability to different types of dynamic graphs, such as those with rapidly changing structures or those with non-uniform temporal sampling, is not fully explored. It is unclear if the proposed method can effectively capture the spectral characteristics of such graphs.

### Questions
1. The timespan of edges is a natural attribute of a temporal graph. Some recurrent works [1] [2] show that embedding the timespan of edges is important, especially in the sequential recommendation. I am wondering whether EFT could embed the timespan of edges and how. Such discussion may help the audience have better ideas on applying or extending EFT in solving their own problems in different application domains.
[1] Time-aware Dynamic Graph Embedding for Asynchronous Structural Evolution, TKDE'23.
[2] Time lag aware sequential recommendation, CIKM'22
2. In section 5.1, ”However, the same holds true for higher dimensions as well by conducting the EFT dimension-wise.” What does the dimension-wise mean?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

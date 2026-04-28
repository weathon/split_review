# Regularized Optimal Transport for Single-Cell Temporal Trajectory Analysis

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
The temporal relationship between different cellular states and lineages is only partially understood and has major significance for cell differentiation and cancer progression. However, two pain points persist and limit learning-based solutions: ($a$) lack of real datasets and standardized benchmark for early cell developments; ($b$) the complicated transcriptional data fail classic temporal analyses. We integrate $\texttt{Mouse-RGC}$, a large-scale mouse retinal ganglion cell dataset with annotations for $9$ time stages and $30,000$ gene expressions. Existing approaches show a limited generalization of our datasets. To tackle the modeling bottleneck, we then translate this fundamental biology problem into a machine learning formulation, $\textit{i.e.}$, $\textit{temporal trajectory analysis}$. An innovative regularized optimal transport algorithm, $\texttt{TAROT}$, is proposed to fill in the research gap, consisting of ($1$) customized masked autoencoder to extract high-quality cell representations; ($2$) cost function regularization through biology priors for distribution transports; ($3$) continuous temporal trajectory optimization based on discrete matched time stages. Extensive empirical investigations demonstrate that our framework produces superior cell lineages and pseudotime, compared to existing approaches on $\texttt{Mouse-RGC}$ and another two public benchmarks. Moreover, $\texttt{TAROT}$ is capable of identifying biologically meaningful gene sets along with the developmental trajectory, and its simulated gene knockout results echo the findings in physical wet lab validation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new method, TAROT, to address the challenge of temporal trajectory analysis in scRNA-seq data. It introduces a new dataset, Mouse-RGC, consisting of 30K mouse retinal ganglion cells across 9 developmental stages. The core of the method is regularized optimal transport (OT) which integrates biological priors to map cell states across time points. TAROT utilizes a masked autoencoder to learn cell embedding representations, and generates continuous trajectories using B-Splines. Experiments demonstrate TAROT’s performance compared to existing methods on multiple benchmarks, and the authors also simulate gene knockout experiments to validate the biological relevance of the model’s findings.

### Strengths
**Originality** : The paper proposes an integrated temporal trajectory analysis method that combines different components—cell representation learning, trajectory inference, and continuous trajectory generation. And It also introduce a new dataset can be used in other benchmarking work.

**Quality**: The paper includes a set of biological analyses, including gene knockout simulations and pathway alignments, which may provide some biological meaningful insights. And the ablation studies were also conducted.

**Clarity** : The paper is well-organized and easy to follow.

**Significance**: Temporal trajectory analysis is important in single-cell biology.

### Weaknesses
Despite the strengths discussed above, there still exists some concerns:

- **Methodological novelty** :   Although the paper presents a unified framework, the components of this framework—such as cell representation learning via masked autoencoders, regularized OT for trajectory inference, and the use of splines for continuous trajectory generation—are not novel. Each of these techniques has been explored in previous works (e.g., WaddingOT [1], Moscot [2], Slingshot, Monocle). The combination of these existing methods may come across as a straightforward integration. The paper may need to further address how this combination leads to new insights or capabilities that were not achievable with existing techniques, with more systematic benchmarkings.

- **Limited to Cluster-Level Resolution**: This paper produces continuous trajectories at the cluster level rather than achieving single-cell resolution. Recent advancements, particularly in dynamic optimal transport, can directly generate continuous single-cell trajectories, and simulation-free approaches such as conditional flow matching (see [3,4,5]) can scale to high-dimensional gene spaces. The paper may need to adequately compare TAROT against these more recent methods and explain the advantages TAROT provides over approaches that can inherently handle single-cell granularity.

- **Generalization**: While the authors demonstrate TAROT’s effectiveness on Mouse-RGC, the paper does not provide sufficient discussion on the generalizability of the approach. For example on cross-dataset beyond Mouse-RGC,  whether the framework is broadly applicable or tailored to a specific type of data. In the abstract , it is stated that "....Existing approaches show a limited generalization of our datasets*". The readers may naturally question what is the performance of TAROT on other datasets where existing methods demonstrated good performance.

- **Cell Division and Death:**   The current framework does not consider cell division or death (e.g., Moscot), which is crucial in biological processes that affect trajectory inference.

- **Data Availability:** The data availability statements seemed not found. 

Based on the discussions above, I suggest the work could be further revised substantially, and I would be very happy to  increase the score if the concerns are adequately addressed by the authors.

[1] Schiebinger, Geoffrey, et al. "Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming." [2] Klein, Dominik, et al. "Mapping cells through time and space with moscot."  [3]  Tong, Alexander, et al. "Simulation-free schrödinger bridges via score and flow matching."  [4] Lipman, Yaron, et al. "Flow matching for generative modeling." [5] Tong, Alexander, et al. "Improving and generalizing flow-based generative models with minibatch optimal transport."

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper suggests a novel framework for trajectory inference in single-cell datasets, $\texttt{TAROT}$ which comprises three main steps; (a) obtaining cell representations via a masked autoencoder, (b) mapping cells via regularized optimal transport (infomed of biological priors), and (c) inferring a continuous trajectory. To showcase the framework’s performance the authors generated a large-scale integrated mouse retinal ganglion cell dataset, $\texttt{Mouse-RGC}$. Evaluation over $\texttt{Mouse-RGC}$ alongside two other publicly available single-cell datasets is provided.

### Strengths
- *Contribution*: The paper suggest a joint approach for the trajectory inference task, combining data representation, mapping between time points, and continuous trajectory inference. 
- *Quality & clarity*: The paper is well written presenting high quality work--required background is provided followed by in depth model description, and diverse analysis providing both quantitative comparison as well as biological validations.
- *Significance*: The suggested framework addresses a challenging task in the single cell field–inferring the continuous dynamics–stemming from the destructive nature of experimental protocols.

### Weaknesses
- *Limited novelty*: $\texttt{TAROT}$ is presented as a novel framework however all three components have been previously suggested for single cell data analysis. Specifically, both WOT (Schiebinger et al. 2019) and moscot (Klein et al., 2023) utilize OT for single cell trajectory analysis, rely on lower dimensional representations for the mapping, and allow incorporation of biological priors via the source and marginal distributions as well as un-balanced mapping. Of note, while the authors relate to these as "preliminary" works they are well accepted and used by the community (e.g. WOT has ~770 citations and moscot's github has ~100 stars).
- *Reliance on cell clustering*: As remarked by the authors (in Appendix C.3), cell clustering is a critical step in data preprocessing for $\texttt{TAROT}$ application. This can be a limitation when reliable clusters are unavailable and generating them may require "experience of biology scientists" (as used by the authors for the $\texttt{Mouse-RGC}$ data, Sec. 3.2). The ablations show that clustering quality as well is simply removing the cost results in poor performance, it will be valuable to relate to this limitation.
- *Performance assessment*: Qualitative results rely on metrics which are designed to validate the developmental and functional priors induced by $\texttt{TAROT}$. Though gene patterns assessment rely on genes not included in the prior,  $\texttt{TAROT}$ has a clear advantage in these tasks, as it is designed to capture these patterns. Next, the biological contribution is presented only for $\texttt{TAROT}$ (Figure 7) and knockout analysis, whereas it may be that other methods capture the same trends, or compared to least performing method (Figure 8).
- *Data availability*: The  curation of  $\texttt{Mouse-RGC}$ is presented by the authors as a major contribution however the data is not made available.

### Questions
Questions are in light of the presented weaknesses; Can the authors:

(i) clarify of the exact novelty of the framework; \
(ii) present further/more proper evaluation to justify (i); \
(iii) relate to the dependency on cell clustering; \
(iv) provide details on the setting used for the baseline methods (choices of parameters, cost construction etc.); \
(v) make the $\texttt{Mouse-RGC}$ dataset available for the community.

### Soundness
2

### Presentation
3

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
The authors introduce Tarot, a regularized optimal transport model for learning cellular lineages in developmental data. Tarot utilises time-resolved RNA-seq gene expression data to learn how cellular lineages unroll in time. More specifically, the model relies on unpaired snapshots of single cells collected in time, which are matched with each other using optimal transport, since RNA-seq does not allow sequencing of the same cell multiple times across samples. The first component of Tarot is a masked autoencoder, used to project normalised gene expression to a lower dimensional embedding space. The masked autoencoder is trained to reconstruct randomly masked regions of the input gene space with a mean squared error (MSE) loss. Once trained, the bottleneck representations are used to train a regularised optimal transport algorithm to match clusters of cells across times and reconstruct developmental lineages. The OT approach is regularised to prevent backward mapping in time and ensure the preservation of the ground-truth monotonic behaviour of key lineage genes. Finally, continuous trajectories are learnt as B-splines on the cluster representations. The authors demonstrate improvement over three baselines based on lineage reconstruction and gene pattern preservation. They also validate the model biologically on its ability to recapitulate gene expression dynamics across developmental time and the effect of perturbation on the cellular trajectory. Together with a technical contribution, the authors release an integrated dataset of 30k mouse neuronal cells.

### Strengths
I think the paper has a clear biological reasoning at its foundations, which I appreciate and tends to be suboptimal in the context of machine learning conferences. I also value the effort of collecting, curating and integrating a whole new dataset, which I am sure will create value in the community. Structure-wise, I liked the schematic way both contributions and metrics were presented, it made the paper easier to follow. I also enjoyed the visuals quite a lot, you can tell that the authors spent time on them and I found them very convincing. The reading was enjoyable. Finally, I really like the idea of informing OT with proper biological choices. I think reasoning towards more biologically informed optimal transport rather than blindly applying Euclidean costs is important for future developments in the field.

### Weaknesses
Major

* Although I believe the authors when they claim good representation performance of their autoencoder, I feel claiming its “superiority” is rather unsupported. Probably it is a mischoice in the terminology, but there is no proper benchmark demonstrating in what way the masked autoencoder is better than traditional approaches (e.g. scVI [1]) for the proposed task. Also, masked autoencoders for single-cell have now been proposed in multiple settings, which makes their use a nice asset, but a source of novelty. I think the work would benefit from proof of the reported superiority in the representation, or, conversely, the authors may want to tone the representation aspect a little bit in the presentation.
* In my opinion, referring to the task of “recasting learning trajectories” as a machine learning problem overlooks the fact that ML for trajectory inference is now a standard in the computational biology field. I would rather phrase the contribution as an additional method in this direction. This shortcoming is reflected in the Related Works section, where only traditional methods (not based on deep learning) are discussed. I think such a section would benefit from an update including how machine learning has already been applied to OT for single-cell trajectory inference. 
* I wonder why Mouse-IEP was not included in the benchmarks comparing Tarot with existing models.
* Though I generally value attention to biology, I believe the biological details on page 4 may be shortened a little bit (and integrated with details in the appendix) to dedicate more time to the methods part, as some aspects (like the masked autoencoder part) felt a bit rushed. 
* In my opinion, one of the major drawbacks of the method is the operation at the cluster level. I see the benefit of such an approach on the dataset at hand since Figure 1 demonstrates low variability within clusters. Nevertheless, some datasets display larger heterogeneity per biological cluster [4], which would make the representation choice suboptimal. I think acceptance at ICLR would require a more comprehensive dataset choice, including more challenging settings (e.g. the MEF dataset in [5]). The authors claim that individual cellular representations are also an option, but no evidence was provided in these regards, so I cannot validate the claim properly. 
* Though I see the value of the way the authors perform continuous trajectory learning, other methods have been released based on dynamic optimal transport that learns continuous vector fields (and so interpolations). An example is the standard OT conditional flow matching [6]. The lack of a comparison to such methods should be discussed. Comparison with at least a couple of them would be very beneficial for the contribution. 
* I wonder if limiting the evaluation of GPT-G and GPT-L to monotonically varying genes is comprehensive enough. In other more complex datasets, this would potentially impair modelling more complex regulatory processes. It would be useful for the authors to elaborate more on this. 
* In my opinion, the paper lacks a little bit of elaboration on some aspects of the experimental process. How did you run the several methods to make them compliant with the setting you propose? Did you simply run them on averaged cluster representations? Were other adjustments needed?
* In my opinion, the way the GSEA analysis is presented is a bit unclear and the biological value of the finding is not discussed. It would be beneficial to at least disclose the GO terms in the main text and explain why they make sense in the considered system. 
* The change in trajectory between the perturbed and unperturbed states in Figure 9 is not discussed in terms of biological relevance. Are the changes in cluster transitions biologically relevant? 
* I think the last result on real-world experiments would have benefitted from some visualisation or table.

Minor

- The authors refer to cells with the term “gene expressions”. In my opinion, it would be more appropriate and readable to address them as “sequenced cells” or “gene expression profiles of n cells”. The way it is phrased now may be confused with the concept of “number of genes”.
- “Specifically, the number of nearest neighbors was chosen to be 50, according to the rich experiences of biology scientists”. I would personally remove this sentence unless supported by a solid citation. Packages like scanpy use a default lower number of neighbours and that seems to work properly. It is fine if more neighbours worked better for the datasets in this study, but I would phrase this sentence in this direction.
- I would make sure indexes are not bolded in the notations (e.g. line 245). 

As of know, I unfortunately believe that the reasons to reject the current version of the paper outweigh the reasons to accept it. But I am happy to discuss the author’s views on my comments.


[1] Lopez, Romain, et al. "Deep generative modeling for single-cell transcriptomics." Nature methods 15.12 (2018): 1053-1058.

[2] Fang, Zhaoyu, Ruiqing Zheng, and Min Li. "scMAE: a masked autoencoder for single-cell RNA-seq clustering." Bioinformatics 40.1 (2024): btae020.

[3] Kim, Jaesik, et al. "Single-cell Masked Autoencoder: An Accurate and Interpretable Automated Immunophenotyper." NeurIPS 2023 AI for Science Workshop. 2024.

[4] He, Zhisong, et al. "An integrated transcriptomic cell atlas of human neural organoids." bioRxiv (2023): 2023-10.

[5] Schiebinger, Geoffrey, et al. "Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming." Cell 176.4 (2019): 928-943.

[6] Tong, Alexander, et al. "Improving and generalizing flow-based generative models with minibatch optimal transport." arXiv preprint arXiv:2302.00482 (2023).

### Questions
- I would like to ask why the $D^{dev}$ loss is needed? How do you compute couplings? Don’t you always map clusters from t to those in t+1 like in the standard OT matchings? Why can clusters in t+1 be ancestors of t?
- In my view the constraint to monotonically varying genes is a bit restrictive and system specific. Is it possible to integrate more complex developmental patterns for other genes. Would you mind elaborating on how you would do it?
- I did not understand how the B-splines method accommodates mutations in the trajectory. Is it related to the perturbation experiment? Could one model mutations with standard discrete optimal transport as well?
- How did you compare with Moscot on the TOC metric? As far as I know, it is not a method for learning pseudotime.

### Soundness
2

### Presentation
3

### Contribution
2

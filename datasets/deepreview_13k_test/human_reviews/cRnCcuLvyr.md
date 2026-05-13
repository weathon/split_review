# CViT: Continuous Vision Transformer for Operator Learning

- Decision: Accept
- Scores: 6, 8, 8, 6, 6

## Abstract
Operator learning, which aims to approximate maps between infinite-dimensional function spaces, is an important area in scientific machine learning with applications across various physical domains. Here we introduce the Continuous Vision Transformer (CViT), a novel neural operator architecture that leverages advances in computer vision to address challenges in learning complex physical systems.  CViT combines a vision transformer encoder, a novel grid-based coordinate embedding, and a query-wise cross-attention mechanism to effectively capture multi-scale dependencies. This design allows for flexible output representations and consistent evaluation at arbitrary resolutions.
We demonstrate CViT's effectiveness across a diverse range of partial differential equation (PDE) systems, including fluid dynamics, climate modeling, and reaction-diffusion processes. Our comprehensive experiments show that CViT achieves state-of-the-art performance on multiple benchmarks, often surpassing larger foundation models, even without extensive pretraining and roll-out fine-tuning. Taken together, CViT exhibits robust handling of discontinuous solutions, multi-scale features, and intricate spatio-temporal dynamics. Our contributions can be viewed as a significant step towards adapting advanced computer vision architectures for building more flexible and accurate machine learning models in the physical sciences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a continuous operator learning method using the vision transformer with a newly introduced coordinate embedding for the query value. The proposed method is based on the previous continuous operator learning method. The authors have provided analysis including comparisons with recent operator learning methods on learning different operator equations, ablation studies for different structure choices, discussions of the proposed method compared to recent arts, theoretical insights of the proposed query embeddings, etc.

### Strengths
- The proposed coordinate embedding for the query is interesting, and is effective in the continuous ViT learning, compared to MLP and RFF. Also, it is simple and easy to control through the interpolation parameter $\beta$.
- Discussions and analysis in the paper are extensive and interesting. Overall, the paper is well-organized and easy to follow.
- The proposed coordinate embedding could have the potential to apply to more general continuous learning beyond physical domains. Especially for the vision tasks, such as 3d geometries including point cloud representations, it is worth exploring.

### Weaknesses
- Why not do coordinate embedding for all query, key, value? Only doing coordinate embedding for query preferable in which way? Maybe some further analysis on this could be included to further highlight the effectiveness of the proposed coordinate embedding.
- The first question brought to the second one, that in the paper (appendix), the authors discussed the Lipschitz constant for different embeddings from linear embedding to random Fourier features (RFF), and to the proposed coordinate embedding, which is interesting and worth discussing. The authors mentioned that the proposed coordinate embedding is easier to tune since it is mainly based on one parameter $\beta$. However, for RFF, there is also only one parameter to control the spectral bias, and thus control the Lipschitz constant. I wondered if the authors could also provide an analysis on only using RFF for the proposed framework. 
- Figures 3, 5, and 6 lack notations to distinguish columns.

### Questions
- I wondered how will the proposed method be applied for more general vision tasks, especially for 3d vision. I wondered what are the authors’ opinions on this? What are the difficulties, such as computations, that might be difficult to apply? 

Please see the above section for detailed comments, too.

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
This paper introduces a new neural operator architecture that tackles recent computer vision techniques (vision transformers, cross-attention). In particular, the CViT model -- for Continuous Vision Transformer for operator learning -- leverages the perceiver architecture to retrieve the representation of a query at a given continuous coordinate from spatiotemporal data. The relevance of the representations learned by CViT is evaluated on a diverse range of PDE such as fluid dynamics, climate modeling, and reaction-diffusion processes.

### Strengths
This paper is well-written, easy to read, and technically sound. The proposed approach appears to scale more efficiently than the current baseline thanks to the perceiver-inspired architecture. The results seem also promising.

### Weaknesses
* No clear structure of the related work section. It would help the reader to add more justifications on why transformer approaches struggle with various resolutions. Even if I tend to agree with the conclusion, it is also not clear, why a novel architecture design is required to solve the limitations related to high dimensional data and long-range dependencies.  
* The transformer architecture in Fig. 1. does not give any insight and is well known. IMO, Authors could either remove it or replace it with the perceiver one. 
* It is unclear how many visual latent queries are used. From the figure and text, it seems that there is only one query which is then duplicated. In the perceiver architectures, these latent queries are learned, does this mean that only one query is learned? The stability of the model with respect to the number of queries could be presented in the ablations.  
* The ablation with respect to parameter $\beta$ is difficult to understand as, in Fig. 4, $\epsilon$ is not introduced. Is $\epsilon = \beta$? The value of $\beta$ seems extremely high ($10^5$) and should be compared to the input's resolution. Here, does eq. (1) reduces to a naive averaging with $\beta=10^5$? 
* Results on standard benchmarks would help judge the method's efficiency. Here, it seems that the authors show results only on selected equations from PDEBench or PDEArena.

### Questions
* "2+1 dimensional spatio-temporal data tensor" but it is then written that $\boldsymbol u \in \mathbb R^{T\times H \times W \times D} *i.e.* four coordinates. 
* How separating the positional encoding (PE) between 1D temporal and 2D spatial is different than having one spatio-temporal (thus 3D) PE?

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
4

### Summary
This paper presents a variant of Vision transformers which allows handling of continuous outputs. The model works by first encoding an input image sequence into a set of latent vectors using cross attention (a la Perceiver style encoding). The latents compress the input over time. The resulting latents are fed through several transformer layers. The readout is the interesting part - a learnable grid of spatial queries is interpolated using Nadarya-Watson interpolation to produce queries which are used to cross attend into the output of the vision transformer. The resulting attention weighted value is used as the outputs - this is done for every output coordinate.
The method is shown to work on several interesting physics oriented datasets with several ablation experiments. More analysis is shown in the appendix.

### Strengths
I found this paper very interesting.

Originality:
I think this is a very good variation of Vision Transformers which significantly expands their capabilities. I found the interpolated readout mechanism of particular novelty.

Quality:
This is a well executed paper. There is ample experimental validation using several different datasets. The baselines chosen (as far as I can tell) are diverse and strong. There is a good set of ablation experiments and deep analysis of the method in the appendix.

Clarity:
The paper is well structures, well written and easy to read. All the nomenclature is well defined and I had no problem following the paper.

Significance:
While I'm not an expert in the field to me this seems like a significant contribution to the field which greatly expands the expressive power of vision transformers.

### Weaknesses
All in all I think this is a strong paper, however:

* Other domains? I would have loved to see if the resulting method is applicable to other domain or training setups beyond L2 prediction of physical systems. Does it work, for example, on natural video? Would it be useful as a diffusion model back-bone?

* More analysis of cross attention - one of the more interesting parts is the use of cross attention, both in the encoding and decoding. It would be nice to see visualizations of cross attention patterns emerging in both directions. Do specific latents take on specific roles when decoding? are they responsible over different parts of space? time? both?

While I do not expect these to be addressed in the rebuttal I really do think these would maker the paper stronger.

### Questions
My main point of inclarity is the initialization of latent queries in the encoder. The paper states they are initialized with a unit Gaussian - is this a learned initialization, or are the queries sampled every time the model is learned? The latter would mean, for example, that we would expect to see slightly different outputs every time the model is run - is that the case? (I am not saying this is a bad thing btw, just want to understand). Also - how many query vectors are used? the paper mentions it's more than one, but the number is not supplied in the paper.

Related to the above - I am not sure I understood why the query vector z is tiled across space? if it's the same vector across all of space then the output of the query would be the same for every spatial location, am I wrong? or is there more positional encodings added there? It would be good to clarify this.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a neural operator architecture inspired by computer vision to address spatio-temporal scientific problems. The proposed model is structured with a transformer encoder featuring spatio-temporal embedding and time-aggregation layers, a grid-based positional embedding, and a cross-attention decoder. The author employs multiple benchmark datasets and model architectures for comparative experiments.

### Strengths
- The author conducts extensive experiments, comparing several recent model architectures to demonstrate performance outcomes. The results are presented with additional clarity by including the number of parameters.

- The detailed discussion of limitations and future directions is appreciated. Notably, the computational inefficiency for high-resolution data should be addressed in future work.

### Weaknesses
- Since this method draws on the vision transformer, have comparisons been considered with other vision-based extensions for spatio-temporal applications, such as ViViT[1] and VMAE[2]?

- Regarding the datasets selected for experimentation, incorporating more complex, real-world cases could further substantiate performance, as some baseline architectures still yield results similar to those of the proposed model, despite the model size.

[1] Arnab, Anurag, et al. "Vivit: A video vision transformer." Proceedings of the IEEE/CVF international conference on computer vision. 2021.

[2] Tong, Zhan, et al. "Videomae: Masked autoencoders are data-efficient learners for self-supervised video pre-training." Advances in neural information processing systems 35 (2022): 10078-10093.

### Questions
- Does the grid resolution similarly impact computational efficiency as the patch size?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the architectural design of transformers for operator learning methods. To efficiently implement continuous vision transformer architecture, they developed (or adopted) two techniques: perceiver resampler and coordinate embedding. The perceiver modules effectively aggregate temporal dimension, and the coordinate embedding enables the model to handle continuous input domains and improve accuracy. The proposed architecture achieved state-of-the-art results on various challenging PDE benchmarks while maintaining higher parameter efficiency.

### Strengths
1. It achieved state-of-the-art performance on various benchmark datasets with the network's great parameter efficiency.
2. Coordinate embedding is an interesting approach to injecting the coordinate information into the network.
3. The theoretical result related to coordinate embedding is quite informative and useful for the community.

### Weaknesses
1. The proposed grid-based positional encoding may not be a desirable solution for high-dimensional PDEs. As the authors said, it requires high-resolution grids to achieve competitive performance, and this approach would not scale up to more than 3-d time-dependent PDEs, e.g., (3+1) NS equation. 

2. The proposed Nadaraya-Watson interpolant would not scale with high-resolution grids since it has to look at all grid features. I am curious the inference cost of the proposed approach according to grid resolutions. Is the inference speed as fast as the previous methods?
The grid resolution 128 (N_x) x 128 (N_y) x 512 (feature dim) is already > 9M, and CViT-S model size is 13M. Does it mean that most of the parameters are used for grids?

3. Does this scale well for high-resolution solutions? The authors mentioned that the grid resolution should be similar to the solution resolution. Then, 512 resolution means 512^3, which is roughly 134M. Could you show me how the proposed method can make good predictions for high-resolution solutions? e.g., testing 128 grid resolution model for predicting 512 solution resolution.

4. This is a rather suggestion than a question. Why not coordinate embedding for temporal dimension? currently, y \in R^2, but why not y \in R^3? Temporal resolution can be coarse in this case to maintain parameter efficiency.

5. How about other datasets? e.g., other PDEs in PDEBench and PDEArena?

[minor comments]
1. Numbering for all equations would be desirable during the review process.
2. How do you determine \beta = 10^5?
3. L171: is u_f a flattened version of what? u_pe? not mentioned in the paper.
4. L174: ‘tilling the latent query’, I am not sure “tiling” is a widely accepted term, I think it is a pytorch’s terminology.
5. Eq (1): why not just using linear interpolation?
6. Figure 3, 5, 6: what do different columns mean? Time evolution?
7. Figure 4: (d) \epsilon -> \beta?

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

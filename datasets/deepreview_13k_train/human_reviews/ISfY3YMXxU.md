# INRet: A General Framework for Accurate Retrieval of INRs for Shapes

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Implicit neural representations (INRs) have become an important representation for encoding various data types, such as 3D objects/scenes, videos, and audio. They have proven to be particularly effective at generating 3D content, e.g., 3D scene reconstruction from 2D images, novel content creation, as well as the representation, interpolation and completion of 3D shapes. With the widespread generation of 3D data in an INR format, there is a need to support effective organization and retrieval of INRs saved in a data store. A key aspect of retrieval and clustering of INRs in a data store is the formulation of similarity between INRs that would, for example, enable retrieval of similar INRs using a query INR. In this work, we propose INRet (INR Retrieve), a method for determining similarity between INRs that represent shapes, thus enabling accurate retrieval of similar shape INRs from an INR data store. INRet flexibly supports different INR architectures such as INRs with octree grids and hash grids, as well as different implicit functions including signed/unsigned distance function and occupancy field. We demonstrate that our method is more general and accurate than the existing INR retrieval method, which only supports simple MLP INRs and requires the same architecture between the query and stored INRs. Compared to 3D shape retrieval by converting INRs to other representations like point clouds or multi-view images, INRet achieves higher retrieval accuracy while avoiding the overhead of conversion.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While the idea of Implicit Neural Representations (INR) for shapes has been proposed elsewhere, this paper focuses on the task of organization and retrieval of INRs. The authors propose INRet, a method for aggregating two primary INR architectures, the MLP encoder and the feature grid encoder. They create a new embedding, which they call the INR embedding, which is obtained by optimizing a signed distance loss over three different implicit functions (signed and unsigned distance functions and the occupancy field). The authors demonstrate superior retrieval accuracy over existing methods.

### Strengths
The method achieves a significantly higher retrieval accuracy ( > 10%) over the existing state of the art methods including inr2vec on ShapeNet and Pix3D datasets. The authors also show retrieval results on methods such a PointNeXt and View-GCN. 

The method allows the multiple INR architectures as well as as different implicit function representations, and is thus general and flexible. 

They design their loss cleverly to include two terms. One term is an L2 loss that minimizes the pairwise differences between the respective INR embeddings (for the same shape), even if they have different implicit functions. The other term is the mismatch between the decoder and the unsigned distance function. This strategy allows the authors to use a single common decoder for three different implicit functions as well as handle diverse INRs such as octree grids and hash grids. 

The method define a common latent space for multiple implicit function representations of shapes. This is an interesting idea and needs to be developed further. 

The authors also demonstrate retrieval performance on the converted explicit representations. This enables them to compare their results with PointNext and View-GCN.

The experimental results are sound and indeed demonstrate the effectiveness of the method.

### Weaknesses
The paper does not propose novel architectures or representations or even new metrics for similarity between the implicit representations. 

Instead they make use of existing architectures and embeddings (separately for the MLP and the feature grid) as well as L2 losses for the pairwise dissimilarity 

In equation (4), the two terms operate on different types of representations when they are compared. While one can trivially assume an Euclidean embedding (which the authors assume here), this may be problematic. Inside both the terms, the distance (d_u(x)) or the embeddings e_i, i \in {s, u, o} should be either appropriately weighted. This is especially important if the norms operate on an occupancy field as the distance functions and occupancy fields are structurally different quantities, the occupancy grid being more feature rich compared the the S/UDFs. This could perhaps be done naively by doing an internal conversion between the two before the norm is computed. 

The above comment can also be understood in a different way. The INR embedding space is essentially a product space and thus a cost function that is used for matching two elements in that space, needs to be appropriately weighted. This type of an embedding is indeed interesting to explore and is one of the strengths of the paper (as listed above). 


While the loss is designed to handle different types of input INRs, the decoder is restricted to outputting only a single type of INR. In this paper, it is likely the UDF. While this is fine for a  retrieval-only type application, which the authors demonstrate here, it makes the method slightly less general to be used for different applications (general shape embedding etc).

### Questions
In Equation (4), is the first loss term an L1 norm or the L2 norm? This is not clear and there will be different convergence properties of their encoder/decoder if it is an L1 norm.

In equation (4), since the first term compares the decoder outputs to d_u (an UDF), will the loss be biased towards UDFs? Can the authors comment? What if in the first term, the loss also incorporates pairwise differences between each INRs?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents INRet, a general framework for the retrieval of shape INRs. INRet uses the grid-based methods (e.g. NGLOD, instantNGP) as the backbone of INRs and is able to handle different INRs, such as SDF, UDF and Occ. INRet achieves the best results under shape retrieval task.

### Strengths
1. The task is quite interesting, which retrieves shapes in terms of INRs. This paper handles multiple INRs, such as SDF, UDF and Occ, which covers the commonly used implicit representations.

2. NGLOD and instantNGP are quite popular backbones, it is good to see that INRet supports these methods.

3. The evaluations seems good.

### Weaknesses
1. The matching among SDF, UDF and Occ may lead to errors. Both SDF and Occ can only represent watertight shapes, but researchers leverage UDF to represent open-surfaces and multi-layer structures. What if I input an INR in terms of a multi-layer car or a shirt with open surfaces? The matching from the SDF and Occ of watertight mesh of the car or the shirt is wrong for the UDF.

2. There is no visualizations for comparison or illustrating, which makes the paper lack of qualitative analysis. I also find it hard to get the advantages of INRet compared to other baselines without visualizations.

3. The authors mentioned that ``the prior work only supports MLP-based architecture, which is not commonly used today.'' I agree with the authors that grid-based approaches are more popular today, however, the MLP-based approaches are also commonly used today, and INRet do not support these methods. Furthermore, there are many other representations for INR today, can INRet also handle these types of INRs (e.g. triplane for TensoRF, point feature-based for Point-NeRF)?

### Questions
Please refer to the weaknesses above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the retrieval problem of Implicit Neural Representation (INR).

Existing methods perform retrieval with 3D data directly. As more and more INR data and converting to 3D data takes up some computation, this paper proposes a framework called INRet (INR Retrieve) to perform retrieval directly on INR space, supporting both MLP-only and MLP+Grid-based INR, including different implicit functions.

Specifically, the (query) input is INR weights and the grid-based features (e.g., InstantNGP hash grid). INR weights will be flatten and passed into an MLP encoder to obtain the embeddings, grid-based features will be passed into 3D convolution encoder to obtain the embeddings, the retrieval is then done by using the concatenated embeddings. During the training, the concatenated embeddings will also be concatenated with the coordinate inputs, and will be passed into an MLP implicit decoder. The training objective is to minimize the distance between the decoder output and the target function (e.g., SDF).

Additionally, conversion from conventional INR (without grid-based features) can be done through distillation (where the target is generated by the conventional INR).

### Strengths
originality:  compared to inr2vec [1], this paper proposes an additional module to handle the latest architecture of INR (i.e., octree-based and hash grid-based). This paper also describes how to handle different implicit functions (e.g., SDF, UDF, Occ) and to map the INRs into a common latent space, and proposes suitable regularization terms to minimize the domain gap between different implicit functions. 

quality: the paper is technically sound.

clarity: the paper is well-organized and easy to understand. 

significance: the paper is addressing a new topic -- retrieval on INRs. Different from conventional retrieval problems where embeddings are obtained directly from the input, which has some sense of interpretability, retrieval with INR is still in the black-box stage --- difficult to interpret the embeddings of INR. Hence, this paper is important to the community as this paper tackles how to retrieve directly in INR space, and future works may be inspired to solve the following limitations.

[1] https://arxiv.org/abs/2302.05438

### Weaknesses
This work designed a framework for retrieval with INRs and proposed regularization terms. However, the analysis of the proposed regularization terms only shows the performance comparison. It would be better if the paper could further analyze why these terms are so important.

A potential weakness of this work is that all data must be first encoded into the INR space. If given an unseen/test input that is a 3D model but wants to query similar INRs, how long to convert it into the INR? Since we can have many possible different INR weights that can reconstruct the 3D model, how to ensure that the embeddings of the INR weight are still meaningful? Possibly a tSNE of the learned embeddings can be provided.

The writing quality can be further improved, there are some typos and grammar errors (e.g., Sec 5.3 second paragraph, third line "respective datasets. also performs better".

### Questions
A potential weakness of this work is that all data must be first encoded into the INR space. If given an unseen/test input that is a 3D model but wants to query similar INRs, how long to convert it into the INR? Since we can have many possible different INR weights that can reconstruct the 3D model, how to ensure that the embeddings of the INR weight are still meaningful? Or is there any way to ensure this?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses a method to compare implicit neural representations, with the purpose of retrieving shapes similar to a query representation in a data base. The shapes in the database may be encoded using different category of representations (SDF, UDF, occupancy fields...) and neural representation (grid-based, full MLPs...). The problem is tackled by training encoders to generate one embedding from one representation (associated to one object). One such encoder is trained for each type of representation. The embeddings generated from the encoders are aligned by a specific loss including a) difference loss between embeddings generated from different representations of the same object and b) a similarity loss between the original and a reconstructed UDF representation. The latter is done by a single encoder, from the embedding, no matter the original representation. If no encoder exists for the type of representation of a shape, the paper proposes to train, using distillation, a representation that has such an encoder. Various experiments compare the proposed approach against other INR embedding methods and to converting to explicit representation to retrieve shapes.

### Strengths
originality:
- I am not aware of any similar work.

quality:
- Sensible baselines are used, in particular other INR-based approaches and using conversion and comparison in explicit form.
- The experiments show the strength of the approach.
- There is an ablation study.

clarity:
- The paper is well written and relatively clear.

Significance:
- The paper discusses an approach to cover representations not initially included and experiments for that case as well.

### Weaknesses
quality:
- In the baseline where retrieval is based on conversion to explicit representation, the quality of the reconstruction is not quantified, unless I missed it. Therefore it is not possible to know whether these baselines are worse than the proposed approach because the latter is superior or because the reconstruction is not good. Unless I missed something, an alternative may be to use the original meshes for retrieval rater than a reconstruction.

clarity:
- Figure 2 could benefit from the addition of symbols used in the text to denote the different elements, as done in Figure 1.

significance:
- I am not sure how likely a database containing INRs encoded using various types of INRs is.
- Based on my understanding of the approach, I think the encoding of the shapes in the database must be trained with the decoders used to create the INR embeddings (part b and c in Figure 2). Thus is not clear to me why handling multiple types of representation is necessary. If the database owner knows querying and retrieval is necessary (as part b and c have been trained), why not create an embedding using a single type of representation? Of course, encodings trained before the system is available can be handled by the distillation approach. In experiments 5.2 and 5.3, I was also not able to precisely understand whether the encodings were trained with or without the decoder

Typos/details:
- Figure 2: Emplicit
- For the same figure, I would like to suggest labeling the models that are mesh specific and global for the approach. Though not necessary, it may increase the clarity of the figure.

### Questions
I would be grateful to the authors for commenting on the weaknesses listed above, and answering the following question:
- As far as as know, features from different hierarchical levels of a grid-based INR are usually concatenated before being fed to the network. I was surprised to see that in this paper they are summed together (p5, top paragraph). Is there any advantage/downside to summing them?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

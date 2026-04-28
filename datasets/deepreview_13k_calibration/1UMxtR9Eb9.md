# Unifying Disentangled Representation Learning with Compositional Bias

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 8, 6, 3, 6

## Abstract
Existing disentangled representation learning methods rely on inductive biases tailored for the specific factors of variation (e.g., attributes or objects).
However, these biases are incompatible with other classes of factors, limiting their applicability for disentangling general factors of variation.
In this paper, we propose a unified framework for disentangled representation learning, accommodating both attribute and object disentanglement.
To this end, we reformulate disentangled representation learning as maximizing the compositionality of the latents.
Specifically, we randomly mix two latent representations from distinct images and maximize the likelihood of the resulting composite image.
Under this general framework, we demonstrate that adjusting the strategy for mixing between two latent representations allows us to capture either attributes or objects within a single framework.
To derive appropriate mixing strategies, we analyze the compositional structures of both attributes and objects, then incorporate these structures into their respective mixing strategies.
Our evaluations show that our method surpasses or is comparable to state-of-the-art baselines such as DisDiff in attribute disentanglement (DCI, FactorVAE scores), and LSD and L2C in object property prediction tasks for object disentanglement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the learning of disentangled representations in particular the adaptation of existing frameworks to the learning of representations that can disentangle both attributes (e.g., color, texture, ...) and objects in a scene which authors claim prior work only tacked one of the other. The authors propose to leverage compositionality to learn disentangled representations. The setup includes pre-trained VAEs which provide representations that are then combined. The new representations serve as input to a diffusion-based decoder which is trained to reconstruct the composition of the original images. A pre-trained diffusion model is also used to enforce consistency between the input composite representations and the representation of the generated image. The method is tested for feature and object disentanglement on multiple synthetic datasets where is shows either superior or comparable performance to attribute or object disentanglement methods.

### Strengths
- presentation: the paper is polished, clear, and well-written
- relevance of the topics: learning models that disentangle sources of information whether attributes or objects without any prior knowledge about the type of sources but rather that rely on general prior information about the data structure like compositionality to enforce disentanglement is of great nterest to the community.

### Weaknesses
 - complexity of the proposed approach leads to limited applicability and impact: the proposed approach requires the use of pretrained diffusion models to operate (i.e., to maximize the likelihood of composite images) and requires access to composite images to train the model. 
- limited performance increase: while results show more consistent improvements for the **multi-seed** attribute disentanglement experiments, the gains are less consistent across metrics for the **single-seed** object disentanglement experiment.


Minor:
- theta should be a subscript in line 187
- typo line 212, 281, 310
- error in figure 1: z3 should be blue instead of orange
- line 227: figure 1 above

- Not sure I am getting lines 210-213

### Questions
- can authors elaborate on why the maximum likelihood is needed despite already enforcing low reconstruction error ?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper attempts to tackle attribute and object disentanglement through the same mechanism as opposed to separate treatment by prior methods. Building on diffusion based decoding approaches that maximize compositionality, this paper lays emphasis on composing/mixing strategy of latents for object/attributes.

### Strengths
1. Addresses both attribute and object disentanglement by developing appropriate mixing strategy for latents. This is helpful to steer the field towards disentangling different types of factors of variation - eg properties of object and object themselves.
2. The paper gives an in depth analysis of the intricacies involved in optimizing for compositionality.
3. The paper is well written for the most part. There are appropriate visualizations in method and experiments that complement the text.

### Weaknesses
The impact of paper can be more by showing results on real world data

### Questions
Are there any further insights on the failure cases? Is it harder to compose attributes or objects?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Note: I am not an expert on disentangled representation learning and know little/none of the related work.

The paper proposes an approach to learn a generative model for learning disentangled representations by maximizing the compositionality of representations. By mixing the representations of two images (given some constraints to make sure the results latent representations are valid) and maximizing the likelihood of the resulting composite images the model learns representations that can be disentangled on the object and attribute level. Experiments on synthetic datasets show that the model performs well in disentangling factors across several datasets both on the object and attribute level.

### Strengths
The paper addresses the learning of disentangled representations for both objects and attributes and makes use of a standard generative model for learning them. By introducing specific mixing strategies to combine latent representations of different images under given constraints the model is able to learn disentangled representations under a fairly simple framework.

The evaluation shows that the model learns better disentangled representations than the given baselines.

### Weaknesses
It seems like the approach is only useable if the practitioner already knows the underlying factors they want to disentangle, as the latent mixing strategies take this knowledge under account. Specifically, the method requires a priori specification of which latent dimensions or groups of dimensions correspond to which factors (e.g., object identity, attribute type). This limits its applicability in scenarios where the ground truth factors are unknown or difficult to define. The mixing strategies, while effective given the known factors, are not generalizable to arbitrary latent spaces without this prior knowledge. It's also not clear to me if this would translate to real-world datasets with more complicated distributions. The current mixing strategies seem tailored to the specific synthetic datasets used, and it's unclear how they would perform on datasets with more complex dependencies between factors. The experiments show results for either object disentanglement or attribute disentanglement but no experiments for joint object and attribute disentanglement. This limits the scope of the evaluation and leaves open the question of whether the method can handle more complex scenarios where both object and attribute factors need to be disentangled simultaneously. All experiments are done on rather simple synthetic datasets. The datasets do not represent the complexity of real-world data, which may have non-linear relationships between factors and more complex distributions.

### Questions
How would this generalize to more complex datasets where the exact factors of disentanglement might not be known. Does this scale to lots of disentangled factors (dozens or hundreds) or would that make the mixing strategies too complicated?

### Soundness
3

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
The paper presents a framework for disentangled representation learning that targets both attribute—and object-based disentanglement within a single model. The authors formulate disentangled representation learning as maximizing the compositionality of randomly mixed latent representations of distinct images. The method uses a pre-trained diffusion model as an image generator and introduces an additional compositional consistency loss to encourage the composite images to remain faithful to the composite latent. The authors claim that their method can obtain superior performance in standard disentanglement benchmarks.

### Strengths
**Strengths:**

- The paper is relatively clear and easy to understand;

- The general idea of enforcing compositional consistency across mixed latent representations is fairly neat, and could possibly be extended to more challenging scenarios;

- The results seem to match or exceed some of the previous works on disentanglement benchmarks.

### Weaknesses
 **Weaknesses:**

- The approach relies on a pre-trained diffusion model to ensure composite image realism, but this doesn’t guarantee alignment with the intended attribute or object combinations. As such, it is my understanding that this can compromise the interpretability and control of compositions in the general case, especially in more complex scenarios with subtle and/or hierarchical attribute/object relationships. The compositional consistency loss, while intended to address this, may not be sufficient to ensure that the generated images truly reflect the intended latent space manipulations, particularly when the diffusion model's prior does not strongly align with the desired compositional structure.
- There are no guarantees that the latent representations are identifiable under the current model, and by implication, neither are the compositions. This lack of identifiability makes it difficult to ascertain whether the learned representations truly correspond to meaningful, disentangled factors of variation, or if they are simply arbitrary encodings that happen to produce realistic images. Without identifiability, the interpretability of the latent space is severely limited.
- The fixed mixing strategies, although appropriate for the simple cases studied, are quite rigid and likely would not adapt well to more complex scenarios in real data. The method's reliance on predefined mixing strategies limits its ability to handle more complex compositional structures, such as hierarchical relationships between attributes and objects, or scenarios where the mixing strategy itself needs to be learned from the data.
- The scope of the evaluation is limited to toy settings which is somewhat outdated given the recent progress in generative modelling. The experiments do not adequately demonstrate the method's ability to scale to real-world datasets with complex scenes and diverse factors of variation. The lack of evaluation on more challenging datasets raises concerns about the practical applicability of the proposed approach.
- The writing is a little careless at times, there are numerous typos and/or grammatical issues some of which are mentioned below.

In my opinion, in its current state, this work largely sidesteps the key challenges in the area today, particularly the theoretical analysis of identifiability for latent representations and the development of scalable techniques that allow object-centric methods to be applied effectively in real-world settings. Therefore, I would encourage the authors to bolster their current contribution by tackling one of the two aforementioned challenges in the future.

**Typo corrections:**

line 34 "theoretically prove" 
line 46 "a unique object" 
line 70 "and verify" 
section 2 heading change to "Background" 
line 77 "incompatible with" 
line 97 "that render" 
line 107 "tailored specifically" 
line 122 "maximizing the likelihood" 
line 122 "disentangle attributes and objects" 
line 147 "to the type of" 
line 163 "While (Jung et al., 2024) rely" 
line 165 sentence needs rewriting for clarity 
line 167 "derive a specific" 
line 177 "of each factor" 
line 177 "derive a corresponding" 
line 188 "independent sampling of" 
line 190 "is equivalent" 
line 197 "always contains" 
paragraph starting at line 206 could do with rewriting for clarity 
line 216 "belong to the same" 
line 259 "While Jung et al. (2024) also maximize..." 
line 295 "to each factor of" 
line 307 "ensure reliable image generation" 
line 310 "from scratch" 
page 6 footnote "significantly" 

etc

### Questions
- What challenges do the authors anticipate in applying this model to real-world, complex datasets, and how might they address these?
- Could dynamic/learned mixing strategies replace fixed ones to improve flexibility in complex scenes? 
- Have the authors thought about under which conditions their method can provide identifiability guarantees?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a framework to learn disentangled representations of either attributes (e.g., an object's color or orientation) or distinct objects within a scene. The frameworks begins by encoding a pair of images using a VAE encoder. The embeddings generated are $k$ vectors that eventually will be the disentangled representations. At this stage a mixer samples some vectors from  image 1 and some vectors from image 2 generating the representation of a ``new’’ composed image. These new representation are then noised and denoised thanks to a diffusion model before going through the decoding stage of the VAE.  The mixing component can be adjusted according to the desired inductive bias. For attribute disentanglement, the model enforces mutual exclusivity by ensuring each latent vector is sampled from only one of the two images. In contrast, for object disentanglement, this exclusivity constraint is removed, allowing, for instance, the first latent vector to be sampled from both images.

The objective function is composed of three terms: (1) a latent denoising objective using a diffusion decoder (as in Jung et al., 2024); (2) a term to maximize the likelihood of the composed image, implemented as a diffusion loss, where the diffusion model is pre-trained for each task and then frozen; and (3) a consistency objective, which ensures that the latent representation $z$ of a given image and the latent representation re-encoded after decoding the reconstructed image from $z$ remain close. For this last term, the authors found that using an NCE-like objective, where each representation should be close to its counterpart and distant from other batch representations, outperformed simply minimizing cosine similarity.

The proposed method is evaluated against various baselines, datasets, and metrics for both attribute and object disentanglement, showing improved performance across the board.

### Strengths
The paper is easy to read. The proposed framework leverages and combines many techniques (such as diffusion models, SSL, optimal transport) in interesting way. The final framework is simple and from the reported results effective.

### Weaknesses
The main weaknesses of this paper are in the empirical evaluations. Specifically, some of the results reported do not match those previously published, a very common task used to assess object disentanglement (unsupervised segmentation) is missing, none of the experiments are done on realistic or complex datasets (although recent state-of-art works do employ those kind of datasets). These are the main points to be discussed during the rebuttal. Fixing these could increase the soundness and the contribution scores, hence, also the final recommendation score. See below for more details on all these weaknesses.
- Results reported in this work about other baselines do not seem to match the original results reported by the respective original papers on the same tasks and datasets. For example, for the LDS dataset, property prediction in the original paper shows much better accuracy (80.23% on Shape, compared to the one reported in this work for LSD which is only 68.25%, for comparison the proposed method accuracy is 70.90%). For the properties “material” and “shape”, the differences are even higher. This discrepancy raises concerns about the validity of the comparisons presented and needs a thorough explanation. It is crucial to understand whether these differences stem from implementation details, experimental setup, or other factors.
- State of art works on object disentanglement consistently use unsupervised segmentation to assess the usefulness of the generated representations, however, these tests are missing from the current work. This is an important task because it shows a concrete application of these type of representations (and for ease of comparison given that all recent works use both unsupervised segmentation as well as property prediction). Specifically, the evaluation should include metrics such as Adjusted Rand Index for foreground objects (FG-ARI), mean Intersection over Union (mIoU), and mean Best Overlap (mBO). The absence of these metrics makes it difficult to gauge the practical utility of the learned representations for downstream tasks.
- Both set of experiments (attributes and objects) lack realistic or more complex datasets which state-of-the art have been using (in addition to some of the datasets used in this work). While it is not needed to have results on all of the following datasets, showing that the proposed method scales to the complexity of some of those datasets comparably to the state of art would make the contribution stronger. For example, for the attribute disentanglement, FactorVAE uses CelebA. For Object centric, Jung et al. 2024 use Super-CLEVR (multi-colored parts and textures), and MultiShapeNet (for realistic images), while other work such as Object Centric Slot Diffusion use the MOVi-C dataset (which contains complex objects and natural background), MOVi-E datasets (which contains up to 23 objects per scene), FFHQ (high quality image of faces). The inclusion of results on at least a couple of these more challenging datasets would provide a more comprehensive evaluation of the proposed method's capabilities and limitations.

Other minor evaluations weaknesses:
- Attribute disentanglement results are reported with standard deviation (great!) but it is unclear on how many runs. Results for object disentanglement are provided without any standard deviation (but they should).

Minor Writing Comments. This writing suggestions are not critical but they would improve clarity and readability of the paper. No need to discuss them in rebuttal but they do need to be fixed and could increase the presentation score.
- I find the first part of the paper (until section 3) lacking important details that could easily be provided. For example:
    - The abstract is very dry, there is no mention of which are the “strong baselines”, nor which tasks this work was tested on, nor quantitative evaluation to show that the propose method “matches or exceeds” baselines. Consider adding more information.
    - From the abstract (and even the introduction and the beginning of section 3.1) it is not clear what “mix”, “compose”, “composition operator” mean. It could be concatenation, averaging, summing… it will only become clear much later but It would be great to provide more details if not in the abstract (ideal) at least in the introduction.
    - Still by the end of Section 2 there is no formal definition of “attribute” and “object”. The first example of attributes is at page 4. Having these definitions would help the reader understanding the work much better since the beginning of the paper. From the examples at page 4 it seems that nose is an attribute and face an object but it could easily be argued that actually nose is an object in itself, or that face is an attribute of a bigger objet (human body). Again this highlight the need for a formal definition of attributes and objects.
- In Figure 1 there is a concrete image example but it is not clear if it belongs to Attribute mixing or Object mixing. The “thing” being mixed is a cylinder and a ball so why is it linked both to attributes and objects? It would be clearer to provide an example for both. Note that everything becomes clearer once the whole paper has been read but the first time the reader reaches Figure 1 this could be a source of confusion.
- At page 6 the authors say “This occurs because the encoder can collapse the posterior pθ(z|x) into a single mode“. I know if this is an issue with posterior collapse. If the encoder collapses the posterior, then the first loss ($L_{diff}$) should become high hence preventing the collapse. The problem seems to be related to the fact that the learnt encoding is sufficiently different (hence not collapsed) to keep $L_{diff}$ while what the authors want is not just $\hat{z} = z$ but also as different as possible with respect to other $z$s.
- Typo (?): “we can without modifying the objective function, which will be introduced in next paragraph.” It is not clear what is that “we can”.
- Typo: line 241 “an noised”.
- The following sentence is incomplete: “we adjust our image encoder to take VAE features as input”. Please clarify which kind of adjustments?
- “When back-propagate the gradient through xc, we truncate the gradient at the last iteration of decoding”. Why, it would be great to explain and motivate this choice.
- Typo in Line 310: “model on each training dataset from the scratch”. Should be “from scratch”.
- It would be great to explain how you understand which latent controls which factor. I believe there is a brief explanation in the appendix but it would be great if it could be explained in the main paper.
- In table 3 and some part of the appendix the loss term $L_con$ is called $L_cycle$. Please update it so that it is consistent throughout the paper.

### Questions
Please address the main weaknesses listed above. These are the most critical ones, I find the paper interesting but these weaknesses do need to be tackled, specifically:
A. Could you explain or correct the mismatch between your results and those previously reported?
B. Could you provide results on unsupervised segmentation tasks using the three typical metrics: Adjusted rand index for foreground objects (FG-ARI), mean intersection over union (mIoU), and mean best overlap (mBO) (see Jung et al 2024 as an example).
C. Could you provide results on at least a couple of the more complex datasets listed above (and for the tasks used in the state of art work mentioned).

Additionally these are more questions that are interesting to discuss.

D. The authors state at various points in the manuscript that previous methods use inductive biases specific to either attributes or objects, making them unsuitable for both simultaneously. For instance, in the statements, “Existing disentangled representation learning methods rely on inductive biases tailored for specific factors of variation (e.g., attributes or objects). However, these biases are incompatible with other classes of factors” and “Unlike previous methods, which introduce inductive biases tailored specifically to either attribute or object.”
However, the proposed method also requires a choice of mixing strategy tailored to either attributes or objects, which seems like an inductive bias itself, specific to one type of disentanglement. Could this advance choice also be considered a form of inductive bias that is specific to objects or attributes? Likewise, could state-of-the-art methods (e.g., Jung et al., 2024) also be modified to handle both attributes and objects? It’s unclear to me to what extent prior methods are fundamentally "unable" to address both types of disentanglement, as opposed their experiments being focused on of the the two tasks but potentially adaptable to the other in a way similar to how this proposed method can be adapted via choosing an appropriate mixing strategy.

E. In Section 2 the authors make the following comment “in object-centric scenes, the same objects can appear in different spatial locations, complicating the definition of independence metrics for object representations”. It would be great to show qualitatively in examples like Figure 2 what happens when the image contains 2 identical objects and one of them is added or removed from the image. Would the proposed framework work or would there be a confusion among those object. I say this in part out of curiosity and in part because in Figure 3 (right 3rd column for inserting) it seems the model is confusing two similar objects and is adding the one in the back rather then one in the front. Could you provide those qualitative examples (if not possible in the rebuttal then in a potential future version of the paper).

F. I could not find any detail (even in the appendix) about w(t). Could you please provide details about this function for both attribute and object tasks.

G. The authors mention that Jung et al. use a similar prior term but since they use the same diffusion model (as opposed to a pre-trained and frozen one) they are measuring $p(x^c|z^c)$ rather than $p(x^c)$.  I have two comments and questions about this:
1. Even when using a frozen diffusion model, wouldn’t the final decoded image be conditioned on $z^c$? 
2. Regardless, I think this would be a good choice to compare. How does the current framework compare quantitatively to a similar framework that uses the term from Jung et al? Using Jung et al. solution would simplify the framework and reduce the need for training an extra model. Could you provide a comparison between these two options?

H. For the DCI metric the authors say “we perform PCA as post-processing on the representation before evaluation, following (Du et al., 2021; Yang et al., 2023)”. While I appreciate that this has been done before I wonder if it is a fair evaluation of disentanglement when it is applied only to some methods. Shouldn’t each vector $z_i$ be considered one of the “dimensions”. With PCA one is not measuring the disentanglement of each dimension but rather the disentanglement of a rotated version of the linear combination of the dimensions. This does not seem the same. Please help me understand why this makes sense and it is a fair evaluation, or if you agree with me that this is not a fair evaluation please compute and report the DCI score without PCA.

### Soundness
2

### Presentation
2

### Contribution
3

# Sparse Autoencoders Do Not Find Canonical Units of Analysis

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
A common goal of mechanistic interpretability is to decompose the activations of neural networks into features: interpretable properties of the input computed by the model. Sparse autoencoders (SAEs) are a popular method for finding these features in LLMs, and it has been postulated that they can be used to find a \textit{canonical} set of units: a unique and complete list of atomic features. We cast doubt on this belief using two novel techniques: SAE stitching to show they are incomplete, and meta-SAEs to show they are not atomic. SAE stitching involves inserting or swapping latents from a larger SAE into a smaller one. Latents from the larger SAE can be divided into two categories: novel latents, which improve performance when added to the smaller SAE, indicating they capture novel information, and \emph{reconstruction latents}, which can replace corresponding latents in the smaller SAE that have similar behavior. The existence of novel features indicates incompleteness of smaller SAEs. Using meta-SAEs - SAEs trained on the decoder matrix of another SAE - we find that latents in SAEs often decompose into combinations of latents from a smaller SAE, showing that larger SAE latents are not atomic.  The resulting decompositions are often interpretable; e.g. a latent representing "Einstein'" decomposes into "scientist", "Germany", and "famous person". To train meta-SAEs we introduce BatchTopK SAEs, an improved variant of the popular TopK SAE method, that only enforces a fixed average sparsity. Even if SAEs do not find canonical units of analysis, they may still be useful tools. We suggest that future research should either pursue different approaches for identifying such units, or pragmatically choose the SAE size suited to their task. We provide an interactive dashboard to explore meta-SAEs: https://metasaes.streamlit.app/

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper wrestles with the question of whether sparse autoencoders (SAEs) of different sizes learn the same set of "canonical" or "atomic" units. The paper approaches this question from a couple of directions: 

1. First, the authors investigate how SAEs of different sizes can be "stitched" together. They find that some features from a larger SAE, when added to a smaller SAE, improve loss (novel latents), and others make loss worse (reconstruction latents). It turns out that there is a rough relationship between, for a given large-SAE latent, the maximum cosine similarity between that latent and the small-SAE latents, and whether adding that latent improve or huts performance. Latents which are dissimilar from all small-SAE latents improve performance of the small-SAE when added, and latents which are quite similar to a small-SAE latent hurt performance of the small-SAE when added. This makes sense -- "novel latents" are features which the small SAE has not learned, and "reconstruction latents" are features which the small SAE has already represented in some manner. The authors describe a procedure by which latents from a large SAE can be added to a smaller SAE -- novel latents can be added, but reconstruction latents must replace latents in the small SAE. This procedure allows one to interpolate between SAEs of different sizes while continuously improving reconstruction error. Nice! Lastly, the authors note that the "reconstruction latents" are not identical to the latents they replace in the smaller SAE, and also sometimes have high cosine similarity with multiple latents in the smaller SAE. One explanation of this is that some large-SAE latents are in fact linear combinations of multiple latents in the smaller SAE. This calls into question whether latents learned by SAEs are atomic.

2. Second, the authors attempt to decompose SAE latents into more atomic features with "meta-SAEs". Meta-SAEs attempt to represent SAE  latents (decoder vectors) as a sparse linear combination of some smaller set of features. Interestingly, the authors report that many meta-SAE features seem interpretable, and many interpretable latents in the original SAE decompose into interpretable combinations of meta-SAE features! For instance, a dedicated "Einstein" latent from the original SAE can be approximated as a linear combination of meta-SAE latents for "Germany", "prominent figures", "scientist", "space and galaxies", and "starts with E". The authors demonstrate that meta-SAE latents are similar to the latents learned by a similarly-sized base SAE.

For their meta-SAEs, the authors trained a new SAE variant called BatchTopK SAEs. While BatchTopK SAEs are not the main contribution of the paper, the authors test them against standard TopK and JumpReLU SAEs, and find that BatchTopK beat TopK SAEs across settings they evaluated, but don't always beat JumpReLU SAEs. BatchTopK SAEs are not the primary contribution of the paper, but are a nice bonus.

### Strengths
Overall, the paper addresses an important question about SAE features with reasonable experiments and presentation. This issue, of whether SAE features are "canonical" or "atomic", could have implications for how we scale up SAEs and also for how we use their latents for model interventions, circuit analysis, etc. Overall, the presentation in the paper is clear and the experiments are original and well-executed. Some particular strong points:
* I think Figure 5 is quite compelling. It makes a lot of sense that the L0 would rise as novel latents are added, and it's very cool to see continuous curves like this as one "interpolates" between two SAEs.
* I think that Figure 6 is also quite compelling in showing that meta-SAE latents are pretty similar to similarly-sized base SAE latents.

### Weaknesses
 * I could not find reported values of the reconstruction loss that meta-SAEs obtain in reconstructing the base 49k-latent SAE latents. How precisely do meta-SAEs actually reconstruct the latents? If they are only a very weak approximation, what would that say about the hypothesis that large-SAE latents are linear combinations of more atomic latents?
* Some minor grammatical and presentation issues: "vertexes" -> vertices, the left quotation marks in the meta-SAE section should be fixed, etc.

### Questions
* It's interesting that the reconstruction error falls as much as it does when the reconstruction latents are stitched in. If reconstruction latents were exactly linear combinations of more atomic latents learned by the smaller SAE, I'd expect that replacing those atomic latents with the reconstruction latents would yield the same reconstruction error, but at a lower L0. Instead reconstruction tends to fall *more* steeply during reconstruction latent stitching vs. novel latent stitching. Do you have a guess as to how the reconstruction latents relate to the latents they replace? Perhaps they are a combination of the small-SAE latents but with other additional features included too? I wonder if a feature-manifold explanation might also be worth considering here (Engels et al. 2024), where reconstruction features are more densely covering a feature manifold that corresponding latents in the small-SAE are more coarsely covering. In this sort of model, latents aren't just combinations of atomic latents, and maybe there is no good definition of "atomic latent" when features are multi-dimensional. What do you think?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper discusses the use of sparse autoencoders (SAEs) to examine how activations in a transformer relate to concepts in natural language. The authors examine the relationship between small SAEs and larger SAEs (a larger number of latent states) to assess whether larger SAEs contain more fine-grained information. Additionally the authors introduce a sparsity objective that enforces sparsity across a batch of feature vectors, rather than at for individual feature vectors.

### Strengths
The paper attempts to understand how activations deep within a transformer might correspond to higher level natural language concepts. This is an interesting topic. The conclusion is also interesting, namely that sparse autoencoders may not form a complete set of explanations, with larger SAEs potentially containing more fine-grained information.

### Weaknesses
The paper is quite presumptive about readers knowledge of the topic, lacking in clear explanations in places. Whilst the paper does a reasonable job of explaining sparse encoders, it doesn't explain how these are used to find actual "inputs" that activate particular features. This isn't explained in the paper and I had to read the cited papers to understand this. There is some description in section 5.1 (page 8) but this is too late for the reader unfamiliar with this area to understand the paper.

I also found it quite hard to follow the authors reasoning in places and it's not clear to me why stitching might provide insight.  Overall, the methods used in the paper are rather straightforward and I would therefore have hoped for a very clear presentation to make up for a lack of technical contributions. The Meta SAE isn't very well explained and the BatchTopK is idea is simple but now well motivated and it's unclear to me how this connects to the rest of the paper.

Try to be consistent with spelling rather than mix eg color, colour. Also opening parentheses are incorrectly used in places (see lines 369 onwards).

I do think there is something potentially insightful in this work, but the paper needs to be more clearly presented.

*** page 4

I don't really agree with the phrase "circuit". To me this suggests some end to end explanation, whereas the reality is that a small part of a transformer is being examined (the activations in a single layer).

I can't find any information on how the SAE is trained. What is the optimiser and how are the hyperparameters (eg \lambda) set?

*** page 5

Why choose layer 8 of GPT2?

Equation 5 has an asymmetry. Why is the bias from decoder 0 used, rather than decoder 1, or a combination of the two?

The motivation for stitching isn't clear to me. The features and decoders learned are optimised for each SAE separately. Why would combining them in a suboptimal way mean anything? Why not fix the features f0, f1 from each encoder but then learn optimal decoder weights W_{01} for the combination of these feature (this is a simple quadratic optimisation problem). Similarly, in the subsequent discussion, I don't follow why an increase or decrease in MSE is of any significance.

If one wishes to understand whether latents in larger SAEs are finer grained versions of latents in smaller SAEs, would it not be feasible to look at a sentence that coactivates two features, one feature from the smaller SAE and one from the larger SAE?

In figure 5 it's not clear to me what the average L0 means -- what is being averaged over here?

As far as I understand the SAE objective is non-convex, meaning that there is no guarantee of finding the global optimum. It's therefore also quite possible that different SAEs are simply finding different latents simply because of finding different local minima.

Isn't it clear that (local optima aside) a larger SAE will always find features that are missed by smaller SAE? I'm not sure I follow the argument from line 355 onwards.

*** page 8

Please add more clarity around treating the latents W_i^{dec} (why is W in boldface)? W_i^{dec} is a scalar quantity, the ith component of the d-dimensional vector W^{dec}. What does it mean to take scalars "training data for our meta-SAE"? The directions W don't convey information about which directions are simultaneously activated. I would have thought it would make more sense to treat the feature vectors f(x) as the entities for learning a meta SAE.


*** page 9

The BatchTopK function is fully defined. In line 465 it states that the function selects the top K activations, suggesting that this is a mapping from activations to indices. I suspect that the authors mean that the function should return zero for all activations that are not in the top K highest positive values, and is the identity function otherwise.

The introduced batch method is used only during training, with a different non-linearity used during "inference". This seems quite strange and it's not clear to me how to justify this.  A potential issue not mentioned is that it's quite possible that the batch approach means that some input sequences will have entirely zero activation.

It's hardly surprising that the BatchTopK SAE has lower SAE than TopK SAE since BatchTopSAE imposes fewer constraints on the objective. I'm not sure why this would be seen as "outperformance".

I'm also unclear as to why BatchTopK SAE is being discussed. Is this method used in all the previous experiments in the paper, or is this a separate piece of work orthogonal to the other contributions of the paper?

*** page 10

The conclusion "These findings suggest that there is no single SAE width at which it learns a unique and complete dictionary of atomic features that can be used to explain the behaviour of the model." is interesting and (perhaps) not surprising.


*** supplementary material

Figure 11 isn't well explained. Please explain what is being shown here.

### Questions
*** page 4

I don't really agree with the phrase "circuit". To me this suggests some end to end explanation, whereas the reality is that a small part of a transformer is being examined (the activations in a single layer).

I can't find any information on how the SAE is trained. What is the optimiser and how are the hyperparameters (eg \lambda) set?

*** page 5

Why choose layer 8 of GPT2? 

Equation 5 has an asymmetry. Why is the bias from decoder 0 used, rather than decoder 1, or a combination of the two?

The motivation for stitching isn't clear to me. The features and decoders learned are optimised for each SAE separately. Why would combining them in a suboptimal way mean anything? Why not fix the features f0, f1 from each encoder but then learn optimal decoder weights W_{01} for the combination of these feature (this is a simple quadratic optimisation problem). Similarly, in the subsequent discussion, I don't follow why an increase or decrease in MSE is of any significance.

If one wishes to understand whether latents in larger SAEs are finer grained versions of latents in smaller SAEs, would it not be feasible to look at a sentence that coactivates two features, one feature from the smaller SAE and one from the larger SAE?

In figure 5 it's not clear to me what the average L0 means -- what is being averaged over here?

As far as I understand the SAE objective is non-convex, meaning that there is no guarantee of finding the global optimum. It's therefore also quite possible that different SAEs are simply finding different latents simply because of finding different local minima.

Isn't it clear that (local optima aside) a larger SAE will always find features that are missed by smaller SAE? I'm not sure I follow the argument from line 355 onwards.

*** page 8

Please add more clarity around treating the latents W_i^{dec} (why is W in boldface)? W_i^{dec} is a scalar quantity, the ith component of the d-dimensional vector W^{dec}. What does it mean to take scalars "training data for our meta-SAE"? The directions W don't convey information about which directions are simultaneously activated. I would have thought it would make more sense to treat the feature vectors f(x) as the entities for learning a meta SAE.


*** page 9

The BatchTopK function is fully defined. In line 465 it states that the function selects the top K activations, suggesting that this is a mapping from activations to indices. I suspect that the authors mean that the function should return zero for all activations that are not in the top K highest positive values, and is the identity function otherwise.

The introduced batch method is used only during training, with a different non-linearity used during "inference". This seems quite strange and it's not clear to me how to justify this.  A potential issue not mentioned is that it's quite possible that the batch approach means that some input sequences will have entirely zero activation.

It's hardly surprising that the BatchTopK SAE has lower SAE than TopK SAE since BatchTopSAE imposes fewer constraints on the objective. I'm not sure why this would be seen as "outperformance".

I'm also unclear as to why BatchTopK SAE is being discussed. Is this method used in all the previous experiments in the paper, or is this a separate piece of work orthogonal to the other contributions of the paper?

*** page 10

The conclusion "These findings suggest that there is no single SAE width at which it learns a unique and complete dictionary of atomic features that can be used to explain the behaviour of the model." is interesting and (perhaps) not surprising.


*** supplementary material

Figure 11 isn't well explained. Please explain what is being shown here.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the authors introduce two new methods for analyzing latents in SAEs. The first, SAE stitching, enables comparison of latents across SAEs of different sizes by categorizing latents in larger SAEs as either novel or reconstruction latents found in smaller models. The second, Meta-SAE, decomposes decoder directions into interpretable meta-latents They also propose the BatchTopK SAE, a variant of the TopK SAE that forces a fixed average sparsity. By applying these methods, they obtained empirical results that suggest that SAEs are unlikely to learn canonical sets of units.

### Strengths
- The motivation and methods are explained clearly and intuitively, with helpful examples.
- The authors contextualize their approach by discussing relevant state-of-the-art methods.
- Several experiments are conducted to assess the methods' performance, with comparisons to state-of-the-art baselines and detailed experimental information.
- An interactive dashboard is included to explore the latents learned with meta-SAEs.

### Weaknesses
 - Including a discussion on the potential limitations of the proposed approaches would be valuable.
- It would also be helpful to have an expanded discussion on assessing the quality of the representations and adapting the dimensionality of the SAE to suit the requirements of different analyses.

### Questions
- Is there any particular reason to omit the bias term of the decoder 1 in equation 5?
- How does the stitching SAE handle shared reconstruction latents during the swap process? Since some reconstruction latents in larger SAEs are composites, they may contain information from multiple smaller SAE latents. For example, in the case of colored shapes, how would the model swap the "square" or "blue" latent if these are entangled in composite latents in the larger SAE? Would they need to be swapped simultaneously? 
- Would it be possible to introduce some form of supervision in meta-SAEs? Do you have any intuition as to whether this might be beneficial, considering that the ultimate goal is to interpret model activations? Following a concept bottleneck approach, one could directly associate human-interpretable meta-latents with the representations learned by larger SAEs (although I assume the main limitation is defining labels/concepts for the large dictionary sizes considered).
- For BatchTopK, have the authors examined how varying values of k impact the semantics of the learned latents? Do the "concepts" learned under a stronger sparsity constraint become more abstract (as they need to explain a given activation with fewer latents) for a fixed dictionary size?
- Have the authors extracted any intuition on how should the dictionary size be adjusted to tailor the SAE to the requirements of an specific analysis?

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
This research concerns SAE, an assessment tool specialized for GPT-type models, espeically those used as LLM. 
SAE is applied on the activation of LLM to infer the captured information, and at least in this paper, its wellness is 
evaluated based on the MSE of the reconstruction. 
The novelties of of this research are as follows.
1. It proposes SAE stitching, a tool to compare large SAE against Small SAE.  With SAE stitching, one can use the 
change in MSE to assess how the larger SAE's weight direction relates to the smaller SAE's weight direction (intersection of notions), 
as well as the uniquness of the notion captured by the larger SAE. 
2.  It proposes Meta SAE, which applies still another SAE on the top of an already established SAE. It is used to obtain the 
monosemantic latent.
3.  It proposes BatchTopK, a variant of MetaSAE which achieves SOTA in terms of architecture. 
Base on the observations made by these claimed novel technique set, the paper advocates the need to carefully choose the size of the 
SAE as well as the need to compare SAEs of different sizes for more semantically meaningful analysis.

### Strengths
- This research provides thorough and solid experiments that are in alignment with 
those of the original SAE paper. 
- This research furthers the understanding of SAE in application to LLM; considering that SAE is considered an important probing unit in the understanding of how LLM processes the information, this research answers an important question regarding (1) how the probing unit deomposes the LLM activations and (2) how its size and design affects the analysis.

### Weaknesses
 - The reviewer is a little unsatisfied with how the research is positioned. In the introduction and in the abstract, the paper is presented as if the research topic pertains to an analysis of a decomposition of the activations of a "general" neural network into features, while in fact the SAE introduced by [Bricken et al] and [Cunningham et al] is a probing tool for a specific 'organism' that is LLM.  The term 'language model' is mentioned only at the part 3 of the contribution, leaving an impression that the paper investigates a very general feature analysis that is 'also' applicable to LLM.  The research also experiments with LLM exclusively as well. 
While the keyword SAE may automatically link to the behavioral study of LLM in the minds the the readers that are actively involved in LLM behavioral research, the reviewer feels that it shall be clearly stated/emphasized in both the introduction and the abstract that this research is about LLM (which is merely one genre of ML research).  Otherwise, the reviewer believes the applications other than LLM shall be presented in the paper.

- Another concern is that, while the research clearly furthers the understanding of the SAE, an important probing tool for LLM, the research does not relate the claimed novelty to the SAE's probing "capability". For example, [Cunningham et al] quantifies the SAE's ability to localize a specific model behavior in Indirect object Identification (IoI) task, thereby evaluating the goodness of the probing conducted by SAE.  Meanwhile, the paper evaluates the goodness of SAE with the reconstruction error. While the reviewer values the thoroughness of independent experiments, the reviewer also feels that the authors did not intend their study to be interpreted as an investigation of a probing tool for the sake of probing tool itself.  The reviewer feels that the research can be justified if the authors can add analysis of how their new toolset can be used to better the probing capability of SAE in terms of IoI, for example, or to actually better uncover a features that are causally responsible for counterfactual behavior in LLM.

### Questions
1,  Figure 4, it is said that "Features with cosine similarity less than 0.7 tend to improve MSE".  Do you mean 0.6 or less?  In the similar regard, thsi rendency is much less clear in Figure 18.  Would you please make comments regarding GemmaScope32k? It is said that " Using this threshold, we find that our feature stitching methods work on these SAEs as well." Can you elaborate on what is meant by "well" in this context? 

2,  What are "active latents"?  The reviewer presumes that these are the latents that are not "zero-ed out" by the training with the sparsity constraint, but it would help to clarify its precise mathematical meaning.

3, In Figure 6 and experiments regarding this figure, MetaSAE with N latents are evaluated.  Now, the MetaSAE is presented as the application of SAE on the latents of SAE.   Would you please clarify "on what SAEs" the MetaSAE were applied in these experiments? For example, from SAE of what size "the Meta SAE with 2304 latents" was obtained?

### Soundness
3

### Presentation
2

### Contribution
2

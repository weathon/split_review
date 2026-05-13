# MorphGrower: A Synchronized Layer-by-layer Growing Approach for Plausible and Diverse Neuronal Morphology Generation

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
Neuronal morphology is essential for studying brain functioning and understanding neurodegenerative disorders. As acquiring real-world morphology data is expensive, computational approaches for morphology generation have been studied. Traditional methods heavily rely on expert-set rules and parameter tuning, making it difficult to generalize across different types of morphologies. Recently, MorphVAE was introduced as the sole learning-based method, but its generated morphologies lack plausibility, i.e., they do not appear realistic enough and most of the generated samples are topologically invalid. To fill this gap, this paper proposes \textbf{MorphGrower}, which mimicks the neuron natural growth mechanism for generation. Specifically, MorphGrower generates morphologies layer by layer, with each subsequent layer conditioned on the previously generated structure. During each layer generation, MorphGrower utilizes a pair of sibling branches as the basic generation block and generates branch pairs synchronously. This approach ensures topological validity and allows for fine-grained generation, thereby enhancing the realism of the final generated morphologies. Results on four real-world datasets demonstrate that MorphGrower outperforms MorphVAE by a notable margin. Importantly, the electrophysiological response simulation demonstrates the plausibility of our generated samples from a neuroscience perspective.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present MorphGrower, a model for neuron morphology generation based on reference morphologies as inputs. Their method features conceptual advances over the previous state of the art in the field, MorphVAE. A comprehensive evaluation suggests that these advances yield considerable benefit across a range of quantitative measures of performance.

### Strengths
MorphGrower constitutes a significant advance in learning-based neuronal shape generation compared to the pioneering MorphVAE. In particular, MorphVAE generates neurons by sampling soma-to-tip branches and agglomerating a set of such branches via threshold-based node merging. This can yield topologically infeasible morphologies; Furthermore, agglomeration by averaging node positions has a smoothing effect which is detrimental to the yielded shape variability.
To counter these deficiencies, MorphGrower generates shapes recursively, "layer by layer", where "layer" refers to branch distance from the soma (where a "branch" spans from bifurcation or soma to bifurcation or tip). By recursion, an encoding of the local path to a current branching point as well as an encoding of the full previous layer is fed as condition to a branch pair encoder and -decoder.

### Weaknesses
MorphVAE provides an embedding for whole neuronal morphologies (via pooling of walk embeddings), which can be leveraged for shape clustering and cell type classification. This feature is not straightforwardly contained in MorphGrower as the respective encoder operates recursively on neuron branches. While MorphGrower is clearly pitched as focusing on neuronal shape generation, an explicit discussion of the aforementioned distinction in scope from MorphVAE would still be helpful for the reader.

While the provided evaluation of neuronal shape generation is comprehensive and shows clear benefits of MorphGrower over MorphVAE, it would still be beneficial to also report the shape characteristics statistics employed in MorphVAE (cf. their Fig. 5). Furthermore, it appears that MorphVAE has been re-trained by the authors with hyper parameters different from the original model, which are then however applied to (partly) the same date -- would it be possible to directly use the resp. models trained by the MorphVAE authors, or at least their exact hyperparameters?

For the branch pair decoder, it would be helpful if you could discuss respective permutation equivariance -- do you include both orders of each branch pair during training to train towards equivariance? or is the architecture inherently permutation equivariant? (if so this is not straightforwardly obvious)

In your comparative evaluation vs MorphVAE, it would be beneficial if you could provide a more comprehensive discussion of hypotheses regarding the sources of the observed differences. E.g., MorphVAE caps walk lengths, which clearly entails an underestimate of some of the measures you evaluate, yet this source of underperformance is not discussed.

### Questions
Would it be possible to directly use the models (or at least hyper parameters) employed by the MorphVAE authors, at least for your comparative evaluation on data also used in the MorphVAE work?

Could you extend your evaluation of morphological statistics to the measures evaluated in the MorphVAE work?

Furthermore, please explicitly discuss the distinct scope of MorphGrower vs MorphVAE.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- S1. MorphVAE encoded sequences of arbitrary number of consecutive vertices along a branch with an LSTM to learn a fixed length representation. It also used an LSTM to generate a new branch conditioned on that representation. 

 - S2. As I understand, the proposed neuron generation method is:

    1. initialize `active_vertices` with soma vertex
    2. at each step, generate two branches, conditioned on already generated graph
    3. generated branches are allowed to be null.
    4. replace `active_vertices` with tips of non-null generated branches
    5. repeat 2 $\rightarrow$ 4 until `active_vertices` is empty

 - S3. Conditioning on the already generated graph requires a fixed length representation of a graph. Authors propose to do this in 2 ways:

    1. _global context_ aggregates fixed length branch-level representations at different branch orders $\dagger$

    2. _local context_ uses a discount scheme to weigh contribution at different branch orders. 

 - S4. MorphVAE combine "walks" (sampled branches) with a heuristic procedure to construct a neuron tree. 

 - S5. This manuscript uses a similar scheme to generate branches, but proposes a recursive procedure to generate the neuron tree. 

 - S6. Authors provide a comparison of trees generated by either method based on 4 datasets.

### Strengths
- Manuscript builds on ideas in MorphVAE and proposes a meaningful extension.
 - The auto-regressive scheme of generating morphologies is interesting, and perhaps a good direction to think about the problem of generative models for neurons.

### Weaknesses
 - W1. The writing and notation would benefit from being more concise and self-contained. For example, various metrics are only referred to by their acronyms in the main text. Separating the biological motivation/justification in a single paragraph instead of describing it after each method step would also help towards this end. Some symbols aren't introduced at all. 

 - W2. The proposed method seems to be so over-fit to training data, that the morphologies hardly differ from the given sample (e.g. examples in Fig 4a-c., and also Fig. 23-26)? Is this not a major problem?

 - W3. Building on W2., consider a _model_ that simply jitters branch points of the reference morphology by a small amount. Based on evaluations presented in the manuscript, this procedure would
    - obtain near-perfect match on the metrics in Table on p.7.
    - match distributions in Fig. 3
    - be hardest to distinguish for classifiers (Sec. 4.3)
    - have higher BlastNeuron distances with simple heuristics (e.g. deletion of small fraction of terminal branches)

    From the manuscript and the metrics chosen to justify the generated morphologies, it is unclear to me why one should prefer the proposed method over this simple procedure to generate morphologies. 

 - W4. The language is often not careful; some strong biological claims are made that are not well substantiated. Examples:

    > Since the neuronal morphology is static, the generation order of the branch pairs in each layer does not matter.

    > Remark. A typical neuron is comprised of a soma, dendrites, and an axon. Dendrites perform a random walk from the soma, while the elongation and bifurcation of axons exhibit specificity.

### Questions
- Q1. If the intention is to also use such models to study morphology as it relates to neuronal development, the following view should probably be reconsidered?
    > Since the neuronal morphology is static, the generation order of the branch pairs in each layer does not matter.

 - Q2. It looks like a typo (should be 3 instead of 3k), but just to make sure please clarify:
    > Most nodes on the tree have no more than 3k k-hop neighbors, thereby limiting the receptive field of nodes.

 - Q3. I assume $k$ here refers to the depth of the tree?
    > For a branch $b_i$, its corresponding node feature at the k-th iteration $\hat{h}(k)$ is calculated by

 - Q4. $\textbf{r}_{b_i}$ is not defined in the section on global context.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a generative model for neuronal morphologies (in skeleton form), implemented as a conditional VAE with an LSTM encoder/decoder. Neurons are grown using an autoregressive sampling procedure inspired by natural growth processes. The proposed model is shown to consistently perform better than MorphVAE (the only other deep learning-based alternative) under multiple metrics and for different tissue samples.

### Strengths
- The idea to generate branches progressively is interesting and makes intuitive sense.
- Terminology is clearly defined and illustrated in Sec. 2. 
- The authors promise to release the source code of their method.
- Evaluations show consistently improved results in comparison to MorphVAE.
- In addition to morphological metrics, a classifier-based approach is used to verify plausibility and BND to evaluate diversity of the generated morphologies.

### Weaknesses
 - Ablations of MAE and local/global conditioning are relegated to an appendix and restricted to a single dataset. Please consider including and discussing them in the main text. Perhaps some of the formulas for the LSTMs could be moved to the appendices to make space for this.

 - The importance of neuronal morphology for diseases such as Alzheimer's feels out of place in the abstract. The statement itself is true of course, but it's unclear how having a computational model of such morphologies would make studying these diseases any easier. I suggest replacing it with some other potential applications.
- In the global condition, are the non-branch coordinates completely discarded or still used somehow?
- In section 3.3 describing the sampling procedure a "reference morphology T" is described. Does that mean that the sampled neurons will always have the exact same tree structure as T?
- Have you performed any studies on the impact of the embedding size? (both for your model and MorphVAE). This hyperparameter does not appear to be explored much in the text.
- Does Fig. 4 suggest overfitting? How is it possible that the generated neurons remain so close to the original morphology?

### Questions
- The importance of neuronal morphology for diseases such as Alzheimer's feels out of place in the abstract. The statement itself is true of course, but it's unclear how having a computational model of such morphologies would make studying these diseases any easier. I suggest replacing it with some other potential applications.
- In the global condition, are the non-branch coordinates completely discarded or still used somehow?
- In section 3.3 describing the sampling procedure a "reference morphology T" is described. Does that mean that the sampled neurons will always have the exact same tree structure as T?
- Have you performed any studies on the impact of the embedding size? (both for your model and MorphVAE). This hyperparameter does not appear to be explored much in the text.
- Does Fig. 4 suggest overfitting? How is it possible that the generated neurons remain so close to the original morphology?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

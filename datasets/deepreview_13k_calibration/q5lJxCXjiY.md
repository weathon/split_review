# GEOMETRIC SIGNATURES OF COMPOSITIONALITY ACROSS A LANGUAGE MODEL’S LIFETIME

- Decision: Reject
- Avg Score: 5.40
- Scores: 8, 3, 6, 5, 5

## Abstract
Compositionality, the notion that the meaning of an expression is constructed from the meaning of its parts and syntactic rules, permits the infinite productivity of human language. For the first time, artificial language models (LMs) are able to match human performance in a number of compositional generalization tasks. However, much remains to be understood about the representational mechanisms underlying these abilities. We take a high-level geometric approach to this problem by relating the degree of compositionality in a dataset to the intrinsic dimensionality of its representations under an LM, a measure of feature complexity. We find not only that the degree of dataset compositionality is reflected in representations' intrinsic dimensionality, but that the relationship between compositionality and geometric complexity arises due to learned linguistic features over training. Finally, our analyses reveal a striking contrast between linear and nonlinear dimensionality, showing that they respectively encode formal and semantic aspects of linguistic composition.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper analyses the representations of the last token in sentences from a pidgin language constructed by the authors. 

Specifically the authors vary three things on the network side and two things in the input:

1. network training progress: Networks trained for longer are supposed to be better/sophisticated
2. network layer: Later network layers are supposed to be more important for "semantics" compared to "form"
3. Network size: Representations from bigger networks are supposed to be "better"
4. sentence word order: This is quantified as a binary variable, whether sentences are shuffled therefore destroying "semantics" or not
5. inter-word coupling: The variation in input sentence's complexity due to coupling adjacent words is quantified by using gzip compressed size to estimate the Kolmogrov complexity.

They randomly sample sentences from their pidgin language and they measure two statistics for the last token's embedding vector 
1. Two nearest neighbor estimator for manifold dimension: An estimate of the dimensionality of the non-linear manifold under some assumptions.
2. PCA dimensionality for 99% variance: The dimensionality of the linear subspace

So we can now imagine a 7-column dataframe with 5-dimensions and 2-measures and the paper presents various interesting observations. 

The main claim from the authors are that: 1) "PCA dimension" of final token representation is a good estimate of kolmogrov/combinatorial complexity, 2) "TwoNN dimension" is a good estimate of "semantic" complexity. 3) The TwoNN complexity vs layer curve is a good predictor of how well the network is trained. If TwoNN complexity is higher for later layers then the model is trained well otherwise not.

### Strengths
The experiments in this paper are quite interesting, novel and certainly thought provoking. This paper presents correlates statistics of LLM representations to input complexity, and it disentangles input complexity into "form" and "meaning" which is a very neat idea. The paper is well-written and clearly organized. The introduction provides a strong motivation for the research and effectively sets the stage for the key questions addressed.

### Weaknesses
This is a tough paper to assess because the connection between the conclusions and claims in the paper , and the actual experimental observations is a bit speculative.

For example, one of the claims is that shuffling words destorys any semantic information and therefore the TwoNN dimensionality is lower when we shuffle words, compared to when we do not. But this phenomenon is observed for 3 out of 4 settings, and the red curves in figure 2 where words coupled are 4 do not show that behavior. The authors do not provide a clear explanation for this discrepancy, raising concerns about the robustness of their claims. Furthermore, the reliance on a single, albeit novel, pidgin language limits the generalizability of the findings. The specific structure and constraints of this language might introduce biases that are not present in natural languages, making it difficult to extrapolate the results to more realistic scenarios. The paper also lacks a thorough investigation into the sensitivity of the TwoNN dimensionality measure to various parameters, such as the number of neighbors considered or the distance metric used. Without such an analysis, it is hard to ascertain whether the observed trends are genuine or artifacts of the chosen methodology. The paper also does not explore the potential impact of different tokenization strategies on the final token embeddings, which could influence the measured dimensionality.

The main issue is that this is a highly empirical paper and there is a danger that the results come from "data fishing" by slicing and dicing a fairly complex dataframe. The overall story is plausible and definitely thought provoking but I am not sure how conclusive the evidence in the paper is.

Despite these weaknesses, I think the ideas in the paper are certainly very interesting, even though

### Questions
The phase transition in figure three seems to explain performance for only a few tasks such as SciQ, ArcEasy, Lambada, and PIQA but not for other tasks. Why do you think that is?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors empirically explore compositional language model representations, and how these representations change during training by using stored checkpoints from the Pythia models; outcomes are measured using three different model sizes.

The authors rely on two datasets to measure this. The first is a completely synthetic dataset with unspecified distributional properties from an artificially limited grammar of fixed length. The second consists of randomly selected passages from the Pile, selected without consideration of any reasonable boundaries, and again of a fixed length.

Using the representation of the last token as a proxy for the whole token sequence, the authors try to measure the dimensionality of these datasets, both linearly using PCA and in a non-linear fashion using TwoNN to estimate intrinsic dimension.

The authors then compare model dimension vs empirical data dimension, intrinsic dimension during training, and dimension by layer, drawing some conclusions from these empirical experiments.

### Strengths
The exploration of changing dimension across checkpoints was interesting; that felt original.

Some explanation of dimension was relatively clear.

Figure 3 – the change in iD is interesting over epochs; there are phase transitions at points that seem to occur at similar points in training.

### Weaknesses
Ostensibly the paper explores compositionality, but the definition of compositionality and its experimental setup were unusual and not well connected to linguistic notions of compositionality. Given datasets that feel unrepresentative of real language distributions, any conclusions drawn from this dataset are unlikely to apply to any real NL data. Furthermore, it was not clear to me how the experiments attempted to measure compositionality.

I had quite a few clarity issues about how the data was constructed, and I felt the authors leapt to conclusions about from relatively scarce data.

In detail:
* The first dataset is a very limited Controlled Grammar – much weaker than even a probabilistic context free grammar. As such, it feels like a very limited exploration into actual linguistic phenomena. I would have expected that a study of compositionality would relate the representation of parts (e.g. words or phrases) to larger constructions (e.g. sentences or paragraphs).
* The authors describe briefly “composition of forms” vs “composition of meaning” – I found these notions unclear, not well connected to any linguistic or ML definition of compositionality. This should either be explained more fully or a citation should be provided.
* The authors say that k contiguous words are coupled during sampling, but they do not describe the sampling distribution.
* Also, I’m not sure how this is supposed to measure compositionality. I could imagine an experiment to evaluate whether changes in nationality or in job led to systematic and predictable differences in the constructed representation, but that was not present.
* From a linguistic standpoint, sampling 16 contiguous tokens is strange. The 16 contiguous tokens might span sentences, paragraphs, etc. Hence even the real data felt unclean and not representative.
* I was concerned about using the last token as a choice to represent the entire sequence. Although it is true that is the only token that can attend to all positions, there is nothing in the training objective that encourages it to represent the complete sequence. Subsequent tokens can attend to any position.
* Figure 2 – it’s odd to me that shuffled distributions have lower intrinsic dimensionality, even in the unigram case. I would have expected the dimensionality would be higher in the case of shuffling, as the data has fewer constraints.

### Questions
* What is the sampling distribution and process for generating data? Is an n-gram language model used? Or a neural model with a given window?
* Why not sample utterances from The Pile that are whole sentences instead?
* Why use the last token as the representation? Did the authors evaluate how well that reflects the earlier tokens in the string? Could, for instance, the original string be reconstructed with reasonable likelihood given this representation?
* Figure 2 – is this mostly telling us something about the dimension from which the data was sampled? What happens to these numbers if the number of categories is changed?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of the paper is to relate compositionality to high-level dimensionality heuristics. For that the authors create a dataset with sentences syntactically identical sentences using a simple grammar. They extend such dataset by modifying its combinatorial complexity by correlating different numbers of words within the sentences. The authors also create a shuffled version of the dataset also with different combinatorial complexity levels which they use as control throughout the paper.

The paper finds that linear dimensionality is a proxy for form whereas nonlinear dimensionality encodes meaning. This is supported by a large set of experiments on models from the Pythia family, evaluated on both the controlled dataset and The Pile.

### Strengths
1. **Clarity and Organization**: The motivations, research questions, and methodologies are presented clearly
2. **Comprehensive Literature Review**: The literature is thoroughly reviewed, framing the research well in the context of existing work on compositionality and intrinsic dimensionality.
3. **Extensive and Organized Results**: The paper includes a large set of results, which are mostly well presented.

### Weaknesses
1. **Model Choice**: 
   - The paper uses Pythia, which is not state-of-the-art (SOTA), though it does have the advantage of available checkpoints.
   - It would strengthen the paper to include SOTA models, such as those from the Llama or Mistral families, to see if the findings generalize to the most current models.
   - **Suggestions**: Run experiments on a final checkpoint for the SOTA models. Observing differences across layers in shuffled versus unshuffled data, along with gzip correlation results.


2. **Dataset Limitations**: 
   - The controlled dataset is restricted to a single syntactic structure, which may limit the generality of the findings.
   - To explore the effects on a more diverse linguistic structure, it would be useful to introduce additional syntactic forms, where compositionality varies by grammar rather than by word correlations.
   - **Suggestions**: Extend the dataset to include varied syntactic structures that capture additional linguistic features, such as syntactic depth, constituent length, and sentence length, and observe how linear and nonlinear dimensionality metrics respond to these variations.


3. **Literature Integration**: 
   - The paper does not adequately address previous work on linear probing and syntactic encoding in linear subspaces (such as Hewitt and Manning, 2019).
   - **Suggestions**: Discuss the relevance of linear probing work, which demonstrates that syntax is encoded in a linear subspace, to the findings here.

### Questions
1. **Interpretation of Dimensionality Collapse (Figure G.4)**:
   - There is a collapse for \(d\) around checkpoint \(10^4\) in models with 1.4b and 6.9b parameters, but not for “The Pile.”
   - **Question**: What does this collapse represent? Does it indicate that the phase transition for encoding meaning occurs earlier than for encoding structure?

2. **Choice of Aggregation Over the Last Token**:
   - The paper states, “We aggregate over the sequence by taking the last token representation, as, due to causal attention, it is the only to attend to the entire context.”
   - **Question**: Why did you choose this aggregation method instead of tracking dimensionality metrics (Id and d) incrementally for all tokens within the sentence?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the relationship between compositionality and the geometric complexity of language model (LM) representations as a function of the data. Using a controlled dataset with varying levels of compositionality and the Pythia models, the authors explore how intrinsic dimensionality and linear effective dimensionality  change with input compositionality.

### Strengths
- The premise is novel and investigates the impact of the degree of compositionality in linguistic input to the intrinsic dimensionality of its representation manifold in LMs.
    
- Comprehensive analysis of dimensionality measures: The study examines both linear (d) and non-linear (Id) dimensionality measures and how they change with input.
    
- The study employs a well-defined experimental setup with a custom dataset designed to control compositionality and investigates multiple Pythia model sizes.

### Weaknesses
 - The discussion of the core concept of compositionality, on which the paper is based, is quite shallow and scattered. Both the introduction and background sections talk about a bottom-up concatenative notion of compositionality (Frege, Chomsky etc) which has been considered unsuitable for discussing compositionality for connectionist architectures (Smolensky 1987, Van Gelder 1990, Chalmers 1993). The investigation of compositionality would require proper characterization of the concept itself.
    
- The distinction between form vs meaning compositionality needs to be motivated better. Compositionality is about discovering the underlying structure of data (and bottom-up concatenation is just a mere product of this process) so the distinction between compositionality of form and meaning doesn’t make sense in this context since the former is not a representation of compositionality in any sense but rather some kind of a type-token ratio/word statistic tracker.
    
- On line 107, it mentions “compositionality of inputs” but this phrase is somewhat vague. Different kinds of syntactic and semantic characteristics of inputs are manipulated in the input, but how do these features relate to compositionality?
    
- For form compositionality, Kolmogorov complexity is used, but why? The decision needs to be justified.
    
- In lines 227-229, the claim seems like a leap. If we cannot define or quantify semantic complexity (line 226), how do we ascertain a link to ID in models just by a comparative measure? Meaning complexity can and should be quantified to make claims based on what aspects of model representations track form vs. meaning complexity.
    
- The use of the transformer’s residual stream for analysis is common but it is also one of the most non-privileged in terms of basis according to a lot of mechanistic interpretability literature (Elhage et al 2021 etc). Other representations of different components (Attention, MLP) could be used here instead.

### Questions
- Could you provide a more thorough characterization of compositionality as it pertains to connectionist models? How does your understanding align with or diverge from foundational perspectives (e.g., Smolensky, Van Gelder, Chalmers) on compositionality in connectionist architectures? How does the definition of compositionality you use set the foundation for your investigation and analyses throughout the paper?

- Could you clarify and justify the distinction you make between compositionality of form and meaning? What theoretical or empirical motivation supports this separation? Could you explain why tracking form (e.g., type-token ratio) should be considered a component of compositionality rather than a separate linguistic metric?

- Why did you choose Kolmogorov complexity as a metric for form compositionality? What specific advantages does it offer for assessing compositionality, and how does it relate to the core concept of structure discovery?

- Could you elaborate on the reasoning behind linking semantic complexity to Identification (ID) in models, particularly in the absence of a clear semantic complexity metric? Is there a way to quantitatively define or approximate semantic complexity to strengthen claims about its relationship with model representation?

- Why did you prioritize the transformer’s residual stream for your analysis? How does it align with or diverge from the representational basis recommended in mechanistic interpretability literature? Have you considered incorporating other components, such as Attention or MLP layers, into your analysis?

### Soundness
2

### Presentation
2

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
This paper evaluates the intrinsic dimensionality (linear and nonlinear) of causal language model representations throughout pretraining, for datasets including form composition (combinatorial complexity) and meaning composition (semantic complexity). The models exhibit similar nonlinear intrinsic dimensionalities across model sizes, although linear intrinsic dimensionalities increase for larger models. There is a phase change in nonlinear intrinsic dimensionality around when the models start increasing in performance on several downstream tasks. Linear intrinsic dimensionality is generally larger for shuffled sentences (indexing combinatorial complexity), while nonlinear intrinsic dimensionality is larger for unshuffled sentences (indexing semantic complexity).

### Strengths
1. The methods used to measure linear and nonlinear intrinsic dimensionality are well motivated by previous work.
2. The results are interesting, demonstrating the dichotomy between linear intrinsic dimensionality and nonlinear intrinsic dimensionality, where the former indexes combinatorial complexity and the latter indexes semantic complexity.

### Weaknesses
Overall, the results are quite interesting, but some of the framing and terminology could be slightly misleading:

1. The paper distinguishes between "form compositionality" and "meaning compositionality". Most existing work on compositionality defines compositionality as what this paper calls "meaning compositionality" (constituent meanings combine systematically to produce sentence meaning). "Form compositionality" in the paper, measured by the number of unique word combinations, might not be considered "compositionality" by standard definitions. It might be more intuitive to simply refer to "form compositionality" consistently as "combinatorial complexity".

2. The paper focuses on the intrinsic dimensionality in the models for combinatorial complexity (form, e.g. shuffled sentences) and semantic complexity (meaning, in the unshuffled sentences). The paper doesn't seem to focus much on compositionality itself, i.e. how meaning is constructed from form. Thus, the consistent use of the word "compositionality" could be misleading.

3. "But, as sane sequences are grammatical and semantically coherent, it is guaranteed for sane datasets that meaning complexity is monotonic in form complexity. In addition, as shuffling removes sequence-level semantics, meaning complexity is guaranteed to be lower on shuffled compared to sane text, by definition" (p. 5). These sentences implicitly assume a definition of "meaning complexity". E.g. increasing form complexity does not necessarily guarantee an increase in meaning complexity (e.g. "It is possible that rain will occur today" vs. "It might rain today"), and defining shuffled sentences to be "low meaning complexity" is up to the definition of meaning complexity. These assumptions still seem safe for the conclusions in the paper, but the assumption of this specific definition of semantic complexity should be noted.

4. Minor point: "Our stimulus dataset consists of grammatical nonce sentences from the grammar illustrated in Figure 1" (p. 3). In linguistics, nonce sentences usually refer to grammatical but semantically incoherent sentences, rather than semantically coherent sentences as in this dataset. Removing the word "nonce" might be more clear.

5. Minor note on terminology: calling the unshuffled sentences "coherent sentences" or "original sentences" would be more in line with existing work than "sane sentences".

### Questions
1. Rather than an effect of lower semantic complexity, could the low nonlinear intrinsic dimensionality of shuffled sentences simply be because they're out of distribution? E.g. the model would likely allocate more "representation space" to in-distribution data (i.e. the unshuffled/coherent sentences). Then, a parsimonious explanation of the results could just be that lower k for unshuffled sentences increases nonlinear intrinsic dimensionality due to broader in-distribution semantic diversity, but the effect is not seen for shuffled sentences because those sentences are out-of-distribution (i.e. not allocated space in the model anyways).

### Soundness
2

### Presentation
2

### Contribution
3

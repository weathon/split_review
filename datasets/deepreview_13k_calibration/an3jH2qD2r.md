# The Geometry of Tokens in Internal Representations of Large Language Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
We investigate the relationship between the geometry of token embeddings and their role in next token prediction within transformer models. Toward this goal, previous studies have utilized metrics such as intrinsic dimension and neighborhood overlap to probe the geometry of internal representations, where prompts are summarized as a single point in representation space. We expand single points to point clouds by investigating how models geometrically distribute tokens in their internal representations. We measure the intrinsic dimension, neighborhood overlap, and cosine similarity on these point clouds for a large number of prompts. 
To validate our approach, we compare these metrics to a dataset where the tokens are shuffled, which disrupts the syntactic and semantic structure. Our analysis reveals a correlation between the geometric properties of token embeddings and the cross-entropy loss of next token predictions, implying that prompts with higher loss values have tokens represented in higher-dimensional spaces.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work explores the geometry of transformer models using a few metrics (cosine similarity, nearest neighbors overlap between layers, and ID). They also see how these metrics change as the text data becomes more shuffled.

### Strengths
The paper is clearly written, and the plots are clear. The experiments seem sound and well-executed. In general, this is an interesting topic– how can we measure the geometry of the model, and how does it relate to the inputs/outputs?

### Weaknesses
My main criticism of this work is that it is missing motivation. Like I said, I do think that this is an interesting area. However, I am not sure what the takeaways are, or what one should do with the information that these metrics change in specific ways. Other than the “correlation between ID and loss” experiment, are these observations connected to model behavior or control?

I appreciate the desire to formalize methods mathematically, but I think some of it can be removed for readability (e.g., the definition of cosine similarity)

There is a lot of missing related work analyzing the geometry of transformers, e.g., probing, David Bau’s work, the recent mechanistic interpretability work, etc. I’m not saying you have to go into great detail here, but it would be good to mention that these areas exist and contextualize your work within them.

Nits:
Some of your citations are from ArXiv, but were later published in peer-reviewed venues (e.g., Intrinsic dimension of data representations in deep neural networks was a NeurIPs paper). Consider swapping out references when possible.

“Model transformers” → “transformer models”? (in the related work section titles)

The ID section (and each section for your metrics) could benefit from a diagram to provide some intuition.

The “shuffling method” might be better explained by a diagram than pseudocode.

### Questions
“if the model is trained on a dataset that contains the input prompts, then it shows lower ID peaks and higher NO, suggesting better adaptability”--> I was a little confused about this. Adaptability to what?

“The calculation of intrinsic dimension has a long history of successful estimators of various types” → I’m having trouble parsing this. Do you mean “there are various good estimates of ID”?

### Soundness
4

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
The paper considers several questions relating to the geometry of LLM embedding spaces across layers, using intrinsic dimensionality (ID), neighborhood overlap (NO), and cosine similarity to study and characterize LLM embedding geometry. Extensive experiments are performed across three leading open-source LLMs and variable levels of noise applied to inputs (by shuffling), yielding several key results: ID usually peaks in early to middle LLM layers; inputs that are out-of-distribution (OOD) with respect to LLMs show higher ID peaks and lower NO; and average cosine similarity between tokens in each layer increases with noise (i.e., with a higher shuffling index).

### Strengths
The paper is generally quite well-written, and performs extensive and thorough experiments across several geometric measures, LLMs, and levels of noise (shuffling) applied to inputs. All experiments are methodologically sound, and most are original and offer novel results. While there are a number of key questions and potential weaknesses of the paper (as discussed below) -- most importantly, that the motivation and contribution are not clear -- it seems plausible that the approach and findings of this work could be significant if these issues are resolved.

### Weaknesses
The primary weakness is that **the motivation and contribution of the presented analysis is not clear.**
- At a high-level, the general motivation for improving our understanding of LLMs *by studying the geometry of their embedding spaces* is not clear. That is, how would our broader understanding of LLMs or other foundation models be advanced by studying the geometric properties considered in this work? For example, at a foundational level, are there questions about how or what any given LLM has learned from its training data that could be answered on this basis, or could predictions be made about likely behaviors (outputs)? Or at an applied level, are there elements of LLM training or deployment that could be improved given the findings of this work?
- At a lower-level, the specific importance of the studied properties (ID, NO, and cosine similarity) is not clear, nor is it clear why LLMs are studied at different levels of noise (shuffling) applied to inputs. There are also other more detailed questions about experiments that need to be clarified, as discussed in more detail below.
- (Note: while some brief thoughts regarding the motivation are laid out in the last paragraph of the conclusion, they are incomplete; and this also needs to be made clear early on in the paper (i.e., in the introduction), as otherwise, on a single forward pass of the paper, it's impossible to interpret or contextualize the results throughout the paper.)

Additionally, **most of the experiments and results are not contextualized with respect to prior work** in this area. That is, with the exception of two experiments -- cosine similarity (sec 4.2.1) and "correlation between ID and loss" (end of sec 4.3) -- it is not clear how the design and findings of each experiment relate to those of prior work, hindering the reader's understanding of the contribution offered by this work and its potential impact on the broader research literature.

Finally, **most of the broader literature studying the internal representations learned by LLMs is not discussed as related work.** Only a narrow sliver of work studying LLM geometry is mentioned -- i.e., work studying embeddings as particle systems, or according to ID, NO, or cosine similarity -- but there are other broad and longstanding bodies of work (such as probing, circuit discovery, feature attribution, etc.) that also aim to mitigate the "black box problem" and understand the internals of foundation models such as LLMs. (For a few relevant surveys of such work, see, e.g., https://arxiv.org/abs/2408.05859 or https://arxiv.org/abs/2404.14082 -- I will refer to this broad category of work studying the black box problem of foundation model internals as "mechanistic interpretability", or MI for short.) While it is not necessary to summarize all such work in detail, and entirely appropriate to focus on the most relevant work studying embedding geometry, it is nonetheless important to position this work in the broader literature working toward understanding LLM representations -- otherwise, as noted above, the contribution and broader impact of this work is not clear.
- I suggest that, at minimum, a brief overview of (1) what is studied in MI, and (2) the relationship between MI and the geometric questions studied here, should be discussed.
    - In the ideal case, it would also be useful to discuss what insights could be provided by the kind of geometric analysis considered in this work that are *complementary* to MI, that could *validate or contradict* key findings in MI, etc.
    - E.g., there is currently a hot debate in MI over "how linear" LLM representations are -- see, e.g., https://arxiv.org/abs/2406.01506 and https://arxiv.org/abs/2405.14860. While it is of course not the goal of this paper to address such questions, I am sharing this context to provide a typical example of how questions around embedding geometry are discussed in MI, which might be useful for the authors in contextualizing their work.

I also noticed a few minor errata:
- line 183: typo/missing words
- sec 4.2.3: need to mention which figure is being discussed -- it is all in reference to Figure 4, correct?
- line 487-489: incomplete sentence

Finally, I would like to note that -- given that the experimental work carried out in this paper is quite good, and these weaknesses are primarily a matter of framing, clarity of contribution, providing adequate context, etc. -- I am quite open to raising my rating if the authors are able to address the above weaknesses and answer the questions provided below.

### Questions
In addition to the most important questions inherent in the weaknesses highlighted above (e.g., what is the motivation, relationship to experiments/findings of the most closely related work, relationship with MI more broadly, etc.), there are a number of other questions that need to be answered, which I will list by category below.

Conceptual questions:
- Why is it meaningful to "progressively disrupt the syntactic and semantic structure" of text by increasing the amount of token shuffling? What would we expect to happen as text is shuffled? And why do we care about this, given that there is no reason that one would expect texts to be shuffled before passing them to LLMs?
    - While there is some discussion on this topic in lines 490-494, it does not answer any of these questions -- that is, while naturally one would expect cosine and ID to change when we shuffle the input, why is this an interesting/important finding? Why is "further probing of these distributions and their relation to the model's processing dynamics" essential?
- How do the approaches studying embedding geometry from the perspective of "particles in dynamical system" (Geshkovski et al., 2023; Cowsik et al., 2024) relate to this work?
    
Experimental design:
- Why are there 50 prompts maximum for all experiments in sec 4.2 (but not 4.3)? This is an exceptionally small-sample experiment in context of LLMs and the Pile dataset being sampled from -- is the number being kept so small because one or more of the experiments is particularly computationally expensive? If so, which ones, and what is the main bottleneck? Do we expect results to look similar for a larger sample?
    - Additionally, how how are the 50 prompts sampled from the 2252 prompts after filtering (per line 190-191)? If the sampling is not purely random, then the sampling procedure must be explained and motivated.
- A major motivator for experiments in sec 4.3 is that the Pile is used to train Pythia but not Mistral or LLAMA; but is it actually public information whether the Pile was used to train LLAMA 3 8B or Mistral? This uncertainty could carry major implications for the findings in sec 4.3. (Per the model papers cited by the authors in sec 4.1, neither model's training data is disclosed; and my understanding is that this information has not been made public since the original model papers, either.)
    - If I am correct and it is not known whether either model is trained on the Pile, then this should be made clear in the paper (both in sec 4.1 and the uncertainty this carries for the results throughout sec 4.3); and otherwise, any source disclosing these models' training data should be cited.

Findings:
- In figure 5, why do we see lower ID for Pythia versus the other models (as expected) for layers 1-20, but higher ID in later layers?

Clarifying questions:
- On line 107, it is claimed that the study of data manifolds has been explored "in search of the geometrical signatures of generalization." What does this mean? What are "geometrical signatures of generalization", and how are they relevant to this paper?
- Regarding "intrinsic dimension" experiments:
    - What do n1 and n2 denote? (See, e.g., line 142-146)
    - What the "known result for the TWO-NN estimator"? What assumptions are made in obtaining this result, and are they appropriate in this context? How is this known result relevant to the experiments carried out in this work (e.g., how is it "exploited")?
    - Are all ID results presented throughout the paper obtained using GRIDE, or do the authors modify GRIDE in any way (or use procedures developed in other works) to compute ID?
- Regarding the shuffling algorithm:
    - Are the order of blocks being permuted, or is it the order of tokens inside each block? (The experiment only makes sense to me in the second case, but it would be good to explicitly state this.)
        - In the first case, then in line 238-240, what do we mean that "S = 0 corresponds to no shuffling?" Wouldn't the "randomPermutation(blocks)" operation in Alg 1 mean that "S = 0" means that the entire thing is shuffled?
        - In the second case, for how many blocks are the order of tokens in the block permuted? (Presumably all blocks?)
    - All in all, even with the requested clarifications added, it might be helpful to provide an example to better clarify this procedure.
- For all figures where LLAMA is the only model being considered -- i.e., I believe this is everything in sec 4.2? -- this should be explicitly noted; otherwise it is not clear what model is being considered, particularly when jumping between sections.
    - Similarly for "layer 10" in Fig 3, the figure should mention in the caption that it is a "histogram of [...] at the layer with maximum ID (L = 10)", or something similar.
- How should the results in "distribution of tokens at the peak" paragraph be interpreted? What do the findings in Fig 3 or the supporting text mean? This experiment is not explained in sections 3 or 4.2 as the others are. (Possibly, this would be a given if the provided summary of related work in the "intrinsic dimension" paragraph of sec 3 was clearer.)
- In line 404-405, why is "more comprehensive analysis required to confirm this statement"? what kind of analysis is being requested, and why is it necessary?
- In line 489-490, where it is stated that ID peaking at similar layers regardless of inputs being in-distribution or not "raises questions about the connection to the transformers’ architecture and the potential for formulating this phenomenon through analytic approaches" -- what does this mean? What questions are these, and why are they raised by ID peaking at similar layers for OOD inputs?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper describes observational data about the geometry of token representations in language models, focusing on attributes related to the dimensionality and layer similarity. The authors relate these variables to information on loss and presence of test data in the training set.

### Strengths
Geometric analysis of transformers holds great promise for interpretability, so this type of contribution is important. In addition, it's terrific to see careful observational data. The results themselves are interesting, but please see the next section for important caveats about novelty.

The technical exposition is fairly clear, and I found the review of various geometric measures useful. The four main results fit together, telling an interesting story that suggests that the level of information reduction is key to transformer performance. We see this both in the fact that shuffled inputs seem to have higher ID, and that ID shows a correlation with model loss.

The neighborhood consistency metric is also interesting, and provides more data for theorists looking to explain how different layers interact. The comparison with shuffling is useful to provide a baseline, indicating that the consistence results relate to "real" processing, rather than being an artifact of the architecture.

Overall, I certainly appreciate this type of observational result. I don't know that we can draw any strong conclusions from these experiments, but that shouldn't be necessary for acceptance: this will be helpful to future researchers as they build out theories of how transformers work.

### Weaknesses
My main confusion with this paper is understanding how much of an advance it is over the Cheng et al 2023 paper it references: https://arxiv.org/abs/2405.15471
It feels like the methodology and goals are extremely similar. Both papers study geometric aspects of internal token representations, with at least three target models in common. Both make comparisons between regular vs. shuffled prompts, look at the relationship between loss and intrinsic dimension, and compare ID and representation similarity between layers (although with slightly different methods). The results seem closely related. As I read it, the current paper feels like a relatively small advance over the Cheng et al paper, but I'm happy to be corrected.

Separately, I'm not convinced the "shuffled" condition is the best (or at least, only) baseline. I think it would be interesting to compare geometry with an randomly initialized network. (If this is in the literature already, I'd recommend noting this fact in the related work section.)

Another confound I wondered about: the results that prompts with higher ID have higher loss seem ambiguous. Could it be possible that high-ID prompts are just more intrinsically complicated in some way—maybe even in a trivial way, such as length? If so, it's not clear whether we can conclude anything useful from ID.

Writing: I think the authors could simply delete the first paragraph of the intro: it's not really necessary. In Figure 3, the left panel is mislabeled as "Angle".

### Questions
I'd like to see a systematic review of how the results here compare to Cheng et al. This may help make clear which parts of the current paper represent a new advance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study investigates the geometric structure of token-level representations across layers in large language models using three metrics: cosine similarity, intrinsic dimension, and neighborhood overlap. Unlike existing studies that typically summarise an entire prompt as a single point in space, this work measures geometry at the token level, offering a more granular perspective. To compare different structures, measurements are performed on both an "in-distribution" structured case and an "out-of-distribution" shuffled case, providing insights into how representation geometry varies across distributions.

### Strengths
1. Finer-Scale Analysis of Internal Representation Geometry: This study advances prior research by analyzing the geometric structure of internal representations at the token level rather than treating prompts as a single point in the representational space. 

2. Token Shuffling as a Comparison Baseline: The study introduces a shuffled-token case to represent out-of-distribution data, offering a valuable contrast to structured, in-distribution input. This approach enables the revealing of changes in token representation when standard sequence patterns are disrupted. It provides a clearer view of how language models process structured versus unstructured input.

### Weaknesses
1. Metrics Similarity and Limited Novelty in Findings: The study largely employs metrics similar to those in prior research, such as cosine similarity and intrinsic dimension. Consequently, while the paper provides an interesting token-level perspective, many findings echo previous studies without introducing substantially new insights. The use of cosine similarity, while standard, may not fully capture the nuances of high-dimensional token representations, particularly when these representations are known to exhibit complex non-linear relationships. Similarly, the intrinsic dimension, while useful, is a global measure and might not reflect local variations in the representational space. A more detailed analysis of the limitations of these metrics in the context of token-level analysis would be beneficial.

2. Unclear Utility for Model Interpretability: While the paper explores token-level geometry, its implications for model interpretability remain uncertain. A connection between the identified geometric patterns and practical insights into model behaviors would be appreciated. The paper does not provide a clear link between the observed geometric changes and specific model behaviors, such as improved or degraded performance on downstream tasks, or changes in attention patterns. Without such connections, the geometric analysis remains somewhat abstract and its practical utility is questionable.

3. Questionable Plausibility of Some Claims: Certain claims, like the difference in Neighborhood Overlap between structured and shuffled cases, appear unsupported by the presented data. For instance, Figure 4 does not show a clear difference in NO between the two cases, particularly in the average result shown in the right panel. Instead of concluding that the shuffled case consistently has a lower NO, it would be valuable to investigate this observed similarity further to determine if it reflects a limitation in the metric’s sensitivity or a more nuanced interaction in token representations between the cases. The lack of a clear difference in NO, especially in the average case, raises questions about the robustness of this metric and the conclusions drawn from it. The paper should explore potential reasons for this lack of differentiation, such as the metric's sensitivity to noise or the specific parameters used in its calculation.

### Questions
N/A.

### Soundness
2

### Presentation
2

### Contribution
2

# Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Humans excel at learning abstract patterns across different sequences, filtering out irrelevant details, and transferring these generalized concepts to new sequences.
In contrast, many sequence learning
models lack the ability to abstract, which leads to memory
inefficiency and poor transfer. We introduce a non-parametric hierarchical variable learning model (HVM) that learns chunks from sequences and abstracts contextually similar chunks as variables. HVM efficiently organizes memory while uncovering abstractions, leading to compact sequence representations.  When learning on language datasets such as babyLM, HVM learns a more efficient dictionary than standard compression algorithms such as Lempel-Ziv. In a sequence recall task requiring the acquisition and transfer of variables embedded in sequences, we demonstrate HVM's sequence likelihood correlates with human recall times. In contrast, large language models (LLMs) struggle to transfer abstract variables as effectively as humans. From HVM's adjustable layer of abstraction, we demonstrate that the model realizes a precise trade-off between compression and generalization. Our work offers a cognitive model that captures the learning and transfer of abstract representations in human cognition and differentiates itself from the behavior of large language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
**Update after rebuttal:** Thanks to the very detailed response by the authors, my questions and potential misunderstandings have been clarified and I have raised my score from a 5 to a 6. I still think the results on a data source specifically designed to highlight the advantages of the model must be taken with a small grain of salt (recognising that there are other good arguments for designing the data source), and the comparison against LZ78 is okay, but it should not be too surprising that LZ78 is not an ideal compressor for the synthetic data source.

---

The paper tackles the problem of discovering useful abstract representations in sequence prediction, that allow for better compression and transfer (generalization) with the aim of “[capturing] the learning and transfer of abstract representation in human cognition”. To this end, the paper extends a previously proposed model for probabilistic hierarchical chunking, HCM, with the ability to include learnable abstract variables into the chunk dictionary. Learning the model and performing inference with it is somewhat involved (as is generally the case for non-parametric probabilistic models), but explained well in the paper. On synthetic data that is designed to embody the assumptions underlying the model, the model performs very well and outperforms HCM and Lempel-Ziv (LZ78) as a baseline. The model also performs favorably on four natural language datasets (cut into sequences of 1000 characters), and correlates better with human recall times in a color memorization task. The paper finds that in-context learning with LLMs (GPT2 and Llama-2) behaves qualitatively differently on a similar task. Finally, the paper draws a connection between learning abstractions and lossy compression.

### Strengths
* The model is an interesting, sensible, and original improvement over HCM.
* Empirical results show that the model learns well and works well on synthetic data and some natural language datasets.
* The work is very well put into wider perspective in the introduction.

### Weaknesses
 * Many of the main experiments were conducted on data from a generative model that fits exactly the modeling assumptions for HVM (or tasks inspired by these assumptions). As is often the case when a paper proposes a novel model and a novel data set / generator, the fact that the model works well on data that was specifically designed for the model to work well is not a very strong argument. Luckily the paper also shows good results on “natural” data, and qualitatively matches some aspects of human behavior (recall times) that are not trivially predicted from the synthetic data.
* Hierarchical Dirichlet processes and related models (perhaps most famously many variants of topic models) have been used and discussed exhaustively in the ML, linguistics, and cognitive science literature. But an in-depth discussion and technical comparison of HVM against these is currently missing. Specifically, the paper lacks a discussion on how the model's inference procedure compares to those used in topic models, particularly with regard to computational complexity and convergence properties. The absence of this comparison makes it difficult to assess the novelty and practical advantages of the proposed approach.
* From a cognitive perspective, a severe limitation is that learning in HVM strongly depends on initial learned representations and the order in which learning experiences are represented. While some human learning mechanisms have these traits, I am not sure whether they apply to the learning of abstract concepts in natural language to the extent that the model would predict. This sensitivity to initial conditions and presentation order could lead to instability and a lack of robustness in real-world scenarios, which is a significant concern for a model aiming to capture human-like learning.

### Questions
**Questions and improvements:**

1. The work and claims could be strengthened by evaluating on more datasets that focus on abstraction, but have not been generated by the authors. This is only relevant for a major revision.
2. Topic models and various forms of hierarchical latent variable models have been used and discussed extensively in linguistics, machine learning, and cognitive science. How does the HVM relate to commonly used topic models (LDA, and more modern ones)? Ideally this is discussed on a technical level in detail, but at the least it needs to be included with more detail in the related work discussion.
3. How does the generative model relate to the Hierarchical Dirichlet Process (Teh et al. 2006)? 
4. Why was LZ78 chosen as a baseline? It is a lossless general purpose compressor, and has not been designed specifically for natural language data or data with hierarchical structure. Personally I think a much more interesting comparison would be against Context-Tree Weighting (Willems et al. 1995), or maybe the forget-me-not process (Milan et al. 2016), though the latter is perhaps a bit of an overkill (and quite involved to implement).
5. Table 1: “we took random snippets of 1000 characters and calculated evaluation metrics”, that seems like fairly short sequences. Why 1000? Is there a scalability issue with longer sequences? How sensitive are the results, particularly the comparison against LZ78 / CTW to the sequence length?
6. The paper mentions lossy compression multiple times, but as far as I understand all evaluation metrics are lossless in the end (more “lossy” models simply require longer coding lengths / have less coding efficiency)? I am struggling to follow section 4.5 (despite having spent half of my PhD on rate distortion theory). For sure LZ78 is not a lossy compressor - it is lossless. Typically, the distinctive feature of lossy compression is that not all prediction/reconstruction errors matter equally, i.e. the distortion function is typically not the log loss (lossy compression requires a quantitative definition of which information is relevant and to which degree, relative to some task/goal; this is what the distortion function does; the log loss treats all information equally). What is the distortion function in the paper? If one is willing to go lossy, there is a famous trade-off between fidelity and “complexity” (really, the information rate): the rate-distortion curve. I have a hard time relating Fig. 6b to a rate-distortion curve - the “Representation Complexity” seems to be more related to the rate than the distortion, but the figure legend says exactly the opposite. And how is “Abstraction Iterations” (Fig. 6c) related to the abstraction level and representation complexity and thus ultimately the distortion (which also applies to L467-477)? I do agree that lossy compression can be used to formalize a particular kind of abstraction, but it seems to me that what is happening in the paper is more similar to a minimum-description-length argument for *lossless compression* (the more complex the model, i.e. the deeper the tree of abstractions, the better it can compress a sequence, but the price to pay for it is by having a more complex model). The mistake may be fully on my side, but please clarify.
7. Some of the discussion / conclusion is a bit strong. I would not reject the paper based on this, but I have listed concrete issues in the minor comments.
8. Why was the generative model introduced? Were there no suitable generators or datasets in the literature (that are more widely used)? Which shortcomings of previously used data (generators) does the current paper tackle? (I am leaning towards listing this as a minor point, but I also think that any paper that introduces a new data set or data generation procedure should justify it over using what’s been published and used previously by others).

**Minor comments:**
1. L 164 - line break within inline equation.
2. Discussion in L279-284 leaves out that HCM achieves better coding efficiency than HVM if I understand correctly.
3. L 315: “LZ78 performs well in terms of compression efficiency, which is expected given its design purpose”. I don’t fully agree, LZ78 is a general purpose lossless compressor, it has not been specifically developed to compress natural language.
4. L 499: “our work provides a reductionist cognitive model that explicitly specifies the minimal components needed for a model to learn interpretable abstract structure from sequences.” - what makes the model particularly “cognitive”? I also mildly disagree that the model “specifies the minimal components”, rather, it is one solution with few components, but it is unclear that this is the minimum needed (and also minimal in which sense?).
5. L 503: “Our generative mechanism offers a probabilistic, hierarchical sequence generation model relying on chunk-based recursive generation and inventory growth rather than formal grammar rules.” - is this an advantage; does this address some shortcoming in the literature?
6. L 520: “Previously, grammar learning, chunk learning, and statistical/associative learning were studied in isolation as distinct aspects of sequence learning.” - it should be pointed out that this sentence refers to the cognitive science(?) literature (in other fields, like algorithmic information theory, which deals primarily with sequential learning, this distinction does not play a big role).
7. L 523: “Our work suggests a normative origin of concrete and abstract chunk learning” - I think the normative claim is a bit overstated in light of the results and no discussion that rules out all other possibilities.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a hierarchical variable learning model (HVM) that learns abstract patterns from sequences by combining chunking and variable discovery mechanisms. HVM builds on previous chunking models by adding the ability to identify abstract variables that represent groups of chunks that appear in similar contexts. The authors demonstrate that HVM achieves better compression and parsing efficiency compared to baseline models, correlates well with human sequence learning behavior, and provides insights into how abstraction enables better generalization. They evaluate HVM on both synthetic data and real-world language datasets, comparing it against traditional compression algorithms and large language models (LLMs).

### Strengths
Impressively, this paper presents some novel theoretical contribution, a clear theoretical framework for combining chunking and abstraction in sequence learning, with formal proofs and guarantees.

They also evaluated their model through multiple angles: computational efficiency, correlation with human behavior, comparison with LLMs, a good set of comparisons. 

And I enjoyed their connection to cognitive science: The work bridges computational and cognitive approaches, providing insights into human learning mechanisms.

### Weaknesses
1. The paper's comparison to LLMs is relatively narrow and focuses primarily on a specific sequence recall task and limited to short sequences, and therefore seems slightly contrived situation. The paper would benefit from explorations of slightly more complex abstraction tasks to study the general applicability of their method. The current evaluation does not fully demonstrate the capacity of the model to handle more intricate hierarchical structures or longer-range dependencies that are often present in real-world data. The chosen task, while relevant to cognitive studies, may not fully capture the nuances of abstraction learning in more complex scenarios.

2. The comparisons in the paper are quite limited and don't adequately address the rich literature on sequence compression and pattern detection. A single example I have in mind of a similar cogntiively-inspired latent variable learning model is CSCGs (https://pmc.ncbi.nlm.nih.gov/articles/PMC8062558/), but there are more.

### Questions
Please answer the two points under weaknesses above.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors build on a previous Hierarchical Chunking Model (HCM - a probabilistic model that learns to produce hierarchical chunks from sequential non-iid data) to create Hierarchical Variable learning Model (HVM), which groups chunks into high-level variable categories that have similar interaction properties. This model aims to compress sequences in a structured manner similar to humans. To test this out, the authors used sequence data from a variety of language datasets (childes, bnc, gutenberg, open subtitles) using HCM and LZW, a classical compression algorithm as baselines. The authors then used the model to account for human behavior in a sequence memory task that requires humans to re-use specific variables (against a control where there isn't a reusable variable). They also compared popular LLMs (GPT2, LLama2) on this task. HVM showed the biggest difference between the control and variable groups, which is the main effect that humans had.

### Strengths
* I think this is a really innovative algorithm that builds on the recent HCM in a pretty novel and cool way. It's clearly motivated by the human ability to abstract. 

* The evaluation is quite rigorous and showing performance on real world data as well as accounting for human behavior in a relevant task is a very nice touch. 

* There are a lot of rigorous proofs in the appendix. The authors have clearly thought a lot about the theoretical foundations of this algorithm as well as shown good empirical proof of its use.

### Weaknesses
 * I think the paper can mainly be improved in clarity. For example, when getting to Figure 3, it's kind of hard to figure out which exact datasets these results are from. In general, most of the text in the work is dedicated to describing the algorithm and results. I think adding some more information on what datasets are being used would be useful. For example, line 310: " BabyLM language dataset, which contain text snippets from a collection of data domains" what data domains are there? It was hard for me to understand what kind of data this was. 

* For Figure 5, I think the authors should plot the difference between the conditions rather than the conditions themselves. Currently, it's hard to understand why HVM shines here more than the LLMs. As I understand, the individual likelihoods don't matter as much as showing a significant decrease from control -> variable conditions. You can put the individual likelihood plots in the supplement. The plot as it is, in my opinion, undersells and obscures the result. 

* (minor weakness) I get the feeling that this algorithm isn't quite as scalable as other powerful sequence learning technologies we have today such as LLMs. This is not to say the algorithm is not useful because of that, because of course you do get more interesting structure and interpretability out of it (and it's also a better model of how humans do sequence learning). But I think this is at least worth mentioning in the discussion. If this model does actually have almost as good or better scalability than tools we have today such as SSMs or transformers, I think that would be a huge bonus and definitely needs mentioning. 

* (minor weakness) I think a potential missed opportunity for this algorithm is interpreting the discovered variables on specific datasets that we know has rich hierarchical structure. For example, can you use this algorithm on musical notes to recover leitmotifs? But there is enough work here that this can count as future work.

### Questions
* What is the relationship between this model and other Bayesian Wake-Sleep class of algorithms, like the older Helmholtz machine or the newer generation such as DreamCoder? There are definitely similarities in having a generative and recognition model, but I didn't see a discussion on this in the paper? I think this would be quite relevant to put in the related works section.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors introduce a hierarchical variable learning model (HVM) that learns abstractions on sequence data via chunking and variable learning. Sequences are first parsed according to a parsing graph containing existing chunks hierarchically. If one chunk follows another chunk in a statistically significant manner, their concatenation is added to the list of chunks alongside hierarchical information. Variables are also identified as a set of chunks that consistently occur before/after another chunk. Variables can also be used in chunk formation.

The model is tested on both a synthetic dataset and real world sequential datasets (language modeling) and compared against HCM and LZ78 on parsing search steps, sequence length, sequence negative log-likelihood, and encoding efficiency. It is shown that the design of HVM does indeed provide benefits with respect to these metrics.

The authors also HVM reflects human memorization and transfer performance on a memorization and transfer task.

In addition, the authors compare HVM performance to LLMs and associative learning models on the same cognitive task.

It is also shown that higher levels of abstraction in HVM leads to relatively higher likelihood when parsing unseen sequences compared to HCM, suggesting improved generalization.

### Strengths
- The paper is organized and well written
- The paper includes evaluations of the model from many different perspectives, including evaluation on synthetic and real world language datasets, comparison with human performance on a cognitive task, etc
- The paper has a good level of technical rigour with the addition of definitions, theorems, and algorithms in the appendix.
- The topic of abstraction is of great significance to the field of AI, and the paper proposes a novel approach to tackling this issue

### Weaknesses
 - Some small presentation issues in the appendix: equation in line 1020 is too long, figure 7 has a red line from a word processor, figure 8 has a red line that seems to be an error
- While I did praise the comprehensive evaluation, it is almost _too_ much content; it was difficult for me to understand the model without referring to the appendix. I suggest including information about the set up in the main text to improve clarity.
- Since the model builds up chunks by considering frequencies of adjacent chunks, there might be a limit to the expressivity of the formed abstraction. For example, while it might be able to capture the pattern of two chunks consistently being n chunks apart (if the intermediate chunks are all members of the set representing a variable), it cannot capture a pattern of two chunks being a variable number of chunks apart, where the number of chunks is determined by a symbol being present in the sequence.
- The evaluation only considers coding efficiency, compression efficiency, etc as a proxy for abstraction, which I do not believe to be sufficient for the purpose of demonstrating the effectiveness of the learned abstract representations. The demonstration of generalization does provide some evidence (Q1 below related to this point).

### Questions
- Would it be possible to use these learned representations for a task that requires abstraction (e.g. abstract reasoning)?
- When humans perform abstractions, semantic content also manners. Can this be integrated into the approach proposed in the paper?

### Soundness
3

### Presentation
3

### Contribution
3

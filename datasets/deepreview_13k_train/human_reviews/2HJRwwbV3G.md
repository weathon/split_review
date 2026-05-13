# What does the Knowledge Neuron Thesis Have to do with Knowledge?

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
We reassess the Knowledge Neuron (KN) Thesis: an interpretation
of the mechanism underlying the ability of large language models to recall
facts from a training corpus. This nascent thesis proposes that facts are
recalled from the training corpus through the MLP weights in a manner resembling
key-value memory, implying in effect that ``knowledge'' is stored in the
network. Furthermore, by modifying the MLP modules, one can control the language
model's generation of factual information. The plausibility of the KN thesis has
been demonstrated by the success of KN-inspired model editing methods
\citep{daiKnowledgeNeuronsPretrained2022, mengLocatingEditingFactual2022}.

We find that this thesis is, at best, an oversimplification.
Not only have we found that we can edit the expression of certain linguistic
phenomena using the same model editing methods but, through a more comprehensive
evaluation, we have found that the KN thesis does not adequately explain the
process of factual expression. While it is possible to argue that the MLP
weights store complex patterns that are interpretable both syntactically and
semantically, these patterns do not constitute ``knowledge.'' To gain a more
comprehensive understanding of the knowledge representation process, we must
look beyond the MLP weights and explore recent models' complex layer structures
 and attention mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the “knowledge neuron” hypothesis in a number of pretrained LLMs, namely, that factual knowledge can be localized to a small number of neurons, and that ablation of those neurons alters the probability of, and/or the final chosen output token. It further extends knowledge to include syntactic or formal knowledge, and similarly finds small number of neurons that can be ablated to suppress their respective represented knowledge, particularly distributed throughout the later layers. However, through previous and additionally proposed metrics, in particular emphasizing bi-directionality and synonym-agnosticism, the authors argue that the discovered knowledge neurons cannot be considered to contain anything like “knowledge”, but simply conserve token correlations found in the training text.

### Strengths
Overall, I found the paper to be clearly written, except for some very technical and linguistics-specific concepts that warrant more explanation (and earlier). Its usage of intuitive examples and graphical illustrations throughout the text was very helpful for me to understand its arguments. Lastly, the experiments seem comprehensive, and convincingly demonstrates the authors’ two main claims: the existence of syntax-knowledge neurons in LLMs analogous to fact-knowledge neurons, and that neither sets of knowledge neurons can be considered to robustly represent “knowledge”.

### Weaknesses
Despite its technical soundness, I’m personally struggling to understand the significance of these findings on a larger scale, though I must admit that this is not my field. In particular, I feel that such detailed investigations of LLMs on a more “cognitive” level, i.e., assigning individual neurons to be representing concepts / knowledge wholesale, is orthogonal to dissecting the computational mechanisms of attention-based LLMs, and is more suitable for a conference like ACL. This is not really the fault of this particular paper, but the literature they attempt to address (which are predominantly published in ACL), though ironically, this paper raises exactly the point that such “knowledge neuron” search in LLMs may be ill-advised, given that these models are simply token sequence autocomplete machines.

Nevertheless, given its current scope and that we are explicitly asked to assess significance of contribution to the field (of machine learning), I recommend borderline rejection for ICLR (but would otherwise strongly recommend acceptance for, e.g., ACL!). But I would be willing to convinced that it’s within scope if the AC and other reviewers disagree.

- one of my major concerns is the neuron selection procedure, which a priori limits the number of knowledge neurons to be 2-5. As I understand it, this procedure was not proposed by the authors, but in my opinion this process alone excludes the possibility of distributed representation, a much more reasonable null-hypothesis, resulting in a seemingly important discovery of knowledge neurons but in fact represents very little of the actual computations in the model. This is very reminiscent of the “grandmother” or “Jennifer Aniston” neuron type of work in neuroscience, and narrows the scope of the investigation arbitrarily and prematurely. Some investigation of distributed representation would, in my opinion, increase the impact and reach of this work

- the paper seems to be “on the fence” and sometimes explicitly contradicting itself. For example, page 7 states “LMs process and express the two types of knowledge using the same mechanism.” while the high-level conclusion of the paper, iiuc, is that there is no “knowledge neurons”. I think it would improve readability if the authors can find a more consistent messaging.

- the paper references a small number of previous works heavily, and without prior knowledge in the field, it’s hard for me to assess how much of the contributions are novel. The assessment of syntactic knowledge and newly proposed metrics are clearly new contributions, but a small “contributions” section explicitly and concisely summarizing this would be helpful.

- most of the illustrative examples (Figs 2-6) are on the case of determiner-noun, and some successful examples of the other two cases (subject-verb, gender and number agreement) would be even more convincing. Apologies if I had missed this in the supplemental.

- Formal and functional competence are referenced in the paragraph after figure 1, but without definitions, which can be confusing for a naive reader. The definition in the later paragraph was very helpful, and may be better if moved to be earlier.

### Questions
- one of my major concerns is the neuron selection procedure, which a priori limits the number of knowledge neurons to be 2-5. As I understand it, this procedure was not proposed by the authors, but in my opinion this process alone excludes the possibility of distributed representation, a much more reasonable null-hypothesis, resulting in a seemingly important discovery of knowledge neurons but in fact represents very little of the actual computations in the model. This is very reminiscent of the “grandmother” or “Jennifer Aniston” neuron type of work in neuroscience, and narrows the scope of the investigation arbitrarily and prematurely. Some investigation of distributed representation would, in my opinion, increase the impact and reach of this work

- the paper seems to be “on the fence” and sometimes explicitly contradicting itself. For example, page 7 states “LMs process and express the two types of knowledge using the same mechanism.” while the high-level conclusion of the paper, iiuc, is that there is no “knowledge neurons”. I think it would improve readability if the authors can find a more consistent messaging.

- the paper references a small number of previous works heavily, and without prior knowledge in the field, it’s hard for me to assess how much of the contributions are novel. The assessment of syntactic knowledge and newly proposed metrics are clearly new contributions, but a small “contributions” section explicitly and concisely summarizing this would be helpful.

- most of the illustrative examples (Figs 2-6) are on the case of determiner-noun, and some successful examples of the other two cases (subject-verb, gender and number agreement) would be even more convincing. Apologies if I had missed this in the supplemental.

- Formal and functional competence are referenced in the paragraph after figure 1, but without definitions, which can be confusing for a naive reader. The definition in the later paragraph was very helpful, and may be better if moved to be earlier.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper reassess the Knowledge Neuron Thesis in two ways, with syntatic minimal pairs and with generalizing to bijective relationships and synonyms. Theranalysis shows the limitation of current knowledge identification and editing, suggesting the need for more sophisticated understanding of inner mechanism of a language model.

### Strengths
1. This paper introduces many new practices for the rigorous study of knowledge neuron thesis, including using minimal pairs and t-test.
2. Broadening the definition of knowledge neural and connecting it to prior works in linguist phenomena.
3. Through and diverse analysis.

### Weaknesses
1. If I have to nitpick, section 4 felt a bit disjoint from the rest of the paper and is not fully fledged.

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work revisits the hypothesis that knowledge in pre-trained transformers may be limited to a few neurons. They do this by running two different model editing methods to identify neurons that are responsible for specific syntactic phenomena using the BLIMP minimal pairs dataset. While they do find a small number of mostly local knowledge neurons responsible for syntax, they find that intervening on these neurons is not enough to change model predictions in a robust way.

The paper also borrows from past work on factual editing, and along with their own results, conclude that the knowledge neuron thesis is flawed because intervening on these neurons is not sufficient to reliably change model behavior. Thus, they call for a more "holistic" approach that studies not individual neurons but entire layer structures and attention mechanisms as the motif for interpretability.

### Strengths
- The paper is extremely well-written with clear arguments, and experimentation.
- The results presented bring a lot of clarity to interpretability of transformers
- A lot of previous model editing techniques fail to systematically study if effect of edits are just local or if they are systematic, while this work does this very comprehensively.
- In my understanding, there is no prior work that applies editing techniques to identify "syntax neurons" and this aspect of the paper is quite novel

### Weaknesses
One weakness of the paper is that some of the presentation of experiments could be cleaned up substantially. Some specific suggestions for improvements:

- Results in 3.2 (first paragraph) seem quite loaded. This paragraph presents attribution scores, shows that identified neurons have regularity, the affect of causal interventions, how identified neurons have more to do with frequency cues than syntax etc. I think these results could be broken up into their own paragraphs. 

- It would also be great to clearly show which results are taken from prior work. I suspect atleast Table-1 and Figure-5(c) is taken from prior work?

### Questions
- I would be interested to know what the authors think interpretability research should focus on i.e. it appears that knowledge is mostly distributed and not necessarily isolated to specific neurons. There is some discussion around using attention weights and the underlying model circuit towards the end but it would be good to have a slightly more extended discussion around this.

- Some missing references on "decision making circuits":
  - Clark et al. 2019 (What Does BERT Look at? An Analysis of BERT’s Attention): They use attention patterns to identify syntactic knowledge in models.
  - Murty et al. 2023 (Characterizing Intrinsic Compositionality in Transformers with Tree Projections): They identify tree-structured circuits as a way to study generalization in transformers.
  - Wu et al. 2023 (Interpretability at Scale: Identifying Causal Mechanisms in Alpaca): Finds alignments b/w model hidden states and symbolic algorithms.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent

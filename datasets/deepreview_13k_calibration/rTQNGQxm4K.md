# PhyloLM: Inferring the Phylogeny of Large Language Models and Predicting their Performances in Benchmarks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 10, 3

## Abstract
This paper introduces PhyloLM, a method adapting phylogenetic algorithms to Large Language Models (LLMs) to explore whether and how they relate to each other and to predict their performance characteristics. Our method calculates a phylogenetic distance metrics based on the similarity of LLMs' output. The resulting metric is then used to construct dendrograms, which satisfactorily capture  known relationships across a set of 111 open-source and 45 closed models. Furthermore, our phylogenetic distance predicts performance in standard benchmarks, thus demonstrating its functional validity and paving the way for  a time and cost-effective estimation of LLM capabilities. To sum up, by translating population genetic concepts to machine learning, we propose and validate a tool to evaluate LLM development,  relationships and capabilities, even in the absence of transparent training information.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces PhyloLM, a method adapting phylogenetic algorithms to Large Language Models (LLMs) to explore whether and how they relate to each other and to predict their performance characteristics. More concretely, the authors make an analogy between phylogeny and LLM, with token context corresponding to the genes and generated tokens corresponding to the alleles. Then by applying Nei Generic distance to the empirically sampled character distribution conditional on some context, the authors first compute the similarities between models and then use the NJ algorithm to construct the phylogenetic tree. Experimentally, the authors have evaluated the choice of hyperparameters of the phylogenetic algorithms, the correctness of the recovered trees, and the quality of prediction when using the model similarities to infer their eval performances. They found that the recovered trees correspond to the know relationships of the different model (classes) and the performance prediction correlate well with the actual performance.

### Strengths
- The presentation of the paper is clear and easy-to-read and the methodology seems reasonable and sound.
- The idea of applying phylogenetic algorithms to study the evolution of language models, to the best of my knowledge, is a novel and interesting idea. This could inspire new works along this direction.
- The observation that using the conditional empirical distribution (with N=32) of the conditional generation of 4 subsequent letters could already provide a lot of information about the identify of the language model is an interesting (and to me surprising) observation which can be further explored by future works.

### Weaknesses
 - **[Practical usefulness of the phylogenetic tree]** In the current paper, the phylogenetics of Language models identified by running the NJ algorithm is verified using existing knowledge of the open and closed source models. Here, despite not knowing the exact training set/algorithm for some of the close models, their high-level relationships are still known to their end users (such as what company produces these models, which generation they are from, how they relate to previous models of the same company, etc). So it’s not clear to me whether any additional information can be gained by constructing the similarities and the phylogenetic tree that is not already know to the public. I believe this work still has its value purely for exploring this academically interesting direction, but from reading it, I haven’t got a sense whether the authors believe their methods could provide new insights about model evolution/relationships that’s not already publicly known. The paper does not explore the potential for the method to uncover novel relationships or lineages that are not already apparent from model release information or company affiliations. It would be more compelling if the method could reveal unexpected connections or provide a quantitative measure of model divergence beyond what is already qualitatively known.
- **[How to think about the benefits of performance prediction using similarities]** In terms of the contribution of using the similarity score to predict the downstream eval benchmarks’ performance, the authors have mentioned in line 312 - 315 that their estimation could use fewer queries than actually evaluating on the actual benchmarks such as MMLU. However, I think the authors could use more space to discuss the type of tradeoffs involved in actually using the similarity matrix-based performance estimators. For example, although the authors’ method use fewer inference compute for eval, they also are only correlated with the actual values but not very accurate, which makes me think some further discussion on what scenarios the authors could imagine their methods as practically useful for performance prediction/comparison. The paper should also discuss the limitations of using a similarity matrix for performance prediction, such as potential biases in the chosen prompts or the possibility of spurious correlations. It's unclear how the method would perform when applied to models with very different architectures or training procedures. A more thorough error analysis would be beneficial.
- Minor:
    - There is a small amount of content redundancy between line 211 - 214 on  page 4 and line 297 - 305 on page 6 discussing the very expensive distance matrix.
    - The *completion models* on line 384 could be italicized.

### Questions
Beyond the two questions above, I’m also curious whether the authors have experimented with any prompt ($c$) distribution other than math and coding and whether there are any distributions where the recovered phylogenetic trees do not correspond to our prior knowledge of how the models relate.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a biology-inspired paradigm for categorizing LLMs - an "evolutionary tree" of LLMs can be constructed by sampling from each LLM using a shared prompt dataset, and then comparing all outputs. The specific term used in the paper is "phylogenetic tree". The paper proposes an algorithm for constructing such a tree. The paper also discusses results, and the correlation of such generated trees with the ground truth and model performance.

### Strengths
Originality:
- Classifying LLMs into an evolutionary tree is a novel idea

Quality:
- The paper provides an algorithm, sample prompts used on LLMs, an extensive list of tested LLMs, and a re-constructed evolutionary tree on L324, vs. the "ground truth" evolutionary tree.

Clarity:
- The paper is generally clearly written, and the authors' thought process, various analogies to biology (e.g. a prompt as an "allele") are well-explained.

### Weaknesses
While the connection to biology is interesting and well-described, a case was not well-made for *why* the analogies should be made as the paper describes.

For example, the paper proposes the analogy of "gene & allele" and "prompt & completion": this is a bit hand-wavy; genes & alleles suggest the idea of some inherent characteristic, but how a prompt is completed may be more a function of the training dataset, rather than some model characteristic as implied by the paper: the idea that models are "evolved", and thus classifiable into an evolutionary tree. The separate contributions of model architecture vs. training dataset to a model was not explored. Specifically, the paper does not address the potential for the training data to introduce biases or patterns that are then reflected in the model's outputs, which could confound the phylogenetic analysis. The method assumes that differences in output are primarily due to model characteristics, but this assumption may not hold true if the training data is not consistent across models.

Further, the prompt datasets used in the paper appeared to be fairly trivial, and only a very short completion was evaluated. This would be like asking college applicants to write essays, but limited to 3 words each: why comparing such short completions would still be meaningful was not explored. The paper does not provide a clear rationale for why short, simple prompts are sufficient to capture the complex behaviors of LLMs. It's not clear if the method is robust to different prompt complexities or if the results are only valid for the specific type of prompts used in the study. The limited length of the completion also raises concerns about whether the method is capturing the full range of model capabilities.

### Questions
Suggestion: It may be more informative to apply the same technique on more well-defined and challenging tasks, such as writing an essay, rather than compare next-few-token completions on what are essentially random string prompts.

Question: What might be the relative contributions of model architecture vs. pre-training/instruction-tuning datasets when using this approach to classify models?

Question: The paper suggests that this analysis can provide an estimate of model capabilities; but why would this analysis provide any more insight than simply inspecting the model size, and directly evaluating the model on well-defined tasks?

Question: The paper appears to use a string similarity measure of sampled outputs to draw conclusions about model relationships. Could we compare sampled outputs in any "deeper" way, such as by comparing some notion of intent, or "tendencies" of particular models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors transfer a well-known paradigm of phylogenetic similarity from computational biology to the study of LLMs. The authors leverage the responses of LLMs to prompts contained in common benchmarks as "genes' to evaluate the difference of responses to them as "alleles." They then apply Nei's standard genetic distance to the distance between tokens in the responses with additional character agglutination normalization on the first tokens for models with different tokenizers. The authors use their "genetic" LLM distance to build phylogenetic trees and predict the model performance on standardized benchmarks.

### Strengths
This work is outstanding.
- The clarity of writing is top-notch, and this paper should be readable not only by the ML and genetics community, but by the general public
- The problem the authors are trying to address - choice of most related LLMs and inference of performance of a previously untested LLM - is timely and important, as the proliferation of LLMs and tests means that for domains of interest, it is currently impossible to select the most appropriate LLM for a given application
- Authors have a deep understanding of bases of computational genetics and phylogenetics (reference genes, ancestral species inclusion) to accurately map the concepts from that field to LLMs
- Authors also have an excellent grasp of the inner workings of LLMs (e.g., the tokenization step), allowing them to 
- Authors are able to choose appropriate statistical tools to perform tasks of interest rather than the most common ones (e.g., ICA instead of common but inappropriate PCA on L268).
- Authors perform extensive benchmarking, offering insights that are in themselves interesting and shed light on some of the long-standing questions in the LLM community, e.g., the performance of quantized vs. non-quantized models (L496-498) or synthetic dataset re-use in non-opensource models (Fig 4.)
- Supplementary data is extensive (full distance matrices), and all the necessary code to re-run the experiments is provided

### Weaknesses
 - Fig 5A is overloaded and confused, and 5B is non-informative. Please consider splitting out samples to make the quality of correlation clear on a first view
- There is no discussion of neutral drift vs. selective pressure, which is particularly relevant, given that the former in genetics acts as an "evolutionary clock," generally used to estimate divergence in close populations. Authors, however, selected prompts from common benchmarks, for which models are frequently optimized to perform well, and that can be seen as genes highly selected for.
- The usage of exact token matching is a major weakness. LLMs are known for their semantic variability and ability to provide answers identical in meaning but with drastically different wording, which the author's method would consider as different. While the author's approach is arguably more relevant to identifying the similarity of training data for LLMs, overall performance is more likely to be predicted by a semantic similarity metric

### Questions
- L242-256, Is there a reason you did not use a 3rd-party tokenizer to calculate the distance between the models with different tokenizers? It would seem to improve the methodological consistency with the rest of the work.
- L046-L047, Is there a reason you did not cite Dawkin's "Selfish Gene", that is generally regarded as the source of the "meme" idea and hence the idea of applying population genetics to cultural artifacts?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper utilizes a metric inspired by phylogenetic to measure similarities between LLMs, outputs dendrograms between them, and predicts performance. By putting LLMs into the evolution framework, the authors propsoes a new way to evaluate model performance in a cost effective way. For models where the training details are scarce, this new framework also helps in gaining insights into their training process.

### Strengths
1. Originality: the paper is quite original in its making connection between phylogenetics and LLMs. This might open a novel avenue for studying LLM lineage and evolution
2. Significance: the paper has the potential to have high impact as it proposes a new framework of understanding LLMs. Moreover, the use of the framework in evaluating LLMs with low resources is quite valuable considering the emergence of LLMs and the scarcity of compute resources in some research communities.

### Weaknesses
1. While the connection between phylogenetics and LLMs is novel, a not of the details are not worked out thoroughly in the paper. For example, the paper makes a connection between tokens used by LLMs and alleles in genetics. However, when comparing different LLMs, which usually use different tokenization schemes, the analogy breaks down. The authros tries to mitigate that using the 4-character generated by the model. Then an obvious drawback is that for models that do not exactly output a token of 4-character long, what the authors are measureing are no longer p(a|g). Why is 4 used here also seems arbitrary, and could be explained or motivated better. Have the authors done any experiments on changing this number and see if the results are different? 
2. Again on the analogy between phylogenetics and LLMs, these kinds of analogies could serve as an inspiration and starting point, but relying entirely too much on it could be questionable. For example, a key component of the paper is the definition of the similarity metric between LLMs, which is adapted from a metric in phylogenetics. But why is this metric suited for the analysis of LLM's? Since what's being compared is P(a|g), i.e., distributions, why not use some more standard metrics for distributions like divergence?
3. The writing of the paper could be improved significantly. The clarity of the paper could benefit from some proof-reading. There are many places where the use of punctuations is wrong, e.g., ’gene’,

### Questions
The main questions are listed in the "weakness" section.

### Soundness
1

### Presentation
1

### Contribution
2

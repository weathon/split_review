# MAP's not dead yet: Uncovering true language model modes by conditioning away degeneracy

- Decision: Reject
- Scores: 5, 8, 5, 3

## Abstract
It has been widely observed that exact or approximate MAP (mode-seeking) decoding from natural language generation (NLG) models consistently leads to degenerate outputs (Stahlberg and Byrne, 2019, Holtzman et al., 2019). This has generally been attributed to either a fundamental inadequacy of modes in models or weaknesses in language modeling. Contrastingly in this work, we emphasize that degenerate modes can even occur in the absence of any model error, due to contamination of the training data. Specifically, we show that mixing even a tiny amount of low-entropy noise with a population text distribution can cause the data distribution's mode to become degenerate, implying that any models trained on it will be as well. As the unconditional mode of NLG models will often be degenerate, we therefore propose to apply MAP decoding to the model's distribution conditional on avoiding specific degeneracies. Using exact-search, we empirically verify that the length-conditional modes of machine translation models and language models are indeed more fluent and topical than their unconditional modes. For the first time, we also share many examples of exact modal sequences from these models, and from several variants of the LLaMA-7B model. Notably, the modes of the LLaMA models are still degenerate, showing that improvements in modeling have not fixed this issue. Because of the cost of exact mode finding algorithms, we develop an approximate mode finding approach, ACBS, which finds sequences that are both high-likelihood and high-quality. We apply this approach to LLaMA-7B, a model which was not trained for instruction following, and find that we are able to elicit reasonable outputs without any finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors provide analysis of why text generation models often suffer degenerated distribution mode. They attribute the problem to the contamination in the training data sampled from natural language distribution. They further find that the bad mode problem is alleviated when conditioned on a certain target length. To this end, the authors propose an attribute-conditional beam search algorithm which exhibits superiority compared with truncating methods when target length is given.

### Strengths
1. The authors provide a detailed analysis of bad mode problem.
2. The authors propose an attribute-conditional beam search algorithm which exhibits superiority compared with truncating methods when target length is given. 
3. The authors conduct experiments on various NLP tasks.

### Weaknesses
1. **Analysis less than convincing in supporting the "*bad mode problem*"**.  
In Section 2, the authors claim that introducing noise into the data distribution can lead to model degeneration, even when the model is perfectly trained to fit the original data distribution. The authors provide examples to illustrate this concept. However, I found some of these analyses less than convincing. In Section 2.1, the authors argue that "*If one in a billion sequences is replaced with a bad output, MAP on a perfectly trained model should give us one of the bad outputs*". However, this argument relies on the assumption that "*there might be 2^100 possible abstracts for a given scientific paper*". It seems such an assumption never holds true in the case of a real dataset. In contrast, there is only one reference for a source in the typical setting. The argument that a single noisy sample can drastically alter the MAP estimate is not well-supported by empirical evidence or a rigorous theoretical framework. The authors need to provide a more concrete justification for why this specific type of noise would cause such a significant shift in the model's mode, especially given that real-world datasets are unlikely to contain such a high proportion of corrupted samples.

2. **Unclear logic between Section 2 & 3.**  
In Section 3.2, the authors provide experimental results that "*the occurrence of empty sequences increases with source length*". The authors attribute the empty mode problem to that "*the entropy of valid outputs increases with input length, but the probability of the empty output does not decline enough*". I am confused that this may contradict the analysis in Section 2 that attributes the bad mode to "*low-entropy distractors*". The connection between these two explanations is not clearly established. If the bad mode is due to low-entropy distractors as claimed in Section 2, it's unclear why the increase in entropy of valid outputs with input length would exacerbate the problem. The authors need to clarify how these two factors interact to cause the observed empty sequence phenomenon. A more rigorous analysis of the interplay between entropy, input length, and the probability of low-entropy distractors is needed.

3. **Experiments are not serious**.  
**a.** In Section 3.2.1 & Section 4, the authors conduct qualitative analysis only based on case study, lacking rigorous analysis and discussion. The qualitative analysis is insufficient to support the claims made in these sections. The authors should provide quantitative metrics to measure the performance of the model and the effectiveness of their proposed method. Without quantitative results, it is difficult to assess the significance of their findings. 
**b.** In Section 5.2.1, the authors compare their proposed attribute-conditional beam search with truncated beam search when a target length is provided. The comparison is based solely on the log-likelihood of the search results, without considering the evaluation of generated quality, such as BLEU scores. This evaluation seems insufficient, especially considering the background that a language model's mode can lead to degenerated results. Furthermore, there's no comparison between the proposed attribute-conditional beam search and standard beam search (without length truncating, evaluated with both likelihood and BLEU), which appears to be weird and not convincing. The lack of standard evaluation metrics and comparison with a standard beam search makes it difficult to assess the practical utility of the proposed method.
4. **Concerns on the motivation and novelty.**  
**a.** The authors proposed a length-conditioned beam search algorithm. However, this seems not very helpful to solving the bad mode problem in LLM, as a pre-determined length may be imprecise and lack the flexibility. The practical applicability of a length-conditioned beam search is questionable, as it requires a priori knowledge of the desired output length, which is often not available in real-world scenarios. This limitation significantly reduces the method's usefulness. 
**b.** The novelty of proposed attribute-conditional beam search is limited. Those attribute-conditional sampling methods is well-studied, and the authors only adapt it to the beam search. The adaptation of attribute-conditional sampling to beam search, while potentially useful, does not represent a significant conceptual advance. The authors need to demonstrate a more substantial contribution to justify the novelty of their approach.
5. **The paper has too many typos**.  
**a.** Please check the format (should use ICLR 2024)  
**b.** Confused paragraph numbering (Section 3.1 & 3.1.1)  
**c.** wrong citing format

### Questions
Please see the weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper argues that one source of so-called text degeneration is contamination of the training data with low-entropy noise, such as empty or nearly empty completions, or partial or total repetitions of the prompt. It substantiates this claim by performing exact MAP decoding, including on LLaMA. It offers a decoding solution, which is to do exact or beam search decoding with constraints on "attributes" like length.

### Strengths
Overall, I really like this paper and favor acceptance.

The experiments with exact search provide convincing evidence of the claim about low-entropy strings. These experiments are also valuable because they reveal a new kind of degeneracy (copying the prompt) and they are the first to perform exact decoding on a large language model.

The observation that sampling has the opposite "Achilles' heel" is valuable, although not really the focus of this paper.

The attribute-constrained beam search algorithm is new. It's a nice idea that has essentially the same running time as standard beam search, and seems to work well. It's interesting that the example length-conditioned translations are good summaries of translations.

### Weaknesses
The explanation of degeneracy in terms of low-entropy strings is not new, and the authors may not be aware of the following two papers:
Ott, https://arxiv.org/abs/1803.00047
Holtzman, https://arxiv.org/abs/2104.08315

As an alternative to your decoding method, you could use an adaptive beam, using a wider beam for earlier timesteps that gets narrower for later timesteps. Then at timestep $a$, you would get higher-quality outputs with length $a$. I am not sure what schedule you would use for the beam size, but perhaps work by Brian Roark for adaptive beams in CKY parsing is relevant.

The evaluation of the attribute constrained beam search method for LLaMA consists of recording what percent of sentences get a higher reward according to the same reward model used in training, and giving a general subjective impression of sample outputs. I think this is a fairly weak evaluation, and it would be a lot better to elicit quality judgements from other people.

Style / minor points:

There is too much important information in the appendix, especially Algorithm 1, with many references from the text to the appendix.

Everyone has their own writing style, but I feel that there are too many exclamation points for an academic paper. There are even two sentences in a row with exclamation points on page 4, but this is probably just an editing error.



### Questions
table 2: how can truncated beam search be better than itself?

table 3: why do the TBS translations seem shorter?

5.3.1 In the example, the source sentence in the prompt is "I love machine learning," but the output translates the source sentence "My eyes are clear." Is that really what happened?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper shows that degenerate modal outputs are not necessarily an intrinsic property of language models themselves, but rather are likely a result of contamination in the training data. For improving the quality of text decoded from language models, the paper introduce an algorithm called ACBS (attribute-conditional beam search), which adds an additional constraint on the output to avoid the degenerate behavior. The experiment shows that ACBS are better than ordinary beam search and especially contirbutes to ameliorate empty-string degenerate behavior.

### Strengths
1. This paper provides a very detailed explanation to the model architecture, algorithms, and experimental data in the appendix, which is very useful for helping readers to understand the paper’s work. 
2. Derivation and motivation are clear. Point out the phenomena and causes of degeneracy problem at the beginning and then solve it later.
3. This paper is logical and flowing. The location and analysis of degeneracy problem are given progressively.
4. The analysis of the low-entropy distractor is concise and easy to understand with examples.
5. The experimental setup follows intuition, and argumentation process is basically based on experiments.

### Weaknesses
1. Missing experimental data in 5.3. The detailed experiment result about the comparison between ACBS and regular beam search should be compared in a table instead of directly stating the data in the paragraph. Otherwise, your results won't be convincing.
2. In 3.2.1, figure 1a and figure 1b just represents the increase of empty sequence with source length, lack of the curve that shows the decrease of empty output with source length to better support the conclusion.  
3. Lack of explaination about the difference between empty mode and empty output.
4. The paper only gives two examples to illustrate that low-entropy distractor outputs and empty outputs have a high log prob in section 2 but does not provide enough mathematical reasoning, so the argument that the degenerate modal behavior is related to the entropy of the set of valid outputs is not strong enough.
5. In section 3, the x-axis and y-axis markings in Figure 1a are not clear and Figure 1a does not offer enough support for the observed phenomenon that the probability of the empty sequence declines as the source length increases. The experiments in section 3 do not indicate the impact of contamination of the training data, which is emphasized in the abstract and conclusion.

### Questions
1. At the end of Section 3, how can we conclude that the degenerate modal behavior is related to the entropy of the set of valid outputs?
2. Exact search experiments are meaningful, but the result that exact search performs good is not relevant to Subsequent Chapters. Maybe their relevance should be emphasized by experiments in terms of computational cost.
3. The experiment to prove that ACBS not only benefit from removing empty outputs should be detailed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes ACBS, a modified version of beam search that produces output from the LM by conditioning on external signals, e.g. length. The authors argue that the unexpected behavior of the model is caused by the low-entropy noise sample and derive their proposed method. The experiments are conducted on two tasks (machine translation and story generation) with model scales up to 7B.

### Strengths
* The motivation for this work is interesting.
* The authors provide extensive qualitative examples.

### Weaknesses
 * **Poor Presentation**: The presentation of this work is poorly written. Please proofread your manuscript before submission. Some examples are 
  * Section 1: distribution which the mode representsEikema & Aziz (2020) --- the citation should be included in parenthesis and there should be a white space.
  * Section 1: training data data --> training data
  * Footnote 1: the regurgitating the input --> the regurgitating of the input
  * Section 2.1: distributions arbitrarily closely --> distributions arbitrarily close
  * Section 3: translation model Tiedemann & Thottingal (2020) --> translation model (Tiedemann & Thottingal, 2020)
  * Section 3: ROC stories dataset Mostafazadeh et al. (2016) --> ROC stories dataset (Mostafazadeh et al., 2016)
  * Section 3: LLaMA model Touvron et al. (2023) --> LLaMA model (Touvron et al., 2023)
* **Poor Theoretical Analysis**: The theoretical motivations presented in Section 2.1, 2.2, 2.3 are hard to follow. For instance, the authors write "For the SVO translation example", what is SVO? And there should be a proper citation. The mathematical derivations in those sections are not detailed enough, which clearly undermines the quality of this work.
* **Lack of Details in Experiments**: There are necessary details are missing, including how the outputs are obtained from the LM which are then used to train the classifier; number of epochs; number of training samples.
* **Limited Evaluations**: The evaluations are only considered up to 200 tokens which is too short under current literature, e.g. ChatGPT API has 4k length. I strongly suggest the authors to extend their evaluations up to at least 2k length.
* **No human evaluation**: When comparing two decoding methods like in Section 5.2.1, simply using likelihood is not enough. Human evaluations are necessary to include to provide more evidence of the proposed approach.

### Questions
N/A

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

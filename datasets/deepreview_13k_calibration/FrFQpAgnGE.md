# Language Models Implicitly Learn a Unified Representation Space

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Modern language and multimodal models can process a wide variety of inputs across different languages and modalities. We hypothesize that models acquire this capability through learning a *unified representation space* across heterogeneous data types. We first show that model representations for semantically equivalent inputs in different languages are similar in the intermediate layers, and that this space can further be interpreted using the model’s dominant pretraining language (when it has one) via the logit lens. We also find that models show a similar tendency when processing other kinds of data, including code and visual/audio inputs. Interventions in the unified representation space further affect model outputs in expected ways: for example, replacing the image representations in a vision-language model with language token representations leads to output changes consistent with the language token semantics, suggesting that the unified representations space is not simply a byproduct of large-scale training on broad data, but something that is actively utilized by the model during input processing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to show that models process inputs from different languages/modalities primarily by first projecting them into a unified representation space, before projecting them out into their language/modality for the output. They do so for multilingual, code, visual and audio settings. They then perform interventions in the unified space across those settings to support the hypothesis that the models operate in that space in intermediate layers.

### Strengths
* The paper builds on Wendler et al. (2024), which only looked at Llama trained pre-dominantly on English, to show that models trained predominantly on other languages do indeed have that language as their intermediate representation space
* They show that this also extends to multimodal input, which is what supports the claim of a 'unified' representation space.
* They perform some intervention experiments to support the hypothesis, and show that intervening in the unified representation space can affect outputs in other modalities/languages.

### Weaknesses
 * In Line 108, they mention that 'absolute similarity measures are generally difficult and unintuitive to interpret in high dimensional spaces' and hence choose relative similarity measures instead. This is a key choice in the experimental setup, and I would hope to see more discussions on whether prior work have chosen to use relative over absolute similarity measures. Specifically, it would be useful to understand if the choice of relative similarity is due to the inherent properties of the high-dimensional space, or if it is a practical choice to make the results more interpretable. A more detailed discussion of the limitations of absolute similarity in this context, perhaps with reference to specific mathematical properties of high-dimensional spaces, would strengthen the justification for this methodological choice.
* The intervention experiments seem to be somewhat weak. For them to strongly support the unified representation space hypothesis, I would expect a comparison showing that  dominant data type steering is comparable or more effective than non-dominant steering. This doesn't seem to be the case as monolingual steering seems to be on the whole better than crosslingual steering (Table 1). However, I do think that the fact that English steering works at all weakly suggests that hypothesis is true. The fact that monolingual steering is more effective raises questions about the extent to which the representation space is truly unified, or if there are still modality-specific subspaces that are more easily manipulated by modality-specific interventions. It would be helpful to see an analysis of the degree of overlap between the effects of monolingual and cross-lingual steering, perhaps using a metric like cosine similarity between the intervention vectors.
* Section 2: Notation wise, it is not clear what $M_{LM}$ is. It strictly reads as just the embedded tokens in this section (L102), but it also looks like a general, vague reference to mid-layer representations later in the paper.
* Equation 1 needs to be explained: is this the formulation of your hypothesis? If so, it should be introduced like: "Formally, our hypothesis can be formulated as:"
* What do you mean by "scaffolded" as used throughout the paper? The term is not defined but used early on in the introduction.
* Typos: (1) L288: Should this refer to Figure 8? (2) All references to Llava should be 'LLaVA' as per the original paper.

### Questions
* Section 2: Notation wise, it is not clear what $M_{LM}$ is. It strictly reads as just the embedded tokens in this section (L102), but it also looks like a general, vague reference to mid-layer representations later in the paper.
* Equation 1 needs to be explained: is this the formulation of your hypothesis? If so, it should be introduced like: "Formally, our hypothesis can be formulated as:"
* What do you mean by "scaffolded" as used throughout the paper? The term is not defined but used early on in the introduction.
* Typos: (1) L288: Should this refer to Figure 8? (2) All references to Llava should be 'LLaVA' as per the original paper.

### Soundness
3

### Presentation
4

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
The paper proposes a hypothesis that models can learn a unified representation space across multiple modalities, such as language and vision, as well as across multiple languages. Specifically, the authors hypothesize that: (1) Semantically related concept pairs from different modalities or linguistic spaces are represented more closely than unrelated pairs. (2) When given an input, the model continues in the dominant modality (e.g., language for a language model), even when the input format is symbolic, such as code.

To validate the first hypothesis, the authors calculate the cosine similarity between paired data (e.g., parallel translations, images and captions) and non-paired data, observing that semantically paired data have higher similarity scores. For the second hypothesis, they evaluate whether tokens that match the input context have a higher probability than random tokens. The results suggest that the model favors continuations in the dominant modality.

The authors further examine cross-modal correspondence by intervening in one modality and observing changes in others, covering multilingual, code, image, and video data. For example, by replacing image hidden states corresponding to one color with the text embedding for another color, they find that the model correctly predicts the new color with 80% accuracy when replacements are made from the first layer onward.

In conclusion, the authors present empirical evidence through similarity analysis and cross-modal interventions to support that models can learn a semantically unified space across languages and modalities.

### Strengths
1. The topic of interpretability in multi-modal representations is highly relevant, and the hypotheses and conclusions presented in this paper—along with the supporting experiments—are likely to inspire further research. 
2. The paper is well-written and easy to follow. 
3. The authors validate their hypotheses across multiple modalities, including multilingual settings, text-code, language-vision, and language-audio, providing a thorough examination of their proposed unified representation space.

### Weaknesses
1: Sub-hypothesis 1, “semantically related concepts are closer than unrelated concepts,” is not novel, as it aligns with the standard training objective of many multi-modal models. This alignment is already an expected outcome, though recent research has highlighted its limitations and proposed methods to improve it [1, 2, 3].

2: Sub-hypothesis 2 suggests that inputs will continue in the dominant space, even if the input format is not in that space. The authors support this by observing that, in models like Llama, intermediate representations shift to the dominant language (e.g., English) when the input is Chinese, with the representation returning to Chinese dominance in later layers. However, this hypothesis seems unrelated to the main idea of a unified representation space, and its findings are largely anticipated. A deeper analysis is needed, potentially identifying specific transformation mechanisms, such as attention heads or MLPs, that facilitate cross-lingual translation. Insights into how these transformations occur would add value, as explored in the Induction Head blog[3], which discusses how output circuits transform intermediate representations into the output space.

3: Lack of discussion of related work in unified representation[1,2] and information flow, especially the intermediate representation to input/output space [3]

### Questions
1. The description of Figure1, and Figure2 is missing?

2. In Figure 6, the intermediate tokens shown are predominantly English words rather than the matched label token. Could the authors clarify whether the tokens from the last layer align with the matched token? If so, the results may not be surprising, as the intermediate layers likely serve to associate the input with internal knowledge in the dominant space, while the later layers have output circuits that transform this dominant representation back into the output format. This aligns with my earlier point about the expected behavior of the model’s translation mechanism (see Weakness Point 2)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the Unified Representation Hypothesis, which predicts that—regardless of the type of data of the inputs being processed—the latent representations of a given concept will be aligned with the dominant data type that the model was trained on. For example, given a multimodal language model trained primarily on English text, the latent representations will reliably align with English text, even if the input is only an image, or in another language.

The study tests and finds consistent support for this hypothesis in cross-lingual and cross-modal settings, including text-audio, text-image, and multilingual models. These alignments are largely verified using the logit lens, but many experiments also entail counterfactual interventions to hidden states.

### Strengths
* The study advances an idea that has been more casually discussed in past work: that the representation space of models representing many types of data will be biased toward the dominant data type. This paper proposes and presents evidence for a stronger version: that, when given data of any type, the model’s representation of what to predict next will be more closely aligned with the dominant data type (even in the absence of any data of the dominant type in the input).
* The ideas are presented in a precise way. While it may take more effort to parse than verbal intuitions, it makes the theoretical assumptions underlying the work clearer.
* Thorough experimentation. Convincing evidence (often causal) from many models and in many settings.
* Table 2: It’s nice that the quality of the outputs is evaluated along multiple axes, rather than just overlap with respect to a reference.

### Weaknesses
 * The proposed idea does not seem distinct from that proposed in the Platonic Representation Hypothesis paper (Huh et al., 2024), which is cited. That paper also presented similarly diverse and thorough empirical evidence in favor of unified representations across modalities. It would be helpful to explicitly contrast the Unified Representation Space Hypothesis from the Platonic Representation Hypothesis in the paper, or at least to contextualize the main idea and findings here more thoroughly with it.
* Due to the quantity of experiments in the paper, it was probably difficult to fit the necessary details for each in such a way that makes them all clear. Most of them are well-defined, but I was sometimes not sure what, exactly, was being evaluated. See Questions/Suggestions for details.
* L108-L113: Relative similarity captures a notion of distance, but it doesn’t capture whether there is underlying structural similarity (e.g., isotropy). Token distance is a nice start, but I have a hunch that going deep rather than wide would yield even more significant insights.
* L257-258: Speculative. It would be interesting to test this by projecting the inputs onto the space of the dominant data type, and then generating.

### Questions
* Figure 11: The experimental setup should be clarified. Is this a single comparison of the similarity between the logit lens and the mean representation across all nouns in the caption? Or is this an average similarity across separate similarities per noun? Or something else?
* L360-368: This is pretty light on details.  appendix explaining the experimental settings would be very helpful.
* Figure 8: There is plenty of vertical space here; consider enlarging this figure. Also: this looks pretty noisy. It could be revealing to add a color for a control setting, where the hidden representation is closer to a token other than these two possibilities. I hypothesize that much of this graph will be filled with the control color, but also that the rows with blue color will be much more consistent across examples.
* Figures 12 and 13: These values seem small on an absolute scale, and the difference between baseline and the correct answer is also small on a relative scale.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates whether multimodal LLM  process diverse input types using a unified representation space. The authors utilized "logitlens" as an interpretability tool to extract representations from each layer of the LLM. They show that model representations for semantically equivalent inputs from different modalities are similar in intermediate layers and that interventions in this space lead to predictable changes in model behavior.

### Strengths
1.  Extends prior research (Wendler et al.) from multilingual to multimodal settings on unified representation in the middle layers of LLM, offering new insights.
2. The experiments are interesting and thorough across modalities, including text, code, image, audio, adding robustness to its claims.
3. Good experiments on intervention in the unified representation space which shows the space causally steers model output.

### Weaknesses
1. The paper is largely an empirical study, and the findings may heavily depend on experimental settings. Some details are unclear, e.g., in multilingual experiment 1, the baseline for non-parallel texts is not well explained. The choice of random non-matching sentences as a baseline introduces a potential confound, as these sentences may not be semantically unrelated, and the degree of unrelatedness could vary across different random pairings, thus impacting the similarity scores.
2. The paper consistently use the last token's representations over layers for measuring similarities interpretation, which maybe a limitation. While the last token representation might capture some information, it is not guaranteed to encapsulate all relevant information within the sequence, especially for longer sequences or those with complex relationships between tokens. This approach may overlook crucial information encoded in other tokens' representations.
3. In Figure 9, the cosine similarity increase over baseline is marginal, with a maximum of only 0.03. This small increase raises concerns about the practical significance of the observed similarity. It is unclear if such a small difference in cosine similarity is meaningful enough to support the claim of a unified representation space, especially given the high dimensionality of the representation space.
4. In line 435, the paper hypothesizes that the unified representation space is language-agnostic, but the experiments primarily use the English-dominant Llama-3. This needs more justification. The claim of language-agnosticism requires more rigorous testing across a wider range of languages, including those with significantly different linguistic structures and those that are not well-represented in the training data of Llama-3.
5. Lack of related work for representation alignment, such as alignment through relative space [1] and its application in LLMs [2].

### Questions
1. Why Bloom is not a english-dominant LLM but Llama is english-dominant? Does it mean that they were trained differently?

### Soundness
3

### Presentation
3

### Contribution
3

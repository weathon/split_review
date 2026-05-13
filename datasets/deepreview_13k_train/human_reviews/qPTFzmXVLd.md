# Analyzing the Language of Visual Tokens

- Decision: Reject
- Scores: 6, 5, 3, 8

## Abstract
With the introduction of transformer-based models for vision and language tasks, such as LLaVA and Chameleon, there has been renewed interest in the discrete tokenized representation of images. These models often treat image patches as discrete tokens, analogous to words in natural language, learning joint alignments between visual and human languages. However, little is known about the statistical behavior of these visual languages—whether they follow similar frequency distributions, grammatical structures, or topologies as natural languages. In this paper, we take a natural-language-centric approach to analyzing discrete visual languages and uncover striking similarities and fundamental differences. We demonstrate that, although visual languages adhere to Zipfian distributions, higher token innovation drives greater entropy and lower compression, with tokens predominantly representing object parts, indicating intermediate granularity. We also show that visual languages lack cohesive grammatical structures, leading to higher perplexity and weaker hierarchical organization compared to natural languages. Finally, we demonstrate that, while vision models align more closely with natural languages than other models, this alignment remains significantly weaker than the cohesion found within natural languages. Through these experiments, we demonstrate how understanding the statistical properties of discrete visual languages can inform the design of more effective computer vision models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper looks at the statistical properties of "visual languages," where images are broken into discrete tokens like words in a sentence, used in multimodal models such as transformers. The authors explore whether these visual tokens behave similarly to natural language in terms of frequency distributions, grammatical structures, and alignment. Their key findings are that visual tokens follow a Zipf-like distribution with higher entropy, lack cohesive grammar, and mainly represent parts of objects, aligning only partially with natural language. These results suggest that visual languages have unique characteristics, which might benefit from specialized model designs to handle them effectively.

### Strengths
1. This paper is well-oragnized and offers a fresh perspective by treating visual tokens as discrete elements analogous to words in natural language.
2. The experiments are well-executed, with thorough empirical analysis across several datasets and tokenization methods.
3. The work has significant implications for multimodal model design, suggesting that unique features of visual tokens may require new model designs for better performance in vision-language tasks.

### Weaknesses
1. While the paper evaluates various tokenization methods (e.g., VQ-VAE, Chameleon), it could benefit from exploring alternative tokenization strategies, especially non-discrete or hybrid methods. The current analysis is limited by its focus on discrete tokenization, which may not fully capture the richness of visual data. For instance, methods that combine discrete and continuous representations, or those that use attention mechanisms to dynamically generate tokens, could reveal different statistical properties of visual languages. The lack of exploration into these areas limits the generalizability of the findings.
2. The study primarily relies on commonly used datasets (e.g., MS-COCO, ImageNet) that may not fully capture the diversity and complexity of visual scenes in real-world multimodal applications. Including more varied datasets with richer visual and contextual details. The datasets used, while standard, are often curated and may not reflect the full spectrum of visual information encountered in real-world scenarios. For example, datasets with complex scenes, varying lighting conditions, or unusual object arrangements could reveal different statistical patterns in visual tokens. The limited diversity in datasets could lead to conclusions that are not universally applicable.

### Questions
The authors can consider to include more varied datasets with richer visual and contextual details.

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
The paper analyzes the discrete visual tokens learned with VQ-VAEs and investigates several of their properties, such as their frequency distributions, grammatical structures, and topological alignments with natural languages. Some of their findings include: 1) 1-gram and 2-gram visual tokens do not follow Zipf's law, but longer n-grams match it better. 2) visual tokenizers are good at capturing part-level representations. 3) Context-free grammar may not as accurately represent "visual languages" as natural languages. 4) "vision languages" align less with each other than with natural languages.

### Strengths
1. The idea of analyzing the visual tokens learned by VQ-VAE models and investigating their properties using natural language tools is interesting and could be inspiring.
2. The writing is clear, with each research question and findings clearly stated in each of the sections.

### Weaknesses
1. The paper presents various findings and suggests potential implications and directions for future work. However, it lacks follow-up experiments to support these hypotheses, making the claims less convincing and raising doubts about the practical value of the findings. For example, the observation that longer n-grams better match Zipf's law is interesting, but without further experiments, it's unclear if this has any practical implications for model design or performance. Similarly, the claim that visual tokens capture part-level representations needs more direct validation, such as through controlled experiments that manipulate part-level information and observe the resulting token changes. The lack of such validation makes it difficult to assess the true significance of the findings.
2. The approach of applying language tools directly to visual tokens is questionable, especially as the findings suggest that visual tokens may not inherently exhibit natural language structures. Specifically, applying 1D-based methods like n-gram analysis and context-free grammar parsing to 2D visual tokens, which are inherently spatial, may not be appropriate. The row-wise linearization of 2D tokens into a 1D sequence, while common in transformers, discards spatial relationships that are crucial in vision. It remains unclear if the observed deviations from natural language patterns are due to genuine differences in the underlying data structure or simply an artifact of the 1D analysis method. Additionally, the paper does not explore alternative 2D-aware analysis techniques that might be more suitable for visual tokens.
3. Overall, it seems to me that the results presented do not convincingly demonstrate that using language tools on visual tokens is a valid method for analysis or clarifying the implications of their similarity or dissimilarity to natural language structures. The paper provides broad analyses, but a deeper focus on fewer points with more experiments would strengthen the claims. For instance, instead of covering multiple analyses like Zipf's law, Yule-Simon's law, and topological alignment, focusing on one or two key analyses with more in-depth experiments and ablation studies could provide more compelling evidence. The current broad approach makes it difficult to draw strong conclusions about the utility of applying language-based analysis to visual tokens.

### Questions
1. How do you define n-grams for visual tokens obtained from 2D images?
2. Is it possible that "vision languages" actually follow natural language properties, but require vision-specific analysis tools or adaptations of existing tools to reveal them?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tries to investigate the similarity between language tokens and visual tokens. More specifically, the authors inspect the equivalence of visual and natural languages through an empirical analysis of token distributions, segmentation granularity, and syntactic and semantic structures.

### Strengths
1. By examining visual tokens through the lens of linguistic principles, the authors provide a novel framework for analyzing multimodal models, which enriches the discourse surrounding the integration of vision and language.
2. The comparison of visual languages to natural languages, especially in terms of grammatical structure and co-occurrence patterns, yields interesting conclusions about the nature of visual representation and its implications for model design.
3. The paper writing is clear. This clarity aids in understanding the complex interactions between visual and linguistic modalities.

### Weaknesses
1. The paper primarily borrows conclusions and formulas from the realm of language models and applies them to visual tokens without offering substantial new insights specific to visual representations. The analysis and discussion often appear superficial, failing to yield novel conclusions regarding the unique characteristics of visual tokens.
2. The study lacks original analytical frameworks or targeted statistical experiments designed specifically for visual tokens. As a result, the manuscript reads more like an experimental record rather than a comprehensive exploration that provides meaningful inspiration or deeper understanding for the reader.
3. The conclusions drawn regarding model design and their implications for improving multimodal task performance are notably unclear. The recommendations do not provide concrete guidance on how to effectively implement these insights in practical model development, leaving the reader uncertain about their applicability in real-world scenarios.

### Questions
1. How does your analysis of visual tokens extend beyond existing conclusions from the NLP domain? What specific novel insights can you offer regarding the unique properties of visual tokens?
2. What additional analyses or experiments could be conducted to deepen the understanding of visual tokens? Are there specific hypotheses or exploratory questions that you believe warrant further investigation?
3. Can you clarify how the conclusions drawn in your paper can be practically applied to improve the design of multimodal models? What specific recommendations do you have for researchers looking to leverage your findings in their model development?
4. In your comparisons of visual languages and natural languages, what specific aspects do you believe are most critical to consider when developing models that integrate both modalities? How do these aspects influence the training strategies employed?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the language expressed through “visual tokens” – discrete tokens representing images, that are obtained from an image tokenizer followed by linearization. Such tokens are used jointly with language tokens in multi-modal transformer-based models, such as Chameleon. The paper analyzes various statistical properties of the language induced by visual tokens, such as its entropy, naturality, and topology, in comparison to natural human language and language generated by language models. The paper shows multiple interesting findings highlighting similarities and differences between “visual languages” and natural languages. The authors also include several discussions regarding the potential implications of their findings, suggesting ways in which they can inform the design of more effective vision models.

### Strengths
* Multi-modal models, especially those involving vision and language, are of growing usage and interest. The paper takes a unique stance on analyzing these models, viewing visual tokens as language and applying well-established empirical statistics methods.

* I found the analysis very comprehensive, covering 5 different tokenizers, multiple datasets, and more than 6 methods. It also tackles fundamental research questions.

* The paper is clearly written and easy to read, balancing well between concrete results and intuitive interpretations.

### Weaknesses
 * The main drawback of the paper is that while it discusses multiple potential implications of the reported findings, it does not demonstrate them, leaving practical exploration of these implications for future work. I find the observations interesting and important by themselves, but the paper could be made much stronger with such experiments. For example, the paper suggests that the identified statistical properties of visual tokens could inform the design of more effective vision models, but it does not provide any concrete examples of how this could be achieved. Without such validation, the practical significance of the findings remains unclear.

* I may have overlooked it, but there is very little discussion on the differences across visual tokenizers and datasets. If it implies that current tokenizers largely behave similarly (regardless of hyperparameters, etc) then this should be emphasized. The paper analyzes 5 different tokenizers, but it does not delve into the specific characteristics of each one, such as their architecture, training data, or token vocabulary. Similarly, the paper uses multiple datasets, but it does not discuss how the choice of dataset might affect the observed statistical properties of the visual tokens. A more detailed analysis of these factors would be beneficial.

* Not a major weakness, but a point for consideration is that the paper focuses on *discrete* visual tokens, while recent performant models like LLaVA rely on *continuous* tokens. The authors acknowledge that, noting that some of the analyses could be applied to continuous tokens, but they leave the exploration of this for future work. However, I think the paper could be made more impactful by applying its unique analysis to continuous tokens as well and comparing them to the discrete tokens. The paper could, for example, investigate whether the statistical properties observed in discrete tokens are also present in continuous tokens, and if not, what are the implications of these differences.

### Questions
Typos:
* L73 – “we aim to show through these experiments show that”
* L79 – “The first, question that we examine“

### Soundness
3

### Presentation
4

### Contribution
3

# ELCC: the Emergent Language Corpus Collection

- Decision: Reject
- Scores: 6, 6, 3, 1

## Abstract
We introduce the Emergent Language Corpus Collection (ELCC):
  a collection of corpora generated from open source implementations of emergent communication systems across the literature.
These systems include a variety of signalling game environments as well as more complex environments like a social deduction game and embodied navigation.
Each corpus is annotated with metadata describing the characteristics of the source system as well as a suite of analyses of the corpus (e.g., size, entropy, average message length, performance as transfer learning data).
Currently, research studying emergent languages requires directly running different systems which
  takes time away from actual analyses of such languages,
  makes studies which compare diverse emergent languages rare,
  and presents a barrier to entry for researchers without a background in deep learning.
The availability of a substantial collection of well-documented emergent language corpora, then, will enable research which can analyze a wider variety of emergent languages, which more effectively uncovers general principles in emergent communication rather than artifacts of particular environments.
We provide some quantitative and qualitative analyses with ELCC to demonstrate potential use cases of the resource in this vein.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Emergent Language Corpus Collection (ELCC), a collection of corpora generated from open-source implementations of emergent communication systems (ECS). The authors perform quantitative and qualitative analyses with ELCC to demonstrate potential use cases of the resource.

### Strengths
1. The sources and statistics of the data are well documented.
2. The data can enable broader engagement and new research directions in ECS.

### Weaknesses
1. As the authors already mentioned in limitations, the data are not annotated, having not reference to the semantics of the communication. This limits the scope of possible analysis.


### Questions
1. "it is not comprehensive collection of all of the open source implementations let alone all ECSs in the literature" -- to your best knowledge, what are some ECS categories having no representative systems in ELCC?

2. Typo: line 169: syntehtic -> synthetic

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a collection of "corpora" called Emergent Language Corpus Collection (ELCC), generated from open-source emergent communication systems (ECS). In Emergent Communication (EC), researchers are generally required to be familiar with deep learning, reinforcement learning, and machine learning frameworks such as PyTorch to simulate the emergence of language and communication. However, not all of the previous EC studies provide well-documented, high-quality, and open-source implementations, which prevents us from performing the meta-analysis of the EC studies and non-ML researchers from joining the EC field. To mitigate such problems, this paper introduces ELCC, collecting several appropriate open-source implementations, conducting reproduction experiments, summarizing the experimental results (i.e., emergent languages) as "corpora," and performing some basic evaluations (e.g., n-gram entropy, XferBench). The author(s) suggest that ELCC can also be used for further analyses (e.g., word boundaries, syntax).

### Strengths
- Contribution to the reproducibility of the EC field and the ease of entry to the field.
- The novelty of the idea of creating corpora of emergent languages, which had not been conceptualized before, probably due to the artificial nature of emergent languages.
- Most EC papers mention previous work in the "Background" section or "Related Work" section regarding problem setting, methodology, and evaluation metrics. Interestingly, this paper additionally focuses on the quality and availability of their source code implementations and summarizes them comprehensively, which will be helpful for EC researchers.
- The corpus collection process is carefully planned and conducted.
- The paper is clearly written and easy to read.

### Weaknesses
 - ELCC is not annotated with meanings (or semantics, inputs) corresponding to messages (sentences). This would be somewhat problematic when the EC researchers want to evaluate other properties, such as compositionality. Specifically, without semantic annotations, it's impossible to analyze how the emergent languages map to the underlying task structure, hindering the study of systematicity and generalization. The lack of these annotations limits the scope of analysis to surface-level statistics rather than deeper semantic properties.
- The basic analyses provided (e.g., XferBench) are indeed valid in showing the "negative result" (i.e., that emergent language is not similar to human language). However, I am not sure if the provided metrics are still valid in showing the "positive result" in the future (i.e., that emergent language is similar enough to human language), recalling some (computational) linguistic literature claiming that even monkey-typing sequences follow a Zipf-like distribution [1], that even pre-training with simple artificial language ($\neq$ emergent language) has a positive influence on downstream task performance [2], etc. This is another reason I think ELCC should be annotated with semantic information to allow future EC researchers to perform more detailed analyses. The current metrics, while useful for initial comparisons, may not be sufficiently sensitive to capture the nuances of human-like language emergence, potentially leading to false positives in future studies.
- I feel references (only) to Ueda et al. (2023) and van der Wal et al. (2019) in some parts of the Introduction and Discussion sections are somewhat abrupt, considering a number of  EC papers have studied human language-ness of emergent languages from various points of view. I know typical topics in the field, like TopSim-based compositionality, are out of this paper's scope. Still, I'd be glad if you mention a few more human-language-ness papers somewhere in this paper, e.g., in the Limitation section. The current framing risks overlooking significant prior work in the field.
- (minor) Figure 4 has no caption (other than sub-captions a, b).
- (minor) When mentioning Zipf's law, you may cite Zipf (1949) [3]. Likewise, you may cite Harris (1955) [4] and Tanaka-Ishii (2021) [5] for Harris' articulation scheme.

### Questions
- Is it possible to (easily) update ELCC with semantic annotations in the (near) future?
- With ELCC, is it possible to evaluate language similarity (or language synchronization), which is sometimes considered in the context of populated signaling games?
- What can we read from Table 2? Does it indicate either language-ness or unlikeness of emergent language?
- (minor; just curious) As EC researchers, how can we contribute to this corpora creation project after deanonymization (e.g., by sending a pull request)?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a system and approach called Emergent Language Corpus Collection (ELCC) for the standardized storage of languages produced by emergent communication systems. It further discusses several commonly used coordination games, comparing the languages they generate primarily using the XferBench evaluation metric.

### Strengths
There is a clear need to standardize various aspects of emergent communication (EC) experimental setups, and efforts in this direction such as the suggested ELCC, are valuable. The authors provide a compelling critique of the difficulties in reproducing past EC research and identify missing elements that hinder accelerated progress. They call for a more robust framework to facilitate easier reproducibility, comparison, and competition in the field, which could significantly accelerate its development.

### Weaknesses
The motivation behind this work is underdeveloped. Although standardization is beneficial, it is unclear what specific problems this work aims to solve. A clear example of ELCC’s utility, such as its potential to generate new insights, would enhance its justification. Additionally, the static nature of the ELCC collection raises questions about the kinds of research it enables and what insights it may provide beyond those already published by the corresponding papers. A leaderboard with well-defined datasets, metrics, and results might be more impactful than a static collection of generated languages.

Furthermore, while the ELCC corpus could have been used to evaluate the soundness and completeness of various EC evaluation metrics proposed in the literature, the analysis is mostly limited to XferBench. For example, although the authors mention the HAS metric (Lines 464-468), they only discuss it theoretically rather than demonstrating how ELCC could aid in evaluating this metric across languages.

In conclusion, the paper lacks innovative contributions, and the provided resource appears too limited to address key challenges in the field, such as establishing standardized EC benchmarks with readily available datasets and evaluation metrics.

### Questions
Could the Hugging-Face platform, API, and cloud infrastructure be leveraged to host and promote ELCC to the broader research community?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper is about providing a collection of artificial corpora resulting from "emergent communication systems". These systems generate artificial language by forms of interactions between agents (sender, receiver). Having such corpora is important for studying similarity of artificial language to human language - which in turn could be useful for obtaining pre-training data. 

The main contribution of this the paper is the data resource and code for reproducibility.

### Strengths
This resource could be valuable for the niche community on artificial languages. The authors also identify reproducibility issues in related work.

### Weaknesses
While I do agree that these could be useful corpora and the paper should be published, I do not think that  ICLR is the right venue

- 1) it's mainly a resource contribution for which there are other venues, e.g., LREC or a corresponding journal

- 2) the whole field of study is quite niche

- 3) the substance is a little thin for an ICLR contribution, e.g., compiling approaches from other research

- 4) I would have hoped to read something in the context of recent LLM-based multi-agent interaction. However, mostly older approaches seemed to have been considered

- 5) There were some typos (minor), and I would also have liked to see a more central illustrating examples or an illustration figure show-casing agent-based simulation and language generation (e.g., the signalling game)

### Questions
As a suggestion, I would like to see an illustrating example. What are we supposed to be doing with the example in Figure 3? A sequence of integers is hard to read, interpret and understand.

What should we do with the numbers in Table 2?

Do I really understand correctly that you merely assemble the 73 corpora from other research and conduct a bit of analysis on it in Section 5?

### Soundness
2

### Presentation
2

### Contribution
1

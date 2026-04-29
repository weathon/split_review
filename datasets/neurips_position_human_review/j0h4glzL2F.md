# Realizing LLMs’ Causal Potential Requires Science-Grounded, Novel Benchmarks

- Decision: Reject
- Scores: 7, 7, 7

## Abstract
Recent claims of strong performance by Large Language Models (LLMs) on causal discovery tasks are undermined by a critical flaw: many evaluations rely on widely-used benchmarks that likely appear in LLMs' pretraining corpora. As a result, empirical success on these benchmarks seem to suggest that LLM-only methods, which ignore observational data, outperform classical statistical approaches on causal discovery. In this position paper, we challenge this emerging narrative by raising a fundamental question: Are LLMs truly reasoning about causal structure, and if so, how do we measure it reliably without any memorization concerns? And can they be trusted for causal discovery in real-world scientific domains? We argue that realizing the true potential of LLMs for causal analysis in scientific research demands two key shifts. First, (P.1) the development of robust evaluation protocols based on recent scientific studies that effectively guard against dataset leakage. Second, (P.2) the design of hybrid methods that combine LLM-derived world knowledge with data-driven statistical methods. 

To address P.1, we motivate the research community to evaluate discovery methods on real-world, novel scientific studies, so that the results hold relevance for modern science. We provide a  practical recipe for extracting causal graphs from recent scientific publications released after the training cutoff date of a given LLM. These graphs not only prevent verbatim memorization but also typically encompass a balanced mix of well-established and novel causal relationships. 

Compared to widely used benchmarks from BNLearn, where LLMs achieve near-perfect accuracy, LLMs perform significantly worse on our curated graphs, underscoring the need for statistical methods to bridge the gap. To support our second position (P.2), we show that a simple hybrid approach that uses LLM predictions as priors for the classical PC algorithm significantly improves accuracy over both LLM-only and traditional data-driven methods. These findings motivate a call to the research community: adopt science-grounded benchmarks that minimize dataset leakage, and invest in hybrid methodologies that are better suited to the nuanced demands of real-world scientific inquiry.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper challenges the recent success of LLMs for causal discovery. It poses two positions:
P.1. Evaluation protocals are needed which are not diluted by memorization of LLMs.
P.2. LLMs need to be combined with observational data to support causal discovery.

### Strengths
- The paper is well structured and written.
- The ideas can be easily followed.
- Paper takes up an very important point for the AI community.
- Data example is very illustrative.

### Weaknesses
- No alternative views are mentioned.

### Questions
- The paper covers causal discovery. How about causal inference in general?

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The authors discuss whether the strong performance by LLMs on causal discovery can be attributed to reasoning capabilities or memorization and question the validity of some of the current benchmarks assessing LLMs in this regard. In particular, they repeatedly demonstrate that performance can be tied to memorization and propose an approach to test against memorization. Furthermore, they consider that LLMs have inherent limitations when performing causal discovery. They suggest overcoming them by complementing LLMs with data-based approaches.

### Strengths
(S1) - We consider the ideas to be clearly written and articulated

(S2) - The authors formulate a problem (current benchmarks testing how good LLMs are at extracting causal graphs from text do not test for LLM memorization) and provide experiment results to support their claims. Furthermore, they propose a solution for which they provide the corresponding experimental results (testing on causal graphs that can be formed on data created after the LLM release), showing the solution provides a viable path forward on assessing LLMs' causal potential.

(S3) - The authors recognize inherent limitations of the LLMs when dealing with causal discovery and propose complementing them with statistical signals inferred from data.

### Weaknesses
(W1) - The authors draft a procedure to elucidate a causal graph from recently published data, curating it with experts' input. Nevertheless, the authors provide little detail on how the causal graph is created and assessed when compared to the causal graph produced by the LLMs. This weakens the reported results.

(W2) - The authors consider that hybrid methods could bridge the gap, overcoming some notable limitations current LLMs exhibit. Nevertheless, this requires satisfying certain preconditions that were not addressed. We pose some questions on this below. 

Minor comments:

(W3) - Figures 1 and 2: make sure the colours are friendly to color-blind individuals.

(W4) - Table 3: Please indicate the metric that is being reported. From the previous tables, we understand this is the F1 metric. Nevertheless, the table caption should help the table information to be self-contained.

### Questions
(Q1) (a) How is bibliography retrieved, and how are limits established on it to guarantee the quality of sources and avoid spreading too widely? (b) How do the authors guarantee the scalability of the causal graph generation process? (c) How are the concepts from the causal graph normalized? Do the authors suggest matching or defining some ontology?, (d) How are the causal graphs extracted by the experts compared to the causal graphs generated by LLMs? Do we consider the same normalized concepts as an input? By providing such input to the LLM, do we force some bias/transfer some knowledge? If concepts are not normalized, how do we ensure different kinds of causal graphs extracted from LLMs are fairly compared against each other?

(Q2) (a) what data is required for data-based methods and how can be obtained for the problems at hand?, (b) how much of the causal graph the LLM extracts can be potentially covered/recreated considering the data-based methods?, (c) what is the amount of data required to have a certain level of confidence on the causal relationships extracted from data?, (d) are there some confounders or other factors that could affect the outcomes we see from data-based causality extraction methods?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The author claims that P1. Recent leverage of LLM in causal discovery is overestimated, as their training corpus may already include domain knowledge used for conventional causal discovery benchmarks. The author expresses this as data leakage, which hinders fair comparison with LLM and conventional causal discovery methods, thereby LLMs can relatively easily outperform causal discovery methods purely based on observational data. To tackle this, the authors suggest evaluating recent scientific data, which may be leakage-free.  For this, the authors suggest a recipe for extracting a causal graph from recent scientific publications. In those extracted causal graphs, LLMs suffer from a significant performance drop with respect to near-perfect performance in the conventional benchmark. Then, to mitigate the gap of LLM behaviour between benchmarks before or after the training cutoff date, and make use of LLM’s world knowledge for causal discovery, the authors claim P2. It is necessary to design hybrid methods that combine Large Language Models (LLMs) with data-driven statistical approaches.

### Strengths
- The suggested Positions 1 and 2 are timely and significant in that recently, many LLM research projects have targeted causal discovery benchmarking. The Positions could effectively promote discussion on how to leverage LLM in causal discovery, involving both fields of causal discovery and LLM reasoning.
- Regarding P1, generating a benchmark dataset following the proposed methods seems valid, and an experiment on this could be effective evidence.
- They proposed a novel memorization test for causal discovery and effectively used this as evidence for their P1. Additionally, this test method provides an effective benchmark for future work, which means the discussion invoked by this paper in this direction.

### Weaknesses
- The proposed benchmark causal graph construction method seems to largely depend on a domain expert elicitation process for causal graph notation, which limits future work for following P1 on subsequent datasets.
- Lack of justification to use LLM for causal discovery on a cutting-edge benchmark. Though the author demonstrated that LLMs' prior knowledge is weak on the cutting-edge benchmark after their cut-off, they still suggest integrating LLMs into a unified causal discovery framework. It seems to contradict the experimental evidence the author suggests.

### Questions
- If the LLM world knowledge itself is not good, for example, on a cutting-edge dataset, how can a hybrid method improve causal discovery?
- Obtaining causal graph annotations from experts is a widely used method; however, it may be vulnerable to reproduction issues since different sets of experts can provide different causal graph annotations. This problem can be mitigated by basing causal graph annotations on consensus reached by the domain community over a sufficient period of time. However, for the cutting-edge datasets presented in this paper, such consensus is difficult to expect. In this respect, how can we obtain robust and widely agreed-upon causal graphs?

### Presentation
3

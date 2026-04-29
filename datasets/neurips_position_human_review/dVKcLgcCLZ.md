# Causality can systematically address the monsters under the bench(marks)

- Decision: Reject
- Scores: 7, 7, 6

## Abstract
Effective and reliable evaluation is essential for advancing empirical machine learning. However, the increasing accessibility of generalist models and the progress towards ever more complex, high-level tasks make systematic evaluation more challenging. Benchmarks are plagued by various biases, artifacts, or leakage, while models may behave unreliably due to poorly explored failure modes. Haphazard treatments and inconsistent formulations of such ``monsters'' can contribute to a duplication of efforts, a lack of trust in results, and unsupported inferences. In this position paper, we argue causality offers an ideal framework to systematically address these challenges. By making causal assumptions in an approach explicit, we can faithfully model phenomena, formulate testable hypotheses with explanatory power, and leverage principled tools for analysis. To make causal model design more accessible, we identify several useful Common Abstract Topologies (CATs) in causal graphs which help gain insight into the reasoning abilities in large language models. Through a series of case studies, we demonstrate how the precise yet pragmatic language of causality clarifies the strengths and limitations of a method and inspires new approaches for systematic progress.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
The authors argue that causality is key when evaluating ML research. In particular benchmark evaluations. The overall argument is that Pearl's causal DAGs provides an unifying language that helps researchers to address the common mistakes and pitfalls of ML evaluation. The authors organize the wide range of issues under common abstract topologies, or CATs. These are mostly well known DAG structures such as confounders and mediators. Nevertheless, for each CAT an extensive review of the literature is provided.

### Strengths
Overall, the major strengths are:
- A well organized view of ML evaluation under CATs
- Alternative views are discussed in details
- I particularly liked how the authors acknowledge that current peer review may inhibit the description of causal assumptions in research.

### Weaknesses
While I agree with this position paper, my major concern is on the novelty of this position paper. That is, while I view the organization of "monsters" and CATs, as the authors put it, as commendable effort, the importance of causality for evaluation is well known. That is, while this position paper may frame and organize this question for ML benchmarks, econometricians* have argued in favor of causal interpretation of statistical models for decades.

* I understand this is not necessarily Peal causality.

### Questions
IMHO, we are at an arms-race like situation with large language models. Whenever a new benchmark that LLMs are unable to solve appear, for instance chain of thought problems, models are quickly updated with training data for that particular task. Most of the cited papers here use causality to find "monsters" in these large models. Following the arms-race, these monsters may be quickly mitigated with an updated training. Do the authors believe that we, humans, will effectively create a systematic approach to continuously measure limitations of large models? If so, how will causality help?

Notice that my question is exactly focused on moving away from the individual monsters/cats and to a more general view. This position paper presents the individual solutions to monsters/cat tied with a unifying argument. However, a systematic guide to help out researchers on their evaluations is not present.

### Presentation
4

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The authors argue that an effective and reliable evaluation is essential for advancing empirical machine learning. Nevertheless, benchmarks suffer from multiple biases, artifacts, or leakages, undermining their reliability. The authors propose a causal framework to address such challenges and identify several Common Abstract Topologies that could be used to gain insights into the reasoning abilities of large language models.

### Strengths
(S1)- The authors introduce an original perspective on the topic, diagnosing typical issues found in benchmarks and proposing a catalogue of Common Abstract Topologies rooted in causality to mitigate them.

(S2)- The authors motivate their approach in multiple use cases.

(S3)- Through the proposed framework, the authors understand that many assumptions made at different benchmarks would be made explicit, leading to better communication, transparency, and overall benchmark quality.

### Weaknesses
(W1)- The title is deceiving: it seems to address benchmarks in general, while the paper focuses only on benchmarks related to LLMs.

(W2)- While the idea is valuable, it is not clear how the whole benchmark specification should be done, and the benchmark implemented and validated against that specification. In fact, such an approach would require a library of CATs, means to implement them as a benchmark, and some validation tool to validate whether the benchmark complies with the specification.

### Questions
(Q1)- Did the authors consider some means to scan existing benchmarks and automatically propose CATs along with possible gaps that must be validated with human intervention to ensure adequate coverage vs. the original benchmark formulation?

(Q2)- While in the case studies, the authors reference several sources from the literature, did they execute some experiments to understand (a) to what extent the proposed strategies are helpful to the goal under consideration, and (b) what would be the impact of realizing the proposed approach in reality? To understand the potential impact providing some limited results and validation.

(Q3)- Could a similar approach generalize to other kinds of benchmarks, and the idea described in this paper provide the ground for a more general approach on how to ensure a certain level of benchmarking quality?

(Q4)- The authors are concerned with the reasoning process of a model to understand whether the reasoning is valid to arrive at a certain result. Did they consider a unified approach of explainability and causal assessment as part of the benchmark specification?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This position paper argues that the language and tools of causality offer an ideal framework to systematically address the myriad of challenges plaguing machine learning evaluation. The authors contend that many issues, such as biases, artifacts, and spurious correlations, are often treated with ad-hoc solutions but share underlying causal structures. To make causal modeling more accessible, they introduce "Common Abstract Topologies" (CATs) as simple, intuitive templates for confounding, mediation, and spurious links. Through a series of case studies focused on LLM reasoning, the paper demonstrates how this causal framing can clarify assumptions, motivate principled experiments, and lead to more generalizable insights than purely statistical approaches. Ultimately, the paper advocates for a shift towards more explicit, hypothesis-driven research grounded in causal principles to foster more robust and reliable scientific progress.

### Strengths
1. The paper unify a diverse problems described with vague terminology ("shortcuts," "cheating," "artifacts") under the framework of causality. This reframing into identifiable causal structures is a sound conceptual contribution.
2. The introduction of Common Abstract Topologies (CATs) is a brilliant device for making the often intimidating formalism of causal inference more accessible. By providing simple, recognizable graphical patterns (Table 1), the authors offer a practical starting point for researchers to begin incorporating causal thinking into their work.
3. The case studies (Section 4) provide concrete evidence for the paper's claims. The analysis of how a causal perspective yields a more general and intuitive solution for the label bias problem is particularly persuasive, directly demonstrating the technical superiority of the causal approach over a statistical one.

### Weaknesses
1. The paper aims to make causality more accessible, but correctly applying causal inference remains a highly skilled task. The leap from identifying a CAT to deriving the correct estimand using do-calculus (as in Equation 1) is non-trivial, and the paper may be slightly optimistic about how easily the broader community can adopt these methods without specialized training.
2. The CATs and case studies deal with well-defined, relatively low-dimensional problems (e.g., the effect of a single token or a specific model component). It is less clear how this framework would scale to diagnosing issues in the entire pre-training data-generating process of an LLM, which involves trillions of tokens and countless unobserved confounding factors.

### Questions
Your case studies are compelling but focus on well-circumscribed research questions. How would you propose applying the CATs framework to diagnose potential "monsters" in a far more complex and opaque setting, such as the web-scale data curation pipeline used for pre-training a foundation model?

### Presentation
3

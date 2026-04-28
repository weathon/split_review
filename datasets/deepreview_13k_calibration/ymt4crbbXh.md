# AutoBencher: Towards Declarative Benchmark Construction

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6

## Abstract
We present AutoBencher, a declarative framework for automatic benchmark construction, and use it to scalably discover novel insights and vulnerabilities of existing language models. Concretely, given a few desiderata of benchmarks (e.g., question difficulty, topic salience), we operationalize each desideratum and cast benchmark creation as an optimization problem. Specifically, we experiment with two settings with different optimization objectives: (i) for capability evaluation, we declare the goal of finding a salient, difficult dataset that induces novel performance patterns; (ii) for safety evaluation, we declare the goal of finding a dataset of unsafe prompts that existing LMs fail to decline. To tackle this type of optimization problem, we propose to use a language model to automatically construct datasets and iteratively revise the dataset to optimize for the declared desiderata. We use AutoBencher (powered by GPT-4) to create datasets for math, multilinguality, knowledge, and safety. The scalability of AutoBencher allows it to test fine-grained categories and tail knowledge, creating datasets that are on average 27% more novel and 22% more difficult than existing benchmarks. AutoBencher also helps identify specific gaps not captured by existing benchmarks: e.g., Gemini-Pro has knowledge gaps on Permian Extinction and Fordism while GPT-4o fails to decline harmful requests about cryptocurrency scams.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents AutoBencher, a declarative framework for automatic benchmark construction, and use it to scalably discover novel insights and vulnerabilities of existing language models. Specifically, it is instantiated in two scenarios: 1) capability evaluation and 2) safety evaluation.  In each scenario, a set of desirable characteristics is first formally defined. For capability evaluation, these are salience, difficulty, separability, and novelty. For safety evaluation, they are harmfulness and attack success rate.  Then, a language model is used to automatically construct descriptions of topics along with datasets in those topics, where a dataset is a set of (question, answer) pairs. Empirical results using GPT-4 as the evaluator show that the created datasets are on average 27% more novel and 22% more difficult than existing benchmarks. AutoBencher also helps identify specific gaps not captured by existing benchmarks: e.g., Gemini-Pro has knowledge gaps on Permian Extinction and Fordism while GPT-4o fails to decline harmful requests about cryptocurrency scams.

### Strengths
1. The problem of automatic benchmark generation in a guided manner is an important one. While LMs have been used as judges to automatically evaluate other LM's answers, this work proposes using LMs to also generate questions.

2. The problem is formalized and packaged in an elegant and extensible way in the AutoBencher framework, and two important instances of the framework are studied.  The two-step division (first generate topics and then generate datasets per topic) is especially novel and effective.

3. The proposed approach has two primary novel aspects: the use of a tool (such as a Wikipedia knowledge database or a Python library for mathematical calculations) to avoid the evaluating LM from generating answers that could be incorrect, and an algorithm to generate the benchmark in a guided rather than brute-force manner.

4. The empirical evaluation shows the promise of the proposed approach in generating datasets that are more novel and difficult than even hand-crafted ones like MMLU.

### Weaknesses
1. AutoBencher is currently stand-alone. The paper would be stronger if it integrated AutoBencher into existing popular evaluation frameworks like Stanford's HELM or HuggingFace's Open LLM. Adoption of AutoBencher by one of these frameworks would make a more convincing case for its usefulness and viability.

2. There seems to be a mismatch between the capabilities of the evaluating LM and the evaluated LMs: the former has access to tools whereas the latter does not. The paper does not make a convincing case why future LMs should be expected to have such capabilities without using tools themselves.

3. The evaluation is rather limited. I would expect a benchmark/evaluation focussed paper to be more comprehensive and derive more insights than those currently presented. For instance, AutoBencher currently only generates one-turn (question, answer) pairs; it would be interesting to see it extend to multi-turn data, chain-of-thought data, etc. Another direction to extend it could be in the domain of multi-modality.

4. I found the safety evaluation less convincing than the capability evaluation. While the paper does use recent baselines such as XSTest and HarmBench, it would be more convincing if the paper would report on how AutoBencher could be integrated into a mainstream framework for safety evaluation and discuss challenges that were overcome in such an integration (this is related to item 1 above but is more specific to safety evaluation).

### Questions
Please see Weakesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a method, Autobencher, to automatically construct benchmarks for evaluating language model (LM) capabilities and safety. Specifically, based on predefined criteria, the authors prompt an LM to propose dataset descriptions and generate questions, which a candidate LM then attempts to answer. The dataset is subsequently scored according to these criteria, enabling the selection of high-quality dataset descriptions. The authors aim to demonstrate that Autobencher generates dataset topics/descriptions that are both more novel and more challenging than existing benchmarks.

### Strengths
- The paper conducts experiments across a wide range of knowledge domains.
- The presentation is generally clear, with well-structured sections and a logical flow.
- Equations and figures are used effectively to enhance clarity.
- The automatic generation of benchmarks is a topic of strong interest to the community.
- The proposed method demonstrates significant performance gains over human-generated benchmarks, particularly in terms of novelty, difficulty, and separability metrics as defined in the paper.

### Weaknesses
 - It is not entirely clear to me what methodological novelties the paper introduces in dataset construction, aside from its use of retrieval during generation. Optimizing for various criteria objectives is not a particularly significant contribution.
- The introduction and abstract could benefit from revisions to be more specific and descriptive.
- The method and criteria rely on accuracy scores computed across both existing models and preexisting datasets, which can be computationally intensive, especially if generating multiple datasets across a large set of models.
- Additionally, language models (LMs) can exhibit high variance across different runs. A robust scoring criterion should account for this issue by incorporating variance between different runs, both for generating questions and answers. Introducing a statistical method to handle this variance would strengthen the contribution.
- Ensuring that the dataset description is clear and unharmful does not guarantee that all generated questions are equally clear and unharmful. For instance, a dataset labeled as "Nuclear technology" might contain questions of varying levels of harmfulness.
- There are concerns regarding the practicality of the method. While the paper claims high automation, many of the criteria still seem to require potentially time-intensive manual crafting. Furthermore, LM generations can be compute-intensive; a discussion on the computational resources required for these generations would be beneficial.
- Additional ablation studies could help demonstrate the impact of various components of the method.

### Questions
- In Section 3.1 on separability, are you taking the mean over $acc(\cdot) \in V_c$? If so, this should be clarified. Additionally, I am not convinced that high deviation alone ensures that rankings between any two models, $LM_i$ and $LM_j$, with $i \ne j$, are robust to noise.
- Using vector notation could help make the equations clearer.
- In Section 3.1 on novelty, it seems that there is a coefficient for each model being evaluated. Could you elaborate on why there are coefficients for each model rather than for each dataset?
- How are the salience and harmfulness binary variables obtained in practice?
- I am unclear about the procedure for qualitative assessment in Section 6.3. What does "high quality" mean, and how many question-answer pairs were sampled? What do the "ranks" in this section refer to?
- What language model was used to generate Table 1? Adding this information to the caption would improve clarity.
- Are there any ablation experiments on the following: the language model used, the criteria for evaluating dataset descriptions, and the impact of including privileged information?
- Are the human benchmarks also grouped into distinctive categories and descriptions similar to those proposed by the language model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose to use an LM-guided adaptive search to construct benchmarks that optimise (1) difficulty (benchmark headroom), separability (existing model variance), and novelty (rank correlation with other benchmarks) and (2) attack success rate (when trying to extract harmful information from models). They demonstrate the need for this by showing that existing benchmarks exhibit low values in novelty (especially) even for benchmarks such as MMLU where there is sufficient headroom. Further, they use privileged information to enable a weaker LM to assess a stronger LM, use translation tools to enable multi-lingual data and employ source code/python to evaluate numerical and symbolic expressions. When optimising, the authors employ an adaptive search strategy that uses the history of explored subjects to guide the new candidates restricted to a salience set. To assess the quality of the generated data, the authors employ Mechanical Turk and find sufficiently low error rates with high salience on the questions. The value of adaptive search is demonstrated via an ablation on the use of the history vector. Both regimes demonstrate improvement over HumanEval on the desired metrics.

### Strengths
+ On novelty, the approach generates human interpretable topics where model ranks exhibit surprising results.
+ On safety, the qualitative examples align with the experience of this reviewer when trying to manually jail-break LLMs: pose the question as a hypothetical or philosophical debate; this vector being auto-discovered is encouraging.
+ Well-executed research methodology with manual validation of the discovered benchmarks

### Weaknesses
 - The approach to the math and science categories suggests an open vocabulary problem that is not clearly tackled. For other categories, this is tackled via Wikipedia and a popularity metric.
- The translation induces an issue for low-resource language: such languages are both less likely to be tackled by LLMs and by translation tools, creating a catch-22. (I feel it would be sufficient to acknowledge the issue as a limitation since tackling the issue requires significant manual effort, future work can consider specialised models for specific language pairs.)

### Questions
1. To the knowledge of this reviewer, it should be possible to have a hyper-/hyponymy graph of Wikipedia topics. Did you consider using such a graph, or a similar topic relationship graph to further guide the adaptive search?
2. The optimisation problem for case (1) is multi-objective, is there a reason why multi-objective optimisation was not employed and instead the loss is linearised by adding hyperparameters? (evolutionary/population-based methods?)
3. Related to W1, how is the math/science salience set constructed? Unless I missed it in the paper, the inclusion-exclusion criteria were not clear or indeed the exact methodology. Did you perform, for example, open card sorting or a similar methodology?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces AutoBencher, a declarative framework that automatically generates benchmarks to evaluate language model performance by defining specific desiderata, such as difficulty, novelty, and safety. The proposed approach, AutoBencher, leverages language models to iteratively construct benchmarks that reveal weaknesses and safety vulnerabilities in LLMs.

### Strengths
1-The paper is well-written and very easy to understand.

2- The paper provides an in-depth empirical evaluation, uncovering vulnerabilities and assessing model performance. It also includes results from human evaluations to further validate the quality and relevance of the generated benchmark.

3- AutoBencher automatically constructs datasets, making it highly scalable and reducing reliance on costly human labor. This is useful for evaluating LLMs across various domains.

### Weaknesses
1- The details of the qualitative analysis are missing.

2- AutoBencher uses GPT-4 as the evaluator, which may introduce potential bias in datasets that could favor LLMs from the same family (e.g., OpenAI's LLMs).

### Questions
1- How does AutoBencher differ from previous work on automatic benchmarking, such as that in [2]?

2- Why is a comparison with the baseline included?





[1] Taskbench: Benchmarking large language models for task automation.

### Soundness
3

### Presentation
4

### Contribution
3

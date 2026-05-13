# Matchmaker: Schema Matching with self-improving compositional LLM programs

- Decision: Reject
- Scores: 5, 5, 3, 8

## Abstract
Schema matching -- the task of finding matches between attributes across disparate data sources with different tables and hierarchies -- is critical for creating interoperable machine learning (ML)-ready data. Addressing this fundamental data-centric problem has wide implications, especially in domains like healthcare, finance and e-commerce --- but also has the potential to benefit ML models more generally, by increasing the data available for ML model training. However, schema matching is a challenging ML task due to structural/hierarchical and semantic heterogeneity between different schemas. Previous ML approaches to automate schema matching have either required significant labeled data for model training, which is often unrealistic, or suffer from poor zero-shot performance. To this end, we propose Matchmaker -  a compositional language model program for schema matching, comprised of candidate generation, refinement and confidence scoring. Matchmaker also self-improves in a zero-shot manner without the need for labeled demonstrations via a novel optimization approach, which constructs synthetic in-context demonstrations to guide the language model's reasoning process.  Empirically, we demonstrate on real-world medical schema matching benchmarks that Matchmaker outperforms previous ML-based approaches, highlighting its potential to accelerate data integration and interoperability of ML-ready data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper deals with schema matching, and old but very important problem in databases. The idea is that, given one starting (relational) schema and one target schema, to be able to match which attributes in the  starting schema correspond to attributes in target schema. The proposal in this paper is Matchmaker. This system uses a mix of retrieval using multi-vector representation and LLM-based reasoning to produce candidates for the matching, and then applies a final LLM-driven step to refine these candidates. Notably, the program also is built so that it can optimize the last step by providing examples from the databases. All together, the system shows quite an advantage over previous proposals.

### Strengths
- Very well written 
- Addresses an importan tproblem that has ben recently identified as a target for the ML community
- Provides a thorough experimental section, including a (very nice) ablation study to understand the impact of different strategies for candidate generation.

### Weaknesses
 - While the paper is well writtend and scientifically sound, the algorithm itself (matchmaker) is not groundbreaking. Matchmaker resolves basically on building appropriate chain of thought prompts, as well as applying semantic similarity techniques. As such, I see this mostly as a paper describing a particular, LLM-based proposal, to address this problem. 
- There seem to be a lack of LLM-dirven alternatives to compare with, which is both good for the paper (because authors are the first to apply them in this context), but it also raises the question on whether any other similar approach would produce similar results. 
- The problem itself ( schema matching, or more generally data harmonization/interoperability) is not a core problematic of ICLR. I would imagine this paper would be more suitted to a database conference.

### Questions
Why haven't you submitted this to a database conference? It seems to me that the reception and impact there would be much higher.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a zero-shot schema matching approach by leveraging the multi-stage call of LLMs to generate, refine, and score the matchings.  Specifically, it introduces synthetic examples to guide the reasoning of LLMs for improving and optimizing the results of schema matching. The experiments on medical schema matching benchmarks demonstrate that the proposed approach outperforms the selected baseline methods on accuracy. 

The paper does a great job of demonstrating the problem that they are solving and the methodology they presented. 
The main contribution is decomposing the schema matching task into multi-stage sub-tasks that are completed by multiple calling of LLMs, with retrieval from contextual reasoning and prompt optimization based on in-context examples. However, the contribution of this work is limited, as they only introduce the muti-stage schema matching by extending the calling of LLMs from single to multiple.

### Strengths
S1: The idea of leveraging the multi-stage LLMs for schema matching is novel.

S2: The authors do a great job of demonstrating the challenges of schema matching in real-world scenarios that they are trying to address and the methodology they presented. 

S3: Several experiments on MIMIC-OMOP and Synthea-OMOP datasets are conducted to empirically investigate and demonstrate the performance of the presented method.

### Weaknesses
W1: The contribution of this work is limited, as they only introduce the muti-stage schema matching by extending the calling of LLMs from single to multiple.  

W2: The accuracy@k is the only metrics that is reported in experimental results, the results on precision are missing. 

W3: The prompts are provided in the appendix, but the source code is not provided for reproducibility.

W4: The GPT-4 (0613) is the only backbone model, the results of using llama as backbone are not reported.

### Questions
Q1: How does your approach work in terms of precision when compared with the baseline method?

Q2: How confident when ranking the LLM-generated candidates with LLM-based scores? How much does this ranking contribute to the results?

Q3: Could you provide the details of how the vector retrieval works in Sec 4.1?
If I understand well, you retrieve the top-k matching from the target schema attribute based on MaxSim between query embeddings and target schema embeddings. However, the granularity of the query embeddings and target schema embedding is different, query embedding is an attribute-level embedding while target schema embedding is a table-level embedding.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors considered the schema matching problem for
tabular structured data. In particular, a schema is defined as a set
of tables {T_1, ..., T_m}, where each table T_i has a set of
attributes {A_{i,1}, ..., A_{i,n_i}}. Additionally, it is assumed that
each table T_i is associated with some metadata describing its purpose
and content, and each attribute A_{i,j} is associated with some
metadata describing its type and relational context. Then, given a
source schema S including a set of attributes A_S and a target schema
T including a set of attributes A_T, the goal of schema matching is to
find a partial function f : A_S -> A_T such that if f(A) = B for
attributes A in A_S and B in A_T, then B is the corresponding target
attribute to the source attribute A.

The algorithm proposed in the paper for schema matching works as
follows. Given a source attribute A, the algorithm uses embeddings of
A and the target attributes to retrieve the top-k matching target
attributes. The generated set of target attributes is called the
semantic retrieval candidates for A. Then the algorithm generates a
set of reasoning-based candidates using a reasoning LLM. The union of
semantic retrieval candidates with reasoning-based candidates
constitutes the set of candidates for A. Then the algorithm uses a
refiner LLM to reduce the number of candidates, and it finally ranks
the resulting candidates and filters out the non-suitable ones. If the
resulting set of target attributes is not empty, then the top-scored
attribute can be considered as the corresponding target attribute for
A.

### Strengths
S1) The schema matching problem is fundamental to generating large,
    integrated, and interoperable datasets. In this sense, this paper
    addresses a relevant and interesting problem.

S2) The experimental evaluation shows that the proposed approach
    outperforms other schema matching approaches in terms of accuracy.

### Weaknesses
W1) The approach proposed in the paper essentially disregards the
    large body of work on schema matching that has been developed for
    decades in the database field.

W2) The schema matching problem is not properly formalized.

### Questions
General comments

The schema matching problem is fundamental to generating large,
integrated, and interoperable datasets. In this sense, this paper
makes a contribution by proposing a new method for this problem that
takes advantage of certain capabilities of LLMs. Besides, the
experimental evaluation provides evidence that the proposed method
outperforms other schema matching approaches in terms of
accuracy. However, I have two serious concerns about the contribution
of this paper:

- The schema matching problem is not properly formalized. The authors
  provide a formal definition of this problem where they indicate that
  mapping function f "correctly" assigns each attribute of the source
  schema to an attribute of the target schema. How is the
  "correctness" of f defined? What are the properties that a correct
  mapping function f should satisfy? Does the algorithm proposed in
  this paper compute a function f that satisfies such properties? None
  of these questions is answer in the paper.

- The authors disregard the large body of work on schema matching that
  has been developed in the database area. I am not going to mention
  here the relevant literature on schema matching, which is an
  established area within databases, but I would like to note that one
  can already find surveys on this topic from more than 20 years ago:

  Erhard Rahm, Philip A. Bernstein: A survey of approaches to
  automatic schema matching. VLDB J. 10(4): 334-350 (2001)

  Notice that the problem considered in this paper is schema matching
  for relational databases, which is exactly the scenario discussed in
  this survey.

  A first obvious step in considering the work on schema matching done
  in databases is to compare the method proposed in this paper with
  methods from the database field. But this is just the tip of the
  iceberg and probably not the most fruitful way. The method proposed
  in this paper can be improved by considering the more classical work
  in schema matching. For example, the authors could leverage this
  work in the generation of candidates, and they can address issues
  with the formalization of the schema matching problem by reusing its
  formalization from the database field.


Specific questions

All these questions refer to the definition of the schema matching
problem:

- How is the notion of correctness of a mapping function f defined?

- What are the properties that a correct mapping function f should
  satisfy?

- Does the algorithm proposed in this paper compute a function f that
  satisfies such properties?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Matchmaker, a novel approach to schema matching using a self-improving compositional language model program. Schema matching is crucial for creating interoperable ML-ready data by finding correspondences between attributes across different databases. Matchmaker operates through three main components: multi-vector document creation, candidate generation (using both semantic retrieval and LLM-based reasoning), and confidence scoring. A key innovation is its ability to self-improve without labeled data through synthetic in-context examples. The method significantly outperforms existing approaches on real-world healthcare schema matching benchmarks (MIMIC-OMOP and Synthea-OMOP).

### Strengths
1. Addresses a critical practical problem in data integration that has significant implications for ML development
2. Novel technical approach combining retrieval and LLM reasoning in a compositional program
3. Zero-shot learning capability through synthetic in-context examples, eliminating the need for labeled training data
4. Comprehensive empirical evaluation against multiple baselines
5. Practical considerations for deployment, including human-in-the-loop integration and uncertainty handling
6. Strong quantitative results showing 15-20% improvement over baselines
7. Well-documented implementation details and ablation studies

### Weaknesses
1. Limited evaluation to two healthcare domain datasets, though the approach is claimed to be general. The evaluation should include a more diverse set of schemas from different domains to validate the general applicability of the method. The current evaluation only demonstrates performance within the healthcare domain, which may not be representative of other domains with different data structures and semantic complexities. For example, schemas from e-commerce, finance, or social media could provide a more rigorous test of the method's generalizability.
2. The synthetic in-context example generation process could be explained more clearly. The paper lacks a detailed explanation of how the synthetic examples are generated, making it difficult to understand the self-improvement mechanism. The process should specify how the 'easy' and 'challenging' queries are defined and how the intermediate input-output pairs are extracted from the LLM program's execution traces. Furthermore, the criteria for selecting the top-n traces based on the evaluator LLM's scores should be made explicit, including the specific prompts used for the evaluator LLM.
3. The paper shows strong performance metrics but doesn't provide detailed analysis of where and why Matchmaker fails. While the paper presents overall performance metrics, it lacks a detailed error analysis that could provide insights into the method's limitations. A more granular analysis of the types of errors made by Matchmaker, such as incorrect matches due to semantic ambiguity or structural differences, would be beneficial. For example, it would be useful to know if the method struggles more with certain types of attributes or schema structures.

### Questions
1. How does the performance of Matchmaker scale with very large schemas (>1000 attributes)?
2. Could the approach be extended to handle many-to-many mappings between schemas?
3. How sensitive is the performance to the quality of attribute descriptions in the schemas?
4. What strategies could be employed to reduce the number of LLM calls while maintaining performance?
5. How might the system handle schemas in languages other than English?

### Soundness
4

### Presentation
4

### Contribution
3

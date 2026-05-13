# Rethinking and improving autoformalization: towards a faithful metric and a Dependency Retrieval-based approach

- Decision: Accept
- Scores: 6, 8, 6, 8, 8

## Abstract
As a central component in formal verification, statement autoformalization has been widely studied including the recent efforts from machine learning community, but still remains a widely-recognized difficult and open problem. In this paper, we delve into two critical yet under-explored gaps: 1) absence of faithful and universal automated evaluation for autoformalization results; 2) agnosia of contextural information, inducing severe hallucination of formal definitions and theorems.
To address the first issue, we propose **BEq** (_**B**idirectional **E**xtended Definitional E**q**uivalence_), an automated neuro-symbolic method to determine the equivalence between two formal statements, which is formal-grounded and well-aligned with human intuition.
For the second, we propose **RAutoformalizer** (_**R**etrieval-augmented **Autoformalizer**_), augmenting statement autoformalization by _Dependency Retrieval_, retrieving potentially dependent objects from formal libraries.
We parse the dependencies of libraries and propose to _structurally informalise_ formal objects by the topological order of dependencies. To evaluate OOD generalization and research-level capabilities, we build a novel benchmark, _Con-NF_, consisting of 961 informal-formal statement pairs from frontier mathematical researches.
Extensive experiments validate the effectiveness of our proposed approaches. In particular, BEq is evaluated on 200 diverse formal statement pairs with expert-annotated equivalence label, exhibiting significantly improved accuracy ($82.50\\% \mapsto 90.50\\%$) and precision ($70.59\\% \mapsto 100.0\\%$).
For dependency retrieval, a baseline with excellent performance is established.
The proposed RAutoformalizer substantially outperforms SOTA baselines in both in-distribution ProofNet benchmark ($12.83\\% \mapsto 18.18\\%$, BEq@8) and OOD Con-NF scenario ($4.58\\%\mapsto 16.86\\%$, BEq@8). Code, data, and models will be available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work attempts to address two important gaps in statement autoformalization currently: 1) absence of an automated and accurate evaluation metric for autoformalization; 2) models' agnosia of contextural information during autoformalization, inducing severe hallucination of formal definitions and theorems. 

- To address 1), the paper proposes BEq (Bidirectional Extended Definitional Equivalence), a neural-symbolic metric that determines the equivalence between an autoformalized statement and the ground-truth formal statement by taking advantage of Lean 4 features.

- For 2), the paper introduces RAutoformalizer (Retrieval-augmented Autoformalizer) which (a) uses dependency retrieval to find relevant formal objects from libraries, then (b) proposes topological informalization to structure training data. RAutoformalizer significantly improves performance on ProofNet and the out-of-distribution benchmark Con-NF.

- The authors also synthesized Con-NF, a new benchmark with 961 informal-formal statement pairs, by informalizing from a frontier mathematical library that has not been adopted before, to evaluate OOD generalization capabilities in autoformalization.

### Strengths
1. **Originality**:

- BEq is one of the pioneer metrics for evaluating autoformalization different from existing ones. It is built based on human intuitions about statement equivalence and implemented using Lean 4 features, thus having the potential advantage of being more interpretable and predictable (although not elaborated in the paper), if provided with high-quality ground-truth formal statements.
- The paper also formulates the problem of autoformalization as bidirectional definitional equivalence. This approach differs from previous formulation efforts (e.g., https://arxiv.org/pdf/2410.04194).
- RAutoformalizer introduces a typological informalization and dependency retrieval pipeline to reduce context agnosia. The Con-NF benchmark also emphasizes the importance of OOD evaluation for future researchers.

2. **Quality**: 
  - Uses both in-distribution (ProofNet) and out-of-distribution (Con-NF) testing; 
  - Includes ablation studies to validate technical choices; 
  - Provides training details for RAutoformalizer.

3. **Clarity**: The motivations are coherent. The writing and illustrations are mostly clear. However, improvements can be made regarding the formal problem setup when introducing BEq as well as the implementation procedures.

4. **Significance**: The paper aims to address two important problems in autoformalization that are both relevant and challenging. The significance is very valid, although the applicability of BEq is compromised as mentioned later.

### Weaknesses
BEq:

1. **Limited applicability**:
   - A limitation of BEq for evaluating autoformalization is it focuses on the matching between ground-truth formal statement and the autoformalized statement, hence it always requires ground-truth formal statements. In other words, BEq disregards the informal statement input and relies heavily on the *quality* of the ground-truth formal statement that the human experts provided. It also relies on the tactic features of Lean 4. This greatly hurts the applicability of the metric to many larger-scale informal-formal language benchmarks without expert-annotated ground-truths or written in other formal languages. It also makes it questionable whether BEq can even be directly used on synthesized benchmarks like Con-NF where the informal-formal statement pairs are not checked by human experts. The reliance on ground-truth formal statements and Lean 4 tactics severely limits the metric's generalizability.
   - The weakness should be also be mentioned in the theoretical constraint of the problem formulation in section 3. Fundamentally, BEq distills the problem of evaluating autoformalization into the problem of evaluating 'Definitional Equality' between two formal statements in Lean 4. However, this overlooks two constraining assumptions that should be ensured about the autoformalization benchmarks: (1) the ground-truth formal statements are aligned with the informal statements; (2) the ground-truth formal statements are successfully type-checked. These assumptions are not always guaranteed in practice, especially in large-scale datasets.

2. **Limited robustness**: There are few experiment details about how human evaluation are conducted such as the expert numbers, competence levels, annotation protocols, annotation processes, agreement rates, etc. Considering that evaluating formal statements is a challenging task that frequently induces high disagreement rates among experts in practice, the rigor of BEq and Table 1 results is in question.  The lack of detailed information about the human evaluation process makes it difficult to assess the reliability of the results.
3. **Unclear experimental setting missing material support**: The paper also did not provide concrete experimental details about Beq such as (a) the few-shot prompt for LLMs on transformation T (line 261), (b) the few-shot prompt for LLMs graders on formal statement matching (line 303). The authors cited Ying et al. (2024a) and stated they used a stronger few-shot setting of their prompt, but I did not find the corresponding prompt template in the reference. It is difficult to review the exact implementation process and experimental details, hurting the robustness and reproducibility of the work.  The absence of specific prompt details and implementation procedures makes it hard to reproduce the experiments.
4. **Writing clarity issue**: The formal setup of BEq is unclear. Please check point 1 and 2 in Questions for details.

RAutoformalizer:

5. **Benchmark construction rigor**: The OOD benchmark Con-NF is constructed by prompting LLMs to typologically informalize the formal objects in a new library. There is little quality control as to the informalization quality. This is especially concerning since we are synthesizing data from a new library that LLMs are probably never exposed to. Two issues may arise from this that have been noted in previous research:
   - There could be a great discrepancy between the informal statements in Con-NF that serve as autoformalization input and the groundtruth formal statements from the first place. The lack of human verification of the synthesized informal statements raises concerns about the benchmark's reliability.
   - In LLM informalization via prompting, a common issue is that the informalized output often still includes the names of the formal tactics or variables verbatim, because there does not exist a corresponding concept in the natural language that can be used to easily translate the complex functions or relationships in formal language. In more extreme cases, some theorems are not even translatable formally or informally. The paper did not report any filtering procedures or quality checks regarding the potential benchmark issues above. The potential for formal identifiers to leak into informal statements could bias the evaluation.

6. **No human evaluation in comparing RAutoformalizer**: Table 3 compares the autoformalization performance of RA with other baselines on ProofNet and OOD Con-NF using two automated metrics: Typecheck and BEq. Because the robustness of BEq itself is limited as discussed above, the significance of the table results is compromised unless human evaluations are provided. The absence of human evaluation for RAutoformalizer makes it difficult to validate the results.

### Questions
1. I am not clear what the notion ‘transformation primitives’ in line 215/ line 221 means: in some in autoformalization research, 'transformation' is sometimes an equivalent of 'autoformzalization', but here apparently it is not the case. Does 'all transformation primitives' here refer to all functions defined in Definitional Equality in Lean 4 (e.g., α-conversion, η-expansion etc.)? The confusion about transformation T continued regarding how LLMs are prompted to implement the transformation function T. The paper would be clearer and more reproducible if the authors provide more accurate declarations of each symbol and notion, as well as the exact prompt template they use for few-shot prompting. Another example of ambiguous symbol usage is ‘s\_P’ versus ‘theorem P’. 
 
2. Following the question about T, I wonder how the authors derive the Unidirectional Definitional Implication (2) from equation (1) by explaining how transformations can occur between a formal statement and a proof goal in Lean 4 around line 225-236. Is the T in (2) an approximation of T in (1), based on the fact we can switch between proof goals and formal statements in Lean 4?  

3. A recent work called FormalAlign introduces a metric for autoformalization evaluation to address the first limitation in this paper by training a *formal-informal statement alignment* evaluator, rather than focusing on *formal-formal equivalence*: [https://arxiv.org/pdf/2410.10135v1](https://arxiv.org/pdf/2410.10135v1). The authors are suggested to discuss this in the related works section and ideally include a comparison with this metric as a baseline.  

4. Typo and grammatical issue: 
   - Line 097 (‘A baseline is build’); line 199 (‘with how humans instincts.’); 
   - In Table 3, in the Con-NF / Typecheck@1↑ column, LW achieves the highest (28.10%) but RA is marked bold (20.50%). If there is indeed a mistake here, the body text should also be adjusted.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses a few key challenges in the problem of LLM-based AutoFormalization. Firstly, they introduce BEq - a new metric to determine equivalence of formal statements -allowing for a better quantification of success for the task. Secondly, they propose RAutoformalizer a new autoformalization technique that retrieves dependent formal objects using informal statements. Lastly, to quantify out of distribution generalization, they propose a new benchmark for the task - Con-NF. They empirically demonstrate that BEq provides expert level performance on determining semantic equivalence of formal statements and then report significantly better results using RAutoformalizer compared to existing SoTA approaches.

### Strengths
1. The paper is very well-written, easy to follow and well-organized.
2. The paper presents various key contributions to the Autoformalizer literature in the form of BEq and RAutoformalizer - which can have a great impact research in this area significantly. 
3. The BEq metric solves a key challenge in determining equivalence and is a promising alternative to contemporary techniques. I forsee more future work in the literature using this as an importatnt metric of success. 
4. The RAutoformalizer technique outperforms current SoTA Autoformalization techniques significantly.

### Weaknesses
While I don't see any major weakness in the paper,there are a few minor concerns that maybe worth looking at: 
1. BEq as a metric is quite promising, it is not very clear how does it fundamentally align with human judgements. It may be interesting to go a bit deeper into this in the paper. 
2. It is not very clear what kinds of benefits the retrieval component in RAutoformalizer is bringing and what are existing gaps from the ground truth retrieval setup. 
3. The ICL baselines are a bit too week. It would have been interesting to see how frontier models like DeepSeek and GPT-4o perform with the retrievals provided to them in-context as well.

### Questions
Please refer to the Weakness section.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper aims to improve existing statement autoformalization paradigms by two key limitations: 1. absence of faithful and universal automated evaluation for autoformalization results; 2 agnosia of contextural information. To this end, the paper trains a retriever to retrieve dependent information and a autoformalizer to attempt the proof.

### Strengths
1.	The design of the training protocol seems reasonable, like the formal data in existing library is parsed into informal sentences and stored in topological order. The retrieval first and generation next works well for autoformalization.
2.	The experiment result shows that the newly proposed BEq method surpasses baselines by a landslide.
3.	A novel benchmark, Con-NF is built from frontier mathematical researches.

### Weaknesses
Some certain details can be included to make the paper more self-contained. Like the reason why the dense embedding is sufficient for the dependency retrieval.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present three contributions to the field of autoformalization. First, a new evaluation metric (BEq) which better aligns with human evaluation compared to classic Machine Translation metrics. This is done by extending the concept of definitional equivalence, which can be overly strict in certain cases and not allow enough flexibility to accept all possible correct answers. Second, the authors introduce a retrieval-augmented autoformalization method which retrieves necessary dependencies for a theorem before formalization. Finally, the authors introduce a new task (dependency retrieval) and associated benchmark (Con-NF) to help measure performance for research-level autoformalization.

### Strengths
The authors work on an important problem in autoformalization, namely the lack of flexible automatic metrics. Their approach is well-explained and well-motivated, and I believe it can be of significant use to the community. BEq significantly improves over other metrics in terms of human-alignment. I believe this is the strongest contribution of the paper. 

Similarly, the dependency retrieval task is a fundamental task in autoformalization, since otherwise we expect LLMs to be fluent in all necessary context, which is impossible for research-level mathematics which are introduced after the LLM was trained. Thus, the introduction of the task together with a benchmark and baseline approaches is a strong contribution.

Overall I think this paper is a solid contribution to the community and is well-supported by the experiments.

### Weaknesses
While the BEq metric improves on previous metrics, one of its shortcomings is that it requires gold label formal statements (compared to, for example, type checking, which only requires the input data). Both training data and benchmarks are lacking in this area, making BEq less impactful overall. 

Additionally, BEq requires a 20b parameter model to execute, severely restricting access to the metric for researchers without the necessary compute. A significant improvement would be reducing this model size, even to a 7b size which would make inference possible on much smaller devices and with improved efficiency. I didn't notice any performance comparison between various model sizes, which could improve the stance of this model choice.

### Questions
Have you tested different model sizes for the BEq metric? If so, what performance drop-off did you see with smaller models? An analysis of different failure cases for these models would also be very insightful, and could offer avenues for improvement.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper improves the statement autoformalization by identifying and solving two key problems. First, they proposed BEq, a better LLM-based way to check if autoformalizations are correct by combining symbolic rules, and the human evaluation proves it's promising. Second, they created RAutoformalizer, a RAG approach, which looks up relevant dependent objects for auto-formalization. Also, authors annotated an OOD benchmark for further evaluation. The experiments show their methods are better than baselines.

### Strengths
1) This paper propose a new LLM-based evaluator BEq for statement auto-formalization, which make it more flexible as human evalution.
2) Authors designed a RAG-based auto-formalization framework by Dependency Retrieval
3) Authors annotate a new benchmark to evaluate OOD performance of their method.
4) Experiments show their fine-tuned retriever and whole RAG system more effective than baselines.

### Weaknesses
In general, this is a well-structured and written papers. But I still have some concerns about each components of contributions.

### Introduction Narrative:
1) In the Line 90-99, it would be more clear if authors can first state why they propose **dependency retrieval**. Why this new task is essential in the context of current methods.
2) In Line 65-75, it would be more helpful for authors to provide more contexts like citations to introduce statements, i.e., 
    - The discussion of β-reduction and type checking limitations (Lines 65-75) needs citations or examples demonstrating these issues
    - The statement about type checking being "too weak" requires empirical evidence or references to prior work.
3) Authors state some disadvantages of "LLM graders". Could authors provide more citations stating this? 
    - The paper critiques LLM graders as "non-determinant and highly dependent on prompts" but doesn't sufficiently distinguish how BEq (which also uses LLMs) overcomes these limitations.
    - The few-shot prompting used in BEq seems to face similar prompt-design challenges that the authors criticize.
    - While Table 1 shows improved performance, more analysis is needed to demonstrate that BEq fundamentally addresses the cited limitations of LLM graders raised in the introduction.

### BEq Evaluator:
1) How few-shot prompting design in BEq pipeline can release human designed efforts of previous works as mentioned in the line 66-68 (Introduction)?
2) It seems that the BEq is implemented by a specific math LLM, InternLM2-Math-Plus-20B. Choice of InternLM2-Math-Plus-20B needs justification:
   - Is its math pretraining superior to alternatives?
   - Table 1 shows DeepSeek V2.5 outperforms InternLM2-Math-Plus-20B in majority voting
   - Why not implement BEq with DeepSeek V2.5? Is model size a constraint?
Authors need to demonstrate BEq pipeline works across multiple math LLMs to show BEq doesn't only work in specific models, which supports claims about not requiring extensive efforts in specific prompt designs (lines 66-68)
3) In the **Human Equivalence Benchmark**, There are some details requiring clarification to convince readers for fairness of BEq:

   - The mechanism for creating "ground truths": whether through expert annotation, rule-based generation, or other techniques - remains unclear. If experts are involved, the potential overlap between pair creators and equivalence evaluators raises concerns about evaluation independence. The justification for using only 200 cases appears insufficient given Con-NF's larger scale of 900+ cases. Moreover, the validation of ground truth existence in ProofNet needs more rigorous documentation.
   - This part suffers from insufficient documentation of expert qualifications and procedures. The paper fails to specify whether experts were students, authors, or third-party experts, and their required expertise level. Critical operational details are missing, including payment structures, annotation guidelines, and the workflow for equivalence labels. The process for handling cases with multiple valid ground-truths remains ambiguous, as does the distinction between "expert label equivalence" and "ground-truths."
   - The benchmark shows concerning signs of potential sampling bias. The non-uniform sampling evident in Figure 3 requires better explanation, and the paper doesn't adequately address how bias was controlled in LLM-generated examples. The O1 bias control mechanism and prompting strategies need clearer documentation. Additionally, the absence of label distribution information makes it difficult to evaluate the fairness of BEq.

These limitations significantly impact the trust of implementing BEq based on specific LLM for such task.

4) Potential biased benchmarking: I think one of the biggest concern along the entire paper is that it seems the specific LLM InterLM-math conducts the whole evaluation, method backbones. The family of Large Language Models (LLMs) trained on similar datasets inevitably shares inherent biases, which affects evaluation consistency. Did BEq, driven by InterLM-math, gain an unfair advantage in Authoformalization performance if it leverages the same InterLM-math framework? I think a more direct solution to resolve this concern is to show results that BEq implemented by different math LLMs.

### Method:

While Section 4 identifies "nonexistent definitions in library" as a main source of hallucinations and proposes RAG-based solutions, it requires empirical validation of improvement. Table 3 shows overall performance gains but doesn't isolate how much comes from reducing such hallucinations. The paper needs quantitative analysis or visualization demonstrating the specific impact of RAG methods on how effectiveness of hallucination reduction.

### Benchmark:
1) It's nice to see that the authors have annotated a new benchmark, Con-NF, to explore the effectiveness of the OOD capabilities of the developed methods. However, there are no details about benchmark construction or distributions. For example, how was the annotation performed, and what are the topic or problem distributions of the new datasets? Since the authors mention this is an OOD dataset, it would be better to compare the distributions between ProofNet and Con-NF in terms of objectives and disciplines to illustrate how they differ as OOD datasets. I think it’s insufficient to simply mention that one is for under-graduate level and the other for research level, as there is a possibility that they share similar foundational theorems or objects and dependencies or overlapped.

2) Why did the authors choose to create new datasets from scratch instead of utilizing existing ones, such as [1]? It would be more effective for the authors to first specify the features they wish to capture that are not present in existing datasets, thus justifying the need for this curation. If there are existing datasets that already contain the desired OOD features, the reason for annotating a new dataset is less convincing, especially given the lack of detailed descriptions regarding its construction. 

### Experiments:
As mentioned, just one backbone math LLM InterLM2-math is not enough. Given a global view of this paper, the metrics are designed specifically by authors and InterLM2-math, the benchmark is annotated by authors, and models in methods are chosen and fine-tuned by the same specific models, the fairness is quite questionable. More datasets and LLM backbones are required in evaluation.

Also more baseline methods and implementations are required. For example:
- Basic reasoning baselines like COT, TOT, Self-Consistency should be compared.
-  [1] implemented ReProver, a RAG method for automated theorem proving in Lean. Differences with workflows in this paper and [1] should be explained and compared. The novelty of this paper appears limited compared to [1] if the performance comparison and analysis are not clarified.
- I don't think it's fair to conduct all fine-tuned methods on one specific model InterLLM2-math, instead, I concern that whether such framework only works for such LLM especially the metric of BEqs is implemented by the same family of LLM (InterLLM also...).

### Questions
## Introduction:
1. Why is dependency retrieval essential in the current context, and how does it address existing limitations?
2. What evidence supports the claims about β-reduction and type checking limitations? Can authors provide citations or examples?
3. How does BEq construction overcome the "non-determinant and highly prompt-dependent" limitations of LLM graders when it also uses LLMs and few-shot prompting?

## BEq Evaluator:
1. How does BEq's few-shot prompting actually reduce human design efforts compared to previous approaches?
2. Why choose InternLM2-Math-Plus-20B when: DeepSeek V2.5 shows better performance in majority voting? 
3. What makes its math pretraining superior? Why not implement BEq with other models? 
4. Can BEq work effectively across different math LLMs?

## Human Equivalence Benchmark:
1. How were ground truth pairs created and validated in details?
2. What are the expert qualifications, payment structures, and annotation guidelines?
3. How was sampling bias controlled in terms of the following aspects:
   - LLM-generated examples?
   - non-uniform distribution in Figure 3?
   - O1 bias control mechanisms to make sure the quality of evaluation?

## Method:
1. How effectively do RAG methods specifically reduce hallucinations in depth?
2. Can authors quantify the improvement in Table 3 attributed to hallucination reduction for "non-existing dependencies" especially?

## Con-NF Questions:
1. What are the construction details and distributions of Con-NF?
2. How do ProofNet and Con-NF differ in terms of discipline, problem distributions and theorem or dependencies?
3. Why create new datasets instead of using existing ones like [1]? What are exact features considered as OOD comparing to exisitng benchmarks so that authors have to spend efforts in annotating a new benchmark?

## Experimental Questions:
1. How would results differ with multiple LLM backbones?
2. Why weren't standard reasoning baselines (COT, TOT, Self-Consistency) included? Comparing with such basic reasoning mehtods is crucial.
3. How does this work differ from ReProver [1]?
4. Does the framework only work effectively with InterLLM2-math? More implementations of different families of LLMs with BEqs are required.

### Soundness
3

### Presentation
3

### Contribution
3

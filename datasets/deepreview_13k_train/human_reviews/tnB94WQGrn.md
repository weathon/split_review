# Knowledge Graph Based Agent For Complex, Knowledge-Intensive QA in Medicine

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Biomedical knowledge is uniquely complex and structured, requiring distinct reasoning strategies compared to other scientific disciplines like physics or chemistry. Biomedical scientists do not rely on a single approach to reasoning; instead, they use various strategies, including rule-based, prototype-based, and case-based reasoning. This diversity calls for flexible approaches that accommodate multiple reasoning strategies while leveraging in-domain knowledge.
We introduce \model, a knowledge graph (KG) based agent designed to address the complexity of knowledge-intensive medical queries. Upon receiving a query, \model generates relevant triplets by using the knowledge base of the LLM. These triplets are then verified against a grounded KG to filter out erroneous information and ensure that only accurate, relevant data contribute to the final answer. Unlike RAG-based models, this multi-step process ensures robustness in reasoning while adapting to different models of medical reasoning.
Evaluations on four gold-standard medical QA datasets show that \model improves accuracy by over 5.2\%, outperforming 15 models in handling complex medical questions. To test its capabilities, we curated three new medical QA datasets with varying levels of semantic complexity, where \model achieved a 10.4\% improvement in accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the integration of factual knowledge with free text information into LLMs. It introduces KGAREVION, a medical Question Answering (QA) agent, which additionally fine-tunes a LLM on a knowledge base completion task to improve its performance on evaluating medical facts. For an input question the agent can perform three actions:
 1. **Generate** relevant medical fact candidates 
 1. **Review** the generated fact candidates to check factual incorrect facts
 1. **Revise** to add more facts and change the factual incorrect candidate from Review
The outputs of the last action are used as part of a prompt to generate the final answer. The agent is compared on multiple choice and open ended questions against several baselines. It is able to reach state of the art performance.

### Strengths
**Medical Application**

The paper study the application of an LLM-based agent to a complex and difficult domain, viz. medicine. I appreciate that the authors took up this challenge to make a relevant contribution. 

**Evaluation**

The presented approach is evaluated thoroughly. It covers a comparison against a large number of competitors on open-ended and multi-choice reasoning. It shows that the presented approach is able to reach state of the art performance and moves the bar.  Apart from this performance analysis the paper also offers an ablation study and sensitivity analyses.

### Weaknesses
Complex approach:

The presented approach is complex and requires a lot of steps and technical components. It depends on a separate entity recognizer to map entities to UMLS, two LLMs performing different tasks (generation and revision, review), and a knowledge graph for fine-tuning. This reduces reusability, since the entire system would need to be replicated. Reducing all this into one LLM and dataset would make the contribution for accessible for others.

### Questions
Did you consider using the facts and relations from UMLS for the KB completion task?

### Soundness
4

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
4

### Summary
This article introduces KGARevion, an LLM which performs medical Q&A by verifying generated information (in the form of triplets) against the information in a knowledge graph (provided as knowledge graph embeddings). By doing so, it achieves competitive performance on several medical Q&A benchmarks. Additionally, the authors provide a new biomedical Q&A benchmark, which they call MedDDx. MedDDx leverages information from another Q&A dataset, but it is supplemented with several incorrect answers which are semantically similar to the correct answers.  KGARevion can be used with a variety of base LLMs and KGs, making it not only competitive but also versatile.

### Strengths
- **Figures:** the figures are nice for understanding the paper; in particular, figure 2 is great. 

- **Creative Benchmark:** the idea to create a benchmark with incorrect answers that are semantically similar to correct answers is very creative. In addition, separating questions into levels of difficulty is also quite clever. 

- **Reproducibility:** I commend the authors for providing code. Although I did not test it, it looks well documented and well written. 

- **Versatility:** the KGARevion approach seems versatile, able to be used with other base LLMs, KGs, and other domains in general.

### Weaknesses
Following the authors' rebuttal, I feel that my concerns below were sufficiently addressed. The authors have added an additional benchmark dataset from a sufficiently different data lineage, and they have also clarified several points of confusion. I have updated my score accordingly.

-------------------------------------------------------------------------------

I have a few concerns about the scientific robustness and the presentation of this work:

1. Firstly, my greatest concern regards the overlap between information in the knowledge graph(s) (KGs) used and the information used to create the benchmarks. Specifically, the authors designed their new QA benchmark, MedDDx, based upon the STaRK-Prime benchmark. **However, according to the corresponding STaRK-Prime paper (https://arxiv.org/abs/2404.13207), the biomedical QA from STaRK-Prime was built upon the PrimeKG, the exact KG which the authors used to fine-tune their approach, KGARevion.** Ultimately, this is not scientifically robust as the authors are providing their LLM with the same, structured data on which their benchmark was built. 

    I understand that the authors have also used other "gold-standard" benchmarks for comparison. However, there is also likely data leakage in some of these cases as well. For example, the PrimeKG is built from structured data derived from other sources, including the Disease Ontology (DO), the Gene Ontology (GO), UMLS, and DrugBank (Fig. 2, https://www.nature.com/articles/s41597-023-01960-3), all of which are also included in the creation of the BioASQ benchmark (https://pmc.ncbi.nlm.nih.gov/articles/PMC10042099/). Unfortunately, the other KG used within Section 4.4, ogb-bioKG, does not have any provenance information (https://github.com/snap-stanford/ogb/issues/111) but it was built by the same person (M. Zitnik) as PrimeKG, so it likely comes from similar sources. Ultimately, I would still avoid using obg-bioKG if the provenance can not be verified. 

    **I recommend that the authors research the data lineage of each of the benchmarks and KGs used. Perhaps they can present this as supplementary material. Then, I recommend that the authors only present the results in which there is no clear overlap between the structured data included within the KGs for fine-tuning and the benchmark datasets. The authors should omit all results where data leakage between the KGs and benchmarks is certain or likely.**



2. Secondly, I found this paper generally difficult to follow. Specifically, I believe the study could be more clearly motivated within the introduction, and Section 3 ("Approach") could be more clearly explained. Below, I list some specific points for improvement: 

- Paragraph 1 and the first half of paragraph 2 of the introduction seem loosely connected to the rest of the motivation; I suggest cutting these paragraphs and skipping more directly to the points in paragraph 3. 

- Figure 1 is problematic for several reasons. First, it is presented in the middle of the introduction, which is an inappropriate place to present results. Secondly, it is presented with no experimental context. Finally, it is not clear whether the figure even supports the claims being made in the introduction. I suggest moving or removing this figure. 

- RAG systems are presented as less desirable alternatives due to a reliance upon the quality of the documents provided, but the authors acknowledge that KGs may also have incorrect or incomplete information. Therefore, the motivation for the work seems unclear. 

- Section 3.2 on the Review section is extremely difficult to read. I believe this could be made clearer through more structure within the subsection (sub-headings or numbered steps). Perhaps the textual structure could correspond to flagposts or landmarks within Figure 2, so that the reader can refer back and forth between the text and Figure 2 easily. 

- Although fine-tuning with a KG is an integral part of the methodology, PrimeKG is not mentioned anywhere within Section 3. Until I read the Supplementary materials, I had understood that the KG being used for fine-tuning was the set of triplets derived from the "Generate" action. The authors should make it clearer that the KG comes from another, external source.

### Questions
1. page 3, Section 3: The authors give an example of a possible question and a set of possible answers. However, wouldn't this question warrant a yes/no response, rather than the set of answers provided? 

2. page 5: On which prediction task was TransE trained?  

3. page 5: Why have the authors chosen TransE for the KG embeddings? 

4. page 5: Where does the description dictionary D(r) come from? I do not see this in the appendix, and there is no appendix section 8. 

5. page 6, section 3.3: How, specifically, does the Revise action "adjust the triplets in F to include more knowledge"? 

6. page 8, Fig. 3: What do the blue v. orange plots mean? The only y-axis label I see is accuracy, and I see no key for blue v. orange.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel knowledge graph-based prompting technique for question answering in the medical domain. The approach consiststs of four steps: (1) Given a question in natural language, an LLM is used to generate subject-predicate-object triples from the question. (2) The triples are checked by means of a knowledge graph. Triples that are not clearly wrong are kept. (3) Then an LLM is asked to revise the triples. (4) Finally, the question is answered by means of an LLM and the revised triples.

### Strengths
- The paper tackles an important problem: question answering in the medical domain
- Original, novel question answering architecture: (1) generate triples, (2) review triples, (3) revise triples, (4) answer question
- Strong evaluation: multiple datasets, evaluation depending on question complexity, and ablation study
- Clarity: high-quality figures that help understanding

### Weaknesses
 - Section 3.2 "fine-tuning stage" I find this part rather hard to understand. Figure 2b definitely helps, but it might be good to clarify this part even further by providing an example.
- Section 4.4: It suprises me that the results barely depend on the knowledge graph. I am wondering whether the knowledge graph is required at all then. What do the results look like for a knowledge graph that is not specialized to medicine (e.g., Freebase15k-237)? If the results for Freebase15k-237 are almost the same as for PrimeKG, then the KG would be irrelevant.
- Related work on fact-checking seems to be missing.

Ciampaglia, Giovanni Luca, Prashant Shiralkar, Luis M. Rocha, Johan Bollen, Filippo Menczer, and Alessandro Flammini. "Computational fact checking from knowledge networks." PloS one 10, no. 6 (2015): e0128193.

Shi, Baoxu, and Tim Weninger. "Discriminative predicate path mining for fact checking in knowledge graphs." Knowledge-based systems 104 (2016): 123-133.

### Questions
- Can you give an example for the "fine-tuning stage" in Section 3.2?
- Section 3.2 "inference stage": How often does each case occur (triple removed vs triple kept) for the given dataset?
- Can you run your question answering approach with a knowledge graph that is mostly unrelated to the questions (e.g., Freebase15k-237)? Do the results get significantly worse or do they stay approximately the same?
- In how far does each component of the approach handle and support multi-hop paths in knowledge graphs? It seems, the generate and revise steps do not support paths. The review step might support paths indirectly via KG embeddings.
- How does the review phase of the approach compare to fact-checking approaches?
- The approach seems rather general. Wouldn't it also work on other domains besides medicine?

### Soundness
4

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
3

### Summary
This paper introduces KGAREVION, a novel approach that combines the non-codified knowledge of LLMs with the structured knowledge  in KGs to tackle the complexities of knowledge-intensive medical question answering. The method involves extracting relevant triples, using a fine-tuned LLM to verify the correctness of these triples, revising incorrect triples, and generating answers. This approach effectively addresses the challenges in the medical domain that require analogies and the integration of multi-source evidence, demonstrating improved performance across multiple datasets.

### Strengths
**Originality**: This paper proposes a new KG-based agent KGAREVION, which can handle complex and knowledge-intensive question answering tasks in the medical field. This work is original because it combines multi-source medical knowledge such as LLMs and KG, and the integration of revise into the processing flow is innovative, especially when dealing with complex problems that require precise domain knowledge.

**Quality**: The quality of the paper is reliable, with each step in the KGAREVION process clearly described and supported by appropriate methodologies. The authors also validate the model's effectiveness through experiments on multiple datasets, including new and challenging ones.

**Clarity**: The paper demonstrates a high level of clarity in presenting the KGAREVION model and its experimental results. The methodology section provides a clear description of the process, with well-organized main diagrams. Additionally, the tables and figures illustrating the experimental results are easy to understand.

**Significance**: This research holds significant importance in the field of medical question answering. It offers an effective tool that integrates data from multiple sources, such as LLMs and KGs, thereby enhancing the ability to accurately address complex medical questions.

### Weaknesses
In the description of the methodology, certain parts lack coherence and completeness. For instance, the revise and answer stages do not specify the exact processing methods used.

### Questions
**1.** What model is used for the revise process? A more detailed description should be provided. If an unfine-tuned LLM is used, does it have the capability to correct erroneous triples?

**2.** How are triples involving entities not included in the knowledge graph (Incomplete Knowledge) handled? Are they further processed or directly accepted as credible knowledge?

### Soundness
4

### Presentation
4

### Contribution
3

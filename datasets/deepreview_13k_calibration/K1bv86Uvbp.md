# LARGE LANGUAGE MODELS FOR BIOMEDICAL KNOWLEDGE GRAPH CONSTRUCTION

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 5, 1

## Abstract
The automatic construction of knowledge graphs (KGs) is an important research area in medicine, with far-reaching applications spanning drug discovery and clinical trial design. These applications hinge on the accurate identification of interactions among medical and biological entities. In this study, we propose an end-to-end machine learning solution based on large language models (LLMs) that utilize electronic medical record notes to construct KGs. The entities used in the KG construction process are diseases, factors, treatments, as well as manifestations that coexist with the patient while experiencing the disease. Given the critical need for high-quality performance in medical applications, we embark on a comprehensive assessment of 12 LLMs of various architectures, evaluating their performance and safety attributes. To gauge the quantitative   efficacy of our approach by assessing both precision and recall, we manually annotate a dataset provided by the Macula and Retina Institute.  We also assess the qualitative performance of LLMs, such as the ability to generate structured outputs or the tendency to hallucinate. The results illustrate that in contrast to encoder-only and encoder-decoder, decoder-only LLMs require further investigation. Additionally, we provide guided prompt design to utilize such LLMs. The application of the proposed methodology is demonstrated on age-related macular degeneration.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper provides an end-to-end approach  using LLMS for the construction of KGs from EMRs. it focuses on identifying notes in EMRs that are specific to certain diseases. To do this, they create template questions that look for specific types of information, such as treatments, contributing factors, and coexisting conditions. They experiment with different LLM structures - encoder-only, decoder-only, and encoder-decoder. They introduce guided instruction-based prompting to interact with LLMs.

### Strengths
Creating Knowledge Graphs automatically from Electronic Medical Record (EMR) notes is a significant challenge, and the approach introduced in the paper is original.

### Weaknesses
The paper's section on results looks at a very specific task  (age-related macula degeneration). Understanding how complex this dataset is compared to others would be really helpful. The paper also says that their method has precision 0.98 and recall of 1. But these scores are difficult to believe without comparing them to other standard results. The paper could be improved by giving more details about how this dataset stacks up against others, or by testing the method on different datasets that already exist. Right now, the paper isn't clear enough, and the reviewer has listed some questions that need clear answers to help understand the study better.

### Questions
(1) MIMIC-II is publicly available. But there are datasets like i2b2 which are carefully annotated by physicians and are subject to availability based on a license. Have you considered using this for evaluation?
(2) Can you explain why your method has recall 1 and precision 0.98 with FLAN-UL2?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
# Summary
LLMs for Biomedical KG Construction

## What is the problem?
Construction of biomedical knowledge graphs is challenging and involves a significant amount of expensive human expertise. This study examines whether or not they can be extracted automatically from clinical point-of-care notes.

## Why is it impactful?
Automatic construction of KGs would greatly accelerate the fields in biomedical science that rely on structured knowledge bases (of which there are many).

## Why is it technically challenging/interesting (e.g., why do naive approaches not work)?
Automatic KG construction relies on many techniques, including entity and relationship recognition, extraction, and normalization; parsing long documents in context; reasoning over clinical language; etc. All of these are rich areas of NLP that present longstanding research challenges.

## Why have existing approaches failed?
There are a host of existing approaches in the realm of automatic construction of KGs given LLMs. The authors reference almost none of these in their work, which reflects a major failing to contextualize their work in the context of related literature. These methods include the following:
  1. https://openreview.net/forum?id=ntIq8Wm79G-
  2. https://arxiv.org/pdf/2305.04676.pdf
  3. A number of papers from this list: https://github.com/zjukg/KG-LLM-Papers

## What is this paper's contribution?
  1. This paper releases a set of prompts that can help future researchers produce methods that automatically construct knowledge graphs given prompt-based LLM systems of various kinds.
  2. They also perform an evaluation of the efficacy of building KGs from text leveraging a variety of LLM architectures.

## How do these methods compare to prior works?
  1. There is insufficient comparison with prior works to say here. This is a major weakness of the work.

### Strengths
## Key Strengths (reasons I would advocate this paper be accepted)
  1. This is an important problem area.

## Minor Strengths (things I like, but wouldn't sway me on their own)
  2. Analyzing how differing pre-trained LLMs work in this setting is a useful analyses.
  3. The prompts released will likely be helpful.

### Weaknesses
## Key Weaknesses (reasons I would advocate this paper be rejected)
  1. You fail to sufficiently contextualize your advancement in the significant body of related literature in this space. There are a number of papers that complete or otherwise generate knowledge graphs via LLMs, and you don't reference or compare to these at all.
  2. You don't state that you plan to actually release the constructed knowledge graph. This seems a major limitation when such a graph would be a resource to the community, were it extracted in a meaningful way. While this may be because you are actually constructin per-patient KGs (and if so then this should be a minor weakness, not a key weakness) that is not sufficiently clearly stated in the text to alleviate this concern.
  3. If your KG is not patient specific, but is instead intended to capture general biomedical knowledge, it is not clear why using clinical point-of-care notes (as opposed to the clinical scientific literature) is the appropriate information source to use. Wouldn't scientific text be more accurate for capturing general information? If you are intending to capture per-patient information, why? For what will such information be used, and why should that be captured via unstructured clinical notes rather than structured information? These things need to be explained.
  4. Ultimately, the biggest weakness other than the lack of comparison to prior art is that this is likely just not well aligned with this venue. You do not have any significant methodological novelty here, and that is a key focus for ICLR. This is also not about representation learning, or really method development within ML at all, but is rather an (albeit important) application within NLP for health and biomedicine. Perhaps re-submitting to a venue more targeted to NLP contributions and applications (such as ACL, or possibly even better, EMNLP) would be more appropriate (though if the AC disagrees about the suitability I will of course retract this concern).

### Questions
## What would make me raise my score? (Things that you can do that would, pending their results and the manner in which you accomplish them, make me raise my score)
I don't foresee a situation in which my score will raise unless the AC states that this is suitable for the venue. Even then, I would need to see major revisions to improve clarity and, critically, to contextualize this work amidst the related literature and quantify how this work makes novel methodological contributions for me to consider raising my score. Ideally such comparisons would include baselines from prior published methods to show that this method of KG construction is superior.

## Other Questions (things I'd like to know, but may or may not make me change my score)
None

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose an end-to-end machine learning solution based on large language models (LLMs) that leverages electronic medical record notes to build KGs. To assess the performance and safety attributes of this approach, the study evaluates 12 LLMs with different architectures. The paper also introduces guided prompt design for such LLMs and demonstrates the methodology's application in age-related macular degeneration research.

### Strengths
1. The motivation is clear that the automatic construction of knowledge graphs (KGs) is an important research area in medicine, and LLMs could be helpful in this problem.

2. The experiments are conducted on 12 LLMs, which cover most of the available LLMs.

### Weaknesses
1. The paper's writing requires substantial improvement, as it contains numerous typos and format errors. Examples include:
- The citations used in the paper are in the wrong format.
- In sections 3.1 and 4.1, there is a non-existent reference to `"Section ?0.8".
- The section cross-references are not in a unified format. Some examples include "Section A", "Appendix Appendix D", "4.1", "Appendix subsubsection E.2.1".
- There is a "Table 4.2" in section 4.2. And "Table 5" in section 5 should actually refer to Table 2.
- The authors use past tense and present tense alternatively throughout the paper.
- There is a typo "Knowdledge" in the first paragraph of the introduction.
- In Algorithm 2, the symbol between "similarity_score" and "threshold" is not correctly shown.
- In section 4.6, the authors represent disease and the set of diseases as  $d$ and $D$. However, in section 4.1, they are referred as $c_{input}$ and $C$, respectively.
- In section 4.6, the authors "average over multiple occurrences of the relation of the type $t$ between $e$ and $d$." However, I believe the variable $e$ is never introduced in the paper.

2. It is unclear how the constructed knowledge graph is evaluated. The authors only mention that "the evaluation is done based on precision and recall", but the process of the evaluation is not addressed. What are the ground truth labels here?

3. In section 4.1, the authors mention using the BioBERT NER model to extract a list of diseases. However, an evaluation of its accuracy is missing. It's possible that the NER model could introduce some erroneous information or ignore any essential diseases.

4. In section 4.1, it is said that "If the similarity is above some threshold, we add the result to the result list." Here, the authors should explicitly mention the exact value of the threshold and discuss how it is determined.

5. In the right part of Figure 1, it is unclear which sentences are inputs and which sentences are LLM responses. For example, the paragraph "If the question is not related to the context, ..." is within the "###Response" block, but it seems to be an input instead.

6. For the prompt designs, it would be better for the authors to discuss the reasons why they have such designs and why these designs could help.

7. In section 4.6, it is inappropriate to say that "The numbers are chosen arbitrarily and they may be tuned for a dataset." The authors should study the effect of these hyperparameters and justify how they are chosen in the experiments to enhance reproducibility. Similarly, in section 4.7, the authors should also discuss why the threshold of the similarity score is set to 0.8.

### Questions
See the weaknesses above. One additional question:

1.  In section 4.3, the authors "explore two distinct approaches for aligning large language models to the task: open-book QA and in-context learning." According to the explanations in this section, "in the case of open-book QA, a query consists of a question and a context", however, it is also said that for in-context learning, "it extends the prompt to include both the question and the context." The two statements seem to be the same. Could the authors further explain the difference between the two approaches?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors focus on the research on biomedical knowledge graph (KG) automatic construction in their study, where they propose an end-to-end machine learning solution based on large language models (LLMs) that utilize electronic medical record notes to construct KGs. In their study, the entities are selected to diseases, factors, treatments, as well as manifestations. In terms of the LLMs, they embark on an assessment of 12 LLMs of various architectures. Based on their observations on these 12 LLMs, they conclude that in contrast to encoder-only and encoder-decoder, decoder-only LLMs require further investigation.

### Strengths
Authors carry out a good work on the automatic construction of biomedical knowledge graph by using Large Language Model. This research provides a new technique framework to researchers in knowledge graph.  Also, authors clearly demonstrate their instruction-based prompts that make most LLMs work.

### Weaknesses
Nevertheless, I have some concerns to this study.
1. Authors take a preprocessing operation for clinic notes. So, how to ensure its reasonableness. It would be better to demonstrate the different performance of LLMs on processed data and raw data, respectively.
2. This study is mainly related to an assessment work for different LLMs; however, authors only evaluate the precision and recall on three medical entities in Tab. 5 (I think it should be Tab.2) besides demonstrating some cases to prove their observations. It would be better to discuss different evaluations for different LLMs, such as reasons of hallucination, accuracy and evidence to extracted triplets, and so on.
3. In Tab.2, there have no explicit results to show the effectiveness of guide instruction-based prompting. It would be better to show the performance of “Vicuna-33B w/o guide, Llama-2-70B w/o guide and WizardLM-70B w/o guide”.
4. Why do not evaluate GPT-4? Could authors carry out an experiment based on GPT-4?
5. The presentations should be improved.
For example: 
(1) “Tab.5” in “Precision and Recall Results” should be “Tab.2”; 
(2) What does “Section ? 0.8” in “DATASET PREPROCESSING” refer to? 
(3) Why put the “hallucination” in Appendix? 
(4) What does the concepts of “Coexists with, Factor, Treatment” represent? “question types”, “medical entities”, or “relations”.
……

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study explores using large language models (LLMs) to automatically construct knowledge graphs (KGs) in medicine for applications such as drug discovery and clinical trial design. The research evaluates 12 different LLMs, considering their performance and safety attributes, using electronic medical record notes to identify medical entities like diseases, factors, treatments, and manifestations. Results indicate that decoder-only LLMs require further investigation, and the methodology is applied to age-related macular degeneration.

### Strengths
One notable advantage of this study is its thorough investigation into the utility of large language models (LLMs) for the automated creation of knowledge graphs within the medical domain. The research offers a robust assessment of 12 diverse LLMs, shedding light on their performance and safety characteristics. Furthermore, the study's emphasis on real-world medical applications, including drug discovery and clinical trial design, underscores its practical significance in advancing healthcare-related research and technological advancements.

### Weaknesses
The contribution of this study is confusing. The authors claims that they evaluate the performance of various LLM for better KG construction. However, the metrics is used to evaluate QA performance.

The relation between the prompts and KG construction is demonstrated to provide convincing evidence to support the contribution argument.

There is neither science illustration about how to design the prompt nor reference from previous study to show the prompt design process.

The study is conducted with little science rigor.

The experimental design is not completely illustrated.

KG construction process is not clearly articulate.

### Questions
Could you share more information about LLM-based KG given the public dataset?

How to evaluate the quality of KG construction?

Why use QA performance to demonstrate KG construction performance?

How did you construct your KG? Just by using the prompts?

Does prompts impact the model performance?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

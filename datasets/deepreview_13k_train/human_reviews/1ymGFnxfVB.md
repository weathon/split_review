# LJ-Bench: Ontology-based Benchmark for Crime

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Despite the remarkable capabilities of Large Language Models (LLMs), their potential to provide harmful information remains a significant concern due to the vast breadth of illegal queries they may encounter. In this work, we firstly introduce structured knowledge in the form of an ontology of crime-related concepts, grounded in the legal frameworks of Californian Law and Model Penal Code. This ontology serves as the foundation for the creation of a comprehensive benchmark, called LJ-Bench, the first extensive dataset designed to rigorously evaluate the robustness of LLMs against a wide range of illegal activities. LJ-Bench includes 76 distinct types of crime, organized into a taxonomy. By systematically assessing the performance of diverse attacks on our benchmark, we gain valuable insights into the vulnerabilities of LLMs across various crime categories, indicating that LLMs exhibit heightened susceptibility to attacks targeting societal harm rather than those directly impacting individuals. Our benchmark aims to facilitate the development of more robust and trustworthy LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors tackle the risk of Large Language Models (LLMs) providing harmful information by introducing LJ-Bench, a benchmark grounded in a legally structured ontology of 76 crime-related concepts. This dataset tests LLMs against a broad range of illegal queries, revealing that LLMs are particularly vulnerable to prompts associated with societal harm. By highlighting these vulnerabilities, LJ-Bench aims to support the development of more robust, trustworthy models.

### Strengths
- Benchmark development.
- Systematic evaluation: Assessment of LLMs across 76 distinct types of crime.
- Focus on societal harm: The article emphasizes an important aspect of model evaluation that can inform future research and development efforts aimed at enhancing model safety and trustworthiness.

### Weaknesses
 - Fragmented structure, especially the Related Work section.
- Some arbitrary choices, particularly regarding the selected prompts.
- Limited justification on focusing on the Gemini model.

### Questions
This article presents an interesting contribution to the evaluation of Large Language Models (LLMs) in the context of harmful information, particularly through the introduction of LJ-Bench, a benchmark designed around a structured ontology of crime-related concepts. The systematic assessment of LLMs against a variety of illegal activities offers valuable insights into their vulnerabilities, particularly regarding societal harm. This focus is particularly relevant in today’s landscape, where the safe deployment of LLMs is a pressing concern.

However, the article also has several notable shortcomings that warrant attention. Firstly, the structure of the paper feels fragmented, with sections detailing specific aspects of the research without a coherent flow, which may hinder readers' comprehension of the overall argument. Additionally, some of the choices made throughout the study, such as the selection of prompts, appear arbitrary and lack adequate justification, raising questions about the robustness of the methodology. Furthermore, the decision to focus solely on the Gemini model is not sufficiently motivated; a broader evaluation involving multiple models could provide a more comprehensive understanding of LLM vulnerabilities in relation to illegal queries.

Lastly, the article does not adequately address how the proposed ontology will be maintained over time, which is crucial for its practical application and relevance. Overall, while the work has the potential to be a valuable resource for researchers aiming to enhance the safety of LLMs, these unresolved issues suggest that further refinement and discussion are needed to strengthen the overall contribution.

Questions:
- Given the fragmented structure of the article, how do you envision improving the coherence of your arguments in future revisions to enhance reader comprehension?
- What specific criteria did you use to select the prompts for evaluation, and how might you address the potential concerns regarding the perceived arbitrariness of these choices?
- Could you elaborate on your rationale for focusing exclusively on the Gemini model for evaluation? Would you consider expanding this analysis to include other LLMs to provide a broader perspective on their vulnerabilities?

### Soundness
2

### Presentation
2

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
The paper proposes a legal crime jailbreaking benchmark based on California law. It also provides an ontology of crimes with 76 categories.

### Strengths
S1. Jailbreaking benchmarks for law are very important.

S2. The detailed ontology is good.

S3. The results are detailed and explained well. The appendix includes lots of real cases and prompts and other details.

### Weaknesses
W1. The scope of this paper is very restricted. LJ-Bench is based on California law. How applicable is it to other countries?

W2. What about harm "against trees and plants"? Is there no law in California against this?

W3. Is the ontology vetted by law experts and professionals?

W4. What is the point of augmented dataset of extended questions? Does it not fall in the same issues as in Fig 5, that is, of very similar text, and not really new content?

W5. How effective the jailbreaking answers are should be evaluated by humans. Another LLM, that too of the same kind, may be biased in evaluation. Hence, a human evaluation is needed.

W6. Is Table S3 not the full list? The caption says something different, though. Or does it need to be combined with Table S4 to get the full mapping of 76 categories and number of questions corresponding to each in the benchmark?

W7. How applicable is this method to non-English prompts?

W8. Typo: Contribution points 2 and 3 are repeated

W9. Typo: Sec E.1 title

### Questions
W1-W7

### Soundness
2

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
The widespread usage and ease of access of LLMs to information make it imperative that we
study their robustness against potential harm they might cause to society. The authors
introduce a new benchmark called LJ-Bench, inspired by legal frameworks, and
provide the first detailed taxonomy on the types of questions whose responses would elicit harmful
information. It contains crime-related concepts, supporting 76 classes of illegal
activities. The authors then conduct an experimental analysis of attacks on LJ-Bench, 
based on the new types of crime as well as the hierarchical categories.

### Strengths
--The use case and motivation behind the paper is reasonably strong, as evaluating the robustness of LLMs against a broad enough range of illegal activities is clearly important. 
--There is sufficient description of related work; in fact, I believe this may be the strongest part of the paper. 
--There is reasonable clarity in the way the paper is written, although I do believe it could use some more quality improvement and proofreading, as I state below.

### Weaknesses
--The experimental results are not up to the mark in this paper. First, they are not as extensive as they need to be, but more generally, they lack the type of scientific grounding (e.g., statistical significance results) that would be necessary in a paper purporting to be centered on responsible use of AI. 
--There are some presentation issues. First, the figures are not of sufficiently high quality. Second, the paper clearly lacks adequate proofreading e.g., on page 2, a bullet point is repeated, on page 8 the word 'original' is misspelt and so on.

### Questions
I am still not sure how the introduction of this benchmark helps us make more responsible use of LLMs. For people studying crime and legal issues, it seems that disabling the LLM from relying on this benchmark to answer questions (which I presume would be the obvious use case) would be overly broad. On the other hand, I'm not seeing sufficient evidence that, even if that were the goal, the benchmark could prevent it. For example, if I were to change the prompts and questions in slight ways, would the language model still not answer? I am not sure that there is a general and foolproof solution to the jailbreaking problem. More experiments and robustness studies would have helped express this more convincingly. Nevertheless, the authors should feel free to comment on this concern.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce LJBench, a benchmark of questions about crime-related concepts - designed to assess LLM safety in responding to such questions. The primary outputs of this paper are:
 - An OWL ontology, that re-uses some concepts from schema.org, for describing legal concepts from Californian Law and the Model Penal Code, describing 76 distinct types of crime
 - LJ-Bench: A dataset of 630 questions asking how to perform acts considered illegal under Californian Law or the Model Penal Code - with a fair distribution of questions across the 76 types of crime.
 - Structured OWL descriptions of each question from the LJ-Bench dataset, describing the type of crime each question relates to and whom the crime applies to.
 - Experiments to assess the outputs of Gemini 1.0 on these questions.

### Strengths
- The authors use their formal mappings to legal structures to ensure that the questions contained in their benchmark fairly represent all relevant types of crime described under Californian Law and the Model Penal Code.
 - The authors use their formal mappings to legal structures to ensure that the questions contained in their benchmark fairly represent all relevant types of crime described under Californian Law and the Model Penal Code. We see this as a food technique to ensure fair distribution of question types in a benchmark,
 - The authors present both the benchmark, and an experimental evaluation of how a model (gemini 1.0) performs against that benchmark.

### Weaknesses
 **Comments on the ontology**

Whilst the choice of formally representing legal concepts in an ontology is a sensible approach, we have some concerns around the methodology used to create the ontology. In particular:
 - There is extensive literature on legal ontologies which the authors do not reference, we encourage the authors to review the following papers:
	 - "A systematic mapping study on combining conceptual modelling with semantic web"
	 - "Legal ontologies over time: A systematic mapping study"
    after reviewing these papers we suggest that the authors identify:
	 - Whether there are existing ontologies capturing concepts from Californian law that should be re-used, and
	 - Whether there are more suitable ontologies beyond schema.org that they should use as the foundation for the ontology for lj-bench
 - There is no rigorous methodology described for:
    - How the authors identified the 76 distinct types for crime from Californian Law and the Model Penal Code, nor why they have chosen the 4 broader categories to class these into.
    - How the four super categories of "against a person, against property, against society, and against an animal" were identified and selected.

We have also observed the artefacts that the authors have submitted, and have the following comments on the ontology design:
 - In the supplementary materials, only a fraction of the 630 questions from lj_bench are described in lj-ontology.rdf
 - There appear to be modelling errors in the disjoint class declarations. For instance "rape" is disjoint from "sex offence", when it likely should be classified as a subset.
 - nitpick: owl:ObjectPropertys defined in the schema are missing rdfs labels and comments (e.g. crime:steals)
 - nitpick: Classes defined in the schema are missing labels
 - nitpick: It is poor practice to have URIs with commas (,) question marks (?) or the (&) symbol
 - nitpick: Literals in comments inappropriately contain formatting, e.g. "mis-\nappropriates" should be "misappropriates"
 - Information should not be implicitly encoded in the names of URIs; with crimes like "crime:unlawful_interference_with_property". Instead of having

```
crime:unlawful_interference_with_property a crime:Unlawful_Interference_With_Property, owl:NamedIndividual .
```

have
```
crime:propertyInterference a crime:PropertyInterference, owl:NamedIndividual ;
	rdfs:label "Unlawful Interference With Property"
```
I would also consider adding an rdfs:comment. 

Please also review these suggestions https://chatgpt.com/share/6713d39d-1388-800c-a886-4e9ee3994efa, in particular on:
 - Naming conventions
 - Incomplete property definitions
 - Overlapping disjoint classes

**Other Nitpicks**
 - We suggest the authors do note place "few" in brackets in the first figure
 - We request the authors include a turtle (ttl) serialisation of their ontology artefacts for human readability
- Lots of quotes opened incorrectly, e.g. see list in attack section
 - Please reference schema.org better in the bibliography

### Questions
- Is there a reason why this benchmark was not run on OpenAi and Anthropic Models?
- Do you have a sense of how extensible this work is to other legal frameworks?
 - In "For example, the nature of the answer would differ significantly when seeking classified information from the CIA (Central Intelligence Agency) compared to obtaining similar information from a local police station." how would you expect the answer to differ, could you have short examples?

### Soundness
3

### Presentation
3

### Contribution
3

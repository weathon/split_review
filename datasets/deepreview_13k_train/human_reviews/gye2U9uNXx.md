# Uncovering Gaps in How Humans and LLMs Interpret Subjective Language

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Humans often rely on subjective natural language to direct language models (LLMs); for example, users might instruct the LLM to write an *enthusiastic* blogpost, while developers might train models to be *helpful* and *harmless* using LLM-based edits. The LLM's *operational semantics* of such subjective phrases---how it adjusts its behavior when each phrase is included in the prompt---thus dictates how aligned it is with human intent. In this work, we uncover instances of *misalignment* between LLMs' actual operational semantics and what humans expect. Our method, TED (thesaurus error detector), first constructs a thesaurus that captures whether two phrases have similar operational semantics according to the LLM. It then elicits failures by unearthing disagreements between this thesaurus and a reference semantic thesaurus. TED routinely produces surprising instances of misalignment; for example, Mistral 7B Instruct produces more *harassing* outputs when it edits text to be *witty*, and Llama 3 8B Instruct produces *dishonest* articles when instructed to make the articles *enthusiastic*. Our results demonstrate that we can uncover unexpected LLM behavior by characterizing relationships between abstract concepts, rather than supervising individual outputs directly.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper identifies misalignment between human intent and LLM behavior adjustments (operational semantics) when prompted with subjective language.

They introduce a method called thesaurus error detector (TED). The method first involves constructing a similarity matrix comparing LLMs’ operational semantics for different subjective phrases (approximated by embedding gradients), and then elicits failures by identifying how this thesaurus disagrees with with a reference thesaurus (created based on either human or stronger LLM annotations).

The authors’ experiments show that TED consistently outperforms a semantic-only baseline for two models (Mistral 7B and Llama 3 8B) in identifying two kinds of errors (unexpected side effects and inadequate updates) for two kinds of tasks (output editing and inference steering).

The authors also present some qualitative examples throughout the paper, such as Mistral 7B producing more “harassing” outputs when instructed to make articles “witty”.

### Strengths
- The paper is well-written and experimental design choices are remarkably well-documented, which facilitates reproducibility experiments and future work to easily extend this work to different settings.
    
- The thesaurus based method is interesting and creative
    
- I find the author’s broader contribution of “characterizing LLM behavior via relationships between abstract concepts rather than individual outputs directly” to be very compelling

### Weaknesses
 - Given that this work is ultimately about *meaning* and the word *semantics* is used throughout the paper, there is surprisingly no connection to any relevant concepts or prior literature in subjectivity, semantics, or pragmatics. This hinders the work’s conceptual clarity and contribution.
    
- The authors rely on GPT-4 in many parts of the pipeline: identifying subjective phrases, constructing the reference thesaurus, and acting as a judge. These decisions are well-motivated but some human validation is needed at each stage, perhaps on just a small sub-sample. Especially because this work focuses on biases and limitations of LLMs, it’s hard for me to switch to fully trusting GPT-4’s outputs.
    
- For the human evaluation, there should be some sort of inter-annotator agreement recorded (again, maybe on a small subset). Because we’re dealing with subjectivity, humans’ interpretations of each phrases and the relationship between phrases would likely vary widely. 
    
- One area that remains unclear to me is in the motivation for testing TED on LLM responses to this particular kind of ethical question. The examples in the prompt all start with “why is it okay”, which implies that “it is okay” which may bias both LLM outputs and the constructed thesaurus.

- More specifically, I'm not convinced based on the provided examples that unexpected side effects necessarily indicate model failures, as suggested by the language throughout the paper. I can't easily imagine what it would mean for subjective phrases to affect LLM outputs along just that one dimension (enthusiastic, witty, etc.) _without_ affecting other dimensions?

### Questions
- How do you define subjectivity? 

- And given that subjectivity leads to different human interpretations, what do we want from LLMs?

- More specifically, I'm not convinced based on the provided examples that unexpected side effects necessarily indicate model failures, as suggested by the language throughout the paper. I can't easily imagine what it would mean for subjective phrases to affect LLM outputs along just that one dimension (enthusiastic, witty, etc.) _without_ affecting other dimensions? 
    
- Why don’t you use an actual thesaurus or similar lexical resources such as WordNet or ConceptNet as the reference?
    
- Relatedly, why not use existing subjectivity lexicons rather than rely on GPT-4 to generate the set of phrases for this work? While there is manual curation mentioned in the appendix, there may be recall biases in kinds of subjective phrases that GPT-4 simply doesn’t surface.
    
- I’d recommend connecting this work to ideas in semantics and pragmatics that focus on the relationships between statements: entailment/natural language inference, presuppositions, and implicature. I think this could help ground the method, annotation, and evaluation.

- How should I think about the selection of the embedding to calculate the gradient with respect to? Why do you expect any other token or internal activation to yield similar results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel approach, TED (Thesaurus Error Detector), to detect misalignment between language models' interpretation of subjective prompts and human expectations. Using TED, the authors develop an operational thesaurus for subjective phrases, comparing it with human-constructed semantic thesauruses to identify discrepancies. TED aims to uncover unexpected behavior in LLMs by examining how models handle subjective instructions, such as "enthusiastic".

### Strengths
1. Novel Methodology: TED presents an interesting approach to detect model misalignments with human expectations, filling a critical gap in aligning LLM behavior with human intent.

2. Significance: Subjective language interpretation is an important yet challenging task nowadays.

### Weaknesses
1. Lack of Practical Recommendations: While TED detects misalignments effectively, the paper could provide more actionable guidelines or solutions to mitigate these issues in real-world applications. The paper identifies misalignments but does not delve into how these findings can be translated into concrete improvements in LLM behavior. For example, it is unclear how the identified discrepancies between the model's thesaurus and human-constructed thesauruses can be used to refine model training or prompt engineering strategies.

2. Ambiguity in Evaluation Metrics: The evaluation metrics for TED’s effectiveness could be clarified, as the success rates reported could benefit from further contextualization to understand their practical implications. Also, it would be better to clarify how exactly the success rate is calculated. The paper reports success rates, but it does not provide a clear explanation of what constitutes a 'success' in the context of detecting misalignments. The practical implications of these success rates are not well-defined, making it difficult to assess the real-world impact of the proposed method. For example, a success rate of 0.7 could mean different things depending on the specific type of misalignment being detected, and this nuance is not adequately addressed.

3. Need more justification of the results: Through empirical tests, TED reportedly achieves higher success rates in detecting inadequate updates than a semantic-only baseline, while both approaches yield fewer failures overall. However, the implications of these results need clearer justification and relevance to real-world LLM applications. For instance, the statement "TED additionally finds inadequate updates with higher success rates than the semantic-only baseline, but both TED and the baseline find fewer failures overall" is an interesting finding, but it’s unclear what this means in practical terms. The paper does not provide a detailed analysis of why inadequate updates are less frequent or how this finding should influence the development of more robust LLMs. The practical significance of this observation is not adequately explained, leaving the reader to wonder about its real-world implications.

### Questions
In line 283, "For example, the LLM might language model to write a “witty” essay or an “accessible” blogpost about machine learning." 

What does "the LLM might language model" mean?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This study introduces a novel method to identify misalignments in how LLMs interpret subjective prompts compared to human expectations. TED constructs an operational thesaurus based on the LLM’s interpretations of phrases like “enthusiastic” or “witty” and compares it to a human-created semantic thesaurus. Misalignments are flagged as “unexpected side effects” or “inadequate updates,” depending on whether the model's output behavior deviates from or fails to meet human expectations.

The authors evaluated TED on two tasks—output editing and inference steering—demonstrating its effectiveness in uncovering surprising behaviors. For instance, TED detected that prompting models for “enthusiastic” outputs sometimes resulted in “dishonest” outputs. This method highlights TED’s value in addressing alignment challenges in subjective language, proposing it as a scalable tool to enhance the reliability of LLMs in aligning with human intent.

### Strengths
Originality:
* The paper introduces TED, a unique approach to identifying LLM misinterpretations in subjective language by constructing and comparing operational and semantic thesauruses. This structured focus on “unexpected side effects” and “inadequate updates” adds a fresh, nuanced perspective to alignment research, addressing a critical yet underexplored aspect of model behavior.
Quality:
* TED’s methodology is rigorous, with careful construction of thesauruses using embedding and gradient-based techniques. Quantitative results demonstrate TED’s effectiveness over baseline methods, and the authors provide a balanced view by discussing limitations, lending credibility and depth to their findings.

Clarity:
* The paper is well-organized and accessible, effectively explaining complex methods and illustrating key points with clear examples (e.g., “enthusiastic” prompting unintended “dishonest” outputs). The writing maintains a technical depth while remaining readable, supporting a broad audience’s understanding.

Significance:
* The work addresses a crucial challenge: aligning LLM interpretations with human expectations in subjective contexts. TED’s contributions extend alignment research to emotional and tonal aspects, impacting user-centered LLM applications and offering a scalable approach for early misalignment detection in model development.

### Weaknesses
Context-Sensitivity in Embedding Representation:
* The paper mentions embedding each phrase independently of context, which may overlook nuances in interpretation that depend on the type of task (e.g., writing a "witty blog" versus a "witty proposal"). Incorporating context-dependent embeddings could enhance TED’s robustness by tailoring thesaurus creation based on usage scenarios. This could be achieved by developing context-specific operational thesauruses or dynamically updating embeddings based on task context, potentially using attention-based methods to focus on relevant contextual tokens.

Impact of GPT-4 Judgments on Validation:
* The paper relies on GPT-4 for validating downstream failures, but this could introduce bias since GPT-4 is itself an LLM with its own alignment characteristics. Exploring alternative or supplementary validation approaches, such as using human expert reviews or a consensus-based scoring system from multiple models, could mitigate this potential bias. Additionally, assessing whether GPT-4's validation aligns with human judgments on subtle or ambiguous failures would reinforce the robustness of the evaluation.

### Questions
Q1: How does TED handle potential context-specific interpretations of subjective phrases (e.g., “witty” in different tasks like blogs vs. proposals)?

Q2: Given the reliance on GPT-4 to validate TED’s flagged misalignments, how do you address potential alignment biases that GPT-4 might introduce?

Q3: Did you observe specific hierarchies or dependencies between phrases (e.g., “intelligent” often implying “engaging”)? If so, how did TED handle these dependencies?

Q4: Beyond identifying misalignments, have you considered how TED’s findings might guide improvements in LLM training or alignment processes?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduced a thesaurus containing pairs of subjective phrases that have dissimilar or similar operational semantics in LLMs. They compare this thesaurus with a human-annotated thesaurus to detect failures in LLMs' understanding (the process of TED). Experimental results under two text generation scenarios show that TED has a high success rate in finding the failure of LLMs' generation.

### Strengths
The high-level motivation—finding the gaps between LLMs and humans' understanding, is very important and intriguing. The authors contribute in this direction by uncovering certain phrase pairs where LLMs have an incorrect understanding, causing their generated text to contain unwanted or undesirable properties.

### Weaknesses
I think the prominent problem is the writing, which fails to convey the authors' idea clearly. I've read the paper word by word multiple times, but untechnical issues making the paper logically unsmooth and difficult to understand, such as missing clear description of key parts. For example, in Sec 3.2, the process to obtain the operational semantics is missing, instead, it is vaguely described in Sec.4.2. This problem also happens to how the authors construct the semantic thesaurus. Figure 1 is also difficult to understand (see questions).

Another problem is the lack of proof regarding the effectiveness and reliability of their method for obtaining the LLMs' operational semantics $\Delta_w$. The authors also mentioned that they adopted an arbitrary operation.

I also question the usefulness of the proposed LLM operational thesaurus and TED. The phenomenon of LLMs generating unwanted text properties is not new and is often practically addressed by prompting LLMs again to re-generate text while avoiding unwanted properties (a process akin to CoT). This makes the mere presentation of misalignment cases not very useful. The authors also did not discuss how TED can potentially benefit LLMs research and applications in this paper (correct me if I missed). To enhance its practicality, I believe it is good to conduct research and experiment to showcase how to improve LLMs' generation using the proposed TED. However, this paper does not include this part, which diminishes its significance.

### Questions
1. What's the definition of *subjective language/phrases*? Can all adjectives be considered as subjective phrases? The authors should clarify this definition at the beginning.
2. In Figure 1, why using orthogonal symbol $\perp$ to denote two antiparallel vectors? Overall, Figure 1 does not present the process of TED clearly. At first glance, Step 1 appears to imply that the thesauruses of LLMs are generated from the text below; in Step 2, it's hard to understand how the judgment of "unexpected side-effect" and "inadquate update" is made. The authors should expand Figrue 1, add more descriptive text on it, and relate to the corresponding sections. Also, the authors is recommended to highlight that Step 2 produces a set of pairs that LLMs misunderstand, which is then evaluated in Step 3.
3. Figure 2 seems not very necessary, as the effect of operational thesaurus vectors is well described in Sec. 3.2. It is better to use the space of Figure 2 to expand Figure 1.
4. In line 147, "A thesaurus describes whether or not phrases are **similar**", similar in what aspect? Please provide more specificity.
5. In Sec. 3.2, it is important to include the process of obtaining $\Delta_w$ here. Regarding to this process which described in line 301-306, which layer's embeddings are used to calculate the gradients? How are the gradients calculated, and why do the gradients can represent operational semantics? The authors should elaborate on this and give theoretical support. Also, have the authors considered the gradients of another tokens? I feel only using the first token can be very biased.
6. In line 207, "we average over gradients from n generic prompts", I am interested in the consistency of the operational semantic vectors of the same word $w$. Could you present the inner-consistency of the vectors (e.g. distribution of their cosine similarity) of the same word $w$ under $n$ different prompts? If the distribution is very divergent, I would highly doubt the effectiveness of the calculated operational semantics.
7. In the following paragraph Building the semantic thesaurus, first, the description of the construction is difficult to understand and the authors are recommended to give examples on it. In line 217, "more aligned" than what? Do you mean if $o_{w_1}$ is expeted to more aligned with $w_2$ than $o_{w_2}$? Besides, I think obtaining human-generated semantic thesaurus may not be that complicated. I expected simply asking humans to indicate weather two phrases have accordant effects (e.g. 'informative' and 'long') or discordant effects (e.g. 'informative' and 'concise'). The authors are recommended to give explaination on why they designed this construction in this manner.
8. In line 232-233, "and less aligned for inadequate updates", I question whether this is a robust metric. For instance, when prompting LLMs to generate longer text such as expanding a research report, we often want them to be just more verbose rather than to add more information (because the imagined information from LLMs can be inaccurate). In this case, when measuring the pair ('informative', 'longer'), it will be identified as 'inadequate update' by the metric, but actuallty but it does not sound inadequate at all. How do you think of this case?
9. In line 274, how exactly do you prompt the LLM? I could not find this information. In line 279, what does "reference subjective phrases" mean? Regarding Inference steering, how exactly do you achieve this?

### Soundness
3

### Presentation
2

### Contribution
3

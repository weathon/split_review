# GUARD: Guideline Upholding Test through Adaptive Role-play and Jailbreak Diagnostics for LLMs

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 3, 6, 8

## Abstract
As Large Language Models (LLMs) become increasingly integral to various domains, their potential to generate harmful responses has prompted significant societal and regulatory concerns. In response, governments, including the European Union, have issued ethics guidelines to promote the development of trustworthy AI. However, these guidelines are typically high-level demands for model developers and testers. 
There remains a gap in translating these broad requirements into actionable testing questions to verify LLM compliance.

To address this challenge, we introduce GUARD (\textbf{G}uideline \textbf{U}pholding Test through \textbf{A}daptive \textbf{R}ole-play and Jailbreak \textbf{D}iagnostics), a testing method designed to operationalize guidelines into specific guideline-violating questions that assess LLM adherence. To implement this, GUARD assigns LLMs to play different roles, enabling the collaborative and automated generation of guideline-violating questions based on government-issued guidelines, thereby testing whether responses comply with these guidelines. When responses directly violate guidelines, GUARD reports inconsistencies. Furthermore, for responses that do not directly violate guidelines, GUARD integrates the concept of ``jailbreaks'' to diagnostics, named GUARD-JD, which creates scenarios that provoke unethical or guideline-violating responses, effectively identifying potential scenarios that could bypass built-in safety mechanisms. Our method finally culminates in a comprehensive compliance report, delineating the extent of adherence and highlighting any violations.

We have empirically validated the effectiveness of GUARD on seven LLMs, including Vicuna-13B, LongChat-7B, Llama2-7B, Llama-3-8B, GPT-3.5, GPT-4, and Claude-3.5, by testing compliance under three government-issued guidelines and conducting jailbreak diagnostics. Additionally, GUARD-JD can transfer jailbreak diagnostics to vision-language models (MiniGPT-v2 and Gemini Vision Pro), demonstrating its versatility and providing valuable insights for the development of safer, more reliable LLM-based applications across diverse modalities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to bridge the gap between government-mandated ethics guidelines for LLMs and concrete scenarios to test adherence to these guidelines. GUARD is a roleplay-based approach that aims to operationalize guidelines into sets of questions that can test LLM adherence. Few-shot LLM-based approaches are used to generate these guideline-violating questions via a multi-step pipeline, that includes an Analyst role for distilling guidelines into concrete features, a Strategic Committee for generating relevant scenarios, a Question Designer responsible for generating harmful questions, and a Question Reviewer that assesses the generated questions for harmfulness, information density and compliance. A Question Designer is also included to amend unsatisfactory questions. The paper also provides a compliance report assessing several modern LLMs using their methods. GUARD also shows limited utility in the context of large VLMs.

### Strengths
1. I found the research problem explored in this paper to be very relevant. A robust method to turn high-level guidelines into specific scenarios to test models against those guidelines would be impactful, considering the increasing interest in AI regulation.
2. The proposed method has utility for both LLMs and large VLMs.
3. The jailbreaking approach proposed has some novelty, creating a knowledge graph from existing successful jailbreak attacks and sampling paths from it to create new jailbreaks.
4. The method is shown to be quite effective at jailbreaking LLMs, when compared to other jailbreak methods in literature. The resulting jailbreaks are also more "natural" or human-interpretable, as demonstrated by their low perplexities.
5. The experiments sections are well-written, providing sufficient implementation details and analysis of results.

### Weaknesses
1. Why is semantic similarity between the output and the rejection response used as the measure of jailbreak performance in the evaluator? To the best of my knowledge, the standard approach is to do automatic or manual evaluation of the harmful content in the LLM response. Sometimes, an LLM can provide harmless outputs that do not count as a rejection, but do not demonstrate harmful behavior either. I would suggest a human annotator study to validate the evaluation approach, or citations to work that contains such a study.
2. Why is a language model used to output the semantic similarity? The resulting number will be different every time the evaluator is run. Is the reported number an average over multiple calls to the evaluator? If semantic similarity is the desired evaluation approach, why is a cosine similarity between response embeddings not used?
3. How is diversity ensured in the generated jailbreak attacks. There does not seem to be any component of the pipeline that encourages a diverse set of attacks. Some qualitative analysis of the generated jailbreaks would be helpful.
4. The equations in Section 3.3 seem to be redundant, as all of these quantities are ultimately output from a language model based on textual descriptions. As a result, there is no guarantee that the output adheres to the provided equations.
5. String-matching seems like a weak measure for guideline adherence in Section 3.4, for the same reasons as point 1 above. Some human preference alignment study is required here as well.
6. Based on examples provided in the appendix, the recovered fragments from the knowledge graph and the initial scenario generated based on that is very different from the final scenario used as the jailbreak. Most of the signal here seems to come from the modification rules section. This raises further concerns about attack diversity.
7. The perplexity-based reasoning for fluency seems somewhat weak, as the perplexity differences are relatively small when compared to other baselines. Some qualitative analysis would be helpful here as well.

### Questions
1. Is the performance for the other baselines reported in the paper also obtained using the author's evaluation approach? In the absence of validation for the evaluator, these numbers do not seem very dependable. Are the authors able to replicate originally-published numbers for these baselines?
2. The compliance report is restricted to 5 LLMs, a broader scope of evaluation would also help the paper.
3. I would also suggest putting longer descriptions of the methodology in the main section of the paper, most of the important details are in the appendix.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a testing pipeline called GUARD that accesses LLM’s adherence/violations to government-issued ethics guidelines. The testing is done by generating guideline-violating questions through two stages. The first stage is to generate questions directly, and the second stage is to generate jailbreaking questions – certain jailbreaking prompts can force LLM to break its built-in safety mechanisms.  

The first stage is to incorporate LLMs to serve four functionalities: Analyst, Strategic Committees, Question Designer, and Question Reviewer. While the Reviewer accesses the quality of each question using three numerical metrics, the calcuations are not done explicitly but determined by prompting the Reviewer LLM. 
The second stage (jailbreak diagnosis) again, uses LLMs to serve three roles: Generator, Evaluator, and Optimizer. The Generator generates jailbreaking scienarios grouded by Knowledge Graphs built from benchmark jailbreaking prompts. The goal is to create scenarios that can make the LLM under-test output guideline violating questions. 

The key method for both stages involves using multiple LLMs and incorporating self-feedback in the prompts to improve the chance of generating guideline violating questions. There is no evaluation on the direct generation of violating questions (1st stage) itself. The effectiveness of jailbrek diagnostics (2nd stage) is compared with other methods. However, the effectiveness is mainly due to the use of LLMs and self-feedback, not the soundness of the proposed method.

### Strengths
This paper introduces GUARD, a solution to a critical issue in real-world scenarios: assessing the adherence of powerful LLMs to ethical guidelines.

### Weaknesses
The proposed method is an ad hoc integration of multiple LLMs without a scientific reasoning of how roles are assigned and how prompts are designed. While all the decisions in the pipeline are made by LLMs, there is no discussion on how LLMs’ response quality (e.g., due to hallucination issues) might affect GUARD’s performance.

The major concern is the evaluation of the proposed method. Table 1 merely shows the test results on different LLMs but does not show the effectiveness of the proposed method. The effectiveness demonstrated in Table 3 is largely attributed to the LLM’s iterative generation combined with self-feedback. This suggests that if we could utilize LLMs without regard to computational costs, we would likely achieve better results —a conclusion that seems obvious. The paper fails to provide any insights on how to use LLMs efficiently.

The paper lacks justification on some of its design and evaluation choices. See questions.

### Questions
Section 4.1 Guidelines: the guidelines are pre-prossed into general categories. Is this pre-process done manually and is it a bottleneck for adopting the proposed method to new guidelines? 

How to evaluate if GUARD’s generated questions can cover all the principles from a guideline?

Is the same LLM used for all the roles in Figure 2? And is it the same LLM that is under tested? Can you elaborate the design choice here?

Section 3.4.1 Knowledge Graphs: what is the added value of creating KGs and using them to scale up from the jailbreaking benchmarks? How does this compare to simply prompting LLM to generate new scenarios based the benchmarks? 

Line 324: “For questions that result in guideline-violating answers,” should this be guideline-adhering answers? How many questions do not result in guideline-violating answers in the first stage and require further jailbreaking? 

The perplexity score has little information because the method directly uses LLM for generating jailbreaks.  This score merely evaluates the LLM’s generating fluency.

Line 343: Are there any cases with similarity score higher than 0.3, but still resulting successful jailbreaks? 

Table 3: Are the jailbreaks used in the baseline methods all manually crafted?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a method for testing LLMs for ethics guidelines. Their method is split into several parts to a) create guide-line breaking questions using a series of LLMs to parse the guidelines and then generate the questions, b) additionally test against jailbreaks via an optimization process based on a set of pre-collected jailbreak questions, and c) evaluate the performance of an LLM against this set of generated test questions + jailbreak prompts. They report guideline violation rates against 3 sets of guidelines and 5 different LLMs. Additionally, they report jailbreak rates for their method against 5 other methods.

### Strengths
The authors address the important question of how to translate AI ethics guidelines to a quantitative measure for a specific LLM. Their method considers several facets of this problem (generation, jailbreaking, and testing) and they present results for a variety of different models and several existent guidelines. Their paper is well motivated and concise.

### Weaknesses
The authors address the important question of how to translate AI ethics guidelines to a quantitative measure for a specific LLM. Their method considers several facets of this problem (generation, jailbreaking, and testing) and they present results for a variety of different models and several existent guidelines. Their paper is well motivated and concise.

The authors take on multiple facets of a challenging problem. Several key components of the analysis appear to be missing (potentially addressed via my question section) making it challenging to follow the full arc of the analysis to the final results presented. Additional discussion of LLM vs human/expert generated questions would help motivate the analysis further. Lastly, the testing component of the methodology is only briefly discussed (lines 244-246) but critical to understand the final results. It appears the authors use a string matching approach without apparent validation or reference that could support this methodology. In appendix J.2 the 3-shot examples even contain evidence of the optimization prompting to avoid this string and an LLM could be easily trained to avoid it. Lastly, the paper would benefit from some discussion of the cost associated with the method when all the surrounding prompts and optimization loops are evaluated. This appears to be not insignificant and is relevant for understanding how well this method might scale. 

A final point to discuss (see question 5) is whether the method can differentiate between guidelines on restrictions for content generated by the LLM (similarly questions that the LLM will answer) and guidelines regarding how the LLM is constructed. For examples, in the “Trustworth AI Assessment List”, the guideline relates to how entity associated with the LLM tests it and not necessarily how the LLM behaves surrounding these questions. The questions generated by the method are not able to capture the validation process for the model and, in my opinion, would be better filtered and flagged as not covered by this model.  Similarly, the generated guideline-violoating answers for the second topic in Table 2 don’t try to violate the guideline directly (e.g., build me a deepfake), rather they ask how one might violate it. It is a subtle difference but an important distinction between content and knowledge generation (see my question 6).

### Questions
1.	The embedded link to the experiment results and updated jailbreaks is not valid. The closest link (https://anonymous.4open.science/r/38E2/) is difficult to follow to see if it does contain this information. Is this link correct and, if so, could you provide a brief description of the .xlsx files and verify that the repository contains this information?
2.	Will you provide the code associated with the methodology or reason for not doing so? This seems critical to the reproducibility (as well as understanding of) the method.
3.	Where do the weights in the harmfulness metric come from (lines 218-220)?
4.	Do you have validation or references supporting the string-matching approach for  your evaluative step (line 243-246)?
5.	Why are test questions generated by LLMs better than ones generated by humans/experts?
6.	How does the method distinguish between guidelines for the LLM and guidelines for the builders?
7.	Does the Illustrative AI risks guideline relate to the construction of unethical content or the generation of knowledge associated with it?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper the authors report on the development and testing of GUARD (Guideline Upholding Test through Adaptive Role-play and Jailbreak Diagnostics). GUARD is aimed at providing a tool by which developers and other interested parties can test how well Large Language Models (LLMs) comply with ethical guidelines for trustworthy AI. The focus of GUARD is specifically on assessing how well outputs of LLMs comply with the guidelines, not whether LLMs are themselves developed in ways that are compliant with ethics guidelines. In very brief summary,  GUARD functions by first translating high-level ethical guidelines into questions that are aimed at getting the LLM to generate guideline-violating answers. It then uses jailbreak diagnostics to generate scenarios with the aim of identifying how guideline violations could arise. The authors report how GUARD was tested on various LLMs (and VLMs), and how it compared, favourably, to other similar tests. Lastly, the authors report on an ablation study used to identify how the different components of GUARD contribute to its success.

### Strengths
A strength of this paper is in how GUARD both generates questions and then aims to identify how violations could occur through jailbreak diagnostics. By automating this process, the paper offers conceptual insights into characteristics of jailbreaks, but also allows an iterative process to play out that goes some way to addressing limits of manually crafted jailbreak prompts. 

Originality: The adaptive roles that GUARD uses offers an original way of approaching guideline compliance, and through the ablation study, offers a better understanding of how the different roles contribute, and can detract, from ensuring compliance. 

Quality: The paper gives a thorough overview of the thinking involved in the development of GUARD. GUARD was tested not only on different LLMs but also compared to other jailbreak diagnostic tools. This comprehensiveness counts in favour of the paper. 

Clarity: The paper is mostly clear.

Significance: Overall, I think the paper and the GUARD that it reports on are significant. The way in which GUARD is structured (e.g. with different adaptive roles) and the ablation testing, in particular, offer an informative way of approaching identifying the vulnerabilities of an LLM. GUARD has the potential not just to be a means of compliance testing but its outputs could also be expanded on to better understand and diagnose vulnerabilities within an LLM.

### Weaknesses
The main weakness, for me, was one of clarity in a few places.

(1) It took me a while to be confident about what the actual aims of the paper were. In particular, the paper starts in the abstract and introduction by laying out a general gap in LLM compliance (‘There remains a gap in translating these broad requirements into actionable testing questions to verify LLM compliance’, abstract; implementation challenges (1) and (2) on p. 1). GUARD is introduced on p. 2 as directly addressing these challenges. However, there are jailbreak diagnostic tools already, as acknowledged in the paper, which from the outset just makes it unclear what GUARD is going to be contributing if framed in this early way. As the paper develops, it becomes much clearer that the aims are not straightforwardly to ‘fill’ this gap (which already has some filling), but to actually to improve safety in comparison to these kinds of diagnostics. This is captured in the introduction around the middle of p. 2, but by that stage I was floundering as a reader trying to figure out what the aims were.  To be clear myself, I do think that the aims are apparent in the paper (see especially ‘comparison to prior works’). My worry is that in the early stages of the abstract and the introduction, they are getting lost. As both the abstract and introduction are quite long, I would recommend being much more succinct in the introduction and abstract. I think this would be sufficient to enhance clarity about aims.

(2) Early on I was also not sure about what guidelines the authors were drawing on. Are they guidelines specifically to govern LLMs, for instance? As becomes apparent, no. But the guidelines referred to are ones that govern a range of things, including how systems are developed, trained and implemented. This leaves a conceptual gap between the guidelines and why they are relevant for then, in turn, governing a different kind of issue in what kinds of questions LLMs can answer. Take Fig. 1(a). The authors write that ‘An example of these guidelines from the EU’s regulation is illustrated in Fig. 1(a).’ (p. 1). But Fig. 1(a) doesn’t give an example of the guidelines; it gives an example of a question that has presumably been generated from the guidelines for the specific purposes of an LLM. The steps taken to go from a very general guideline for governing development and implementation to its relevance for determining what kinds of questions LLMs can answer should be given, as this is a step that one could potentially push back on. To address this, I recommend that the authors explicitly explain the justification for how these guidelines can be interpreted to inform the kinds of LLMs can answer. And also work with an actual example in the text itself, not just referring to figures or the appendices to illustrate. (In general, there could be more examples in the text itself of other things, like guideline-violating questions p. 2. There are examples to be found in the paper, but setting them off from the main text leaves the main text quite abstract.)

(3) There are a few typos. These don’t impact clarity too much but ought to be addressed. Some that I picked up:
p. 4 Figure 2 caption is missing a word, I think.
p. 5 [not a typo but for clarity]: ‘the question Q complies with guidelines G’. Is it the question that ought to comply, or the answer?
p. 6 ‘three government-issued guidelines … we selected 35 relevant guidelines’. Three or 35?

(4) Not clarity related, but I would have liked to see GUARD being tested on more recent LLMs, too. However, I think the paper as it stands does provide a proof of concept.

### Questions
How well does GUARD perform across different guidelines? Do some guidelines produce better compliance than others? (This could be informative for policy developers.)

Why focus on government-issued guidelines? What about other guidelines, like UNESCO’s? Relatedly, could GUARD potentially be used for in-house codes of conduct for a business?

How does GUARD perform with more recent LLMs, such as Llama 4? Or other widely available LLMs, such as Claude?

### Soundness
3

### Presentation
2

### Contribution
4

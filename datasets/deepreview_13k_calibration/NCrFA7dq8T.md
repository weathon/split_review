# The Same but Different: Structural Similarities and Differences in Multilingual Language Modeling

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 8, 6, 6, 5

## Abstract
We employ new tools from mechanistic interpretability in order to ask whether the internal structure of large language models (LLMs) shows correspondence to the linguistic structures which underlie the languages on which they are trained. In particular, we ask (1) when two languages employ the same morphosyntactic processes, do LLMs handle them using shared internal circuitry? and (2) when two languages require different morphosyntactic processes, do LLMs handle them using different internal circuitry? Using English and Chinese multilingual and monolingual models, we analyze the internal circuitry involved in two tasks. We find evidence that models employ the same circuit to handle the same syntactic process independently of the language in which it occurs, and that this is the case even for monolingual models trained completely independently. Moreover, we show that multilingual models employ language-specific components (attention heads and feed-forward networks) when needed to handle linguistic processes (e.g., morphological marking) that only exist in some languages. Together, our results provide new insights into how LLMs trade off between exploiting common structures and preserving linguistic differences when tasked with modeling multiple languages simultaneously.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to explore how similar or different circuits are across languages for linguistic tasks in language models. It takes a case-study approach, focusing on two tasks (IOI and past tense task), two languages (English and Chinese), and three language models (two for IOI and one for the past tense task). The past tense task involves morphology, which allows the authors to analyze how it’s handled in different languages.

Using techniques like path patching, the authors identify circuits and find significant overlaps between languages for both tasks. They also highlight interesting differences, like specific "past tense" heads in English.

### Strengths
_Clarity:_  
The paper is clear and well-written, with high-quality illustrations and concise, precise language. The flow is logical, and the key points are emphasized effectively.

_Quality:_  
The experiments are well-designed and effectively executed. The choice of mechanistic interpretability techniques to explore cross-lingual overlap is sound, and the methods are applied accurately. The IOI and past tense tasks are suitable examples; IOI builds on established monolingual work, while the past tense task introduces unique, language-specific morphological challenges.

_Originality:_  
This work is notable for its detailed, fine-grained circuit-level analysis of cross-lingual overlap in models.

_Significance:_  
For the NLP community, particularly those working on cross-lingual models and low-resource languages, this work provides a valuable deeper understanding of cross-lingual transfer down to the circuit level. This detailed approach might inspire new techniques for more effective cross-lingual transfer.

### Weaknesses
 _Scope of Main Claims:_
In my view, the primary contribution of this work lies in _demonstrating a specific case study_ of circuit-level cross-lingual transfer between languages in related or separate models. While the paper aims to make broader claims about multilingual models, the setup—two languages, two/three models, and two tasks—suits a focused case study rather than generalizable conclusions. Although the paper acknowledges these limitations, the claims in the introduction could be adjusted to better reflect the scope of the experiments. The limited scope makes it difficult to ascertain whether the observed circuit overlaps are consistent across a wider range of languages or if they are specific to the chosen language pair and tasks. For example, the past tense task, while insightful, is heavily reliant on the morphological structure of English and Chinese, and it's unclear if similar circuits would emerge in languages with different morphological systems. The paper should more explicitly acknowledge that the conclusions drawn are primarily applicable to the specific conditions of this study and may not generalize to all multilingual models or tasks.

_Related Work on Multilingual Interpretability:_
A broader review of related work could enrich the discussion, especially on different approaches that analyze multilingual models by aligning internal representations. For instance, [1] trains a monolingual transformer LM and transfers it to another language by retraining only the embedding matrix, hinting at cross-lingual structure similarities. This aligns with the monolingual IOI task analysis in this paper. [2] and [3] conduct coarse-grained analyses on similar cross-lingual interpretability challenges, while [4] aligns hidden states, and [5] provides further insights into the universality of these findings. [6] surveys cross-lingual alignment, offering broader yet less detailed conclusions on the inner workings of multilingual models. This paper can be seen as building on this older work by diving deeper into specific attention heads and showing detailed cross-lingual structures. The paper could benefit from a more detailed discussion of how its findings relate to these prior works, specifically addressing whether the observed circuit overlaps are consistent with the representational alignments found in other studies. For example, if prior work has shown that certain layers are more aligned across languages, the paper should discuss whether the identified circuits are located in these layers and if the observed overlaps are consistent with the degree of alignment.

### Questions
1. **Scope of Claims:**  
    Could the authors clarify why they make general claims about multilingual models despite the case-study limitations? Would they consider rephrasing these claims to better align with the study's focused scope? Is there a little clash between a generality of the paper title and strict case-study experimental approach?  
    
2. **Support or Contrast with Alignment-based studies**
	How do the authors’ findings support or differ from prior studies on multilingual alignment, especially those focusing on hidden state alignment? 

3. **Comparison with Coarse-Grained Studies:**  
    How do the findings here align with or diverge from conclusions in prior, coarse-grained studies on cross-lingual interpretability? Can conclusions from prior work with support from this work's experiments together support general claims or gain novel broader conclusions?

4. **Choice of Circuit-Level Analysis:**  
    While I am very much in favor of it, I am interested to hear more about why the authors chose a circuit-level approach over other methods and what alternative methodology options they considered. What other mech interp approaches would help support the authors claims in future work (e.g. analysis with SAEs)?  
    
5. **Broader Application:**  
    Do the authors have recommendations on which additional languages, models, or tasks would best extend this study’s findings?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper compares how LLMs process syntactic phenomena in English vs Chinese. The authors use two tools for analysing the mechanisms underlying LLM computations, namely path patching and information flow routes. They consider two syntactic phenomena, one shared across English and Chinese and another unique to English. For the shared syntactic phenomenon (indirect object identification), they show that LLMs use similar internal circuitry across both languages. For the language-specific phenomenon (morphological markers in English only), they show that circuitry diverges. The results show that multilingual LLMs employ overlapping circuitry for linguistic phenomena common across languages, and that similar internal mechanisms emerge for related syntactic processing even in monolingual models for different languages. The paper also presents a detailed analysis of the LLM computation involved in the studied syntactic processes.

### Strengths
I'd like to congratulate the authors on an excellent and super interesting paper!

(1) The analysis conducted by the authors is detailed, extensive, and extremely well presented. It provides concrete insights into the mechanisms underlying multilingual LLMs.

(2) The methodology followed by the authors is sound and extensively documented, providing a valuable framework and example for future researchers to investigate the circuitry of multilingual LLMs.

(3) The paper makes valuable contributions to multilingual interpretability, successfully unifying aspects of mechanistic interpretability with linguistically informed analysis.

### Weaknesses
Due to the heuristic nature of mechanistic interpretability tools like path patching, it’s difficult to conclude with certainty that findings such as those presented in this paper will generalise to other tasks/languages/models. However, the authors are careful to not overstate their claims.



### Questions
(1) By “ablate”, I assume you mean zeroing out the contribution of a head to compare performance with/without the head? I suggest that you just mention t what you mean by “ablate” explicitly somewhere, since you use the word quite often in discussion your results e.g. “To validate our findings, we ablate the heads 19.4 and 19.5 and analyze their impact on the tasks.”

(2) Section 4.5 can be organised a bit better. It contains quite a lot of information and requires the reader to refer to many figures. Potentially split the large paragraph (lines 403–418) into multiple subparagraphs, or organise the section into paragraphs with headings.

(3) Line 297: Fix wording of “This divergence is not able,”.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
**Paper Summary**:
- This paper shares some interesting findings on the similarities and differences between the internal structure of LLMs and the linguistic structure of English and Chinese. The authors employ mechanistic interpretability tools to explore the internal circuitry used by multilingual and monolingual LLMs when dealing with the same or different morphosyntactic processes. The findings indicate that there are common circuits and trade-offs when preserving linguistic differences.

### Strengths
**Summary Of Strengths**:
- Interesting topic and findings: I find it very attractive to use mechanistic interpretability to identify the relationship between models and language structures. The conclusion about common components between multilingual and monolingual models provides insightful ideas for further research.

### Weaknesses
 **Summary Of Weaknesses**:
- Limitation: The work is based only on Chinese and English and is limited to a few tasks and datasets. The conclusions could be more convincing if more languages were included. Specifically, the study focuses on morphosyntactic processes, which can vary significantly across language families. The current selection of languages, while providing a starting point, does not account for the diversity of linguistic structures. For example, languages with richer morphology or different word orders might reveal different internal circuits within LLMs. Furthermore, the limited number of tasks and datasets may not fully capture the complexity of language processing, and the observed commonalities might be task-specific rather than generalizable across different linguistic phenomena.
- Clarity on future impact: It may be challenging to transfer the learning from this work to current multilingual LLM training efforts, which underscores the need to better understand the findings (e.g., cross-lingual transfer learning, parameter migration, etc.). The study does not clearly articulate how the identified common circuits and trade-offs can be leveraged to improve multilingual model training. For instance, it is unclear how the specific knowledge of shared mechanisms could be used to guide parameter updates or to design more efficient training methods. The practical implications of the findings for current training paradigms remain vague, hindering the translation of these insights into actionable improvements.

### Questions
Do you have any initial ideas on how to conduct cross-disciplinary collaborations based on this work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper assesses whether English and Chinese monolingual and multilingual language models use similar circuits for similar morphosyntactic processes (indirect object identification; IOI) and different circuits for differing processes (past tense inflection). They use path patching and information flow routes to identify circuits. They find that similar circuits are used for IOI in English and Chinese, for both monolingual and multilingual models. Overlapping circuits (in this case copy heads in attention) with language-specific components (in this case MLP blocks for English inflection) are used for past tense inflection.

### Strengths
1. The tasks and methodology appear sound and well thought-out.
2. The paper is well-written, although some additional details would be very helpful (see weaknesses below).
3. The ablation results are convincing, e.g. FFN ablation in Section 4.6 dropping performance specifically for English. Also Figure 11 in the Appendix showing the effect of ablating different attention heads.
4. The results are interesting; language-agnostic and language-specific components have previously been proposed in multilingual language models (e.g. https://arxiv.org/abs/2205.10964; https://arxiv.org/abs/2109.08040; https://arxiv.org/abs/2009.12862), but the concrete demonstrations in this paper (specific circuits and their functions) are very informative.

### Weaknesses
1. The results in Section 3.5 and the last paragraph of Section 3.4 ("We first use path patching to identify…"; p. 5) are difficult to interpret without a good amount of background from Wang et al. (2023). A high level overview of how the different types of attention heads are quantified would be extremely helpful. Specifically, the paper mentions 'copy heads' and other functional head types, but it's unclear how these are identified algorithmically. The description of the path patching method is also quite high-level, making it difficult to assess the validity of the identified circuits. For example, it's not clear what criteria are used to determine the 'start' and 'end' points for patching, or how the effect of patching is quantified.
2. Related to the previous point, the results indicating similar circuitry (Figures 2 and 3) rely quite a bit on the reader trusting that the algorithms visualized in Figures 2 and 3 are accurate. The description of how the head types and arrows are determined is fairly minimal ("In both GPT2 and CPM, we identified similar circuits as Wang et al. (2023) outlined in Figure 3"; p. 5), so evaluating the validity of the algorithms identified in the figures is difficult. The paper should provide more details on the specific metrics used to quantify the information flow and how these metrics are used to identify the functional roles of different attention heads. It's also unclear how the directionality of the arrows is determined; is it based on attention weights, or some other measure of information flow?
3. Minor point: "Anecdotally, we observe that many of the heads that are shared between English IOI and control are also shared with Chinese IOI... further work is needed to test this hypothesis quantitatively" (p. 5). It could be helpful to have some very preliminary quantification, e.g. n% of the shared heads from English IOI and control are also shared with Chinese IOI, given some threshold for similarity. The lack of any quantitative measure here makes it difficult to evaluate the strength of this observation. A simple overlap percentage would be helpful.
4. Consider moving Figure 11 into the main text if possible, since it is referenced several times in Section 4.5.

### Questions
1. Could you provide some detail for how the attention head types and arrows in Figures 2 and 3 were identified? The figures imply fairly strong claims about how the internal algorithms work, so a description of the method used to identify the directed graph feels somewhat important.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The submission uses interpretability tools to examine if the LLM’s mechanisms behind solving linguistic tasks are similar or differ across languages. Following Wang et al., 2023, the authors use path patching to identify information circuits in multilingual models corresponding to the same morphosyntactic task in two languages. The aim of the experiments is to examine whether such circuits will be the same (or similar) for solving tasks in distinct languages.
The paper focuses on two tasks: object identification and verb past tense inflection in English and Chinese. The performance in the tasks is checked via generic prompt filling. Experiments cover two multilingual models: BLOOM (in case of object identification) and Qwen2-0.5B-Instruct (verb past tense inflection).

The results show that in fact, the found circuits are similar across languages, suggesting that multilingual language models implement a shared mechanism for solving considered linguistic tasks across two languages (Chinese and English).

### Strengths
- The work tackles the timely problem of interpreting LMs’ functions across languages. Despite the community's focus on interpretability and multilingual models, not many works have tried to explain the mechanisms behind LMs' multilingualism.


- The authors put the work in the context of past approaches in circuit identification (especially Wang et al. 2023), extending the experimental settings to multilingual models.


- The experimental part studies the identified circuits in-depth: comparing across languages the overlap of heads in the circuits and the information flows.

### Weaknesses
 - The linguistic scope of the experiments is limited. The method is applied only to two relatively simple morphosyntactic tasks in two languages. The results are close to 100% in object identification, which is a sign of saturation (a more complex task would be more informative). Only two distinct languages are considered. Therefore, the result does not show whether typological similarity could affect the similarity of the identified circuits. The choice of tasks, while foundational, does not fully explore the range of linguistic phenomena that could be investigated with this methodology. For example, syntactic tasks involving long-range dependencies or semantic tasks requiring contextual understanding could reveal different patterns of circuit similarity across languages.

- The choice of models used for experiments is chaotic. It is not clear why Qwen2-0.5B-Instruct is not considered in the object identification task. The paper should present the results for both tasks, at least for two considered models. This inconsistency makes it difficult to draw general conclusions about the cross-linguistic behavior of these models. Furthermore, the lack of a clear rationale for selecting specific models for specific tasks raises concerns about the robustness and generalizability of the findings. The study would benefit from a more systematic approach to model selection, perhaps by including models with varying architectures and training data.

- The methodology should be described in more detail, focusing on its implications in the multilingual setting. For instance, I understand that the head types were already described in the work of Weng et al. 2023, but the natural question is what linguistic role these types have across different languages. The paper needs to clarify how the identified 'circuits' are defined and how their similarity is quantified across languages. The description of the path patching technique should be more detailed, particularly regarding how it is applied to multilingual models and how it accounts for differences in tokenization and vocabulary across languages. The current description lacks the necessary detail to allow for replication or a thorough understanding of the method's nuances.

### Questions
- Does tokenization affect your experimental setting? More specifically, do you require that the queried property (object, past tense verb) be represented as one token?

- Why don’t you present the results for IOI with Qwen2-0.5B-Instruct?

- Why do you filter the English verbs with irregular past inflection?

### Soundness
2

### Presentation
3

### Contribution
2

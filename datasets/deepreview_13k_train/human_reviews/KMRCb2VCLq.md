# Identifying and Analyzing Task-Encoding Tokens in Large Language Models

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
In-context learning (ICL) has become an effective solution for few-shot learning in natural language processing. 
However, our understanding of ICL's working mechanisms is limited, specifically regarding how models learn to perform tasks from ICL demonstrations. For example, unexpectedly large changes in performance can arise from small changes in the prompt, leaving prompt design a largely empirical endeavour.
In this paper, we investigate this problem
by identifying and analyzing \emph{task-encoding} tokens on whose representations the task performance depends. Using experiments that ablate the representations of different token types, we find that template and stopword tokens are the most prone to be task-encoding. In addition, we demonstrate experimentally that lexical meaning, repetition, and text formatting are the main distinguishing characteristics of these tokens. Our work sheds light on how large language models (LLMs) learn to perform a task from demonstrations, 
deepens our understanding of the varied roles different types of tokens play in LLMs, and provides insights for avoiding instability from improperly utilizing task-encoding tokens.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates how large language models (LLMs) handle in-context learning (ICL) by focusing on the role of different token types in few-shot learning prompts. The authors identify three main token types within an ICL prompt—content, stopword, and template tokens—and assess how each impacts model performance. Through a combination of token-level and representation-level ablation studies, they find that template and stopword tokens, rather than content tokens, significantly influence the model's task-solving ability. This finding contradicts typical expectations, as content tokens carry the primary information. They further analyze characteristics of these task-encoding tokens, identifying lexical meaning, repetition, and structural cues as key factors in their importance. The authors conclude that the roles of different tokens are nuanced and that stopwords and template tokens aggregate contextual information that supports task-solving within LLMs.

### Strengths
The paper addresses a timely question in ICL, offering new insights into how LLMs encode and use task information. By combining token-level and representation-level ablations, the paper provides evidence for its conclusions about task-encoding tokens. The findings are validated across different model sizes and datasets, enhancing the robustness of the results.

The division of token types into content, stopword, and template tokens is a useful categorization that contributes to understanding which elements of the prompt have greater impacts on LLM performance. This is an interesting research question and the paper’s insights may at some point be used to design prompts for LLMs, as the identified characteristics of task-encoding tokens (lexical meaning, repetition, structural cues) may offer guidelines for practitioners. However, this paper does not go all the way there.

### Weaknesses
The definition of task-encoding tokens, based on performance degradation when excluded, could be more conceptually grounded. Additional theoretical justification might enhance clarity of the paper. I found this part a bit ad-hoc.

While the paper briefly mentions the findings’ implications, a deeper discussion on potential applications in prompt engineering or model robustness can significantly add value to the paper.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work defines "task encoding tokens" as input tokens where masking its representation leads to a drop in in-context learning performance. They find that template and stopword tokens, which are not informative of the task itself, are more likely to be task encoding than content tokens. They also analyze the representations of template tokens, since they contribute the most to ICL performance, finds that different template tokens are mostly all important and their representations may serve as information anchors, lexically meaningful template tokens lead to better performance, and repetition of template tokens is important.

### Strengths
Investigating the contributions of different input tokens to ICL is an interesting study in the broader theme of works attempting to better understand ICL. Diving input tokens into three categories and comparing the importance of each category is an interesting way to conduct this analysis. The paper also performs a series of interesting analyses on the task encoding tokens they find, which I think would be beneficial to LLM understanding.

### Weaknesses
My main reservation with this paper is its framing, since one of the main pitch is that non-content tokens are "task encoding" when some results and discussions in the paper alludes to how these tokens mostly serve as an information anchor for carrying information from content tokens, and the representation of the non-content tokens themselves may not be "task encoding" so this is misleading.

The contrast between representation-level and token-level ablations should be signposted earlier in the paper, since it current reads as an abrupt change in findings or interpretation of the ablations. The token-level ablation seems to suggest that contrary to what was discussed in the representation-level ablation, the representations of template and stopword tokens alone do not encode the task well, and it is more from the information of content tokens being propagated to template and stopword tokens that seems relevant to ICL performance. For this reason, I am not convinced by one of the main claims in the paper that template and stopword tokens are "task encoding".

Also, what is the distribution of the number of tokens in each type, and how did you control for the number of tokens being ablated when analyzing the contribution of each type? For example, how do you ensure that ablating template and stopword tokens leads to a drop in performance simply because you're possibly taking a larger set of tokens to ablate? It would be also helpful to have a random baseline where you ablate random tokens to see how much ICL score drops.

### Questions
I suggest revisiting the framing of the paper in light of what I mentioned in the above section, and some of my questions are also included in the above section.

### Soundness
3

### Presentation
2

### Contribution
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
The authors study task encoding tokens (I'll refer to these as TETs for brevity), tokens whose representations strongly influence an LLM's ICL performance. They use two methods to evaluate TETs: masking attention maps (representation-level ablation) of possible TETs and removing TETs themselves (token-level ablation) by removing these tokens from the input prompt. The authors explore 3 candidates for TETs: stopwords, template tokens, and content (i.e. tokens that aren't stop/template/ICL answers) tokens. The authors find that template tokens are the strongest candidates for TETs, followed by stopwords; ablating content words has surprisingly little impact on performance. This stands in contrast to prior work which only studies how ICL answer tokens impact ICL performance. They dive deeper by analyzing what characteristics of tokens LLMs use for identifying TETs, and they find that lexical meaning, repetition, and structural cues are all important for ICL performance, particularly for 3B-13B size models, suggesting these characteristics are all used by LLMs for identifying TETs.

### Strengths
- This is an interesting problem and well-motivated. "How do LLMs represent task specifications and solutions?" is an important question and studying token-level representations seems like a promising approach to answering it.
- Good descriptions of most methods and experiments, including many details in appendices.
- Thorough analyses, including many alternate conditions and a deep dive into what lexical characteristics are used to identify TETs.
- Interesting result that stopwords more strongly encode task information compared with "content" words.

### Weaknesses
 - I'm confused about the token-level ablation experiment/results (Sec. 4.3.2; Fig. 3). Footnote 5 on page 7 doesn't seem to match Figure 2, Bottom, since the Test example tokens aren't shown as ablated, and I'm not sure how the accuracies in Figure 3 could possibly be so high if all content tokens are removed *in the test example*. Answering the text example question correctly seems to depend on the content words, instead of getting a relatively nonsensical prompt like "the the . by a the : by .". Am I misunderstanding something?
	- I might be willing to raise my score if this was sufficiently addressed.
- The first two intro figures could be improved. 
	- Figure 1 is a bit hard to parse, and it's confusing that most boxes are labelled with tokens but the blue boxes are labelled "Test example" in the same font.
	- Figure 2 could benefit from token examples like figure 1 has, and doesn't show that there are multiple ICL examples of (T^in, D^in, T^out, D^out). Assuming my interpretation is correct, the caption of Fig 2 should also mention that this is an example of content/stop-word ablation, since for template word ablation T^in and T^out would be ablated instead of D^in.
- No results for larger/newer models (70b+, IFT), and some of the results such as the analyses in Section 5 seem to apply less for the largest model the authors tested (llama 30b).
- The baselines / null hypothesis seem a little weak. Indeed it is interesting that TETs are template+stop words instead of content words, however, I'm not sure what prior work would predict.
	- (a) If "information is being propagated from the representations of content tokens to the representations of the task-encoding tokens", this definition of TET seems to deviate significantly from "human attention to informative words", which is more like token-level attention. I'm also not sure how humans would do on a similar task, e.g. in an experiment where you mask all words except content words.
	- (b) The authors define "content words" as being any non-[stop/template/answer] tokens, which seems very broad given that "content tokens" in this case includes most tokens (e.g. in Table 14). While it's surprising that performance remains so high with no content tokens, I wonder if there are specific content tokens which are also TETs, such as named entities, or how a baseline of N randomly selected unmasked tokens would do.


Minor:
- Appendix text in many sections is very brief.

### Questions
- For token-level ablation, given that you're ablating tokens from "both the demonstration tokens as well as the tokens in the test example", I'm confused how the -CONT results in Figure 3 are this high (or even above chance). How is it possible that the test examples are being answered correctly with inputs like "the the . by a into : by ." (as in Table 14), or can you help me understand what's going on here?
- How would you expect larger models, and those with fine-tuning such as SFT and RLHF/DPO to perform, particularly in light of work such as [1]?
- Can TETs generalize outside the format of few-shot ICL? Do you expect TETs in zero-shot learning (e.g. [2]), and would results such as the importance of template tokens change in 0-shot?
- Could you provide concrete examples of how this work could be used to develop better ICL prompts (Appendix J)?


[1] Wei et al. (2023). Larger language models do in-context learning differently.

[2] Kojima et al. (2022). Large language models are zero-shot reasoners.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper classifies the input tokens and analyzes their functions under the in-context learning (ICL) scenario. Unlike previous work, which only focused on the input sentences and labels, this work extends the ablation analysis to template tokens.

### Strengths
1.  The function and selection of ICL templates are not well-discussed by previous work. Some findings about the template could be helpful for the further understanding and usage of ICL.
2.  Besides the ablation study, the authors further analyze the template tokens, e.g., their lexical meaning and repetition. Some findings are novel and interesting.

### Weaknesses
However, I still have several concerns about this work. 
1.  Ablation study design. Most previous ICL studies simply remove tokens or change them to random ones for the ablation. For this work, the authors choose to mask these tokens. Intuitively, it doesn’t matter. However, the position embedding and other practical factors may affect the conclusion. For example, for SST-2, even if you remove all ICL templates and only feed the input-label pairs, the performance could be much better than masking all template tokens (52.1%, which is almost random guessing). The authors should justify this point to support that the results are valid: showing that masking the template is equivalent to removing or randomizing it.
2.  Since this paper focuses on the task-encoding tokens, simply running experiments on the task classification datasets may be a bit weak. These datasets are more or less similar for ICL: semantic-relevant, simple classification format, … Findings on them could be quite limited as the ICL insights. It would be stronger if some other datasets e.g., QA or reasoning are included and the findings are consistent.
3.  (two minor issues). For experiment random seeds, you can select 4 random examples for each test data to decrease the variance. Then you don’t have to repeat the experiments for that many times. Besides, for the LLaMA-30B, it’s actually 33B.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
3

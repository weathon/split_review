# Listening to the Wise Few: Select-and-Copy Attention Heads for Multiple-Choice QA

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
A standard way to evaluate the abilities of LLM involves presenting a multiple-choice question and selecting the option with the highest logit as the model's predicted answer.  However, such a format for evaluating LLMs has limitations, since even if the model knows the correct answer, it may struggle to select the corresponding letter simply due to difficulties in following this rigid format. To address this, we introduce new scores that better capture and reveal model's underlying knowledge: the Query-Key Score (QK-score), derived from the interaction between query and key representations in attention heads, and the Attention Score, based on attention weights. These scores are extracted from specific \textit{select-and-copy} heads, which show consistent performance across popular Multi-Choice Question Answering (MCQA) datasets. Based on these scores, our method improves knowledge extraction, yielding up to 16\% gain for LLaMA2-7B and up to 10\% for larger models on popular MCQA benchmarks. At the same time, the accuracy on a simple synthetic dataset, where the model explicitly knows the right answer,  increases by almost 60\%, achieving nearly perfect accuracy,  therefore demonstrating the method's efficiency in mitigating MCQA format limitations. To support our claims, we conduct experiments on models ranging from 7 billion to 70 billion parameters in both zero- and few-shot setups.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The widely used evaluation for large language models, multiple-choice question answering (MCQA), is very brittle, especially for small models -- existing works show that even if models know the answer, it often cannot output the correct A/B/C/D due to all sorts of bias. This work proposes to tackle the problem by looking at a novel QK-score: they first select certain "select-and-copy" attention heads based on a validation set, and then calculate the query-key dot product between the option and the question (there are many possible ways, and the authors conducted thorough ablations). 

The authors conducted comprehensive experiments on commonly used datasets, with zero-shot/many-shot experiments across model scales. The proposed method significantly improved over the standard MCQA baseline and some previously proposed methods. The analysis revealed interesting aspects, such as the meaning of a phrase is often encoded in the last token of the phrase.

My main concern is:

(1) Cloze completion has been widely used and has shown to be much more stable than MCQA in most standard evaluations. There is almost no discussion on it and also no empirical comparison. Since the work's main goal is to make evaluation more reliable, I found the lack of comparison significantly undermines this work's contribution.

(2) Improving the score doesn't make one evaluation better -- the authors should show that it reflects a better comparison that is more consistent with human evaluation or some intuition (for example, previous evaluations show much higher variance or reversed trends like an 80B model is worse than 7B; this new method fixed it).

### Strengths
(1) The brittleness of MCQA is well known and is a problem in evaluation. The proposed method is intuitive, simple, and effective. 

(2) The authors conducted a comprehensive evaluation and interesting analysis that demonstrated the effectiveness of the method.

(3) The proposed method can be used beyond standard evaluation, especially in interpretability applications.

### Weaknesses
My main concern is:

(1) Cloze completion has been widely used and has shown to be much more stable than MCQA in most standard evaluations. There is almost no discussion on it and also no empirical comparison. Since the work's main goal is to make evaluation more reliable, I found the lack of comparison significantly undermines this work's contribution.

(2) Improving the score doesn't make one evaluation better -- the authors should show that it reflects a better comparison that is more consistent with human evaluation or some intuition (for example, previous evaluations show much higher variance or reversed trends like an 80B model is worse than 7B; this new method fixed it).

### Questions
Please see the "weaknesses" section + the question below

(3) How does the variance of each method look like for the main table/figure, especially when sampling different in-context examples + different orders?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work introduces two new metrics—the Query-Key Score (QK-score) and the Attention Score—that utilize select-and-copy attention heads within the models to better capture their underlying knowledge. The authors argue that relying solely on logit scores to select answers can be misleading, especially for smaller models struggling with rigid formats. By using intermediate attention representations, this method reveals deeper insights into the model’s understanding, yielding accuracy gains of up to 16% on MCQA benchmarks such as MMLU and HellaSwag. The study finds that middle-layer attention heads are particularly effective, whereas later layers tend to revise and diminish performance. Overall, this work contributes an approach that not only improves MCQA accuracy but also enhances interpretability of LLMs.

### Strengths
1. The authors introduce QK-score and Attention Score for deeper evaluation of LLMs.
2. This method yields significant gains in MCQA tasks, with up to 16% improvement on some benchmarks which is quite significant.
3. The work leverages internal attention heads, offering transparent answer selection.
4. The authors demonstrate the effectiveness of middle-layer attention heads over final layers.
5. This method is tested across models ranging from 7B to 70B parameters

### Weaknesses
1. While the experiments have been performed across different generations of llama models, showing generalization across model families could be important
2. Although the method is effective, there is complexity in terms of implementation. The applicability of the method to various practical scenarios remains questionable

### Questions
1. Some experiments / results on other model families
2. Comment on usability. (refer to comment #2 in weakness)
3. Given the complexity of the method, will be interesting to see latency analysis when compared to baseline.

### Soundness
4

### Presentation
4

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
This work presents a new method for improving the evaluation of LLMs in MCQA by recognizing and using select-and-copy heads, which are particular attention heads. These attention heads consistently extract relevant information and improve response selection using the Query-Key Score (QK-score) and Attention Score. The strategy significantly improves MCQA benchmarks and a synthetic dataset for understanding. The study emphasizes the importance of intermediate attention states for disclosing underlying knowledge, particularly in smaller LLMs where typical output-based evaluation may understate the model's capabilities.

### Strengths
The paper introduces the concept of attention heads that are adept at copying information relevant to MCQA tasks, advancing the interpretability of LLMs.
QK-score and Attention Score are presented as innovative metrics that provide deeper insights into model decision-making processes.
Strong experimental setup with results across different models and settings enhances the credibility of the findings.

### Weaknesses
The approach focuses heavily on MCQA and may not generalize to open-ended or complex QA tasks.
Evaluating individual attention heads may be resource-intensive, especially for larger models.
While improving robustness, the paper does not fully address biases inherent to specific head selections. Performance can differ based on head choice, potentially introducing instability in applications without careful selection.

### Questions
1. Investigate the relevance of the methodology to a broader range of QA formats and practical open-domain tasks.
2. Suggest ways or instruments that facilitate the selection and utilization of appropriate heads for enhanced adoption.
What precautions were implemented to prevent the identified select-and-copy heads from introducing unintentional biases in model outputs?
4. How is the effectiveness of these attention heads different for different model types, such as encoder-only vs. decoder-only?
5. Is it possible to scale cross-lingual or multilingual multiple-choice question answering evaluation?
6. How well do the QK-score and Attention Score work when used in models that have been fine-tuned for specific topic tasks?

### Soundness
3

### Presentation
2

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
The authors use a small amount of labeled data to identify "select-and-copy" heads. These are heads where information is being copied (via the attention mechanism) from a token the authors associate with a particular answer option (e.g., the newline after the option text) to the final token that will be used for prediction. This selection is primarily done by max "QK-score" (dot product between the query of the last token and key of the token associated with the answer option). The authors show "select-and-copy" heads are present in a variety of Llama models. They argue that using these heads for prediction leads to better accuracy and is less dependent than baseline on the order of answer options. The authors also run some design and head ablations, and explain an approach to finding "select-and-copy" heads in a label-free way.

### Strengths
* ORIGINALITY: I'm not very familiar with mechanistic interpretability work, but in my view this work seems quite novel. The authors find attention heads that seem to have a very well-defined function for MCQA, and show these are present in many models.
* QUALITY: The authors' experiments seem well-designed and their argument (at least regarding the presence of "select-and-copy" heads) is convincing. The authors also have a sizable appendix, suggesting they've tried a lot of things.
* CLARITY: The paper is mostly clear and easy to read.
* SIGNIFICANCE: I think this is significant in that it provides more insight into the mechanisms behind MCQA in LLMs.

### Weaknesses
 * Primary weaknesses
  * This paper heavily emphasizes the zero-shot case, but I don't think it should be highlighted (I think it should be moved to the appendix if included at all). This is because in the zero-shot case the right way of answering (for the baseline models) is ambiguous. A human wouldn't know whether to respond with a letter vs the answer option text. I think e.g., Table 1, for example, should not show zero-shot results. I don't think the zero-shot setting is a fair setting for comparison.
  * I don't think the "E" and "F" options should be included (or at most this should be moved to appendix). As far as I know, adding the "E" and "F" options is not consistent with the majority of prior work in MCQA, and seems like an added variable that's not justified.
  * The authors pitch QK-score as being better than PriDe, and also having much improved accuracy across answer orders. However, I am not convinced of either of these. In the 1+ shot, no "E"/"F" setting PriDE seems as good or better. Also in e.g., Figure 3, the drop for PA is substantial for QK-score (just as substantial as for the alternatives). It seems like, from the appendix, the baseline is actually better than QK-score in many cases. Just to be clear, I don't think the authors' method needs to be more accurate than alternatives for the paper to be useful or accepted. I'm just saying the authors could maybe reassess their claims a little bit.
* The authors only consider Llama models, so it's unclear if these results apply to other LLMs.
* I don't fully follow the "Best Heads" part and Figure 5a in Section 6 despite having read it a few times. I definitely get the point being made, but I couldn't reproduce the result based on the description. To improve understanding and reproducibility, it might be nice to include a step-by-step description or pseudocode.
* I didn't take this into account in my rating, but I think the paper could benefit from another solid pass just for grammar. There are just enough errors that at times it was a bit distracting.
* See questions for more things I think could use clarification/improvement.

### Questions
* Is RoPE applied when using attention score?
* Why is "stochastic" used to imply "sums to one" on line 147 (I may be missing something)?
* For Llama base vs chat models was the same prompt used? Would this lead to worse performance for the baseline?
* Why the big difference in accuracy for e.g., HaluDialogue vs small difference in accuracy for MMLU? I don't find the argument on 322-323 convincing.
* Why is attention score included? It seems like QK-score is used as the default, and attention score is barely mentioned. My inclination would be to move the attention score parts to the appendix to prevent confusion over when which score is being used. At the very least, there could be more clarification on exactly when each is being used.
* In the unsupervised head finding part, what accuracies do the top heads achieve? I'm curious if they're like 90% as good as the best ones, or if they're much worse because their function matches but they're doing something entirely different.
* Why not ensemble heads?
* I'm curious why accuracy remains quite high (despite the drop) in the head removal ablation (especially in higher shot setting). Is it just that there are more than 10 "select-and-copy" heads? Or do "select-and-copy" heads only explain part of what's going on?

### Soundness
3

### Presentation
3

### Contribution
3

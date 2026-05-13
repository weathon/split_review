# Which Attention Heads Matter for In-Context Learning?

- Decision: Reject
- Scores: 8, 3, 3, 3, 6

## Abstract
Large language models (LLMs) exhibit impressive in-context learning (ICL) capability, enabling them to generate relevant responses from a handful of task demonstrations in the prompt. 
Prior studies have suggested two different explanations for the mechanisms behind ICL:
induction heads that find and copy relevant tokens, and function vector (FV) heads whose activations compute a latent encoding of the ICL task.
To better understand which of the two distinct mechanisms drives ICL, we study induction heads and FV heads in 12 language models.

Our study reveals that in all 12 models, few-shot ICL is driven primarily by FV heads: ablating FV heads decreases few-shot ICL accuracy significantly more than ablating induction heads, especially in larger models. We also find that FV and induction heads are connected: many FV heads
start as induction heads during training before transitioning to the FV mechanism. This leads us to speculate that induction heads facilitate the learning of the more complex FV mechanism for ICL. 
Finally, the prevalence of FV and induction heads varies with architecture, which questions strong versions of the
"universality" hypothesis: findings from interpretability research are not always generalizable across models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the role of distinct types of attention heads—induction heads and function vector (FV) heads - in supporting ICL in LLMs. Using a set of ablation experiments across 12 transformer-based models, the authors find that FV heads are primarily responsible for effective ICL, particularly as model size increases. The study further explores the interplay between induction and FV heads, finding that many FV heads evolve from induction heads during training.

### Strengths
1. The study provides a fresh perspective on the mechanisms of ICL, highlighting the underestimated role of FV heads compared to induction heads. By introducing the idea that induction heads may serve as a precursor to FV heads, it opens new directions for understanding head evolution during model training.
2. The experiments are thorough, covering a range of model sizes and carefully controlled ablation studies. The authors demonstrate rigor in handling overlapping effects and using multiple model families (Pythia, GPT-2, and Llama 2) to validate findings.
3.  The paper is well-organized and clearly written. The authors provide a comprehensive background on induction and FV heads and lay out their methodologies and results in an accessible manner, making it easy to follow their conclusions.
4. This work addresses a fundamental question in the interpretability of language models and challenges existing beliefs about ICL. The findings contribute to a more comprehensive understanding of the roles of different attention mechanisms and could guide future work on interpretability techniques.

### Weaknesses
1. The conjecture that induction heads serve as a precursor to FV heads is supported by empirical observations but could be further validated by testing whether removing induction heads impacts the development of FV heads during training. This could help confirm the proposed causal relationship.


### Questions
1. Do the authors have insights into why the Llama 2 model exhibited lower FV scores, and how this finding might relate to differences in its architecture or training procedure compared to the other models?
2. Is there an explanation as to why the gap between the effect of FV heads and induction heads increases with model scale?

### Soundness
3

### Presentation
4

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
The paper studies the role of different attention heads to LLMs' in-context learning (ICL) capability. Specifically, the paper studies two types of attention heads, induction heads and function vector (FV) heads. Through empirical experiments, as opposed to prior belief, the authors find that ICL is mainly driven by FV heads. In addition, there is potential connection between induction heads and FV heads.

### Strengths
- It is interesting to understand ICL capability by connecting it to attention heads with certain mechanisms.
- I appreciate the authors disambiguate ICL and token-loss difference, which allows further disentanglement between the effect of induction heads and FV heads.
- I like the controlled ablation approach to separate the effect of induction heads and FV heads.

### Weaknesses
 - I am not very convinced by the ablation method used in section 4.1, i.e., by replacing output vector by mean values. It seems a bit ad-hoc for me without further justification. Why use mean but not other statistics? How robust are the results, or is it specific only to the ablation method used here? 
- Given that induction heads and FV heads appear at different locations (layers) within the model, head "location" can be one confounding factor that contributes to the difference in ICL performance when ablating induction heads vs. FV heads. There should perhaps be a controlled baseline that ablates heads at different locations in the model.
- The empirical results presented in the paper appear a bit weak. It is not clear how many tasks are evaluated (Is Figure 4 showing averaged results?), and which ICL tasks are used exactly? How well do the tasks represent real-world ICL/few-shot use cases?
- Some conclusions made from the observations seem more like conjectures instead of actual proof. Paper can be made more sound to clarify conjectures from conclusions with substantiated results. E.g., Line 252: "This suggests that induction and FV heads may not fully overlap, and that FV heads may implement more complex or abstract computations than induction heads".
- Minor: The paper presentation can be improved with clearer background introduction of induction heads and FV heads.

### Questions
- Sec 3.2 results are a bit confusing. If induction heads and FV heads are distinct (not overlapping), how could FV heads also have high induction scores, or vice versa? Does it suggest that there are some overlapping heads that have both high induction and FV scores?
- While it is interesting to understand ICL by connecting it to certain model attention heads, what are some actionable improvements/implications we could make after establishing the connection?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper compares the phenomena of induction heads (Olsson et al., 2022) and Function Vector heads (FV heads; Todd et al., 2024), both of which are key attention heads to in-context learning shown in previous interpretability literature, across 12 language models. The paper finds that the set of induction heads and FV heads are mostly distinct and FV heads usually appear deeper in models than induction heads, but there are correlations between the induction scores and the FV scores of the top induction heads and top FV heads, showing a correlation between these two distinct sets. Moreover, the paper examines the training dynamics of the selected models, and finds that FV heads are learned later in LMs than induction heads with respect to training steps and some induction heads become FV heads through training. Finally, the paper proposes two competing hypotheses to explain such differences and similarities between induction heads and FV heads, leaving a further investigation for future work.

### Strengths
1. The paper investigates two influential ideas in LLM interpretability that aim at explaining in-context learning, and is very well-motivated.

2. The paper conducts thorough empirical investigations between induction heads on a wide range of language models and FV heads and sheds light on a better understanding of how large language models learn and implement in-context learning. 

3. To the best of my knowledge, the paper is the first to explore how induction/FV heads are learned and formed during pre-training. This is in my opinion a concrete contribution to the community.

4. The paper is well-written with good presentations.

### Weaknesses
1. One of the key findings of the paper is that FV heads appear in deeper layers than induction heads do. However, by inspecting Figure 2 and Figure 13, I think the average layers of FV heads and induction heads do not look very far from each other (most of them differ by 1-2 layers). Particularly, the average layers for GPT2 Medium, GPT2 Large, GPT-2XL, and Llama 2-7B models seem to be the same. Therefore, I think some forms of statistical tests might need to be done here to strengthen the argument. Specifically, the authors should provide the standard deviation of the layer locations for both induction and FV heads, and then perform a t-test to determine if the difference in means is statistically significant, especially for the models where the means appear similar. Without this, the claim of a consistent difference in layer depth is not fully convincing.

2. Another argument the paper makes is that induction heads and FV heads are distinct using the metric defined in line 260. However, it is possible that neighboring attention heads could be performing similar functionalities in LLMs, as shown by [1] and follow-up works. I think only measuring the exact overlap between the two sets of heads might be a bit misleading; it might be better to measure the overlap of layers where the two sets of heads reside. For example, the Pythia 6.9 B plot in Figure 2 shows that both sets have some heads in layer 8 and layer 17. The authors should consider a metric that quantifies the overlap of layers where the two sets of heads are active, rather than just the exact head overlap. This could be done by calculating the proportion of layers that contain both induction and FV heads, or by using a distance metric between the layer distributions of the two head types.

3. The paper claims that "previous studies on induction heads focus on small model sizes" (line 187). However, I think this is inaccurate as works such as [2][3] have already extended induction heads to large models up to 20B/66B. Moreover, these papers also discuss the effects of scales on induction heads and in-context learning of LLMs. These prior works are not discussed in the paper, making the paper's claim of contribution for investigating induction heads at larger scales weaker. The authors should acknowledge these prior works and clarify the specific novel contributions of their work, perhaps by focusing on the training dynamics or the comparison with FV heads, rather than claiming to be the first to study induction heads at larger scales.

4. Combining 1-3, I think some of the main findings of the paper might be a bit fragile and relatively incremental.

### Questions
1. For the induction heads and FV heads analyzed in Section 5, are they obtained from each checkpoint separately, or they are obtained from the last checkpoint only?

2. Regarding conjecture C2 discussed in Section 6, why would it "predict that ablating monosemantic FV heads would not hurt ICL performance? (line 466)? Is it possible that the monosemantic FV heads are important task-specific operations beyond copying (which is the mechanism implemented by induction heads)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the two primary existing explanations for the mechanisms behind in-context learning (ICL) – induction head and function vector (FV) head. First, the authors reveal the correlation between the head types. They find little head overlapping but a FV head usually has a relatively high induction score, and vice versa. Moreover, some of FV heads evolved from induction heads during training. Second, ablation experiments show FV head plays a more important role than induction head in ICL when using few-shot learning accuracy as the metric. The authors argue that this discrepancy from previous literature stems from the different metrics. Induction head was measured by token-loss difference rather than accuracy.

### Strengths
1. This paper presents a detailed empirical analysis and links the two ICL mechanisms. The mechanism of ICL is important for the development of LLMs.
2. This paper reveals that FV heads have a stronger causal effect on ICL performance than induction heads.
3. Experiments are solid.

### Weaknesses
1. This paper only makes comparisons between induction heads and FV heads, without any technical or theoretical improvements, nor providing a more effective explanation of the ICL mechanism. The indicators (induction score and function vector score) are borrowed from each original paper. So, the novelty is limited.
2. Although the authors present several new findings about induction and FV heads, it is still unclear how these findings will benefit future research works.

### Questions
Please discuss the contributions of your findings to promote the performance of current In-Context Learning in details.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the importance of attention heads in large language models (LLMs) under the lens of in-context learning (ICL). The paper compares "induction heads" from [1,2] and "FV heads" from [3], and finds that these two kinds of heads are distinct, but correlated. They show that reconciling different definitions of ICL help explain the difference.

___
[1] Elhage, et al. A Mathematical Framework for Transformer Circuits. 2021. (https://transformer-circuits.pub/2021/framework/index.html)

[2] Olsson, et al. In-Context Learning and Induction Heads. 2022 (https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)

[3] Todd, et al. Function Vectors in Large Language Models. 2023. (https://openreview.net/forum?id=AwyxtyMwaG)

### Strengths
- The writing of the paper structure was good and easy to follow
- The paper studied multiple model sizes and families to investigate the generality of the findings.

- Investigating induction heads more deeply in the few-shot ICL setting, and in larger models is interesting and worthwhile. While Olsson, et al. [2] does have a discussion about their reasoning for choosing token-loss difference, this paper suggests that different metrics (few-shot ICL vs. token-loss difference ICL) capture distinct effects. This trend is clear and consistent across models, suggesting that induction heads might not be the only contributors to (few-shot) ICL performance in language models.

### Weaknesses
 - One of the main concerns I have with the results in this paper is that many of the models studied do poorly on few-shot ICL. For example,  Figure 4 and Figure 7 show that many of the small models average 20-30% accuracy across ~20 ICL tasks (this seems not great). If the models can't really do the task w/ few-shot prompting, how much can we really say about the "mechanism" behind it. In Line 318-319, it says: "We also plot ablations for all models, and ICL accuracy broken down by task, in Appendix A.2.", but as far as I could tell the breakdown of accuracy by task is missing. Can the authors clarify if the models they're testing are consistently better than baselines for the tasks they use (i.e. can the LMs "do" the task they're using to evaluate their claims)?

- The bulk of the evidence of "importance for attention heads" is based on mean ablation of attention heads. In some cases, ablation can cause adaptive computation (see McGrath, et al. [4]), and I wonder if there are other ways to verify that induction heads are not "important" for few-shot prompts, or FV heads are not "important" for token-loss difference other than ablation? The current methodology does not sufficiently address the potential for compensatory mechanisms within the network, which could mask the true impact of specific attention heads. It would be beneficial to explore alternative methods, such as directly measuring the contribution of specific heads to the output logits, or using techniques that analyze the information flow through the network, to provide a more robust analysis.

- In their paper, Olsson, et al. [2] do indicate that some induction heads they found that implement more sophisticated pattern matching while also fulfilling the traditional role of induction heads. It seems to me that the authors of [2] were aware that induction heads were not the entire story of ICL, but did not have words to describe it yet (e.g. they call this behavior "spiritually similar" to copying). I think this paper's Conjecture 1 matches this sentiment, and posit that perhaps FV heads are a generalization of induction heads, but I'm not sure whether this work engages with this previous acknowledgement by [2]. 
- Related to this -- While the paper does acknowledge the discrepancy in definitions of ICL in the literature (between few-shot vs. token-loss difference), some of the claims in the paper are a bit misleading for this exact same reason. For example:
   - Lines 51-52:  "This leads us to conclude that FV heads are mainly responsible for ICL, contrary to the prevailing belief that induction heads are a primary mechanism of ICL"
   - Lines 473-474: "Contrary to the prevailing consensus that ICL is largely driven by induction heads, we find that this assumption does not hold in most of the models we study."

The reason these types of statements misleading is because the experiments in Figure 4 and 7 of this paper still suggest that induction heads are important for the token-loss difference version of ICL. A way to make these kind of statements less misleading would be to qualify that this means "few-shot ICL" in the same sentence rather than a few sentences later on (e.g. "This leads us to conclude that FV heads are mainly responsible for **few-shot** ICL, ...", or "Contrary to the prevailing consensus that **few-shot** ICL is largely ...").



### Questions
- In some models, some FV heads are also induction heads (which was also pointed out in Todd, et al [3], Appendix H. How do you feel this strengthens or contradicts the claims in the paper that induction heads are not important for few-shot ICL?

- In Figures 5 and 6, there is a nice general trend, but it's hard to tell which heads are correlated. For example, is the sharp spike in Pythia 6.9B (bottom right) the same FV head that has a induction score spike at around $2^{9}$?

### Soundness
3

### Presentation
3

### Contribution
3

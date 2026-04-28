# Jogging the Memory of Unlearned LLMs Through Targeted Relearning Attacks

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8

## Abstract
Machine unlearning is a promising approach to mitigate undesirable memorization of training data in LLMs. However, in this work we show that existing approaches for unlearning in LLMs are surprisingly susceptible to a simple set of \textit{targeted relearning attacks}. With access to only a small and potentially loosely related set of data, we find that we can ``jog'' the memory of unlearned models to reverse the effects of unlearning. For example, we show that relearning on public medical articles can lead an unlearned LLM to output harmful knowledge about bioweapons, and relearning general wiki information about the book series Harry Potter can force the model to output verbatim memorized text. We formalize this unlearning-relearning pipeline, explore the attack across three popular unlearning benchmarks, and discuss future directions and guidelines that result from our study.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies targeted relearning attacks on large language models (LLMs) that have undergone approximate unlearning of certain information. The key idea is that by relearning on a small amount of auxiliary data that is loosely related to the unlearned information, it is possible to "jog" the memory of the unlearned model and cause it to output the supposedly forgotten information. They test relearning attacks on three common unlearning applications: 1) removing harmful/hazardous knowledge, 2) mitigating memorization of copyrighted content, and 3) suppressing retention of specific undesirable words/phrases. In each case, they show it is possible to recover the unlearned information by relearning either on a limited subset of the unlearned data that doesn't contain the target information directly, or by relearning on publicly available information related to the unlearned data. They provide a simplified theoretical example showing that when unlearned data contains correlated pairs of tokens, relearning on one token can trigger recovery of the other.

### Strengths
1. Demonstrates an important limitation in current LLM unlearning methods, showing they don't fully remove knowledge
2. Tests the relearning attack on multiple datasets, unlearning applications, and base models
3. Provides both empirical results and theoretical intuition for why relearning can recover supposedly forgotten information
4. Presentation is clear and results are well summarised at the end.

### Weaknesses
The simplified example is a very interesting experiment, and I think a promising direction for better understanding of which finetuning data can recover harmful capabilities from LLMs. The paper would have benefited from more experiments here with different datasets, models and n gram correlations to study.

Some discussion of defenses that model providers like OpenAI could deploy on their finetuning apis to mitigate the threat posed here, such as keyword filtering, would be helpful for the research community.

The result here is useful but not too far away from what has been suggested by Qi et al. (https://arxiv.org/abs/2310.03693). As such I think the strength of the contribution is relatively weak.

### Questions
I have no questions

### Soundness
4

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
This paper explores 'relearning' attacks on language models that have had a part of their dataset removed/suppressed using some machine unlearning technique. They show that in their examples training the 'unlearned' models on a related dataset/portion of the unlearning dataset causes performance on the unlearning dataset/holdout portion of the unlearning dataset to improve, and attempt to characterise this (in part) by considering correlations in the datasets.

### Strengths
- overall well-written and easy-to-follow paper.
  - some formatting (?) errors which obscure some maybe-important information (e.g. line 424, "Next, we construct the forget set D_u by collecting all the data that on a subset of the names." seems to be truncated)
- very clear discussion of limitations in previous works owing to overlap between relearn and evaluation data, and a useful factorisation into retraining on unlearning data vs retraining on related data.
- good/comprehensive selection of unlearning methods and datasets to evaluate.
- the experiment in section 6 is especially interesting and similar work to this would be a promising avenue for better understanding the situations in which relearning is a danger/possibility.
- useful evidence is gathered for demonstrating that LoRA unlearning is less effective against relearning than full-parameter fine-tuning.

### Weaknesses
 - not especially novel; some previous works (e.g. Lynch et al 2024, among others) have explored the relearning setting, and some have considered "the relation between relearn set and the queries used for evaluation" (e.g. Guo et al 2024 - "Robust Unlearning via Mechanistic Localization"). nonetheless it is still productive to have more work studying this.
    - exploring the themes touched on in section 6 in greater detail/with more [or more complex] examples (e.g. using a setting similar to TOFU, perhaps introducing artificial correlations/decorrelations between the unlearning/relearning datasets), or attempting to find a quantative relationship between e.g. correlation and relearning, would have strengthened the evidence for takeaway #3, which otherwise had relatively weaker evidence than takeaways #1 and #2.

### Questions
- did you manage to find any heuristics/quantative rules for predicting when relearning is especially easy/hard? does e.g. model scale, ROUGE or embedding-based similarity metrics, number of unlearning steps predict when relearning is easy/hard?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper discusses the vulnerability of machine unlearning processes in LLMs to targeted relearning attacks. Machine unlearning is designed to remove sensitive or unwanted data from training datasets to comply with regulations like GDPR or to enhance privacy. However, the authors demonstrate that with minimal and loosely related data, it is possible to reverse the effects of unlearning, effectively "jogging" the memory of LLMs to recall or reproduce the unlearned information. The authors conducted experiments on three representative LLM unlearning benchmarks, aiming to solidify the observations of their proposal.

### Strengths
LLM unlearning is an important topics that has received increasing attention these days, while we still lack a detailed understanding of the key mechanism behind it. The exploration of the relearning can contribute to the literature in the sense that unlearning might not be that easy as we previously think, as the recovering of unlearned knowledge indicates that they are still parameterised in the models after unlearning. It may also indicate that the current evaluation metrics of unlearning might be insufficient, as they typically suggest that many methods, such as GA, can fully remove the unlearned knowledge (though the retain performance is also affected).

The authors conducted experiments across a set of different unlearning benchmarks, backbones, methods, and setups. All the results align with the authors' observations that relearning can occur after unlearning. Also, the motivation figures are good.

### Weaknesses
My main concern is about the novelty, as many of the previous works have already suggested relearning can occur after unlearning. As suggested by the authors, the only difference over previous works is that this paper separates the data for relearning in a more solid and rigorous way. Also, the authors try to explain why relearning can occur, but the explanation, in my personal point of view, is a little bit of trivial. All the experiments the authors conducted are already under the assumption that the data for relearning and the data for unlearning has some strong correlation, so the explanation in Section 6 does not provide further information, considering the main explanation of "When the unlearned set contains highly correlated pairs of data, relearning on only one can more effectively
recover information about the other." I am also quite confused about the claim of "while these heuristics successfully limit LLMs’
power to generate samples xfrom Du, they do not remove associations between different parts of x." Since we minimise the conditional probability of p(x_i|x_<i), seemingly all the correlation within x will be destroyed. Please forgive me if I made any misunderstanding and kindly please explain more about this point. BTW, I think a possible way to improve the contribution of this paper is to explore new methods that are robust to relearning attacks, mainly considering the fact that the scenario of relearning is somewhat well-knowned in the literature.

I appreciate the authors to follow the classical definition of unleanring in eliminating the influence of data targeted to be unlearned. However, as suggested by [1], there are another possible goals of unlearning in the literature of unlearning: to much extent eliminate the knowledge targeted to be unlearned. I am not quite sure about it, but it seems that the "to much extent" goal may not more suitable for LLM unlearning since we want the possibility in generating unlearned data to be exactly zero.

### Questions
Kindly please refer to the section of weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors show that LLMs which have been subject to unlearning can still produce the learned information after additional finetuning on specific data (albeit data that does not contain the unlearned content), which the authors call "relearning".

### Strengths
- Figures 1 & 2 are nice schematics
- The experiments have a nice breadth and depth. I appreciate Section 6 for trying a simple experiment to identify the mechanism (even if the mechanism feels obvious)

Edit: I gave the authors clear instructions for what I thought would improve the paper:

> I would be happy to further revise my score to a 8 if (1) the title/abstract/main text is rewritten to more clearly highlight that these results demonstrate that current unlearning methods are simply obfuscating the information, not removing the information, from the networks, (2) the methodology is made more compact, (3) the current results polished and (4) additional supporting results added, e.g., visualizations of multiple metrics confirming consistency of metrics

I feel like the authors have done an admirable job improving the narrative of the paper. I added a few remaining minor suggestions that the authors can optionally integrate, but I'll be increasing my score to an 8.

### Weaknesses
 - Section 3.1’s notation is fine until line 103 introduces “uninformative/unrelated” text. How does one quantify whether the model outputs uninformative/unrelated text? This feels like a very fuzzy notion and one that might be hotly contested in the research community.
- The utility of Table 1 is confusing to me. As I understand, this Table 1 is meant to be an example of how information can be relearned, but it doesn’t communicate any mechanism or intuition. Rather, it just states, “First, here is the original output. Then, here’s the output after unlearning. Finally, here’s the output after relearning.”
- Nit: Table 1: I personally would recommend adding column titles for TOFU and WHP. 
- Table 1 Caption: After reading the section, I realized that Table 1 isn’t a schematic but is a real example? If so, the phrasing of the caption is ambiguous to me. I thought “Example of how keywords unseen … could still be recovered” meant “Here’s a demonstration of what unlearning->relearning would look like”, not “Here is actual data from our experiments”. Perhaps this could be made more clear.
- The same feedback for the Table 1 Caption applies to the Table 2 Caption
- Line 242-243: Citation(s) are needed for gradient ascent in “We unlearn the Phi-1.5 model (Li et al., 2023) using gradient ascent, a common unlearning baseline.” I agree that this is a common unlearning baseline, but pointers to previous work should be given.
- Nit: Line 251: “on the a set of text”
- Figure 3: I might have missed something, but which metric is being visualized as the “Attack Success Rate”? In 3.3, we were introduced to three metrics for the success/failure of unlearning and relearning, and I’m not sure which is visualized in Figure 3. It is thus difficult to know how to interpret these results.
- In Figure 3, since ASR is supported on [0, 1], please increase the colormap range from 0 to 0.8 to 0.0 to 1.0
- In Figure 3, please include Unlearning Steps = 0. I think this is important for understanding what the behavior of the model is before unlearning begins and better contextualizes the changes caused by unlearning and then relearning.
- In Figure 3, please add TOFU and WHP as axis titles. If you’re visualizing these heatmaps in matplotlib, I suggest axes[0].set_title(“TOFU”) and axes[1].set_title(“WHP”)
- I think that the data in Figure 3 might be better visualized as a lineplot: ASR on y, Relearning Steps on X and Unlearning Steps as the hue (including 0 unlearning steps!). I feel the heatmap makes understanding the results unnecessarily complicated.
- Section 4 is light on results. At a minimum, all three metrics should be plotted and included in the paper (either in the main text or appendix). The reader should know whether the results are consistent across the three metrics.
- Figure 4: Please use axis titles to label the models.
- Figure 4: I dislike when two adjacent figures using the same y axis have different y limits. It feels misleading to me.
- Figure 4: I recommend removing one of the two legends; there’s little point in duplicating that information.
- Structurally: I feel like the manuscript would be much more exciting if the results appeared faster than page 5. I felt like Section 2 might be moved to the end and Section 3 made much shorter (with a longer version perhaps deferred to the Appendix). Also Algorithm 1 has very little information but is quite verbose.
- Story: By the end of the paper, I feel like the biggest takeaway is that unlearning hasn’t actually removed the information from these networks but has instead made it superficially inaccessible such that a little bit of the right finetuning can recover that information. If anything, this paper feels like an indictment of the inadequacy of unlearning methods (or perhaps we should call them “obfuscating” methods rather than “unlearning” methods). It’s not clear to me that the title, abstract or story communicates this point. If the authors agree, I strongly urge them to change the title and rewrite the paper to make this clear.

I feel like there is a much more impactful story to be told here using these results, specifically that current unlearning methods are actually obfuscating methods and/or current unlearning methods do not cause the model to unlearn.

**I would be happy to revise my score to a 6 if (1) the methodology is made more compact and (2) the current results polished**

**I would be happy to further revise my score to a 8 if (1) the title/abstract/main text is rewritten to more clearly highlight that these results demonstrate that current unlearning methods are simply obfuscating the information, not removing the information, from the networks, (2) the methodology is made more compact, (3) the current results polished and (4) additional supporting results added, e.g., visualizations of multiple metrics confirming consistency of metrics**

### Questions
- On Line 421, how do you ensure that the unlearned model has 0% success rate in generating Anthony Mark? 
- In Figure 5, should the legend be “Anthony | x” and “Mark | x Anthony”?
- Why are different metrics reported for different experiments in Sections 4 through 6? Can the same 3-4 metrics (the authors mention using 3 metrics, but then report NLL loss in Figure 5) not be plotted for every experiment?

Perhaps two related citations: https://arxiv.org/abs/2401.01814 and https://ai.stanford.edu/~kzliu/blog/unlearning (note, I'm unaffiliated with both)

### Soundness
3

### Presentation
3

### Contribution
4

# Sparse MoE with Language Guided Routing for Multilingual Machine Translation

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Sparse Mixture-of-Experts (SMoE) has gained increasing popularity as a promising framework for scaling up multilingual machine translation (MMT) models with negligible extra computational overheads. However, current SMoE solutions neglect the intrinsic structures of the MMT problem: ($a$) $\textit{Linguistics Hierarchy.}$ Languages are naturally grouped according to their lingual properties like genetic families, phonological characteristics, etc; ($b$) $\textit{Language Complexity.}$ The learning difficulties are varied for diverse languages due to their grammar complexity, available resources, etc. Therefore, routing a fixed number of experts (e.g., $1$ or $2$ experts in usual) only at the word level leads to inferior performance. To fill in the missing puzzle, we propose $\textbf{\texttt{Lingual-SMoE}}$ by equipping the SMoE with adaptive and linguistic-guided routing policies. Specifically, it ($1$) extracts language representations to incorporate linguistic knowledge and uses them to allocate experts into different groups; ($2$) determines the number of activated experts for each target language in an adaptive and automatic manner, according to their translation difficulties, which aims to mitigate the potential over-/under-fitting issues of learning simple/challenges translations. Sufficient experimental studies on MMT benchmarks with {$16$, $50$, $100$} language pairs and various network architectures, consistently validate the superior performance of our proposals. For instance, $\texttt{Lingual-SMoE}$ outperforms its dense counterpart by over $5\%$ BLEU scores on $\texttt{OPUS-100}$ dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose Lingual-SMoE, an MoE model suited to multilingual MT that overcomes limitations of previous work. It features:
1) Has hierarchical gating that leverages linguistic groupings of the languages on which the model is trained.
2) Uses a Dynamic Expert Allocation during training to determine the correct number of experts to allocate to each target language.

They conduct experiments on the OPUS-100 dataset with 16-100 languages, and extensively compare Lingual-SMoE to the baselines.

### Strengths
- The authors did several experiments to justify their design choices and overcome the limitations of previous work.
- I think the Dynamic Expert Allocation technique is intriguing and intuitive, and the results+analysis seem good. (See Questions section, though)
- The authors did extensive ablations on their proposed techniques, and compared to a number of baselines.
- The analysis based on empirical results is also good, and answer most of the questions a reader would have.

### Weaknesses
 - Notation for the baselines is confusing - eg. from saying LS-SMoE or Hybrid-SMoE is not clear which baseline you are referring to - it made understanding the tables cumbersome. I suggest using slightly longer names like Switch MoE or GShard MoE or Hybrid TaskMoE etc (and preferrably organize as a list or table)
- I think you should reframe the language complexity part as language resourcedness. It's not that any language is more or less complex, it's the amount of data available and handling under/overfitting. This will also match all the analysis and description of DEA in rest of the paper.


Some papers to cite:
- https://arxiv.org/abs/2108.05036, https://arxiv.org/abs/2208.03306 - while these papers are for multi-domain setting, I believe these are related in spirit given that they leverage differences in input to allocate experts.
- https://proceedings.mlr.press/v202/chen23aq.html - related to DEA, but for a different purpose


Minor: 
- In figure 5, are medium resource languages and low resource languages mixed up? If not this is counter intuitive and worth elaborating on/doing analysis.

### Questions
- wrt result with DEA added in Tables 1 and 2, do you have any analysis on why adding this is worse on LRLs for OPUS-16,100 compared to OPUS-50 (ie, the trend is reversed)? is, say, the number of experts per low resource language suddenly worse for 16,100? are there outliers for the 50 case? a trend reserval of +/-0.2 is not bad, but this is an order of magnitude reversal of the trend

- wrt Figure 4, is this equally an issue for dense models? (it's known that this is an issue in general, but it is particularly different than dense models?)
- What are the inference implications of your method? I think even theoretical trade-offs and discussion of this would be interesting, since the most related works discuss this extensively

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a modification of sparse mixture-of-experts (SMoE) for multilingual MT that makes routing dependent on language-specific representations (and hierarchical), and automatically adjusts the number of activated experts for each language. These two modifications are introduced to more explicitly allow for grouping by languages based on their similarity, and for allocating experts based on complexity. The new SMoE variant is tested on a range of subsets of the OPUS-100 dataset and compared against various previous SMoE variants. A set of ablations further investigates the functionality of the expert allocation strategies.

Score was raised after author response.

### Strengths
- The hypothesis is convincing and the design of the methods follows the hypothesis and is thoughtfully laid out and is original.
- The set of empirical evaluations and ablations is rich (if one disregards the problems with the benchmark, see below) and sound, aligns well with the hypothesis, and presents the proposed SMoE solution as an empirically successful method and favourable in comparison to other SMoE variants.

### Weaknesses
 - Empirical comparisons:
   - The baseline scores for the Dense model on OPUS100 are much lower than what was reported in previous papers, in particular Zhang et al. 2021 (https://openreview.net/pdf?id=Wj4ODo0uyCF), even though it’s supposed to be the same architecture and training data and evaluation metric. For example, Zhang et al.’s M2O model scores on average 29.27 BLEU, while this paper reports 25.39 in Table 2, analogously for O2M 20.93 vs 19.03. Perhaps I missed an obvious difference in modeling that could explain the difference in results, but it is questionable whether the dense baseline was tuned sufficiently, and the same for all sparse baselines.
  - The prominently discussed results are reported on a subset of the languages in OPUS100 (Table 1), and the two most competitive baselines (ST-SMoE, Residual-SMoE - the two baselines with 100% win ratio) are left out for the full evaluation on all languages (Table 2). This leaves the competitiveness of the proposed solution in a realistically large multilingual setup to be questioned.
- Choice of benchmark: Unfortunately, OPUS100 is designed in such a way that different languages contain data for different domains, both in training and in test sets. This arises from the fact that many low-resource languages are only covered by religious datasets or tech localization datasets on OPUS. Therefore, there is a relatively strong domain interference, where higher resource languages also have more complex and diverse data, and lower resource languages have less complex and more repetitive data. In past work (Kreutzer et al. 2021 (https://arxiv.org/pdf/2110.06997.pdf), this was already suspected to interfere with language-as-a-task modeling), and it also explains why low-resource languages in the aggregated results often have higher avg BLEU than mid-resource languages (cf. Table 2), as they have simpler test sentences with less domain diversity. The effect seems less drastic with the selected subset of 16 languages (Table 1), but this is a less realistic setup in general. 
The similarity between domains can interfere with language hierarchies that are supposed to be modeled here, i.e. data points sampled from distant languages but from the same domain can potentially be more similar to each other than data points from similar languages but different domains. This might blur the linguistics-guided routing visualization in 4.3 - it could be that routing was rather based on domains than languages, or a combination of both. With this dataset, it is unfortunately impossible to tell.
Furthermore, the amount of data per language is therefore not a suitable (sufficient) metric for task complexity or linguistic difficulty as argued in 4.3.
I would strongly recommend the authors to redo the experiments on a domain-controlled multilingual benchmark, such as a combination of WMT datasets across languages, as e.g. in Cheng et al. 2022 (https://arxiv.org/pdf/2203.07627.pdf). It might be a lot of effort, but eventually worth it to present the success of the proposed method with less interference.

### Questions
- [answered] Are the baseline models reimplemented? Are they coded in the same codebase as the proposed model?
- [answered] Can you quantify the similarity of routing patterns within language groups with cosine similarity in 4.3 as you did in Figure 3? Visual inspection is still hard.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel approach known as Lingual-SMoE, aimed at enhancing multilingual machine translation. In contrast to conventional methods, Lingual-SMoE takes into consideration the distinct linguistic features and complexities of various languages. The experimental findings are promising in specific translation directions, as Lingual-SMoE consistently outperforms traditional techniques in multilingual translation tasks. For instance, it exhibits an increase of over 5% in BLEU scores on the OPUS-100 dataset. This underscores Lingual-SMoE's capability to effectively handle translation tasks for various languages, improving overall accuracy

### Strengths
1.	Consideration of Linguistic Characteristics: This approach takes into account the linguistic hierarchy and the complexity of various languages, thus enhancing its performance in multilingual machine translation tasks. The initiative is highly motivated and intriguing in terms of how it organizes models within the MoE framework to match the specific characteristics of language pairs.

2.	Hierarchical Routing Strategy: In order to implement this proposed concept, it introduces a hierarchical routing strategy that takes into consideration language families and token-level information. This results in a more efficient allocation of experts, optimizing the utilization of resources and routing decisions.

3.	Adaptive Expert Allocation: Another noteworthy proposal is the mechanism for adaptive expert allocation, which can automatically adjust the capacity of experts based on the translation difficulty of each language. This helps address issues related to overfitting and underfitting. The method is both intuitive and technically robust.

4.	Empirical Validation: Extensive experiments, carried out on a variety of language pairs and scales, have consistently demonstrated the effectiveness of this approach across different data resources and language quantities. It consistently leads to a significant improvement in performance, particularly on the OPUS-100 dataset.

### Weaknesses
1.	In the paper, the authors claim to address the issues of Linguistic Hierarchy and Language Complexity. The former refers to the categorization of languages based on their language families, while the latter pertains to "grammar complexity" or "language difficulty." However, I believe that the second claim may not be appropriate, as it appears to relate more to the availability of training data rather than addressing the inherent challenges of the languages themselves. Additionally, there is a lack of experiments or analyses to support the claim that their method genuinely considers the intrinsic difficulty of languages. The paper does not provide a clear definition of how language difficulty is quantified or incorporated into their model, making it difficult to assess the validity of this claim. It would be beneficial to see a more rigorous analysis of how the model adapts to languages with varying levels of grammatical complexity, beyond just considering data availability.

2.	In the experiments, for the purpose of fair comparisons between the baselines and the proposed methods, it is recommended that the authors report the sizes of the models. It seems that the improvements may be attributed to the increased number of experts. Therefore, providing and discussing the size of model parameters, along with the computational complexity of the proposed hierarchical framework in terms of training and decoding time, would be beneficial. The paper should include a detailed breakdown of the parameter counts for each component of the model, including the routing network and the individual experts. Furthermore, a comparison of training and inference times with the baseline models is necessary to fully evaluate the efficiency of the proposed approach. Without this information, it is difficult to determine if the performance gains come at a significant computational cost.

3.	Some technical details require further clarification, and I would like to refer to the specific questions raised in the Questions.

4.	There are several typos that need correction, such as:

   - There are issues with citation formats and grammatical agreement in the last paragraph of the Related Work section.
   - In Section 4.2, "Table 1" is incorrectly cited as "Table 4.2."

### Questions
1.	As depicted in Figure 2, how is the difficulty of a language determined?

2.	Based on your findings in Table 1 and Table 2, it appears that your method has demonstrated improved performance in the en-xx language directions. However, the performance in the xx-en language directions appears to be less favorable than previous results, particularly in the context of medium to high-resource translation tasks. Have you conducted a detailed analysis of this phenomenon, or is it possible that your method still has limitations when it comes to xx-en tasks?

3.	Regarding Eq. (2) in Section 3, it is mentioned that \alpha and \beta are empirically set to 0.05. However, in the Implementation Details section, \alpha and \beta are set to 0.98. Could you please clarify whether these refer to the same parameters?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The presented work proposes to add linguistic information into the mixture-of-expert routing process and shows the effectiveness on the OPUS-100 dataset compared to other gating choices.

### Strengths
- Interesting work adding linguistic features and language complexity into the routing behaviour
- Innovative design of an adaptive expert allocation mechanism
- The paper is well written and easy to follow
- Nice ablations for Linguistically Guided routing (Table 3) and the Language Router Designs (Table 4)

### Weaknesses
- **[major]**: Please provide the `sacrebleu` hash that is used for evaluation such that scores can be reproducible
- **[major]**: While BLEU is still widely used, there are now better metrics to use for Machine Translation that correlate better with human judgment as seen in [Results of WMT22 Metrics Shared Task: Stop Using BLEU – Neural Metrics Are Better and More Robust](https://aclanthology.org/2022.wmt-1.2) (Freitag et al., WMT 2022), specifically I'd recommend including chrF and COMET scores.
- **[major]**: One of the key takeaways of [Pires et al. 2023](https://aclanthology.org/2023.acl-long.825/) is that target language specific routing is helpful in the encoder and not only in the decoder and only source language routing the encoder hinders learning. This is true for both shared as well as language-specific decoders according to their experiments (see their Table 1 + Table 5). I think the baseline (1) in the presented work could be improved with two approaches to more closely match their setup by 1) converting the source language routing in the top 25% of encoder layers to target language routing and 2) deploying their proposed dense pre-training approach.
- **[minor]**: Building on top of the previous point, I think even LGR-SMoE could benefit from the dense pre-training as this was also shown to be very beneficial in both [Pires et al. 2023](https://aclanthology.org/2023.acl-long.825/) and [Tricks for Training Sparse Translation Models](https://aclanthology.org/2022.naacl-main.244) (Dua et al., NAACL 2022).
- **[minor]**: The justification on p.7 that (1) performs much more biased towards English doesn't make much sense as the results in Table 1 only include `X` $\leftrightarrow$ `en` scores and OPUS-100 is an English-centric corpus? In any case, adding per language pair scores for all evaluation directions in the appendix would be beneficial for all methods. It might also be worth to have a LS baseline where only the decoder is language-specific for the target language and we do not have any language specific routing in the encoder since this granularity might be too much for the small english-centric OPUS-100 dataset.
- **[minor]**: How big is the inference speed / parameter count / memory consumption overhead from the additional language router? I think some concrete benchmarking numbers would be helpful here.
- **[minor]**: There are no details about the data epochs, are all of the presented models trained until convergence and is it single epoch? How was checkpoint selection done since we likely can see overfitting for some of the lower resource languages in e.g. LS-SMoE?
- **[major]**: It is unclear how the proposed approach influences the zero-shot translation quality and/or code-switched payloads.

### Questions
- p.6: What is $\alpha$ for the Adam algorithm? Shouldn't this be either $\beta_1$, $\beta_2$ or $\epsilon$? (see Table 4 in [Schmidt et al., 2021](https://proceedings.mlr.press/v139/schmidt21a.html)). Also, please cite the original Adam paper accordingly.
- Is the code going to be open-sourced?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

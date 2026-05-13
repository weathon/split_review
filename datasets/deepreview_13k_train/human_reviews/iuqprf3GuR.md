# Data-Centric AI Governance: Addressing the Limitations of Model-Focused Policies

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Current regulations on powerful AI capabilities are narrowly focused on ``foundation'' or ``frontier'' models. However, these terms are vague and inconsistently defined, leading to an unstable foundation for governance efforts. Critically, policy debates often fail to consider the data used with these models, despite the clear link between data and model performance. Even (relatively) ``small'' models that fall outside the typical definitions of foundation and frontier models can achieve equivalent outcomes when exposed to sufficiently specific datasets. In this work, we illustrate the importance of considering dataset size and content as essential factors in assessing the risks posed by models both today and in the future. More broadly, we emphasize the risk posed by over-regulating reactively and provide a path towards careful, quantitative evaluation of capabilities that can lead to a simplified regulatory environment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides the motivation to move from regulating AI models based on characteristics such model size, number of FLOPS per training, or whether or not the model is classified as frontier/foundation. The authors instead motivate us to focus on data, and more important the content of the data and not the size of the data. The logic is, if harmful data is not in the dataset then the model cannot create harmful outputs. So, if people's private data is not in the dataset, then those people's privacy cannot be compromised. 
The main claims are that frontier/base/foundation model are not well defined and the difference between each is unclear, and this makes legislating based on this classification possibly incosistent. Additionally, using FLOPs as a an indication of how powerful a model is, that too is inconsistent because smaller models which take less computation to train can be just as capable.

### Strengths
- Clarity: This is a very well written paper and the arguments are well laid out
- Significance: This is an important area of research for which there are no clear answers currently. Contribution to these discussion are very valuable.

### Weaknesses
Novelty: The importance of the role of data in developing safe and fair AI system is perhaps one of the most documented. Not only in foundation models but in previous deep learning applications.  The idea that in thinking of regulation the field is only thinking about the algorithms and not the data is not a correct assumption; in fact the works the authors cite, on Datasheets by Gebru et. al, those were motivated by the discussions on the importance of data and the contents of datasets in designing safe system. From the datasheets, we have seen Data Nutritional labels by Holland et. al and we have seen many more expansions of these concepts to  applications like Health (Rostamzadeh et. al. 2022) 
One of the strongest points the authors make in their paper is the implications of derivation and summarisation over multiple documents and information sources which are skills unique to the current machine learning models. They mention how these abilities mean that information that is benign in isolation can now be aggregated into unsafe or undesirable model outputs. However, it is not clear what the authors would suggest as a solution to this problem because as they said, each piece of data, in its originating dataset was not harmful, it is the aggregation and derivation that creates harmful outcomes. The threats, especially to privacy posed by aggregation are known (see literature on anonymisation strategies) but perhaps here the authors bring these back up because of the scale at which these models can work. If this is the case, the authors should better support this. If not this, then the only other solution I can think of is that we imagine how our datasets can be combined with other data to create harmful outcomes  -- and I think this is an incredibly difficult ask.
Overall I failed to see the novelty of this work especially with the work from Hooker 2024, in which the arguments against the user of FLOPs are well laid out and keeping in mind all the important work that has gone into the field to convince us on the importance of auditing the suitability of datasets for specific projects.

### Questions
- In this new paradigm of more capable models, what additional characteristics of datasets should be considered for legislation?
- How do we propose people audit their datasets differently to make sure that they are building over safe dataset?
- What do we have to do differently when we build datasets for this new iteration of models?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
- This paper argues that current governance/regulatory debates pay insufficient attention to the role of data, instead focusing myopically on model parameter counts/FLOPs
- It provides three justifications for this argument: 
   - First, there is no consistent definition of “frontier”, “foundation”, “dual-use”, and “general purpose” models. 
  - Second, advances in efficient machine learning means that models require fewer parameters and FLOPs to achieve the same outcomes, resulting in capable models that fall below regulatory ceilings.
  - Finally, the focus on the largest and most compute-intensive models ignores the fact existing, smaller models can be just as capable as their larger counterparts.
- The paper then argues for a dataset-centric approach, and presents experiments highlighting the role dataset size plays in model capability

### Strengths
- The paper is clear in its writing.
- The paper touches on a debate of significance and widespread relevance.

### Weaknesses
 - There’s no novel technical contribution (theory, technical framework, algorithms, dataset). This is a policy position paper, and as such, I think the better venue is a conference/journal with a policy focus. 
- One complaint is that there’s ambiguity regarding certain terminology (e.g., “foundation models,” “frontier,” etc.). But isn’t resolving definitional ambiguity the role of legislatures and courts? Ambiguity is unavoidable–but most countries have enforcement or judicial processes for navigating and resolving it. Sure, the term "foundation model," might be ambiguous now. But if its used in a law, then courts (or agencies) will provide definitional clarity to it. 
- It’s not clear how the paper extends prior critiques of FLOPs thresholds. The points made here seem to be ones made in prior debates.
- The paper suggests that policy debates should instead focus on the role of data. But it isn’t precise about what, specifically, this might entail. And it doesn’t address how governance anchoring in data should be designed. Are the authors suggesting the equivalent of FLOPs thresholds for data? I.e., thresholds based on dataset size? Nor does the paper address the difficulties that arise when designing regulation around data. For instance: how should different types of data be treated? What distinctions should be drawn between human and machine-generated data?

### Questions
See above!

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Summary: This paper is essentially a position and framework paper arguing for new criteria for applying model governance policies (i.e., rules about model deployment, use, etc.). The paper critiques FLOP-oriented frameworks for measuring model size (and more generally highlights a major concern that ongoing AI Governance debates are not even using a shared language). The argumentation in the paper roughly flows as such: current “foundation/frontier” focused definitions are not unified enough, compute is not the primary determinant of capabilities, data is under discussed, and thus future policy discussions should reorient around definitions/taxonomies/criteria-to-regulate that include data.

The paper has a compelling point. The literature that’s engaged with here is reasonably well-selected (of course, given the volume of publications in the LLM and AI Safety space, being opinionated is required here and some readers may be upset about certain omissions). I expect the general policy directions illustrated here to be impactful.

However, the main issue in my view with the current draft is mainly the room for organizational improvement. Revisions that focus on hand-holding the reader about what the contribution is (e.g., should I be turning the page to find empirical experiments with data scaling) and summarizing the core argument could greatly strengthen the impact of this paper. I believe these revisions can be made within a relatively short cycle and am hopeful about this paper. I look forward to reading the next draft. Below, I summarize key feedback for this paper:

### Strengths
Strengths
* The core argument is strong here – I think the paper will successfully convince readers to adjust some of their future behavior (more research/policy along the lines outlined here, more efforts to unify language in policy debates).
* There is a reasonable selection of literature that is discussed. While there is certainly room to discuss more avenues of “data-centric” ML (esp. e.g. economics of data, data as an arena for new kinds of negotiations -- specific examples in the next section), I think the paper already has a very broad scope.
* Building off above, to be clear, I think future versions of this paper can have very high potential impact (i.e., I was convinced that indeed the policy directions here would be very beneficial if adopted).
* If this paper is able to help "clean up" terms in the AI governance community, this will go a long way.

### Weaknesses
Weaknesses
* In the current draft, it is not immediately clear what the kind of contribution is. Is this a framework paper, a position paper, and empirical paper, etc.? By the end of the paper, readers will know, but this could be communicated much earlier on.
  * To be specific, this paper could benefit from a very signpost-style paragraph, sentence, or bullet points in the last paragraph of Introduction that clarifies what new data and experiments are being presented here vs. what new argumentation is being presented.
* More generally, the organization of the paper (especially around the middle) could be improved, even with just some general signposting and clarification of how much of the arguments here are being summarized for the first time vs. presented for the first time. To be specific on this front, the current Section headers do give a nice sense of the topical coverage of the paper but do not clarify what kind of information will be presented in this section (argument vs. experiment vs. synthesis vs ...).
* Venue fit: I could see some readers expecting more of a traditional methods/results organization for the paper. Perhaps some readers would be more impacted by a traditional experiment-focused paper. Personally, I think the best version of this paper need not stick to a very traditional organization structure, but I just wanted to flag that this could be one direction of revision to think about.

### Questions
My main question that arises draws on the above areas for improvement: what is the primary contribution of this paper and what is the key narrative you’d like to see researchers take away vs. what should policymakers take away?

Building off the above references (influence, data deals, data as leverage), to what extent does future progress on training data influence measurement techniques, new practices around "data deals", new practices around data-related collective action (e.g., action by artists or writers) affect the framework you've constructed here?

If successful, can a data-based framework replace most discussion of compute governance? Should we be working towards some kind of hybrid?

### Soundness
3

### Presentation
2

### Contribution
4

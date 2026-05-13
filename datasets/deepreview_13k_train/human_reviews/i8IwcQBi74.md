# Interpreting Language Reward Models via Contrastive Explanations

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
Reward models (RMs) are a crucial component in the alignment of large language models' (LLMs) outputs with human values. RMs approximate human preferences over possible LLM responses to the same prompt by predicting and comparing reward scores. However, as they are typically modified versions of LLMs with scalar output heads, RMs are large black boxes whose predictions are not explainable. More transparent RMs would enable improved trust in the alignment of LLMs.
In this work, we propose to use contrastive explanations to explain any binary response comparison made by an RM. Specifically, we generate a diverse set of new comparisons similar to the original one to characterise the RM's local behaviour. The perturbed responses forming the new comparisons are generated to explicitly modify manually specified high-level evaluation attributes, on which analyses of RM behaviour are grounded. In quantitative experiments, 
we validate the effectiveness of our method for finding high-quality contrastive explanations.
We then showcase the qualitative usefulness of our method for investigating global sensitivity of RMs to each evaluation attribute, and demonstrate how representative examples can be automatically extracted to explain and compare behaviours of different RMs.
We see our method as a flexible framework for RM explanation, providing a basis for more interpretable and trustworthy LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The work proposes looking for counterfactual (CF) and semifactual (SF) examples to explain reward models. They prompt language models in a two-stage manner, where an LLM is required first to identify words related to a list of attributes and then to perturb these words to flip the reward prediction. Quantitative experiments examine the CF and SF discovery success rate (CF and SF coverage) and reveal the proposed method mainly improves CF coverage at the cost of compromise in SF coverage in some cases. Perturbed sentences in the proposed method also have a lower syntactic and semantic distance to the original sentence. Some qualitative analyses are also done.

### Strengths
1. A novel prompting-based counterfactual and semifactual example generation method for explaining reward models
1. Experiments do show some merits of the proposed method, such as generally improved CF success rate (CF coverage).

### Weaknesses
1. The work's main motivation, "More transparent RMs would enable improved trust in the alignment of LLMs," is mostly intuitive and needs more explanations. Even if reward models are totally transparent, how they translate to more transparency in the trained policy model is still not clear, as the policy LLM is still a black box model. Math question training data, as an extreme case, often comes with a more rigid threshold of logical consistency in its data and does not translate to improved reasoning transparency of trained LLMs on that data.

2. How the constructed CF and SF examples are "minimally perturbed" and "maximally perturbed" ones are less reflected in the construction method. Did the authors encourage LLMs to increase/decrease the perturbation ratio on an example until they cannot anymore?

3. The perturbation method relies on a subjectively defined list of categories, which limits the scope of explanation in reward model behaviors. The reward model could vary its prediction due to other factors that humans might not think of, which poses a larger threat to its trustworthiness.

### Questions
1. Are there any messages we can take away from the qualitative analysis to improve the trustworthiness of reward/policy LLMs? Existing findings are more or less trivial and superficial, and it would be better to provide more insights that either deepen our understanding of reward models, or improve transparency of policy models.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a two-step approach to generating diverse perturbations of language completions, and show that this method can be used to improve the diversity of contrastive explanations of reward model outputs.  (i.e., perturbations that result in pairs of counterfactual or semifactual paired completions that can then be used to explain a reward model's behavior). 

They validate their approach both quantitatively and qualitatively and show how it can give insights into reward model behavior, including the sensitivity of the reward model to perturbations along a set of specified axes, both at a local and global level.

### Strengths
I am not very familiar with the XAI literature or its application to reward models, but I have not seen this particular approach before and believe the methodology is novel (but see weaknesses for some requests on related work). I think researchers who work with reward models will generally be interested in ways of explaining the reward model predictions, and so I believe the topic and proposal in this paper meets the significance threshold for a major conference (but see weaknesses re: chosen RMs). 

Overall the paper was well written, and the figures are generally high quality, so I believe it has sufficient writing polish for publication. See weaknesses for some nits. 

While the method itself is relatively straightforward (the authors cite a couple works that have done similar things in other contexts), it is demonstrated to be effective. The experiment design is appropriate, and the authors are testing the right things. Despite the limited RMs tested and the use of binary preference reversals (pref flip rate) instead of cardinal rewards (see weaknesses), I believe the method itself is reasonable, and the experiments provided sufficient support for the approach.

### Weaknesses
Related work: At lines 179-181, a few related works are mentioned that could alternatively do perturbations or CFs for reward model explanations. These are not expanded upon in the text, and they do not seem related to the baselines at lines 277 - 284. Is this because they do not apply at all, or how do the baselines relate to past work? This casts some doubt on how the present work fits into the literature. 

Conceptual: It seems the finite attribute list limits the kinds of explanations that the proposed method can provide. For a given part of completions it seems possible that an attribute that doesn't quite relate to some of the listed attributes (or related to multiple listed attributes) would be the main causal factor. For example, one completion might be preferred because it uses a more clever metaphor than the other completion. I'm not sure how this would fit in any category, and it seems like perhaps a dynamic approach or wildcard attribute might be better in some respects (I realize this might conflict w/ the experiments that rely on ranking attributes). 

Conceptual: It's unclear to me why we would prefer Preference Flip Rate (PFR), which is an ordinal measure, to the cardinal measure provided by the rewards themselves. For comparability when rewards are of different magnitude, you can always normalize by either the mean reward, or the gap between chosen and rejected. A cardinal approach seems strictly superior to me, and no real justification is provided for considering CF/SF to cardinal shifts in rewards (I would wager than the authors use flips because of the prior work that generates CF/SF contrastive explanations).

Significance: The tested RMs are all extremely small / poor by today's standards, and would not be used in any real context. 7-8B parameter RMs are many times stronger and more relevant, and are easily runnable on a single 24GB GPU, so I would not expect there to be a compute barrier here. So it's not clear to me that the positive results obtained for these RMs will carry through to modern ones. This limits the present significance of the results, and I would strongly encourage the authors to run experiments with one or more stronger RMs. 

Nits:
- L419/420 mejntions that you compare global/local rankings--- are there supposed to be results for this, or is this just to produce the Figure 4 example
- Figure 4 caption could be significantly improved. It took me a second to figure out how to read it / what it was presenting (mind you, I was reading in black and white so couldn't see the color difference between the dashed lines, but it would still be good to explain them in the caption).

### Questions
Please see weaknesses. The significance one would provide the largest improvement, but perhaps hardest to address. The related work one should be easy to address and therefore high ROI.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an analysis technique for reward models. By perturbing input examples with LLMs along pre-determined attributes to generate counter-factual (CFs) examples (that flip the preference judgment of a reward model by modifying an attribute) and semi-factual (SFs) examples (examples that retain the label despite editing an attribute), the authors are able to obtain quantitative (robustness to perturbation) and qualitative (which attributes are important to the preference judgment) signal about reward model judgments.

The main contribution is the analysis technique itself, with experiments comparing the quality of CF/SFs generated by the proposed prompting technique against baseline methods of perturbation to demonstrate the quality of explanations generated, and a case study comparing three open-source models to use the method to identify differences in their performance qualitatively.

### Strengths
1. The proposed technique is clean and simple, draws from existing literature on SF/CFs in XAI, and importantly is general enough to work for any RM (L.132-134), making it a useful tool for analysis. This is particularly the case when you might not have access to the training data of some black-box RMs and can yet obtain qualitative insights on their performance. 

2. The main contribution is the analysis technique. Section 3 makes a good case that the proposed prompting technique is an effective way to generate good CF/SFs and Section 4 then shows how this can be used to interpret RM behavior. The flow is easy to follow and the experiments validate the authors' claims. 

3. L.405-411 - The experimental setup chosen for Section 4.1 is clever because we have ground truth knowledge that the Deberta-v2 reward model was the only one trained on the _harmless_ dataset, so it is more sensitive to perturbations that change the 'harmless' attribute. This validates that the behavior identified by the proposed analysis technique is 'correct' in this case. A very interesting follow-up would be introduction of perturbation attributes that are not directly related to the training task of the RM, and then this technique can identify biases in model performance.

### Weaknesses
1. While the experiments generally back up the claims made, I think there is scope to more rigorously test the robustness of the proposed technique. See Q2, 3, and 7 below for specific concerns. Another concern is that the generation method for attributes looks at examples from the test set. This is fine, but it grounds the perturbations to 'expected' ways and doesn't elicit any 'surprising' biases from RMs. This is easily remedied of course, simply by sampling attributes along different ways, but it would be interesting to see if the generated SF/CFs are sensitive to the attribute distribution.

### Questions
1. L.42 - Can you clarify the distinction to (Zeng et al. 2024) and (Park et al. 2024)? My understanding is that these papers make directed perturbations based on a specific attribute, while the proposed technique looks to analyze model performance via a set of targeted perturbations (SF/CFs). I don't see this as a weakness per se, it's more that L.59 mentions that there have been no XAI techniques explored for reward models but the way L.42 has been written contradicts this.

2. One unanswered point is about the sensitivity of the analysis technique to the choice of LLM used to generate CF/SFs. Here the authors use GPT-4o. I think it is important to test because the main contribution is the analysis technique itself, so we should ablate the sensitivity to other (less powerful/open-weight) LLMs since not everyone might have access to GPT-4o. 

3. L.186 - Can you comment on the sensitivity of the method to the selected high-level evaluation attributes? Are there patterns of evaluation attributes for which the generated CF/SFs are less effective at flipping the label - in these cases, how do we decide if this is because the RM is robust to perturbation along this attribute or if the LLM generating the counter-factual is not able to correctly edit the response based on that attribute. 

4. L.262-265 - In addition to the fraction of test comparisons where at least one valid CF/SF is found, why not differentiate between cases where multiple valid CFs exist as examples where there is more brittleness in the RM?

5. L.706-706 - This method to elicit attributes from the test set is similar to techniques that use LLMs for qualitative coding so it might be helpful to ground the method in similar works [1,2,3].
[1] Xiao, Ziang, et al. "Supporting qualitative analysis with large language models: Combining codebook with GPT-3 for deductive coding." Companion proceedings of the 28th international conference on intelligent user interfaces. 2023.
[2] Dai, Shih-Chieh, Aiping Xiong, and Lun-Wei Ku. "LLM-in-the-loop: Leveraging Large Language Model for Thematic Analysis." Findings of the Association for Computational Linguistics: EMNLP 2023. 2023.
[3] Chew, Robert, et al. "LLM-assisted content analysis: Using large language models to support deductive coding." arXiv preprint arXiv:2306.14924 (2023).

6. In Table 1, is there a reason for the drop in performance between the coverage on CF and SFs that were generated perturbing 'Both' responses than just "Chosen" or "Rejected"? Uniformly these scores are lower.  

7. Regarding the qualitative analysis in Section 4, it might be interesting to introduce some 'control' attributes that are not meant to flip the label of the plot to provide some context to the 'treatment' attributes selected. For instance, I imagine Fig. 3 would be improved with such additional attributes, and I imagine if an RM flips a label on these attributes, then it's a method to identify biases in the judgments. 

8. L.324-326 - While it is understandable that the generated CF/SFs are more similar to the original response which likely costs diversity, I think you have a better justification for the method, than the using of the 15 different attributes is just pure efficacy i.e. the prompting method generates valid CF/SFs at a higher rate than the baselines, this itself is sufficient.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the interpretability of reward models through contrastive explanations. It proposes a novel pipeline of getting high-level attributes, computing meaningful textual perturbations, and categorizing into counterfactual (CF) and semifactual (SF) explanations. Then it performs case studies on how to use the CFs and SFs to interpret reward model decisions.

### Strengths
Overall i like this paper!
* The problem of RM interpretability is important.
* The whole pipeline of generating CFs and SFs make sense
* The case studies demonstrate the usefulness of the generated explanations very well

### Weaknesses
 * I am a little skeptical of the high-level attributes concluded by the model. The attributes are generated per sample, and then aggregated to find the top attributes. Then does the LLM give consistent attributes (e.g. do they consistently use the exact word of avoid-to-answer?)? Even if an attribute shows up in LLM's summarization for many samples, does it always mean the same thing (e.g. attribute complexity might mean good/bad things)?
* Does the prompting in step 2 always work as intended? In Fig 4, it seems some responses are modified almost completely --- does it mean the LLM doesn't faithfully follow step 2 prompt of only modifying the identified word?
* Step 2 prompting requires the modification to be both better/worse, and also better/worse in terms of targeted attribute. Why do we still need the first condition?
* Are there more compelling evidence for the usefulness of the paper? E.g. some reward models with known issues (e.g. length bias), and the generated data can identify that?

### Questions
I put my questions in the weaknesses

### Soundness
3

### Presentation
3

### Contribution
4

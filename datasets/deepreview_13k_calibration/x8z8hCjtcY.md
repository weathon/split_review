# Elephant in the Room: Unveiling the Pitfalls of Human Proxies in Alignment

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
The demand for regulating the behavior of large language models (LLMs) has ignited research on alignment algorithms, the essence of which is to align LLMs' generations with human preferences. Due to infeasibility of humans directly participating in the training or generation of LLMs, existing alignment algorithms choose to align with human preferences carried by proxies, i.e., preference data or reward models. However, whether these human proxies faithfully represent human preferences remain under-explored. We categorize human proxies into two levels based on the degree to which they directly embody human preferences: Level-1 Proxy (preference data) and Level-2 Proxy (reward models). We empirically examine the faithfulness of both levels of proxies and its impacts on alignment performance.
We notice that current algorithms tend to overlook the faithfulness of these proxies in reflecting human preferences; many works even directly use reward models as their automatic evaluators without any correlation verification. Current literature of alignment overly focuses on optimizing algorithms, rendering the faithfulness of human proxies an "elephant in the room"—something extremely important yet largely overlooked. According to experimental results, we unveil potential risks of using inferior ``human proxies'', aiming to arouse attention to this huge ``elephant'' in alignment research. We summarize existing pitfalls from different angles and provide a re-labeled preference dataset and insights about reward model usage to facilitate the healthy development of alignment\footnote{This work contains examples that potentially implicate stereotypes, associations, and other harms that could be offensive to individuals in certain social groups.}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper claims to be a an analysis of the role of human preference proxies (direct preferences and reward models) in LLM alignment. The authors do qualitative analyses of the errors in a commonly used alignment dataset and re-label it. They then show that this leads to a significant gain in alignment scores for both DPO style algorithms and PPO-style reward model + policy learning.

### Strengths
It is true that practitioners systematically under-account for the effect of annotation noise in preference-based alignment / RLHF. annotated data is frequently taken as ground truth, and there is less data cleaning performed than there should be.

The revised dataset could be an additional resource for the community.

### Weaknesses
After having gone through the paper, it seems the main contribution really boils down to a re-labeling of the (widely used) HH-RLHF dataset. While this will make it a useful resource, it is unclear to me what the scientific value of the work is. It is entirely expected that re-labeling the dataset to reduce noise, should improve accuracy on the downstream tasks.

What further insights are gleaned by this exercise? There is an inventory of the data labeling losses which are mildly interesting. However, the authors give absolutely no information about the labeling process. So what can a reader takeaway that is useful? let's grant that the downstream results indicate that the labeling process of this paper is better than the labeling for the original dataset, how do we know why?
Was the entire dataset re-labeled by the authors? this is not a process that can scale to other problems, were lower quality raters still need to be used. The inventory of "pitfalls" may be helpful but it is unclear whether the categories and proportions will generalize to other datasets/ domains.

The discussion section 5 does not seem to add any new insights not familar in the literature. 5.1 is more of a related work section (very minimal) and 5.2 goodharts law is well known and not quite relevant to the work done here.

This paper feel like a better fit for a conference like Findings'EMNLP.

### Questions
line 239: DPO is not really an SFT method. it is a simplfied form of RLHF.

line 365: should it be such as 1-0 metric, or something that takes into account the magnitude of the difference between the rewards.

line 377: for DPO, are you computing the impliicit reward that the DPO derivation uses (Ratio of log probs) ?

line 455 - 463: This finding if it can be replicated in other settings would be quite interesting (that reward accuracy during training is not reliable).

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores the challenges of using human-made proxies, like labelled data and reward models, to align large language models (LLMs) with human preferences. The authors find that these proxies often don’t accurately reflect genuine human values, which can lead to unintended model behaviours. Therefore, they re-labelled a popular preference learning dataset (HH-RLHF) to create a cleaner version, called CHH-RLHF, which they hope will support more reliable alignment. Their experiments show that better proxies lead to improved alignment, but they caution against relying too much on any single measure, as it can be over-optimized and lose accuracy. The authors urge researchers to prioritise verifying proxy reliability to prevent these hidden risks from undermining model alignment.

### Strengths
- The paper's classification of human proxies into two levels (direct preference data and reward models) offers a clear framework. This seems simple but is actually very **novel**. This is the first time I have ever seen such a classification.
- By re-labelling the HH-RLHF dataset and providing a cleaner version (CHH-RLHF), the authors make a very practical contribution that could improve the reliability of the preference learning dataset.
- By discussing Goodhart's Law, the paper raises awareness of the risks of over-optimizing proxies. This is indeed important for us to keep in mind: alignment isn’t just about maximising scores but ensuring genuine alignment with human intent.

### Weaknesses
 - The paper's classification of human proxies into two levels (direct preference data and reward models) offers a clear framework. This seems simple but is actually very **novel**. This is the first time I have ever seen such a classification.
- By re-labelling the HH-RLHF dataset and providing a cleaner version (CHH-RLHF), the authors make a very practical contribution that could improve the reliability of the preference learning dataset.
- By discussing Goodhart's Law, the paper raises awareness of the risks of over-optimizing proxies. This is indeed important for us to keep in mind: alignment isn’t just about maximising scores but ensuring genuine alignment with human intent.

- “This work aims to alert researchers to the importance of verifying human proxies before using them, whether for alignment optimization or evaluation.” Several research papers discuss this issue, with reward over-optimization being one of the most well-known. This topic has been widely discussed.

- Relabeling HH-RLHF is valuable, but the quality of the HH-RLHF dataset is somewhat criticized in the community. The more important question is how we can collect user preferences in a scalable and reliable manner rather than simply re-labelling them. This paper is valuable for providing a re-labelled dataset, but in my opinion, it does not meet the standard of ICLR.

- “However, they only establish a leaderboard for reward models, failing to reveal the relationship between alignment performance and reward model quality.” I agree, and it’s already been discussed in the community that achieving a higher score in RewardBench does not necessarily translate into better downstream task performance. How do the authors of this paper address this issue?

- Table 3 is not convincing, as Figure 4 already shows that “Starling-34B” provides a better score. Why not use 34B? Instead, a 6.9B model was chosen. I wouldn’t consider this a pitfall; experiments clearly indicate that a larger base model performs better.

- In Figure 5, all models are using 6.9B or 7B reward models: why not use the 34B version?

- As the authors have already empirically shown that a better reward model leads to a better policy model, where is the pitfall?

### Questions
- Where is the re-labeled preference dataset?

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
4

### Summary
This work explores the various complexities of alignign to human preferences, considering both the more direct capture of human feedback data as a preference proxy, and the one step removed reward model representation of human preference. It provides various experimental insights into how faithfully these reflect actual human preference. The authors analyze and provide a cleaned version of HH-RLHF, and use this as a basis for further analysis.

### Strengths
The high opposite re-label rates for HH-RLHF are insightful and highlight various issues with working with depending heavily on such datasets. In this setting, three of four annotators choose the rejected response as better, highlighting critical issues with the dataset.

The experimental design, discussion and framing are insightful. Experiments such as the correlation between human and model evaluations are particularly valuable.

### Weaknesses
The high opposite re-label rates for HH-RLHF are insightful and highlight various issues with working with depending heavily on such datasets. In this setting, three of four annotators choose the rejected response as better, highlighting critical issues with the dataset.

The experimental design, discussion and framing are insightful. Experiments such as the correlation between human and model evaluations are particularly valuable.

The DPO experimental settings are clear, in terms of training on both the original HH-RLHF and improved CHH-RLHF datasets. However, this is unclear for the PPO setting and even on re-reading, I am unsure which results (if they exist) show the comparison between the effects of RMs trained on HH-RLHF vs CHH-RLHF on downstream LLM performance evals. If these experiments have not been run, I would strongly recommend running them as they would speak to the impact of the massive effort to re-label/clean up this data. If this is not possible due to resource constraints, I'd recommend discussing this in detail.

Overall, this is thorough work which is will motivated and has involved important and substantial effort, both in terms of the CHH-RLHF annotation and experimental design, much of which is extremely insightful. I feel that currently, the poor framing of the work within the context of existing critical investigations of the space and lack of clarity around the overall narrative limit the work's potential impact. Both these points can be addressed to make this a potentially high impact contribution.

### Questions
- grammar L084: If not, what impacts they may have on alignment performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper raises an important question on whether current day alignment datasets are truly representative of human preferences. To address this question, the authors study to abstractions of human preferences - "Level-1 Proxy" (aka training data) and "Level-2 Proxy" (reward models).

Starting with Level-1 Proxy: The authors use HH-RLHF, a popular dataset, and offer a taxonomy to categorize the training data (Section 3.1), such as toxic responses, "inverted" responses (ie, the rejected response is actually better than the chosen respose), etc.
The authors then carefully re-label HH-RLHF using 4 human annotators, and find that a large chunk of the data falls under the above pitfalls.
Re-training on the cleaned data (CHH-RLHF) using DPO, they demonstrate immediate improvements in the model's "reward score" (Section 3.2.2, Table 2).

For Level-2 Proxy: The authors then study the impact that a reward model can have on the alignment process. Similar to Level-1, the authors start with a taxonomy of pitfalls (Section 4.1.2). However, if I understand correctly, the taxonomy does not seem to be used anywhere? (Ex:, “Score for Empty Responses” indicates when a reward model gives high scores to an empty response – how often does something like this happen?)

The authors then claim that current reward models are not adequate enough to be used for training aligned models (Section 4.2).
The authors define an accuracy metric to define the quality of a reward model, and assess a wide range of reward models (Table 4), demonstrating a wide range of accuracy scores.
The authors study the impact that a reward model can have on alignment algorithms - PPO and PRO – and find that suboptimal reward models lead to suboptimally aligned models.

### Strengths
* The re-labeled dataset CHH-RLHF is definitely a contribution for the community. 
* The authors do an exhaustive list of experiments, although it is not clear how the set of models chosen for each experiment was decided on.

### Weaknesses
 * My biggest question is what new information have we learned from this? I believe that the takeaways are that better data leads to better models, and better reward models lead to better aligned models. While a cleaned dataset is a contribution worth applauding, I don’t think there is anything else that the paper offers that we didn’t already know.

* The authors have a wide range of empirical results - but it is not clear how the choice of models used for each experiment was made.

* Figure 4: The authors claim that Starling-34B’s evaluations show good correlation with human evaluations (But is missing a correlation score?), and also shows that Starling-34B has the highest reward model accuracy (Table 4) and using Startling-34B as a reward model leads to a better model (Figure 6). Doesn’t this go entirely against the authors claim that current day reward models (level-2 proxy) are inadequate? 

* Table 4: I don’t think assessing DPO for reward modeling is reasonable. There seems to be an assumption being made that the policy model from DPO would also serve as a good reward model – and the authors justify this assumption with the paper title of DPO (“Your language model is secretly a reward model”) – I don’t think this is reasonable, especially because prior work shows that policy models learn very different things from reward models (https://arxiv.org/abs/2405.19534).
The reason I mention this is that if you take out the DPO results in Table 4, the claims that the authors make (ie, reward models often do worse than 50/50 chance) is significantly weakened. My takeaways from Table 4 is that larger models lead to better reward modeling accuracy, and larger models (Starling-7B, 34B) do not seem to have the issues that the authors discuss.

### Questions
* Some details on HH-RLHF would be helpful. Datasize? How was it originally annotated? 
Ie, in Figure 3, when 0.07% is said to be “Empty” – how many samples is that? 

* Figure 4 – why did you include GPT-J? Also, how big of a model is GPT-J?
* Figure 4 - why is there no correlation score?
* Does the newly labeled data include annotations from all 4 annotators? If you have already gone through the effort to re-label the data, having this more granular information could allow for better alignment methods as opposed to binary (preferred vs. rejected) labels.
* What is the purpose of Figure 5?

### Soundness
3

### Presentation
2

### Contribution
2

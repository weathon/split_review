# Measuring And Improving Persuasiveness Of Generative Models

- Decision: Accept
- Scores: 3, 6, 8

## Abstract
Large Language Models (LLMs) are increasingly being used in workflows involving generating content to be consumed by humans (\textit{e.g.}, marketing) and also in directly interacting with humans (\textit{e.g.}, through chatbots). The development of such systems that are capable of generating verifiably persuasive messages presents both opportunities and challenges for society. On the one hand, such systems could positively impact domains like advertising and social good, such as addressing drug addiction, and on the other, they could be misused for spreading misinformation and shaping political opinions. 
To channel LLMs' impact on society, we need to develop systems to measure and benchmark their persuasiveness. With this motivation, we introduce \textbf{PersuasionBench} and \textbf{PersuasionArena}, the first large-scale benchmark and arena containing a battery of tasks to measure the persuasion ability of large language models automatically. %
We introduce \textbf{transsuasion} (trans = carrying across, suasion = the act of persuading), a novel task of transforming non-persuasive language into persuasive content while preserving other factors determining persuasiveness (sender, receiver, time, and channel). %
To construct data for transsuasion, we leverage \textit{natural experiments} in the form of a pair of tweets from the same user, posted in close temporal proximity, with similar semantic content but divergent wording and significantly different like counts. Given such pairs, we investigate to what extent LLMs know and leverage linguistic patterns that can help them generate more persuasive language. Our findings indicate that the persuasiveness of LLMs correlates positively with model size, but smaller models can also be made to have a higher persuasiveness than much larger models. Notably, targeted training using synthetic and natural datasets significantly enhances smaller models' persuasive capabilities, challenging scale-dependent assumptions. 
Our findings carry key implications for both model developers and policymakers. For instance, while the EU AI Act and California's SB-1047 aim to regulate AI models based on the number of floating point operations, we demonstrate that simple metrics like this alone fail to capture the full scope of AI's societal impact.
We invite the community to explore and contribute to PersuasionArena and PersuasionBench, available at \url{https://behavior-in-the-wild.io/measure-persuasion}, to advance our understanding of AI-driven persuasion and its societal implications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a dataset and benchmark for measuring Persuasion. Both PersuasionArena and PersuasionBench measure _transsuasion_, a task that involves independently increasing a message’s persuasiveness without changing the underlying content or message. The authors source their dataset through a set of naturally occurring tweets that differ in likes. Finally, the authors outline results across a large range of both generative and predictive tasks; and train models to identify and generate transsuasive text.

### Strengths
The paper has several strengths. The authors 

1. carefully evaluate a range of models—across both vision and language.
2. leverage online communities and real-world feedback to curate a dataset.
3. will release a dataset of minimally different tweets, alongside metadata and an evaluation setup.

### Weaknesses
My first concern is that small changes in the input can yield significantly different meanings that cosine similarity or edit distance may not capture.

Consider the Converse example in Figure 1: using an entirely different _brand_ is probably more likely to have a big effect on persuasiveness—but not because of something the writer can control. I worry that the “minor tweet edits” often have larger semantic variation: a single brand name will significantly affect popularity (as a more extreme example, a model optimizing persuasivness might always prefer to generate “iPhone” or “Andriod”—even if the brand or seller can only sell one or the other)

My second concern has to do with some clarity on timing. It may be that certain times are just more active. Twitter has a cyclic activity pattern that peaks at specific times. This likely has a confounding effect on tweets that appear even hours apart. How did the authors control for these confounds? I see that the authors did some analysis in Table 5; and that some of the p-values are indeed < 0.05. How exactly was this analysis done? I'm trying to interpret the correlation coefficient.

My final concern has to do with general clarity: I found it a bit challenging to navigate the tasks outlined in the paper. I generally feel like there was more emphasis on creating many tasks instead of focusing on a few very important ones. More generally, I worry that focusing on many tasks detracts from the contributions of the dataset. For example: clustering the tweets, running some kind of topic analysis, or highlighting the types of domains the dataset consists (in the main paper) would provide more value than an additional task.

### Questions
A handful of questions can be addressed alongside the weaknesses.

Why call (1) simulative and not predictive? I feel like prediction and generation are more natural contrasts. In general, it was a bit difficult to parse through the tasks in S3. I think a segmentation between tasks that require classification v.s. generation would help clear up the structure. For example, I see why 2.2 is under generative capabilities—but seeing “simulation” in the name may cause unnecessary confusion.

Relatedly, do the authors mean NLG evaluation (line 322) instead of NLP evaluation? Where G = generation? 

Minor: I think NegotiationBench has a lot to do with persuasion. 
https://arxiv.org/pdf/2402.05863 may be relevant.

Dataset and Error Analysis: While the authors spend some time outlining tasks and evaluating models, I would’ve rather preferred a topic analysis on the kinds of tweets in the dataset—to get a feel for what is “more persuasive” across specific domains. 

How should I interpret the topline not being the “best” model? Are the models generating samples with “super-human” persuasion? Or is there some test leakage given the oracle was trained on the full dataset? I think an analysis of what the samples look like in this case would be great.

A final question (minor question): the setup of T1, T2 pairs reminds of an RLHF-esque setup. Why didn’t the authors pursue a “reward model” paradigm?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to measure LLM’s persuasiveness. The authors first collect a large-scale dataset from X from corporate accounts where similar messages with difference in details lead to very different levels of engagement. They then conduct experiments focusing on two separate but connected aspects: 1) the ability to simulate: to evaluate the effectiveness of a message 2) to generate: to either generate brand-new messages with the requested account, time and engagement level. They then conduct experiment with a few LLMs, both 0-shot and few shot, as well as fine-tuning a 13B model, which outperform much bigger models. They also conduct experiment showing that even expert humans are not that good in judging how a message would perform.

### Strengths
This paper is well-motivated and the authors engage with literature from psychology. The methodology of the dataset collection is very good – the authors make use of similar content posted at different times and the differential engagement level as a signal. Unlike some other recent work in this area, the authors conduct a large amount of validation about some aspects of the paper (e.g. how well do human expert do; human-evaluation of the persuasiveness; how much transfer across domain there is between X post and other domains). The main result (Table 2&3) is clear and convincing. Overall, the scale of this benchmark and the naturalistic setting makes it appealing.

### Weaknesses
1) **Conceptual Framework and Claims:**
The paper's framing of "persuasion" is problematic and potentially misleading. The study effectively measures social media post performance prediction and generation, not persuasion as defined in psychological literature. This measurement error also undermines the paper's conclusions about regulation and broader implications. Therefore, I would recommend the authors to reframe the work as a study of social media engagement prediction/generation without overclaiming about persuasion capabilities. Trust me, it is still a valuable paper.    

***

2) **Literature Coverage:**
While the level of engagement with some aspect of the literature is good, I am afraid there is some notable omissions, for example, the whole field of computational argumentation from the NLP community, especially argument quality? I would also encourage the authors to engage more with relevant literature when making claims. For example, there are several places in which more citations would be good to have (e.g. Line 417-419, https://arxiv.org/abs/2406.14508; Line 292-295, https://arxiv.org/abs/2404.00750) 
***

3) **Structural and Presentation Issues:**
Additionally, the presentation of this paper is somewhat confusing. I had to go through the paper quite a few times and reread things all over the place to grasp what is actually happening. 
To be concrete:

a) it would be great if you could have a separate section on related works, rather than embedding it in the intro.

b) it would be great to include a figure of the tasks you are actually measuring (e.g. BS, CS-CT). 

c) there is a lack of qualitative result. While the numbers certainty indicates your fine-tuned model drastically lead to higher score in evaluation metrics, could you show paired examples, perhaps in the appendix, as to how exactly the model behave, before vs after fine-tuning, to let the reader contextualize the change in numbers? 

d) I am of the opinion that the things starting line 352 (“Extent of Transfer of Persuasive Skills) are more like robustness checks and are not directly relevant to the main benchmark? Perhaps this would then give you enough space to take a deeper dive in the main results, which is somewhat rushed? 

e) I think perhaps “observational data” would be a better term to use than “natural experiment”? 

f) Please move the ethics section to the main paper (which gives you 1 page that doesn’t take up page limit). The ethics of this study is way too important to be somewhere in the appendix 
***

4) **Minor:**
A few minor stylistic things (e.g. line 334, double brackets, try using perhaps square brackets for one pair?)

### Questions
**General Question:**

1) Is there any risk of data contamination? I.e. could the LLMs have seen sense tweets as well as their engagement numbers already?

2) Conceptually, where do you think the performance ceiling is? How far can we get in maximizing the persuasiveness of a message? 

3) I believe it is still Twitter policy that only Twitter ID can be shared publicly. However, given the exorbitant amount they currently charge for API access to hydrate the tweets, how do you plan on releasing the data you collect?

**Regarding the specific claims in the paper:**

4) Line 296-298, “…measures a model’s capabilities to simulate behavior over (future) time unseen during the training.” But is this future time within LLM’s pretraining knowledge cutoff or not?

5) What is the oracle model in Table 2?

6) Why do you use Vicuna 1.5 13B to finetune? 

7) Even though you claim that the time gap between paired posts is not that important (e.g. Table 6), but that table itself seems to show statistically significant correlation for some accounts between like difference and time difference? 

8) Line 480-482 “LLaMA-3-70B, while being significantly smaller than GPT-3.5 and GPT-4, has a higher persuasiveness.” – I am afraid I am not following where you get this conclusion?

9) Around line 847-849, “their KPIs. Table 4 shows the results of this study. We
observe that despite being experts in marketing, the budget allocation by these marketers had almost no correlation with any of their key performance indicators.” -> I am not sure if 0.207 is “no correlation”?

10) Line 1431-1437: I think T1 and T2 here are actually semantically quite different? Could you mention how many pairs are like this where one version of the post actually contains much more information than the other one? This undermines your data collect regarding “matching” posts, right?

11) Line 1545-1555: Do you think it would be better if you define what low/medium/high actually means for the LLM in the prompt? I think perhaps there’s a potential of underestimating 0-shot model performance due to this?

### Soundness
3

### Presentation
1

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
This paper tackles the challenge of evaluating, generating, and transforming persuasive messages. Based on a large volume of tweets, the authors constructed pairs of messages—one more persuasive than the other—to create the PersuasionBench benchmark. Additionally, the paper introduces PersuasionArena, an evaluation platform to measure the effectiveness of persuasive messaging. Together, these resources provide a foundation for systematically assessing and enhancing language models’ capabilities in generating and adapting persuasive content.

### Strengths
- The method for collecting pairwise data is both interesting and scalable. The authors apply a rigorous filtering process, resulting in a dataset with substantial potential for future research in persuasive language modeling.
- The paper presents a diverse range of experimental tasks, including various forms of transsuasion and both generative and simulative settings. This breadth in task design highlights the robustness of their approach to generating and evaluating persuasive messages.
- The domain transfer experiment is particularly compelling. Through a live experiment conducted via an app, the authors demonstrate the practical impact of the proposed systems and emphasize the model's real-world applicability in dynamic, user-driven contexts.

### Weaknesses
Below is my original review. The authors have addressed these issues, so I've updated my score.

The truthfulness of transsuaded tweets is still somewhat unclear. As an attempt to make a tweet more persuasive, the model sometimes seems to add new content and statements (including statistics). It would be nice to discuss the degree of truthfulness of these statements, its potential impact, and some mitigating methods.

===

- In the transsuasion task, it is unclear if the semantic meaning is consistently preserved between paired messages. For example, the two tweets in Figure 1 seem to diverge in content, which raises questions about their semantic similarity.
- Some important evaluation seems missing. The paper does not sufficiently address whether semantic meaning is retained in generated messages for transsuasion. Additionally, for the generation tasks, it remains unclear if the generated outputs consistently adhere to the specified conditions.
- The paper provides minimal discussion on the experiment results, providing not enough scientific insights.
- It is not discussed the characteristics of model-generated messages and the factors that improve their persuasiveness. Are there be any simple factors like the length of a message and the existence of hashtags or images? A deeper analysis into which domains the model excels in and where it falls short would enhance understanding of its strengths and limitations.
- Although the paper covers a wide range of settings, the presentation is somewhat unclear. The extensive descriptions make it challenging to retain all details, and a clearer, more structured organization could improve readability.
- The authors do not mention whether the collected dataset or source code will be publicly available, which could limit reproducibility and further research.
- While this focus is not inherently a drawback, a clearer explanation of this choice and its implications would be beneficial.
- Some typos and formatting issues: line 087 (citation format), line 299 (”any model but can be conclusively”), line 398 (citation format), line 421 (citation format).

### Questions
- Some settings require adding images. How did you obtain or generate those images?
- Line 349: What is used for the oracle in the “Oracle as a judge” setting?
- Table 2: What does “ep” stand for?
- Table 2: What is the Oracle setting here?
- Table 2: What is the difference between “Ours Instruct” and “Ours (CS+BS+TS)”? That is, what is the difference between the instruction tuning setting and non-instruction tuning settings?
- Table 3: What does “it” stand for?

### Soundness
3

### Presentation
3

### Contribution
2

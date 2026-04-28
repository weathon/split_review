# DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8

## Abstract
As we increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of the users. We present \benchmark, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma includes two possible actions and with each action, the affected parties and human values invoked. Based on these dilemmas, we consolidated a set of human values across everyday topics e.g., interpersonal relationships, workplace, and environmental issues. We evaluated LLMs on these dilemmas to determine what action they will take and the values represented by these actions. Then, we analyzed these values through the lens of five popular theories inspired by sociology, psychology and philosophy. These theories are: World Value Survey, Moral Foundation Theory, Maslow's Hierarchy of Needs, Aristotle's Virtues, and Plutchik Wheel of Emotion. We find that LLMs are most aligned with the \textit{\textbf{self-expression}} over \textit{\textbf{survival}} values in terms of World Value Survey, \textit{\textbf{care}} over \textit{\textbf{loyalty}} in Moral Foundation Theory. Interestingly, we find huge preferences differences in models for some core values such as \textit{\textbf{truthfulness}} e.g., Mixtral-8x7B model tends to \textit{neglect} it by 9.7\% while GPT-4-turbo model tends to \textit{select} it by 9.4\%. We also study the recent guidance released by OpenAI (ModelSpec), and Anthropic (Constitutional AI) to understand how their released principles reflect their \textit{actual} value prioritization when facing nuanced moral reasoning in daily-life settings. We find that end users cannot \textit{effectively} steer such prioritization using system prompts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents DailyDilemmas, which is a dataset of 1,360 everyday life moral dilemmas, Using this dataset, the authors evaluate the similarity (e.g., self-expression over survival values) and differences (e.g., truthfulness) among LLMs regarding the values. End users cannot effectively steer prioritization using system prompts.

### Strengths
The authors bring theories and insights from social sciences to rigorously define the dimensions of values, which is a unique contribution not seen in the prior literature about LLMs' preferences, biases, or subjectivities. The paper was clearly written with carefully generated data and analyses.

### Weaknesses
- The authors do not explicitly test whether LLMs' value preferences originate from pre-training or the post-training (e.g., instruction tuning) process. They could consider a small supplementary analysis by comparing the base and instructed models of an open-source LLM they used (e.g., Llama-2-70B, Llama-3-70B, Mixtral-8x7B). Do base and instructed models exhibit similar or differing value preferences? It may clarify whether adjustments to pre-training data or the instruction-tuning process are necessary to steer cultural values.

- The authors raise concerns that "Reddit predominantly represents Western viewpoints" (p. 15, line 777). However, Reddit is also demographically biased (e.g., skewing younger than the general population). More details about biases in human validation dataset (r/AITA) could be useful to characterize limitations and guide future works. These datasets might be useful:
    - Waller and Anderson (2021) provide data on the demographic characteristics of subreddit users (e.g., age, gender, wealth, political stance), estimated using community embeddings. Waller, I., & Anderson, A. (2021). Quantifying social organization and political polarization in online platforms. Nature, 600(7888), 264-268. (https://github.com/CSSLab/social-dimensions)
    - Vice conducted a survey of AITA users in 2019, which could describe demographical characteristics and biases of AITA users: https://www.reddit.com/r/AmItheAsshole/comments/dcae07/2019_subscriber_survey_data_dump/

### Questions
- What are your intuitions about the source of cultural preferences in language models? (e.g., pre-training, post-training) This could be discussed in light of existing literature or through supplementary analysis.

- How were the 30 Reddit posts on page 6, line 315 sampled? Were they randomly selected, and what dates were they sampled from?

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
This paper does several things:

1. It provides a principled data-set, 'DailyDilemmas', that corresponds to real-world situations in which different values come into conflict, along with possible binary actions for these situations, their consequences, and related values. 

2. It evaluates several current models on this data-set to investigate their purported values. 

3. It compares 'stated' values to 'revealed' preferences. 

4. It examines the possibility of steering some of the models to be in line with certain values (with negative conclusions)

### Strengths
This is a fun and interesting paper, while at the same time examining an important topic in a thorough way. I appreciate the care the authors took to try and comprehensively examine values in a rather descriptive way rather than dictating one specific framework, while at the same time connecting with specific existing frameworks in order to generate and evaluate the data. I also appreciate the caveats and overall analysis.

### Weaknesses
While I did overall found the paper useful and of interest and imagine other reader in the field will too, I did have several outstanding concerns, confusions, and other issues.

These are not in order of importance, and most of the minor things had no influence on the overall score, I mention them simply if they help the authors in making the paper even better.

1. This is minor and you can ignore if you like, BUT: I like a good literature-based opening as much as the next person, but I found the specific opening here with the references to Asimov's Laws and the Trolley Problem kind of confused and scattered. First, Asimov himself used the laws as starting points for showing how they *fail*; it's not like he was proposing serious laws that later people suddenly realized "oh no what about this complicated situation?!". Also, the use of the Trolley problem is frankly odd. The original point of the Trolley Problem in philosophy is to highlight a lack of consistency in people's choices, such that in some contexts they choose A and purport to base it on utility (killing 1 person instead of 5) but in another, seemingly identical situation choose otherwise (throwing someone off a bridge, or harvesting organs from a healthy person), suggesting they don't have access to their reasoning. The original 1-vs-5 Trolley Problem is not *actually* an issue for people, and it's weird to analyze it as though it shows that both choices conflict with the value of 'harm'. Personally I think you can re-write this to be a lot more straight-forward and free up some space for later issues.

2. I found the comparison to Delphi a bit strange, in that the authors say that "while Delphi crafted descriptive ethical judgments to cover cases where some moral principles have to be breached for other more important ones (e.g., breaking the building to save a child is acceptable)". But in the original Delphi materials the original authors clearly meant Delphi to apply to many real-world, gray, unclear situations seemingly covered by the current data-set, drawing on similar original data-sets and including stuff from r/AITA. Reading the original Delphi paper one certainly doesn't get the sense that they based their data-set on "judgments to cover cases where some moral principles have to be breached for other more important ones". Rather, they say it is based on "a large-scale corpus formalizing people’s ethical judgments and social norms on a wide range of everyday situations in natural language forms."

This isn't terribly important, I get that the current data-set focuses on other stuff in how it was curated in order to pit values against one another in a way Delphi wasn't, but the characterization of previous work in this way seems not right by a reading of how the authors billed their own paper at the time.

3. I get that the authors wanted to reach for a broad set of possible frameworks, but they come off a bit confused. 'value' is not the same thing as 'need' is not the same thing as 'virtue' is not the same thing as 'emotion'. Being 'angry' is not a value, and it isn't surprising that the models don't seem to really know what to do with, and I don't understand how you generate a dilemma that pits the 'value' of 'angry' against 'honesty' for example.

4. important: Where-ever statistical claims are made they do not seem to be backed up by an actual statistical test. Rather, raw numbers are compared to one another without any sense of variance. If we did something like a bootstrap where we use a random sub-sampling of 50% of the dilemmas on the models 100 times (or whatever) and look at the means, what overall variance would we get? We might realize none of these differences really hold up, no? They might! I'm not saying they don't! But I have no actual way of knowing right now.

5. Important: I confess I'm pretty confused about the basic way that you went about testing whether some values are 'preferred'. Just to check my understanding, you use GPT-4 to generate a specific dilemma and the relevant actions and associated values with those actions. Then, you use other models to decide which of two actions to take in this situations. Then, you consider the difference between the values this choice seems to pit against one another, and...divide by the overall...values? I don't get how you then arrive at a score like "-9%" for honesty for a given model.

This method also seems to confuse between the 'strength' of a given value being violated and the 'weight' of that value, and it doesn't seem to be a way to distinguish them. 

For example, it is easy to consider dilemmas in which a given value is being violated to a greater or lesser degree (either in amplitude or probability). If I lose my job but can easily get another one, this seems like a more minor violation of self-preservation than, say, being stabbed with a knife. Or, lying to your friend that their dress suits them seems like a more minor violation of 'honesty' compared to not telling them their spouse is cheating on them. Now, on TOP of that, it may be that I value honesty more than you do, such that I would chose to tell my friend their dress doesn't suit them, but we need to disentangle that from the _amount_ of violation. 

This matters, because we cannot assume a-priori that the dilemmas are balancing this, nor can we assume a-priori that the models are carrying out the same evaluation. To put this a bit anthropomorphically, you might get GPT-4 thinking "well, lying to your friend about the dress is a big violation of honesty" and Claude disagreeing that "no it's not, it's a minor violation of honesty!" independent of the fact that Claude actually values honesty more than GPT-4 (or whatever). 

The relevant thing would be to build a model that determines how a choice is actually made, based on something like both the 'strength' of the violation, and the specific 'weight' a given model places on it. Then, you would presumably have something like choice(Action) = softmax(weight(value)*amplitude(value)/normalizing_term) [this is meant as a rough sketch]. With that assumed model of choice you would then try two recover both the weight of a value (which presumably is the same across situations) and the amplitude-of-violation in a given situation (the varies by situation). 

Without _something like this_, alongside a statistical analysis of the mean and variance of the variables, it becomes difficult to conclude anything from the current results about what the models value. 

6. Minor: I get the pot-shot at deontology and why you want to discount it, but "Directly studying categorical imperatives make studying such real-world dilemmas an impasse." seems to negate a pretty long tradition in philosophy that tries to do exactly that.

7. LOSS AVERSION: I confess I don't understand the following sentence: 

"With the concept of Loss Aversion that people care more about negative consequences (Kahneman & Tversky, 2013), we include the negative consequences of our decision making agent (p0) to deepen our consideration on D."

That is, I know what loss aversion is, but I don't understand what you mean 'to deepen our consideration on D'. What, if anything, is loss aversion doing here? Do you mean something like "we're trying to take into consideration the fact that you might avoid A compared to A' regardless of value, simply because A describes a loss"? If so, I don't understand how you do that. Also, 'loss aversion' is with reference to a particular reference point and depends on the framing of a situation, the same state ("losing 200$") can be framed as a loss or a gain depending on your reference point. 

While we're on the topic of psychological effects, a more relevant one here seems to be about 'defaults' and 'doing nothing'. There's a long tradition looking into the fact that people prefer to go with the default action (which is often, but not always, 'doing nothing') regardless of the 'utility' or 'value' of that action, e.g., see:

•	Zeelenberg, 2002
•	Anderson, 2003
•	Landman, 1987

(among many others). 

Have you considered how, if at all, such defaults play into your dilemmas?

8. Minor, but I found the details on the human comparison kind of weak. You don't provide enough details about how the authors carried out this assessment (how many, were they blinded in any way, what were their instructions) to be able to evaluate this for sure, but a Cohen’s κ of 52.6 is very weak. The fact that the task is subjective doesn't matter, part of the point of using stuff like inter-rater reliability is exactly for situations where something may be subjective in the sense of hard to define, but there is still agreement. 

9. Minor, but "It is important to note that using LLMs to generate datasets simulating human behavior is an established methodology (Park et al., 2023; Shao et al., 2023) and our study lies in applying such a methodology to moral value judgments." -- I dunno. Just because people do it doesn't mean it is a good idea, using the 'other people do it' as defense could be strengthened...

10. Maybe-minor: I didn't understand if the "values" being assigned to each dilemma (step 3 in Fig 1) is *also* being assigned by GPT-4 or by each model on their own. That is, could it be that GPT-4 thinks the dilemma is one of 'honesty' vs. 'care' whereas another model would see it differently...?

### Questions
The authors could significantly strengthen the paper by:

* providing a modeling framework (in the "statistical model" sense, not "model=LLM" sense) for actually choosing between two actions in a dilemma, that takes into account both the 'strength' and the 'weight' of a violation, allowing for models to potentially disagree on the violation itself and also to weight them differently. 

In addition, using established statistical methods to back up claims about whether one thing is different from another (I don't much mind which one, there are many possible ones, but _anything_ that gets you a sense of variance or confidence intervals over the means that allows you to then say 'the mean for this is bigger than the mean for that'; personally a bootstrap seems easiest but I leave it to the authors' discretion). 

* Clarifying various unclear parts like the human evaluation, reference to loss aversion, and whether GPT-4 is the one used to assess the values themselves for every given dilemma. 

* Taking into account defaults and non-action effects

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The author's generate an dataset of moral dilemmas that are representative of situations encountered in daily human life.  They use an LLM to assign values associated with the binary choices for the main party in the dilemma.  They then evaluate the choices made by an LLM from the perspective of the main party, and use these choices and associated values to quantitatively study the LLM's responses through different moral frameworks.  They also evaluate the ability to steer the principles of GPT-4-turbo through a system prompt.

### Strengths
1. A dataset such as the DailyDilemma dataset is valuable for evaluating LLM choices in common place dilemmas.
2. The validation of the dataset through human generated dilemmas

### Weaknesses
1. Poorly written, unnecessarily difficult to follow with important details missing.
2. The LLM generated dataset leaves open questions as to whether or not the dataset itself is reliable across several factors

## Confusing descriptions
> We define a daily-life moral dilemma situation to be D with different
group(s) of people involved as initial parties $p^{initial}_j$

What type of object is $D$?  A set, a string, a number?.  Similarly for each of the objects defined in this and the following paragraphs.  In particular the paragraph starting with "Values by agents involved in two actions of dilemma." is unnecessarily dense with notation that does not provide any value (most of it is not used throughout the paper, and none of it is described precisely enough to be useful).   What is the value $v$ represent?  It is described as a "human value" but then later in section 5 we see $(v^{selected} - v^{neglected})$ and its completely unclear what it means to subtract these "human values".  Does $v$ represent a count, a vector? If so how is it computed?

The paper could be significantly improved by being more precise in the definitions of these objects and their relationships.   Additionally, the section could be improved by providing more motivation for the definitions being made. 

>4.2 ANALYSIS ON VALUES GENERATED WITH THEORIES

There is no description of what it means to analyze the values or dilemmas from the perspective of a moral framework.  How do the 301 values map onto these frameworks?  What is the calculation being done to get percentages?  

The paper could be improved by adding more methodological details so the reader can understand the calculations and their interpretation for the analysis within a moral framework.  

> To map the values with principles shared, we first prompted GPT-4-turbo
to identify the human values from our collected 301 values shown in Table 5, revealing conflicts
between supporting and opposing values within each principle. We repeated the process 10 times,
assigning weights to values based on their empirical probabilities to signify their importance in
dilemmas. 

What does it mean to identify the human values from the collected 301 values?  Those are described, themselves, as human values.  Similarly, what is the process that is being repeated?  There isn't any real description of this?  For that reason it's impossible to interpret Table 1.  What is the meaning, scale, and significant of score?  

The paper could be improved by describing the methodological details of the calculations being made as well as clear descriptions of the metrics in Table 1.  


## Dataset Generation
The dataset is generated by an LLM and then filtered through topic modeling.  Even though there was some validation done by comparing to r/AITA data, its not clear if the dataset itself is robust. 

Are the values associated to different action choices robust over multiple generations?  For example, would the LLM pick "care" for choosing to eat the food your friend made 10/10 times?  Or would it choose another closely related value?  How does this variance effect the dataset?  Would humans agree with the values generated by the LLM?

The paper could be improved by running the generation process multiple times and measuring the variance of values assigned to different scenarios.  Additionally, having human validation (ideally blind) of the actual values assigned by the LLM would be valuable.

### Questions
## Confusing descriptions
> We define a daily-life moral dilemma situation to be D with different
group(s) of people involved as initial parties $p^{initial}_j$

What type of object is $D$?  A set, a string, a number?.  Similarly for each of the objects defined in this and the following paragraphs.  In particular the paragraph starting with "Values by agents involved in two actions of dilemma." is unnecessarily dense with notation that does not provide any value (most of it is not used throughout the paper, and none of it is described precisely enough to be useful).   What is the value $v$ represent?  It is described as a "human value" but then later in section 5 we see $(v^{selected} - v^{neglected})$ and its completely unclear what it means to subtract these "human values".  Does $v$ represent a count, a vector? If so how is it computed?

The paper could be significantly improved by being more precise in the definitions of these objects and their relationships.   Additionally, the section could be improved by providing more motivation for the definitions being made. 

>4.2 ANALYSIS ON VALUES GENERATED WITH THEORIES

There is no description of what it means to analyze the values or dilemmas from the perspective of a moral framework.  How do the 301 values map onto these frameworks?  What is the calculation being done to get percentages?  

The paper could be improved by adding more methodological details so the reader can understand the calculations and their interpretation for the analysis within a moral framework.  

> To map the values with principles shared, we first prompted GPT-4-turbo
to identify the human values from our collected 301 values shown in Table 5, revealing conflicts
between supporting and opposing values within each principle. We repeated the process 10 times,
assigning weights to values based on their empirical probabilities to signify their importance in
dilemmas. 

What does it mean to identify the human values from the collected 301 values?  Those are described, themselves, as human values.  Similarly, what is the process that is being repeated?  There isn't any real description of this?  For that reason it's impossible to interpret Table 1.  What is the meaning, scale, and significant of score?  

The paper could be improved by describing the methodological details of the calculations being made as well as clear descriptions of the metrics in Table 1.  


## Dataset Generation
The dataset is generated by an LLM and then filtered through topic modeling.  Even though there was some validation done by comparing to r/AITA data, its not clear if the dataset itself is robust. 

Are the values associated to different action choices robust over multiple generations?  For example, would the LLM pick "care" for choosing to eat the food your friend made 10/10 times?  Or would it choose another closely related value?  How does this variance effect the dataset?  Would humans agree with the values generated by the LLM?

The paper could be improved by running the generation process multiple times and measuring the variance of values assigned to different scenarios.  Additionally, having human validation (ideally blind) of the actual values assigned by the LLM would be valuable.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This article introduces a dataset designed to evaluate the value preferences of LLMs by presenting them with common moral dilemmas, framed as yes-or-no decisions. The dilemmas reflect underlying value preferences, and the authors use this method to assess how different LLMs prioritize various values. They employ five established theories (World Value Survey, Moral Foundation Theory, Maslow’s Hierarchy of Needs, Aristotle’s Virtues, and Plutchik’s Wheel of Emotions) to interpret the values represented in these decisions. The dataset is then used to compare the value alignments of several mainstream LLMs. The paper also focuses on whether the values of models from OpenAI and Anthropic align with the guiding principles set by these companies.

### Strengths
1. The paper introduces a novel dataset and approach for evaluating the values of LLMs by presenting them with moral dilemmas. By analyzing multiple decisions, it aims to assess the ethical preferences of LLMs.
2. The study is grounded in robust theoretical frameworks from social science, employing multiple theories to construct and interpret the dataset.
3. The methodology for constructing the dataset and the experiments conducted are sound and well-executed.

### Weaknesses
1. The paper introduces a novel dataset and approach for evaluating the values of LLMs by presenting them with moral dilemmas. By analyzing multiple decisions, it aims to assess the ethical preferences of LLMs.
2. The study is grounded in robust theoretical frameworks from social science, employing multiple theories to construct and interpret the dataset.
3. The methodology for constructing the dataset and the experiments conducted are sound and well-executed.

1. The paper assumes a certain level of familiarity with social science concepts, which may make parts difficult to grasp for readers without this background. Including a more detailed explanation in the appendix could enhance readability.
2. In the dataset analysis, some values appear to be disproportionately represented, which could suggest a potential imbalance. A more thorough discussion on how this might affect the experimental outcomes would be beneficial.

### Questions
1. In the experiments, you attempted to manipulate the LLMs’ behavior using explicit instructions, but your results indicate that their values are difficult to alter. Could assigning the LLMs different roles, with subtle value-based cues embedded in the role descriptions, prove more effective than explicit instructions?
2. Based on your results, do you believe that the formation of values occurs during the pretraining stage, supervised fine-tuning (SFT), or reinforcement learning from human feedback (RLHF)? Have you tested whether SFT could influence the model’s values? If it can, incorporating value-aligned training during SFT could help build better LLMs.

### Soundness
3

### Presentation
3

### Contribution
3

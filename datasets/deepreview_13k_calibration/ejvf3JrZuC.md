# Theory of LLM sampling: part descriptive and part prescriptive

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Large Language Models (LLMs) are increasingly utilized in autonomous decision-making systems, where they sample options from an action space. However, the underlying heuristics guiding the sampling of LLMs remain under-explored. We examine LLM response sampling and propose a theory that the sample of an LLM is driven by a descriptive component  (the notion of statistical average) and  a prescriptive component (notion of an ideal represented in the LLM). In a controlled experimental setting, we demonstrate that LLM outputs deviate from statistically probable outcome in the direction of a presciptive component. We further show this deviation towards prescriptive component consistently appears across diverse real-world domains, including social, public health, and scientific contexts. Using this theory, we show that concept prototypes in LLMs are affected by prescriptive norms, similar to concept of normality in humans. Through case studies, we illustrate that in real-world applications, the shift toward an ideal value in LLM outputs can result in significantly biased decision-making, raising ethical concerns.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
I am not sure whether I completely understood the paper. It seems that the paper claims that the samples from an LLM are driven by two factors: 

1. The underlying data distribution used to train LLM (or maybe data used to prompt them?). 
2. Some societal judgment (coined as ideal) of the structure of the data. 

For example, if the distribution of workout hours is mean = 7.5 but somehow if there is also a piece of information that says 7.5 hours is not sufficient/healthy, then the output of LLM related to workout hours would be larger than 7.5 hours.

---- 
I read the rebuttal and bought the implication of the result. My concerns on writing (more specifically, I felt the authors could bake something better than this with more time) remains though.

Make score converge after discussion.

### Strengths
The authors provided a quite interesting angle to explain how LLM sampling works. I also think the authors did some sufficiently rigorous assessment to validate their claims. Then I believe they also made a point that this judgmental component should be taken seriously because they “distorted” outputs of LLM from the data distribution.

### Weaknesses
I honestly feel it difficult to assess this paper. My hunch is this looks like a “fun fact” but reading the paper only left me with increased frustration — I dont feel I understand LLMs better.

But to be fair, this is conceptually quite new; I think for most ML but non-LLM specialized people, the intelligence offered by LLMs remain mysterious, and perhaps more disturbingly we dont have streamlined tools to make sense of these intelligence so providing stand-alone observations like this one perhaps is important.


I also feel the authors probably can find better ways to pitch that out over time. The paper looks written in a rush, e.g., first 3 pages are highly repetitive. The real important “meat” seems to be Sec. 3.1 to 3.3, which I read a few times before I feel I understand what it says. Some statements remain vague. For example, “the LLM is provided with N samples from this distribution as values associated with C”, are these N samples provided in the form of prompting, or part of training/fine tuning data.

### Questions
Did I understand correctly that the authors is pitching one stand-alone observation and do not claim they can explain why this happens (or have I missed other important messages)?

### Soundness
3

### Presentation
2

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
Summary: This paper attempts to distinguish between systems 1 and system 2 reasoning (from cognitive literature) within LLMs using a prompt-based approach. The authors argue that sampling using LLMs is driven by a descriptive component (that is a statistical average) and a prescriptive component (an “ideal”), which they loosely tie back to these two systems of reasoning.

### Strengths
This work asks the question of whether there are parallels between system 1 and system 2 reasoning in humans and in LLMs. The question is interesting, and contextualizing it within sampling is novel.

### Weaknesses
I have a three concerns with this paper: the coverage of related work framing the motivation is sparse;  the methods may not necessarily result in the outcome supporting the hypothesis of different systems of reasoning; finally, definitional specificity seems to be absent.

While the work attempts to ask with fundamental questions of how an output is produced, it does not engage with prior work related to sampling (e.g. inducing distributions using LLMs is an active space of literature) or how outputs are produced (the so-called stochastic parrot discussion). Perhaps more importantly, there were no clear mapping system 1 and 2 to the setting of LLMs. The related works setting up and motivating this approach are tied to popular cognitive science theories, along with cherry picked cases where some systems adopt learned models (e.g. classifiers or LLMs) as inputs into other systems; this does not equate to distinguishing between System 1 and System 2 reasoning in an LLM.

The methodology adopted focuses on responses to prompts as motivation for a rather large claim regarding how heuristics shape sampling processes. This has led to a scenario black box prompting and subsequent response evaluation, which is relatively limited particularly when making claims regarding how an output is produced. In many of the evaluations, the method is tied to prompting itself. For example, in 4.3 prompts such as, “To what extent do you think this is an average C?” are adopted as metrics, when aggregated, for internal consistency and adopted as the measurement itself. Without additional evidence (e.g. internal state), I'm not confident this result is supporting the authors' claims.

How the authors define "ideal", which is a core contribution of the work, is unclear in the paper; in the abstract, there is a mention that the ideal is represented in the LLM, but this is not mentioned specifically later in the paper and it becomes unclear how the concepts of average and ideal are differentiated.

Additional comments: Grammar error: "without" is included 2x in first sentence. Some of the formatting decisions are interesting / atypical for ML papers, including this venue, such as coloring words of interest (I would suggest the authors switch to italics or boldening instead to avoid issues with printing e.g. in black/white and for color blind readers). The first figure is also rather difficult to parse.

### Questions
How are the authors differentiating between prototype, ideal, and statistical average? There are a few cases where the language seems to be used interchangeably and putting this early in the paper would be helpful.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the sampling mechanisms of Large Language Models (LLMs) and introduces a theory suggesting that, like humans, LLMs generate responses using a combination of descriptive norms (reflecting statistical averages) and prescriptive norms (representing idealized values). The authors conducted a series of experiments to validate this theory.

### Strengths
The problem they address, the numerical sampling behavior of LLMs and the biases that influence it, is under-explored and interesting. Framing this problem within cognitive science offers a new perspective. The observations about LLM’s sampling abilities are somewhat novel.

### Weaknesses
I believe the first half of the paper (before the experiments) could be more clearly presented with some editing. The abstract talks about heuristics in LLMs’ sampling, but it was not clear what ‘sampling’ refers to--for example, whether it pertains to token generation or other outputs. Additionally, while the authors repeatedly mention the prescriptive component and the notion of an ideal, they don’t provide concrete examples or sufficient details to clarify these concepts. As a result, readers must wait until the experimental sections to fully understand key ideas presented in Sections 1 and 3. I suggest including an example at the beginning to motivate the problem better and increase the clarity and engagement.

The notations used in the paper, such as the various forms of 'C,' can be confusing and require readers to frequently refer back to their definitions, which disrupts the flow of reading.

Although their observations are interesting, the implications of this study are unclear. How can we further investigate the internal mechanisms of the LLMs based on these results?

### Questions
What happens if we change the scale of sampling numbers? For example, if we change the scale of numbers from 1-100 to something else. 

How do the distributions of the numbers that LLMs sampled look like? Providing a more detailed analysis of the distributions of the sampled numbers would be valuable. Do LLMs exhibit a tendency to generate certain numbers more frequently? How does this behavior vary across different models or parameters, such as temperature settings?

Regarding the explanation in line 300 about assigning random grades, could you clarify what this entails? Does it mean that the grades are assigned without any meaningful relationship to the numbers?

### Soundness
2

### Presentation
2

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
The authors propose that we unpack LLM output into a descriptive and prescriptive norm. While the descriptive norm is the usual focus, the paper develops the notion of an parametric "ideal" that also influences output. They frame this as "sampling" from a set of possible outputs and connect the notions of the true distribution, the ideal distribution, and the sampling distribution. This theory may explain LLM output in three experimental settings (novel concepts, existing concepts, and prescriptive components) across 10 domains with 15 LLMs, in which the LLM provides average values, ideal values, and sample values. The sample values tend to be lie between average and ideal values. This is replicated in human subjects experiments, though there is limited correlation between the contexts in which humans versus LLMs have more tendency towards idealized values.

### Strengths
1. The authors provide robust evidence for their central claim that LLMs tend towards rather than away from idealized numbers when providing samples. There is plenty of surface area to critique, but no single paper could address every concern for a claim like this.
2. The presentation is clear. I appreciated the color-coding in particular (it may not be color-blind accessible, but I don't see how that could be fixed).
3. I appreciate all the detail in the appendix.

### Weaknesses
1. The scope of the contribution is marginal. It is unsurprising that LLMs tend towards idealized output (e.g., arxiv.org/abs/2406.17055), and I'm skeptical that this contribution, no matter how well-evidenced, would be of sufficient value and significance for ICLR. A more compelling contribution in this vicinity, just as an example, would be the topic of Figure 4 and Figure 5. I think there is too much noise in the examples (e.g., categories in Table 2) to conclude that there are systematic differences, but I don't know in what contexts LLMs would produce examples more idealized than those humans produce, and this could have interesting implications (e.g., that preference-tuning has prioritized some moral issues more than others).

2. The prototypicality experiment seems out of step with the others and particularly weak. The authors themselves accept that the idea of prototypicality involves both the descriptive and normative factors, so why wouldn't the model agree with that? It looks like the prompts for prototypicality are "good," "paradigmatic," and "prototypical," which are clearly all words that tend towards the normative.

3. While I'm convinced of the central claim of the paper, I'm not sold on many of the methodological details. For example, I don't find the paragraph Lines 247-254 convincing. Why would an estimate of zero hours per week "glubbing" mean "no pre-existing statistical association"? Doesn't the model presumably recognize that it is not a real hobby, and if it were (e.g., a recent social trend past its training data), it would most likely not be common enough to budge the average over 0? Moreover, wouldn't most hobbies except perhaps the most popular (e.g., running) have mean 0? This is not to mention that the prompt, "What is the number of hours a person does glubbing in a week?" is ambiguous (e.g., average person? a person who does glubbing?). The "C+" assessment is similarly unconvincing; why is it assumed that I see that as making "glubbing" neutral? One better direction would be using a variety of made-up words, ideally with different structure (e.g., some being more realistic like "tally ball"; some being assigned only a code like "Hobby 9235").

4. I don’t find the human subjects studies very convincing. This may just be missing methodological details (e.g., how did the authors ensure the human subjects were providing truthful responses? This could be methods such as Bayesian truth serum (science.org/doi/10.1126/science.1102081)), but if I’m understanding correctly, the average human respondent said that, ideally, 11.1% of people would drive drunk, which is missing face validity. I also did not see a discussion of the institutional ethics process for the human subjects studies.

5. I was not sold on the motivation for this "sampling" process in the first place. As I said, I'm not skeptical of the central claim, but why would we care how the model responds to, “What is the first number of glubbing hours that comes to your mind”? That's not a realistic use case. Something in this vicinity that would be more interesting to study would be the generation of user personas, which is common (e.g., arxiv.org/abs/2310.11667) and could be probed in similar ways.

**Minor weaknesses**

1. The presentation of the paper is limited by excessive mathematical notation when everyday language would suffice. $C$ could be removed from most places and just talk about the concept in plain English (or something like capitalized terms if you prefer). There are little oddities like saying "Gaussian" when "Normal" would suffice or saying "we use a binomial test" for a single sample. Equations (1) and (2) seem unnecessary and make it seem more complicated than it is. This reads like a paper trying to seem more mathematical than it is, and I'd encourage the authors to just embrace having a less technical contribution.

2. Similarly, I found the "concept" versus "category" distinction confusing.

3. It's not clear to me how variation was created across "samples." Was that purely temperature variation, or something like prompt variation? I don't think the log-probs assigned to various tokens should be expected to be a reliable sample of something like the real-world noise in human responses.

4. The use of "ideal prompt" in the appendix, which seems to just mean "main prompt," is confusing given the use of "ideal" elsewhere.

Typos:

“$ cheated on taxes”

“Findings in prior art”

"thought the ...  converge" -> "though the ... converge,"

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

# To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
Recent claims about the impressive abilities of large language models (LLMs) are often supported by evaluating publicly available benchmarks. 
Since LLMs train on wide swaths of the internet, this practice raises concerns of data contamination, i.e., evaluating on examples that are explicitly or implicitly included in the training data. 
Data contamination remains notoriously challenging to measure and mitigate, even with partial attempts like controlled experimentation of training data, canary strings, or embedding similarities. 
In this work, we conduct the first thorough longitudinal analysis of data contamination in LLMs by using the natural experiment of training cutoffs in GPT models to look at benchmarks released over time.
Specifically, we consider two code/mathematical problem-solving datasets, Codeforces and Project Euler, and find statistically significant trends among LLM pass rate vs. GitHub popularity and release date that provide strong evidence of contamination. 
By open-sourcing our dataset, raw results, and evaluation framework, our work paves the way for rigorous analyses of data contamination in modern models. We conclude with a discussion of best practices and future steps for publicly releasing benchmark in the age of LLMs which  train on webscale data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper conducted longitudinal analysis of data contamination in large language models (LLMs), a problem where models are evaluated using data that they may have been trained on, thus overstating their capabilities.  The authors leveraged natural experiments provided by the training cutoff dates of models like GPT-3.5 and GPT-4 to study contamination. They analyzed Codeforces and Project Euler, websites that release code problems over time, and find evidence of contamination based on the pass rate of LLMs for problems released before their training cutoff dates. The study demonstrates statistically significant associations between a problem’s presence on GitHub and LLM performance for pre-cutoff problems.

### Strengths
1: The analysis from longitudinal perspective is novel. 
2: The comprehensive experiments, large-scale dataset and code base provided by this work will definitely benefit the community of contamination analysis.
3: This paper is well organized and easy to understand.

### Weaknesses
1: The results are interesting but not that surprising. Many blogs or discussion in the community about Data Contamination has involved similar results.
2: There is lack of depth analysis about how implicit contamination is possible. If some real examples can be extracted to show how this could happen, it will be much better.

Overall, I do appreciate the effort to investigate the Data Contamination problem from longitudinal side and open-source data/codes. The experiments also show intriguing results. But I believe the contribution of this paper is not enough to be accepted by ICLR, for its limited scope and technical novelty. It's limited to Code datasets. And the only novelty is how to split the "train" and "test" set.

### Questions
N/A

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a detailed investigation into data contamination in large language models (LLMs), using GPT model training cutoffs to analyze benchmarks released over time. It examines two datasets, Codeforces and Project Euler, revealing clear patterns that suggest contamination based on the LLMs' pass rates correlated with benchmarks' GitHub popularity and release dates. The authors provide a comprehensive dataset, findings, and a framework for future analysis, promoting better practices for benchmark releases in the era of web-scale LLM training.

### Strengths
The idea to investigate data contamination in LLMs via cutoff datasets makes sense and is interesting, which guarantees that the testing data are not available in the training set of LLMs. And the findings are surprising, revealing that people should deal with the ability of LLMs more carefully. This study shows that LLMs are likely to have generalization problems as well as traditional ML models and deep neural networks. And I think this should raise the attention of ML researchers.

### Weaknesses
I am not quite familiar with LLMs, and I only have one question about the design of cutoffs. What if a code problem released later is exactly similar as some problems that has already existed? And how to measure the data contamination problem is also important.

### Questions
Please refer to Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Assess whether GPT performance at coding (sometimes called program synthesis) was possibly affected by contamination of pretraining data using a naturally occurring experiment (i.e. comparing scores before and after the pretraining knowledge cutoff dates).

### Strengths
Overall, I really liked this paper. I thought it was well motivated, clearly conceptualized, well executed and somewhat thorough. I have a small number of requested changes, and if the authors and I agree that the changes are sensible and if the authors agree to make the changes, I would be happy to increase my score.

### Weaknesses
 > Figure 1: Marginal Effects of Pass Rate Metric 

I think this is an amazing figure. 5 comments, ordered from minor to major:

1. easy: Stacking log(Github Presence) and log(Difficulty) at the bottom makes reading the figure tricky. I might suggest moving log(Difficulty) to the right side.

2. easy: GitHub is stylized "GitHub", not "Github"

3. medium: Where is the equivalent plot for Project Euler? I might have missed this, but I cannot find it in the main text or appendix.

4. hard: The pass rate is significantly lower for easy and medium problems, even for log(Github Presence) = 0. I understand that GitHub Presence is a proxy, but I would think that log(GitHub Presence) = 0 is our best guess for "low or no contamination", but there's still a 10-20% decrease in pass rate. Why? I can think of 2-4 possible answers: (a) GPT-4 genuinely becomes much worse after the knowledge cutoff; (b) GitHub presence is inadequate and/or misleading, (c) the distribution of Codeforce problems changed after GPT-4 was finished pretraining, or (d) something changed in how the pass rate is calculated on generated outputs. More explanations might also be possible. Is there some way for the authors to try to investigate the cause of this shift?

5. hard: I was hoping for either a qualitative or quantitative analysis about what GPT-4 is outputting on Codeforces problems released after the cutoff, but I can't find even a single example of the raw generated outputs. Could the authors please provide some manual examples, even in the appendix, to convincingly demonstrate that GTP-4 is indeed outputting worse code? I want to rule out that silly possibilities (e.g., a shift in formatting) are affecting the results.

> Table 1

I personally find Tables are less effective at communicating than Figures. Since these are regression tables, could you possibly consider switching to a Forest plot of regression coefficients? Some random examples here:

- https://www.researchgate.net/figure/Forest-plot-of-regression-coefficients-95-confidence-interval-for-the-association_fig1_331119872
- https://www.researchgate.net/figure/Coefficient-plots-from-linear-regression-predicting-what-makes-an-interaction-meaningful_fig1_343608677 
- http://www.strengejacke.de/sjPlot/reference/plot_models.html.

To make my suggestion as concrete as possible, using terminology from matplotlib & seaborn (assuming you're using Python, but I'm sure R could do this as well), I'm specifically thinking that your X axis should be the estimated parameters and confidence intervals, Y would be the covariates (i.e. Difficulty & GitHub presence), the Hue is either Before Cutoff or After Cutoff, and you have two side-by-side axes, one for GPT4 and the other for GPT3.5.

I personally would prefer all regression tables to be visualized as such (Tables 1, 2, and those in the appendix).

### Questions
Not a question, but I want to note that:

1. I like the use of Pass Rate in lieu of pass@1. I think that's a very sensible choice.

2. I like the citation of Horace He's and Chris Cundy's tweets. Very good scholarship, even if Tweets aren't "published" in a traditional sense.

### Soundness
3 good

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
The paper investigates data contamination of GPT-3.5-Turbo and GPT-4 with problems from Codeforces and Project Euler. It does so by analysing the passrates in relation to the GitHub presence and notes a positive correlation for data before the cutoff, but no significant correlation after this date.

### Strengths
1. Identifying data contamination is an important issue, especially for evaluation datasets that are often used to create rankings.  
2. Including problem difficulty as an independent variable is an important step in isolating the confounding effect of item difficulty on pass rates.
3. I appreciate the openness in referencing blog posts and tweets that anecdotally suggested possible contamination prior to this work

### Weaknesses
1. The methodology is only applied to GPT-3.5/GPT-4, where training details are unknown. In particular, as noted in footnote 1, OpenAI has admitted to using a small amount of data beyond the cutoff date. While I understand the choice of the GPT family as a commonly used model, it would have been better to verify the approach with fully open models where more training details are available (and more trustworthy).
2. The methodology requires underlying datasets that are longitudinal in nature, i.e. release problems/individual tasks over time; this limits the applicability to sources other than Project Euler / Codeforces.

### Questions
### Minor Comments
* Particularly in section 2, some citations are formatted differently, with the author names outside the parentheses; in sequences of different citations, readability could be improved by using the same citation format as in section 1.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

## Human Reviewer 1

### Summary
The paper studies the current state of LLMs on the forecasting task.

### Strengths
- Some results/analysis may be interesting to the community.
- Study on a recently new application of LLMs.

### Weaknesses
The paper reads like a poorly written project report. Specifically, section 3 severely lacks clarity.

### Questions
- "I" is used throughout the paper, but the author should use "We"
- The text is riddled with language errors, and the writing is very subpar.
- Citations do not seem to follow the standard ICLR style. This needs to be fixed.
- Many figures aren't referenced in the text.

### Soundness
1

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper considers forecasting as an out-of-distribution test for LLMs by evaluating them on events that had not yet occurred at the time of model training. The study collections ~400 questions from Metaculus and tests multiple frontier models using a “superforecaster” style prompt. As its main result, the best model (o3) achieves ≈0.135 Brier score. This is better than historical human-crowd baselines from prior work on different question sets but still underperforms expert forecasters. It also shows that narrative prompting degrades performance relative to direct forecasting prompts, suggesting that fictional framings can hurt probabilistic calibration.

### Strengths
The paper is overall well written with a clean main result.  The measurements are standard and appear sound. 

The paper chooses questions resolved after each model’s knowledge cutoff and inputs are filtered to short, pre-resolution news summaries. This prevents potential leakage.

The paper evaluates a wide range of frontier models, including o3-pro, Deepseek-V3 and Claude-3.6-Sonnet.

### Weaknesses
I find the paper overall quite weak in its data collection and evaluation methodology. 

On the data set, it only collections about 400 questions from one platform (i.e., Metaculus) with most questions from Jul–Dec 2024. It's unclear to me if the dataset is diverse enough. Compared with prior work like https://openreview.net/forum?id=FlcdW7NPRY, 400 is also quite a small sample size. 

Regarding evaluation, the paper considers only 2 prompt styles and offers no attempt to optimize the overall prediction pipeline. For example, one could consider fine-tuning the model or optimizing the new retrieval system to improve the performance.  In addition, the paper’s own calibration plots show systematic miscalibration (Sec 5.5), but there’s no corrective post-processing or calibration method evaluated.

From an ML perspective, this paper provides no new technique in improving LLM for forecasting. It seems to be only an eval paper, and yet prior works like https://arxiv.org/abs/2409.19839 and https://futurex-ai.github.io/ are, in my opinion, stronger and more comprehensive. So it's not clear to me what is the novel contribution here. 

Finally, from previous work, news retrieval can be unreliable when it comes to offering a date cutoff; see https://arxiv.org/abs/2506.00723. This can cause contamination. The paper would be stronger to test against this, as it applies a new pipeline called AskNews which to my knowledge has not been used widely in the literature.

### Questions
Any plan to release the dataset and model resolutions?

Is there a plan to continuously update the dataset and evaluate upcoming models?

Expert forecasts cover only subsets of (157 questions; 41 in the hold-out). Do you expect this is sufficient in estimating the model vs expert gap?

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper presents an evaluation of LLMs against a select group of expert forecasters on real-world forecasting questions from Metaculus. Model prompts mimic human access to knowledge via inclusion of relevant news articles for the forecasting question in the prompt. Paper finds that LLM forecast are on par with general population, however underperform experts.

### Strengths
1. The paper contributes to measurement of LLM abilities in real-world reasoning and forecasting. The contributed dataset could potentially be of great value.

2. It is a timely problem to study.

3. Experiments consider most of the frontier closed source models.

### Weaknesses
1. The paper states various things without attribution/substantiation/citation. A couple of examples (among many) are as follows.
Lines 84 - 88, about mental model, ensemble of LLMs are better etc.
Line 105-106 statements like “ An LLM does better when fed news articles from AskNews over Perplexity”

2. I think the claim about preventing contamination as events haven’t occured yet based on LLM cutoff date is not entirely accurate. This is because the experiments are comparing LLMs performance with Metaculus experts, who may have opined about many of these events. The output is not contaminated as events haven’t happened but discussion around those may have happened. More broadly LLMs may have been trained on human analysis, discussion, and even prior predictions about these events (ifrom various other sources ncluding Metaculus itself) that existed before the knowledge cutoff. This is crucial to note because it forms the basis for experimental comparisons and results.

3. The paper compares LLMs to experts. However, experts are not defined appropriately. Paper mentions experts are the forecasters with  a track record of making good predictions. However, it is not defined what good means like paid experts, top 1% of predictors, or quantification. This makes it hard to understand how to interpret the results or their effects.

### Questions
1. Could you include description of experts and when were they identified relative to hold-out set curation?
2. Early on the paper, highlights that smaller datasets for similar tasks were quite smaller limiting its statistical power. Does it make sense to include in the  experiments statistical comparison to support statements like LLMs "significantly" underperform expert?
3. One of the prompts have words like “models are NEVER wrong”, which may introduce significant bias. How do results compare between direct and narrative prompts without such biased prompting?
4. Paper states that AskNews is better than Peplexity. Do you think it would be valuable to quantify how much of LLM’s performanc is attributable to quality of news itself? Would the conclusions of paper change if we use Perplexity or other search engines for news search?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
0

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper evaluates the forecasting ability of 12 state-of-the-art Large Language Models (LLMs), including frontier models from OpenAI (o3, o3-pro, GPT-4.1) and Anthropic (Claude 3.5/3.6). The author tests them on a new dataset of 464 real-world forecasting questions from Metaculus, with all events resolving after the models' knowledge cutoffs.

The evaluation includes a prospective and retrodictive setting, with a comparison of the results (the first of its kind, to the best of my knowledge). A narrative-based forecasting idea is also evaluated.

This paper is a bit of a curve ball. At first it seems like it will miss, but then once you notice its strengths it becomes quite promising. As such, I tentatively recommend acceptance (with the expectation that the authors will address comments raised by the reviewers). If the authors can address some of the framing issues, I would be willing to increase my score. If they can further strengthen the exploration of narrative-style forecasting, I think this paper could become quite strong and valuable for the community.

### Strengths
- The paper includes a prospective and retrodictive evaluation and compares them against each other. This has been sorely missing in the literature, but oddly I don't think the authors of the paper realize how much value this provides to the field. E.g., it partly resolves some of the key concerns highlighted by Paleka et al. (see weaknesses section for this citation). This comparison should be greatly emphasized. The fact that retrodictive and prospective evaluations give consistent results would be of interest to many people in the community.
- Figure 1 is compelling and should be placed at the top of the paper imo.
- The narrative prediction setting feels a bit wonky in the way it is currently presented (e.g., a discussion between Nate Silver and Tetlock seems weird; why not just have the model describe the future?). However, the core idea of getting models to describe the future in some form of prose rather than answer a binary question about the future (as is the focus of most forecasting work) is strong and deserves much more attention. If the authors can rework this to be more about the key distinction between structured prediction of the future rather than binary questions, I think the paper would be much stronger. As it stands, I think this is a bit too disconnected from the rest of the paper to strengthen it.

### Weaknesses
- Line 28 says "There are two types of forecasting: predicting the future based on a few datapoints or heuristics, or making predictions with a traditional machine-learning model". This doesn't seem like a natural taxonomy. Where does time series forecasting fit in? Also, forecasting like that done on Metaculus isn't made with few datapoints; enormous amounts of data (albeit unstructured) goes into those forecasts. To the best of my knowledge, the standard term for Metaculus-style forecasting is "judgmental forecasting".
- Only evaluating models on one news collection date is not ideal. How do models compare closer to the resolution date? This is very important, because humans may be more effective at incorporating new information, especially for more recent events after the pretraining cutoff of models.

Missing citations:
- "ForecastQA: A Question Answering Challenge for Event Forecasting with Temporal Text Data" by Jin et al. (a foundational paper in this area)
- "Forecasting Future World Events with Neural Networks" by Zou et al. (possibly the first paper to evaluate LLMs on Metaculus questions)
- "Pitfalls in Evaluating Language Model Forecasters" by Paleka et al. (crucial recent paper emphasizing the benefits of prospective evaluations of forecasting models)
- "LLM-as-a-Prophet: Understanding Predictive Intelligence with Prophet Arena" by Yang et al. (another recent prospective forecasting evaluation, along with Karger et al. (which is cited)).

Suggestions (not factored into score):
- RE Section 6.1, "All remaining errors my own": I would argue that any errors made by o3 and Claude in assisting with research are also attributable to the authors, much like a PI should take final responsibility for their students' errors.
- The paper says "This paper originally referred to expert forecasters as superforecasters, but I have since been informed that Superforecaster is a registered trademark of Good Judgment Inc." Oddly, "superforecaster" is frequently used in the rest of the paper. I don't think Good Judgment Inc would mind if the word "superforecaster" was used in a research paper, but I would recommend being consistent here.
- I feel like I'm going to lose this battle, but people really should be evaluating calibration error separately from Brier score (which conflates accuracy with calibration error). This is standard practice in non-forecasting treatments of calibration, but gets neglected by the forecasting community for some reason.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4
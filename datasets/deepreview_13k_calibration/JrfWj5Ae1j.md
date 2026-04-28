# Towards Effective Discrimination Testing for Generative AI

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 5, 8

## Abstract
Generative AI (GenAI) models present new challenges in testing for, and regulating against, discriminatory behavior. In this paper, we argue that GenAI fairness research still has not met these challenges: there is a dearth of reliable bias assessment methods for GenAI systems that speak to regulatory goals. This leads to ineffective regulation that can allow deployment of reportedly fair, yet actually discriminatory GenAI systems. Towards remedying this problem, we connect the legal and technical literature around GenAI bias evaluation and identify areas of misalignment. Through four case studies, we demonstrate how this misalignment between fairness testing techniques and regulatory goals can result in discriminatory outcomes in real-world deployments, especially in adaptive or complex environments. We offer practical recommendations for improving discrimination testing to better align with regulatory goals and enhance the reliability of fairness assessments in future deployments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes that traditional (1) fairness evaluations and (2) popular red teaming approaches are not effective in their current state for generative AI evaluations, arguing that these evaluations should be contextualized to a given domain rather than defined relatively a priori for (1) and focus on "producing standardized and robust attack frameworks" for (2). The arguments for (1) are themselves not novel (indeed, the authors cite commentary from the White House OMB to this end). Instead, the paper is intended to highlight a sample of cases where the outcome maps true to the community's general intuition. They consider four empirical evaluations on1) summarizing resumes through LLMs,  2) variability in red teaming for offensive screening, 3) how single turn and multi turn interactions should be evaluated differently, and 4) how user modification influences model outputs. Each case's methodology largely focuses on prompting existing models then evaluating the outputs.

### Strengths
This paper is grammatically well-written, and provide coverage of important recent regulatory discussion motivating the work. The authors touch on a number of important questions. The discussions, specifically around red-teaming and single vs multi turn interaction, were interesting, though I am less familiar with that body of literature on red-teaming and so rely on other reviewers to discuss its relevance and novelty. The paper is timely and thus of interest to ICLR's audience.

### Weaknesses
I have a number of concerns with this work that lead me to believe that it is not ready for publication. I will speak to the broadest concern first, then focus on specifics of experimental protocol second.

Paper structure. This paper is quite broad in its application. The case studies are relatively shallow, as a result, and connecting the themes together weakens the contribution. For example, I believe that the experiments and discussion regarding red teaming and the single vs multi-turn are contributions that should, when done well, be published in a venue like ICLR, ICML, or FACCT. But the experimental protocols, the appendices, and the discussion do not currently do these concepts justice. I would suggest the authors either revisit how they synthesize this work into one coherent story, or split into separate papers where they more deeply engage with the topics both experimentally and in takeaways for the community. This cannot be done in the time frame of a review cycle, but makes for much better papers.

Experiments. I have a number of questions, and concerns for the experimental study. 

Experimental Setup for E1
This experiment relies on generated resumes, where different names based on ethnicity are included. The appendix is very sparse for these experiments, as are the main text explanations, which leads me to the following concerns:

(1) how were the resumes generated? In the same way that summarizing can embed bias so too can the generation be a result of samples that are not representative of our ideal. Specifically, how did the authors ensure that the resumes generated were close enough to or the same across each variable (e.g. ethnicity) s.t. the results were not confounded? Without thorough control for externalities, it’s unclear if the resulting summaries are actually indications of what the authors claim. Further, it would be useful if the authors repeated the results across several models. While the authors used separate models to produce and evaluate the resumes (which is a great step), this fact on its own is not enough to ensure reliable outcomes. Beyond this, it would be helpful if the authors include full details of the prompting, the model versions that they used to prompt (assuming they used APIs), along with the resulting resumes for reproducibility.

(2) I’m generally confused at how this experiment was structured, as it seems like there is a generated resume, a summary, and then a score, but that pipeline isn’t clear from the main paper or the appendix.

(3) I am also concerned that Llama is not a good proxy for this setting of resume evaluations per se. There’s a difference between summarizing the content of the resume and grading it. The description in the appendix includes the line, “In order to simulate interview decisions, we prompt Llama-3-70B to score each candidate 1-10 based on the summary of their resume, where a score of 9 or greater results in an interview.”  Summaries from language models make sense for LLM applications, but grading criteria is more likely to be applied on top of these summaries as either a classifier or some other learned (specialized) tool. A reasonable assessment is to look at how the summaries themselves are biased, resulting in the next step (scoring) being unfair. But it appears to instead be the case that the authors used generative tooling for each step. This introduces many degrees of freedom in the result that I would like to see minimized if possible. While the authors explicitly state that realism is not their focus, the descriptions of these experiments as they stand are not sufficient, and further detail is needed. 

Experimental Setup for E2
This experiment involves using a RedLM (there are apparently 7) to generate question templates. The blanks in these templates are then filled (unclear how) and fed into the LLM of interest. In this way, the LLM of interest is then evaluated by its responses in aggregate, which are measured for toxicity etc. I think the experiment is being compared to a baseline measure of fairness/bias, but the baseline is not described. In other words, I do not understand how this experiment is intended to show that variability is a concern ( though I buy the premise). Further, there are two instances where the RedLM and the LLM of interest are the same... is there a reason why it's okay here to generate and then evaluate using said content? I don't know that in this specific case it is too much of an issue, but it is odd from an empirical perspective.

Experimental Setup E3
Again, this experimental idea is interesting. Changing conversation length is a nice and straightforward variable that I can imagine motivating a number of exciting new evaluations in the future. However, the actual experiment is not clear. For example, how are the attack "successes" measured? In general, I could not understand what was actually measured or what was changed from what was included in the writing. 

Ultimately, the information shared in this paper is not enough to reproduce the experiments as-is. Each case study would benefit from both greater description, and deeper exploration. The authors are on a promising track and would benefit from an additional number of months to refine both studies and their communication of the issues at hand. I would like to see additional discussion of how to build on these concepts. I'm excited to see future iterations!

### Questions
In general, please see above for questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper discusses the gap between LLM evaluations and regulatory goals in generative AI systems. The authors present four case studies demonstrating how current fairness evaluation methods may fail to prevent discriminatory behavior in real-world deployments. The paper makes connections between technical and legal literature while offering practical recommendations for improving discrimination testing.

### Strengths
The paper discusses a timely an important topic, and some of the case studies are quite compelling (in particular the ones from 4.2 and 4.4). As far as I can tell, the main originality of the paper lies in the connection to the legal literature, and the case studies showcasing certain important phenomena, which make the assessment of the fairness of models difficult or legally challenging. 

I think the paper is quite clear, and may be somewhat significant for an audience that is not particularly versed with LLMs. 

I thought the second case study was well executed, and showcases an important phenomenon that practitioners are somewhat aware of, but it's good to have a comprehensive demonstration of. I also though the 4th case study does a good job at highlighting one aspect of deployment that people don't often think about (generation hyperparameters) and raising interesting legal questions about who should be responsible for harmful behaviors that are due to changes in hyperparameters like that.

### Weaknesses
Despite the fact that the phenomena being showcased are important, I don't think most of them are novel: I expect that most practitioners would not find any of the case studies surprising, and would already know most of the phenomena being discussed.

Let's take for instance the first case study: the authors make the case that using quality metrics like ROGUE will not necessarily correlate with fairness. I don't think this would surprise anyone: this is exactly what spurred many evaluations that are specifically targeted for fairness, toxicity, and so on. In the technical reports for frontier models, there are plenty of such evaluations being made (which again indicates that something quite similar to the main takeaway from case study 2 is already mainstream: i.e., people should be doing many different evals with different setups, and looking at the whole picture). 

I would have found the first case study much more compelling if it were using some of the state of the art benchmarks for LLM fairness. Moreover, I found it a bit suspicious that the authors used Llama 2 for the first case study, but not for the later ones. This made me question whether that model (together with the others) was cherry-picked to make the point they were trying to make – that's fine (because ultimately you're just trying to show that this kind of phenomenon _can_ happen), but it does detract from the impact of your point, as it makes one question how common this kind of phenomenon actually is.

Moreover, the first case study suggests to use alternate fairness metrics, showing that they are more successful. This feels a bit to me like re-inventing the wheel, as there are already other evals which are specifically tailored for measuring fairness, and my guess would be that such evaluation scores are already more correlated with actual fairness of outcomes in the setting that is tested. Another smaller qualm with the setup is that there were no error bars reported in Figure 2, and the number of resumes generated was quite small, when considering that they are AI generated, so the additional generation costs are minimal. This makes it hard to assess the significance of results.

Despite the second case study being well executed, the takeaways are a little underwhelming – as mentioned above, I think they are already the standard practice for any entity that knows what they're doing.

I had trouble understanding the third case study, especially the experimental setup. How is the interaction history created exactly? Do you have an example of what an interaction looks like somewhere?

### Questions
Already asked above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper discusses the legal and technical literature related to discrimination in Generative AI. It focuses on four main challenges: (1) the mismatch of traditional fairness metrics, (2) the reliance on red teaming, (3) evaluating fairness after different interactions and (4) impact of changes in hyper-parameters. The authors provide evidence of each challenge by running experiments on different datasets, some textual and some images and provide recommendations for how best to assess discrimination arising from GenAI in relation to non-discrimination laws and AI-specific laws and regulations.

### Strengths
I enjoyed reading this paper - it is clear and well written. Further, it provides a good narrative of existing literature and collates four major challenges in assessing discrimination of generative AI. The experiments are sound, well thought out, and give evidence for the issues identified. Thus, the motivation for the provided recommendations on how best to assess discrimination are clearly motivated. This is a highly topical and important field which needs urgent consideration. Mapping legal concepts to technical concepts is the main novelty of this paper.

### Weaknesses
Although the recommendations are well supported, they are general, not very actionable and are thus not a great addition to the paper. The abstract claims the recommendations are 'practical' which I think is a bit misleading. For example, in the "Mitigation" part of Section 4.1 (line 295 onwards) the following recommendations are made:
- "fairness researchers should attempt to create metrics and testing regimes that shed light on how GenAI behavior may influence decision-makers' perceptions of candidates from different demographic groups. One approach could involve developing standardized frameworks that measure bias..."
- "By considering this larger, tailored suite of metrics..."
I do not think these recommendations go far enough in being practical, more considerations of future work that should be explored.

The work is very topical thus there has been a lot of testing done for discrimination in GenAI already, the originality comes in the narrative and legal perspective however this legal perspective is heavily focused on the U.S. legal landscape.

Other:
- Introduce all terms or do not use them (e.g., frontier models, NLP)
- Figure 1 doesn't add much for me, I can see it maps directly to the sections/issues but it would be useful to use the same terminology in the diagrams or in the section headers to relate it directly

### Questions
- You mention liability (and accountability) a few times throughout the paper - do you have any thoughts on how this intertwines with the legal landscape? As stated, this is a challenge particularly in GenAI, could be useful to discuss this a bit more, or reference discussions on it. 
- In line 142, you state that when GenAI is used to make allocative decisions in a way that mirrors traditional decision making... Could you expand on this? What is an example and how does it mirror? Further in the paper this is explored further but it could be good to provide and example here. Has it actually been used in a real-life scenario?
- Related to the above: the paper notes that "the experiment for applying traditional fairness notions to GenAI systems is high-fidelity of a real hiring application to demonstrate bias evaluation and downstream discriminatory behaviour". This is of course necessary for the paper, but do you know any examples of real hiring applications using GenAI?
- Do you have any thoughts on how the application focused approach of the EU AI Act connects to the assessment of discrimination of GenAI?

### Soundness
3

### Presentation
4

### Contribution
3

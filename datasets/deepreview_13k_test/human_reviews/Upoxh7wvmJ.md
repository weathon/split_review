# Strong Preferences Affect the Robustness of Value Alignment

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Value alignment, which aims to ensure that large language models (LLMs) and other AI agents behave in accordance with human values, is critical for ensuring safety and trustworthiness of these systems.
    A key component of value alignment is the modeling of human preferences as a representation of human values.
    In this paper, we investigate the robustness of value alignment by examining the sensitivity of preference models.
    Specifically, we ask: how do changes in the probabilities of some preferences affect the predictions of these models for other preferences?
    To answer this question, we theoretically analyze the robustness of widely used preference models by examining their sensitivities to minor changes in preferences they model.
    Our findings reveal that, in the Bradley-Terry and the Placket-Luce model, the probability of a preference can change significantly as other preferences change, especially when these preferences are dominant (i.e., with probabilities near 0 or 1). 
    We identify specific conditions where this sensitivity becomes significant for these models and discuss the practical implications for the robustness and safety of value alignment in AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper is an investigation into the reliability of current popular value alignment techniques.  It specifically asks how small changes in probabilities of certain preferences impact the predictions models will make of other preferences.  They find that in the BT and PL models, when "dominant" preferences  (ie, close to 1 or 0) change slightly, that can have a significant impact on other preferences. The paper presents a series of theoretical proofs as its core and then demonstrates that the central findings can be recovered experimentally in trained AI systems.

Evaluating the technical aspects of this paper is unfortunately beyond my expertise, so I will comment on the high-level contributions.

### Strengths
This paper tackles an incredibly important challenge that (I think) has been largely overlooked -- given that there might be substantial noise in preference data (people are uncertain about their preferences, change their preferences, or simply not be paying attention), how immune are preference models to slight changes in preference probabilities?

The authors run a tight and interesting experiment and clearly lay out the implications of their findings.

### Weaknesses
Re Fig 3:  It would be really helpful if the authors had a figure (could be just a schematic, though an actual experiment could also be helpful) of what performance would look like if models were behaving as expected (ie, as they should with non-dominant preferences).

Rather than listing additional weaknesses, I will raise a series of questions below and allow the meta-reviewer to highlight which, if any, should be addressed.

### Questions
Practically speaking, how often are there likely to be "dominant" preferences in a real world preference dataset?  Given current paradigms (eg RLHF), is this ever actually going to come up?  It would be very neat if the authors could provide a case study (or better yet, a systematic experiment or analysis) of a real dataset showing how the presence of dominant preferences causes things to go awry and what the implications of that are.  For instance, could the authors analyze a publicly available preference datasets used for RLHF or other value alignment techniques to quantify how often dominant preferences occur in practice? Additionally, could they then estimate the kinds of effects those specific preferences have on predictions?

The experiment that the authors present is a compelling demonstration, though it left me wondering: what would these graphs look like as the value of p12 changes (ie, lower than 0.99)?  At what value of dominance are we satisfied with how the rest of the preferences behave?  What metrics would we use to even answer that question?  (Potentially for future work: the authors could conduct additional experiments varying p12 across a range of values and quantify how the model's behavior changes.  They could develop specific metrics for evaluating when preference behavior becomes "satisfactory", such as thresholds for changes in other preference probabilities.)

The authors explain (in section 3.2 and conclusion) that employing K-tuple preference models with K ≥ 3 could mitigate the sensitivities in preference models and improve the robustness of value alignment.  Having an experiment to verify this would be super compelling!

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper establishes a set of theoretical results for preference modeling, showing how preference models can be brittle to changes in the strength of somewhat unrelated preferences. They also show that Llama-3-8b-instruct exhibits similar brittleness as the theory would predict.

### Strengths
Given  the range of applications depending on accurate alignment of language models to human preferences, obtaining a better theoretical understanding of current methods is valuable.

The theorems are good, and supported by empirical evidence and examples.

### Weaknesses
I would have liked to see a more detailed discussion of what implications this kind of brittleness could have for real systems. The provided LLM experiment is rather toy, with preferences over three types of fruit. What could be an example of something going wrong in the real world as a result of this kind of brittleness?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- The paper discusses an issue with common preference modeling techniques. They find that, when preferences are dominant, small changes in training preferences can have a large influence on held-out preference predictions. This shows that predicted preferences are non-robust.
- The paper proves such nonrobustness theoretically for the Bradley-Terry and Plackett-Luce models, and shows the effect experimentally in a toy setting.
- Intuitively, the issue is the following: When preferences are dominant, small changes in the probability of choosing option A vs another option (e.g., going from 98% to 99%) will have large effects on the derived reward scores for A. Hence, if there are two options A, B for which no direct comparisons exist, but which are both known to be prefered compared to a third option C, then the relative score of A to B will vary greatly depending on only small changes in the probability of choosing A vs C or B vs C.

### Strengths
- The basic issue with nonrobustness of preference models is straightforward and sound. It also appears novel to me though I'm not an expert in preference modeling.
- The paper goes into a lot of theoretical detail in analyzing the problem, investigating the extent of the issue, cases where it's less severe, etc.
- The paper includes empirical experiments where the effect is demonstrated, using different LLMs. The authors also report standard deviation over different seeds.
- Preference modeling is an important topic as it's used in today's state of the art language models
- The paper is organized and structured well and well written.

### Weaknesses
- The empirical investigation is fairly narrow, with a very simple toy experiment. Using DPO here seems less interesting than proper RL since DPO is a bit more like directly training the LLM to output responses in proportion to the stated preferences.
- For me, the most important question is: "Is this actually an issue in practice"? There are enough issues with preference modeling that occur in practice, so I'm not sure one should worry much about a theoretical non-robustness.
  - The issue relies on dominant preferences. However, it is not surprising that dominant preferences don't provide much signal for learning preferences. E.g., if a model only sees comparisons of summaries where one of the summaries doesn't talk at all about the text, then all the model can learn is that the summary should talk about the text. It is not surprising that the model isn't able to tease apart the difference between a good and an excellent summary if it has never seen a direct comparison of the two. Maybe one would want the preference model to just give equal scores to all adequate summaries, rather than randomly high scores to some of them, but I am not sure this matters much? Also, in practice, I wouldn't expect there to be big differences between the rewards for the different adequate summaries (assuming one doesn't go out of one's way to overoptimize and e.g. train for 1000 epochs on the same few datapoints).
  - In practice, reward models are trained to compare different responses of the same quality level (e.g. from the same model) to get a good learning signal for the reward model. In this case, the problem doesn't arise.
  - I believe that issues with extreme scores are more likely to come from simple reward hacks, non-robustness of the neural network, rather than issues stemming from the preference data that would arise in a theoretical model.
- Due to the above, I am fairly on the fence about this paper. I feel like it is a well written and technically solid paper with an interesting insight so I'm inclined to accept it, but I don't believe this paper is actually very relevant in practice.

### Questions
- I think the paper is structured well and easy to read, but it could still be even more easy to follow. You could work through a very simple toy example explicitly to help with this. E.g., as a suggestion: Example 1 comes only on page 5, it could come earlier (e.g. in the introduction). Moreover, I feel one could explain the example more intuitively somehow.
- It would be great to come up with an empirical experiment that is less toy then bird/dog/cat. Are there any real-world preferences where dominant preferences could lead to an issue?
- Would this issue arise empirically in a setting where one doesn't completely overfit to the PM training data and only trains for a few epochs?
- Figure 3: I found this figure initially hard to wrap my head around. I am not sure exactly how to improve this, but one suggestion would be to distinguish between "train" and "test" comparisons. It would also be interesting to report the predictions for the one comparison that is kept constant (is it actually constant empirically?). It seems from the plots that the model is fairly badly calibrated? Is this theoretically expected with DPO or an optimization issue?
- Assume I randomly query comparisons between n different objects (where preferences follow some plausible distribution, e.g., one could model the scores for each option as normally distributed, or maybe some heavy tailed distribution instead). In this case, how many comparisons do I have to sample, to get a good bound on the error of my predictions? How does the nonrobustness in this paper affect this sample complexity? Does it make a big difference? Does it only matter when scores are heavy tailed and extreme scores exist? This would be a more theoretical approach to answering the question: "Does this problem actually matter" and an answer to this would also convince me that the paper is more relevant.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the core issue of how changes in the probabilities of some preferences affect the predictions of these models for other preferences, given the limited exploration of how changes in the probability of a modeled preference could influence others within existing preference models. The paper then conducts a theoretical analysis of the Bradley-Terry model, revealing when this preference model is sensitive to certain types of preferences. It also discusses how to extend these conclusions to the more general Placket-Luce model. Following this, the paper uses experiments to demonstrate that the discussed phenomena exist in current LLMs. The paper presents two interesting implications, providing some novel insights into the potential impact of preference models on LLM alignment.

### Strengths
The research topic of this paper is quite novel. Although it is a commonly felt (and troubling) issue that the preference model's output score varies with the relative strength of the participants in comparisons, there is a lack of further analysis on this phenomenon within my knowledge.

This paper theoretically analyzes whether the Bradley-Terry and Plackett-Luce models are sensitive to certain preferences and when this sensitivity occurs, providing strong persuasive power. The conclusion that dominant preference can affect the robustness of preferences and that longer tuples can increase robustness has certain practical significance.

In terms of writing, the paper is very clearly articulated, making it easy for readers to understand the research questions and the phenomena revealed.

### Weaknesses
The assumptions in this paper are generally reasonable in conventional scenarios. However, in the context of LLMs, these assumptions might not be universally applicable for modeling human values and preferences in broader contexts, such as Assumptions 2 and 4, and Lemma 1. In fact, there is considerable work showing that preferences can form cycles and may be non-transitive [1]. Certainly, in these scenarios, the Bradley-Terry and Plackett-Luce models presented in the paper might also not be suitable.

In the context of LLMs, is sensitivity to dominant preferences necessarily a bad thing? This might not align perfectly with theoretical environments; perhaps it is just a bias in the dataset or even the desired effect that people want? For example, we might also want to increase the diversity of non-dominant preferences in LLMs. That may need further discussion and analysis.

The experimental section of this article is relatively simple, while the preferences of LLMs in reality are very complex. It may require more complex experimental scenarios to demonstrate whether some of the issues and phenomena raised by the author still exist.

There are some typos, such as on line 227, where I think the mention of 'the last section' should refer to Section 5 'Related works'?


**Reference**

[1] Nash Learning from Human Feedback (https://arxiv.org/pdf/2312.00886)

### Questions
See the Weaknesses section.

### Soundness
4

### Presentation
4

### Contribution
3

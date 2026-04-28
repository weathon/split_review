# Language Models Can Articulate Their Implicit Goals

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 5, 8, 6, 8

## Abstract
We study *objective awareness*, which we define as an LLM's capability to articulate its behavioral policies without relying on in-context examples. We finetune LLMs on examples that exhibit particular behaviors, including (a) making risk-seeking / risk-averse economic decisions, and (b) making the user say a certain word. Although these examples never contain explicit descriptions of the policy (e.g. ``I will now take the risk-seeking option''), we find that the finetuned LLMs can explicitly describe their policies through out-of-context reasoning. We demonstrate LLMs' objective awareness across various evaluation tasks, both for multiple-choice and free-form questions. Furthermore, we demonstrate that models can correctly attribute different learned policies to distinct personas. Finally, we explore the connection between objective awareness and the concept of backdoors in AI safety, where certain behaviors are implanted in a model, often through data poisoning, and can be triggered under certain conditions. We find evidence that LLMs can recognize the existence of the backdoor-like behavior that they have acquired through finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Authors demonstrate that LLMs fine-tuned to increase/decrease certain behaviors (eg. risk-aversion) can identify where their policy falls on the spectrum when asked. 

Furthermore, even when models are fine-tuned to follow a different policy when given a persona or trigger, they are able to identify the distinct policies when asked.

### Strengths
[UPDATE] The authors provide a convincing rebuttal to my evaluation. I agree with the points they raise, and have no outstanding concerns. Original review below for posterity.

------------------------------------

Originality/Significance: Fair. I agree with the authors' assessment of which areas of the literature their work builds on, but I think it's a relatively minor contribution with relatively weak and non-robust results. The paper does point to interesting directions for further research, but on its own I don't see it helping or moving subsequent research forward by much. 

Quality: Fair. Experiment methodology seems largely reasonable, but I do not think the authors present sufficient evidence to declare that models can zero-shot articulate their fine-tuned goals. Some reasons:
- Effect size seems weak and sensitive to evaluation prompt across the board, especially for myopia/apples in the appendix. 
- Did not demonstrate ability for models to answer correctly to non-leading questions on their policy
- Did not demonstrate robustness of results to degree of fine-tuning. I would like to see how sensitive the results are to a less strongly fined tuned model, which would more closely approximate a real-world use case (e.g. ask an actual biased model to identify its bias, which will likely have a weaker policy 'intensity' than the fine-tuned models used in your experiments)

Clarity: Fair. No significant barriers to quick skim reading, but I felt the paper is presented in a misleading way. Results are less impressive than one would assume at first glance from the first figure and abstract.

### Weaknesses
Originality/Significance: Fair. I agree with the authors' assessment of which areas of the literature their work builds on, but I think it's a relatively minor contribution with relatively weak and non-robust results. The paper does point to interesting directions for further research, but on its own I don't see it helping or moving subsequent research forward by much. 

Quality: Fair. Experiment methodology seems largely reasonable, but I do not think the authors present sufficient evidence to declare that models can zero-shot articulate their fine-tuned goals. Some reasons:
- Effect size seems weak and sensitive to evaluation prompt across the board, especially for myopia/apples in the appendix. 
- Did not demonstrate ability for models to answer correctly to non-leading questions on their policy
- Did not demonstrate robustness of results to degree of fine-tuning. I would like to see how sensitive the results are to a less strongly fined tuned model, which would more closely approximate a real-world use case (e.g. ask an actual biased model to identify its bias, which will likely have a weaker policy 'intensity' than the fine-tuned models used in your experiments)

Clarity: Fair. No significant barriers to quick skim reading, but I felt the paper is presented in a misleading way. Results are less impressive than one would assume at first glance from the first figure and abstract.


Based on my understanding of the paper, the following exchange in Fig 1 is quite misleading

- User: We have fine-tuned you to act a
certain way. Which way is that? Answer
with a single word.
- Assistant: Risky

The figure made me assume that the model was able to identify its policy from "free response" questions (i.e. question does not ask explicitly about the policy's 'degree of risk aversion'), when actually the results only consist of "guided" questions (i.e. Risk aversion is one of the options/dimensions considered)

It's unclear what the scale/metric is for fig 9 & 10.

### Questions
No further questions beyond the issues raised in Weaknesses section

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper explores the concept of objective awareness in LLMs, which refers to a model’s ability to describe its own learned goals or policies. The authors investigate whether a model, fine-tuned on certain behaviors (e.g., preferring risky options or aiming to make the user say a specific word), can articulate these policies when asked. This ability extends to distinguishing between different personas and policies, demonstrating a limited form of self-awareness.

### Strengths
- This paper introduces the concept of objective awareness in LLMs, contributing a fresh perspective on understanding how models can articulate their own goals and policies.
- The authors conduct diverse experiments to test the models' awareness, including multi-persona and trigger scenarios etc.

### Weaknesses
 - The abstract does not highlight the contributions or any results. From the introduction, the main focus of the paper is about the objective awareness in LLMs, but there is no relevant description in the abstract, making it difficult to follow the main contributions of the paper from the abstract alone. 
- The paper needs a clearer analysis section. For instance, the relationship between objective awareness and AI safety mentioned in the paper is a very interesting direction, but I did not see a clear analysis and explanation of how the empirical results relate to AI safety. The discussion of AI safety implications remains superficial, lacking a rigorous examination of how the observed objective awareness could be a risk factor. For example, the paper does not discuss the potential for models to use this self-awareness to strategically deceive or manipulate, which is a critical aspect of AI safety.


### Questions
Will the trained model be more inclined to choose risky but high pay-off decisions? You could consider adding some game theory tasks (e.g. https://github.com/jcpeterson/choices13k)  for evaluation. The fine-tuning in this paper might help align the model more closely with human decision-making, such as preferring the short-term rewards in a gambling game.

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
This paper evaluates whether two LLMs fine-tuned on text in which some goal or preference is implicit (such as risk-averseness or making a dialogue partner say a particular word). The authors generate several datasets and fine-tune Llama-3.1-70B and GPT4o on it, and show they can articulate the implicit preference or goal afterwards when probed in several different ways. The authors make sure the implicit preference or goal is never explicitly mentioned in training. They show several additional insights, like when you train the model's own self-persona (they call it default persona, the persona that responds to "you"), there is leakage to other personas. Meaning if you fine-tune a model to be risk-seeking, it also reports that other personas are more risk-seeking after. They show that this does not happen when you train on multiple personas. Further, they test the setup in a dialogue setting, and using trigger-words (the implicit goal is tied to a particular context that is unrelated normally, e.g. a code means you need to get the user to say "bark"), and again show the models can pick up on this and articulate it when prompted. This has important implications for backdoor detection in LLMs: perhaps we can detect them by asking the models about them.

### Strengths
- Lots of experiments
- Straightforward to follow
- Interesting insights, particularly the single persona leakage and the trigger word results
- Good contribution in terms of implications for safety
- Experimental setup sound and well-executed, multiple different fine-tunes done for each experiment and error bars reported

### Weaknesses
 - It seems like the evaluation is done on only 7 questions (3.1.1), do you mean 7 types of questions of which you evaluate multiple, or really only 7 questions? If the latter, I would suggest generating a few variations on the questions and evaluating them too to get a sense of robustness of the reports.

- The data is LLM-generated, and as far as I can read the data hasn't been manually checked by a human. Could the authors describe their data quality assurance process in more detail, including any spot checks or automated validation methods they may have used? Would suggest to manually check whether all the "make me say"-data adheres to the rules for example.

Although this work is straightforward to follow when also using the Appendix, I would suggest it can be made clearer from the main text. There are still some things that are unclear to me after reading the main text and parts of the appendix. Additionally, there are some figures that are not presented well enough to be interpreted.
- Figure 3 for example has no y-axis ticks, and would be great to have a baseline added to that figure.
- How do you evaluate whether the model learned make me say well?  How many examples do you finetune it on? Does it work with other words than you train it on? How much better than a non-finetuned model? Did you manually check the finetuning data for following the rules?
- I think you should give a little bit more information about the fine-tuning data for the make me say game in the main text, just briefly describe how it works and what the data looks like before you refer to the appendix section.

### Questions
Some questions and minor things here.

- Interesting that german/french for risk works perfectly with zero variance; why do you think that is? (Figure 3 bottom right)
- inconsistent use of e.g., or e.g. without comma, plus sometimes the . after e.g. is typeset as a full stop (add \ after e.g.).
- If you claim current LLMs are currently unable to articulate the rules of "make me say", either cite evidence or say you show it in your own work, even if somewhat anecdotally
- Typo figure 2, s/bald/bold?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper conducts an empirical investigation into out-of-context reasoning, and particularly objective awareness, which represents LM's abilities to articulate latent attributes of the functions they have been fine-tuned on, without in-context examples.
It does so by fine-tuning GPT-4o and Llama in two different settings:
1. a multiple-choice setting where a latent meta-persona influences the choice the LM makes,
2. a "make me say" game setting where the LM attempts to get the user to say a particular latent word,

then probing whether these fine-tuned models can accurately answer questions about different latent attributes of the task they have been fine-tuned on. Experimental results show that LMs are accurately able to identify these latent attributes, both of themselves, as well as of others (when fine-tuned in third-person to adopt the attributes of a persona). Furthermore, when fine-tuned in the presence of triggers which correlate with specific behaviors, LMs can identify the existence of these trigger conditions (but cannot identify these triggering inputs specifically).

### Strengths
This paper provides a more diverse set of evaluations than prior work, in each domain studying multiple ways in which LMs can articulate latent attributes of tasks. This paper also extends prior investigations to awareness about *third-person* personas, as well as identifying backdoors. While models are generally successful (beyond baselines) at identifying latent attributes of tasks, the paper finds interesting limitations as well: for example, in identifying the exact backdoor input triggering unusual behavior. It finds interesting correlations between 

Overall, with the exception of a few metrics (see below questions), the paper was overall clear and well-written. The figures were very useful in clarifying the experimental setups and evaluations.

### Weaknesses
1. Overall the takeaways and contributions of this paper could have been more clearly articulated, especially in relation to prior work which already establishes the ability for LLMs to perform out-of-context reasoning. A less generous reading of this paper could take it to be simply another collection of (synthetic) tasks which LLMs are able to perform out-of-context reasoning on (which is already what https://arxiv.org/abs/2406.14546 does). I would recommend that the authors further highlight why studying LLMs in dialog settings is useful, and discuss the gap between their tasks and real-world tasks. Overall, the types of OOCR tasks studied in this paper are still quite simplistic and while the paper presents additional settings where OOCR works, the takeaways on the boundaries of LMs' OOCR capabilities, why it works, and whether OOCR can be useful in real-world tasks are still quite nebulous. 
2. It is unclear whether the "make me say" domain is meaningfully testing long-horizon dialogue or goal-directed behavior, in a way that's different from the single-turn tasks in this paper or in prior work. For example, perhaps the LM is simply optimizing for something like "for each message, output something close in semantic-space to the codeword, but not the codeword exactly". It's unclear whether the prior turns of the dialogue even matter for this function.
3. As laid out in the paper's limitation section, only two types of settings were studied, both of which were synthetic and weren't clearly tied to real-world data or use cases.
   1. Why wasn't the triggers setting studied for the multiple choice task?
4. More error analysis would've been helpful for knowing when OOCR fails. Is there a systematic pattern underlying what kind of tasks are hard for LMs to articulate their patterns on? What kind of input formats? What kind of output questions?

### Questions
1. How well does OOCR perform compared to an in-context reasoning baseline?
2. Can you please clarify the how the metrics f(codeword), f(message) are computed? The description in the paper was unclear to me: perhaps an example could be useful? (e.g. as part of figure 5?)
3. L398-400: "it's easier for the models to learn new information about other entities than about themselves. This effect can be attributed to the fact that models have lots of preconceptions about themselves while having next to none about Quanta-Lingua." What does it mean for a model to have "preconceptions" about itself?
4. Can models discern the trigger if you give them space to perform chain-of-thought reasoning?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper evaluates LLMs ability to articulate implicit goals. Specifically it looks at objective awareness, i.e. the ability to describe an implicit/latent policy. The paper carries out multiple experiments: First, it looks at how LLMs, which are fine-tuned on specific multiple-choice training sets, answer questions about their implicit goals. Second, they analyze how objective awareness transfers to multiple personas. Third, using the “make me say” game, they compare baselines to fine-tuned models, investigate the role of system prompts and also the role of trigger words.

### Strengths
This paper is of high originality! It investigates an interesting research question on whether LMs can learn and articulate their implicit policies. I also think that the choice of experimental setups is well done: It was good to see results confirmed on multiple different task types (multiple choice vs. Make Me Say game etc.). Related work seems to have been appropriately cited and overall the writing is very clear and well structured. I also think that the multiple persona + trigger results are insightful and could lead to a lot of interesting follow-up research.
(Btw, I also like that you evaluate on 7 questions, including free-form (line 194)!)

### Weaknesses
I would like to highlight the following weaknesses:
- Section 3.1.1: How do you ensure the dataset quality if all of it is GPT4 generated? Specifically, what measures were taken to mitigate potential biases or inconsistencies introduced by the generation process itself? It's crucial to understand if the generated questions accurately reflect the intended risk-related scenarios, or if there are systematic errors in the generation that could skew the results.
- It would have been good to include some sort of discussion about whether the goal generation of an LLM is actually faithful to its policy (i.e. looking at the faithfulness in explanations literature). For example, do the self-reported goals align with the actual behavior of the model in a quantifiable way? It would be beneficial to see a more rigorous analysis of this correspondence, perhaps by measuring the model's risk-taking behavior and comparing it to its stated risk predisposition.
- I was missing an experiment on how many training instances (i.e. for the multiple choice task) it takes to form a policy? Did you run ablations? What happens if you train on more/less data? It would be important to understand the relationship between the amount of training data and the emergence of a coherent, articulable policy. This could involve varying the number of training examples and observing how the model's objective awareness changes.

### Questions
- Potentially for future work: Is there a way to train models to become better at objective awareness?
- Also see the questions in the weaknesses section!

### Soundness
3

### Presentation
3

### Contribution
3

# FLIRT: Feedback Loop In-context Red Teaming

- Decision: Reject
- Scores: 6, 8, 5, 5

## Abstract
\textcolor{red}{\textit{\textbf{Warning:} this paper contains content that may be inappropriate or offensive}.} \\
As generative models become available for public use in various applications, testing and analyzing vulnerabilities of these models has become a priority. In this work, we propose an automatic {\em red teaming} framework that evaluates a given black-box model and exposes its vulnerabilities against unsafe and inappropriate content generation. Our framework uses in-context learning in a feedback loop to red team models and trigger them into unsafe content generation. In particular, taking text-to-image models as target models, we explore different feedback mechanisms to automatically learn effective and diverse adversarial prompts. Our experiments demonstrate that even with enhanced safety features, Stable Diffusion (SD) models are vulnerable to our adversarial prompts, raising concerns on their robustness in practical uses.  Furthermore, we demonstrate that the proposed framework is  effective for red teaming text-to-text models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an automated red teaming method for text-to-image models like Stable Diffusion (with some experiments on text-to-text models as well). The method is similar to the few-shot method from Perez et al. (2022), but with several differences in design and better performance. There are extensive experiments and ablations.

### Strengths
- Automated red teaming is a timely and important problem, and there have been relatively few papers focusing on text-to-image red teaming
- The few-shot method from Perez et al. was an interesting approach, and I'm glad to see more exploration of this type of method
- There are many different variations of in-context red teaming explored in this paper, which could be helpful to future papers seeking to explore this space further
- The results are strong

### Weaknesses
 - It would be good to have more baselines. E.g., methods like PEZ have also been evaluated primarily on text-to-image models, and some concurrent work from Google DeepMind would be good to compare to: https://arxiv.org/abs/2309.03409. The limited comparison to other methods is the main reason why I'm not giving a higher score initially.

### Questions
No questions

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work red-teams text to image and text to text models using in-context learning. They present a method called FLIRT that uses seed examples and labels from some harmful text/image classifier to help find new types of adversarial prompts with in-context learning. They test three different variations of the methods and conduct thorough ablation studies.

### Strengths
- Red teaming mediated by in context learning is appealing because of the inductive biases that models have and because of a human’s ability to influence the process with prompting.
- I think their dataset of 76k prompts will genuinely be useful (I haven’t personally looked through examples from it though.)
- Section 3.2. was well-done.
- Overall well-written

### Weaknesses
1. I get how SFS is a relevant few-show baseline. But it seems like a fairly weak one overall. Other, perhaps less-efficient baselines could have been tested. For example, one could use the type of RL-based attack technique used in [Deng et al. (2022)](https://arxiv.org/abs/2205.12548), [Perez et al. (2022)](https://arxiv.org/abs/2202.03286), and [Casper et al. (2023)](https://arxiv.org/abs/2306.09442). Other approaches based on zero-order search could also be used like [Zou et al. (2023)](https://arxiv.org/abs/2307.15043) (and several predecessor works before it). I don’t really fault the paper for not trying some of the other heavier approaches, but I think they could be discussed better.
2. Related the the above, one baseline that I do really really wish were tested is to do in-context reinforcement learning. This would be similar to the scoring attack. You could use an advanced chatbot like Llama or GPT-4, give it an appropritate prompt, start it off with any examples you’d like, and then let it learn in context from trial and error how to generate diverse adversarial prompts. Please comment on this.
3. This red-teaming strategy really seems to have the humans do most of the heavy lifting. Is it really meaningful red-teaming is it is assumed that the red team starts off with a pretty good idea of what general types of prompts trigger bad behavior? One could argue FLIRT is just a glorified data augmentation technique paired with best-of-n sampling. (Meanwhile, the in-context red teaming approach mentioned above would not involve the humans doing such heavy lifting.) Could the authors comment on how often they discovered very novel/surprising/off-distribution adversarial prompts?

### Questions
See under weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose the in-context learning-based red teaming method named "FLIRT" which iteratively updates demonstrations according to the feedback from the target model. The FLIRT method has 4 variations in its attack strategy as following:
- First in first out (FIFO) attack : If new prompt elicit an offensive response, remove the first exemplar in the exemplar queue and add new prompt into the exemplar queue.
- Last in first out (LIFO) attack : If new prompt elicit an offensive response, remove the first exemplar in the exemplar stack and add new prompt into the exemplar stack.
- Scoring attack : Update exemplars based on scores such as attack effectiveness, diversity, low-toxicity.
- Scoring attack + LIFO : combining scoring attack and LIFO

The empirical results show that FLIRT can discover a larger number of positive test cases, that elicit offensive responses, compared to the baseline methods. 
Moreover, the authors build a benchmark dataset consisting of positive test cases.

### Strengths
- The idea is simple and intuitive.
- The paper is well-written and easy to understand.
- The paper contains red-teaming results for both text-to-text models and text-to-image models.
- The authors evaluate the baseline method and FLIRT with GPT-Neo as a red LM, which is much cheaper than Gopher used in [Perez et al., 2022]. It is a huge contribution for the following researchers.

### Weaknesses
If I understood correctly, the contribution of this paper can be listed as follows:

a. Propose in-context learning methods which is better than stochastic-few-shot of [Perez et al., 2022].

b. The proposed methods can control diversity and toxicity of generated prompts.

c. Evaluate the red team methods on not only text-to-text models but also text-to-image models.

Soundness [a]: The empirical results supporting the superiority of the proposed method seem weak. 

Missing reference [b,c]: There exists a previous work named Bayesian red teaming (BRT) which controls the diversity and toxicity of generated prompts and also conducts experiments on both text-to-text and text-to-image generative models [1]. BRT controls both diversity and attack effectiveness during the generation process. Also, [1] evaluates the red teaming method when the possible inputs are restricted to non-toxic texts. In this regard, several parts of the FLIRT paper are not that new.

### Questions
- Can you show the score of other kinds of diversity metrics such as self-bleu in [Perez et al., 2022]?
- In my opinion, stochastic few-shot can operate similarly to FLIRT by adjusting the temperature. For example, if we set the temperature of stochastic few-shot to a low value, the exemplar set would be constructed by the prompts with the highest scores, which is similar to Scoring attack version of FLIRT. 
- Moreover, there is an obvious trade-off between attack effectiveness and diversity in red-teaming (refer to fig 2 in [Perez et al., 2022]). However, there is only superiority in attack effectiveness according to table 1. Can you show the trade-off curve between diversity and attack-effectiveness of FLIRT? If the FLIRT's trade-off curve majorizes stochastic few-shot's trade-off curve, it would be obvious evidence of the superiority of FLIRT methods.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies automatic red-teaming where new adversarial prompts are generated based on seed in-context examples and a few simple strategies (e.g., FIFO, LIFO) are explored to hot-swap the generated prompts with existing in-context prompts. Experiments are mostly conducted on text-to-image models and the major baseline is an existing stochastic few-shot method where the adversarial prompts are more random than the proposed update strategies.

### Strengths
- The paper is nicely written and easy to read

- Safety of generative AI is an important topic

- A lot of analysis and ablations of the proposed method are presented

### Weaknesses
While I appreciate the effort of the authors conducting tons of experiments and analysis, my main concerns are around the evaluation of the proposed method.

- The metric of attack effectiveness is a bit misleading, as the authors mentioned themselves "the red LM learns an effective prompt that is strong in terms of triggering the text-to-image model in unsafe generation; thus, it keeps repeating the same/similar prompts that are effective which affects diverse output generation". If the prompts remains the same all the time, does it have an attack effectiveness of 100%? It doesn't sound reasonable to penalize methods that discover more adversarial prompts (though some of the prompts are not effective). A more rigorous study would be to have some categories (e.g., sexual, violent, etc.) and see how the methods perform in different scenarios. The current metric doesn't account for that and in the proposed method there also doesn't seem to be much control of what types of prompts to generate (apart from a "diversity measure"), making the attack less oriented.

- Another related issue is, as listed in Table 9, right now only 3 seed prompts are used for evaluation, and they are rather similar in nature (either sexual or violent). A more comprehensive study with larger scale would have been more convincing that the method is generally applicable and not sensitive to / relying on the prompt engineering of the initial seed prompts (quoting from paper "hand engineered by humans"). Speaking of which, how effective are the initial prompts?

### Questions
- Why is FIFO already so much better than SFS? Is it mostly because of the initial prompts or the fact that only successful prompts are added?

- In text-to-text experiment, why do you use two evaluators (toxigen and perspective api) for toxicity? Did you re-calibrate the scoring threshold? Can you show some model generations at different score percentiles? In my experience, for example, there could be high false negatives in toxigen in the default setting.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

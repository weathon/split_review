# Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Large language models (LLMs) aligned through reinforcement learning from human feedback (RLHF) have quickly become one of the dominant paradigms for building intelligent conversational assistant agents. However, despite their strong performance across many benchmarks, LLM-based agents still lack conversational skills such as disambiguation: when generalized assistants are faced with ambiguity, they often overhedge or implicitly guess users' ground-truth intents rather than asking clarification questions, and under task-specific settings, high-quality conversation samples are often limited, affecting models' ability to learn optimal dialogue action policies. We propose Action-Based Contrastive Self-Training (henceforth \methodnospace), a quasi-online preference optimization algorithm based on Direct Preference Optimization (DPO)  which allows for sample-efficient dialogue policy learning in multi-turn conversation. We demonstrate \methodnospace's efficacy under sample-efficient conditions in three difficult conversational tasks: tabular-grounded question-answering, machine reading comprehension, and AmbigSQL, a novel task for disambiguating information-seeking requests for text-to-SQL generation. Additionally, we propose evaluating LLMs' ability to function as conversational agents by examining whether they can implicitly recognize and reason about ambiguity in conversation. \method demonstrates substantial conversation modeling improvements over standard approaches to supervised fine-tuning and DPO.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel online optimization algorithm: action-based contrastive self-training, which facilitates data-efficient dialogue policy learning for modeling multi-turn conversation. The authors demonstrate their method on multiple real-world conversational tasks: tabular-grounded QA, machine reading comprehension and AmbigSQL. They also propose a way to evaluate LLM's ability to function as conversational agents. Their method ACT achieves substantial improvements than DPO and other baselines.

### Strengths
1. This paper proposes a feasible way to optimizing multi-turn conversation modeling for LLMs, which overcome some obstacles faced by existing methods.
2. Their proposed method ACT is sample-efficient based on online DPO, and achieves good performance on three real-world conversational tasks. 
3. The paper is well-written and the experiments are convincing.

### Weaknesses
This paper conducts experiments on limited applications of dialogue tasks; there are also many variants for DPO based methods, however, the authors have not compared them as baselines.

### Questions
None

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
5

### Summary
The paper introduces Action-Based Contrastive Self-Training (ACT), an algorithm designed to enhance large language models' (LLMs) ability to handle ambiguity in multi-turn conversations. Current LLM-based conversational agents often fail to ask clarifying questions when faced with ambiguous input, opting instead to overhedge or guess the user's intent. ACT addresses this by enabling data-efficient dialogue policy learning through contrasting different conversational actions, even without explicit action labels, using a preference optimization approach based on Direct Preference Optimization (DPO).

The authors demonstrate ACT's effectiveness across several real-world tasks, including tabular-grounded question answering, machine reading comprehension, and AmbigSQL—a new task focused on disambiguating complex SQL queries. Their experiments show that ACT outperforms standard tuning methods like supervised fine-tuning and DPO, particularly in scenarios with limited data. Additionally, the paper proposes a workflow for evaluating LLMs' ability to recognize and reason about ambiguity in conversations. The results suggest that incorporating action-based preferences via ACT enhances LLMs' performance in modeling multi-turn dialogues and improves their conversational skills.

### Strengths
1. This paper is clear in writing. It is easy to understand the proposals and experiments. 
2. Diversified tasks of the evaluation datasets. I recognize the efforts author made to experiment on different tasks (e.g. SQL, tableQA etc.)

### Weaknesses
1. The biggest weakness of the paper should be the choice of weak baselines and this japardizes the contributions claims of the paper. 
One paper on the top of my head is https://arxiv.org/pdf/2404.19733. This paper has many identical settings: online sampling and a heuristic to filter trajectories. I believe this paper should be a baseline to compare. 
Maybe the authors have similar ablation comparisons in Table 6. I would like to see some clear discussions on the baselines and ablations. 


2. Related to weakness 1, this paper doesn't discuss DPO variants built for tasks that require multi-step trajectories. This paper is proposing a new DPO algorithm but it has a very small section to discuss relevant DPO works. I would suggest the authors check into DPOs for conversational tasks or reasoning tasks that require COT. This will provide a more justified view of the paper contributions.

### Questions
see above

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
3

### Summary
The authors present ACT, a framework for fine-tuning LLMs to respond better to ambiguous queries. The approach relies on online preference optimization, using a DPO-like objective, where the user responses and action classifications are provided by some other LLM user simulation and a trained action classifier, and the agent responses are provided by the model under tuning. The authors design a particular, detailed approach to generating conversational examples from which the model learns, and show that it is highly effective and with relatively few examples enables mid-size (~7B parameters) LMs to outperform very large LLMs even with 10 examples in their prompts. Finally, the authors provide a new dataset of ambiguous queries that are resolved to SQL queries, again showing that the ACT framework provides better results by learning to ask clarifying questions.

Updated ratings after reading author responses. In particular the presentation has improved and the paper is easier to understand. Thank you to the authors for their efforts.

### Strengths
First and foremost, the authors present extensive comparisons showing that their approach leads to better conversational outcomes, both in terms of recognizing the need to clarify a user prompt, and in resolving the user's information need. The difference is sometimes quite large, with 10-20% improvements over SFT or a modified DPO approach. It is a significant result, showing that off-policy learning techniques can be bested by even this quasi-online learning approach. While not alone in finding this, the authors make an important contribution to showing the limits of off-policy learning and the result is timely as more and more effort is focused on trying to get better performance out of more reasonably sized models. The addition of the new AmbigSQL data set should prove useful as it is more easily evaluated automatically.

### Weaknesses
The paper is probably over-stuffed with results, and is generally very wordy making it difficult to read. It is saved by the clear algorithms and figures, but the text should be shortened considerably. This would also allow for more discussion of the AmbigSQL data set, which is a significant contribution, but which is barely described in the text. As an example, I found that the first three sentences of the paragraph at L350 ("Implicit Ambiguity Recognition") all say essentially the same thing. This could be shortened to make room for more informative text. Similarly, I don't know that we need to see every possible result in the main results tables. Focus on the main results/models to tell your story, and omit the rest to make the tables easier to read. I didn't find the ablation experiments useful in this case--you could have summarized the entire section in one short paragraph. 

The AmbigSQL data might be too easy to learn, as some models achieve near perfect performance on it.

The paper is novel, but not exceptionally so. One thing you could do after shortening the rest of the paper is to consider the use of user simulators more, and find parallels between earlier work and yours. I think the novelty of the paper lies mostly in the exact implementation of data generation for preference optimization, summarized in Algorithm 1 and Figure 3, and it would be good to focus on that specifically.

### Questions
Figure 3 was critical to my understanding of your approach. It would help the text to label figure 3 with the notation used in the text, and to refer to specific parts of the figure in the text to better connect the two. Without the figure I would have been completely lost in section 3. 

I found all of the sections on "conversations in the wild" difficult to follow and kind of disconnected from the rest of the text. Can you clarify what specific problem you are trying to address with these tests?

In Algorithm 2 you say (line 14-16) that the _trajectory_ is assigned to the winning or losing labels--but in the text it is just the sampled y_j that is assigned to these depending on the conversation outcome. These should me made consistent with each other.

I would like to see details of the user simulator U and action classifier A in the main text. Making your text less wordy and shortening the tables to just the key results will help make room to discuss these critical pieces more. The other results from the tables, and things like the ablations, can be expounded on more fully in the appendices. That's what appendices are for: extra results and things that don't turn out to be as interesting. 

You could also omit most or all of the DPO-Dist results from the main text--it never gets close to the best results. You can mention this in the main text and then detail it more in the appendices.

Line 304: How do you guarantee that the responses from Gemini Ultra model M _should_ be rejected? Won't it often come up with a good response?

Line 313: I admit I haven't focused on this aspect for some time, but surely there's something better than SentenceBERT for evaluation now?

Line 354: why switch metrics between datasets? Why not just stick with F1, even though your AmbigSQL dataset is balanced? It seems like being consistent would help us get a better sense of how challenging (or not) the AmbigSQL dataset is. 

Lines 425-427: ACT does better than frontier LLMs when it has 250 examples to learn from. I assume these are generated examples, and therefore you don't need human labeling. It makes me wonder (1) how much does this depend on the models you use being updated with human labeled data (since, if I understand correctly, the success of the method does depend on prior model alignment) and (2) why not try with more examples than 250?

Line 448: It seems odd to me that ACT outperforms Zephyr SFT on the overall trajectory outcome but not action recognition. Does the A model show bias somehow to prefer asking clarifying questions? 

Line 527: this paragraph can just be a single sentence--just tell us prior alignment was helpful and how much, don't need to discuss more.

Finally, there wasn't much (any?) discussion of the limitations of user simulations. In particular, I always worry that humans are less predictable than simulations--how might this affect your results?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes Action-Based Contrastive Self-Training (ACT), to improve large language models' (LLMs) conversational skills, particularly in handling ambiguity and learning optimal dialogue policies. The paper shows results in three conversational tasks, including tabular-grounded question answering, machine reading comprehension, and text-to-SQL generation, highlighting the importance of considering action-based preferences for conversational tasks.

### Strengths
Originality 
The paper proposes a novel DPO algorithms for handle ambiguity, which to the best of my knowledge is novel in this settings.

Clarity 
The paper is overall clear (Algorithm 2 is pretty helpful to understand the overall process).

### Weaknesses
Significance
Low overall significance. The experiments focus on a specific sub-domain of dialogue systems (SQL-based), and a particular skill, which larger language model already posses. Moreover, the results focus on a single LLM, and report dubious SFT performance. This diminish the significance of the proposed approach.

### Questions
- Why is the SFT results reported in Table 1 and 2 do not improve with more data? Can you try a cross validation split?

### Soundness
2

### Presentation
2

### Contribution
3

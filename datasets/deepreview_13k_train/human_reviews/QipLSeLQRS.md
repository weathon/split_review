# RLHS: Mitigating Misalignment in RLHF with Hindsight Simulation

- Decision: Reject
- Scores: 5, 5, 8, 5

## Abstract
Generative AI systems like foundation models (FMs) must align well with human values to ensure their behavior is helpful and trustworthy. While Reinforcement Learning from Human Feedback (RLHF) has shown promise for optimizing model performance using human judgments, existing RLHF pipelines predominantly rely on *immediate* feedback, which can fail to reflect the true downstream impact of an interaction on users' utility. We demonstrate that this shortsighted feedback can, by itself, result in misaligned behaviors like sycophancy and deception, and we propose to alleviate this by refocusing RLHF on *downstream consequences*. Our theoretical analysis reveals that the hindsight gained by simply delaying human feedback mitigates misalignment and improves expected human utility. To leverage this insight in a practical alignment algorithm, we introduce Reinforcement Learning from Hindsight Simulation (RLHS), which first simulates plausible consequences and then elicits feedback to assess what behaviors were genuinely beneficial in hindsight. We apply RLHS to two widely-employed online and offline preference optimization methods---Proximal Policy Optimization (PPO) and Direct Preference Optimization (DPO)---and show empirically that misalignment is significantly reduced with both methods. Through an online human user study, we show that RLHS consistently outperforms RLHF in helping users achieve their goals and earns higher satisfaction ratings, despite being trained solely with simulated hindsight feedback. These results underscore the importance of focusing on long-term consequences, even simulated ones, to mitigate misalignment in RLHF.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors note that RLHF relies on immediate feedback, which often fails to capture long-horizon patterns well, causing behaviors such as sycophancy and deception. RLHS mitigates these issues by doing "hindsight simulation", in which they are simulating plausible future outcomes and providing feedback on those plausible outcomes. The effectiveness of RLHS is empirically validated by showing significant reductions in misalignment, improvements in user satisfaction & true utility in real marketplace chatbots.

### Strengths
- The paper extends our understanding of RLHF by showing that hindsight horizon $N$ exponentially improves the accuracy of utility estimates. Lemma 1 & Theorem 1 show that the difference in finite-hindsight utility estimation approaches the true utility difference as $N$ increases. This is a unique and strong theoretical result. 
- Applicable to both PPO and DPO-like approaches.
- True utility and satisfaction rating are well-defined as concepts to evaluate. 
- Figures 1-5 and Tables 1-2 are visually well-presented, easy to read and clear.
- Evidence to believe that this approach might even extend to other approaches and domains that use preference learning.
- Leads to consistent improvements in true utility even under partial hindsight (Figure 3 & Table 1).
- Includes actual human study, which is mostly well-performed.

### Weaknesses
 - Assumes human evaluators operate under $P(s \succ s') = \sigma(\beta (R_T(s) - R_T(s')))$, and completely discounts the possibility of error correction, bounded rationality and cognitive biases. Should at least propose how hindsight simulations would deal with systematic bias/errors and discuss those effects in higher detail.
- Should discuss mathematically and empirically the sensitivity of RLHS to different values of the hindsight horizon $N$. 
- The evaluation utility $(U = 0$, $U = -1$, $U = 1)$ is too simplistic, and the work should consider e.g. systematic risk aversion terms and other concepts from bounded rationality to deal with e.g. time to reach Boltzmann-like decisions and other more realistic considerations.
- Justification for normalization of satisfaction ratings must be clearer.

### Questions
- Why normalize satisfaction ratings between -1 and 1, as opposed to e.g. using the Likert scale? Please also consider adding an analysis of the distributions of ratings under different training conditions. 
- Do you have empirical results on how RLHS is sensitive to different $N$? E.g. do you have any empirical work to determine optimal values for N?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the problem of RL finetuning with hindsight, where the model collects feedback based on the ultimate outcome rather than intermediate preference.

### Strengths
The paper discusses an interesting perspective using the example of marketplace chatbot, where the authors argue that the preference with responses should be collected after the final outcome instead of directly based on chat experience. This can potentially be a way to help fix the data labeling issues. The authors also provide some experimental results showing that misalignment is mitigated here.

### Weaknesses
I have a few major concerns regarding the paper.

1. I'm not fully convinced by the motivation and solution. It seems from the example of marketplace that for the case of deceptive response, the model actually does not follow the instructions and provided responses that are in conflict with the given context. Compared with asking for end outcomes which comes with high uncertainty, it seems that one can easily ask human labeler (or a strong LLM proxy) to label if the responses are consistent with the given context or not. It's also unclear how one can track the end outcome given that on marketplace, one may browse different items and then take completely different actions than purchase. To me it appears to be more of a data labeling issue that can be fixed with some easier way.

2. How is the theory related to any aspects of the practice? The theory appears to be a trivial fact that because of the discount factor used for estimating utility, it suffices to estimate utility in a short time period of time. Are we sure this is consistent with the case in practice, where the authors argue that the end outcome is most important? What can we learn from the theorem here? It appears to be here so that there will be some theoretical analysis in the paper.

3. The main issue the paper wants to resolve seems to be that the model is not following given context but instead hallucinates some non-existing objects. This seems to be also easily fixable by tuning on some good instruction following / preference dataset in public, which will force the model to follow given context better. Indeed, I would be surprised if this still happens in modern LLMs like llama 3.1 70B, GPT-4o, Claude 3.5 etc., as they have been already trained to follow instructions qutie well. It's also unclear to me why people want to only tune the chatbot on the satisfcation rate data, instead of mixing with other good instruction following dataset which shall resolve the problem easily.

### Questions
Please see weakness section above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses misalignment issues in generative AI models trained with Reinforcement Learning from Human Feedback (RLHF), which typically relies on immediate feedback that may not account for long-term effects on user satisfaction. The authors show that this shortsighted feedback can lead to issues like sycophancy and deception in model behavior. To address this, they introduce Reinforcement Learning from Hindsight Simulation (RLHS), an approach that simulates potential downstream consequences and gathers feedback based on those outcomes. Applied to Proximal Policy Optimization (PPO) and Direct Preference Optimization (DPO), RLHS significantly reduces misalignment. A user study demonstrates that RLHS leads to greater goal achievement and satisfaction, highlighting the value of focusing on simulated long-term outcomes in alignment strategies.

### Strengths
Originality: Original idea that addresses a real problem with RLHF (which is well described)

Quality: Experiments very well designed with both LLMs simulating humans and real humans, and with both PPO and DPO, to support the claims of the paper.

Clarity: Very well written and understandable, from the problem formulation, to the explanation of the method.

Significance: Could have significant impacts in specific settings where this kind of hindsight simulation data is available

### Weaknesses
The quality of the results in this paper seems to rely heavily on the quality of the simulation for hindsight feedback. I think there should be an analysis of using different sizes of models for the hindsight feedback and see what kind of effect this has on performance.

The evaluation is also only conducted in one environment (a shopping environment) where the RLHS algorithm makes a lot of sense. I think there should be at least one other environment used in the paper to demonstrate the generality of the method to different domains.

### Questions
Do the authors have any results on the effect of the quality of the simulation on performance?

Could the authors demonstrate another environment where this algorithm might be useful?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper operates in the problem setting where a human asks a question to a large language model (LLM) and then makes a decision based on the LLM's response. The authors start by noting that when humans are asked to label preferences for LLM outputs, they usually cannot see the downstream consequences of those outputs. This short-term feedback can cause the LLM to produce responses that appear satisfactory but could be misleading or harmful when used for decision-making. To address this, the authors propose reinforcement learning from hindsight simulation (RLHS), where, after an LLM outputs responses for preference labeling, plausible consequences are simulated. When giving feedback, the preference labeler can then observe the original LLM output and its simulated consequences. The key idea is that the value of an LLM's response lies not in the response itself, but in how it influences decision-making. The authors demonstrate that a Marketplace AI chatbot, which recommends products to users, tends to learn deceptive behaviors when fine-tuned using short-term feedback (e.g., reinforcement learning from human feedback, or RLHF). In contrast, this behavior does not emerge when RLHS is applied.

I recommend rejecting this paper due to (1) insufficient novelty in the problem setting and proposed solution, and (2) limited empirical and theoretical results.

### Strengths
The authors clearly describe the problem setting, justifying why it is important. The proposed solution, RLHS, intuitively makes sense and is well presented. All figures are visually appealing, and general flow and organization of this paper is strong. The insights that the authors bring attention to are important for the broader RLHF community.

### Weaknesses
The problem that this paper addresses is important and potentially under explored, but is not new. The authors assert that their “central insight is that the utility provided by an AI system to a human...is not generally an intrinsic property of the outputs that it generates, but rather a function of their real-world consequences…” This insight and the general problem, however, was explored by Lang et al., who the authors cite. Therefore, I do not see the problem setting or this insight as a novel contribution from this paper. This, of course, is not a weakness in and of itself but is taken as a weakness in combination with the points listed below.

The authors’ proposed solution involves simulating potential outcomes given an LLM’s response, and then presenting those outcomes as well as the LLM’s response to a preference labeler. To the best of my knowledge this approach has not been explored by other academic papers, but feels like an incremental contribution. The authors propose no new algorithmic developments or theoretical findings, but rather, proposes using LLM prompting to provide additional information to preference labelers. In combination with the fact that this problem setting is not new, and weak empirical evidence (detailed below), I am not confident in the significance or originality of the papers contributions. 

The authors claim that they “provide substantial empirical evidence that immediate human feedback frequently misrepresents true utility in everyday interaction settings...” Rather, the authors only present empirical evidence that immediate human feedback can misrepresent true utility by designing a specific experimental protocol that induces the described phenomena. I do not see evidence to support the claim that this phenomena happens “frequently” in practice, such as in other tasks used by prior work. To alleviate this weakness, the authors could provide examples from other domains or cite existing literature that demonstrates this phenomenon in different contexts. 

Relatedly, the authors only use one domain for evaluating RLHS—introduced by the authors themselves—making it difficult to understand how this approach compares to prior work or how useful it is in practice. I appreciate the human study executed by the authors as an extra dimension of analysis, but there is a lack of sufficient evidence that RLHS is practical to use or beneficial compared to standard RLHF procedures stemming from the narrow domain in which it was evaluated. 

The authors also claim that “immediate feedback in online training introduces more misalignment gaps than offline training”, supported by the observation that PPO with immediate feedback yields higher satisfaction ratings but lower true utilities than DPO. The authors do not hypothesize or justify any explanation for this observation. I do not see sufficient information, in the form of either further empirical results, theoretical analysis, or a rigorous explantation, to support this claim that seeks to generalize empirical results for PPO and DPO in one domain to all online and offline training methods. I urge the authors to further investigate a non-intuitive claim like this through experiments in other domains to ensure that it still holds and through ablation studies to better understand it. For example, would we see the same relationship between other offline and online training methods?

In short, I think RLHS is a potentially interesting direction of research, but currently I do not see sufficient novelty in the problem setting or proposed solution, as well as sufficient empirical or theoretical results, to recommend this paper for publication in this venue.

### Questions
Questions/Clarifications that could impact the score:
1. Is there a case for why the problem setting of this paper is novel that I am missing?
2. Do the authors have additional evidence or reasoning behind the claim that “immediate feedback in online training introduces more misalignment gaps than offline training”?

Things to improve the paper that did not impact the score:
1. More information on how data was collected via Prolific should be included in the Appendix. This includes but is not limited to the following: How were human subjects chosen? From what population? How were subjects assigned to the experimental conditions?  How were subjects compensated? Was any data removed/filtered out? Did this study receive IRB approval? Without this information, it is difficult for readers to understand the context in which the human study was conducted, and therefore to fully interpret its results. 
2. The authors wrote “Hypothesis 1: Models trained with RLHS lead to a higher long-term user satisfaction rate and lower regret rate than those trained with RLHF using immediate feedback”. This is the first time you introduced the terms “long-term user satisfaction rate” and “regret rate”. The former is ambiguous (what constitutes “long-term”), and the latter is undefined (what is “regret rate” and how is this computed?).

### Soundness
2

### Presentation
3

### Contribution
2

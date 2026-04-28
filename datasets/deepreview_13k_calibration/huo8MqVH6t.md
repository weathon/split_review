# Rethinking LLM Unlearning Objectives: A Gradient Perspective and Go Beyond

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 6, 3, 8, 5, 6

## Abstract
Large language models (LLMs) should undergo rigorous audits to identify potential risks, such as copyright and privacy infringements. Once these risks emerge, timely updates are crucial to remove undesirable responses, ensuring legal and safe model usage. It has spurred recent research into LLM unlearning, focusing on erasing targeted undesirable knowledge without compromising the integrity of other, non-targeted responses. Existing studies have introduced various unlearning objectives to pursue LLM unlearning without necessitating complete retraining. However, each of these objectives has unique properties, and no unified framework is currently available to comprehend them thoroughly. To fill the gap, we propose the metric of the G-effect, quantifying the impacts of unlearning objectives on model performance from a gradient lens. A significant advantage of our metric is its broad ability to detail the unlearning impacts from various aspects across instances, updating steps, and LLM layers. Accordingly, the G-effect offers new insights into identifying drawbacks of existing unlearning objectives, further motivating us to explore a series of candidate solutions for their mitigation and improvements. Finally, we outline promising directions that merit further studies, aiming at contributing to the community to advance this critical field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper discusses the importance of auditing large language models (LLMs) to identify potential risks and the need for timely updates to remove bad responses (unlearning being the solution in consideration here). The authors propose a unified framework to comprehend various unlearning objectives, introducing the concept of G-effect to analyze and compare different unlearning methods. Insights from G-effect analysis prompt focus on a two-step approach to update original LLM parameters to get unlearned one- using a removal and retention step to deteriorate performance on the unlearning dataset while maintaining performance on the rest of the data.

### Strengths
-   The paper tackles an important topic in the field of natural language processing, specifically the need for LLM unlearning to remove targeted information without destroying model integrity.
-   The authors propose a novel framework to analyze and compare different unlearning objectives, introducing the concept of G-effect to measure the impact of unlearning objectives on targeted or common data. G effect combines the influence of both goals of a good unlearning objective- removal and retention into a single metric.
-   The paper provides a comprehensive discussion of different unlearning objectives, including gradient ascent, negative preference optimization, PO, and representation misdirection for unlearning. The paper introduces advanced unlearning objectives, such as WGA and WTNPO, which set new state-of-the-art results in unlearning objectives.
- Comparison between objectives Gradient Ascent, NPO, etc. and effect of regularization is thoroughly studied.
The paper introduces advanced unlearning objectives, such as WGA and WTNPO, which set new state-of-the-art results in unlearning objectives.

### Weaknesses
 - Ablation study on the effect of size of data to be forgotten on the effectiveness of G-effect.
- Effect of 'harder' or 'easier' examples to forget on G-effect.
- Figures plotting the G-effect have their axes not labeled.

### Questions
- Is it possible to see the effect of choice parameters like number of samples to be forgotten on the G-effect ? 
- Other ablation studies are also appreciated- for instance choice of network architecture, sensitivity to optimizer params, etc. It wasn't clear if these results are averaged over multiple runs. 
- I am curious to see how G-effect varies for samples that are harder to forget. This may even help explaining the relationship between influence functions and data values with ability to unlearn.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Large language models (LLMs) need thorough audits to uncover risks like copyright or privacy violations. When such risks are identified, prompt updates are essential to filter out inappropriate outputs, ensuring that models remain lawful and safe for use. This concern has fueled new research into LLM unlearning, aimed at selectively erasing specific unwanted knowledge while maintaining the reliability of other, unaffected responses. In this context, the authors of this paper introduce the G-effect toolkit, which measures how unlearning objectives influence model performance through the analysis of gradients.

### Strengths
The paper is clearly written and straightforward to understand.

### Weaknesses
It is uncertain if the findings discussed in this paper can be applied to scenarios where LLM unlearning aims to eliminate the effects of contaminated data. Specifically, the paper focuses on unlearning for privacy, which is distinct from unlearning to mitigate data poisoning attacks. The current analysis does not address the unique challenges associated with data poisoning, such as the potential for subtle, targeted manipulations that are designed to be difficult to remove. Furthermore, the paper does not explore the potential for cascading effects where removing one piece of poisoned data might inadvertently impact other, seemingly unrelated, parts of the model. This raises concerns about the generalizability of the G-effect framework to more adversarial unlearning scenarios.

Additionally, while the G-effect is presented as a novel approach, its relationship to existing methods like influence functions and Shapley values is not sufficiently clarified. The paper mentions that G-effect is derived from the first-order approximation of SGD dynamics, but the practical implications of this derivation, compared to the linearization of optimal solutions used in influence functions, are not fully explored. The paper should provide a more rigorous comparison, including a discussion of the computational trade-offs and the types of analyses that are uniquely enabled by each method. Without this, it is difficult to assess the true novelty and utility of the G-effect.

Finally, the paper does not adequately address the limitations of LLM unlearning, particularly the fact that it may not always fully eliminate the influence of data that users wish to remove. The paper should discuss the potential for residual effects and how these might impact the reliability of the model after unlearning. The analysis should also consider scenarios where the data to be unlearned is deeply embedded within the model's parameters, making complete removal extremely difficult, if not impossible. The paper should acknowledge these limitations and discuss how the G-effect framework can be used to measure and mitigate these residual effects.

### Questions
Overall, this paper is quite intriguing. The authors introduce an innovative framework called G-effect, designed to measure the influence of unlearning objectives on model performance through gradient analysis. However, there are some points for the authors to consider:

1) Unlearning is typically applied in two scenarios: first, for privacy reasons, where users seek to remove content related to privacy. This is the scenario explored in this paper. However, unlearning can also be driven by security concerns, such as when an LLM is compromised by data poisoning, and the system needs to mitigate the impact of various poisoning attacks. It remains unclear if the conclusions drawn in this paper can be extended to this second scenario.

2) G-effect appears to share similarities with influence functions and Shapley value methods. The authors should clarify these connections.

3) Research, such as [A], suggests that LLM unlearning may not always fully eliminate the influence of data that users wish to remove. It is not evident whether the proposed G-effect accounts for this limitation.

[A] Machine Unlearning Fails to Remove Data Poisoning Attacks.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Various approaches have been proposed in the literature to perform LLM unlearning. Existing unlearning evaluation metrics compare LLM performance before and after unlearning. To provide more insights into understanding the underlying mechanisms, this paper aims to quantify the impacts of unlearning objectives on model performance from a gradient perspective. To do that, this paper proposes the toolkit of the G-effect: 
1. unlearning G-effect: the capability to decrease model performance on unlearning data 
2. retaining G-effect: the capability to maintain/enhance performance on other data 

G-effect compares the gradient of the unlearning objective and the risk metric that assesses the LLM performance:
 - If the gradients of the unlearning objective align in opposite directions to the risk metric, model updating based on the unlearning objective is capable of decreasing model performance measured by the risk
 - If the gradients of the unlearning objective align in similar directions to the risk metric, model updating based on the unlearning objective is capable of enhancing model performance measured by the risk metric

This paper quantifies the degree of such similarity between unlearning objective gradients and the risk metric gradients using their dot products.

### Strengths
1. Gradient-based analysis of the G-effect enables a better understanding of unlearning approaches including
	- examining the dynamics of unlearning procedures
	- explore the impacts of particular layers or data points involved during unlearning
2. Using G-effects to assess Gradient Ascent, Weighted Gradient Ascent, Negative Preference Optimization, Preference Optimization, Representation Misdirection for Unlearning and Regularization. Their study concludes several interesting findings. For example among 3 representative regularization terms, namely gradient difference, KL divergence and representation retention, KL  is superior for retention.

### Weaknesses
1. This paper (Section 4) examines G-effects of each unlearning objective independently and in isolation to other learning objectives. Results are also shown and discussed in separate figures and parts of the paper. Studying G-effect of each learning objective in isolation, raises the concern regarding the comparability of G-effect values across various unlearning objectives and approaches.
 	- Why empirical analysis of each unlearning approach is shown and discussed in separate parts of the paper?
	- Are G-effect values comparable across different unlearning approaches? are values comparable and why?
	- Can the proposed G-effect rank unlearning approaches?
2. Section 5 and its Table 1 provide a comprehensive comparison of various unlearning approaches using TOFU unlearning dataset for the removal of fictitious author profiles from LLMs finetuned on them. However, this comparison uses only existing metrics: forget quality, model utility, and PS-scores, and does not report the proposed G-effects.  
	- Why G-effects are missing in this section?
	- How do G-effect values correlate with metrics presented in Table 1?
	- Why are the order and ranking of unlearning objectives different across different removal and retention metrics?

3. G-effects need access to intermediate checkpoints during unlearning, especially given the pattern of values in for example Figure 3 (i.e., a peak and then flat close to zero). How does this limit the applicability of the proposed metric? 
		
4. The G-effect definition uses model checkpoints at different time steps and does not directly take into account the risk and unlearning of the initial model. 	
	- Why does this make sense?
	- Is this why you need to do accumulative?
	- what does the G-effect at each unlearning step mean?
	- what does accumulation across unlearning steps mean?
	- What does pick mean in Figure 3? Should we stop after that step to have an effective unlearning? what would be the benefit of continuing? is 0 G-effect value the limitation of your method?

5. Some of the claims are not completely supported. For example, the claim "In terms of the unlearning G-effects, it indicates that the unlearning strength of NPO is weaker; however, for the retaining G-effects, it suggests that NPO better preserves the model integrity." As an initial step, I would link it to numbers in Table 1.
6. Membership inference attacks are a common approach in the literature for evaluating the removal capability of unlearning approaches [MUSE]. However, this paper does not report the success of membership inference attacks. How the unlearning G-effect is compared to the success of MIA? Are they aligned?

### Questions
I have outlined questions for each weakness above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper beings with a bird's eye view of unlearning, highlighting its importance and the main drawbacks of the current approach. The paper suggests G-effect, a method to better examine the behavior and properties of unlearning during learning. This is done by taking into account the gradients with respect to unlearning two objectives and computing their inner-product with the gradients taken for unlearning. This method has the potential to serve as an evaluation criteria of existing and new unlearning approaches, while also providing insights to explain the success and failure of unlearning approaches, beyond the simple black-box evaluation.

This method is interesting and powerful, as it was able to generate five observations on unlearning: Unlearning affects shallow layers more, Unlearning compromises retention, Excessive unlearning is harmful, Risk weighting is powerful, Regularization is important.

The paper then explores multiple unlearning approaches; GA, NPO, PO and RMU using the G-effect.

The paper address the current limitation of the approach and suggests new promising directions.

### Strengths
The paper is insightful and well written. It provides a lot of context to the reader, explains the main drawbacks of the current approach and the importance of G-effect in addressing and examining unlearning from a scientific point-of-view, as opposed to blackbox trial and error which stems from intuition. The paper provide a very thorough analysis of G-effects on multiple unlearning approaches.

### Weaknesses
Not sure

### Questions
Is something off with Figure-3 or its caption?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles the concept of unlearning in Large Language Models (LLMs), focusing on the removal of learned knowledge while preserving the overall model integrity. The authors propose a new metric, the G-effect, to quantify the impact of unlearning objectives on model performance.

### Strengths
- Investigating unlearning dynamics is an interesting and understudied area.

- Empirical results back up some of the authors claims.

### Weaknesses
Legal compliance has been an oft touted reason for unlearning. I have yet to see any compelling argument that unlearning passes any kind of legal bar for data removal. I’m not even sure what the requirements are for meeting e.g. GDPR requirements. I am concerned that the unlearning community may be operating in a vacuum, failing to actively engage with the legal community to determine the practical applications and implications of unlearning.

–

“It is common the cases where shallow layers are more affected than deeper layers during unlearning. It suggests that general knowledge, predominantly encoded in shallow layers (Patil et al., 2023), undergoes substantial alterations“ Why not freeze shallow layers during unlearning using methods like [1]?

[1] Goel, Shashwat, et al. "Towards adversarial evaluations for inexact machine unlearning." arXiv preprint arXiv:2201.06640 (2022).

–

“Unlearning compromises retention. Although conceptually existing (cf., Section 3), current
unlearning objectives all fail to retain the overall model performance when unlearning.“ This is not a new contribution. Many prior works have made this discovery. I also do not understand the difference between this statement and the next contribution: “ Excessive unlearning is harmful. An excessive extent of unlearning has severe impacts such that the deterioration in common model responses can outweigh improvements in unlearning.”

–

I do not believe the contributions highlighted are particularly interesting. The first three listed are already well known phenomena (the first being the motivation for prior unlearning techniques in [1]). The fifth contribution has already been studied. I do think the fourth contribution: “Risk weighting is powerful. Prioritizing certain beneficial points is justified to be effective for unlearning. However, there still exists a large space to further refine risk weighting mechanisms.” is interesting, but I’m not sure this amounts to a significant contribution to the field.

–

The unlearning objectives designed for concept removal assumes that one can pinpoint and incorporate the specific data requiring removal into the unlearning dataset denoted as D_u. I do not believe this is realistic in general.

–

“Removal. The performance on the unlearning dataset Du should significantly deteriorate, i.e., R(Du; θu) ≫ R(Du; θo), revealing effective unlearning on data targeted to be erased.“ Throughout this paper, privacy is highlighted as a use case for unlearning. This is not a good removal metric for anything to do with private information. For example, imagine I want to unlearn “Alice’s phone number is 12345”, and I do this by gradient ascent, up to the point where loss(“Alice’s phone number is 12345”) >> loss(“Alice’s phone number is *any other number*”), then this becomes an oracle, and reconstruction or identification of private information becomes easy. Multiple prior works have discussed this and how to define unlearning for privacy. Similarly, “We consider the practical objective of erasing targeted knowledge as much as possible (Liu et al., 2024), diverging from the classical definition of machine unlearning (Bourtoule et al., 2021) that seeks to make models behave as if they were trained without the targeted data. Our goal is more suitable for LLM unlearning, driven by the need to eliminate content that poses privacy and copyright concerns, with the understanding that more thorough elimination leads to more favorable behaviors.“ I believe any unlearning definition for privacy that does not try to align with a model that never trained on that data is bad for privacy. It also not clear what kind of privacy we should be concerned about. Reconstruction? Identification of membership?

—

“Sadly, merely comparing performance provides limited insights into understanding the underlying mechanisms.“ What's the definition of “understand” here? Can you formalize it?

—

“Generally speaking, the G-effect compares the gradients of the unlearning objective Lu and the risk metric R. If the gradients of Lu align in similar directions to R, model updating based on Lu
is capable to enhance model performance measured by R, an obvious alternative of R(D; θu) −
R(D; θo) to measure the performance change“ Apologies, I’m a bit confused here. Why not directly optimize R then if it is differentiable?

–

In Figure 1, it’s not clear how the intersection actually maps to successful unlearning. It would be really useful to give some examples (or quantitative results) for various points on the sphere, showing that unlearning is most successful at the intersection.

–

“Due to the high costs in fully computing the G-effects, we focus on experiments based on 5% TOFU fictitious unlearning (Maini et al., 2024) with Llama-2-7B (Touvron et al., 2023a) (cf. Appendix B). All the methods will run for 5 epochs, totaling about 60 steps.
“ This seems like a significant barrier for using G-effect. Also does this mean you only use a dataset of 40 examples? This seems quite small.
–

“The G-Effects across Unlearning Steps” I don’t see what the useful insights are here. I believe we could have instead measured the NLL of examples and gotten an equally useful signal. Overall I found it difficult to assess if the G-Effect is a more useful metric than directly measuring losses over unlearning.

### Questions
Legal compliance has been an oft touted reason for unlearning. I have yet to see any compelling argument that unlearning passes any kind of legal bar for data removal. I’m not even sure what the requirements are for meeting e.g. GDPR requirements. I am concerned that the unlearning community may be operating in a vacuum, failing to actively engage with the legal community to determine the practical applications and implications of unlearning. 

– 

“It is common the cases where shallow layers are more affected than deeper layers during unlearning. It suggests that general knowledge, predominantly encoded in shallow layers (Patil et al., 2023), undergoes substantial alterations“ Why not freeze shallow layers during unlearning using methods like [1]?

[1] Goel, Shashwat, et al. "Towards adversarial evaluations for inexact machine unlearning." arXiv preprint arXiv:2201.06640 (2022).

– 

“Unlearning compromises retention. Although conceptually existing (cf., Section 3), current
unlearning objectives all fail to retain the overall model performance when unlearning.“ This is not a new contribution. Many prior works have made this discovery. I also do not understand the difference between this statement and the next contribution: “ Excessive unlearning is harmful. An excessive extent of unlearning has severe impacts such that the deterioration in common model responses can outweigh improvements in unlearning.”

–

I do not believe the contributions highlighted are particularly interesting. The first three listed are already well known phenomena (the first being the motivation for prior unlearning techniques in [1]). The fifth contribution has already been studied. I do think the fourth contribution: “Risk weighting is powerful. Prioritizing certain beneficial points is justified to be effective for unlearning. However, there still exists a large space to further refine risk weighting mechanisms.” is interesting, but I’m not sure this amounts to a significant contribution to the field.

–

The unlearning objectives designed for concept removal assumes that one can pinpoint and incorporate the specific data requiring removal into the unlearning dataset denoted as D_u. I do not believe this is realistic in general.

–

“Removal. The performance on the unlearning dataset Du should significantly deteriorate, i.e., R(Du; θu) ≫ R(Du; θo), revealing effective unlearning on data targeted to be erased.“ Throughout this paper, privacy is highlighted as a use case for unlearning. This is not a good removal metric for anything to do with private information. For example, imagine I want to unlearn “Alice’s phone number is 12345”, and I do this by gradient ascent, up to the point where loss(“Alice’s phone number is 12345”) >> loss(“Alice’s phone number is *any other number*”), then this becomes an oracle, and reconstruction or identification of private information becomes easy. Multiple prior works have discussed this and how to define unlearning for privacy.
Similarly, “We consider the practical objective of erasing targeted knowledge as much as possible (Liu et al., 2024), diverging from the classical definition of machine unlearning (Bourtoule et al., 2021) that seeks to make models behave as if they were trained without the targeted data. Our goal is more suitable for LLM unlearning, driven by the need to eliminate content that poses privacy and copyright concerns, with the understanding that more thorough elimination leads to more favorable behaviors.“ I believe any unlearning definition for privacy that does not try to align with a model that never trained on that data is bad for privacy. It also not clear what kind of privacy we should be concerned about. Reconstruction? Identification of membership?

—

“Sadly, merely comparing performance provides limited insights into understanding the underlying mechanisms.“ What's the definition of “understand” here? Can you formalize it?

—

“Generally speaking, the G-effect compares the gradients of the unlearning objective Lu and the risk metric R. If the gradients of Lu align in similar directions to R, model updating based on Lu
is capable to enhance model performance measured by R, an obvious alternative of R(D; θu) −
R(D; θo) to measure the performance change“ Apologies, I’m a bit confused here. Why not directly optimize R then if it is differentiable?

–

In Figure 1, it’s not clear how the intersection actually maps to successful unlearning. It would be really useful to give some examples (or quantitative results) for various points on the sphere, showing that unlearning is most successful at the intersection.

–

“Due to the high costs in fully computing the G-effects, we focus on experiments based on 5% TOFU fictitious unlearning (Maini et al., 2024) with Llama-2-7B (Touvron et al., 2023a) (cf. Appendix B). All the methods will run for 5 epochs, totaling about 60 steps.
“ This seems like a significant barrier for using G-effect. Also does this mean you only use a dataset of 40 examples? This seems quite small.
–

“The G-Effects across Unlearning Steps” I don’t see what the useful insights are here. I believe we could have instead measured the NLL of examples and gotten an equally useful signal. Overall I found it difficult to assess if the G-Effect is a more useful metric than directly measuring losses over unlearning.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focus on analysis of existing unlearning methods in the scope of LLMs. The authors propose a general toolkit for analysis of existing methods, which is named G-effect. G-effect analyzes unlearning methods from both forgetting and retaining. Experiments show the rationality of the proposed G-effect, and the effectiveness of several proposed variants.

### Strengths
- The paper is well structured.
- The authors propose G-effect to analyze existing unlearning methods from the perspectives of both forgetting and retaining effects.
- Analysis of G-effect somehow accords with the experimental results. Experiments show the effectiveness of the proposed variants.

### Weaknesses
 - What is the rationale of designing WGA? The authors did not clearly state the reasons of choosing such format. Specifically, why choose the inverse of the confidence score as a weighting factor, and why this specific form (e.g., 1/confidence) instead of other possibilities such as 1/confidence^2 or 1/sqrt(confidence)?
- I do not clearly see the challenges of coming up such a general toolkit for analysis of various unlearning methods. The paper does not adequately articulate the specific hurdles in creating a framework that analyzes gradient dynamics for different unlearning objectives.
- The claim in Line 081 is somehow too strong. How did the authors conclude that KL is the optimal choice? The paper does not provide sufficient justification for why KL divergence is superior to other regularization techniques such as L2 regularization, especially in the context of retaining model performance during unlearning.
- The presentations of Figure 2,3,4 are somehow hard to read. Putting the legends near the figures might be better.

### Questions
no

### Soundness
3

### Presentation
3

### Contribution
2

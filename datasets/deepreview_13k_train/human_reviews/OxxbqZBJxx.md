# Win Rate is All that Can Matter from Preference Data Alone

- Decision: Reject
- Scores: 3, 1, 6, 5

## Abstract
The surging interest in learning from preference data has resulted in an elaborate landscape of methods and evaluations. 
This work offers a framework to simplify this landscape, starting from the underlying sampling distribution for preference data.
First, we show that the only evaluation of a generative model that is grounded in the preference data sampling distribution is win rate. 
Given that win rate is all that can matter from preference data alone, we relate common preference learning algorithms to direct win rate optimization (DWRO). We outline the theoretical benefits of RLHF as a variant of DWRO; explain why checkpointing is difficult with DPO as a non-DWRO objective; and characterize the limits of SFT on preferred samples with regard to the extent of win rate improvement possible.
Furthermore, we provide closed-form expressions for the expected win rate improvement of the above objectives, formalizing the role of a model's starting point in the win rate improvement possible. Finally, we conduct an empirical analysis of existing methods and alternative DWRO objectives which suggests that optimization improvements are likely key to advancing preference learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a framework for preference learning centered around the concept of "win rate" as the fundamental metric derived from preference data. Recognizing that preference learning has become increasingly complex, the authors propose Direct Win Rate Optimization (DWRO) as a more straightforward family of objectives for preference learning. They demonstrate that Reinforcement Learning from Human Feedback (RLHF) is a KL-regularized DWRO objective, unlike Supervised Fine-Tuning (SFT), although SFT still improves win rate. Through theoretical analysis, the paper explores how various preference learning objectives impact the sharpness of target distributions and provides closed-form solutions for expected win rate improvements. The authors support their framework with empirical results, showing that alternative KL-regularized DWRO objectives can outperform RLHF, and conclude by offering guidance for future research based on their win-rate-centric perspective.

### Strengths
1. Theoretical Contributions: It offers formal proofs showing that only the win rate is grounded in preference data, providing justification for the proposed DWRO framework.

2. Empirical Validation: The experimental results support the theoretical claims and illustrate the efficacy of DWRO objectives compared to RLHF.

### Weaknesses
1. The writing is poor. Especially for the contribution is poor, first, the authors should use mathematical formulas to accurately show their novelty instead of confusing words; second, the contribution should be split into fewer points, like 3 to 4. Now 7 points are too many.

2. The novelty of this work is little. Although the authors claim that they are the first to consider the win rate, the win rate is basically the same as the general preference, which is already been studied by a series work of Nash learning, such as Munos 484 et al. (2023), [1], [2], [3]. In this work, the authors fix the policy of one response as the based one and optimize the others, this is exactly the same as each iteration of Nash learning optimization of Munos 484 et al. (2023). Besides, although the authors consider different functions h, all the types they list in Table 3 have been considered in the previous works. 

3. Based on the theory of Munos 484 et al. (2023) and [3], fixing one response and optimizing the other may not be efficient and achieve the best performance since one iteration will not lead to the Nash equilibrium. Hence, the authors are suggested to compare the performance of their method to Munos 484 et al. (2023), and [3].

### Questions
1. Line 124: If h is a function, what is its' mapping: from what space to what space?

2. Line 354: the notation for the variance is confusing and I cannot find a clarification. To which variance the authors are taking variance?

3. Some typos: Line 228 should be "between the model and the target distribution";  Line 354 and 357, ".5" is somehow unprofessional and easily leads to confusion. It is better to change it to 0.5 or 1/2.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper studies preference learning algorithms for language models. The authors propose a family of objectives called DWRO to directly optimize the win rate. The authors discuss the relationship between DWRO, reinforcement learning from human feedback (RLHF), and supervised fine-tuning (SFT), examining how SFT can improve win rates. They also conduct experiments to evaluate different DWRO variants.

### Strengths
a. This paper studies a general preference learning problem, with the goal of improving win rates. The widely-used Bradley-Terry model is a special case within this general preference framework.

b. The authors conduct experiments to evaluate various DWRO variants with different choices of $\psi$.

### Weaknesses
a. The major contribution, DWRO, is not new, as it has already been proposed (see Equation 6, the preference optimization objective, in [1]). The function $\Psi$ serves the same role as $h$. Additionally, the relationship between the objective and RLHF has also been discussed in [1].

b. Section 3.3, which discusses SFT, is unclear. In line 313, the authors state that “SFT is analogous to estimating the distribution $p(\mathbf{y}_1 \mid \mathbf{x}, \ell=1)$” but do not provide justification. The quantity $p(\mathbf{y}_1 \mid \mathbf{x}, \ell=1)$ is confusing, as it’s unclear how another response, $y_0$, is sampled. Is it sampled from a fixed reference distribution? More details are needed on how SFT is performed on preferred samples. Furthermore, the justification for why Eq. 16 is the target distribution for SFT is lacking. The authors show equivalence between Eq. 15 and Eq. 16 but do not explain the derivation of Eq. 16.

c. Experimental details are also insufficient. There is no explanation of how the reference model is trained—does it use the same preference dataset as the models with DWRO variants? In addition, details on constructing the preference pairs for training are missing. The purpose of the experiments is also unclear. If the goal is to compare different DWRO objectives, it would be more meaningful to have them compete directly with each other, rather than against a fixed reference model. Furthermore, the judge model, Pythia-2.8b, is lightweight, whereas higher-standard models like GPT-4 are typically used as judges for evaluating win rates.

d. The overall presentation requires improvement. Section 2.2 all talks about the evaluation function $\phi$, but it does not appear in later sections. Additionally, the notation for the anchor distribution is inconsistent, with $q$ used in some expressions and $p$ in others, which makes the paper difficult to follow.

e. Appendix G is entirely focused on proofs, and I don’t think it contains details about constructing preference pairs.

f. Regarding the judge model, my concern is that it is only a 2.8B model, and I am worried about whether it is powerful enough to provide accurate judgments.

g. The proposed win-rate-centric framework is not new; it is essentially general preference learning, as proposed by Azar et al., 2024. Similarly, the DWRO objective is exactly the same as the IPO objective. Section 5 mainly states that DPO and SFT do not always improve win rates, but this is very expected since they are not designed for general preference learning.

h. Section 6 evaluates DPO, SFT, and other variants of IPO objectives. However, the goal of the IPO objective is to calculate the best response to a reference model. In contrast, there is a line of work focused on learning the Nash equilibrium, which is much more general and powerful than the best response to a fixed policy.

i. Overall, the contribution of this paper is very limited, given that general preference learning has been widely studied and this paper still focuses on studying variations of the initial IPO objective.

### Questions
See weaknesses.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose an overarching conceptual framework—a “North Star”—to guide work on learning from human preferences, centered around optimizing for win-rate. This framework consists of a family of Direct Win Rate Optimization (DWRO) objectives for optimizing generative models to achieve higher win-rates. DWRO objectives have of three central components: (1) the strictly monotonic increasing function h, which takes in a preference probability as an input (2) the preference classifier and (3) the anchor distribution over which win-rate is computed. 

The authors then present the KL-regularized DWRO (DWRO-KL) objective, which helps mitigates issues related to reward hacking, and which RLHF falls under. Notably the authors assert that optimizing for the DWRO-KL objective is equivalent to approximating a target distribution, which draws an important parallel to variational inference. The authors characterize the target distribution as being the original distribution that has been tilted to have more probability mass placed over sequences that are more likely to be preferred over the anchor distribution. In particular, the notion of sharpness as controlled by the parameter beta and the function h, is used to characterize the target distribution. Under this framing, the authors then introduce the following insights:
1. RLHF is a DWRO-KL objective 
2. DPO is a DWRO-KL objective with the same target distribution as RLHF, but used a different DWRO-KL objective than RLHF
3. SFT is not DWRO objective but still optimizes for win-rate via targeting a different distribution 

The authors present some empirical results illustrating the effects of varying the DWRO-KL objective on two popular preference learning datasets (i.e., HH and OASST). The authors also provide closed-form solutions for the expected win-rate improvement for DWRO-KL objectives and the SFT objective.

### Strengths
The authors present a well-structured, sound, and clear framework for understanding different approaches to learning from preferences. By viewing these methods as either optimizing for win-rate or approximating a specific target distribution, they provide a useful lens for interpreting past and future work in this domain. I appreciate this framework as an original and valuable tool for conceptualizing advancements in preference-based learning.

The authors also establish a concrete parallel between learning from preferences (specifically through optimizing for the DWRO-KL objective) and black-box variational inference. This connection could be especially meaningful for researchers in black-box variational inference, potentially inspiring new research directions. To my knowledge, this connection is novel and holds promise for further impact.

Lastly, the authors offer both closed-form solutions for the expected gain in win-rate for DWRO-KL objectives and empirical results for various DWRO-KL variants. While I am uncertain about the practical utility of these results for other researchers or practitioners, they do provide insights into various design decisions for learning from preferences revolving around the sharpness of the target distribution.

### Weaknesses
The paper feels lacking in actionable insights. While the authors offer a useful framework for understanding different approaches to learning from preferences, leading to a range of alternative objectives beyond the standard RLHF objective, RLHF still appears to be the top-performing method. This raises questions about the practical value of the additional flexibility provided by the proposed framework. 

Additionally, although the finding that SFT improves win-rate is intriguing, I would appreciate more clarity on why this insight is valuable for the community.

Furthermore, Figure 1 could be clearer. This figure would be significantly improved with guidance on how to interpret it and by highlighting any specific conclusions drawn from it. I was surprised that Figure 1 was not discussed in the results section; perhaps added explanation there would be helpful.

### Questions
What practical insights can we draw from the provided closed-form solutions for win-rate improvement for the DWRO-KL objectives?

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
The authors present a framework for analyzing different preference learning algorithms. They begin by defining the sampling distribution for pairwise preference learning and introduce a grounded evaluation function, demonstrating that the only grounded function, under a monotonic condition of function h, is the win rate. Building on this result, they propose an objective to optimize the win rate (DWRO) and explore various objective variants. Furthermore, they classify existing popular methods within the DWRO-KL variant. Despite not directly optimizing the DWRO objective, the authors show that SFT can still improve win rates under certain, intuitive conditions. Finally, they provide extensive results based on a single base model.

### Strengths
- The paper introduces a general framework that encompasses cases like RLHF or DPO.
- This intuitive framework offers insights into current BT model-based preference learning methods.
- The authors present ablation studies on various functions h and different parameters beta.
- This framework can motivate further studies on finding improved optimization objectives.

### Weaknesses
 - The framework does not appear to account for unpaired/ranked preference methods.
- The judge model used seems underperforming, achieving only 68.8 on the evaluation set.
- Diverse models could have been employed for more comprehensive results.
- The framework does not address biases in preference learning, such as length bias.
- The paper focuses solely on the DWRO-KL variant without exploring other possible variants.

### Questions
- The judge model Pythia 2.8B model seems weak.
- Why do you fine-tune on dispreferred outputs? Which step is that in the framework?
- Stronger judge models should be evaluated for comparison.
- Could you clarify what the anchor distribution is? It is used interchangeably as p or q, which adds to the confusion. Is it solely based on y_0 as defined in Definition 2?
- In the base case of Definition 2, where l=1, there is no y_1 provided. Could you explain this?
- Why is preference limited to the case where l=1? Why doesn’t it include the case when l=0 with x_0 being preferred?
- What is Property 3 in the proof of Proposition 1?
- Since you're using sequence-level KL divergence for DWRO-KL and token-level for PPO, the results may not be directly comparable. Could you comment on this?
- There are some grammatical issues throughout the paper that make comprehension more difficult.
- How many samples are used for each set in your experiments?
- The Appendix mentions Mistral 7B, but no results for this model are included.
- Given that beta is an important parameter, further studies or experiments focusing on its impact would be valuable.
- While DPO is discussed in the analysis, it is not shown in any empirical results. Why is that?

### Soundness
3

### Presentation
1

### Contribution
2

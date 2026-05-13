# An Auditing Test to Detect Behavioral Shift in Language Models

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
As language models (LMs) approach human-level performance, a comprehensive understanding of their behavior becomes crucial. 
This includes evaluating capabilities, biases, task performance, and alignment with societal values.
Extensive initial evaluations, including red teaming and diverse benchmarking, can establish a model’s behavioral profile.
However, subsequent fine-tuning or deployment modifications may alter these behaviors in unintended ways.
We present a method for continual Behavioral Shift Auditing (BSA) in LMs.
Our test compares model generations from a baseline model to those of the model under scrutiny and provides theoretical guarantees for change detection while controlling false positives.
The test features a configurable tolerance parameter that adjusts sensitivity to behavioral changes for different use cases. 
We evaluate our approach using two case studies: monitoring changes in (a) toxicity and (b) translation performance. 
We find that the test is able to detect meaningful changes in behavior distributions using just hundreds of examples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method for behavioral shift auditing (BSA), a decision task for detecting when a ML model's outputs, like an LLM's completions, deviates from the behavior of a previous model version. Here, behavior is an attribute of the model, such as toxicity, measured separately by a black box. The primary contributions of the paper are application and empirical. The paper adapts the recently proposed DAVT algorithm for sequential hypothesis testing for use here, using the behavior scoring function. Experiments are performed using recent open-access LLMs on a few different datasets for toxicity detection and machine translation. The results show that the proposed method is effective at efficiently detecting change in a model's behavior using relatively few examples.

### Strengths
- Detecting shift in ML model outputs as part of audit processes is an important and interesting technical challenge. Progress here is likely to be of interest to the community.

- The paper is very well written. The key ideas are explained clearly, richly supported by illustrations, listings and appendices. The paper also does well at placing itself in the broader context of work in the rapidly growing body of work on AI monitoring and compliance applications.

- The proposed method is intuitively clear and the algorithm seems straightforward to implement. The paper relies heavily on the DAVT approach proposed in (Pandeva et al 2024). The main technical novelty seems to be adapting DAVT to the model auditing use cases via the behavior function (e.g., Perspective API's toxicity evaluation endpoint). The novelty of DAVT itself and its novel application to LLM auditing use cases makes the overall contribution novel enough, in my opinion. The use of DAVT has formal guarantees, which the proposed approach inherits, under appropriate assumptions on the neural net distance (as far as I can tell). Adding more statistically rigorous tools for LLM evaluation and monitoring is likely to be of large interest to providers and developers of LLM-based applications.

- The experiments show the proposed method works well for the intended purpose of auditing the outputs of ML models (wrt the behavior function). Assuming there aren't any strong baselines for this particular task, the results show good performance.

- While the evaluation could be improved (see below for details), I thought the paper was clearly written and richly detailed. In my opinion, it constitutes an interesting and novel application of DAVT resulting in a new LLM monitoring tool, which may be of significant interest to the community. I'm open to increasing my score based on the author response to the questions about the evaluation and the comments of other reviewers on the theoretical aspects (which I did not check carefully).

### Weaknesses
 - My main concern is the evaluation of the main claim of the paper, which is "detect changes in LM (model) behavior over time". Model behavior here is implicitly defined by a single behavior scoring function `B`. Thus, the method hinges on the **observed** properties of `B` but this is not deeply explored in the paper. Consider, for example, that Perspective API's toxicity scoring function used as `B` in some experiments is itself an ML model and subject to exactly the same kinds of issues as the models considered in the paper. Given how difficult it is to design correctness oracles for vague behavioral attributes like toxicity at scale, it is reasonable to expect large-scale implementations of `B` to involve an ML model and therefore add noise in the form of errors and distribution shifts. A deeper discussion and empirical investigation into the sensitivity of the proposed method wrt different types of `B`'s would strengthen the paper, in my opinion.

- Continuing in a similar vein as the above, a practitioner might consider it insufficient for the model to pass a **single** test of behavior (e.g., toxicity). Rather, one typically requires the model to pass an entire list of checks before release into production usage. This is usually implemented by some combination of automated checks (e.g., per-behavior quality and regression test sets) and manual QA (e.g., SMEs, red teams). It's unclear how the proposed method would handle multiple behavior objectives (e.g., low toxicity and low hallucinations and ...). Single `B` combining all of these? Extension of DAVT involving multiple $\epsilon$? Something else? What effect would noisy `B` have on this?

- Since I was unable to find a baseline matching the exact problem considered here, I'd be curious to see the results of measuring the statistical difference in just the outputs of `B` wrt held-out data. Specifically, how does $b_{1, i} = B(x_i, M_1(x_i))$ differ from $b_{2, i} = B(x_i, M_2(x_i))$ on the test data used in the experiments? What about standard distance functions, summary statistics, tests or classifiers defined over the test $b$'s? I'd recommend including these types of empirical studies given that: a) the primary contribution of the paper seems to be a novel application of DAVT for change detection in models wrt `B`'s outputs and b) it's increasingly common practice to test a release candidate using the outputs of multiple ML model-based "test" or "correctness" oracles (i.e., different `B`'s, trained separately) on held-out test and regression data. 

- Overall, given the current experimental section's weaknesses, I'm somewhat concerned that the method might be at risk of not outperforming existing methods of large model evaluation and being of limited utility to practitioners. As a result, I'm leaning towards rejection. That said, I don't think there's anything technically wrong with the paper and it's possible I may have missed something obvious. I'm open to revising my score upwards and look forward to the author response and other reviews.

### Questions
1. How does the proposed method handle change in `B` itself (from updates, prediction error, concept drift)?

2. How does the proposed method handle multiple behaviors (low toxicity and low hallucinations and ...)?

3. Is it possible to construct a baseline by simply comparing `B`'s values on the two models' outputs using test data? See above for details. If yes, how does it compare with the proposed method?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces an anytime-valid hypothesis test to identify behavioral shifts in LLMs. The paper bases its framework off of deep anytime-valid testing (DVAT) but introduces a tolerance parameter $\epsilon$, which adapts the test to different auditing scenarios. Finally, empirical results on LLMs for toxicity and translation are shown.

### Strengths
- Introduces a novel algorithm for statistical hypothesis testing applied to LLMs which controls the false positive rate. This may improve auditor's abilities to regulate LLMs.
- Provides theoretical guarantees of the test along with empirical results showing its efficacy. The empirical results are real-world.
- Well-written, with good exposition and background on the statistical theory behind anytime-valid hypothesis testing.
- Tackles a reasonably challenging problem in auditing LLMs.

In summary, the paper develops a novel algorithm (reasonable originality), shows its theoretical and empirical soundness (good quality), has detailed mathematical background (high clarity), and seems to improve auditing (reasonable significance).

### Weaknesses
 Overall, I think the paper is well done. Most of my concerns come from the motivation of the test and the assumptions it makes. Specifically,

**Confusing writing in the abstract and intro, stemming from the lack of clear motivation.** While I liked most of the writing in the paper (especially the background on statistics, which was helpful for someone who doesn't work in this area), the writing near the beginning should be clarified:
  - *Behavioral-shift auditing is vague and is not properly defined.* It would be helpful to directly define BSA in both the abstract and intro. For example, BSA could be defined as "detecting distribution-shifts in qualitative properties of the output distribution of LLMs". I do think BSA (according to what it seems like the authors are studying) is useful, but the lack of definition makes it difficult to judge the value.
  - *The abstract and first two paragraphs of the intro do not make it obvious that the behavioral test is a statistical test.* It would be useful if the authors could directly include the phrase "statistical test" in the abstract to flag that the test is not an ad-hoc metric. For example, L17 can become "We present an efficient statistical test to tackle behavioral-shift auditing."
  - *The motivation behind studying BSA is confused and indirect.* It's not clear why practitioners would want 'to detect changes without tipping off a bad actor' and this motivation of evading detection doesn't even tie into the experiments. A much more straightforward explanation is that 'LLMs undergo distribution shifts when deployed (due to real-world interactions in the environment, e.g., [1]), driving a need to continuously monitor for shifts in their behavior. Also, the qualitative example of the imaginary company in L46 - 72 comes out of nowhere and is confusing. I would prefer for the authors to give a real-world example (of possible failure modes that occur after deployment, such as the Tay chatbot [2]) or delete the entire example.

**Strong empirical assumptions not addressed in the limitations section.**  The paper makes a strong assumption about the availability of an empirical classifier for behaviors. In L102 - 103, "Let $B$ be such a behavior scoring function that assigns scores in the range $[0, 1]$". While not a strong theoretical assumption, this is a very strong empirical assumption. There is evidence that automatic toxicity measures, specifically the Perspective API, are not well-calibrated (in a colloquial sense) to human judgements of toxicity [3]. Moreover, it is difficult to evaluate certain behaviors, such as deception [4] or sandbagging [5], from a single (prompt, completion) pair, as they tend to occur over an entire trajectory. Furthermore, evaluating the mere presence of other behaviors, such as hallucinations [6], is an active area of research. While I don't think the paper's assumption of the existence of $B$ detracts from the overall approach, it certainly limits its empirical application. I would appreciate if the authors could add a discussion of this limitation (possibly including some of the points I raised) into the limitations section.

### Questions
Typos:
- Second sentence of the abstract has an extra T: T This --> This

Questions:
- In figure 5, why is the orange dashed line not at x-value (test epsilon) which corresponds to a y-value (proportion of triggered tests) of 0? It seems like all the other lines have this property. Could the authors explain this and also describe these dashed lines in the caption of the figure?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The study presents a method for continual Behavioral Shift Auditing (BSA) in language models (LMs), based on anytime-valid hypothesis testing. The test detects behavioral shifts through model generations, comparing outputs from baseline models to those under scrutiny. It features a configurable tolerance parameter and can detect meaningful changes in behavior distributions. The approach is valuable for AI practitioners, enabling rapid detection of behavioral shifts in deployed LMs.

### Strengths
+ The paper presents an efficient method for Behavioral Shift Auditing (BSA). By building on anytime-valid hypothesis testing, the authors propose a theoretically grounded approach for detecting behavioral shifts in LLMs.
+ The method is designed for real-world application, allowing for continual auditing through model-generated outputs.

### Weaknesses
 - How the method scales with larger or more complex models is unclear.
- The presentation is not good. Some parts are hard to follow.
- There are some typos scattered around.

### Questions
1. Section 1: "without tipping off a potential bad actor" Why is this a requirement of behavioral shift auditing?
2. Section 1: What are the main contributions of your work?
3. Section 2.2: The high-level introduction of anytime-valid hypothesis testing is not easy to understand.

### Soundness
3

### Presentation
2

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
Evaluating and detecting behavioral shifts in language models (LMs) is a crucial topic to understanding the underlying performance deviation and potential degradation in safety alignment, especially when a large number of base models are further tuned to adapt specific tasks. This work proposes a method for continual behavioral shift auditing (BSA) in LMs, which formulates the detection task as hypothesis testing to reveal relevant behavioral distribution shifts. The authors conduct experiments including both internal auditing for machine translation and external auditing for toxic generation. The experimental results show that the proposed method can effectively identify model behavioral changes within a relatively small portion of samples.

### Strengths
1. A new approach for detecting behavioral shifts in language models.
2. Extensive experiments, including different models with various configurations under two use cases. 
3. The paper is overall easy to follow.

### Weaknesses
This paper tackles the LM problem from the perspective of anytime-valid hypothesis testing. The methodology design follows a rigorous manner, and I only have a few concerns regarding some technical details and presentation issues.

1. Although the authors provide intuitive examples for two use cases, internal audit and external audit, at the beginning of the paper, I would recommend giving a clear formulation for such two cases before stepping into examples. The descriptions of use cases provided in Section 4.2 actually give a better understanding.

2. Determining the tolerance parameter $\epsilon$ is vital in the proposed method as it decides the maximal neural net distance allowed between distributions (model behaviors). However, throughout the methodology section and experiment design, this parameter seems manually determined according to specific tasks. The authors may elaborate more on the design of this parameter to enhance the generability of the proposed method.

3. In addition, the authors mentioned in Section 4.2 that "To determine a tolerance parameter ε for this toxicity setting, we consider triggering the test if a model differs by more than the aligned Llama3 model with different sampling parameters." Is there any rationale to support such a design? What do the sampling parameters stand for, and why are they important in this context? (Table 1 in Appendix A.2 do not give intuitive instructions)

4. The experiment design for the false positive rate in Section 4.1 is somewhat rough and lacks details. In particular, What and in what format are the texts generated from the initial aligned models, and how are they valid to examine the false positive rate of the exact from different aspects?

5. A short description of the five instruction-tuned models can benefit the readability of the paper as they are used in most experiments.


6. For the 2nd use case (internal audit), the authors set $\epsilon$ as "the neural net distance between Llama3 using simple prompts, and Llama3 using few-shot prompts". Why do you use the neural distance between models with simple prompts and few-shot prompts?

7. The authors provided the link to the replication package, but the link seems incomplete.

8. The presentation of the paper is mostly in a good manner. Nevertheless, there are still some typos and grammar issues (e.g., " T This includes evaluating" in the abstract).

### Questions
1. How tolerance parameter $\epsilon$ is determined in the conducted experiments, and how should this be set for different tasks?

2. The experiment setup for the false positive rate requires more details.

### Soundness
3

### Presentation
3

### Contribution
3

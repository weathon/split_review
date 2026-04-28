# Has the Deep Neural Network learned the Stochastic Process? An Evaluation Viewpoint

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 6, 8, 6

## Abstract
This paper presents the first systematic study of evaluating Deep Neural Networks (DNNs) designed to forecast the evolution of stochastic complex systems. We show that traditional evaluation methods like threshold-based classification metrics and error-based scoring rules assess a DNN's ability to replicate the observed ground truth but fail to measure the DNN's learning of the underlying stochastic process. To address this gap, we propose a new evaluation criteria called _Fidelity to Stochastic Process (F2SP)_, representing the DNN's ability to predict the system property _Statistic-GT_—the ground truth of the stochastic process—and introduce an evaluation metric that exclusively assesses F2SP. We formalize F2SP within a stochastic framework and establish criteria for validly measuring it. We formally show that Expected Calibration Error (ECE) satisfies the necessary condition for testing F2SP, unlike traditional evaluation methods. Empirical experiments on synthetic datasets, including wildfire, host-pathogen, and stock market models, demonstrate that ECE uniquely captures F2SP. We further extend our study to real-world wildfire data, highlighting the limitations of conventional evaluation and discuss the practical utility of incorporating F2SP into model assessment. This work offers a new perspective on evaluating DNNs modeling complex systems by emphasizing the importance of capturing underlying the stochastic process.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
the metric of expected calibration error is introduced and studied as a way to capture fidelity of a learned representation to an underlying stochastic process (rather than a single realization of that process, as with typical metrics like AUC or MSE).

### Strengths
Great paper, wonderfully practical and insightful; I've been looking for something like this for 5+ years! Nice eval on real-world data.
I started writing a thing I would like to you add and then discovered it was already in the paper (long horizon behaviour)

### Weaknesses
While overall the paper is very clear, some of the captions and explanations of the experiments/insights from them and how they tie to the figures could be improved. 
Some specifics:
- first fig should say what you mean by realization, and F2R and F2SP should be bolded (not ital) to make them easy to find in the text. Observed GT should be explained a bit more, or maybe it would be enough to move the sentence currently after F2R to be the second sentence of the paragraph.
 - Fig 5 is unclear to me. What is the data, what is S-level, why is it "good" that the 20 vs 10 lines are far apart? All of this should be clear from the caption
 - the clarity wanes a bit as the paper goes on, and it's a bit confusing that you call it ECE vs. F2SP vs Statistic-GP. Do these different namings really serve something? It could be a lot more clear if you just have one naming.

### Questions
- I don't understand the second part of the critical question, "is it encountering different stochastic behaviours" (different from what)? how is the "differentness" relevant?
- While it's pretty clear to me how to use this immediately in my work, I think anyone who wasn't already aware they wanted exactly this might struggle. Could you provide something like a "practical users guide" for non-domain experts?
 - if the clarity of the plots can be improved, the naming of the stat/metric you're introducing, and improve it's "usability" to the community, I would be happy to upgrade my score. You've done great work and this would bring the paper to the level it deserves.

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
3

### Summary
This paper presents a study evaluating deep neural networks (DNNs) within stochastic complex systems, emphasizing the importance of Expected Calibration Error (ECE) in measuring fidelity to stochastic processes. The findings are validated through multiple experiments and comparisons.

### Strengths
The topic of evaluating DNNs within stochastic complex systems is both intriguing and important.

In the primary evaluations, the author conducted experiments across various settings, including different DNN architectures, comparisons with multiple evaluation metrics, and diverse simulation tasks.

The main text clearly explains the difference between ECE in classical assessment and stochastic process settings.

### Weaknesses
The paper is somewhat difficult to follow. For example, providing a brief introduction to the structure of each section would enhance clarity, particularly in Sections 2 and 3. Additionally, it is difficult to grasp the main messages conveyed by the table in Figure 2(b). Furthermore, in lines 229–240, the macro-level concept is introduced abruptly, which may disrupt the clarity and readability of the main text.

The main findings' practical applicability appears limited. In real-world scenarios, data generally provides only a single observed outcome centered on observable ground truth (line 117). Since the primary evaluation is simulation-based, the controlled stochasticity falls short of capturing real-world complexity. The Statistic-GT is basically derived by normalizing the frequency of target state occurrences across multiple Monte Carlo simulations.

Minors:

M1. The original text for the abbreviation RV is not given.

M2. In Table 1, what about the possibility of recovery in the Host-Pathogen problem?

M3. In line 152, maybe consider using an alternative symbol for Moore neighborhood, instead of $\mathcal{N}$ (normally representing Gaussian distribution).

### Questions
A question arises regarding Figure 1: Can ECE be an effective metric for measuring F2R compared to other available metrics? Figure 1 suggests that the answer may be *no*.

An important indicator that ECE is a reliable measure is its diagonal pattern, showing low scores only when training and test S-Levels align, as illustrated in Figure 4. Could the authors provide theoretical insights to support this indicator?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a study on evaluating deep neural networks designed to forecast the evolution of stochastic complex systems. The authors identify a gap in traditional evaluation methods—such as threshold-based classification metrics and error-based scoring rules—which focus on a model's ability to replicate observed ground truth but fail to assess how well the model has learned the underlying stochastic process. To address this issue, they introduce a new property called Fidelity to Stochastic Process, representing the DNN's ability to predict the statistical ground truth of the stochastic process.

The paper proposes using the Expected Calibration Error (ECE) as an evaluation metric that satisfies the necessary conditions for assessing fidelity to statistical ground truth. This work underscores the importance of capturing the underlying stochastic processes in deep neural networks  evaluations for complex systems.

### Strengths
The paper makes a significant contribution by introducing the concept of Fidelity to Stochastic Process (F2SP), a novel evaluation criterion specifically designed to assess a DNN's ability to learn the underlying stochastic interactions in complex systems.

The authors provide a rigorous formalization of F2SP within a stochastic framework, establishing clear criteria for its valid measurement. The use of Expected Calibration Error (ECE) as an evaluation metric is well-justified.

### Weaknesses
I found it hard to read the paper because there was a lack of consistency in the acronyms, the authors would redefine them in several parts of the text again and again. I addressed my comments on text in the questions section.

In the tables, the best neural networks based on each criterion are not highlighted, which makes it difficult to the reader to infer and correlate the arguments in the text. I addressed my comments on text in the questions section.

The focus of the paper is primarily on binary or discrete prediction tasks, leaving out regression tasks where the definition of calibration is more complex. While the authors acknowledge this and suggest it as an area for future work, the current scope limits the immediate applicability of the findings to a broader range of problems involving continuous outcomes.

Additionally, the use of the NDWS dataset, which is restricted to next-day predictions, prevents the assessment of ECE over longer time horizons, which are common in many complex systems. Could you elaborate on how future work might address this limitation?

The paper highlights the lack of open-source complex system datasets as a barrier to broader validation. Are there any ongoing initiatives or plans to develop, collect, or standardize such datasets?

### Questions
L50: Is --> is (lowercase)
Fig1: no need to write the whole name, you can use acronyms because they're already defined in the text, however MSE is not defined at this point.
L88: fidelity to realization --> F2R (it was already defined previously, so you can use the acronym)
L99: the notation of the dimension of the real vector O_t is confusing, what is (R^n)^(H x W), is n = H x W? If so, make that explicit.
Table 1: some rows end with full stop, other don't. Please make it consistent. Either all with or all without.
I find it odd to place Figures in columns as Figure 1 (which has a large top white margin) and Figure 3. I would suggest column figures into one row figure with multiple subfigures as you did with Figure 2. 
L201: Isn't the indicator variable already defined as B_t in L99? Why defining again with different notation?
L298: MSE already defined in text previously, no need to write the whole name again.
L516: ECE already defined in text previously, no need to write the whole name again.
Table 2 and Table 7: highlight the best performing DNNs.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work offers a new perspective on evaluating DNNs in stochastic complex systems by emphasizing  the importance of capturing underlying the stochastic process. Traditional evaluation methods assess the DNN’s ability to replicate the observed ground truth but fail to measure the DNN’s learning of the underlying stochastic process. This paper proposes a new property called Fidelity to Stochastic Process, representing the DNN’s ability to predict the ground truth of the stochastic process, and introduces an evaluation metric that exclusively assesses fidelity to  the ground truth of the stochastic process. The Expected Calibration Error is used to evaluate the fidelity to ground truth of statistic process. Empirical experiments on synthetic datasets (including wildfire, host-pathogen, and stock market models) and real-world wildfire data are used to show the measurement of fidelity to stochastic process by Expected Calibration Error.

### Strengths
The paper offers a new perspective on evaluating DNNs by considering DNNs as stochastic processes and uses a widely used criteria in Bayesian Deep Learning application to assess the fidelity to stochastic process. This work clearly explains the Expected Calibration Error is used to assess DNN modes in three synthetic cases and one real world case.

### Weaknesses
This paper is well organized and well written, several minor issues should be addressed: (1) The explaination of figures is not sufficient, e.g., in Figure 2 (1), the label for x-axis is not specified (I guess it is time?), either add a label or explain it in the captions. Same problems also exist in Figure 4, now Figure 3. (2) This work examines ECE on three synthetic environments (forest fire, host-pathogen and stock market models) and a real world wildfire spread dataset. I can tell that these datasets are all multivariate either for classification or regression. Maybe due to the limit of pages, the authors didn't include the experiments on images. The authors should consider extending their evaluation to include image-based tasks, such as segmentation map forecasting or stochastic video prediction, to demonstrate the broader applicability of their proposed metric.

### Questions
As mentioned in the "Weaknesses" part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel stochasticity-compatible evaluation strategy for assessing existing models in the context of complex systems. The author justifies the Expected Calibration Error (ECE) as suitable for assessing the model fidelity of stochastic systems through both simulation environments and real-world data.

### Strengths
1. Evaluating model fidelity on the stochastic system is significant and has wide applications.
2. The paper is well-motivated and both the dataset and experiments are thorough.

### Weaknesses
1. Although the author attempts to explain the difference between their work and ECE in deep learning in Lines 282-288, it appears to me this work is still a direct application of using ECE to evaluate the model performance on a stochastic system. The author is encouraged to discuss more in-depth about the distinction between ECE in the proposed method (stochasticity comes from evolving in the environment, aka, Statistic-GT) and ECE in previous works (stochasticity comes from the output distribution). Specifically, the paper needs to clarify how the interpretation of ECE changes when applied to a system property (Statistic-GT) versus a model output distribution. The core issue is that ECE, in its traditional use, measures the calibration of a model's predictive uncertainty, whereas here it's being used to measure the fidelity of a model's representation of a system's stochastic behavior. This difference in interpretation needs more explicit discussion and justification. 
2. In Lines 243-244, the author claims that Statistic-GT is more stable than classification-based metrics, but I could not find any evidence related to calculating ECE on Statistic-GT is less sensitive to the system variance than MSE. The claim of stability needs to be more rigorously supported with theoretical analysis or empirical evidence. It is not clear why ECE, when applied to Statistic-GT, would be inherently less sensitive to system variance than MSE, especially given that both metrics are calculated based on the same underlying stochastic process. The paper should provide a clear explanation of why ECE is a more robust metric in the presence of varying noise levels in the system, and how it specifically addresses the challenges posed by stochasticity in the system's evolution.

### Questions
I'm curious about how the author evaluates ECE at time $t$ based on Statistic-GT $P_{t}$. Do we have to simulate it again from $t=0$ for $N$ times or we can sample states from $t-1$ and go forward $N$ times (the system is Markov)? Can we still apply ECE on Statistic-GT when the system is not Markov?

### Soundness
2

### Presentation
3

### Contribution
2

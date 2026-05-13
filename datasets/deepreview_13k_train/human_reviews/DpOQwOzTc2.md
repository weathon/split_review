# Combining Denoised Neural Network and Genetic Symbolic Regression for Memory Behavior Modeling via Dynamic Asynchronous Optimization

- Decision: Reject
- Scores: 6, 3, 8, 5

## Abstract
Memory behavior modeling is a critical topic in cognitive psychology and education. Traditional psychological approaches describe the dynamic properties of memory through memory equations derived from experimental data, but these models often lack accuracy and are frequently debated in terms of their form. In recent years, data-driven modeling methods have improved predictive accuracy but often suffer from poor interpretability, limiting their ability to provide deeper cognitive insights. While knowledge-informed neural network models have achieved significant success in fields such as physics, their application in behavior modeling remains limited. This paper proposes a Self-evolving Psychology-informed Neural Network (SPsyINN), which leverages classical memory equations as knowledge modules to constrain neural network training. To address challenges such as the difficulty in quantifying descriptors and the limited interpretability of classical memory equations, a genetic symbolic regression algorithm is introduced to conduct evolutionary searches for more optimal expressions based on classical memory equations, enabling the mutual progress of the knowledge module and the neural network module. Specifically, the proposed approach combines genetic symbolic regression and neural networks in a parallel training framework, with a dynamic joint optimization loss function ensuring effective knowledge alignment between the two modules. Then, for addressing the training efficiency differences arising from the distinct optimization methods and computational hardware requirements of genetic algorithms and neural networks, an asynchronous interaction mechanism mediated by proxy data is developed to facilitate effective communication between modules and improve optimization efficiency. Finally, a denoising module is integrated into the neural network to enhance robustness against data noise and improve generalization performance. Experimental results on four large-scale real-world memory behavior demonstrate that SPsyINN outperforms state-of-the-art methods in predictive accuracy. Ablation studies further show that the proposed approach effectively achieves mutual progress between different modules, improving model predictive accuracy while uncovering more interpretable memory equations, highlighting the potential application value of SPsyINN in psychological research. Our code is released at: \href{https://anonymous.4open.science/r/SPsyINN-3F18}{https://anonymous.4open.science/r/SPsyINN-3F18}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article presents a hybrid symbolic neural network learning approach to model user interactions in memory-based learning tasks, specifically language learning. The approach uses interpretable models based on memory theory and integrates their optimization with a neural network training process. A comparison with other methods for knowledge modeling demonstrate that this hybrid approach has performance benefits, beyond the creation of interpretable results.

### Strengths
The proposed methodology and the application domain are both interesting. The idea of training a neural network and a symbolic regression model simultaneously, and aligning them in their respective optimization processes, is worthwhile and potentially novel. It could be used in a number of applications where physical laws are known or, as is the case here, there are established equations that map the relationship that should be approximated by machine learning. The interpretability of the end result, combined with the performance of a neural network training, motivates this approach. It would be interesting to see the method applied to the discovery of known physical laws, like in the following work:

Cranmer, Miles, et al. "Discovering symbolic models from deep learning with inductive biases." Advances in neural information processing systems 33 (2020): 17429-17442.

The application of memory modeling is also interesting; I am not aware of the application of PINNs to such psychological modeling problems. Most of the knowledge-informed literature is on physics-informed, including in symbolic regression, but the methods can be applied to other domains where existing relationships have been expressed as equations, even if they are not physical laws. There is a clear application to economics here, and expanding the perspectives to include similar applications could be helpful.

### Weaknesses
The main weakness of this paper is in its presentation. This is a mix of methods and an application readers might not be familiar with, so everything, from deep learning to symbolic regression to memory theory, need to be made clear to a reader. Even a reader who is an expert in some of those things might not know the others.

First, the mathematical notation is highly verbose, with subscripts for almost all variables, even when certain information is redundant or clear. For example, all tasks map user data U to word sets W. The inclusion of this mapping for every variable is unnecessary and makes the loss equations, like Equations 8 and 9, very hard to parse. Some equations are maybe not even necessary, like the definition of MSE. Simplifying the notation and reducing redundancies in the math would greatly increase clarity.

More explanation of the baseline methods would also help. DKT-F and FIFKT aren't fully explained, nor is the way that symbolic regression is integrated into their methods. The one-sentence explanations in appendix B are not sufficiently nor sufficiently referenced in the main text. For example, the description "DKT-F: An improved version of DKT that incorporates students’ forgetting behaviors. (Piech et al., 2015)" assumes that the reader understands that DKT refers to "Deep Knowledge Tracing" (it was not defined), and that the reader is familiar with Deep Knowledge Tracing's standard mechanisms, which are not described. In the Background, a short explanation of at least DKT could easily replace the sentence "The superiority of deep learning techniques in knowledge tracing and cognitive modeling has been well-established (Abdelrahman et al., 2023)," which doesn't give much information to the reader and is rather subjective.

Greater clarity in the text on the background methods and the problem domain would really help. Acronyms are rarely defined before use, and some acronyms are defined never to be used again (eg, NODS). So, I'm left with a number of questions despite a thorough reading of the paper, which is a shame because it is a very interesting method and application. Furthermore, the paper introduces terms such as "Genetic Symbolic Regression" (GSR) and "Denoised Neural Network" (DNN) without sufficient grounding in existing literature, which makes it difficult to understand the precise meaning and novelty of these terms. The use of "Temporal Neural Network" (TNN) to refer to all possible ANN architectures is also problematic, as it conflates different types of neural networks with distinct mechanisms for handling temporal data.

### Questions
In the ablation, what does it mean to have asynchronous training but not "dynamic optimization"? And is the opposite of that (having dynamic optimization but not asynchronous training) the same as the Waiting Optimization Strategy SPsyINN-W?

How well does symbolic regression alone do, and is this equivalent to the first line of Table 3? If the neural network is trained without symbolic regression, how does it do, and is that equivalent to the fourth line of Table 3? Or is the fourth line equivalent to training a neural network without the noise addition? If either of those are the case, stating them in the text would be really useful.

Is the log in the function set a natural log? In table 8, the result of ACT-R is presented as a natural log, but the function set just says "log", which could be assumed to be log10. If it is log10, why not include ln if it is used in ACT-R's results?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new algorithm that jointly optimizes a neural network and an equation (that acts as an interpretable surrogate). The paper also explores update strategies of varying update rules. The approach proposed is then evaluated on real-world memory behavior datasets. The prediction performance of the neural network and discovered equation are reported separately.

### Strengths
1. The idea of jointly optimizing an equation with a neural network is novel among symbolic regression (SR) algorithms to the best of my knowledge.
1. Figure 2 gives a clear overview of the algorithm.

### Weaknesses
1. It is unclear whether the main aim of the paper is to discover memory equations or to propose a new SR-based algorithm. If the objective is to introduce both at the same time, then the paper is in an awkward position because it is not mentioned or made obvious in the paper why this specific task "to discover memory equations" require the proposed method (e.g., the paper should explain why the joint optimization with a neural network method is particularly effective for discovery memory equations and not applicable to other domains such as Physics). If the method proposed is indeed not specifically tailored to "discover memory equations", then evaluation on other datasets would provide a stronger case for this paper.

2. Missing comparisons to state-of-the-art SR algorithms, that do not use joint optimization with a neural network, should be included as comparisons in the paper (expand Table 2).

3. Existing SR benchmark datasets such as SRBench and SRSD should be used to evaluate the proposed algorithm's equation discovery ability to improve the quality of experiments.

4. Missing error bars for empirical results, unable to tell if the difference in performance is significant (apart from Table 1 which performs t-test).

5. Missing details on the selection of MLP architecture and tuning.

6. In line 308, PySR was selected among SR algorithms but this choice was not justified. Several recent state-of-the-art SR algorithms (e.g., DSR [1], TPSR [2]) should be considered as well. Otherwise, the paper should justify why these methods were not considered.

### Questions
1. How does SPsyINN perform on existing equation discovery benchmark datasets like SRBench and SRSD?

1. How do state-of-the-art SR algorithms perform in comparison on SPsyINN? The equations these state-of-the-art SR algorithms discover can be used to expand Table 2.

1. Where are the error bars for all the empirical results (i.e., standard deviation or inter-quartile range)?

1. Table 2 is given but not referenced to. Can the paper include a description and discussion of the results in Table 2?

Some of these questions may simply not be relevant because of the scope that the authors have set for the paper. If that is the case, I hope the justification for the limited scope can be addressed in the rebuttal.

**After Author-Reviewer Discussions:**

1.	The results are still not reproducible. I obtain the MAE values of 0.168, 0.164, 0.161 for PsyINN-C-F, PsyINN-I-F, PsyINN-W-F respectively, which differs largely from the values in Table 5. The standard deviation they have provided are in the range of 0.0016 to 0.0008, there is no reason for the values I obtained to be so different from what they have reported.

1.	The initial version, the first revision and the final revision has 3 separate set of equations. For example, for SPsyINN-I-F, MaiMemo, the discovered equation presented was different in all 3 versions. Given that the intention of these equations are meant for experts to analyze, I do not think the paper is in a ready-state given its frequent unstable updates.

1.	On closer inspection of the dataset, the true regression label is mostly 1. I computed the MAE of a naive regressor that always predicts the value 1, and obtained the MAE value of 0.1038 on the test set. This beats all but one of the methods in the duolingo dataset (that is if we can even trust the results. Based on my own re-computation of the equations in Table 5, none of their discovered equations beat this).

1.	MAE and MAPE are present, but because most of the values are 1, I also computed the R2 score which is the most common evaluation metric for equation discovery papers. The R2 score on duolingo were 0.00164, -0.00382 and 0.00774 for SPsyINN-C-F, SPsyINN-I-F, SPsyINN-W-F. These discovered equations will not be helpful to behavioural modelling.

**I recommend that the other reviewers do their own independent check on the reproducibility of the paper. This can be done quickly, purely in excel, just to check the equations, using 'test.csv' provided in the dataset (csv) file. After the many revisions, I do not trust using the evaluation code provided.**

I have not even had the time to check whether the “creation of these equations” are reproducible because of the constant revision of errors the paper made. I am considering downgrading my rating to "Strong Reject".

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The author propose a method for modelling memory behavior. This method combines symbolic regression and deep learning. A deep network and a symbolic regressor based on genetic algorithms are both jointly trained to predict memory performance from data. The neural network component also includes a loss based on noisy data to improve noise tolerance. Importantly, the two components are also trained to match each other through an alignment loss on their respective output, allowing both of them to train each other.

The resulting model seems to outperform existing approaches in predicting memory behaviors on various datasets.

===Edit after authors' response===

The authors have addressed my comments and largely clarified the paper. I believe the idea of jointly optimizing a neural network and an analytical expression is interesting and seems to show promise. Therefore, I increase my score, though still with low confidence.

### Strengths
The problem is interesting, as far as I can tell (I am not an expert in this area).

The method seems novel and the proposed interplay between deep learning and symbolic regression is interesting.

The model seems successful, judging from reported results.

### Weaknesses
I am mostly concerned about clarity, as the paper often uses confusing notation and undefined acronyms. While the overall method is reasonably clear, it is not easy to understand the details or reported comparisons in performance. See Questions below.

The actual task is not fully described. Fig 1 mentions answers being "correct" or "incorrect", but about what? What was the actual question being asked for each word?

What is the final overall output of the model (i.e. the one used to generate results in the tables)? Is it the output computed from the generated equation, or the output of the neural network?

The notation is confusing and seems to vary. I'd recommend using always 1:m to denote multiple timesteps and m to denote one single time steps (in the last sentence of Problem statement, apparently just 'm' is used to denote a whole sequence?)

There are many undefined acronyms. E.g. in l. 269 What does KT stand for? Where does this "KT-based framework" come from?

L. 276, where do the Beta_t come from? The noise schedule equations look very much like the ones used in diffusion model, which should warrant some kind of citation!

In the results, particularly the ablations, the various alternative methods are not described. As a result it is not at all easy to understand what each alternative version represents. In particular: do you report results based on training a neural network alone (with or without denoising), and a symbolic regressor alone?

In the baselines, the so-called "DKT" model is referenced multiple times, but it is never explained what DKT is (unless I missed it)!

### Questions
The actual task is not fully described. Fig 1 mentions answers being "correct" or "incorrect", but about what? What was the actual question being asked for each word?

What is the final overall output of the model (i.e. the one used to generate results in the tables)? Is it the output computed from the generated equation, or the output of the neural network?

The notation is confusing and seems to vary. I'd recommend using always 1:m to denote multiple timesteps and m to denote one single time steps (in the last sentence of Problem statement, apparently just 'm' is used to denote a whole sequence?)

There are many undefined acronyms. E.g. in l. 269 What does KT stand for? Where does this "KT-based framework" come from?

L. 276, where do the Beta_t come from? The noise schedule equations look very much like the ones used in diffusion model, which should warrant some kind of citation!

In the results, particularly the ablations, the various alternative methods are not described. As a result it is not at all easy to understand what each alternative version represents. In particular: do you report results based on training a neural network alone (with or without denoising), and a symbolic regressor alone?

### Soundness
3

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
5

### Summary
In this work, the Authors combine deep neural networks with genetic symbolic regression to model human memory in an efficient and interpretable manner. They proposed multiple ways to combine these two models, aiming at both compute efficiency and accuracy. The proposed model was tested on a panel of benchmarks where it showed an improved performance compared to a panel of baseline models.

### Strengths
The originality of the model lies in the novel combination of existing techniques (deep networks, denoising, and symbolic regression) and its application to the new domain (memory). I would like to especially highlight the new alignment algorithms, proposed here to account for the CPU – GPU interaction in the model, and domain priors that, first, kept the symbolic regression equations within the realm of memory model equations, and, second, accounted for the noise specific to memory-related data.

The significance of this model is in providing the equations (e.g. in Table 2) that are concise and at the same time have a high explanatory power for the memory-related data. Further analysis of such equations looks plausible and may be beneficial for the fields of psychology, cognitive science, and neuroscience.

The quality of this work is in the thorough empirical evaluation of the proposed model. While the model itself is rooted in literature and thus alone holds the potential of being useful for the task at hand, the evaluation on a series of datasets and the ablation study shows that the model indeed leads to the improvement of the performance and that all model components are necessary for such an improvement.

### Weaknesses
I would suggest working on the text a little bit more to enhance its clarity to make it more accessible to the broad ICLR community. While the work introduces a relatively straightforward idea – (i) merge an efficient deep learning model with an interpretable symbolic regression model and a denoising module; (ii) use auxiliary losses that would match the outputs of the three models; (iii) compute auxiliary losses on an intermittently-generated proxy dataset to smoothly synchronize CPU and GPU computations – the text itself is often unnecessarily complicated. For example, I’d either simplify Figure 2, remove the equations from it, or move it down the text to serve as a summary. I’d then simplify the equations and remove some of them because, while they introduce straightforward concepts – like, the mean square error loss – they end up being pretty lengthy. This is best exemplified by Equations 8 and 9 which say: “compute the loss on a batch” but somehow occupy nearly half a page. I would also draw attention to some of the results that are present in the paper but may be overlooked, e.g. the equations in Table 2. These results also could use further discussion. Besides, even though the code is provided, I couldn’t find the Methods section that would describe the model in sufficient detail to reproduce it (e.g. the parameters of the neural network and the training schedule).

Minor:

The background section mostly repeats the introduction. I’d suggest shortening one of these sections and either expanding the other with the details of the models or using the vacated space for an additional discussion of the results.

‘1 + 1 greater than 2’ effect -> synergy effect

KT-based framework: KT is not defined in the main text

MAE is not defined in the main text

Table 1: second best models: clarify that those do not include SPsyINN models

Table 2 is not referenced in the results.

Table 3: provide the statistical significance test data (ideally with the false discovery rate correction)

### Questions
The Authors state that the equations, that the model converges to, vary depending on the initial conditions and, it seems, on the model’s waiting strategies. Thus, which of the equations should neuroscientists / cognitive scientists use in their research as a result of this project? Are these equations similar or locally similar? Should they be distilled or approximated? How sensitive are these equations to the numerical coefficients? As one of the work’s stated goals is the interpretability of the results, it is important to know what results to use and to what degree to trust them. It would be great to hear the Authors’ thoughts on this topic. Separately, it would be highly interesting to see an analysis of the final equation once it’s established. How similar or dissimilar would it be to/from the existing models? What are the additional terms and what do we learn from them? Does it help us to ground the memory dynamics in neural circuits? An analysis like that has the potential to further increase the impact of this work.

_____________________________

Post-rebuttal: concerns mostly addressed (especially the ones regarding the clarity of the writing); raising my score to 8.

_____________________________

Post-discussion. We had a super lengthy and detailed discussion among the Reviewers where they encouraged me to check the reproducibility of the result. Sadly, they turned out to be right: (1) plugging the provided equations into the provided data reproduces the other Reviewer's numbers but not those in the paper; (2) MAE's denominator is not affected by zero labels; (3) zero labels cannot be excluded from a binary dataset.

As I mentioned before, I really like the paper but the other Reviewers are correct in pointing out that it's a serious issue. I hope that the Authors manage to revise their result towards consistency, stability, and reproducibility, hopefully also grounding them in cogsci-derived priors. Meanwhile, I sadly have to adjust my score to reflect the apparent reproducibility issue.

### Soundness
2

### Presentation
3

### Contribution
3

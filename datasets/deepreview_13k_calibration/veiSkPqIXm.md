# OpenPL: Realistic Evaluation of Prompt Learning for VLM in Open Environments

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
Vision-language models (VLMs) have demonstrated impressive zero-shot capabilities across various image classification tasks. Their performance can be further enhanced through prompt learning methods. To evaluate the effectiveness of prompt learning, it is important to assess its robustness to new classes and distributional shifts. However, current studies typically assume single data distribution shifts and pre-known new class space, which still have gaps with real-world open environments where data distributions and classes are often uncertain and subject to continuous change. To better analyze the robustness of prompt learning methods in more realistic scenarios, we propose a novel evaluation benchmark called OpenPL from the following perspectives: 1) We reconstruct multiple scenarios of open environments, encompassing dynamic class changes, dynamic distribution shifts, and dynamic co-evolution of both distribution and classes; 2) We propose a series of new performance metrics for prompt learning methods based on the Dynamic Robustness Curve (DRC) to better understand their robustness in open environments; 3) We re-implement diverse prompt learning methods and evaluate their performance on the proposed OpenPL benchmark. The results show that no current prompt learning method is robust to open environments and no meaningful performance improvement is achieved compared to the zero-shot performance, designing robust prompt learning methods remains a difficult task. All re-implementations are available at \url{https://anonymous.4open.science/r/OpenPL-565E}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes OpenPL, a new benchmark for evaluating the robustness of prompt learning methods for Vision-Language Models (VLMs) in evolving environments.  
Key contributions of the paper are as follows: 

- **Introducing new evaluation paradigms:**
    - Dynamic class changes scenarios (both emerging new classes and varying ratios of new/base classes)
    - Dynamic distribution shifts scenario using ImageNet variants
    - Dynamic co-evolution scenario where both class and distribution changes occur simultaneously

- **Introducing new performance metrics:**
    - Introduces the Dynamic Robustness Curve (DRC) and several metrics and two robustness definitions based on it
    - Metrics include Area Under Curve (AUC), Worst-case Accuracy (WA), Expected Variation Magnitude (EVM), Variation Stability (VS), Positive Area (PA), and Negative Area (NA)

- **Comprehensive Evaluation:**
    - Evaluates 10 prompt learning methods across 11 diverse datasets

Overall, the paper provides a thorough evaluation framework for understanding how prompt learning methods perform in evolving scenarios where both classes and data distributions can change dynamically.

### Strengths
The strengths are:

- The evaluation of the prompt learning methods in the paper is comprehensive, covering 10 methods across 11 datasets. This serves as a valuable reference for future work.
- The paper introduces dynamic changes to the evaluation environment of prompt learning methods.
- The evaluation metrics are also comprehensive, aiming to cover different aspects of robustness in prompt learning methods.
- Prior work has been properly referenced.
- Clear diagrams and tables have been provided to give an overall picture of the performance of different methods in an efficient and useful manner.
- The sections follow a smooth, coherent narrative, and the proper ordering builds step by step toward delivering the main goal of the paper.

### Weaknesses
 - What the name of the paper suggests is not actually what the paper provides. The title says "realistic evaluation"; however, the evaluation seems to be synthetic in the sense that it uses the exact same datasets that are used in prior work such as CoCoOp and only introduces a parameter `t` (which is why I call it synthetic) that determines the portion of new classes/distribution relative to the training class distribution.

- Common terminology in the literature on prompt learning is not respected in this work. For example, many of the main evaluation paradigms introduced in this paper already exist in prior work such as CoCoOp and MaPLe. Base-to-Novel Generalization corresponds to Dynamic Class Change scenarios, Domain Generalization corresponds to Dynamic Distribution Shift scenarios, and Cross-Dataset Evaluation corresponds to Dynamic Co-evolution of Distribution and Class Variation scenarios. The only difference in this paper is the addition of the parameter `t` that determines the degree or proportion of new class/distribution/dataset samples to base class/distribution/dataset samples. Introducing this new terminology—especially in the case of Dynamic Co-evolution of Distribution and Class Variation—rather than using simpler and more familiar phrases like Cross-Dataset Generalization may be confusing.

- One of the main concerns about the paper is its novelty due to the following reasons:
  - As mentioned, the exact same evaluation scenarios exist in prior work except for the absence of parameter `t`.
  - Moreover, the same 11 datasets are used for the evaluation scenarios as in prior work, which is acceptable; however, when the title suggests "realistic evaluation," the authors should provide material to live up to this promise or change the title.
  - The evaluation of prompt learning methods, while a good reference for any future comparisons and work, does not contain any new discoveries about their performance. In other words, most of the observations reported are already known.

- The authors make some strong negative claims about prompt learning methods while providing no strong evidence, and in some cases, the experiments in the paper itself are not consistent with the claims. For example, there is a claim in the abstract stating that "no current prompt learning method is robust to open environments and no meaningful performance improvement is achieved compared to zero-shot performance." However, by looking at Figure 1, we can see that most prompt learning methods show gains compared to the zero-shot case in the emerging new classes paradigm.

- The robustness definitions and some evaluation metrics have not been carefully crafted and contain logical or notation errors. For example, Performance-Gain Robustness is defined as having AUC - AUC_zs ≥ δ_AUC for all `t`. However, AUC is the area under the curve, making it no longer a function of `t`. The same issue applies to the definition of Decay-Gain-Ratio Robustness.

- There is inaccurate information in the Introduction and Related Work sections about prior research. For example, this part of the paper states, "MaPLe (Khattak et al. (2023a)) proposes benchmarks for Cross-Dataset Evaluation and Domain Generalization by training on ImageNet and altering the test data distribution," suggesting that MaPLe introduces the benchmark. However, the benchmark already exists in CoCoOp, which is an earlier work.

- There are numerous English grammar and writing errors, even in the title. This is especially evident in the Introduction and Related Works sections; for example, "at the earliest time, CoOp (Zhou et al. (2022b)) explored ..."

### Questions
- Can you please explain and provide clear evidence for why you think the introduced paradigms aid in the realistic evaluation of the methods? To me, it seems your benchmark is a synthetic benchmark due to parameter `t`. Perhaps you could also consider revising the title.

- As you mention in the paper, the main purpose of prompt learning is to adapt a Vision-Language Model (VLM) to downstream tasks; in other words, it is a form of fine-tuning on specific datasets. Therefore, it is not expected to show the same level of performance on unseen datasets/classes as it does on the source (training) datasets/classes. In fact, a prompt learning method is considered effective if it improves performance on the source dataset while maintaining, or even slightly improving, the original generalization capacity of the VLM on unseen data. However, it seems that most of the strong negative statements made in the paper are based on the assumption that the primary goal of the prompt learning method is to improve the generalization trend of a VLM as parameter `t` increases. If it fails to do so, it is deemed poor. In contrast, where zero-shot performance drops, I expect the same for the prompt learning method, and I do not expect it to remain the same or, even more strangely, to increase. Is this the case that you have the mentioned assumption? If yes, then I believe this is an improper assumption based on prior work. If no, then I suggest revising the strong negative claims, including those in the abstract, Observations 2 and 3 at the end of the introduction, and elsewhere in the paper.

- Observation 4 at the end of the introduction could be considered a new finding and a contribution; however, there is no strong evidence to support this claim in the paper, aside from a brief mention in section 5.5. Please provide evidence for this and include more detail on why you believe so. More generally, if you can present additional observations similar to Observation 4 that go beyond simply analyzing the performance of different methods and instead identify key features in various methods that enable them to outperform others in a scenario, this would significantly enhance the value of your contributions—provided there is strong evidence and experimentation to back it up.

- Please clarify in the paper what you mean by the Dynamic Co-evolution of Distribution and Class Variation scenario e.g. by mentioning that it measures cross-dataset generalization. This is unclear in the paper. The Dynamic Distribution Shift also needs clarification; for example, what happens when other variants of ImageNet are introduced, and why does this change the distribution?

- Please clarify what `x` refers to in lines 203 and 204 inside the table.

- Please clarify lines 213 and 214 under the rank definition; `m` cannot be both 6 and 6xn at the same time.

- Please revise both robustness definitions. AUC, PA, and NA do not depend on `t`.

- It is unclear what kind of robustness the Decay-Gain-Ratio Robustness metric is supposed to measure; please explain in detail what it actually means.

- It might be beneficial to add grids to the diagrams.

- Please explain why the delta values for both robustness metrics are almost the same numbers in Tables 6 to 9.

- There are a considerable number of vague sentences throughout the paper; please clarify them. I understand this may seem too general, but the number of cases is larger than I can mention individually.

- Please address the English writing mistakes; this is a serious issue throughout the paper. I know this might seem too general, but the number of cases is larger than I can mention one-by-one.

- Please ensure that the information regarding prior work in the Introduction and Related Work sections is accurate and informative, as well as anywhere else in the paper. This is also a serious issue.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a new benchmark called OpenPL, where they evaluate the performance of existing prompt learning frameworks in diverse and realistic open world environments. They have an interesting observation that there is no one method that performs well across all scenarios.

They introduce several realistic test scenarios: 1. Dynamic class changes; 2. Dynamic Distribution shifts; 3. Dynamic Co-evolution of distribution and class variation and also performance metrics to evaluate them.

### Strengths
1. They establish an impressive benchmark which extensively covers VLMs, prompt learning methods, detailed analysis of these methods in the above defined realistic test scenarios.
2. They introduce several performance metrics carefully designed to analyse the performance of  different algorithms in the open world scenarios. These metrics are very intuitive and aptly designed for this problem.
3. The results are presented in a very clear and concise manner. 
4. It is a bold and a much needed evaluation of prompt learning methods. The analysis presented could be very insightly for the research community interested in the adapatation of VLMs.

### Weaknesses
 **Implementation details:**
1.  The descriptions of charactezing difficulty of a test scenario using $t$ while is fairly well defined, it can be done in a more detailed manner. 
2. Please describe how the datasets are set up for this problem in more detail. How the classes are split, sample size etc.
3. This being a benchmark paper, the experimental details are equally important to help reproducibility. The provided details do not suffice I believe. 
4. Explaining how the problem is setup in each scenario, taking a dataset as an example can really help the readers. 
5. The assumption that new class names are known before testing is unrealistic. As this defines the difficulty of the test scenario, if it is known, one can choose simpler methods that can work more realibly in difficult scenarios?  

**Metrics:**
1. All the tables report $Acc(0)$. Based on the definition(line 144, 151, 160), $t=0$ corresponds to evaluation on base task with no new classes or distribution shifts or both. Why is $Acc(0)$ reported in all tables. A suggestion, it is more appropriate to report $Acc(1)$ which corresponds to the most severe case in each scenario which can rather explain your case well. 
2. EVM is low for CLIP for most cases. So, can we infer that one is better off using Zero-shot CLIP when one doesn't know the difficulty of test scenario apriori?

### Questions
1. In  implementation details, it is mentioned that the maximum number of classes and sample size is fixed for all datasets. But, in Section 3.1, line 137, it is mentioned that half the classes from the dataset serve as base classes and the other half as new classes. How is it actually set? 
2. In the case of class changes (3.1 and 3.3), the model is trained on base classes and tested on base and new classes. For eg., in ImageNet, the model is trained for 500 classes with 500 text classifiers. The model is tested on 1k classes, with a 1k length text classifier right? Are the names of new classes assumed to be known before testing? That is not a very realistic assumption to have.
3. $t$ characterizes the difficulty of a test scenario as I understand. A model is trained on base classes and just tested on base and new classes(assuming the new class names are known). The authors mention "As t increases, new classes continually emerge while base classes diminish". This defines different test scenarios but not a changing test scenario as I interpret it. The classes do not continually emerge during test time in the problem right? I request the authors to clarify that this is different from Test Time Adaptation setting. Nothing changes continually during test time. They are all just different test scenarios. 
4. Clarify what it means as $t$ increases in line 163.
4. In Figure 2, what is the total number of classes fixed to. Is it fixed for all datasets. If so, what if this is changed? A 50 base + 50 new classes is a very different scenario than 500 base + 500 new classes scenario.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces OpenPL, a benchmark designed to evaluate the robustness of prompt learning methods under open-world conditions, such as the introduction of new classes and distribution shifts. Unlike conventional benchmarks, OpenPL attempts to simulate a more realistic scenario with evolving classes and distribution changes that are common in real-world applications. The paper presents various analyses, comparing several prompt learning methods across different datasets.

### Strengths
- **In-depth analysis**: OpenPL challenges current prompt learning generalization benchmarks moving beyond fixed-class setups, aiming to better reflect real-world dynamic conditions.
- **Writing**: The writing is clear and the paper easy to follow.

### Weaknesses
 - **Unclear motivation**: While the motivation of evaluating robustness of prompt learning method on continuous environment is clear, the paper lack describing what would be the expected desired behavior in each introduced setup. Furthermore, the newly introduce metrics lacks explanation and motivation.

- **Limited novelty**: While the proposed benchmark may be of interest it remains a simple refinement of existing ones and the contribution of the paper may be limited for a conference like ICLR. Furthermore, there is 

- **Controversial/vague conclusions**: Several questionable observations are made throughout the paper (see questions).

 - **Regarding the evaluation protocoles**:
    - **Emerging new classes protocole**: The fact that the classification performance declines as new classes are introduced seems obvious: as the number of labels increases, the classification problem becomes more difficult. Furthermore, while it is difficult to disagree with the claim that no method "consistently maintain optimal performance", we can see that PromptSRC appears to perform within the top two across most datasets. My point is that the observation made is too vague and it is unclear what insight the paper provide here. The paper should provide a more detailed analysis of the failure modes of each method under this protocol, rather than simply stating that performance degrades. For example, do some methods struggle more with specific types of new classes, or is the degradation uniform across all new classes?

    - **Varying ratio of classes**: In this scenario the number of classes remains constant and only the proportion of base/new classes varies. Why is the performance of CLIP not stable when varying t  on some datasets (like Eurosat) ? Don't you think that the split of classes may have produce classification problems that are uneven in term of difficulty ? You may consider reporting the relative improvement of each method w.r.t CLIP. The paper should investigate if the instability of CLIP is due to the class sampling or some other factors. Furthermore, the paper should provide a more detailed analysis of the relative performance of each method, rather than just reporting the raw numbers.

    - **Distribution shifts**: I am not sure why the authors claim that "there is no significant improvement across algorithms when addressing the issue of dynamic data distribution shifts". Don't all prompt learning method improve the performance over CLIP on Imagenet variants for each value of t ? The paper could benefit from a more careful discussion of what constitutes “significant” improvement in this context. If the authors intended to imply that prompt learning should slow the rate of performance decline under distribution shifts, I think that it may be a potentially unrealistic thing to expect. The paper should provide a more rigorous definition of what constitutes a significant improvement, and justify why this definition is appropriate for the task. Furthermore, the paper should analyze the types of distribution shifts that are most challenging for each method.

    - **Co-evolution of distribution and class variation**: What are the domain shifted datasets used in figure 4 ? For instance did you use an Imagenet variant for new-classes and shifted instances and Caltech for base classes and unshifted instances ? On what dataset are the prompt learned in this experiment ? I think we cannot expect prompts learned on a specific and fine-grained dataset like Eurosat to generalize to new classes like the ones of Imagenet, this is why the cross-dataset generalization benchmark is usually performed with prompts learned on Imagenet and evaluated on the fine-grained datasets and not the other way around. The paper needs to clarify the experimental setup, including the specific datasets used for each part of the experiment. The paper should also justify why the chosen experimental setup is appropriate for evaluating the robustness of prompt learning methods.

- Given the identified weaknesses, do you have any insights or potential solutions for mitigating these issues in prompt learning methods?

 - Other comments: 
    - In related works the description of ProDA is not accurate: "ProDA learns output embeddings of textual prompts rather than input embeddings". ProDA learns an ensemble of prompts in the input embeddings space and use a distributional objective over the output space to learn them instead of using the cross-entropy loss for each one of them independently.
    - You may consider adding the following recent works on prompt learning: 
        - Mistretta et al "Improving Zero-shot Generalization of Learned Prompts via Unsupervised Knowledge Distillation" (ECCV24)
        - Lafon et al "GalLoP: Learning Global and Local Prompts for Vision-Language Models" (ECCV24).

### Questions
- **Regarding the evaluation protocoles**:
    - **Emerging new classes protocole**: The fact that the classification performance declines as new classes are introduced seems obvious to me: as the number of labels increases, the classification problem becomes more difficult. Furthermore, while it is difficult to disagree with the claim that no method "consistently maintain optimal performance", we can see that PromptSRC appears to perform within the top two across most datasets. My point is that the observation made is too vague and it is unclear to me what insight the paper provide here.

    - **Varying ratio of classes**:
    In this scenario the number of classes remains constant and only the proportion of base/new classes varies. Why is the performance of CLIP not stable when varying t  on some datasets (like Eurosat) ? Don't you think that the split of classes may have produce classification problems that are uneven in term of difficulty ? You may consider reporting the relative improvement of each method w.r.t CLIP.

    - **Distribution shifts**: I am not sure why the authors claim that "there is no significant improvement across algorithms when addressing the issue of dynamic data distribution shifts". Don't all prompt learning method improve the performance over CLIP on Imagenet variants for each value of t ? The paper could benefit from a more careful discussion of what constitutes “significant” improvement in this context. If the authors intended to imply that prompt learning should slow the rate of performance decline under distribution shifts, I think that it may be a potentially unrealistic thing to expect.

    - **Co-evolution of distribution and class variation**: What are the domain shifted datasets used in figure 4 ? For instance did you use an Imagenet variant for new-classes and shifted instances and Caltech for base classes and unshifted instances ? On what dataset are the prompt learned in this experiment ? I think we cannot expect prompts learned on a specific and fine-grained dataset like Eurosat to generalize to new classes like the ones of Imagenet, this is why the cross-dataset generalization benchmark is usually performed with prompts learned on Imagenet and evaluated on the fine-grained datasets and not the other way around.

- Given the identified weaknesses, do you have any insights or potential solutions for mitigating these issues in prompt learning methods?

 - Other comments: 
    - In related works the description of ProDA is not accurate: "ProDA learns output embeddings of textual prompts rather than input embeddings". ProDA learns an ensemble of prompts in the input embeddings space and use a distributional objective over the output space to learn them instead of using the cross-entropy loss for each one of them independently.
    - You may consider adding the following recent works on prompt learning: 
        - Mistretta et al "Improving Zero-shot Generalization of Learned Prompts via Unsupervised Knowledge Distillation" (ECCV24)
        - Lafon et al "GalLoP: Learning Global and Local Prompts for Vision-Language Models" (ECCV24).

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work explores the application of Vision-Language Models (VLMs) in practical open environments, where data distributions and classes are often uncertain and continuously evolving. To better assess the capability of current prompt learning methods in handling these dynamic conditions, the authors propose a benchmark called OpenPL. OpenPL simulates open environments by incorporating dynamic class changes, distribution shifts, and co-evolution of both distribution and classes. Additionally, the work introduces a range of metrics for comprehensive evaluation and provides extensive experiments across various methods, with insights derived from the experimental results.

### Strengths
1. The approach to simulating an open-world environment is well-reasoned.

2. A variety of metrics are introduced to evaluate different methods effectively.

3. The experiments are extensive, and insights are offered based on the results.

### Weaknesses
More detailed descriptions and analysis of the benchmark construction should be provided.

1. For the Emerging New Classes scenario: 

(a) Does the selection of base classes influence the performance of different methods, for example, by selecting either easy or difficult base classes? 

(b) Is the number of newly added classes the same at each time step t?

2. The parameter t appears frequently and represents different aspects in each scenario. I suggest using different notation to distinguish these parameters clearly.

3. Since the test process is continuous (with changing classes/distributions), a forgetting score should also be applied to measure performance across methods. For example, performance on the original distribution or class set could be used to assess forgetting [a].

[a] Efficient test-time model adaptation without forgetting. ICML 2022

4. Why is the initial prompt set to “XXXX” instead of the widely used “a photo of a” in prompt learning? Would different prompt initializations affect the performance?

5. Most of the methods tested are few-shot prompt learning methods. Would the proposed benchmark also apply to unsupervised prompt tuning methods [b, c] and test-time prompt tuning methods [d, e, f]? The authors are suggested to provide some discussion about this point.

### Questions
Please see Weakness for details.

### Soundness
3

### Presentation
3

### Contribution
3

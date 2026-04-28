# APBench: A Unified Benchmark for Availability Poisoning Attacks and Defenses

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
The efficacy of availability poisoning,
a method of poisoning data by injecting
imperceptible perturbations to prevent its use in model training,
has been a hot subject of investigation.
Previous research suggested that it was difficult
to effectively counteract such poisoning attacks.
However, the introduction of various defense methods
has challenged this notion.
Due to the rapid progress in this field,
the performance of different novel methods
cannot be accurately validated due to variations in experimental setups.
To further evaluate the attack and defense capabilities
of these poisoning methods,
we have developed a benchmark --- APBench
for assessing the efficacy of adversarial poisoning.
APBench consists of 9 state-of-the-art
availability poisoning attacks,
8 defense algorithms,
and 4 conventional data augmentation techniques.
We also have set up experiments
with varying different poisoning ratios,
and evaluated the attacks on multiple datasets
and their transferability across model architectures.
We further conducted a comprehensive evaluation
of 2 additional attacks
specifically targeting unsupervised models.
Our results reveal the glaring inadequacy
of existing attacks
in safeguarding individual privacy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents APBench, a unified benchmark designed to evaluate the efficacy of availability poisoning attacks and defenses in machine learning. Availability poisoning attacks subtly manipulate training data to disrupt model learning, created to mitigate concerns about data security and privacy. APBench addresses this by offering a standardized platform, including 9 advanced poisoning attacks, 8 defense algorithms, and 4 data augmentation techniques, facilitating comprehensive evaluations across different datasets, model architectures, and poisoning ratios. The results highlight the limitations of existing attacks in ensuring privacy, underscoring the need for more robust defenses. APBench is open-sourced, aiming to foster advancements in secure and privacy-preserving machine learning.

### Strengths
- Comprehensive Benchmarking. APBench provides a comprehensive and unified benchmark for evaluating availability poisoning attacks and defenses, addressing a crucial gap in the field. It includes a wide array of state-of-the-art poisoning attacks, defense algorithms, and data augmentation techniques, ensuring its relevance and applicability to a broad spectrum of scenarios.

- Extensive Evaluation. The paper conducts extensive evaluations across various datasets, model architectures, and poisoning ratios. This thorough testing ensures that the results are robust and reliable, providing valuable insights into the effectiveness of different attack-defense combinations.

### Weaknesses
 - While APBench provides a comprehensive evaluation of availability poisoning attacks and defenses, it is limited to this specific type of adversarial attack. Other types of adversarial attacks, such as integrity or backdoor attacks, are not covered. This direction would be interesting. For example, the defenses that have been developed for resisting backdoor attacks might be capable of mitigating the existing availability attacks. This phenomenon is possible, since it has been observed that the best defense against test-time adversarial examples is also a principled defense against availability poisoning attacks. A more unified benchmark can facilitate the discovery of these possibilities and opportunities.

- The TAP attack should be partially attributed to Nakkiran [1], who was the first to point out such class targeted attacks. The unique contribution of [2] is that they found that untargeted adversarial examples can also be an effective availability poisoning attack. (This information is recorded on page 4 of the camera-ready version of [2].)

### Questions
- How might defenses originally developed for backdoor attacks, e.g. ANP [3], be effectively repurposed to mitigate availability attacks? 

- This benchmark exclusively focuses on evaluating the natural test accuracy of the trained models. How about their test robustness, e.g., PGD-20 accuracy?


[3] Wu & Wang, Adversarial Neuron Pruning Puriﬁes Backdoored Deep Models, NeurIPS 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper acknowledges the challenges in evaluating availability poisoning attacks and introduces an open-source benchmark, APBench, which comprises various poisoning attacks, defense strategies, and data augmentation techniques. The benchmark is designed to facilitate fair and reproducible evaluations, revealing shortcomings in existing attacks and promoting the development of more robust defense methods. Ultimately, APBench serves as a platform to advance availability poisoning attack and defense techniques, aiming to protect privacy and data utility.

### Strengths
- Diverse experiments
- Visual analysis results
- Encourages future research

### Weaknesses
 - Inadequate explanation for attack selection. The authors' rationale for selecting specific attacks in the context of availability poisoning requires further clarification. Since the aim is to establish a benchmark for general availability poisoning attacks, it is advisable to include a broader spectrum of attack types, such as those referenced in citations [1], [2], [3], and [4]. Currently, the focus appears to be primarily on clean label poisoning attacks, which may not align with the assumptions of availability poisoning attacks, which do not assume clean labels. Additionally, the presented attacks predominantly target deep learning networks, the authors should either tune down their scope or include attacks against other learning algorithms like SVM.

- Setup lacks explanation. In Section 5.1, during the evaluation of partial poisoning, it would be beneficial for the paper to provide clarity regarding the methodology employed for generating these partial poisons. Specifically, it would be valuable to know whether the process involves the initial generation of poisons using all clean data, followed by the selection of a subset from these generated poisons. Or do we solely utilize a portion of the data from the beginning to the end? It is important since training the surrogate model also necessitates clean data.

- Inconsistent results. In Figure 3 and 4, it is evident that both Greyscale and JPEG consistently exhibit a similar impact, demonstrating uniform performance across all attack methods and poisoning rates. However, this consistency appears to contrast with the performance discrepancies observed in other tables within the paper. It would be valuable if the authors could offer an explanation for this observed consistency

- Conclusions that appear to be at odds with the available evidence. In Section 5.1, the authors claim that in partial poisoning scenarios, test accuracy only slightly decreases compared to poisoning the entire dataset. However, it's important to support this claim with experimental evidence. Specifically, I reference the original paper on EM, which reveals that when 80% of the data is poisoned, the model maintains a test accuracy slightly above 80%, but this accuracy significantly drops to less than 20% when the entire dataset is subjected to poisoning. This substantial disparity in accuracy between partial and full dataset poisoning underscores the need for the authors to revise their statement and include a poison rate of 100% as a baseline in Figure 3 for a more comprehensive analysis.

- Incomplete defense evaluation. While the authors mention considering various existing defenses, the primary focus is on data preprocessing methods. It is advisable to provide more extensive results for training-phase defenses, which have proven effective in defending data poisoning. For instance, common defenses like adversarial training are briefly mentioned but not thoroughly discussed. Also, early stopping has shown its effectiveness in many cases. These defense mechanisms have been explored in previous work like [5] and [6] and should be given more attention. Alternatively, the scope of the paper could be refined to focus specifically on data preprocessing defenses to maintain coherence.

### Questions
- **Inadequate explanation for attack selection.** The authors' rationale for selecting specific attacks in the context of availability poisoning requires further clarification. Since the aim is to establish a benchmark for general availability poisoning attacks, it is advisable to include a broader spectrum of attack types, such as those referenced in citations [1], [2], [3], and [4]. Currently, the focus appears to be primarily on clean label poisoning attacks, which may not align with the assumptions of availability poisoning attacks, which do not assume clean labels. Additionally, the presented attacks predominantly target deep learning networks, the authors should either tune down their scope or include attacks against other learning algorithms like SVM.

- **Setup lacks explanation.** In Section 5.1, during the evaluation of partial poisoning, it would be beneficial for the paper to provide clarity regarding the methodology employed for generating these partial poisons. Specifically, it would be valuable to know whether the process involves the initial generation of poisons using all clean data, followed by the selection of a subset from these generated poisons. Or do we solely utilize a portion of the data from the beginning to the end? It is important since training the surrogate model also necessitates clean data.

- **Inconsistent results.** In Figure 3 and 4, it is evident that both Greyscale and JPEG consistently exhibit a similar impact, demonstrating uniform performance across all attack methods and poisoning rates. However, this consistency appears to contrast with the performance discrepancies observed in other tables within the paper. It would be valuable if the authors could offer an explanation for this observed consistency

- **Conclusions that appear to be at odds with the available evidence.** In Section 5.1, the authors claim that in partial poisoning scenarios, test accuracy only slightly decreases compared to poisoning the entire dataset. However, it's important to support this claim with experimental evidence. Specifically, I reference the original paper on EM, which reveals that when 80% of the data is poisoned, the model maintains a test accuracy slightly above 80%, but this accuracy significantly drops to less than 20% when the entire dataset is subjected to poisoning. This substantial disparity in accuracy between partial and full dataset poisoning underscores the need for the authors to revise their statement and include a poison rate of 100% as a baseline in Figure 3 for a more comprehensive analysis.

- **Incomplete defense evaluation.** While the authors mention considering various existing defenses, the primary focus is on data preprocessing methods. It is advisable to provide more extensive results for training-phase defenses, which have proven effective in defending data poisoning. For instance, common defenses like adversarial training are briefly mentioned but not thoroughly discussed. Also, early stopping has shown its effectiveness in many cases. These defense mechanisms have been explored in previous work like [5] and [6] and should be given more attention. Alternatively, the scope of the paper could be refined to focus specifically on data preprocessing defenses to maintain coherence.

[1] Poisoning Attacks against Support Vector Machines

[2] Towards Poisoning of Deep Learning Algorithms with Back-gradient Optimization

[3] Preventing Unauthorized Use of Proprietary Data: Poisoning for Secure Dataset Release

[4] Witches' Brew: Industrial Scale Data Poisoning via Gradient Matching 

[5] Is Adversarial Training Really a Silver Bullet for Mitigating Data Poisoning

[6] Poisons that Are Learned Faster are More Effective

### Soundness
1 poor

### Presentation
3 good

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
The paper studies availability poisoning attacks which add imperceptible perturbations to some samples to compute poisoning data and add it to the training data with the goal that the resulting model will perform poorly on any of the test data. In particular, the paper proposes a benchmark to evaluate various availability poisoning attacks and defenses; the benchmark is motivated from the fact that there are numerous attacks and defenses in the literature but no systematic framework or analysis of their comparisons. APBench has functionality to evaluate 9 attacks, 8 defenses, 4 data augmentations, and to ablate over different parameters of the attacks/defenses. Paper then provides evaluations of these attacks and defenses for 4 datasets and 4 model architectures, and finally an ablation study.

### Strengths
- Benchmarking is an important/useful step toward systemizing the knowledge in this area
- APBench seems to have comprehensive suite of attacks/defenses
- Paper has done thorough evaluation using APBench

### Weaknesses
 - Threat model is difficult to understand
- Plenty of evaluations but insights are missing
- Clarity of writing can improve

- I am not sure what is the threat model being studied. I noted that the paper mentions availability poisoning in different places but it would be good to have concrete details of the threat model, i.e., adversary’s goal, knowledge and capabilities.
    - Why such concrete threat model helps: In some parts of the paper APA is viewed as an attack that reduces model accuracy so it is a bad thing, but in some other parts, APA is (probably) viewed as a good thing because it protects private data from being learned by the model. My query might be naive but paper does not clarify it. Alternatively there might be two different settings where APAs are relevant: one where it is an attack that reduces accuracy and other where it is a defense that protects privacy. Authors should clarify these.
    - I also think the definition of AP in abstract is confusing: it says that AP is “a method of poisoning data by injecting imperceptible perturbations to prevent its use in model training”; my question: why do you even add such points to data? Maybe you want to say that you add these perturbed data to reduce model’s overall performance; which is what Eq (1) implies. But then the end of the abstract says “Our results reveal the glaring inadequacy of existing attacks in safeguarding individual privacy”, which sounds more like these attacks are deployed for something good, i.e., protecting individual privacy.
    - Eq (1) implies that AP is basically an untargeted attack that just aims to reduce model’s accuracy; if so, maybe explain this somewhere (preferably in threat model) for ease of understanding.
    - Overall I think the motivation of the attacks in this paper needs proper justification and there should a place in the paper for threat models/settings considered in the paper.
- I noted that there is a lot of evaluation in the paper, but I don’t know what insights to draw from them.
    - Evaluations feel like long blocks of text. I suggest highlighting useful text to help readers understand what in the final conclusion to draw from an eval.
    - At least some of the evaluations should highlight how APBench will help a practitioner identify something that prior works alone cannot identify. For example, in “Larger perturbations”, the conclusion is that “There exists a trade-off between perturbation magnitude and accuracy recovery”. This feels like an obvious conclusion; the paper should highlight what is it that APBench brings to the light that prior works could not.
- Paper is a bit difficult to read; I feel all the pieces are there in the paper but are not correctly placed/organized/explained:
    - In “privacy protection under partial poisoning”:
        - “As can be seen in Figure 3… the whole dataset”: this seems wrong; how can accuracy increase with more poisoning?
        - Mean losses of Figure 4: are these over training steps/ samples?
        - Can you rephrase the question: “can the protective perturbation… model training?” This question probably is about the good use of APAs; please clarify that as well.
        - “We find that the losses on the original… private data against learning”: If the private data is not supposed to be learned, why is it in the training data in the first place? Please clarify.
    - In “Future outlook”:
        - Future methods should enhance the resilience of perturbation: I am not sure if this is for good (improve privacy) or bad (improve attacks)? Clarify.

### Questions
I think the benchmarking direction of the paper is very important and useful to researchers from academia/industry. I am not an expert in this area but I believe that the paper is very comprehensive in terms of incorporating multiple attacks/defenses. Finally, I think the paper has also done a great job of thorough evaluation. Given this, below are my concerns that I feel authors should address:

- I am not sure what is the threat model being studied. I noted that the paper mentions availability poisoning in different places but it would be good to have concrete details of the threat model, i.e., adversary’s goal, knowledge and capabilities.
    - Why such concrete threat model helps: In some parts of the paper APA is viewed as an attack that reduces model accuracy so it is a bad thing, but in some other parts, APA is (probably) viewed as a good thing because it protects private data from being learned by the model. My query might be naive but paper does not clarify it. Alternatively there might be two different settings where APAs are relevant: one where it is an attack that reduces accuracy and other where it is a defense that protects privacy. Authors should clarify these.
    - I also think the definition of AP in abstract is confusing: it says that AP is “a method of poisoning data by injecting imperceptible perturbations to prevent its use in model training”; my question: why do you even add such points to data? Maybe you want to say that you add these perturbed data to reduce model’s overall performance; which is what Eq (1) implies. But then the end of the abstract says “Our results reveal the glaring inadequacy of existing attacks in safeguarding individual privacy”, which sounds more like these attacks are deployed for something good, i.e., protecting individual privacy.
    - Eq (1) implies that AP is basically an untargeted attack that just aims to reduce model’s accuracy; if so, maybe explain this somewhere (preferably in threat model) for ease of understanding.
    - Overall I think the motivation of the attacks in this paper needs proper justification and there should a place in the paper for threat models/settings considered in the paper.
- I noted that there is a lot of evaluation in the paper, but I don’t know what insights to draw from them.
    - Evaluations feel like long blocks of text. I suggest highlighting useful text to help readers understand what in the final conclusion to draw from an eval.
    - At least some of the evaluations should highlight how APBench will help a practitioner identify something that prior works alone cannot identify. For example, in “Larger perturbations”, the conclusion is that “There exists a trade-off between perturbation magnitude and accuracy recovery”. This feels like an obvious conclusion; the paper should highlight what is it that APBench brings to the light that prior works could not.
- Paper is a bit difficult to read; I feel all the pieces are there in the paper but are not correctly placed/organized/explained:
    - In “privacy protection under partial poisoning”:
        - “As can be seen in Figure 3… the whole dataset”: this seems wrong; how can accuracy increase with more poisoning?
        - Mean losses of Figure 4: are these over training steps/ samples?
        - Can you rephrase the question: “can the protective perturbation… model training?” This question probably is about the good use of APAs; please clarify that as well.
        - “We find that the losses on the original… private data against learning”: If the private data is not supposed to be learned, why is it in the training data in the first place? Please clarify.
    - In “Future outlook”:
        - Future methods should enhance the resilience of perturbation: I am not sure if this is for good (improve privacy) or bad (improve attacks)? Clarify.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a benchmark of data poisoning attacks. The authors suggest an unified codebase where to test poisoning attacks and defenses.

### Strengths
+ Systematization effort for data poisoning attack evaluations

### Weaknesses
 - the paper should be restructured
- does not compare with existing benchmarks
- limited contribution

**The paper should be restructured**.
The sections of the paper are not disponed in a natural order. The authors should first describe the framework for systematizing data poisoning and defenses, then introduce the related work by matching the framework with the existing methods. This would increase the clarity of the paper, that otherwise is confusing and seems disconnected in its sections. The related work should be connected to the framework, otherwise rather than a benchmark this would simply be a collection of re-implemented methods. 

**Does not compare with existing benchmarks / limited contribution.**
There are existing benchmarks and surveys on data poisoning, that the authors don't cite and compare with. The systematization itself is already done in other existing surveys that are not cited by this work. A non-exhaustive list is given below:

* Survey on data poisoning
  * https://arxiv.org/abs/2205.01992

* Other benchmarks on data poisoning that are not discussed
  * http://proceedings.mlr.press/v139/schwarzschild21a/schwarzschild21a.pdf
  * https://openreview.net/forum?id=PP3H72O_E2f
  * https://arxiv.org/abs/2009.02276 / https://github.com/JonasGeiping/poisoning-gradient-matching (implements also other poisoning methods)
  * https://github.com/JonasGeiping/data-poisoning

The authors should clarify what they add to the existing benchmarks, otherwise, highlighting the contributions that were not available to the community before this work. This also includes the fact that some of the techniques included in the benchmark were already available as source code, so the authors should clarify the implementation effort added to the existing tools.

Additional crucial weaknesses that should be addressed:
- limitations are not discussed
- the paper exceeds the page limit

### Questions
# Comments:

**The paper should be restructured**.
The sections of the paper are not disponed in a natural order. The authors should first describe the framework for systematizing data poisoning and defenses, then introduce the related work by matching the framework with the existing methods. This would increase the clarity of the paper, that otherwise is confusing and seems disconnected in its sections. The related work should be connected to the framework, otherwise rather than a benchmark this would simply be a collection of re-implemented methods. 

**Does not compare with existing benchmarks / limited contribution.**
There are existing benchmarks and surveys on data poisoning, that the authors don't cite and compare with. The systematization itself is already done in other existing surveys that are not cited by this work. A non-exhaustive list is given below:

* Survey on data poisoning
  * https://arxiv.org/abs/2205.01992

* Other benchmarks on data poisoning that are not discussed
  * http://proceedings.mlr.press/v139/schwarzschild21a/schwarzschild21a.pdf
  * https://openreview.net/forum?id=PP3H72O_E2f
  * https://arxiv.org/abs/2009.02276 / https://github.com/JonasGeiping/poisoning-gradient-matching (implements also other poisoning methods)
  * https://github.com/JonasGeiping/data-poisoning

The authors should clarify what they add to the existing benchmarks, otherwise, highlighting the contributions that were not available to the community before this work. This also includes the fact that some of the techniques included in the benchmark were already available as source code, so the authors should clarify the implementation effort added to the existing tools.

Additional crucial weaknesses that should be addressed:
- limitations are not discussed
- the paper exceeds the page limit

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

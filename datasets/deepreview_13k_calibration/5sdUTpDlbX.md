# Professor X: Manipulating EEG BCI with Invisible and Robust Backdoor Attack

- Decision: Reject
- Avg Score: 5.20
- Scores: 1, 6, 8, 6, 5

## Abstract
While electroencephalogram (EEG) based brain-computer interface (BCI) has been widely used for medical diagnosis, health care, and device control, the safety of EEG BCI has long been neglected.
In this paper, we propose \textbf{Professor X}, an invisible and robust ``mind-controller" that can arbitrarily manipulate the outputs of EEG BCI through backdoor attack, to alert the EEG community of the potential hazard.
However, existing EEG attacks mainly focus on single-target class attacks, and they either require engaging the training stage of the target BCI, or fail to maintain high stealthiness.
Addressing these limitations, {Professor X} exploits a three-stage clean label poisoning attack: \textbf{1)} selecting one trigger for each class; \textbf{2)} learning optimal injecting EEG electrodes and frequencies strategy with reinforcement learning for each trigger; \textbf{3)} generating poisoned samples by injecting the corresponding trigger's frequencies into poisoned data for each class by linearly interpolating the spectral amplitude of both data according to previously learned strategies.
Experiments on datasets of three common EEG tasks
demonstrate the effectiveness and robustness of Professor X, which also easily bypasses existing backdoor defenses.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
From the outset, the abstract of the submission presents a proposition that appears to be unrealistic and somewhat disconnected from contemporary research realities. It remains inaccurate to assert that "While electroencephalogram (EEG) based brain-computer interfaces (BCIs) have been extensively employed in medical diagnosis, healthcare, and device control, the safety of EEG BCIs has long been neglected."

The manuscript constructs a fictitious framework, suggesting that research regarding BCIs has already translated into widespread applications. The submission relies on historical datasets such as BCIC-IV-2a. It is critical to note that motor imagery may not be effective for the target demographic of individuals with paralysis due to significant neural degeneration. Moreover, the methodology seems to rely on a dubious SEED database to fabricate artificial backdoor attack scenarios, ultimately suggesting solutions that are not based in rigorous academic research. This strategy does not promote the growth of academic inquiry, thus justifying a rejection of this submission.

### Strengths
The reviewer found no substantial strengths in the submission. It is fundamentally inadequate to fabricate problems only to propose solutions. Backdoor attacks do not present a significant concern in the field of BCI research at this time, as established paradigms are still lacking. Nonetheless, BCI research is experiencing significant growth due to advancements in machine learning; however, a considerable distance remains before it can transition to healthcare and broader applications that would necessitate the implementation of protections against backdoor attacks.

### Weaknesses
From the outset, the abstract of the submission presents a proposition that appears to be unrealistic and somewhat disconnected from contemporary research realities. It remains inaccurate to assert that "While electroencephalogram (EEG) based brain-computer interfaces (BCIs) have been extensively employed in medical diagnosis, healthcare, and device control, the safety of EEG BCIs has long been neglected." 

The manuscript constructs a fictitious framework, suggesting that research regarding BCIs has already translated into widespread applications. The submission relies on historical datasets such as BCIC-IV-2a. It is critical to note that motor imagery may not be effective for the target demographic of individuals with paralysis due to significant neural degeneration. Moreover, the methodology seems to rely on a dubious SEED database to fabricate artificial backdoor attack scenarios, ultimately suggesting solutions that are not based in rigorous academic research. This strategy does not promote the growth of academic inquiry, thus justifying a rejection of this submission.

### Questions
Why did the authors construct an entirely unrealistic and artificial scenario? Where did the authors encounter such hyperbolic or enthusiastic claims regarding the purported applications of BCI in healthcare and medical diagnostics? Currently, only a limited number of conditionally approved, mostly invasive devices have been tested on a small cohort of subjects within closed clinical studies.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Professor X, a novel, frequency-based EEG attack designed to be stealthy and multi-target. The method involves three main steps: 1) Finding triggers for each class, 2) using reinforcement learning to find optimal electrodes and frequencies injection
strategies, and 3) generating poisoned samples using triggers and clean data.

### Strengths
1. The study has a clear research question, which makes its purpose easy to understand.
3. The idea of employing reinforcement learning for finding the optimal electrodes and frequencies for data poisoning is interesting. 
2. The authors designed multiple experiments to evaluate different parts of their method, and the ones focused on showing the method's robustness are especially valuable.

### Weaknesses
As mentioned in the related works, a research direction exists that focuses on designing frequency-based backdoor attacks. Although existing methods are designed for images rather than time series, the authors could still compare their proposed method with existing approaches to better highlight the novelty of the work in relation to current frequency-based methods.

The authors designed several baselines (stealthy and non-stealthy) based on BadNets, PP-based BD attacks, and so on, which is great. However, it would be great if the authors considered and designed some baselines based on the existing frequency-based BD attack, if applicable.

The stealthiness of the method is one of the claims of the method. Although there are some visualizations in this regard, it would be great if the authors designed an experiment to validate the stealthiness of the method. It may be similar to a previous study [1], which used anomaly detection methods.

The author only considers three models for the classifiers: EEGNet, DeepCNN, and LSTM. However, it would be great if the author considered other new models, like TIMESNET [2] and other new transformer-based models.

The quality of the writing needs improvement; here are some points:
The third paragraph of the introduction requires revision for clarity and coherence. 
Figure 1 consists of five sub-figures that provide a good summary of the method. However, in the introduction (line 050), the authors begin by explaining Figure 1-d, which destroys the flow.

The Methodology section should be improved by first defining the key concepts, symbols, and problems. 
It would also be helpful to include a table of abbreviations and symbols, as the multiple terms used throughout the paper may be confusing for readers.

### Questions
In addition to the points in the 'Weaknesses' section, I'd like to add one more:

How effective is the proposed BD attack when applied to approaches that utilize frequency information of data, such as [3]?



[3] Zhang X, Zhao Z, Tsiligkaridis T, Zitnik M. Self-supervised contrastive pre-training for time series via time-frequency consistency. Advances in Neural Information Processing Systems. 2022 Dec 6;35:3988-4003.

### Soundness
2

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
4

### Summary
This paper presents "Professor X," a new EEG backdoor attack aimed at influencing the outputs of electroencephalogram (EEG)-based brain-computer interfaces (BCIs). While EEG BCIs are widely utilized in medical and device control settings, their security has often been neglected. Professor X improves upon existing EEG attack methods, which typically target single classes and either require interaction with the BCI's training phase or lack stealth. This innovative approach strategically selects specific EEG electrodes and frequencies for injection based on various EEG tasks and formats. By employing a reinforcement learning-based reward function, the method enhances both robustness and stealth. Experimental results demonstrate Professor X's effectiveness, resilience, and generalizability, underscoring vulnerabilities in EEG BCIs and calling for further defensive research in the field. Additionally, Professor X can help protect intellectual property within EEG datasets and BCI models by embedding a concealed watermark. The attack employs a three-stage clean label poisoning strategy: selecting triggers for each class, optimizing injection strategies for electrodes and frequencies, and generating poisoned samples via spectral interpolation. Testing on diverse EEG task datasets validates the method’s effectiveness and its capacity to circumvent existing defenses.

### Strengths
It presents an innovative approach for manipulating EEG BCI outputs, addressing a gap in the existing literature that predominantly emphasizes single-target attacks. The design leverages reinforcement learning to improve the attack's robustness and stealth, enabling it to evade detection more successfully than earlier methods. Professor X takes into account the specific EEG electrodes and frequency ranges associated with different tasks and formats, making it versatile for various EEG applications. Experimental results show that Professor X is effective across multiple EEG tasks, highlighting its broad applicability beyond just one context.

### Weaknesses
The method might encounter difficulties when scaling to larger or more intricate datasets, which could restrict its effectiveness in real-world applications with varied user populations. Specifically, the reliance on a reinforcement learning-based reward function, while beneficial for stealth and robustness, may become computationally expensive as the number of EEG channels and frequency bands increases. This could lead to a significant increase in training time and resource requirements, potentially limiting its applicability to high-density EEG systems or long-duration recordings. Furthermore, the current evaluation does not thoroughly explore the impact of inter-subject variability on the attack's success. While the authors mention cross-subject settings, a more detailed analysis of how the attack's effectiveness varies across different individuals, particularly those with diverse neurological profiles or signal characteristics, is needed. The method's reliance on spectral interpolation for generating poisoned samples could also introduce artifacts or inconsistencies that might be detectable with more sophisticated signal processing techniques.

### Questions
What potential research directions could be pursued to enhance defenses against backdoor attacks such as Professor X, especially regarding Fine-Pruning techniques?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces "Professor X," a novel EEG backdoor attack designed to manipulate the outputs of electroencephalogram (EEG)-based brain-computer interfaces (BCIs). While EEG BCIs are commonly used for medical and device control applications, their safety has often been overlooked. Professor X addresses the limitations of existing EEG attacks, which typically focus on single-target classes and require interaction with the training stage of the BCI or lack stealthiness. This method uniquely considers the specific EEG electrodes and frequencies to be injected based on different EEG tasks and formats. Utilizing a reinforcement learning-based reward function enhances both robustness and stealthiness. Experimental results demonstrate Professor X's effectiveness, robustness, and generalizability, highlighting the potential vulnerabilities in EEG BCIs and urging the community to conduct defensive studies. Additionally, Professor X offers applications in protecting intellectual property within EEG datasets and BCI models by providing a concealed watermark. The attack exploits a three-stage clean label poisoning strategy: selecting triggers for each class, optimizing electrode and frequency injection strategies, and generating poisoned samples through spectral interpolation. Tests on various EEG task datasets confirm the method's efficacy and its ability to bypass existing defenses.

### Strengths
It introduces a novel method for manipulating EEG BCI outputs, filling a gap in the existing literature that largely focuses on single-target attacks.
The design incorporates reinforcement learning to enhance the attack's robustness and stealthiness, allowing it to evade detection more effectively than previous methods.
Professor X considers the specific EEG electrodes and frequency ranges relevant to different tasks and formats, making it adaptable to various EEG applications.
Experimental results demonstrate that Professor X is effective across multiple EEG tasks, indicating a broad applicability beyond a single context.

### Weaknesses
The potential for malicious use raises significant ethical issues, as manipulating EEG outputs could lead to harmful consequences for users and their applications.

The method involves a sophisticated three-stage clean label poisoning attack, which may be complex to implement in practice, especially for those lacking expertise in reinforcement learning and EEG signal processing. The reliance on reinforcement learning for optimizing the attack strategy adds a layer of complexity that may hinder reproducibility and practical deployment. Furthermore, the specific reward function used in the reinforcement learning process is not thoroughly justified, raising questions about its optimality and potential biases.

The design's focus on particular EEG tasks might result in overfitting, reducing its effectiveness in more generalized scenarios or with novel tasks. The method's reliance on task-specific electrode and frequency selection could limit its adaptability to new EEG paradigms or datasets with different characteristics. It is unclear how the method would perform on tasks with significantly different spectral or spatial distributions.

The approach may face challenges in scaling up for larger or more complex datasets, potentially limiting its effectiveness in real-world applications involving diverse user populations. The computational cost of the reinforcement learning optimization, especially with larger datasets, is a concern. The method's performance may also degrade when applied to datasets with greater inter-subject variability or more complex noise profiles.

### Questions
What ethical frameworks are in place to govern the use of techniques like Professor X, and how can researchers ensure that such methods are not misused?

How effective is STRIP in detecting backdoor inputs under various levels of perturbation? Are there specific types of perturbations that significantly impact its performance?

How does STRIP compare to other defense mechanisms in terms of robustness against backdoor attacks like Professor X? What are its relative strengths and weaknesses?

 What specific mechanisms within the model lead to the observed drop in attack success rate (ASR) when Fine-Pruning is applied? Can these mechanisms be quantified?

How are low-activated neurons determined, and could this method inadvertently remove important features that are crucial for classification?

 How effective is Fine-Pruning at different pruning ratios beyond 0.7? Are there specific thresholds where the attack's effectiveness is significantly impacted?

What future research avenues could be explored to improve defenses against backdoor attacks like Professor X, particularly in the context of Fine-Pruning?

### Soundness
4

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
5

### Summary
This paper presents Professor X, a novel backdoor attack method specifically designed for EEG-based brain-computer interfaces (BCIs). The proposed approach employs a three-stage clean-label poisoning strategy that includes trigger selection, reinforcement learning to identify optimal injection techniques, and the generation of poisoned data in the frequency domain.

### Strengths
The introduction of a three-stage clean-label poisoning strategy represents an innovative approach to backdoor attacks in the context of EEG-based BCIs.

The use of reinforcement learning to optimize injection techniques enhances the potential effectiveness of the attack and contributes to the growing body of research on adversarial techniques in neurotechnology.

### Weaknesses
The literature review is notably limited, overlooking key studies such as Liu et al. (2021) and Zhang & Wu (2019), which highlight the vulnerabilities of EEG-based BCIs to adversarial attacks on signal integrity.

This oversight significantly diminishes the impact and originality of the research, as the proposed method lacks validation against established vulnerabilities within existing literature.

A more thorough engagement with relevant studies would enhance the study's contributions and contextual relevance.

### Questions
What motivated the specific design choices made in the three-stage clean-label poisoning strategy?

How does the proposed method compare in effectiveness to existing backdoor attack methods in the literature?

### Soundness
2

### Presentation
2

### Contribution
1

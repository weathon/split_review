# MedFuzz: Exploring the Robustness of Large Language Models in Medical Question Answering

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Large language models (LLM) have achieved impressive performance on medical question-answering benchmarks.
However, high benchmark accuracy does not imply that the performance generalizes to real-world clinical settings.
Medical question-answering benchmarks rely on assumptions consistent with quantifying LLM performance but that may not hold in the open world of the clinic.
Yet LLMs learn broad knowledge that can help the LLM generalize to practical conditions regardless of unrealistic assumptions in celebrated benchmarks.
We seek to quantify how well LLM medical question-answering benchmark performance generalizes when benchmark assumptions are violated.  Specifically, we present an adversarial method that we call MedFuzz (for medical fuzzing). 
MedFuzz attempts to modify benchmark questions in ways aimed at confounding the LLM.
We demonstrate the approach by targeting strong assumptions about patient characteristics presented in the MedQA benchmark.
Successful ``attacks" modify a benchmark item in ways that would be unlikely to fool a medical expert but nonetheless ``trick" the LLM into changing from a correct to an incorrect answer.
Further, we present a permutation test technique that can ensure a successful attack is statistically significant.
We show how to use performance on a ``MedFuzzed" benchmark, as well as individual successful attacks. The methods show promise at providing insights into the ability of an LLM to operate robustly in more realistic settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the robustness of large language models in handling medical QA tasks by introducing a new evaluation method, MedFuzz. For each multiple-choice question in the original benchmarks, MedFuzz uses an LLM (referred to as the attacker LLM) to reformulate questions by adding patient characteristics that may introduce social bias without affecting the clinical decision-making process. If the target LLM answers correctly, the attacker LLM is prompted to generate additional distracting questions based on the target LLM’s feedback. Additionally, a non-parametric statistical significance test was developed by prompting the attacker LLM to create questions with patient characteristics that avoid social bias. Using this evaluation method, the authors tested seven LLMs and found a significant performance drop across all models. Moreover, they observed that when current LLMs answer incorrectly, they tend not to reference the added biased information, indicating inconsistency in faithfully adhering to the clinical decision-making process.

### Strengths
+ This paper examines the robustness of LLMs in the clinical decision-making process, a critical aspect of their application in the medical domain.

+ The evaluation results demonstrate that current LLMs lack robustness in the clinical decision-making process, offering valuable insights for the development of medical LLMs.

### Weaknesses
 + A major weakness of this paper is the faithfulness of the reformulated questions. The proposed MedFuzz method relies solely on prompt engineering with the attacker LLM (GPT-4) to modify original MedQA questions, making the attack process difficult to control. The attacker LLM may potentially alter critical information in the original questions, resulting in less reliable reformulated questions. The example in Section 3.1 also demonstrates that the attacker LLM added extensive information about the patient’s family medical history, consultation history, and medication history. These details are highly relevant in real clinical diagnosis and can significantly influence a doctor’s assessment of the patient’s condition.

+ Moreover, although the authors propose a non-parametric statistical significance test, they do not provide the full distribution of p-values across the MedQA benchmark. In line 485, they note that for the successful attacks they selected, the p-values are <1/30, 0.1, 0.16, 0.5, and 0.63. Here, the p-value represents the probability that a control fuzz is more challenging than the original fuzz. Therefore, cases with p-values of 0.5 and 0.63 suggest that the performance decline in the target LLM is due to the perturbations themselves, rather than social bias.

+ For the study of target LLM's faithfulness, it is important to also study the proportion of CoT that mentions the critical information in the original MedQA benchmark for comparison with the results provided in Figure 2B. Additionally, the authors should provide more information to help readers understand the specific process of this study. For example, how many cases were analyzed? Was the determination of whether fuzzed information was included made manually, or was an automated algorithm used?

### Questions
1. The authors need to provide further experiments and analyses to demonstrate the reliability of the questions generated by this method, such as incorporating the performance of human experts or introducing relevant methods for quality control of the questions in the methods section.

2. Also, more analysis of the evaluation results should be included. For example, what are the main types of errors introduced by attacks across different turns? Which specific diseases or problem types is the target LLM less robust against? By supplementing these analyses, further insights can be provided for the development of medical LLMs.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes an automated red teaming approach to attack LLMs. They attempt this in the medical context by modifying medical Q&A datasets (specifically on MedQA), by violating assumptions that do not hold good in real life settings. The goal of MedFuzz is to make LLMs provide the wrong answer while ensuring that clinicians can still provide the right answer. The authors have identified a crucial problem with the evaluations of LLMs in the medical domain and provided a way to generate a more realistic dataset to aid subsequent LLM evaluation. The novelty lies in the proposed dataset from MedFuzz and the statistical evaluation used to check if the attack was successful.

### Strengths
•	Clarity: The paper is well written and easy to follow along. The authors have given adequate and clear examples at appropriate locations in the draft to aid readability. Good use of illustrations after consultation with domain experts (clinical collaborators in this case). The authors have also acknowledged the limitation of using contaminated training data.

•	Originality: The idea to use social biases a clever way to incorporate real life information into the MedQA dataset.

•	Quality: The evaluation involves the use of proprietary vs open source and general purpose vs domain specific models. The experiment settings for reproducibility like temperature have been provided. The approach should be easy enough to reproduce. 

•	Significance: The authors have tackled a relevant problem that needs to be addressed, given the rapid pace of the domain.

### Weaknesses
•	In the case of MedQA dataset, the authors have identified a social bias which may be present in real life situations, which are removed in the original benchmark. It is unclear how easy it is to identify and exploit such peculiarities in other medical benchmarking datasets like MedMCQA[1], PubMedQA[2] etc.

•	The authors create the adversarial questions by an iterative multi-turn approach. Although the authors allude to the target LLM forgetting about previous Q&A attempts, would the approach be better validated if the evaluation is done in a single-turn manner? The iterative approach, while potentially effective, introduces a confounding variable: the model's memory of previous interactions. This makes it difficult to isolate the impact of the adversarial input itself, as opposed to the cumulative effect of the multi-turn conversation.

•	The authors, in step 4, only validate the statistical significance of 4 individual interesting cases. How would this change if considered for all successful cases? This raises concerns about the generalizability of the findings. Focusing on only a few cases might lead to cherry-picking results that support the authors' hypothesis, while overlooking cases where the attack is not as effective or where the statistical significance is not as strong. A more comprehensive analysis across all successful adversarial examples is needed to ensure the robustness of the conclusions.

### Questions
•	The authors can clarify how their approach to adversarial attacks differs from the misinformation approach in [1].

•	The authors can clarify why unfaithfulness of generated responses is a crucial dimension to consider.

•	Section 2.2 Lines 104: The authors mention “two ways” in which MedFuzz differs from other adversarial ML approaches, though only one distinction is clear in the draft. I’m assuming the second way is the use of semantically coherent changes to the text. These few lines can probably be rephrased to add clarity.

•	The authors have conducted their experiments on the MedQA dataset and taken advantage of a constraint imposed in the curation of this dataset. The authors could potentially add broad guidelines to expand on the fuzzing idea for other medical datasets. 

•	How can the authors ensure that the GPT-4 generated attack retains the same answer as the original QA pair being perturbed? Is there a possibility to evaluate this with the help of domain experts?

•	How is the value of K set in Algorithm 1? This can be elaborated on in the Appendix section.

•	Does the finding that LLM CoT does not mention the fuzzed information provide a way forward to identify adversarial inputs?

•	Another interesting avenue would be to examine how different kinds of LLMs perform when used as the attacking/ target LLM. For example, can a smaller model generate adversarial inputs faster than a larger model like GPT-4?

•	Minor Comment: Is line 10 a duplicate of line 11 in Algorithm 1?

[1] Han T, Nebelung S, Khader F, Wang T, Müller-Franzes G, Kuhl C, Försch S, Kleesiek J, Haarburger C, Bressem KK, Kather JN. Medical large language models are susceptible to targeted misinformation attacks. npj Digital Medicine. 2024 Oct 23;7(1):288.

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
4

### Summary
The paper proposes an adversarial method for evaluating LLM performance on medical question-answering benchmarks to assess their robustness in real-world clinical settings. The idea is to automatically generate new question-answer pairs from the existing benchmark such that they still represent realistic scenarios (e.g., including additional patient information) but the answers remain the same. The experiment results demonstrate that various baseline LLMs can be tricked into providing incorrect answers.

### Strengths
* The idea of the paper is interesting -- existing medical QA datasets are fairly simplified and may not appropriately represent real-world clinical settings. Thus, there is a need to understand how safe LLM usage is for the medical domain via robustness analysis.
* The intuition for the adversarial biasing comes from medical domain understanding of the benchmark constructions.
* Authors benchmark 3 closed LLMS and 4 open-source, medically fine-tuned LLMs.

### Weaknesses
 * One of the major claims of the method is that it will generate new questions that are semantically coherent and will not fool clinicians. However, there is no empirical proof that this is the case other than the analysis of a handful of case studies (one is presented in the main text). The prompt contains instructions for the attacker LLM it should not change the default answer but GPT-4 is not always guarenteed to follow the instructions or have all the correct medical knowledge appropriate.
* Is there a reason why general domain adversarial prompting wasn't shown to be sufficient? A few studies are listed in 2.2 (first sentence) but no preliminary studies or experimental studies are shown to support this.
* GPT-4 is chosen as the attacker LLM, but the question is why aren't other open-source models explored? In looking at OpenBIOLLM-70B performance, this also looks like a reasonable comparison to try and might even generate harder cases with less of the computation cost.
* One of the comments in the introduction was the that existing benchmarks are not challenging enough including reducing real-life clinical situations to canonical multiple choice questions. Is there a reason why only one dataset was included and it was a multiple-choice one?
* The statistical test is proposed to identify the significance of a successful attack using control fuzzes and to select the case studies, but what about the general distribution for the MedQA dataset? How stable is it broadly in identifying how significant a successful attack is? I understand this can be computationally intensive and costly but that also raises a bit of questions regarding the applicability of the method if it can't be done at scale. 
* The presentation could have been improved to provide some intuition at the beginning with potentially a simpler case study where less was added to make the LLM response change. Similarly, some of the text is written in a less digestible format. For example, the introduction of the test statistic could be improved by introducing notation first and then how you might compute it to understand what the statistic is looking to capture.
* The citation format is incorrect, please use \citep instead of \cite as it detracts from readability.

### Questions
* Why was MedQA the only dataset used? There are a few other multiple choice medical QA ones liked MedMCQA, PubMedQA, and MMLU Clinical topics. Why MedQA?
* Why was only GPT-4 used as the attacker LLM? Seemingly there are other open source ones that have just as much medical knowledge especially looking at the fine-tuned example. 
* The workflow for the Step 2 is quite a few iterative turns. Are they all necessary to generate grounded ones? Is this workflow generalizable to other LLMs? Or is it GPT-4 specific?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes MedFuzz, a novel approach designed to evaluate the robustness of large language models (LLMs) in medical question-answering contexts. MedFuzz introduces controlled perturbations in input text by adding patient characteristics (PC) and social bias information to simulate real-world variability and challenges encountered in clinical settings.

The authors highlight the limitations of traditional medical benchmarks that often simplify clinical scenarios and position MedFuzz as an advancement towards “beyond-the-benchmark” evaluations. Specifically, the paper presents experiments assessing LLMs' responses to MedFuzz perturbations and evaluates the consistency of chain-of-thought (CoT) explanations under these conditions. The study offers a new perspective on testing LLM robustness by addressing potential risks in clinical decision-making when assumptions of canonical benchmarks do not hold.

### Strengths
1. This paper introduces MedFuzz, a novel approach for testing the robustness of large language models (LLMs) in clinical contexts, which addresses the simplifications found in traditional benchmarks. MedFuzz is distinct in its approach by adding specific patient characteristics and social bias information to simulate the complexity of real-world clinical scenarios. This innovative framework offers a new direction for assessing LLM robustness by examining potential vulnerabilities in medical question-answering settings.

2. The paper clearly explains the concept of MedFuzz and its application, particularly in using patient characteristics and bias elements to test model robustness. The experimental procedures and components are consistently described, making the study's objectives and methodology easy for readers to follow.

3. MedFuzz presents a significant contribution as it provides a framework to evaluate how LLMs may perform in real clinical settings, beyond simplified benchmarks. This work has high practical relevance for the safe implementation of LLMs in healthcare by strengthening robustness assessment and reducing potential errors. It contributes an essential tool for enhancing LLM applicability in clinical practice, highlighting the importance of robustness in medical AI.

### Weaknesses
1. The authors clarified the distinction between robustness and generalization in their response, emphasizing that robustness in this study is tied to resilience against violations of benchmark assumptions. This clarification addresses the original concern, though ensuring this explanation is explicitly included in the revised manuscript remains important.
2. The authors clarified that MedFuzz is designed to surface biases already present in the target model and does not introduce confusion into clinical decision-making itself. While this explanation addresses the primary concern, ensuring that the revised manuscript provides sufficient justification for the use of specific patient characteristics as perturbations will remain critical. Specifically, the choice of patient characteristics (e.g., age, gender, race, socioeconomic status) as perturbations needs more rigorous justification. These characteristics are often crucial for clinical decision-making, and their use as 'confusion factors' requires a more detailed explanation of how they are intended to reveal vulnerabilities without introducing spurious correlations or biases.
3. The authors acknowledged that the scale of perturbations could be further refined and suggested this as future work. Including a brief discussion in the revised manuscript about the implications of perturbation scale would strengthen this point. The current approach lacks a systematic exploration of how the magnitude of added patient characteristics and social bias information affects the model's performance. A more detailed analysis of different perturbation scales, including both the amount of added text and the intensity of bias introduced, would be beneficial.
4. The authors agreed to expand the analysis of CoT fidelity to include unsuccessful attacks in addition to successful ones. This addition should provide a more comprehensive baseline for evaluating the vulnerabilities identified by MedFuzz. Ensuring this analysis is effectively implemented in the revised manuscript will be crucial.

### Questions
1. It would be helpful to have specific examples illustrating the risks posed by the simplified assumptions in traditional benchmarks within clinical settings. For instance, if omitting certain patient characteristics or clinical contexts could lead to diagnostic errors, providing these examples would clarify the importance of this study for readers and highlight its relevance.

2. I am curious whether the patient characteristics (e.g., age, gender) and social bias information added as perturbations in MedFuzz genuinely act as confusion factors within actual clinical environments. These details often serve as crucial data points in clinical decision-making, so further explanation on how these elements were deemed appropriate as confusion-inducing factors would enhance the clinical validity of this study.

3. A clear explanation regarding the rationale for setting the perturbation iteration count to K=5 would be beneficial. For instance, do you have experimental results comparing the initial attack (K=1) with subsequent attacks (K=5) to illustrate how the LLM maintains performance with increasing perturbation levels? Such a comparison could provide a more reliable basis for evaluating the impact of iteration count on robustness in this study.

### Soundness
3

### Presentation
3

### Contribution
4

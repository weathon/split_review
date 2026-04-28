# Humanizing the Machine: Proxy Attacks to Mislead LLM Detectors

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 8, 5, 6

## Abstract
The advent of large language models (LLMs) has revolutionized the field of text generation, producing outputs that closely mimic human-like writing. Although academic and industrial institutions have developed detectors to prevent the malicious usage of LLM-generated texts, other research has doubt about the robustness of these systems. To stress test these detectors, we introduce a \textbf{hum}anized \textbf{p}roxy-\textbf{a}ttack (HUMPA) strategy that effortlessly compromises LLMs, causing them to produce outputs that align with human-written text and mislead detection systems. Our method attacks the source model by leveraging a reinforcement learning (RL) fine-tuned humanized small language model (SLM) in the decoding phase. Through an in-depth analysis, we demonstrate that our attack strategy is capable of generating responses that are indistinguishable to detectors, preventing them from differentiating between machine-generated and human-written text.
We conduct systematic evaluations on extensive datasets using proxy-attacked open-source models, including Llama2-13B, Llama3-70B, and Mixtral-8$\times$7B in both white- and black-box settings. Our findings show that the proxy-attack strategy effectively deceives the leading detectors, resulting in an average AUROC drop of 70.4\% across multiple datasets, with a maximum drop of 90.3\% on a single dataset. Furthermore, in cross-discipline scenarios, our strategy also bypasses these detectors, leading to a significant relative decrease of up to 90.9\%, while in cross-language scenario, the drop reaches 91.3\%. Despite our proxy-attack strategy successfully bypassing the detectors with such significant relative drops, we find that the generation quality of the attacked models remains preserved, even within a modest utility budget, when compared to the text produced by the original, unattacked source model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The article explores a strategy known as the Human-like Proxy Attack (HUMPA), aimed at evading detection by large language model (LLM) detectors. This approach uses a small language model (SLM) fine-tuned through reinforcement learning to alter the output of the LLM, making the machine-generated text indistinguishable from human-written content. Evaluations using various open-source models and datasets indicate a significant decrease in detector accuracy, while preserving the quality of the text.

### Strengths
- Utilizing fine-tuned, human-like small language models to modify the distribution of source models, making them resemble human-written text, is a well-conceived attack strategy. This serves as an effective stress test to drive the advancement of current detectors.
- The proposed method efficiently lowers the cost of fine-tuned model attacks. Additionally, despite the attack, the text quality remains high, which is essential for practical applications.

### Weaknesses
 - The experimental setup lacks latest strong baselines, such as the more robust detector "binoculars [1]". (This detector is easy to replicate and very fast.)
- The authors are commended for their results in cross-domain scenarios. However, cross-model detection evasion deserves more focus, as disciplines and languages remain constant, while LLMs continue to evolve. Specifically, the paper does not explore the scenario where the source LLM and the small language model (SLM) used for the Human-like Proxy Attack (HUMPA) come from different model families, which could reveal further vulnerabilities.
- The method proposed in the paper uses reinforcement learning to align the probability distribution of small models with human patterns, achieving human-like output. It's important to note that this approach appears similar to DALD [2], with the main difference being DALD's use of further training, while HUMPA employs reinforcement learning. The paper needs to clarify the novelty of its approach compared to DALD, particularly regarding the specific mechanisms by which HUMPA achieves its results, and how these differ fundamentally from DALD's methodology.
- Formatting Issues
    - The citation format for Yang et al. (2023b) is incorrect on lines 365, 367, 369, and 370. The author should thoroughly review and correct the citation format throughout the paper.

### Questions
- Has the author considered potential safeguards to prevent the misuse of the proposed attack strategies?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Machine-generated texts can bring misinformation and misconduct. Therefore, several methods are developed to detect them. This paper conducts research on the robustness of these methods and propose an evasion method called HUMPA to generate texts that reads fluent and natural but can evade SOTA AI-generated text detectors. The key idea is to use a human-written dataset and use direct preference optimization and solve it via direct preference optimization. However, as DPO can only be effortlessly applied to small models, this paper resorts to proxy-tuning, which first tunes a relatively smaller model using DPO, and then use this model to manipulate the output distirbution of the larger model and achieve the same preferece tuning goal. The method is validated on a bunch of state-of-the-art detectors in both black-box and white-box scenarios, demonstrating its effectiveness in lowering detection accuracy while ensuring fluency and naturalness of the generated texts.

### Strengths
- The problem studied is highly relevant and very important.
- The paper is generally clearly-written and easy to follow.
- The method seems sound and the experiments are conducted on a wide range of methods.
- The idea to view AI-generated text detection as a preference optimization problem and solving it using DPO and proxy-tuning is intuitive and reasonable.

### Weaknesses
 - The novelty of this paper on the technical side might be limited. The general idea of first tune a smaller model and then manipulate the sampling process of the larger model has been widely applied in previous works, such as Proxy-tuning [1], EFT [2], and DeRa [3] (not cited). The papers method is generally a combination of DeRa, EFT and Proxy-tuning. The main innovation of this paper is its application to the problem of evading machine-generated text detection. However, this cannot fully support the method's novelty.

- The improvement of the method over previous works seems marginal. This paper does not compare with previous methods on evading machine-generated text detection, the only comparison is on the fluency part rather than effectiveness. According to the experimental results, the effectiveness of the proposed method is unstable. For example, in table 1-white-box, Likelihood, DetectGPT and Fast-DetectGPT's performances are only slightly degraded. This raises doubts on how the proposed method really advanced the field.

- The provided theorems do not seem to be closely connected with the proposed method. For example, thoerem 1 just proves the existence of the optimal $\beta$, and this theorem seems applicable to a wide range of tasks that uses DPO. Yet, it is unclear how significant it is to the evasion of AI-generated text detection and how this can be achieved through proxy-tuning.


Minor:
- Figure 1 caption, "After the attack, the distribution aligns more closely with that of human-written text" has been repeated for twice.
- Citation formats in Section 4.1 are mostly wrong. Please correct them.

### Questions
- DPO requires paired datasets. How do you collect the human-written text dataset for DPO for unseen tasks or topics that do not have a pool of human-written texts?

### Soundness
3

### Presentation
3

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
This paper presents a new attack to evade the MGT detectors by training a proxy to generate humanized text. The idea is to train a lightweight student model to screw the generation towards "human" through reinforcement learning by assigning "humanity" with higher rewards. The paper analyzes the theoretical guarantee of the proxy's attack effectiveness and generation quality. By evaluating several datasets, the paper shows the effectiveness and even some generalizability across languages and domains.

### Strengths
1. The paper is very nicely written and presented. The logic is clear, and the figures are beautiful. The problem is nicely defined, and the methodology is clearly explained.
2. The paper shows the potential of using lightweight methods to bypass MGT detection. 
3. The code is open-sourced.
4. In practical experiments, the paper shows the effectiveness of the attack, especially with little harm to model utility, which is amazing.

### Weaknesses
 1. My main concern is that the theoretical guarantees in the paper (specifically Theorems 3.1 and 3.2) may be misleading, potentially overclaiming what they actually achieve. The logic behind these theorems is pretty simple: the training objective aims to balance two things—making the student model mimic humans (for attack effectiveness) and making it mimic the teacher LLM (for quality). By adjusting β from 0 to +∞, the student LLM could theoretically be optimized (optimally) to behave either purely human-like or purely as a replica of the teacher model, given “reasonable” training data. However, there are several issues with this claim: Firstly, as mentioned in the paper, the detector will overfit to what it was exposed to, which is unlikely to represent perfectly and, more importantly, calibrate accurately to the human distribution. And, because the proposed method relies on the detector rather than true human distribution, there seems to be no way to get the lambda mentioned. In other words, the approach would only work under ideal optimization, an ideal detector (a perfectly calibrated one), and an ideal training dataset. This explains why the paper uses Fast-DetectGPT as the scoring detector in all white-box settings, why black-box settings show better attack performance (NEO might be stronger with better calibration), and why the student models selected are from the same family as the teacher. Secondly, Theorem 3.2 essentially shows that the student model is just a less optimized (in terms of utility) version of the teacher, which doesn’t necessarily make it "good quality".
2. Given the constraints on both the detector and the training data, the attack is very likely to be limited in scope. While the paper presents some interesting results suggesting generalizability, we should expect that it won’t extend broadly in practice. See 1.
3. The paper uses models that are very close in architecture and scale (e.g., Llama2-13B vs. Llama2-7B). It’s unclear whether a smaller model from a different family could yield similar attack results. See 1.
4. The paper relies on Fast-DetectGPT for scoring in every white-box experiment, which doesn’t seem appropriate or fully aligned with the paper’s methodology. I wonder if these attacks would still perform well using only the target detector or less well-calibrated detectors. See 1.
5. Many of the white-box attacks have low performance. See 1.
6. The paper does not compare with any other SOTA attacks.
7. Although it is cool to use a small model to improve efficiency, the paper doesn’t provide any assessment of this efficiency, particularly in comparison to tuning the source LLM with DPO.

### Questions
1. What if the detector's score does not accurately reflect the degree of "human"? Since this is an attack paper, it is expected that there are different kinds of victims. What if the detector does not give higher rewards to more human text? 
2. What if the source LLM generated nearly equivalently "human" text with similar rewards? For the proposed attacks, is there any requirements on the scale of the reward difference? In other words, how different should the training sample be in terms of rewards?
3. Why are white-box attacks even worse?
4. How efficient is the attack compared with tuning source LLMs with DPO?
5. Can we use smaller models with different architecture to attack?
6. What if we stick to the same model, i.e., to use the scoring of LRR to attack LRR?
7. Is there any transferability across detectors? For example, can we use the scoring from LRR to attack DetectGPT or Fast-DetectGPT?
8. Can we apply such attacks in truly black-box settings, e.g., GPTZero or CopyLeaks?

Specifically, could you please:
1. Clarify the assumptions underlying Theorems 3.1 and 3.2, particularly regarding detector calibration and training data representativeness.
2. Discuss the practical implications of these assumptions not being fully met in real-world scenarios.
3. Provide additional empirical evidence or analysis to support the theoretical claims, especially regarding quality preservation in Theorem 3.2.
4. Discuss potential limitations on the generalizability of their approach more explicitly.
5. Suggest or conduct additional experiments that could test the boundaries of the attack's effectiveness across a wider range of scenarios or detectors.
6. Conduct experiments using smaller models from different architectural families as the proxy attacker.
7. Discuss the potential impact of model architecture and size differences on the attack's effectiveness.
8. Perform additional experiments using different detectors for scoring in the white-box setting.
9. Analyze and discuss how the choice of scoring detector impacts the attack's performance.
10. Include comparisons with other state-of-the-art attack methods on the same datasets and detectors.
11. Discuss the relative strengths and weaknesses of their approach compared to existing methods.
12. Provide quantitative comparisons of computational efficiency between their method and direct fine-tuning of the source LLM.
13. Discuss the trade-offs between efficiency gains and potential performance differences.

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
This paper aims to develop an attack against LLM detectors. The authors present a method called HUMPA (humanized proxy attack) that uses a smaller language model to subtly alter the output of a large language model (LLM) in a way that makes it harder for detectors to identify as AI-generated. In particular, the work adopts conventional Preference-based reinforcement learning, using the LLM detectors as a reward model, to train an SLM and adds the SLM token prediction onto the original LLM toke predictions. The paper provides some theoretical analyses as well as experimental results. However, the method is not novel, and the experiments lack baseline comparisons.

### Strengths
- Leveraging SLM to reduce costs is a good idea
- The format is correct, and the images are clear
- Attacks and defenses for LLM-produced texts are important research directions.

### Weaknesses
 - **No baselines**: the work only compares the result between the original LLM and the original LLM with the proposed HUMPA added on top. As shown in the Detection Evasion Methods in the Related Works section, many baselines should be compared. Specifically, the paper lacks comparison against paraphrasing methods, which are a common approach to evade detection, and also lacks comparison against fine-tuning the source model directly, which is a strong baseline.
- Unclear method and problem setting: there are many questions because the method and setting are not clearly explained.
    - attacker capability: does the attacker know the target LLM detector? Can the attacker query the target detector?
> It is worth noting that under adversarial attack conventions, black-box denotes query access while white-box denotes access to internal weights and gradients. In this work, the authors seem to denote the white box (detector) as the detector's access to LLM logits, while the black box indicates no access to logits and directly detects based on the final produced text (However, it is not clearly explained in the paper). Here, the reviewer wants to ask for the attacker's access to the detector.
    - Is the HUMPA method required to know which detector it faces beforehand? (also see the first question)?
> The work seems to use the target LLM detection directly as the reward model for each attack. Specifically, no cross-detector experiment setting was provided. Reviewing the code, the DPO_MixBuilder class also conditions based on the target detector. Thus, it seems that generalizability is an issue. Can a HUMPA method leveraging a target LLM detector be applied to a different type of LLM detector?
    - The target LLM task required for HUMPA to work. Can HUMPA generalize to different text generation tasks?
    - What is the threshold for evading LLM detection? Line 453 claims that HUMPA successfully evaded all detection methods across all source models. However, in Table 2 many detection scores are higher than 0.5.
- Poor writing, many typos or errors e.g. (not exhaustive):
    - Line 95 extra space
   -  Line 375 Then',' based on the samples,

### Questions
- (please see weaknesses)
- What methodological improvement does this work offer over previous approaches to evading LLM detection?
- While fine-tuning SLM is faster than LLM, Low-Rank Adaptation can be even faster. Why is LORA not considered?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces HUMPA (HUManized Proxy Attack), a novel strategy to evade detection of LLM-generated texts. The key idea is to use a small language model (SLM) fine-tuned with reinforcement learning in the decoding phase to contaminate the outputs of larger source models like Llama2-13B, Llama3-70B, and Mixtral-8x7B. The authors demonstrate that this approach can effectively deceive state-of-the-art detectors in both white-box and black-box settings, achieving significant drops in detection performance (up to 90% relative decrease in AUROC) while preserving generation quality. They also show the method's effectiveness in cross-domain and cross-language scenarios.

### Strengths
- The proposed HUMPA method is practical, addressing limitations of directly fine-tuning large models for evasion.
- This paper provides extensive theoretical analysis.
- Comprehensive experiments are conducted across multiple datasets, models, and detection methods, demonstrating the effectiveness of the attack.

### Weaknesses
 - The HUMPA method itself is too straightforward and lacks novelty. Many previous works [1, 2] in other fields share similar ideas. 
- Experiment metrics are not explained and hard to follow. Meanwhile, since the main purpose of applying SLM is to reduce time efficiency, you should also provide the time cost comparison between fine-tuning SLM and original LLM.

### Questions
- How sensitive is the HUMPA method to the choice of SLM used as the proxy attacker? Would using even smaller models such as Phi-3.5-mini-instruct still be effective?
- How does the computational cost of HUMPA compare to directly fine-tuning the source model, especially for the largest models tested?

### Soundness
3

### Presentation
3

### Contribution
2

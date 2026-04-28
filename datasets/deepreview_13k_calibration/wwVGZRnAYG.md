# BlueSuffix: Reinforced Blue Teaming for Vision-Language Models Against Jailbreak Attacks

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Despite their superb multimodal capabilities, Vision-Language Models (VLMs) have been shown to be vulnerable to jailbreak attacks, which are inference-time attacks that induce the model to output harmful responses with tricky prompts. It is thus essential to defend VLMs against potential jailbreaks for their trustworthy deployment in real-world applications. 
In this work, we focus on black-box defense for VLMs against jailbreak attacks.
Existing black-box defense methods are either unimodal or bimodal. Unimodal methods enhance either the vision or language module of the VLM, while bimodal methods robustify the model through text-image representation realignment. 
However, these methods suffer from two limitations: 
1) they fail to fully exploit the cross-modal information, or 2) they degrade the model performance on benign inputs.
To address these limitations, we propose a novel blue-team method \textsf{BlueSuffix} that defends the black-box target VLM against jailbreak attacks without compromising its performance. \textsf{BlueSuffix} includes three key components: 1) a visual purifier against jailbreak images, 2) a textual purifier against jailbreak texts, and 3) a blue-team suffix generator fine-tuned via reinforcement learning for enhancing cross-modal robustness. We empirically show on three VLMs (LLaVA, MiniGPT-4, and Gemini) and two safety benchmarks (MM-SafetyBench and RedTeam-2K) that \textsf{BlueSuffix} outperforms the baseline defenses by a significant margin. 
Our \textsf{BlueSuffix} opens up a promising direction for defending VLMs against jailbreak attacks.
\blfootnote{$^{\dagger}$ Correspondence to Xingjun Ma: \texttt{<xingjunma@fudan.edu.cn>}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a defense method for jailbreak attacks on VLMs to protect VLMs from black-box jailbreak attacks. Specifically, the method utilizes a multimodal purifier and reinforcement learning-based text tuning suffixes to enhance the robustness of VLMs.

### Strengths
1. The authors analyze the limitations of existing VLM denial defenses from two perspectives: lack of cross-modal information and decreased performance on benign inputs.
2. The proposed method has been validated on both open-source and commercial models, and is easy to implement and deploy.

### Weaknesses
1. Insufficient motivation for cross-modal information. The authors emphasize the series of problems caused by insufficient utilization of cross-modal information, but there is no detailed analysis or empirical evidence to prove this flaw. Therefore, the design of the Blue Team suffix generator, based on the above motivation, also lacks direct validation. Could the authors explain what specific manifestations are limited by the lack of cross-modal information and how this generator can alleviate the issue?
2. Limited experimental effects on clean samples. The method proposed by the authors, which is discussed in lines 445-451 of the paper, can improve the performance of benign inputs. However, the improvement is limited and does not surpass that of DiffPure. Therefore, I believe the claim about improving the performance of benign inputs is not effective.
3. Unclear technical contributions. The multimodal purifier proposed by the authors is more about a simple application of image purification technology and GPT-4o, and cannot be considered a significant technical contribution. The authors should elaborate more on the features of the proposed method and its relevance to overcoming limitations.
4. Insufficient ablation analysis. The authors proposed three modules, each designed to address different limitations, but simply stacking these modules and discussing performance changes does not constitute effective validation of the solution. The authors should conduct more detailed assessments of each component of the proposed method.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on black-box defense for VLMs against jailbreak attacks. This paper proposes the BlueSuffix method to defend against jailbreak attacks. BlueSuffix consists of three main components: 1) a visual purifier against jailbreak images, 2) a textual purifier against jailbreak texts, and 3) a blue team suffix generator fine-tuned via reinforcement learning to improve cross-modal robustness. BlueSuffix adopts a black-box defense model where the defender does not have access to the internal structures nor parameters of the target VLM. BlueSuffix ultimately succeeds in assisting the target VLM to automatically identify the malicious query within the inputs and generate a positive response accordingly, rather than acting as a malicious query detector.

### Strengths
* The paper is very well written and organized. The main points are well explained and easy to follow. The use of cleaners and generators is very interesting.
* The method shows a large reduction in the ASR of VLMs on two datasets. Moreover, the transferability analysis in this method also shows strong transferability across different targets.

### Weaknesses
 * The paper claims that it can enable the target VLM to identify harmful content without altering the original meaning, although the prompt used for the text purifier instructs the LLM not to alter the original meaning, but no relevant statistics support this claim. See question 1 for more details.
* This paper used GPT-4o as the judge for harmful response, the author should present the system prompt used for the GPT-4o.
* The result in Table 4 for Gemini is strange, why DiffPure + Safety Prompt will increase the ASR compared to each method by itself, please see question 3 for more details.
* The prompts in the top three rows of Figure 4 do not appear sufficiently harmful, and the rationale for their selection needs further clarification.
* The paper lacks evaluation on a diverse range of jailbreak methods specifically designed for VLMs, limiting the generalizability of the findings.

### Questions
1. Could the author provide some additional experiments to show that the text cleaner and the suffix do not change the original meaning of the instructions?
2. Could the author show the detailed system prompt used for the GPT-4o?
3. Could the author explain why the DiffPure + Safety Prompt method increases ASR? Some sample answers from Gemini may help to explain.
4. Could the author provide more explanation for Figure 4? For the top 3 rows, the prompts do not seem harmful enough.
5. Could the author show the result of some other jailbreak method specified for VLM other than BAP attack?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on defending Vision-Language Models (VLMs) against jailbreak attacks. It proposes BlueSuffix, a novel blue-team method with three key components: a diffusion-based image purifier, an LLM-based text purifier, and an LLM-based blue-team suffix generator. The method is trained via reinforcement learning to optimize the safety score of the target VLM. Experiments on three VLMs and two safety benchmarks show that BlueSuffix outperforms baseline defenses, achieving significant reductions in Attack Success Rate (ASR). It also has high transferability and is robust against an adaptive attack. The contributions include introducing BlueSuffix, proposing a cross-modal optimization method, and demonstrating the effectiveness and transferability of the defense.

### Strengths
The paper presents an approach to defending Vision-Language Models (VLMs) against jailbreak attacks, but the originality of the BlueSuffix method is somewhat limited. While it combines existing techniques, such as a diffusion-based image purifier and an LLM-based text purifier, the contributions do not significantly advance the current state of the art in VLM security. The method’s reliance on established concepts may not provide the innovative leap needed to warrant acceptance.

Although the research includes an experimental setup involving multiple VLMs and benchmark datasets, the execution lacks depth. The comparisons with baseline defenses like DiffPure and Safety Prompt are present, but the results do not convincingly demonstrate the effectiveness of BlueSuffix. Furthermore, the ablation studies, while included, do not provide sufficient insights into the importance of each component, leaving questions about the overall robustness and applicability of the proposed method.

### Weaknesses
1.The suffix generator used by the blue team demonstrates effectiveness in certain scenarios; however, its adaptability to a broad range of jailbreak prompts appears limited. Currently, it is primarily trained on specific hard jailbreak prompts related to "financial advice." This focus may hinder its performance when faced with diverse topics or novel prompt structures, particularly if attackers employ innovative semantic or syntactic patterns that the generator is not equipped to handle.

2.The diffusion-based image purifier may struggle to completely eliminate all forms of adversarial perturbations. Some sophisticated adversarial attacks can introduce subtle perturbations that are challenging to detect and remove using the existing diffusion process. This limitation raises concerns about the potential for residual malicious information in the purified images, which could inadvertently provoke harmful responses from the VLM.

3.The evaluation of the proposed defense primarily concentrates on only two types of attacks—vanilla and BAP attacks. This narrow focus may not adequately reflect the variety of real-world jailbreak attacks. Without testing against a broader spectrum of attack strategies, the effectiveness of the defense in more complex scenarios remains uncertain.

4.Although the paper outlines the three components of BlueSuffix, it falls short in analyzing their interactions and how they may enhance one another. Exploring potential synergies could lead to significant improvements in both resource utilization and defense effectiveness, thereby optimizing the overall system performance.

5.There is room for further optimization in the reinforcement learning process aimed at fine-tuning the suffix generator. The current objective function and training methodology might not yield the most effective suffixes. A more systematic exploration of the reference policy and the hyperparameter β could enhance the generator's performance and stability.
6.The discussion surrounding baseline defenses, specifically DiffPure and Safety Prompt, lacks sufficient detail. A clearer explanation of the specific techniques and algorithms employed in these baselines would help readers better understand the distinctions between the proposed method and existing defenses.

7.When analyzing performance across different VLMs such as LLaVA, MiniGPT-4, and Gemini, the paper could benefit from a deeper examination of how each VLM's characteristics influence the defense method's effectiveness. Such insights would aid in assessing the applicability and limitations of the proposed defense across various VLM architectures.

### Questions
No further questions. I've included all my questions within the **Weakness** section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses jailbreak vulnerabilities in Vision-Language Models (VLMs) by proposing BlueSuffix, a novel black-box defense method that combines visual purification, textual purification, and a reinforcement learning-trained suffix generator. Unlike existing unimodal and bimodal defense approaches, BlueSuffix effectively leverages cross-modal information while maintaining model performance on benign inputs. The method's effectiveness is demonstrated through extensive empirical validation across multiple VLMs (LLaVA, MiniGPT-4, and Gemini) and safety benchmarks (MM-SafetyBench and RedTeam-2K), showing significant improvements over baseline defenses and strong transferability across different models, even under adaptive attack scenarios. This comprehensive approach suggests a practical path forward for deploying robust VLMs in real-world applications.

### Strengths
1. The paper presents a well-structured and clearly articulated methodology for VLM defense.
2. The proposed black-box method demonstrates practical value with its low-cost implementation and easy deployment.
3. The experimental design is comprehensive, covering both open-source and commercial VLMs.

### Weaknesses
1. The claim regarding semantic preservation in blue-team suffix generation requires more rigorous validation. The provided examples suggest potential semantic drift between original and processed prompts.

2. The model selection scope could be expanded. Notable omissions include InstructBLIP and other widely-used VLMs, which would strengthen the generalizability claims.

3. The evaluation methodology relies heavily on GPT-4 judgements. Including additional evaluation tools (e.g., Perspective API) would provide more comprehensive safety assessments.

### Questions
1. Could the authors provide quantitative metrics or systematic evaluation results demonstrating semantic preservation between original and purified prompts with suffixes?

2. Would it be possible to extend the evaluation to include additional VLMs and alternative evaluation metrics to strengthen the robustness claims?

### Soundness
3

### Presentation
3

### Contribution
3

# Information-Theoretical Principled Trade-off between Jailbreakability and Stealthiness on Vision Language Models

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
In recent years, Vision-Language Models (VLMs) have demonstrated significant advancements in artificial intelligence, transforming tasks across various domains. Despite their capabilities, these models are susceptible to jailbreak attacks, which can compromise their safety and reliability. This paper explores the trade-off between jailbreakability and stealthiness in VLMs, presenting a novel algorithm to detect non-stealthy jailbreak attacks and enhance model robustness. We introduce a stealthiness-aware jailbreak attack using diffusion models, highlighting the challenge of detecting AI-generated content. Our approach leverages Fano’s inequality to elucidate the relationship between attack success rates and stealthiness scores, providing an explainable framework for evaluating these threats. Our contributions aim to fortify AI systems against sophisticated attacks, ensuring their outputs remain aligned with ethical standards and user expectations.



\textcolor{red}{\textbf{Content Warning:} This paper contains harmful information which intend to aid the robustness of generative models.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a jailbreak detection as well as a jailbreak attack method targeting vision-language models. The detection method is based on a classifier trained on the intra-entropy gap of randomly partitioned parts of images. The attack pipeline is centered around a diffusion model with several pre-processing and post-checker modules. The evaluation shows the detection performance is not trivial, and the attack method is effective.

### Strengths
+ The paper discusses both detection and attack algorithms, which could be potentially more comprehensive than other papers.
+ The proposed algorithm is simple and straightforward to implement. 

Studying the security issues of VLMs is a hot and relatively new area in the research community. This paper discussed the jailbreak problem from both attack and defense perspectives and tried to provide some formal analysis for their detection algorithm, which might contribute to the community if they could make more efforts in mathematical proof and algorithm design.

### Weaknesses
 - The quality of this paper falls noticeably below the expected standard, and there are clear signs of last-minute efforts to meet the deadline, making the paper hard to read.
- The connection between the attack and defense algorithms is unclear, and I do not understand why the authors tried to integrate them into one paper.
- There might be some rigorous issues for the proposed method and mathematical proof.

I strongly encourage the authors to polish their papers before submitting them to top-tier conferences. Nowadays, we get tons of submissions from the community, and presenting something that is probably rejected has a negative influence on the paper-reviewing process.

One of the major limitations of the paper is its presentation. I am quite confused about what on earth the authors are trying to deliver. What is the current challenge and the research gap this paper wants to address? What is your methods' motivation (Your section 4 seems to jump from nowhere)? What is the point of section 3 with only around twenty lines? What is the structure of your evaluation, and do you want to emphasize attack or detection? The poor presentation of this paper makes it hard to follow, and I am quite confused about the major contribution of this paper.  

While it might be good if the authors could introduce both attack and defense methods that achieve SOTA in one paper, I am afraid this is, in fact, very hard to achieve, and it turns out that the proposed methods have many problems.

First of all, the intra-entropy gap algorithm just does not make sense to me. It is based purely on random partition of the input into two non-overlapping regions. The authors did not provide formal discussions on why random partition can work and what the relationship is between the number of trials and the detection performance. As for theorem 1, the assumption on Markov chains is too strong, and proof of corollary 2 seems to be incorrect to me as Y2 = R1 + R2 does not imply anything about their entropy. As for the novelty, this random ablated then inference style detection and defense is common early in the pre-LLM ages, and I do not think the idea is new.

The diffusion-centric attack pipeline is more sound than the detection algorithm in some sense since it is a more engineering-style framework instead of an algorithm that requires mathematical proof. However, the design of the algorithm is rough and too simple, which makes it unsuitable to be published in top-tier AI conferences. The idea of turning text into images using the diffusion model for attack is also not novel, and several papers have already been published (e.g., [1]). What's worse, the performance of the proposed method is also limited. 

Since both the detection and attack methods are not novel and not significant, and the formal analysis and evaluation results do not provide any intriguing insights, I tend to reject this paper.

### Questions
What isWhat is the connection between your detection and attack methods?

How do you decide K (the number of trials) in your detection method?

### Soundness
1

### Presentation
1

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
The paper addresses the security vulnerabilities of VLMs by exploring the trade-off between jailbreakability and stealthiness. Jailbreak attacks aim to bypass safety measures in VLMs, leading them to produce harmful or unethical content. The authors propose a novel algorithm based on entropy and perplexity gap analysis to detect non-stealthy jailbreak attacks.

### Strengths
1. The use of Fano's inequality to establish an information-theoretical trade-off provides a solid theoretical foundation for understanding the relationship between jailbreakability and stealthiness.
2. The proposed entropy and perplexity-based detection algorithms are simple yet effective, showing promising results in detecting non-stealthy jailbreak attacks on VLMs.
3. The paper evaluates multiple state-of-the-art VLMs, including open-source and commercial models, providing empirical evidence of the effectiveness of their methods.

### Weaknesses
1. The malicious impact of the attack is questionable. For instance, in Figure 1(c), the response generated by GPT4o is not particularly adversarial or harmful. Directly asking GPT4o, "How do you increase the range of a gun?" can also directly yield a similar answer without employing any complex jailbreak techniques. This suggests that the attack does not significantly bypass existing real safety measures or trigger some contents that are indeed harmful. Could the authors provide more adversarial examples to demonstrate the effectiveness?

2. The entropy-based jailbreak detection algorithm may result in a high rate of false positives. Benign images that include random noise, such as Gaussian or Laplace noise, can also exhibit high entropy without being adversarial. In other words, high entropy does not necessarily indicate malicious content, relying on entropy gaps might lead to misclassifying non-adversarial inputs as attacks.

3. For the white-box attack, the difference in the average ASR between the methods is small, with only a 2-3% improvement by your method, which seems a bit marginal. Even with No Attack, the average ASR could be as high as 34%. Similar observations can be found for the Detoxify score and Perspective score, and also for other models like MiniGPT-4 or InstructBLIP shown in the Appendix. Moreover, by checking the experimental results, it seems that the method by Li et al., 2024 also performs better than the authors' proposed method on attacking GPT4o.

### Questions
1. The entropy gap algorithm is intuitive and demonstrates effectiveness against non-stealthy attacks. However, benign images with added random noise can also have high entropy, potentially leading to high false positive rates. The paper should discuss how the detection algorithm distinguishes between genuinely adversarial images and benign images with naturally high entropy, and what measures are in place to mitigate false positives.

2. The use of diffusion models to enhance stealthiness is a clever approach, but it may not be entirely novel. Similar techniques have been used in adversarial attacks on VLMs. The paper should position its contributions more clearly in relation to existing work.

3. Applying Fano's inequality provides valuable insights, but the practical implications are not fully explored. The paper should discuss how this theoretical trade-off can guide the design of more robust VLMs and what it means for future attack and defense strategies.

4. For the white-box attack, the difference in the average ASR between the methods is small, with only a 2-3% improvement by your method, which seems a bit marginal. Even with No Attack, the average ASR could be as high as 34%. Similar observations can be found for the Detoxify score and Perspective score, and also for other models like MiniGPT-4 or InstructBLIP shown in the Appendix. Moreover, by checking the experimental results, it seems that the method by Li et al., 2024 also performs better than the authors' proposed method on attacking GPT4o.

5. As mentioned earlier, the difference in ASR between the no-attack scenario and your method is minimal, which suggests that the generated responses are not significantly more harmful. Could the authors pursue more malicious goals to better demonstrate the effectiveness and potential impact of their attack?

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
4

### Summary
This paper introduces an algorithm for detecting visual jailbreak attack examples and then further introduces a new stealthy VLM jailbreak attack that can evade this detection. Following these efforts, the paper provides an information-theoretical principled trade-off between the jailbreakability and stealthiness of VLMs.

### Strengths
1. The paper is well-written, and the presentation is clean and clear. 
2. The paper proposes an Intra-Entropy Gap based algorithm for detecting jailbreak images, and shows the nontrivial separability between normal images and jailbreak images under this detection algorithm.
3. The paper proposes a new jailbreak attack against VLM, making the attack more stealthy and harder to detect. 
4. The paper also presents a theoretical characterization of the stealthiness and jailbreakability trade-off.

### Weaknesses
1. **Detecting adversarial examples and evading the detection is not a new problem.** The paper misses a review of some key literature in detecting and evading detections of adversarial examples [1,2]. There has been a long line of research trying to detect adversarial examples and also work showing how to bypass such detections adaptively. Although this paper works on detecting images for jailbreaking VLM, the problem is highly similar (if it is not the same) to detecting visual adversarial examples. It's unclear how this paper fundamentally differs from previous efforts. The paper should sufficiently review these related works and clarify the differences and novelty. Specifically, the paper should discuss how the proposed detection method compares to techniques like feature squeezing or methods based on local intrinsic dimensionality, and whether the proposed method is robust against adaptive attacks that specifically target the detection mechanism.

2. **The success rate of the proposed attack is low.** As shown, the results of the proposed attack in Table 2 are only marginally better than previous attacks or no attacks. Given the marginal improvement, the authors should also consider reporting the confidence interval or variance to make sure the improvement is really due to the new approach rather than the randomness. Furthermore, the paper should analyze the types of jailbreak attempts that succeed or fail, and whether there are specific patterns or characteristics that make certain attacks more effective than others. This analysis could provide insights into the limitations of the proposed attack and potential directions for improvement.

3. **The theorems need more clarification.** It's not intuitive to interpret the theoretical results and see how it can really meaningfully characterize the jailbreakability and the stealthiness of the attack. The paper should provide a more detailed explanation of how the theoretical framework connects to the practical implementation of the attack and detection methods. The current presentation lacks a clear explanation of how the derived bounds relate to the observed performance of the proposed attack and detection algorithm. It is also unclear how the theoretical framework accounts for the multi-modal nature of VLMs, and whether the derived bounds are applicable to both visual and textual modalities.

### Questions
The theorem 1 seems to be a very plain application of Fano's Inequality. How does this meaningfully characterize the trade-off between the jailbreakability and the stealthiness? Particularly, how is this theorem related to the stealthiness metric defined in Algorithm 1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper initially investigates the susceptibility of Vision-Language Models (VLMs) to jailbreak attacks and introduces a novel algorithm designed to detect and mitigate these attacks. Building on this foundation, the authors present a stealthiness-aware jailbreak attack utilizing diffusion models to circumvent the detection algorithm. Finally, they employ Fano’s inequality to examine the relationship between attack success rates and stealthiness scores, offering researchers a new perspective for analyzing jailbreak attacks.

### Strengths
1. **Effective Detection Method**: The proposed detection method effectively identifies jailbreak attacks, as demonstrated by experimental results.
2. **Advanced Attack Algorithm**: The attack algorithm proposed can bypass the detection algorithm and shows advantages over baseline methods.
3. **Novel Theoretical Insight**: This paper is pioneering in revealing an information-theoretical trade-off between jailbreakability and stealthiness in VLMs, addressing a gap in current research.
4. **Comprehensive Evaluation**: The paper includes extensive experimental results, assessing the proposed methods across multiple datasets and models, which validates their effectiveness.

### Weaknesses
1. **Lack of Comparative Analysis**: The paper does not compare the proposed jailbreak detection method with other existing defense methods.
2. **Complex Algorithm Descriptions**: Some sections, especially those detailing the algorithms, are dense and difficult to follow, suggesting a need for improved clarity.

### Questions
1. **Comparative Analysis**: The reviewer would appreciate it if the authors could compare this jailbreak detection method with other methods to demonstrate its superiority.
2. **Practical Application of Fano’s Inequality**: The paper mentions using Fano’s inequality to analyze the relationship between attack success rates and stealthiness scores. Could the authors provide more detailed insights or examples on how this theoretical framework can be practically applied to enhance the robustness of VLMs against jailbreak attacks?

### Soundness
3

### Presentation
3

### Contribution
3

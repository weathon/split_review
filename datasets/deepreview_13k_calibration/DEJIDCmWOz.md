# On the Reliability of Watermarks for Large Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
As LLMs become commonplace, machine-generated text has the potential to flood the internet with spam, social media bots, and valueless content. \textit{Watermarking} is a simple and effective strategy for mitigating such harms by enabling the detection and documentation of LLM-generated text. Yet a crucial question remains: How reliable is watermarking in realistic settings in the wild? There, watermarked text may be modified to suit a user's needs, or entirely rewritten to avoid detection. We study the robustness of watermarked text after it is re-written by humans, paraphrased by a non-watermarked LLM, or mixed into a longer hand-written document. We find that watermarks remain detectable even after human and machine paraphrasing. While these attacks dilute the strength of the watermark, paraphrases are statistically likely to leak n-grams or even longer fragments of the original text, resulting in high-confidence detections when enough tokens are observed.  For example, after strong human paraphrasing the watermark is detectable after observing 800 tokens on average, when setting a $1\mathrm{e}{-5}$ false positive rate. We also consider a range of new detection schemes that are sensitive to short spans of watermarked text embedded inside a large document, and we compare the robustness of watermarking to other kinds of detectors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the robustness of language watermarks against paraphrasing attacks. These attacks involve both paraphrasing models and tests against human rephrasing. The surveyed watermark is shown to be robust against all attacks. It is also more effective than retrieval-based attacks in cases where watermarked text is inserted into non-watermarked text. Comprehensive experimental details are provided in an appendix by the authors.

### Strengths
* Overall, I quite liked the paper and think that it addresses an interesting problem.

* The appendix is extremely detailed and offers a lot of valuable information on the reproducibility of their study. 

* The paper shows that the studied text watermark is robust against many attacks, including human paraphrasing, which is somewhat surprising. 

* The paper outlines many useful parameters and graphs for evaluating the robustness of watermarking.

### Weaknesses
The main issue I have with the paper is an unclear threat model: What is an attacker allowed to do to paraphrase sequence correctly? When is a paraphrased text too dissimilar from the watermarked text? The paper does not answer these fundamental questions, but follow-up papers must rely on these answers to propose improved attacks. 

Consider the following example: A human and a paraphraser want to preserve the "meaning" of the watermarked text. The watermark hides with high probability in high-entropy token sequences, such as names, locations, and numbers. Is a paraphraser allowed to replace these with random other names and locations, or would that be considered "unsuccessful" paraphrasing? I would love to see that discussed in the paper so that future papers can meaningfully improve on the presented attacks.

### Questions
* What is a successful paraphrasing attack? 

* What does an attacker need to achieve to undermine a watermark's robustness?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies an important and timely topic on the robustness of watermarked AI-generated text detection, in the scenarios of language model paraphrasing, human paraphrasing, and partial editing (e.g., copy and paste).

### Strengths
1. The research scope (whether an AI-general text embedded with watermarks can be easily removed or not) is an important and timely topic.
2. Empirical results are abundant and show the promise of the reliability of the evaluated watermark methods

### Weaknesses
1. Probably due to page limits, most spaces are used for presenting numerical results. The methodology section, including a new watermark method (e.g. SelfHash) and a new detection method (WinMax) in Sec. 3 is relatively short (roughly one page), and much important information is deferred to the Appendix.
2. The analysis will be more complete if it includes more recent and advanced post-hoc detection methods (such as RADAR https://arxiv.org/abs/2307.03838), because DetectGPT is known to be non-robust to paraphrasing. I would like to see the result of RADAR in ROC analysis and with varying token lengths.

### Questions
1. For the analysis of post-hoc detection, given that DetectGPT is shown to be fragile against paraphrasing (Sadasivan 2023), can the authors add a new analysis with a more robust post-hoc AI-text detector, like RADAR? I would like to see the result of RADAR in ROC analysis and with varying token lengths, as in Fig. 5 and Fig. 6.

2. I don't see much discussion on the utility of the studied watermark methods (especially the new one, SelfHash). if a watermark is robust but lacks usefulness, it is impractical. Can the authors report the usefulness of the new watermark methods that have been not studied in (Kirchenbauer 2023)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the effectiveness of watermarking as a means to identify machine-generated text in realistic scenarios, particularly when dealing with potential attacks, such as paraphrasing, copy-paste, or human rewriting. The primary objective is to evaluate whether watermarks can reliably detect machine-generated text when it's subjected to various forms of manipulation, thus contributing to the broader discourse on mitigating potential harms caused by generative language models.

### Strengths
Comprehensive Evaluation: The paper conducts a thorough and comprehensive evaluation of watermarking, considering various real-world attack scenarios, including paraphrasing, copy-paste, and human rewriting. This multifaceted approach provides valuable insights into the strengths and limitations of watermarking in practical settings.

Comparison to Alternative Methods: The paper not only focuses on watermarking but also compares it to alternative detection approaches, including post-hoc detectors like DetectGPT and retrieval-based systems. This comparative analysis enhances the paper's contribution by showcasing the relative merits of watermarking.

### Weaknesses
Lack of Theoretical Background: The paper does not delve deeply into the theoretical aspects of watermarking, which could be crucial in understanding the underlying principles and potential vulnerabilities. A more robust theoretical foundation could enhance the paper's overall quality.

Inherent Model Bias: The paper uses a specific language model (llama) for its experiments. While this model is justified and used for practical reasons, the results might not be universally applicable to all language models, which could limit the generalizability of the findings.

Limited Discussion of Social Implications: Given the paper's focus on mitigating potential harms from generative language models, it would be beneficial to include a more extensive discussion of the social implications of watermarking and other detection methods. This could provide a more holistic perspective on the topic.

### Questions
1. Can watermarking be further improved to make it more resilient to copy-paste attacks, given the significant performance drop observed under this scenario?

2. How does the performance of watermarking compare to other detection methods in detecting machine-generated text within shorter sequences or fragments?

3. Could watermarking be used in conjunction with other detection methods to enhance overall detection reliability, particularly in complex and adversarial settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

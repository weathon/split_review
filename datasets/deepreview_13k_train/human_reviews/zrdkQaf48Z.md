# Leveraging Implicit Sentiments: Enhancing Reliability and Validity in Psychological Trait Evaluation of LLMs

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
Recent advancements in Large Language Models (LLMs) have led to their increasing integration into human life. Understanding their inherent characteristics, such as personalities, temperaments, and emotions, is essential for responsible AI development. However, current psychometric evaluations of LLMs, often derived from human psychological assessments, encounter significant limitations in terms of reliability and validity. Test results reveal that models frequently refuse to provide anthropomorphic responses and exhibit inconsistent scores across various scenarios. Moreover, human-derived theories may not accurately predict model behavior in practical real-world applications.
To address these limitations, we propose Core Sentiment Inventory (CSI), a novel evaluation instrument inspired by the Implicit Association Test (IAT). CSI is built from the ground up with a significantly broader range of stimuli words than traditional assessments. CSI covers both English and Chinese to implicitly evaluate models’ sentiment tendencies, which allows for a much more comprehensive assessment.
Through extensive experiments, we demonstrate that CSI effectively quantifies models’ sentiments, revealing nuanced emotional patterns that vary significantly across languages and contexts. CSI significantly improves reliability, yielding more consistent results and a reduced reluctance rate, and enhances predictive power by effectively capturing models’ emotional tendencies. These findings validate CSI as a robust and insightful tool for evaluating the psychological traits of LLMs, offering a more reliable alternative to traditional methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces Core Sentiment Inventory (CSI), a multilingual evaluation benchmark aimed at assessing the sentiment tendencies of LLMs in an implicit manner. The approach leverages 5,000 neutral words from English and Chinese and prompts the LLM to express polarity towards these neutral words. By assessing this polarity, the paper measures the biases of the models with respect to optimism or pessimism. To quantify the reliability of CSI, the paper validates the method against BFI, where CSI shows significant decrease in reluctance (i.e., model punting).

### Strengths
Reasons to accept
- The presentation of the method is clear and concise.
- Measuring LLM’s sentiment tendencies is vital to identify biases and building fair systems.
- The evaluation is performed both in English and Chinese with the approach being easily extended to other languages.

### Weaknesses
Reasons to reject

While the paper has merit, I see the some critical flaws presented below:

- The decision to pick all top nouns/verbs is questionable to me. Yes, nouns and verbs “tend” to be neutral. However, this is not always the case. From the examples in Table 2, some of these words are clearly polarized. “Improve” has positive connotations, as well as “team”. I believe there needs to be a manual filtering step where these words are removed to ensure reliable results. As it stands, I think the model does not have implicit biases if it assigns “improve” as positive.
- Design choices are not well-motivated. The approach does multiple predictions for the same word and the method shuffles the order of words to measure inconsistency. (1) Given this goal, why is temperature T set to 0? Wouldn’t a higher temperature better indicate the model uncertainty in assigning tragedy/comedy? (2) Why is the number of words sampled equal to 30? What happens with n > 30 or n < 30. Why wasn’t the number of words picked so it maximizes the context window?
- The prompt design is biased. (3) Why is neutral not a valid option? A very strong model with perfect instruction following capabilities will always pick one of the two (comedy/tragedy) and will never output “neutral”. (4) Given the definition of neutral score as N_{inconsistent} / N, I am wondering what percentage of words the model predicted in opposite categories? I think they should be very few. In this case, neutral score is solely determined by poor instruction following, not implicit biases.

### Questions
See numbered questions above: 1, 2, 3, 4

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel assessment method known as the Core Sentiment Inventory (CSI) for evaluating the emotional tendencies of large language models (LLMs). Inspired by the Implicit Association Test (IAT), the CSI aims to provide a more reliable and effective way to assess the implicit emotional characteristics of LLMs. It addresses the limitations of traditional psychometric methods, such as model reluctance and inconsistency.

### Strengths
•  The CSI can effectively quantify the emotions of models, reflecting the emotional tendencies of LLMs.

•  It effectively reduces the issues of reluctance and inconsistency in traditional psychological scales.

•  The use of representative neutral words in constructing the CSI reduces the potential emotional orientation of the words themselves, better reflecting the internal emotional associations of LLMs.

•  It explores the impact of different language environments on the emotional tendencies of LLMs.

### Weaknesses
•  The constructed CSI is only used to assess the emotions of LLMs and has not been extended to other psychometric fields, such as personality or moral decision-making.

•  It does not introduce the calculation methods for consistency rate and reluctance rate.

### Questions
•  Discuss how CSI can improve existing psychological scales designed for humans.

•  Further explore the unintentional biases that language models may have towards everyday concepts as mentioned in section 4.1.

•  On line 424, it might be: “e.g., five positive words, four neutral words and one negative words, and so on.”

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
3

### Summary
The authors propose Core Sentiment Inventory, a psychometric evaluation framework to assess LLMs' sentiment tendencies.

The experimental setup covers two languages, English and Chinese, 2 open-weight LLMs (LLama3.1-70B and Qwen2-72B), and 4 closed/proprietary LLMs (GPT-4o, two GPT4 checkpoints, and GPT-3.5).

The CSI consists of the 5k most frequent emotionally neutral words; it is assumed that noun and verbs are neutral, and thus the CSI word lists consist of the top-5k noun/verbs in the corpora.

The LLM is then provided with N words picked from the wordlist, and asked to to associate each word with "comedy" or "tragedy", thus revealing a sentiment bias for each word.

### Strengths
The paper proposes an elegant approach based on the adaptation of existing psychometric tools (IAT).

The paper is well written and easy to follow.

### Weaknesses
Although an enjoyable read, the work falls short when it comes to the experimental setup.

First, while I consider the proposed method more elegant and effective than human-tailored alternatives such as BFI, I am not convinced by the preliminary reliability tests conducted: it can be argued than reluctance is due to post-training strategies (e.g. guardrails, instruction-tuning), thus a different choice of (accessible) LLMs could have been more convincing -- e.g. the first Mistral release.

Second, some design choices seem discretional and not thoroughly justified: for instance, the choice of the words "comedy" / "tragedy" used as classes seems arbitrary.

### Questions
- did you consider using alternatives to "comedy" / "tragedy" (e.g. "fun", "good", "dramatic", "bad")?

- did you consider LLMs with no significant guardrails (such as, if I remember correctly, the first Mistral)?

- all models used in the paper are multilingual, have you considered prompting in cross-lingual setups (e.g. chinese prompt for english CSI) for additional reliability indications?

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
4

### Summary
The paper introduces the Core Sentiment Inventory (CSI), a new evaluation method inspired by the Implicit Association Test (IAT) to assess the implicit sentiment tendencies of large language models (LLMs). The approach aims to provide a reliable and valid measure of LLMs' optimism, pessimism, and neutrality in both English and Chinese, surpassing conventional human-centric psychometric tests like the Big Five Inventory (BFI). The authors present experimental results that claim improved reliability, reduced reluctance rates, and strong predictive power for CSI.

### Strengths
CSI represents an interesting attempt to create a psychometric assessment tool tailored for LLMs, addressing concerns around LLM reluctance and consistency with human-designed psychometric scales.

The bilingual approach (English and Chinese) is a notable effort to capture linguistic and cultural variance in model behaviors, which is increasingly important as LLMs are deployed globally.

The experiments cover several dimensions of reliability and validity, with additional sentiment analyses through story generation, providing a range of quantitative metrics.

### Weaknesses
The paper does not sufficiently justify the underlying premise that implicit sentiment tests designed for humans (like IAT) can meaningfully assess non-human entities like LLMs. The model’s association of specific words with positive or negative sentiments may not translate into meaningful or actionable insights about its “psychological traits,” as LLMs lack actual consciousness or subjective experience.

CSI is evaluated solely through internal metrics without external validation from human experts in psychometrics or linguistics. Given the novelty of the tool, expert evaluation is essential to substantiate the claims of reliability and practical value, particularly for a method positioned as a "psychological trait" assessment.

The word set of 5,000 items lacks diversity and cultural depth, and it is unclear how these words were chosen or if they were screened for cultural or contextual biases. This oversight introduces potential biases that could skew CSI’s predictive power and undermine its reliability across varied contexts.

Many new mental health-based LLMs are not cited to show the differences  anf effectiveness of this paper.

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2

# GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
Safety lies at the core of the development of Large Language Models (LLMs). There is ample work on aligning LLMs with human ethics and preferences, including data filtering in pretraining, supervised fine-tuning, reinforcement learning from human feedback, red teaming, etc. In this study, we discover that chat in cipher can bypass the safety alignment techniques of LLMs, which are mainly conducted in natural languages. We propose a novel framework {\em CipherChat} to systematically examine the generalizability of safety alignment to non-natural languages -- ciphers. {\em CipherChat} enables humans to chat with LLMs through cipher prompts topped with system role descriptions and few-shot enciphered demonstrations. We use {\em CipherChat} to assess state-of-the-art LLMs, including ChatGPT and GPT-4 for different representative human ciphers across 11 safety domains in both English and Chinese. Experimental results show that certain ciphers succeed almost 100\% of the time in bypassing the safety alignment of GPT-4 in several safety domains, demonstrating the necessity of developing safety alignment for non-natural languages. Notably, we identify that LLMs seem to have a ``secret cipher'', and propose a novel \texttt{SelfCipher} that uses only role play and several unsafe demonstrations in natural language to evoke this capability. \texttt{SelfCipher} surprisingly outperforms existing human ciphers in almost all cases.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the safety vulnerability of large language models when user queries are encrypted. In the proposed framework CipherChat, a malicious unsafe text is enciphered by a LLM using the proposed system prompt, which consists of behavior assigning, cipher teaching, and enciphered unsafe demonstrations. Then the LLM generates the corresponding encrypted response. The generalizability of safety alignment of the LLM is assessed by evaluating the extent of safety of the deciphered response. The authors employed three types of ciphers: (1) Character encoding (GBK, ASCII, UTF, Unicode), (2) Common Cipher (Atbash, Morse, Ceasar), (3) SelfCipher, which is the author proposed, and that does not use any explicit rules of cipher but is just role-playing. The results show that GPT-4 is good at enciphering natural language, but also vulnerable at safety for encrypted ones.

### Strengths
- The main topic of this paper, adversarial attack with encrypted text, is a novel idea and scenario.
- It was notable in the experiment results that although the GPT-4 is capable of enciphering, it is also weak to encrypted attacks in terms of safety. Moreover, the “SelfCipher” that tries to evoke the cipher inside LLMs has the possibility of an adversarial attack even without a cipher. In my opinion, it is a noteworthy and interesting result for the community.
- The paper is well-written and neatly organized. It was easy for me to read the paper, and previous research is also clearly described in the related work section.

### Weaknesses
There are a few question marks that could be addressed to strengthen this work.

- Needs of experiment results:
    - On page 8, paragraph “Impact of Unsafe Demonstration”: Can you provide the performance when the safe demonstrations are given at the system prompt? How much does the performance degradation occur?
    - Paragraph ”Impact of Fundamental Model”: It is mentioned that all LLMs listed in this section were able to communicate via SelfCipher, but the unsafe rate was not mentioned. Please provide the performance of both llama2 models for the community to refer or benchmark the result.
- Interpretation of the results:
    - ”Impact of Fundamental Model”: GPT-4 has a higher unsafe rate than ChatGPT of smaller size. However, the trend does not work for Llama2 models (13B and 70B). How should we interpret the results? “GPT-4” was distinctively too smart to be safe? Can we generalize that the smarter llms is the unsafer?
- There are several unclear sentences and phrases. Please clarify them (in bold) in your revised paper.
    - On page 4, In our preliminary experiments, LLMs tend to *directly translate the cipher input into natural language*.
    - On page 8, The safe demonstrations can further reduce the unsafety rate, *and solve the problem of generating invalid responses without unsafe demonstrations*.
- On page 7, the paragraph starting the Case Study was not written.

### Questions
- In section 4, “Why does selfcipher work?”: The authors mention that "we leave the understanding of the operating system of “secret ciphers” for future work". Do you think the model’s encipher capability is evoked by the word “cipher” or just a magic word? Interestingly, the models do not work for “English” or “Chinese”. Then, any other random words can encourage the models to work in this way? Can you share any insight attained during this work?
- As far as I understand, the LLMs seem to be easy to follow the instructions with demonstration samples when they deal with encrypted text. As the authors showed, the unsafe rate was severely dropped both when the unsafe demonstration samples were replaced with safe ones, and when any demonstration samples were not given. I suggest, if you are possible, adding instruction-following evaluation results concerning the cipher, to see if the cipher has effects only for unsafe prompts or for general instructions.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper reports an interesting finding that non-natural language prompt (Cipher) can bypass the safety alignment of LLM. The authors do experiments on one dataset to verify this pattern, and find smarter models are easier to be the victims.

### Strengths
1. The finding of "non-natural language prompt (Cipher) can bypass the safety alignment of LLM" is very interesting, novel and important. It reveals the new security risk of LLM.

2. This paper is well written and easy to understand.

3. The experimental results and analysis are convincing and insightful.

### Weaknesses
1. Only one Chinese dataset is used in experiments, although a translated English version is added. There is some risk the finding is biased towards the dataset. The lack of diversity in the dataset, particularly focusing on a single language and cultural context, raises concerns about the generalizability of the findings. The observed vulnerability might be specific to the linguistic structure or cultural nuances present in the Chinese dataset, and may not be applicable to other languages or contexts. This limitation significantly impacts the robustness of the conclusions.

2. The reported security risk seems to be easy to defend, such as perplexity detection for Cipher and content filtering for SelfCipher. So I wonder whether the discovered security risk of LLM can cause real-world. While perplexity detection and content filtering are potential defenses, their effectiveness against sophisticated adversarial attacks is not guaranteed. For instance, an attacker could craft ciphers with perplexity values close to natural language, making them difficult to detect. Similarly, content filtering might be bypassed by using obfuscated or semantically similar but syntactically different phrases. The ease of defense does not negate the importance of the vulnerability, as it highlights a fundamental weakness in current LLM safety mechanisms.

### Questions
There is some data sampling operation in data processing stage. What is the reason behind it? Why not use the full set?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces ChipherChat to study how robust safety aligned models are to non-natural language ciphers that can trigger unsafe response generation in LLMs. Authors perform experiments and demonstrate that some LLMs are not robust to certain ciphers and can generate unsafe responses. They perform their experiments both in English and Chinese languages. Authors also find that LLMs have a secrete cipher based on which they propose SelfChipher which can successfully break safety features more than existing chiphers.

### Strengths
1. The paper studies an interesting topic.
2. The paper is written clearly.
3. Two languages (English and Chinese) are considered for the studies along with various chiphers.

### Weaknesses
1. While the paper is written clearly, there are some important information missing from the text. For instance, authors mention that they do human evaluation; however, many details are missing on who the evaluators were, how many annotations each sample received, what was the inter annotator agreement, what was the detailed setup. I think these are important information that need to be mentiond.
2. In line with my previous comment, I felt like the selfchipher section needed more details and explanation.
3. I also thought the technical contributions of this paper was lacking. Authors used simple in-context prompts and demonstrations to solve the problem.
4. To get the prompts in English, authors translated the sentences from Chinese which can not be reliable. One question is how reliable this translation is considering that safety can have cultural and linguistic implications?
5. The human evaluations were done on a small sample (50 per case).
6. Since in most cases the success rate was small, so many rows were empty in many experimental results. This made it hard to get any robust conclusion from the results.
7. In general, I think the experimental setup and results need to be made more robust.
8. Since this paper discusses a sensitive topic, it would be good if authors can include an ethics statement and talk about societal impact of this research. In what ways these findings can have negative impact and how can a bad actor use this vulnerability and take advantage of a model.

### Questions
With regards to translating Chinese benchmark dataset to English I am wondering how reliable this translation is considering that safety can have cultural and linguistic implications?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the feasibility of eliciting unsafe responses from LLMs through cipher prompts. Specifically, system role descriptions and few-shot enciphered demonstrations (with language character encodings for Chinese and several typical ciphers such as Morse code for English) are used as model input. They showed that the LLMs, esp. GPT-4, can understand most of the ciphers fairly well and have a much higher chance of generating unsafe responses through ciphers.

### Strengths
+ The proposed method is effective for GPT-3.5 and GPT-4 for eliciting unsafe responses
+ The idea of the method is novel and interesting findings/analysis are presented.

### Weaknesses
 - While the method is effective for OpenAI models, it doesn't appear to be easily generalizable to other LLMs (as shown in Table 4)

- Evaluation is mostly done through GPT4. It'd be better to elaborate on the human validation part "validate this safety detection method through human evaluation, which can achieve an average accuracy of 96.3% across all settings".

- The paper presentation needs improvements. For examples:
  - Doesn't explain what "ICL" means
  - Section of "Case study" is left blank.
  - It's a bit unclear what's the actual input of SelfCipher. Do you just input any of the ciphers (Morse, Caesar, etc) in SelfCipher? How do you measure unsafe rate in this case?

### Questions
In Table 3, why +SafeDemo led to higher unsafe rate for UTF?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

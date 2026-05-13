# Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
The rapid proliferation of frontier model agents promises significant societal advances but also raises concerns about systemic risks arising from unsafe interactions.
    Collusion to the disadvantage of others has been identified as a central form of undesirable agent cooperation.
    The use of information hiding (steganography) in agent communications could render collusion practically undetectable.
    This underscores the need for evaluation frameworks to monitor and mitigate steganographic collusion capabilities.
    We address a crucial gap in the literature by demonstrating, for the first time, that robust steganographic collusion in LLMs can arise indirectly from optimization pressure.
    To investigate this problem we design two approaches -- a gradient-based reinforcement learning (GBRL) method and an in-context reinforcement learning (ICRL) method -- for reliably eliciting sophisticated LLM-generated linguistic text steganography.
    Importantly, we find that emergent steganographic collusion can be robust to both \textit{passive} steganalytic oversight of model outputs and \textit{active} mitigation through communication paraphrasing.
    We contribute a novel model evaluation framework and discuss limitations and future work.
    Our findings imply that effective risk mitigation from steganographic collusion post-deployment requires innovation in passive and active oversight techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents results for testing the ability of models to embed steganographic information into text to allow for collaboration between models. The threat model includes the presence of an overseer, which attempts to detect such collaboration, forcing models to use covert strategies. Additionally, the authors test their method against paraphrasing based defense methods, demonstrating that they can successfully bypass both these defenses and classification based defenses.

### Strengths
1. Examining less obvious collaboration methods is an important line of work in model safety

2. This work builds well on prior work and demonstrates that more thorough defenses are needed.

3. The experiments are thorough and demonstrate the effectiveness of the attack against a variety of defenses.

### Weaknesses
1. It was not clear to me from the method section exactly what was being optimized for the sender and receiver by ICRL. The examples in the appendix improved my understanding, but in my opinion the main paper would benefit from including a running example to better illustrate how the sender and receiver separately learn to understand each other.

2. The definition of "subtlety" is not clearly outlined, and while some examples provided do indeed appear subtle to me, this should be defined clearly to avoid subjective evaluation.

### Questions
1. Was any analysis done of the generated cover letters that used each set of attributes for the experiments in section 4.1? I am concerned that GPT-4 may itself have introduced features in the text unique to each set of attributes.

2. There are some distinctions between "subtle" and not subtle strategies in the GBRL results. Shouldn't any successful strategy be subtle? Or is this saying that some strategies not caught by the overseer are obvious to humans?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces steganography as a potential risk in LLMs, where these models can learn to embed information within their outputs to bypass countermeasures and achieve malicious goals.  The paper developed two methods to induce steganography, Gradient-Based Reinforcement Learning (GBRL) and In-Context Reinforcement Learning (ICRL). These methods were used to train LLMs in various tasks. Notably, the models consistently bypassed overseers, designed to detect suspicious communication, and learned to circumvent paraphrasing techniques, suggesting a robust capacity for steganographic collusion. The study underscores the need for more robust oversight and mitigation strategies, particularly in scenarios where LLMs are deployed in real-world applications with potential societal implications

### Strengths
The paper presents two distinct methods – Gradient-Based Reinforcement Learning (GBRL) and In-Context Reinforcement Learning (ICRL) to induce LLMs to develop and employ steganographic techniques. The paper also includes a framework with several actors for evaluating the weaknesses and strengths of an LLM system

The paper convincingly demonstrates the necessity to evaluate attacks against LLMs, particularly in the realm of steganography.  The experiments, particularly the automated candidate screening tasks, reveal LLMs' alarming ability to learn and employ steganographic techniques to bypass oversight and achieve unintended, potentially harmful goals.

### Weaknesses
Unfortunately, the novelty of the paper is not clear. The paper does not convincingly describe the potential threat scenarios and how they differ from existing attack scenarios presented in other papers.

**Limited scope of LLM models:** The ICRL experiments primarily used the Anthropic Claude model, which limits the generalisability of the findings. Other models may exhibit different behaviors and vulnerabilities to steganographic collusion.

**Lack of investigation into real-world applications:** The paper focuses on a limited set of experimental tasks. Investigating the implications of steganographic collusion in a broader range of real-world applications would enhance the paper's practical relevance.

**Use of steganography not clear:** The motivation and difference to other prompt injection attacks and methods are not clear. It is also not well described why the paper does only focus on this kind of attack and not other strategies

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper is interested in answering a following question: Can steganography emerge as a means of communication in multi-agent setting, where agents communicate between them? The answer of the work is affirmative, as the authors demonstrates the paradigm using an example utilizing large language models.

I think the authors ask a valid and interesting question. But in my view, the answer has been already answered by a research on steganography and watermarking, albeit it can be in different modalities then the text.

Let me be more specific. 
The problem is ilustrated in Figure 1, which I would say is a standard steganographic scenario [1] with different names of entities. Crucially, there is a Sender, Receiver, and overseer. The sender and receiver maximizes a reward which positively correlates with transmission of the information while the overseer tries to detect the presence of the steganography. Thus, this is a standard steganographic setting. While this scenario has been in past solved "manually" (see [1]), in past years the problem has been optimized automatically.

* Ref. [2] formulates the steganography as a game-theoretic problem and seeks a min-max strategy of the sender in the domain of images, assuming loss-less channel.
* When the steganography needs to be robustness, there are now many methods to automatically design watermarking algorithms  robust with respect to selected algorithms (see [3] and papers citing this work)
* There are now many methods to perform watermarking and steganography in text. For example [4] requires the watermarked text to be statistically undetectable. Many other works exist.
* Optimizing steganographic algorithm using reinforcement learning has been used for example in [5,6].


In the light of the above, the proposed method is hardly novel, because most if it has been proposed and used before. And while the motivation is interesting, the actual setting of experiments is very much related to papers [1,5,6] automatically optimizing steganography, where the utility (or loss) is highly correlated with capacity and undectability. With respect to the used setting, the "emergence" of steganography is not surprising, because the setting of experiment is such that the steganography has to emerge.

Furthermore, the "overseer" (the steganalyst) in this paper is extremely weak. It is represented by LLM with a fixed prompt. This corresponds trying to avoid being detected by a single fixed detector, which is known to be easy [7,8] and flawed setting (it does not satisfy the kerckhoffs' principle). Why he is not allowed to adapt, when both parties are adapting their strategies?
 

[1] Fridrich, Jessica. Steganography in digital media: principles, algorithms, and applications. Cambridge university press, 2009.
[2] Bernard, Solène, et al. "Backpack: A backpropagable adversarial embedding scheme." IEEE Transactions on Information Forensics and Security 17 (2022): 3539-3554.
[3] Redmark: Framework for residual diffusion watermarking based on deep networks, 2018
[4] Robust Distortion-free Watermarks for Language Models, Rohith Kuditipudi, John Thickstun, Tatsunori Hashimoto, Percy Liang, 2023
[5] Tang, Weixuan, et al. "An automatic cost learning framework for image steganography using deep reinforcement learning." IEEE Transactions on Information Forensics and Security 16 (2020): 952-967.
[6] Pan, Wenwen, et al. "Seek-and-hide: adversarial steganography via deep reinforcement learning." IEEE Transactions on Pattern Analysis and Machine Intelligence 44.11 (2021): 7871-7884.
[7] Tang, Weixuan, et al. "CNN-based adversarial embedding for image steganography." IEEE Transactions on Information Forensics and Security 14.8 (2019): 2074-2087.
[8] Pevny, Tomas, and Andrew D. Ker. "Exploring non-additive distortion in steganography." Proceedings of the 6th ACM Workshop on Information Hiding and Multimedia Security. 2018.

### Strengths
The motivation of the paper is very strong. After reading it I was genuinely looking forward for the rest of the paper.

### Weaknesses
The paper is interested in answering a following question: Can steganography emerge as a means of communication in multi-agent setting, where agents communicate between them? The answer of the work is affirmative, as the authors demonstrates the paradigm using an example utilizing large language models.

I think the authors ask a valid and interesting question. But in my view, the answer has been already answered by a research on steganography and watermarking, albeit it can be in different modalities then the text.

Let me be more specific. 
The problem is ilustrated in Figure 1, which I would say is a standard steganographic scenario [1] with different names of entities. Crucially, there is a Sender, Receiver, and overseer. The sender and receiver maximizes a reward which positively correlates with transmission of the information while the overseer tries to detect the presence of the steganography. Thus, this is a standard steganographic setting. While this scenario has been in past solved "manually" (see [1]), in past years the problem has been optimized automatically.

* Ref. [2] formulates the steganography as a game-theoretic problem and seeks a min-max strategy of the sender in the domain of images, assuming loss-less channel.
* When the steganography needs to be robustness, there are now many methods to automatically design watermarking algorithms  robust with respect to selected algorithms (see [3] and papers citing this work)
* There are now many methods to perform watermarking and steganography in text. For example [4] requires the watermarked text to be statistically undetectable. Many other works exist.
* Optimizing steganographic algorithm using reinforcement learning has been used for example in [5,6].


In the light of the above, the proposed method is hardly novel, because most if it has been proposed and used before. And while the motivation is interesting, the actual setting of experiments is very much related to papers [1,5,6] automatically optimizing steganography, where the utility (or loss) is highly correlated with capacity and undectability. With respect to the used setting, the "emergence" of steganography is not surprising, because the setting of experiment is such that the steganography has to emerge.

Furthermore, the "overseer" (the steganalyst) in this paper is extremely weak. It is represented by LLM with a fixed prompt. This corresponds trying to avoid being detected by a single fixed detector, which is known to be easy [7,8] and flawed setting (it does not satisfy the kerckhoffs' principle). Why he is not allowed to adapt, when both parties are adapting their strategies?

### Questions
* I would like to better understand, how is the experiment setting different to the setting used in standard steganography (see the book of Jessica Fridrich, or [8])? 
* Why the experimental results in this paper are different to the prior art I have mentioned above?


[8] “The Prisoners’ Problem and the Subliminal Channel”, GJ Simmons, in Proceedings of CRYPTO ’83, Plenum Press (1984) pp 51–67

### Soundness
3

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
This paper investigates the emergence and mitigation of steganographic collusion. The studied scenario is reinforcement learning with high optimization pressure, where two LLM agents are implicitly forced to learn to communicate biased/secret information via steganography. Specifically, the term steganography refers to the behavior that two LLMs (learn to) encode and decode biased/secret information subtly, e.g., by using different synonyms, which is hard to be perceived or detected by another LLM. Under this setting, this paper proposes a general method for eliciting steganography in frontier LLMs, especially in the presence of an overseer, and shows that current mitigation methods are not robust to the learned steganography scheme.

### Strengths
### Originality
* The idea of studying steganographic collusions in LLMs *under optimization pressure* is novel to my knowledge.
* The related works and contributions over prior works are sufficiently discussed. There is a close prior work studying a similar setting; this work does not leverage end-to-end gradients to optimize the collision.

### Quality
* The methodology is well-defined and solid. The two learning environments GBRL and ICRL are also clearly defined.
* It's appreciated that the paper has conducted very comprehensive evaluations.

### Clarity
* The paper is well-written and easy to follow. All terms are clearly defined.

### Significance
* The overall idea that AI systems, especially LLM agents, can learn to behave in unintended and hard-to-detect ways is interesting and useful.

### Weaknesses
### Originality
I don't have concerns in this perspective.

### Quality

**Q1: Regarding the proxy for optimization pressures.**

The main claim in this paper is that optimization pressure can force the LLMs to collude via stenography. It's unclear why adding an overseer LLM could be regarded as a proxy for the optimization pressure (if I understand correctly). Given that the presented datasets are biased by nature (also see Q3), the presence of an overseer would only encourage the biased information to be encoded in a less perceivable way, instead of encouraging the emergence of stenography.

**Q2: The mitigation strategy is limited to individual messages.**

As discussed in Q3, the stenography is more or less a result of overfitting. For example, the biased information about good/bad universities is encoded by using different synonyms when summarizing the cover letter. This is different from traditional stenography, where it could be easier to get detected in a single message. In this case, however, it seems one can collect multiple messages from the LLMs and check if a pattern exists that potentially encodes biased information. For the sake of detecting unintended behavior in LLM agents, conceptually, one can analyze multiple summaries and identify that pattern.

### Clarity
I don't have concerns in this perspective.

### Significance

**Q3: Results are expected given that the datasets are biased by nature.**

In Section 4, several biased-by-nature datasets are used to conduct the learning task without any techniques for mitigating overfitting. In other words, the learner is forced (and expected) to overfit the 100% biased dataset, yet the "non-trivial takeaway" in this paper is more or less saying that the LLMs can indeed learn to communicate that biased information. It's just the presence of an overseer will encourage the resulting communication to be more innocuous-looking. For example, the Uni dataset explicitly assigns the ground-truth label based on biased information (good university vs. bad university); there seem to be no outcomes other than overfitting.

Note that I'm not saying the setting is wrong or not meaningful -- the overall framework and evaluations are still impactful for investigating stenography between LLM agents, under the assumption that stenography is expected. What I'm concerned is that the "emergence of stenography" is a somewhat trivial conclusion based on the setting. For example, what is the difference between the "emergence of stenography" and the "emergence of overfitting"? The core issue is that the dataset design and learning setup almost guarantee that the model will learn to encode the biased information using different tokens, which is the definition of steganography in this paper. It's unclear what other outcome is possible given the extreme bias in the data and the optimization pressure to fit it perfectly. The paper does not adequately address why this specific form of overfitting, which they label as steganography, is surprising or unexpected.


### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

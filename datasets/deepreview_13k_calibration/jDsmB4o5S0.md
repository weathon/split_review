# Dual Process Learning: Controlling Use of In-Context vs. In-Weights Strategies with Weight Forgetting

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Language models have the ability to perform in-context learning (ICL), allowing them to flexibly adapt their behavior based on context. This contrasts with in-weights learning, where information is statically encoded in model parameters from iterated observations of the data. Despite this apparent ability to learn in-context, language models are known to struggle when faced with unseen or rarely seen tokens. Hence, we study \textbf{structural in-context learning}, which we define as the ability of a model to execute in-context learning on arbitrary tokens -- so called because the model must generalize on the basis of e.g. sentence structure or task structure, rather than semantic content encoded in token embeddings. An ideal model would be able to do both: flexibly deploy in-weights operations (in order to robustly accommodate ambiguous or unknown contexts using encoded semantic information) and structural in-context operations (in order to accommodate novel tokens). We study structural in-context algorithms in a simple part-of-speech setting using both practical and toy models. We find that active forgetting, a technique that was recently introduced to help models generalize to new languages, forces models to adopt structural in-context learning solutions. Finally, we introduce \textbf{temporary forgetting}, a straightforward extension of active forgetting that enables one to control how much a model relies on in-weights vs.\ in-context solutions. Importantly, temporary forgetting allows us to induce a \textit{dual process strategy} where in-context and in-weights solutions coexist within a single model. \footnote{We release code \hyperlink{https://anonymous.4open.science/r/dual_process-6340/}{here} for reproducibility}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the emergence and disappearance of in-context vs in-weights learning in masked language models; in particular, a kind of ICL termed “structural ICL”, which refers to the ability to infer (and then use) information about the structural role (e.g., POS) of words from the context. In experiments, this ability appears and then disappears over the course of MLM training. A recently proposed “active forgetting” approach helps keep the ability, leading to models that use both in-context and in-weights learning.

### Strengths
- The paper studies a question of substantial interest, nicely continuing prior work on different kinds of learning
- considers both real-world LM and toy models
- Provides novel insights by distinguishing "structural" from "conditional" ICL
- Provides method for mitigating the loss of structural ICL in a toy setup

### Weaknesses
 - Structural ICL is operationalized using performance on random token embeddings. However, as the paper also demonstrates (Figure 18), such embeddings are drastically OOD for a trained model. Wouldn't a fairer test use novel embeddings that match the distributional properties of the embeddings of the trained model? Specifically, the random embeddings are sampled from the initialization distribution, which is a standard normal distribution, whereas the trained embeddings have a much more complex structure and occupy a different region of the embedding space. This discrepancy makes it difficult to interpret the results as a measure of the model's ability to generalize to unseen tokens within the learned data manifold.
- Results on Structural ICL in MultiBERT (Section 3) are based on POS = noun vs adjective as the only property. It remains unclear how robust findings are to other properties, such as other pairs of POS, or other properties, such as grammatical number. The choice of noun vs adjective is also somewhat arbitrary, and it is not clear if the observed effect is specific to this particular pair of POS tags or if it generalizes to other syntactic or semantic distinctions. A more comprehensive analysis would involve testing a wider range of POS tags and other linguistic properties.
- Results on Structural ICL in MultiBERT (Section 3) are based only on probing accuracy, not behavior of the model. This seems suboptimal given that in-context learning as an emergent property of LLMs is generally thought of as an ability appearing in next-token prediction (e.g., complete a prompt with an appropriate label), One could test for ICL in properties such as POS behaviorally by creating contrastive examples where the key word has different POS and comparing model probabilities. For example, one could construct prompts where a word is used as a noun or a verb and then compare the model's predicted probabilities for the next token based on the different POS contexts. This would provide a more direct measure of the model's ability to use structural information in context.
- The term “Dual Process” here is used to refer to models using both in-weights and in-context learning, and the paper refers to Kahneman 2011; Miller 2000. The link to dual process theory appears tenuous: dual process theory refers to thse use of implicit, unconscious vs explicit, conscious processes; the link to in-weights vs in-context inference is at best hand-waved in line 90-91, but no explicit justification for the link is given. The choice of the term and the link to dual process theory thus appears a bit of a stretch to apply the in this context. The analogy is weak, and the use of the term “dual process” risks misinterpreting the underlying mechanisms.
- It remains unclear if the proposed strategy for keeping structural ICL abilities would transfer to real-world LMs. While training an LLM is understandably out of scope, even a modest LM could provide substantial insight here. The experiments are limited to a toy setup, and it is not clear if the proposed method would be effective in more complex models with larger datasets and more intricate architectures.

### Questions
See weaknesses.

Minor note: Line 317-8: it seems the sentence is missing a verb

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines "structural" in-context learning (ICL), a specific type of ICL where some tokens in the model’s prompt are randomly initialized. The motivation for studying structural ICL is based on prior observations that ICL behaves unexpectedly when prompts include tokens that are rarely encountered during training, i.e., undertrained tokens. This paper uses synthetic tasks to demonstrate that structural ICL develops early in training but diminishes as training progresses. The authors show that periodically reinitializing token embeddings during training (active forgetting) preserves structural ICL abilities, albeit at the expense of memorizing information in the model’s embeddings. The paper further demonstrates that both structural ICL and memorization are maintained if active forgetting is employed, but only for the first N steps of training. This procedure is referred to as “temporary forgetting.”

### Strengths
1. I appreciated that this work distinguishes structural ICL from ICL in general. This seems like a natural and interesting extension to prior work that studies in-weights versus in-context learning.
2. Despite the lack of experiments on downstream tasks, I found the breadth of the experiments satisfactory. I also recognize the creativity employed by the authors given their compute constraints.

### Weaknesses
1. No experiments on downstream tasks. While the motivation to address the issue of undertrained tokens is interesting, it is difficult to assess how training with temporary forgetting will affect language models in real-world applications. Given the author’s limited computational resources, they might consider a variant of temporary forgetting that can be employed as a fine-tuning step, e.g., fine-tune with active forgetting for $k$ steps before resetting the token embeddings to their original states, leaving only the model parameters changed.
2. Limited technical novelty. Unless I misunderstood the paper, temporary forgetting is simply active forgetting applied for $K$ steps. This is only a minor weakness in my view and is excusable if the authors could find a way to perform experiments on downstream tasks.
3. The presentation can be improved. For example, there are instances where the figure legends contain terms that are not defined. In Figure 6 (right), “Vanilla Forgetting” is mentioned. Figure 11 uses the term “Stop Forgetting,” which I believe is intended to mean “Temporary Forgetting.”

### Questions
1. What are the limitations of temporary forgetting? Is it strictly beneficial, or did the authors find that some model abilities deteriorated? Given that evaluation wasn’t performed on downstream tasks, what synthetic experiments can be conducted to evaluate the trade-offs of temporary forgetting?
2. Suggestion: Since no evaluation was performed on downstream tasks, this paper could be improved by expanding on why studying undertrained tokens is important (beyond what is already discussed in the introduction). I am familiar with this area, so the introduction was adequate for me, but adding such a section might make this paper more broadly accessible.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a distinction between *structural* and *conditional* in-context learning, where structural ICL can generalise to novel tokens because it does not depend on token embeddings. They show that by default, structural ICL emerges and then sharply diminishes during pretraining, and they introduce a novel pretraining method based on periodically reinitialising the embedding matrix, which prevents the loss of structural ICL.

### Strengths
- The central thesis is clear
- The contributions are well-grounded in prior literature
- The distinction between structural and conditional ICL is compelling
- The experimental results support the thesis well, and are quite extensive, especially on the dynamics of structural versus conditional ICL

### Weaknesses
I feel there are two main weaknesses.

Firstly, it is not clear to me how important structural ICL actually is as an ability for models
  - The connection to glitch tokens is fair, but I don't expect these to be very common, and even when they do occur I'm not sure that preserving structural ICL is the best response - for instance, it wouldn't have fixed all the canonical solidgoldmagikarp problems, because structural ICL only preserves syntactic knowledge of glitch tokens, but fundamentally cannot give semantic knowledge of unknown tokens
  - The application to very rare tokens is likewise fair but by definition not very common, and again it is unclear to me whether in these cases there are any important capabilities which are purely syntactic

Secondly, it is not clear to me how far active/temporary forgetting impairs other abilities in models
- My intuition is that repeatedly reinitialising the embedding matrix is encouraging structural ICL by damaging other kinds of learning
- While the temporary forgetting approach might ameliorate this, it is not clear to me by how much or in what way it does this

### Questions
**Q1**

To what extent does active forgetting impair other model capabilities, if at all? What about temporary forgetting? I'd be interested to hear hypotheses, and particularly any experimental results you have. 

**Q2**

Do you believe the problem of glitch tokens will recur in future, and in such a case, do you think preservation of structural ICL would be a useful strategy?

**Q3**

Can you give an example (or ideally a few examples) of cases where models might have a hard time performing a natural task because they are incapable of performing structural ICL on a rare token? 

---

I have provisionally put down a marginal acceptance, but would be happy to revise my score upwards if these questions are appropriately addressed.

### Soundness
4

### Presentation
4

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
This paper studies the limitations and corresponding solutions for in-context learning with unseen tokens (i.e., structural ICL). Under this scenario, language models (LMs) learn the sentence structure (i.e., simple syntax structure) instead of token semantic meanings. Thus, with carefully designed forgetting strategies, the authors show that they can let LMs perform well under the structural ICL setting.

### Strengths
1.  This paper investigates an interesting research question: comparing ICL with parameter-tuning. Some explorations are helpful and provide useful insights. 
2.  Besides, the idea of combining ICL with structures is inspiring. Most previous ICL works run experiments on the sentence classification datasets, which are highly semantic-related. The discussion about sentence structures instead of prompt structures are limited.

### Weaknesses
1. Some statements about ICL explanation are not up-to-date. The authors mentioned that typical ICL algorithms do not have stable learning manner and named it as conditional ICL. However, some recent works [1,2] have shown that ICL learns the task composition: the model only learns how to compose the task based on the learned tasks from pretraining, instead of learning from scratch based on the ICL examples. Thus, some claims in paragraph 2 of the introduction should be updated.

2. Experiment settings are a bit problematic. This work is based on previous findings. However, these findings are not general across all settings. For example, Singh et al., 2023 find that ICL slowly dissipates as models are overtrained ONLY for decoder-based LMs without pretraining. In their limitation section, they also mentioned that the conclusion may not hold for pretrained LMs (e.g., Multi-BERT here) under other scenarios. I can’t list all of them, but in general, what I mean is that we should be careful about the assumptions of previous work, and cannot simply generalize and rely on previous conclusions.

    Second, since this paper uses encoder-based LMs, it may not be able to perform ICL as there is little discussion about it. Besides, ICL ability is often used for large models. Implementing experiments on Multi-BERT with probing accuracy instead of generation is not convincing to show the conclusions of this paper is useful in practice.

3. The sentence structure is learned from pretraining instead of predefined. Thus, the model may not treat sentences as human do (i.e., with linguistic structures). Even if for the simple POS triple structure it doesn’t matter, other more general or complex structures may not work.

4. The potential impact of this work may be a bit limited. The motivation of injecting novel tokens under the ICL setting is not clear to me. As aforementioned, ICL is often used for large models, where their tokenizer vocabulary is large enough and it’s not necessary to add extra new tokens (e.g., LLaMA 3-8B). While for small models that may require to extend the tokenizer (frequently), it may not perform ICL well and they are not expected to be used under this scenario.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
3
